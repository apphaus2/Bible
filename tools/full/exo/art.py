"""New drawings for Exodus chapter 1 (Exodus 1–4), and the Exodus cast for distant scenes.

Each cast function has the signature of genesis.art10.figure's callables, f(p, x, y, s, flip=False, up=None), so it can
go straight into T.stage(...)'s cast list. Faces follow the Exodus character guide in CLAUDE.md."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3, exodus4 as E4, exodus5 as V, numbers1 as N, ruth1 as R, samuel2 as A2, egypt as EG
import exodus5
from faces_ex import F
from genesis import art2 as Y, art3 as Z, art10 as T
from genesis.art2 import fit, ground, hills, city, SKIN
from genesis.art3 import sun, label, man, woman, node, grid_bg, HOLD_STAFF, STAFF, GREY_BEARD
from genesis.art2 import WHITE_BEARD
def f(v): return f"{v:.1f}"

# ---- faces ------------------------------------------------------------------------------------------------
_T = exodus5.tokens()
def tok(name): return _T[f"__FACE_{name}__"]
MOSES, MOSES_FIRE, MOSES_AFRAID, MOSES_STERN, MOSES_CALM = tok("MOSES"), tok("MOSES_FIRE"), tok("MOSES_AFRAID"), tok("MOSES_STERN"), tok("MOSES_CALM")
MOSES_PRINCE, MOSES_ANGRY = tok("MOSES_PRINCE"), tok("MOSES_ANGRY")
AARON, AARON_FIRE = tok("AARON"), tok("AARON_FIRE")
PRINCESS, MIRIAM, JOCHEBED = tok("PRINCESS"), tok("MIRIAM"), tok("JOCHEBED")
# a woven hem along the front edge of a headscarf, so a warm-coloured scarf reads as cloth rather than hair
HEM = ('\n<path d="M238 106 C 220 108 202 112 184 122 C 166 132 154 152 150 182 C 146 214 152 300 158 392" fill="none" stroke="#0D0D0F" stroke-width="7"></path>'
       '<path d="M238 106 C 220 108 202 112 184 122 C 166 132 154 152 150 182 C 146 214 152 300 158 392" fill="none" stroke="#E8B830" stroke-width="4" stroke-dasharray="7 4"></path>')
ZIPPORAH = F("eve", skin="#C98E66", shadow="#8A5A3E", hair="#1A1210", scarf="#9A2A2E", light="#FFC14D") + HEM
PHARAOH, TASKMASTER, SLAVE, HEBREW_ANGRY = tok("PHARAOH_NEW"), tok("TASKMASTER"), tok("SLAVE"), tok("HEBREW_ANGRY")
PHARAOH_FEAR = tok("PHARAOH_FEAR")
SHIPHRAH = F("eve", skin="#C99A84", shadow="#6A4A3A", hair="#3A2A1E", scarf="#2A5A6A", light="#FFE680")
PUAH = F("eve", skin="#B98A6E", shadow="#5A3A3A", hair="#1A1210", scarf="#4A4A7A", light="#FFC14D")
SHIPHRAH_BOLD = F("eve", skin="#C99A84", shadow="#6A4A3A", hair="#3A2A1E", scarf="#2A5A6A", light="#FFD23F", brow="scowl")
JETHRO = F("adam", skin="#B98A6E", shadow="#5A3A3A", hair="#E8E2D6", hl="#B8B2A6", beard=True, beard_color="#E8E2D6", scarf="#1F4A5A", band=True, light="#FFC14D")
MOSES_OLD_PLEA = F("adam", skin="#C98E66", shadow="#6A4A5A", hair="#2A1A10", hl="#5A4A3E", beard=True, scarf="#E2D8C4", cord=True, brow="sorrow", light="#9FB8FF")
ZIPPORAH_NIGHT = F("eve", skin="#A88A8A", shadow="#3A2A4A", hair="#1A1210", scarf="#7A1A2E", brow="scowl", light="#9FB8FF") + HEM
MOSES_PRINCE_AFRAID = F("adam", skin="#D9A27A", shadow="#7A4A4A", egypt=("#F3EFE6", "#D7261E"), collar=True, kohl=True, brow="sorrow", sweat=True, light="#FF8A3D")
LEVITE = F("adam", skin="#B98A6E", shadow="#6A4A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", light="#FFC14D")

# ---- the cast at a distance --------------------------------------------------------------------------------
# headcloths drawn over the figure's head (local units: the head is a circle of radius ~12 at (0, -188))
def headcloth(color, cord="#3A2214"):
    return (f'<path d="M-15 -186 C -16 -206 16 -206 15 -186 L 19 -158 L 10 -166 L -10 -166 L -19 -158 Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.8"></path>'
            + (f'<path d="M-14 -194 C -6 -198 6 -198 14 -194" fill="none" stroke="{cord}" stroke-width="3.4"></path>' if cord else ""))
BLACK_BEARD = WHITE_BEARD.replace("#E8E2D6", "#2A1A10")
MOSES_ROBE, AARON_ROBE, JETHRO_ROBE, ZIPPORAH_ROBE = "#8A6A4A", "#3A5A8A", "#1F4A5A", "#9A2A2E"
HEBREW = ["#5A3A22", "#8A6A4A", "#4A3A6A", "#6A5A3A", "#3A4A3A", "#7A4A2E"]
NEMES = T.NEMES_BLUE.replace("#1F5FAD", "#0D0D0F")

def moses(p, x, y, s, flip=False, up=None):
    """Moses the shepherd: brown robe, off-white headcloth with a dark cord, black beard; the rod when holding a staff."""
    rod = STAFF if up is HOLD_STAFF else ""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=MOSES_ROBE, sw=3, flip=flip, up=up, extra=headcloth("#E2D8C4") + BLACK_BEARD + rod)

def moses_prince(p, x, y, s, flip=False, up=None):
    """Moses grown up in Pharaoh's house: white kilt-robe, red-and-white headcloth, gold collar."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#F3EFE6", kind="Tunic", sw=3, flip=flip, up=up,
                     extra=headcloth("#F3EFE6", cord=None) + '<path d="M-12 -196 L 12 -196 M-16 -180 L 16 -180 M-18 -168 L 18 -168" stroke="#D7261E" stroke-width="3.4"></path>' + T.COLLAR.split("<circle")[0])

