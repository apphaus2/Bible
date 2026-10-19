"""Drawings for the Ecclesiastes volume (chapter by chapter, added below), on top of 2 Chronicles' (chr2.art, which carries
chr1.art, kg2.art, kg1.art, and 2 Samuel's drawings as K2).

The Preacher at a distance: Solomon old, a deep-blue tunic, grey beard and the gold crown (preacher()). The images he speaks
of are drawn as landscapes, diagrams and still objects: the sun's course, the wind's circuits, the rivers and the sea, the
ruins of the former generations, a time to every purpose as a ring of fourteen cells, and so on."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from chr2.art import *
from chr2.art import f, K2, K3
from kg1.art import SOL_C, bed
from genesis.art2 import fit, ground, hills, bird, birds, SKIN
from genesis.art3 import man, woman, sun, label, grid_bg, node, route, GREY_BEARD
from exo.art8 import bp, dim, tag
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, joshua1 as J, judges1 as J1, judges2 as JG2, ruth1 as R1
import samuel1 as S1, samuel2 as S2, samuel3 as S3, samuel4 as S4, numbers1 as N
from num.art import ALL
from ecc import G

GOLD, CYAN, ROSE = "#FFD23F", "#8FD0E2", "#FF8A6A"

def preacher(p, x, y, s, flip=False, up=None):
    """The Preacher at a distance: Solomon old, deep-blue tunic, grey beard, the gold crown."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#5A2A16", cloth=SOL_C, kind="Tunic", sw=3, flip=flip, up=up, extra=GREY_BEARD + S3.KING)

def hgrad(gid, stops, vertical=False):
    """A linear gradient definition: stops [(offset, colour)]."""
    x2, y2 = ("0", "1") if vertical else ("1", "0")
    return (f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="{x2}" y2="{y2}">'
            + "".join(f'<stop offset="{o}" stop-color="{c}"></stop>' for o, c in stops) + '</linearGradient></defs>')

def arc_pts(cx, cy, rx, ry, a0, a1, n=24):
    """Points along an ellipse from angle a0 to a1 (degrees; 0 = east, 90 = up)."""
    return [(cx + rx * math.cos(math.radians(a0 + (a1 - a0) * k / n)), cy - ry * math.sin(math.radians(a0 + (a1 - a0) * k / n))) for k in range(n + 1)]

def tree(x, y, s=1.0, color="#2E6B3A", lean=0, kind="round", seed=1):
    """A tree standing on (x, y): round (fruit or olive), tall (cypress), or bare."""
    r = random.Random(seed)
    tx = x + lean * 40 * s
    o = f'<path d="M{f(x)} {f(y)} C {f(x)} {f(y - 40 * s)} {f(tx)} {f(y - 70 * s)} {f(tx)} {f(y - 90 * s)}" stroke="#5A3A22" stroke-width="{f(9 * s)}" fill="none" stroke-linecap="round"></path>'
    if kind == "tall":
        o += f'<path d="M{f(tx)} {f(y - 200 * s)} C {f(tx + 26 * s)} {f(y - 150 * s)} {f(tx + 24 * s)} {f(y - 90 * s)} {f(tx)} {f(y - 70 * s)} C {f(tx - 24 * s)} {f(y - 90 * s)} {f(tx - 26 * s)} {f(y - 150 * s)} {f(tx)} {f(y - 200 * s)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'
    elif kind == "round":
        for _ in range(6):
            o += f'<circle cx="{f(tx + r.uniform(-34, 34) * s + lean * 20 * s)}" cy="{f(y - r.uniform(96, 140) * s)}" r="{f(r.uniform(26, 36) * s)}" fill="{color}" stroke="#0D0D0F" stroke-width="1.8"></circle>'
    return o

def wind_lines(w, h, seed, n=10, color="#F3EFE6", op=0.7, y0=0.1, y1=0.7):
    """Streaks of wind blowing across a panel."""
    r = random.Random(seed); o = []
    for _ in range(n):
        x = r.uniform(-w * 0.1, w * 0.8); y = r.uniform(h * y0, h * y1); L = r.uniform(w * 0.15, w * 0.35)
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x + L * 0.4)} {f(y - 10)} {f(x + L * 0.7)} {f(y + 8)} {f(x + L)} {f(y - 4)}" stroke="{color}" stroke-width="2.4" fill="none" stroke-linecap="round" opacity="{op}"></path>')
    return "".join(o)

# ---- Ecclesiastes 1 -----------------------------------------------------------------------------------------------------
def roof_view(p, w, h, seed):
    """The Preacher, king in Jerusalem, on the roof of his house at evening, his arm stretched over the rooftops of the city."""
    top = h * 0.46; b = h * 0.97
    o = [mk.defs(p, *ALL), sky(w, h, "#2A1A3A", "#E8803A"), sun(w * 0.8, h * 0.4, max(12, h * 0.05), color="#FF8A3D", op=0.4), S3.roof(w, h, top, seed)]
    s = min(fit(b, h * 0.26), 1.1 * w / 702)
    o.append(preacher(p, w * 0.2, b, s, flip=True, up=[(-22, -158), (-50, -170), (-78, -176)]))
    return "".join(o)

def generations(p, w, h, seed):
    """One generation goeth, and another generation cometh: a line of people walking across the earth, from the dawn on the
    left (children) to the dusk on the right (the old, fading); the hills abide."""
    gid = f"gen{p}"
    b = h * 0.9
    o = [mk.defs(p, *ALL), hgrad(gid, [(0, "#FFE6A0"), (0.5, "#8FD0E2"), (1, "#3A2A5A")]), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{gid})"></rect>',
         sun(w * 0.06, h * 0.5, max(10, h * 0.05), color="#FFD23F", op=0.4), hills(w, h, h * 0.56, seed, color="#6A7A5A", amp=10, step=70), ground(w, h, h * 0.68, "#9A8A5A", dy=0)]
    o.append(mk.stars(20, w * 0.3, h * 0.4, seed).replace("<g ", f'<g transform="translate({f(w * 0.7)} 0)" ', 1))
    s = fit(b, max(h * 0.4, b - 190))
    cl = ["#C2456A", "#1F5FAD", "#E8A317", "#5E8F26", "#B5421E", "#7A3BA8", "#2C7DA8", "#8A5A30", "#5A5A6A", "#4A4A5A"]
    n = 10
    for i in range(n):
        x = w * (0.06 + 0.9 * i / (n - 1))
        op = 1.0 if i < 6 else 1.0 - (i - 5) * 0.17
        fig = (woman(p, x, b, s * (0.6 if i == 0 else 0.95), cl[i]) if i % 2 == 0 else man(p, x, b, s * (0.66 if i == 1 else 1.0), cl[i], extra=GREY_BEARD if i > 6 else ""))
        o.append(f'<g opacity="{op:.2f}">{fig}</g>')
    o.append(route([(w * 0.1, h * 0.96), (w * 0.9, h * 0.96)], color="#3A2A1A", sw=2, dash="8 6"))
    return "".join(o)

def sun_course(w, h, seed):
    """The sun ariseth and goeth down, and hasteth to its place where it ariseth: its course over the earth as a diagram —
    five suns along the arc of the day, and the dashed way back under the earth."""
    hz = h * 0.72; cx, rx, ry = w * 0.5, w * 0.42, h * 0.6
    o = [sky(w, h, "#1F5F9A", "#FFD8A0"), hills(w, h, hz, seed, color="#3A2A3A", amp=8, step=60),
         f'<rect x="-10" y="{f(hz + 8)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A1E2A"></rect>']
    o.append(route(arc_pts(cx, hz, rx, ry, 180, 0), color="#FFF4C2", sw=2.2, dash="8 7"))
    o.append(route(arc_pts(cx, hz + 8, rx, h * 0.18, 0, -180), color="#FFD23F", sw=2, dash="4 6"))
    for k, (t, c, r) in enumerate([(170, "#FF6A2A", 0.05), (135, "#FFB04A", 0.055), (90, "#FFF4C2", 0.065), (45, "#FFB04A", 0.055), (10, "#D7261E", 0.05)]):
        x = cx + rx * math.cos(math.radians(t)); y = hz - ry * math.sin(math.radians(t))
        rr = max(8, min(w, h) * r)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rr * 2)}" fill="{c}" opacity="0.18"></circle><circle cx="{f(x)}" cy="{f(y)}" r="{f(rr)}" fill="{c}" stroke="#0D0D0F" stroke-width="1.6"></circle>')
    o.append(label(w * 0.06, hz - 10, "E", "#FFF4C2", 12) + label(w * 0.94, hz - 10, "W", "#FFF4C2", 12))
    return "".join(o)

def wind_circuits(w, h, seed):
    """The wind goeth toward the south, and turneth about unto the north: a field with its trees bent, and the wind's
    circuits drawn as loops of streamlines round a compass."""
    r = random.Random(seed)
    o = [sky(w, h, "#6A8AA8", "#D8E4EA"), hills(w, h, h * 0.62, seed, color="#5A7A5A", amp=12, step=80), ground(w, h, h * 0.74, "#8AA05A", dy=0)]
    for i in range(3):
        o.append(tree(w * (0.12 + i * 0.1), h * (0.8 + i * 0.03), min(0.9, h / 420) * (0.8 + 0.1 * i), color="#3F7A44", lean=0.6, seed=seed + i))
    for _ in range(30):
        x, y = r.uniform(0, w), r.uniform(h * 0.78, h)
        o.append(f'<path d="M{f(x)} {f(y)} q 6 -10 14 -12" stroke="#4A6A2A" stroke-width="2" fill="none"></path>')
    cx, cy = w * 0.58, h * 0.4
    for k in range(3):
        rx, ry = w * (0.34 - k * 0.07), h * (0.26 - k * 0.05)
        o.append(route(arc_pts(cx, cy, rx, ry, 100 + k * 30, 100 + k * 30 - 320, n=40), color=["#F3EFE6", "#CFE0FF", "#FFF4C2"][k], sw=2.6 - k * 0.4, dash="10 6"))
    for _ in range(9):
        x, y = r.uniform(w * 0.2, w * 0.95), r.uniform(h * 0.15, h * 0.65)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="5" ry="2.6" fill="#5E8F26" stroke="#0D0D0F" stroke-width="0.8" transform="rotate({r.randint(0, 180)} {f(x)} {f(y)})"></ellipse>')
    kx, ky, kr = w * 0.9, h * 0.86, min(w, h) * 0.07
    o.append(f'<circle cx="{f(kx)}" cy="{f(ky)}" r="{f(kr)}" fill="#0B1A2E" fill-opacity="0.6" stroke="#F3EFE6" stroke-width="1.6"></circle>'
             f'<path d="M{f(kx)} {f(ky - kr)} L {f(kx)} {f(ky + kr)} M{f(kx - kr)} {f(ky)} L {f(kx + kr)} {f(ky)}" stroke="#F3EFE6" stroke-width="1.2"></path>'
             + label(kx, ky - kr - 4, "N", "#F3EFE6", 10) + label(kx, ky + kr + 12, "S", "#FFD23F", 10))
    return "".join(o)

