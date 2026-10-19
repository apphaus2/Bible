"""Drawings for the 2 Chronicles volume (chapter by chapter, added below), on top of 1 Chronicles' (chr1.art, which carries
kg2.art, kg1.art, and 2 Samuel's drawings as K2). Solomon's house is 1 Kings' blueprints; the kings of Judah reuse 1 and 2
Kings' figures."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from chr1.art import *
from chr1.art import f, K2, K3
import kg1.art as K1
from kg1.art import SOL_C, AHAB_C, JERO_C, REHO_C, MANTLE
from sa2.art import king_fig

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

# ---- 2 Chronicles 13–16 -------------------------------------------------------------------------------------------------
from jos.art import crowd_at, warrior, WAR
from genesis.art2 import hills

def zemaraim(p, w, h, seed):
    """Abijah standing up upon mount Zemaraim, his arm raised, speaking to Jeroboam's host spread below; Judah's host behind him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.6, seed, "#8A8A5A", amp=10, step=90),
         f'<path d="M-10 {f(h * 0.66)} L {f(w * 0.12)} {f(h * 0.3)} L {f(w * 0.32)} {f(h * 0.34)} L {f(w * 0.46)} {f(h * 0.72)} L {f(w * 0.46)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.74, "#B89A6A", dy=0)]
    s = fit(h * 0.32, h * 0.12)
    o.append(king_fig(p, w * 0.22, h * 0.32, s, up=[(-22, -158), (-40, -190), (-52, -222)], cloth=REHO_C))
    o.append(crowd_at(p, w, h, seed, w * 0.5, w * 0.98, h * 0.76, b, 22, s * 0.6, s * 1.1, flip=True))
    for i in range(6): o.append(warrior(p, w * (0.02 + i * 0.05), b - (i % 2) * 6, s * 0.9, WAR[i % 4]))
    return "".join(o)

def battle_map(w, h, stage=0):
    """Abijah's battle as a technical map: Judah in the midst, Israel before, Jeroboam's ambushment come round behind; stage 1:
    the shout, and Israel fleeing."""
    o = [grid_bg(w, h)]
    jx, jy = w * 0.5, h * 0.5
    o.append(f'<rect x="{f(jx - w * 0.1)}" y="{f(jy - h * 0.12)}" width="{f(w * 0.2)}" height="{f(h * 0.24)}" fill="#FFD23F" fill-opacity="0.25" stroke="#FFD23F" stroke-width="2"></rect>'
             + label(jx, jy + 4, "JUDAH · 400,000", "#FFD23F", 9))
    for x, nm in ((0.82, "ISRAEL · 800,000"), (0.16, "THE AMBUSHMENT")):
        o.append(f'<rect x="{f(w * x - w * 0.1)}" y="{f(h * 0.3)}" width="{f(w * 0.2)}" height="{f(h * 0.4)}" fill="#D7261E" fill-opacity="{0.2 if stage == 0 else 0.07}" stroke="#D7261E" stroke-width="2"'
                 + (' stroke-dasharray="6 6"' if stage else '') + '></rect>' + label(w * x, h * 0.5 + 4, nm, "#FF8A6A", 9))
    if stage == 0:
        o.append(route([(w * 0.7, h * 0.2), (w * 0.5, h * 0.12), (w * 0.28, h * 0.2)], color="#D7261E") + label(w * 0.5, h * 0.08, "ROUND ABOUT BEHIND THEM", "#FF8A6A", 8))
    else:
        o.append(route([(w * 0.84, h * 0.5), (w * 0.98, h * 0.5)], color="#FF8A6A") + route([(w * 0.14, h * 0.5), (w * 0.02, h * 0.5)], color="#FF8A6A")
                 + label(jx, h * 0.84, "THE MEN OF JUDAH GAVE A SHOUT", "#FFD23F", 10))
    return "".join(o)

