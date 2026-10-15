"""Forces of nature against a temporary-works standard: how foreseeable is a damaging storm at a river crossing?

(1) Analytic: probability that a temporary works designed for a T-year event is exceeded at least once during a
    contract of n years, at one structure and at any of k structures (independent, upper bound) or k_eff effectively
    independent structures (estimated from the observed cross-crossing correlation of annual maxima).
(2) Empirical, at the 34 HydroRIVERS crossings of the Project A and B roads: annual maximum 1-day and 3-day CHIRPS
    rainfall (1981-2018 pre-award baseline, GEV fit), and the return period of the largest event each crossing saw
    during its contract (A: 25 Apr 2019 - 31 Dec 2024, including the extended period; B: 10 May 2023 - 30 Sep 2026).
Outputs: results/exceedance_analytic.csv, results/crossing_events.csv, figures/fig_forces_of_nature.png
"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import genextreme

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.style import CAT, INK2, MUTED, paper_dir, save  # noqa: E402

D = paper_dir("08_forces_of_nature")
BASE = ("1981", "2018")
WINDOWS = {"A": ("2019-04-25", "2024-12-31"), "B": ("2023-05-10", "2026-09-30")}
T_STD = [2, 5, 10, 25, 50, 100]


def p_exceed(T, n, k=1):
    return 1 - (1 - 1 / T) ** (n * k)


def main():
    rain = pd.read_csv(D["data"] / "crossing_rain_daily.csv", index_col=0, parse_dates=True)
    cr = pd.read_csv(D["data"] / "crossings.csv")
    cr["key"] = cr.corridor + "@" + cr.chainage_km.astype(str)
    rows = []
    amax_all = {}
    for r in cr.itertuples():
        x = rain[r.key]
        proj = "A" if r.corridor.startswith("A") else "B"
        s, e = WINDOWS[proj]
        for dur in (1, 3):
            xs = x.rolling(dur).sum()
            amax = xs.loc[BASE[0]:BASE[1]].groupby(xs.loc[BASE[0]:BASE[1]].index.year).max()
            if dur == 1:
                amax_all[r.key] = amax
            c, loc, sc = genextreme.fit(amax.values)
            ev = xs.loc[s:e].max()
            when = xs.loc[s:e].idxmax()
            rp = 1 / max(genextreme.sf(ev, c, loc, sc), 1e-6)
            rows.append({"crossing": r.key, "project": proj, "upland_km2": r.upland_km2, "duration_d": dur,
                         "contract_max_mm": round(ev, 1), "date": when.date(), "return_period_yr": rp,
                         "rl10_mm": genextreme.isf(0.1, c, loc, sc), "years_in_window":
                             (pd.Timestamp(e) - pd.Timestamp(s)).days / 365.25})
    ev = pd.DataFrame(rows)
    ev.round(2).to_csv(D["results"] / "crossing_events.csv", index=False)
    # effective number of independent crossings per project (from the correlation of annual maxima)
    keff = {}
    for proj in ("A", "B"):
        cols = [k for k in amax_all if (k.startswith("A") if proj == "A" else k.startswith("B"))]
        m = pd.DataFrame({k: amax_all[k] for k in cols})
        m = m.loc[:, ~m.T.duplicated()]                        # crossings sharing a CHIRPS cell
        rho = m.corr().values[np.triu_indices(m.shape[1], 1)].mean() if m.shape[1] > 1 else 1
        keff[proj] = m.shape[1] / (1 + (m.shape[1] - 1) * max(rho, 0))
        print(f"{proj}: {len(cols)} crossings, {m.shape[1]} distinct rainfall cells, mean rho {rho:.2f},"
              f" effective independent k = {keff[proj]:.1f}")
    for proj, g in ev.groupby(["project", "duration_d"]):
        print(proj, f"crossings {len(g)}; max RP {g.return_period_yr.max():.0f} yr; share > 10-yr "
              f"{(g.return_period_yr > 10).mean():.0%}; > 25-yr {(g.return_period_yr > 25).mean():.0%}")
    an = []
    for T in T_STD:
        for n in (3, 5):
            an.append({"T": T, "contract_years": n, "one_structure": p_exceed(T, n),
                       "k_eff_A": p_exceed(T, n, keff["A"]), "k_eff_B": p_exceed(T, n, keff["B"]),
                       "k10_independent": p_exceed(T, n, 10)})
    an = pd.DataFrame(an)
    an.round(3).to_csv(D["results"] / "exceedance_analytic.csv", index=False)
    print(an.round(2).to_string(index=False))

    fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
    Ts = np.logspace(np.log10(2), 2, 80)
    for n, ls in [(3, "-"), (5, "--")]:
        ax[0].plot(Ts, p_exceed(Ts, n) * 100, color=CAT[0], ls=ls, label=f"one structure, {n}-yr contract")
        ax[0].plot(Ts, p_exceed(Ts, n, keff["B"]) * 100, color=CAT[3], ls=ls, lw=4, alpha=0.55, zorder=1,
                   label=f"any crossing, Project B (k_eff {keff['B']:.1f}), {n}-yr")
    ax[0].set_xscale("log")
    ax[0].set_xticks(T_STD, [str(t) for t in T_STD])
    ax[0].set_xlabel("Temporary-works design return period T (years)")
    ax[0].set_ylabel("Probability of exceedance during contract (%)")
    ax[0].set_title("A design storm is likely to be exceeded somewhere", fontsize=9, loc="left")
    ax[0].legend(fontsize=7, loc="upper right")
    rng = np.random.default_rng(1)
    for dur, filled in [(1, True), (3, False)]:
        g = ev[ev.duration_d == dur]
        jit = 10 ** rng.uniform(-0.04, 0.04, len(g))
        for proj, col in [("A", CAT[0]), ("B", CAT[3])]:
            m = (g.project == proj).values
            ax[1].scatter(g.upland_km2[m] * jit[m], g.return_period_yr[m].clip(upper=500), s=26,
                          facecolor=col if filled else "white", edgecolor=col, linewidths=1.2,
                          label=f"Project {proj}, {dur}-day maximum")
    for t in (10, 25):
        ax[1].axhline(t, color=MUTED, lw=0.8, ls="--")
        ax[1].text(11, t * 1.08, f"{t}-yr", fontsize=7, color=INK2)
    ax[1].set_xscale("log")
    ax[1].set_yscale("log")
    ax[1].set_yticks([1, 2, 5, 10, 25, 50], ["1", "2", "5", "10", "25", "50"])
    ax[1].legend(fontsize=7, loc="upper right")
    ax[1].set_xlabel("Upstream catchment area (km2, log scale)")
    ax[1].set_ylabel("Return period of largest rain in contract (yr)")
    ax[1].set_title("Largest storm each crossing saw during its contract", fontsize=9, loc="left")
    fig.suptitle("Forces of nature at river crossings: 'Unforeseeable' at one culvert, expected across a project",
                 x=0.02, ha="left", fontweight="bold", fontsize=10)
    fig.tight_layout()
    save(fig, D["figures"], "fig_forces_of_nature")


if __name__ == "__main__":
    main()
