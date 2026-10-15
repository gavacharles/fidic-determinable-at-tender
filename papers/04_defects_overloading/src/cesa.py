"""How determinable is 'design traffic'? Recomputing the cumulative equivalent standard axles (CESA) of Project B
(Busunju-Kiboga, Busunju count station) under the alternative, individually defensible inputs in its design review.

Inputs (Project B design review, sections 6.3.1-6.3.6):
  - 2018 ADT by vehicle class at Busunju; seasonal factor 0.94 (ADT -> AADT);
  - vehicle equivalence factors (VEF): project axle-load survey (Kihemba, May 2018) and six other Ugandan surveys;
  - growth scenarios low / medium / high, with the Design Team's (opening 2021) and Supervision Team's (opening 2027)
    growth periods; design period 10 or 15 years.
The lane/direction factor is not reported ('an assumption has been made'); it is calibrated so that the Supervision
Team's own case (project VEF, medium, opening 2027, 10 years) reproduces its 19.27 MESA, and 0.5 is the alternative.
Traffic classes (URDM / ORN 31, MESA): T6 6-10, T7 10-17, T8 17-30, T9 > 30.
Outputs: results/cesa_cases.csv, results/cesa_summary.csv, figures/fig_cesa.png
"""
import itertools
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.style import CAT, INK2, MUTED, paper_dir, save  # noqa: E402

D = paper_dir("04_defects_overloading")

ADT_2018 = {"med_bus": 16, "large_bus": 31, "truck_2ax": 238, "truck_3ax": 471, "artic": 35}   # Busunju station
SEASONAL = 0.94
VEF = {  # medium bus, large bus, 2-axle truck, 3-axle truck, articulated (mean of semi- and truck-trailer)
    "Project B (Kihemba 2018)": (6.29, 6.29, 3.17, 5.86, 10.04),
    "Tororo-Kamdini (2013)": (0.09, 1.62, 2.64, 0.92, (1.08 + 5.48) / 2),
    "Nebbi-Pakwach (2017)": (3.63, 3.63, 3.93, 3.93, 8.52),
    "Kyenjojo-Fort Portal (2014)": (0.05, 1.32, 0.18, 1.84, (5.8 + 11.5) / 2),
    "Kapchorwa-Suam (2015)": (0.3, 1.1, 0.3, 2.0, (2.0 + 9.0) / 2),
    "Jinja-Mukono": (0.07, 3.2, 1.02, 1.84, (6.47 + 12.74) / 2),
    "Busega-Mityana (2009)": (0.0, 2.5, 0.3, 2.0, (6.4 + 10.0) / 2),
}
GROWTH = {  # (first period rate, second period rate, later rate) in %
    "low": (2.7, 3.5, 3.0), "medium": (4.2, 5.0, 3.0), "high": (5.7, 6.5, 3.0)}
OPENING = {2021: (2021, 2031), 2027: (2027, 2036)}    # opening year -> last year of the second growth period
CLASSES = [(0, 6, "T5-"), (6, 10, "T6"), (10, 17, "T7"), (17, 30, "T8"), (30, 1e9, "T9")]
ST_TARGET = 19.266922   # MESA, Supervision Team, Busunju, medium, 10 years


def tclass(m):
    return next(c for lo, hi, c in CLASSES if lo <= m < hi)


def cesa(v, g, o, n, lane):
    vef, growth, opening, years = v, g, o, n
    g1, g2, g3 = (x / 100 for x in GROWTH[growth])
    open_y, end2 = OPENING[opening]
    daily = SEASONAL * sum(n * v for n, v in zip(ADT_2018.values(), VEF[vef]))
    total, y = 0.0, 2018
    while y < open_y + years:
        if y >= open_y:
            total += daily * 365
        daily *= 1 + (g1 if y < open_y else g2 if y <= end2 else g3)
        y += 1
    return total * lane / 1e6


