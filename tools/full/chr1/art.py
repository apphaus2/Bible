"""Drawings for the 1 Chronicles volume (chapter by chapter, added below), on top of everything in kg2.art (which carries
kg1.art) and 2 Samuel's drawings (sa2.art as K2): David's story in Chronicles runs alongside 2 Samuel.

The genealogies are technical charts on the blueprint grid: lineage() a line of fathers and sons, branch() a father and his
sons, with the names in the ASV's spelling for this book."""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from kg2.art import *
from kg2.art import f
import sa2.art as K2
import kg2.art as K3
from genesis.art3 import grid_bg, node, route, label

GOLD, CYAN, RED_C = "#FFD23F", "#8FD0E2", "#D7261E"

def lineage(w, h, names, hi=(), per=None, color=CYAN, top=0.2, bot=0.86):
    """A line of fathers and sons as a chart: names in reading order, snaking row by row; names in hi lit gold."""
    n = len(names)
    per = per or math.ceil(n / math.ceil(n / 6))
    rows = math.ceil(n / per)
    size = max(8, min(12, w / (per * 9.5)))
    o = [grid_bg(w, h)]
    pts = []
    for i, nm in enumerate(names):
        r, c = divmod(i, per)
        if r % 2: c = per - 1 - c
        x = w * (0.1 + 0.8 * (c / max(1, per - 1) if per > 1 else 0.5))
        y = h * (top + (bot - top) * (r / max(1, rows - 1) if rows > 1 else 0.5))
        pts.append((x, y))
    for a, b in zip(pts, pts[1:]): o.append(route([a, b], color="#4A7A9A", sw=2, dash="5 5", arrow=True))
    for (x, y), nm in zip(pts, names):
        o.append(node(x, y, nm, GOLD if nm in hi else color, r=5, dy=-12, size=size))
    return "".join(o)

def branch(w, h, root, kids, hi=(), color=CYAN, per=None):
    """A father and his sons: the father above, the sons in a row (or two) below, a line to each."""
    n = len(kids)
    per = per or (n if n <= 7 else math.ceil(n / 2))
    rows = math.ceil(n / per)
    size = max(8, min(12, w / (per * 9.5)))
    rx, ry = w * 0.5, h * 0.22
    o = [grid_bg(w, h)]
    pts = []
    for i, nm in enumerate(kids):
        r, c = divmod(i, per)
        m = min(per, n - r * per)
        if rows > 1:                       # rows staggered by half a step, so no line crosses a name
            step = 0.82 / (per - 1 + (rows - 1) / rows)
            x = w * (0.08 + r * step / rows + c * step)
        else:
            x = w * (0.5 if m == 1 else 0.06 + 0.8 * c / (m - 1))
        y = h * (0.5 + (0.22 if rows == 2 else 0.38 / (rows - 1)) * r) if rows > 1 else h * 0.66
        pts.append((x, y))
    for x, y in pts:
        o.append(f'<path d="M{f(rx)} {f(ry)} L {f(rx)} {f((ry + y) / 2)} L {f(x)} {f((ry + y) / 2)} L {f(x)} {f(y)}" fill="none" stroke="#4A7A9A" stroke-width="2"></path>')
    o.append(node(rx, ry, root, GOLD, r=7, dy=-14, size=size + 1))
    for (x, y), nm in zip(pts, kids):
        o.append(node(x, y, nm, GOLD if nm in hi else color, r=5, dy=18, size=size))
    return "".join(o)

import exodus as E, exodus5 as V, samuel4 as S4, joshua1 as J
from genesis.art2 import fit, ground

