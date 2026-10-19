"""Drawings for the Ezra volume (chapter by chapter, added below), on top of 2 Chronicles' (chr2.art, which carries chr1.art,
kg2.art, kg1.art and 2 Samuel's drawings as K2)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from chr2.art import *
from chr2.art import f, K2, K3, K1

PERSIA_C = "#7A2A6A"

# ---- Ezra 1–2 -----------------------------------------------------------------------------------------------------------
def return_caravan(p, w, h, seed, ruins=True):
    """The children of the captivity going up to Jerusalem: a long train of people, camels, asses and mules winding west
    toward the hill of Jerusalem with its broken walls."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#FFC890", "#FFE6B0"), sun(w * 0.86, h * 0.3, 22, color="#FFF4C2", op=0.4),
         hills(w, h, h * 0.46, seed, "#B8946A", amp=12, step=90)]
    if ruins:
        o.append(J.city_hill(w * 0.14, h * 0.5, w * 0.3, h * 0.2, seed))
        o.append(f'<path d="M{f(w * 0.02)} {f(h * 0.36)} l {f(w * 0.04)} -12 l {f(w * 0.03)} 14 l {f(w * 0.05)} -8 l {f(w * 0.04)} 10" stroke="#0D0D0F" stroke-width="2" fill="none"></path>')
    o.append(ground(w, h, h * 0.52, "#C8A06A", dy=0))
    items = []
    for i in range(18):
        k = i / 17; x = w * (0.98 - 0.72 * k) + r.uniform(-10, 10); y = h * (0.97 - 0.36 * k)
        items.append((y, x, r.random()))
    for y, x, q in sorted(items):
        k = (y - h * 0.6) / (h * 0.37); s = max(0.12, 0.18 + 0.4 * k)
        if q < 0.2: o.append(J1.camel(x, y, h * s * 0.0034, flip=True, color="#B5844A"))
        elif q < 0.4: o.append(N.ass(x, y, h * s * 0.003, color="#7A6A5A"))
        else: o.append(man(p, x, y, fit(y, y - h * 0.5 * s), r.choice(["#6A3A2A", "#3A4A6A", "#5A4A3A", "#4A5A3A", "#E8D8B0", "#7A5A3A"]), flip=True))
    return "".join(o)

# ---- Ezra 3–4 -----------------------------------------------------------------------------------------------------------
def altar_ruins(p, w, h, seed, foundation=False, weep=False):
    """The altar set upon its base among the ruins of the house on the mount, the morning burnt-offering smoking
    (foundation=True: the foundation stones laid in courses, priests with trumpets; weep=True: old men with covered heads
    among them)."""
    r = random.Random(seed)
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), J.city_hill(w * 0.84, h * 0.5, w * 0.3, h * 0.16, seed), ground(w, h, h * 0.62, "#C8B88A", dy=0)]
    for _ in range(10):
        x, y = r.uniform(0, w), r.uniform(h * 0.64, h * 0.98)
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.05)}" height="{f(h * 0.03)}" rx="3" fill="#A89E92" stroke="#0D0D0F" stroke-width="1.4" transform="rotate({r.randint(-20, 20)} {f(x)} {f(y)})"></rect>')
    if foundation:
        for row in range(3):
            for k in range(9):
                x = w * (0.26 + k * 0.055) + (row % 2) * w * 0.027; y = h * (0.8 - row * 0.045)
                o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.052)}" height="{f(h * 0.042)}" fill="#D8CDB8" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    o.append(horned_altar(w * (0.14 if foundation else 0.5), h * 0.84, min(0.8, h / 380), fire=True, seed=seed))
    s = fit(b, max(h * 0.44, b - 230))
    if foundation:
        for i in range(3): o.append(J.trumpeter(p, w * (0.78 + i * 0.07), b, s * 0.9, flip=True))
    if weep:
        for i in range(3): o.append(man(p, w * (0.06 + i * 0.08), b, s * 0.9, "#6A6460", kind="Robe"))
    if not foundation:
        o.append(priest(p, w * 0.32, b, s) + priest(p, w * 0.68, b, s, flip=True))
    return "".join(o)

