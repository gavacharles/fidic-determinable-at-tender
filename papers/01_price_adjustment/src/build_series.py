"""Build continuous UBOS input index series from all release vintages, log revisions, and measure the legacy
(2006 = 100) to modern (CIPI 2016/17 = 100) splice.

Outputs:
  data/ubos_series_legacy.csv   item x month, latest vintage, legacy base
  data/ubos_series_modern.csv   item x month, latest vintage, modern base
  results/revisions.csv         per item: share of months revised across vintages, max absolute revision (%)
  results/splice_overlap.csv    per legacy->modern item pair: overlap months, mean ratio, CV of ratio
  results/base_check.csv        parsed Mar 2017 legacy values vs base values printed in a signed contract
"""
import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from parse_ubos import MONTHS, OCR, release_month  # noqa: E402

HERE = Path(__file__).resolve().parent
DATA, RES = HERE.parent / "data", HERE.parent / "results"
RES.mkdir(exist_ok=True)

CLEAN = {"ageregate_hardcore_crushed_broken_stone": "aggregate_hardcore_crushed_broken_stone",
         "equipment": "equipment_hire_charges", "labour_charges": "labour", "eucalyptus_props_r": "eucalyptus_props"}
# legacy basic heading -> modern CIPI item: the mapping a contract administrator would have to choose
SPLICE = {"labour_wage_rates": "labour", "equipment_charge_out": "equipment_hire_charges", "cement": "cement",
          "steel_bars": "high_tensile_steel_bars", "other_iron_steel": "high_tensile_steel_bars",
          "roofing_sheets": "sheet_steel_roofing_sheets_and_similar", "diesel": "diesel", "bitumen": "bitumen_and_bitumen_primer",
          "aggregate": "aggregate_hardcore_crushed_broken_stone", "lime": "lime", "paint": "paints_and_varnishes",
          "pvc_hdpe_pipes": "plastic_pipes_and_fittings", "clay_bricks_tiles": "clay_bricks_and_tiles"}
# base values printed in Project D's Schedule of Adjustment Data (Mar 2017, UBOS)
CONTRACT_BASE = {"labour_wage_rates": 332, "equipment_charge_out": 279, "cement": 190, "steel_bars": 293,
                 "diesel": 208, "bitumen": 179}


def vintage_order():
    out = {}
    for f in OCR.glob("*.txt"):
        rm = release_month(f.read_text())
        if rm is None:
            m = re.search(r"(20\d\d)", f.stem)
            rm = (int(m.group(1)) if m else 2000, 6)
        out[f.stem] = rm[0] * 12 + rm[1]
    return out


def main():
    d = pd.read_csv(DATA / "ubos_input_indices_vintages.csv")
    d["item"] = d["item"].replace(CLEAN)
    d = d[d.item.str.len() > 3]
    vo = vintage_order()
    d["vintage"] = d.release.map(vo).fillna(0)
    d["date"] = pd.to_datetime(dict(year=d.year, month=d.month, day=1))
    d["era"] = (d.table == "M").map({True: "modern", False: "legacy"})
    d = d.drop_duplicates(["era", "item", "date", "vintage"])
    latest = d.sort_values("vintage").groupby(["era", "item", "date"]).tail(1)
    for era in ("legacy", "modern"):
        w = latest[latest.era == era].pivot(index="date", columns="item", values="value").sort_index()
        w.to_csv(DATA / f"ubos_series_{era}.csv")
        print(era, w.shape, w.index.min().date(), w.index.max().date())
    g = d.groupby(["era", "item", "date"]).value
    rev = pd.DataFrame({"n_vintages": g.size(), "range_pct": (g.max() - g.min()) / g.mean() * 100}).reset_index()
    rev = rev[rev.n_vintages > 1].groupby(["era", "item"]).agg(
        months_with_multiple_vintages=("range_pct", "size"),
        share_revised=("range_pct", lambda x: (x > 0.05).mean()),
        max_revision_pct=("range_pct", "max")).reset_index()
    rev.round(3).to_csv(RES / "revisions.csv", index=False)
    L = pd.read_csv(DATA / "ubos_series_legacy.csv", index_col=0, parse_dates=True)
    M = pd.read_csv(DATA / "ubos_series_modern.csv", index_col=0, parse_dates=True)
    rows = []
    for lo, mo in SPLICE.items():
        if lo in L and mo in M:
            r = (L[lo] / M[mo]).dropna()
            rows.append({"legacy_item": lo, "modern_item": mo, "overlap_months": len(r),
                         "first": r.index.min().date() if len(r) else None, "last": r.index.max().date() if len(r) else None,
                         "mean_ratio": r.mean(), "cv_ratio_pct": r.std() / r.mean() * 100 if len(r) > 1 else None})
    sp = pd.DataFrame(rows)
    sp.round(3).to_csv(RES / "splice_overlap.csv", index=False)
    b = pd.DataFrame([{"item": k, "contract_base_mar2017": v,
                       "parsed_mar2017": L.loc["2017-03-01", k] if ("2017-03-01" in L.index.strftime("%Y-%m-%d") and k in L) else None}
                      for k, v in CONTRACT_BASE.items()])
    b.to_csv(RES / "base_check.csv", index=False)
    pd.set_option("display.width", 200)
    print(sp.round(3).to_string(index=False))
    print(b.to_string(index=False))
    print(rev.round(2).to_string(index=False))


if __name__ == "__main__":
    main()
