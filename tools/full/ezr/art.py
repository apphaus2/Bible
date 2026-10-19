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
