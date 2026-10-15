"""Recompute a signed contract's price adjustment (Project D, anonymised) under defensible index choices.

Formula per bill (Schedule of Adjustment Data, base Mar 2017, all UBOS legacy basic headings, 2006 = 100):
  Pn = a + b Ln/L0 + c En/E0 + d Cn/C0 + e Rn/R0 + f Bn/B0 + g Fn/F0 + h Mn/M0
The legacy series stop in June 2022. After that the administrator must choose
  - a splice rule to the CIPI 2016/17 = 100 series: link at the last legacy month, at the mean overlap ratio, at
    the first overlap month, or freeze the index at its last published value; and
  - a successor for 'metal products' (legacy 'other iron & steel'), which has no direct CIPI equivalent.
Indices are read 49 days before the end of the payment month, i.e. with a 2-month lag (approximation).
Outputs: results/contract_D_pn.csv, results/contract_D_spread.csv, results/dead_band.csv, figures/fig_contract_D.png
"""
import itertools
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.style import CAT, INK2, MUTED, RED, paper_dir, save  # noqa: E402

D = paper_dir("01_price_adjustment")
LAG = 2
CONTRACTS = {}
BILLS_D = {  # weights from the Schedule of Adjustment Data; amount = bidder's local-currency amount (UGX)
    "Drainage": dict(a=.2, L=.25, E=.05, C=.15, R=.15, F=.10, M=.10, amount=26.364e9),
    "Earthworks & pavement layers": dict(a=.2, L=.15, E=.25, C=.05, F=.35, amount=26.020e9),
    "Bituminous layers & seals": dict(a=.2, L=.10, E=.20, B=.30, F=.20, amount=3.126e9),
    "Ancillary road works": dict(a=.2, L=.20, C=.05, R=.10, F=.20, M=.25, amount=1.956e9),
    "Structures": dict(a=.2, L=.10, E=.10, C=.15, R=.20, F=.10, M=.15, amount=6.341e9),
}
CONTRACTS["D"] = dict(base=pd.Timestamp("2017-03-01"), bills=BILLS_D)
# Project C: single local-currency formula, base June 2019 (all seven base values equal UBOS Jun 2019 exactly;
# bitumen's 'source of material' is given as Dubai but its index as UBOS)
CONTRACTS["C"] = dict(base=pd.Timestamp("2019-06-01"),
                      bills={"Whole works (local currency)": dict(a=.2, L=.10, C=.25, B=.15, R=.10, E=.10, F=.05, M=.05,
                                                                  amount=161.826e9)})
LEGACY = {"L": "labour_wage_rates", "E": "equipment_charge_out", "C": "cement", "R": "steel_bars", "B": "bitumen",
          "F": "diesel", "M": "other_iron_steel"}
MODERN = {"L": "labour", "E": "equipment_hire_charges", "C": "cement", "R": "high_tensile_steel_bars",
          "B": "bitumen_and_bitumen_primer", "F": "diesel"}
M_SUCCESSORS = {"steel bars": "high_tensile_steel_bars", "roofing sheets": "sheet_steel_roofing_sheets_and_similar",
                "nails, bolts & screws": "nails_bolts_screws"}
SPLICES = ["link at Jun 2022", "mean overlap ratio", "link at Mar 2022", "freeze at Jun 2022"]


def series(Lg, Md, code, m_succ, splice):
    leg = Lg[LEGACY[code]].dropna()
    if splice == "freeze at Jun 2022":
        return leg.reindex(pd.date_range(leg.index.min(), "2025-12-01", freq="MS")).ffill()
    mod = Md[MODERN.get(code) or m_succ].dropna() if code != "M" else Md[m_succ].dropna()
    ov = (leg / mod).dropna()
    ratio = {"link at Jun 2022": ov.iloc[-1], "mean overlap ratio": ov.mean(), "link at Mar 2022": ov.iloc[0]}[splice]
    after = mod[mod.index > leg.index.max()] * ratio
    return pd.concat([leg, after]).sort_index()


