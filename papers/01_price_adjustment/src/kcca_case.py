"""Case: the 'sources of indices' dispute on an urban road contract (KCCA KCRRP Lot 1; FIDIC MDB 2010; commencement
Aug 2022; reported anonymised as Project E in the paper).

Table B (foreign currency, USD) names US BLS indices (base Dec 2020); the note under Tables A and B names, for foreign
inputs, the official index of the expatriates' home country (China) or the input's source country. The Engineer
proposed UBOS for both currencies. The Contractor reported average increases of 21.89% (UBOS) vs 32.19% (BLS).
Here the foreign-currency multiplier Pn is recomputed, Aug 2022 - Dec 2025, under:
  US BLS (current vintage, via FRED), US BLS with the bid's preliminary base values, UBOS (spliced Jun 2022),
  (China, the third source the note points to, is not computed: no open monthly series).
Outputs: data/fred_series.csv, results/kcca_foreign_pn.csv, results/kcca_summary.csv, figures/fig_kcca.png
"""
import io
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common.style import CAT, INK2, paper_dir, save  # noqa: E402
from contract_recompute import series  # noqa: E402

D = paper_dir("01_price_adjustment")
W = dict(a=.20, L=.15, B=.10, C=.05, R=.10, F=.19, M=.01, E=.20)        # Table B weights
FRED = {"L": "CES2000000008", "B": "WPU0581", "C": "WPU1322", "R": "WPU1017", "F": "WPU057303", "M": "WPU10",
        "E": "WPU112"}
# China ('home country of the expatriate workforce') is a third defensible source; no open monthly series of Chinese
# construction-input indices is available without registration, so it is reported but not computed.
BID_BASE = {"L": 29.71, "R": 191.1, "M": 231.4, "E": 236.8}               # printed in the bid (Dec 2020, preliminary)
BASE_US, BASE_UG = pd.Timestamp("2020-12-01"), pd.Timestamp("2020-11-01")
MONTHS = pd.date_range("2022-08-01", "2025-12-01", freq="MS")


def fred():
    f = D["data"] / "fred_series.csv"
    if f.exists():
        return pd.read_csv(f, index_col=0, parse_dates=True)
    out = {}
    for k, sid in FRED.items():
        d = pd.read_csv(io.StringIO(requests.get(f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={sid}", timeout=60).text))
        d.columns = ["date", k]
        out[k] = d.set_index(pd.to_datetime(d["date"]))[k].apply(pd.to_numeric, errors="coerce")
    df = pd.DataFrame(out)
    df.to_csv(f)
    return df


def pn(idx, base, base_override=None, lag=2):
    vals = []
    for t in MONTHS:
        tl = t - pd.DateOffset(months=lag)
        s = W["a"]
        for k, w in W.items():
            if k == "a":
                continue
            b = (base_override or {}).get(k, idx[k].get(base))
            s += w * idx[k].get(tl) / b
        vals.append(s)
    return pd.Series(vals, index=MONTHS)


def main():
    F = fred()
    us = {k: F[k].dropna() for k in "LBCRFME"}
    Lg = pd.read_csv(D["data"] / "ubos_series_legacy.csv", index_col=0, parse_dates=True)
    Md = pd.read_csv(D["data"] / "ubos_series_modern.csv", index_col=0, parse_dates=True)
    ug = {k: series(Lg, Md, k, "high_tensile_steel_bars", "link at Jun 2022") for k in "LBCRFME"}
    res = pd.DataFrame({
        "US BLS (current vintage)": pn(us, BASE_US),
        "US BLS (bid's preliminary base values)": pn(us, BASE_US, BID_BASE),
        "UBOS (Engineer's proposal)": pn(ug, BASE_UG),
    })
    res.to_csv(D["results"] / "kcca_foreign_pn.csv")
    summ = pd.DataFrame({"mean_increase_pct": (res.mean() - 1) * 100, "Dec2025_increase_pct": (res.iloc[-1] - 1) * 100})
    summ.round(2).to_csv(D["results"] / "kcca_summary.csv")
    print(summ.round(2).to_string())
    print("Contractor-reported averages: UBOS 21.89%, BLS 32.19%")

    fig, ax = plt.subplots(figsize=(9, 4))
    for c, col in zip(res.columns, [CAT[0], CAT[6], CAT[1]]):
        ax.plot(res.index, (res[c] - 1) * 100, color=col, lw=1.8, label=c)
    ax.axhline(0, color=INK2, lw=0.8)
    ax.set_ylabel("Price adjustment on the foreign-currency\nportion (% of certified value)")
    ax.set_title("One contract, three index sources for its foreign-currency portion (Project E)", loc="left",
                 fontsize=9.5)
    ax.legend(fontsize=7.5, loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2, frameon=False)
    ax.grid(axis="x", visible=False)
    save(fig, D["figures"], "fig_kcca")


if __name__ == "__main__":
    main()
