#!/usr/bin/env python3
"""Move amounts written inside ingredient names into the amount/unit fields.

Usage: python3 tools/split_amounts.py ID [ID ...] [--apply]
'닭가슴살 200g' -> ['닭가슴살', '200', 'g'], '말린 오레가노 1작은술(선택)' ->
['말린 오레가노', '1', '작은술', '선택']. Only ingredients whose amount field is
empty and whose name holds exactly one number+unit are changed; anything
ambiguous ('작은 양파 2개 또는 큰 양파 1개') stays as it is. Without --apply it
prints the changes.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UNITS = r"kg|g|ml|mL|L|큰술|작은술|컵|개|쪽|송이|대|장|줄기|캔|병|봉지|팩|덩이|조각|줌|알|마리|토막|모"
FRAC = {"½": "0.5", "¼": "0.25", "¾": "0.75", "⅓": "0.33", "⅔": "0.67"}
NUM = r"\d+(?:\.\d+)?(?:/\d+)?|[½¼¾⅓⅔]|\d+[½¼¾]"
PAT = re.compile(rf"^(?P<name>.*?)\s*(?:약\s*)?(?P<amt>(?:{NUM})(?:\s*[~\-–]\s*(?:{NUM}))?)\s*(?P<unit>{UNITS})(?P<rest>(?:\s*\(.*?\))?(?:\s*〔.*〕)?)\s*$")


def norm(a):
    a = a.replace("~", "-").replace("–", "-").replace(" ", "")
    for k, v in FRAC.items():
        a = re.sub(rf"(\d+){k}", lambda m: str(int(m.group(1)) + float(v)), a)
        a = a.replace(k, v)
    if re.fullmatch(r"\d+/\d+", a):
        n, d = a.split("/")
        a = str(round(int(n) / int(d), 2))
    return a


def split(name):
    outside = re.sub(r"\(.*?\)|〔.*?〕", "", name)
    # one amount outside brackets; '닭가슴살 또는 닭다리살 320g' is fine, '양파 2개 또는 1개' is not
    if len(re.findall(rf"(?:{NUM})\s*(?:{UNITS})", outside)) != 1:
        return None
    m = PAT.match(name)
    if not m or not m.group("name").strip():
        return None
    unit = m.group("unit")
    if unit in ("병", "캔"):  # '피망 480g 병' keeps the container in the name
        return None
    if re.search(r"\d", m.group("name")):  # '생강 5cm 또는 ... 1작은술': another amount stays behind
        return None
    parts = re.findall(r"\((.*?)\)|(〔.*?〕)", m.group("rest"))
    note = "; ".join(a or b for a, b in parts)
    return m.group("name").strip(), norm(m.group("amt")), unit, note


def main():
    ids = [int(x) for x in sys.argv[1:] if x.isdigit()]
    apply = "--apply" in sys.argv
    p = ROOT / "data" / "recipes.json"
    lines = p.read_text(encoding="utf-8").split("\n")
    total = changed = 0
    for i in ids:
        r = json.loads(lines[i + 1].rstrip(","))
        for x in r["ing"]:
            if x[1]:
                continue
            total += 1
            s = split(x[0])
            if not s:
                print(f"  keep #{i} {x[0]}")
                continue
            nm, amt, unit, note = s
            if not apply:
                print(f"  #{i} {x[0]!r} -> {[nm, amt, unit, note]}")
            x[0], x[1], x[2] = nm, amt, unit
            x[3] = "; ".join(t for t in (note, x[3]) if t)
            changed += 1
        lines[i + 1] = json.dumps(r, ensure_ascii=False) + ("," if lines[i + 1].endswith(",") else "")
    print(f"{changed}/{total} split")
    if apply:
        p.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