def aaron(p, x, y, s, flip=False, up=None):
    """Aaron: blue headcloth with a cord, grey beard, blue robe."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=AARON_ROBE, sw=3, flip=flip, up=up, extra=headcloth("#4A6A9A") + GREY_BEARD)

def jethro(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=JETHRO_ROBE, sw=3, flip=flip, up=up, extra=headcloth("#1F4A5A", cord="#E8B830") + WHITE_BEARD)

def zipporah(p, x, y, s, flip=False, up=None):
    return woman(p, x, y, s, ZIPPORAH_ROBE, flip=flip, up=up)

def pharaoh(p, x, y, s, flip=False, up=None):
    """The new Pharaoh: black-and-gold nemes, white robe, gold collar."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#8A4A2E", cloth="#F3EFE6", sw=3, flip=flip, up=up, extra=NEMES + T.COLLAR.split("<circle")[0])

def taskmaster(p, x, y, s, flip=False, up=None):
    whip = '<path d="M30 -150 C 50 -170 70 -150 90 -170" fill="none" stroke="#3A2214" stroke-width="3"></path>' if up else ""
    return mk.person(p, round(x), round(y), round(s, 3), body="#8A4A2E", cloth="#E8E2D6", kind="Tunic", sw=3, flip=flip, up=up, extra=headcloth("#E8E2D6", cord=None) + whip)

def hebrew(c):
    def fn(p, x, y, s, flip=False, up=None): return man(p, x, y, s, c, flip=flip, up=up)
    return fn

CLOTHS = ["#C8BCA6", "#8A7A6A", "#5A6E8A", "#A88A5A", "#6A4A5A", "#E2D8C4"]
def elder(c, k=0):
    """An elder of Israel: robe c, a headcloth (one of CLOTHS, by k) with a dark cord, grey beard."""
    def fn(p, x, y, s, flip=False, up=None):
        return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=c, sw=3, flip=flip, up=up, extra=headcloth(CLOTHS[k % len(CLOTHS)], cord="#2A1A10") + GREY_BEARD)
    return fn

def son(c, k=0):
    """One of the sons of Israel: robe c, headcloth, black beard."""
    def fn(p, x, y, s, flip=False, up=None):
        return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=c, sw=3, flip=flip, up=up, extra=headcloth(CLOTHS[k % len(CLOTHS)], cord="#2A1A10") + BLACK_BEARD)
    return fn

def princess(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body="#8A4A2E", cloth="#F3EFE6", woman=True, hair="#0D0D0F", sw=3, flip=flip, up=up, extra=T.COLLAR.split("<circle")[0])

# ---- scenes -------------------------------------------------------------------------------------------------
LEAH_C, ZILPAH_C, RACHEL_C, BILHAH_C = "#6A7AD8", "#8A6AB8", "#C2456A", "#1F7A8C"
SONS = [("REUBEN", LEAH_C), ("SIMEON", LEAH_C), ("LEVI", LEAH_C), ("JUDAH", LEAH_C), ("ISSACHAR", LEAH_C), ("ZEBULUN", LEAH_C),
        ("BENJAMIN", RACHEL_C), ("DAN", BILHAH_C), ("NAPHTALI", BILHAH_C), ("GAD", ZILPAH_C), ("ASHER", ZILPAH_C)]

