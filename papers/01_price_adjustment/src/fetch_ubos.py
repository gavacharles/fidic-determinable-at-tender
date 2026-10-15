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
# 2017-2019 legacy releases not in the tracker cache (each carries the previous year's full monthly series)
EXTRA = [
    "https://www.ubos.org/wp-content/uploads/publications/CSI Press release January 2018.pdf",
    "https://www.ubos.org/wp-content/uploads/publications/CSI Press release 2017 Dec.pdf",
    "https://www.ubos.org/wp-content/uploads/publications/CSI Press release 2017 Oct-Nov final.pdf",
    "https://www.ubos.org/wp-content/uploads/publications/05_2018CSI_Press_release_2018_March.pdf",
    "https://www.ubos.org/wp-content/uploads/2018/06/CSI-Press-release-for-April-and-May-2018_20-06-2018_Final.pdf",
    "https://www.ubos.org/wp-content/uploads/publications/11_2018CSI_October_2018_Press_Release.pdf",
    "https://www.ubos.org/wp-content/uploads/publications/06_2019CSI-PRESS_RELEASE_APRIL_2019-final1.pdf",
    "https://www.ubos.org/wp-content/uploads/publications/07_2019CSI_Press_Release_MAY_AND_JUNE_2019-final.pdf",
    "https://www.ubos.org/wp-content/uploads/publications/12_2019CSI-Press-Release-Sept-And-Oct-2019.pdf",
    "https://www.ubos.org/wp-content/uploads/2019/12/CSI-November-2019-Press-release.pdf",
    "https://www.ubos.org/wp-content/uploads/2020/02/CSI-_December-2019.pdf",
]


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
    for url in EXTRA:
        dest = OUT / urllib.parse.unquote(url.rsplit("/", 1)[1]).replace(" ", "_")
        if dest.exists() and dest.stat().st_size > 0:
            ok += 1
            continue
        try:
            r = requests.get(urllib.parse.quote(url, safe=":/"), timeout=60)
            print(r.status_code, dest.name, flush=True)
            if r.status_code == 200 and r.content[:4] == b"%PDF":
                dest.write_bytes(r.content)
                ok += 1
            else:
                fail.append((r.status_code, dest.name))
        except requests.RequestException as e:
            fail.append((type(e).__name__, dest.name))
    print(f"ok={ok} fail={len(fail)}")
    for f in fail:
        print("  fail", *f)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
