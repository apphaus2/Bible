"""Drawings for the Micah volume, on the minor prophets' kit (oba.minor), with 1 and 2 Kings' drawings where they fit
(kg1.art.vine_fig, kg2.art.captives, siege_forts, assyria_map). Micah at a distance: a dark brown tunic and a slate headcloth,
grey-black beard (micah_fig)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from oba.minor import *
from ecc.art import scales, lion_lying
from kg1.art import vine_fig
from kg2.art import captives, siege_forts, assyria_map
import samuel1 as S1, samuel4 as S4, judges2 as JG2

MICAH_C = "#4A3424"

def micah_fig(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=MICAH_C, sw=3, flip=flip, up=up, kind="Tunic", extra=A.headcloth("#2F3A4A") + GREY_BEARD.replace("#B8B2A6", "#5A544E"))

def melting(w, h, seed):
    """The mountains melted as wax before the fire, the valleys cleft (God is not drawn: fire and storm on the heights)."""
    r = random.Random(seed)
    o = [sky(w, h, "#1A0A0A", "#6A1A10"), bolt(w * 0.3, 0, h * 0.3, seed), bolt(w * 0.72, 0, h * 0.26, seed + 1)]
    for i, (x0, x1, top) in enumerate(((-0.1, 0.5, 0.2), (0.3, 0.9, 0.28), (0.6, 1.1, 0.24))):
        o.append(f'<path d="M{f(w * x0)} {f(h * 0.8)} L {f(w * (x0 + x1) / 2)} {f(h * top)} L {f(w * x1)} {f(h * 0.8)} Z" fill="{["#4A1A12", "#5A2214", "#3A140E"][i]}" stroke="#0D0D0F" stroke-width="2.2"></path>')
        cx = w * (x0 + x1) / 2
        for k in range(4):
            dx = r.uniform(-w * 0.08, w * 0.08)
            o.append(f'<path d="M{f(cx + dx * 0.3)} {f(h * top + 8)} C {f(cx + dx * 0.6)} {f(h * 0.5)} {f(cx + dx)} {f(h * 0.6)} {f(cx + dx * 1.2)} {f(h * 0.82)}" stroke="#FF8A3D" stroke-width="{f(r.uniform(3, 7))}" fill="none" stroke-linecap="round"></path>')
        o.append(E.blaze(cx, h * top + 14, w * 0.12, h * 0.14, seed + i, n=5))
    o.append(f'<path d="M-10 {f(h * 0.8)} L {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2A100C" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.46)} {f(h * 0.8)} L {f(w * 0.5)} {f(h * 0.9)} L {f(w * 0.47)} {f(h + 10)} M{f(w * 0.5)} {f(h * 0.9)} L {f(w * 0.56)} {f(h + 10)}" stroke="#FF6A2A" stroke-width="4" fill="none"></path>')
    return "".join(o)

def samaria_heap(w, h, seed):
    """Samaria as a heap of the field and places for planting vineyards, her stones poured down into the valley, her
    graven images beaten to pieces."""
    o = [sky(w, h, "#6A6A7A", "#D8C8A8"), f'<path d="M{f(w * 0.1)} {f(h * 0.7)} C {f(w * 0.3)} {f(h * 0.2)} {f(w * 0.6)} {f(h * 0.2)} {f(w * 0.8)} {f(h * 0.7)} Z" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="2.2"></path>',
         ruin(w * 0.28, w * 0.62, h * 0.4, h * 0.14, seed), ground(w, h, h * 0.68, "#9A8A6A", dy=0), vines(w * 0.04, w * 0.5, h * 0.78, h * 0.96, seed, rows=2, fruit=False)]
    r = random.Random(seed)
    for i in range(10):
        x, y = w * r.uniform(0.6, 0.95), h * r.uniform(0.74, 0.96)
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(14 + r.uniform(0, 12))}" height="{f(10 + r.uniform(0, 8))}" fill="#B8A88A" stroke="#0D0D0F" stroke-width="1.4" transform="rotate({r.randint(-30, 30)} {f(x)} {f(y)})"></rect>')
    o.append(f'<path d="M{f(w * 0.56)} {f(h * 0.94)} l 30 -6 l 6 12 l -24 8 Z M{f(w * 0.62)} {f(h * 0.86)} l 18 4 l -4 14 l -18 -4 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path>')
    return "".join(o)

TOWNS = [("GATH", 0.14, 0.3), ("BETH-LE-APHRAH", 0.3, 0.52), ("SHAPHIR", 0.2, 0.62), ("ZAANAN", 0.34, 0.74), ("BETH-EZEL", 0.5, 0.66),
         ("MAROTH", 0.58, 0.5), ("LACHISH", 0.24, 0.84), ("MORESHETH-GATH", 0.42, 0.4), ("ACHZIB", 0.12, 0.48), ("MARESHAH", 0.36, 0.6),
         ("ADULLAM", 0.5, 0.3), ("JERUSALEM", 0.84, 0.22)]

def towns_map(w, h, lit=()):
    """The towns of the lowland of Judah as a technical map, the evil coming down to the gate of Jerusalem."""
    o = [grid_bg(w, h, color="#3A1E2A", step=28, bg="#1A0A12")]
    for name, x, y in TOWNS:
        c = "#FFD23F" if name in lit else "#FF8A6A"
        an = "start" if x < 0.7 else "end"
        o.append(node(w * x, h * y, "", color=c, r=4) + label(w * x + (9 if an == "start" else -9), h * y + 4, name, c, 9, anchor=an))
    o.append(route([(w * 0.3, h * 0.8), (w * 0.5, h * 0.6), (w * 0.82, h * 0.26)], color="#D7261E"))
    o.append(label(w * 0.03, h * 0.1, "THE LOWLAND OF JUDAH", "#FF8A6A", 9, anchor="start"))
    return "".join(o)

def devisers(w, h, seed):
    """They devise iniquity upon their beds; when the morning is light they practise it; they covet fields and seize them:
    a lamp-lit chamber by night, and at morning a boundary stone moved in the field."""
    from genesis.art4 import clay_lamp
    from kg1.art import bed
    o = [f'<rect x="-10" y="-10" width="{f(w * 0.48)}" height="{f(h + 20)}" fill="#1A1028"></rect>', halo(w * 0.24, h * 0.4, h * 0.4, "#FFC14D", 0.35),
         clay_lamp(w * 0.38, h * 0.44, min(1.0, h / 300)), bed(w * 0.48, h, w * 0.04, w * 0.34, h * 0.96, cover="#5A2A4A", head="#B98A6E", hair="#1A1210"),
         f'<g transform="translate({f(w * 0.48)} 0)">{vista(w * 0.52, h, seed, tone="dawn", sun_at=(0.8, 0.4), field="grain", hills_n=1, horizon=0.55)}</g>',
         f'<path d="M{f(w * 0.48)} -10 L {f(w * 0.48)} {f(h + 10)}" stroke="#0D0D0F" stroke-width="4"></path>']
    x, y = w * 0.74, h * 0.9
    o.append(f'<rect x="{f(x - 10)}" y="{f(y - 40)}" width="20" height="40" fill="#B8A890" stroke="#0D0D0F" stroke-width="1.8"></rect>'
             f'<path d="M{f(x - 50)} {f(y)} L {f(x + 50)} {f(y)}" stroke="#D7261E" stroke-width="2.4" stroke-dasharray="6 4"></path>'
             f'<path d="M{f(x - 40)} {f(y - 20)} l 26 0 M{f(x - 22)} {f(y - 26)} l 8 6 l -8 6" stroke="#D7261E" stroke-width="2.4" fill="none"></path>')
    return "".join(o)

def yoke(w, h, seed):
    """An evil from which ye shall not remove your necks: a heavy yoke, and the measuring line cast by lot left lying."""
    o = [sky(w, h, "#3A2A2A", "#A87A5A"), ground(w, h, h * 0.62, "#6A5A4A", dy=0)]
    k = min(1.6, h / 200)
    x, y = w * 0.4, h * 0.56
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})"><path d="M-120 -10 C -60 -30 60 -30 120 -10 L 120 6 C 60 -12 -60 -12 -120 6 Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2.4"></path>'
             '<path d="M-70 0 C -80 30 -40 50 -30 4 M30 4 C 40 50 80 30 70 0" stroke="#5A3A1E" stroke-width="7" fill="none"></path>'
             '<path d="M-120 -2 L -150 -2" stroke="#3A2214" stroke-width="5"></path></g>')
    o.append(f'<path d="M{f(w * 0.62)} {f(h * 0.86)} C {f(w * 0.7)} {f(h * 0.8)} {f(w * 0.8)} {f(h * 0.94)} {f(w * 0.94)} {f(h * 0.84)}" stroke="#E8D8A8" stroke-width="2.4" fill="none"></path>'
             + "".join(f'<circle cx="{f(w * (0.66 + i * 0.07))}" cy="{f(h * (0.86 + (i % 2) * 0.03))}" r="4" fill="#B5652E" stroke="#0D0D0F" stroke-width="1"></circle>' for i in range(4)))
    return "".join(o)

def cast_out(w, h, seed):
    """Arise ye, and depart, for this is not your resting-place: the doors of pleasant houses standing open, their goods
    thrown out in the street, wine jars by the false prophet's seat."""
    o = [sky(w, h, "#8A8A9A", "#E8D8C0")]
    k = h / 300
    for i in range(3):
        x = w * (0.08 + i * 0.3); wd = w * 0.24
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.3)}" width="{f(wd)}" height="{f(h * 0.5)}" fill="#D8C090" stroke="#0D0D0F" stroke-width="2.2"></rect>'
                 f'<path d="M{f(x + wd * 0.36)} {f(h * 0.8)} L {f(x + wd * 0.36)} {f(h * 0.5)} L {f(x + wd * 0.64)} {f(h * 0.5)} L {f(x + wd * 0.64)} {f(h * 0.8)} Z" fill="#1A0E08"></path>'
                 f'<path d="M{f(x + wd * 0.64)} {f(h * 0.8)} L {f(x + wd * 0.8)} {f(h * 0.84)} L {f(x + wd * 0.8)} {f(h * 0.54)} L {f(x + wd * 0.64)} {f(h * 0.5)} Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.8"></path>')
    o.append(ground(w, h, h * 0.8, "#A8987A", dy=0))
    r = random.Random(seed)
    for i in range(6):
        x = w * r.uniform(0.05, 0.9); y = h * r.uniform(0.86, 0.96)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(20 * k)} {f(-10 * k)} l {f(16 * k)} {f(8 * k)} l {f(-18 * k)} {f(10 * k)} Z" fill="{r.choice(["#7A3A5A", "#3A5A7A", "#C8A060"])}" stroke="#0D0D0F" stroke-width="1.4"></path>')
    return "".join(o)

