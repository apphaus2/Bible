"""Drawings for Ezekiel 43–44: the glory of the God of Israel coming from the way of the east, the earth shining (light, no
figure); the house filled with the glory; the altar of the vision as a blueprint (the bottom, the lesser and greater ledges,
the altar hearth twelve by twelve with its four horns, the steps toward the east); the altar's consecration (the young
bullock, the he-goat, the ram, the salt — whole beasts beside the altar, then fire); the outer east gate shut; the prince
eating bread in the gate; the Levites keeping the gates; the priests the sons of Zadok in linen garments; their inheritance."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ezk.art15 import *
from ezk.art15 import f, K2, K3, P, rect, seated, clouds, smoke, house, INK, EZ_C, GB_BEARD, CAPT, bg, glow, vgrad, rgrad, KK2, JJ2, J1, LIT, LINE, FILL
from lev import art as LA
import exodus4 as E4

def glory_east(p, w, h, seed):
    """The glory of the God of Israel came from the way of the east, his voice like the sound of many waters, and the earth
    shined with his glory: a great light rising over the eastern hills toward the east gate, the land lit gold; Ezekiel
    fallen upon his face before the gate."""
    o = [mk.defs(p, *ALL), bg(f"ge{seed}", w, h, [(0, "#1A1A4A"), (0.6, "#E8A060"), (1, "#FFE8A0")])]
    o.append(glory(f"geg{seed}", w * 0.84, h * 0.6, w * 0.16, h * 0.7, seed))
    o.append(V.rays(w * 0.84, h * 0.4, 30, h * 0.1, w * 1.2, color="#FFF4C2", op=0.22))
    o.append(hills(w, h, h * 0.66, seed, "#C8905A", amp=10, step=80))
    o.append(S4.gatehouse(w * 0.36, h * 0.92, w * 0.5, h * 0.5))
    o.append(f'<rect x="-10" y="{f(h * 0.92)}" width="{f(w + 20)}" height="{f(h * 0.1)}" fill="#E8C878" stroke="{INK}" stroke-width="2"></rect>')
    o.append(N.prostrate(w * 0.66, h * 0.98, min(1.0, h / 400), color=EZ_C, skin=SKIN))
    return "".join(o)

def altar_plate(w, h):
    """The measures of the altar by cubits (the cubit a cubit and a handbreadth): the bottom a cubit; the lower ledge two
    cubits; the greater ledge four cubits; the upper altar four cubits, and from the altar hearth four horns; the hearth twelve
    by twelve, the ledge fourteen by fourteen, the border half a cubit; the steps looking toward the east."""
    o = [bp(w, h), title_bar(w, "THE MEASURES OF THE ALTAR · BY CUBITS")]
    u = min(w * 0.7 / 20, h * 0.74 / 12.5)
    cx, base = w * 0.46, h * 0.92
    tiers = [(18, 1, "#4A5A6A"), (16, 2, "#5A6A7A"), (14, 4, "#6A7A8A"), (12, 4, "#B07A3A")]
    y = base
    for wd, ht, c in tiers:
        o.append(f'<rect x="{f(cx - wd / 2 * u)}" y="{f(y - ht * u)}" width="{f(wd * u)}" height="{f(ht * u)}" fill="{c}" stroke="{LINE}" stroke-width="2"></rect>')
        y -= ht * u
    for dx in (-5.5, 5.5):
        o.append(f'<path d="M{f(cx + dx * u - 0.5 * u)} {f(y)} L {f(cx + dx * u)} {f(y - 1.2 * u)} L {f(cx + dx * u + 0.5 * u)} {f(y)} Z" fill="{BGOLD}" stroke="#0D0D0F" stroke-width="1.6"></path>')
    o.append(E.blaze(cx, y, 8 * u, 2.6 * u, 4301, n=5))
    sx = cx + 9 * u
    for i in range(7):
        o.append(f'<rect x="{f(sx + i * 0.7 * u)}" y="{f(base - 11 * u + i * 1.5 * u)}" width="{f(0.7 * u + 2)}" height="{f(1.5 * u)}" fill="#3A4A5A" stroke="{LINE}" stroke-width="1"></rect>')
    o.append(tag(sx + 2 * u, base - 8 * u, "THE STEPS · TOWARD THE EAST", w * 0.78, h * 0.3))
    o.append(dim(cx - 9 * u - 14, base, cx - 9 * u - 14, base - 1 * u, "1", size=8, off=0))
    o.append(dim(cx - 8 * u - 14, base - 1 * u, cx - 8 * u - 14, base - 3 * u, "2", size=8))
    o.append(dim(cx - 7 * u - 14, base - 3 * u, cx - 7 * u - 14, base - 7 * u, "4", size=8))
    o.append(dim(cx - 6 * u - 14, base - 7 * u, cx - 6 * u - 14, base - 11 * u, "4", size=8))
    o.append(dim(cx - 6 * u, base - 11 * u - 30, cx + 6 * u, base - 11 * u - 30, "HEARTH · 12 × 12", size=8))
    o.append(tag(cx + 7 * u, base - 5 * u, "LEDGE · 14 × 14", w * 0.8, h * 0.62) + tag(cx + 5.5 * u, base - 11.8 * u, "FOUR HORNS", w * 0.8, h * 0.16))
    return "".join(o)

def consecration(p, w, h, seed, beast="bullock"):
    """The ordinances of the altar: the young bullock for a sin-offering, the he-goat, the ram, the salt cast upon them — the
    whole beasts led beside the altar, the priests in linen, the fire upon the hearth (no carcass drawn)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(f"cs{seed}", w, h, [(0, "#5A6A8A"), (1, "#E8D8B8")]), ground(w, h, h * 0.6, "#C8B898", dy=0)]
    o.append(K1.temple_front(w * 0.82, h * 0.6, w * 0.3, seed))
    o.append(K1.horned_altar(w * 0.5, b - 4, min(1.0, h / 300), fire=True, seed=seed))
    s = min(fit(b, h * 0.42), 1.0)
    o.append({"bullock": S1.cow(w * 0.24, b, s * 1.05, color="#5A3A22", patch="#3A2214"), "goat": LA.goat(w * 0.24, b, s * 1.2), "ram": E.sheep(w * 0.24, b, s * 1.2)}[beast])
    o.append(K1.priest(p, w * 0.1, b, s) + K1.priest(p, w * 0.7, b, s * 0.95, flip=True))
    o.append(LA.salt(w * 0.38, b, s * 1.4))
    return "".join(o)