def sons_row(p, w, h, seed):
    """The eleven who came into Egypt with Jacob, robed and bearded, names in tags (coloured by mother); Joseph apart, already in Egypt."""
    b = h * 0.74; o = [sun(w * 0.92, h * 0.3, 12, op=0.2), EG.pyramid(w * 0.95, b, w * 0.12, h * 0.24), ground(w, h, b, "#C8A06A", dy=0)]
    n = len(SONS); x0, x1 = w * 0.05, w * 0.74
    for i, (nm, c) in enumerate(SONS):
        x = x0 + (x1 - x0) * i / (n - 1); ty = b + 8 + (i % 2) * 20
        o.append(son(c, i)(p, x, b, fit(b, h * 0.42)))
        o.append(f'<path d="M{f(x)} {f(b)} L {f(x)} {f(ty)}" stroke="{c}" stroke-width="1.4"></path>'
                 f'<rect x="{f(x - 31)}" y="{f(ty)}" width="62" height="15" fill="#12113A" stroke="{c}" stroke-width="1.6"></rect>' + label(x, ty + 11, nm, "#F3EFE6", 7.5, ls=0.04))
    jx = w * 0.87
    o.append(T.figure(p, "joseph_eg", jx, b, fit(b, h * 0.42)))
    o.append(f'<rect x="{f(jx - 31)}" y="{f(b + 8)}" width="62" height="15" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></rect>' + label(jx, b + 19, "JOSEPH", "#0D0D0F", 7.5, ls=0.04))
    o.append(f'<path d="M{f(w * 0.795)} {f(h * 0.36)} L {f(w * 0.795)} {f(h - 4)}" stroke="#0D0D0F" stroke-width="1.6" stroke-dasharray="6 5"></path>')
    return "".join(o)

def households(p, w, h, seed):
    """He made them households: families before their houses, a man, his wife and their children."""
    r = random.Random(seed); b = h * 0.9
    o = [sun(w * 0.9, h * 0.2, 12, op=0.25)]
    for i, x in enumerate((0.16, 0.5, 0.84)):
        o.append(f'<rect x="{f(w * x - 60)}" y="{f(b - h * 0.5)}" width="120" height="{f(h * 0.5)}" fill="#B88A5A" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<rect x="{f(w * x - 14)}" y="{f(b - h * 0.26)}" width="28" height="{f(h * 0.26)}" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(ground(w, h, b, "#C8A06A", dy=0))
    for i, x in enumerate((0.16, 0.5, 0.84)):
        X0 = w * x
        o.append(man(p, X0 - 44, b, fit(b, h * 0.44), r.choice(HEBREW)) + woman(p, X0 + 40, b, fit(b, h * 0.48), r.choice(["#5A6E8A", "#7A3A5A", "#2A5A6A"]), flip=True)
                 + T.figure(p, ("lad", r.choice(["#C8A06A", "#E8E2D6"])), X0 - 6, b, fit(b, h * 0.66)) + T.figure(p, ("lad", "#E8E2D6"), X0 + 12, b, fit(b, h * 0.76)))
    return "".join(o)

def tombs(w, h, seed):
    """Joseph died, and all his brethren, and all that generation: a row of tombs at dusk, the pyramids beyond."""
    b = h * 0.8; o = [sun(w * 0.5, b, 40, color="#FF8A3D", op=0.25), EG.pyramid(w * 0.24, b, w * 0.22, h * 0.36), EG.pyramid(w * 0.78, b, w * 0.3, h * 0.46), hills(w, h, b, seed, color="#2A1A2E", amp=4)]
    o.append(ground(w, h, b, "#3A2A2E", dy=0))
    for i in range(12):
        x = w * (0.06 + i * 0.08); hh = 26 + (i % 3) * 6
        o.append(f'<path d="M{f(x - 16)} {f(b + 14)} L {f(x - 16)} {f(b + 14 - hh)} C {f(x - 16)} {f(b - hh)} {f(x + 16)} {f(b - hh)} {f(x + 16)} {f(b + 14 - hh)} L {f(x + 16)} {f(b + 14)} Z" fill="#6A5A5E" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def bricks(p, w, h, seed):
    """Mortar and brick: men treading clay in a pit, brick moulds, rows of bricks drying, a taskmaster with a rod."""
    r = random.Random(seed); b = h * 0.86
    o = [sun(w * 0.86, h * 0.16, 16, color="#FFF4C2", op=0.3), ground(w, h, b - h * 0.12, "#C8A06A", dy=0)]
    o.append(f'<path d="M{f(w * 0.04)} {f(b - h * 0.1)} L {f(w * 0.46)} {f(b - h * 0.1)} L {f(w * 0.42)} {f(b + 10)} L {f(w * 0.08)} {f(b + 10)} Z" fill="#6A3A22" stroke="#0D0D0F" stroke-width="2.4"></path>')
    for i in range(4):
        o.append(man(p, w * (0.1 + i * 0.09), b, fit(b, h * 0.58), r.choice(HEBREW), flip=i % 2 == 1))
    for row in range(3):
        for i in range(9):
            x = w * 0.52 + i * w * 0.04 + (row % 2) * 8; y = b - h * 0.04 - row * 14
            o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.034)}" height="11" fill="#A85A32" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    o.append(taskmaster(p, w * 0.9, b, fit(b, h * 0.5), flip=True, up=[(-22, -158), (2, -170), (26, -186)]))
    return "".join(o)

