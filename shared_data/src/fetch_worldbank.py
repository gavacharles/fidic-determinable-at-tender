"""Download World Bank project documents (PAD, ICR, ICRR) for Ugandan road and transport projects
(shared by Papers 4, 5, 10: design traffic, completion traffic, delays, costs). Uses the public WDS API."""
import json
import re
import time
from pathlib import Path

import requests

OUT = Path(__file__).resolve().parents[1] / "raw" / "worldbank"
API = "https://search.worldbank.org/api/v2/wds"
TYPES = ["Project Appraisal Document", "Implementation Completion and Results Report", "Implementation Completion Report Review"]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    meta = []
    for q in ["Uganda road", "Uganda transport sector", "Uganda highway", "Uganda North Eastern Road", "Uganda Albertine"]:
        for dt in TYPES:
            r = requests.get(API, params={"format": "json", "qterm": q, "docty_exact": dt, "count_exact": "Uganda",
                                          "rows": 50, "fl": "id,display_title,docty,docdt,pdfurl,projectid"}, timeout=120)
            docs = r.json().get("documents", {})
            for k, d in docs.items():
                if isinstance(d, dict) and d.get("pdfurl"):
                    meta.append({k2: d.get(k2) for k2 in ("id", "display_title", "docty", "docdt", "pdfurl", "projectid")})
            time.sleep(1)
    uniq = {m["pdfurl"]: m for m in meta}
    (OUT / "documents.json").write_text(json.dumps(list(uniq.values()), indent=1))
    print("documents", len(uniq), flush=True)
    for m in uniq.values():
        name = re.sub(r"[^A-Za-z0-9_.-]+", "_", f"{m['projectid']}_{m['docty']}_{m['id']}")[:120] + ".pdf"
        dest = OUT / name
        if dest.exists():
            continue
        try:
            c = requests.get(m["pdfurl"], timeout=300).content
            if c[:4] == b"%PDF":
                dest.write_bytes(c)
                print("ok", name, flush=True)
        except requests.RequestException as e:
            print("fail", name, e, flush=True)
        time.sleep(1)


if __name__ == "__main__":
    main()