def main():
    lane_cal = ST_TARGET / cesa("Project B (Kihemba 2018)", "medium", 2027, 10, 1.0)
    print(f"calibrated lane/direction factor {lane_cal:.3f}")
    rows = []
    for v, g, o, n, lane in itertools.product(VEF, GROWTH, OPENING, (10, 15), (lane_cal, 0.5)):
        m = cesa(v, g, o, n, lane)
        rows.append({"vef": v, "growth": g, "opening": o, "design_years": n,
                     "lane_factor": "calibrated" if lane == lane_cal else "0.5", "mesa": m, "class": tclass(m)})
    c = pd.DataFrame(rows)
    c.round(2).to_csv(D["results"] / "cesa_cases.csv", index=False)

    # one-at-a-time swings around the Supervision Team's case
    base = dict(v="Project B (Kihemba 2018)", g="medium", o=2027, n=10, lane=lane_cal)
    b = cesa(**base)
    swings = []
    for lab, key, alts in [("Axle-load survey (VEF)", "v", list(VEF)), ("Growth scenario", "g", list(GROWTH)),
                           ("Opening year 2021 vs 2027", "o", list(OPENING)), ("Design period 10 vs 15 yr", "n", [10, 15]),
                           ("Lane/direction factor", "lane", [lane_cal, 0.5])]:
        vals = [cesa(**{**base, key: a}) for a in alts]
        swings.append({"input": lab, "min_mesa": min(vals), "max_mesa": max(vals), "ratio": max(vals) / min(vals)})
    s = pd.DataFrame(swings)
    summ = pd.concat([s, pd.DataFrame([{"input": "ALL combinations", "min_mesa": c.mesa.min(), "max_mesa": c.mesa.max(),
                                        "ratio": c.mesa.max() / c.mesa.min()}])])
    summ.round(2).to_csv(D["results"] / "cesa_summary.csv", index=False)
    print(f"ST base case {b:.2f} MESA")
    print(summ.round(2).to_string(index=False))
    print(c["class"].value_counts(normalize=True).round(3).to_string())
    print("10-year cases by class:", c[c.design_years == 10]["class"].value_counts(normalize=True).round(3).to_dict())

    fig, ax = plt.subplots(1, 2, figsize=(12, 4.4), gridspec_kw={"width_ratios": [1.1, 1]})
    s = s.sort_values("ratio")
    y = np.arange(len(s))
    ax[0].barh(y, s.max_mesa - s.min_mesa, left=s.min_mesa, color=CAT[0], height=0.55)
    ax[0].axvline(b, color=INK2, lw=1, ls="--", label=f"Supervision Team case {b:.1f} MESA")
    ax[0].axvline(10, color=CAT[3], lw=1, ls=":", label="Design Team 10 MESA")
    ax[0].set_yticks(y, s.input, fontsize=8)
    for yi, r in zip(y, s.itertuples()):
        ax[0].text(r.max_mesa + 0.6, yi, f"x{r.ratio:.1f}", va="center", fontsize=7.5, color=INK2)
    ax[0].set_xlabel("Design traffic, CESA (MESA)")
    ax[0].set_title("One input changed at a time", fontsize=9, loc="left")
    ax[0].legend(fontsize=7, loc="lower right")
    ax[0].set_xlim(0, max(s.max_mesa) * 1.18)
    bins = np.arange(0, c.mesa.max() + 5, 2.5)
    for n, col in [(10, CAT[0]), (15, CAT[2])]:
        ax[1].hist(c[c.design_years == n].mesa, bins=bins, alpha=0.7, color=col, label=f"{n}-year design period")
    for lo, hi, lab in CLASSES[1:]:
        ax[1].axvline(lo, color=MUTED, lw=0.8)
        ax[1].text(lo + 0.4, ax[1].get_ylim()[1] * 0.93, lab, fontsize=7.5, color=INK2)
    ax[1].set_xlabel("Design traffic (MESA)")
    ax[1].set_ylabel("Number of input combinations")
    ax[1].set_title(f"All {len(c)} combinations span {c.mesa.min():.1f}-{c.mesa.max():.0f} MESA", fontsize=9, loc="left")
    ax[1].legend(fontsize=7, loc="center right")
    for a in ax:
        a.grid(axis="y", visible=False)
    fig.suptitle("Project B: the design load against which 'overloading' and defects are judged is itself a choice",
                 x=0.02, ha="left", fontweight="bold", fontsize=10)
    fig.tight_layout()
    save(fig, D["figures"], "fig_cesa")


if __name__ == "__main__":
    main()
