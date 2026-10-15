"""Same pandemic, different verdict: how the choice of indicator and country fixes an Exceptional Event's duration.

(1) OxCGRT, Kenya / Rwanda / Tanzania / Uganda: for each indicator that could define a COVID-19 Exceptional Event
    (C2 workplace closing >= 2, C5 public transport closed >= 2, C6 stay at home >= 2, C7 internal movement >= 2,
    C8 international travel >= 3, Stringency >= 70), the first and last day in force and the days in force in 2020-21,
    and within Project A's granted window (10 Mar - 20 Sep 2020).
(2) UCDP GED: monthly probability of at least one fatal organised-violence event within 50 km of the programme's
    project sites, 2000-2023 (a baseline for 'riot, commotion' claims), and the events recorded in 2020-21.
Outputs: results/ea_indicator_days.csv, results/ucdp_site_baseline.csv, figures/fig_ea_compare.png
"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.style import CAT, INK2, MUTED, paper_dir, save  # noqa: E402

D = paper_dir("07_exceptional_events")
WINDOW = (pd.Timestamp("2020-03-10"), pd.Timestamp("2020-09-20"))
IND = {"Workplace closing (C2>=2)": ("C2", 2), "Public transport closed (C5>=2)": ("C5", 2),
       "Stay at home (C6>=2)": ("C6", 2), "Internal movement (C7>=2)": ("C7", 2),
       "International travel ban (C8>=3)": ("C8", 3), "Stringency index >= 70": ("StringencyIndex", 70)}
SITES = {"Masindi (A)": (1.68, 31.72), "Hoima (A/B)": (1.43, 31.35), "Kiboga (B)": (0.92, 31.77),
         "Busunju (B)": (0.57, 32.21), "Kampala (E)": (0.35, 32.58), "Kapchorwa (D)": (1.40, 34.45)}


def oxcgrt():
    o = pd.read_csv(D["data"] / "oxcgrt_uganda.csv", low_memory=False)
    o["date"] = pd.to_datetime(o.Date.astype(str))
    rows, series = [], {}
    for c, g in o.groupby("CountryName"):
        g = g.set_index("date").sort_index()
        for lab, (k, thr) in IND.items():
            col = [x for x in g.columns if x.startswith(k)][0]
            on = (g[col] >= thr)
            days = on[on]
            w = on.loc[WINDOW[0]:WINDOW[1]]
            rows.append({"country": c, "indicator": lab, "first_day": days.index.min(), "last_day": days.index.max(),
                         "days_2020_21": int(on.loc["2020":"2021"].sum()), "days_in_window": int(w.sum()),
                         "window_days": len(w)})
            series[(c, lab)] = on.loc["2020-01-01":"2021-12-31"]
    r = pd.DataFrame(rows)
    r.to_csv(D["results"] / "ea_indicator_days.csv", index=False)
    pd.set_option("display.width", 200)
    print(r.pivot(index="indicator", columns="country", values="days_2020_21").to_string())
    print(r.pivot(index="indicator", columns="country", values="days_in_window").to_string())
    return r, series


def ucdp():
    u = pd.read_csv(D["data"] / "ucdp_ged_ea.csv", low_memory=False)
    u["date"] = pd.to_datetime(u.date_start.str[:10])
    u = u[(u.date >= "2000-01-01")]
    rows = []
    months = pd.period_range("2000-01", "2023-12", freq="M")
    for s, (la, lo) in SITES.items():
        dist = 111.2 * np.hypot(u.latitude - la, (u.longitude - lo) * np.cos(np.radians(la)))
        near = u[(dist <= 50) & (u.best > 0)]
        hit = near.date.dt.to_period("M").unique()
        p = len(hit) / len(months)
        rows.append({"site": s, "events_2000_23": len(near), "months_with_fatal_event": len(hit),
                     "monthly_probability": p, "return_period_months": 1 / p if p else np.inf,
                     "events_2020_21": int((near.date.dt.year.isin([2020, 2021])).sum())})
    b = pd.DataFrame(rows)
    b.round(4).to_csv(D["results"] / "ucdp_site_baseline.csv", index=False)
    print(b.round(3).to_string(index=False))
    ug = u[u.country == "Uganda"]
    print("UCDP Uganda events in 2020:", int((ug.date.dt.year == 2020).sum()), "; 2021:", int((ug.date.dt.year == 2021).sum()))
    return b


def main():
    r, series = oxcgrt()
    ucdp()
    countries = ["Uganda", "Kenya", "Rwanda", "Tanzania"]
    fig, ax = plt.subplots(1, 2, figsize=(13, 5.2), gridspec_kw={"width_ratios": [1.6, 1]})
    y, labels = 0, []
    cols = dict(zip(countries, [CAT[0], CAT[3], CAT[2], CAT[4]]))
    for lab in IND:
        for c in countries:
            s = series[(c, lab)]
            on = s[s].index
            ax[0].scatter(on, np.full(len(on), y), marker="|", s=18, color=cols[c], linewidths=1)
            labels.append((y, f"{lab} — {c}"))
            y += 1
        y += 0.8
    ax[0].axvspan(*WINDOW, color=MUTED, alpha=0.25, lw=0)
    ax[0].text(WINDOW[0] + pd.Timedelta(days=3), -0.9, "Project A window granted", fontsize=7, color=INK2, va="bottom")
    ax[0].set_yticks([a for a, _ in labels], [b for _, b in labels], fontsize=6.3)
    ax[0].invert_yaxis()
    ax[0].set_title("Days each candidate trigger was in force, 2020-21", fontsize=9, loc="left")
    ax[0].grid(axis="y", visible=False)
    for c in countries:
        ax[0].plot([], [], color=cols[c], lw=3, label=c)
    ax[0].legend(fontsize=7, loc="upper center", bbox_to_anchor=(0.5, -0.07), ncol=4, frameon=False)

    piv = r[r.country == "Uganda"].set_index("indicator")
    yy = np.arange(len(piv))
    ax[1].barh(yy, piv.days_in_window, color=CAT[0], height=0.55, label="Uganda: days in force within window")
    ax[1].axvline(194, color=INK2, ls="--", lw=1, label="Granted (194 days)")
    ax[1].axvline(230, color=CAT[3], ls=":", lw=1.2, label="Claimed (230 days)")
    ax[1].set_yticks(yy, piv.index, fontsize=7.5)
    ax[1].invert_yaxis()
    ax[1].set_xlabel("Days (10 Mar - 20 Sep 2020 = 195 days)")
    ax[1].set_title("Project A: the verdict depends on the indicator", fontsize=9, loc="left")
    ax[1].set_xlim(0, 250)
    ax[1].legend(fontsize=7, loc="upper center", bbox_to_anchor=(0.4, -0.12), ncol=3, frameon=False)
    ax[1].grid(axis="y", visible=False)
    fig.suptitle("COVID-19 as an Exceptional Event in East Africa: same pandemic, different durations", x=0.02,
                 ha="left", fontweight="bold", fontsize=10)
    fig.tight_layout()
    save(fig, D["figures"], "fig_ea_compare")


if __name__ == "__main__":
    main()
