"""Leviticus pictograms and scenes.

Pictograms are 320 x 100 strips for kit.law cells (f(p) -> svg, p = the cell's id prefix for <defs>), on art6.GND's
indigo ground. They never show slaughter or carcasses: an offering is the whole beast beside the brass altar, then fire on
the altar. Scenes are full panels f(p, w, h, seed)."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, samuel1 as S1, ruth1 as R, numbers1 as N, judges1 as J1
from genesis import art2 as Y, art3 as Z, art10 as T
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import sun, label, man, woman, grid_bg
from exo import art as A, art8 as B8, art9 as Q
from exo.art6 import GND
from exo.art7 import ban, coins
def f(v): return f"{v:.1f}"

BRASS, BRASS_TOP, BRASS_SIDE = "#B87333", "#D8935A", "#8A5222"

# ---- small parts (local units) -------------------------------------------------------------------------------------
def altar(x, y, s=1.0, fire=True, smoke=True):
    """The altar of burnt-offering: a brass box with a horn at each corner, the fire laid on wood."""
    w, h = 60 * s, 34 * s; d = 18 * s
    o = [B8.box(x - w / 2, y, w, d, h, fill=BRASS, top=BRASS_TOP, side=BRASS_SIDE)]
    for hx, hy in ((x - w / 2, y - h), (x + w / 2, y - h), (x - w / 2 + d * 0.5, y - h - d * 0.35), (x + w / 2 + d * 0.5, y - h - d * 0.35)):
        o.append(f'<path d="M{f(hx - 3 * s)} {f(hy)} C {f(hx - 3 * s)} {f(hy - 6 * s)} {f(hx + s)} {f(hy - 10 * s)} {f(hx + 4 * s)} {f(hy - 11 * s)} C {f(hx + 2 * s)} {f(hy - 6 * s)} {f(hx + 3 * s)} {f(hy - 3 * s)} {f(hx + 3 * s)} {f(hy)} Z" fill="{BRASS_TOP}" stroke="#0D0D0F" stroke-width="1"></path>')
    if fire:
        fx, fy = x + d * 0.25, y - h - d * 0.18
        o.append(f'<path d="M{f(fx - 20 * s)} {f(fy)} L {f(fx + 20 * s)} {f(fy - 2 * s)} M{f(fx - 18 * s)} {f(fy - 4 * s)} L {f(fx + 16 * s)} {f(fy - 6 * s)}" stroke="#5A3A22" stroke-width="{f(3 * s)}"></path>'
                 + E.flame(fx - 14 * s, fy - 4 * s, 28 * s, 34 * s, 0.1))
        if smoke: o.append(f'<path d="M{f(fx)} {f(fy - 36 * s)} c {f(8 * s)} {f(-10 * s)} {f(-8 * s)} {f(-20 * s)} 0 {f(-30 * s)} c {f(8 * s)} {f(-10 * s)} {f(-6 * s)} {f(-18 * s)} {f(2 * s)} {f(-28 * s)}" fill="none" stroke="#D8D2C6" stroke-width="{f(5 * s)}" opacity="0.5" stroke-linecap="round"></path>')
    return "".join(o)

def dove(x, y, s=1.0, flip=False, color="#C8C2D6"):
    """A turtle-dove or a young pigeon, standing."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})"><path d="M-14 -6 C -12 -18 4 -22 12 -16 C 16 -22 24 -22 24 -16 L 30 -14 L 24 -12 C 22 -4 12 2 0 2 C -8 2 -18 0 -24 4 L -20 -4 Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.6"></path>'
            '<path d="M-6 -10 C 2 -14 8 -12 12 -6" fill="none" stroke="#0D0D0F" stroke-width="1" opacity="0.6"></path><circle cx="19" cy="-17" r="1.4" fill="#0D0D0F"></circle>'
            '<path d="M0 2 L -2 10 M6 2 L 6 10" stroke="#C8682E" stroke-width="1.6"></path></g>')