def wine_jars(w, h, seed):
    """I will prophesy unto thee of wine and of strong drink: a row of wine jars and a cup by a seat."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A1A2A"></rect>', halo(w * 0.5, h * 0.3, h * 0.6, "#FFB04A", 0.3),
         f'<rect x="-10" y="{f(h * 0.8)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#5A3A2A" stroke="#0D0D0F" stroke-width="2"></rect>']
    k = min(1.2, h / 260)
    for i in range(5):
        x = w * (0.14 + i * 0.12)
        o.append(f'<path d="M{f(x - 22 * k)} {f(h * 0.8)} C {f(x - 40 * k)} {f(h * 0.8 - 60 * k)} {f(x - 20 * k)} {f(h * 0.8 - 110 * k)} {f(x - 8 * k)} {f(h * 0.8 - 120 * k)} L {f(x + 8 * k)} {f(h * 0.8 - 120 * k)} C {f(x + 20 * k)} {f(h * 0.8 - 110 * k)} {f(x + 40 * k)} {f(h * 0.8 - 60 * k)} {f(x + 22 * k)} {f(h * 0.8)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(cup(w * 0.8, h * 0.8, k * 0.8, color="#E8B830", spill=True))
    return "".join(o)

def fold(p, w, h, seed):
    """The sheep of Bozrah, a flock in the midst of their pasture; the breaker gone up before them, the gate broken open."""
    o = [vista(w, h, seed, tone="dawn", sun_at=(0.82, 0.3), hills_n=2, horizon=0.5)]
    o.append(f'<path d="M{f(w * 0.02)} {f(h * 0.94)} L {f(w * 0.02)} {f(h * 0.62)} L {f(w * 0.62)} {f(h * 0.62)} L {f(w * 0.62)} {f(h * 0.94)}" stroke="#8A7A6A" stroke-width="{f(h * 0.05)}" fill="none"></path>')
    o.append(f'<path d="M{f(w * 0.62)} {f(h * 0.62)} L {f(w * 0.72)} {f(h * 0.56)} M{f(w * 0.62)} {f(h * 0.94)} L {f(w * 0.74)} {f(h * 0.98)}" stroke="#8A5A30" stroke-width="8"></path>')
    o.append(sheep_row(w * 0.06, w * 0.6, h * 0.86, 7, seed, s=min(0.6, h / 500)) + sheep_row(w * 0.66, w * 0.96, h * 0.82, 3, seed + 1, s=min(0.55, h / 520)))
    return "".join(o)

def breaker(p, w, h, seed):
    """The breaker is gone up before them: they have broken forth and passed on to the gate, and are gone out thereat; and
    Jehovah at the head of them: a gate broken open in the wall, the people streaming out on the road toward the light
    (their king and Jehovah are not drawn: the light goes before them)."""
    o = [mk.defs(p, *ALL), sky(w, h, "#2A2A5A", "#FFD8A0"), halo(w * 0.86, h * 0.3, h * 0.7, "#FFF4C2", 0.55),
         rays(w * 0.86, h * 0.3, 22, h * 0.12, max(w, h), "#FFF4C2", 0.22, 4), hills(w, h, h * 0.56, seed, color="#5A4A6A", amp=14),
         ground(w, h, h * 0.6, "#8A7A6A", dy=0)]
    gx = w * 0.2
    o.append(walls(-10, w * 0.36, h * 0.94, h * 0.5, seed, color="#A8906A", towers=2, gate=False, houses=False))
    o.append(f'<path d="M{f(gx - w * 0.06)} {f(h * 0.94)} L {f(gx - w * 0.06)} {f(h * 0.7)} Q {f(gx)} {f(h * 0.6)} {f(gx + w * 0.06)} {f(h * 0.7)} L {f(gx + w * 0.06)} {f(h * 0.94)} Z" fill="#FFE6A0" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(gx + w * 0.06)} {f(h * 0.94)} L {f(gx + w * 0.13)} {f(h * 0.97)} L {f(gx + w * 0.12)} {f(h * 0.74)} L {f(gx + w * 0.06)} {f(h * 0.7)} Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(route([(gx + w * 0.06, h * 0.9), (w * 0.6, h * 0.76), (w * 0.86, h * 0.62)], color="#FFE680", sw=3, dash="2 8", arrow=False))
    r = random.Random(seed)
    for i in range(7):
        t = (i + 0.6) / 7
        x = gx + w * 0.1 + (w * 0.66 - gx) * t; b = h * (0.96 - 0.22 * t); top = b - h * (0.36 - 0.18 * t)
        o.append(figure(p, x, b, top, r.choice(["#6A4A3A", "#3A4A6A", "#5A6A3A", "#7A3A3A", "#4A3A5A"]), "woman" if i % 3 == 1 else "man"))
    o.append(sheep_row(w * 0.42, w * 0.7, h * 0.97, 4, seed, s=min(0.5, h / 560)))
    return "".join(o)

def caldron(w, h, seed):
    """Ye heads of Jacob, who chop them in pieces as for the pot: the empty judgment seats in a dark hall, a caldron
    steaming on its fire (nothing in it drawn)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1E0E10"></rect>']
    for i in range(4):
        x = w * (0.1 + i * 0.12)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.4)}" width="{f(w * 0.08)}" height="{f(h * 0.4)}" fill="#4A2A2A" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<rect x="{f(x - 4)}" y="{f(h * 0.6)}" width="{f(w * 0.08 + 8)}" height="{f(h * 0.06)}" fill="#6A3A3A" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.8)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#2A1414" stroke="#0D0D0F" stroke-width="2"></rect>')
    k = min(1.4, h / 240); x, y = w * 0.76, h * 0.86
    o.append(E.blaze(x, y + 6 * k, 120 * k, 50 * k, seed, n=5))
    o.append(f'<path d="M{f(x - 60 * k)} {f(y - 80 * k)} C {f(x - 64 * k)} {f(y - 20 * k)} {f(x - 30 * k)} {f(y)} {f(x)} {f(y)} C {f(x + 30 * k)} {f(y)} {f(x + 64 * k)} {f(y - 20 * k)} {f(x + 60 * k)} {f(y - 80 * k)} Z" fill="#2A2A2E" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(x)}" cy="{f(y - 80 * k)}" rx="{f(60 * k)}" ry="{f(10 * k)}" fill="#1A1A1E" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    o.append(smoke(x, y - 90 * k, 7, seed, color="#C8C0B8", op=0.4, k=k * 0.8))
    return "".join(o)

def sun_down(w, h, seed):
    """The sun shall go down upon the prophets, and the day shall be black over them: a black sun setting over the seers'
    tents."""
    o = [sky(w, h, "#05050A", "#3A1A1A"), f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.62)}" r="{f(h * 0.2)}" fill="#0D0D0F" stroke="#D7261E" stroke-width="3"></circle>',
         rays(w * 0.5, h * 0.62, 30, h * 0.22, h * 0.36, "#D7261E", 0.4, 2), hills(w, h, h * 0.66, seed, color="#0D0A0E", amp=10),
         ground(w, h, h * 0.72, "#120A0C", dy=0)]
    for i in range(5):
        x = w * (0.08 + i * 0.2)
        o.append(f'<path d="M{f(x - 34)} {f(h * 0.9)} L {f(x)} {f(h * 0.74)} L {f(x + 34)} {f(h * 0.9)} Z" fill="#1A1218" stroke="#3A2A2E" stroke-width="2"></path>')
    return "".join(o)

