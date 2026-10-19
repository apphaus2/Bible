"""Drawings for the Daniel volume (chapter by chapter, below), on top of Esther's (est.art carries chr2.art, chr1.art, kg2.art,
kg1.art and 2 Samuel's drawings as K2).

Babylon: walls and a gate of blue glazed brick with walking lions and rosettes in yellow (bab_wall), the stepped tower
(ziggurat), palms by the river. Figures at a distance: Nebuchadnezzar in deep red with a tall gold tiara (neb), Belshazzar in
purple with the tiara (bel), Darius the Mede in crimson with the Persian crown (darius), Daniel in blue with a blue headcloth
(dan_fig: a youth, black-bearded, greying, grey), Hananiah, Mishael and Azariah in rust, green and teal (three_fig), the
magicians and Chaldeans in violet with tall caps (magus), the prince of the eunuchs in white (eunuch)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from est.art import *
from est.art import f, K2, K3, PCROWN, GREY_BEARD, frieze, pavement, guard, prince, behind
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, numbers1 as N, samuel3 as S3, judges1 as J1, joshua1 as J
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import man, woman, sun, label, grid_bg, node, route
from exo import art as A
from exo.art8 import bp, dim, tag
from num.art import ALL
from job.art import smoke
import kg1.art as K1

INK, GOLD, CREAM, CYAN = "#0D0D0F", "#E8B830", "#F3EFE6", "#8FD0E2"
NEB_C, BEL_C, DAR_C, DAN_C, DAN_H = "#7A1A1A", "#5A1A6A", "#8A1A2A", "#1F5FAD", "#1F4A8A"
THREE_C = [("#A8421E", "#A8421E"), ("#2E7A3A", "#2E7A3A"), ("#1F7A8A", "#1F7A8A")]   # Shadrach, Meshach, Abed-nego
MAGI_C = ["#4A2A6A", "#5A3A7A", "#3A2A5A", "#6A3A6A", "#4A3A7A"]
GLAZE, GLAZE_D = "#1F4FA0", "#173A7A"

TIARA = ('<path d="M-11 -192 L -12 -224 C -6 -228 6 -228 12 -224 L 11 -192 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6" stroke-linejoin="round"></path>'
         '<path d="M-11.5 -204 L 11.5 -204 M-12 -216 L 12 -216" stroke="#A8721A" stroke-width="1.6"></path><circle cx="0" cy="-210" r="2.4" fill="#B5121B" stroke="#0D0D0F" stroke-width="0.8"></circle>')
CAP = '<path d="M-13 -190 L -4 -234 L 4 -234 L 13 -190 Z" fill="#3A2A5A" stroke="#0D0D0F" stroke-width="1.6" stroke-linejoin="round"></path><path d="M-12 -196 L 12 -196" stroke="#E8B830" stroke-width="2.4"></path>'
STUBBLE = '<path d="M-8 -172 C -7 -164 -3 -160 0 -159 C 3 -160 7 -164 8 -172" fill="none" stroke="#2A1A10" stroke-width="2" opacity="0.6"></path>'
def beard(color): return A.WHITE_BEARD.replace("#E8E2D6", color)
CHAIN = '<path d="M-12 -148 C -8 -126 8 -126 12 -148" fill="none" stroke="#E8B830" stroke-width="3.2"></path><circle cx="0" cy="-130" r="3.4" fill="#E8B830" stroke="#0D0D0F" stroke-width="1"></circle>'

def neb(p, x, y, s, flip=False, up=None, extra=""):
    """Nebuchadnezzar at a distance: deep red robe, black beard, a tall gold tiara."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=NEB_C, sw=3, flip=flip, up=up, extra=A.BLACK_BEARD + TIARA + extra)

def bel(p, x, y, s, flip=False, up=None, extra=""):
    """Belshazzar at a distance: purple robe, young, the gold tiara."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=BEL_C, sw=3, flip=flip, up=up, extra=STUBBLE + TIARA + extra)

def darius(p, x, y, s, flip=False, up=None, extra=""):
    """Darius the Mede at a distance: crimson robe, grey beard, the Persian crown."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=DAR_C, sw=3, flip=flip, up=up, extra=GREY_BEARD + PCROWN + extra)

def dan_fig(p, x, y, s, age=1, flip=False, up=None, chain=False, kind="Robe"):
    """Daniel at a distance: blue robe, blue headcloth with a dark cord; age 0 a youth (tunic), 1 black beard, 2 greying, 3 grey."""
    b = {0: STUBBLE, 1: A.BLACK_BEARD, 2: beard("#6A645E"), 3: beard("#B8B2A8")}[age]
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=DAN_C, kind="Tunic" if age == 0 else kind, sw=3, flip=flip, up=up,
                     extra=A.headcloth(DAN_H, cord="#2A1A10") + b + (CHAIN if chain else ""))

def three_fig(p, x, y, s, i, flip=False, up=None, young=False, cloth=None):
    """Hananiah (Shadrach, rust), Mishael (Meshach, green), Azariah (Abed-nego, teal) at a distance."""
    c, hc = THREE_C[i]
    b = STUBBLE if young or i == 1 else A.BLACK_BEARD
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth or c, kind="Tunic" if young else "Robe", sw=3, flip=flip, up=up,
                     extra=A.headcloth(hc, cord="#2A1A10") + b)

