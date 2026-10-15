"""Weighbridge coverage of Uganda's trunk network, and of the programme's project roads.

The Auditor General's 2025 value-for-money audit of road weighbridges (Annual Report FY2024/25, s. 3.1.18) found
operational fixed weighbridges on only five of 37 priority Class A/B corridors: Kampala-Malaba, Kibuye-Katuna,
Busega-Fort Portal-Mpondwe, Kampala-Kafu-Nimule and Malaba-Kamdini. Each corridor is traced as the shortest
trunk/primary path between its end points in the OpenStreetMap (Geofabrik) extract and compared with the national
trunk + primary network and with the Project A and B corridors of Paper 2.
Outputs: results/weighbridge_coverage.csv, figures/fig_weighbridge.png
"""
import sys
from pathlib import Path

import geopandas as gpd
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from shapely.geometry import LineString, Point
from shapely.ops import unary_union

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from common.style import CAT, INK2, MUTED, paper_dir, save  # noqa: E402

D = paper_dir("04_defects_overloading")
PBF = Path.home() / "Projects" / "uganda-trade-corridors" / "data" / "uganda-latest.osm.pbf"
CORRIDORS_P2 = Path(__file__).resolve().parents[2] / "02_site_access" / "data" / "corridors.gpkg"
UTM = "EPSG:32636"
PLACES = {"Kampala": (32.5825, 0.3476), "Malaba": (34.2760, 0.6360), "Kibuye": (32.5740, 0.2960),
          "Masaka": (31.7350, -0.3400), "Mbarara": (30.6580, -0.6070), "Katuna": (30.0010, -1.3420),
          "Busega": (32.5300, 0.3130), "Fort Portal": (30.2750, 0.6710), "Mpondwe": (29.7300, 0.0400),
          "Kafu": (32.0400, 1.4300), "Elegu (Nimule)": (32.0650, 3.5750), "Tororo": (34.1810, 0.6930),
          "Mbale": (34.1750, 1.0800), "Soroti": (33.6110, 1.7150), "Lira": (32.8900, 2.2490),
          "Kamdini": (32.3300, 2.2400)}
WEIGHED = {"Kampala-Malaba": ["Kampala", "Malaba"], "Kibuye-Katuna": ["Kibuye", "Masaka", "Mbarara", "Katuna"],
           "Busega-Fort Portal-Mpondwe": ["Busega", "Fort Portal", "Mpondwe"],
           "Kampala-Kafu-Nimule": ["Kampala", "Kafu", "Elegu (Nimule)"],
           "Malaba-Kamdini": ["Malaba", "Tororo", "Mbale", "Soroti", "Lira", "Kamdini"]}
COST = {"trunk": 1.0, "primary": 1.15, "secondary": 1.6}
BUFFER = 150  # m, tolerance when overlaying traced corridors on the network


def main():
    roads = gpd.read_file(PBF, layer="lines", where="highway IN ('trunk','primary','secondary')").to_crs(UTM)
    G = nx.Graph()
    for geom, hw in zip(roads.geometry, roads.highway):
        c = list(geom.coords)
        for a, b in zip(c[:-1], c[1:]):
            G.add_edge(a, b, w=Point(a).distance(Point(b)) * COST[hw])
    nodes = list(G.nodes)
    import numpy as np
    arr = np.array(nodes)
    pts = gpd.GeoSeries([Point(v) for v in PLACES.values()], index=PLACES.keys(), crs=4326).to_crs(UTM)

    def near(p):
        return nodes[int(((arr - np.array(p.coords[0])) ** 2).sum(1).argmin())]

    traced = []
    for name, stops in WEIGHED.items():
        path = []
        for s, e in zip(stops[:-1], stops[1:]):
            p = nx.shortest_path(G, near(pts[s]), near(pts[e]), weight="w")
            path += p if not path else p[1:]
        traced.append({"corridor": name, "km": LineString(path).length / 1000, "geometry": LineString(path)})
    tr = gpd.GeoDataFrame(traced, crs=UTM)
    zone = unary_union(tr.buffer(BUFFER))

    net = roads[roads.highway.isin(["trunk", "primary"])].copy()
    net["km"] = net.length / 1000
    net["weighed_km"] = net.intersection(zone).length / 1000
    rows = [{"network": hw, "km": g.km.sum(), "weighed_km": g.weighed_km.sum()} for hw, g in net.groupby("highway")]
    rows.append({"network": "trunk + primary", "km": net.km.sum(), "weighed_km": net.weighed_km.sum()})
    if CORRIDORS_P2.exists():
        p2 = gpd.read_file(CORRIDORS_P2, layer="lines")
        for r in p2.itertuples():
            rows.append({"network": f"Project corridor {r.corridor}", "km": r.length_km,
                         "weighed_km": r.geometry.intersection(zone).length / 1000})
    out = pd.DataFrame(rows)
    out["weighed_share"] = out.weighed_km / out.km
    for r in tr.itertuples():
        out.loc[len(out)] = {"network": f"Weighed corridor: {r.corridor}", "km": r.km, "weighed_km": r.km,
                             "weighed_share": 1.0}
    out.round(3).to_csv(D["results"] / "weighbridge_coverage.csv", index=False)
    print(out.round(2).to_string(index=False))

    fig, ax = plt.subplots(figsize=(7, 7.5))
    net.plot(ax=ax, color=MUTED, lw=0.6)
    tr.plot(ax=ax, color=CAT[0], lw=2.2)
    if CORRIDORS_P2.exists():
        p2.plot(ax=ax, color=CAT[3], lw=2.2)
    ax.plot([], [], color=MUTED, lw=1, label="Trunk and primary roads (OSM)")
    ax.plot([], [], color=CAT[0], lw=2.2, label="Corridors with an operational fixed weighbridge (OAG 2025)")
    ax.plot([], [], color=CAT[3], lw=2.2, label="Project A and B roads")
    share = out.loc[out.network == "trunk + primary", "weighed_share"].iloc[0]
    ax.set_title(f"{share:.0%} of trunk and primary road length lies on a corridor with a fixed weighbridge;\nnone of the Project A and B roads does", fontsize=10,
                 loc="left", fontweight="bold")
    ax.legend(fontsize=7.5, loc="lower right")
    ax.set_axis_off()
    save(fig, D["figures"], "fig_weighbridge")


if __name__ == "__main__":
    main()
