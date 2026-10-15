"""How slow is 'too slow'? Benchmarks for FIDIC 8.6 [2017: 8.7] and 15.2, on Projects A and B.

Project B (rehabilitation, 145 km; commenced 10 May 2023, Time for Completion 36 months to 9 May 2026; Engineer has
recommended a 273-day EOT): planned and actual monthly physical progress from Monthly Progress Report 23 (May 2023 -
Jul 2025); 31 Aug 2025: 21.55% actual vs 90.56% planned, time 77%; the Contractor reduced the rate of work under
16.1 for unpaid IPCs (UGX 26 bn).
Project A (design and build, 97 km): Engineer's snapshots - Feb 2021: time 58.73%, revised plan 22.29%, actual 20.56%;
Dec 2021: time 81.50%, plan 61.10%, actual 54.05%.
Benchmarks: (i) time-linear; (ii) the programme (original or revised); (iii) the milestone '40% physical progress
in 60% of the contract period' (Projects B, E). Recovery test: required average monthly progress to finish by the
(possibly extended) Time for Completion, as a multiple of the programme's peak monthly rate and of the Contractor's
best demonstrated 3-month rate.
Outputs: results/progress_B.csv, results/benchmarks.csv, figures/fig_progress.png
"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.style import CAT, INK2, MUTED, paper_dir, save  # noqa: E402

D = paper_dir("10_rate_of_progress")
PLAN_M = [0.00, 0.00, 0.00, 1.33, 1.33, 1.33, 1.34, 1.82, 1.55, 3.29, 3.23, 3.18, 3.29, 3.08, 3.21, 5.12, 5.17, 5.35,
          5.43, 5.38, 5.21, 5.50, 5.08, 5.03, 4.40, 3.95, 3.93, 3.03, 2.64, 2.60, 1.88, 1.54, 0.54, 0.19, 0.05, 0.00]
ACT_M = [0.00, 0.00, 0.00, 0.04, 0.14, 0.12, 0.11, 0.15, 0.04, 0.34, 0.43, 0.38, 0.16, 0.66, 1.09, 1.41, 1.63, 1.87,
         2.53, 2.63, 1.23, 2.34, 0.59, 0.86, 0.73, 1.06, 0.68]
TFC_M = 36
EOT_M = 273 / 30.44
A_SNAPS = [("Feb 2021", 58.73, 22.29, 20.56), ("Dec 2021", 81.50, 61.10, 54.05)]


def main():
    months = pd.period_range("2023-05", periods=len(PLAN_M), freq="M")
    b = pd.DataFrame({"month": months.astype(str), "t": np.arange(1, len(PLAN_M) + 1),
                      "plan_cum": np.cumsum(PLAN_M)})
    b["actual_cum"] = pd.Series(np.cumsum(ACT_M)).reindex(range(len(b))).values
    b["time_pct"] = b.t / TFC_M * 100
    peak_plan = max(PLAN_M)
    best3_to_date = pd.Series(ACT_M).rolling(3).mean().expanding().max().reindex(range(len(b))).values
    best3 = np.nanmax(best3_to_date)
    b["best3_to_date"] = best3_to_date
    for lab, T in [("tfc", TFC_M), ("tfc_eot", TFC_M + EOT_M)]:
        rem = (T - b.t).clip(lower=0.5)
        b[f"required_rate_{lab}"] = (100 - b.actual_cum) / rem
        b[f"R_plan_peak_{lab}"] = b[f"required_rate_{lab}"] / peak_plan
        b[f"R_demonstrated_{lab}"] = b[f"required_rate_{lab}"] / b.best3_to_date.where(b.t >= 6)
    b.round(3).to_csv(D["results"] / "progress_B.csv", index=False)
    a = b.dropna(subset=["actual_cum"])
    first = lambda col: a.loc[a[col] > 1, "month"].iloc[0] if (a[col] > 1).any() else None  # noqa: E731
    t60 = 0.6 * TFC_M
    act60 = np.interp(t60, a.t, a.actual_cum)
    plan60 = np.interp(t60, b.t, b.plan_cum)
    print(f"Project B: at 60% time (month {t60:.1f}) actual {act60:.1f}% vs plan {plan60:.1f}% vs milestone 40%")
    print(f"peak planned monthly {peak_plan}%, best demonstrated 3-month {best3:.2f}%/month")
    for col in ["R_plan_peak_tfc", "R_demonstrated_tfc", "R_plan_peak_tfc_eot", "R_demonstrated_tfc_eot"]:
        print(f"  first month {col} > 1: {first(col)}")
    last = a.iloc[-1]
    print(f"  at {last.month}: required {last.required_rate_tfc:.1f}%/month (TfC) or {last.required_rate_tfc_eot:.1f}"
          f"%/month (with EOT) vs demonstrated {best3:.2f}")

    rows = []
    for lab, tp, plan, act in [(f"B {r.month}", r.time_pct, r.plan_cum, r.actual_cum) for r in a.iloc[[20, -1]].itertuples()] + \
            [(f"A {m}", tp, pl, ac) for m, tp, pl, ac in A_SNAPS]:
        rows.append({"case": lab, "time_pct": tp, "actual": act, "behind_time_linear": tp - act,
                     "behind_programme": plan - act, "milestone_40_at_60": ("met" if act >= 40 else "missed")
                     if tp >= 60 else "n/a (before 60%)"})
    bm = pd.DataFrame(rows)
    bm.round(2).to_csv(D["results"] / "benchmarks.csv", index=False)
    print(bm.round(1).to_string(index=False))

    fig, ax = plt.subplots(1, 2, figsize=(12.5, 4.8))
    ax[0].plot(b.time_pct, b.plan_cum, color=CAT[0], lw=2, label="Programme (planned)")
    ax[0].plot(a.time_pct, a.actual_cum, color=CAT[3], lw=2.2, label="Actual (MPR 23)")
    ax[0].plot([0, 100], [0, 100], color=MUTED, lw=1, ls="--", label="Time-linear")
    ax[0].scatter([60], [40], marker="D", s=50, color=INK2, zorder=4, label="Milestone: 40% at 60% of time")
    for name, tp, pl, ac in A_SNAPS:
        ax[0].scatter(tp, ac, marker="s", s=36, color=CAT[2], zorder=4)
        ax[0].scatter(tp, pl, marker="s", s=36, facecolor="white", edgecolor=CAT[2], zorder=4)
    ax[0].scatter([], [], marker="s", color=CAT[2], label="Project A actual (Engineer's snapshots)")
    ax[0].scatter([], [], marker="s", facecolor="white", edgecolor=CAT[2], label="Project A revised programme")
    ax[0].set_xlabel("Time elapsed (% of original Time for Completion)")
    ax[0].set_ylabel("Cumulative physical progress (%)")
    ax[0].set_title("Three benchmarks, three verdicts", fontsize=9, loc="left")
    ax[0].legend(fontsize=7, loc="upper left")
    ax[0].set_xlim(0, 102)
    ax[0].set_ylim(0, 102)

    ax[1].plot(a.month.str[2:], a.required_rate_tfc, color=CAT[3], lw=2, label="Required to finish by original TfC")
    ax[1].plot(a.month.str[2:], a.required_rate_tfc_eot, color=CAT[3], lw=1.6, ls="--",
               label="Required to finish with 273-day EOT")
    ax[1].axhline(peak_plan, color=CAT[0], lw=1.2, label=f"Programme's peak monthly rate ({peak_plan}%)")
    ax[1].plot(a.month.str[2:], a.best3_to_date, color=INK2, lw=1.2, ls=":",
               label=f"Contractor's best 3-month rate to date (max {best3:.1f}%)")
    ax[1].set_ylabel("Average monthly progress needed (% of works)")
    ax[1].set_title("Project B: when did completion on time become infeasible?", fontsize=9, loc="left")
    ax[1].set_xticks(range(0, len(a), 3), a.month.str[2:].iloc[::3], rotation=45, fontsize=7)
    ax[1].legend(fontsize=7, loc="upper left")
    ax[1].set_ylim(0, max(a.required_rate_tfc.max() * 1.1, 12))
    fig.suptitle("Rate of progress: 'too slow' depends on the benchmark the contract never names", x=0.02, ha="left",
                 fontweight="bold", fontsize=10)
    fig.tight_layout()
    save(fig, D["figures"], "fig_progress")


if __name__ == "__main__":
    main()
