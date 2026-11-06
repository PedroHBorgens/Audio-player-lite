#!/usr/bin/env python3
"""Recalcula os hashes SHA-256 dos <script> inline de index.html e atualiza a
Content-Security-Policy em index.html (meta) e em _headers.

Recomputes the SHA-256 hashes of the inline <script> blocks in index.html and
updates the Content-Security-Policy in index.html (meta tag) and _headers.

Uso / Usage:  python3 tools/update-csp.py [--check]
"""
import base64, hashlib, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
HTML, HEADERS = ROOT / "index.html", ROOT / "_headers"

def policy(hashes, extra=""):
    src = " ".join(f"'sha256-{h}'" for h in hashes)
    return ("default-src 'none'; script-src " + src + "; style-src 'unsafe-inline'; "
            "media-src blob:; img-src data: blob:; connect-src 'none'; form-action 'none'; "
            "base-uri 'none'; object-src 'none'" + extra)

html = HTML.read_text(encoding="utf-8")
scripts = re.findall(r"<script>(.*?)</script>", html, flags=re.S)
hashes = [base64.b64encode(hashlib.sha256(s.encode("utf-8")).digest()).decode() for s in scripts]

new_html = re.sub(r'(<meta http-equiv="Content-Security-Policy" content=")[^"]*(")',
                  lambda m: m.group(1) + policy(hashes) + m.group(2), html, count=1)
headers = HEADERS.read_text(encoding="utf-8")
new_headers = re.sub(r"(Content-Security-Policy: ).*",
                     lambda m: m.group(1) + policy(hashes, "; frame-ancestors 'none'"), headers, count=1)

if "--check" in sys.argv:
    ok = new_html == html and new_headers == headers
    print("CSP em dia / CSP up to date" if ok else "CSP desatualizada: rode tools/update-csp.py / CSP out of date: run tools/update-csp.py")
    sys.exit(0 if ok else 1)

HTML.write_text(new_html, encoding="utf-8")
HEADERS.write_text(new_headers, encoding="utf-8")
print(f"{len(hashes)} script(s):", *hashes, sep="\n  ")