def letter_scroll(w, h, seed, seal="#7A2A6A", text_lines=8):
    """A letter beyond the River: an unrolled scroll in the Syrian character, sealed with the king's seal."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A2A"></rect>', V.rays(w * 0.5, h * 0.5, 24, 12, max(w, h), color="#E8C88A", op=0.08),
         f'<rect x="{f(w * 0.2)}" y="{f(h * 0.16)}" width="{f(w * 0.6)}" height="{f(h * 0.68)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    r = random.Random(seed)
    for k in range(text_lines):
        y = h * (0.24 + k * 0.56 / text_lines)
        x = w * 0.26
        while x < w * 0.74:
            L = w * r.uniform(0.02, 0.06)
            o.append(f'<path d="M{f(x)} {f(y)} l {f(min(L, w * 0.74 - x))} 0" stroke="#6A4A2A" stroke-width="2.4"></path>'); x += L + w * 0.012
    o.append(f'<ellipse cx="{f(w * 0.2)}" cy="{f(h * 0.5)}" rx="{f(w * 0.03)}" ry="{f(h * 0.35)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<ellipse cx="{f(w * 0.8)}" cy="{f(h * 0.5)}" rx="{f(w * 0.03)}" ry="{f(h * 0.35)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.88)}" r="{f(min(w, h) * 0.05)}" fill="{seal}" stroke="#0D0D0F" stroke-width="2"></circle>')
    return "".join(o)

def work_ceased(p, w, h, seed):
    """The work made to cease: the half-built house with its scaffold abandoned, tools left on the stones, horsemen of the
    adversaries at the edge."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#6A6A8A", "#C8B8A0"), ground(w, h, h * 0.7, "#A89A80", dy=0)]
    for row in range(4):
        for k in range(8 - row):
            x = w * (0.3 + k * 0.05) + row * w * 0.025; y = h * (0.82 - row * 0.05)
            o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.048)}" height="{f(h * 0.048)}" fill="#C8BDA8" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.86)} L {f(w * 0.3)} {f(h * 0.44)} M{f(w * 0.72)} {f(h * 0.86)} L {f(w * 0.72)} {f(h * 0.44)} M{f(w * 0.28)} {f(h * 0.5)} L {f(w * 0.74)} {f(h * 0.5)} M{f(w * 0.28)} {f(h * 0.64)} L {f(w * 0.74)} {f(h * 0.64)}" stroke="#6A4A2A" stroke-width="4"></path>')
    for i in range(3):
        o.append(E3.horse(w * (0.84 + i * 0.05), b, min(0.36, h / 900), color="#3A2214", flip=True))
    return "".join(o)