def fire_altar(p, w, h, seed, king=True):
    """The altar on the threshing-floor of Ornan answered from heaven by fire: a shaft of fire falling out of a gold sky
    onto the burnt-offering, Jerusalem on its hill beyond, the king bowed before it (the cover and chapter 8)."""
    b = h * 0.86
    ax = w * 0.6
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#7A2A0A", "#FFC14D"), V.rays(ax, h * 0.1, 36, 24, max(w, h) * 1.2, color="#FFF4C2", op=0.22),
         J.city_hill(w * 0.18, h * 0.66, w * 0.4, h * 0.22, seed), ground(w, h, h * 0.68, "#C8A06A", dy=0), S4.threshing_floor(ax, b, w * 0.62),
         f'<path d="M{f(ax - w * 0.05)} -10 L {f(ax + w * 0.05)} -10 L {f(ax + w * 0.03)} {f(b - h * 0.2)} L {f(ax - w * 0.03)} {f(b - h * 0.2)} Z" fill="#FFE680" opacity="0.55"></path>'
         f'<path d="M{f(ax - w * 0.02)} -10 L {f(ax + w * 0.02)} -10 L {f(ax + w * 0.012)} {f(b - h * 0.2)} L {f(ax - w * 0.012)} {f(b - h * 0.2)} Z" fill="#FFF4C2"></path>',
         S4.altar(ax, b - h * 0.02, min(1.6, h / 260), seed=seed),
         E.blaze(ax, b - h * 0.16, w * 0.22, h * 0.24, seed + 3, n=7)]
    if king:
        o.append(E.kneel(w * 0.3, b, fit(b, h * 0.62) * 0.9, color="#4A2A6A", skin="#B98A6E"))
    return "".join(o)

# ---- 1 Chronicles 3–4 ---------------------------------------------------------------------------------------------------
import random, numbers1 as N
from genesis.art2 import hills
from genesis.art3 import flock, sun

def jabez_border(w, h):
    """Enlarge my border: a holding drawn as a survey plan, its old bound dashed and the new bound pushed out around it."""
    o = [grid_bg(w, h)]
    cx, cy = w * 0.5, h * 0.54
    for k, (col, dash, sw) in enumerate((("#4A7A9A", "6 6", 2), ("#8FD0E2", "10 6", 2.4), ("#FFD23F", "", 3))):
        rx, ry = w * (0.12 + 0.12 * k), h * (0.14 + 0.12 * k)
        pts = [(cx + rx * math.cos(a) * (1 + 0.12 * math.sin(3 * a + k)), cy + ry * math.sin(a) * (1 + 0.1 * math.cos(2 * a + k))) for a in [i * math.pi / 9 for i in range(18)]]
        d = "M" + " L ".join(f"{f(x)} {f(y)}" for x, y in pts) + " Z"
        o.append(f'<path d="{d}" fill="{col}" fill-opacity="{0.05 + 0.04 * k}" stroke="{col}" stroke-width="{sw}"' + (f' stroke-dasharray="{dash}"' if dash else "") + '></path>')
    for a in range(0, 360, 45):
        r = math.radians(a)
        o.append(route([(cx + w * 0.2 * math.cos(r), cy + h * 0.24 * math.sin(r)), (cx + w * 0.34 * math.cos(r), cy + h * 0.36 * math.sin(r))], color="#FFD23F", sw=2, dash="4 4"))
    o.append(node(cx, cy, "JABEZ", GOLD, r=6, dy=-14, size=11) + label(cx, h * 0.96, "ENLARGE MY BORDER", GOLD, 10))
    return "".join(o)