def rivers_sea(w, h, seed):
    """All the rivers run into the sea, yet the sea is not full: rivers winding down from the mountains to the sea, and the
    clouds over the sea going back to the mountains (dashed)."""
    r = random.Random(seed)
    o = [sky(w, h, "#7AB8D8", "#E8F6FA"),
         f'<path d="M-10 {f(h * 0.62)} L {f(w * 0.12)} {f(h * 0.2)} L {f(w * 0.22)} {f(h * 0.34)} L {f(w * 0.34)} {f(h * 0.14)} L {f(w * 0.5)} {f(h * 0.5)} L {f(w * 0.56)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#5A6A7A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.08)} {f(h * 0.28)} L {f(w * 0.12)} {f(h * 0.2)} L {f(w * 0.16)} {f(h * 0.27)} Z M{f(w * 0.3)} {f(h * 0.22)} L {f(w * 0.34)} {f(h * 0.14)} L {f(w * 0.39)} {f(h * 0.22)} Z" fill="#F3EFE6"></path>',
         ground(w, h, h * 0.62, "#7A9A5A", dy=4),
         f'<path d="M{f(w * 0.6)} {f(h * 0.6)} C {f(w * 0.7)} {f(h * 0.58)} {f(w * 0.85)} {f(h * 0.59)} {f(w + 10)} {f(h * 0.57)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.54)} {f(h + 10)} C {f(w * 0.58)} {f(h * 0.8)} {f(w * 0.56)} {f(h * 0.7)} {f(w * 0.6)} {f(h * 0.6)} Z" fill="#1F6F9A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for k in range(5):
        y = h * (0.66 + k * 0.07)
        o.append(f'<path d="M{f(w * 0.64 + k * 8)} {f(y)} q 12 -6 24 0 t 24 0 M{f(w * 0.82)} {f(y + 10)} q 12 -6 24 0" stroke="#E8F6FA" stroke-width="2" fill="none"></path>')
    for k, (x0, y0) in enumerate([(0.14, 0.34), (0.3, 0.3), (0.44, 0.5)]):
        pts = f"M{f(w * x0)} {f(h * y0)} C {f(w * (x0 + 0.04))} {f(h * (y0 + 0.2))} {f(w * (x0 + 0.2))} {f(h * 0.7)} {f(w * 0.58)} {f(h * (0.66 + k * 0.06))}"
        o.append(f'<path d="{pts}" stroke="#0D0D0F" stroke-width="{f(7 + k * 2)}" fill="none"></path><path d="{pts}" stroke="#2C9DB8" stroke-width="{f(4 + k * 2)}" fill="none"></path>')
    for k in range(3):
        x, y = w * (0.66 + k * 0.1), h * (0.18 + (k % 2) * 0.06)
        o.append(f'<g fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"><ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * 0.06)}" ry="{f(h * 0.04)}"></ellipse><ellipse cx="{f(x + w * 0.04)}" cy="{f(y - h * 0.02)}" rx="{f(w * 0.04)}" ry="{f(h * 0.035)}"></ellipse></g>')
    o.append(route([(w * 0.78, h * 0.5), (w * 0.76, h * 0.3)], color="#F3EFE6", sw=2, dash="5 5")
             + route([(w * 0.62, h * 0.16), (w * 0.44, h * 0.1), (w * 0.26, h * 0.1)], color="#F3EFE6", sw=2, dash="5 5"))
    for _ in range(14):
        x = r.uniform(w * 0.08, w * 0.36); y = r.uniform(h * 0.04, h * 0.14)
        o.append(f'<path d="M{f(x)} {f(y)} l -3 10" stroke="#2C7DA8" stroke-width="1.6"></path>')
    return "".join(o)

def ruins(w, h, seed):
    """There is no remembrance of the former generations: broken columns and walls half buried in the sand, a low sun."""
    r = random.Random(seed)
    o = [sky(w, h, "#C88A5A", "#F3D8A0"), sun(w * 0.8, h * 0.5, max(12, h * 0.06), color="#FFE680", op=0.3),
         hills(w, h, h * 0.62, seed, color="#C8A06A", amp=14, step=90)]
    base = h * 0.78
    for k, (x, ht, bw) in enumerate([(0.14, 0.34, 0.05), (0.24, 0.22, 0.05), (0.62, 0.4, 0.06), (0.74, 0.18, 0.06)]):
        X, W2 = w * x, w * bw; top = base - h * ht
        jag = f"L {f(X + W2)} {f(top + 6)} L {f(X + W2 * 0.6)} {f(top - 4)} L {f(X + W2 * 0.3)} {f(top + 8)} L {f(X)} {f(top)}"
        o.append(f'<path d="M{f(X)} {f(base)} L {f(X + W2)} {f(base)} {jag} Z" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2"></path>'
                 + "".join(f'<path d="M{f(X + W2 * q)} {f(base)} L {f(X + W2 * q)} {f(top + 10)}" stroke="#B8A880" stroke-width="1.6"></path>' for q in (0.33, 0.66)))
    o.append(f'<path d="M{f(w * 0.36)} {f(base)} L {f(w * 0.36)} {f(base - h * 0.2)} C {f(w * 0.36)} {f(base - h * 0.32)} {f(w * 0.5)} {f(base - h * 0.32)} {f(w * 0.5)} {f(base - h * 0.2)} L {f(w * 0.5)} {f(base - h * 0.12)} L {f(w * 0.47)} {f(base - h * 0.2)} C {f(w * 0.47)} {f(base - h * 0.27)} {f(w * 0.39)} {f(base - h * 0.27)} {f(w * 0.39)} {f(base - h * 0.2)} L {f(w * 0.39)} {f(base)} Z" fill="#D8C8A0" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(f'<g transform="rotate(-8 {f(w * 0.86)} {f(base)})"><rect x="{f(w * 0.8)}" y="{f(base - h * 0.06)}" width="{f(w * 0.2)}" height="{f(h * 0.06)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2"></rect></g>')
    o.append(f'<path d="M-10 {f(base - 6)} C {f(w * 0.2)} {f(base - 20)} {f(w * 0.4)} {f(base + 6)} {f(w * 0.6)} {f(base - 12)} C {f(w * 0.8)} {f(base - 24)} {f(w * 0.9)} {f(base)} {f(w + 10)} {f(base - 8)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></path>')
    for _ in range(12):
        x, y = r.uniform(0, w), r.uniform(base, h)
        o.append(f'<path d="M{f(x)} {f(y)} q {f(w * 0.04)} -6 {f(w * 0.08)} 0" stroke="#C8A06A" stroke-width="1.6" fill="none"></path>')
    return "".join(o)

def crooked(w, h, seed=1):
    """That which is crooked cannot be made straight; and that which is wanting cannot be numbered: a blueprint — a crooked
    rod above a straight rule, and a row of tally cells with the last ones empty."""
    o = [bp(w, h)]
    x0, x1 = w * 0.1, w * 0.9; y = h * 0.28
    pts = [(x0 + (x1 - x0) * k / 8, y + (h * 0.07) * (1 if k % 2 else -1) * (0 if k in (0, 8) else 1)) for k in range(9)]
    o.append(f'<path d="M' + " L ".join(f"{f(a)} {f(b)}" for a, b in pts) + f'" stroke="#0D0D0F" stroke-width="9" fill="none" stroke-linejoin="round"></path>'
             f'<path d="M' + " L ".join(f"{f(a)} {f(b)}" for a, b in pts) + f'" stroke="{GOLD}" stroke-width="5" fill="none" stroke-linejoin="round"></path>')
    ry = h * 0.5
    o.append(f'<rect x="{f(x0)}" y="{f(ry - 8)}" width="{f(x1 - x0)}" height="16" fill="none" stroke="{CYAN}" stroke-width="2"></rect>'
             + "".join(f'<path d="M{f(x0 + (x1 - x0) * k / 20)} {f(ry - 8)} L {f(x0 + (x1 - x0) * k / 20)} {f(ry - (2 if k % 5 else -2))}" stroke="{CYAN}" stroke-width="1.4"></path>' for k in range(21)))
    o.append(f'<path d="M{f(w * 0.5)} {f(y + h * 0.1)} L {f(w * 0.5)} {f(ry - 16)}" stroke="#D7261E" stroke-width="2" stroke-dasharray="4 4"></path>'
             f'<path d="M{f(w * 0.5 - 10)} {f((y + ry) / 2 - 10)} L {f(w * 0.5 + 10)} {f((y + ry) / 2 + 10)} M{f(w * 0.5 + 10)} {f((y + ry) / 2 - 10)} L {f(w * 0.5 - 10)} {f((y + ry) / 2 + 10)}" stroke="#D7261E" stroke-width="3"></path>')
    n = 10; cw = (x1 - x0) / n; cy = h * 0.72
    for k in range(n):
        cx = x0 + k * cw
        if k < 7:
            o.append(f'<rect x="{f(cx + 4)}" y="{f(cy)}" width="{f(cw - 8)}" height="{f(h * 0.16)}" fill="{GOLD}" fill-opacity="0.2" stroke="{GOLD}" stroke-width="1.6"></rect>'
                     + "".join(f'<path d="M{f(cx + cw * (0.3 + q * 0.12))} {f(cy + h * 0.03)} L {f(cx + cw * (0.3 + q * 0.12))} {f(cy + h * 0.13)}" stroke="{GOLD}" stroke-width="2"></path>' for q in range(4)))
        else:
            o.append(f'<rect x="{f(cx + 4)}" y="{f(cy)}" width="{f(cw - 8)}" height="{f(h * 0.16)}" fill="none" stroke="#4A7A9A" stroke-width="1.6" stroke-dasharray="5 4"></rect>'
                     + label(cx + cw / 2, cy + h * 0.1, "?", "#4A7A9A", 14))
    return "".join(o)

# ---- Ecclesiastes 2 -----------------------------------------------------------------------------------------------------
def jar(x, y, s=1.0, color="#B5652E"):
    """A wine jar standing on (x, y)."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-10 -60 L -10 -52 C -26 -46 -28 -20 -16 -4 L -8 0 L 8 0 L 16 -4 C 28 -20 26 -46 10 -52 L 10 -60 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M-10 -52 C -18 -54 -20 -44 -12 -42 M10 -52 C 18 -54 20 -44 12 -42" stroke="#0D0D0F" stroke-width="2" fill="none"></path></g>')

def feast_hall(p, w, h, seed):
    """Mirth: a cedar hall with the table set, wine jars, singers with harp and timbrel, a lamp."""
    from genesis.art4 import clay_lamp
    b = h * 0.94; k = min(1.2, h / 330)
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.8), S3.table(w * 0.56, b, w * 0.42, k)]
    for i in range(3): o.append(jar(w * (0.84 + i * 0.05), b, k * 0.8, ["#B5652E", "#8A3A1E", "#C87A3E"][i]))
    s = min(fit(b, max(h * 0.2, b - 230)), k * 0.9)
    o.append(S3.musician(p, w * 0.1, b, s, kind="harp", cloth="#C2456A", woman=True) + S3.musician(p, w * 0.22, b, s * 0.96, kind="timbrel", cloth="#E8A317", woman=True, seed=seed))
    o.append(S3.notes(w * 0.2, b - 250 * s, 6, seed) + clay_lamp(w * 0.62, b - 150 * k, min(1.0, h / 300)))
    return "".join(o)

def works(p, w, h, seed, wind=False):
    """I made me great works: houses on the hill, terraced vineyards, gardens and parks with trees of all kinds of fruit,
    and a great pool of water; the Preacher in the foreground (wind=True: the same under a grey sky, the wind blowing over
    it all — a striving after wind)."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2" if not wind else "#6A6A7A", "#F3E8C8" if not wind else "#B8B0A8"),
         hills(w, h, h * 0.36, seed, color="#7A9A5A" if not wind else "#6A7A5A", amp=12, step=90), J.city_hill(w * 0.78, h * 0.5, w * 0.36, h * 0.22, seed)]
    for row in range(4):
        y = h * (0.42 + row * 0.04)
        o.append(f'<path d="M-10 {f(y + 4)} C {f(w * 0.2)} {f(y - 6)} {f(w * 0.4)} {f(y + 6)} {f(w * 0.56)} {f(y)}" stroke="#4A6A2A" stroke-width="2" fill="none"></path>'
                 + "".join(f'<circle cx="{f(w * (0.02 + q * 0.05))}" cy="{f(y + 1 - 3 * math.sin(q))}" r="4" fill="#3F8A44" stroke="#0D0D0F" stroke-width="0.8"></circle>' for q in range(11)))
    o.append(ground(w, h, h * 0.58, "#9CB86A" if not wind else "#8A9A6A", dy=0))
    for i in range(5):
        o.append(tree(w * (0.04 + i * 0.07), h * (0.74 + (i % 2) * 0.04), min(0.6, h / 600), color=["#3F8A44", "#2E6A32", "#5E8F26"][i % 3], lean=0.4 if wind else 0, seed=seed + i))
    px0, px1, py0, py1 = w * 0.38, w * 0.74, h * 0.68, h * 0.86
    o.append(f'<path d="M{f(px0 + 20)} {f(py0)} L {f(px1 - 20)} {f(py0)} L {f(px1)} {f(py1)} L {f(px0)} {f(py1)} Z" fill="#A89A82" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(px0 + 30)} {f(py0 + 8)} L {f(px1 - 30)} {f(py0 + 8)} L {f(px1 - 12)} {f(py1 - 8)} L {f(px0 + 12)} {f(py1 - 8)} Z" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(px0 + 50 + q * 40)} {f(py0 + 20 + (q % 2) * 16)} l 20 0" stroke="#E8F6FA" stroke-width="2"></path>' for q in range(int((px1 - px0 - 100) / 40))))
    b = h * 0.97
    o.append(preacher(p, w * 0.88, b, fit(b, max(h * 0.5, b - 200)), flip=True))
    if wind: o.append(wind_lines(w, h, seed, n=12, color="#E8E2D6", op=0.8))
    return "".join(o)

def possessions(p, w, h, seed):
    """Men-servants and maid-servants, herds and flocks, silver and gold and the treasure of kings, men-singers and women-
    singers: flocks and kine on the hills, heaps of silver and gold, singers beside them."""
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.42, seed, color="#8AA06A", amp=10, step=80), ground(w, h, h * 0.56, "#B8A86A", dy=0)]
    r = random.Random(seed)
    for i in range(9):
        o.append(E.sheep(w * r.uniform(0.02, 0.4), h * r.uniform(0.5, 0.62), min(0.5, h / 700), flip=r.random() < 0.5))
    for i in range(3):
        o.append(S1.cow(w * (0.12 + i * 0.12), h * (0.74 + (i % 2) * 0.04), min(0.5, h / 700), flip=i % 2 == 1))
    b = h * 0.95
    o.append(R1.heap(w * 0.62, b, w * 0.16, h * 0.14, color="#C8C8D0") + JG2.silver(w * 0.62, b - h * 0.08, 8, seed, spread=w * 0.06)
             + R1.heap(w * 0.8, b, w * 0.16, h * 0.16, color="#E8B830"))
    s = fit(b, max(h * 0.4, b - 200))
    o.append(S3.musician(p, w * 0.5, b, s * 0.9, kind="harp", cloth="#2C7DA8", woman=False) + S3.musician(p, w * 0.94, b, s * 0.86, kind="timbrel", cloth="#C2456A", woman=True, seed=seed))
    return "".join(o)

def light_dark(p, w, h, seed):
    """Wisdom excelleth folly, as far as light excelleth darkness: the wise man walking in the sun on the left, the fool
    stumbling in the night on the right, on the one road."""
    gid = f"ld{p}"
    b = h * 0.92
    o = [mk.defs(p, *ALL), hgrad(gid, [(0, "#FFE680"), (0.45, "#FFC14D"), (0.55, "#1E1650"), (1, "#0B0B2A")]),
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{gid})"></rect>', sun(w * 0.16, h * 0.24, max(12, h * 0.07), color="#FFF4C2", op=0.4),
         mk.stars(30, w * 0.45, h * 0.6, seed).replace("<g ", f'<g transform="translate({f(w * 0.55)} 0)" ', 1),
         ground(w, h, h * 0.78, "#C8A06A", dy=0), f'<rect x="{f(w * 0.5)}" y="{f(h * 0.78)}" width="{f(w * 0.6)}" height="{f(h * 0.3)}" fill="#1A1430" stroke="#0D0D0F" stroke-width="2"></rect>']
    s = fit(b, max(h * 0.36, b - 210))
    o.append(man(p, w * 0.28, b, s, "#E8E2D6") + f'<g opacity="0.85">{E.kneel(w * 0.76, b, s * 0.8, color="#2A2440", skin="#1A1430", flip=True)}</g>')
    o.append(f'<path d="M{f(w * 0.86)} {f(b - 4)} l 30 -10 l 12 10 Z" fill="#2A2440" stroke="#0D0D0F" stroke-width="1.6"></path>')
    return "".join(o)

def heir(p, w, h, seed):
    """I must leave it unto the man that shall be after me: the cedar hall with the empty throne and the crown laid on its
    seat, the Preacher going out at the left, a young man coming in at the bright door on the right."""
    b = h * 0.94; k = min(1.2, h / 300)
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.82),
         f'<rect x="{f(w * 0.78)}" y="{f(h * 0.2)}" width="{f(w * 0.16)}" height="{f(h * 0.62)}" fill="#FFE680" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         V.rays(w * 0.86, h * 0.5, 16, 10, w * 0.3, color="#FFF4C2", op=0.25), S3.throne(w * 0.48, b, k), S2.crown(w * 0.48, b - 84 * k, 0.6 * k)]
    s = fit(b, max(h * 0.3, b - 220))
    o.append(f'<g opacity="0.75">{preacher(p, w * 0.12, b, s)}</g>' + man(p, w * 0.86, b, s * 0.96, "#B5421E", flip=True))
    return "".join(o)

def sleepless(p, w, h, seed):
    """Even in the night his heart taketh no rest: a dark chamber, the moon at the window, one lamp burning, and a man lying
    awake on his bed."""
    from genesis.art4 import clay_lamp
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1430"></rect>',
         S3.window(w * 0.7, h * 0.2, w * 0.14, h * 0.3, inner="#0B0B2A"), f'<circle cx="{f(w * 0.72)}" cy="{f(h * 0.3)}" r="{f(min(w, h) * 0.04)}" fill="#F3EFE6"></circle>',
         ground(w, h, h * 0.84, "#2A2238", dy=0), bed(w, h, w * 0.08, w * 0.56, b, cover=SOL_C, head="#B98A6E", hair="#8A847A"),
         f'<circle cx="{f(w * 0.82)}" cy="{f(h * 0.8)}" r="{f(min(w, h) * 0.22)}" fill="#FFC14D" opacity="0.12"></circle>', clay_lamp(w * 0.82, h * 0.84, min(1.0, h / 300))]
    return "".join(o)

# ---- Ecclesiastes 3 -----------------------------------------------------------------------------------------------------
def _w(ref, a, b=None): return G.v(ref, frm=a, to=b or a)
TIMES = [(_w("3:2", "born"), _w("3:2", "die")), (_w("3:2", "plant"), _w("3:2", "pluck up")),
         (_w("3:3", "kill"), _w("3:3", "heal")), (_w("3:3", "break down"), _w("3:3", "build up")),
         (_w("3:4", "weep"), _w("3:4", "laugh")), (_w("3:4", "mourn"), _w("3:4", "dance")),
         (_w("3:5", "cast away stones"), _w("3:5", "gather stones")), (_w("3:5", "embrace"), _w("3:5", "refrain")),
         (_w("3:6", "seek"), _w("3:6", "lose")), (_w("3:6", "keep"), _w("3:6", "cast away")),
         (_w("3:7", "rend"), _w("3:7", "sew")), (_w("3:7", "keep silence"), _w("3:7", "speak")),
         (_w("3:8", "love"), _w("3:8", "hate")), (_w("3:8", "war"), _w("3:8", "peace"))]

