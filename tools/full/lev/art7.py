"""Pictograms for Leviticus chapter 7 (Leviticus 19–22): the holiness laws, the penalties of chapter 20 (drawn as the
kinship chart of chapter 18 with a red penalty bar: no executions are shown), the holiness of the priests, and the
blemishes (shown as the list, not as bodies)."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus5 as V, ruth1 as R, samuel1 as S1, numbers1 as N, judges1 as J1
from genesis import art2 as Y, art10 as T
from genesis.art3 import label, man, woman
from exo import art as A, art8 as B8, art9 as Q
from exo.art6 import GND
from exo.art7 import ban, coins
from lev.art import altar, door, priest, offerer, goat, dove, REACH, jar, flour
from lev.art6 import kin, ME
from lev.art4 import days
def f(v): return f"{v:.1f}"
CY = B8.CY

def penalty(svg, text="SURELY PUT TO DEATH"):
    """A kinship chart (or other pictogram) with the law's penalty as a red bar along the top."""
    return svg + f'<rect x="0" y="0" width="320" height="14" fill="#8A0E16"></rect>' + label(160, 10, text, "#F3EFE6", 8, ls=0.2)

# ---- Leviticus 19 ----
def pg_holy(p):        return GND + V.rays(160, 10, 24, 10, 120, color="#FFF4C2", op=0.3) + "".join(A.black_tent(40 + i * 60, 84, 46, 30) for i in range(5)) + label(160, 30, "YE SHALL BE HOLY", "#FFD23F", 11)
def pg_parents(p):     return GND + mk.person(p, 80, 86, 0.36, body="#A8704E", cloth="#5A3A22", sw=3, extra=Y.WHITE_BEARD) + woman(p, 120, 86, 0.34, "#5A6E8A") + days(170, 40, 7) + label(210, 70, "MY SABBATHS", CY, 8)
def pg_idols(p):       return GND + '<path d="M146 84 L 150 34 C 150 24 170 24 170 34 L 174 84 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path><circle cx="160" cy="22" r="10" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></circle>' + ban(160, 52, 40)
def pg_peace(p):       return GND + E3.lamb(80, 84, 0.4) + altar(170, 84, 1.0) + days(220, 40, 3, lit=2) + label(240, 70, "NOT THE THIRD DAY", CY, 7)
def pg_corners(p):     return (GND + R.field(20, 300, 80, 30, 7, rows=1) + '<rect x="20" y="40" width="40" height="44" fill="#E8C88A" opacity="0.4" stroke="#FFD23F" stroke-width="1.4" stroke-dasharray="4 3"></rect>'
                                + '<rect x="260" y="40" width="40" height="44" fill="#E8C88A" opacity="0.4" stroke="#FFD23F" stroke-width="1.4" stroke-dasharray="4 3"></rect>' + label(160, 96, "THE CORNERS · THE GLEANING · FOR THE POOR", CY, 7))
