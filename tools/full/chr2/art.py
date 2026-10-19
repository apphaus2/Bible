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

# ---- 2 Chronicles 17–19 -------------------------------------------------------------------------------------------------
def teachers(p, w, h, seed):
    """The princes, Levites and priests going about the cities of Judah with the book of the law, teaching at a city gate,
    the people sitting before them."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), J.city_hill(w * 0.78, h * 0.62, w * 0.3, h * 0.26, seed), ground(w, h, h * 0.64, "#C8A06A", dy=0)]
    s = fit(b, max(h * 0.4, b - 230))
    o.append(priest(p, w * 0.22, b, s, up=[(22, -158), (34, -176), (40, -150)]))
    o.append(f'<rect x="{f(w * 0.22 + 30 * s)}" y="{f(b - 172 * s)}" width="{f(30 * s)}" height="{f(24 * s)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(man(p, w * 0.1, b, s * 0.96, "#3A4A6A"))
    for i in range(6):
        o.append(E.kneel(w * (0.4 + i * 0.09), b, s * 0.62, color=["#6A3A2A", "#3A4A6A", "#5A4A3A", "#4A5A3A", "#6A5A3A", "#5A3A5A"][i], skin="#9A6A4A", flip=True))
    return "".join(o)

def judges_gate(p, w, h, seed):
    """Judges set in the land city by city: elders seated at a gate, a man standing before them with his cause."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#C8B8A0", "#F3E0B0"), S4b.gatehouse(w * 0.5, h * 0.8, w * 0.7, h * 0.66), ground(w, h, h * 0.8, "#B8A07A", dy=0)]
    s = fit(b, max(h * 0.44, b - 220))
    for i in range(3):
        o.append(E.kneel(w * (0.3 + i * 0.12), b, s * 0.7, color=["#5A4A3A", "#3A4A6A", "#6A5A3A"][i], skin="#9A6A4A"))
    o.append(man(p, w * 0.8, b, s, "#8A5A30", flip=True))
    return "".join(o)

# ---- 2 Chronicles 20–21 -------------------------------------------------------------------------------------------------
TEKOA_M = [("JERUSALEM", 0.42, 0.14), ("TEKOA", 0.44, 0.42), ("EN-GEDI", 0.74, 0.56), ("ASCENT OF ZIZ", 0.66, 0.42), ("WILDERNESS OF JERUEL", 0.6, 0.3), ("BERACAH", 0.32, 0.5)]
def tekoa_map(w, h, stage=0):
    """The great multitude come up from beyond the sea to Hazazon-tamar (En-gedi), the ascent of Ziz, the wilderness of
    Jeruel; Judah's way out by Tekoa (stage 1: the singers going out before the army; stage 2: the valley of Beracah)."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.86)} -10 C {f(w * 0.84)} {f(h * 0.3)} {f(w * 0.9)} {f(h * 0.6)} {f(w * 0.86)} {f(h + 10)} L {f(w + 10)} {f(h + 10)} L {f(w + 10)} -10 Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>'
             + label(w * 0.93, h * 0.7, "THE SEA", "#8FD0E2", 8))
    pos = {n: (w * x, h * y) for n, x, y in TEKOA_M}
    o.append(f'<ellipse cx="{f(w * 0.74)}" cy="{f(h * 0.62)}" rx="{f(w * 0.08)}" ry="{f(h * 0.12)}" fill="#D7261E" fill-opacity="0.22" stroke="#D7261E" stroke-width="2"></ellipse>'
             + label(w * 0.74, h * 0.82, "AMMON · MOAB · MOUNT SEIR", "#FF8A6A", 8))
    if stage >= 1: o.append(route([pos["JERUSALEM"], pos["TEKOA"]], color="#FFD23F") + label(w * 0.3, h * 0.3, "THE SINGERS BEFORE THE ARMY", "#FFD23F", 8))
    if stage >= 2: o.append(route([pos["TEKOA"], pos["BERACAH"]], color="#9CCB5E"))
    for nm, x, y in TEKOA_M:
        o.append(node(w * x, h * y, nm, "#9CCB5E" if nm == "BERACAH" and stage >= 2 else ("#FFD23F" if nm in ("JERUSALEM", "TEKOA") else CYAN), r=4, dy=-10, size=8))
    return "".join(o)

def singers_march(p, w, h, seed):
    """The singers in holy array going out before the army into the wilderness of Tekoa at dawn, harps and cymbals raised,
    the men of war behind them."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A4A7A", "#FFC890"), sun(w * 0.82, h * 0.5, 22, color="#FFE680", op=0.4), hills(w, h, h * 0.56, seed, "#8A6A5A", amp=12, step=80),
         ground(w, h, h * 0.66, "#C8A06A", dy=0)]
    s = fit(b, max(h * 0.44, b - 220))
    for i in range(4):
        o.append(S3.musician(p, w * (0.5 + i * 0.12), b, s, kind=("harp", "cymbals")[i % 2], cloth="#F3EFE6", woman=False, seed=seed + i))
    for i in range(6): o.append(warrior(p, w * (0.04 + i * 0.065), b - (i % 2) * 5, s * 0.86, WAR[i % 4]))
    return "".join(o)

