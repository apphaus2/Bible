"""Drawings for Leviticus chapter 3 (Leviticus 9–11): the eighth day, the fire from before Jehovah, Nadab and Abihu, and
the clean and unclean living things.

Restraint for 10:1–5: the two sons are shown offering the strange fire, then only their censers on the ground under the
fire; Mishael and Elzaphan carry two shapes wrapped in their coats, far off. No one is shown dying."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3, exodus4 as E4, exodus5 as V, samuel1 as S1, numbers1 as N, judges1 as J1
from faces_ex import F
from genesis import art2 as Y, art3 as Z, art10 as T
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import sun, label, man, woman
from exo import art as A, art8 as B8, art9 as Q
from exo.art6 import GND
from exo.art7 import ban
from lev.art import altar, door, priest, offerer, dove, goat, REACH, A_ALL, jar
def f(v): return f"{v:.1f}"

AARON_GRIEF = F("adam", skin="#B98A7E", shadow="#4A3A5A", hair="#9A968E", hl="#6A665E", beard=True, scarf="#F3EFE6", cord=False, brow="sorrow", light="#9FB8FF")
AARON_HP = F("adam", skin="#C98E66", shadow="#8A5A3E", hair="#9A968E", hl="#6A665E", beard=True, scarf="#F3EFE6", light="#FFE680")
MOSES, MOSES_STERN, MOSES_CALM = A.MOSES, A.MOSES_STERN, A.MOSES_CALM

def court(p, w, h, seed, cast=(), base=0.9, fire=True, glory=False, people=0, fallen=False):
    """The court of the tabernacle: the tent at the back, the brass altar, the cast in front; people at the sides."""
    r = random.Random(seed); b = h * base
    o = [mk.defs(p, *A_ALL)]
    if glory: o.append(V.rays(w * 0.62, h * 0.3, 40, 20, max(w, h) * 1.2, color="#FFF4C2", op=0.35))
    o.append(ground(w, h, h * 0.58, "#C8B080", dy=0) + V.tabernacle(w * 0.66, h * 0.62, w * 0.5, uid=p + "tn"))
    o.append(altar(w * 0.46, h * 0.78, min(2.4, h / 140), fire=fire))
    for c in cast:
        fn, x, top = c[0], c[1], c[2]; flip = c[3] if len(c) > 3 else False; up = c[4] if len(c) > 4 else None
        if isinstance(up, str): up = T.POSES[up]
        o.append(fn(p, w * x, b, fit(b, h * top), flip=flip, up=up))
    for i in range(people):
        x = w * (0.04 + i * 0.05) if i % 2 == 0 else w * (0.96 - i * 0.05); y = b - (i % 3) * 6
        if fallen: o.append(E.kneel(x, y, fit(y, h * 0.62) * 0.9, color=r.choice(A.HEBREW), skin="#8A5A3E", flip=x > w / 2))
        else: o.append(man(p, x, y, fit(y, h * 0.5), r.choice(A.HEBREW), flip=x > w / 2))
    return "".join(o)

def hp(p, x, y, s, flip=False, up=None): return Q.high_priest(p, x, y, s, flip=flip, up=up)
def sp(p, x, y, s, flip=False, up=None): return Q.son_priest(p, x, y, s, flip=flip, up=up)
BOTH = [(-22, -158), (-30, -196), (-36, -232)]

def offerings_row(w, h, seed):
    """A calf, a ram, a he-goat, a calf and a lamb, an ox and a ram, and the meal-offering: the oblations of the eighth day."""
    b = h * 0.9; o = [ground(w, h, h * 0.6, "#C8B080", dy=0)]
    xs = [0.12, 0.26, 0.4, 0.54, 0.66, 0.8]
    o += [S1.cow(w * xs[0], b, h / 300, color="#C9A27A"), E.sheep(w * xs[1], b, h / 260), goat(w * xs[2], b, h / 260), E3.lamb(w * xs[3], b, h / 300),
          S1.cow(w * xs[4], b, h / 260, color="#5A3A22", patch="#3A2214"), E.sheep(w * xs[5], b, h / 260)]
    o.append(f'<g transform="translate({f(w * 0.92)} {f(b)})">' + '<path d="M-26 0 C -16 -22 16 -22 26 0 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></path></g>')
    return "".join(o)

def fire_falls(p, w, h, seed):
    """There came forth fire from before Jehovah, and consumed upon the altar the burnt-offering: a column of fire from the
    tent onto the altar; the people fallen on their faces."""
    o = [court(p, w, h, seed, people=12, fallen=True, glory=True, fire=False)]
    ax, ay = w * 0.46, h * 0.78
    o.append(f'<path d="M{f(w * 0.66)} {f(h * 0.3)} C {f(w * 0.6)} {f(h * 0.46)} {f(w * 0.5)} {f(h * 0.5)} {f(ax)} {f(ay - 40)}" fill="none" stroke="#FFD23F" stroke-width="26" opacity="0.6" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.66)} {f(h * 0.3)} C {f(w * 0.6)} {f(h * 0.46)} {f(w * 0.5)} {f(h * 0.5)} {f(ax)} {f(ay - 40)}" fill="none" stroke="#FFF4C2" stroke-width="10" stroke-linecap="round"></path>')
    o.append(E.blaze(ax + 14, ay - h * 0.1, w * 0.16, h * 0.36, seed, n=8))
    return "".join(o)

def censer(x, y, s=1.0, fire=True, fallen=False):
    """A censer: a bronze fire-pan on a long handle; fire and the smoke of incense in it."""
    rot = 70 if fallen else 0
    o = (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({f(s)})"><path d="M-16 0 C -16 10 16 10 16 0 Z" fill="#B87333" stroke="#0D0D0F" stroke-width="1.6"></path>'
         '<path d="M16 2 L 46 -6" stroke="#5A3A22" stroke-width="3" stroke-linecap="round"></path>')
    if fire: o += E.flame(-8, 0, 16, 18, 0.1) + '<path d="M0 -18 c 6 -8 -6 -14 0 -24" fill="none" stroke="#E8E2D6" stroke-width="2.4" opacity="0.7"></path>'
    return o + "</g>"

def strange_fire(p, w, h, seed):
    """Nadab and Abihu took each of them his censer, and offered strange fire before Jehovah: two priests at the door of the tent."""
    b = h * 0.9; s = fit(b, h * 0.36)
    o = [mk.defs(p, *A_ALL), ground(w, h, h * 0.6, "#C8B080", dy=0), V.tabernacle(w * 0.62, h * 0.66, w * 0.6, uid=p + "tn")]
    for i, x in enumerate((0.36, 0.5)):
        o.append(sp(p, w * x, b, s, up=REACH) + censer(w * x + 30 * s, b - 126 * s, s * 0.8))
    return "".join(o)

def censers_fallen(w, h, seed):
    """Fire came forth and devoured them: only the two censers on the ground, overturned, under the fire (no one is shown)."""
    b = h * 0.84
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A0A0A"></rect>' + V.rays(w * 0.5, -40, 30, 20, h * 1.4, color="#FF8A3D", op=0.4)
            + ground(w, h, b, "#4A2A1E", dy=0) + E.blaze(w * 0.5, b, w * 0.5, h * 0.5, seed, n=10)
            + censer(w * 0.36, b + 6, min(1.8, h / 160), fire=False, fallen=True) + censer(w * 0.6, b + 8, min(1.8, h / 160), fire=False, fallen=True))

def carried(p, w, h, seed):
    """Mishael and Elzaphan carried them in their coats out of the camp: two pairs of bearers, far off, with two wrapped shapes."""
    b = h * 0.86
    o = [mk.defs(p, *A_ALL), sun(w * 0.86, h * 0.3, 18, color="#FF8A3D", op=0.3), hills(w, h, b - 8, seed, color="#4A3A4E", amp=8), ground(w, h, b, "#5A4A4E", dy=0)]
    o += [A.black_tent(w * x, b, w * 0.1, h * 0.14) for x in (0.08, 0.2)]
    for k, x in enumerate((0.52, 0.76)):
        s = fit(b, h * 0.5)
        o.append(man(p, w * x - 30 * s, b, s, "#6A5A4E", up=[(-22, -158), (-6, -150), (14, -150)]) + man(p, w * x + 50 * s, b, s, "#6A5A4E", flip=True, up=[(-22, -158), (-6, -150), (14, -150)]))
        o.append(f'<path d="M{f(w * x - 20 * s)} {f(b - 150 * s)} C {f(w * x)} {f(b - 168 * s)} {f(w * x + 30 * s)} {f(b - 168 * s)} {f(w * x + 40 * s)} {f(b - 150 * s)} Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def wine(w, h, seed):
    """Drink no wine nor strong drink when ye go into the tent of meeting: a cup and a wine-skin under a red bar, the tent door."""
    cx = w * 0.7
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#12113A"></rect>' + door(w * 0.92, h * 0.86, h / 90)
            + f'<path d="M{f(cx - 26)} {f(h * 0.5)} L {f(cx + 6)} {f(h * 0.5)} L {f(cx - 2)} {f(h * 0.66)} L {f(cx - 18)} {f(h * 0.66)} Z" fill="#8A1E3A" stroke="#0D0D0F" stroke-width="2"></path>'
            + f'<path d="M{f(cx - 10)} {f(h * 0.66)} L {f(cx - 10)} {f(h * 0.76)} M{f(cx - 26)} {f(h * 0.78)} L {f(cx + 6)} {f(h * 0.78)}" stroke="#E8B830" stroke-width="3"></path>'
            + jar(cx + 50, h * 0.78, h / 110, color="#6A2A3A") + ban(cx + 10, h * 0.62, min(w, h) * 0.22))

def goat_burnt(w, h, seed):
    """Moses diligently sought the goat of the sin-offering, and, behold, it was burnt: ashes smoking on the altar."""
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A2E"></rect>' + ground(w, h, h * 0.86, "#4A3A3E", dy=0)
            + altar(w * 0.5, h * 0.86, min(2.6, h / 110), fire=False)
            + f'<path d="M{f(w * 0.5)} {f(h * 0.4)} c 14 -20 -14 -40 0 -60 c 14 -20 -10 -40 4 -60" fill="none" stroke="#8A8478" stroke-width="10" opacity="0.6" stroke-linecap="round"></path>')

# ---- Leviticus 11 pictograms -------------------------------------------------------------------------------------
def hoof(x, y, s=1.0, cloven=True):
    """A hoof seen from below: cloven (two toes) or whole."""
    if cloven:
        return (f'<path d="M{f(x - 2 * s)} {f(y)} C {f(x - 14 * s)} {f(y)} {f(x - 14 * s)} {f(y - 22 * s)} {f(x - 2 * s)} {f(y - 22 * s)} Z" fill="#3A2214" stroke="#0D0D0F" stroke-width="1.4"></path>'
                f'<path d="M{f(x + 2 * s)} {f(y)} C {f(x + 14 * s)} {f(y)} {f(x + 14 * s)} {f(y - 22 * s)} {f(x + 2 * s)} {f(y - 22 * s)} Z" fill="#3A2214" stroke="#0D0D0F" stroke-width="1.4"></path>')
    return f'<path d="M{f(x - 12 * s)} {f(y)} C {f(x - 14 * s)} {f(y - 24 * s)} {f(x + 14 * s)} {f(y - 24 * s)} {f(x + 12 * s)} {f(y)} Z" fill="#3A2214" stroke="#0D0D0F" stroke-width="1.4"></path>'

def creature(kind, x, y, s=1.0, color=None):
    """Small creatures in profile, facing right: hare, coney, swine, weasel, mouse, lizard, eel, fish, bat."""
    P = {"hare": ("M-24 0 C -28 -16 -10 -24 8 -20 C 14 -30 18 -44 22 -44 C 24 -40 22 -30 20 -22 C 28 -20 30 -10 24 -4 L 20 0 Z", "#B8A07A"),
         "coney": ("M-22 0 C -26 -18 -4 -24 12 -18 C 22 -16 26 -8 22 0 Z", "#8A6A4A"),
         "swine": ("M-30 0 L -30 -8 C -30 -26 10 -30 24 -20 L 34 -16 L 34 -8 L 24 -6 L 22 0 Z", "#D8A090"),
         "weasel": ("M-36 -2 C -30 -10 -10 -12 10 -10 C 18 -14 26 -12 28 -6 L 22 -2 Z", "#8A5A30"),
         "mouse": ("M-14 0 C -16 -12 0 -16 10 -10 L 18 -6 L 10 0 Z M-14 -2 C -24 -2 -30 4 -36 0", "#7A7A80"),
         "lizard": ("M-34 0 C -20 -4 -10 -8 0 -8 C 10 -8 18 -6 26 -2 C 18 2 10 2 0 2 C -10 2 -20 4 -34 0 Z", "#7A9A5A"),
         "eel": ("M-36 -4 C -20 -14 -4 6 10 -4 C 20 -12 28 -8 34 -6 C 28 -2 20 -4 10 2 C -4 12 -20 -8 -36 -4 Z", "#4A5A6A"),
         "fish": ("M-30 -4 L -40 -14 L -40 6 Z M-30 -4 C -20 -18 10 -18 26 -4 C 10 10 -20 10 -30 -4 Z", "#8FB8C8"),
         "bat": ("M0 -6 C -10 -20 -30 -22 -40 -10 C -30 -12 -24 -6 -20 0 C -14 -4 -6 -2 0 4 C 6 -2 14 -4 20 0 C 24 -6 30 -12 40 -10 C 30 -22 10 -20 0 -6 Z", "#3A3440")}
    d, c = P[kind]
    extra = ""
    if kind == "fish": extra = "".join(f'<path d="M{-14 + i * 8} -6 a 4 4 0 0 1 8 0" fill="none" stroke="#0D0D0F" stroke-width="0.8"></path>' for i in range(4)) + '<path d="M-6 -14 L 2 -22 L 6 -12 Z" fill="#8FB8C8" stroke="#0D0D0F" stroke-width="1"></path>'
    if kind == "swine": extra = '<path d="M-22 0 L -22 6 M-10 0 L -10 6 M8 0 L 8 6 M18 0 L 18 6" stroke="#0D0D0F" stroke-width="2.4"></path>'
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="{d}" fill="{color or c}" stroke="#0D0D0F" stroke-width="1.4" fill-rule="evenodd"></path>{extra}'
            + ('<circle cx="16" cy="-12" r="1.4" fill="#0D0D0F"></circle>' if kind not in ("eel", "bat", "lizard") else "") + '</g>')

def raptor(x, y, s=1.0, kind="eagle"):
    """Birds of prey and water-birds in silhouette."""
    P = {"eagle": "M-40 -6 C -24 -20 -8 -18 0 -8 C 8 -18 24 -20 40 -6 C 26 -10 14 -6 6 0 C 4 8 -4 8 -6 0 C -14 -6 -26 -10 -40 -6 Z",
         "owl": "M-12 0 C -16 -18 -12 -34 0 -34 C 12 -34 16 -18 12 0 Z M-10 -32 L -12 -40 L -4 -34 M10 -32 L 12 -40 L 4 -34",
         "stork": "M-10 -20 C -16 -26 -4 -32 6 -28 L 10 -40 L 14 -40 L 12 -28 L 30 -26 L 12 -24 C 10 -16 0 -14 -10 -20 Z M-2 -16 L -4 0 M4 -16 L 6 0",
         "raven": "M-24 -10 C -20 -20 0 -24 14 -18 L 26 -16 L 14 -12 C 6 -4 -10 -2 -24 -10 Z M-2 -6 L -4 2 M4 -6 L 4 2"}
    return f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="{P[kind]}" fill="#2A2430" stroke="#8FD0E2" stroke-width="1.2" fill-rule="evenodd"></path></g>'

def pg_beasts_clean(p):  return GND + S1.cow(90, 84, 0.36, color="#8A5A30", patch="#5A3A22") + E.sheep(170, 84, 0.34) + hoof(236, 84, 1.4) + label(236, 96, "CLOVEN · CHEWETH THE CUD", B8.CY, 6.5)
def pg_camel(p):         return GND + J1.camel(110, 84, 0.42) + hoof(236, 84, 1.4, cloven=False) + ban(236, 50, 30)
def pg_coney_hare(p):    return GND + creature("coney", 80, 84, 1.4) + creature("hare", 170, 84, 1.4) + ban(260, 50, 30)
def pg_swine(p):         return GND + creature("swine", 120, 84, 1.6) + hoof(220, 84, 1.4) + ban(270, 50, 26)
def pg_fins(p):          return GND + creature("fish", 110, 60, 1.8) + label(110, 96, "FINS AND SCALES", B8.CY, 8) + creature("eel", 240, 60, 1.6) + ban(240, 56, 36)
def pg_birds(p):         return GND + raptor(70, 50, 1.2) + raptor(150, 70, 1.0, "raven") + raptor(220, 80, 1.1, "owl") + raptor(280, 80, 1.0, "stork") + ban(160, 50, 44)
def pg_bat(p):           return GND + raptor(90, 60, 0.9, "stork") + raptor(170, 80, 0.9, "owl") + creature("bat", 250, 50, 1.4) + ban(170, 50, 44)
def pg_locusts(p):       return GND + E2.locust(90, 60, 1.2) + E2.locust(170, 70, 1.0, rot=-10) + E2.locust(250, 60, 1.1, rot=8) + label(160, 96, "LEGS ABOVE THEIR FEET · TO LEAP", B8.CY, 7)
def pg_four_feet(p):     return GND + E2.fly(110, 50, 2.0) + E2.fly(170, 60, 1.6) + ban(150, 50, 40)
def pg_wash_even(p):     return GND + man(p, 80, 86, 0.36, "#5A3A22") + '<path d="M140 70 C 150 60 170 60 180 70 L 176 84 L 144 84 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.4"></path>' + sun(260, 70, 12, color="#FF8A3D", op=0.3) + label(260, 96, "UNTIL THE EVEN", B8.CY, 8)
def pg_paws(p):          return GND + creature("weasel", 110, 84, 1.6) + '<path d="M210 84 l -8 -10 m 8 10 l 0 -12 m 0 12 l 8 -10" stroke="#3A2214" stroke-width="3"></path>' + ban(250, 50, 30)
def pg_creeping(p):      return GND + creature("weasel", 80, 84, 1.2) + creature("mouse", 160, 84, 1.4) + creature("lizard", 240, 84, 1.4) + ban(160, 50, 44)
def pg_vessels(p):       return (GND + '<path d="M70 84 L 74 54 L 110 54 L 114 84 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.6"></path><path d="M78 60 L 96 76 L 104 62" fill="none" stroke="#0D0D0F" stroke-width="2"></path>'
                                  + '<rect x="150" y="56" width="50" height="28" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="1.6"></rect><path d="M230 84 C 230 70 280 70 280 84 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.4"></path>'
                                  + label(92, 96, "EARTHEN · BROKEN", B8.CY, 7) + label(175, 96, "WOOD · WASHED", B8.CY, 7) + label(255, 96, "RAIMENT", B8.CY, 7))
def pg_oven_broken(p):   return GND + '<path d="M90 84 C 88 46 150 46 148 84 Z" fill="#A85A32" stroke="#0D0D0F" stroke-width="1.8"></path><path d="M110 50 L 120 66 L 112 84" stroke="#0D0D0F" stroke-width="2.4" fill="none"></path>' + creature("mouse", 220, 84, 1.4)
def pg_fountain(p):      return GND + '<ellipse cx="120" cy="80" rx="60" ry="10" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="1.6"></ellipse>' + label(120, 96, "A FOUNTAIN · A PIT · CLEAN", B8.CY, 7) + "".join(f'<circle cx="{220 + i * 12}" cy="80" r="3" fill="#C8A06A" stroke="#0D0D0F" stroke-width="0.8"></circle>' for i in range(6)) + label(250, 96, "SOWING SEED", B8.CY, 7)
def pg_carcass(p):       return GND + man(p, 80, 86, 0.36, "#5A3A22") + '<path d="M140 84 C 150 72 200 72 210 84 Z" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="1.4"></path>' + label(260, 50, "UNCLEAN UNTIL THE EVEN", "#FFD23F", 7.5)
def pg_belly(p):         return GND + creature("lizard", 80, 84, 1.4) + '<path d="M160 80 C 180 70 200 90 220 80 C 240 70 250 82 266 78" fill="none" stroke="#5A6A3A" stroke-width="6" stroke-linecap="round"></path>' + ban(170, 50, 44)
def pg_holy(p):          return GND + "".join(A.black_tent(40 + i * 60, 84, 46, 30) for i in range(5)) + V.rays(160, 0, 20, 10, 80, color="#FFF4C2", op=0.3) + label(160, 22, "BE YE HOLY; FOR I AM HOLY", "#FFD23F", 9)
def pg_egypt(p):         return GND + A.EG.pyramid(70, 84, 80, 50) + Z.route([(120, 70), (260, 70)], color="#FFD23F", sw=2.4) + "".join(A.black_tent(220 + i * 30, 84, 26, 18) for i in range(3))
def pg_distinction(p):   return GND + S1.cow(70, 84, 0.3, color="#8A5A30", patch="#5A3A22") + creature("fish", 140, 60, 1.2) + '<path d="M180 20 L 180 96" stroke="#FFD23F" stroke-width="2" stroke-dasharray="5 4"></path>' + creature("swine", 230, 84, 1.0) + creature("eel", 280, 60, 1.0)
