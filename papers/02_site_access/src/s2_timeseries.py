"""Monthly Sentinel-2 L2A time series of vegetation and bare-soil indices per 1 km right-of-way section.

For each corridor and month (2018-01 .. 2024-12): the two least-cloudy scenes on different MGRS tiles intersecting
the corridor are read (window only, via Microsoft Planetary Computer COGs); clouds, shadows and snow are masked with
the SCL band; per section the median NDVI = (B08-B04)/(B08+B04) and NDBI = (B11-B08)/(B11+B08) are taken from the
scene with the larger valid fraction.
Usage: python s2_timeseries.py A_lot3 [B ...]   Output: data/s2_sections_<corridor>.csv
"""
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import geopandas as gpd
import numpy as np
import pandas as pd
import planetary_computer as pc
import pystac_client
import rasterio
from rasterio.features import rasterize
from rasterio.warp import transform_bounds
from rasterio.windows import from_bounds

D = Path(__file__).resolve().parents[1] / "data"
BAD_SCL = {0, 1, 3, 8, 9, 10, 11}          # no data, saturated, shadow, cloud medium/high, cirrus, snow


def read(href, bounds, crs, out_shape=None):
    with rasterio.open(href) as src:
        b = transform_bounds(crs, src.crs, *bounds)
        win = from_bounds(*b, transform=src.transform).round_offsets().round_lengths()
        arr = src.read(1, window=win, out_shape=out_shape, boundless=True, fill_value=0)
        return arr, src.window_transform(win), src.crs


def scene_stats(item, sections):
    item = pc.sign(item)
    secs = sections.to_crs(item.properties["proj:epsg"] if "proj:epsg" in item.properties else sections.crs)
    bounds = tuple(secs.total_bounds)
    crs = secs.crs
    b04, tr, scrs = read(item.assets["B04"].href, bounds, crs)
    shape = b04.shape
    b08, _, _ = read(item.assets["B08"].href, bounds, crs)
    b11, _, _ = read(item.assets["B11"].href, bounds, crs, out_shape=shape)
    scl, _, _ = read(item.assets["SCL"].href, bounds, crs, out_shape=shape)
    labels = rasterize([(g, i + 1) for i, g in enumerate(secs.to_crs(scrs).geometry)], out_shape=shape, transform=tr,
                       fill=0, dtype="int32")
    b04, b08, b11 = (x.astype("float32") for x in (b04, b08, b11))
    valid = ~np.isin(scl, list(BAD_SCL)) & (b08 > 0)
    ndvi = np.where(valid, (b08 - b04) / np.maximum(b08 + b04, 1), np.nan)
    ndbi = np.where(valid, (b11 - b08) / np.maximum(b11 + b08, 1), np.nan)
    rows = []
    for i, sec in enumerate(sections.section.values):
        m = labels == i + 1
        n = m.sum()
        v = m & valid
        rows.append({"section": sec, "valid_frac": v.sum() / n if n else 0.0,
                     "ndvi": float(np.nanmedian(ndvi[v])) if v.sum() >= 5 else np.nan,
                     "ndbi": float(np.nanmedian(ndbi[v])) if v.sum() >= 5 else np.nan})
    return pd.DataFrame(rows)


def run(code):
    sections = gpd.read_file(D / "corridors.gpkg", layer="sections")
    sections = sections[sections.corridor == code].reset_index(drop=True)
    bbox = list(sections.to_crs(4326).total_bounds)
    cat = pystac_client.Client.open("https://planetarycomputer.microsoft.com/api/stac/v1", modifier=pc.sign_inplace)
    items = list(cat.search(collections=["sentinel-2-l2a"], bbox=bbox, datetime="2018-01-01/2024-12-31",
                            query={"eo:cloud_cover": {"lt": 50}}).items())
    df = pd.DataFrame([{"item": it, "month": it.datetime.strftime("%Y-%m"), "tile": it.properties.get("s2:mgrs_tile"),
                        "cloud": it.properties.get("eo:cloud_cover")} for it in items])
    picks = df.sort_values("cloud").groupby(["month", "tile"]).head(1).groupby("month").head(3)
    print(code, len(items), "items;", picks.month.nunique(), "months;", len(picks), "scenes to read", flush=True)
    out = D / f"s2_sections_{code}.csv"
    done = set(pd.read_csv(out).scene) if out.exists() else set()

    def work(row):
        if row.item.id in done:
            return None
        try:
            s = scene_stats(row.item, sections)
            s["month"], s["scene"], s["tile"], s["cloud"] = row.month, row.item.id, row.tile, row.cloud
            return s
        except Exception as e:                                      # network or asset errors: skip scene
            print("skip", row.item.id, type(e).__name__, flush=True)
            return None

    with ThreadPoolExecutor(6) as ex:
        for k, res in enumerate(ex.map(work, picks.itertuples())):
            if res is not None:
                res.to_csv(out, mode="a", header=not out.exists(), index=False)
            if k % 20 == 0:
                print(code, "scenes", k, flush=True)
    print("done", code, flush=True)


if __name__ == "__main__":
    for c in sys.argv[1:] or ["A_lot3"]:
        run(c)