def run(code):
    BASE, BILLS = CONTRACTS[code]["base"], CONTRACTS[code]["bills"]
    Lg = pd.read_csv(D["data"] / "ubos_series_legacy.csv", index_col=0, parse_dates=True)
    Md = pd.read_csv(D["data"] / "ubos_series_modern.csv", index_col=0, parse_dates=True)
    months = pd.date_range(BASE + pd.DateOffset(months=1), "2025-12-01", freq="MS")
    rows = []
    for (mname, msucc), splice in itertools.product(M_SUCCESSORS.items(), SPLICES):
        idx = {c: series(Lg, Md, c, msucc, splice) for c in LEGACY}
        for bill, w in BILLS.items():
            for t in months:
                tl = t - pd.DateOffset(months=LAG)
                pn = w["a"] + sum(w[c] * idx[c].get(tl, np.nan) / idx[c][BASE] for c in LEGACY if c in w)
                rows.append({"bill": bill, "metal_successor": mname, "splice": splice, "month": t, "Pn": pn})
    pn = pd.DataFrame(rows)
    pn.to_csv(D["results"] / f"contract_{code}_pn.csv", index=False)

    # spread across choices, by bill, at key dates; and money over Jul 2022 - Dec 2025 at a uniform work rate
    spread = []
    for bill, g in pn.groupby("bill"):
        for date in ("2023-06-01", "2024-12-01", "2025-12-01"):
            v = g[g.month == date].Pn
            spread.append({"bill": bill, "date": date, "Pn_min": v.min(), "Pn_max": v.max(),
                           "spread_pct_points": (v.max() - v.min()) * 100})
        post = g[(g.month >= "2022-07-01")]
        tot = post.groupby(["metal_successor", "splice"]).Pn.mean() - 1
        amt = BILLS[bill]["amount"]
        spread.append({"bill": bill, "date": "Jul 2022-Dec 2025 mean adjustment",
                       "Pn_min": tot.min() + 1, "Pn_max": tot.max() + 1, "spread_pct_points": (tot.max() - tot.min()) * 100,
                       "money_spread_ugx_bn_if_whole_bill_in_window": (tot.max() - tot.min()) * amt / 1e9})
    sp = pd.DataFrame(spread)
    sp.round(4).to_csv(D["results"] / f"contract_{code}_spread.csv", index=False)

    # dead band: escalation (Pn - 1) during the first 18 months after the Base Date, when no adjustment is paid
    base_case = pn[(pn.metal_successor == "steel bars") & (pn.splice == "link at Jun 2022")]  # dead band before splice
    db = base_case[base_case.month <= BASE + pd.DateOffset(months=18)].groupby("bill").Pn.agg(["mean", "max"]) - 1
    db.columns = ["mean_escalation_unpaid", "max_escalation_unpaid"]
    db.round(4).to_csv(D["results"] / f"dead_band_{code}.csv")
    pd.set_option("display.width", 200)
    print(sp.round(3).to_string(index=False))
    print(db.round(4))

    show = [b for b in ["Earthworks & pavement layers", "Structures"] if b in BILLS] or list(BILLS)
    fig, axes = plt.subplots(1, len(show), figsize=(max(8, 6 * len(show)), 4), sharey=True, squeeze=False)
    axes = axes[0]
    for ax, bill in zip(axes, show):
        g = pn[pn.bill == bill]
        for i, ((m, s), gg) in enumerate(g.groupby(["metal_successor", "splice"])):
            gg = gg.set_index("month").Pn
            ax.plot(gg.index, gg.values, lw=1, color=MUTED, alpha=0.6, label="Each defensible choice" if i == 0 else None)
        env = g.groupby("month").Pn.agg(["min", "max"])
        ax.fill_between(env.index, env["min"], env["max"], color=RED[1], alpha=0.5, lw=0, label="Range across choices")
        ax.axvspan(BASE, BASE + pd.DateOffset(months=18), color=CAT[3], alpha=0.12, lw=0, label="No adjustment (first 18 months)")
        ax.axvline(pd.Timestamp("2022-06-01"), color=INK2, ls="--", lw=1)
        ax.text(pd.Timestamp("2022-07-01"), 0.98, "legacy index ends Jun 2022", transform=ax.get_xaxis_transform(),
                fontsize=7.5, color=INK2, va="top")
        ax.axhline(1, color=INK2, lw=0.8)
        ax.set_title(bill, fontsize=9)
        ax.set_ylabel("Price adjustment multiplier Pn")
        ax.grid(axis="x", visible=False)
    axes[0].legend(fontsize=7.5, loc="upper left")
    fig.suptitle(f"Project {code} price adjustment: the same contract under defensible splice and successor-index choices",
                 x=0.06, ha="left", fontweight="bold", fontsize=10)
    save(fig, D["figures"], f"fig_contract_{code}")
    return sp


def main():
    for code in CONTRACTS:
        run(code)


if __name__ == "__main__":
    main()