def magus(p, x, y, s, k=0, flip=False, up=None):
    """A magician, enchanter or Chaldean: a violet robe, a tall cap with a gold band, black beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=MAGI_C[k % len(MAGI_C)], sw=3, flip=flip, up=up, extra=A.BLACK_BEARD + CAP)

def eunuch(p, x, y, s, flip=False, up=None, cloth="#E8E2D6"):
    """The prince of the eunuchs (or his steward): a pale robe, beardless, a white headcloth with a gold band."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, sw=3, flip=flip, up=up, extra=A.headcloth("#F3EFE6", cord="#E8B830"))

def youth(p, x, y, s, cloth, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, kind="Tunic", sw=3, flip=flip, up=up, extra=A.headcloth(cloth, cord="#2A1A10"))

def glow_fig(x, y, s, op=0.9, color="#FFF4C2"):
    """A figure of light (an angel, the fourth in the fire): a tall shape with no face, ringed with a glow."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
            f'<ellipse cx="0" cy="-100" rx="60" ry="120" fill="{color}" opacity="{op * 0.25}"></ellipse>'
            f'<ellipse cx="0" cy="-100" rx="38" ry="96" fill="{color}" opacity="{op * 0.3}"></ellipse>'
            f'<path d="M-24 0 C -26 -60 -22 -120 -14 -150 C -18 -170 -12 -190 0 -192 C 12 -190 18 -170 14 -150 C 22 -120 26 -60 24 0 Z" fill="#FFFFFF" opacity="{op}" stroke="#FFD23F" stroke-width="2"></path></g>')

# ---- Babylon ----------------------------------------------------------------------------------------------------------------
def lion_walk(x, y, s=1.0, color="#E8C040", flip=False):
    """A walking lion in profile, as on the glazed brick of Babylon ((x, y) = its feet)."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            f'<path d="M-52 -18 C -56 -34 -44 -42 -30 -40 L 16 -40 C 22 -52 44 -56 54 -44 C 62 -36 62 -24 56 -18 L 48 -16 C 46 -10 40 -8 34 -12 L 32 0 L 23 0 L 22 -14 L -24 -14 L -26 0 L -35 0 L -40 -16 Z" '
            f'fill="{color}" stroke="#0D0D0F" stroke-width="{f(2.2 / max(s, 0.3))}" stroke-linejoin="round"></path>'
            f'<path d="M-52 -30 C -66 -32 -70 -20 -62 -12" fill="none" stroke="#0D0D0F" stroke-width="{f(3 / max(s, 0.3))}" stroke-linecap="round"></path>'
            f'<path d="M18 -40 C 22 -30 22 -22 18 -16" fill="none" stroke="#0D0D0F" stroke-width="{f(1.4 / max(s, 0.3))}" opacity="0.7"></path>'
            f'<circle cx="48" cy="-36" r="1.8" fill="#0D0D0F"></circle></g>')

def bab_wall(w, y0, y1, seed=1, lions=True):
    """A wall of blue glazed brick from y0 to y1: courses of brick, a band of rosettes, and walking lions in yellow."""
    hh = y1 - y0
    o = [f'<rect x="-10" y="{f(y0)}" width="{f(w + 20)}" height="{f(hh)}" fill="{GLAZE}" stroke="#0D0D0F" stroke-width="2"></rect>']
    o.append("".join(f'<path d="M-10 {f(y0 + k)} L {f(w + 10)} {f(y0 + k)}" stroke="{GLAZE_D}" stroke-width="1"></path>' for k in range(8, int(hh), 10)))
    o.append(frieze(w, y0 + hh * 0.08, max(10, hh * 0.1), color="#173A7A"))
    if lions:
        k = max(0.18, min(0.55, hh / 520))
        n = max(2, int(w / (260 * k)))
        for i in range(n):
            o.append(lion_walk(w * (i + 0.5) / n, y0 + hh * 0.42, k))
    o.append(frieze(w, y1 - max(10, hh * 0.1) - hh * 0.04, max(10, hh * 0.1), color="#173A7A"))
    return "".join(o)