def goat(x, y, s=1.0, flip=False, color="#5A4A3A"):
    """A he-goat: dark coat, swept horns, a beard."""
    sx = -s if flip else s
    return (E.sheep(x, y, s, flip=flip, wool=color, face="#3A2A1E")
            + f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})"><path d="M26 -46 C 20 -60 8 -66 0 -64 M30 -46 C 28 -60 18 -70 10 -70" fill="none" stroke="#E8E2D6" stroke-width="3" stroke-linecap="round"></path>'
              '<path d="M36 -26 L 34 -16 L 40 -24 Z" fill="#3A2A1E"></path></g>')

def flour(x, y, s=1.0):
    """A heap of fine flour."""
    return f'<path d="M{f(x - 26 * s)} {f(y)} C {f(x - 16 * s)} {f(y - 22 * s)} {f(x + 16 * s)} {f(y - 22 * s)} {f(x + 26 * s)} {f(y)} Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></path>'

def jar(x, y, s=1.0, color="#C8B040"):
    """A jar of oil."""
    return (f'<path d="M{f(x - 8 * s)} {f(y - 30 * s)} L {f(x + 8 * s)} {f(y - 30 * s)} C {f(x + 18 * s)} {f(y - 16 * s)} {f(x + 14 * s)} {f(y)} {f(x)} {f(y)} C {f(x - 14 * s)} {f(y)} {f(x - 18 * s)} {f(y - 16 * s)} {f(x - 8 * s)} {f(y - 30 * s)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.6"></path>'
            f'<rect x="{f(x - 6 * s)}" y="{f(y - 36 * s)}" width="{f(12 * s)}" height="{f(6 * s)}" fill="#8A5A3E" stroke="#0D0D0F" stroke-width="1.2"></rect>')

def incense(x, y, s=1.0):
    """Frankincense: white lumps of resin in a little dish."""
    return (f'<ellipse cx="{f(x)}" cy="{f(y - 4 * s)}" rx="{f(18 * s)}" ry="{f(5 * s)}" fill="#8A5A3E" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'
            + "".join(f'<circle cx="{f(x + d * s)}" cy="{f(y - 9 * s - (abs(d) % 4))}" r="{f(4 * s)}" fill="#F8F4E0" stroke="#0D0D0F" stroke-width="1"></circle>' for d in (-10, -3, 4, 11)))

def cakes(x, y, s=1.0, n=3):
    return "".join(f'<ellipse cx="{f(x + i * 6 * s)}" cy="{f(y - i * 6 * s)}" rx="{f(20 * s)}" ry="{f(5 * s)}" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>' for i in range(n))

def pan(x, y, s=1.0, deep=False):
    """A baking-pan (flat) or a frying-pan (deep), with a handle."""
    hh = 12 if deep else 5
    return (f'<path d="M{f(x - 24 * s)} {f(y - hh * s)} L {f(x + 24 * s)} {f(y - hh * s)} L {f(x + 20 * s)} {f(y)} L {f(x - 20 * s)} {f(y)} Z" fill="#5A5A60" stroke="#0D0D0F" stroke-width="1.6"></path>'
            f'<path d="M{f(x + 24 * s)} {f(y - hh * s)} L {f(x + 42 * s)} {f(y - (hh + 6) * s)}" stroke="#3A3A40" stroke-width="{f(4 * s)}" stroke-linecap="round"></path>')

def oven(x, y, s=1.0):
    return (f'<path d="M{f(x - 22 * s)} {f(y)} C {f(x - 24 * s)} {f(y - 40 * s)} {f(x + 24 * s)} {f(y - 40 * s)} {f(x + 22 * s)} {f(y)} Z" fill="#A85A32" stroke="#0D0D0F" stroke-width="1.8"></path>'
            f'<path d="M{f(x - 8 * s)} {f(y)} C {f(x - 8 * s)} {f(y - 14 * s)} {f(x + 8 * s)} {f(y - 14 * s)} {f(x + 8 * s)} {f(y)} Z" fill="#FF8A3D" stroke="#0D0D0F" stroke-width="1.2"></path>')

