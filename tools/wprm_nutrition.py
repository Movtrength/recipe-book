#!/usr/bin/env python3
"""Fetch the WP Recipe Maker nutrition label from recipe blogs.

Usage: python3 tools/wprm_nutrition.py OUT.json DOMAIN [DOMAIN ...]
Reads every recipe without nu whose source is on DOMAIN, parses the
'wprm-nutrition-label-text-nutrition-container-*' blocks and the recipe's
servings, and writes them for review. data/recipes.json is not touched.
"""
import html
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KEYS = {"calories": "kcal", "carbohydrates": "carb", "protein": "protein", "fat": "fat",
        "saturated_fat": "satfat", "cholesterol": "chol", "sodium": "na", "potassium": "k",
        "phosphorus": "p", "calcium": "ca", "fiber": "fiber", "sugar": "sugar"}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh)"})
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")


def text(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def parse(raw):
    out = {"values": {}, "units": {}}
    for m in re.finditer(r'wprm-nutrition-label-text-nutrition-container-([a-z_]+)', raw):
        key = m.group(1)
        chunk = raw[m.end(): m.end() + 1500].split("wprm-nutrition-label-text-nutrition-container-")[0]
        val = re.search(r'wprm-nutrition-label-text-nutrition-value[^>]*>([^<]*)<', chunk)
        unit = re.search(r'wprm-nutrition-label-text-nutrition-unit[^>]*>([^<]*)<', chunk)
        if not val or key in out["units"]:
            continue
        v = val.group(1).strip()
        if key == "serving_size":
            out["serving_size"] = (v + " " + (unit.group(1).strip() if unit else "")).strip()
        elif key in KEYS and re.fullmatch(r"\d+(?:\.\d+)?", v):
            out["values"][KEYS[key]] = float(v) if "." in v else int(v)
            out["units"][KEYS[key]] = unit.group(1).strip() if unit else ""
    sv = re.search(r'class="wprm-recipe-servings [^"]*"[^>]*>(\d+)<', raw)
    out["servings"] = int(sv.group(1)) if sv else None
    unit_txt = re.search(r'wprm-recipe-servings-unit[^>]*>([^<]*)<', raw)
    out["servings_unit"] = unit_txt.group(1).strip() if unit_txt else ""
    return out


def main():
    dest, domains = Path(sys.argv[1]), sys.argv[2:]
    recipes = json.loads((ROOT / "data" / "recipes.json").read_text(encoding="utf-8"))
    result = []
    for i, r in enumerate(recipes):
        if r.get("nu") or not any(d in r["src"][1] for d in domains):
            continue
        e = {"id": i, "t": r["t"], "sv": r["sv"], "url": r["src"][1]}
        try:
            e.update(parse(fetch(r["src"][1])))
        except Exception as ex:
            e["error"] = f"{type(ex).__name__}: {ex}"[:160]
        result.append(e)
        flag = "" if e.get("servings") == r["sv"] else f" SERVINGS {e.get('servings')} vs sv {r['sv']}"
        print(f"#{i} {r['t']}: {sorted(e.get('values', {}))}{flag} {e.get('error', '')}", file=sys.stderr)
        time.sleep(0.7)
    dest.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
