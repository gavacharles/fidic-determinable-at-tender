"""Parse subgrade test-pit results (chainage, Atterberg limits, AASHTO class, MDD, OMC, soaked CBR) from the text of a
soil and materials investigation report (Project A, Masindi-Biiso; the text file is kept outside the repository).
Usage: python parse_testpits.py <report.txt>   Output: data/raw/testpits_A_lot3.csv (not committed)
"""
import re
import sys
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parents[1] / "data" / "raw" / "testpits_A_lot3.csv"
CH = re.compile(r"(\d{1,2})\+(\d{3})")
ROW = re.compile(r"Subgrade\s+[\d.]+-[\d.]+\s+(.*)$")


def main(path):
    lines = Path(path).read_text().splitlines()
    i0 = next(i for i, l in enumerate(lines) if "Summary of Laboratory Test Results for Subgrade Materials" in l and "Table 1-12" in l
              and not l.strip().endswith("..."))
    rows, pending = [], None
    for l in lines[i0:i0 + 400]:
        if "Table 1-13" in l:
            break
        ch = CH.search(l)
        if ch and "Subgrade" not in l:
            pending = int(ch.group(1)) + int(ch.group(2)) / 1000
            continue
        m = ROW.search(l)
        if not m:
            continue
        km = int(ch.group(1)) + int(ch.group(2)) / 1000 if ch else pending
        toks = m.group(1).split()
        aashto = next((t for t in toks if re.match(r"A-\d", t)), None)
        if aashto is None or km is None:
            continue
        k = toks.index(aashto)
        num = lambda t: float(t) if re.match(r"^-?\d+(\.\d+)?$", t) else None  # noqa: E731
        before, after = [num(t) for t in toks[:k]], [num(t) for t in toks[k + 1:]]
        # before: 8 grading values, GM, LL, PL, PI, LS, PM ; after: MDD, OMC, CBR90, CBR93, CBR95, NMC
        if len(before) < 14 or len(after) < 5:
            continue
        rows.append({"chainage_km": km, "LL": before[9], "PL": before[10], "PI": before[11], "PM": before[13],
                     "aashto": aashto, "MDD": after[0], "OMC": after[1], "CBR90": after[2], "CBR93": after[3],
                     "CBR95": after[4], "p075": before[7]})
        pending = None
    df = pd.DataFrame(rows).drop_duplicates("chainage_km").sort_values("chainage_km")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False)
    print(len(df), "test pits;", df.chainage_km.min(), "-", df.chainage_km.max(), "km")
    print(df.describe().round(1).T[["mean", "min", "max"]])
    print(df.aashto.value_counts().to_dict())


if __name__ == "__main__":
    main(sys.argv[1])
