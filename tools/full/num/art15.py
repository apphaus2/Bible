"""New drawings for Numbers chapter 15 (Numbers 32–33): Gilead, a land for cattle, with the flocks of Reuben and Gad;
sheepfolds and fortified cities; a map of the land beyond Jordan; and the journeys of the children of Israel from Rameses
to the plains of Moab — a long route map lit section by section, and a "station" cell for each encampment."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus5 as V, samuel1 as S1, numbers1 as N
from genesis.art2 import fit, ground, hills
from genesis.art3 import sun, label, man, grid_bg, node, route
from exo import art as A, art8 as B8
from num.art import ALL, TRIBE_C
def f(v): return f"{v:.1f}"
CY = B8.CY

def gilead(p, w, h, seed, folds=False):
    """The land of Jazer and of Gilead, a place for cattle: green uplands thick with flocks and herds (folds=True: stone
    sheepfolds and a walled town being built)."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), sun(w * 0.86, h * 0.16, 14, op=0.25), hills(w, h, h * 0.4, seed, color="#4A7A3A", amp=20, step=80),
         hills(w, h, h * 0.52, seed + 1, color="#6A9A4A", amp=14), ground(w, h, h * 0.62, "#8AAA5A", dy=0)]
    for i in range(22):
        x = r.uniform(0, w); y = r.uniform(h * 0.64, h * 0.96); s = 0.1 + 0.18 * (y - h * 0.6) / (h * 0.4)
        o.append(E.sheep(x, y, s * 1.1) if i % 3 else S1.cow(x, y, s * 0.6, color=r.choice(["#8A5A30", "#5A3A22", "#C9A27A"]), patch="#E8E2D6"))
    if folds:
        for k in range(2):
            cx = w * (0.2 + k * 0.5); cy = h * 0.6
            o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(w * 0.12)}" ry="{f(h * 0.05)}" fill="none" stroke="#A89E92" stroke-width="{f(h * 0.02)}" stroke-dasharray="6 3"></ellipse>')
        o.append(f'<rect x="{f(w * 0.72)}" y="{f(h * 0.34)}" width="{f(w * 0.22)}" height="{f(h * 0.12)}" fill="#B8A88A" stroke="#0D0D0F" stroke-width="2"></rect>'
                 + "".join(f'<rect x="{f(w * 0.72 + i * w * 0.028)}" y="{f(h * 0.31)}" width="{f(w * 0.016)}" height="{f(h * 0.03)}" fill="#B8A88A" stroke="#0D0D0F" stroke-width="1.2"></rect>' for i in range(8)))
    return "".join(o)

def beyond_jordan(w, h, hi=None):
    """The land beyond the Jordan eastward: Gad, Reuben and the half-tribe of Manasseh, with the cities they built."""
    o = [grid_bg(w, h)]
    jx = w * 0.3
    o.append(f'<path d="M{f(jx)} -10 C {f(jx - 10)} {f(h * 0.3)} {f(jx + 10)} {f(h * 0.6)} {f(jx)} {f(h * 0.82)}" fill="none" stroke="#8FD0E2" stroke-width="4"></path>'
             f'<ellipse cx="{f(jx)}" cy="{f(h * 0.9)}" rx="{f(w * 0.03)}" ry="{f(h * 0.08)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></ellipse>' + label(jx - 10, h * 0.4, "JORDAN", "#8FD0E2", 8, "end"))
    regions = [("MANASSEH · GILEAD · BASHAN", 0.04, 0.42, TRIBE_C["MANASSEH"]), ("GAD", 0.42, 0.66, TRIBE_C["GAD"]), ("REUBEN", 0.66, 0.92, TRIBE_C["REUBEN"])]
    for nm, y0, y1, c in regions:
        on = hi is None or any(k in nm for k in hi)
        o.append(f'<rect x="{f(jx + 16)}" y="{f(h * y0)}" width="{f(w * 0.62)}" height="{f(h * (y1 - y0) - 6)}" fill="{c}" opacity="{0.55 if on else 0.15}" stroke="{c}" stroke-width="2"></rect>'
                 + label(jx + 26, h * y0 + 16, nm, "#F3EFE6", 10, "start", ls=0.12))
    cities = {"GAD": [("DIBON", 0.5, 0.6), ("ATAROTH", 0.58, 0.5), ("AROER", 0.72, 0.62), ("JAZER", 0.46, 0.48), ("BETH-NIMRAH", 0.38, 0.56), ("JOGBEHAH", 0.66, 0.46)],
              "REUBEN": [("HESHBON", 0.48, 0.74), ("ELEALEH", 0.6, 0.72), ("KIRIATHAIM", 0.72, 0.82), ("NEBO", 0.4, 0.84), ("BAAL-MEON", 0.56, 0.86)],
              "MANASSEH": [("GILEAD", 0.5, 0.24), ("HAVVOTH-JAIR", 0.66, 0.16), ("KENATH · NOBAH", 0.82, 0.3)]}
    for k, cs in cities.items():
        on = hi is None or k in hi
        for nm, x, y in cs: o.append(node(w * x, h * y, nm, "#FFD23F" if on else "#6A7A8A", r=3.5, dy=-7, size=7.5))
    return "".join(o)