def plowed(w, h, seed):
    """Zion plowed as a field, Jerusalem become heaps, the mountain of the house as the high places of a forest."""
    from samuel1 import cow
    o = [sky(w, h, "#7A7A8A", "#D8C8A8"), f'<path d="M{f(w * 0.4)} {f(h * 0.6)} C {f(w * 0.6)} {f(h * 0.1)} {f(w * 0.9)} {f(h * 0.1)} {f(w + 20)} {f(h * 0.5)} L {f(w + 20)} {f(h * 0.6)} Z" fill="#6A7A4A" stroke="#0D0D0F" stroke-width="2"></path>']
    r = random.Random(seed)
    for i in range(9): o.append(tree(w * r.uniform(0.5, 0.98), h * r.uniform(0.3, 0.6), min(0.5, h / 600) * r.uniform(0.7, 1.1), color="#2E5A2E", kind=r.choice(["round", "tall"]), seed=seed + i))
    o.append(ruin(w * 0.02, w * 0.4, h * 0.58, h * 0.14, seed))
    o.append(ground(w, h, h * 0.6, "#8A6A4A", dy=0))
    for k in range(6):
        y = h * (0.66 + k * 0.06)
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y + 6)}" stroke="#5A3A22" stroke-width="3"></path>')
    o.append(cow(w * 0.3, h * 0.9, min(0.6, h / 500)))
    return "".join(o)