def ziggurat(cx, base, wd, ht, color="#C8A06A", dark=False):
    """The stepped tower of Babylon: seven stages and a stair up the front."""
    cols = ("#5A4A5A", "#6A5A6A") if dark else (color, "#B08A5A")
    o = []
    for i in range(7):
        ww = wd * (1 - i * 0.12); y = base - ht * i / 7
        o.append(f'<rect x="{f(cx - ww / 2)}" y="{f(y - ht / 7)}" width="{f(ww)}" height="{f(ht / 7)}" fill="{cols[i % 2]}" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(f'<path d="M{f(cx - wd * 0.06)} {f(base)} L {f(cx - wd * 0.03)} {f(base - ht * 0.72)} L {f(cx + wd * 0.03)} {f(base - ht * 0.72)} L {f(cx + wd * 0.06)} {f(base)} Z" fill="{"#4A3A4A" if dark else "#E8D0A0"}" stroke="#0D0D0F" stroke-width="1.6"></path>')
    o.append(f'<rect x="{f(cx - wd * 0.08)}" y="{f(base - ht - ht * 0.08)}" width="{f(wd * 0.16)}" height="{f(ht * 0.1)}" fill="{"#3A5AA0" if not dark else "#2A3A6A"}" stroke="#0D0D0F" stroke-width="2"></rect>')
    return "".join(o)

def bab_gate(cx, base, wd, ht):
    """A gate of Babylon in blue glazed brick: two crenellated towers, the arch, rows of beasts in yellow."""
    o = []
    for dx in (-0.5, 0.18):
        x0 = cx + wd * dx
        o.append(f'<rect x="{f(x0)}" y="{f(base - ht)}" width="{f(wd * 0.32)}" height="{f(ht)}" fill="{GLAZE}" stroke="#0D0D0F" stroke-width="2.2"></rect>')
        for i in range(4):
            o.append(f'<rect x="{f(x0 + i * wd * 0.08 + wd * 0.01)}" y="{f(base - ht - ht * 0.07)}" width="{f(wd * 0.05)}" height="{f(ht * 0.07)}" fill="{GLAZE}" stroke="#0D0D0F" stroke-width="1.6"></rect>')
        for j in range(3):
            o.append(lion_walk(x0 + wd * 0.16, base - ht * (0.2 + j * 0.26), min(1, wd / 900), color="#E8C040" if j % 2 == 0 else "#F3EFE6"))
    o.append(f'<rect x="{f(cx - wd * 0.18)}" y="{f(base - ht * 0.82)}" width="{f(wd * 0.36)}" height="{f(ht * 0.82)}" fill="{GLAZE}" stroke="#0D0D0F" stroke-width="2.2"></rect>'
             f'<path d="M{f(cx - wd * 0.1)} {f(base)} L {f(cx - wd * 0.1)} {f(base - ht * 0.42)} A {f(wd * 0.1)} {f(wd * 0.1)} 0 0 1 {f(cx + wd * 0.1)} {f(base - ht * 0.42)} L {f(cx + wd * 0.1)} {f(base)} Z" fill="#2A1A10" stroke="#E8C040" stroke-width="2.4"></path>')
    return "".join(o)

def babylon(w, h, seed, tone="day"):
    """Babylon from the river: the walls and a blue gate, the stepped tower behind, palms along the water."""
    skies = {"day": ("#8FD0E2", "#F3E8C8"), "dusk": ("#3A2A5A", "#E88A5A"), "night": ("#0F0E2A", "#3A2A5A")}
    dark = tone != "day"
    o = [K2.sky(w, h, *skies[tone])]
    if tone == "night": o.append(mk.stars(50, w, h * 0.5, seed))
    o.append(ziggurat(w * 0.3, h * 0.62, w * 0.36, h * 0.46, dark=dark))
    o.append(f'<rect x="-10" y="{f(h * 0.5)}" width="{f(w + 20)}" height="{f(h * 0.14)}" fill="{"#5A4A4A" if dark else "#C8A878"}" stroke="#0D0D0F" stroke-width="2"></rect>')
    for i in range(int(w / 26) + 2):
        o.append(f'<rect x="{f(i * 26)}" y="{f(h * 0.47)}" width="14" height="{f(h * 0.03)}" fill="{"#5A4A4A" if dark else "#C8A878"}" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    o.append(bab_gate(w * 0.72, h * 0.66, w * 0.3, h * 0.3))
    o.append(f'<rect x="-10" y="{f(h * 0.66)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="{"#1A2A4A" if dark else "#3A7AA0"}" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append("".join(f'<path d="M{f(x)} {f(h * (0.74 + (i % 3) * 0.07))} l {f(w * 0.06)} 0" stroke="{"#3A5A8A" if dark else "#8FD0E2"}" stroke-width="2"></path>'
                     for i, x in enumerate(random.Random(seed).uniform(0, w) for _ in range(14))))
    for x in (0.04, 0.12, 0.92):
        o.append(J1.palm(w * x, h * 0.68, min(0.9, h / 420)))
    return "".join(o)

def bab_floor(w, h, y0, color="#B89A6A"):
    """A floor of baked brick in perspective from y0 down to the bottom edge."""
    o = [f'<rect x="-10" y="{f(y0)}" width="{f(w + 20)}" height="{f(h - y0 + 10)}" fill="{color}" stroke="#0D0D0F" stroke-width="2"></rect>']
    vx = w * 0.5
    for j in range(-8, 9):
        o.append(f'<path d="M{f(vx + j * w * 0.06)} {f(y0)} L {f(vx + j * w * 0.2)} {f(h + 10)}" stroke="#8A6A4A" stroke-width="1.2" opacity="0.7"></path>')
    for i in range(1, 5):
        y = y0 + (h - y0) * (i / 5) ** 1.4
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#8A6A4A" stroke-width="1.2" opacity="0.7"></path>')
    return "".join(o)

def bab_hall(p, w, h, seed, floor=0.7, tone="day"):
    """A hall of the palace of Babylon: the glazed blue wall with its lions, cedar beams above, the paved floor."""
    fy = h * floor
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="{"#2A1A2A" if tone == "night" else "#C8B08A"}"></rect>']
    o.append(bab_wall(w, h * 0.06, fy, seed))
    o.append(f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h * 0.06 + 10)}" fill="#6A3A1E" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(bab_floor(w, h, fy))
    if tone == "night": o.append(f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0F0E2A" opacity="0.45"></rect>')
    return "".join(o)

def throne_k(p, w, h, xk, b, who="neb", up=None):
    """The king seated on his throne, the throne's foot at b."""
    kk = min(1.5, (b - h * 0.06) / 185)
    fig = {"neb": neb, "bel": bel, "darius": darius}[who]
    o, _, _ = seated_king(p, xk, b, kk, up=up, fig=fig)
    return o

# ---- Daniel 1 -----------------------------------------------------------------------------------------------------------------
def youths(p, w, h, seed):
    """In the court of the palace: the prince of the eunuchs before a row of youths of the children of Israel, Daniel and his
    three companions at the front."""
    b = h * 0.94
    o = [bab_hall(p, w, h, seed, floor=0.68)]
    s = fit(b, max(h * 0.2, b - 250))
    o.append(eunuch(p, w * 0.14, b, s, up=[(-22, -158), (-10, -176), (6, -186)]))
    cl = ["#8A7A5A", "#6A5A7A", "#7A6A4A", "#5A6A7A"]
    for i in range(4):
        o.append(youth(p, w * (0.66 + i * 0.09), b - 26, s * 0.84, cl[i], flip=True))
    o.append(dan_fig(p, w * 0.32, b, s * 0.94, age=0, flip=True))
    for i in range(3):
        o.append(three_fig(p, w * (0.42 + i * 0.08), b - (i % 2) * 4, s * 0.92, i, flip=True, young=True))
    return "".join(o)

def names_plate(w, h):
    """The names given by the prince of the eunuchs, as a technical plate: each Hebrew name to its Babylonian name."""
    o = [grid_bg(w, h)]
    rows = [("DANIEL", "BELTESHAZZAR", DAN_C), ("HANANIAH", "SHADRACH", THREE_C[0][0]), ("MISHAEL", "MESHACH", THREE_C[1][0]), ("AZARIAH", "ABED-NEGO", THREE_C[2][0])]
    sz = max(10, min(16, h / 14))
    for i, (a, b2, c) in enumerate(rows):
        y = h * (0.18 + i * 0.2)
        o.append(f'<rect x="{f(w * 0.08)}" y="{f(y - sz)}" width="{f(w * 0.3)}" height="{f(sz * 1.8)}" fill="{c}" fill-opacity="0.3" stroke="{c}" stroke-width="2"></rect>'
                 + label(w * 0.23, y + sz * 0.3, a, CREAM, sz)
                 + route([(w * 0.4, y), (w * 0.58, y)], color="#FFD23F")
                 + f'<rect x="{f(w * 0.6)}" y="{f(y - sz)}" width="{f(w * 0.32)}" height="{f(sz * 1.8)}" fill="#12113A" stroke="#FFD23F" stroke-width="2"></rect>'
                 + label(w * 0.76, y + sz * 0.3, b2, "#FFD23F", sz))
    o.append(label(w * 0.23, h * 0.95, "OF THE CHILDREN OF JUDAH", CYAN, 9) + label(w * 0.76, h * 0.95, "THE NAMES GIVEN THEM IN BABYLON", "#FFD23F", 9))
    return "".join(o)

def platter(x, y, k):
    return (f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(40 * k)}" ry="{f(10 * k)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></ellipse>'
            f'<path d="M{f(x - 26 * k)} {f(y - 2 * k)} C {f(x - 24 * k)} {f(y - 26 * k)} {f(x + 24 * k)} {f(y - 26 * k)} {f(x + 26 * k)} {f(y - 2 * k)} Z" fill="#9A4A2A" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<path d="M{f(x - 12 * k)} {f(y - 16 * k)} C {f(x - 4 * k)} {f(y - 20 * k)} {f(x + 6 * k)} {f(y - 20 * k)} {f(x + 14 * k)} {f(y - 14 * k)}" fill="none" stroke="#E8A06A" stroke-width="2"></path>')

def cup(x, y, k, color="#E8B830", fill="#7A1A2A"):
    return (f'<path d="M{f(x - 12 * k)} {f(y - 30 * k)} L {f(x + 12 * k)} {f(y - 30 * k)} C {f(x + 12 * k)} {f(y - 16 * k)} {f(x + 4 * k)} {f(y - 12 * k)} {f(x + 3 * k)} {f(y - 10 * k)} '
            f'L {f(x + 3 * k)} {f(y - 3 * k)} L {f(x + 9 * k)} {f(y)} L {f(x - 9 * k)} {f(y)} L {f(x - 3 * k)} {f(y - 3 * k)} L {f(x - 3 * k)} {f(y - 10 * k)} '
            f'C {f(x - 4 * k)} {f(y - 12 * k)} {f(x - 12 * k)} {f(y - 16 * k)} {f(x - 12 * k)} {f(y - 30 * k)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<ellipse cx="{f(x)}" cy="{f(y - 29 * k)}" rx="{f(11 * k)}" ry="{f(3 * k)}" fill="{fill}"></ellipse>')

def bowl(x, y, k, fill="#8A9A3A", color="#B5652E"):
    return (f'<path d="M{f(x - 26 * k)} {f(y - 18 * k)} C {f(x - 24 * k)} {f(y)} {f(x + 24 * k)} {f(y)} {f(x + 26 * k)} {f(y - 18 * k)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<ellipse cx="{f(x)}" cy="{f(y - 18 * k)}" rx="{f(26 * k)}" ry="{f(6 * k)}" fill="{fill}" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')

def jug(x, y, k, color="#C8A06A"):
    return (f'<path d="M{f(x - 8 * k)} {f(y - 50 * k)} L {f(x + 8 * k)} {f(y - 50 * k)} L {f(x + 6 * k)} {f(y - 40 * k)} C {f(x + 22 * k)} {f(y - 32 * k)} {f(x + 22 * k)} {f(y - 4 * k)} {f(x + 10 * k)} {f(y)} '
            f'L {f(x - 10 * k)} {f(y)} C {f(x - 22 * k)} {f(y - 4 * k)} {f(x - 22 * k)} {f(y - 32 * k)} {f(x - 6 * k)} {f(y - 40 * k)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="2"></path>')

def two_tables(w, h, seed, ten=False):
    """The king's dainties and his wine on a gold table at the left; pulse and water on a plain board at the right.
    ten=True: ten marks above the plain board, the days of the proving."""
    o = [bab_hall("tt", w, h, seed, floor=0.62)]
    k = min(1.4, h / 260)
    y = h * 0.84
    o.append(f'<rect x="{f(w * 0.06)}" y="{f(y)}" width="{f(w * 0.4)}" height="{f(12 * k)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(w * x)}" y="{f(y + 12 * k)}" width="{f(8 * k)}" height="{f(h - y)}" fill="#C8962E" stroke="#0D0D0F" stroke-width="1.6"></rect>' for x in (0.08, 0.42)))
    o.append(platter(w * 0.18, y, k) + platter(w * 0.32, y, k * 0.8) + cup(w * 0.4, y, k) + cup(w * 0.11, y, k * 0.9))
    o.append(f'<rect x="{f(w * 0.56)}" y="{f(y)}" width="{f(w * 0.38)}" height="{f(12 * k)}" fill="#A8885A" stroke="#0D0D0F" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(w * x)}" y="{f(y + 12 * k)}" width="{f(8 * k)}" height="{f(h - y)}" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="1.6"></rect>' for x in (0.58, 0.9)))
    for i in range(4): o.append(bowl(w * (0.62 + i * 0.075), y, k * 0.7))
    o.append(jug(w * 0.88, y, k * 0.9))
    o.append(label(w * 0.26, y + 30 * k, "THE KING'S DAINTIES · THE WINE", CREAM, max(8, 9 * k * 0.8)) + label(w * 0.75, y + 30 * k, "PULSE · WATER", CREAM, max(8, 9 * k * 0.8)))
    if ten:
        for i in range(10):
            x = w * (0.58 + i * 0.037)
            o.append(f'<rect x="{f(x)}" y="{f(h * 0.1)}" width="{f(w * 0.028)}" height="{f(h * 0.08)}" fill="#12113A" stroke="#FFD23F" stroke-width="1.6"></rect>'
                     + label(x + w * 0.014, h * 0.165, str(i + 1), "#FFD23F", 9))
    return "".join(o)

