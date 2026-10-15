"""Corridor geometries for Paper 2 (shortest road paths between named places in the Geofabrik OSM extract),
cut into 1 km sections with a right-of-way buffer.

  A_lot3  Masindi -> towards Butiaba, truncated at 43 km (Project A, Masindi-Biiso lot)
  A_lot4  Kabaale -> Kiziranfumbi (Project A, Kabaale-Kiziranfumbi lot)
  B       Busunju -> Kiboga -> Hoima (Project B, 145 km rehabilitation)
Outputs: data/corridors.gpkg (layers: lines, sections)
"""
from pathlib import Path

import geopandas as gpd
import networkx as nx
from shapely.geometry import LineString, Point
from shapely.ops import linemerge, substring

D = Path(__file__).resolve().parents[1] / "data"
PBF = Path.home() / "Projects" / "uganda-trade-corridors" / "data" / "uganda-latest.osm.pbf"
PLACES = {"Masindi": (31.72059, 1.68525), "Butiaba": (31.32676, 1.81842), "Kabaale": (31.04528, 1.47417),
          "Kiziranfumbi": (31.20941, 1.32215), "Busunju": (32.20551, 0.56512), "Kiboga": (31.76683, 0.91557),
          "Hoima": (31.35251, 1.43098)}
ROUTES = {"A_lot3": (["Masindi", "Butiaba"], 43_000), "A_lot4": (["Kabaale", "Kiziranfumbi"], None),
          "B": (["Busunju", "Kiboga", "Hoima"], None)}
COST = {"trunk": 1.0, "primary": 1.0, "secondary": 1.0, "tertiary": 1.3, "unclassified": 2.0,
        "trunk_link": 1.0, "primary_link": 1.0, "secondary_link": 1.0}
UTM = "EPSG:32636"
ROW_HALF_WIDTH = 30  # m, each side of the centreline


def graph(roads):
    G = nx.Graph()
    for geom, hw in zip(roads.geometry, roads.highway):
        coords = list(geom.coords)
        for a, b in zip(coords[:-1], coords[1:]):
            L = Point(a).distance(Point(b))
            G.add_edge(a, b, w=L * COST.get(hw, 3.0), L=L)
    return G


def nearest(G, xy):
    return min(G.nodes, key=lambda n: (n[0] - xy[0]) ** 2 + (n[1] - xy[1]) ** 2)


def main():
    roads = gpd.read_file(PBF, layer="lines", bbox=(30.8, 0.4, 32.4, 2.0),
                          where="highway IN ('trunk','primary','secondary','tertiary','unclassified','trunk_link','primary_link','secondary_link')")
    roads = roads.to_crs(UTM)
    G = graph(roads)
    places = gpd.GeoSeries([Point(v) for v in PLACES.values()], index=PLACES.keys(), crs=4326).to_crs(UTM)
    lines, sections = [], []
    for code, (stops, trunc) in ROUTES.items():
        path = []
        for s, e in zip(stops[:-1], stops[1:]):
            p = nx.shortest_path(G, nearest(G, places[s].coords[0]), nearest(G, places[e].coords[0]), weight="w")
            path += p if not path else p[1:]
        line = LineString(path)
        if trunc:
            line = substring(line, 0, min(trunc, line.length))
        lines.append({"corridor": code, "length_km": line.length / 1000, "geometry": line})
        n = int(line.length // 1000) + 1
        for i in range(n):
            seg = substring(line, i * 1000, min((i + 1) * 1000, line.length))
            sections.append({"corridor": code, "section": i, "chainage_km": i, "geometry": seg.buffer(ROW_HALF_WIDTH, cap_style=2)})
        print(code, f"{line.length / 1000:.1f} km, {n} sections")
    gpd.GeoDataFrame(lines, crs=UTM).to_file(D / "corridors.gpkg", layer="lines", driver="GPKG")
    gpd.GeoDataFrame(sections, crs=UTM).to_file(D / "corridors.gpkg", layer="sections", driver="GPKG")


if __name__ == "__main__":
    main()
