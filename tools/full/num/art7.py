"""New drawings for Numbers chapter 7 (Numbers 13–14): Moses sending the twelve from the wilderness of Paran, the
hill-country of Canaan in the season of the first-ripe grapes, the spies' road as a map (Zin to Rehob and Hamath, by
Hebron and Eshcol, back to Kadesh), Moses and Aaron fallen on their faces, the glory in the tent of meeting, and the
people going up presumptuously to the top of the mountain. The spies' deaths (14:37) and Hormah (14:45) are told in
captions over landscape and distant silhouettes. Faces: Caleb, a frightened spy, Joshua (numbers1 / exodus tokens)."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, numbers1 as N
from genesis.art2 import fit, ground, hills
from genesis.art3 import sun, label, man, grid_bg, node, route
from exo import art as A, art8 as B8
from num.art import ALL, TRIBE_C, standard
def f(v): return f"{v:.1f}"
_T = N.tokens()
CALEB, SPY, JOSHUA = _T["__FACE_CALEB__"], _T["__FACE_SPY__"], _T["__FACE_JOSHUA__"]
HEBREW_FEAR, HEBREW_ANGRY = _T["__FACE_HEBREW_FEAR__"], _T["__FACE_HEBREW_ANGRY__"]
SPY_C = "#7A6A4A"

def sending(p, w, h, seed):
    """Moses sending the twelve from the wilderness of Paran: the twelve with staves, the hill-country far off."""
    r = random.Random(seed); b = h * 0.9
    o = [mk.defs(p, *ALL), sun(w * 0.86, h * 0.16, 14, op=0.25), hills(w, h, h * 0.42, seed, color="#6A8A4A", amp=18), ground(w, h, h * 0.5, "#D8B878", dy=0)]
    s = fit(b, h * 0.44)
    o.append(A.moses(p, w * 0.1, b, s, up=[(-22, -158), (10, -180), (40, -196)]))
    for i in range(12):
        x = w * (0.24 + i * 0.062); y = b - (i % 2) * 6
        o.append(man(p, x, y, s * 0.88, r.choice(["#7A6A4A", "#6A5A3A", "#8A6A4A", "#5A4A3A"]), flip=False))
    return "".join(o)

def hill_country(w, h, seed):
    """The hill-country: terraced green hills, vineyards heavy with the first-ripe grapes, a walled city far off."""
    r = random.Random(seed)
    o = [sun(w * 0.84, h * 0.18, 14, op=0.25), hills(w, h, h * 0.4, seed, color="#4A7A3A", amp=24, step=80), hills(w, h, h * 0.6, seed + 1, color="#6A9A4A", amp=18),
         ground(w, h, h * 0.78, "#8AAA5A", dy=0)]
    for i in range(10):
        x = w * (0.04 + i * 0.1); y = h * (0.84 + (i % 2) * 0.06)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - h * 0.08)}" stroke="#5A3A22" stroke-width="3"></path>' + N.grapes(x + 6, y - h * 0.08, min(0.4, h / 900), seed + i))
    o.append(f'<path d="M{f(w * 0.62)} {f(h * 0.42)} L {f(w * 0.62)} {f(h * 0.34)} L {f(w * 0.66)} {f(h * 0.34)} L {f(w * 0.66)} {f(h * 0.3)} L {f(w * 0.7)} {f(h * 0.3)} L {f(w * 0.7)} {f(h * 0.34)} L {f(w * 0.78)} {f(h * 0.34)} L {f(w * 0.78)} {f(h * 0.42)} Z" fill="#B8A88A" stroke="#0D0D0F" stroke-width="1.6"></path>')
    return "".join(o)

def spy_map(w, h):
    """The way of the spies: from Kadesh in the wilderness of Paran by the South to Hebron and the valley of Eshcol,
    from the wilderness of Zin unto Rehob, to the entrance of Hamath; and back after forty days."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.06)} -10 C {f(w * 0.08)} {f(h * 0.4)} {f(w * 0.1)} {f(h * 0.7)} {f(w * 0.14)} {f(h + 10)} L -10 {f(h + 10)} L -10 -10 Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(label(w * 0.04, h * 0.5, "THE SEA", "#8FD0E2", 9, "start"))
    o.append(f'<path d="M{f(w * 0.56)} {f(h * 0.08)} C {f(w * 0.54)} {f(h * 0.3)} {f(w * 0.58)} {f(h * 0.5)} {f(w * 0.56)} {f(h * 0.62)}" fill="none" stroke="#8FD0E2" stroke-width="3"></path>' + label(w * 0.6, h * 0.36, "JORDAN", "#8FD0E2", 8, "start"))
    pts = {"KADESH": (0.3, 0.9), "HEBRON": (0.4, 0.62), "ESHCOL": (0.3, 0.58), "REHOB": (0.44, 0.18), "HAMATH": (0.62, 0.06)}
    P = {k: (w * x, h * y) for k, (x, y) in pts.items()}
    o.append(route([P["KADESH"], P["HEBRON"], P["REHOB"], P["HAMATH"]], color="#FFD23F"))
    o.append(route([P["ESHCOL"], (w * 0.24, h * 0.8), P["KADESH"]], color="#9CCB5E"))
    for k, (x, y) in P.items(): o.append(node(x, y, k, "#FFD23F" if k != "ESHCOL" else "#9CCB5E", dy=-12 if k != "ESHCOL" else 22))
    o.append(label(w * 0.96, h * 0.95, "FORTY DAYS", "#FFD23F", 11, "end", ls=0.2))
    return "".join(o)