def before_king(p, w, h, seed, n=4, magi=3, who="neb"):
    """The king on his throne; the four youths standing before him (n=4), the magicians behind them."""
    b = h * 0.94
    o = [bab_hall(p, w, h, seed, floor=0.62), throne_k(p, w, h, w * 0.84, b, who)]
    s = fit(b, max(h * 0.2, b - 250))
    for i in range(magi): o.append(magus(p, w * (0.06 + i * 0.07), b - 22, s * 0.8, i))
    if n:
        o.append(dan_fig(p, w * 0.58, b, s, age=0))
        for i in range(3): o.append(three_fig(p, w * (0.32 + i * 0.08), b - (i % 2) * 4, s * 0.96, i, young=True))
    return "".join(o)

def treasure_house(p, w, h, seed):
    """The vessels of the house of God brought into the treasure-house of the god of Babylon: gold cups, bowls and basins set
    out on shelves in a dim storeroom of blue brick, a soldier carrying in one more."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A2440"></rect>', bab_wall(w, h * 0.04, h * 0.8, seed, lions=False),
         bab_floor(w, h, h * 0.8, color="#7A6A5A")]
    k = min(1.2, h / 300)
    for row in range(3):
        y = h * (0.28 + row * 0.22)
        o.append(f'<rect x="{f(w * 0.04)}" y="{f(y)}" width="{f(w * 0.62)}" height="{f(8 * k)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
        for i in range(7):
            x = w * (0.08 + i * 0.085)
            o.append((cup(x, y, k * 0.6, fill="#E8B830") if (i + row) % 3 == 0 else bowl(x, y, k * 0.6, fill="#FFE680", color="#E8B830") if (i + row) % 3 == 1 else jug(x, y, k * 0.5, color="#E8B830")))
    s = fit(b, max(h * 0.2, b - 230))
    o.append(guard(p, w * 0.84, b, s, cloth="#5A4A6A", flip=True))
    o.append(bowl(w * 0.79, b - 120 * s, s * 1.2, fill="#FFE680", color="#E8B830"))
    o.append(V.rays(w * 0.35, h * 0.5, 20, 10, w * 0.4, color="#FFE680", op=0.08))
    return "".join(o)

# ---- Daniel 2 -----------------------------------------------------------------------------------------------------------------
def king_bed(p, w, h, seed):
    """The king's bedchamber by night: the king lying on his gold bed, troubled, a lamp, the stars in the high window."""
    o = [bab_hall(p, w, h, seed, floor=0.7, tone="night")]
    wx, wy = w * 0.62, h * 0.12
    o.append(f'<path d="M{f(wx)} {f(wy + h * 0.32)} L {f(wx)} {f(wy + h * 0.08)} A {f(w * 0.08)} {f(w * 0.08)} 0 0 1 {f(wx + w * 0.16)} {f(wy + h * 0.08)} L {f(wx + w * 0.16)} {f(wy + h * 0.32)} Z" fill="#0F0E2A" stroke="#0D0D0F" stroke-width="3"></path>'
             + f'<g>{mk.stars(14, w * 0.14, h * 0.28, seed)}</g>'.replace("<g><g", f'<g transform="translate({f(wx + w * 0.01)} {f(wy)})"><g'))
    o.append(K1.bed(w, h, w * 0.16, w * 0.62, h * 0.86, cover="#7A1A1A", head="#C98E66", hair="#0D0D0F"))
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.4)} C {f(w * 0.54)} {f(h * 0.3)} {f(w * 0.48)} {f(h * 0.24)} {f(w * 0.52)} {f(h * 0.16)}" fill="none" stroke="#B89AFF" stroke-width="2.4" stroke-dasharray="4 6" opacity="0.8"></path>')
    o.append(f'<path d="M{f(w * 0.84)} {f(h * 0.9)} l 8 -30 l 8 30 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path><ellipse cx="{f(w * 0.85 + 4)}" cy="{f(h * 0.9 - 36)}" rx="10" ry="6" fill="#C8962E" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
             + E.flame(w * 0.85 + 4, h * 0.9 - 40, 10, 22, 2))
    return "".join(o)