def pg_vineyard(p):    return GND + N.grapes(90, 24, 0.5) + N.grapes(140, 24, 0.5) + "".join(f'<circle cx="{180 + i * 14}" cy="82" r="5" fill="#6A2A6A" stroke="#0D0D0F" stroke-width="1"></circle>' for i in range(5)) + R.gleaner(270, 86, 0.36)
def pg_steal(p):       return GND + R.sack(110, 84, 0.8) + ban(110, 54, 34) + man(p, 220, 86, 0.36, "#5A3A22", up=T.POSES["raise"]) + ban(220, 44, 26)
def pg_wages(p):       return GND + man(p, 70, 86, 0.36, "#8A7A6A") + coins(120, 70, 5) + '<circle cx="250" cy="40" r="12" fill="#FF8A3D"></circle><path d="M200 84 L 300 84" stroke="#FF8A3D" stroke-width="2"></path>' + label(250, 70, "NOT UNTIL THE MORNING", CY, 7)
def pg_blind(p):       return GND + man(p, 120, 86, 0.36, "#6A6460", up=[(-22, -158), (-40, -126), (-56, -112)]) + '<rect x="170" y="74" width="30" height="10" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="1.4"></rect>' + ban(185, 64, 22) + label(160, 96, "THE DEAF · THE BLIND", CY, 7)
def pg_judgment(p):    return GND + '<path d="M160 18 L 160 80 M100 40 L 220 40" stroke="#E8B830" stroke-width="4"></path><path d="M140 82 L 180 82" stroke="#E8B830" stroke-width="5"></path>' + "".join(f'<path d="M{x - 22} 66 C {x - 22} 78 {x + 22} 78 {x + 22} 66 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path><path d="M{x} 40 L {x - 20} 66 M{x} 40 L {x + 20} 66" stroke="#E8B830" stroke-width="1.6"></path>' for x in (100, 220)) + label(100, 96, "THE POOR", CY, 7) + label(220, 96, "THE MIGHTY", CY, 7)
def pg_tale(p):        return GND + man(p, 80, 86, 0.34, "#5A3A22") + man(p, 160, 86, 0.34, "#4A3A6A", flip=True, up=T.POSES["point"]) + man(p, 240, 86, 0.34, "#6A5A3A", flip=True) + ban(160, 30, 18)
def pg_love(p):        return GND + man(p, 120, 86, 0.38, "#5A3A22", up=[(-22, -158), (4, -150), (30, -160)]) + man(p, 196, 86, 0.38, "#4A3A6A", flip=True, up=[(-22, -158), (4, -150), (30, -160)]) + label(160, 22, "AS THYSELF", "#FFD23F", 11)
def pg_diverse(p):     return GND + S1.cow(70, 84, 0.3, color="#8A5A30", patch="#5A3A22") + N.ass(130, 84, 0.22) + ban(100, 54, 30) + R.sheaf(200, 84, 0.5) + R.sheaf(220, 84, 0.5, color="#9CCB5E") + '<rect x="250" y="44" width="40" height="40" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.4"></rect><rect x="250" y="44" width="20" height="40" fill="#C8BCA6"></rect>'
def pg_bondmaid(p):    return GND + woman(p, 90, 86, 0.36, "#7A5A3A") + R.sack(150, 84, 0.6) + E.sheep(220, 84, 0.4) + door(290, 84, 0.8)
def pg_ram(p):         return GND + E.sheep(110, 84, 0.46) + altar(220, 84, 1.0)
def pg_trees(p):       return GND + "".join(f'<path d="M{x} 84 L {x} 50" stroke="#5A3A22" stroke-width="4"></path><circle cx="{x}" cy="44" r="16" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="1.4"></circle>' + label(x, 96, t, CY, 7) for x, t in ((60, "YEARS 1–3"), (160, "YEAR 4 · HOLY"), (260, "YEAR 5")))
def pg_augury(p):      return GND + '<path d="M80 50 a 20 20 0 1 0 40 0 a 20 20 0 1 0 -40 0" fill="#12113A" stroke="#8FD0E2" stroke-width="2"></path>' + label(100, 54, "✶", "#FFD23F", 14) + ban(100, 50, 30) + E3.basin(220, 70, 30) + ban(220, 60, 30)
def pg_corners_head(p): return GND + man(p, 120, 86, 0.38, "#5A3A22", flip=True) + '<path d="M180 30 L 210 30 M195 20 L 195 40" stroke="#D7261E" stroke-width="3"></path>' + label(220, 60, "THE CORNERS OF THY BEARD", CY, 7)
def pg_cuttings(p):    return GND + man(p, 120, 86, 0.38, "#5A3A22") + ban(200, 50, 30) + label(200, 90, "NO CUTTINGS · NO MARKS", CY, 7)
def pg_daughter(p):    return GND + woman(p, 120, 86, 0.36, "#C2456A") + mk.person(p, 80, 86, 0.38, body="#A8704E", cloth="#5A3A22", sw=3) + label(220, 50, "PROFANE NOT THY DAUGHTER", "#FFD23F", 8)
def pg_sanctuary(p):   return GND + days(40, 40, 7) + V.tabernacle(240, 84, 120, uid=p + "t")
def pg_wizards(p):     return GND + '<path d="M120 84 C 120 50 200 50 200 84 Z" fill="#2A2430" stroke="#8FD0E2" stroke-width="1.6"></path>' + label(160, 70, "✶ ✶", "#B07AE8", 12) + ban(160, 56, 40)
def pg_hoary(p):       return GND + mk.person(p, 110, 86, 0.38, body="#A8704E", cloth="#5A3A22", sw=3, extra=Y.WHITE_BEARD) + man(p, 210, 86, 0.36, "#4A3A6A", flip=True, up=T.POSES["raise"]) + label(160, 22, "RISE UP BEFORE THE HOARY HEAD", "#FFD23F", 7.5)
def pg_stranger(p):    return GND + T.figure(p, ("man", "#7A5A3A"), 110, 86, 0.36, pose="staff") + man(p, 200, 86, 0.36, "#5A3A22", flip=True, up=[(-22, -158), (4, -150), (30, -160)]) + label(160, 22, "AS THE HOME-BORN", "#FFD23F", 9)
def pg_weights(p):     return (GND + '<path d="M80 18 L 80 80 M40 34 L 120 34" stroke="#E8B830" stroke-width="3"></path>' + "".join(f'<path d="M{x - 16} 60 C {x - 16} 70 {x + 16} 70 {x + 16} 60 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path>' for x in (40, 120))
                                + flour(190, 84, 0.8) + label(190, 96, "EPHAH", CY, 7) + jar(260, 84, 0.8) + label(260, 96, "HIN", CY, 7))
