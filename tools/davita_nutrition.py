#!/usr/bin/env python3
"""Fetch the 'Nutrients per serving' table from each DaVita source page.

Usage: python3 tools/davita_nutrition.py OUT.json
Writes one entry per DaVita recipe without nu: parsed values, portions and the
English serving size. It does not touch data/recipes.json: values are reviewed
(and the serving size translated) before they are applied.
"""
import html
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# DaVita label -> nu key. "Added Sugar" is not total sugar, so it is kept apart.
LABELS = {
    "Calories": "kcal", "Protein": "protein", "Carbohydrates": "carb", "Fat": "fat",
    "Saturated Fat": "satfat", "Cholesterol": "chol", "Sodium": "na", "Potassium": "k",
    "Phosphorus": "p", "Calcium": "ca", "Fiber": "fiber", "Added Sugar": "added_sugar",
}


def page_text(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    raw = re.sub(r"<script.*?</script>|<style.*?</style>", "", raw, flags=re.S)
    lines = (html.unescape(x).strip() for x in re.sub(r"<[^>]+>", "\n", raw).split("\n"))
    return [x for x in lines if x]


def parse(lines):
    out = {"values": {}, "unknown": []}
    try:
        i = lines.index("Nutrients per serving") + 1
    except ValueError:
        out["error"] = "no 'Nutrients per serving' block"
        return out
    while i < len(lines):
        name = lines[i]
        m = re.fullmatch(r"(\d+(?:\.\d+)?)", lines[i + 1]) if i + 1 < len(lines) else None
        if not m:
            break
        if name in LABELS:
            out["values"][LABELS[name]] = float(m.group(1)) if "." in m.group(1) else int(m.group(1))
        else:
            out["unknown"].append(name)
        i += 2
        if i < len(lines) and lines[i] in ("g", "mg", "mcg"):
            i += 1
    for key, label in (("portions", "Portions:"), ("serving", "Serving Size:")):
        if label in lines:
            out[key] = lines[lines.index(label) + 1]
    return out


def main():
    dest = Path(sys.argv[1])
    recipes = json.loads((ROOT / "data" / "recipes.json").read_text(encoding="utf-8"))
    result = []
    for i, r in enumerate(recipes):
        if r.get("nu") or "davita.com" not in r["src"][1]:
            continue
        entry = {"id": i, "t": r["t"], "sv": r["sv"], "url": r["src"][1]}
        try:
            entry.update(parse(page_text(r["src"][1])))
        except Exception as ex:  # keep going; failures are listed for review
            entry["error"] = str(ex)
        result.append(entry)
        print(f"#{i} {r['t']}: {len(entry.get('values', {}))} values {entry.get('error', '')}", file=sys.stderr)
        time.sleep(1)
    dest.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