def shut_gate(p, w, h, seed, prince=False):
    """This gate shall be shut; it shall not be opened, neither shall any man enter in by it: the outer east gate with its
    doors shut and barred, the glory's light behind the wall; prince=True: the prince seated in the porch of the gate to eat
    bread before Jehovah."""
    o = [mk.defs(p, *ALL), bg(f"sg{seed}", w, h, [(0, "#3A4A7A"), (1, "#E8D0A0")])]
    o.append(glow(f"sgg{seed}", w * 0.5, h * 0.3, w * 0.4, h * 0.3, "#FFE680", 0.5))
    o.append(J.jericho(-10, w + 10, h * 0.34, h * 0.9, seed, color="#C8B090", towers=2, houses=False))
    gx, gw = w * 0.5, w * 0.24
    o.append(f'<rect x="{f(gx - gw / 2)}" y="{f(h * 0.4)}" width="{f(gw)}" height="{f(h * 0.5)}" fill="#B8A07A" stroke="{INK}" stroke-width="2.4"></rect>')
    o.append(P(f"M{f(gx - gw * 0.32)} {f(h * 0.9)} L {f(gx - gw * 0.32)} {f(h * 0.56)} Q {f(gx)} {f(h * 0.46)} {f(gx + gw * 0.32)} {f(h * 0.56)} L {f(gx + gw * 0.32)} {f(h * 0.9)} Z", "#6A4A2A", 2.4))
    o.append(f'<path d="M{f(gx)} {f(h * 0.52)} L {f(gx)} {f(h * 0.9)}" stroke="#3A2A1A" stroke-width="2"></path>'
             f'<rect x="{f(gx - gw * 0.36)}" y="{f(h * 0.7)}" width="{f(gw * 0.72)}" height="{f(h * 0.03)}" fill="#3A3A44" stroke="{INK}" stroke-width="1.6"></rect>')
    for i in range(4):
        for j in range(5):
            o.append(f'<circle cx="{f(gx - gw * 0.26 + i * gw * 0.17)}" cy="{f(h * 0.6 + j * h * 0.06)}" r="2.4" fill="#C8A040"></circle>')
    o.append(ground(w, h, h * 0.9, "#B8A888", dy=0))
    if prince:
        s = min(h * 0.3 / 135, 0.8)
        o.append(seated(w * 0.78, h * 0.98, s, "#5A2A7A", head="#5A2A7A", beard="#2A1A10", band=True, flip=True))
        o.append(f'<ellipse cx="{f(w * 0.7)}" cy="{f(h * 0.97)}" rx="{f(14 * s * 2)}" ry="{f(5 * s * 2)}" fill="#C8A060" stroke="{INK}" stroke-width="1.4"></ellipse>')
    return "".join(o)