def mountain_house(w, h, seed):
    """The mountain of Jehovah's house established on the top of the mountains, and peoples flowing unto it."""
    o = [sky(w, h, "#2A3A6A", "#FFD8A0"), halo(w * 0.5, h * 0.2, h * 0.5, "#FFE680", 0.55), rays(w * 0.5, h * 0.22, 28, h * 0.12, max(w, h), "#FFF4C2", 0.2, 4),
         hills(w, h, h * 0.62, seed, color="#4A4A6A", amp=24, step=90),
         f'<path d="M{f(w * 0.2)} {f(h * 0.7)} L {f(w * 0.44)} {f(h * 0.28)} L {f(w * 0.56)} {f(h * 0.28)} L {f(w * 0.8)} {f(h * 0.7)} Z" fill="#7A6A8A" stroke="#0D0D0F" stroke-width="2.2"></path>',
         temple_front(w * 0.5, h * 0.29, w * 0.14, seed), ground(w, h, h * 0.7, "#8A7A6A", dy=0)]
    for side in (-1, 1):
        pts = [(w * 0.5 + side * w * (0.5 - 0.42 * t), h * (0.98 - 0.3 * t)) for t in (0, 0.25, 0.5, 0.75, 1)]
        o.append(route(pts, color="#FFE680", sw=3, dash="2 7", arrow=False))
        for t in (0.1, 0.3, 0.5, 0.7):
            x, y = w * 0.5 + side * w * (0.5 - 0.42 * t), h * (0.98 - 0.3 * t)
            o.append(f'<path d="M{f(x - 3)} {f(y)} L {f(x)} {f(y - 14 * (1 - t * 0.6))} L {f(x + 3)} {f(y)} Z" fill="#3A2A4A"></path>')
    return "".join(o)

def plowshares(w, h, seed):
    """They shall beat their swords into plowshares, and their spears into pruning-hooks: the anvil, a sword beaten into a
    plowshare, a pruning-hook beside it, sparks."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A14"></rect>', halo(w * 0.5, h * 0.6, h * 0.6, "#FF8A3D", 0.4)]
    k = min(1.6, h / 220); x, y = w * 0.5, h * 0.8
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})"><path d="M-80 -40 L 70 -40 L 100 -54 L 70 -24 L 40 -24 L 30 0 L 40 30 L -40 30 L -30 0 L -40 -24 L -80 -24 Z" fill="#3A3A44" stroke="#0D0D0F" stroke-width="2.6"></path>'
             '<path d="M-60 -48 L 0 -48 C 20 -48 34 -60 40 -72 C 20 -74 0 -64 -10 -56 L -60 -56 Z" fill="#E86A2A" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M-60 -52 L -90 -52" stroke="#5A3A22" stroke-width="8"></path></g>')
    o.append(f'<g transform="translate({f(w * 0.18)} {f(h * 0.94)}) scale({f(k)})"><path d="M0 0 L 0 -110" stroke="#6A4A2A" stroke-width="7"></path><path d="M0 -110 C 30 -120 40 -100 30 -86 C 22 -96 12 -100 0 -98 Z" fill="#B8B8C0" stroke="#0D0D0F" stroke-width="2"></path></g>')
    o.append(f'<g transform="translate({f(w * 0.84)} {f(h * 0.94)}) scale({f(k)})"><path d="M0 0 L -10 -80 L 10 -80 L 6 0 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path><path d="M-10 -80 L -24 -120 L 0 -140 L 24 -120 L 10 -80 Z" fill="#B8B8C0" stroke="#0D0D0F" stroke-width="2"></path></g>')
    o.append(mk.speed(x - 10 * k, y - 60 * k, 16, 10 * k, 60 * k, seed, color="#FFD23F", op=0.8))
    return "".join(o)

def remnant(p, w, h, seed):
    """I will assemble that which is lame, and gather that which is driven away: a remnant coming up the road to mount Zion,
    some leaning on staves."""
    o = [vista(w, h, seed, tone="dawn", far="zion", cx=0.74, cw=0.46, sun_at=(0.5, 0.2), hills_n=1, horizon=0.56)]
    o.append(mk.defs(p, *ALL) + crowd(p, w * 0.04, w * 0.56, h * 0.95, h * 0.56, 6, seed, flip=False, up=[(-22, -158), (-40, -120), (-48, -92)]))
    return "".join(o)

def tower_flock(w, h, seed):
    """O tower of the flock, the hill of the daughter of Zion: a shepherds' watchtower on a hill above the flock."""
    o = [vista(w, h, seed, tone="dusk", hills_n=2, horizon=0.62, sheep=7)]
    x = w * 0.66
    o.append(f'<path d="M{f(x - 30)} {f(h * 0.66)} L {f(x - 22)} {f(h * 0.2)} L {f(x + 22)} {f(h * 0.2)} L {f(x + 30)} {f(h * 0.66)} Z" fill="#A8906A" stroke="#0D0D0F" stroke-width="2.2"></path>'
             + "".join(f'<rect x="{f(x - 26 + i * 14)}" y="{f(h * 0.16)}" width="9" height="{f(h * 0.04)}" fill="#A8906A" stroke="#0D0D0F" stroke-width="1.4"></rect>' for i in range(4))
             + f'<rect x="{f(x - 6)}" y="{f(h * 0.3)}" width="12" height="{f(h * 0.08)}" fill="#FFC14D"></rect>')
    return "".join(o)

def thresh(w, h, seed):
    """Arise and thresh, O daughter of Zion; I will make thy horn iron, and thy hoofs brass: sheaves gathered to the
    threshing-floor, an ox with horns of iron and hoofs of brass treading."""
    from samuel1 import cow
    o = [sky(w, h, "#FFE6A0", "#E8B880"), hills(w, h, h * 0.5, seed, color="#B8905A", amp=14), ground(w, h, h * 0.56, "#C8A06A", dy=0),
         S4.threshing_floor(w * 0.5, h * 0.84, w * 0.7)]
    for i in range(6):
        x = w * (0.08 + i * 0.17) if i % 2 else w * (0.1 + i * 0.16)
        y = h * (0.66 if i % 2 else 0.98)
        o.append(f'<path d="M{f(x - 16)} {f(y)} L {f(x - 6)} {f(y - 40)} L {f(x + 6)} {f(y - 40)} L {f(x + 16)} {f(y)} Z" fill="#E8C060" stroke="#0D0D0F" stroke-width="1.6"></path>')
    k = min(0.9, h / 320)
    cx = w * 0.34
    o.append(cow(cx, h * 0.86, k, color="#7A5A3A", patch="#5A3A22"))
    o.append(f'<path d="M{f(cx + 64 * k)} {f(h * 0.86 - 96 * k)} l {f(14 * k)} {f(-20 * k)} M{f(cx + 54 * k)} {f(h * 0.86 - 96 * k)} l {f(4 * k)} {f(-22 * k)}" stroke="#5A6A7A" stroke-width="{f(6 * k)}" stroke-linecap="round"></path>'
             + "".join(f'<path d="M{f(cx + dx * k)} {f(h * 0.86)} l {f(-5 * k)} {f(-12 * k)} l {f(10 * k)} 0 Z" fill="#C8963E" stroke="#0D0D0F" stroke-width="1.2"></path>' for dx in (-74, -58, 44, 60)))
    return "".join(o)

