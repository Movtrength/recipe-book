#!/usr/bin/env python3
"""Open source pages and report which nutrition values each one publishes.

Usage: python3 tools/probe_nutrition.py OUT.json [tier]   (default tier C)
Looks at schema.org Recipe JSON-LD 'nutrition', the WP Recipe Maker
nutrition block, and 'Sodium 123 mg'-style text. Read-only: data is not changed.
"""
import html
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import nutrition_gaps as ng  # noqa: E402

# what we look for -> (JSON-LD field, text label regex)
FIELDS = {
    "kcal": ("calories", r"calories|kcal|열량|칼로리"),
    "na": ("sodiumContent", r"sodium|나트륨"),
    "k": (None, r"potassium|칼륨"),
    "p": (None, r"phosphorus|인\b"),
    "protein": ("proteinContent", r"protein|단백질"),
    "carb": ("carbohydrateContent", r"carbohydrates?|탄수화물"),
}
NUM = r"[:\s]*([\d.,]+)\s*(?:mg|g|kcal|칼로리)?"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh)"})
    with urllib.request.urlopen(req, timeout=30) as res:
        ctype = res.headers.get("Content-Type", "")
        body = res.read(8_000_000)
    return ctype, body


def jsonld_nutrition(raw):
    found = {}
    for block in re.findall(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', raw, flags=re.S):
        try:
            data = json.loads(block)
        except ValueError:
            continue
        stack = [data]
        while stack:
            x = stack.pop()
            if isinstance(x, dict):
                if isinstance(x.get("nutrition"), dict):
                    found.update({k: v for k, v in x["nutrition"].items() if not k.startswith("@")})
                stack.extend(x.values())
            elif isinstance(x, list):
                stack.extend(x)
    return found


def probe(url):
    ctype, body = fetch(url)
    if "pdf" in ctype or url.lower().endswith(".pdf"):
        return {"kind": "pdf", "have": [], "note": "PDF 책자 — 텍스트 추출 필요"}
    raw = body.decode("utf-8", "replace")
    ld = jsonld_nutrition(raw)
    text = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", " ", raw, flags=re.S)))
    text = re.sub(r"\s+", " ", text)
    wprm = "wprm-nutrition" in raw
    have = []
    for key, (ldkey, label) in FIELDS.items():
        if ldkey and ld.get(ldkey):
            have.append(key)
        elif re.search(rf"(?i)(?:{label}){NUM}", text) and re.search(rf"(?i)(?:{label})[:\s]*\d", text):
            have.append(key)
    return {"kind": "html", "have": have, "jsonld": bool(ld), "wprm": wprm,
            "sample": {k: v for k, v in ld.items() if k in ("calories", "sodiumContent", "servingSize")}}


def regrade(have):
    if {"na", "k", "p"} <= set(have):
        return "A"
    if have:
        return "B"
    return "D"


def main():
    dest = Path(sys.argv[1])
    tier = sys.argv[2] if len(sys.argv) > 2 else "C"
    out = []
    for i, r in enumerate(ng.R):
        if r.get("nu") or ng.tier_of(r) != tier:
            continue
        e = {"id": i, "t": r["t"], "domain": ng.domain(r), "url": r["src"][1]}
        try:
            e.update(probe(r["src"][1]))
            e["new_tier"] = "C" if e["kind"] == "pdf" else regrade(e["have"])
        except Exception as ex:
            e.update({"error": f"{type(ex).__name__}: {ex}"[:160], "new_tier": "C"})
        out.append(e)
        print(f"#{i} {e['domain']}: {e.get('have')} -> {e['new_tier']} {e.get('error', '')}", file=sys.stderr)
        time.sleep(0.7)
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