def gatekeepers(p, w, h, seed):
    """The Levites ministers in the sanctuary, having oversight at the gates of the house: keepers standing at a gate of the
    court with staves, the people's offerings brought."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bg(f"gk{seed}", w, h, [(0, "#5A6A8A"), (1, "#E8D8B8")]), S4.gatehouse(w * 0.5, h * 0.9, w * 0.6, h * 0.6), ground(w, h, h * 0.9, "#C8B898", dy=0)]
    s = min(fit(b, h * 0.4), 0.9)
    for i, x in enumerate((0.12, 0.88)):
        o.append(mk.person(p, round(w * x), round(b), round(s, 3), body=SKIN, cloth="#5A6A8A", sw=3, flip=i == 1, extra=A.headcloth("#E8E2D6") + A.BLACK_BEARD))
        o.append(f'<path d="M{f(w * x + (16 if i == 0 else -16) * s)} {f(b)} L {f(w * x + (16 if i == 0 else -16) * s)} {f(b - 200 * s)}" stroke="#5A3A1A" stroke-width="{f(4 * s)}"></path>')
    return "".join(o)

def linen_priests(p, w, h, seed):
    """When they enter in at the gates of the inner court, they shall be clothed with linen garments, linen tires upon their
    heads, linen breeches: the sons of Zadok in white linen at the inner gate, the outer garments laid in the holy chambers."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bg(f"lp{seed}", w, h, [(0, "#6A8AB0"), (1, "#F3E8D0")]), K1.temple_front(w * 0.72, h * 0.66, w * 0.4, seed), ground(w, h, h * 0.66, "#E8DCC0", dy=0)]
    s = min(fit(b, h * 0.36), 1.0)
    for i in range(4):
        o.append(K1.priest(p, w * (0.1 + i * 0.13), b - (i % 2) * 6, s * (1 - 0.04 * i)))
    o.append(f'<rect x="{f(w * 0.66)}" y="{f(b - 40 * s)}" width="{f(80 * s)}" height="{f(40 * s)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.66 + 6)} {f(b - 40 * s)} l {f(30 * s)} {f(-14 * s)} l {f(36 * s)} {f(14 * s)}" fill="#5A3A6A" stroke="{INK}" stroke-width="1.6"></path>')
    return "".join(o)

def firstfruits(w, h, seed):
    """The first of all the first-fruits of every thing, and every oblation, shall be for the priest; the first of your dough:
    baskets of first-fruits, loaves and the meal-offering set before the house."""
    o = [bg(f"ff{seed}", w, h, [(0, "#C8905A"), (1, "#F3E0B0")]), K1.temple_front(w * 0.76, h * 0.6, w * 0.3, seed), ground(w, h, h * 0.6, "#D8C8A0", dy=0)]
    k = min(1.6, h / 200)
    for i in range(4):
        x = w * (0.1 + i * 0.14)
        o.append(E4.basket(x, h * 0.92, k * 1.4) if i % 2 == 0 else LA.ears(x - 10 * k, h * 0.92, k, 3))
    o.append(LA.cakes(w * 0.62, h * 0.94, k) if hasattr(LA, "cakes") else "")
    return "".join(o)