def watchtower_view(w, h, seed):
    """From the watch-tower of the wilderness: the valley below silent, spears and shields strewn on the ground, no one standing."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8A7A8A", "#E8C8A0"), hills(w, h, h * 0.4, seed, "#8A6A5A", amp=16, step=70), ground(w, h, h * 0.5, "#B8946A", dy=0)]
    for _ in range(26):
        x, y = r.uniform(0, w), r.uniform(h * 0.56, h * 0.96); a = r.uniform(-30, 30); L = w * r.uniform(0.04, 0.08)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(L * math.cos(math.radians(a)))} {f(L * math.sin(math.radians(a)) * 0.3)}" stroke="#3A2A1E" stroke-width="2.4"></path>')
        if r.random() < 0.4: o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * 0.014)}" ry="{f(w * 0.008)}" fill="#B87333" stroke="#0D0D0F" stroke-width="1.2"></ellipse>')
    o.append(f'<path d="M{f(w * 0.06)} {f(h + 10)} L {f(w * 0.06)} {f(h * 0.62)} L {f(w * 0.2)} {f(h * 0.62)} L {f(w * 0.2)} {f(h + 10)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    return "".join(o)

def writing(w, h, seed):
    """A writing come from Elijah the prophet: a sealed scroll unrolled on a dark table."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A2A"></rect>', V.rays(w * 0.5, h * 0.5, 24, 12, max(w, h), color="#E8C88A", op=0.1),
         f'<rect x="{f(w * 0.24)}" y="{f(h * 0.24)}" width="{f(w * 0.52)}" height="{f(h * 0.52)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    for k in range(7):
        o.append(f'<path d="M{f(w * 0.3)} {f(h * (0.32 + k * 0.055))} L {f(w * (0.7 - (k == 6) * 0.2))} {f(h * (0.32 + k * 0.055))}" stroke="#8A6A4A" stroke-width="2"></path>')
    o.append(f'<ellipse cx="{f(w * 0.24)}" cy="{f(h * 0.5)}" rx="{f(w * 0.03)}" ry="{f(h * 0.27)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<ellipse cx="{f(w * 0.76)}" cy="{f(h * 0.5)}" rx="{f(w * 0.03)}" ry="{f(h * 0.27)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.8)}" r="{f(min(w, h) * 0.04)}" fill="#B5121B" stroke="#0D0D0F" stroke-width="2"></circle>')
    return "".join(o)

