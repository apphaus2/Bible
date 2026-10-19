"""Drawings for Ezekiel 22–23: the bloody city at dusk; the house of Israel become dross in the furnace; the roaring lion and
the wolves; the gap in the wall where no man stood; Oholah and Oholibah told with restraint, words only over cities, maps
and things — Samaria and Jerusalem with their lovers (a map), the horsemen clothed in blue far off, the Chaldeans portrayed
in vermilion upon the wall (a painted relief), the army with chariots and wagons, the cup of astonishment, the stately
bed and the table (no one there), the heap of stones and the houses burned."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ezk.art7 import *
from ezk.art7 import f, K2, K3, P, rect, seated, clouds, smoke, house, INK, EZ_C, GB_BEARD, CAPT, bg, glow, vgrad, rgrad, KK2, JJ2
from neh.art import horseman
import exodus3 as E3

def bloody_city(w, h, seed):
    """The bloody city: Jerusalem against a red sky at dusk, smoke over the houses (no one drawn)."""
    o = [jerusalem("bc", w, h, seed, mode="dusk")]
    o.append(f'<rect x="-10" y="-1500" width="{f(w + 20)}" height="{f(h * 0.6 + 1500)}" fill="#8A0E16" opacity="0.25"></rect>')
    return "".join(o)

def furnace(w, h, seed):
    """As they gather silver and brass and iron and lead and tin into the midst of the furnace, to blow the fire upon it:
    the furnace glowing, the crucible of molten metal, the dross skimmed off, the bellows."""
    o = [bg(f"fu{seed}", w, h, [(0, "#1A0A0A"), (1, "#4A2A1A")]), f'<rect x="-10" y="{f(h * 0.84)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#2A1A10" stroke="{INK}" stroke-width="2"></rect>']
    cx = w * 0.5; k = min(1.6, h / 240)
    o.append(P(f"M{f(cx - 70 * k)} {f(h * 0.86)} L {f(cx - 56 * k)} {f(h * 0.86 - 110 * k)} L {f(cx + 56 * k)} {f(h * 0.86 - 110 * k)} L {f(cx + 70 * k)} {f(h * 0.86)} Z", "#6A4A3A", 2.6))
    o.append(P(f"M{f(cx - 34 * k)} {f(h * 0.86)} L {f(cx - 34 * k)} {f(h * 0.86 - 50 * k)} Q {f(cx)} {f(h * 0.86 - 76 * k)} {f(cx + 34 * k)} {f(h * 0.86 - 50 * k)} L {f(cx + 34 * k)} {f(h * 0.86)} Z", "#1A0A0A", 2))
    o.append(E.blaze(cx, h * 0.86, 60 * k, 60 * k, seed, n=5))
    o.append(P(f"M{f(cx - 40 * k)} {f(h * 0.86 - 110 * k)} C {f(cx - 40 * k)} {f(h * 0.86 - 150 * k)} {f(cx + 40 * k)} {f(h * 0.86 - 150 * k)} {f(cx + 40 * k)} {f(h * 0.86 - 110 * k)} Z", "#5A5A64", 2.2))
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(h * 0.86 - 128 * k)}" rx="{f(36 * k)}" ry="{f(8 * k)}" fill="#FFB04A" stroke="{INK}" stroke-width="1.6"></ellipse>')
    o.append(glow(f"fg{seed}", cx, h * 0.86 - 128 * k, 60 * k, 30 * k, "#FF8A3D", 0.7))
    o.append("".join(f'<circle cx="{f(cx + (i - 2) * 9 * k)}" cy="{f(h * 0.86 - 128 * k)}" r="{f(3 * k)}" fill="#3A2A2A"></circle>' for i in range(5)))
    bx = cx + 110 * k
    o.append(P(f"M{f(bx)} {f(h * 0.86 - 20 * k)} L {f(bx + 50 * k)} {f(h * 0.86 - 40 * k)} L {f(bx + 50 * k)} {f(h * 0.86)} Z", "#8A5A30", 2) + f'<path d="M{f(bx)} {f(h * 0.86 - 20 * k)} L {f(cx + 70 * k)} {f(h * 0.86 - 30 * k)}" stroke="#3A2A1A" stroke-width="{f(5 * k)}"></path>')
    for i, (nm, c) in enumerate((("SILVER", "#C8C8D0"), ("BRASS", "#B87333"), ("IRON", "#6A6A74"), ("LEAD", "#8A8A9A"), ("TIN", "#D8D8E0"))):
        x = w * (0.08 + i * 0.07)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.86 - 18 * k)}" width="{f(w * 0.05)}" height="{f(14 * k)}" fill="{c}" stroke="{INK}" stroke-width="1.4"></rect>' + label(x + w * 0.025, h * 0.95, nm, c, 8))
    return "".join(o)

def gap(w, h, seed):
    """I sought for a man among them that should build up the wall and stand in the gap before me, but I found none: the
    wall broken, the gap open and empty."""
    o = [bg(f"gp{seed}", w, h, [(0, "#2A2A4A"), (1, "#C8A080")]), hills(w, h, h * 0.5, seed, "#7A6A6A", amp=8, step=90)]
    o.append(J.jericho(-10, w * 0.4, h * 0.36, h * 0.84, seed, color="#A88A6A", towers=1, houses=False))
    o.append(J.jericho(w * 0.6, w + 10, h * 0.36, h * 0.84, seed + 1, color="#A88A6A", towers=1, houses=False))
    o.append(rubble(w * 0.4, w * 0.6, h * 0.86, h * 0.1, seed))
    o.append(ground(w, h, h * 0.84, "#8A7A5A", dy=0))
    o.append(glow(f"gg{seed}", w * 0.5, h * 0.6, w * 0.08, h * 0.3, "#FFE680", 0.3))
    return "".join(o)

def oholah_map(w, h, stage=0):
    """Oholah is Samaria, and Oholibah Jerusalem: the two cities as a map with the lovers they went after — Egypt in their
    youth, Assyria (stage 0), the Chaldeans of Babylon (stage 1); stage 2: the Babylonians, Pekod, Shoa and Koa and all the
    Assyrians come against Jerusalem."""
    o = [grid_bg(w, h)]
    S, J0 = (w * 0.3, h * 0.36), (w * 0.32, h * 0.62)
    Eg, As, Ba = (w * 0.08, h * 0.9), (w * 0.78, h * 0.12), (w * 0.9, h * 0.64)
    o.append(route([S, Eg], color="#4A7A9A", sw=1.6, dash="4 6", arrow=False) + route([J0, Eg], color="#4A7A9A", sw=1.6, dash="4 6", arrow=False))
    if stage == 0: o.append(route([S, As], color="#FF8A6A", sw=2.4))
    if stage == 1: o.append(route([J0, As], color="#FF8A6A", sw=2) + route([J0, Ba], color="#FF8A6A", sw=2.4))
    if stage == 2:
        for src in (Ba, As, (w * 0.86, h * 0.84)):
            o.append(route([src, J0], color="#D7261E", sw=3))
        o.append(label(w * 0.86, h * 0.94, "PEKOD · SHOA · KOA", "#FF8A6A", 8))
    o.append(node(*S, "SAMARIA · OHOLAH", "#FFD23F" if stage == 0 else "#8FD0E2", r=6, dy=-12, size=9))
    o.append(node(*J0, "JERUSALEM · OHOLIBAH", "#FFD23F" if stage else "#8FD0E2", r=7, dy=-14, size=9))
    o.append(node(*Eg, "EGYPT", "#8FD0E2", r=5, dy=-11, size=9) + node(*As, "ASSYRIA", "#8FD0E2", r=5, dy=-11, size=9) + node(*Ba, "BABYLON", "#8FD0E2", r=5, dy=-11, size=9))
    return "".join(o)

def blue_horsemen(p, w, h, seed):
    """The Assyrians clothed with blue, governors and rulers, horsemen riding upon horses — far off on the plain."""
    o = [mk.defs(p, *ALL), bg(f"bh{seed}", w, h, [(0, "#6A8AB0"), (1, "#E8D0A0")]), hills(w, h, h * 0.6, seed, "#9A8A6A", amp=8, step=90), ground(w, h, h * 0.68, "#C8A878", dy=0)]
    s = min(fit(h * 0.96, h * 0.5), 0.9) * 0.6
    for i in range(5):
        o.append(horseman(p, w * (0.12 + i * 0.18), h * (0.9 + (i % 2) * 0.05), s, cloth="#1F3A8A", color=["#3A2214", "#5A3A22", "#2A1A10"][i % 3]))
    return "".join(o)

def vermilion(w, h, seed):
    """Men portrayed upon the wall, the images of the Chaldeans portrayed with vermilion, girded, with flowing turbans,
    captains on horseback: a painted relief on a palace wall (pictures, not men)."""
    o = [bg(f"vm{seed}", w, h, [(0, "#3A2A2A"), (1, "#6A4A3A")]), f'<rect x="-10" y="{f(h * 0.1)}" width="{f(w + 20)}" height="{f(h * 0.8)}" fill="#D8C8A0" stroke="{INK}" stroke-width="2.4"></rect>']
    o.append(f'<rect x="-10" y="{f(h * 0.16)}" width="{f(w + 20)}" height="4" fill="#B5121B"></rect><rect x="-10" y="{f(h * 0.82)}" width="{f(w + 20)}" height="4" fill="#B5121B"></rect>')
    k = min(1.2, h / 300)
    for i in range(4):
        x = w * (0.12 + i * 0.25); y = h * 0.78
        o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(k)})" fill="none" stroke="#B5121B" stroke-width="3" stroke-linejoin="round">'
                 '<path d="M-50 0 L -44 -40 C -40 -60 30 -66 40 -44 L 56 -60 L 62 -50 L 48 -36 L 46 0 M-40 -40 L -60 -30"></path>'
                 '<path d="M-6 -56 L -8 -96 M-8 -96 C -16 -100 -16 -114 -6 -118 C 6 -120 12 -108 6 -98 Z M-14 -118 C -24 -124 -30 -116 -34 -108"></path>'
                 '<path d="M-8 -80 L 20 -70 M-14 -66 L 10 -66"></path></g>')
    return "".join(o)

def army(p, w, h, seed):
    """They shall come against thee with weapons, chariots and wagons, with a company of peoples, buckler and shield and
    helmet, round about: the host on the plain before the city (no battle drawn)."""
    o = [mk.defs(p, *ALL), bg(f"ar{seed}", w, h, [(0, "#5A4A5A"), (1, "#D8B080")]), J.city_hill(w * 0.12, h * 0.6, w * 0.16, h * 0.18, seed), ground(w, h, h * 0.6, "#A88A5A", dy=0)]
    k = min(0.8, h / 400)
    for i in range(3): o.append(E3.chariot(w * (0.3 + i * 0.22), h * 0.8 - i * 4, k * 0.7, flip=True, color="#3A2214", driver="#3A3A5A"))
    s = min(fit(h * 0.98, h * 0.6), 0.8)
    for i in range(10): o.append(warrior(p, w * (0.22 + i * 0.08), h * 0.98 - (i % 2) * 6, s * 0.8, "#3A3A5A"))
    return "".join(o)

def cup(w, h, seed):
    """Thy sister's cup, deep and large, the cup of astonishment and desolation, drained, its sherds gnawed: a great dark
    cup overflowing, set on a stone."""
    o = [bg(f"cu{seed}", w, h, [(0, "#1A0A1A"), (1, "#4A2A3A")]), glow(f"cg{seed}", w * 0.5, h * 0.6, w * 0.3, h * 0.4, "#8A0E16", 0.4)]
    cx, cy = w * 0.5, h * 0.62; R = min(w * 0.18, h * 0.32)
    o.append(f'<rect x="{f(cx - R * 1.2)}" y="{f(cy + R * 0.9)}" width="{f(R * 2.4)}" height="{f(R * 0.3)}" fill="#5A5A5A" stroke="{INK}" stroke-width="2"></rect>')
    o.append(P(f"M{f(cx - R)} {f(cy - R * 0.4)} C {f(cx - R)} {f(cy + R * 0.5)} {f(cx + R)} {f(cy + R * 0.5)} {f(cx + R)} {f(cy - R * 0.4)} Z", "#8A6A2A", 2.6))
    o.append(f'<path d="M{f(cx - R * 0.1)} {f(cy + R * 0.3)} L {f(cx - R * 0.12)} {f(cy + R * 0.9)} M{f(cx + R * 0.1)} {f(cy + R * 0.3)} L {f(cx + R * 0.12)} {f(cy + R * 0.9)}" stroke="{INK}" stroke-width="3"></path>'
             + P(f"M{f(cx - R * 0.4)} {f(cy + R * 0.9)} L {f(cx + R * 0.4)} {f(cy + R * 0.9)} L {f(cx + R * 0.2)} {f(cy + R * 0.7)} L {f(cx - R * 0.2)} {f(cy + R * 0.7)} Z", "#8A6A2A", 2))
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy - R * 0.4)}" rx="{f(R)}" ry="{f(R * 0.2)}" fill="#3A0A10" stroke="{INK}" stroke-width="2.4"></ellipse>')
    o.append(P(f"M{f(cx + R * 0.8)} {f(cy - R * 0.36)} C {f(cx + R * 1.1)} {f(cy - R * 0.1)} {f(cx + R * 1.05)} {f(cy + R * 0.4)} {f(cx + R * 1.1)} {f(cy + R * 0.9)} L {f(cx + R * 0.98)} {f(cy + R * 0.9)} C {f(cx + R * 0.96)} {f(cy + R * 0.3)} {f(cx + R * 0.92)} {f(cy - R * 0.1)} {f(cx + R * 0.7)} {f(cy - R * 0.3)} Z", "#5A0A10", 1.6))
    return "".join(o)

def stately_bed(w, h, seed):
    """A stately bed with a table prepared before it, whereupon thou didst set mine incense and mine oil: the room alone,
    the couch, the table, the lamp (no one there)."""
    o = [bg(f"sb{seed}", w, h, [(0, "#2A1A2A"), (1, "#5A3A3A")]), f'<rect x="-10" y="{f(h * 0.72)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="#3A2A2A" stroke="{INK}" stroke-width="2"></rect>']
    k = min(1.4, h / 260)
    bx = w * 0.3
    o.append(P(f"M{f(bx - 110 * k)} {f(h * 0.8)} L {f(bx - 110 * k)} {f(h * 0.8 - 30 * k)} L {f(bx + 110 * k)} {f(h * 0.8 - 30 * k)} L {f(bx + 110 * k)} {f(h * 0.8)} Z", "#7A2A5A", 2.2)
             + P(f"M{f(bx - 110 * k)} {f(h * 0.8 - 30 * k)} L {f(bx - 110 * k)} {f(h * 0.8 - 70 * k)} L {f(bx - 90 * k)} {f(h * 0.8 - 70 * k)} L {f(bx - 90 * k)} {f(h * 0.8 - 30 * k)} Z", "#E8B830", 2)
             + "".join(f'<rect x="{f(bx + dx * k)}" y="{f(h * 0.8)}" width="{f(8 * k)}" height="{f(20 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="1.4"></rect>' for dx in (-104, 96)))
    tx = w * 0.72
    o.append(f'<rect x="{f(tx - 60 * k)}" y="{f(h * 0.8 - 40 * k)}" width="{f(120 * k)}" height="{f(10 * k)}" fill="#8A5A30" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(tx + dx * k)}" y="{f(h * 0.8 - 30 * k)}" width="{f(6 * k)}" height="{f(50 * k)}" fill="#6A4A2A" stroke="{INK}" stroke-width="1.4"></rect>' for dx in (-56, 50)))
    o.append(P(f"M{f(tx - 30 * k)} {f(h * 0.8 - 40 * k)} L {f(tx - 34 * k)} {f(h * 0.8 - 62 * k)} L {f(tx - 16 * k)} {f(h * 0.8 - 62 * k)} L {f(tx - 20 * k)} {f(h * 0.8 - 40 * k)} Z", "#C8A040", 1.6))
    o.append(smoke(tx - 25 * k, h * 0.8 - 70 * k, 5, seed, color="#C8B8A8", op=0.4, k=k * 0.5))
    o.append(P(f"M{f(tx + 14 * k)} {f(h * 0.8 - 40 * k)} C {f(tx + 10 * k)} {f(h * 0.8 - 60 * k)} {f(tx + 34 * k)} {f(h * 0.8 - 60 * k)} {f(tx + 30 * k)} {f(h * 0.8 - 40 * k)} Z", "#8A6A5A", 1.6))
    return "".join(o)

def stones_fire(w, h, seed):
    """The company shall stone them with stones and burn their houses with fire: a heap of stones before houses burning, no
    one drawn."""
    o = [bg(f"sf{seed}", w, h, [(0, "#2A0A0A"), (1, "#8A3A1A")])]
    for i in range(4):
        o.append(house(w * (0.5 + i * 0.12), h * 0.8, w * 0.11, h * (0.3 + (i % 2) * 0.1), color="#6A4A3A"))
        o.append(f'<g opacity="0.9">' + E.blaze(w * (0.555 + i * 0.12), h * (0.5 - (i % 2) * 0.1), w * 0.08, h * 0.2, seed + i, n=4) + '</g>')
    o.append(smoke(w * 0.7, h * 0.3, 7, seed, color="#2A1A1A", op=0.6, k=h / 300))
    o.append(ground(w, h, h * 0.8, "#3A2A1A", dy=0))
    o.append(S4.stone_heap(w * 0.24, h * 0.92, w * 0.3, h * 0.3, seed))
    return "".join(o)
