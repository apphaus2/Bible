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
        x = w * (0.5 if m == 1 else (0.06 + 0.07 * r) + (0.8 - 0.07 * r) * c / (m - 1))   # a second row sits half a step over, so no line crosses a name
        y = h * (0.5 + 0.22 * r) if rows > 1 else h * 0.74
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
