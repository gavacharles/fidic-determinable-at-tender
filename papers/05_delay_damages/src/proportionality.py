"""Is 0.05% of the Contract Price per day proportionate? The daily public loss from late completion of Ugandan roads,
inferred from World Bank appraisal and completion economic returns.

A day of late completion defers the road's benefit stream by one day; with costs sunk, the loss is approximately
the first-year benefit / 365 (the shift of the end-of-life benefits is negligible after discounting). The first-year
benefit-cost ratio (FYRR) is recovered from each reported EIRR with a standard appraisal profile: cost spread evenly
over a 3-year construction period, benefits from opening for 20 years growing at g (5% base; 3% and 7% sensitivity),
no residual value. Daily loss rate = FYRR / 365, as a share of project cost, plus the Employer's own prolongation
cost (supervision consultancy, ~6% of works cost over a 3-year contract).
The uniform Contract Data rate (Projects A-E: 0.05%/day, cap 10%) corresponds to FYRR = 18.25%.
Outputs: results/daily_loss.csv, figures/fig_proportionality.png
"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import brentq

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.style import CAT, INK2, MUTED, paper_dir, save  # noqa: E402

D = paper_dir("05_delay_damages")
RATE = 0.0005           # Contract Data delay damages per day, share of Contract Price
CAP = 0.10
BUILD, LIFE = 3, 20
SUPERVISION = 0.06 / (3 * 365)   # Employer's supervision cost per day of prolongation, share of works cost


def npv(fyrr, r, g):
    cost = sum((1 / BUILD) / (1 + r) ** t for t in range(BUILD))
    ben = sum(fyrr * (1 + g) ** k / (1 + r) ** (BUILD + k) for k in range(LIFE))
    return ben - cost


def fyrr_from_eirr(eirr, g):
    return brentq(lambda f: npv(f, eirr, g), 1e-4, 5)


def eirr_from_fyrr(f, g):
    return brentq(lambda r: npv(f, r, g), 1e-4, 3)


def main():
    e = pd.read_csv(D["data"] / "eirr_roads.csv")
    for g in (0.03, 0.05, 0.07):
        e[f"fyrr_g{int(g * 100)}"] = [fyrr_from_eirr(x / 100, g) for x in e.eirr_pct]
    e["daily_loss_pct"] = (e.fyrr_g5 / 365 + SUPERVISION) * 100
    e["daily_loss_lo"] = (e.fyrr_g7 / 365 + SUPERVISION) * 100
    e["daily_loss_hi"] = (e.fyrr_g3 / 365 + SUPERVISION) * 100
    e["ratio_rate_to_loss"] = RATE * 100 / e.daily_loss_pct
    e["days_to_cap"] = CAP / RATE
    e["loss_at_cap_pct"] = e.daily_loss_pct * CAP / RATE        # public loss over the 200 days the cap allows
    e.round(4).to_csv(D["results"] / "daily_loss.csv", index=False)
    pd.set_option("display.width", 200)
    print(e[["road", "stage", "eirr_pct", "fyrr_g5", "daily_loss_pct", "ratio_rate_to_loss"]].round(3).to_string(index=False))
    be = {g: eirr_from_fyrr(RATE * 365 - SUPERVISION * 365, g) for g in (0.03, 0.05, 0.07)}
    print("EIRR at which 0.05%/day equals the daily loss:", {k: round(v * 100, 1) for k, v in be.items()})
    print("share of cases where 0.05% < loss:", round((e.daily_loss_pct > RATE * 100).mean(), 2))

    fig, ax = plt.subplots(1, 2, figsize=(12, 4.8), gridspec_kw={"width_ratios": [1.25, 1]})
    e = e.sort_values("daily_loss_pct").reset_index(drop=True)
    colors = {"rural trunk": CAT[0], "peri-urban trunk": CAT[3], "urban": CAT[2]}
    y = np.arange(len(e))
    for s, c in colors.items():
        m = e.setting == s
        ax[0].errorbar(e.daily_loss_pct[m], y[m], xerr=[e.daily_loss_pct[m] - e.daily_loss_lo[m],
                                                        e.daily_loss_hi[m] - e.daily_loss_pct[m]],
                       fmt="none", ecolor=c, elinewidth=1, capsize=2)
        ax[0].scatter(e.daily_loss_pct[m], y[m], color=c, s=28, zorder=3, label=s)
    hollow = e.stage == "completion"
    ax[0].scatter(e.daily_loss_pct[hollow], y[hollow], facecolor="white", edgecolor=INK2, s=10, zorder=4,
                  label="(white centre = at completion)")
    ax[0].axvline(RATE * 100, color=INK2, ls="--", lw=1.2, label="Contract Data rate 0.05%/day")
    ax[0].set_yticks(y, [f"{r} ({s[:4]}.)" for r, s in zip(e.road, e.stage)], fontsize=7)
    ax[0].set_xscale("log")
    ax[0].set_xticks([0.03, 0.05, 0.1, 0.2], ["0.03", "0.05", "0.1", "0.2"])
    ax[0].xaxis.set_minor_formatter(plt.NullFormatter())
    ax[0].set_xlabel("Public loss per day of late completion (% of project cost, log scale)")
    ax[0].set_title("Daily loss implied by each road's economic return", fontsize=9, loc="left")
    ax[0].legend(fontsize=7, loc="lower right")
    ax[0].grid(axis="y", visible=False)

    xs = np.linspace(0.12, 0.60, 60)
    for g, c in [(0.03, CAT[1]), (0.05, CAT[0]), (0.07, CAT[4])]:
        ax[1].plot(xs * 100, [(fyrr_from_eirr(x, g) / 365 + SUPERVISION) * 100 for x in xs], color=c,
                   label=f"benefit growth {int(g * 100)}%/yr")
    ax[1].axhline(RATE * 100, color=INK2, ls="--", lw=1.2, label="0.05%/day")
    ax[1].axvline(12, color=MUTED, lw=0.8)
    ax[1].text(12.5, 0.2, "12% hurdle", fontsize=7, color=INK2)
    ax[1].set_xlabel("Economic internal rate of return (%)")
    ax[1].set_ylabel("Daily loss (% of project cost)")
    ax[1].set_title("A proportionate rate follows the road's own appraisal", fontsize=9, loc="left")
    ax[1].legend(fontsize=7, loc="upper left")
    fig.suptitle("One rate for every road: 0.05% per day against the public loss from late completion", x=0.02,
                 ha="left", fontweight="bold", fontsize=10)
    fig.tight_layout()
    save(fig, D["figures"], "fig_proportionality")


if __name__ == "__main__":
    main()