def seasons(w, h, lit=range(14), top=None):
    """A time to every purpose under heaven: fourteen cells in a ring, each a pair (a time to … / a time to …), the cells
    of the verses beside them lit; a sun half day, half night in the middle."""
    o = [grid_bg(w, h, color="#2A2A5A", bg="#12113A")]
    mx, my, mb = w * 0.04, top or h * 0.05, max(h * 0.05, 28)
    cw = (w - 2 * mx) / 5 - 10; chh = min(52, (h - my - mb) / 4 - 10)
    xs = [mx + 5 + cw / 2 + k * (cw + 10) for k in range(5)]
    ys = [my + 5 + chh / 2 + k * ((h - my - mb - chh - 10) / 3) for k in range(4)]
    pos = [(xs[k], ys[0]) for k in range(5)] + [(xs[4], ys[1]), (xs[4], ys[2])] + [(xs[k], ys[3]) for k in range(4, -1, -1)] + [(xs[0], ys[2]), (xs[0], ys[1])]
    o.append(route(pos + [pos[0]], color="#4A4A8A", sw=2, dash="6 6", arrow=False))
    cx, cy = w * 0.5, (ys[1] + ys[2]) / 2
    rr = min((ys[2] - ys[1]) * 0.5 + chh * 0.3, w * 0.12)
    o.append(f'<path d="M{f(cx)} {f(cy - rr)} A {f(rr)} {f(rr)} 0 0 0 {f(cx)} {f(cy + rr)} Z" fill="#FFD23F" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(cx)} {f(cy - rr)} A {f(rr)} {f(rr)} 0 0 1 {f(cx)} {f(cy + rr)} Z" fill="#1E1650" stroke="#0D0D0F" stroke-width="2"></path>'
             + mk.stars(10, rr * 0.7, rr * 1.2, 7).replace("<g ", f'<g transform="translate({f(cx + rr * 0.15)} {f(cy - rr * 0.6)})" ', 1))
    for k in range(12):
        a = math.radians(90 + k * 15)
        o.append(f'<path d="M{f(cx + rr * 1.15 * math.cos(a))} {f(cy - rr * 1.15 * math.sin(a))} L {f(cx + rr * 1.4 * math.cos(a))} {f(cy - rr * 1.4 * math.sin(a))}" stroke="#FFE680" stroke-width="2.4" stroke-linecap="round"></path>')
    fs = max(8, min(11, cw / 12))
    for i, (a, b) in enumerate(TIMES):
        x, y = pos[i]
        on = i in lit
        o.append(f'<rect x="{f(x - cw / 2)}" y="{f(y - chh / 2)}" width="{f(cw)}" height="{f(chh)}" rx="6" fill="{"#0B0B2A" if on else "#16163A"}" stroke="{GOLD if on else "#3A3A6A"}" stroke-width="{2 if on else 1.4}"></rect>'
                 + label(x, y - 3, a.upper(), GOLD if on else "#5A5A8A", min(fs, cw * 0.9 / (len(a) * 0.74))) + label(x, y + fs + 2, b.upper(), ROSE if on else "#5A5A8A", min(fs, cw * 0.9 / (len(b) * 0.74))))
    return "".join(o)

def eternity(p, w, h, seed):
    """He hath set eternity in their heart: the night sky full of stars over a hill, the Preacher small on the hilltop
    looking up."""
    b = h * 0.8
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#2A1E5A"), mk.stars(160, w, h * 0.8, seed),
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.3)}" rx="{f(w * 0.7)}" ry="{f(h * 0.08)}" fill="#CFE0FF" opacity="0.12" transform="rotate(-14 {f(w * 0.5)} {f(h * 0.3)})"></ellipse>',
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.86)} C {f(w * 0.2)} {f(h * 0.82)} {f(w * 0.4)} {f(b)} {f(w * 0.56)} {f(b)} C {f(w * 0.72)} {f(b)} {f(w * 0.86)} {f(h * 0.86)} {f(w + 10)} {f(h * 0.9)} L {f(w + 10)} {f(h + 10)} Z" fill="#0D0B1A" stroke="#0D0D0F" stroke-width="2"></path>']
    s = fit(b, max(h * 0.5, b - 140))
    o.append(preacher(p, w * 0.56, b + 2, s, flip=True, up=[(-22, -158), (-36, -196), (-40, -232)]))
    return "".join(o)

def scales(x, y, s=1.0, tilt=0):
    """A pair of scales on a post, the beam tilted by `tilt` degrees."""
    a = math.radians(tilt); dx, dy = 100 * math.cos(a), 100 * math.sin(a)
    pan = lambda px, py: (f'<path d="M{f(px)} {f(py)} L {f(px - 34)} {f(py + 60)} M{f(px)} {f(py)} L {f(px + 34)} {f(py + 60)}" stroke="#5A3A22" stroke-width="1.6"></path>'
                          f'<path d="M{f(px - 40)} {f(py + 60)} C {f(px - 30)} {f(py + 78)} {f(px + 30)} {f(py + 78)} {f(px + 40)} {f(py + 60)} Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="2"></path>')
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-40 0 L 40 0 L 10 -10 L 10 -170 L -10 -170 L -10 -10 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<path d="M{f(-dx)} {f(-170 - dy)} L {f(dx)} {f(-170 + dy)}" stroke="#0D0D0F" stroke-width="8" stroke-linecap="round"></path><path d="M{f(-dx)} {f(-170 - dy)} L {f(dx)} {f(-170 + dy)}" stroke="#E8B830" stroke-width="4" stroke-linecap="round"></path>'
            + pan(-dx, -170 - dy) + pan(dx, -170 + dy) + '</g>')

def justice(p, w, h, seed):
    """In the place of justice, wickedness was there: the judgment seat empty in the gate under a red sky, the scales tilted."""
    b = h * 0.92
    o = [sky(w, h, "#3A0A1A", "#C8402A"), S4.gatehouse(w * 0.5, b, w * 0.8, h * 0.72), ground(w, h, b, "#5A3A3A", dy=0),
         S3.throne(w * 0.5, b, min(1.0, h / 330)), scales(w * 0.2, b, min(0.9, h / 330), tilt=-16)]
    return "".join(o)

def man_beast(p, w, h, seed):
    """That which befalleth the sons of men befalleth beasts; all are of the dust: a man, an ox and sheep side by side on a
    plain at dusk, the dust blowing over them, one road to the horizon."""
    r = random.Random(seed)
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#4A2A4A", "#E8A06A"), sun(w * 0.5, h * 0.52, max(10, h * 0.05), color="#FF8A3D", op=0.3),
         hills(w, h, h * 0.56, seed, color="#6A4A4A", amp=6, step=90), ground(w, h, h * 0.6, "#A8805A", dy=0),
         f'<path d="M{f(w * 0.48)} {f(h * 0.6)} L {f(w * 0.52)} {f(h * 0.6)} L {f(w * 0.7)} {f(h + 10)} L {f(w * 0.3)} {f(h + 10)} Z" fill="#C8A07A" stroke="#0D0D0F" stroke-width="1.6"></path>']
    s = fit(b, max(h * 0.36, b - 200))
    o.append(man(p, w * 0.18, b, s, "#8A6A4A") + S1.cow(w * 0.82, b, min(0.8, s * 0.9), flip=True, color="#8A6A4A", patch="#C8B8A0") + E.sheep(w * 0.62, b, s * 0.5) + E.sheep(w * 0.38, b - 4, s * 0.45, flip=True))
    for _ in range(14):
        x, y = r.uniform(0, w), r.uniform(h * 0.3, h * 0.9)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * r.uniform(0.04, 0.12))}" ry="{f(h * 0.02)}" fill="#C8A07A" opacity="0.35"></ellipse>')
    return "".join(o)

# ---- Ecclesiastes 4 -----------------------------------------------------------------------------------------------------
ROD_UP = '<path d="M-64 -190 L -96 -250" stroke="#3A2214" stroke-width="5" stroke-linecap="round"></path>'

def oppressed(p, w, h, seed):
    """The tears of such as were oppressed, and they had no comforter: bowed figures at their labor among the stacks of a
    brick field at dusk, an overseer standing over them with his rod raised — on the side of the oppressors there was power."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#4A2A3A", "#C86A4A"), hills(w, h, h * 0.5, seed, color="#6A3A3A", amp=8, step=90), ground(w, h, h * 0.6, "#A8704A", dy=0)]
    for x in (0.08, 0.5, 0.62):
        for row in range(3):
            for col in range(3 - row):
                bx = w * x + col * 22 + row * 11; by = h * 0.66 - row * 12
                o.append(f'<rect x="{f(bx)}" y="{f(by)}" width="20" height="11" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    s = fit(b, max(h * 0.34, b - 210))
    for i in range(4):
        o.append(E.kneel(w * (0.12 + i * 0.15), b - (i % 2) * 4, s * 0.72, color=["#5A4A3A", "#4A3A3A", "#6A5A4A", "#3A3A4A"][i], skin="#3A1E14"))
    o.append(man(p, w * 0.86, b, s * 1.05, "#E8E2D6", flip=True, up=[(-22, -158), (-46, -176), (-64, -190)], extra=ROD_UP))
    return "".join(o)

def handful(w, h, seed):
    """Better is a handful, with quietness, than two handfuls with labor and striving after wind: on the left, in the still
    blue, one bowl of grain at rest; on the right, two bowls heaped and spilling, the wind tearing the grain away."""
    r = random.Random(seed)
    gid = f"hf{seed}"
    o = [hgrad(gid, [(0, "#2A4A6A"), (0.48, "#3A5A7A"), (0.52, "#6A4A3A"), (1, "#8A5A3A")]),
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{gid})"></rect>',
         f'<rect x="-10" y="{f(h * 0.78)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A1E1A" stroke="#0D0D0F" stroke-width="2"></rect>']
    bw = min(w * 0.2, h * 0.5)
    o.append(R1.heap(w * 0.25, h * 0.78 - bw * 0.3 + 4, bw * 0.7, bw * 0.28) + J1.bowl(w * 0.25, h * 0.78, bw, full=False))
    for x in (0.64, 0.84):
        o.append(R1.heap(w * x, h * 0.78 - bw * 0.3 + 4, bw * 0.9, bw * 0.62) + J1.bowl(w * x, h * 0.78, bw, full=False))
    for _ in range(8):
        x = r.uniform(w * 0.52, w * 0.9); y = r.uniform(h * 0.12, h * 0.55); L = r.uniform(w * 0.1, w * 0.2)
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x + L * 0.4)} {f(y - 10)} {f(x + L * 0.7)} {f(y + 8)} {f(x + L)} {f(y - 4)}" stroke="#F3E0C0" stroke-width="2.4" fill="none" stroke-linecap="round" opacity="0.75"></path>')
    for _ in range(40):
        x = r.uniform(w * 0.6, w * 1.0); y = r.uniform(h * 0.2, h * 0.7)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="2.6" ry="1.4" fill="#E8C88A" transform="rotate({r.randint(0, 180)} {f(x)} {f(y)})"></ellipse>')
    return "".join(o)

def alone(p, w, h, seed):
    """One that is alone, and he hath not a second: a man by himself at night at a table heaped with silver, one lamp, the
    benches about him empty."""
    from genesis.art4 import clay_lamp
    b = h * 0.94
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1430"></rect>',
         f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.62)}" r="{f(max(w, h) * 0.34)}" fill="#FFC14D" opacity="0.1"></circle>', ground(w, h, h * 0.8, "#2A2238", dy=0)]
    s = fit(b, max(h * 0.3, b - 220))
    o.append(man(p, w * 0.5, b, s, "#6A2A3A", extra=GREY_BEARD))
    tx0, tx1, ty = w * 0.3, w * 0.7, b - 80 * s
    o.append(f'<rect x="{f(tx0)}" y="{f(ty)}" width="{f(tx1 - tx0)}" height="{f(12 * s)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<path d="M{f(tx0 + 10)} {f(ty + 12 * s)} L {f(tx0 + 16)} {f(b)} M{f(tx1 - 10)} {f(ty + 12 * s)} L {f(tx1 - 16)} {f(b)}" stroke="#5A3A22" stroke-width="{f(6 * s)}"></path>')
    o.append(JG2.silver(w * 0.42, ty - 5, 9, seed, spread=w * 0.05) + JG2.silver(w * 0.58, ty - 8, 9, seed + 1, spread=w * 0.05) + clay_lamp(w * 0.66, ty - 2, min(0.8, s)))
    for x in (0.1, 0.82):
        o.append(f'<rect x="{f(w * x)}" y="{f(b - 46 * s)}" width="{f(w * 0.08)}" height="{f(8 * s)}" fill="#5A3A22" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 f'<path d="M{f(w * x + 6)} {f(b - 38 * s)} L {f(w * x + 6)} {f(b)} M{f(w * (x + 0.08) - 6)} {f(b - 38 * s)} L {f(w * (x + 0.08) - 6)} {f(b)}" stroke="#3A2214" stroke-width="4"></path>')
    return "".join(o)

def two_better(p, w, h, seed):
    """If they fall, the one will lift up his fellow: two travellers on a stony road in the hills, one fallen, the other
    stooping to lift him up."""
    r = random.Random(seed)
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.44, seed, color="#8A9A6A", amp=16, step=80), ground(w, h, h * 0.58, "#B89A6A", dy=0),
         f'<path d="M{f(w * 0.56)} {f(h * 0.58)} L {f(w * 0.62)} {f(h * 0.58)} L {f(w * 0.9)} {f(h + 10)} L {f(w * 0.2)} {f(h + 10)} Z" fill="#C8B08A" stroke="#0D0D0F" stroke-width="1.6"></path>']
    for _ in range(14):
        x, y = r.uniform(w * 0.2, w * 0.9), r.uniform(h * 0.7, h)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(r.uniform(5, 12))}" ry="{f(r.uniform(3, 6))}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="1.2"></ellipse>')
    s = fit(b, max(h * 0.34, b - 210))
    o.append(E.kneel(w * 0.56, b, s * 0.8, color="#3A5A8A", skin="#5A2A16", flip=True))
    o.append(mk.person(p, round(w * 0.36), round(b), round(s, 3), body=SKIN, cloth="#8A3A1E", kind="Tunic", sw=3, flip=True, up=[(-22, -158), (-46, -120), (-74, -104)]))
    return "".join(o)

def threefold(w, h, seed):
    """A threefold cord is not quickly broken: three strands — gold, red and blue — twisted into one rope across the panel,
    and beneath it a single strand snapped."""
    o = [bp(w, h)]
    cy = h * 0.42; amp = min(h * 0.08, 26); x0, x1 = w * 0.06, w * 0.94
    cols = ["#E8B830", "#D7261E", "#1F5FAD"]
    n = 60
    for k in range(3):
        pts = [(x0 + (x1 - x0) * i / n, cy + amp * math.sin(i * 0.5 + k * 2.094)) for i in range(n + 1)]
        d = "M" + " L ".join(f"{f(a)} {f(c)}" for a, c in pts)
        o.append(f'<path d="{d}" stroke="#0D0D0F" stroke-width="{f(amp * 0.9 + 4)}" fill="none" stroke-linecap="round"></path><path d="{d}" stroke="{cols[k]}" stroke-width="{f(amp * 0.9)}" fill="none" stroke-linecap="round"></path>')
    sy = h * 0.8
    o.append(f'<path d="M{f(w * 0.12)} {f(sy)} L {f(w * 0.44)} {f(sy)}" stroke="#0D0D0F" stroke-width="10" stroke-linecap="round"></path><path d="M{f(w * 0.12)} {f(sy)} L {f(w * 0.44)} {f(sy)}" stroke="#E8B830" stroke-width="6" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.52)} {f(sy + 6)} L {f(w * 0.84)} {f(sy + 14)}" stroke="#0D0D0F" stroke-width="10" stroke-linecap="round"></path><path d="M{f(w * 0.52)} {f(sy + 6)} L {f(w * 0.84)} {f(sy + 14)}" stroke="#E8B830" stroke-width="6" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.46)} {f(sy - 12)} l 8 10 l -6 4 l 8 12" stroke="#D7261E" stroke-width="2.4" fill="none"></path>')
    return "".join(o)

def youth_king(p, w, h, seed):
    """Better is a poor and wise youth than an old and foolish king: on the left the old king alone on his throne in a dim
    hall; on the right the prison door open and the youth come out into the light, all the people following after him."""
    b = h * 0.94; k = min(1.1, h / 340)
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, h * 0.8, "#B89A6A", dy=0),
         f'<rect x="-10" y="-10" width="{f(w * 0.42 + 10)}" height="{f(h + 20)}" fill="#2A1E2A"></rect>',
         f'<rect x="-10" y="{f(h * 0.8)}" width="{f(w * 0.42 + 10)}" height="{f(h)}" fill="#3A2A2A" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<path d="M{f(w * 0.42)} -10 L {f(w * 0.42)} {f(h + 10)}" stroke="#0D0D0F" stroke-width="4"></path>', S3.throne(w * 0.18, b, k)]
    s = fit(b, max(h * 0.32, b - 220))
    o.append(old_king(p, w * 0.18, b - 38 * k, s * 0.86))
    gx = w * 0.52
    o.append(f'<rect x="{f(gx - w * 0.06)}" y="{f(b - h * 0.5)}" width="{f(w * 0.12)}" height="{f(h * 0.5)}" fill="#5A5A62" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<rect x="{f(gx - w * 0.035)}" y="{f(b - h * 0.36)}" width="{f(w * 0.07)}" height="{f(h * 0.36)}" fill="#1A1214" stroke="#0D0D0F" stroke-width="2"></rect>'
             + "".join(f'<path d="M{f(gx - w * 0.03 + q * w * 0.015)} {f(b - h * 0.48)} L {f(gx - w * 0.03 + q * w * 0.015)} {f(b - h * 0.4)}" stroke="#0D0D0F" stroke-width="2"></path>' for q in range(5)))
    o.append(man(p, w * 0.64, b, s, "#E8D8B0", flip=True))
    o.append(crowd_at(p, w, h, seed, w * 0.72, w * 0.98, h * 0.82, b, 7, s * 0.7, s * 0.95, flip=True))
    return "".join(o)

# ---- Ecclesiastes 5 -----------------------------------------------------------------------------------------------------
def house_of_god(p, w, h, seed):
    """Keep thy foot when thou goest to the house of God: the house above its court, a man coming quietly to it, the smoke
    of the altar rising."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), temple_front(w * 0.56, h * 0.62, w * 0.5, seed), ground(w, h, h * 0.62, "#C8B88A", dy=0),
         horned_altar(w * 0.24, h * 0.8, min(0.6, h / 500), fire=True, seed=seed)]
    s = fit(b, max(h * 0.4, b - 200))
    o.append(man(p, w * 0.8, b, s, "#5A6A8A", flip=True))
    return "".join(o)