def pasture(p, w, h, seed, smoke=False):
    """The fat pasture at the entrance of Gedor, wide and quiet, flocks grazing (smoke=True: tents far off under smoke)."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8") if not smoke else K2.sky(w, h, "#5A4A5A", "#C8A080"),
         hills(w, h, h * 0.42, seed, "#6A8A4A" if not smoke else "#5A5A4A", amp=18, step=90), ground(w, h, h * 0.56, "#9CCB5E" if not smoke else "#8A9A5A", dy=0)]
    if smoke:
        o.append(N.camp(8, w * 0.5, w * 0.98, h * 0.5, h * 0.62, seed, color=("#4A3A3A", "#3A2A2A", "#5A4A40")))
        r = random.Random(seed)
        for i in range(4):
            x = w * (0.56 + 0.1 * i)
            o.append(f'<path d="M{f(x)} {f(h * 0.54)} C {f(x - 30)} {f(h * 0.4)} {f(x + 30)} {f(h * 0.26)} {f(x + r.uniform(-20, 40))} {f(h * 0.06)}" stroke="#3A3434" stroke-width="{f(w * 0.03)}" stroke-linecap="round" fill="none" opacity="0.55"></path>')
        o.append(flock(w * 0.02, w * 0.46, h * 0.66, h * 0.92, 10, seed, cows=0.1))
    else:
        o.append(sun(w * 0.84, h * 0.14, 20, color="#FFE680", op=0.5) + flock(w * 0.04, w * 0.96, h * 0.6, h * 0.94, 18, seed, cows=0.2))
    return "".join(o)

def seir(p, w, h, seed):
    """Mount Seir, red and steep, and the men of Simeon going up toward it in a long file, small with distance."""
    from genesis.art3 import man
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#C86A3A", "#F3C88A"),
         f'<path d="M-10 {f(h * 0.7)} L {f(w * 0.3)} {f(h * 0.2)} L {f(w * 0.44)} {f(h * 0.34)} L {f(w * 0.62)} {f(h * 0.12)} L {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A3A1E" stroke="#0D0D0F" stroke-width="2.6"></path>',
         hills(w, h, h * 0.76, seed, "#B8682E", amp=10, step=70), ground(w, h, h * 0.86, "#C8A06A", dy=0)]
    r = random.Random(seed)
    for i in range(14):
        k = i / 13
        x, y = w * (0.06 + 0.7 * k), h * (0.98 - 0.12 * k)
        o.append(man(p, x, y, fit(y, y - h * (0.3 - 0.18 * k)), r.choice(["#8A3A1E", "#5A2A16", "#3A2214", "#5A6E8A"])))
    return "".join(o)

# ---- 1 Chronicles 5–6 ---------------------------------------------------------------------------------------------------
import samuel1 as S1, samuel3 as S3, judges1 as J1, exodus4 as E4

EAST = [("AROER", 0.34, 0.82), ("NEBO", 0.3, 0.64), ("BAAL-MEON", 0.4, 0.7), ("GILEAD", 0.36, 0.46), ("BASHAN", 0.4, 0.26), ("SALECAH", 0.56, 0.3),
        ("HERMON", 0.34, 0.08), ("HAGRITES", 0.66, 0.6)]
def east_jordan(w, h, hi=("GILEAD",), war=False):
    """The land beyond the Jordan as a technical map: Reuben, Gad and the half-tribe of Manasseh from Aroer up to Hermon,
    the wilderness eastward to the Euphrates (war=True: the Hagrites' country marked and the march toward it)."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.2)} -10 C {f(w * 0.22)} {f(h * 0.3)} {f(w * 0.18)} {f(h * 0.6)} {f(w * 0.2)} {f(h + 10)}" stroke="#2C9DB8" stroke-width="4" fill="none"></path>'
             + label(w * 0.17, h * 0.5, "JORDAN", "#8FD0E2", 9, "end"))
    o.append(f'<rect x="{f(w * 0.26)}" y="{f(h * 0.04)}" width="{f(w * 0.34)}" height="{f(h * 0.88)}" fill="#FFD23F" fill-opacity="0.07" stroke="#FFD23F" stroke-width="1.6" stroke-dasharray="8 6"></rect>')
    o.append(label(w * 0.94, h * 0.12, "TO THE RIVER EUPHRATES →", "#8FD0E2", 9, "end"))
    pos = {n: (w * x, h * y) for n, x, y in EAST}
    if war:
        o.append(f'<ellipse cx="{f(w * 0.74)}" cy="{f(h * 0.6)}" rx="{f(w * 0.16)}" ry="{f(h * 0.2)}" fill="#D7261E" fill-opacity="0.2" stroke="#D7261E" stroke-width="2"></ellipse>')
        o.append(route([pos["GILEAD"], (w * 0.6, h * 0.58)], color="#FFD23F"))
    for nm, x, y in EAST:
        if nm == "HAGRITES" and not war: continue
        o.append(node(w * x, h * y, nm, RED_C if nm == "HAGRITES" else (GOLD if nm in hi else CYAN), r=5, dy=-11, size=9))
    return "".join(o)

