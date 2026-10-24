"""The map of Acts: one projection of the Mediterranean and the lands about it, from Rome to Parthia, as a technical map.

    med_map(w, h, box=(lon0, lon1, lat0, lat1), places=("JERUSALEM", ...), routes=[("JERUSALEM", "JOPPA")], hi=("JOPPA",),
            regions=("JUDÆA", ...), title="…")

Coastlines are traced by hand in longitude and latitude (rough, but in the right places); places and regions are named in
PLACES / REGIONS. A route is a list of place names or (lon, lat) points; routes are drawn in gold (the last one lit red
with red=True). Everything is scaled to fit the panel, centred."""
import math
from genesis.art3 import grid_bg, node, route, label as _label
import zlib

def label(x, y, text, color="#F3EFE6", size=11, anchor="middle", weight=600, ls=0.14):
    """A map label with a dark halo (the map's sea colour) so it reads over coastlines and routes."""
    return _label(x, y, text, color, size, anchor, weight, ls).replace("<text ", '<text stroke="#0B1A2E" stroke-width="3" paint-order="stroke" stroke-linejoin="round" ', 1)
def f(v): return f"{v:.1f}"

LAND = [(-20, 60), (-20, 36.1), (-5.6, 36.05), (-4.4, 36.7), (-2.0, 36.75), (-0.8, 37.6), (-0.5, 38.3), (0.2, 38.8), (-0.3, 39.4), (0.0, 39.9),
        (0.9, 41.0), (2.2, 41.4), (3.2, 42.0), (3.1, 43.0), (4.0, 43.5), (5, 43.3), (7.0, 43.5), (7.5, 43.8), (8.8, 44.4), (9.8, 44.07), (10.25, 43.6), (10.5, 42.95), (11.1, 42.4), (11.8, 42.1),
        (12.25, 41.75), (12.6, 41.45), (13.2, 41.27), (13.6, 41.22), (14.05, 40.83), (14.35, 40.6), (14.75, 40.65), (15.0, 40.3), (15.6, 40.05),
        (15.8, 39.6), (16.05, 39.0), (15.7, 38.6), (15.65, 38.1), (15.75, 37.92), (16.1, 37.92), (16.55, 38.4), (17.15, 38.95), (16.55, 39.65),
        (17.0, 40.45), (18.0, 40.0), (18.5, 40.15), (18.0, 40.65), (16.9, 41.15), (16.0, 41.45), (15.95, 41.9), (14.7, 42.1), (13.9, 42.8),
        (13.6, 43.55), (12.6, 44.0), (12.3, 44.5), (12.3, 45.3), (12.9, 45.65), (13.75, 45.65), (13.9, 44.8), (14.5, 45.3), (15.2, 44.3),
        (15.9, 43.5), (17.0, 43.1), (18.1, 42.65), (18.7, 42.3), (19.3, 41.9), (19.5, 41.3), (19.4, 40.4), (20.0, 39.7), (20.6, 39.1),
        (20.9, 38.8), (21.1, 38.4), (21.4, 38.2), (21.3, 37.9), (21.6, 37.6), (21.7, 37.0), (21.9, 36.8), (22.4, 36.4), (22.5, 36.9),
        (22.75, 36.45), (23.2, 36.45), (23.05, 36.9), (22.75, 37.55), (23.15, 37.45), (23.4, 37.4), (23.0, 37.85), (23.5, 38.0), (23.7, 37.8),
        (24.05, 37.65), (24.05, 38.1), (23.6, 38.45), (22.9, 38.9), (23.1, 39.3), (22.6, 40.0), (22.6, 40.5), (22.95, 40.62), (23.3, 40.2),
        (23.7, 40.0), (24.0, 40.4), (23.85, 40.75), (24.4, 40.92), (25.2, 40.95), (26.0, 40.75), (26.6, 40.6), (26.2, 40.05), (26.15, 39.75),
        (26.1, 39.45), (26.9, 39.5), (26.65, 39.3), (26.95, 38.95), (26.75, 38.65), (26.3, 38.6), (26.55, 38.3), (26.85, 38.1), (27.2, 37.95),
        (27.1, 37.65), (27.25, 37.5), (27.6, 37.3), (27.25, 37.05), (27.4, 36.95), (27.35, 36.7), (28.0, 36.8), (28.3, 36.6), (28.9, 36.65),
        (29.1, 36.2), (29.3, 36.25), (29.95, 36.2), (30.45, 36.25), (30.55, 36.8), (30.7, 36.88), (31.4, 36.75), (32.0, 36.5), (32.6, 36.1),
        (33.3, 36.15), (34.0, 36.3), (34.6, 36.75), (35.6, 36.6), (36.15, 36.85), (35.8, 36.3), (35.95, 36.0), (35.85, 35.6), (35.9, 35.2),
        (35.65, 34.5), (35.35, 33.6), (35.2, 33.27), (35.07, 32.93), (34.95, 32.6), (34.88, 32.45), (34.75, 32.05), (34.5, 31.6), (34.2, 31.3),
        (33.6, 31.15), (32.6, 31.05), (32.3, 31.25), (31.8, 31.5), (31.0, 31.6), (30.3, 31.5), (29.9, 31.2), (29.0, 30.85), (28.0, 31.1),
        (27.0, 31.4), (25.2, 31.6), (24.0, 32.0), (23.1, 32.6), (22.0, 32.9), (21.0, 32.8), (20.1, 32.2), (19.9, 31.3), (19.0, 30.3),
        (18.0, 30.8), (16.6, 31.2), (15.4, 31.9), (15.2, 32.4), (13.2, 32.9), (11.5, 33.1), (10.9, 33.6), (10.1, 34.3), (11.1, 35.2),
        (10.4, 36.7), (11.05, 37.05), (10.2, 37.2), (9.8, 37.35), (8.6, 36.95), (7.75, 36.9), (5.0, 36.8), (3.0, 36.8), (1.4, 36.5),
        (0.1, 35.9), (-1.0, 35.7), (-2.9, 35.3), (-5.3, 35.9), (-20, 35.9), (-20, -10), (90, -10), (90, 60)]
