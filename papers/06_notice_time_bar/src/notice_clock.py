"""When 'should' the Contractor have become aware? Objective awareness dates for data-observable events (Project A).

(1) Exceptionally adverse climate under MoWT Clause 1229 (Masindi, CHIRPS, contractor's 2005-2017 baseline,
    contract 25 Apr 2019 - 28 Apr 2022). For each month of the contract, the candidate awareness dates are:
      a. first day on which the month's rain-day count (>= 10 mm) exceeds its normal Nn  (first sign of excess);
      b. month end, when the month's V = (N - Nn) + (R - Rn)/20 is computable from a site gauge;
      c. publication of the gridded record (CHIRPS final, taken as the 20th of the following month).
    Clause 1229 entitles the algebraic sum of V over the whole period for completion, so entitlement itself is
    known only at the end: the running sum is tracked, with the months whose positive V is later cancelled.
(2) Possession (Sub-Clause 2.1 / Appendix to Bid): access to 30% of the remaining Site within 91 days of
    commencement, the rest 'in approximately 5 km sections over a period of 546 days'. For the 42.9 km Masindi-Biiso
    lot, the due date of each km under three readings: (i) sequential 5 km sections released evenly from day 91 to
    day 546; (ii) everything due at day 546; (iii) the Addendum 1 date for the first section (16 Mar 2021).
    Compared with the Sentinel-2 clearance month (Paper 2).
(3) Rhythm of the Contractor's possession notices listed in EOT-7 (letters 2687-2846).
Outputs: results/weather_awareness.csv, results/possession_awareness.csv, results/notice_intervals.csv,
         figures/fig_notice_clock.png
"""
import sys
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.style import CAT, INK2, MUTED, paper_dir, save  # noqa: E402

D = paper_dir("06_notice_time_bar")
P2 = Path(__file__).resolve().parents[2] / "02_site_access" / "results" / "clearance_A_lot3.csv"
START, END = pd.Timestamp("2019-04-25"), pd.Timestamp("2022-04-28")
BASE = (2005, 2017)
NOTICE = 28
LOT_KM = 42.851
NOTICES = {"2687 halting of works (KK)": "2022-10-26", "2731 pending land, Masindi-Biiso": "2022-11-18",
           "2798 pending land, Masindi-Biiso": "2023-01-06", "2823 pending land, Masindi-Biiso": "2023-01-25",
           "2846 further notice, Masindi-Biiso (dated 2022 in the report; sequence implies 2023)": "2023-02-20"}


def weather():
    x = pd.read_csv(D["data"] / "masindi_chirps_daily.csv", index_col=0, parse_dates=True).iloc[:, 0]
    wet = (x >= 10).astype(float)
    m = pd.DataFrame({"R": x.resample("MS").sum(), "N": wet.resample("MS").sum()})
    b = m[(m.index.year >= BASE[0]) & (m.index.year <= BASE[1])]
    m["Nn"] = b.N.groupby(b.index.month).mean().reindex(m.index.month).values
    m["Rn"] = b.R.groupby(b.index.month).mean().reindex(m.index.month).values
    m["V"] = np.maximum((m.N - m.Nn) + (m.R - m.Rn) / 20, -m.Nn)
    w = m.loc["2019-05-01":"2022-04-01"].copy()
    rows = []
    for ms, r in w.iterrows():
        days = x.loc[ms:ms + pd.offsets.MonthEnd(0)]
        cum = (days >= 10).cumsum()
        first = cum[cum > r.Nn].index.min() if (cum > r.Nn).any() else pd.NaT
        rows.append({"month": ms.strftime("%Y-%m"), "N": r.N, "Nn": round(r.Nn, 2), "R": round(r.R, 1),
                     "Rn": round(r.Rn, 1), "V": round(r.V, 2), "first_excess_day": first,
                     "month_end": ms + pd.offsets.MonthEnd(0),
                     "data_published": ms + pd.offsets.MonthBegin(1) + pd.Timedelta(days=19)})
    a = pd.DataFrame(rows)
    a["cum_V"] = a.V.cumsum()
    a["deadline_from_first_excess"] = a.first_excess_day + pd.Timedelta(days=NOTICE)
    a["deadline_before_month_end"] = a.deadline_from_first_excess < a.month_end
    a["deadline_before_data"] = a.deadline_from_first_excess < a.data_published
    a.to_csv(D["results"] / "weather_awareness.csv", index=False)
    pos = a[a.V > 0]
    final = a.cum_V.iloc[-1]
    flips = int((np.sign(a.cum_V).diff().fillna(0) != 0).sum())
    print(f"months {len(a)}, V>0 in {len(pos)}; final algebraic sum {final:.1f} days; running-sum sign changes {flips};"
          f" running max {a.cum_V.max():.1f} in {a.loc[a.cum_V.idxmax(), 'month']}")
    print(f"positive months with a first-excess day: {pos.first_excess_day.notna().sum()};"
          f" 28-day deadline from first excess falls before the data are published in "
          f"{pos.deadline_before_data.mean():.0%} of positive months (before month end in "
          f"{pos.deadline_before_month_end.mean():.0%})")
    return a