# ---- Micah 5–7 ---------------------------------------------------------------------------------------------------------
def bethlehem(w, h, seed):
    """Beth-lehem Ephrathah, little among the thousands of Judah: a small town on its terraced hill at night, its few lamps
    lit, the shepherds' fields below."""
    o = [sky(w, h, "#05051A", "#2A2A5A"), starfield(w, h, seed, 80, 0.7), hills(w, h, h * 0.6, seed, color="#1A1A3A", amp=14),
         f'<path d="M{f(w * 0.2)} {f(h * 0.8)} C {f(w * 0.36)} {f(h * 0.36)} {f(w * 0.64)} {f(h * 0.36)} {f(w * 0.8)} {f(h * 0.8)} Z" fill="#2A2A4A" stroke="#0D0D0F" stroke-width="2"></path>']
    for k in range(3):
        y = h * (0.62 + k * 0.06)
        o.append(f'<path d="M{f(w * (0.3 - k * 0.05))} {f(y)} L {f(w * (0.7 + k * 0.05))} {f(y)}" stroke="#3A3A5A" stroke-width="2"></path>')
    o.append(walls(w * 0.38, w * 0.62, h * 0.52, h * 0.12, seed, color="#6A6A8A", lit=True, towers=1, gate=False))
    o.append(ground(w, h, h * 0.8, "#14142A", dy=0) + sheep_row(w * 0.1, w * 0.9, h * 0.94, 6, seed, s=min(0.4, h / 700)))
    return "".join(o)

def shepherd_ruler(p, w, h, seed):
    """He shall stand, and shall feed his flock in the strength of Jehovah: the flock feeding in a broad light, a shepherd's
    staff planted upright among them (the ruler himself is not drawn)."""
    o = [sky(w, h, "#3A4A8A", "#FFE6A0"), halo(w * 0.5, h * 0.34, h * 0.6, "#FFF4C2", 0.5), rays(w * 0.5, h * 0.34, 24, h * 0.1, max(w, h), "#FFF4C2", 0.2, 4),
         hills(w, h, h * 0.62, seed, color="#6A8A5A", amp=14), ground(w, h, h * 0.68, "#9CAB6A", dy=0)]
    x, b = w * 0.5, h * 0.94
    o.append(f'<path d="M{f(x)} {f(b)} L {f(x)} {f(h * 0.42)} C {f(x)} {f(h * 0.34)} {f(x + h * 0.08)} {f(h * 0.34)} {f(x + h * 0.08)} {f(h * 0.42)}" stroke="#0D0D0F" stroke-width="9" fill="none" stroke-linecap="round"></path>'
             f'<path d="M{f(x)} {f(b)} L {f(x)} {f(h * 0.42)} C {f(x)} {f(h * 0.34)} {f(x + h * 0.08)} {f(h * 0.34)} {f(x + h * 0.08)} {f(h * 0.42)}" stroke="#8A6A3A" stroke-width="5" fill="none" stroke-linecap="round"></path>')
    o.append(sheep_row(w * 0.04, w * 0.44, h * 0.94, 5, seed, s=min(0.6, h / 480)) + sheep_row(w * 0.56, w * 0.96, h * 0.92, 5, seed + 1, s=min(0.6, h / 480)))
    return "".join(o)

def dew_lion(w, h, seed):
    """As dew from Jehovah, as showers upon the grass — as a young lion among the flocks of sheep: grass with dew at dawn on
    the left, a young lion going through the flocks on the right."""
    r = random.Random(seed)
    o = [sky(w, h, "#8FB8D8", "#F3E8C8"), ground(w, h, h * 0.6, "#7AA84A", dy=0)]
    for i in range(40):
        x = r.uniform(0, w * 0.48); y = r.uniform(h * 0.64, h)
        o.append(f'<path d="M{f(x)} {f(y)} l -3 -14 M{f(x)} {f(y)} l 4 -12" stroke="#2E6B3A" stroke-width="2"></path><circle cx="{f(x - 3)}" cy="{f(y - 14)}" r="2.4" fill="#E8F6FA" stroke="#8FD0E2" stroke-width="0.8"></circle>')
    o.append(rain(w * 0.48, h * 0.6, seed, n=20, color="#E8F6FA", op=0.6))
    k = min(0.9, h / 300)
    o.append(sheep_row(w * 0.56, w * 0.98, h * 0.98, 4, seed, s=k * 0.6))
    o.append(JG2.lion(w * 0.74, h * 0.8, k * 0.8))
    return "".join(o)