ISLANDS = {
    "SICILY": [(12.45, 37.8), (13.3, 38.2), (14.3, 38.0), (15.65, 38.27), (15.2, 37.6), (15.3, 37.05), (15.1, 36.68), (14.4, 36.75), (13.1, 37.5)],
    "MELITA": [(14.2, 36.05), (14.55, 35.98), (14.6, 35.8), (14.3, 35.88)],
    "CRETE": [(23.55, 35.65), (24.2, 35.55), (25.0, 35.43), (25.75, 35.33), (26.3, 35.3), (26.15, 35.0), (25.5, 34.98), (24.75, 34.93), (24.1, 35.15), (23.55, 35.25)],
    "CYPRUS": [(32.3, 34.9), (32.4, 35.1), (32.9, 35.2), (33.9, 35.4), (34.6, 35.7), (34.0, 35.1), (33.9, 34.95), (33.0, 34.6), (32.4, 34.7)],
    "RHODES": [(27.7, 36.15), (28.2, 36.45), (28.25, 36.3), (27.75, 35.9)],
    "LESBOS": [(25.85, 39.15), (26.15, 39.38), (26.6, 39.3), (26.45, 39.0), (26.0, 39.0)],
    "CHIOS": [(25.85, 38.55), (26.15, 38.55), (26.1, 38.25), (25.95, 38.2)],
    "SAMOS": [(26.55, 37.8), (27.05, 37.75), (26.95, 37.65), (26.6, 37.68)],
    "COS": [(26.95, 36.85), (27.35, 36.9), (27.15, 36.75)],
    "SAMOTHRACE": [(25.4, 40.48), (25.7, 40.52), (25.65, 40.38), (25.45, 40.4)],
    "EUBOEA": [(22.85, 38.85), (23.4, 38.95), (24.6, 38.15), (24.5, 37.98), (23.6, 38.4), (22.9, 38.7)],
    "CAUDA": [(23.98, 34.88), (24.15, 34.88), (24.12, 34.8), (24.0, 34.8)],
    "SARDINIA": [(8.4, 39.0), (9.6, 39.1), (9.8, 40.9), (9.2, 41.25), (8.2, 40.9), (8.4, 39.9)],
    "CORSICA": [(8.6, 41.4), (9.4, 41.4), (9.5, 42.9), (8.6, 42.4)],
}
WATERS = [
    [(28.0, 41.6), (28.0, 43.3), (28.6, 44.3), (29.7, 45.2), (30.7, 46.5), (31.8, 46.6), (33.6, 46.1), (32.5, 45.4), (33.5, 44.5), (34.5, 44.8),
     (36.4, 45.3), (37.5, 44.7), (38.7, 44.3), (39.7, 43.5), (41.6, 41.6), (40.5, 41.0), (38.4, 40.9), (36.5, 41.3), (35.2, 42.0), (34.0, 41.95),
     (32.3, 41.7), (31.2, 41.1), (29.1, 41.2)],                                                         # the Black Sea
    [(26.7, 40.4), (27.5, 40.95), (29.0, 41.0), (29.9, 40.7), (28.9, 40.4), (27.5, 40.35)],               # Marmara
    [(21.2, 38.3), (22.0, 38.4), (22.9, 38.0), (22.3, 38.1), (21.6, 38.15)],                             # the gulf of Corinth
    [(47, 44.5), (49, 46.6), (51, 46.0), (53, 45), (51.3, 43.1), (50.5, 41), (53, 40.0), (54, 37.4), (53.6, 36.8), (51.5, 36.8), (50, 37.4),
     (49, 38.4), (49.3, 40.3), (48.6, 41.8), (47.5, 43)],                                                # the Caspian
    [(32.55, 29.95), (32.7, 29.6), (33.6, 27.8), (34.25, 27.75), (34.45, 28.1), (34.95, 29.55), (35.0, 29.45), (34.6, 28.0), (35.5, 27.0), (38.0, 24.0),
     (39.5, 21.0), (41, 17), (43.3, 12.6), (42.6, 12.5), (40, 15), (38, 18), (36.5, 22), (35.5, 23.8), (34, 26), (33.0, 27.5), (32.4, 29.5)],  # the Red Sea
    [(47.9, 30.0), (48.8, 29.9), (50, 29.2), (51.5, 27.9), (54, 26.5), (56.3, 26.8), (56.5, 24), (48, 24)],  # the Persian gulf
    [(35.5, 32.9), (35.65, 32.88), (35.62, 32.7), (35.55, 32.7)],                                        # the sea of Galilee
    [(35.4, 31.78), (35.58, 31.75), (35.5, 31.1), (35.38, 31.25)],                                       # the Salt Sea
]
RIVERS = [[(38.0, 37.3), (38.5, 36.0), (40, 35.2), (41.5, 34.2), (43.5, 32.5), (45.5, 31.2), (47.0, 30.8), (48.0, 30.0)],
          [(40.2, 37.9), (42.6, 37.0), (43.2, 36.3), (43.5, 35.0), (44.4, 33.3), (46.0, 32.3), (47.2, 31.0)],
          [(31.2, 31.5), (31.0, 30.1), (31.3, 27.0), (32.9, 24.1)],
          [(35.6, 33.2), (35.6, 32.9)], [(35.57, 32.7), (35.55, 32.3), (35.55, 31.78)]]