def levite_house(p, w, h, seed):
    """A man of the house of Levi took to wife a daughter of Levi: a lamp-lit Hebrew house, the two side by side."""
    return _levite(p, w, h, seed, h * 0.9)

def _levite(p, w, h, seed, b):
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A14"></rect>',
         f'<rect x="{f(w * 0.04)}" y="{f(h * 0.08)}" width="{f(w * 0.92)}" height="{f(b - h * 0.08)}" fill="#5A3A26" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.74)}" y="{f(h * 0.2)}" width="{f(w * 0.12)}" height="{f(h * 0.22)}" fill="#12113A" stroke="#0D0D0F" stroke-width="2"></rect>',
         mk.stars(6, w * 0.12, h * 0.22, seed).replace("<g", f'<g transform="translate({f(w * 0.74)} {f(h * 0.2)})"', 1),
         f'<circle cx="{f(w * 0.46)}" cy="{f(h * 0.4)}" r="{f(h * 0.42)}" fill="#FFC14D" opacity="0.16"></circle>',
         lamp(w * 0.46, h * 0.36, 1.0), ground(w, h, b, "#3A2418", dy=0),
         man(p, w * 0.32, b, fit(b, h * 0.3), "#5A3A22", up=[(-22, -158), (2, -150), (24, -146)]),
         woman(p, w * 0.6, b, fit(b, h * 0.34), "#5A6E8A", flip=True)]
    return "".join(o)

def lamp(x, y, s=1.0):
    """A clay oil lamp on a ledge, its flame lit."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-30 6 L 30 6 L 26 14 L -26 14 Z" fill="#6A4A2E" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M-18 6 C -18 -6 14 -8 22 -2 L 30 -4 L 22 6 Z" fill="#A8743A" stroke="#0D0D0F" stroke-width="2"></path>'
            + E.flame(26, -4, 8, 22, 0.1) + '</g>')

def milk_honey(p, w, h, seed):
    """A good land and a large, flowing with milk and honey: green hills, a stream, goats and kine, bees about the flowers."""
    r = random.Random(seed); b = h * 0.62
    o = [sun(w * 0.84, h * 0.2, 16, op=0.3), hills(w, h, b - 20, seed, color="#4E8A3A", amp=18), hills(w, h, b, seed + 1, color="#2E6B3A", amp=10), ground(w, h, b + 6, "#9CCB5E", dy=0)]
    o.append(f'<path d="M{f(w * 0.3)} {f(b + 6)} C {f(w * 0.36)} {f(b + 40)} {f(w * 0.2)} {f(h * 0.8)} {f(w * 0.3)} {f(h + 10)}" fill="none" stroke="#8FD0E2" stroke-width="16" stroke-linecap="round"></path>')
    o.append(Z.flock(w * 0.42, w * 0.96, b + 20, h * 0.96, 14, seed, cows=0.4, smin=0.2, smax=0.36))
    for _ in range(26):
        x, y = r.uniform(0, w * 0.26), r.uniform(b + 20, h)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="4" fill="{r.choice(["#FFD23F", "#F3EFE6", "#E07A9A"])}" stroke="#0D0D0F" stroke-width="1"></circle>')
    for _ in range(10):
        x, y = r.uniform(0, w * 0.3), r.uniform(b - 20, h * 0.9)
        o.append(f'<g transform="translate({f(x)} {f(y)})"><ellipse cx="0" cy="0" rx="4.5" ry="3" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.2"></ellipse>'
                 '<path d="M-1.5 -2.5 L -1.5 2.5 M1.5 -2.5 L 1.5 2.5" stroke="#0D0D0F" stroke-width="1.2"></path><ellipse cx="-1" cy="-5" rx="3" ry="2" fill="#F3EFE6" opacity="0.8"></ellipse></g>')
    return "".join(o)

def peoples_map(w, h, seed):
    """The place of the Canaanite, the Hittite, the Amorite, the Perizzite, the Hivite and the Jebusite, as a technical map."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.2)} -10 C {f(w * 0.18)} {f(h * 0.4)} {f(w * 0.12)} {f(h * 0.7)} {f(w * 0.04)} {f(h + 10)} L -10 {f(h + 10)} L -10 -10 Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.66)} {f(h * 0.04)} C {f(w * 0.64)} {f(h * 0.3)} {f(w * 0.7)} {f(h * 0.5)} {f(w * 0.68)} {f(h * 0.74)}" fill="none" stroke="#2C9DB8" stroke-width="3"></path>')
    o.append(f'<ellipse cx="{f(w * 0.68)}" cy="{f(h * 0.86)}" rx="{f(w * 0.03)}" ry="{f(h * 0.1)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></ellipse>')
    pts = [("CANAANITE", 0.3, 0.22), ("HITTITE", 0.5, 0.14), ("AMORITE", 0.56, 0.56), ("PERIZZITE", 0.42, 0.4), ("HIVITE", 0.32, 0.62), ("JEBUSITE", 0.48, 0.78)]
    for nm, x, y in pts:
        o.append(node(w * x, h * y, nm, "#FFD23F", r=5, dy=-10, size=10))
    o.append(f'<path d="M{f(w * 0.24)} {f(h * 0.08)} L {f(w * 0.62)} {f(h * 0.06)} L {f(w * 0.64)} {f(h * 0.92)} L {f(w * 0.18)} {f(h * 0.9)} Z" fill="#9CCB5E" fill-opacity="0.1" stroke="#9CCB5E" stroke-width="2" stroke-dasharray="8 5"></path>')
    o.append(label(w * 0.42, h * 0.97, "A LAND FLOWING WITH MILK AND HONEY", "#9CCB5E", 9))
    o.append(label(w * 0.94, h * 0.08, "N ↑", "#8FD0E2", 12, "end"))
    return "".join(o)