# ---- 2 Chronicles 25–27 -------------------------------------------------------------------------------------------------
def rock_top(w, h, seed):
    """The top of the rock in Seir: a sheer red crag against the sky, nothing on it (25:12 told in words only)."""
    o = [K2.sky(w, h, "#5A3A4A", "#E8A06A"),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.34)} {f(h * 0.3)} L {f(w * 0.46)} {f(h * 0.24)} L {f(w * 0.62)} {f(h * 0.26)} L {f(w * 0.66)} {f(h + 10)} Z" fill="#8A3A1E" stroke="#0D0D0F" stroke-width="2.6"></path>'
         f'<path d="M{f(w * 0.36)} {f(h * 0.4)} L {f(w * 0.38)} {f(h * 0.9)} M{f(w * 0.5)} {f(h * 0.3)} L {f(w * 0.52)} {f(h * 0.8)} M{f(w * 0.6)} {f(h * 0.34)} L {f(w * 0.62)} {f(h * 0.9)}" stroke="#5A2412" stroke-width="2"></path>',
         hills(w, h, h * 0.82, seed, "#5A2A1E", amp=8, step=60)]
    return "".join(o)

def idols_edom(p, w, h, seed):
    """The gods of the children of Seir set up, and incense burning before them (no worshipper drawn)."""
    o = [K2.sky(w, h, "#2A1A2A", "#6A3A3A"), ground(w, h, h * 0.76, "#3A2A2A", dy=0)]
    for i in range(3):
        x = w * (0.28 + i * 0.22); s = min(1.0, h / 360)
        o.append(f'<g transform="translate({f(x)} {f(h * 0.76)}) scale({f(s)})"><rect x="-20" y="-24" width="40" height="24" fill="#5A4A4A" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<path d="M-14 -24 L -14 -110 Q 0 -130 14 -110 L 14 -24 Z" fill="#8A6A5A" stroke="#0D0D0F" stroke-width="2.2"></path>'
                 f'<circle cx="0" cy="-118" r="14" fill="#8A6A5A" stroke="#0D0D0F" stroke-width="2.2"></circle>'
                 f'<circle cx="-5" cy="-120" r="2.4" fill="#0D0D0F"></circle><circle cx="5" cy="-120" r="2.4" fill="#0D0D0F"></circle></g>')
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.7)} C {f(w * 0.46)} {f(h * 0.5)} {f(w * 0.56)} {f(h * 0.36)} {f(w * 0.5)} {f(h * 0.12)}" stroke="#C8C2B6" stroke-width="{f(w * 0.02)}" fill="none" opacity="0.6"></path>'
             + horned_altar(w * 0.5, h * 0.82, min(0.4, h / 800), fire=True, seed=seed))
    return "".join(o)

def towers_engines(w, h, seed):
    """Uzziah's towers at the corner gate and the valley gate, and the engines on the battlements to shoot arrows and great
    stones, as a blueprint elevation."""
    o = [bp(w, h)]
    base = h * 0.84
    for i, x in enumerate((0.22, 0.78)):
        cx = w * x; tw, th = w * 0.18, h * 0.5
        o.append(f'<rect x="{f(cx - tw / 2)}" y="{f(base - th)}" width="{f(tw)}" height="{f(th)}" fill="none" stroke="#8FD0E2" stroke-width="2.2"></rect>'
                 + "".join(f'<rect x="{f(cx - tw / 2 + k * tw / 5)}" y="{f(base - th - 14)}" width="{f(tw / 10)}" height="14" fill="none" stroke="#8FD0E2" stroke-width="1.8"></rect>' for k in range(5))
                 + label(cx, base + 16, ["THE CORNER GATE", "THE VALLEY GATE"][i], "#8FD0E2", 9))
        ex, ey = cx, base - th - 22
        o.append(f'<path d="M{f(ex - 30)} {f(ey)} L {f(ex + 30)} {f(ey)} M{f(ex - 20)} {f(ey)} L {f(ex + 10)} {f(ey - 40)}" stroke="#FFD23F" stroke-width="3"></path>'
                 f'<circle cx="{f(ex + 10)}" cy="{f(ey - 44)}" r="7" fill="none" stroke="#FFD23F" stroke-width="2"></circle>')
    o.append(f'<path d="M{f(w * 0.31)} {f(base - h * 0.36)} L {f(w * 0.69)} {f(base - h * 0.36)} L {f(w * 0.69)} {f(base)} L {f(w * 0.31)} {f(base)} Z" fill="none" stroke="#4A7A9A" stroke-width="1.8" stroke-dasharray="6 5"></path>'
             + label(w * 0.5, base - h * 0.4, "THE WALL", "#4A7A9A", 9) + label(w * 0.5, base - h * 0.2, "ENGINES · ARROWS AND GREAT STONES", "#FFD23F", 10))
    return "".join(o)