PLACES = {
    "JERUSALEM": (35.23, 31.78), "ROME": (12.5, 41.9), "ANTIOCH": (36.16, 36.2), "DAMASCUS": (36.3, 33.51), "CÆSAREA": (34.89, 32.5),
    "JOPPA": (34.75, 32.05), "LYDDA": (34.9, 31.95), "SAMARIA": (35.19, 32.28), "GAZA": (34.45, 31.5), "AZOTUS": (34.65, 31.8),
    "TARSUS": (34.9, 36.92), "SELEUCIA": (35.93, 36.12), "SALAMIS": (33.9, 35.18), "PAPHOS": (32.42, 34.76), "PERGA": (30.85, 36.96),
    "ATTALIA": (30.7, 36.89), "ANTIOCH OF PISIDIA": (31.19, 38.3), "ICONIUM": (32.49, 37.87), "LYSTRA": (32.33, 37.58), "DERBE": (33.36, 37.35),
    "TROAS": (26.15, 39.75), "NEAPOLIS": (24.4, 40.94), "PHILIPPI": (24.29, 41.01), "AMPHIPOLIS": (23.84, 40.82), "APOLLONIA": (23.47, 40.62),
    "THESSALONICA": (22.95, 40.64), "BERŒA": (22.2, 40.52), "ATHENS": (23.73, 37.98), "CORINTH": (22.88, 37.91), "CENCHREÆ": (22.99, 37.88),
    "EPHESUS": (27.34, 37.94), "MILETUS": (27.28, 37.53), "COS": (27.15, 36.85), "RHODES": (28.22, 36.43), "PATARA": (29.32, 36.26),
    "TYRE": (35.2, 33.27), "PTOLEMAIS": (35.07, 32.93), "SIDON": (35.37, 33.56), "MYRA": (29.98, 36.26), "CNIDUS": (27.37, 36.69),
    "SALMONE": (26.3, 35.28), "FAIR HAVENS": (24.8, 34.95), "PHŒNIX": (24.1, 35.2), "CAUDA": (24.07, 34.84), "MELITA": (14.4, 35.92),
    "SYRACUSE": (15.29, 37.07), "RHEGIUM": (15.65, 38.11), "PUTEOLI": (14.1, 40.83), "MARKET OF APPIUS": (13.1, 41.45), "THREE TAVERNS": (12.85, 41.62),
    "MITYLENE": (26.55, 39.1), "CHIOS": (26.0, 38.4), "SAMOS": (26.8, 37.72), "ASSOS": (26.34, 39.49), "SAMOTHRACE": (25.55, 40.45),
    "ALEXANDRIA": (29.92, 31.2), "CYRENE": (21.85, 32.82), "ANTIPATRIS": (34.93, 32.1), "PHŒNICIA": (35.4, 33.9), "TROGYLLIUM": (27.1, 37.66),
    "UR": (46.1, 30.96), "HARAN": (39.03, 36.87), "SHECHEM": (35.28, 32.21), "MOUNT SINAI": (33.97, 28.54), "MEMPHIS": (31.25, 29.85),
}
REGIONS = {
    "JUDÆA": (35.0, 31.5), "SAMARIA": (35.3, 32.3), "GALILEE": (35.35, 32.85), "SYRIA": (37.2, 34.8), "CILICIA": (35.0, 37.3),
    "CYPRUS": (33.2, 35.0), "PAMPHYLIA": (31.0, 37.25), "PISIDIA": (30.9, 37.85), "LYCAONIA": (33.0, 38.0), "GALATIA": (32.6, 39.5),
    "PHRYGIA": (30.2, 38.7), "ASIA": (28.0, 38.6), "MYSIA": (27.4, 39.6), "BITHYNIA": (30.4, 40.5), "PONTUS": (36.0, 40.6),
    "CAPPADOCIA": (35.5, 38.9), "MACEDONIA": (22.4, 41.0), "ACHAIA": (22.2, 37.6), "ITALY": (14.2, 42.0), "EGYPT": (30.5, 29.0),
    "LIBYA": (23.5, 30.6), "CRETE": (24.9, 35.2), "ARABIA": (38.5, 29.5), "MESOPOTAMIA": (41.5, 36.0), "MEDIA": (48.0, 35.5),
    "PARTHIA": (55.0, 36.5), "ELAM": (48.5, 32.0), "LYCIA": (29.6, 36.6), "SICILY": (14.2, 37.45), "MELITA": (14.4, 35.6),
    "THE GREAT SEA": (19.0, 34.6), "ADRIA": (18.0, 37.2), "ARABIA ": (44.0, 27.0),
    "CANAAN": (36.7, 30.5), "MIDIAN": (35.9, 27.6), "CHALDÆA": (45.0, 31.9),
}

