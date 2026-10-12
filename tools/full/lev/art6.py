"""Drawings for Leviticus chapter 6 (Leviticus 16–18): the Day of Atonement as blueprint panels (the linen garments, the
two goats and the lots, the cloud of incense over the mercy-seat, the goat for Azazel led into a solitary land), and the
pictograms for the laws of the blood (17) and of the forbidden degrees (18).

Leviticus 18 is drawn only as a technical kinship chart: a family tree in which the forbidden relation is a red line
crossed out. No bodies, no figures for 18:22–23 (a plain red bar)."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, samuel1 as S1
from genesis import art2 as Y, art10 as T
from genesis.art2 import fit, ground, hills
from genesis.art3 import label, man, woman
from exo import art as A, art8 as B8, art9 as Q
from exo.art6 import GND
from exo.art7 import ban
from lev.art import altar, door, priest, offerer, goat, REACH, A_ALL
def f(v): return f"{v:.1f}"
CY, GOLD = B8.CY, B8.GOLD

def linen_priest(p, x, y, s, flip=False, up=None):
    """Aaron in the holy linen garments of the Day of Atonement: white coat, linen girdle and mitre."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#A8704E", cloth="#F3EFE6", sw=3, flip=flip, up=up,
                     extra='<path d="M-20 -110 L 20 -110" stroke="#E8E2D6" stroke-width="6"></path><path d="M-14 -192 C -16 -212 16 -212 14 -192 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></path>' + A.GREY_BEARD)

def floor(w, h, p):
    b = h * 0.9
    return b, [B8.bp(w, h), f'<path d="M{f(w * 0.5)} {f(b)} L {f(w)} {f(b)}" stroke="{CY}" stroke-width="1.6"></path>', mk.defs(p, *A_ALL)]

def b_linen(w, h, p="d1"):
    b, o = floor(w, h, p)
    o.append(linen_priest(p, w * 0.74, b, min(1.2, (b - h * 0.18) / 205)))
    o.append(B8.tag(w * 0.74, b - 205 * min(1.2, (b - h * 0.18) / 205) + 10, "THE LINEN MITRE", w * 0.96, h * 0.16) + B8.tag(w * 0.74 + 18, b - 110 * min(1.2, (b - h * 0.18) / 205), "THE LINEN GIRDLE", w * 0.96, h * 0.5))
    return "".join(o) + B8.title_bar(w, "THE HOLY LINEN GARMENTS")

def b_cloud(w, h, p="d2"):
    """I will appear in the cloud upon the mercy-seat: the mercy-seat behind the veil, a bright cloud over it."""
    return (B8.bp(w, h) + B8.title_bar(w, "WITHIN THE VEIL · THE CLOUD UPON THE MERCY-SEAT") + B8.mercy_seat(w, h, grid=False, cx=0.74, scale=0.7)
            + "".join(f'<circle cx="{f(w * (0.64 + 0.06 * i))}" cy="{f(h * (0.36 + 0.04 * (i % 2)))}" r="{f(h * 0.1)}" fill="#F3EFE6" opacity="0.75"></circle>' for i in range(4)))

def b_goats(w, h, p="d3", lots=False):
    """Two he-goats set before Jehovah at the door of the tent; with lots=True, the two lots: FOR JEHOVAH, FOR AZAZEL."""
    b, o = floor(w, h, p)
    s = min(1.7, h / 280)
    o += [goat(w * 0.64, b, s), goat(w * 0.86, b, s, color="#3A2A1E")]
    if lots:
        for x, t in ((0.66, "FOR JEHOVAH"), (0.86, "FOR AZAZEL")):
            o.append(f'<rect x="{f(w * x - 44)}" y="{f(b - 130 * s - 30)}" width="88" height="22" fill="#12113A" stroke="#FFD23F" stroke-width="1.6"></rect>' + label(w * x, b - 130 * s - 14, t, "#FFD23F", 9))
    return "".join(o) + B8.title_bar(w, "TWO HE-GOATS" + (" · THE LOTS" if lots else ""))

def b_bullock(w, h, p="d4"):
    b, o = floor(w, h, p)
    o.append(S1.cow(w * 0.74, b, min(0.9, h / 250), color="#5A3A22", patch="#3A2214") + E.sheep(w * 0.92, b, min(0.7, h / 300)))
    return "".join(o) + B8.title_bar(w, "A YOUNG BULLOCK · A RAM")