def censer_altar(p, w, h, seed, priests=True):
    """Within the temple: the golden altar of incense smoking, a censer in the king's hand, priests coming in after him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#C8962A"></rect>']
    for k in range(int(w // 60) + 2):
        o.append(f'<path d="M{f(k * 60)} -10 L {f(k * 60)} {f(h * 0.88)}" stroke="#A8761A" stroke-width="3"></path>'
                 f'<circle cx="{f(k * 60 + 30)}" cy="{f(h * 0.3)}" r="{f(min(w, h) * 0.03)}" fill="none" stroke="#7A5210" stroke-width="2"></circle>')
    o.append(ground(w, h, h * 0.88, "#8A6A3A", dy=0))
    ax = w * 0.62
    o.append(f'<rect x="{f(ax - w * 0.06)}" y="{f(b - h * 0.26)}" width="{f(w * 0.12)}" height="{f(h * 0.26)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<path d="M{f(ax)} {f(b - h * 0.28)} C {f(ax - 20)} {f(h * 0.4)} {f(ax + 20)} {f(h * 0.3)} {f(ax)} {f(h * 0.06)}" stroke="#E8E2D6" stroke-width="{f(w * 0.02)}" fill="none" opacity="0.6"></path>')
    s = fit(b, max(h * 0.4, b - 240))
    o.append(king_fig(p, w * 0.44, b, s, up=[(22, -158), (40, -170), (54, -160)], cloth=REHO_C))
    if priests:
        for i in range(3): o.append(priest(p, w * (0.08 + i * 0.1), b, s * 0.94))
    return "".join(o)

# ---- 2 Chronicles 28–29 -------------------------------------------------------------------------------------------------
def captives_clothed(p, w, h, seed):
    """The captives of Judah clothed and shod, the feeble carried upon asses, going down to Jericho, the city of palm-trees."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.5, seed, "#8A8A5A", amp=10, step=80), ground(w, h, h * 0.6, "#C8A06A", dy=0)]
    for i in range(4):
        o.append(J1.palm(w * (0.8 + i * 0.05), h * 0.62, min(0.5, h / 700)))
    s = fit(b, max(h * 0.44, b - 220))
    cl = ["#E8D8B0", "#C8D8E8", "#E8C8B0", "#D8E8C8"]
    for i in range(5):
        x = w * (0.08 + i * 0.13)
        if i % 2: o.append(N.ass(x, b, s * 0.6, color="#7A6A5A"))
        else: o.append(man(p, x, b, s * 0.9, cl[i % 4]))
    return "".join(o)

