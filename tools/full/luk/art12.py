"""Drawings for Luke 21–22: Jerusalem compassed with armies — the camps and their standards ringed about the walls, smoke
going up (no fighting drawn); the two swords laid on the table of the upper room; on the mount of Olives the angel from
heaven strengthening him — Jesus kneeling far off under the olives, a figure of white light standing by (the sweat as great
drops of blood told in words only). Built on luk.art11."""
from luk.art11 import *
from luk.art11 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, jesus_risen, roman_fig, torch, \
    jesus_kneel, light_seated, WOMEN3, PURPLE, GOLD, kneel_w, boy_fig, zach_fig, elis_fig, shepherd_fig, swaddled, fish_heap, WIDOW_C, WIDOW_V, SINNER_C, SINNER_V, \
    JOANNA, SUSANNA, SAMARITAN_C, samaritan_fig, priest_fig, levite_fig, RICH_C, rich_fig, barn, son_fig, father_fig, elder_fig, farm, LAZ_C, LEPER_C, ZAC_C, \
    zacchaeus_fig
import random, math
from oba.minor import cup

def compassed(p, w, h, seed):
    """When ye see Jerusalem compassed with armies: the city on its hill under a heavy sky, and all about it on the slopes the
    tents and earthworks of the camps, rows of standards, the smoke of their fires — no one fighting drawn."""
    r = random.Random(seed)
    o = [jerusalem_far(w, h, seed, tone="storm")]
    for i in range(14):
        x = w * (0.02 + 0.96 * i / 13) + r.uniform(-8, 8); y = h * (0.82 + 0.1 * r.random())
        tw = max(10, h * 0.05)
        o.append(f'<path d="M{f(x - tw)} {f(y)} L {f(x)} {f(y - tw)} L {f(x + tw)} {f(y)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="1.6"></path>')
    for i in range(6):
        x = w * (0.08 + 0.17 * i)
        o.append(f'<path d="M{f(x)} {f(h * 0.94)} L {f(x)} {f(h * 0.74)}" stroke="#3A2A1A" stroke-width="2.4"></path>'
                 f'<rect x="{f(x)}" y="{f(h * 0.74)}" width="{f(14)}" height="10" fill="#8A1A1A" stroke="{INK}" stroke-width="1.2"></rect>'
                 f'<circle cx="{f(x)}" cy="{f(h * 0.73)}" r="3.4" fill="{GOLD}"></circle>')
    o.append(smokes([w * r.uniform(0.05, 0.95) for _ in range(4)], h * 0.84, seed, k=max(0.5, h / 400), color="#4A4450", op=0.5))
    return "".join(o)

def two_swords(p, w, h, seed):
    """Lord, behold, here are two swords: on the table of the upper room under the lamp, among the bread and the cups, two
    short swords laid side by side in their sheaths."""
    o = [bgr(w, h, "#2A1E1A"), glow(w * 0.5, h * 0.4, h * 0.7, "#FFE680", 0.4, f"{p}g"), A.lamp(w * 0.5, h * 0.2, max(0.6, h / 300)),
         f'<rect x="-10" y="{f(h * 0.6)}" width="{f(w + 20)}" height="{f(h)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2.4"></rect>']
    k = max(0.6, h / 280)
    for i, dy in enumerate((0, 22)):
        y = h * 0.72 + dy * k
        o.append(f'<rect x="{f(w * 0.3)}" y="{f(y - 5 * k)}" width="{f(150 * k)}" height="{f(10 * k)}" rx="{f(4 * k)}" fill="#5A3A22" stroke="{INK}" stroke-width="1.8"></rect>'
                 f'<rect x="{f(w * 0.3 - 10 * k)}" y="{f(y - 12 * k)}" width="{f(8 * k)}" height="{f(24 * k)}" fill="#C8963E" stroke="{INK}" stroke-width="1.6"></rect>'
                 f'<rect x="{f(w * 0.3 - 40 * k)}" y="{f(y - 4 * k)}" width="{f(30 * k)}" height="{f(8 * k)}" fill="#8A6A4A" stroke="{INK}" stroke-width="1.4"></rect>')
    o.append(loaf(w * 0.14, h * 0.66, k * 0.8) + cup(w * 0.82, h * 0.68, k * 0.4))
    return "".join(o)

def strengthened(p, w, h, seed):
    """There appeared unto him an angel from heaven, strengthening him: the garden of olives at night, Jesus kneeling alone
    far off in the moonlight with his face bowed, and beside him a figure of white light with a gold rim, no face."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#1E1650"), mk.stars(40, w, h * 0.4, seed), moon(w * 0.84, h * 0.14, max(8, h * 0.04)),
         hills(w, h, h * 0.56, seed, color="#14142E", amp=10, step=80), ground(w, h, h * 0.66, "#1A1830", dy=0)]
    for i, x in enumerate((0.06, 0.92)):
        o.append(olive(w * x, h * 0.98, max(0.5, h / 300), seed=seed + i))
    s = fit(b, max(h * 0.3, b - 200))
    o.append(glow(w * 0.56, b - 80 * s, 160 * s, "#FFFFFF", 0.6, f"{p}a"))
    o.append(jesus_kneel(w * 0.46, b, s * 0.8))
    o.append(angel(p, w * 0.6, b, s * 0.92, up=UP_BLESS))
    return "".join(o)
