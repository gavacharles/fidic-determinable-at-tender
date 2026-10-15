"""Pilot: COVID-19 restrictions in Uganda vs a contractor's Exceptional Event (force majeure) EOT claim.

Project A (anonymised) claimed 230 days; the Engineer granted 194 days for 10 Mar - 20 Sep 2020.
Measured against OxCGRT Uganda indicators (ordinal scales):
  C2 workplace closing (>= 2: closing required for some sectors), C5 public transport (>= 2: closed),
  C6 stay at home (>= 2: required except essential trips), C8 international travel (>= 3: bans on some regions),
  StringencyIndex (0-100).
Outputs: results/covid_claim_days.csv, figures/fig_covid_claim.png
"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.style import BLUE, CAT, INK2, RED, paper_dir, save  # noqa: E402

D = paper_dir("07_exceptional_events")
CLAIM = ("2020-03-10", "2020-09-20")


def main():
    o = pd.read_csv(D["data"] / "oxcgrt_uganda.csv", low_memory=False)
    u = o[o.CountryName == "Uganda"].copy()
    u["date"] = pd.to_datetime(u.Date.astype(str))
    u = u.set_index("date").sort_index()
    col = lambda k: [c for c in u.columns if c.startswith(k)][0]  # noqa: E731
    ind = pd.DataFrame({
        "workplace_closing": u[col("C2")] >= 2, "public_transport_closed": u[col("C5")] >= 2,
        "stay_at_home": u[col("C6")] >= 2, "intl_travel_ban": u[col("C8")] >= 3,
        "stringency": u["StringencyIndex_Average"] if "StringencyIndex_Average" in u else u[col("StringencyIndex")]})
    ind["any_site_relevant"] = ind[["workplace_closing", "public_transport_closed", "stay_at_home"]].any(axis=1)
    w = ind.loc[CLAIM[0]:CLAIM[1]]
    first = {k: (ind.index[ind[k]].min().date() if ind[k].any() else None)
             for k in ["workplace_closing", "public_transport_closed", "stay_at_home", "intl_travel_ban"]}
    summary = pd.DataFrame([{
        "claimed_days": (pd.Timestamp(CLAIM[1]) - pd.Timestamp(CLAIM[0])).days + 1,
        "days_any_site_relevant_restriction": int(w.any_site_relevant.sum()),
        "days_public_transport_closed": int(w.public_transport_closed.sum()),
        "days_stay_at_home": int(w.stay_at_home.sum()),
        "days_workplace_closing": int(w.workplace_closing.sum()),
        "days_before_first_restriction": int((w.index < pd.Timestamp(min(v for v in first.values() if v))).sum()),
        "mean_stringency_in_claim": round(w.stringency.mean(), 1),
        **{f"first_{k}": v for k, v in first.items()}}])
    summary.to_csv(D["results"] / "covid_claim_days.csv", index=False)
    print(summary.T.to_string())

    fig, ax = plt.subplots(figsize=(10, 4))
    s = ind.loc["2020-02-01":"2021-12-31"]
    ax.fill_between(s.index, 0, s.stringency, color=BLUE[1], lw=0, label="Stringency index (0-100)")
    for i, (k, lab, c) in enumerate([("public_transport_closed", "Public transport closed", RED[3]),
                                      ("stay_at_home", "Stay-at-home required", CAT[3]),
                                      ("workplace_closing", "Workplace closing required", CAT[6])]):
        on = s[k]
        ax.fill_between(s.index, 102 + i * 5, 106 + i * 5, where=on, color=c, lw=0, step="mid", label=lab)
    ax.axvspan(pd.Timestamp(CLAIM[0]), pd.Timestamp(CLAIM[1]), color=INK2, alpha=0.08, lw=0,
               label="Period granted (194 days; 230 claimed)")
    ax.set_ylim(0, 120)
    ax.set_ylabel("Stringency index")
    ax.set_title("COVID-19 restrictions in Uganda vs an Exceptional Event EOT claim (Project A)", loc="left")
    ax.legend(fontsize=7.5, loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=3, frameon=False)
    ax.grid(axis="x", visible=False)
    save(fig, D["figures"], "fig_covid_claim")


if __name__ == "__main__":
    main()
