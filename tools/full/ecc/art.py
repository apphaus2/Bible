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
                 + label(x, y - 3, a.upper(), GOLD if on else "#5A5A8A", fs) + label(x, y + fs + 2, b.upper(), ROSE if on else "#5A5A8A", fs))
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
