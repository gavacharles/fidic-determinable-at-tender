"""Foreseeability of poor subgrade as a function of site-investigation density (Project A, Masindi-Biiso test pits).

A test pit is 'poor' if soaked CBR at 95% MDD < POOR_CBR (sensitivity 6, 8, 10). The Base-Date information is
simulated by keeping test pits at spacing s (1, 2, 5, 10 km; every offset), and predicting each unsampled pit from
its two nearest sampled neighbours ('foreseeable as poor' if either neighbour is poor). Unforeseen = actually poor
but both neighbours good. Outputs the share of poor ground that is unforeseen at each spacing, the expected unforeseen
length per 10 km, and the lag correlation of CBR along the alignment.
Outputs: results/foreseeability.csv, results/autocorrelation.csv, figures/fig_foreseeability.png
"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.style import CAT, INK2, paper_dir, save  # noqa: E402

D = paper_dir("03_ground_conditions")
SPACINGS = [1, 2, 3, 5, 10]
THRESHOLDS = [6, 8, 10]


def simulate(tp, s, thr):
    poor = (tp.CBR95 < thr).values
    km = tp.chainage_km.values
    res = []
    grid = np.arange(0, 0.5 * s * 2 + 1e-9, 0.5)                   # offsets on the 0.5 km grid
    for off in grid[grid < s]:
        sampled = np.isclose(((km - off) % s), 0, atol=0.26) | np.isclose(((km - off) % s), s, atol=0.26)
        if sampled.sum() < 2:
            continue
        sk, sp = km[sampled], poor[sampled]
        for k, p, smp in zip(km, poor, sampled):
            if smp:
                continue
            left = sk[sk < k]
            right = sk[sk > k]
            nb = []
            if len(left):
                nb.append(sp[np.where(sk == left.max())[0][0]])
            if len(right):
                nb.append(sp[np.where(sk == right.min())[0][0]])
            res.append({"poor": p, "foreseen_poor": any(nb)})
    r = pd.DataFrame(res)
    n_poor = r.poor.sum()
    return {"spacing_km": s, "threshold_cbr": thr, "unsampled_pits": len(r), "poor_pits": int(n_poor),
            "unforeseen_share_of_poor": (r.poor & ~r.foreseen_poor).sum() / n_poor if n_poor else np.nan,
            "false_alarm_share_of_good": (~r.poor & r.foreseen_poor).sum() / (~r.poor).sum()}


def main():
    tp = pd.read_csv(D["data"] / "raw" / "testpits_A_lot3.csv").dropna(subset=["CBR95"])
    rows = [simulate(tp, s, t) for t in THRESHOLDS for s in SPACINGS]
    f = pd.DataFrame(rows)
    base_rate = {t: (tp.CBR95 < t).mean() for t in THRESHOLDS}
    f["poor_share_overall"] = f.threshold_cbr.map(base_rate)
    f["unforeseen_km_per_10km"] = f.unforeseen_share_of_poor * f.poor_share_overall * 10
    f.round(3).to_csv(D["results"] / "foreseeability.csv", index=False)
    print(f.round(3).to_string(index=False))
    x = tp.set_index("chainage_km").CBR95
    ac = []
    for lag in [0.5, 1, 2, 3, 5]:
        pairs = [(x[a], x[b]) for a in x.index for b in x.index if abs((b - a) - lag) < 0.05]
        if len(pairs) > 5:
            a, b = zip(*pairs)
            ac.append({"lag_km": lag, "n_pairs": len(pairs), "corr_CBR95": np.corrcoef(a, b)[0, 1]})
    ac = pd.DataFrame(ac)
    ac.round(3).to_csv(D["results"] / "autocorrelation.csv", index=False)
    print(ac.round(3).to_string(index=False))

    fig, ax = plt.subplots(1, 2, figsize=(11, 3.8))
    ax[0].plot(tp.chainage_km, tp.CBR95, "o-", ms=3, lw=1, color=CAT[0])
    for t, c in zip(THRESHOLDS, [CAT[7], CAT[3], CAT[2]]):
        ax[0].axhline(t, color=c, lw=1, ls="--", label=f"CBR95 = {t}%")
    ax[0].set_xlabel("Chainage (km)")
    ax[0].set_ylabel("Soaked CBR at 95% MDD (%)")
    ax[0].set_title("Subgrade test pits along the alignment", fontsize=9)
    ax[0].legend(fontsize=7, loc="upper right")
    for t, c in zip(THRESHOLDS, [CAT[7], CAT[3], CAT[2]]):
        g = f[f.threshold_cbr == t]
        ax[1].plot(g.spacing_km, g.unforeseen_share_of_poor * 100, "o-", color=c, label=f"poor = CBR95 < {t}%")
    ax[1].set_xlabel("Site-investigation spacing available at Base Date (km)")
    ax[1].set_ylabel("Share of poor subgrade that is unforeseen (%)")
    ax[1].set_title("The location of poor subgrade is not foreseeable at any spacing", fontsize=9)
    ax[1].legend(fontsize=7)
    for a in ax:
        a.grid(axis="x", visible=False)
    fig.suptitle("Project A: how much poor subgrade an experienced contractor could have foreseen", x=0.06,
                 ha="left", fontweight="bold", fontsize=10)
    save(fig, D["figures"], "fig_foreseeability")


if __name__ == "__main__":
    main()