def vow(p, w, h, seed):
    """When thou vowest a vow unto God, defer not to pay it: a man kneeling before the altar with his offering in a bowl,
    the fire burning (God is never drawn)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#2A1A3A", "#E8A06A"), mk.stars(30, w, h * 0.4, seed), ground(w, h, h * 0.8, "#8A6A5A", dy=0)]
    ax, k = w * 0.6, min(1.1, h / 300)
    for i in range(4):
        o.append(f'<path d="M{f(ax + (i - 1.5) * 12)} {f(b - 130 * k)} C {f(ax - 40 + i * 20)} {f(h * 0.5)} {f(ax + 40 - i * 10)} {f(h * 0.3)} {f(ax + (i - 1.5) * 30)} -10" stroke="#C8C2D6" stroke-width="{f(10 + i * 4)}" fill="none" opacity="{0.3 - i * 0.05:.2f}"></path>')
    o.append(horned_altar(ax, b, k, fire=True, seed=seed))
    s = fit(b, max(h * 0.4, b - 220))
    o.append(E.kneel(w * 0.28, b, s * 0.85, color="#2C5F9A", skin="#5A2A16"))
    return "".join(o)

def field_king(p, w, h, seed):
    """The profit of the earth is for all: the king himself is served by the field — reapers in the ripe field, sheaves,
    and the king standing at its edge, his house on the hill above it."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.36, seed, color="#9AA06A", amp=10, step=90),
         J.city_hill(w * 0.76, h * 0.44, w * 0.36, h * 0.2, seed), R1.field(-10, w + 10, h * 0.5, h * 0.4, seed, rows=4)]
    s = fit(b, max(h * 0.4, b - 210))
    for i in range(3): o.append(R1.reaper(p, w * (0.14 + i * 0.22), b - (i % 2) * h * 0.04, s * (0.9 + 0.05 * i), cloth=["#8A6A4A", "#6A4A2A", "#5A6A3A"][i]))
    for i in range(3): o.append(R1.sheaf(w * (0.24 + i * 0.22), b, s * 0.7))
    o.append(king_fig(p, w * 0.9, b, s * 0.95, flip=True, cloth=SOL_C))
    return "".join(o)

def sleep_two(p, w, h, seed):
    """The sleep of a laboring man is sweet; the fulness of the rich will not suffer him to sleep: on the left a laborer
    asleep on his mat under the stars, his mattock beside him; on the right a rich man's chamber, the lamp burning, the
    silver heaped, the man standing awake."""
    from genesis.art4 import clay_lamp
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="#14123A"></rect>', mk.stars(40, w * 0.48, h * 0.6, seed),
         f'<circle cx="{f(w * 0.36)}" cy="{f(h * 0.2)}" r="{f(min(w, h) * 0.04)}" fill="#F3EFE6"></circle>',
         f'<rect x="{f(w * 0.5)}" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="#5A3A2A"></rect>',
         f'<rect x="-10" y="{f(h * 0.82)}" width="{f(w * 0.5 + 10)}" height="{f(h)}" fill="#3A3A2A" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<rect x="{f(w * 0.5)}" y="{f(h * 0.82)}" width="{f(w * 0.5 + 10)}" height="{f(h)}" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<path d="M{f(w * 0.5)} -10 L {f(w * 0.5)} {f(h + 10)}" stroke="#0D0D0F" stroke-width="4"></path>',
         f'<circle cx="{f(w * 0.66)}" cy="{f(h * 0.6)}" r="{f(min(w, h) * 0.3)}" fill="#FFC14D" opacity="0.14"></circle>']
    k = min(1.0, h / 300)
    o.append(J1.rug_sleeper(w * 0.24, h * 0.9, k, color="#8A6A4A") + f'<path d="M{f(w * 0.38)} {f(h * 0.9)} L {f(w * 0.44)} {f(h * 0.72)}" stroke="#5A3A22" stroke-width="5"></path>')
    s = fit(b, max(h * 0.34, b - 210))
    o.append(R1.heap(w * 0.66, b, w * 0.14, h * 0.12, color="#C8C8D0") + JG2.silver(w * 0.66, b - h * 0.08, 7, seed, spread=w * 0.04) + clay_lamp(w * 0.58, h * 0.56, k * 0.9)
             + man(p, w * 0.86, b, s, "#7A2A6A", flip=True, extra=GREY_BEARD))
    return "".join(o)

def naked_road(p, w, h, seed):
    """Naked shall he go again as he came, and shall take nothing for his labor: a man walking away down the long road into
    the sunset, his hands empty, his heaped silver left behind by the way."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#4A2A4A", "#FF9A4A"), sun(w * 0.62, h * 0.5, max(12, h * 0.07), color="#FFD23F", op=0.35),
         hills(w, h, h * 0.54, seed, color="#5A3A4A", amp=8, step=80), ground(w, h, h * 0.58, "#8A6A5A", dy=0),
         f'<path d="M{f(w * 0.6)} {f(h * 0.58)} L {f(w * 0.64)} {f(h * 0.58)} L {f(w * 0.82)} {f(h + 10)} L {f(w * 0.36)} {f(h + 10)} Z" fill="#B8906A" stroke="#0D0D0F" stroke-width="1.6"></path>']
    o.append(man(p, w * 0.63, h * 0.76, fit(h * 0.76, h * 0.54), "#E8E2D6"))
    o.append(R1.heap(w * 0.24, b, w * 0.16, h * 0.12, color="#C8C8D0") + JG2.silver(w * 0.24, b - h * 0.07, 9, seed, spread=w * 0.05) + R1.heap(w * 0.1, b, w * 0.1, h * 0.08, color="#E8B830"))
    return "".join(o)

# ---- Ecclesiastes 6 -----------------------------------------------------------------------------------------------------
def alien_eats(p, w, h, seed):
    """A man to whom God giveth riches, yet giveth him not power to eat thereof, but an alien eateth it: a stranger at the
    laden table, the owner standing apart with empty hands."""
    b = h * 0.94; k = min(1.2, h / 330)
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.82), S3.window(w * 0.3, h * 0.24, w * 0.12, h * 0.22, inner="#E8A06A"), S3.window(w * 0.7, h * 0.24, w * 0.12, h * 0.22, inner="#E8A06A")]
    for i in range(3): o.append(jar(w * (0.78 + i * 0.05), b, k * 0.7, ["#B5652E", "#8A3A1E", "#C87A3E"][i]))
    s = min(fit(b, max(h * 0.3, b - 220)), k)
    o.append(man(p, w * 0.5, b, s * 0.9, "#2C7DA8", extra=A.headcloth("#E8A317")) + S3.table(w * 0.5, b, w * 0.4, k) + man(p, w * 0.12, b, s, "#7A2A6A", extra=GREY_BEARD))
    return "".join(o)

def one_place(p, w, h, seed):
    """Do not all go to one place? Paths from every side of the plain running together toward one dark gate on the
    horizon at dusk, small figures walking on them."""
    o = [mk.defs(p, *ALL), sky(w, h, "#2A1A3A", "#C87A5A"), ground(w, h, h * 0.42, "#6A5A4A", dy=0)]
    gx, gy = w * 0.5, h * 0.42
    for x in (-0.1, 0.12, 0.32, 0.68, 0.88, 1.1):
        o.append(f'<path d="M{f(w * x - w * 0.04)} {f(h + 10)} L {f(gx - w * 0.01)} {f(gy)} L {f(gx + w * 0.01)} {f(gy)} L {f(w * x + w * 0.04)} {f(h + 10)} Z" fill="#9A8060" stroke="#0D0D0F" stroke-width="1.2"></path>')
    o.append(f'<path d="M{f(gx - w * 0.05)} {f(gy)} L {f(gx - w * 0.05)} {f(gy - h * 0.14)} C {f(gx - w * 0.05)} {f(gy - h * 0.22)} {f(gx + w * 0.05)} {f(gy - h * 0.22)} {f(gx + w * 0.05)} {f(gy - h * 0.14)} L {f(gx + w * 0.05)} {f(gy)} Z" fill="#0D0B14" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(gx - w * 0.09)} {f(gy)} L {f(gx - w * 0.09)} {f(gy - h * 0.18)} L {f(gx - w * 0.06)} {f(gy - h * 0.2)} L {f(gx - w * 0.06)} {f(gy)} Z M{f(gx + w * 0.06)} {f(gy)} L {f(gx + w * 0.06)} {f(gy - h * 0.2)} L {f(gx + w * 0.09)} {f(gy - h * 0.18)} L {f(gx + w * 0.09)} {f(gy)} Z" fill="#3A2A3A" stroke="#0D0D0F" stroke-width="2"></path>')
    for k, x in enumerate((0.12, 0.32, 0.68, 0.88)):
        t = 0.5
        fx, fy = w * x + (gx - w * x) * t, h - (h - gy) * t
        o.append(man(p, fx, fy, fit(fy, fy - h * 0.14), ["#5A4A6A", "#6A4A3A", "#3A4A5A", "#5A3A3A"][k], flip=x > 0.5))
    return "".join(o)

def shadow(p, w, h, seed):
    """All the days of his vain life which he spendeth as a shadow: a man standing alone on the plain at sunset, his long
    shadow stretched behind him across the ground."""
    b = h * 0.86
    o = [mk.defs(p, *ALL), sky(w, h, "#5A2A4A", "#FFB04A"), sun(w * 0.86, h * 0.6, max(12, h * 0.06), color="#FF6A2A", op=0.35),
         hills(w, h, h * 0.6, seed, color="#6A3A3A", amp=6, step=90), ground(w, h, h * 0.64, "#C8905A", dy=0)]
    s = fit(b, max(h * 0.38, b - 200))
    x = w * 0.62
    o.append(f'<path d="M{f(x - 14 * s)} {f(b)} L {f(x + 14 * s)} {f(b)} L {f(x - w * 0.5)} {f(b + h * 0.1)} L {f(x - w * 0.62)} {f(b + h * 0.08)} Z" fill="#3A1E1A" opacity="0.7"></path>')
    o.append(man(p, x, b, s, "#5A4A6A"))
    return "".join(o)

# ---- Ecclesiastes 7 -----------------------------------------------------------------------------------------------------
def flask(x, y, s=1.0, color="#E8E2D6"):
    """An alabaster flask of precious oil standing on (x, y)."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-6 -70 L -6 -56 C -24 -50 -26 -12 -14 -2 L 14 -2 C 26 -12 24 -50 6 -56 L 6 -70 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'
            '<rect x="-9" y="-78" width="18" height="9" rx="2" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.6"></rect><path d="M-14 -36 C -6 -40 6 -40 14 -36" stroke="#C8B8A0" stroke-width="2" fill="none"></path></g>')

def two_houses(p, w, h, seed):
    """The house of mourning and the house of feasting: on the left a house at dusk, its door dark, mourners sitting with
    covered heads before it; on the right a house with lit windows, music and lamps; between them a flask of precious oil."""
    b = h * 0.92
    gid = f"th{p}"
    o = [mk.defs(p, *ALL), hgrad(gid, [(0, "#2A2A3A"), (0.5, "#5A4A5A"), (0.5, "#E8A04A"), (1, "#FFD890")]),
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{gid})"></rect>', ground(w, h, h * 0.8, "#6A5A4A", dy=0)]
    for x0, lit in ((0.06, False), (0.58, True)):
        X, W2, top = w * x0, w * 0.36, h * 0.36
        o.append(f'<rect x="{f(X)}" y="{f(top)}" width="{f(W2)}" height="{f(h * 0.44)}" fill="{"#8A7A6A" if not lit else "#E8D0A0"}" stroke="#0D0D0F" stroke-width="2.4"></rect>'
                 f'<rect x="{f(X - 6)}" y="{f(top - 10)}" width="{f(W2 + 12)}" height="12" fill="{"#5A4A3A" if not lit else "#C8A070"}" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<rect x="{f(X + W2 * 0.4)}" y="{f(h * 0.56)}" width="{f(W2 * 0.2)}" height="{f(h * 0.24)}" fill="{"#1A1214" if not lit else "#FFE680"}" stroke="#0D0D0F" stroke-width="2"></rect>'
                 + "".join(f'<rect x="{f(X + W2 * q)}" y="{f(h * 0.44)}" width="{f(W2 * 0.12)}" height="{f(h * 0.07)}" fill="{"#2A2228" if not lit else "#FFD23F"}" stroke="#0D0D0F" stroke-width="1.6"></rect>' for q in (0.12, 0.76)))
    s = fit(b, max(h * 0.44, b - 170))
    for i in range(3):
        o.append(E.kneel(w * (0.1 + i * 0.1), b, s * 0.62, color=["#3A3440", "#2A2A36", "#4A4250"][i], skin="#2A1A14"))
    o.append(S3.notes(w * 0.76, h * 0.26, 5, seed) + flask(w * 0.5, b, min(1.2, h / 260)))
    return "".join(o)

