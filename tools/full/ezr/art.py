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
