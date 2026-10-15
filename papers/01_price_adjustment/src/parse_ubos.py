"""OCR UBOS Construction Sector Index releases and parse the 'basic heading' input price index tables.

Legacy releases (Jan-Mar 2006 = 100) carry four tables of monthly indices for the previous and current year:
  A: cement, concrete articles, steel bars, roofing sheets, other iron & steel
  B: timber, paint, PVC/HDPE pipes, water tanks, burnt clay bricks & tiles
  C: electrical wire & cable, aggregate, lime, diesel, bitumen
  D: labour wage rates, equipment charge-out rates, CPI (rescaled), cement quantities
Rows: month label followed by 2k numbers (previous, current year pairs) or k numbers (previous year only).
Output: data/ubos_input_indices_vintages.csv (one row per release x item x month), so revisions are kept.
"""
import re
import subprocess
import sys
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
PDFS = HERE.parent / "data" / "raw" / "ubos_pdfs"
OCR = HERE.parent / "data" / "raw" / "ocr"
OUT = HERE.parent / "data" / "ubos_input_indices_vintages.csv"

TABLES = {
    "S1": (["whole sector", "buildings"], ["whole_sector", "all_buildings", "residential_total", "residential_formal",
                                          "residential_own_account"]),
    "S2": (["civil works", "roads"], ["nonresidential_buildings", "civil_works", "roads_paved", "roads_gravel",
                                     "water_projects"]),
    "A": (["cement", "concrete"], ["cement", "concrete_articles", "steel_bars", "roofing_sheets", "other_iron_steel"]),
    "B": (["timber", "paint"], ["timber", "paint", "pvc_hdpe_pipes", "water_tanks", "clay_bricks_tiles"]),
    "C": (["diesel", "bitumen", "aggregate"], ["electrical_wire_cable", "aggregate", "lime", "diesel", "bitumen"]),
    "D": (["labour", "equipment"], ["labour_wage_rates", "equipment_charge_out", "cpi_rescaled", "cement_quantities"]),
}
MONTHS = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
NUM = re.compile(r"\d{2,4}\.\d{1,2}")


def ocr(pdf):
    out = OCR / (pdf.stem + ".txt")
    if out.exists():
        return out.read_text()
    OCR.mkdir(parents=True, exist_ok=True)
    tmp = OCR / "_page"
    subprocess.run(["pdftoppm", "-r", "200", "-gray", "-png", str(pdf), str(tmp)], check=True)
    txt = []
    for p in sorted(OCR.glob("_page*.png")):
        txt.append(subprocess.run(["tesseract", str(p), "stdout", "--psm", "6"], capture_output=True, text=True).stdout)
        p.unlink()
    out.write_text("\n".join(txt))
    return out.read_text()


def parse(text, release):
    """Find every table by its year header row (two years repeated), identify it from the column names in the
    four lines above, then read the month rows below it."""
    lines = text.splitlines()
    rows = []
    for j, line in enumerate(lines):
        yrs = re.findall(r"\b(20\d\d)\b", line)
        if not (len(yrs) >= 6 and len(set(yrs)) == 2):
            continue
        years = sorted(set(int(y) for y in yrs))
        h = " ".join(lines[max(0, j - 5): j]).lower()
        table = next((k for k, (keys, _) in TABLES.items() if all(kw in h for kw in keys)), None)
        if table is None:
            continue
        items = TABLES[table][1]
        k = len(items)
        for row in lines[j + 1: j + 24]:
            if re.findall(r"\b(20\d\d)\b", row) and len(re.findall(r"\b(20\d\d)\b", row)) >= 6:
                break
            m = re.match(r"\s*([A-Za-z]{3})[a-z]*\b", row)
            if not m or m.group(1).lower() not in MONTHS:
                continue
            nums = [float(x) for x in NUM.findall(row)]
            month = MONTHS[m.group(1).lower()]
            if len(nums) == 2 * k:
                for q in range(k):
                    rows.append((release, table, items[q], years[0], month, nums[2 * q]))
                    rows.append((release, table, items[q], years[1], month, nums[2 * q + 1]))
            elif len(nums) == k:
                for q in range(k):
                    rows.append((release, table, items[q], years[0], month, nums[q]))
    return rows


def main():
    rows = []
    for pdf in sorted(PDFS.glob("*.pdf")):
        r = parse(ocr(pdf), pdf.stem)
        print(f"{pdf.stem}: {len(r)} values")
        rows += r
    df = pd.DataFrame(rows, columns=["release", "table", "item", "year", "month", "value"])
    df.to_csv(OUT, index=False)
    print("wrote", OUT, len(df))
    return 0


if __name__ == "__main__":
    sys.exit(main())
