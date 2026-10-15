"""SoilGrids 2.0 (ISRIC) clips for Uganda via WCS: clay, sand, silt, bulk density, CEC at 0-5, 15-30, 60-100 cm."""
from pathlib import Path

import requests

OUT = Path(__file__).resolve().parents[1] / "data" / "raw" / "soilgrids"
BBOX = (29.5, -1.5, 35.0, 4.3)
PROPS = ["clay", "sand", "silt", "bdod", "cec"]
DEPTHS = ["0-5cm", "15-30cm", "60-100cm"]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for p in PROPS:
        for d in DEPTHS:
            dest = OUT / f"{p}_{d}_mean.tif"
            if dest.exists():
                continue
            params = [("map", f"/map/{p}.map"), ("SERVICE", "WCS"), ("VERSION", "2.0.1"), ("REQUEST", "GetCoverage"),
                      ("COVERAGEID", f"{p}_{d}_mean"), ("FORMAT", "GEOTIFF_INT16"),
                      ("SUBSET", f"long({BBOX[0]},{BBOX[2]})"), ("SUBSET", f"lat({BBOX[1]},{BBOX[3]})"),
                      ("SUBSETTINGCRS", "http://www.opengis.net/def/crs/EPSG/0/4326"),
                      ("OUTPUTCRS", "http://www.opengis.net/def/crs/EPSG/0/4326")]
            r = requests.get("https://maps.isric.org/mapserv", params=params, timeout=600)
            if r.ok and r.content[:2] in (b"II", b"MM"):
                dest.write_bytes(r.content)
                print("ok", dest.name, len(r.content) // 1e6, "MB", flush=True)
            else:
                print("fail", dest.name, r.status_code, r.text[:200], flush=True)


if __name__ == "__main__":
    main()
