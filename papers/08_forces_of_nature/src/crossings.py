"""River crossings of the programme's project roads (HydroRIVERS reaches with >= 10 km2 upstream area crossing the
Paper 2 corridor centrelines), with upstream area, mean discharge and Strahler order.
Outputs: data/crossings.csv (corridor, chainage, lon/lat, upland area, discharge, order)
"""
from pathlib import Path

import geopandas as gpd
import pandas as pd
from shapely.geometry import MultiPoint, Point

D = Path(__file__).resolve().parents[1] / "data"
CORR = Path(__file__).resolve().parents[2] / "02_site_access" / "data" / "corridors.gpkg"
UTM = "EPSG:32636"


def main():
    lines = gpd.read_file(CORR, layer="lines").to_crs(UTM)
    box = tuple(lines.to_crs(4326).total_bounds)
    rivers = gpd.read_file(D / "raw" / "hydrorivers_uganda.gpkg", bbox=box).to_crs(UTM)
    rows = []
    for c in lines.itertuples():
        cand = rivers[rivers.intersects(c.geometry)]
        for r in cand.itertuples():
            x = c.geometry.intersection(r.geometry)
            pts = [x] if isinstance(x, Point) else list(x.geoms) if isinstance(x, MultiPoint) else []
            for p in pts:
                ll = gpd.GeoSeries([p], crs=UTM).to_crs(4326).iloc[0]
                rows.append({"corridor": c.corridor, "chainage_km": round(c.geometry.project(p) / 1000, 2),
                             "lon": round(ll.x, 5), "lat": round(ll.y, 5), "hyriv_id": r.HYRIV_ID,
                             "upland_km2": r.UPLAND_SKM, "dis_av_cms": r.DIS_AV_CMS, "strahler": r.ORD_STRA})
    out = pd.DataFrame(rows).sort_values(["corridor", "chainage_km"])
    out.to_csv(D / "crossings.csv", index=False)
    print(out.groupby("corridor").agg(n=("hyriv_id", "size"), max_area=("upland_km2", "max"),
                                      median_area=("upland_km2", "median")))


if __name__ == "__main__":
    main()