def salt(x, y, s=1.0):
    return (f'<path d="M{f(x - 20 * s)} {f(y - 12 * s)} C {f(x - 20 * s)} {f(y + 2 * s)} {f(x + 20 * s)} {f(y + 2 * s)} {f(x + 20 * s)} {f(y - 12 * s)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="1.6"></path>'
            + "".join(f'<rect x="{f(x + d * s)}" y="{f(y - 18 * s - (abs(d) % 5))}" width="{f(5 * s)}" height="{f(5 * s)}" fill="#FFFFFF" stroke="#8FD0E2" stroke-width="0.8" transform="rotate(20 {f(x + d * s)} {f(y - 16 * s)})"></rect>' for d in (-14, -6, 2, 10)))

def ears(x, y, s=1.0, n=3):
    """Ears of grain parched with fire."""
    return "".join(f'<path d="M{f(x + i * 8 * s)} {f(y)} L {f(x + i * 8 * s + 4 * s)} {f(y - 40 * s)}" stroke="#8A6A3A" stroke-width="{f(2 * s)}"></path>'
                   f'<ellipse cx="{f(x + i * 8 * s + 5 * s)}" cy="{f(y - 46 * s)}" rx="{f(4 * s)}" ry="{f(10 * s)}" fill="#C8902E" stroke="#0D0D0F" stroke-width="1.2"></ellipse>' for i in range(n))

def hand_on(x, y, s=1.0):
    """A hand laid upon the head of the offering (a mark above the beast's head)."""
    return f'<path d="M{f(x)} {f(y)} l 0 -10 m -6 4 l 6 6 l 6 -6" stroke="#FFD23F" stroke-width="2.4" fill="none"></path>'

def drops(x, y, n=6, s=1.0):
    return "".join(f'<circle cx="{f(x + i * 7 * s)}" cy="{f(y + (i % 2) * 5 * s)}" r="{f(2.6 * s)}" fill="#B5121B"></circle>' for i in range(n))

def door(x, y, s=1.0):
    """The door of the tent of meeting: the screen of blue, purple and scarlet between gold pillars."""
    w, h = 40 * s, 56 * s
    o = [f'<rect x="{f(x - w / 2)}" y="{f(y - h)}" width="{f(w)}" height="{f(h)}" fill="#8A3A2A" stroke="#0D0D0F" stroke-width="1.6"></rect>']
    for i, c in enumerate((B8.BLUE, B8.PURPLE, B8.SCARLET, B8.LINEN)):
        o.append(f'<rect x="{f(x - w * 0.3 + i * w * 0.15)}" y="{f(y - h * 0.8)}" width="{f(w * 0.15)}" height="{f(h * 0.8)}" fill="{c}"></rect>')
    o.append(f'<path d="M{f(x - w * 0.32)} {f(y)} L {f(x - w * 0.32)} {f(y - h * 0.82)} M{f(x + w * 0.32)} {f(y)} L {f(x + w * 0.32)} {f(y - h * 0.82)}" stroke="#E8B830" stroke-width="{f(3 * s)}"></path>')
    return "".join(o)

def priest(p, x, y=86, s=0.38, high=False, up=None, flip=False):
    return (Q.high_priest if high else Q.son_priest)(p, x, y, s, flip=flip, up=up)

def offerer(p, x, y=86, s=0.36, up=None, flip=False, c="#5A3A22"):
    return man(p, x, y, s, c, flip=flip, up=up)

REACH = [(-22, -158), (2, -136), (26, -124)]