def cut_off(w, h, seed):
    """I will cut off thy horses and destroy thy chariots, and throw down all thy strongholds: an overturned chariot, its
    wheels broken, and a thrown-down fortress behind."""
    o = [sky(w, h, "#5A3A3A", "#D8A07A"), ground(w, h, h * 0.62, "#8A6A4A", dy=0), ruin(w * 0.46, w * 0.98, h * 0.64, h * 0.34, seed)]
    k = min(1.2, h / 220)
    for i, (x, y, rot) in enumerate(((0.16, 0.78, 70), (0.32, 0.84, 20))):           # broken chariot wheels and the pole
        cx, cy, r = w * x, h * y, 34 * k
        o.append(f'<g transform="rotate({rot} {f(cx)} {f(cy)})"><circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="none" stroke="#5A3A1E" stroke-width="{f(6 * k)}"></circle>'
                 + "".join(f'<path d="M{f(cx)} {f(cy)} L {f(cx + r * math.cos(a * 1.05))} {f(cy + r * math.sin(a * 1.05))}" stroke="#5A3A1E" stroke-width="{f(3 * k)}"></path>' for a in range(5))
                 + f'<path d="M{f(cx + r * 0.7)} {f(cy - r * 0.7)} L {f(cx + r)} {f(cy)}" stroke="#F3E8C8" stroke-width="{f(7 * k)}"></path></g>')
    o.append(f'<path d="M{f(w * 0.04)} {f(h * 0.98)} L {f(w * 0.3)} {f(h * 0.9)}" stroke="#6A4A2A" stroke-width="10" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.22)} {f(h * 0.78)} L {f(w * 0.4)} {f(h * 0.72)} L {f(w * 0.42)} {f(h * 0.8)} L {f(w * 0.26)} {f(h * 0.86)} Z" fill="#B8863E" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def idols_down(w, h, seed):
    """I will cut off witchcrafts, thy graven images and thy pillars, and pluck up thine Asherim, and destroy thy cities:
    a broken pillar, a toppled image, a felled Asherah pole, an empty city on the hill under a red sky."""
    o = [sky(w, h, "#3A1A1A", "#C8704A"), ruin(w * 0.56, w * 0.98, h * 0.6, h * 0.22, seed + 3), ground(w, h, h * 0.62, "#6A4A3A", dy=0)]
    k = min(1.3, h / 240)
    x, b = w * 0.18, h * 0.94                               # a standing pillar snapped
    o.append(f'<path d="M{f(x - 16 * k)} {f(b)} L {f(x - 16 * k)} {f(b - 70 * k)} L {f(x - 4 * k)} {f(b - 80 * k)} L {f(x + 6 * k)} {f(b - 66 * k)} L {f(x + 16 * k)} {f(b - 74 * k)} L {f(x + 16 * k)} {f(b)} Z" fill="#A8A098" stroke="#0D0D0F" stroke-width="2.2"></path>'
             f'<path d="M{f(x + 30 * k)} {f(b - 4 * k)} L {f(x + 96 * k)} {f(b - 18 * k)} L {f(x + 100 * k)} {f(b - 2 * k)} L {f(x + 34 * k)} {f(b + 10 * k)} Z" fill="#A8A098" stroke="#0D0D0F" stroke-width="2.2"></path>')
    x = w * 0.46                                            # a graven image fallen on its face, broken
    o.append(f'<rect x="{f(x - 70 * k)}" y="{f(b - 16 * k)}" width="{f(30 * k)}" height="{f(16 * k)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<g transform="translate({f(x)} {f(b - 8 * k)}) rotate(84) scale({f(k)})"><path d="M-12 0 L -12 -54 L -6 -66 L 6 -66 L 12 -54 L 12 0 Z" fill="#C8A040" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M-12 -20 L 12 -20 M-12 -40 L 12 -40" stroke="#8A6A1A" stroke-width="2"></path></g>'
             f'<path d="M{f(x + 40 * k)} {f(b)} l {f(10 * k)} {f(-16 * k)} l {f(12 * k)} {f(4 * k)} l {f(-2 * k)} {f(12 * k)} Z" fill="#C8A040" stroke="#0D0D0F" stroke-width="1.6"></path>'
             f'<path d="M{f(x - 70 * k)} {f(b - 4 * k)} l {f(14 * k)} {f(-6 * k)} l {f(6 * k)} {f(8 * k)} Z" fill="#C8A040" stroke="#0D0D0F" stroke-width="1.4"></path>')
    x = w * 0.7                                             # an Asherah pole hewn down, the stump left
    o.append(f'<rect x="{f(x - 7 * k)}" y="{f(b - 20 * k)}" width="{f(14 * k)}" height="{f(20 * k)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<path d="M{f(x + 10 * k)} {f(b - 6 * k)} L {f(x + 160 * k)} {f(b - 34 * k)}" stroke="#0D0D0F" stroke-width="{f(13 * k)}" stroke-linecap="round"></path>'
             f'<path d="M{f(x + 10 * k)} {f(b - 6 * k)} L {f(x + 160 * k)} {f(b - 34 * k)}" stroke="#7A5A32" stroke-width="{f(9 * k)}" stroke-linecap="round"></path>')
    o.append(smokes([w * 0.66, w * 0.86], h * 0.6, seed, k=max(0.5, h / 400), color="#2A1A1E", op=0.5, n=6))
    return "".join(o)

def mountains_hear(w, h, seed):
    """Hear, O ye mountains, Jehovah's controversy, and ye enduring foundations of the earth: ranges of mountains under a
    storm-lit sky (God is not drawn)."""
    o = [sky(w, h, "#14142E", "#5A4A7A"), halo(w * 0.5, h * 0.1, h * 0.5, "#CFE0FF", 0.35), bolt(w * 0.2, 0, h * 0.36, seed)]
    for i, (y, c) in enumerate(((0.42, "#3A3A5A"), (0.56, "#2A2A44"), (0.72, "#1A1A30"))):
        o.append(hills(w, h, h * y, seed + i, color=c, amp=40 - i * 8, step=110 - i * 15))
    o.append(f'<rect x="-10" y="{f(h * 0.86)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#0D0D1A"></rect>'
             + "".join(f'<path d="M{f(x)} {f(h * 0.86)} L {f(x + 30)} {f(h + 10)}" stroke="#2A2A44" stroke-width="2"></path>' for x in range(0, int(w), 40)))
    return "".join(o)

def exodus_route(w, h):
    """I brought thee up out of the land of Egypt; remember from Shittim unto Gilgal: the way from Egypt to the land, as a
    technical map with Moses, Aaron and Miriam, Balak and Balaam marked."""
    o = [grid_bg(w, h)]
    pts = [("EGYPT", 0.12, 0.8), ("SINAI", 0.36, 0.86), ("KADESH", 0.46, 0.6), ("MOAB", 0.72, 0.46), ("SHITTIM", 0.78, 0.34), ("GILGAL", 0.66, 0.22)]
    o.append(route([(w * x, h * y) for _, x, y in pts], color="#FFD23F"))
    for name, x, y in pts: o.append(node(w * x, h * y, name, color="#8FD0E2", r=5))
    o.append(label(w * 0.14, h * 0.62, "MOSES · AARON · MIRIAM", "#FFD23F", 9, anchor="start"))
    o.append(label(w * 0.96, h * 0.58, "BALAK · BALAAM", "#FF8A6A", 9, anchor="end"))
    return "".join(o)

def offerings(p, w, h, seed):
    """Wherewith shall I come before Jehovah? burnt-offerings, calves a year old, thousands of rams, rivers of oil: an altar
    with the fire, calves and rams led up, jars of oil, a worshipper bowed."""
    from samuel1 import calf
    o = [sky(w, h, "#6A4A3A", "#E8C090"), ground(w, h, h * 0.66, "#B8986A", dy=0), S4.altar(w * 0.5, h * 0.9, min(1.2, h / 260), seed=seed)]
    k = min(0.7, h / 400)
    o.append(calf(w * 0.18, h * 0.94, k) + sheep_row(w * 0.68, w * 0.96, h * 0.94, 3, seed, s=k * 0.9))
    for i in range(3):
        x = w * (0.32 + i * 0.04)
        o.append(f'<path d="M{f(x - 10 * k)} {f(h * 0.96)} C {f(x - 16 * k)} {f(h * 0.96 - 40 * k)} {f(x + 16 * k)} {f(h * 0.96 - 40 * k)} {f(x + 10 * k)} {f(h * 0.96)} Z" fill="#C8A040" stroke="#0D0D0F" stroke-width="1.6"></path>')
    o.append(E.kneel(w * 0.62, h * 0.96, fit(h * 0.96, h * 0.6) * 0.8, color="#5A4A6A", flip=True))
    return "".join(o)

def balances(w, h, seed):
    """Wicked balances, a bag of deceitful weights, a scant measure: the scales tipped, the weights spilled from their bag,
    a half-filled ephah."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A2A3A"></rect>', halo(w * 0.4, h * 0.4, h * 0.6, "#FFC14D", 0.25),
         f'<rect x="-10" y="{f(h * 0.82)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="2"></rect>']
    k = min(1.0, h / 300)
    o.append(f'<g transform="translate({f(w * 0.36)} {f(h * 0.82)}) scale({f(k)})">{scales(0, 0, 1.0, tilt=14)}</g>')
    o.append(f'<path d="M{f(w * 0.66)} {f(h * 0.82)} C {f(w * 0.64)} {f(h * 0.66)} {f(w * 0.72)} {f(h * 0.6)} {f(w * 0.74)} {f(h * 0.62)} C {f(w * 0.78)} {f(h * 0.6)} {f(w * 0.84)} {f(h * 0.66)} {f(w * 0.82)} {f(h * 0.82)} Z" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2"></path>')
    r = random.Random(seed)
    for i in range(5):
        x = w * (0.84 + i * 0.03); o.append(f'<rect x="{f(x)}" y="{f(h * 0.82 - 12 * k)}" width="{f(12 * k)}" height="{f(12 * k)}" fill="#6A6A72" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    o.append(f'<path d="M{f(w * 0.06)} {f(h * 0.82)} L {f(w * 0.08)} {f(h * 0.62)} L {f(w * 0.2)} {f(h * 0.62)} L {f(w * 0.22)} {f(h * 0.82)} Z" fill="#A8804A" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.08)} {f(h * 0.72)} L {f(w * 0.2)} {f(h * 0.72)}" stroke="#E8C060" stroke-width="{f(10 * k)}"></path>')
    return "".join(o)

def futile(w, h, seed):
    """Thou shalt sow, but shalt not reap; tread the olives, but not anoint thee; the vintage, but not drink: a sown field
    gone to dust, an olive press dry, an empty winepress — three cells, each with its label."""
    o = [sky(w, h, "#C8A880", "#F3E8C8")]
    cw = w / 3; k = min(cw / 220, h / 240); g = h * 0.42
    for i in range(3):
        x0 = i * cw
        o.append(f'<g transform="translate({f(x0)} 0)">' + hills(cw, h, g - 6, seed + i, color="#A8906A", amp=8) + ground(cw, h, g, "#C8A070", dy=0))
        if i == 0:
            o.append(grain(0, cw, h * 0.98, h * 0.12, seed, color="#9A8A5A") + grain(0, cw, h * 0.7, h * 0.08, seed + 3, color="#9A8A5A")
                     + label(cw / 2, h * 0.2, "SOW · NOT REAP", "#5A3A22", 10))
        if i == 1:
            o.append(olive(cw * 0.3, h * 0.8, k * 0.8, seed)
                     + f'<ellipse cx="{f(cw * 0.66)}" cy="{f(h * 0.9)}" rx="{f(cw * 0.24)}" ry="{f(cw * 0.07)}" fill="#8A8478" stroke="#0D0D0F" stroke-width="2"></ellipse>'
                     + f'<rect x="{f(cw * 0.6)}" y="{f(h * 0.9 - 90 * k)}" width="{f(cw * 0.12)}" height="{f(90 * k)}" fill="#A89E92" stroke="#0D0D0F" stroke-width="2"></rect>'
                     + label(cw / 2, h * 0.2, "OLIVES · NO OIL", "#5A3A22", 10))
        if i == 2:
            o.append(vines(cw * 0.05, cw * 0.95, h * 0.62, h * 0.62, seed, rows=1, fruit=False)
                     + f'<rect x="{f(cw * 0.16)}" y="{f(h * 0.8)}" width="{f(cw * 0.68)}" height="{f(h * 0.14)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></rect>'
                     + f'<rect x="{f(cw * 0.22)}" y="{f(h * 0.83)}" width="{f(cw * 0.56)}" height="{f(h * 0.08)}" fill="#5A4A3A"></rect>'
                     + label(cw / 2, h * 0.2, "VINTAGE · NO WINE", "#5A3A22", 10))
        o.append('</g>')
        if i: o.append(f'<path d="M{f(x0)} {f(h * 0.12)} L {f(x0)} {f(h + 10)}" stroke="#0D0D0F" stroke-width="3"></path>')
    return "".join(o)

def want(w, h, seed):
    """Therefore I have smitten thee with a grievous wound: thou shalt eat, but not be satisfied; that which thou savest
    will I give up to the sword: an emptied house, the bowls and the bread-basket bare, the storage jar overturned, a
    sword hung by the door."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#5A4030"></rect>',
         f'<rect x="{f(w * 0.62)}" y="{f(h * 0.12)}" width="{f(w * 0.2)}" height="{f(h * 0.76)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.65)}" y="{f(h * 0.18)}" width="{f(w * 0.14)}" height="{f(h * 0.7)}" fill="#E8D0A0"></rect>',
         halo(w * 0.72, h * 0.5, h * 0.5, "#FFE6A0", 0.25),
         f'<rect x="-10" y="{f(h * 0.88)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#3A2A1E" stroke="#0D0D0F" stroke-width="2"></rect>']
    k = min(1.3, h / 230)
    tx, ty = w * 0.3, h * 0.88                              # the low table with empty bowls
    o.append(f'<rect x="{f(tx - 110 * k)}" y="{f(ty - 40 * k)}" width="{f(220 * k)}" height="{f(10 * k)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<path d="M{f(tx - 96 * k)} {f(ty - 30 * k)} L {f(tx - 96 * k)} {f(ty)} M{f(tx + 96 * k)} {f(ty - 30 * k)} L {f(tx + 96 * k)} {f(ty)}" stroke="#5A3A1E" stroke-width="{f(7 * k)}"></path>')
    for dx in (-60, 0, 60):
        o.append(f'<path d="M{f(tx + (dx - 24) * k)} {f(ty - 40 * k)} C {f(tx + (dx - 20) * k)} {f(ty - 58 * k)} {f(tx + (dx + 20) * k)} {f(ty - 58 * k)} {f(tx + (dx + 24) * k)} {f(ty - 40 * k)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.8"></path>'
                 f'<ellipse cx="{f(tx + dx * k)}" cy="{f(ty - 54 * k)}" rx="{f(19 * k)}" ry="{f(4 * k)}" fill="#3A1A10"></ellipse>')
    jx, jy = w * 0.56, h * 0.86                             # the storage jar overturned, empty
    o.append(f'<g transform="translate({f(jx)} {f(jy)}) rotate(-80) scale({f(k)})"><path d="M-20 0 C -36 -30 -26 -70 -10 -80 L -10 -92 L 10 -92 L 10 -80 C 26 -70 36 -30 20 0 Z" fill="#9A5A2E" stroke="#0D0D0F" stroke-width="2"></path></g>')
    sx, sy = w * 0.9, h * 0.3                               # the sword on its peg by the door
    o.append(f'<g transform="translate({f(sx)} {f(sy)}) rotate(8) scale({f(k)})"><path d="M-3 0 L -3 120 L 0 132 L 3 120 L 3 0 Z" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="1.8"></path>'
             '<rect x="-14" y="-4" width="28" height="7" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="1.6"></rect><rect x="-4" y="-26" width="8" height="22" fill="#4A2A1A" stroke="#0D0D0F" stroke-width="1.6"></rect></g>')
    return "".join(o)