# the stations of Numbers 33, as (name, x, y) on a 1 x 1 map: Egypt at the left, the sea, Sinai at the bottom, Kadesh, Edom,
# up the east side to the plains of Moab
STATIONS = [("RAMESES", 0.04, 0.42), ("SUCCOTH", 0.1, 0.44), ("ETHAM", 0.15, 0.46), ("PI-HAHIROTH", 0.19, 0.52), ("MARAH", 0.27, 0.58),
            ("ELIM", 0.29, 0.64), ("BY THE RED SEA", 0.27, 0.72), ("WILDERNESS OF SIN", 0.3, 0.78), ("DOPHKAH", 0.33, 0.83), ("ALUSH", 0.36, 0.86),
            ("REPHIDIM", 0.38, 0.9), ("SINAI", 0.42, 0.95), ("KIBROTH-HATTAAVAH", 0.45, 0.88), ("HAZEROTH", 0.47, 0.82), ("RITHMAH", 0.49, 0.76),
            ("RIMMON-PEREZ", 0.5, 0.7), ("LIBNAH", 0.51, 0.64), ("RISSAH", 0.53, 0.6), ("KEHELATHAH", 0.55, 0.64), ("MOUNT SHEPHER", 0.57, 0.68),
            ("HARADAH", 0.58, 0.73), ("MAKHELOTH", 0.6, 0.77), ("TAHATH", 0.62, 0.8), ("TERAH", 0.63, 0.84), ("MITHKAH", 0.65, 0.87),
            ("HASHMONAH", 0.67, 0.84), ("MOSEROTH", 0.68, 0.8), ("BENE-JAAKAN", 0.7, 0.84), ("HOR-HAGGIDGAD", 0.72, 0.88), ("JOTBATHAH", 0.73, 0.92),
            ("ABRONAH", 0.75, 0.94), ("EZION-GEBER", 0.78, 0.96), ("KADESH", 0.62, 0.5), ("MOUNT HOR", 0.7, 0.54), ("ZALMONAH", 0.76, 0.5),
            ("PUNON", 0.8, 0.46), ("OBOTH", 0.84, 0.42), ("IYE-ABARIM", 0.86, 0.36), ("DIBON-GAD", 0.86, 0.3), ("ALMON-DIBLATHAIM", 0.86, 0.24),
            ("ABARIM", 0.84, 0.18), ("PLAINS OF MOAB", 0.8, 0.12)]

def stations_map(w, h, lit=None, title="THE JOURNEYS OF THE CHILDREN OF ISRAEL · NUMBERS 33"):
    """The whole route; lit = (first, last) indexes of the stations to light (the rest dim)."""
    o = [grid_bg(w, h), label(14, 18, title, "#FFD23F", 10, "start", ls=0.16)]
    o.append(f'<path d="M{f(w * 0.2)} {f(h * 0.5)} L {f(w * 0.24)} {f(h * 0.62)} L {f(w * 0.28)} {f(h * 1.0)}" fill="none" stroke="#2C9DB8" stroke-width="{f(max(4, w * 0.012))}" opacity="0.7"></path>')
    o.append(f'<path d="M{f(w * 0.66)} {f(h * 0.62)} L {f(w * 0.78)} {f(h * 1.0)}" fill="none" stroke="#2C9DB8" stroke-width="{f(max(3, w * 0.008))}" opacity="0.6"></path>')
    o.append(f'<path d="M{f(w * 0.76)} {f(h * 0.0)} C {f(w * 0.74)} {f(h * 0.1)} {f(w * 0.76)} {f(h * 0.14)} {f(w * 0.75)} {f(h * 0.2)}" fill="none" stroke="#8FD0E2" stroke-width="3"></path>')
    a, b = lit if lit else (0, len(STATIONS) - 1)
    P = [(w * x, h * y) for _, x, y in STATIONS]
    o.append(route(P, color="#4A5A6A", arrow=False))
    o.append(route(P[a:b + 1], color="#FFD23F", arrow=True) if b > a else "")
    for i, (nm, x, y) in enumerate(STATIONS):
        on = a <= i <= b
        o.append(node(w * x, h * y, nm if on else "", "#FFD23F" if on else "#4A5A6A", r=3 if not on else 4, dy=-7 if i % 2 else 13, size=7))
    return "".join(o)

def station(name, text, ref, accent="#FFD23F", size=12):
    """One encampment: its name over the verse (the verse in full)."""
    return (f'\n    <div style="position: relative; min-height: 0; overflow: hidden; border: 3px solid #0D0D0F; background: #0B1A2E; color: #F3EFE6; padding: 8px 11px 9px; display: flex; flex-direction: column; gap: 4px; box-shadow: inset 0 3px 0 {accent}">'
            f'\n      <div style="display: flex; justify-content: space-between; align-items: baseline; gap: 6px"><span data-label style="font-family: Anton, sans-serif; font-size: 18px; line-height: 1.05; letter-spacing: 0.04em; color: {accent}">{name}</span>'
            f'<span data-label style="font-size: 8.5px; font-weight: 600; letter-spacing: 0.16em; white-space: nowrap; opacity: 0.8">{ref}</span></div>'
            f'\n      <div style="font-size: {size}px; font-weight: 600; line-height: 1.4; letter-spacing: 0.03em; text-transform: uppercase">{text}</div>\n    </div>')

from faces_ex import F
GADITE = F("adam", skin="#B98A6E", shadow="#5A3A2A", hair="#3A2A1E", hl="#6A5A4E", beard=True, beard_color="#3A2A1E", scarf="#E87A2A", cord=True, light="#FFC14D")
