"""Drawings for the proverbs of Solomon, Proverbs 10–29 (chapters 4–10 of the volume): the scenes on chapter title pages and
the drawn cells among the sayings, on top of pro.art3 (everything there is re-exported here)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from pro.art3 import *
from pro.art3 import f, K2, K1, EM, INK, SON_C, WIS_C, STRANGE_C, glow, son_fig, wisdom_fig, veiled, emb_art, deer, stone_well, street_row

def father_son(p, w, h, seed, gate=False):
    """A wise son maketh a glad father: Solomon in the court of his house with his son, an open scroll between them."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFE3B8"), ground(w, h, b, "#E8C88A", dy=0)]
    if gate: o.append(S4.gatehouse(w * 0.82, b, min(w * 0.36, h * 0.9), h * 0.66))
    else:
        o.append(f'<rect x="-10" y="{f(h * 0.2)}" width="{f(w + 20)}" height="{f(b - h * 0.2)}" fill="#D8C8A0" stroke="{INK}" stroke-width="2"></rect>'
                 + "".join(f'<rect x="{f(x)}" y="{f(h * 0.2)}" width="{f(w * 0.05)}" height="{f(b - h * 0.2)}" fill="#C8B890" stroke="{INK}" stroke-width="1.6"></rect>' for x in [w * (0.08 + i * 0.22) for i in range(5)]))
    s = min(fit(b, h * 0.3), 1.3)
    o.append(glow(w * 0.48, b - 110 * s, 150 * s, "#FFE680", 0.35))
    o.append(K1.sol_fig(p, w * 0.36, b, s, flip=True, up=[(-22, -158), (-44, -136), (-62, -128)]))
    o.append(son_fig(p, w * 0.6, b, s * 0.86, up=[(-22, -158), (-44, -136), (-62, -128)]))
    o.append(f'<rect x="{f(w * 0.48 - 40 * s)}" y="{f(b - 132 * s)}" width="{f(80 * s)}" height="{f(30 * s)}" fill="#F3E8C8" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<rect x="{f(w * 0.48 - 46 * s)}" y="{f(b - 136 * s)}" width="{f(8 * s)}" height="{f(38 * s)}" rx="3" fill="#8A5A30" stroke="{INK}" stroke-width="1.4"></rect>'
             f'<rect x="{f(w * 0.48 + 38 * s)}" y="{f(b - 136 * s)}" width="{f(8 * s)}" height="{f(38 * s)}" rx="3" fill="#8A5A30" stroke="{INK}" stroke-width="1.4"></rect>')
    return "".join(o)
