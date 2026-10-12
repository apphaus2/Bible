"""New drawings for Genesis chapter 7 (Genesis 25:19–27:46): Rebekah inquiring of Jehovah, Isaac in Gerar, the wells
Esek, Sitnah and Rehoboth, the oath with Abimelech, the blind father, the kids of the goats, the stolen blessing."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus4 as E4, exodus5 as V, joshua1 as J, judges1 as G1, judges2 as S, samuel4 as A4, numbers1 as N, ruth1 as R
from faces_ex import F
from genesis import art2 as Y, art3 as Z, art4 as Q, art5 as K, art6 as R6
from genesis.art2 import fit, ground, hills, birds, city, SKIN, FUR
from genesis.art3 import sun, label, man, woman, grid_bg, node, route, STAFF, HOLD_STAFF, GREY_BEARD
from genesis.art5 import well, abimelech
from genesis.art6 import rebekah, isaac, REBEKAH_ROBE, ISAAC_ROBE
def f(v): return f"{v:.1f}"

# ---- faces ----------------------------------------------------------------------------------------------
JACOB = F("adam", skin="#D9A27A", shadow="#A8684A", hair="#2A1A10", hl="#5A4A3E", light="#9FB8FF")
JACOB_AFRAID = F("adam", skin="#C98E66", shadow="#5A3A4A", hair="#2A1A10", hl="#5A4A3E", brow="sorrow", sweat=True, light="#FF8A3D")
ESAU = F("adam", skin="#C47A5A", shadow="#8A4A32", hair="#B5421E", hl="#E06A3A", stubble="#B5421E", light="#FFC14D")
ESAU_FAINT = F("adam", skin="#C47A5A", shadow="#8A4A32", hair="#B5421E", hl="#E06A3A", stubble="#B5421E", brow="sorrow", sweat=True, light="#FF6A2A")
ESAU_CRY = F("adam", skin="#C47A5A", shadow="#6A3A3A", hair="#B5421E", hl="#E06A3A", stubble="#B5421E", brow="sorrow", tear=True)
ESAU_HATE = F("adam", skin="#B9684A", shadow="#4A1A16", hair="#B5421E", hl="#E06A3A", stubble="#B5421E", brow="scowl", light="#D7261E")
ISAAC_OLD = F("adam", skin="#D9A27A", shadow="#9A6A4A", hair="#E8E2D6", hl="#B8B2A6", beard=True, blind=True, light="#FFC14D")
ISAAC_TREMBLE = F("adam", skin="#C9A28A", shadow="#5A4A5A", hair="#E8E2D6", hl="#B8B2A6", beard=True, blind=True, brow="sorrow", sweat=True, light="#9A8AFF")
ISAAC_GERAR = R6.ISAAC
REBEKAH_ELDER = F("eve", skin="#DDA684", shadow="#9A6A5A", hair="#5A4A3E", scarf="#2E7A4A", light="#FFC14D")
REBEKAH_URGENT = F("eve", skin="#DDA684", shadow="#6A3A3A", hair="#5A4A3E", scarf="#2E7A4A", brow="scowl", light="#FF6A4A")

# ---- people ---------------------------------------------------------------------------------------------
ESAU_TUNIC, JACOB_ROBE = "#B5421E", "#5A6E8A"
BOW = ('<path d="M30 -236 C 60 -206 60 -126 30 -96" fill="none" stroke="#0D0D0F" stroke-width="7" stroke-linecap="round"></path>'
       '<path d="M30 -236 C 60 -206 60 -126 30 -96" fill="none" stroke="#8A5A30" stroke-width="4" stroke-linecap="round"></path>'
       '<path d="M30 -236 L 30 -96" stroke="#F3EFE6" stroke-width="1.2"></path>')
QUIVER = '<path d="M-18 -190 L -30 -120 L -20 -116 L -8 -186 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="1.6"></path>'

def esau(p, x, y, s, flip=False, up=None, bow=True):
    return mk.person(p, round(x), round(y), round(s, 3), body="#8A4A2E", cloth=ESAU_TUNIC, kind="Tunic", sw=3, flip=flip, up=up,
                     pre=QUIVER if bow else "", extra=FUR + (BOW if bow else ""))

def jacob(p, x, y, s, flip=False, up=None, skins=False):
    gloves = ('<path d="M-30 -110 C -34 -96 -30 -84 -24 -82 C -18 -84 -18 -96 -22 -110 Z M22 -110 C 18 -96 20 -84 26 -82 C 32 -84 34 -96 30 -110 Z" fill="#3A2A22"></path>'
              '<path d="M-14 -176 C -4 -170 4 -170 14 -176 L 12 -164 C 4 -160 -4 -160 -12 -164 Z" fill="#3A2A22"></path>') if skins else ""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=ESAU_TUNIC if skins else JACOB_ROBE, kind="Tunic" if skins else "Robe",
                     sw=3, flip=flip, up=up, extra=gloves)

def old_isaac(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=ISAAC_ROBE, sw=3, flip=flip, up=up, extra=Y.WHITE_BEARD)

def couch(x, y, w):
    return (f'<rect x="{f(x - w / 2)}" y="{f(y - 28)}" width="{f(w)}" height="28" rx="6" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2.4"></rect>'
            f'<rect x="{f(x - w / 2 - 6)}" y="{f(y - 46)}" width="22" height="46" rx="4" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></rect>')

def tent_inside(w, h, glow=0.3):
    """Inside a goat-hair tent: dark striped walls, a lamp-glow in the middle."""
    stripes = "".join(f'<path d="M{x} -10 L {x - 30} {f(h + 10)}" stroke="#2A1408" stroke-width="10"></path>' for x in range(0, int(w) + 60, 52))
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2214"></rect>' + stripes
            + f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.5)}" r="{f(h * 0.6)}" fill="#FFC14D" opacity="{glow}"></circle>')

def bowl(x, y, s=1.0, steam=True):
    st = "".join(f'<path d="M{f(x + dx * s)} {f(y - 20 * s)} c -8 -14 8 -24 0 -40" fill="none" stroke="#F3EFE6" stroke-width="{f(2.4 * s)}" opacity="0.6"></path>' for dx in (-14, 0, 14)) if steam else ""
    return (f'<path d="M{f(x - 34 * s)} {f(y - 18 * s)} C {f(x - 30 * s)} {f(y + 6 * s)} {f(x + 30 * s)} {f(y + 6 * s)} {f(x + 34 * s)} {f(y - 18 * s)} Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>'
            f'<ellipse cx="{f(x)}" cy="{f(y - 18 * s)}" rx="{f(34 * s)}" ry="{f(8 * s)}" fill="#B5421E" stroke="#0D0D0F" stroke-width="1.6"></ellipse>' + st)

def goat(x, y, s=1.0, flip=False):
    return E.sheep(x, y, s, flip=flip, wool="#3A2A22", face="#2A1A10")

# ---- Genesis 25:19–34 -----------------------------------------------------------------------------------
def inquire(p, w, h, seed):
    """She went to inquire of Jehovah: Rebekah kneeling alone on a hill under the stars."""
    base = h * 0.86
    return (mk.stars(110, w, h * 0.7, seed) + V.rays(w * 0.6, -30, 30, 30, h * 1.4, color="#FFF4C2", op=0.2)
            + hills(w, h, base, seed, color="#12102A", amp=8) + E.kneel(w * 0.4, base + 2, round(h / 380, 3), color=REBEKAH_ROBE, skin=SKIN))

def two_nations(w, h, seed):
    """Two nations are in thy womb: two streams of light, one red and one blue, rising and parting."""
    o = [mk.stars(70, w, h, seed)]
    for c, d in [("#D7261E", -1), ("#5A8AD8", 1)]:
        pts = [(w * 0.5 + d * w * 0.04 * t * t * 9, h * (0.96 - 0.86 * t)) for t in [i / 10 for i in range(11)]]
        dd = "M" + " L ".join(f"{f(x)} {f(y)}" for x, y in pts)
        o.append(f'<path d="{dd}" fill="none" stroke="{c}" stroke-width="16" opacity="0.4" stroke-linecap="round"></path><path d="{dd}" fill="none" stroke="{c}" stroke-width="4" stroke-linecap="round"></path>')
    return "".join(o)

def hunter_and_tent(p, w, h, seed):
    """Esau a man of the field with his bow; Jacob a quiet man at the tent door."""
    base = h * 0.88
    return (sun(w * 0.86, h * 0.2, 14, op=0.25) + ground(w, h, base, "#9AAA5A", dy=0) + J.oak(w * 0.08, base, 0.5, seed=seed)
            + esau(p, w * 0.24, base, fit(base, h * 0.36)) + G1.tent_big(w * 0.74, base, w * 0.36, h * 0.6, color="#3A2214", glow="#5A2A12")
            + jacob(p, w * 0.56, base, fit(base, h * 0.38), flip=True))

def pottage(w, h, seed):
    """Jacob boiled pottage: the pot on the fire in the tent, red lentils, steam."""
    base = h * 0.84
    return (tent_inside(w, h, 0.25) + ground(w, h, base, "#2A1408", dy=0) + E.blaze(w * 0.5, base + 4, 60, 40, seed)
            + f'<path d="M{f(w * 0.3)} {f(base - 60)} C {f(w * 0.3)} {f(base)} {f(w * 0.7)} {f(base)} {f(w * 0.7)} {f(base - 60)} Z" fill="#3A3A44" stroke="#0D0D0F" stroke-width="2.6"></path>'
            + f'<ellipse cx="{f(w * 0.5)}" cy="{f(base - 60)}" rx="{f(w * 0.2)}" ry="12" fill="#B5421E" stroke="#0D0D0F" stroke-width="2"></ellipse>'
            + "".join(f'<path d="M{f(w * (0.42 + i * 0.08))} {f(base - 70)} c -10 -20 10 -34 0 -60" fill="none" stroke="#F3EFE6" stroke-width="3" opacity="0.6"></path>' for i in range(3)))

def sold(p, w, h, seed):
    """Swear to me first; and he sware unto him: the brothers' hands clasped over the bowl."""
    cx, cy = w * 0.5, h * 0.5
    arm = lambda x0, x1, c: (f'<path d="M{f(x0)} {f(cy + 30)} L {f(x1)} {f(cy)}" stroke="#0D0D0F" stroke-width="34" stroke-linecap="round"></path>'
                             f'<path d="M{f(x0)} {f(cy + 30)} L {f(x1)} {f(cy)}" stroke="{c}" stroke-width="28" stroke-linecap="round"></path>')
    return (tent_inside(w, h, 0.3) + bowl(cx, h * 0.92, 2.2) + arm(-20, cx - 10, "#C47A5A") + arm(w + 20, cx + 10, "#D9A27A")
            + f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="30" ry="22" fill="#CF9070" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
            + "".join(f'<path d="M{f(cx - 20 + i * 10)} {f(cy - 14)} l 4 26" stroke="#0D0D0F" stroke-width="1.6"></path>' for i in range(4))
            + "".join(f'<path d="M{f(x)} {f(cy + 34 + k * 4)} l 8 -6" stroke="#8A3A1E" stroke-width="2"></path>' for x in range(30, int(cx - 30), 16) for k in (0, 1)))