def b_censer(w, h, p="d5"):
    """A censer full of coals and his hands full of sweet incense beaten small, within the veil."""
    from lev.art3 import censer
    b, o = floor(w, h, p)
    s = min(1.1, (b - h * 0.2) / 205)
    o.append(linen_priest(p, w * 0.66, b, s, up=REACH) + censer(w * 0.66 + 34 * s, b - 120 * s, s * 1.2))
    o.append(f'<path d="M{f(w * 0.82)} {f(b)} L {f(w * 0.82)} {f(b - 180 * s)}" stroke="{B8.SCARLET}" stroke-width="8"></path>' + B8.tag(w * 0.82, b - 100 * s, "THE VEIL", w * 0.96, h * 0.3))
    o += [f'<circle cx="{f(w * (0.74 + 0.04 * i))}" cy="{f(b - 190 * s + (i % 2) * 14)}" r="{f(18 * s)}" fill="#F3EFE6" opacity="0.6"></circle>' for i in range(4)]
    return "".join(o) + B8.title_bar(w, "THE CLOUD OF THE INCENSE")

def b_sprinkle(w, h, p="d6"):
    """Sprinkle of the blood upon the mercy-seat on the east, and before the mercy-seat seven times."""
    o = [B8.bp(w, h), B8.title_bar(w, "UPON THE MERCY-SEAT · SEVEN TIMES"), B8.mercy_seat(w, h, grid=False, cx=0.72, scale=0.6)]
    o += [f'<circle cx="{f(w * 0.56 + i * 14)}" cy="{f(h * 0.86)}" r="4" fill="#B5121B"></circle>' for i in range(7)]
    o.append(label(w * 0.6, h * 0.95, "EAST", CY, 9) + label(w * 0.66, h * 0.79, "7", "#FFD23F", 12))
    return "".join(o)

def b_no_man(w, h, p="d7"):
    """No man in the tent of meeting when he goeth in: the tent with one figure within, the court empty."""
    return (B8.bp(w, h) + B8.title_bar(w, "NO MAN IN THE TENT OF MEETING") + V.tabernacle(w * 0.74, h * 0.86, min(w * 0.44, h * 1.2), uid=p)
            + label(w * 0.74, h * 0.95, "UNTIL HE COME OUT", CY, 9))

def b_altar_blood(w, h, p="d8"):
    from lev.art import altar as L_altar
    b, o = floor(w, h, p)
    o.append(L_altar(w * 0.76, b, min(3.0, h / 90)) + "".join(f'<circle cx="{f(w * 0.62 + i * 12)}" cy="{f(b - 10)}" r="3.6" fill="#B5121B"></circle>' for i in range(7)))
    return "".join(o) + B8.title_bar(w, "THE ALTAR · THE HORNS · SEVEN TIMES")

def b_confess(w, h, p="d9"):
    """Aaron shall lay both his hands upon the head of the live goat, and confess over him all the iniquities."""
    b, o = floor(w, h, p)
    s = min(1.0, (b - h * 0.24) / 205)
    o.append(goat(w * 0.84, b, min(1.4, h / 280), color="#3A2A1E") + linen_priest(p, w * 0.62, b, s, up=[(-22, -158), (4, -120), (30, -100)]))
    return "".join(o) + B8.title_bar(w, "THE LIVE GOAT · ALL THEIR INIQUITIES")