def thorns_pot(w, h, seed):
    """As the crackling of thorns under a pot, so is the laughter of the fool: a clay pot on three stones over a quick fire
    of thorns, sparks flying."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1214"></rect>',
         f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.7)}" r="{f(max(w, h) * 0.4)}" fill="#FF8A3D" opacity="0.12"></circle>', ground(w, h, h * 0.86, "#2A1E1A", dy=0)]
    cx, by = w * 0.5, h * 0.86; k = min(1.4, h / 260)
    for _ in range(9):
        a = r.uniform(-0.8, 0.8); L = r.uniform(30, 60) * k
        o.append(f'<path d="M{f(cx + r.uniform(-50, 50) * k)} {f(by)} l {f(L * math.sin(a))} {f(-L * 0.4)} l {f(8 * k)} {f(-6 * k)} M{f(cx + r.uniform(-40, 40) * k)} {f(by - 4)} l {f(-6 * k)} {f(-10 * k)}" stroke="#5A3A22" stroke-width="2.4" fill="none"></path>')
    o.append(E.blaze(cx, by, 120 * k, 70 * k, seed, n=7))
    for dx in (-56, 0, 56):
        o.append(f'<ellipse cx="{f(cx + dx * k)}" cy="{f(by - 6 * k)}" rx="{f(14 * k)}" ry="{f(9 * k)}" fill="#6A6460" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    o.append(f'<path d="M{f(cx - 70 * k)} {f(by - 70 * k)} C {f(cx - 80 * k)} {f(by - 20 * k)} {f(cx + 80 * k)} {f(by - 20 * k)} {f(cx + 70 * k)} {f(by - 70 * k)} L {f(cx + 50 * k)} {f(by - 110 * k)} L {f(cx - 50 * k)} {f(by - 110 * k)} Z" fill="#8A4A2A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(cx)}" cy="{f(by - 110 * k)}" rx="{f(50 * k)}" ry="{f(10 * k)}" fill="#5A2A16" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    for _ in range(26):
        x, y = cx + r.uniform(-w * 0.4, w * 0.4), by - r.uniform(20, h * 0.8)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(1.2, 3))}" fill="{r.choice(["#FFD23F", "#FF8A3D", "#FFF4C2"])}"></circle>')
    o.append(f'<text x="{f(w * 0.78)}" y="{f(h * 0.4)}" font-family="Noto Sans JP, sans-serif" font-weight="900" font-size="{f(min(40, h * 0.12))}" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.6" transform="rotate(-8 {f(w * 0.78)} {f(h * 0.4)})">パチパチ</text>')
    return "".join(o)

def defence(p, w, h, seed):
    """Wisdom is a defence, even as money is a defence: a walled city on its hill in the sun, its gate shut, and a chest
    of silver laid up within."""
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), sun(w * 0.84, h * 0.2, max(12, h * 0.06), color="#FFE680", op=0.4),
         hills(w, h, h * 0.64, seed, color="#8A9A6A", amp=8, step=90), J.jericho(w * 0.08, w * 0.92, h * 0.3, h * 0.8, seed, towers=4, houses=True),
         ground(w, h, h * 0.8, "#B89A6A", dy=0)]
    o.append(R1.heap(w * 0.16, h * 0.96, w * 0.14, h * 0.1, color="#C8C8D0") + JG2.silver(w * 0.16, h * 0.9, 7, seed, spread=w * 0.04))
    return "".join(o)

def day_night(w, h, seed):
    """In the day of prosperity be joyful, and in the day of adversity consider: God hath made the one side by side with
    the other — a sunny field on the left, a storm on the right, and between them a tree grown crooked."""
    r = random.Random(seed)
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"), sun(w * 0.18, h * 0.24, max(12, h * 0.07), color="#FFE680", op=0.4),
         f'<rect x="{f(w * 0.5)}" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="#3A3A4A"></rect>',
         ground(w, h, h * 0.76, "#9CB86A", dy=0), f'<rect x="{f(w * 0.5)}" y="{f(h * 0.76)}" width="{f(w * 0.5 + 10)}" height="{f(h)}" fill="#4A5A3A" stroke="#0D0D0F" stroke-width="2"></rect>']
    for i in range(5):
        x = w * (0.56 + i * 0.1)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(h * 0.14)}" rx="{f(w * 0.09)}" ry="{f(h * 0.08)}" fill="#1A1A2A"></ellipse>')
    for _ in range(30):
        x, y = r.uniform(w * 0.52, w), r.uniform(h * 0.2, h * 0.76)
        o.append(f'<path d="M{f(x)} {f(y)} l -5 14" stroke="#8FB0D0" stroke-width="1.6"></path>')
    o.append(f'<path d="M{f(w * 0.72)} {f(h * 0.2)} l -14 {f(h * 0.14)} l 16 0 l -22 {f(h * 0.2)}" stroke="#FFF4C2" stroke-width="4" fill="none"></path>')
    tx, ty = w * 0.5, h * 0.78; k = min(1.2, h / 300)
    o.append(f'<path d="M{f(tx)} {f(ty)} C {f(tx - 30 * k)} {f(ty - 40 * k)} {f(tx + 40 * k)} {f(ty - 70 * k)} {f(tx - 10 * k)} {f(ty - 110 * k)} C {f(tx - 40 * k)} {f(ty - 140 * k)} {f(tx + 30 * k)} {f(ty - 160 * k)} {f(tx + 10 * k)} {f(ty - 190 * k)}" stroke="#0D0D0F" stroke-width="{f(14 * k)}" fill="none" stroke-linecap="round"></path>'
             f'<path d="M{f(tx)} {f(ty)} C {f(tx - 30 * k)} {f(ty - 40 * k)} {f(tx + 40 * k)} {f(ty - 70 * k)} {f(tx - 10 * k)} {f(ty - 110 * k)} C {f(tx - 40 * k)} {f(ty - 140 * k)} {f(tx + 30 * k)} {f(ty - 160 * k)} {f(tx + 10 * k)} {f(ty - 190 * k)}" stroke="#6A4A2A" stroke-width="{f(9 * k)}" fill="none" stroke-linecap="round"></path>')
    for dx, dy in ((-20, -200), (30, -186), (10, -220), (-34, -170)):
        o.append(f'<circle cx="{f(tx + dx * k)}" cy="{f(ty + dy * k)}" r="{f(22 * k)}" fill="#3F7A44" stroke="#0D0D0F" stroke-width="1.8"></circle>')
    return "".join(o)

def ten_rulers(p, w, h, seed):
    """Wisdom is a strength to the wise man more than ten rulers that are in a city: the ten rulers seated in the gate,
    and one wise man standing before them."""
    from exo.art import elder
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#E8C8A0", "#F3E0B0"), S4.gatehouse(w * 0.5, h * 0.84, w * 0.9, h * 0.7), ground(w, h, h * 0.84, "#B8A07A", dy=0)]
    s = fit(b, max(h * 0.4, b - 200))
    for i in range(10):
        o.append(E.kneel(w * (0.06 + i * 0.075), h * 0.86, s * 0.5, color=["#5A4A3A", "#3A4A6A", "#6A5A3A", "#4A3A5A", "#5A5A3A"][i % 5], skin="#5A2A16"))
    o.append(elder("#F3EFE6", 2)(p, w * 0.5, b, s, flip=True))
    return "".join(o)

def deep_well(w, h, seed):
    """That which is, is far off and exceeding deep; who can find it out? A well as a cross-section: the shaft going down
    and down, a bucket on its rope far below, the water out of sight."""
    o = [bp(w, h)]
    cx = w * 0.5; ww = min(w * 0.14, 90); top = h * 0.12
    o.append(f'<path d="M{f(cx - ww)} {f(top)} L {f(cx - ww)} {f(h + 10)} M{f(cx + ww)} {f(top)} L {f(cx + ww)} {f(h + 10)}" stroke="{CYAN}" stroke-width="2.4"></path>')
    for k in range(int((h - top) / 18)):
        y = top + k * 18
        o.append(f'<path d="M{f(cx - ww - 16)} {f(y)} L {f(cx - ww)} {f(y)} M{f(cx + ww)} {f(y)} L {f(cx + ww + 16)} {f(y)}" stroke="#4A7A9A" stroke-width="1.2"></path>')
    gid = f"dw{seed}"
    o.append(hgrad(gid, [(0, "#0B1A2E"), (1, "#000000")], vertical=True)
             + f'<rect x="{f(cx - ww + 2)}" y="{f(h * 0.5)}" width="{f(ww * 2 - 4)}" height="{f(h)}" fill="url(#{gid})" opacity="0.9"></rect>')
    o.append(f'<path d="M{f(cx - ww - 30)} {f(top)} L {f(cx + ww + 30)} {f(top)}" stroke="{GOLD}" stroke-width="4"></path>'
             f'<path d="M{f(cx - ww - 20)} {f(top)} L {f(cx - ww - 20)} {f(top - 40)} L {f(cx + ww + 20)} {f(top - 40)} L {f(cx + ww + 20)} {f(top)}" stroke="{GOLD}" stroke-width="3" fill="none"></path>'
             f'<path d="M{f(cx)} {f(top - 40)} L {f(cx)} {f(h * 0.7)}" stroke="#E8C88A" stroke-width="2" stroke-dasharray="6 4"></path>'
             f'<path d="M{f(cx - 14)} {f(h * 0.7)} L {f(cx + 14)} {f(h * 0.7)} L {f(cx + 10)} {f(h * 0.7 + 20)} L {f(cx - 10)} {f(h * 0.7 + 20)} Z" fill="#8A5A30" stroke="#E8C88A" stroke-width="1.6"></path>'
             + dim(cx + ww + 50, top, cx + ww + 50, h * 0.96, "? CUBITS", size=10, color=CYAN))
    return "".join(o)

def snares(w, h, seed):
    """The woman whose heart is snares and nets, and whose hands are bands: a fowler's net spread on the ground with its
    pegs, a snare's noose set beside it, and coiled bands of cord — nothing caught."""
    r = random.Random(seed)
    o = [sky(w, h, "#5A4A5A", "#C8A080"), ground(w, h, h * 0.42, "#7A6A4A", dy=0)]
    x0, x1, y0, y1 = w * 0.08, w * 0.62, h * 0.52, h * 0.92
    for k in range(9):
        t = k / 8
        o.append(f'<path d="M{f(x0 + (x1 - x0) * t)} {f(y0)} L {f(x0 + (x1 - x0) * t - w * 0.04)} {f(y1)}" stroke="#2A1E14" stroke-width="1.8"></path>')
    for k in range(6):
        t = k / 5
        y = y0 + (y1 - y0) * t
        o.append(f'<path d="M{f(x0 - w * 0.04 * t)} {f(y)} L {f(x1 - w * 0.04 * t)} {f(y)}" stroke="#2A1E14" stroke-width="1.8"></path>')
    for x, y in ((x0, y0), (x1, y0), (x0 - w * 0.04, y1), (x1 - w * 0.04, y1)):
        o.append(f'<path d="M{f(x)} {f(y)} l 0 -14" stroke="#5A3A22" stroke-width="5"></path>')
    nx, ny = w * 0.8, h * 0.7; k = min(1.2, h / 300)
    o.append(f'<path d="M{f(nx)} {f(h * 0.94)} L {f(nx)} {f(ny - 70 * k)} C {f(nx + 40 * k)} {f(ny - 90 * k)} {f(nx + 60 * k)} {f(ny - 40 * k)} {f(nx + 20 * k)} {f(ny)}" stroke="#5A3A22" stroke-width="{f(5 * k)}" fill="none"></path>'
             f'<ellipse cx="{f(nx + 20 * k)}" cy="{f(ny + 20 * k)}" rx="{f(26 * k)}" ry="{f(12 * k)}" stroke="#2A1E14" stroke-width="2.4" fill="none"></ellipse>')
    for i in range(3):
        cx, cy = w * (0.7 + i * 0.1), h * 0.96
        o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(22 * k)}" ry="{f(8 * k)}" stroke="#8A6A3A" stroke-width="3" fill="none"></ellipse><ellipse cx="{f(cx)}" cy="{f(cy - 4)}" rx="{f(16 * k)}" ry="{f(6 * k)}" stroke="#8A6A3A" stroke-width="3" fill="none"></ellipse>')
    return "".join(o)

def thousand(w, h, seed):
    """One man among a thousand have I found: a thousand marks in a grid, one of them lit."""
    r = random.Random(seed)
    o = [bp(w, h)]
    cols, rows = 50, 20
    mx, my = w * 0.05, h * 0.08
    dx, dy = (w - 2 * mx) / (cols - 1), (h - 2 * my) / (rows - 1)
    lit = (r.randrange(cols), r.randrange(rows))
    rr = max(1.4, min(dx, dy) * 0.28)
    for i in range(cols):
        for j in range(rows):
            x, y = mx + i * dx, my + j * dy
            if (i, j) == lit:
                o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rr * 4)}" fill="{GOLD}" opacity="0.25"></circle><circle cx="{f(x)}" cy="{f(y)}" r="{f(rr * 1.8)}" fill="{GOLD}" stroke="#0D0D0F" stroke-width="1"></circle>')
            else:
                o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rr)}" fill="#4A7A9A"></circle>')
    return "".join(o)

# ---- Ecclesiastes 8 -----------------------------------------------------------------------------------------------------
def throne_room(p, w, h, seed):
    """Keep the king's command: the king on his throne in the cedar hall, a man bowed before him, the king's word going out."""
    b = h * 0.94; k = min(1.2, h / 320)
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.82), S3.window(w * 0.56, h * 0.26, w * 0.12, h * 0.24, inner="#8FD0E2"), S3.window(w * 0.84, h * 0.26, w * 0.12, h * 0.24, inner="#8FD0E2"),
         f'<rect x="{f(w * 0.18)}" y="{f(h * 0.08)}" width="{f(w * 0.24)}" height="{f(h * 0.5)}" fill="#7A1A2A" stroke="#0D0D0F" stroke-width="2"></rect>'
         f'<path d="M{f(w * 0.18)} {f(h * 0.58)} L {f(w * 0.3)} {f(h * 0.64)} L {f(w * 0.42)} {f(h * 0.58)}" fill="#7A1A2A" stroke="#0D0D0F" stroke-width="2"></path>'
         f'<rect x="{f(w * 0.18)}" y="{f(h * 0.08)}" width="{f(w * 0.24)}" height="10" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></rect>', S3.throne(w * 0.3, b, k)]
    s = min(fit(b, max(h * 0.3, b - 220)), k)
    o.append(king_fig(p, w * 0.3, b - 40 * k, s * 0.86, cloth="#7A1A2A"))
    o.append(E.kneel(w * 0.66, b, s * 0.8, color="#3A5A6A", skin="#5A2A16", flip=True) + man(p, w * 0.88, b, s, "#8A6A3A", flip=True, extra=E4.SPEAR))
    return "".join(o)