def went_his_way(p, w, h, seed):
    """He did eat and drink, and rose up, and went his way: Esau walking off into the field, the empty bowl behind."""
    base = h * 0.86
    return (sun(w * 0.86, base - 10, h * 0.18, color="#FF8A3D", op=0.3) + ground(w, h, base, "#8A9A5A", dy=0)
            + bowl(w * 0.16, base + 10, 1.2, steam=False) + esau(p, w * 0.66, base, fit(base, h * 0.4)))

# ---- Genesis 26 -----------------------------------------------------------------------------------------
def at_window(p, w, h, seed):
    """Abimelech looked out at a window, and saw Isaac with Rebekah his wife: below, the two walk close, his arm about her."""
    base = h * 0.9; s = fit(base, h * 0.5)
    arm = [(-22, -158), (4, -140), (28, -132)]
    return (sun(w * 0.86, h * 0.2, 14, op=0.25) + ground(w, h, base, "#C8A06A", dy=0)
            + f'<rect x="-10" y="-10" width="{f(w * 0.36)}" height="{f(base + 10)}" fill="#B59A7A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
            + f'<path d="M{f(w * 0.08)} {f(h * 0.4)} L {f(w * 0.08)} {f(h * 0.14)} C {f(w * 0.08)} {f(h * 0.04)} {f(w * 0.24)} {f(h * 0.04)} {f(w * 0.24)} {f(h * 0.14)} L {f(w * 0.24)} {f(h * 0.4)} Z" fill="#12090A" stroke="#0D0D0F" stroke-width="2"></path>'
            + mk.face(K.ABIMELECH, w * 0.06, h * 0.06, h / 1200)
            + isaac(p, w * 0.58, base, s, up=arm) + rebekah(p, w * 0.68, base, s * 0.95, flip=True))

