"""Drawings for the 2 Chronicles volume (chapter by chapter, added below), on top of 1 Chronicles' (chr1.art, which carries
kg2.art, kg1.art, and 2 Samuel's drawings as K2). Solomon's house is 1 Kings' blueprints; the kings of Judah reuse 1 and 2
Kings' figures."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from chr1.art import *
from chr1.art import f, K2, K3
import kg1.art as K1

# ---- 2 Chronicles 8–9 ---------------------------------------------------------------------------------------------------
from genesis.art2 import fit, ground
from genesis.art3 import man, woman
import joshua1 as J

def queen_house(p, w, h, seed):
    """Pharaoh's daughter brought up out of the city of David to the house built for her: the city of David on its hill
    behind, her own white house with a gold door, she in white linen with her maidens, Solomon beside them."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), J.city_hill(w * 0.24, h * 0.6, w * 0.4, h * 0.26, seed), ground(w, h, h * 0.62, "#C8B88A", dy=0),
         f'<rect x="{f(w * 0.56)}" y="{f(h * 0.3)}" width="{f(w * 0.38)}" height="{f(h * 0.4)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2.4"></rect>'
         f'<rect x="{f(w * 0.53)}" y="{f(h * 0.26)}" width="{f(w * 0.44)}" height="{f(h * 0.05)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></rect>'
         f'<rect x="{f(w * 0.71)}" y="{f(h * 0.5)}" width="{f(w * 0.08)}" height="{f(h * 0.2)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></rect>']
    s = fit(b, max(h * 0.4, b - 230))
    o.append(sol_fig(p, w * 0.3, b, s) + woman(p, w * 0.46, b, s * 0.92, "#F3EFE6") + woman(p, w * 0.56, b, s * 0.86, "#E8D8B0") + woman(p, w * 0.64, b, s * 0.86, "#E8D8B0"))
    return "".join(o)