def elders(p, w, h, seed, setting="egypt", bow=False, extra_cast=(), top=0.5):
    """The elders of Israel gathered together: grey-bearded men in headcloths; bowing their heads when bow=True."""
    r = random.Random(seed); b = h * 0.88
    cast = list(extra_cast)
    o = []
    if bow:
        o.append(T.stage(p, w, h, seed, setting, cast))
        for i in range(9):
            x = w * (0.08 + i * 0.1)
            o.append(E.kneel(x, b + 4, 0.36 + (i % 2) * 0.04, color=r.choice(HEBREW), skin="#8A5A3E", flip=i < 5))
        return "".join(o)
    cast += [(elder(r.choice(HEBREW), i), 0.06 + i * 0.088, top + (i % 2) * 0.04, i > 4) for i in range(9)]
    return T.stage(p, w, h, seed, setting, cast)

def jewels(w, h, seed):
    """Jewels of silver, and jewels of gold, and raiment: bracelets, ear-rings and folded cloth laid out on a rug."""
    r = random.Random(seed)
    o = [f'<rect x="{f(w * 0.06)}" y="{f(h * 0.2)}" width="{f(w * 0.88)}" height="{f(h * 0.7)}" rx="6" fill="#7A2A3A" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.1)}" y="{f(h * 0.26)}" width="{f(w * 0.8)}" height="{f(h * 0.58)}" fill="none" stroke="#E8B830" stroke-width="2" stroke-dasharray="10 6"></rect>']
    for i, c in enumerate(["#1F5FAD", "#F3EFE6", "#5E8F26"]):
        X0, Y0, W0, H0 = w * (0.58 + i * 0.1), h * (0.34 + i * 0.05), w * 0.2, h * 0.3
        o.append(f'<rect x="{f(X0)}" y="{f(Y0)}" width="{f(W0)}" height="{f(H0)}" fill="{c}" stroke="#0D0D0F" stroke-width="2"></rect>'
                 + "".join(f'<path d="M{f(X0)} {f(Y0 + H0 * k)} L {f(X0 + W0)} {f(Y0 + H0 * k)}" stroke="#0D0D0F" stroke-width="1.2" opacity="0.4"></path>' for k in (0.33, 0.66))
                 + f'<path d="M{f(X0 + 6)} {f(Y0 + 6)} L {f(X0 + W0 - 6)} {f(Y0 + 6)}" stroke="#E8B830" stroke-width="3"></path>')
    for _ in range(14):
        x, y = r.uniform(w * 0.14, w * 0.52), r.uniform(h * 0.32, h * 0.78); c = r.choice(["#E8B830", "#C8C8D0"]); rx, ry = r.uniform(12, 22), r.uniform(6, 10)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rx)}" ry="{f(ry)}" fill="none" stroke="#0D0D0F" stroke-width="6"></ellipse>'
                 f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rx)}" ry="{f(ry)}" fill="none" stroke="{c}" stroke-width="3.4"></ellipse>'
                 f'<path d="M{f(x - rx * 0.5)} {f(y - ry * 0.8)} l 6 -2" stroke="#FFF4C2" stroke-width="2"></path>')
    return "".join(o)