# ---- Ezra 7–8 -----------------------------------------------------------------------------------------------------------
def ahava(p, w, h, seed, fast=False):
    """By the river that runneth to Ahava: tents pitched along the water three days, the people gathered (fast=True: bowed
    in sackcloth, dusk)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A4A7A" if fast else "#8FD0E2", "#C89A8A" if fast else "#F3E8C8"), hills(w, h, h * 0.44, seed, "#8A7A6A", amp=10, step=90),
         ground(w, h, h * 0.5, "#B8A07A", dy=0),
         f'<path d="M-10 {f(h * 0.6)} C {f(w * 0.3)} {f(h * 0.56)} {f(w * 0.6)} {f(h * 0.64)} {f(w + 10)} {f(h * 0.58)} L {f(w + 10)} {f(h * 0.66)} C {f(w * 0.6)} {f(h * 0.72)} {f(w * 0.3)} {f(h * 0.64)} -10 {f(h * 0.68)} Z" fill="#2C7DA8" stroke="#0D0D0F" stroke-width="2"></path>',
         N.camp(10, -10, w + 10, h * 0.42, h * 0.54, seed, color=("#5A3A22", "#6B4A2A", "#3A2214"))]
    s = fit(b, max(h * 0.7, b - 160))
    r = random.Random(seed)
    for i in range(9):
        x = w * (0.06 + i * 0.11)
        if fast: o.append(E.kneel(x, b, s * 0.8, color="#5A5040", skin="#9A6A4A", flip=i % 2 == 1))
        else: o.append(man(p, x, b - r.randint(0, 6), s, r.choice(["#6A3A2A", "#3A4A6A", "#5A4A3A", "#E8D8B0", "#4A5A3A"])))
    return "".join(o)

def weighing(p, w, h, seed):
    """The silver, the gold and the vessels weighed into the hands of the priests: a great balance, ingots and bowls on
    the scales, the twelve chiefs of the priests in white beside it."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), ground(w, h, h * 0.84, "#6A4A2A", dy=0)]
    cx, top = w * 0.5, h * 0.3
    o.append(f'<path d="M{f(cx)} {f(b)} L {f(cx)} {f(top)}" stroke="#B87333" stroke-width="8"></path>'
             f'<path d="M{f(cx - w * 0.2)} {f(top + 6)} L {f(cx + w * 0.2)} {f(top - 6)}" stroke="#B87333" stroke-width="6"></path>')
    for side, dy, c in ((-1, 6, "#C8C8D0"), (1, -6, "#E8B830")):
        px = cx + side * w * 0.2
        o.append(f'<path d="M{f(px)} {f(top + dy)} L {f(px - w * 0.05)} {f(top + dy + h * 0.2)} M{f(px)} {f(top + dy)} L {f(px + w * 0.05)} {f(top + dy + h * 0.2)}" stroke="#6A4A2A" stroke-width="2"></path>'
                 f'<path d="M{f(px - w * 0.07)} {f(top + dy + h * 0.2)} Q {f(px)} {f(top + dy + h * 0.28)} {f(px + w * 0.07)} {f(top + dy + h * 0.2)} Z" fill="#B87333" stroke="#0D0D0F" stroke-width="2"></path>')
        for k in range(3):
            o.append(f'<rect x="{f(px - w * 0.04 + k * w * 0.027)}" y="{f(top + dy + h * 0.16)}" width="{f(w * 0.024)}" height="{f(h * 0.04)}" rx="2" fill="{c}" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    s = fit(b, max(h * 0.4, b - 240))
    for i in range(3):
        o.append(priest(p, w * (0.06 + i * 0.08), b, s) + priest(p, w * (0.94 - i * 0.08), b, s, flip=True))
    return "".join(o)

# ---- Ezra 9–10 ----------------------------------------------------------------------------------------------------------
def rain_square(p, w, h, seed):
    """The people sitting in the broad place before the house of God in the ninth month, trembling because of the great rain:
    a dark sky, slanting rain, the crowd hunched in their cloaks."""
    r = random.Random(seed)
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#2A2A3A", "#6A6A7A"), temple_front(w * 0.5, h * 0.62, w * 0.5, seed), ground(w, h, h * 0.62, "#6A6458", dy=0)]
    s = fit(b, max(h * 0.66, b - 150))
    for i in range(12):
        x = w * (0.04 + i * 0.083) + r.uniform(-8, 8)
        o.append(E.kneel(x, b - r.randint(0, 10), s * 0.7, color=r.choice(["#3A3438", "#4A4040", "#3A3A4A"]), skin="#8A6A5A", flip=i % 2 == 1))
    for _ in range(90):
        x, y = r.uniform(-20, w), r.uniform(0, h)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(-h * 0.02)} {f(h * 0.06)}" stroke="#C8D8E8" stroke-width="1.6" opacity="0.6"></path>')
    return "".join(o)

def prayer_evening(p, w, h, seed):
    """At the evening oblation: Ezra on his knees, his garment rent, his hands spread out before the house, the people who
    trembled sitting about him in the dusk."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#3A2A4A", "#E8907A"), temple_front(w * 0.5, h * 0.66, w * 0.46, seed), ground(w, h, h * 0.66, "#8A7A6A", dy=0)]
    s = fit(b, max(h * 0.4, b - 240))
    o.append(S3.dancer(w * 0.5, b, s * 0.9, p + "ez", [(-22, -158), (-40, -200), (-46, -238)], [(22, -158), (40, -200), (46, -238)], cloth="#E8E2D6", body="#5A2A16", crown=False))
    for i in range(6):
        o.append(E.kneel(w * (0.06 + i * 0.07) if i < 3 else w * (0.74 + (i - 3) * 0.08), b, s * 0.62, color="#5A5040", skin="#9A6A4A", flip=i >= 3))
    return "".join(o)