def gleaned(w, h, seed):
    """As the grape gleanings of the vintage: there is no cluster to eat — bare vines and a fig-tree without fruit at the
    end of summer."""
    o = [vista(w, h, seed, tone="dusk", hills_n=2, horizon=0.56, field="bare"), fig_tree(w * 0.82, h * 0.98, min(1.0, h / 280), fruit=False, seed=seed)]
    return "".join(o)

def thorns(w, h, seed):
    """The best of them is as a brier, the most upright worse than a thorn hedge; the day of thy watchmen is come: a hedge
    of thorns before shut doors, a watchtower dark on the hill."""
    r = random.Random(seed)
    o = [sky(w, h, "#2A1A2A", "#8A5A5A"), hills(w, h, h * 0.5, seed, color="#3A2A2E", amp=14)]
    x = w * 0.8
    o.append(f'<path d="M{f(x - 16)} {f(h * 0.5)} L {f(x - 12)} {f(h * 0.2)} L {f(x + 12)} {f(h * 0.2)} L {f(x + 16)} {f(h * 0.5)} Z" fill="#4A3A3A" stroke="#0D0D0F" stroke-width="2"></path>')
    for i in range(3):
        hx = w * (0.06 + i * 0.22)
        o.append(f'<rect x="{f(hx)}" y="{f(h * 0.4)}" width="{f(w * 0.18)}" height="{f(h * 0.36)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<rect x="{f(hx + w * 0.06)}" y="{f(h * 0.54)}" width="{f(w * 0.06)}" height="{f(h * 0.22)}" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(ground(w, h, h * 0.76, "#3A2A2A", dy=0))
    for i in range(40):
        x, y = r.uniform(-10, w + 10), h * r.uniform(0.78, 1.0)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-20, 20))} {f(-r.uniform(10, 30))} m 0 0 l 6 -4 m -10 8 l -6 -2" stroke="#1A1210" stroke-width="2.4" fill="none"></path>')
    return "".join(o)