def spoil(p, w, h, seed):
    """The cattle taken away: camels, sheep and asses driven in a long stream across the plain."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#C8A878", "#F3E0B0"), hills(w, h, h * 0.44, seed, "#A8784A", amp=12, step=80), ground(w, h, h * 0.52, "#C8A06A", dy=0)]
    items = sorted((r.uniform(h * 0.56, h * 0.96), r.uniform(-20, w + 20), r.random()) for _ in range(30))
    for y, x, q in items:
        k = (y - h * 0.56) / (h * 0.4); s = 0.12 + 0.3 * k
        if q < 0.3: o.append(J1.camel(x, y, s, color="#B5844A"))
        elif q < 0.85: o.append(E.sheep(x, y, s * 0.9))
        else: o.append(N.ass(x, y, s * 0.8))
    return "".join(o)

def singers(p, w, h, seed, n=6, top=0.42):
    """They that ministered with song before the tabernacle of the tent of meeting: the tent in its linen court, singers
    with harps and cymbals before it."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#FFB04A", "#F3E0B0"), ground(w, h, h * 0.6, "#C8A06A", dy=0), S1.shiloh(w * 0.5, h * 0.64, w * 0.7, h * 0.44)]
    s = fit(b, h * top)
    for i in range(n):
        o.append(S3.musician(p, w * (0.08 + i * 0.84 / max(1, n - 1)), b, s, kind=("harp", "cymbals")[i % 2], cloth="#F3EFE6", woman=False, seed=seed + i))
    o.append(S3.notes(w * 0.5, h * 0.3, 8, seed))
    return "".join(o)