def shut_doors(w, h, seed, open_=False):
    """The doors of the porch of the house of Jehovah shut and the lamps put out; open_=True: the doors opened and repaired,
    light within."""
    o = [K2.sky(w, h, "#3A2A3A" if not open_ else "#FFE680", "#8A6A6A" if not open_ else "#F3E0B0"), ground(w, h, h * 0.86, "#6A5A4A" if not open_ else "#C8B88A", dy=0)]
    x0, x1, top = w * 0.2, w * 0.8, h * 0.12
    o.append(f'<rect x="{f(x0)}" y="{f(top)}" width="{f(x1 - x0)}" height="{f(h * 0.74)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2.6"></rect>')
    dx0, dx1, dt = w * 0.34, w * 0.66, h * 0.32
    if open_:
        o.append(f'<rect x="{f(dx0)}" y="{f(dt)}" width="{f(dx1 - dx0)}" height="{f(h * 0.54)}" fill="#FFD23F" stroke="#0D0D0F" stroke-width="2.4"></rect>'
                 + V.rays(w * 0.5, h * 0.6, 20, 12, w * 0.5, color="#FFF4C2", op=0.3)
                 + f'<path d="M{f(dx0)} {f(dt)} L {f(dx0 - w * 0.08)} {f(dt + h * 0.04)} L {f(dx0 - w * 0.08)} {f(h * 0.9)} L {f(dx0)} {f(h * 0.86)} Z" fill="#B8862A" stroke="#0D0D0F" stroke-width="2"></path>'
                 + f'<path d="M{f(dx1)} {f(dt)} L {f(dx1 + w * 0.08)} {f(dt + h * 0.04)} L {f(dx1 + w * 0.08)} {f(h * 0.9)} L {f(dx1)} {f(h * 0.86)} Z" fill="#B8862A" stroke="#0D0D0F" stroke-width="2"></path>')
    else:
        o.append(f'<rect x="{f(dx0)}" y="{f(dt)}" width="{f(dx1 - dx0)}" height="{f(h * 0.54)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
                 f'<path d="M{f(w * 0.5)} {f(dt)} L {f(w * 0.5)} {f(h * 0.86)}" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<rect x="{f(dx0 - 6)}" y="{f(h * 0.56)}" width="{f(dx1 - dx0 + 12)}" height="10" fill="#3A2A1A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(S1.lamp(w * 0.12, h * 0.86, min(0.5, h / 600), lit=open_) + S1.lamp(w * 0.88, h * 0.86, min(0.5, h / 600), lit=open_))
    return "".join(o)

def cleansing(p, w, h, seed):
    """The Levites carrying forth the uncleanness out of the house to the brook Kidron: men bearing baskets down to the
    brook, the house open above."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), temple_front(w * 0.3, h * 0.56, w * 0.44, seed), ground(w, h, h * 0.56, "#C8B88A", dy=0),
         f'<path d="M-10 {f(h * 0.88)} C {f(w * 0.3)} {f(h * 0.84)} {f(w * 0.6)} {f(h * 0.92)} {f(w + 10)} {f(h * 0.86)}" stroke="#2C7DA8" stroke-width="12" fill="none"></path>']
    s = fit(b, max(h * 0.44, b - 220))
    for i in range(4):
        x = w * (0.46 + i * 0.13); y = h * (0.66 + i * 0.06)
        o.append(priest(p, x, y, fit(y, y - (b - h * 0.44) * 0.7) * 0.9, up=[(22, -158), (30, -190), (10, -214)])
                 + f'<rect x="{f(x - 6)}" y="{f(y - fit(y, y - (b - h * 0.44) * 0.7) * 0.9 * 236)}" width="22" height="14" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    return "".join(o)

# ---- 2 Chronicles 30–32 -------------------------------------------------------------------------------------------------
import ruth1 as R1

POSTS_M = [("BEER-SHEBA", 0.42, 0.94), ("JERUSALEM", 0.44, 0.62), ("EPHRAIM", 0.42, 0.42), ("MANASSEH", 0.4, 0.28), ("ZEBULUN", 0.36, 0.14), ("ASHER", 0.24, 0.12), ("DAN", 0.5, 0.04)]
def posts_map(w, h, scorn=False):
    """The posts with the letters from Beer-sheba even to Dan (scorn=True: Ephraim, Manasseh and Zebulun laughing them to
    scorn, a few of Asher, Manasseh and Zebulun coming to Jerusalem)."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.14)} -10 C {f(w * 0.16)} {f(h * 0.4)} {f(w * 0.12)} {f(h * 0.7)} {f(w * 0.1)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.66)} -10 C {f(w * 0.64)} {f(h * 0.3)} {f(w * 0.68)} {f(h * 0.5)} {f(w * 0.64)} {f(h * 0.62)}" stroke="#2C9DB8" stroke-width="4" fill="none"></path>')
    pos = {n: (w * x, h * y) for n, x, y in POSTS_M}
    for nm in ("BEER-SHEBA", "EPHRAIM", "DAN"): o.append(route([pos["JERUSALEM"], pos[nm]], color="#FFD23F", sw=2))
    if scorn:
        for nm in ("ASHER", "MANASSEH", "ZEBULUN"): o.append(route([pos[nm], (w * 0.46, h * 0.58)], color="#9CCB5E", sw=2))
    for nm, x, y in POSTS_M:
        c = "#D7261E" if scorn and nm in ("EPHRAIM",) else ("#FFD23F" if nm == "JERUSALEM" else CYAN)
        o.append(node(w * x, h * y, nm, c, r=5, dy=-11, size=9))
    o.append(label(w * 0.8, h * 0.9, "THE POSTS WITH THE LETTERS", "#FFD23F", 9))
    return "".join(o)

def heaps(p, w, h, seed):
    """The heaps of the first-fruits and the tithes laid up in the court, heap upon heap, the king and the princes blessing."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), temple_front(w * 0.5, h * 0.56, w * 0.5, seed), ground(w, h, h * 0.56, "#C8B88A", dy=0)]
    for i, c in enumerate(("#E8C88A", "#C8A060", "#D9A25A", "#E8D8A0")):
        o.append(R1.heap(w * (0.2 + i * 0.2), h * 0.86, w * 0.16, h * 0.18, color=c))
    s = fit(b, max(h * 0.42, b - 230))
    o.append(king_fig(p, w * 0.08, b, s, up=[(22, -158), (40, -190), (50, -222)], cloth=REHO_C))
    return "".join(o)

def stopped_springs(w, h, upper=False):
    """The waters of the fountains stopped without the city, and (upper=True) the upper spring of Gihon brought straight
    down on the west side of the city of David — a technical plan."""
    o = [bp(w, h)]
    cx, cy = w * 0.56, h * 0.48
    o.append(f'<path d="M{f(cx - w * 0.18)} {f(cy - h * 0.3)} L {f(cx + w * 0.16)} {f(cy - h * 0.34)} L {f(cx + w * 0.2)} {f(cy + h * 0.32)} L {f(cx - w * 0.14)} {f(cy + h * 0.36)} Z" fill="#8FD0E2" fill-opacity="0.08" stroke="#8FD0E2" stroke-width="2.4"></path>'
             + label(cx, cy, "THE CITY OF DAVID", "#8FD0E2", 10))
    gx, gy = cx + w * 0.3, cy - h * 0.06
    o.append(node(gx, gy, "GIHON", "#FFD23F", r=6, dy=-12, size=10))
    if upper:
        o.append(route([(gx, gy), (cx + w * 0.02, cy - h * 0.08), (cx - w * 0.22, cy + h * 0.1)], color="#2C9DB8", sw=3, dash="2 0"))
        o.append(node(cx - w * 0.22, cy + h * 0.1, "WEST SIDE", "#2C9DB8", r=5, dy=18, size=9) + label(cx - w * 0.02, cy - h * 0.14, "BROUGHT STRAIGHT DOWN", "#2C9DB8", 8))
    else:
        for x, y in ((0.14, 0.2), (0.12, 0.7), (0.9, 0.82)):
            o.append(f'<circle cx="{f(w * x)}" cy="{f(h * y)}" r="10" fill="none" stroke="#D7261E" stroke-width="2"></circle>'
                     f'<path d="M{f(w * x - 8)} {f(h * y - 8)} L {f(w * x + 8)} {f(h * y + 8)} M{f(w * x + 8)} {f(h * y - 8)} L {f(w * x - 8)} {f(h * y + 8)}" stroke="#D7261E" stroke-width="2.4"></path>')
        o.append(f'<path d="M-10 {f(h * 0.96)} C {f(w * 0.3)} {f(h * 0.88)} {f(w * 0.6)} {f(h * 0.98)} {f(w + 10)} {f(h * 0.9)}" stroke="#2C9DB8" stroke-width="3" stroke-dasharray="10 8" fill="none"></path>'
                 + label(w * 0.5, h * 0.86, "THE FOUNTAINS STOPPED", "#D7261E", 9))
    return "".join(o)