def pg_observe(p):     return GND + "".join(A.black_tent(40 + i * 60, 84, 46, 30) for i in range(5)) + label(160, 22, "I AM JEHOVAH", "#FFD23F", 10)

# ---- Leviticus 20 ----
def pg_molech(p):      return penalty(GND + E.blaze(160, 84, 70, 56, 3, n=7) + ban(160, 54, 40) + label(160, 96, "MOLECH", CY, 8), "STONED WITH STONES")
def pg_face(p):        return GND + E.blaze(160, 84, 60, 50, 4, n=6) + "".join(A.black_tent(40 + i * 40, 84, 30, 20) for i in range(2)) + label(160, 22, "I WILL SET MY FACE AGAINST THAT MAN", "#FFD23F", 7.5)
def pg_spirits(p):     return penalty(pg_wizards(p), "CUT OFF")
def pg_sanctify(p):    return pg_holy(p)
def pg_curse(p):       return penalty(kin({"f": (110, 34, "FATHER", "m"), "m": (210, 34, "MOTHER", "f"), "me": (160, 80, "HE THAT CURSETH", "m")}, [("f", "me"), ("m", "me")], None))
def pg_adultery(p):    return penalty(kin({"me": (90, 64, "THE MAN", "m"), "n": (190, 64, "NEIGHBOR", "m"), "w": (280, 64, "HIS WIFE", "f")}, [("n", "w")], ("me", "w")))
def pg_fwife(p):       return penalty(kin({"f": (110, 34, "FATHER", "m"), "w": (230, 34, "FATHER'S WIFE", "f"), "me": (160, 80, "THE MAN", "m")}, [("f", "me"), ("f", "w")], ("me", "w")))
def pg_dil(p):         return penalty(kin({"me": (90, 34, "THE MAN", "m"), "s": (90, 84, "SON", "m"), "w": (230, 84, "HIS WIFE", "f")}, [("me", "s"), ("s", "w")], ("me", "w")))
def pg_mankind(p):     return penalty(GND + '<rect x="70" y="44" width="180" height="20" fill="#D7261E"></rect>' + label(160, 84, "ABOMINATION", "#FFD23F", 9))
def pg_wife_mother(p): return penalty(kin({"me": (90, 40, "THE MAN", "m"), "w": (220, 40, "A WIFE", "f"), "m": (220, 84, "HER MOTHER", "f")}, [("me", "w"), ("m", "w")], ("me", "m")), "BURNT WITH FIRE")
def pg_beast(p):       return penalty(GND + '<rect x="70" y="44" width="180" height="20" fill="#D7261E"></rect>' + label(160, 84, "AND YE SHALL SLAY THE BEAST", "#FFD23F", 8))
def pg_sister(p):      return penalty(kin({"f": (110, 30, "FATHER", "m"), "m": (210, 30, "MOTHER", "f"), "me": (120, 80, "THE MAN", "m"), "s": (220, 80, "SISTER", "f")}, [("f", "me"), ("m", "me"), ("f", "s"), ("m", "s")], ("me", "s")), "CUT OFF")
def pg_sickness(p):    return penalty(GND + label(160, 56, "HER SICKNESS", "#FFD23F", 10) + ban(160, 54, 40), "BOTH CUT OFF")
def pg_aunt(p):        return penalty(kin({"gf": (160, 30, "", "m"), "f": (90, 54, "FATHER", "m"), "a": (230, 54, "AUNT", "f"), "me": (90, 88, "THE MAN", "m")}, [("gf", "f"), ("gf", "a"), ("f", "me")], ("me", "a")), "THEY SHALL BEAR THEIR INIQUITY")
def pg_uncle_wife(p):  return penalty(kin({"f": (90, 40, "FATHER", "m"), "u": (190, 40, "UNCLE", "m"), "w": (280, 40, "HIS WIFE", "f"), "me": (90, 86, "THE MAN", "m")}, [("f", "me"), ("f", "u"), ("u", "w")], ("me", "w")), "THEY SHALL DIE CHILDLESS")
def pg_bwife(p):       return penalty(kin({"me": (90, 76, "THE MAN", "m"), "b": (190, 76, "BROTHER", "m"), "w": (280, 76, "HIS WIFE", "f"), "f": (140, 30, "", "m")}, [("f", "me"), ("f", "b"), ("b", "w")], ("me", "w")), "THEY SHALL BE CHILDLESS")
def pg_land(p):        return GND + A.milk_honey(None, 320, 100, 7)
def pg_distinction(p): return GND + S1.cow(70, 84, 0.3, color="#8A5A30", patch="#5A3A22") + dove(130, 80, 1.0) + '<path d="M170 20 L 170 96" stroke="#FFD23F" stroke-width="2" stroke-dasharray="5 4"></path>' + N.ass(230, 84, 0.22)
def pg_set_apart(p):   return GND + "".join(A.black_tent(30 + i * 34, 84, 28, 20) for i in range(4)) + '<path d="M170 20 L 170 96" stroke="#FFD23F" stroke-width="2" stroke-dasharray="5 4"></path>' + "".join(A.black_tent(200 + i * 40, 84, 30, 22, color="#5A4A4E") for i in range(3)) + label(90, 22, "MINE", "#FFD23F", 9)
def pg_familiar(p):    return penalty(pg_wizards(p), "STONED WITH STONES")

