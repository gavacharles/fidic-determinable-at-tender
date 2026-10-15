"""HydroRIVERS v1.0 (Africa) clipped to Uganda (+0.5 deg) for flood and culvert-washout analysis."""
import io
import zipfile
from pathlib import Path

import geopandas as gpd
import requests

OUT = Path(__file__).resolve().parents[1] / "data" / "raw"
URL = "https://data.hydrosheds.org/file/HydroRIVERS/HydroRIVERS_v10_af_shp.zip"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    dest = OUT / "hydrorivers_uganda.gpkg"
    if dest.exists():
        return
    z = zipfile.ZipFile(io.BytesIO(requests.get(URL, timeout=1200).content))
    tmp = OUT / "hr"
    z.extractall(tmp)
    shp = next(tmp.rglob("*.shp"))
    g = gpd.read_file(shp, bbox=(29.0, -2.0, 35.5, 4.8))
    g.to_file(dest, driver="GPKG")
    print("rivers", len(g))


if __name__ == "__main__":
    main()