ZERAH_M = [("MARESHAH", 0.44, 0.3), ("ZEPHATHAH", 0.3, 0.42), ("GERAR", 0.16, 0.86), ("JERUSALEM", 0.8, 0.14)]
def zerah_map(w, h, pursuit=False):
    """Zerah the Ethiopian with a thousand thousand in the valley of Zephathah at Mareshah, Asa's host before him; pursuit=True:
    the Ethiopians fleeing unto Gerar."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.08)} -10 C {f(w * 0.1)} {f(h * 0.4)} {f(w * 0.06)} {f(h * 0.7)} {f(w * 0.02)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    pos = {n: (w * x, h * y) for n, x, y in ZERAH_M}
    o.append(f'<ellipse cx="{f(w * 0.28)}" cy="{f(h * 0.62)}" rx="{f(w * 0.16)}" ry="{f(h * 0.12)}" fill="#D7261E" fill-opacity="{0.08 if pursuit else 0.25}" stroke="#D7261E" stroke-width="2"></ellipse>'
             + label(w * 0.28, h * 0.62 + 4, "ZERAH · A THOUSAND THOUSAND", "#FF8A6A", 8))
    o.append(f'<rect x="{f(w * 0.52)}" y="{f(h * 0.52)}" width="{f(w * 0.14)}" height="{f(h * 0.16)}" fill="#FFD23F" fill-opacity="0.25" stroke="#FFD23F" stroke-width="2"></rect>'
             + label(w * 0.59, h * 0.61, "ASA", "#FFD23F", 9))
    if pursuit: o.append(route([(w * 0.5, h * 0.66), pos["GERAR"]], color="#FFD23F"))
    else: o.append(route([pos["JERUSALEM"], (w * 0.62, h * 0.5)], color="#FFD23F"))
    for nm, x, y in ZERAH_M: o.append(node(w * x, h * y, nm, "#8FD0E2", r=4, dy=-10, size=8))
    return "".join(o)

def oath(p, w, h, seed):
    """Judah swearing unto Jehovah with a loud voice, with trumpets and cornets: the court with the altar smoking, priests
    with trumpets, the people's arms raised."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#FFB04A", "#F3E0B0"), ground(w, h, h * 0.66, "#C8B88A", dy=0), temple_front(w * 0.5, h * 0.66, w * 0.5, seed),
         horned_altar(w * 0.5, h * 0.86, min(0.7, h / 440), fire=True, seed=seed)]
    s = fit(b, max(h * 0.44, b - 220))
    for i in range(4):
        x = w * (0.06 + i * 0.09)
        o.append(J.trumpeter(p, x, b, s * 0.9))
        o.append(man(p, w * (0.66 + i * 0.09), b, s * 0.9, ["#3A4A6A", "#6A3A2A", "#4A5A3A", "#5A4A6A"][i], flip=True, up=[(22, -158), (40, -190), (50, -222)]))
    return "".join(o)

def spice_burning(w, h, seed):
    """A very great burning for him: a sepulchre hewn in the rock, the door shut, and the smoke of spices rising in a great column."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#3A2A4A", "#C88A6A"), f'<path d="M-10 {f(h * 0.4)} C {f(w * 0.3)} {f(h * 0.3)} {f(w * 0.6)} {f(h * 0.36)} {f(w + 10)} {f(h * 0.3)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A6A5A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.2)} {f(h * 0.9)} L {f(w * 0.2)} {f(h * 0.62)} Q {f(w * 0.28)} {f(h * 0.52)} {f(w * 0.36)} {f(h * 0.62)} L {f(w * 0.36)} {f(h * 0.9)} Z" fill="#2A1E1E" stroke="#0D0D0F" stroke-width="2.4"></path>'
         f'<circle cx="{f(w * 0.28)}" cy="{f(h * 0.8)}" r="{f(h * 0.1)}" fill="#A89A8A" stroke="#0D0D0F" stroke-width="2.4"></circle>',
         ground(w, h, h * 0.9, "#6A5A4A", dy=0)]
    for i in range(12):
        x = w * 0.66 + r.uniform(-30, 30); y = h * (0.86 - i * 0.07)
        o.append(f'<circle cx="{f(x + i * 6)}" cy="{f(y)}" r="{f(w * (0.05 + i * 0.006))}" fill="#E8E2D6" opacity="{0.6 - i * 0.03:.2f}"></circle>')
    o.append(E.blaze(w * 0.66, h * 0.9, w * 0.16, h * 0.18, seed, n=6))
    return "".join(o)