def blood_ground(p, w, h, seed):
    """Water of the river poured upon the dry land becomes blood: Moses pours from a pitcher; on the sand the stream turns red."""
    b = h * 0.86; sc = fit(b, h * 0.42); x = w * 0.3
    o = [sun(w * 0.9, h * 0.18, 14, op=0.25), f'<path d="M-10 {f(h * 0.5)} C {f(w * 0.2)} {f(h * 0.46)} {f(w * 0.3)} {f(h * 0.56)} {f(w * 0.5)} {f(h * 0.52)} L {f(w * 0.5)} {f(h * 0.62)} L -10 {f(h * 0.62)} Z" fill="#1F6F9A"></path>',
         E.reeds(0, w * 0.46, h * 0.6, h * 0.16, 16, seed), ground(w, h, h * 0.6, "#C8A06A", dy=0)]
    hx, hy = x - 30 * sc, b - 120 * sc
    o.append(moses(p, x, b, sc, up=[(-22, -158), (-6, -134), (-30, -120)]))
    o.append(f'<g transform="translate({f(hx)} {f(hy)}) scale({f(sc)}) rotate(-60)"><path d="M-14 -10 C -22 10 -16 34 0 36 C 16 34 22 10 14 -10 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2.6"></path>'
             '<path d="M-10 -10 L -12 -20 L 12 -20 L 10 -10" fill="#B5652E" stroke="#0D0D0F" stroke-width="2.6"></path></g>')
    sx, sy = hx - 26 * sc, hy - 4 * sc
    o.append(f'<path d="M{f(sx)} {f(sy)} C {f(sx - 14)} {f(sy + 20)} {f(sx - 16)} {f(b - 30)} {f(sx - 18)} {f(b - 14)}" fill="none" stroke="#8FD0E2" stroke-width="5" stroke-linecap="round"></path>')
    o.append(f'<path d="M{f(sx - 18)} {f(b - 16)} L {f(sx - 18)} {f(b + 2)}" stroke="#B5121B" stroke-width="5" stroke-linecap="round"></path>')
    o.append(f'<ellipse cx="{f(sx - 40)}" cy="{f(b + 6)}" rx="{f(w * 0.1)}" ry="8" fill="#8A0E16" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    return "".join(o)

def journey(p, w, h, seed):
    """Moses took his wife and his sons, and set them upon an ass: Zipporah riding, the two boys beside her, Moses ahead with the rod of God."""
    b = h * 0.88; sc = fit(b, h * 0.42)
    o = [sun(w * 0.18, h * 0.2, 14, op=0.25), hills(w, h, b - 30, seed, color="#8A6A5A", amp=14), ground(w, h, b, "#C8A06A", dy=0)]
    o.append(N.mount(w * 0.58, b, round(sc * 1.15, 3), flip=True, rider_body=SKIN, rider_cloth=ZIPPORAH_ROBE, p=p))
    o.append(T.figure(p, ("lad", "#C8A06A"), w * 0.72, b, fit(b, h * 0.62), flip=True) + T.figure(p, ("lad", "#E8E2D6"), w * 0.8, b, fit(b, h * 0.7), flip=True))
    o.append(moses(p, w * 0.36, b, fit(b, h * 0.48), flip=True, up=HOLD_STAFF))
    return "".join(o)

def lodging(w, h, seed):
    """The lodging-place on the way by night: a tent pitched under the stars, a small fire."""
    b = h * 0.84
    return (mk.stars(60, w, h * 0.6, seed) + f'<circle cx="{f(w * 0.8)}" cy="{f(h * 0.4)}" r="16" fill="#E8E2D6"></circle>' + hills(w, h, b - 10, seed, color="#1A1430", amp=10)
            + ground(w, h, b, "#1A1430", dy=0) + black_tent(w * 0.42, b, w * 0.64, h * 0.2) + E.blaze(w * 0.86, b, 30, 36, seed, n=5))

def black_tent(x, b, w, h, color="#2A2230", lit="#FFC14D"):
    """A low tent of black goats' hair: a sagging ridge on poles, guy-ropes, the door-flap open on lamplight."""
    l, r = x - w / 2, x + w / 2
    roof = (f'M{f(l)} {f(b)} L {f(l + w * 0.06)} {f(b - h * 0.8)} C {f(l + w * 0.2)} {f(b - h)} {f(l + w * 0.3)} {f(b - h * 0.86)} {f(x)} {f(b - h)} '
            f'C {f(r - w * 0.3)} {f(b - h * 0.86)} {f(r - w * 0.2)} {f(b - h)} {f(r - w * 0.06)} {f(b - h * 0.8)} L {f(r)} {f(b)} Z')
    return (f'<path d="M{f(l - w * 0.08)} {f(b)} L {f(l + w * 0.06)} {f(b - h * 0.8)} M{f(r + w * 0.08)} {f(b)} L {f(r - w * 0.06)} {f(b - h * 0.8)}" stroke="#8A7A6A" stroke-width="1.4"></path>'
            f'<path d="{roof}" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></path>'
            f'<path d="M{f(x - w * 0.08)} {f(b)} L {f(x - w * 0.06)} {f(b - h * 0.62)} L {f(x + w * 0.06)} {f(b - h * 0.62)} L {f(x + w * 0.08)} {f(b)} Z" fill="{lit}" opacity="0.85" stroke="#0D0D0F" stroke-width="2"></path>'
            + "".join(f'<path d="M{f(l + w * k)} {f(b - h * 0.9)} L {f(l + w * k)} {f(b)}" stroke="#0D0D0F" stroke-width="1.2" opacity="0.5"></path>' for k in (0.25, 0.75)))

def crowd(p, w, h, seed, n=40):
    """The land was filled with them: a crowd of small figures thickening toward the front, houses behind."""
    r = random.Random(seed); hz = h * 0.42
    o = [city(w * 0.8, hz + 6, w * 0.3, h * 0.3, seed, color="#B88A5A", lit="#FFC14D", wall="#C8A06A"), ground(w, h, hz, "#C8A06A", dy=0)]
    for y, x in sorted((r.uniform(hz + 8, h * 1.05), r.uniform(-10, w + 10)) for _ in range(n)):
        k = (y - hz) / (h - hz); s = 0.12 + 0.3 * k
        if r.random() < 0.45: o.append(woman(p, x, y, s, r.choice(["#5A6E8A", "#7A3A5A", "#2A5A6A", "#C2456A"]), flip=r.random() < 0.5))
        else: o.append(man(p, x, y, s, r.choice(HEBREW), flip=r.random() < 0.5))
    return "".join(o)

def wonders(w, h, seed):
    """I will put forth my hand, and smite Egypt with all my wonders: lightning and a black storm over the pyramids (God is never drawn)."""
    b = h * 0.86
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#12102A"></rect>'
            + "".join(f'<ellipse cx="{f(w * x)}" cy="{f(h * y)}" rx="{f(w * 0.3)}" ry="{f(h * 0.12)}" fill="#2A2448" opacity="0.9"></ellipse>' for x, y in ((0.2, 0.08), (0.6, 0.04), (0.9, 0.12), (0.4, 0.18)))
            + E2.bolt(w * 0.3, h * 0.12, h * 0.7, seed) + E2.bolt(w * 0.74, h * 0.16, h * 0.62, seed + 1, w=0.8)
            + EG.pyramid(w * 0.5, b, w * 0.5, h * 0.4) + EG.pyramid(w * 0.86, b, w * 0.3, h * 0.24) + ground(w, h, b, "#2A2030", dy=0))