def possession():
    commence = START
    d91, d546 = commence + pd.Timedelta(days=91), commence + pd.Timedelta(days=546)
    n_sec = int(np.ceil(LOT_KM * 0.7 / 5))
    rows = []
    clr = pd.read_csv(P2).set_index("section").clearance_month if P2.exists() else pd.Series(dtype=str)
    for k in range(int(np.ceil(LOT_KM))):
        if k < 0.3 * LOT_KM:
            seq = d91
        else:
            i = int((k - 0.3 * LOT_KM) // 5)
            seq = d91 + (d546 - d91) * (i + 1) / n_sec
        rows.append({"km": k, "due_sequential": seq.normalize(), "due_all_at_546": d546,
                     "due_addendum_first_section": pd.Timestamp("2021-03-16") if k < 0.3 * LOT_KM else d546,
                     "clearance_month": clr.get(k)})
    p = pd.DataFrame(rows)
    p["spread_days"] = (p[["due_sequential", "due_all_at_546", "due_addendum_first_section"]].max(axis=1)
                        - p[["due_sequential", "due_all_at_546", "due_addendum_first_section"]].min(axis=1)).dt.days
    p.to_csv(D["results"] / "possession_awareness.csv", index=False)
    print(f"possession due-date spread across readings: median {p.spread_days.median():.0f} days, "
          f"max {p.spread_days.max()} days; day 91 = {d91.date()}, day 546 = {d546.date()}")
    return p


def intervals():
    n = pd.Series({k: pd.Timestamp(v) for k, v in NOTICES.items()}).sort_values()
    out = pd.DataFrame({"letter": n.index, "date": n.values})
    out["days_since_previous"] = out.date.diff().dt.days
    out.to_csv(D["results"] / "notice_intervals.csv", index=False)
    print(out.to_string(index=False))
    return out


def main():
    a, p, n = weather(), possession(), intervals()
    fig, ax = plt.subplots(2, 1, figsize=(11, 7.5), gridspec_kw={"height_ratios": [1.15, 1]})
    t = pd.to_datetime(a.month)
    ax[0].bar(t, a.V, width=25, color=[CAT[0] if v > 0 else MUTED for v in a.V], label="Monthly V (days)")
    ax[0].plot(t, a.cum_V, color=CAT[3], lw=2, label="Running algebraic sum (Clause 1229 entitlement)")
    ax[0].axhline(0, color=INK2, lw=0.8)
    ax[0].set_ylabel("Days")
    ax[0].set_title("(a) Weather: entitlement under the algebraic-sum rule is known only at the end of the contract",
                    fontsize=9, loc="left")
    ax[0].legend(fontsize=7.5, loc="upper left")
    ax[0].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))

    ax[1].scatter(p.due_sequential, p.km, marker="s", s=14, color=CAT[0],
                  label="Due: sequential 5 km sections, day 91-546")
    ax[1].scatter(p.due_all_at_546, p.km, marker="|", s=40, color=CAT[2], label="Due: all by day 546 (22 Oct 2020)")
    ax[1].scatter(p.due_addendum_first_section, p.km, marker="x", s=16, color=CAT[4],
                  label="Due: Addendum 1, first section by 16 Mar 2021")
    c = p.dropna(subset=["clearance_month"])
    ax[1].scatter(pd.to_datetime(c.clearance_month), c.km, s=14, color=CAT[3], zorder=3,
                  label="Corridor cleared (Sentinel-2, Paper 2)")
    for i, (lab, d) in enumerate(NOTICES.items()):
        ax[1].axvline(pd.Timestamp(d), color=MUTED, lw=0.8)
    ax[1].plot([], [], color=MUTED, lw=0.8, label="Contractor's notices to claim (EOT-7)")
    ax[1].set_ylabel("Chainage, Masindi-Biiso (km)")
    ax[1].set_title("(b) Possession: three readings of the access schedule give three awareness dates per km",
                    fontsize=9, loc="left")
    ax[1].legend(fontsize=7, loc="upper left", bbox_to_anchor=(0.0, 1.0), ncol=1)
    ax[1].xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    for x_ in ax:
        x_.grid(axis="x", visible=False)
    fig.suptitle("Project A: when should the Contractor have become aware?", x=0.02, ha="left",
                 fontweight="bold", fontsize=10)
    fig.tight_layout()
    save(fig, D["figures"], "fig_notice_clock")


if __name__ == "__main__":
    main()
