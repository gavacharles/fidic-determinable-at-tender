"""Does open soil data (SoilGrids 2.0, 250 m) predict poor subgrade found by site investigation?

Test pits (Project A, Masindi-Biiso) are located by chainage along the corridor centreline (Paper 2 corridor A_lot3,
chainage 0 at Masindi). SoilGrids clay, sand, silt, bulk density and CEC at 15-30 and 60-100 cm are sampled at each pit
and related to PI and soaked CBR95 (Spearman correlation; ROC AUC for CBR95 < 8 %).
Output: results/soil_predictor.csv
"""
import sys
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.style import paper_dir  # noqa: E402

D = paper_dir("03_ground_conditions")
CORR = Path(__file__).resolve().parents[2] / "02_site_access" / "data" / "corridors.gpkg"


def auc(score, y):
    pos, neg = score[y], score[~y]
    if len(pos) == 0 or len(neg) == 0:
        return np.nan
    return (pos.values[:, None] > neg.values[None, :]).mean() + 0.5 * (pos.values[:, None] == neg.values[None, :]).mean()


def main():
    tp = pd.read_csv(D["data"] / "raw" / "testpits_A_lot3.csv").dropna(subset=["CBR95"])
    line = gpd.read_file(CORR, layer="lines").query("corridor == 'A_lot3'").geometry.iloc[0]
    pts = gpd.GeoSeries([line.interpolate(k * 1000) for k in tp.chainage_km], crs="EPSG:32636").to_crs(4326)
    for f in sorted((D["data"] / "raw" / "soilgrids").glob("*_mean.tif")):
        with rasterio.open(f) as src:
            tp[f.stem.replace("_mean", "")] = [v[0] for v in src.sample([(p.x, p.y) for p in pts])]
    poor = tp.CBR95 < 8
    rows = []
    for c in [c for c in tp.columns if any(c.startswith(p) for p in ("clay", "sand", "silt", "bdod", "cec"))]:
        x = tp[c].astype(float)
        if x.nunique() < 3:
            continue
        rows.append({"soilgrids_layer": c, "rho_vs_PI": stats.spearmanr(x, tp.PI).correlation,
                     "rho_vs_CBR95": stats.spearmanr(x, tp.CBR95).correlation,
                     "AUC_poor_CBR95<8": max(auc(x, poor), 1 - auc(x, poor))})
    r = pd.DataFrame(rows).sort_values("AUC_poor_CBR95<8", ascending=False)
    r.round(3).to_csv(D["results"] / "soil_predictor.csv", index=False)
    print(r.round(3).to_string(index=False))
    print("pits", len(tp), "poor", int(poor.sum()))


if __name__ == "__main__":
    main()
