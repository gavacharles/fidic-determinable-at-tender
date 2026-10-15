"""Download UBOS Construction Sector Index / CIPI press releases (PDF) listed in the CIPI tracker cache.

Files are written to ../data/raw/ubos_pdfs only when the response is a PDF (no partial files are kept).
"""
import sys
import time
import urllib.parse
from pathlib import Path

import requests

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "data" / "raw" / "ubos_pdfs"
CACHE = Path.home() / "Projects" / "cipi-tracker" / "data" / "raw" / "ocr_text"
BASE = "https://www.ubos.org/wp-content/uploads/publications/"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    names = sorted(p.stem + ".pdf" for p in CACHE.glob("*.json"))
    ok, fail = 0, []
    for n in names:
        dest = OUT / n
        if dest.exists() and dest.stat().st_size > 0:
            ok += 1
            continue
        try:
            r = requests.get(BASE + urllib.parse.quote(n), timeout=60)
            print(r.status_code, n, flush=True)
            if r.status_code == 200 and r.content[:4] == b"%PDF":
                dest.write_bytes(r.content)
                ok += 1
            else:
                fail.append((r.status_code, n))
        except requests.RequestException as e:
            fail.append((type(e).__name__, n))
        time.sleep(0.5)
    print(f"ok={ok} fail={len(fail)}")
    for f in fail:
        print("  fail", *f)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