def fallen(p, w, h, seed):
    """Moses and Aaron fallen on their faces before all the assembly."""
    r = random.Random(seed); b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#3A2A3A"></rect>', ground(w, h, h * 0.6, "#5A4A4A", dy=0)]
    s = min(1.2, h / 260)
    o.append(N.prostrate(w * 0.3, b, s, color="#7A5A3A", skin="#C98E66") + N.prostrate(w * 0.56, b + 4, s, color="#4A6A9A", skin="#C98E66"))
    for i in range(8):
        x = w * (0.04 + i * 0.12); y = h * 0.66
        o.append(man(p, x, y, fit(y, y - h * 0.22), r.choice(A.HEBREW)))
    return "".join(o)

def stoning(p, w, h, seed):
    """All the congregation bade stone them; the glory of Jehovah appeared in the tent of meeting."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), V.rays(w * 0.7, h * 0.4, 44, 30, max(w, h) * 1.2, color="#FFF4C2", op=0.45), ground(w, h, h * 0.58, "#C8B080", dy=0),
         V.tabernacle(w * 0.7, h * 0.64, w * 0.4, uid=p + "tb")]
    s = fit(b, h * 0.42)
    for i in range(7):
        x = w * (0.04 + i * 0.07)
        o.append(man(p, x, b - (i % 2) * 6, s * 0.9, r.choice(A.HEBREW), up=[(-22, -158), (-10, -196), (6, -222)]))
        o.append(f'<circle cx="{f(x + 6 * s)}" cy="{f(b - 228 * s)}" r="{f(7 * s)}" fill="#8A8478" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    return "".join(o)

def presumed(p, w, h, seed, smitten=False):
    """They gat them up to the top of the mountain; the ark and Moses departed not out of the camp (smitten=True: the
    Amalekite and the Canaanite coming down upon them, as silhouettes against the dusk)."""
    r = random.Random(seed); b = h * 0.92
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="{"#3A1A1A" if smitten else "#8FD0E2"}"></rect>']
    o.append(f'<path d="M-10 {f(h)} L {f(w * 0.45)} {f(h * 0.12)} L {f(w * 0.62)} {f(h * 0.26)} L {f(w * 1.1)} {f(h)} Z" fill="{"#1A0A0A" if smitten else "#8A6A4A"}" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(mk.defs(p, *ALL))
    if not smitten:
        for i in range(9):
            t = i / 8; x = w * (0.08 + 0.36 * t); y = h * (0.9 - 0.7 * t)
            o.append(man(p, x, y, fit(y, y - h * 0.12), r.choice(A.HEBREW), flip=False))
    else:
        for i in range(8):
            t = i / 7; x = w * (0.46 + 0.2 * t); y = h * (0.16 + 0.4 * t)
            o.append(man(p, x, y, fit(y, y - h * 0.12), "#0D0D0F", flip=True, up=[(-22, -158), (-30, -190), (-44, -214)]))
        for i in range(6):
            t = i / 5; x = w * (0.1 + 0.3 * t); y = h * (0.92 - 0.3 * t)
            o.append(man(p, x, y, fit(y, y - h * 0.12), "#2A1A1A", flip=True))
    return "".join(o)

def empty_wilderness(w, h, seed, dusk=True):
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="{"#2A1A2E" if dusk else "#E8C88A"}"></rect>', V.rays(w * 0.5, h * 0.62, 30, 20, w, color="#FF8A3D", op=0.2),
         hills(w, h, h * 0.56, seed, color="#3A2430", amp=12), ground(w, h, h * 0.66, "#4A3030", dy=0)]
    return "".join(o)