def hundredfold(p, w, h, seed):
    """Isaac sowed in that land, and found in the same year a hundredfold."""
    base = h * 0.86
    return (sun(w * 0.8, h * 0.2, 18, color="#FFE680", op=0.35) + ground(w, h, base, "#C8A06A", dy=0)
            + S.grain(-10, w + 10, base + 6, h * 0.4, seed) + isaac(p, w * 0.2, base + 10, fit(base, h * 0.34)))

def wells_stopped(p, w, h, seed):
    """The wells the Philistines had stopped, and filled with earth: a well-head heaped with dirt, men with baskets."""
    base = h * 0.86
    heap = f'<path d="M{f(w * 0.36)} {f(base - 14)} C {f(w * 0.4)} {f(base - 60)} {f(w * 0.56)} {f(base - 60)} {f(w * 0.62)} {f(base - 14)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>'
    return (ground(w, h, base, "#C8A06A", dy=0) + well(w * 0.5, base, h / 300, full=False) + heap
            + S.philistines(p, 4, w * 0.66, w * 0.96, base - 6, base + 4, seed, 0.26, 0.32, spear=False))

def digging(p, w, h, seed, xs=(0.24, 0.76), well_x=0.5, top=0.56):
    """Isaac's servants digged in the valley, and found a well of springing water."""
    base = h * 0.86; o = [ground(w, h, base - 20, "#B5A06A", dy=0)]
    o.append(f'<ellipse cx="{f(w * well_x)}" cy="{f(base)}" rx="{f(w * 0.14)}" ry="{f(h * 0.06)}" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    o.append(V.rays(w * well_x, base - 6, 16, 6, h * 0.3, color="#CFEFFF", op=0.6))
    spade = '<path d="M14 -150 L 40 -60" stroke="#5A3A22" stroke-width="5"></path><path d="M34 -64 L 50 -58 L 44 -40 L 30 -46 Z" fill="#8A8478" stroke="#0D0D0F" stroke-width="1.4"></path>'
    for x, fl in zip(xs, (False, True)):
        o.append(man(p, w * x, base, fit(base, h * top), "#5A3A22", flip=fl, up=[(-22, -158), (-6, -140), (14, -150)], extra=spade))
    return "".join(o)

def strife_wells(w, h, seed):
    """Esek, Sitnah, Rehoboth: three wells on the map; strife at the first two, room at the third."""
    o = [grid_bg(w, h, color="#3A2A1E", bg="#1A120A")]
    pts = [("ESEK", 0.18, 0.66, "CONTENTION", "#D7261E"), ("SITNAH", 0.46, 0.4, "ENMITY", "#D7261E"), ("REHOBOTH", 0.8, 0.62, "ROOM", "#9CCB5E")]
    o.append(route([(w * x, h * y) for _, x, y, _, _ in pts], color="#C8A06A", sw=2.4))
    for nm, x, y, tag, c in pts:
        o.append(f'<circle cx="{f(w * x)}" cy="{f(h * y)}" r="16" fill="#2C9DB8" stroke="{c}" stroke-width="3"></circle>'
                 + label(w * x, h * y - 24, nm, c, 12) + label(w * x, h * y + 34, tag, c, 8.5))
    return "".join(o)

def night_altar(p, w, h, seed):
    """At Beer-sheba: an altar, Isaac's tent pitched, and the servants digging a well, under the stars."""
    base = h * 0.86
    return (mk.stars(80, w, h * 0.6, seed) + V.rays(w * 0.4, -30, 30, 30, h * 1.4, color="#FFF4C2", op=0.2) + ground(w, h, base, "#1A1430", dy=0)
            + A4.altar(w * 0.36, base, round(h / 420, 3), seed=seed) + E4.tent(w * 0.9, base, w * 0.14, h * 0.24, color="#2A1A14")
            + isaac(p, w * 0.7, base + 2, fit(base, h * 0.5), up=[(-22, -158), (-30, -196), (-36, -232)]))

def three_visitors(p, w, h, seed):
    """Abimelech, Ahuzzath his friend, and Phicol the captain of his host come from Gerar to Isaac."""
    base = h * 0.88; s = fit(base, h * 0.42)
    spear = '<path d="M14 -150 L 34 -270" stroke="#3A2214" stroke-width="4"></path><path d="M30 -270 L 38 -288 L 40 -268 Z" fill="#A8B0BA" stroke="#0D0D0F" stroke-width="1.2"></path>'
    return (sun(w * 0.5, h * 0.2, 14, op=0.25) + ground(w, h, base, "#C8A06A", dy=0) + E4.tent(w * 0.1, base, w * 0.14, h * 0.24)
            + isaac(p, w * 0.26, base, s) + abimelech(p, w * 0.6, base, s, flip=True) + man(p, w * 0.72, base, s, "#7A3BA8", flip=True, kind="Robe")
            + man(p, w * 0.84, base, s, "#3A5A8A", flip=True, extra=spear))

def feast_oath(p, w, h, seed):
    """He made them a feast, and they did eat and drink; and in the morning they sware one to another."""
    base = h * 0.88
    return (sun(w * 0.9, base - 10, h * 0.14, color="#FFC14D", op=0.3) + ground(w, h, base, "#C8A06A", dy=0)
            + f'<rect x="{f(w * 0.3)}" y="{f(base - 40)}" width="{f(w * 0.4)}" height="10" fill="#C2456A" stroke="#0D0D0F" stroke-width="2"></rect>'
            + "".join(f'<ellipse cx="{f(w * (0.34 + i * 0.08))}" cy="{f(base - 44)}" rx="12" ry="5" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>' for i in range(5))
            + E.kneel(w * 0.24, base, round(h / 520, 3), color=ISAAC_ROBE, skin=SKIN) + E.kneel(w * 0.76, base, round(h / 520, 3), color="#1F5FAD", skin=SKIN, flip=True)
            + E.kneel(w * 0.86, base, round(h / 520, 3), color="#7A3BA8", skin=SKIN, flip=True))

def hittite_wives(p, w, h, seed):
    """Esau took to wife Judith and Basemath, Hittites; and they were a grief of mind unto Isaac and Rebekah."""
    base = h * 0.88; s = fit(base, h * 0.42)
    return (ground(w, h, base, "#B59A7A", dy=0) + woman(p, w * 0.28, base, s * 0.95, "#C2A23A") + esau(p, w * 0.42, base, s, bow=False)
            + woman(p, w * 0.56, base, s * 0.95, "#D8803A", flip=True) + label(w * 0.28, base + 18, "JUDITH", "#12113A", 9) + label(w * 0.56, base + 18, "BASEMATH", "#12113A", 9)
            + isaac(p, w * 0.84, base, s * 0.98, flip=True) + rebekah(p, w * 0.94, base, s * 0.92, flip=True))

# ---- Genesis 27 -----------------------------------------------------------------------------------------
def father_calls(p, w, h, seed):
    """Isaac on his couch in the tent calls Esau; Esau stands before him with his bow."""
    base = h * 0.88
    return (tent_inside(w, h, 0.25) + ground(w, h, base, "#2A1408", dy=0) + couch(w * 0.3, base, w * 0.34)
            + E.kneel(w * 0.3, base - 24, round(h / 560, 3), color=ISAAC_ROBE, skin=SKIN) + esau(p, w * 0.7, base, fit(base, h * 0.36), flip=True))

def overheard(p, w, h, seed):
    """Rebekah heard when Isaac spake to Esau: she listens behind the tent curtain; Esau goes out to the field."""
    base = h * 0.88
    return (sun(w * 0.86, h * 0.24, 16, op=0.3) + ground(w, h, base, "#9AAA5A", dy=0) + G1.tent_big(w * 0.3, base, w * 0.56, h * 0.7, color="#3A2214", glow="#5A2A12")
            + rebekah(p, w * 0.08, base, fit(base, h * 0.36)) + esau(p, w * 0.82, base, fit(base, h * 0.5), flip=False))

def two_kids(p, w, h, seed):
    """Fetch me from thence two good kids of the goats."""
    base = h * 0.86
    return (ground(w, h, base - 10, "#9AAA5A", dy=0) + Z.flock(w * 0.5, w * 0.98, base - 6, base + 20, 8, seed, cows=0.0, smin=0.2, smax=0.28)
            + goat(w * 0.64, base + 10, 1.0) + goat(w * 0.82, base + 14, 0.94, flip=True))

def dressing(p, w, h, seed):
    """Rebekah put Esau's goodly garments on Jacob, and the skins of the kids upon his hands and the smooth of his neck."""
    base = h * 0.88; s = fit(base, h * 0.32)
    return (tent_inside(w, h, 0.3) + ground(w, h, base, "#2A1408", dy=0)
            + rebekah(p, w * 0.3, base, s * 0.95, up=[(-22, -158), (4, -150), (30, -156)]) + jacob(p, w * 0.5, base, s, skins=True, flip=True)
            + f'<path d="M{f(w * 0.7)} {f(base)} C {f(w * 0.72)} {f(base - 30)} {f(w * 0.84)} {f(base - 30)} {f(w * 0.86)} {f(base)} Z" fill="#3A2A22" stroke="#0D0D0F" stroke-width="2"></path>'
            + bowl(w * 0.9, base + 4, 1.0))

def kiss(p, w, h, seed):
    """Come near now, and kiss me, my son: the son bending over the old man on his couch."""
    base = h * 0.88; s = fit(base, h * 0.3)
    return (tent_inside(w, h, 0.32) + ground(w, h, base, "#2A1408", dy=0) + couch(w * 0.4, base, w * 0.4)
            + E.kneel(w * 0.4, base - 24, round(h / 480, 3), color=ISAAC_ROBE, skin=SKIN)
            + jacob(p, w * 0.64, base, s, skins=True, flip=True, up=[(-22, -158), (-40, -140), (-58, -126)]))

def blessed_field(w, h, seed):
    """The smell of a field which Jehovah hath blessed; the dew of heaven, the fatness of the earth, grain and new wine."""
    base = h * 0.8; r = random.Random(seed)
    return (sun(w * 0.7, h * 0.24, 20, color="#FFE680", op=0.4) + ground(w, h, base, "#5E8F26", dy=0) + S.grain(-10, w * 0.6, base + 6, h * 0.36, seed)
            + "".join(N.grapes(w * x, base - h * 0.1, 0.4, seed=int(x * 10)) for x in (0.72, 0.84, 0.94))
            + "".join(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(h * 0.1, base))}" r="{f(r.uniform(1.4, 3))}" fill="#CFEFFF"></circle>' for _ in range(40)))

def bows_down(p, w, h, seed):
    """Let peoples serve thee, and nations bow down to thee: rows of figures bowing toward one standing in light."""
    base = h * 0.88; r = random.Random(seed)
    o = [V.rays(w * 0.16, base - h * 0.3, 30, 30, w, color="#FFF4C2", op=0.35), ground(w, h, base, "#8A6A4A", dy=0), jacob(p, w * 0.16, base, fit(base, h * 0.3))]
    for row, (dy, k, n) in enumerate([(h * 0.12, 900, 7), (0, 620, 5)]):     # back row first, smaller
        for i in range(n):
            o.append(E.kneel(w * (0.34 + i * 0.6 / n) + row * 20, base - dy, round(h / k, 3),
                             color=r.choice(["#5A3A22", "#3A2214", "#8A6A4A", "#B5421E"]), skin=SKIN, flip=True))
    return "".join(o)

def came_in(p, w, h, seed):
    """Jacob scarce gone out from the presence of Isaac, Esau came in from his hunting with venison on his shoulder."""
    base = h * 0.88; s = fit(base, h * 0.4)
    deer = '<path d="M-30 -170 C -10 -190 30 -190 40 -170 L 34 -150 L -24 -152 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>'
    return (sun(w * 0.86, base - 20, h * 0.18, color="#FF8A3D", op=0.3) + ground(w, h, base, "#9AAA5A", dy=0)
            + G1.tent_big(w * 0.5, base, w * 0.3, h * 0.6, color="#3A2214", glow="#5A2A12")
            + jacob(p, w * 0.14, base, s * 0.9, skins=True) + esau(p, w * 0.82, base, s, flip=True).replace("</g>", deer + "</g>", 1))

def trembling(w, h, seed):
    """Isaac trembled very exceedingly: shaking lines around the couch in the dark tent."""
    return (tent_inside(w, h, 0.15) + mk.speed(w * 0.5, h * 0.5, 50, h * 0.3, w, seed, color="#9A8AFF", sw=1.6, op=0.5))

def flee_road(p, w, h, seed):
    """Flee thou to Laban my brother to Haran: a road north out of Beer-sheba at dusk."""
    return R6.to_mesopotamia(w, h, seed).replace("HEBRON", "BEER-SHEBA").replace("CITY OF NAHOR", "HARAN")