def wise_men(p, w, h, seed, who="neb", magi=6, daniel=False, arioch=False):
    """The magicians, the enchanters, the sorcerers and the Chaldeans standing before the king on his throne."""
    b = h * 0.94
    o = [bab_hall(p, w, h, seed, floor=0.62), throne_k(p, w, h, w * 0.84, b, who)]
    s = fit(b, max(h * 0.2, b - 250))
    for i in range(magi):
        o.append(magus(p, w * (0.06 + i * 0.085), b - (i % 2) * 18, s * (0.86 + (i % 2) * 0.06), i))
    if daniel: o.append(dan_fig(p, w * 0.62, b, s, age=1))
    if arioch: o.append(guard(p, w * 0.7, b, s, cloth="#7A2A1A"))
    return "".join(o)

def guards_out(p, w, h, seed):
    """The decree gone forth: Arioch the captain of the guard and his men going out by the gate of the palace."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), babylon(w, h, seed, tone="dusk"), ground(w, h, h * 0.8, "#8A6A5A", dy=0)]
    s = fit(b, max(h * 0.3, b - 220))
    for i in range(6):
        o.append(guard(p, w * (0.18 + i * 0.12), b - (i % 2) * 6, s * (1 - i * 0.03), cloth=["#7A2A1A", "#5A4A6A", "#6A5A3A"][i % 3], flip=True))
    return "".join(o)

def four_pray(p, w, h, seed, n=4, age=1):
    """Daniel's house by night: Daniel and his companions kneeling by a lamp, the window open to the stars."""
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A2A"></rect>']
    o.append(f'<rect x="{f(w * 0.62)}" y="{f(h * 0.1)}" width="{f(w * 0.24)}" height="{f(h * 0.4)}" fill="#0F0E2A" stroke="#0D0D0F" stroke-width="3"></rect>'
             + f'<g transform="translate({f(w * 0.62)} {f(h * 0.1)})">{mk.stars(18, w * 0.24, h * 0.4, seed)}</g>'
             + f'<path d="M{f(w * 0.74)} {f(h * 0.1)} L {f(w * 0.74)} {f(h * 0.5)} M{f(w * 0.62)} {f(h * 0.3)} L {f(w * 0.86)} {f(h * 0.3)}" stroke="#5A3A22" stroke-width="5"></path>')
    o.append(f'<rect x="-10" y="{f(h * 0.82)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#5A4030" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(V.rays(w * 0.5, h * 0.7, 18, 8, h * 0.5, color="#FFE680", op=0.12))
    o.append(f'<path d="M{f(w * 0.49)} {f(h * 0.82)} l 6 -20 l 6 20 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>' + E.flame(w * 0.5 + 1, h * 0.82 - 22, 10, 24, 2))
    k = h * 0.42 / 130 / 0.62
    cl = [DAN_C, THREE_C[0][0], THREE_C[1][0], THREE_C[2][0]]
    xs = [0.36, 0.22, 0.64, 0.78]
    for i in range(n):
        o.append(E.kneel(w * xs[i], h * 0.83, k * 0.62, color=cl[i], flip=xs[i] > 0.5, skin="#C98E66"))
    return "".join(o)

def image_plate(w, h, stage=0):
    """The great image as a technical plate: stage 0 the image and its metals; 1 the stone cut out without hands smiting it
    upon its feet; 2 the metals broken like chaff, the stone become a great mountain; 3 the four kingdoms, and the fifth."""
    o = [bp(w, h)]
    cx = w * (0.34 if stage == 3 else 0.42)
    k = min(h / 560, w / 380)
    top, foot = h * 0.06, h * 0.06 + 520 * k
    if stage == 2:
        r = random.Random(7)
        for i in range(70):
            x = cx + r.uniform(-80, 260) * k; y = r.uniform(h * 0.1, h * 0.7)
            c = r.choice(("#FFD23F", "#C8D0D8", "#C8783A", "#8A9AA8", "#A87A5A"))
            o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(3, 8))} {f(r.uniform(-3, 3))}" stroke="{c}" stroke-width="2.2" opacity="0.8"></path>')
        o.append("".join(f'<path d="M{f(cx - 40 * k)} {f(h * (0.2 + i * 0.12))} C {f(cx + 80 * k)} {f(h * (0.16 + i * 0.12))} {f(cx + 200 * k)} {f(h * (0.24 + i * 0.12))} {f(w * 0.98)} {f(h * (0.18 + i * 0.12))}" fill="none" stroke="#8FD0E2" stroke-width="1.6" stroke-dasharray="10 8" opacity="0.6"></path>' for i in range(4)))
        o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.8)} C {f(w * 0.2)} {f(h * 0.62)} {f(w * 0.36)} {f(h * 0.42)} {f(w * 0.5)} {f(h * 0.4)} C {f(w * 0.64)} {f(h * 0.42)} {f(w * 0.8)} {f(h * 0.62)} {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} Z" '
                 f'fill="#8A8A9A" fill-opacity="0.35" stroke="#F3EFE6" stroke-width="2.4"></path>'
                 + label(w * 0.5, h * 0.62, "THE STONE · A GREAT MOUNTAIN, AND FILLED THE WHOLE EARTH", "#F3EFE6", max(9, 11 * min(1.2, k * 1.6))))
        return "".join(o)
    parts = [("HEAD · FINE GOLD", "#FFD23F", 0, 70), ("BREAST AND ARMS · SILVER", "#C8D0D8", 70, 190), ("BELLY AND THIGHS · BRASS", "#C8783A", 190, 300),
             ("LEGS · IRON", "#8A9AA8", 300, 450), ("FEET · IRON AND CLAY", "#A87A5A", 450, 520)]
    def Y(u): return top + u * k
    # the figure, front-on, in outline
    head = f'<ellipse cx="{f(cx)}" cy="{f(Y(36))}" rx="{f(26 * k)}" ry="{f(32 * k)}" fill="#FFD23F" fill-opacity="0.55" stroke="#FFD23F" stroke-width="2"></ellipse>'
    chest = (f'<path d="M{f(cx - 70 * k)} {f(Y(80))} L {f(cx + 70 * k)} {f(Y(80))} L {f(cx + 52 * k)} {f(Y(190))} L {f(cx - 52 * k)} {f(Y(190))} Z" fill="#C8D0D8" fill-opacity="0.45" stroke="#C8D0D8" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(cx + sx * 70 * k)} {f(Y(80))} L {f(cx + sx * 96 * k)} {f(Y(190))} L {f(cx + sx * 84 * k)} {f(Y(250))} L {f(cx + sx * 70 * k)} {f(Y(246))} L {f(cx + sx * 76 * k)} {f(Y(192))} L {f(cx + sx * 56 * k)} {f(Y(120))}" fill="#C8D0D8" fill-opacity="0.45" stroke="#C8D0D8" stroke-width="2"></path>' for sx in (-1, 1)))
    belly = f'<path d="M{f(cx - 52 * k)} {f(Y(190))} L {f(cx + 52 * k)} {f(Y(190))} L {f(cx + 56 * k)} {f(Y(300))} L {f(cx - 56 * k)} {f(Y(300))} Z" fill="#C8783A" fill-opacity="0.5" stroke="#C8783A" stroke-width="2"></path>'
    legs = "".join(f'<path d="M{f(cx + sx * 6 * k)} {f(Y(300))} L {f(cx + sx * 54 * k)} {f(Y(300))} L {f(cx + sx * 44 * k)} {f(Y(450))} L {f(cx + sx * 14 * k)} {f(Y(450))} Z" fill="#8A9AA8" fill-opacity="0.5" stroke="#8A9AA8" stroke-width="2"></path>' for sx in (-1, 1))
    feet = "".join(f'<path d="M{f(cx + sx * 12 * k)} {f(Y(450))} L {f(cx + sx * 46 * k)} {f(Y(450))} L {f(cx + sx * 60 * k)} {f(Y(520))} L {f(cx + sx * 8 * k)} {f(Y(520))} Z" fill="url(#ic{int(w)}{int(h)}{stage})" stroke="#A87A5A" stroke-width="2"></path>' for sx in (-1, 1))
    o.append(f'<defs><pattern id="ic{int(w)}{int(h)}{stage}" width="10" height="10" patternUnits="userSpaceOnUse"><rect width="10" height="10" fill="#A87A5A" fill-opacity="0.6"></rect><rect width="5" height="5" fill="#8A9AA8"></rect><rect x="5" y="5" width="5" height="5" fill="#8A9AA8"></rect></pattern></defs>')
    if stage == 1:
        g = f'<g transform="rotate(6 {f(cx)} {f(Y(520))})">'
        o.append(g + head + chest + belly + legs + "".join(f'<path d="M{f(cx + sx * 12 * k)} {f(Y(450))} L {f(cx + sx * 30 * k)} {f(Y(472))} L {f(cx + sx * 16 * k)} {f(Y(496))} L {f(cx + sx * 44 * k)} {f(Y(520))}" fill="none" stroke="#A87A5A" stroke-width="2.4"></path>' for sx in (-1, 1)) + '</g>')
        for i in range(10):
            a = random.Random(i).uniform(-2.6, -0.6)
            o.append(f'<path d="M{f(cx + 40 * k)} {f(Y(500))} l {f(math.cos(a) * 30 * k)} {f(math.sin(a) * 30 * k)}" stroke="#A87A5A" stroke-width="2.2"></path>')
        sx, sy = cx + 150 * k, Y(486)
        o.append(f'<path d="M{f(w * 0.98)} {f(h * 0.12)} C {f(w * 0.9)} {f(h * 0.3)} {f(sx + 60 * k)} {f(sy - 120 * k)} {f(sx + 20 * k)} {f(sy - 20 * k)}" fill="none" stroke="#F3EFE6" stroke-width="2" stroke-dasharray="8 6"></path>'
                 + f'<path d="M{f(sx - 34 * k)} {f(sy + 10 * k)} L {f(sx - 20 * k)} {f(sy - 30 * k)} L {f(sx + 20 * k)} {f(sy - 34 * k)} L {f(sx + 38 * k)} {f(sy)} L {f(sx + 14 * k)} {f(sy + 30 * k)} L {f(sx - 22 * k)} {f(sy + 28 * k)} Z" fill="#B8B8C8" stroke="#F3EFE6" stroke-width="2.4"></path>'
                 + tag(sx + 30 * k, sy - 30 * k, "A STONE · CUT OUT WITHOUT HANDS", w * 0.6, h * 0.08, color="#F3EFE6"))
        return "".join(o)
    o.append(head + chest + belly + legs + feet)
    if stage == 0:
        for name, c, a, b2 in parts:
            ym = Y((a + b2) / 2)
            o.append(tag(cx + 60 * k, ym, name, w * 0.64, ym - 6, color=c))
        o.append(dim(cx - 120 * k, Y(0), cx - 120 * k, Y(520), "A GREAT IMAGE · ITS BRIGHTNESS EXCELLENT", color=CYAN))
    else:
        names = [("I · THOU ART THE HEAD OF GOLD", "#FFD23F", 0, 70), ("II · ANOTHER KINGDOM INFERIOR TO THEE", "#C8D0D8", 70, 190),
                 ("III · A THIRD KINGDOM OF BRASS", "#C8783A", 190, 300), ("IV · STRONG AS IRON", "#8A9AA8", 300, 450), ("· A DIVIDED KINGDOM, PARTLY STRONG", "#A87A5A", 450, 520)]
        for name, c, a, b2 in names:
            ym = Y((a + b2) / 2)
            o.append(tag(cx + 60 * k, ym, name, w * 0.52, ym - 6, color=c, size=9))
    return "".join(o)

