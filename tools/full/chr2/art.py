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

# ---- 2 Chronicles 10–12 -------------------------------------------------------------------------------------------------
FORTS = [("BETH-LEHEM", 0.52, 0.36), ("ETAM", 0.56, 0.44), ("TEKOA", 0.62, 0.5), ("BETH-ZUR", 0.5, 0.56), ("SOCO", 0.36, 0.5), ("ADULLAM", 0.4, 0.58),
         ("GATH", 0.24, 0.52), ("MARESHAH", 0.3, 0.64), ("ZIPH", 0.56, 0.74), ("ADORAIM", 0.44, 0.7), ("LACHISH", 0.26, 0.72), ("AZEKAH", 0.32, 0.42),
         ("ZORAH", 0.36, 0.3), ("AIJALON", 0.4, 0.18), ("HEBRON", 0.5, 0.66)]
def judah_forts(w, h):
    """Rehoboam's cities for defence in Judah and Benjamin as a technical map, Jerusalem marked."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.1)} -10 C {f(w * 0.12)} {f(h * 0.4)} {f(w * 0.08)} {f(h * 0.7)} {f(w * 0.06)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.84)} -10 C {f(w * 0.82)} {f(h * 0.3)} {f(w * 0.86)} {f(h * 0.5)} {f(w * 0.8)} {f(h * 0.62)}" stroke="#2C9DB8" stroke-width="4" fill="none"></path>'
             f'<ellipse cx="{f(w * 0.8)}" cy="{f(h * 0.78)}" rx="{f(w * 0.03)}" ry="{f(h * 0.16)}" fill="#2C9DB8"></ellipse>')
    for nm, x, y in FORTS:
        o.append(f'<rect x="{f(w * x - 6)}" y="{f(h * y - 6)}" width="12" height="12" fill="#FFD23F" fill-opacity="0.3" stroke="#FFD23F" stroke-width="1.6"></rect>'
                 + label(w * x, h * y - 10, nm, "#FFD23F", 8))
    o.append(node(w * 0.56, h * 0.26, "JERUSALEM", RED_C, r=6, dy=-12, size=10))
    return "".join(o)