def horeb(w, h, b, seed, color="#6A4A4A", lit="#B5652E"):
    """The mountain of God: a jagged granite massif, sunlit on one face."""
    r = random.Random(seed)
    pk = [(0.1, 0.62), (0.26, 0.4), (0.36, 0.5), (0.52, 0.12), (0.62, 0.3), (0.74, 0.22), (0.9, 0.5), (1.02, 0.6)]
    d = f"M-10 {f(b)} " + " ".join(f"L {f(w * x)} {f(h * y + r.uniform(-6, 6))}" for x, y in pk) + f" L {f(w + 10)} {f(b)} Z"
    lit_d = f"M{f(w * 0.52)} {f(h * 0.12)} L {f(w * 0.62)} {f(h * 0.3)} L {f(w * 0.74)} {f(h * 0.22)} L {f(w * 0.9)} {f(h * 0.5)} L {f(w * 0.7)} {f(b)} Z"
    return f'<path d="{d}" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></path><path d="{lit_d}" fill="{lit}" opacity="0.7"></path>'

def meeting(p, w, h, seed):
    """Aaron met Moses in the mountain of God, and kissed him: the two brothers embracing below Horeb."""
    b = h * 0.86; sc = fit(b, h * 0.36)
    return (sun(w * 0.9, h * 0.16, 16, op=0.25) + horeb(w, h, b, seed) + ground(w, h, b, "#8A6A5A", dy=0)
            + aaron(p, w * 0.47, b, sc, up=[(-22, -158), (4, -150), (30, -160)]) + moses(p, w * 0.53, b, sc, flip=True, up=[(-22, -158), (4, -150), (30, -150)]))