# ---- pictograms (f(p) -> svg in 320 x 100) ---------------------------------------------------------------------------
def pg_called(p):    return GND + door(150, 84, 1.2) + A.moses(p, 230, 86, 0.36, flip=True, up=T.POSES["raise"])
def pg_herd(p):      return GND + offerer(p, 60) + S1.cow(150, 84, 0.42, color="#5A3A22", patch="#3A2214") + altar(260, 84, 1.0)
def pg_herd_door(p): return GND + door(50, 84) + S1.cow(150, 84, 0.42, color="#5A3A22", patch="#3A2214") + offerer(p, 230, up=REACH, flip=True)
def pg_hand(p):      return GND + offerer(p, 100, up=REACH) + S1.cow(190, 84, 0.42, color="#5A3A22", patch="#3A2214") + hand_on(226, 40)
def pg_sprinkle(p):  return GND + priest(p, 90, up=REACH) + E3.basin(126, 82, 26) + drops(150, 46) + altar(250, 84, 1.0, smoke=False)
def pg_fire(p):      return GND + priest(p, 100, up=REACH) + altar(200, 84, 1.4)
def pg_burn(p):      return GND + altar(160, 84, 1.6)
def pg_flock(p):     return GND + E.sheep(80, 84, 0.42) + goat(150, 84, 0.42) + altar(250, 84, 1.0)
def pg_north(p):     return GND + E.sheep(80, 84, 0.42) + altar(200, 84, 1.0) + label(290, 30, "N ↑", B8.CY, 12) + priest(p, 260, up=REACH, flip=True)
def pg_doves(p):     return GND + dove(70, 80, 1.2) + dove(110, 80, 1.1, flip=True) + dove(150, 82, 1.0) + altar(250, 84, 1.0)
def pg_ashes(p):     return GND + altar(130, 84, 1.0) + f'<path d="M210 84 C 214 70 246 70 250 84 Z" fill="#6A6460" stroke="#0D0D0F" stroke-width="1.4"></path>' + label(230, 96, "THE PLACE OF THE ASHES · EAST", B8.CY, 7)
def pg_meal(p):      return GND + flour(80, 84, 1.3) + jar(140, 84, 1.0) + incense(200, 84, 1.0) + altar(270, 84, 0.9)
def pg_handful(p):   return GND + priest(p, 90, up=REACH) + flour(160, 84, 1.0) + altar(250, 84, 1.0)
def pg_portion(p):   return GND + flour(110, 84, 1.0) + cakes(170, 84, 1.0) + priest(p, 250, flip=True) + priest(p, 280, flip=True)
def pg_oven(p):      return GND + oven(90, 84, 1.2) + cakes(170, 84, 1.0) + cakes(240, 70, 0.8, n=2)
def pg_pans(p):      return GND + pan(90, 84, 1.2) + pan(200, 84, 1.2, deep=True) + label(100, 96, "BAKING-PAN", B8.CY, 7) + label(210, 96, "FRYING-PAN", B8.CY, 7)
def pg_bring(p):     return GND + cakes(90, 84, 1.0) + priest(p, 160, up=REACH) + altar(250, 84, 1.0)
def pg_leaven(p):    return GND + jar(120, 84, 1.0, color="#E8C88A") + jar(200, 84, 1.0, color="#E8A317") + ban(160, 50, 40) + label(120, 96, "LEAVEN", B8.CY, 7) + label(200, 96, "HONEY", B8.CY, 7)
def pg_salt(p):      return GND + flour(110, 84, 1.0) + salt(190, 84, 1.3) + label(190, 96, "THE SALT OF THE COVENANT", B8.CY, 7)
def pg_ears(p):      return GND + ears(80, 84, 1.0, n=4) + E.blaze(150, 84, 26, 30, 3, n=4) + jar(220, 84, 0.9) + incense(270, 84, 0.9)
def pg_peace_herd(p): return GND + S1.cow(90, 84, 0.42, color="#8A5A30", patch="#5A3A22") + S1.cow(160, 84, 0.38, color="#C9A27A") + altar(260, 84, 1.0)
def pg_fat(p):       return GND + altar(110, 84, 1.3) + label(230, 50, "ALL THE FAT IS JEHOVAH'S", "#FFD23F", 9)
def pg_lamb(p):      return GND + E3.lamb(110, 84, 0.5) + offerer(p, 190, up=REACH, flip=True) + altar(260, 84, 0.9)
def pg_goat(p):      return GND + goat(110, 84, 0.46) + offerer(p, 190, up=REACH, flip=True) + altar(260, 84, 0.9)
def pg_no_blood(p):  return GND + E3.basin(130, 70, 36) + jar(200, 84, 1.0, color="#E8E2D6") + ban(165, 50, 42)
def pg_statute(p):   return GND + "".join(A.black_tent(40 + i * 60, 84, 46, 30) for i in range(5)) + label(160, 22, "A PERPETUAL STATUTE · IN ALL YOUR DWELLINGS", "#FFD23F", 8)

