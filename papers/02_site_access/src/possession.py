"""Date right-of-way clearance per 1 km section from the Sentinel-2 series and compare with land-acquisition records.

Clearance month: first month in which section NDVI falls below (pre-works median - max(0.12, 3 x MAD)) and stays
below in at least 3 of the next 4 observed months, with NDBI above its pre-works median. Pre-works = 2018-01 .. 2019-12.
Comparison for Project A Masindi-Biiso (A_lot3):
  - land acquired by chainage (EOT-7, Employer strip map 9 Jun 2022 / Engineer letter 8 Feb 2023);
  - contractual availability date for the whole Site: 25 Oct 2020;
  - Contractor's claimed Section 2 delay window: 8 Jul 2021 - 24 Dec 2023.
Outputs: results/clearance_<corridor>.csv, results/possession_summary_<corridor>.csv, figures/fig_clearance_<corridor>.png
"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import ListedColormap

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.style import BLUE, CAT, INK2, MUTED, RED, paper_dir, save  # noqa: E402

D = paper_dir("02_site_access")
PRE = ("2018-01", "2019-12")
DATES = {"Contractual availability (25 Oct 2020)": "2020-10", "Claimed delay starts (8 Jul 2021)": "2021-07",
         "Strip map (9 Jun 2022)": "2022-06", "Claimed delay ends (24 Dec 2023)": "2023-12"}


def monthly(code):
    s = pd.read_csv(D["data"] / f"s2_sections_{code}.csv")
    s = s[(s.valid_frac >= 0.5) & s.ndvi.notna()]
    best = s.sort_values("valid_frac").groupby(["section", "month"]).tail(1)
    nd = best.pivot(index="month", columns="section", values="ndvi").sort_index()
    nb = best.pivot(index="month", columns="section", values="ndbi").sort_index()
    return nd, nb


def clearance(nd, nb):
    rows = []
    for sec in nd.columns:
        x, y = nd[sec].dropna(), nb[sec].dropna()
        pre = x.loc[PRE[0]:PRE[1]]
        if len(pre) < 6:
            rows.append({"section": sec, "clearance_month": None, "pre_ndvi": np.nan})
            continue
        med, mad = pre.median(), (pre - pre.median()).abs().median()
        thr = med - max(0.12, 3 * mad)
        ymed = y.loc[PRE[0]:PRE[1]].median()
        post = x.loc["2020-01":]
        found = None
        for i, (m, v) in enumerate(post.items()):
            nxt = post.iloc[i + 1:i + 5]
            if v < thr and (nxt < thr).sum() >= min(3, len(nxt)) and y.get(m, -9) > ymed:
                found = m
                break
        rows.append({"section": sec, "clearance_month": found, "pre_ndvi": med, "threshold": thr,
                     "min_post_ndvi": post.min() if len(post) else np.nan})
    return pd.DataFrame(rows)


def acquired(code, n_sections):
    f = D["data"] / "raw" / f"{code}_land_acquired.csv"
    if not f.exists():
        return pd.Series(np.nan, index=range(n_sections))
    a = pd.read_csv(f)
    share = []
    for k in range(n_sections):
        lo, hi = k, k + 1
        ov = sum(max(0, min(hi, r.end_km) - max(lo, r.start_km)) for r in a.itertuples())
        share.append(ov)
    return pd.Series(share, index=range(n_sections))


def main(code="A_lot3"):
    nd, nb = monthly(code)
    c = clearance(nd, nb)
    c["acquired_share"] = acquired(code, len(c)).values
    c["acquired"] = np.where(c.acquired_share >= 0.5, "acquired (by Jun 2022 / Feb 2023)", "not acquired")
    c.to_csv(D["results"] / f"clearance_{code}.csv", index=False)
    rows = []
    for grp, g in c.groupby("acquired"):
        r = {"group": grp, "sections": len(g), "cleared_ever": g.clearance_month.notna().mean()}
        for lab, m in DATES.items():
            r[f"cleared_by {lab}"] = (g.clearance_month.notna() & (g.clearance_month <= m)).mean()
        r["median_clearance"] = g.clearance_month.dropna().sort_values().iloc[len(g.clearance_month.dropna()) // 2] \
            if g.clearance_month.notna().any() else None
        rows.append(r)
    summ = pd.DataFrame(rows)
    summ.to_csv(D["results"] / f"possession_summary_{code}.csv", index=False)
    pd.set_option("display.width", 220)
    print(summ.round(2).to_string(index=False))

    # figure: NDVI anomaly heatmap (section x month), with acquisition status and key dates
    anom = nd.sub(nd.loc[PRE[0]:PRE[1]].median(), axis=1)
    fig, (ax0, ax) = plt.subplots(1, 2, figsize=(12, 6), gridspec_kw={"width_ratios": [0.4, 12], "wspace": 0.02},
                                  sharey=True)
    ax0.imshow(c.acquired_share.values[:, None], aspect="auto", cmap=ListedColormap([RED[3], BLUE[1]]), vmin=0, vmax=1,
               interpolation="nearest")
    ax0.set_xticks([])
    ax0.set_ylabel("Chainage (km)")
    ax0.set_title("land", fontsize=7.5)
    im = ax.imshow(anom.T.values, aspect="auto", cmap="RdBu", vmin=-0.3, vmax=0.3, interpolation="nearest")
    months = list(anom.index)
    ticks = [i for i, m in enumerate(months) if m.endswith("-01")]
    ax.set_xticks(ticks, [months[i][:4] for i in ticks])
    for lab, m in DATES.items():
        if m in months:
            ax.axvline(months.index(m), color=INK2, lw=1, ls="--")
            ax.text(months.index(m) + 0.5, -0.8, lab, rotation=0, fontsize=6.5, color=INK2, va="bottom")
    cm = [(months.index(m), s) for s, m in zip(c.section, c.clearance_month) if m in months]
    ax.scatter([a for a, _ in cm], [b for _, b in cm], marker="|", color="black", s=40, label="Detected clearance")
    ax.set_title("Right-of-way vegetation anomaly by 1 km section (Sentinel-2 NDVI vs 2018-19); blue = acquired land, "
                 "red = not acquired", fontsize=8.5, loc="left", pad=16)
    ax.legend(fontsize=7, loc="lower left")
    ax.grid(False)
    cb = fig.colorbar(im, ax=ax, fraction=0.025, pad=0.01)
    cb.set_label("NDVI anomaly", fontsize=8)
    save(fig, D["figures"], f"fig_clearance_{code}")


if __name__ == "__main__":
    main(*(sys.argv[1:] or ["A_lot3"]))