def altar_service(p, w, h, seed):
    """Aaron and his sons at the altar of burnt-offering and the altar of incense: the priests in white at the two altars."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A4A6A", "#E8C890"), ground(w, h, h * 0.66, "#C8B88A", dy=0),
         horned_altar(w * 0.3, b, min(1.2, h / 280), fire=True, seed=seed), horned_altar(w * 0.72, b, min(0.7, h / 480), seed=seed + 1),
         f'<path d="M{f(w * 0.72)} {f(b - h * 0.24)} C {f(w * 0.68)} {f(h * 0.4)} {f(w * 0.78)} {f(h * 0.3)} {f(w * 0.72)} {f(h * 0.08)}" stroke="#E8E2D6" stroke-width="10" fill="none" opacity="0.6"></path>']
    s = fit(b, max(h * 0.42, b - 220))
    o.append(priest(p, w * 0.12, b, s) + priest(p, w * 0.5, b, s * 0.94, flip=True) + priest(p, w * 0.9, b, s, flip=True))
    return "".join(o)

# ---- 1 Chronicles 7–9 ---------------------------------------------------------------------------------------------------
from exo.art8 import bp, dim, tag
import samuel4 as S4b

def porters_plan(w, h, lit=(), names=None):
    """The porters on the four sides of the house of the tent, toward the east, west, north and south, as a blueprint:
    the court and the tent in plan, a gate on each side with its ward (lit: sides drawn gold)."""
    o = [bp(w, h)]
    cx, cy = w * 0.5, h * 0.54
    cw, ch = min(w * 0.56, h * 1.1), min(h * (0.44 if names else 0.6), w * 0.4)
    o.append(f'<rect x="{f(cx - cw / 2)}" y="{f(cy - ch / 2)}" width="{f(cw)}" height="{f(ch)}" fill="none" stroke="#8FD0E2" stroke-width="2.4"></rect>'
             f'<rect x="{f(cx - cw * 0.16)}" y="{f(cy - ch * 0.2)}" width="{f(cw * 0.32)}" height="{f(ch * 0.4)}" fill="#8FD0E2" fill-opacity="0.12" stroke="#8FD0E2" stroke-width="2"></rect>'
             + label(cx, cy + 4, "THE HOUSE OF THE TENT", "#8FD0E2", 9))
    gates = {"EAST": (cx + cw / 2, cy, 0), "WEST": (cx - cw / 2, cy, 0), "NORTH": (cx, cy - ch / 2, 1), "SOUTH": (cx, cy + ch / 2, 1)}
    for nm, (x, y, horiz) in gates.items():
        col = GOLD if (not lit or nm in lit) else CYAN
        gw = cw * 0.12 if horiz else ch * 0.18
        if horiz: o.append(f'<path d="M{f(x - gw / 2)} {f(y)} L {f(x + gw / 2)} {f(y)}" stroke="{INK if False else "#0B1A2E"}" stroke-width="6"></path>')
        else: o.append(f'<path d="M{f(x)} {f(y - gw / 2)} L {f(x)} {f(y + gw / 2)}" stroke="#0B1A2E" stroke-width="6"></path>')
        o.append(node(x, y, "", col, r=6, dy=0))
        tx = x + (w * 0.1 if nm == "EAST" else -w * 0.1 if nm == "WEST" else 0)
        ty = y + (-h * 0.1 if nm == "NORTH" else h * 0.12 if nm == "SOUTH" else 4)
        o.append(label(tx, ty, nm, col, 11))
        if names and nm in names:
            for k, line in enumerate(names[nm].split("|")):
                o.append(label(tx, ty + 14 + k * 12, line, "#F3EFE6", 9))
    if not names: o.append(dim(cx - cw / 2, cy + ch / 2 + h * 0.06, cx + cw / 2, cy + ch / 2 + h * 0.06, "FOUR SIDES · BY WARDS", size=8))
    return "".join(o)

EPHRAIM_M = [("BETH-EL", 0.44, 0.78), ("NAARAN", 0.66, 0.74), ("GEZER", 0.14, 0.86), ("SHECHEM", 0.48, 0.52), ("BETH-SHEAN", 0.72, 0.26),
             ("TAANACH", 0.46, 0.24), ("MEGIDDO", 0.36, 0.18), ("DOR", 0.12, 0.2), ("BETH-HORON", 0.3, 0.8)]
def ephraim_map(w, h, hi=()):
    """The possessions of Ephraim and Manasseh as a technical map: Beth-el to Gezer, Shechem, and by Manasseh's borders
    Beth-shean, Taanach, Megiddo and Dor."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.06)} -10 C {f(w * 0.08)} {f(h * 0.4)} {f(w * 0.04)} {f(h * 0.7)} {f(w * 0.02)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.84)} -10 C {f(w * 0.86)} {f(h * 0.3)} {f(w * 0.82)} {f(h * 0.6)} {f(w * 0.86)} {f(h + 10)}" stroke="#2C9DB8" stroke-width="4" fill="none"></path>'
             + label(w * 0.88, h * 0.5, "JORDAN", "#8FD0E2", 9, "start"))
    o.append(f'<path d="M{f(w * 0.06)} {f(h * 0.42)} L {f(w * 0.84)} {f(h * 0.36)}" stroke="#FFD23F" stroke-width="1.6" stroke-dasharray="8 6"></path>'
             + label(w * 0.6, h * 0.34, "MANASSEH", "#FFD23F", 9) + label(w * 0.6, h * 0.46, "EPHRAIM", "#FFD23F", 9))
    for nm, x, y in EPHRAIM_M:
        o.append(node(w * x, h * y, nm, GOLD if nm in hi else CYAN, r=5, dy=-11, size=9))
    return "".join(o)

def beth_horon(p, w, h, seed):
    """Beth-horon the nether and the upper, which Sheerah built: two walled towns on the ridge, one above the other."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.5, seed, "#8A7A5A", amp=10, step=80),
         J.city_hill(w * 0.66, h * 0.5, w * 0.3, h * 0.2, seed), J.city_hill(w * 0.3, h * 0.82, w * 0.36, h * 0.2, seed + 1), ground(w, h, h * 0.84, "#C8A06A", dy=0),
         label(w * 0.66, h * 0.16, "THE UPPER", "#0D0D0F", 10), label(w * 0.3, h * 0.5, "THE NETHER", "#0D0D0F", 10)]
    return "".join(o)

def opening(p, w, h, seed):
    """Morning by morning: the porters opening the gate of the house of God at dawn, a Levite with the keys."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A4A7A", "#FFC890"), sun(w * 0.86, h * 0.62, 26, color="#FFE680", op=0.4), ground(w, h, h * 0.7, "#B8A07A", dy=0),
         S4b.gatehouse(w * 0.44, h * 0.8, w * 0.44, h * 0.56, lit=True)]
    s = fit(b, max(h * 0.46, b - 200))
    for i, x in enumerate((0.12, 0.76, 0.88)):
        o.append(priest(p, w * x, b, s, flip=i > 0))
    return "".join(o)