# ---- scenes ------------------------------------------------------------------------------------------------------
def tent_call(p, w, h, seed):
    """Jehovah called unto Moses out of the tent of meeting: the tabernacle in its court, the cloud above, Moses before the door."""
    b = h * 0.9
    return (mk.defs(p, *A_ALL) + V.rays(w * 0.6, h * 0.24, 30, 20, max(w, h), color="#FFF4C2", op=0.25) + ground(w, h, h * 0.62, "#8A6A4A", dy=0)
            + E3.pillar_cloud(w * 0.6, h * 0.5, -20, w * 0.07, seed) + V.tabernacle(w * 0.6, h * 0.8, w * 0.6, uid=p + "tn")
            + A.moses(p, w * 0.22, b, fit(b, h * 0.44), up=T.POSES["raise"]))

def altar_scene(p, w, h, seed, beast="bullock", priests=2):
    """The court before the tent: the brass altar with its fire, an offerer with his beast, Aaron's sons in white."""
    b = h * 0.9
    o = [mk.defs(p, *A_ALL), ground(w, h, h * 0.6, "#C8B080", dy=0), V.tabernacle(w * 0.78, h * 0.62, w * 0.36, uid=p + "tn"), altar(w * 0.5, b - 4, min(2.6, h / 120))]
    s = fit(b, h * 0.46)
    o.append(offerer(p, w * 0.16, b, s, up=REACH))
    o.append({"bullock": S1.cow(w * 0.3, b, s * 1.1, color="#5A3A22", patch="#3A2214"), "sheep": E.sheep(w * 0.28, b, s * 1.2), "goat": goat(w * 0.28, b, s * 1.2),
              "doves": dove(w * 0.28, b - 10, s * 3)}[beast])
    for i in range(priests):
        o.append(priest(p, w * (0.66 + i * 0.08), b, s, flip=True, up=REACH if i == 0 else None))
    return "".join(o)

A_ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")

# ---- Leviticus 4–5: the sin-offering and the trespass-offering --------------------------------------------------
def veil(x, y, s=1.0):
    """The veil of the sanctuary between two gold pillars."""
    w, h = 70 * s, 70 * s
    return (f'<rect x="{f(x - w / 2)}" y="{f(y - h)}" width="{f(w)}" height="{f(h)}" fill="{B8.BLUE}" stroke="#0D0D0F" stroke-width="1.6"></rect>'
            + "".join(f'<rect x="{f(x - w / 2 + i * w / 4)}" y="{f(y - h)}" width="{f(w / 8)}" height="{f(h)}" fill="{c}"></rect>' for i, c in enumerate((B8.PURPLE, B8.SCARLET, B8.LINEN, B8.PURPLE)))
            + f'<path d="M{f(x - w / 2)} {f(y)} L {f(x - w / 2)} {f(y - h - 4)} M{f(x + w / 2)} {f(y)} L {f(x + w / 2)} {f(y - h - 4)}" stroke="#E8B830" stroke-width="{f(4 * s)}"></path>')

def incense_altar(x, y, s=1.0):
    w, h, d = 16 * s, 34 * s, 10 * s
    return (B8.box(x - w / 2, y, w, d, h, fill=B8.GOLD, top="#FFD23F", side="#C8981E")
            + f'<path d="M{f(x)} {f(y - h - 6 * s)} c {f(6 * s)} {f(-8 * s)} {f(-6 * s)} {f(-14 * s)} 0 {f(-22 * s)}" fill="none" stroke="#E8E2D6" stroke-width="{f(3 * s)}" opacity="0.7"></path>')

def seven(x, y):
    return "".join(f'<circle cx="{f(x + i * 9)}" cy="{f(y)}" r="3" fill="#B5121B"></circle>' for i in range(7)) + label(x + 27, y + 16, "SEVEN TIMES", B8.CY, 7)

def crowned(p, x, c="#7A2A3A"):
    return T.figure(p, ("man", c), x, 86, 0.36) + f'<g transform="translate({f(x)} 86) scale(0.36)">{Z.CROWN}</g>'