def builders(p, w, h, seed):
    """A day for building thy walls! — builders setting stones on the rising wall, and from far off the roads of the
    nations coming in."""
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.44, seed, color="#9A9A6A", amp=12), ground(w, h, h * 0.5, "#C8A878", dy=0),
         route([(w * 0.02, h * 0.56), (w * 0.3, h * 0.66)], color="#E8B830", dash="8 6"), route([(w * 0.98, h * 0.52), (w * 0.7, h * 0.64)], color="#E8B830", dash="8 6"),
         walls(w * 0.3, w * 0.74, h * 0.96, h * 0.34, seed, towers=2, gate=True, houses=False)]
    s = fit(h * 0.66, h * 0.4)
    for i, x in enumerate((0.36, 0.52, 0.66)):
        o.append(man(p, w * x, h * 0.66, s * 0.6, ["#6A4A3A", "#3A4A6A", "#5A6A3A"][i], up=[(22, -158), (40, -176), (58, -196)] if i == 1 else None))
    return "".join(o)

def carmel(p, w, h, seed):
    """Feed thy people with thy rod, the flock of thy heritage, which dwell solitarily in the forest in the midst of
    Carmel: a flock in a forest glade on the heights, a shepherd's rod standing among them (no shepherd drawn: the prayer
    is to Jehovah)."""
    o = [vista(w, h, seed, tone="day", hills_n=2, horizon=0.56, trees=6, tree_kind="round", sheep=7)]
    x, b = w * 0.46, h * 0.99
    d = f"M{f(x)} {f(b)} L {f(x)} {f(h * 0.62)} C {f(x)} {f(h * 0.55)} {f(x + h * 0.07)} {f(h * 0.55)} {f(x + h * 0.07)} {f(h * 0.62)}"
    o.append(f'<path d="{d}" stroke="#0D0D0F" stroke-width="9" fill="none" stroke-linecap="round"></path><path d="{d}" stroke="#8A6A3A" stroke-width="5" fill="none" stroke-linecap="round"></path>')
    return "".join(o)

def nations_bow(w, h, seed):
    """The nations shall see and be ashamed; they shall lay their hand upon their mouth; they shall lick the dust like a
    serpent: kings in their robes and crowns bowed to the ground before a great light."""
    o = [sky(w, h, "#2A1A3A", "#FFC890"), halo(w * 0.5, h * 0.18, h * 0.6, "#FFF4C2", 0.6), rays(w * 0.5, h * 0.18, 30, h * 0.1, max(w, h), "#FFF4C2", 0.25, 4),
         ground(w, h, h * 0.62, "#8A6A5A", dy=0)]
    ks = min(1.1, h * 0.34 / 130)
    for i in range(5):
        x = w * (0.1 + i * 0.2); c = ["#6A1A5A", "#1F5FAD", "#2E6B3A", "#B5652E", "#7A1A2A"][i]
        fl = i >= 3; sx = -1 if fl else 1; b = h * (0.94 if i % 2 == 0 else 0.86)
        o.append(E.kneel(x, b, ks, color=c, skin=SKIN, flip=fl)
                 + f'<g transform="translate({f(x + sx * 32 * ks)} {f(b - 124 * ks)}) scale({f(ks)})"><path d="M-9 4 L -10 -10 L -4 -4 L 0 -13 L 4 -4 L 10 -10 L 9 4 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path></g>')
    return "".join(o)

def depths(w, h, seed):
    """Thou wilt cast all their sins into the depths of the sea: the calm sea under a clear sky, and below the surface dark
    stones sinking away into the deep."""
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"), sun(w * 0.8, h * 0.12, max(14, h * 0.05), color="#FFE680", op=0.4),
         hgrad(f"dps{seed}", [("0", "#2C7DA8"), ("1", "#03101E")], vertical=True), f'<rect x="-10" y="{f(h * 0.3)}" width="{f(w + 20)}" height="{f(h * 0.8)}" fill="url(#dps{seed})"></rect>',
         f'<path d="M-10 {f(h * 0.3)}' + "".join(f" Q {x + 20} {f(h * 0.3 - 4)} {x + 40} {f(h * 0.3)}" for x in range(-10, int(w) + 40, 40)) + '" stroke="#CFEFFF" stroke-width="2" fill="none"></path>']
    r = random.Random(seed)
    for i in range(9):
        x = w * r.uniform(0.1, 0.9); y = h * (0.4 + i * 0.065); s = 22 * (1 - i * 0.07) * min(1.0, h / 300)
        o.append(f'<path d="M{f(x - s)} {f(y)} L {f(x - s * 0.5)} {f(y - s * 0.7)} L {f(x + s * 0.6)} {f(y - s * 0.6)} L {f(x + s)} {f(y + s * 0.2)} L {f(x + s * 0.2)} {f(y + s * 0.6)} Z" fill="#1A1A22" stroke="#0D0D0F" stroke-width="1.4" opacity="{1 - i * 0.08:.2f}"></path>')
    return "".join(o)