def tombs(w, h, seed):
    """I saw the wicked buried, and they came to the grave; and they that had done right were forgotten in the city: the
    sepulchres hewn in the hillside at dusk, their stones rolled to, the city far off."""
    o = [sky(w, h, "#3A2A4A", "#C88A6A"), J.city_hill(w * 0.82, h * 0.5, w * 0.3, h * 0.16, seed),
         f'<path d="M-10 {f(h * 0.4)} C {f(w * 0.3)} {f(h * 0.3)} {f(w * 0.5)} {f(h * 0.44)} {f(w * 0.66)} {f(h * 0.56)} L {f(w * 0.66)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A6A5A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.86, "#6A5A4A", dy=0)]
    for i, x in enumerate((0.08, 0.3, 0.5)):
        X, Y = w * x, h * (0.6 + i * 0.04); r_ = min(w, h) * 0.08
        o.append(f'<path d="M{f(X)} {f(Y + r_ * 1.4)} L {f(X)} {f(Y)} Q {f(X + r_)} {f(Y - r_)} {f(X + r_ * 2)} {f(Y)} L {f(X + r_ * 2)} {f(Y + r_ * 1.4)} Z" fill="#2A1E1E" stroke="#0D0D0F" stroke-width="2.4"></path>'
                 f'<circle cx="{f(X + r_ * 1.4)}" cy="{f(Y + r_ * 0.6)}" r="{f(r_ * 0.8)}" fill="#A89A8A" stroke="#0D0D0F" stroke-width="2.4"></circle>')
    return "".join(o)

def city_night(w, h, seed):
    """Neither day nor night seeth sleep with his eyes: the city at night under the stars, a lamp in every window."""
    r = random.Random(seed)
    o = [sky(w, h, "#05051A", "#2A1E5A"), mk.stars(80, w, h * 0.5, seed), f'<circle cx="{f(w * 0.2)}" cy="{f(h * 0.18)}" r="{f(min(w, h) * 0.05)}" fill="#F3EFE6"></circle>']
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.62)} C {f(w * 0.3)} {f(h * 0.5)} {f(w * 0.7)} {f(h * 0.5)} {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} Z" fill="#1A1626" stroke="#0D0D0F" stroke-width="2"></path>')
    for row in range(4):
        y0 = h * (0.56 + row * 0.1)
        for i in range(10):
            hx = w * (i / 9) + r.uniform(-14, 14) + (row % 2) * w * 0.05; hw = r.uniform(w * 0.07, w * 0.11); hh = h * r.uniform(0.06, 0.1)
            top = y0 - hh + 20 * abs(i / 9 - 0.5)
            o.append(f'<rect x="{f(hx - hw / 2)}" y="{f(top)}" width="{f(hw)}" height="{f(hh + h * 0.1)}" fill="{r.choice(["#2A2238", "#1E1A2E", "#3A2E44"])}" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                     + (f'<rect x="{f(hx - 5)}" y="{f(top + hh * 0.3)}" width="10" height="12" fill="#FFC14D"></rect>' if r.random() < 0.6 else ""))
    o.append(f'<rect x="-10" y="{f(h * 0.9)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A2030" stroke="#0D0D0F" stroke-width="2"></rect>'
             + "".join(f'<rect x="{x}" y="{f(h * 0.9 - 12)}" width="20" height="12" fill="#2A2030" stroke="#0D0D0F" stroke-width="1.4"></rect>' for x in range(-6, int(w), 36)))
    return "".join(o)

# ---- Ecclesiastes 9 -----------------------------------------------------------------------------------------------------
def dog(x, y, s=1.0, flip=False, color="#C8965A"):
    """A dog standing, its tail up."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            f'<path d="M-40 -40 C -40 -56 -20 -60 10 -58 L 30 -60 L 40 -84 L 52 -80 L 50 -66 L 66 -60 L 62 -50 L 40 -46 L 36 -36 L 34 0 L 26 0 L 24 -30 L -24 -30 L -26 0 L -34 0 L -36 -36 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.2" stroke-linejoin="round"></path>'
            f'<path d="M-38 -48 C -54 -60 -56 -78 -48 -88" stroke="#0D0D0F" stroke-width="7" fill="none" stroke-linecap="round"></path><path d="M-38 -48 C -54 -60 -56 -78 -48 -88" stroke="{color}" stroke-width="4" fill="none" stroke-linecap="round"></path>'
            '<circle cx="48" cy="-66" r="2.4" fill="#0D0D0F"></circle></g>')

def lion_lying(x, y, s=1.0, color="#9A8A7A"):
    """A lion lying still on its side in the shade, its eyes shut."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
            f'<path d="M-90 0 C -96 -30 -70 -46 -30 -46 L 40 -44 C 70 -42 80 -20 76 0 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.2"></path>'
            f'<path d="M-90 -6 C -110 -4 -124 2 -130 -8" stroke="#0D0D0F" stroke-width="5" fill="none"></path><circle cx="-132" cy="-9" r="6" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="1.4"></circle>'
            f'<path d="M36 -10 C 20 -40 36 -76 64 -76 C 92 -76 104 -44 92 -14 C 80 -4 50 -2 36 -10 Z" fill="#6A4A2E" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<path d="M50 -40 C 50 -56 72 -60 80 -46 L 90 -34 C 92 -24 82 -18 70 -20 C 58 -20 50 -28 50 -40 Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<path d="M68 -42 l 9 2" stroke="#0D0D0F" stroke-width="2"></path><circle cx="89" cy="-30" r="3" fill="#2A1A14"></circle>'
            f'<path d="M40 0 L 104 0 L 104 -8 L 44 -10 Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.8"></path></g>')

def dog_lion(w, h, seed):
    """A living dog is better than a dead lion: a dog standing in the sunlight on the left, a great lion lying still in the
    shadow of the rocks on the right."""
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"), sun(w * 0.14, h * 0.2, max(12, h * 0.06), color="#FFE680", op=0.4),
         f'<path d="M{f(w * 0.5)} {f(h * 0.8)} L {f(w * 0.56)} {f(h * 0.3)} L {f(w * 0.74)} {f(h * 0.2)} L {f(w * 0.96)} {f(h * 0.34)} L {f(w + 10)} {f(h * 0.8)} Z" fill="#6A5A5A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.8, "#C8A06A", dy=0), f'<path d="M{f(w * 0.52)} {f(h * 0.8)} L {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.44)} {f(h + 10)} Z" fill="#5A4A3A" opacity="0.5"></path>']
    k = min(1.3, h / 220)
    o.append(dog(w * 0.24, h * 0.92, k * 0.9) + lion_lying(w * 0.72, h * 0.92, k * 0.9))
    return "".join(o)

def white_garments(p, w, h, seed):
    """Eat thy bread with joy, and drink thy wine with a merry heart; let thy garments be always white: a man and his wife
    in white at their table under the vine, bread and a cup before them, the lamp lit and the day bright."""
    r = random.Random(seed)
    b = h * 0.94; k = min(1.2, h / 330)
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.5, seed, color="#8AA06A", amp=10, step=90), ground(w, h, h * 0.62, "#C8B88A", dy=0),
         f'<path d="M{f(w * 0.14)} {f(b)} L {f(w * 0.14)} {f(h * 0.18)} M{f(w * 0.86)} {f(b)} L {f(w * 0.86)} {f(h * 0.18)} M{f(w * 0.1)} {f(h * 0.18)} L {f(w * 0.9)} {f(h * 0.18)}" stroke="#5A3A22" stroke-width="7"></path>']
    for _ in range(26):
        x, y = r.uniform(w * 0.1, w * 0.9), h * r.uniform(0.1, 0.26)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * 0.04)}" ry="{f(h * 0.03)}" fill="{r.choice(["#3F8A44", "#2E6A32", "#5E8F26"])}" stroke="#0D0D0F" stroke-width="1.2"></ellipse>')
    for _ in range(5):
        x, y = r.uniform(w * 0.2, w * 0.8), h * r.uniform(0.24, 0.3)
        o.append(N.grapes(x, y, min(0.5, h / 700), seed=r.randint(1, 99)))
    s = min(fit(b, max(h * 0.36, b - 210)), k)
    o.append(man(p, w * 0.32, b, s, "#F3EFE6") + woman(p, w * 0.68, b, s * 0.94, "#F3EFE6", flip=True) + S3.table(w * 0.5, b, w * 0.3, k * 0.8))
    return "".join(o)

def race(p, w, h, seed):
    """The race is not to the swift, nor the battle to the strong; but time and chance happeneth to them all: runners on a
    track, the swiftest fallen, a slower one running on."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.5, seed, color="#8A9A6A", amp=8, step=90), ground(w, h, h * 0.6, "#C8A06A", dy=0),
         f'<path d="M-10 {f(h * 0.72)} L {f(w + 10)} {f(h * 0.7)} M-10 {f(h * 0.98)} L {f(w + 10)} {f(h * 0.96)}" stroke="#F3EFE6" stroke-width="3" stroke-dasharray="14 10"></path>']
    s = fit(b, max(h * 0.4, b - 200))
    o.append(S4.runner(p, w * 0.42, b, s, flip=True, cloth="#E8D8B0") + S4.runner(p, w * 0.2, b - h * 0.04, s * 0.92, flip=True, cloth="#8A5A30")
             + E.kneel(w * 0.72, b, s * 0.78, color="#D7261E", skin="#3A1E14", flip=True))
    o.append(f'<path d="M{f(w * 0.9)} {f(h * 0.6)} L {f(w * 0.9)} {f(b)}" stroke="#F3EFE6" stroke-width="4"></path><path d="M{f(w * 0.9)} {f(h * 0.6)} L {f(w * 0.98)} {f(h * 0.63)} L {f(w * 0.9)} {f(h * 0.66)} Z" fill="#D7261E" stroke="#0D0D0F" stroke-width="1.6"></path>')
    return "".join(o)

def nets(w, h, seed):
    """As the fishes that are taken in an evil net, and as the birds that are caught in the snare: a fishing net drawn up
    from the water full of fish on the left; a fowler's snare closed upon a bird on the right."""
    r = random.Random(seed)
    o = [sky(w, h, "#8FB8D0", "#E8E0C8"), f'<rect x="-10" y="{f(h * 0.5)}" width="{f(w * 0.56)}" height="{f(h)}" fill="#1F6F9A" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<path d="M{f(w * 0.54)} {f(h * 0.5)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.5)} {f(h + 10)} Z" fill="#9AA06A" stroke="#0D0D0F" stroke-width="2"></path>']
    nx, ny, nw, nh = w * 0.06, h * 0.56, w * 0.4, h * 0.36
    o.append(f'<path d="M{f(nx)} {f(ny)} C {f(nx + nw * 0.1)} {f(ny + nh)} {f(nx + nw * 0.9)} {f(ny + nh)} {f(nx + nw)} {f(ny)} Z" fill="#0F4C68" stroke="#E8E2D6" stroke-width="2"></path>')
    for k in range(1, 8):
        x = nx + nw * k / 8
        o.append(f'<path d="M{f(x)} {f(ny)} L {f(nx + nw / 2 + (x - nx - nw / 2) * 0.5)} {f(ny + nh * 0.9)}" stroke="#E8E2D6" stroke-width="1.2" opacity="0.8"></path>')
    for k in range(1, 4):
        y = ny + nh * k / 4
        o.append(f'<path d="M{f(nx + nw * 0.06 * k)} {f(y)} L {f(nx + nw - nw * 0.06 * k)} {f(y)}" stroke="#E8E2D6" stroke-width="1.2" opacity="0.8"></path>')
    for _ in range(8):
        x, y = nx + r.uniform(nw * 0.2, nw * 0.8), ny + r.uniform(nh * 0.2, nh * 0.6)
        o.append(f'<path d="M{f(x - 14)} {f(y)} C {f(x - 6)} {f(y - 8)} {f(x + 8)} {f(y - 8)} {f(x + 12)} {f(y)} C {f(x + 8)} {f(y + 8)} {f(x - 6)} {f(y + 8)} {f(x - 14)} {f(y)} Z M{f(x + 12)} {f(y)} l 8 -6 l 0 12 Z" fill="#C8D8E0" stroke="#0D0D0F" stroke-width="1.2"></path>')
    sx, sy = w * 0.78, h * 0.62; k = min(1.2, h / 260)
    o.append(f'<path d="M{f(sx)} {f(h * 0.94)} L {f(sx)} {f(sy - 60 * k)} C {f(sx + 30 * k)} {f(sy - 80 * k)} {f(sx + 50 * k)} {f(sy - 40 * k)} {f(sx + 16 * k)} {f(sy)}" stroke="#5A3A22" stroke-width="{f(5 * k)}" fill="none"></path>'
             f'<path d="M{f(sx + 4 * k)} {f(sy + 10 * k)} C {f(sx + 10 * k)} {f(sy - 4 * k)} {f(sx + 30 * k)} {f(sy - 4 * k)} {f(sx + 36 * k)} {f(sy + 8 * k)} L {f(sx + 50 * k)} {f(sy + 2 * k)} L {f(sx + 40 * k)} {f(sy + 16 * k)} C {f(sx + 30 * k)} {f(sy + 24 * k)} {f(sx + 10 * k)} {f(sy + 24 * k)} {f(sx + 4 * k)} {f(sy + 10 * k)} Z" fill="#8A6A5A" stroke="#0D0D0F" stroke-width="1.6"></path>'
             f'<path d="M{f(sx + 14 * k)} {f(sy + 6 * k)} C {f(sx + 6 * k)} {f(sy - 14 * k)} {f(sx + 26 * k)} {f(sy - 20 * k)} {f(sx + 28 * k)} {f(sy + 4 * k)}" fill="#6A4A3A" stroke="#0D0D0F" stroke-width="1.4"></path>'
             f'<ellipse cx="{f(sx + 22 * k)}" cy="{f(sy + 12 * k)}" rx="{f(22 * k)}" ry="{f(9 * k)}" stroke="#2A1E14" stroke-width="2.4" fill="none"></ellipse>')
    o.append(birds(4, w * 0.6, w * 0.95, h * 0.1, h * 0.3, seed))
    return "".join(o)

def little_city(p, w, h, seed):
    """There was a little city, and few men within it; and there came a great king against it, and besieged it, and built
    great bulwarks against it: the small walled city on its hill, the great king's camp and siege-mounds all round, and on
    its wall a poor wise man."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#C8B8A0", "#F3E0B0"), ground(w, h, h * 0.6, "#A8905A", dy=0),
         f'<path d="M{f(w * 0.3)} {f(h * 0.62)} C {f(w * 0.36)} {f(h * 0.4)} {f(w * 0.64)} {f(h * 0.4)} {f(w * 0.7)} {f(h * 0.62)} Z" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         J.jericho(w * 0.38, w * 0.62, h * 0.3, h * 0.46, seed, towers=2, houses=True)]
    for x in (0.12, 0.84):
        o.append(f'<path d="M{f(w * x - w * 0.1)} {f(h * 0.62)} L {f(w * x)} {f(h * 0.5)} L {f(w * x + w * 0.1)} {f(h * 0.62)} Z" fill="#6A5A3A" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<rect x="{f(w * x - w * 0.02)}" y="{f(h * 0.36)}" width="{f(w * 0.04)}" height="{f(h * 0.16)}" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(N.camp(14, w * 0.02, w * 0.98, h * 0.66, h * 0.86, seed))
    s = fit(h * 0.32, h * 0.2)
    o.append(man(p, w * 0.5, h * 0.32, s, "#8A7A6A", up=[(-22, -158), (-36, -196), (-40, -232)]))
    o.append(warriors_row(p, w, h, b, seed))
    return "".join(o)

# ---- Ecclesiastes 10 ----------------------------------------------------------------------------------------------------
import snake as SN
from genesis.art3 import STAFF, HOLD_STAFF

def ointment(w, h, seed):
    """Dead flies cause the oil of the perfumer to send forth an evil odor: the perfumer's jar with its lid off, dead flies
    on the rim and in the oil, the scent rising dark."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A2A"></rect>', ground(w, h, h * 0.84, "#5A4A3A", dy=0)]
    k = min(1.6, h / 220); cx, by = w * 0.5, h * 0.86
    o.append(f'<g transform="translate({f(cx)} {f(by)}) scale({f(k)})"><path d="M-30 -96 L -30 -84 C -64 -76 -70 -20 -44 -2 L 44 -2 C 70 -20 64 -76 30 -84 L 30 -96 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2.4"></path>'
             '<ellipse cx="0" cy="-96" rx="32" ry="8" fill="#C8A040" stroke="#0D0D0F" stroke-width="2"></ellipse><path d="M-50 -40 C -20 -48 20 -48 50 -40" stroke="#C8B8A0" stroke-width="3" fill="none"></path></g>')
    for i in range(4):
        x = cx + (i - 1.5) * 30 * k; y = by - 100 * k - r.uniform(-4, 4)
        o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k * 1.1)}) rotate({r.randint(150, 210)})"><ellipse cx="0" cy="0" rx="6" ry="4" fill="#1A1214"></ellipse><ellipse cx="-4" cy="-5" rx="5" ry="3" fill="#8A9AAA" opacity="0.7"></ellipse><ellipse cx="4" cy="-5" rx="5" ry="3" fill="#8A9AAA" opacity="0.7"></ellipse></g>')
    for i in range(3):
        o.append(f'<path d="M{f(cx + (i - 1) * 18 * k)} {f(by - 110 * k)} C {f(cx + (i - 1) * 40 * k)} {f(by - 160 * k)} {f(cx - (i - 1) * 30 * k)} {f(by - 200 * k)} {f(cx + (i - 1) * 50 * k)} {f(by - 260 * k)}" stroke="#4A5A3A" stroke-width="{f(8 * k)}" fill="none" opacity="0.6"></path>')
    return "".join(o)