class Proj:
    def __init__(self, w, h, box, pad=0.04):
        lon0, lon1, lat0, lat1 = box
        self.k = math.cos(math.radians((lat0 + lat1) / 2))
        sx = w * (1 - 2 * pad) / ((lon1 - lon0) * self.k); sy = h * (1 - 2 * pad) / (lat1 - lat0)
        self.s = min(sx, sy)
        self.cx, self.cy = (lon0 + lon1) / 2, (lat0 + lat1) / 2
        self.w, self.h = w, h
    def __call__(self, lon, lat):
        return self.w / 2 + (lon - self.cx) * self.k * self.s, self.h / 2 - (lat - self.cy) * self.s
    def pt(self, p):
        return self(*(PLACES[p] if isinstance(p, str) else p))

def _poly(P, pts, fill, stroke, sw=1.6):
    return f'<path d="M' + " L ".join(f"{f(x)} {f(y)}" for x, y in (P(*q) for q in pts)) + f' Z" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"></path>'

SEA, LANDC, COAST = "#0B1A2E", "#1C2C34", "#8FD0E2"

# where a place's name goes when the default (centred above the dot) would crowd a neighbour: (dx, dy, anchor)
LABEL_AT = {"CENCHREÆ": (8, 12, "start"), "CORINTH": (-8, -8, "end"), "ATHENS": (8, -6, "start"), "PERGA": (8, -6, "start"), "ATTALIA": (-8, 12, "end"),
            "LYSTRA": (8, 12, "start"), "ICONIUM": (8, -6, "start"), "DERBE": (8, 4, "start"), "SELEUCIA": (-8, 12, "end"), "ANTIOCH": (8, -6, "start"),
            "TARSUS": (-6, -8, "end"), "PTOLEMAIS": (8, 4, "start"), "TYRE": (8, 4, "start"), "SIDON": (8, 4, "start"), "CÆSAREA": (-8, 4, "end"),
            "JOPPA": (-8, 4, "end"), "LYDDA": (8, 10, "start"), "JERUSALEM": (8, 12, "start"), "AZOTUS": (-8, 4, "end"), "GAZA": (-8, 6, "end"),
            "SAMARIA": (8, -4, "start"), "ANTIPATRIS": (8, 2, "start"), "DAMASCUS": (8, 4, "start"), "NEAPOLIS": (8, 10, "start"), "PHILIPPI": (0, -10, "middle"),
            "AMPHIPOLIS": (-8, -8, "end"), "APOLLONIA": (0, 16, "middle"), "THESSALONICA": (-8, -6, "end"), "BERŒA": (-8, 4, "end"), "TROAS": (-8, 4, "end"),
            "ASSOS": (8, -4, "start"), "MITYLENE": (8, 4, "start"), "CHIOS": (-8, 4, "end"), "SAMOS": (8, 6, "start"), "EPHESUS": (8, -4, "start"),
            "MILETUS": (8, 6, "start"), "TROGYLLIUM": (8, -4, "start"), "COS": (-8, 6, "end"), "RHODES": (8, 6, "start"), "PATARA": (0, 16, "middle"),
            "MYRA": (0, 16, "middle"), "CNIDUS": (-8, 6, "end"), "SALMONE": (8, 4, "start"), "FAIR HAVENS": (0, 18, "middle"), "PHŒNIX": (-8, 14, "end"),
            "CAUDA": (0, 16, "middle"), "MELITA": (0, 18, "middle"), "SYRACUSE": (8, 6, "start"), "RHEGIUM": (8, 4, "start"), "PUTEOLI": (8, 6, "start"),
            "MARKET OF APPIUS": (8, 8, "start"), "THREE TAVERNS": (8, -2, "start"), "ROME": (-8, -6, "end"), "SAMOTHRACE": (0, -10, "middle"),
            "SALAMIS": (8, 4, "start"), "PAPHOS": (-8, 10, "end"), "ANTIOCH OF PISIDIA": (0, -10, "middle"), "ALEXANDRIA": (0, 16, "middle"),
            "CYRENE": (0, 16, "middle")}

