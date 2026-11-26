#!/usr/bin/env python3
"""Validate data/recipes.json and inline it into src/template.html -> index.html.

Usage:
  python3 build.py            # validate + build index.html
  python3 build.py --check    # validate only (exit 1 on errors)

Standard library only. No network, no dependencies.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "recipes.json"
TEMPLATE = ROOT / "src" / "template.html"
OUT = ROOT / "index.html"
PLACEHOLDER = "/*@@RECIPES@@*/[]"

CATEGORIES = ["아침", "밥", "면", "국", "메인", "반찬", "샐러드", "소스", "간식", "디저트", "음료", "기타"]
NUTRI_KEYS = {"kcal", "carb", "protein", "fat", "satfat", "chol", "na", "k", "p", "ca", "fiber", "sugar", "sv", "approx"}
STR_LISTS = ["tags", "al", "mise", "cau", "done", "notes"]


def is_num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def validate(recipes, warns):
    errs = []
    if not isinstance(recipes, list):
        return ["root must be a JSON array"]
    seen = {}
    for i, r in enumerate(recipes):
        where = f"#{i} {r.get('t', '?') if isinstance(r, dict) else '?'}"
        e = lambda msg: errs.append(f"{where}: {msg}")
        if not isinstance(r, dict):
            e("recipe must be an object"); continue
        if not isinstance(r.get("t"), str) or not r["t"].strip():
            e("t (title) is required")
        elif r["t"] in seen:
            warns.append(f"{where}: same title as #{seen[r['t']]} (allowed; add a source hint to t if confusing)")
        else:
            seen[r["t"]] = i
        if r.get("c") not in CATEGORIES:
            e(f"c must be one of {CATEGORIES}")
        for k in ("sv", "min"):
            if r.get(k) is not None and not (isinstance(r[k], int) and r[k] > 0):
                e(f"{k} must be a positive integer or null")
        for k in ("heat", "cu"):
            if not isinstance(r.get(k), str):
                e(f"{k} must be a string (may be empty)")
        for k in ("en", "yl"):
            if k in r and not isinstance(r[k], str):
                e(f"{k} must be a string")
        if "kid" in r and not isinstance(r["kid"], bool):
            e("kid must be true/false")
        for k in STR_LISTS:
            v = r.get(k)
            if not isinstance(v, list) or not all(isinstance(s, str) for s in v):
                e(f"{k} must be a list of strings")
        ing = r.get("ing")
        if not isinstance(ing, list) or not ing:
            e("ing must be a non-empty list")
        else:
            for j, x in enumerate(ing):
                if not (isinstance(x, list) and len(x) == 4 and all(isinstance(s, str) for s in x)):
                    e(f"ing[{j}] must be [name, amount, unit, note] (all strings)")
        subs = r.get("subs")
        if not isinstance(subs, list) or not all(isinstance(x, list) and len(x) == 3 and all(isinstance(s, str) for s in x) for x in subs):
            e("subs must be a list of [from, to, memo] strings")
        st = r.get("st")
        if not isinstance(st, list) or not st:
            e("st must be a non-empty list")
        else:
            for j, x in enumerate(st):
                # [text] = no timer; [text, minMin, maxMin, alertText] = timer step.
                ok = isinstance(x, list) and x and isinstance(x[0], str)
                if ok and len(x) != 1:
                    ok = len(x) == 4 and is_num(x[1]) and is_num(x[2]) and 0 < x[1] <= x[2] and isinstance(x[3], str)
                if not ok:
                    e(f"st[{j}] must be [text] or [text, minMin, maxMin, alertText] with 0<min<=max")
        src = r.get("src")
        if not (isinstance(src, list) and len(src) == 2 and all(isinstance(s, str) for s in src)):
            e("src must be [label, url]")
        nu = r.get("nu")
        if nu is not None:
            if not isinstance(nu, dict):
                e("nu must be an object or null")
            else:
                for k, v in nu.items():
                    if k not in NUTRI_KEYS:
                        e(f"nu.{k} is not a known key {sorted(NUTRI_KEYS)}")
                    elif k == "sv" and not isinstance(v, str):
                        e("nu.sv must be a string")
                    elif k == "approx" and not isinstance(v, bool):
                        e("nu.approx must be true/false")
                    elif k not in ("sv", "approx") and not is_num(v):
                        e(f"nu.{k} must be a number")
    return errs


def main():
    check_only = "--check" in sys.argv
    try:
        recipes = json.loads(DATA.read_text(encoding="utf-8"))
    except json.JSONDecodeError as ex:
        print(f"recipes.json is not valid JSON: {ex}", file=sys.stderr)
        return 1
    warns = []
    errs = validate(recipes, warns)
    for m in warns:
        print("warning: " + m, file=sys.stderr)
    if errs:
        print(f"{len(errs)} error(s):", file=sys.stderr)
        for m in errs:
            print("  " + m, file=sys.stderr)
        return 1
    print(f"ok: {len(recipes)} recipes")
    if check_only:
        return 0
    tpl = TEMPLATE.read_text(encoding="utf-8")
    if tpl.count(PLACEHOLDER) != 1:
        print(f"template must contain {PLACEHOLDER} exactly once", file=sys.stderr)
        return 1
    # "</" escaped so recipe text can never close the <script> tag.
    payload = json.dumps(recipes, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    OUT.write_text(tpl.replace(PLACEHOLDER, payload), encoding="utf-8")
    print(f"built {OUT.relative_to(ROOT)} ({OUT.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
