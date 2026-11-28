#!/usr/bin/env python3
"""Estimate per-serving nutrition from ingredient weights (recipes whose source has none).

Usage: python3 tools/estimate_nutrition.py FCT.csv [--apply]
  FCT.csv  MFDS 전국통합식품영양성분정보(원재료성식품) 표준데이터 CSV (cp949), from
           https://www.data.go.kr/data/15100065/standard.do
  --apply  write nu (approx: true, calc: basis) into data/recipes.json

Every ingredient -> one food entry and a weight in grams; the volume conversions
are the assumptions listed in VOLUME. Items missing from the Korean raw-food DB
(brewed soy sauce, vinegars) use USDA FoodData Central SR Legacy values per 100 g.
"""
import csv
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TSP, TBSP = 5, 15  # mL
VOLUME = {"oil": 0.92, "soy": 1.15, "balsamic": 1.06, "vinegar": 1.01}  # g/mL
SUGAR_TSP, SUGAR_TBSP, SALT_TSP = 4.2, 12.5, 6.0  # g

# USDA FDC SR Legacy, per 100 g (kcal from kJ where FDC reports kJ)
USDA = {
    "usda:174277 soy sauce (shoyu)": {"kcal": 53, "carb": 4.93, "protein": 8.14, "fat": 0.57, "na": 5490, "k": 435, "p": 166, "ca": 33, "fiber": 0.8, "sugar": 0.4},
    "usda:172241 balsamic vinegar": {"kcal": 88, "carb": 17.0, "protein": 0.49, "fat": 0, "na": 23, "k": 112, "p": 19, "ca": 27, "sugar": 14.95},
    "usda:172237 distilled vinegar": {"kcal": 18, "carb": 0.04, "protein": 0, "fat": 0, "na": 2, "k": 2, "p": 4, "ca": 6},
    # MFDS dried kelp entries have energy but no minerals; generic dried seaweed (FNDDS) fills those.
    "usda:2709988 seaweed, dried": {"na": 575, "k": 1244, "p": 85, "ca": 372},
}
KELP = "다시마류_참다시마_전체_말린것_해남_7월"
RICE = "avg:멥쌀_*_백미_생것"

# recipe id -> (servings divisor note, [(DB food, grams, divisor)])
# divisor = how many servings that batch makes, so one serving gets grams/divisor.
RECIPES = {
    109: ("1인분(3인분 기준)", [
        (RICE, 270, 3), ("우엉_생것", 45, 3), ("느타리버섯_참타리버섯_생것", 45, 3), ("당근_뿌리_생것", 45, 3),
        (KELP, 1.5, 3), ("usda:2709988 seaweed, dried", 1.5, 3), ("포도씨유", 3 * TBSP * VOLUME["oil"], 3),
        ("usda:174277 soy sauce (shoyu)", 1 * TSP * VOLUME["soy"], 3)]),
    110: ("1인분(샐러드 3인량의 1/3 + 소스 5인분의 1/5)", [
        ("닭고기_가슴(껍질 제거)_생것", 120, 3), ("상추_완전결구상추(양상추)_청상추_생것", 60, 3),
        ("치커리_잎_생것", 30, 3), ("오이_개량종_생것", 90, 3),
        ("파프리카(착색단고추)_노란색_생것", 15, 3), ("파프리카(착색단고추)_빨간색_생것", 15, 3),
        ("올리브유", 3 * TSP * VOLUME["oil"], 3), ("가지_생것", 90, 3),
        ("usda:172241 balsamic vinegar", 5 * TBSP * VOLUME["balsamic"], 5), ("올리브유", 1 * TBSP * VOLUME["oil"], 5),
        ("usda:174277 soy sauce (shoyu)", 1 * TSP * VOLUME["soy"], 5), ("설탕_백설탕", 2 * SUGAR_TSP, 5),
        ("양파_생것", 5, 5), ("마늘_구근_생것", 10, 5)]),
    111: ("1인분(5인분 기준, 절임물까지 다 먹는다고 가정)", [
        ("오이_개량종_생것", 250, 5), ("생강_뿌리줄기_생것", 5, 5), ("참기름", 0.5 * TBSP * VOLUME["oil"], 5),
        ("usda:172237 distilled vinegar", 70 * VOLUME["vinegar"], 5), ("설탕_백설탕", 2.5 * SUGAR_TBSP, 5),
        ("소금", 0.5 * SALT_TSP, 5), ("콩기름", 5 * TBSP * VOLUME["oil"], 5)]),
}
NOTES = {
    109: "물은 0으로 봤고 간장은 진간장(양조) 값을 썼다. 다시마도 먹는 것으로 계산했는데, 식약처 건다시마 항목에 무기질 값이 없어 나트륨·칼륨·인·칼슘은 USDA 일반 건조 해조류 값을 썼다(다시마는 칼륨이 이보다 높을 수 있다).",
    110: "후춧가루(약간)는 뺐다. 발사믹식초 밀도 1.06g/mL로 계산했다.",
    111: "절임물을 다 먹지는 않으므로 나트륨·당류·열량은 실제보다 높게 잡힌 상한값이다. 고추기름은 콩기름 값으로 대신했다.",
}
COLS = {"kcal": "에너지(kcal)", "carb": "탄수화물(g)", "sugar": "당류(g)", "fiber": "식이섬유(g)", "protein": "단백질(g)",
        "fat": "지방(g)", "satfat": "포화지방산(g)", "na": "나트륨(mg)", "k": "칼륨(mg)", "ca": "칼슘(mg)", "p": "인(mg)"}