def b_wilderness(w, h, p="da"):
    """The goat shall bear upon him all their iniquities unto a solitary land: a man leading the goat into the wilderness."""
    b = h * 0.9
    o = [mk.defs(p, *A_ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#C8A06A"></rect>', Y.ground(w, h, h * 0.56, "#E8C88A", dy=0),
         hills(w, h, h * 0.56, 4, color="#B5652E", amp=12), f'<circle cx="{f(w * 0.86)}" cy="{f(h * 0.2)}" r="18" fill="#FFF4C2"></circle>']
    s = fit(b, h * 0.5)
    o.append(man(p, w * 0.64, b, s, "#6A5A4E", up=[(-22, -158), (4, -140), (26, -120)]) + goat(w * 0.78, b, s * 1.1, color="#3A2A1E"))
    o.append(label(w * 0.75, h * 0.96, "UNTO A SOLITARY LAND", "#5A3A22", 10))
    return "".join(o)

def b_bathe(w, h, p="db"):
    b, o = floor(w, h, p)
    o.append(Q.laver_shape(w * 0.62, b, min(1.0, h / 260)) + Q.high_priest(p, w * 0.84, b, min(1.1, (b - h * 0.2) / 205), flip=True))
    return "".join(o) + B8.title_bar(w, "HE SHALL BATHE · AND PUT ON HIS GARMENTS")

def b_without(w, h, p="dc"):
    return (B8.bp(w, h) + B8.title_bar(w, "WITHOUT THE CAMP") + "".join(A.black_tent(w * (0.56 + i * 0.07), h * 0.88, w * 0.06, h * 0.1) for i in range(3))
            + f'<path d="M{f(w * 0.78)} {f(h * 0.3)} L {f(w * 0.78)} {f(h * 0.94)}" stroke="#FFD23F" stroke-width="2" stroke-dasharray="6 5"></path>' + E.blaze(w * 0.9, h * 0.88, w * 0.1, h * 0.3, 6, n=6))

def b_tenth(w, h, p="dd"):
    """The seventh month, the tenth day: a calendar strip with the tenth day ringed."""
    o = [B8.bp(w, h), B8.title_bar(w, "THE SEVENTH MONTH · THE TENTH DAY")]
    cw = w * 0.4 / 10
    for d in range(1, 11):
        x = w * 0.56 + (d - 1) * cw
        o.append(f'<rect x="{f(x + 2)}" y="{f(h * 0.44)}" width="{f(cw - 4)}" height="{f(min(cw, 40))}" fill="{"#FFD23F" if d == 10 else "#12113A"}" stroke="{"#D7261E" if d == 10 else "#2C9DB8"}" stroke-width="{3 if d == 10 else 1.2}"></rect>'
                 + label(x + cw / 2, h * 0.44 + min(cw, 40) / 2 + 5, str(d), "#0D0D0F" if d == 10 else CY, 11))
    o.append(label(w * 0.76, h * 0.7, "A SABBATH OF SOLEMN REST", "#FFD23F", 10))
    return "".join(o)

def b_once(w, h, p="de"):
    return (B8.bp(w, h) + B8.title_bar(w, "ONCE IN THE YEAR · AN EVERLASTING STATUTE") + B8.mercy_seat(w, h, grid=False, cx=0.74, scale=0.6)
            + label(w * 0.74, h * 0.96, "1 / YEAR", "#FFD23F", 12))

# ---- Leviticus 17 pictograms ----
def pg_door_only(p):  return GND + S1.cow(80, 84, 0.3, color="#8A5A30", patch="#5A3A22") + E3.lamb(140, 84, 0.3) + goat(190, 84, 0.3) + door(270, 84) + '<path d="M210 60 L 245 60" stroke="#FFD23F" stroke-width="2"></path><path d="M245 60 l -8 -5 l 0 10 Z" fill="#FFD23F"></path>'
def pg_field(p):      return GND + Y.ground(320, 100, 84, "#4A6A3A", dy=0) + offerer(p, 80) + E3.lamb(140, 84, 0.34) + '<path d="M170 60 L 240 60" stroke="#FFD23F" stroke-width="2" stroke-dasharray="5 4"></path>' + door(270, 84)
def pg_he_goats(p):   return GND + goat(110, 84, 0.42, color="#3A2A1E") + goat(170, 84, 0.42, color="#3A2A1E", flip=True) + ban(140, 50, 44)
def pg_stranger(p):   return GND + T.figure(p, ("man", "#7A5A3A"), 90, 86, 0.36, pose="staff") + E3.lamb(150, 84, 0.34) + door(250, 84)
def pg_life_blood(p): return GND + altar(110, 84, 1.3) + '<path d="M200 70 C 200 50 230 30 230 30 C 230 30 260 50 260 70 C 260 86 200 86 200 70 Z" fill="#B5121B" stroke="#0D0D0F" stroke-width="1.6"></path>' + label(230, 96, "THE LIFE OF THE FLESH IS IN THE BLOOD", CY, 6.5)
def pg_cover_dust(p): return GND + man(p, 80, 86, 0.36, "#5A3A22") + '<path d="M150 84 C 160 66 210 66 220 84 Z" fill="#C8A06A" stroke="#0D0D0F" stroke-width="1.6"></path>' + label(185, 96, "COVER IT WITH DUST", CY, 7) + E2_birds()
def E2_birds():       return '<path d="M250 40 q 6 -8 12 0 q 6 -8 12 0" fill="none" stroke="#F3EFE6" stroke-width="2"></path><path d="M270 60 q 5 -6 10 0 q 5 -6 10 0" fill="none" stroke="#F3EFE6" stroke-width="2"></path>'
def pg_torn_wash(p):  return GND + '<path d="M60 84 C 70 70 110 70 120 84 Z" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="1.4"></path>' + E3.basin(180, 82, 30) + label(250, 50, "UNCLEAN UNTIL THE EVEN", "#FFD23F", 7.5)

# ---- Leviticus 18: kinship charts ----
def kin(nodes, edges, bad, title=""):
    """A family-tree chart. nodes: {key: (x, y, label, sex)}; edges: [(a, b)] family lines; bad: (a, b) the forbidden pair."""
    o = [GND]
    for a, b in edges:
        (x1, y1, _, _), (x2, y2, _, _) = nodes[a], nodes[b]
        o.append(f'<path d="M{f(x1)} {f(y1)} L {f(x2)} {f(y2)}" stroke="{CY}" stroke-width="1.6"></path>')
    if bad:
        (x1, y1, _, _), (x2, y2, _, _) = nodes[bad[0]], nodes[bad[1]]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        o.append(f'<path d="M{f(x1)} {f(y1)} C {f(mx)} {f(my - 26)} {f(mx)} {f(my - 26)} {f(x2)} {f(y2)}" fill="none" stroke="#D7261E" stroke-width="2.4" stroke-dasharray="5 3"></path>'
                 + f'<g transform="translate({f(mx)} {f(my - 20)})"><circle r="9" fill="#12113A" stroke="#D7261E" stroke-width="2.4"></circle><path d="M-5 -5 L 5 5 M5 -5 L -5 5" stroke="#D7261E" stroke-width="2.4"></path></g>')
    for k, (x, y, t, sex) in nodes.items():
        me = k == "me"
        shape = (f'<rect x="{f(x - 8)}" y="{f(y - 8)}" width="16" height="16" fill="{"#FFD23F" if me else "#12113A"}" stroke="{CY}" stroke-width="1.6"></rect>' if sex == "m"
                 else f'<circle cx="{f(x)}" cy="{f(y)}" r="8" fill="#12113A" stroke="#E07A9A" stroke-width="1.6"></circle>')
        o.append(shape + label(x, y + 20, t, "#FFD23F" if me else CY, 7))
    if title: o.append(label(160, 10, title, "#FFD23F", 7.5))
    return "".join(o)

ME = (160, 70, "THOU", "m")
def pg_k_parents(p):  return kin({"f": (110, 22, "FATHER", "m"), "m": (210, 22, "MOTHER", "f"), "me": ME}, [("f", "me"), ("m", "me")], ("me", "m"))
def pg_k_fwife(p):    return kin({"f": (110, 22, "FATHER", "m"), "w": (230, 22, "FATHER'S WIFE", "f"), "me": ME}, [("f", "me"), ("f", "w")], ("me", "w"))
def pg_k_sister(p):   return kin({"f": (110, 18, "FATHER", "m"), "m": (210, 18, "MOTHER", "f"), "me": (120, 70, "THOU", "m"), "s": (220, 70, "SISTER", "f")}, [("f", "me"), ("m", "me"), ("f", "s"), ("m", "s")], ("me", "s"))
def pg_k_grand(p):    return kin({"me": (160, 18, "THOU", "m"), "s": (90, 50, "SON", "m"), "d": (230, 50, "DAUGHTER", "f"), "sd": (90, 84, "SON'S DAUGHTER", "f"), "dd": (230, 84, "DAUGHTER'S DAUGHTER", "f")},
                             [("me", "s"), ("me", "d"), ("s", "sd"), ("d", "dd")], ("me", "sd"))
def pg_k_half(p):     return kin({"f": (160, 18, "FATHER", "m"), "w": (250, 18, "HIS WIFE", "f"), "me": (100, 70, "THOU", "m"), "s": (230, 70, "HER DAUGHTER", "f")}, [("f", "me"), ("f", "w"), ("w", "s"), ("f", "s")], ("me", "s"))
def pg_k_aunts(p):    return kin({"gf": (160, 14, "", "m"), "f": (90, 44, "FATHER", "m"), "a": (230, 44, "FATHER'S SISTER", "f"), "me": (90, 84, "THOU", "m")}, [("gf", "f"), ("gf", "a"), ("f", "me")], ("me", "a"))
def pg_k_maunt(p):    return kin({"gm": (160, 14, "", "f"), "m": (90, 44, "MOTHER", "f"), "a": (230, 44, "MOTHER'S SISTER", "f"), "me": (90, 84, "THOU", "m")}, [("gm", "m"), ("gm", "a"), ("m", "me")], ("me", "a"))
def pg_k_uncle(p):    return kin({"f": (90, 30, "FATHER", "m"), "u": (190, 30, "FATHER'S BROTHER", "m"), "w": (280, 30, "HIS WIFE", "f"), "me": (90, 80, "THOU", "m")}, [("f", "me"), ("f", "u"), ("u", "w")], ("me", "w"))
def pg_k_dil(p):      return kin({"me": (90, 24, "THOU", "m"), "s": (90, 80, "SON", "m"), "w": (230, 80, "HIS WIFE", "f")}, [("me", "s"), ("s", "w")], ("me", "w"))
def pg_k_bwife(p):    return kin({"me": (90, 70, "THOU", "m"), "b": (190, 70, "BROTHER", "m"), "w": (280, 70, "HIS WIFE", "f"), "f": (140, 20, "", "m")}, [("f", "me"), ("f", "b"), ("b", "w")], ("me", "w"))
def pg_k_wdaughter(p): return kin({"me": (90, 24, "THOU", "m"), "w": (230, 24, "A WOMAN", "f"), "d": (230, 80, "HER DAUGHTER", "f")}, [("me", "w"), ("w", "d")], ("me", "d"))
def pg_k_sisters(p):  return kin({"me": (90, 70, "THOU", "m"), "w": (190, 70, "WIFE", "f"), "s": (280, 70, "HER SISTER", "f"), "m": (235, 20, "", "f")}, [("me", "w"), ("m", "w"), ("m", "s")], ("me", "s"))
def pg_impure(p):     return GND + label(160, 50, "AS LONG AS SHE IS IMPURE", "#FFD23F", 10) + ban(160, 50, 40)
def pg_neighbor(p):   return kin({"me": (90, 60, "THOU", "m"), "n": (190, 60, "NEIGHBOR", "m"), "w": (280, 60, "HIS WIFE", "f")}, [("n", "w")], ("me", "w"))
def pg_molech(p):     return GND + E.blaze(160, 84, 70, 60, 3, n=7) + ban(160, 52, 44) + label(160, 96, "MOLECH", CY, 8)
def pg_abomination(p): return GND + '<rect x="70" y="40" width="180" height="20" fill="#D7261E"></rect>' + label(160, 78, "ABOMINATION · CONFUSION", "#FFD23F", 9)
def pg_vomit(p):      return (GND + '<path d="M40 84 L 90 50 L 130 66 L 180 40 L 230 64 L 280 52 L 300 84 Z" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="1.6"></path>'
                              + "".join(A.black_tent(70 + i * 50, 84, 30, 18, color="#5A4A4E") for i in range(4)) + '<path d="M290 60 L 314 60" stroke="#D7261E" stroke-width="3"></path><path d="M314 60 l -8 -5 l 0 10 Z" fill="#D7261E"></path>'
                              + label(160, 96, "THE LAND VOMITETH OUT HER INHABITANTS", "#FFD23F", 7))
def pg_keep(p):       return GND + "".join(A.black_tent(40 + i * 60, 84, 46, 30) for i in range(5)) + label(160, 22, "I AM JEHOVAH YOUR GOD", "#FFD23F", 9)
def pg_egypt_canaan(p): return GND + A.EG.pyramid(60, 84, 70, 46) + ban(60, 54, 30) + A.black_tent(160, 84, 40, 24) + '<path d="M240 84 L 260 50 L 280 84 Z" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="1.4"></path>' + ban(260, 60, 26) + label(60, 96, "EGYPT", CY, 7) + label(260, 96, "CANAAN", CY, 7)
def pg_live(p):       return GND + man(p, 160, 86, 0.38, "#5A3A22", up=T.POSES["raise"]) + label(250, 50, "HE SHALL LIVE IN THEM", "#FFD23F", 8)
def pg_near_kin(p):   return kin({"me": (160, 70, "THOU", "m"), "a": (70, 30, "NEAR OF KIN", "f"), "b": (250, 30, "NEAR OF KIN", "f")}, [], ("me", "a"))
