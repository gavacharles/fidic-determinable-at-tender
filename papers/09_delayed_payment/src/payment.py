"""Does the FIDIC financing charge compensate a Ugandan contractor for late payment?

Contract Data (Projects B, D, E): B = 1 percentage point above 'the discount rate of the Central Bank';
D and E (MDB 2010 GC) = 3 points above 'the discount rate of the central bank in the country of the currency of
payment'. Bank of Uganda publishes no rate called the 'discount rate': candidates are the Central Bank Rate (CBR,
policy rate, from July 2011), the 91-day Treasury bill yield (the market discount rate), or the rediscount rate
(set by BoU as a margin above the CBR; taken here as CBR + 4 points, illustrative).
Cost of funds: commercial bank weighted average lending rate (World Bank WDI FR.INR.LEND, annual, to 2018).
Also: the cost to a contractor of a delayed UGX 10 bn certificate over the delays reported by the Auditor General
(94-461 days beyond the 56-day payment period).
Inputs: cipi-tracker master_macro.csv (CBR, T-bills); WDI API.
Outputs: data/rates.csv, results/charge_gap.csv, results/ipc_cost.csv, figures/fig_delayed_payment.png
"""
import json
import sys
import urllib.request
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.style import CAT, INK2, MUTED, paper_dir, save  # noqa: E402

D = paper_dir("09_delayed_payment")
MACRO = Path.home() / "Projects" / "cipi-tracker" / "data" / "processed" / "master_macro.csv"
REDISCOUNT_MARGIN = 4.0
IPC = 10e9
DELAYS = [94, 200, 461]


def lending():
    f = D["data"] / "wdi_lending.csv"
    if not f.exists():
        u = "https://api.worldbank.org/v2/country/UGA/indicator/FR.INR.LEND?format=json&per_page=80&date=2000:2025"
        d = json.load(urllib.request.urlopen(u, timeout=60))[1]
        pd.DataFrame([{"year": int(x["date"]), "lending_rate": x["value"]} for x in d if x["value"]]) \
            .sort_values("year").to_csv(f, index=False)
    return pd.read_csv(f)


def main():
    m = pd.read_csv(MACRO, parse_dates=["date"]).set_index("date")
    r = m[["cbr_policy_rate", "tbill_91d_yield"]].loc["2011-07":].copy()
    r["rediscount_illustrative"] = r.cbr_policy_rate + REDISCOUNT_MARGIN
    lend = lending().set_index("year").lending_rate
    r["lending_rate_annual"] = lend.reindex(r.index.year).values
    r.to_csv(D["data"] / "rates.csv")
    charges = {"B: CBR + 1": r.cbr_policy_rate + 1, "B: T-bill + 1": r.tbill_91d_yield + 1,
               "D/E: CBR + 3": r.cbr_policy_rate + 3, "D/E: T-bill + 3": r.tbill_91d_yield + 3,
               "D/E: rediscount + 3": r.rediscount_illustrative + 3}
    rows = []
    ov = r.loc[: "2018-12"]
    for k, s in charges.items():
        gap = (r.lending_rate_annual - s).loc[: "2018-12"]
        rows.append({"charge": k, "mean_rate_2011_18": s.loc[:"2018-12"].mean(), "mean_rate_2019_26": s.loc["2019":].mean(),
                     "mean_gap_to_lending_2011_18": gap.mean(), "min_gap": gap.min(), "max_gap": gap.max()})
    g = pd.DataFrame(rows)
    g.round(2).to_csv(D["results"] / "charge_gap.csv", index=False)
    print("mean lending rate 2011-18:", round(ov.lending_rate_annual.mean(), 2))
    print(g.round(2).to_string(index=False))

    lend_ref = ov.lending_rate_annual.mean()
    recent = {k: s.loc["2023":].mean() for k, s in charges.items()}
    out = []
    for k, rate in recent.items():
        for d in DELAYS:
            charge = IPC * ((1 + rate / 100 / 12) ** (d / 30.4) - 1)       # compounded monthly (14.8)
            cost = IPC * ((1 + lend_ref / 100 / 12) ** (d / 30.4) - 1)
            out.append({"charge": k, "rate_2023_26": rate, "delay_days": d, "charge_ugx_m": charge / 1e6,
                        "cost_at_lending_ugx_m": cost / 1e6, "uncompensated_ugx_m": (cost - charge) / 1e6,
                        "share_compensated": charge / cost})
    o = pd.DataFrame(out)
    o.round(3).to_csv(D["results"] / "ipc_cost.csv", index=False)
    print(o[o.delay_days == 200].round(2).to_string(index=False))

    fig, ax = plt.subplots(1, 2, figsize=(12.5, 4.6), gridspec_kw={"width_ratios": [1.4, 1]})
    styles = {"B: CBR + 1": (CAT[0], "-"), "B: T-bill + 1": (CAT[0], ":"), "D/E: CBR + 3": (CAT[3], "-"),
              "D/E: T-bill + 3": (CAT[3], ":"), "D/E: rediscount + 3": (CAT[3], "--")}
    for k, s in charges.items():
        c, ls = styles[k]
        ax[0].plot(s.index, s, color=c, ls=ls, lw=1.4, label=f"Financing charge, {k}")
    ax[0].step(r.index, r.lending_rate_annual, where="post", color=INK2, lw=2.2, label="Commercial lending rate (WDI)")
    ax[0].set_ylabel("Annual rate (%)")
    ax[0].set_title("Contract financing charge vs the cost of borrowing", fontsize=9, loc="left")
    ax[0].legend(fontsize=6.8, loc="upper center", bbox_to_anchor=(0.5, -0.08), ncol=3, frameon=False)
    ax[0].set_ylim(0, 34)
    sub = o[o.delay_days == 200].sort_values("share_compensated")
    y = np.arange(len(sub))
    ax[1].barh(y, sub.cost_at_lending_ugx_m, color=MUTED, height=0.6, label=f"Contractor's financing cost at the 2011-18 mean lending rate ({lend_ref:.1f}%)")
    ax[1].barh(y, sub.charge_ugx_m, color=CAT[0], height=0.6, label="Financing charge recoverable under 14.8")
    for yi, row in zip(y, sub.itertuples()):
        ax[1].text(row.cost_at_lending_ugx_m + 15, yi, f"{row.share_compensated:.0%}", va="center", fontsize=7.5,
                   color=INK2)
    ax[1].set_yticks(y, sub.charge, fontsize=7.5)
    ax[1].set_xlabel("UGX million on a UGX 10 bn certificate paid 200 days late")
    ax[1].set_title("Share of the financing cost recovered (2023-26 rates)", fontsize=9, loc="left")
    ax[1].legend(fontsize=7, loc="upper center", bbox_to_anchor=(0.45, -0.17), frameon=False)
    ax[1].set_xlim(0, sub.cost_at_lending_ugx_m.max() * 1.18)
    for a in ax:
        a.grid(axis="x" if a is ax[1] else "y", visible=True)
    fig.suptitle("Delayed payment in Uganda: which 'discount rate', and does the charge compensate?", x=0.02,
                 ha="left", fontweight="bold", fontsize=10)
    fig.tight_layout()
    save(fig, D["figures"], "fig_delayed_payment")


if __name__ == "__main__":
    main()