CORE = ["kcal", "carb", "protein", "fat", "na", "k", "p", "ca"]


def load_fct(path):
    rows = list(csv.DictReader(io.StringIO(Path(path).read_bytes().decode("cp949"))))
    by = {}
    for r in rows:
        vals = {k: float(r[c]) for k, c in COLS.items() if r.get(c, "").strip() not in ("", "-")}
        by.setdefault(r["식품명"], vals)
    rice = [v for n, v in by.items() if re.fullmatch(r"멥쌀_[^_]+_백미_생것", n)]
    by[RICE] = {k: sum(v[k] for v in rice if k in v) / sum(1 for v in rice if k in v)
                for k in COLS if any(k in v for v in rice)}
    by.update(USDA)
    return by, len(rice), rows[0].get("데이터기준일자", "")


def estimate(db, items):
    total, gaps = {k: 0.0 for k in COLS}, []
    for food, grams, div in items:
        v = db[food]  # KeyError = mapping typo, fail loudly
        for k in COLS:
            if food == KELP and k in ("na", "k", "p", "ca"):
                continue  # supplied by the FNDDS seaweed row
            if k in v:
                total[k] += v[k] * grams / 100 / div
            elif k in CORE:
                gaps.append(f"{food}:{k}")
    return total, gaps


def rounded(total):
    out = {}
    for k in ["kcal", "carb", "sugar", "fiber", "protein", "fat", "satfat", "na", "k", "ca", "p"]:
        x = total[k]
        out[k] = round(x) if k in ("kcal", "na", "k", "ca", "p") else round(x, 1)
    return out


def main():
    db, nrice, asof = load_fct(sys.argv[1])
    apply = "--apply" in sys.argv
    p = ROOT / "data" / "recipes.json"
    lines = p.read_text(encoding="utf-8").split("\n")
    for rid, (sv, items) in RECIPES.items():
        total, gaps = estimate(db, items)
        nu = rounded(total)
        r = json.loads(lines[rid + 1].rstrip(","))
        print(f"#{rid} {r['t']}: {nu}  gaps={gaps}")
        if not apply:
            continue
        assert not r.get("nu"), f"#{rid} already has nu"
        nu.update({"sv": sv, "approx": True,
                   "calc": f"재료량 × 식약처 원재료성식품 DB({asof})·USDA FDC"})
        r["nu"] = nu
        r["notes"].append(
            f"영양 정보는 원문에 없어 계산한 추정값이다. 식약처 전국통합식품영양성분정보(원재료성식품, {asof} 기준, 쌀은 백미 {nrice}품종 평균)와 "
            f"USDA FoodData Central(진간장·식초류·해조류 무기질)을 썼고, 1큰술 15mL·1작은술 5mL, 기름 0.92g/mL·간장 1.15g/mL로 환산했다. {NOTES[rid]}")
        comma = "," if lines[rid + 1].endswith(",") else ""
        lines[rid + 1] = json.dumps(r, ensure_ascii=False) + comma
    if apply:
        p.write_text("\n".join(lines), encoding="utf-8")
        print("applied")


if __name__ == "__main__":
    main()