def servants_horses(p, w, h, seed):
    """I have seen servants upon horses, and princes walking like servants upon the earth: servants riding high on the road,
    and princes with their crowns going on foot in the dust behind."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#E8C8A0", "#F3E0B0"), hills(w, h, h * 0.5, seed, color="#A8906A", amp=10, step=90), ground(w, h, h * 0.6, "#C8A06A", dy=0)]
    k = min(1.0, h / 320)
    for i in range(2):
        x = w * (0.62 + i * 0.22)
        sh = k * 0.9
        o.append(mk.person(p, round(x + 8 * sh), round(b - 52 * sh), round(sh * 0.66, 3), body="#3A1E14", cloth="#8A7A5A", kind="Tunic") + E3.horse(x, b, sh, color=["#3A2214", "#6A4A2A"][i], flip=True))
    s = fit(b, max(h * 0.4, b - 190))
    for i in range(3):
        o.append(king_fig(p, w * (0.1 + i * 0.12), b, s * 0.9, cloth=["#7A1A2A", "#1F3A7A", "#5A2A6A"][i], flip=True))
    return "".join(o)

def hazards(w, h, seed=1):
    """He that diggeth a pit shall fall into it; whoso breaketh through a wall, a serpent shall bite him; whoso heweth out
    stones, he that cleaveth wood; the blunt iron; the serpent before it is charmed: a plate of six cells."""
    o = [grid_bg(w, h, color="#3A2A5A", bg="#1A1430")]
    cw, ch = w / 3, h / 2
    def cell(i, g, ref):
        cx, cy = cw * (i % 3) + cw / 2, ch * (i // 3) + ch / 2 + 6; s = min(cw, ch) / 130
        return (f'<rect x="{f(cw * (i % 3) + 6)}" y="{f(ch * (i // 3) + 6)}" width="{f(cw - 12)}" height="{f(ch - 12)}" fill="none" stroke="#5A4A8A" stroke-width="1.4"></rect>'
                + f'<g transform="translate({f(cx)} {f(cy)}) scale({f(s)})">{g}</g>' + label(cw * (i % 3) + 16, ch * (i // 3) + 22, ref, GOLD, 9, "start"))
    pit = ('<path d="M-60 -10 L 60 -10" stroke="#C8A06A" stroke-width="4"></path><path d="M-40 -10 L -30 50 L 30 50 L 40 -10 Z" fill="#0D0B14" stroke="#C8A06A" stroke-width="3"></path>'
           '<path d="M-6 -60 L -6 -24 M-16 -34 L -6 -24 L 4 -34" stroke="#FF8A6A" stroke-width="3" fill="none"></path>')
    wall = "".join(f'<rect x="{-60 + (r % 2) * 14 + c * 28}" y="{-50 + r * 18}" width="26" height="16" fill="#8A6A4A" stroke="#E8C88A" stroke-width="1.4"></rect>' for r in range(5) for c in range(4) if not (r in (1, 2) and c == 2))
    wall += SN.snake([(16, -18), (28, -24), (40, -16), (50, -26)], 8, f"hz{seed}", head_scale=0.7)
    stones = '<path d="M-50 40 L -40 0 L 0 -10 L 30 10 L 40 40 Z" fill="#8A8478" stroke="#E8E2D6" stroke-width="2"></path><path d="M10 -30 L 30 -50 L 50 -40" stroke="#C8C2B6" stroke-width="5" fill="none"></path><path d="M30 -50 L 34 -20" stroke="#5A3A22" stroke-width="6"></path>'
    wood = '<rect x="-50" y="10" width="100" height="30" rx="12" fill="#8A5A30" stroke="#E8C88A" stroke-width="2"></rect><path d="M0 10 L 0 -10" stroke="#E8C88A" stroke-width="3"></path><path d="M-6 -60 L 30 -10" stroke="#5A3A22" stroke-width="6"></path><path d="M24 -14 L 44 -24 L 40 0 Z" fill="#A8A8B8" stroke="#E8E2D6" stroke-width="1.6"></path>'
    iron = '<path d="M-50 20 L 30 -20" stroke="#5A3A22" stroke-width="8"></path><path d="M24 -36 L 54 -40 L 50 -2 L 26 -10 Z" fill="#8A8A9A" stroke="#E8E2D6" stroke-width="2"></path><rect x="-40" y="34" width="70" height="14" rx="5" fill="#6A6A7A" stroke="#E8E2D6" stroke-width="1.6"></rect>'
    charm = SN.snake([(-40, 40), (-20, 30), (0, 40), (10, 10), (0, -20), (14, -40)], 10, f"hc{seed}", head_scale=0.8) + '<path d="M30 30 C 40 10 60 10 56 -14" stroke="#E8B830" stroke-width="4" fill="none"></path>'
    for i, (g, ref) in enumerate([(pit, "10:8"), (wall, "10:8"), (stones, "10:9"), (wood, "10:9"), (iron, "10:10"), (charm, "10:11")]):
        o.append(cell(i, g, ref))
    return "".join(o)

def child_king(p, w, h, seed):
    """Woe to thee, O land, when thy king is a child, and thy princes eat in the morning: a child on the great throne, the
    princes at the feast table in the early light."""
    b = h * 0.94; k = min(1.2, h / 320)
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.82), S3.window(w * 0.5, h * 0.2, w * 0.12, h * 0.22, inner="#FFD8A0"), S3.throne(w * 0.16, b, k)]
    s = min(fit(b, max(h * 0.3, b - 220)), k)
    o.append(S1.boy(p, w * 0.16, b - 40 * k, s * 0.6, extra=S3.KING))
    for i in range(3):
        o.append(man(p, w * (0.46 + i * 0.16), b, s * 0.92, ["#5A2A6A", "#2C5F9A", "#8A3A1E"][i], extra=A.headcloth(["#E8B830", "#F3EFE6", "#E8B830"][i])))
    o.append(S3.table(w * 0.62, b, w * 0.5, k * 0.9))
    for i in range(3): o.append(jar(w * (0.88 + i * 0.04), b, k * 0.6, "#8A3A1E"))
    return "".join(o)

def leaky_house(w, h, seed):
    """By slothfulness the roof sinketh in; and through idleness of the hands the house leaketh: a house in the rain, its
    roof-beam sagging, water dripping through into the room."""
    r = random.Random(seed)
    o = [sky(w, h, "#4A5A6A", "#8A9AAA"), ground(w, h, h * 0.86, "#5A5A4A", dy=0)]
    x0, x1, top, base = w * 0.18, w * 0.82, h * 0.34, h * 0.86
    o.append(f'<rect x="{f(x0)}" y="{f(top)}" width="{f(x1 - x0)}" height="{f(base - top)}" fill="#A8906A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<rect x="{f(x0 + 16)}" y="{f(top + 16)}" width="{f(x1 - x0 - 32)}" height="{f(base - top - 16)}" fill="#3A3028" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<path d="M{f(x0 - 16)} {f(top)} C {f(w * 0.4)} {f(top + h * 0.1)} {f(w * 0.6)} {f(top + h * 0.1)} {f(x1 + 16)} {f(top)} L {f(x1 + 16)} {f(top - 14)} C {f(w * 0.6)} {f(top + h * 0.08)} {f(w * 0.4)} {f(top + h * 0.08)} {f(x0 - 16)} {f(top - 14)} Z" fill="#6A5A4A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    for _ in range(50):
        x, y = r.uniform(0, w), r.uniform(0, h * 0.86)
        if x0 < x < x1 and y > top: continue
        o.append(f'<path d="M{f(x)} {f(y)} l -4 12" stroke="#C8D8E8" stroke-width="1.4"></path>')
    for i in range(5):
        x = w * (0.36 + i * 0.07); y = top + h * (0.1 + (i % 3) * 0.12)
        o.append(f'<path d="M{f(x)} {f(y)} c 3 6 3 10 0 12 c -3 -2 -3 -6 0 -12 Z" fill="#8FD0E2" stroke="#2C7DA0" stroke-width="1"></path>')
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(base - 6)}" rx="{f(w * 0.14)}" ry="6" fill="#4A6A8A" opacity="0.8"></ellipse>')
    return "".join(o)

def bird_tell(w, h, seed):
    """A bird of the heavens shall carry the voice: a bird flying out of the bedchamber window into the night, across the moon."""
    o = [sky(w, h, "#0B0B2A", "#2A1E5A"), mk.stars(50, w, h * 0.6, seed), f'<circle cx="{f(w * 0.7)}" cy="{f(h * 0.3)}" r="{f(min(w, h) * 0.14)}" fill="#F3EFE6" opacity="0.9"></circle>',
         f'<rect x="-10" y="{f(h * 0.3)}" width="{f(w * 0.36)}" height="{f(h)}" fill="#3A2E44" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         S3.window(w * 0.16, h * 0.5, w * 0.1, h * 0.22, inner="#FFC14D")]
    k = min(1.6, h / 200)
    o.append(bird(w * 0.62, h * 0.32, k * 1.6, "#0D0D0F") + bird(w * 0.42, h * 0.46, k * 0.7, "#2A2238"))
    o.append(f'<path d="M{f(w * 0.24)} {f(h * 0.56)} C {f(w * 0.34)} {f(h * 0.5)} {f(w * 0.44)} {f(h * 0.44)} {f(w * 0.58)} {f(h * 0.34)}" stroke="#FFD23F" stroke-width="2" stroke-dasharray="5 6" fill="none" opacity="0.7"></path>')
    return "".join(o)

# ---- Ecclesiastes 11 ----------------------------------------------------------------------------------------------------
def loaf(x, y, s=1.0):
    return f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(16 * s)}" ry="{f(8 * s)}" fill="#D9A25A" stroke="#0D0D0F" stroke-width="1.6"></ellipse><path d="M{f(x - 8 * s)} {f(y - 3 * s)} l {f(16 * s)} 0" stroke="#8A5A2A" stroke-width="1.2"></path>'

def bread_waters(w, h, seed):
    """Cast thy bread upon the waters; give a portion to seven, yea, even unto eight: loaves going down the river to the sea,
    and on the bank eight portions laid out in a row."""
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.36, seed, color="#8AA06A", amp=10, step=90), ground(w, h, h * 0.44, "#9CB86A", dy=0),
         f'<path d="M-10 {f(h * 0.5)} C {f(w * 0.3)} {f(h * 0.46)} {f(w * 0.6)} {f(h * 0.6)} {f(w + 10)} {f(h * 0.52)} L {f(w + 10)} {f(h * 0.74)} C {f(w * 0.6)} {f(h * 0.8)} {f(w * 0.3)} {f(h * 0.66)} -10 {f(h * 0.72)} Z" fill="#2C7DA8" stroke="#0D0D0F" stroke-width="2.4"></path>']
    k = min(1.4, h / 260)
    for i, (x, y) in enumerate(((0.16, 0.6), (0.36, 0.6), (0.56, 0.66), (0.78, 0.63))):
        o.append(loaf(w * x, h * y, k * (1.1 - i * 0.12)) + f'<path d="M{f(w * x - 24 * k)} {f(h * y + 8)} q 12 -5 24 0 t 24 0" stroke="#E8F6FA" stroke-width="1.6" fill="none"></path>')
    for i in range(8):
        o.append(loaf(w * (0.08 + i * 0.09), h * 0.9, k))
    return "".join(o)

def clouds_tree(p, w, h, seed):
    """If the clouds be full of rain, they empty themselves upon the earth; and if a tree fall, there shall it be: rain from
    heavy clouds, a tree lying where it fell, and a man by the field watching the wind, not sowing."""
    r = random.Random(seed)
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#5A6A7A", "#B8C0C0"), ground(w, h, h * 0.66, "#7A8A5A", dy=0)]
    for i in range(5):
        o.append(f'<ellipse cx="{f(w * (0.1 + i * 0.2))}" cy="{f(h * 0.12)}" rx="{f(w * 0.14)}" ry="{f(h * 0.1)}" fill="#3A4250" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    for _ in range(50):
        x, y = r.uniform(0, w * 0.6), r.uniform(h * 0.2, h * 0.66)
        o.append(f'<path d="M{f(x)} {f(y)} l -4 12" stroke="#C8D8E8" stroke-width="1.4"></path>')
    k = min(1.2, h / 300)
    fx, fy = w * 0.12, h * 0.86
    o.append(f'<circle cx="{f(fx)}" cy="{f(fy - 22 * k)}" r="{f(26 * k)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></circle>'
             + "".join(f'<path d="M{f(fx)} {f(fy - 22 * k)} l {f(dx * k)} {f(dy * k)}" stroke="#4A2A1A" stroke-width="3"></path>' for dx, dy in ((-30, -20), (-34, 6), (-20, 26), (6, -40), (-10, -44)))
             + f'<path d="M{f(fx)} {f(fy - 34 * k)} L {f(fx + w * 0.3)} {f(fy - 18 * k)} L {f(fx + w * 0.3)} {f(fy - 4 * k)} L {f(fx)} {f(fy - 10 * k)} Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2.2"></path>')
    for dx, dy, rr in ((0.3, -30, 30), (0.36, -22, 34), (0.42, -26, 28), (0.33, -6, 24), (0.4, -4, 26)):
        o.append(f'<circle cx="{f(fx + w * dx)}" cy="{f(fy + dy * k)}" r="{f(rr * k)}" fill="#3F7A44" stroke="#0D0D0F" stroke-width="1.8"></circle>')
    s = fit(b, max(h * 0.4, b - 200))
    o.append(man(p, w * 0.84, b, s, "#8A6A4A", flip=True, up=[(-22, -158), (-40, -190), (-30, -226)]) + wind_lines(w, h, seed, n=5, color="#E8E2D6", op=0.6, y0=0.3, y1=0.6))
    return "".join(o)

def sowers(p, w, h, seed):
    """In the morning sow thy seed, and in the evening withhold not thy hand: one field from dawn on the left to evening on
    the right, a sower in each light casting seed."""
    r = random.Random(seed)
    gid = f"sw{p}"
    b = h * 0.92
    o = [mk.defs(p, *ALL), hgrad(gid, [(0, "#FFE6A0"), (0.4, "#8FD0E2"), (0.6, "#8FD0E2"), (1, "#E8803A")]),
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{gid})"></rect>',
         sun(w * 0.06, h * 0.5, max(10, h * 0.05), color="#FFE680", op=0.35), sun(w * 0.94, h * 0.5, max(10, h * 0.05), color="#FF6A2A", op=0.3),
         hills(w, h, h * 0.54, seed, color="#7A8A5A", amp=8, step=90), ground(w, h, h * 0.62, "#8A6A4A", dy=0)]
    for k in range(6):
        y = h * (0.66 + k * 0.06)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y - 4)}" stroke="#6A4A2A" stroke-width="2"></path>')
    s = fit(b, max(h * 0.4, b - 200))
    for x, fl in ((0.24, False), (0.74, True)):
        o.append(man(p, w * x, b, s, "#C8A878", flip=fl, up=[(-22, -158), (-50, -150), (-74, -170)]))
        for _ in range(12):
            sx = w * x + (-1 if not fl else 1) * r.uniform(60, 140) * s; sy = b - r.uniform(40, 170) * s
            o.append(f'<circle cx="{f(sx)}" cy="{f(sy)}" r="2" fill="#F3E0B0" stroke="#0D0D0F" stroke-width="0.6"></circle>')
    return "".join(o)

def sweet_light(w, h, seed):
    """Truly the light is sweet, and a pleasant thing it is for the eyes to behold the sun: the sun rising over the hills."""
    o = [sky(w, h, "#FFB04A", "#FFF4C2"), sun(w * 0.5, h * 0.62, max(18, h * 0.12), color="#FFE680", op=0.5),
         hills(w, h, h * 0.62, seed, color="#8A6A7A", amp=14, step=80), hills(w, h, h * 0.74, seed + 1, color="#6A5A6A", amp=10, step=60), ground(w, h, h * 0.86, "#4A3A4A", dy=0)]
    return "".join(o)

def youth(p, w, h, seed):
    """Rejoice, O young man, in thy youth: a young man walking out through a field in spring, flowers about his feet."""
    r = random.Random(seed)
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3F8E8"), sun(w * 0.84, h * 0.18, max(12, h * 0.06), color="#FFE680", op=0.4),
         hills(w, h, h * 0.5, seed, color="#9CCB5E", amp=12, step=90), ground(w, h, h * 0.6, "#9CCB5E", dy=0)]
    for _ in range(60):
        x, y = r.uniform(0, w), r.uniform(h * 0.62, h)
        c = r.choice(["#FFD23F", "#F3EFE6", "#E85A7A", "#C2456A"])
        o.append(f'<path d="M{f(x)} {f(y)} l 0 -8" stroke="#3F7A44" stroke-width="1.6"></path><circle cx="{f(x)}" cy="{f(y - 9)}" r="3" fill="{c}" stroke="#0D0D0F" stroke-width="0.8"></circle>')
    s = fit(b, max(h * 0.38, b - 210))
    o.append(man(p, w * 0.44, b, s, "#2C7DA8", up=[(-22, -158), (-50, -170), (-70, -196)]))
    return "".join(o)

# ---- Ecclesiastes 12 ----------------------------------------------------------------------------------------------------
def darkening(w, h, seed):
    """Before the sun, and the light, and the moon, and the stars, are darkened, and the clouds return after the rain: the
    sun and the moon dimmed in a grey sky, the stars faint, the clouds coming back."""
    o = [sky(w, h, "#2A2A34", "#6A6A74"), mk.stars(40, w, h * 0.5, seed, color="#6A6A7A"),
         f'<circle cx="{f(w * 0.26)}" cy="{f(h * 0.34)}" r="{f(min(w, h) * 0.1)}" fill="#A89A6A" opacity="0.6"></circle>',
         f'<circle cx="{f(w * 0.72)}" cy="{f(h * 0.26)}" r="{f(min(w, h) * 0.07)}" fill="#8A8A9A" opacity="0.6"></circle>']
    for i in range(6):
        o.append(f'<ellipse cx="{f(w * (0.05 + i * 0.19))}" cy="{f(h * (0.5 + (i % 2) * 0.06))}" rx="{f(w * 0.16)}" ry="{f(h * 0.1)}" fill="#3A3A46" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    o.append(hills(w, h, h * 0.76, seed, color="#2A2A30", amp=10, step=70))
    return "".join(o)

def old_house(p, w, h, seed):
    """In the day when the keepers of the house shall tremble: an old house at dusk — an old man bowed on his staff at the
    door, the millstones idle in the court, the windows dark, the street door shut, a bird on the roof."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#4A3A5A", "#C88A6A"), ground(w, h, h * 0.84, "#7A6A5A", dy=0)]
    x0, x1, top = w * 0.3, w * 0.94, h * 0.26
    o.append(f'<rect x="{f(x0)}" y="{f(top)}" width="{f(x1 - x0)}" height="{f(h * 0.58)}" fill="#A89070" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<rect x="{f(x0 - 8)}" y="{f(top - 12)}" width="{f(x1 - x0 + 16)}" height="14" fill="#7A6A5A" stroke="#0D0D0F" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(x0 + (x1 - x0) * q)}" y="{f(top + h * 0.08)}" width="{f(w * 0.06)}" height="{f(h * 0.1)}" fill="#1A1214" stroke="#0D0D0F" stroke-width="1.8"></rect>' for q in (0.12, 0.44, 0.76))
             + f'<rect x="{f(x0 + (x1 - x0) * 0.62)}" y="{f(h * 0.56)}" width="{f(w * 0.1)}" height="{f(h * 0.28)}" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></rect>'
             + f'<path d="M{f(x0 + (x1 - x0) * 0.62)} {f(h * 0.7)} L {f(x0 + (x1 - x0) * 0.62 + w * 0.1)} {f(h * 0.7)}" stroke="#2A1A10" stroke-width="5"></path>')
    o.append(bird(w * 0.6, top - 22, min(1.6, h / 200)) + JG2.mill(w * 0.16, h * 0.88, min(0.5, h / 700)))
    s = fit(b, max(h * 0.4, b - 190))
    o.append(f'<g transform="rotate(10 {f(w * 0.36)} {f(b)})">' + man(p, w * 0.36, b, s, "#6A5A6A", up=HOLD_STAFF, extra=GREY_BEARD + STAFF) + '</g>')
    return "".join(o)

