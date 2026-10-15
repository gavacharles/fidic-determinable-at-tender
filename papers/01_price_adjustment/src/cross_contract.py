"""Cross-contract analysis for Paper 1.

1. Weights: bidder-proposed weights (Projects C and D, by bill) vs the official UBOS CIPI civil-engineering basket
   (Annex 3 weights, CIPI 2016/17 = 100), as shares of the variable (adjustable) part.
2. Dead band and cap: hypothetical 3-year contracts with every Base Date from Jan 2016 to Jan 2023 (commencement
   3 months after the Base Date, linear progress over 36 months, index lag 2 months), run through each formula.
   Escalation that would be paid with no dead band and no cap, vs the share lost to (i) the 18-month dead band and
   (ii) a 10% cap on cumulative adjustment (as in Project B's Contract Data). Indices spliced at June 2022.
Outputs: results/weights.csv, results/deadband_cap_by_base.csv, figures/fig_weights.png, figures/fig_deadband_cap.png
"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common.style import BLUE, CAT, INK2, MUTED, RED, paper_dir, save  # noqa: E402
from contract_recompute import CONTRACTS, LEGACY, series  # noqa: E402

D = paper_dir("01_price_adjustment")
INPUTS = {"L": "Labour", "E": "Equipment", "C": "Cement", "R": "Steel", "B": "Bitumen", "F": "Fuel / diesel",
          "M": "Metal products", "O": "Other materials (aggregate, murram, concrete, pipes...)"}
# UBOS CIPI Annex 3 (Civil engineering works) weights, Feb 2026 / Sep 2025 releases
OFFICIAL = {"L": 9.5732, "E": 13.1711, "C": 3.6797, "R": 1.9412, "B": 22.4555, "F": 2.9294, "M": 0.6857 + 0.9924 + 0.1594 + 0.1992,
            "O": 14.8509 + 4.2186 + 5.4440 + 1.4732 + 1.6945 + 0.6604}


def weights_table():
    rows = []
    for code, c in CONTRACTS.items():
        for bill, w in c["bills"].items():
            var = 1 - w["a"]
            rows.append({"source": f"Project {code}: {bill}", "a": w["a"],
                         **{INPUTS[k]: w.get(k, 0) / var for k in INPUTS}})
    tot = sum(OFFICIAL.values())
    rows.append({"source": "UBOS CIPI civil engineering basket", "a": np.nan, **{INPUTS[k]: v / tot for k, v in OFFICIAL.items()}})
    return pd.DataFrame(rows).set_index("source")


def fig_weights(t):
    cols = list(INPUTS.values())
    fig, ax = plt.subplots(figsize=(10, 4.2))
    left = np.zeros(len(t))
    colors = [CAT[0], CAT[6], MUTED, CAT[4], INK2, RED[3], CAT[3], BLUE[1]]
    for c, col in zip(cols, colors):
        ax.barh(range(len(t)), t[c].values * 100, left=left, color=col, height=0.62, label=c)
        for i, v in enumerate(t[c].values):
            if v >= 0.08:
                ax.text(left[i] + v * 50, i, f"{v:.0%}", ha="center", va="center", fontsize=7, color="white")
        left += t[c].values * 100
    ax.set_yticks(range(len(t)), t.index, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xlabel("Share of the adjustable part of the formula (%)")
    ax.set_title("Bidder-proposed weights vs the official UBOS civil-engineering basket", loc="left", fontsize=9.5)
    ax.legend(fontsize=7, ncol=4, loc="upper center", bbox_to_anchor=(0.45, -0.18), frameon=False)
    ax.grid(axis="y", visible=False)
    save(fig, D["figures"], "fig_weights")
    plt.close(fig)


def deadband_cap():
    Lg = pd.read_csv(D["data"] / "ubos_series_legacy.csv", index_col=0, parse_dates=True)
    Md = pd.read_csv(D["data"] / "ubos_series_modern.csv", index_col=0, parse_dates=True)
    idx = {k: series(Lg, Md, k, "high_tensile_steel_bars", "link at Jun 2022") for k in LEGACY}
    formulas = {"D earthworks": CONTRACTS["D"]["bills"]["Earthworks & pavement layers"],
                "D structures": CONTRACTS["D"]["bills"]["Structures"],
                "C whole works": CONTRACTS["C"]["bills"]["Whole works (local currency)"]}
    rows = []
    for base in pd.date_range("2016-01-01", "2023-01-01", freq="MS"):
        start = base + pd.DateOffset(months=3)
        months = pd.date_range(start, periods=36, freq="MS")
        for name, w in formulas.items():
            pn = []
            for t in months:
                tl = t - pd.DateOffset(months=2)
                if tl not in idx["L"].index or tl > idx["L"].index.max():
                    pn = None
                    break
                pn.append(w["a"] + sum(w[k] * idx[k].get(tl, np.nan) / idx[k].get(base, np.nan) for k in LEGACY if k in w))
            if pn is None or any(np.isnan(pn)):
                continue
            adj = np.array(pn) - 1                               # per unit of work value in each month
            full = adj.mean()                                    # escalation with no dead band, no cap (share of contract)
            mask = months >= base + pd.DateOffset(months=18)
            db = (adj * mask).mean()
            cum = np.cumsum(adj * mask) / len(months)
            capped = np.minimum(cum, 0.10)[-1] if cum.max() > 0 else cum[-1]
            rows.append({"base": base, "formula": name, "escalation_no_band_no_cap": full,
                         "paid_with_dead_band": db, "paid_with_dead_band_and_cap": capped,
                         "cap_binds": bool(cum.max() > 0.10)})
    return pd.DataFrame(rows)


def fig_deadband(r):
    fig, axes = plt.subplots(1, 3, figsize=(13, 3.8), sharey=True)
    for ax, (name, g) in zip(axes, r.groupby("formula")):
        g = g.set_index("base")
        ax.plot(g.index, g.escalation_no_band_no_cap * 100, color=INK2, lw=1.6, label="Escalation (no dead band, no cap)")
        ax.plot(g.index, g.paid_with_dead_band * 100, color=CAT[0], lw=1.6, label="Paid with 18-month dead band")
        ax.plot(g.index, g.paid_with_dead_band_and_cap * 100, color=RED[3], lw=1.6, ls="--",
                label="Paid with dead band and 10% cap")
        ax.axhline(0, color=MUTED, lw=0.8)
        ax.set_title(name, fontsize=9)
        ax.set_xlabel("Base Date of a 3-year contract")
        ax.grid(axis="x", visible=False)
    axes[0].set_ylabel("Price adjustment, % of contract value")
    axes[0].legend(fontsize=7.5, loc="upper left")
    fig.suptitle("How much escalation the dead band and the cap leave unpaid, by Base Date (UBOS indices, spliced Jun 2022)",
                 x=0.06, ha="left", fontweight="bold", fontsize=10)
    save(fig, D["figures"], "fig_deadband_cap")
    plt.close(fig)


def main():
    t = weights_table()
    t.round(3).to_csv(D["results"] / "weights.csv")
    print(t.round(2).to_string())
    fig_weights(t)
    r = deadband_cap()
    r.round(4).to_csv(D["results"] / "deadband_cap_by_base.csv", index=False)
    s = r.groupby("formula").agg(
        mean_escalation=("escalation_no_band_no_cap", "mean"), mean_paid_deadband=("paid_with_dead_band", "mean"),
        share_lost_to_deadband=("escalation_no_band_no_cap", lambda x: np.nan), cap_binds_share=("cap_binds", "mean"))
    r["lost_db"] = r.escalation_no_band_no_cap - r.paid_with_dead_band
    print(r.groupby("formula")[["escalation_no_band_no_cap", "paid_with_dead_band", "paid_with_dead_band_and_cap",
                                "lost_db", "cap_binds"]].agg(["mean", "max"]).round(3).to_string())
    fig_deadband(r)


if __name__ == "__main__":
    main()
