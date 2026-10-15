"""OSM roads around each project corridor (Overpass) and the Sentinel-2 L2A scene catalogue (Planetary Computer).
Project bounding boxes are approximate (anonymised projects A-D; no project documents stored here)."""
import json
from pathlib import Path

import geopandas as gpd
import pystac_client

OUT = Path(__file__).resolve().parents[1] / "data" / "raw"
BOXES = {  # (south, west, north, east)
    "A_lot3": (1.55, 31.30, 1.85, 31.80), "A_lot4": (0.95, 30.90, 1.40, 31.35),
    "B": (0.55, 31.30, 1.50, 32.25), "D": (1.25, 34.35, 1.45, 34.80), "C": (0.18, 32.55, 0.30, 32.65)}
PBF = Path.home() / "Projects" / "uganda-trade-corridors" / "data" / "uganda-latest.osm.pbf"   # Geofabrik extract


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    roads = gpd.read_file(PBF, layer="lines", where="highway IN ('trunk','primary','secondary','tertiary','unclassified','trunk_link','primary_link')")
    for k, (s, w, n, e) in BOXES.items():
        dest = OUT / f"osm_roads_{k}.gpkg"
        if not dest.exists():
            sub = roads.cx[w:e, s:n]
            sub.to_file(dest, driver="GPKG")
            print("osm", k, len(sub), flush=True)
    cat = pystac_client.Client.open("https://planetarycomputer.microsoft.com/api/stac/v1")
    scenes = {}
    for k, (s, w, n, e) in BOXES.items():
        items = cat.search(collections=["sentinel-2-l2a"], bbox=[w, s, e, n], datetime="2017-01-01/2025-12-31",
                           query={"eo:cloud_cover": {"lt": 40}}).item_collection()
        scenes[k] = [{"id": i.id, "date": i.datetime.isoformat(), "cloud": i.properties.get("eo:cloud_cover")} for i in items]
        print("s2", k, len(scenes[k]), flush=True)
    (OUT / "s2_catalogue.json").write_text(json.dumps(scenes, indent=1))


if __name__ == "__main__":
    main()