def almond(p, w, h, seed):
    """The almond-tree shall blossom, and the grasshopper shall be a burden; man goeth to his everlasting home, and the
    mourners go about the streets: an almond-tree white with blossom, a grasshopper on a stalk, and far off in the street the
    mourners with covered heads."""
    r = random.Random(seed)
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#8A9AB0", "#E8E0D8"), J.city_hill(w * 0.76, h * 0.62, w * 0.44, h * 0.18, seed), ground(w, h, h * 0.66, "#A89A7A", dy=0)]
    tx, ty = w * 0.28, h * 0.94; k = min(1.6, h / 260)
    o.append(f'<path d="M{f(tx)} {f(ty)} C {f(tx - 8 * k)} {f(ty - 60 * k)} {f(tx + 10 * k)} {f(ty - 100 * k)} {f(tx)} {f(ty - 130 * k)} M{f(tx)} {f(ty - 90 * k)} C {f(tx + 30 * k)} {f(ty - 110 * k)} {f(tx + 50 * k)} {f(ty - 120 * k)} {f(tx + 70 * k)} {f(ty - 140 * k)} M{f(tx)} {f(ty - 100 * k)} C {f(tx - 30 * k)} {f(ty - 120 * k)} {f(tx - 50 * k)} {f(ty - 130 * k)} {f(tx - 70 * k)} {f(ty - 150 * k)}" stroke="#4A3A2A" stroke-width="{f(8 * k)}" fill="none" stroke-linecap="round"></path>')
    for _ in range(70):
        x, y = tx + r.uniform(-90, 90) * k, ty - r.uniform(110, 190) * k
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(4, 7) * k)}" fill="{r.choice(["#F3EFE6", "#FFE8EE", "#F8D8E0"])}" stroke="#C8A8B0" stroke-width="0.8"></circle>')
    gx, gy = w * 0.56, h * 0.9
    o.append(f'<path d="M{f(gx)} {f(h + 10)} C {f(gx + 4)} {f(gy)} {f(gx - 4)} {f(gy - 40 * k)} {f(gx + 6)} {f(gy - 70 * k)}" stroke="#5A7A3A" stroke-width="3" fill="none"></path>'
             f'<g transform="translate({f(gx + 4)} {f(gy - 50 * k)}) scale({f(k * 0.8)}) rotate(-60)"><ellipse cx="0" cy="0" rx="18" ry="6" fill="#7A8A3A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'
             '<path d="M8 -2 L 30 -16 L 34 6" stroke="#0D0D0F" stroke-width="2" fill="none"></path><circle cx="-16" cy="-2" r="5" fill="#7A8A3A" stroke="#0D0D0F" stroke-width="1.2"></circle><path d="M-18 -6 C -26 -20 -30 -22 -36 -24" stroke="#0D0D0F" stroke-width="1.2" fill="none"></path></g>')
    s = fit(h * 0.7, h * 0.62)
    for i in range(4):
        o.append(mk.person(p, round(w * (0.66 + i * 0.07)), round(h * 0.7), round(s, 3), body="#2A1E1A", cloth="#3A3440", kind="Tunic", sw=3, flip=True, extra=A.headcloth("#4A4450")))
    return "".join(o)

def silver_cord(w, h, seed=1):
    """Before the silver cord is loosed, or the golden bowl is broken, or the pitcher is broken at the fountain, or the wheel
    broken at the cistern: a plate of four cells — the golden lamp-bowl fallen from its silver cord, the shards of the pitcher
    by the spring, the broken wheel over the cistern's mouth, and the cord itself."""
    o = [grid_bg(w, h, color="#3A2A5A", bg="#1A1430")]
    cw = w / 4
    def frame(i, g, s):
        cx, cy = cw * i + cw / 2, h * 0.54
        return (f'<rect x="{f(cw * i + 6)}" y="6" width="{f(cw - 12)}" height="{f(h - 12)}" fill="none" stroke="#5A4A8A" stroke-width="1.4"></rect>'
                + f'<g transform="translate({f(cx)} {f(cy)}) scale({f(s)})">{g}</g>')
    s = min(cw, h) / 150
    cord = ('<path d="M0 -80 L 0 -20" stroke="#E8E8F0" stroke-width="3"></path><path d="M0 -20 C 6 -10 -6 0 2 10" stroke="#E8E8F0" stroke-width="3" fill="none" stroke-dasharray="4 3"></path>'
            '<path d="M-6 30 C 0 24 4 26 6 32" stroke="#E8E8F0" stroke-width="3" fill="none"></path>')
    bowl = ('<path d="M-40 20 C -36 46 36 46 40 20 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path><path d="M-6 20 L 2 34 L -4 44" stroke="#0D0D0F" stroke-width="2" fill="none"></path>'
            '<path d="M-44 60 L -20 56 L -30 70 Z M20 58 L 40 62 L 30 72 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path><path d="M0 -80 L 0 0" stroke="#E8E8F0" stroke-width="3"></path>')
    pitcher = ('<path d="M-60 60 C -20 54 20 54 60 60" stroke="#2C9DB8" stroke-width="6" fill="none"></path><path d="M-30 50 L -20 10 L 0 20 L -6 50 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>'
               '<path d="M6 50 L 14 18 L 32 26 L 26 52 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path><path d="M-10 -10 L 0 -30 L 14 -10 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>')
    wheel = ('<rect x="-50" y="40" width="100" height="24" fill="#6A6A7A" stroke="#0D0D0F" stroke-width="2"></rect><ellipse cx="0" cy="40" rx="50" ry="10" fill="#0D0B14" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             '<path d="M-44 40 L -44 -40 M44 40 L 44 -40" stroke="#5A3A22" stroke-width="6"></path><path d="M-36 -36 A 30 30 0 0 1 20 -60" stroke="#8A5A30" stroke-width="8" fill="none"></path>'
             '<path d="M-20 -30 L -8 -50 M4 -40 L 0 -60" stroke="#8A5A30" stroke-width="4"></path><path d="M14 -30 A 30 30 0 0 1 30 -10" stroke="#8A5A30" stroke-width="8" fill="none" transform="translate(10 30)"></path>')
    for i, g in enumerate((cord, bowl, pitcher, wheel)):
        o.append(frame(i, g, s))
    return "".join(o)

def dust_spirit(w, h, seed):
    """The dust returneth to the earth as it was, and the spirit returneth unto God who gave it: dust settling over the
    earth at evening, and a light going up from it into the sky (God is never drawn)."""
    r = random.Random(seed)
    o = [sky(w, h, "#2A2A5A", "#E8B88A"), V.rays(w * 0.5, -h * 0.2, 30, 20, h * 1.2, color="#FFF4C2", op=0.18),
         hills(w, h, h * 0.66, seed, color="#6A5A5A", amp=8, step=80), ground(w, h, h * 0.74, "#A8906A", dy=0)]
    for _ in range(40):
        x, y = r.uniform(0, w), r.uniform(h * 0.6, h * 0.86)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(1, 3))}" fill="#C8A07A" opacity="0.6"></circle>')
    for i in range(14):
        o.append(f'<circle cx="{f(w * 0.5 + r.uniform(-30, 30))}" cy="{f(h * (0.7 - i * 0.05))}" r="{f(r.uniform(2, 4))}" fill="#FFF4C2" opacity="{0.9 - i * 0.05:.2f}"></circle>')
    return "".join(o)

def goads_books(w, h, seed):
    """The words of the wise are as goads, and as nails well fastened; of making many books there is no end: an ox-goad and
    a row of nails driven into a beam, and beside them scrolls heaped without end."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A22"></rect>', S3.cedar(w, h, h * 0.86)]
    k = min(1.4, h / 260)
    o.append(f'<rect x="-10" y="{f(h * 0.22)}" width="{f(w * 0.46)}" height="{f(h * 0.08)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></rect>'
             + "".join(f'<path d="M{f(w * (0.06 + i * 0.08))} {f(h * 0.24)} L {f(w * (0.06 + i * 0.08))} {f(h * 0.3)}" stroke="#8A8A9A" stroke-width="4"></path><circle cx="{f(w * (0.06 + i * 0.08))}" cy="{f(h * 0.24)}" r="5" fill="#A8A8B8" stroke="#0D0D0F" stroke-width="1.4"></circle>' for i in range(5))
             + f'<path d="M{f(w * 0.04)} {f(h * 0.8)} L {f(w * 0.42)} {f(h * 0.44)}" stroke="#0D0D0F" stroke-width="{f(10 * k)}" stroke-linecap="round"></path><path d="M{f(w * 0.04)} {f(h * 0.8)} L {f(w * 0.42)} {f(h * 0.44)}" stroke="#8A5A30" stroke-width="{f(6 * k)}" stroke-linecap="round"></path>'
             + f'<path d="M{f(w * 0.42)} {f(h * 0.44)} L {f(w * 0.46)} {f(h * 0.38)}" stroke="#C8C8D0" stroke-width="{f(4 * k)}" stroke-linecap="round"></path>')
    for i in range(18):
        x = w * (0.56 + (i % 6) * 0.07) + (i // 6) * w * 0.03; y = h * 0.84 - (i // 6) * 22 * k
        o.append(f'<rect x="{f(x - 22 * k)}" y="{f(y - 10 * k)}" width="{f(44 * k)}" height="{f(20 * k)}" rx="{f(9 * k)}" fill="{r.choice(["#E8D8B0", "#F3E0B8", "#D8C8A0"])}" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 f'<ellipse cx="{f(x + 22 * k)}" cy="{f(y)}" rx="{f(5 * k)}" ry="{f(10 * k)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    return "".join(o)

def warriors_row(p, w, h, b, seed):
    s = fit(b, max(h * 0.5, b - 160))
    return "".join(warrior(p, w * (0.04 + i * 0.08), b - (i % 2) * 6, s, WAR[i % 4]) for i in range(4)) + king_fig(p, w * 0.9, b, s * 1.05, flip=True, cloth="#7A1A2A")