# ---- the map of the Exodus ------------------------------------------------------------------------------------
PLACES = {"EGYPT": (0.14, 0.62), "GOSHEN": (0.26, 0.27), "RAAMSES": (0.2, 0.46), "SUCCOTH": (0.36, 0.38), "THE RED SEA": (0.42, 0.56),
          "MARAH": (0.46, 0.66), "ELIM": (0.5, 0.74), "SINAI": (0.62, 0.86), "HOREB": (0.62, 0.86), "MIDIAN": (0.84, 0.82), "KADESH": (0.66, 0.3),
          "CANAAN": (0.7, 0.2), "THE WILDERNESS": (0.56, 0.48)}

def exodus_map(w, h, legs=(), cur=None, color="#FFD23F", names=None):
    """Egypt, the wilderness and Canaan as a technical map: the Nile and its delta, the two gulfs of the Red Sea around the
    mount of Sinai, Midian across the eastern gulf. legs = the route so far; names = other places to mark."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 {f(h * 0.2)} C {f(w * 0.1)} {f(h * 0.16)} {f(w * 0.3)} {f(h * 0.12)} {f(w * 0.5)} {f(h * 0.14)} C {f(w * 0.6)} {f(h * 0.1)} {f(w * 0.66)} {f(h * 0.0)} {f(w * 0.7)} -10 L -10 -10 Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>'
             + label(w * 0.2, h * 0.08, "THE GREAT SEA", "#8FD0E2", 9))
    o.append(f'<path d="M{f(w * 0.2)} {f(h + 10)} C {f(w * 0.2)} {f(h * 0.7)} {f(w * 0.18)} {f(h * 0.4)} {f(w * 0.2)} {f(h * 0.24)}" fill="none" stroke="#2C9DB8" stroke-width="5"></path>'
             + f'<path d="M{f(w * 0.2)} {f(h * 0.26)} L {f(w * 0.12)} {f(h * 0.18)} M{f(w * 0.2)} {f(h * 0.26)} L {f(w * 0.28)} {f(h * 0.16)}" stroke="#2C9DB8" stroke-width="3"></path>'
             + label(w * 0.17, h * 0.8, "NILE", "#8FD0E2", 9, anchor="end"))
    o.append(f'<path d="M{f(w * 0.38)} {f(h * 0.42)} C {f(w * 0.4)} {f(h * 0.6)} {f(w * 0.5)} {f(h * 0.8)} {f(w * 0.6)} {f(h * 0.98)} L {f(w * 0.7)} {f(h + 10)} L {f(w * 0.46)} {f(h + 10)} C {f(w * 0.42)} {f(h * 0.8)} {f(w * 0.36)} {f(h * 0.6)} {f(w * 0.36)} {f(h * 0.42)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.78)} {f(h * 0.5)} C {f(w * 0.76)} {f(h * 0.66)} {f(w * 0.72)} {f(h * 0.84)} {f(w * 0.68)} {f(h + 10)} L {f(w * 0.74)} {f(h + 10)} C {f(w * 0.78)} {f(h * 0.84)} {f(w * 0.8)} {f(h * 0.66)} {f(w * 0.8)} {f(h * 0.5)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.6)} {f(h * 0.9)} l -12 16 l 24 0 Z" fill="#C8682E" stroke="#0D0D0F" stroke-width="1.6"></path>')
    pts = [(PLACES[n][0] * w, PLACES[n][1] * h) for n in legs]
    if len(pts) > 1: o.append(Z.route(pts, color=color, sw=3))
    for n in list(dict.fromkeys(list(legs) + list(names or []))):
        x, y = PLACES[n][0] * w, PLACES[n][1] * h
        o.append(node(x, y, n, "#D7261E" if n == cur else color, r=5, dy=-12 if y > h * 0.15 else 22, size=10))
    o.append(label(w * 0.95, h * 0.94, "N ↑", "#8FD0E2", 12, "end"))
    return "".join(o)

def burning(w, h, seed, cx=0.5, size=1.0, sky=True, bw=None, bh=None):
    """The bush that burned and was not consumed, at night on the mountain of God (bw, bh: the bush's size in px)."""
    b = h * 0.92
    bh = bh or min(h * 0.62, w * 0.5) * size; bw = bw or bh * 1.1         # a broad, round-topped bush, whatever the panel's shape
    return ((X_COSMIC(w, h) if sky else "") + hills(w, h, b - 6, seed, color="#1A1430", amp=10) + ground(w, h, b, "#1A1430", dy=0)
            + f'<circle cx="{f(w * cx)}" cy="{f(b - bh * 0.5)}" r="{f(bh * 0.8)}" fill="#FF8A3D" opacity="0.18"></circle>'
            + E.bush(w * cx, b, bw, bh, seed))

from genesis import art as _X
def X_COSMIC(w, h): return _X.cosmic(w, h)