def pg_unwitting(p):  return GND + A.moses(p, 70, 86, 0.36, up=T.POSES["raise"]) + "".join(man(p, 140 + i * 34, 86, 0.32, A.HEBREW[i], flip=True) for i in range(5))
def pg_priest_sin(p): return GND + Q.high_priest(p, 70, 86, 0.36) + S1.cow(160, 84, 0.42, color="#3A2214", patch="#1A1210") + door(270, 84)
def pg_veil(p):       return GND + priest(p, 70, high=True, up=REACH) + seven(110, 40) + veil(210, 84, 1.0) + incense_altar(270, 84, 1.2)
def pg_without(p):    return (GND + "".join(A.black_tent(30 + i * 40, 84, 34, 24) for i in range(3)) + '<path d="M150 20 L 150 96" stroke="#FFD23F" stroke-width="2" stroke-dasharray="5 4"></path>'
                              + E.blaze(240, 84, 60, 50, 7, n=6) + label(232, 22, "WITHOUT THE CAMP", B8.CY, 7) + label(232, 32, "A CLEAN PLACE", B8.CY, 7))
def pg_congregation(p): return GND + "".join(A.elder(c, i)(p, 40 + i * 32, 86, 0.32) for i, c in enumerate(A.HEBREW[:4])) + S1.cow(220, 84, 0.42, color="#3A2214", patch="#1A1210") + hand_on(250, 40)
def pg_ruler(p):      return GND + crowned(p, 80) + goat(170, 84, 0.46) + altar(260, 84, 1.0)
def pg_common(p):     return GND + offerer(p, 70) + goat(150, 84, 0.44, color="#8A7A6A") + altar(250, 84, 1.0)
def pg_horns(p):      return GND + priest(p, 100, up=REACH) + altar(200, 84, 1.4, smoke=False) + '<circle cx="164" cy="34" r="4" fill="#B5121B"></circle><circle cx="236" cy="34" r="4" fill="#B5121B"></circle>'
def pg_she_lamb(p):   return GND + offerer(p, 70) + E3.lamb(150, 84, 0.5) + altar(250, 84, 1.0)
def pg_witness(p):    return GND + A.elder("#5A6E8A", 2)(p, 70, 86, 0.36) + A.elder("#6A4A5A", 4)(p, 110, 86, 0.36) + man(p, 220, 86, 0.36, "#5A3A22", flip=True)
def pg_unclean(p):    return GND + man(p, 100, 86, 0.36, "#5A3A22", up=REACH) + '<path d="M150 84 C 160 70 200 70 214 84 Z" fill="#3A3A3E" stroke="#0D0D0F" stroke-width="1.4"></path>' + label(180, 96, "AN UNCLEAN THING", B8.CY, 7)
def pg_oath(p):       return GND + man(p, 140, 86, 0.38, "#5A3A22", up=T.POSES["raise"]) + label(230, 40, "RASHLY · WITH AN OATH", "#FFD23F", 8)
def pg_confess(p):    return GND + E.kneel(120, 86, 0.36, color="#5A3A22", skin="#8A5A3E") + priest(p, 200, flip=True) + E3.lamb(260, 84, 0.4)
def pg_two_doves(p):  return GND + offerer(p, 60) + dove(130, 80, 1.2) + dove(170, 80, 1.2, flip=True) + altar(260, 84, 1.0)
def pg_ephah(p):      return (GND + offerer(p, 60) + flour(130, 84, 1.2) + label(130, 96, "1/10 EPHAH OF FINE FLOUR", B8.CY, 7)
                              + jar(262, 72, 0.6) + ban(262, 54, 28) + label(262, 96, "NO OIL · NO FRANKINCENSE", B8.CY, 6.5))
def pg_ram(p):        return GND + offerer(p, 60) + goat(150, 84, 0.46, color="#E8E2D6") + coins(220, 60, 5)
def pg_fifth(p):      return GND + coins(60, 70, 10) + label(150, 56, "+", "#FFD23F", 22) + coins(190, 70, 2) + label(205, 96, "THE FIFTH PART", B8.CY, 8)
def pg_guilty(p):     return GND + E.kneel(120, 86, 0.36, color="#5A3A22", skin="#8A5A3E") + altar(230, 84, 1.0)