def med_map(w, h, box=(10, 37, 29.5, 43), places=(), routes=(), hi=(), regions=(), title=None, red=False, lit_routes=None, size=9, dots=True,
            ship=None, rsize=None, labels_left=(), rings=None):
    """rings=place: rings spreading out from that place (the witnesses of 1:8); hi= places lit red, the rest gold."""
    P = Proj(w, h, box)
    uid = f"mc{zlib.crc32(repr((box, places, title, w, h)).encode()) % 10 ** 8}"
    o = [f'<defs><clipPath id="{uid}"><rect x="0" y="0" width="{f(w)}" height="{f(h)}"></rect></clipPath></defs><g clip-path="url(#{uid})">',
         grid_bg(w, h, color="#1E3A5A", bg=SEA)]
    o.append(_poly(P, LAND, LANDC, COAST, 1.8))
    for pts in ISLANDS.values(): o.append(_poly(P, pts, LANDC, COAST, 1.4))
    for pts in WATERS: o.append(_poly(P, pts, SEA, COAST, 1.4))
    for r in RIVERS: o.append(f'<path d="M' + " L ".join(f"{f(x)} {f(y)}" for x, y in (P(*q) for q in r)) + f'" fill="none" stroke="{COAST}" stroke-width="1.4" opacity="0.8"></path>')
    if rings:
        x, y = P.pt(rings)
        for k in range(1, 5):
            o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(min(w, h) * 0.12 * k)}" fill="none" stroke="#FF6A4A" stroke-width="1.6" stroke-dasharray="5 6" opacity="{0.8 - 0.15 * k:.2f}"></circle>')
    rs = rsize or max(8, size - 1)
    for nm in regions:                               # a name, or (name, lon, lat[, anchor]) to set it elsewhere
        if isinstance(nm, tuple): nm, lon, lat, *an = nm; x, y = P(lon, lat); an = an[0] if an else "middle"
        else: x, y = P(*REGIONS[nm]); an = "middle"
        o.append(label(x, y, nm.strip(), "#7AAAC8", rs, anchor=an, weight=500, ls=0.3))
    for i, rt in enumerate(routes):
        pts = [P.pt(q) for q in rt]
        lit = (red and i == len(routes) - 1) if lit_routes is None else (i in lit_routes)
        o.append(route(pts, color="#FF6A4A" if lit else "#FFD23F", sw=2.6 if lit else 2.2))
    for nm in places:
        x, y = P.pt(nm)
        c = "#FF6A4A" if nm in hi else "#FFD23F"
        dx, dy, anchor = LABEL_AT.get(nm, (0, -10, "middle"))
        if nm in labels_left: dx, dy, anchor = -10, 4, "end"
        o.append(node(x, y, "", c, r=3.6 if nm not in hi else 5, dy=-10, size=size) + label(x + dx, y + dy, nm, c, size, anchor))
    if ship:
        x, y = P.pt(ship)
        o.append(f'<g transform="translate({f(x)} {f(y)})"><path d="M-12 0 L 12 0 L 8 6 L -8 6 Z" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.2"></path>'
                 '<path d="M0 0 L 0 -18" stroke="#FFD23F" stroke-width="1.6"></path><path d="M-8 -16 L 8 -16 L 6 -4 L -6 -4 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1"></path></g>')
    if title:
        o.append(f'<rect x="10" y="{f(h - 30)}" width="{f(len(title) * 7.4 + 20)}" height="20" fill="#0B1A2E" stroke="#8FD0E2" stroke-width="1.4"></rect>'
                 + label(20, h - 16, title, "#8FD0E2", 10, anchor="start"))
    return "".join(o) + "</g>"