def night_song(p, w, h, seed):
    """The singers employed in their work day and night: the tent under the stars, harps lit by a lamp."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#0B0B2A", "#3A2A5A"), mk.stars(60, w, h * 0.5, seed), ground(w, h, h * 0.62, "#3A3448", dy=0),
         S1.shiloh(w * 0.5, h * 0.66, w * 0.64, h * 0.42), S1.lamp(w * 0.5, h * 0.62, min(0.4, h / 900))]
    s = fit(b, max(h * 0.5, b - 180))
    for i in range(4):
        o.append(S3.musician(p, w * (0.1 + i * 0.26), b, s, kind="harp", cloth="#C8C2D6", woman=False, seed=seed + i))
    return "".join(o)

# ---- 1 Chronicles 10–12 -------------------------------------------------------------------------------------------------
import exodus3 as E3

def oak_jabesh(w, h, seed):
    """The oak in Jabesh at dusk, the ground beneath it fresh-turned, the men of Jabesh-gilead small and still."""
    o = [K2.sky(w, h, "#2A1A3A", "#C8807A"), hills(w, h, h * 0.6, seed, "#3A2A3A", amp=12, step=80), ground(w, h, h * 0.78, "#4A3A30", dy=0),
         S4b.great_oak(w * 0.42, h * 0.8, min(1.4, h / 300), seed=seed, dark=True),
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.82)}" rx="{f(w * 0.12)}" ry="{f(h * 0.025)}" fill="#6A4A30" stroke="#0D0D0F" stroke-width="1.6"></ellipse>']
    for i in range(7):
        x = w * (0.68 + i * 0.045)
        o.append(f'<path d="M{f(x)} {f(h * 0.9)} l 0 {f(-h * 0.08)}" stroke="#1A1218" stroke-width="{f(w * 0.014)}" stroke-linecap="round"></path>'
                 f'<circle cx="{f(x)}" cy="{f(h * 0.8)}" r="{f(w * 0.009)}" fill="#1A1218"></circle>')
    return "".join(o)

def bringing(p, w, h, seed):
    """Bread on asses, on camels, on mules and on oxen, coming to Hebron: a long train of beasts laden with sacks, figs and
    raisins, wine-skins and oil, Hebron on its hill with the feast."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#FFE680", "#FFB04A"), J.city_hill(w * 0.84, h * 0.6, w * 0.26, h * 0.26, seed), ground(w, h, h * 0.62, "#C8A06A", dy=0)]
    for i in range(9):
        k = i / 8; x = w * (0.04 + 0.7 * k); y = h * (0.96 - 0.26 * k); s = 0.5 - 0.3 * k
        q = i % 3
        if q == 0: o.append(J1.camel(x, y, s * min(1.0, h / 360), color="#B5844A"))
        elif q == 1: o.append(N.ass(x, y, s * min(1.0, h / 360)))
        else: o.append(S1.cow(x, y - h * 0.02, s * min(1.0, h / 360), color="#8A5A30"))
        o.append(f'<rect x="{f(x - 14 * s)}" y="{f(y - h * 0.22 * s - 10)}" width="{f(28 * s)}" height="{f(18 * s)}" rx="4" fill="{r.choice(["#E8D8A0", "#C8A060", "#8A3A4A"])}" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    return "".join(o)

# ---- 1 Chronicles 21–22 -------------------------------------------------------------------------------------------------
def tally(w, h, rows, title=""):
    """A tally board: rows of (name, number, colour) in framed columns."""
    o = [grid_bg(w, h, color="#3A2A5A", bg="#1A1430")]
    n = len(rows)
    for i, (nm, num, c) in enumerate(rows):
        x = w * (0.5 + (i - (n - 1) / 2) * (0.9 / n))
        bw = w * 0.82 / n
        o.append(f'<rect x="{f(x - bw / 2)}" y="{f(h * 0.2)}" width="{f(bw)}" height="{f(h * 0.6)}" fill="none" stroke="{c}" stroke-width="2"></rect>'
                 + label(x, h * 0.34, nm, c, 12) + f'<text x="{f(x)}" y="{f(h * 0.62)}" fill="{c}" font-family="Anton, sans-serif" font-size="{f(min(bw * 0.18, h * 0.18))}" text-anchor="middle">{num}</text>')
    if title: o.append(label(w * 0.5, h * 0.92, title, "#C8C2D6", 9))
    return "".join(o)

def sackcloth_elders(p, w, h, seed):
    """The angel of Jehovah between earth and heaven with his sword stretched out over Jerusalem; David and the elders in
    sackcloth fallen upon their faces below."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#2A1A3A", "#8A5A6A"), J.city_hill(w * 0.7, h * 0.74, w * 0.5, h * 0.3, seed), ground(w, h, h * 0.78, "#3A2A2A", dy=0),
         V.rays(w * 0.62, h * 0.24, 24, 12, w * 0.5, color="#FFF4C2", op=0.25), N.angel(p, w * 0.62, h * 0.6, fit(h * 0.6, h * 0.06), sword=True, glow=True, flip=True)]
    s = fit(b, h * 0.6)
    for i in range(4):
        o.append(N.prostrate(w * (0.06 + i * 0.12), b - i * h * 0.01, s * 0.7, color="#5A5040", skin="#9A6A4A"))
    return "".join(o)

def stores(w, h, seed):
    """Prepared in abundance: stacks of gold and silver talents, brass and iron without weight, cedar logs, hewn stones."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#3A2A1A", "#8A6A4A"), ground(w, h, h * 0.62, "#6A5040", dy=0)]
    piles = [("#E8B830", "GOLD"), ("#C8C8D0", "SILVER"), ("#B87333", "BRASS"), ("#5A5A62", "IRON")]
    for i, (c, nm) in enumerate(piles):
        x0 = w * (0.04 + i * 0.16); base = h * 0.94
        for row in range(5):
            for k in range(4 - row // 2):
                x = x0 + k * w * 0.032 + row * w * 0.008
                o.append(f'<rect x="{f(x)}" y="{f(base - (row + 1) * h * 0.06)}" width="{f(w * 0.03)}" height="{f(h * 0.055)}" rx="2" fill="{c}" stroke="#0D0D0F" stroke-width="1.4"></rect>')
        o.append(label(x0 + w * 0.06, h * 0.6, nm, c, 9))
    for k in range(5):
        y = h * (0.92 - k * 0.07)
        o.append(f'<rect x="{f(w * 0.7)}" y="{f(y - h * 0.06)}" width="{f(w * 0.26)}" height="{f(h * 0.06)}" rx="{f(h * 0.03)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 f'<ellipse cx="{f(w * 0.96)}" cy="{f(y - h * 0.03)}" rx="{f(h * 0.012)}" ry="{f(h * 0.03)}" fill="#C8965A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    o.append(label(w * 0.83, h * 0.48, "CEDAR", "#E8C88A", 9))
    return "".join(o)

def charge_son(p, w, h, seed, princes=False):
    """David old charging Solomon his son in the cedar hall (princes=True: the princes of Israel standing by)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84)]
    s = fit(b, max(h * 0.3, b - 260))
    o.append(K2.old_king(p, w * 0.32, b, s) + sol_fig(p, w * 0.56, b, s * 0.95, flip=True))
    if princes:
        for i in range(4):
            o.append(man(p, w * (0.72 + i * 0.07), b, s * 0.85, ["#3A4A6A", "#6A3A2A", "#4A5A3A", "#5A4A6A"][i], flip=True))
    return "".join(o)
from genesis.art3 import man

# ---- 1 Chronicles 23–27 -------------------------------------------------------------------------------------------------
def lot_grid(w, h, names, lit=None, cols=6, color=GOLD, top=0.06):
    """The courses drawn by lot as a board of numbered tiles: the lot's number large, the name beneath (lit: the indices
    drawn in colour, the rest dimmed)."""
    o = [grid_bg(w, h, color="#3A2A5A", bg="#1A1430")]
    n = len(names); rows = math.ceil(n / cols)
    gx, gy = w * 0.03, h * 0.03
    tw = (w * 0.94 - gx * (cols - 1)) / cols
    th = (h * (0.96 - top) - gy * (rows - 1)) / rows
    for i, nm in enumerate(names):
        r, c = divmod(i, cols)
        x, y = w * 0.03 + c * (tw + gx), h * top + r * (th + gy)
        on = lit is None or i in lit
        col = color if on else "#5A5480"
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(tw)}" height="{f(th)}" rx="4" fill="{col}" fill-opacity="{0.16 if on else 0.06}" stroke="{col}" stroke-width="{2 if on else 1.2}"></rect>'
                 f'<text x="{f(x + tw / 2)}" y="{f(y + th * 0.56)}" fill="{col}" font-family="Anton, sans-serif" font-size="{f(min(th * 0.46, tw * 0.4))}" text-anchor="middle">{i + 1}</text>'
                 + label(x + tw / 2, y + th * 0.86, nm, col if on else "#7A7498", max(7, min(10, tw / (len(nm) * 0.7 + 1))), ls=0.06))
    return "".join(o)

def month_wheel(w, h, names, lit=None):
    """The twelve courses of the captains as a calendar wheel: twelve sectors for the twelve months, each with its captain
    (lit: the month indices drawn in gold)."""
    o = [grid_bg(w, h, color="#3A2A5A", bg="#1A1430")]
    cx, cy = w * 0.5, h * 0.52
    R = min(w * 0.4, h * 0.42); r0 = R * 0.34
    for i, nm in enumerate(names):
        a0, a1 = math.radians(-90 + i * 30), math.radians(-90 + (i + 1) * 30)
        on = lit is None or i in lit
        col = GOLD if on else "#5A5480"
        pts = (f"M{f(cx + r0 * math.cos(a0))} {f(cy + r0 * math.sin(a0))} L {f(cx + R * math.cos(a0))} {f(cy + R * math.sin(a0))} "
               f"A {f(R)} {f(R)} 0 0 1 {f(cx + R * math.cos(a1))} {f(cy + R * math.sin(a1))} L {f(cx + r0 * math.cos(a1))} {f(cy + r0 * math.sin(a1))} "
               f"A {f(r0)} {f(r0)} 0 0 0 {f(cx + r0 * math.cos(a0))} {f(cy + r0 * math.sin(a0))} Z")
        o.append(f'<path d="{pts}" fill="{col}" fill-opacity="{0.18 if on else 0.05}" stroke="{col}" stroke-width="{1.8 if on else 1}"></path>')
        am = (a0 + a1) / 2
        o.append(f'<text x="{f(cx + (r0 + (R - r0) * 0.3) * math.cos(am))}" y="{f(cy + (r0 + (R - r0) * 0.3) * math.sin(am) + 7)}" fill="{col}" font-family="Anton, sans-serif" '
                 f'font-size="{f(R * 0.12)}" text-anchor="middle">{i + 1}</text>')
        lx, ly = cx + (R + 12) * math.cos(am), cy + (R + 12) * math.sin(am)
        anchor = "start" if math.cos(am) > 0.2 else ("end" if math.cos(am) < -0.2 else "middle")
        o.append(label(lx, ly + 4, nm, col if on else "#7A7498", 9, anchor, ls=0.06))
    o.append(label(cx, cy - 2, "24,000", "#F3EFE6", 12) + label(cx, cy + 12, "EACH COURSE", "#C8C2D6", 7))
    return "".join(o)
