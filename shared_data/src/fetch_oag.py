"""Download Auditor General (OAG Uganda) consolidated annual reports, FY2017/18 onward (shared by Papers 4, 9, 10).
Logic follows the author's OAG text-mining pipeline (consolidatedreports -> viewmegareport -> embedded PDF)."""
import re
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE = "https://www.oag.go.ug"
OUT = Path(__file__).resolve().parents[1] / "raw" / "oag"
H = {"User-Agent": "Mozilla/5.0"}


def get(url, **kw):
    return requests.get(url, headers=H, timeout=kw.pop("timeout", 90), **kw)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    soup = BeautifulSoup(get(f"{BASE}/consolidatedreports").text, "html.parser")
    mega = sorted({(a["href"] if a["href"].startswith("http") else BASE + a["href"])
                   for a in soup.select("a[href]") if "viewmegareport" in a["href"]})
    print("megareports", len(mega), flush=True)
    for url in mega:
        try:
            s = BeautifulSoup(get(url).text, "html.parser")
        except requests.RequestException as e:
            print("skip", url, e, flush=True)
            continue
        srcs = [t.get("src") or t.get("href") or t.get("data") for t in s.select("iframe, embed, object, a[href]")]
        for src in [x for x in srcs if x and ".pdf" in x.lower()]:
            pdf = src if src.startswith("http") else BASE + src
            name = re.sub(r"[^A-Za-z0-9_.-]+", "_", pdf.rsplit("/", 1)[-1])
            dest = OUT / name
            if dest.exists():
                continue
            try:
                r = get(pdf, timeout=600)
                if r.content[:4] == b"%PDF":
                    dest.write_bytes(r.content)
                    print("ok", name, len(r.content) // 1e6, "MB", flush=True)
            except requests.RequestException as e:
                print("fail", name, e, flush=True)
            time.sleep(1)


if __name__ == "__main__":
    main()