def mountain_kingdom(w, h, seed):
    """The stone become a great mountain that filled the whole earth: the image gone like chaff of the summer threshing-floors."""
    return image_plate(w, h, 2)

def oblation(p, w, h, seed):
    """The king fallen upon his face before Daniel in the hall, sweet odours rising from the censers."""
    b = h * 0.94
    o = [bab_hall(p, w, h, seed, floor=0.6)]
    s = fit(b, max(h * 0.2, b - 250))
    o.append(dan_fig(p, w * 0.7, b, s, age=1, flip=True))
    o.append(N.prostrate(w * 0.32, b, s * 0.9, color=NEB_C, skin="#C98E66"))
    for x in (0.12, 0.88):
        o.append(f'<path d="M{f(w * x - 14)} {f(b)} L {f(w * x - 8)} {f(b - 40 * s)} L {f(w * x + 8)} {f(b - 40 * s)} L {f(w * x + 14)} {f(b)} Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="2"></path>'
                 + smoke(w * x, b - 44 * s, 4, int(x * 100), color="#E8E2D6", op=0.5, k=s))
    return "".join(o)

# ---- Daniel 6: the den ------------------------------------------------------------------------------------------------------
from ecc.art import lion_lying

def den(p, w, h, seed, cover=False, daniel=True, stone=True, dawn=False, glow=True, lions=4):
    """Inside the den of lions: walls of rough stone, the mouth above (sealed with the stone, or open at dawn), a shaft of light
    on Daniel standing unharmed, the lions lying still about him."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1E1824"></rect>']
    for i in range(int(w * h / 5200)):
        x, y = r.uniform(-20, w), r.uniform(-10, h * 0.8)
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(r.uniform(30, 70))}" height="{f(r.uniform(16, 30))}" rx="4" fill="{r.choice(("#2E2634", "#3A3040", "#2A2230"))}" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    mx = w * 0.5
    o.append(f'<ellipse cx="{f(mx)}" cy="{f(h * 0.04)}" rx="{f(w * 0.16)}" ry="{f(h * 0.06)}" fill="{"#FFE8B0" if dawn else "#3A3A6A"}" stroke="#0D0D0F" stroke-width="3"></ellipse>')
    if stone:
        o.append(f'<ellipse cx="{f(mx)}" cy="{f(h * 0.03)}" rx="{f(w * 0.15)}" ry="{f(h * 0.05)}" fill="#5A5460" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
                 f'<circle cx="{f(mx + w * 0.06)}" cy="{f(h * 0.05)}" r="{f(max(5, h * 0.014))}" fill="#B5121B" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    if glow:
        o.append(f'<path d="M{f(mx - w * 0.12)} {f(h * 0.06)} L {f(mx + w * 0.12)} {f(h * 0.06)} L {f(mx + w * 0.26)} {f(h + 10)} L {f(mx - w * 0.26)} {f(h + 10)} Z" fill="#FFF4C2" opacity="{0.28 if dawn else 0.18}"></path>')
    o.append(f'<path d="M-10 {f(h * 0.8)} C {f(w * 0.3)} {f(h * 0.76)} {f(w * 0.7)} {f(h * 0.76)} {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#4A3A34" stroke="#0D0D0F" stroke-width="2"></path>')
    k = min(1.1, h / 520) * (1.15 if cover else 1)
    spots = [(0.16, 0.86, False), (0.84, 0.88, True), (0.3, 0.98, False), (0.7, 0.99, True), (0.06, 0.97, False)][:lions]
    for x, y, fl in spots:
        o.append(f'<g transform="translate({f(w * x)} {f(h * y)}) scale({-1 if fl else 1} 1)">{lion_lying(0, 0, k, color="#B8925A")}</g>')
    if daniel:
        s = fit(h * 0.86, h * 0.36)
        o.append(dan_fig(p, mx, h * 0.86, s, age=3, up=None if cover else [(-22, -158), (-34, -190), (-26, -222)]))
    return "".join(o)
