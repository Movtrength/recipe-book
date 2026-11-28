#!/usr/bin/env python3
"""List recipes without nutrition (nu) and rank them for filling in.

Writes reports/nutrition-gaps.md (summary + prioritized lists) and
reports/nutrition-gaps.csv (one row per recipe). Re-run after editing data.

Tiers are by source domain. What each source publishes was spot-checked
on sample pages (2026-11-28), not on every page.
"""
import csv
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
R = json.loads((ROOT / "data" / "recipes.json").read_text(encoding="utf-8"))
OUT = ROOT / "reports"

# tier, label, what the source offers
TIERS = {
    "A": ("원문에 신장 핵심값", "1회분 표에 나트륨·칼륨·인까지 있음. 그대로 옮기면 된다"),
    "B": ("원문에 일부 값", "열량·탄수화물 등 일부만, 또는 칼륨·인 없음. 있는 값만 옮긴다"),
    "C": ("원문 확인 필요", "샘플을 못 봤거나 값이 있을지 불확실"),
    "D": ("원문에 값 없음", "SNS·영상·개인 기록. 채우려면 식품 성분 DB로 직접 계산(추정값 표시)"),
}
DOMAIN_TIER = {
    "davita.com": "A",
    "kidneycareuk.org": "B",          # kcal, 탄수화물, 저염/저칼륨/저인 표시만 (mg 값 없음)
    "dishingouthealth.com": "B",      # 열량·나트륨 등, 저자 계산값
    "justonecookbook.com": "B",
    "kidney.org": "C",                # 다른 224개는 값이 있었는데 이 1개만 빠짐
    "ksn.or.kr": "C",                 # PDF 책자, 텍스트로 못 읽음
    "10000recipe.com": "C",
    "instagram.com": "D", "threads.com": "D", "youtube.com": "D", "youtu.be": "D",
}
SOURCE_NOTE = {
    "davita.com": "Na·K·P·Ca·단백질 등 전체 표",
    "kidneycareuk.org": "kcal·탄수화물 + 저염/저칼륨/저인 표시",
    "dishingouthealth.com": "열량·나트륨 등 (저자 계산), 인 없음",
    "justonecookbook.com": "열량·나트륨·칼륨 등, 인 없음",
}
BLOG_DEFAULT = "C"  # other recipe blogs: often have a nutrition card, not checked


def domain(r):
    url = r["src"][1]
    return urlparse(url).netloc.removeprefix("www.") if url else ""


def tier_of(r):
    d = domain(r)
    if not d:
        return "D"
    return DOMAIN_TIER.get(d, BLOG_DEFAULT)


def main():
    rows = []
    for i, r in enumerate(R):
        if r.get("nu"):
            continue
        d = domain(r)
        rows.append({
            "id": i, "tier": tier_of(r), "kid": bool(r.get("kid")),
            "title": r["t"], "category": r["c"],
            "source": r["src"][0] or "-", "domain": d or "(URL 없음)", "url": r["src"][1],
            "offers": SOURCE_NOTE.get(d, ""),
        })
    # kidney recipes first inside each tier: kid diet needs Na/K/P most
    rows.sort(key=lambda x: (x["tier"], not x["kid"], x["domain"], x["id"]))

    OUT.mkdir(exist_ok=True)
    with open(OUT / "nutrition-gaps.csv", "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    partial = [(i, r["t"], [k for k in ("na", "k", "p") if k not in r["nu"]])
               for i, r in enumerate(R) if r.get("nu") and any(k not in r["nu"] for k in ("na", "k", "p"))]
    tc = Counter(x["tier"] for x in rows)
    tk = Counter(x["tier"] for x in rows if x["kid"])
    md = [
        "# 영양 정보 보완 대상",
        "",
        f"레시피 {len(R)}개 중 {len(rows)}개에 영양 정보(`nu`)가 없다. 값이 있는 {len(R) - len(rows)}개는 모두 kidney.org 출처다.",
        "먼저 채울 것은 **A등급 24개**(DaVita, 원문에 나트륨·칼륨·인 표가 있다)이고, 그중 콩팥 레시피부터 한다.",
        "",
        "`python3 tools/nutrition_gaps.py`로 다시 만든다. 등급은 출처 사이트별로 매겼고, 사이트마다 1~2쪽만 확인했다.",
        "",
        "| 등급 | 뜻 | 개수 | 콩팥 레시피 | 채우는 방법 |",
        "| --- | --- | ---: | ---: | --- |",
    ]
    for t, (label, how) in TIERS.items():
        md.append(f"| {t} | {label} | {tc[t]} | {tk[t]} | {how} |")
    md += ["", "| 출처 | 개수 | 등급 | 원문에 있는 값 |", "| --- | ---: | :---: | --- |"]
    for d, n in Counter(x["domain"] for x in rows).most_common():
        md.append(f"| {d} | {n} | {DOMAIN_TIER.get(d, 'D' if d == '(URL 없음)' else BLOG_DEFAULT)} | {SOURCE_NOTE.get(d, '')} |")
    if partial:
        md += ["", "값은 있지만 신장 핵심값이 빠진 레시피:", ""]
        md += [f"- #{i} {t}: {', '.join(ks)} 없음" for i, t, ks in partial]
    md += ["", "## 원칙", "",
           "- A·B는 원문 수치만 옮기고 1회 제공량(`nu.sv`)을 원문대로 적는다.",
           "- D를 계산으로 채울 때는 `nu.approx: true`로 두고 `notes`에 계산 근거(사용한 DB)를 남긴다.",
           "- 출처에 없는 값을 추정해서 A·B 레시피에 섞지 않는다."]
    for t, (label, _) in TIERS.items():
        part = [x for x in rows if x["tier"] == t]
        md += ["", f"## {t}. {label} ({len(part)}개)", "", "| # | 콩팥 | 요리 | 분류 | 출처 |", "| ---: | :---: | --- | --- | --- |"]
        for x in part:
            src = f"[{x['source']}]({x['url']})" if x["url"] else x["source"]
            md.append(f"| {x['id']} | {'●' if x['kid'] else ''} | {x['title']} | {x['category']} | {src} |")
    (OUT / "nutrition-gaps.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{len(rows)} recipes without nu -> reports/nutrition-gaps.md, .csv")
    print("tiers:", dict(sorted(tc.items())), "kid:", dict(sorted(tk.items())))


if __name__ == "__main__":
    main()