# ---- Leviticus 21–22: the priests ----
def pg_dead(p):        return GND + priest(p, 80) + '<path d="M150 84 C 160 70 230 70 240 84 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.4"></path>' + ban(195, 56, 30) + label(195, 96, "FOR THE DEAD", CY, 7)
def pg_kin(p):         return GND + priest(p, 70) + kin({"m": (150, 40, "MOTHER", "f"), "f": (190, 40, "FATHER", "m"), "s": (230, 40, "SON", "m"), "d": (270, 40, "DAUGHTER", "f"), "b": (210, 80, "BROTHER", "m"), "si": (260, 80, "SISTER", "f")}, [], None)[len(GND):]
def pg_baldness(p):    return GND + priest(p, 110) + '<path d="M160 30 L 200 30" stroke="#D7261E" stroke-width="3"></path>' + ban(230, 50, 30) + label(230, 90, "NO BALDNESS · NO CUTTINGS", CY, 7)
def pg_bread(p):       return GND + priest(p, 90) + E4_bread() + label(220, 96, "THE BREAD OF THEIR GOD", CY, 7)
def E4_bread():        return "".join(f'<ellipse cx="{170 + i * 18}" cy="{70 - (i % 2) * 6}" rx="14" ry="5" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.2"></ellipse>' for i in range(6))
def pg_wife(p):        return GND + priest(p, 100) + woman(p, 180, 86, 0.34, "#C2456A", flip=True) + label(250, 40, "HE SHALL BE HOLY", "#FFD23F", 8)
def pg_pdaughter(p):   return penalty(GND + priest(p, 100) + woman(p, 180, 86, 0.34, "#C2456A", flip=True), "BURNT WITH FIRE")
def pg_high(p):        return GND + Q.high_priest(p, 100, 86, 0.38) + S1.vial(106, 6, 0.5, rot=-120, pour=12) + label(220, 50, "THE CROWN OF THE ANOINTING OIL", "#FFD23F", 7.5)
def pg_hp_dead(p):     return GND + Q.high_priest(p, 90, 86, 0.38) + '<path d="M150 84 C 160 70 230 70 240 84 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.4"></path>' + ban(195, 56, 30) + label(195, 96, "NOT FOR HIS FATHER OR MOTHER", CY, 6.5)
def pg_hp_wife(p):     return GND + Q.high_priest(p, 100, 86, 0.38) + woman(p, 190, 86, 0.34, "#F3EFE6", flip=True) + label(250, 40, "A VIRGIN OF HIS OWN PEOPLE", "#FFD23F", 7)
def pg_blemish(p):     return (GND + priest(p, 70) + "".join(label(220, 18 + i * 13, t, CY, 7.5) for i, t in enumerate(["BLIND · LAME · FLAT NOSE", "ANYTHING SUPERFLUOUS", "BROKEN-FOOTED · BROKEN-HANDED", "CROOK-BACKED · A DWARF", "A BLEMISH IN HIS EYE", "SCURVY · SCABBED"])))
def pg_veil(p):        return GND + priest(p, 70) + '<path d="M150 20 L 150 84" stroke="#C8202A" stroke-width="8"></path>' + ban(200, 50, 30) + label(240, 92, "NOT IN UNTO THE VEIL", CY, 7)
def pg_eat_holy(p):    return GND + priest(p, 90) + E4_bread() + label(220, 96, "OF THE MOST HOLY, AND OF THE HOLY", CY, 6.5)
def pg_spake(p):       return GND + A.moses(p, 70, 86, 0.36, up=T.POSES["raise"]) + Q.high_priest(p, 140, 86, 0.36, flip=True) + "".join(priest(p, 180 + i * 30, flip=True) for i in range(4))
def pg_separate(p):    return GND + priest(p, 70) + E4_bread() + '<path d="M150 20 L 150 96" stroke="#FFD23F" stroke-width="2" stroke-dasharray="5 4"></path>' + label(220, 22, "SEPARATE THEMSELVES", "#FFD23F", 8)
def pg_leper_priest(p): return GND + priest(p, 70) + ban(130, 50, 24) + E4_bread() + label(220, 96, "UNTIL HE BE CLEAN", CY, 7)
def pg_sun_down(p):    return GND + priest(p, 70) + '<circle cx="190" cy="80" r="16" fill="#FF8A3D"></circle><rect x="140" y="84" width="100" height="16" fill="#1A1640"></rect>' + E3.basin(270, 82, 24) + label(190, 52, "WHEN THE SUN IS DOWN", "#FFD23F", 7.5)
def pg_stranger_eat(p): return GND + priest(p, 70) + E4_bread() + T.figure(p, ("man", "#7A5A3A"), 280, 86, 0.32, flip=True, pose="staff") + ban(280, 40, 20)
def pg_bought(p):      return GND + priest(p, 70) + coins(110, 70, 4) + man(p, 170, 86, 0.32, "#8A7A6A") + "".join(f'<ellipse cx="{220 + i * 18}" cy="{70 - (i % 2) * 6}" rx="12" ry="5" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.2"></ellipse>' for i in range(4))
def pg_pdaughter2(p):  return GND + priest(p, 70) + woman(p, 130, 86, 0.34, "#C2456A") + door(220, 84) + label(250, 22, "RETURNED UNTO HER FATHER'S HOUSE", "#FFD23F", 6.5)
def pg_unwitting(p):   return GND + E4_bread() + label(160, 50, "+ 1/5", "#FFD23F", 14) + coins(250, 70, 2)
def pg_male(p):        return GND + S1.cow(80, 84, 0.3, color="#5A3A22", patch="#3A2214") + E.sheep(150, 84, 0.34) + goat(210, 84, 0.34) + label(280, 50, "WITHOUT BLEMISH", "#FFD23F", 8)
def pg_no_blemish(p):  return GND + E.sheep(110, 84, 0.42) + ban(110, 50, 34) + label(220, 30, "BLIND · BROKEN · MAIMED", CY, 7) + label(220, 44, "A WEN · SCURVY · SCABBED", CY, 7)
def pg_freewill(p):    return GND + S1.cow(110, 84, 0.34, color="#8A5A30", patch="#5A3A22") + label(230, 40, "FOR A FREEWILL-OFFERING", "#FFD23F", 8) + label(230, 60, "BUT NOT FOR A VOW", CY, 7)
def pg_foreigner(p):   return GND + T.figure(p, ("man", "#7A5A3A"), 90, 86, 0.36, pose="staff") + E.sheep(170, 84, 0.36) + ban(240, 50, 30)
def pg_seven_dam(p):   return GND + S1.cow(90, 84, 0.34, color="#8A5A30", patch="#5A3A22") + S1.calf(140, 84, 0.34) + days(180, 40, 7) + label(220, 70, "THE EIGHTH DAY", CY, 7)
def pg_one_day(p):     return GND + E.sheep(100, 84, 0.42) + E3.lamb(150, 84, 0.3) + ban(125, 50, 40) + label(240, 50, "NOT BOTH IN ONE DAY", "#FFD23F", 8)
def pg_thanks(p):      return GND + E3.lamb(100, 84, 0.4) + days(170, 40, 1) + label(200, 70, "THE SAME DAY", CY, 8)
def pg_hallowed(p):    return GND + A.EG.pyramid(60, 84, 70, 44) + "".join(A.black_tent(150 + i * 40, 84, 32, 22) for i in range(4)) + label(200, 22, "I WILL BE HALLOWED", "#FFD23F", 9)
