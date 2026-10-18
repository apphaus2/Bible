"""New drawings for Numbers chapter 3 (Numbers 5–6): the unclean put out without the camp, law pictograms for restitution,
the law of jealousy and the vow of a Nazirite (320 x 100 cells, like Leviticus), and Aaron blessing the people.
Restraint (5:11–31): the woman is drawn only as a figure standing before the priest with the earthen vessel; nothing of
the curse is shown."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus5 as V, numbers1 as N
from genesis.art2 import fit, ground, hills
from genesis.art3 import sun, label, man, woman
from exo import art as A, art8 as B8, art9 as Q
from exo.art7 import ban, coins
from lev.art import GND, priest, offerer, REACH, altar, dove, flour, jar, cakes, door, goat
from lev.art3 import BOTH
from lev.art4 import verdict, days
from lev.art5 import water, earthen
from num.art import ALL, wilderness_camp
def f(v): return f"{v:.1f}"
CY = B8.CY
W_C = "#6A3A5A"                                     # the woman's robe

def scroll(x, y, s=1.0, text=""):
    o = (f'<rect x="{f(x - 26 * s)}" y="{f(y - 30 * s)}" width="{f(52 * s)}" height="{f(30 * s)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.4"></rect>'
         f'<rect x="{f(x - 30 * s)}" y="{f(y - 33 * s)}" width="{f(6 * s)}" height="{f(36 * s)}" rx="2" fill="#C8A06A" stroke="#0D0D0F" stroke-width="1.2"></rect>'
         f'<rect x="{f(x + 24 * s)}" y="{f(y - 33 * s)}" width="{f(6 * s)}" height="{f(36 * s)}" rx="2" fill="#C8A06A" stroke="#0D0D0F" stroke-width="1.2"></rect>'
         + "".join(f'<path d="M{f(x - 18 * s)} {f(y - (24 - 6 * i) * s)} L {f(x + 18 * s)} {f(y - (24 - 6 * i) * s)}" stroke="#5A4A3A" stroke-width="1.2"></path>' for i in range(4)))
    return o + (label(x, y + 12, text, CY, 7) if text else "")

def razor(x, y, s=1.0):
    return (f'<path d="M{f(x - 18 * s)} {f(y)} L {f(x + 14 * s)} {f(y - 10 * s)} L {f(x + 18 * s)} {f(y - 4 * s)} Z" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="1.4"></path>'
            f'<path d="M{f(x - 18 * s)} {f(y)} L {f(x - 30 * s)} {f(y + 4 * s)}" stroke="#5A3A22" stroke-width="{f(4 * s)}"></path>')

def shroud(x, y, s=1.0):
    """The dead, wrapped and laid down (drawn only as a wrapped shape)."""
    return (f'<path d="M{f(x - 40 * s)} {f(y)} C {f(x - 44 * s)} {f(y - 14 * s)} {f(x - 30 * s)} {f(y - 16 * s)} {f(x - 20 * s)} {f(y - 12 * s)} L {f(x + 36 * s)} {f(y - 10 * s)} C {f(x + 44 * s)} {f(y - 8 * s)} {f(x + 44 * s)} {f(y)} {f(x + 36 * s)} {f(y)} Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6"></path>'
            + "".join(f'<path d="M{f(x + dx * s)} {f(y - 12 * s)} L {f(x + dx * s)} {f(y)}" stroke="#8A8478" stroke-width="1"></path>' for dx in (-14, 4, 22)))

def locks(p, x, y=86, s=0.36):
    """A Nazirite: a man whose locks hang long below his shoulders."""
    return man(p, x, y, s, "#7A6A4A") + "".join(f'<path d="M{f(x + dx * s)} {f(y - 186 * s)} C {f(x + (dx - 4) * s)} {f(y - 150 * s)} {f(x + (dx + 4) * s)} {f(y - 130 * s)} {f(x + dx * s)} {f(y - 110 * s)}" fill="none" stroke="#1A1210" stroke-width="{f(5 * s)}" stroke-linecap="round"></path>' for dx in (-16, -9, 9, 16))

def cup(x, y, s=1.0, color="#7A1A3A"):
    return (f'<path d="M{f(x - 10 * s)} {f(y - 24 * s)} L {f(x + 10 * s)} {f(y - 24 * s)} L {f(x + 6 * s)} {f(y - 10 * s)} L {f(x - 6 * s)} {f(y - 10 * s)} Z" fill="{color}" stroke="#0D0D0F" stroke-width="1.4"></path>'
            f'<path d="M{f(x)} {f(y - 10 * s)} L {f(x)} {f(y - 2 * s)} M{f(x - 8 * s)} {f(y)} L {f(x + 8 * s)} {f(y)}" stroke="#0D0D0F" stroke-width="{f(2 * s)}"></path>')

def spark(x, y, s=1.0):
    return f'<path d="M{f(x - 20 * s)} {f(y)} L {f(x - 8 * s)} {f(y - 10 * s)} L {f(x - 2 * s)} {f(y + 4 * s)} L {f(x + 8 * s)} {f(y - 12 * s)} L {f(x + 20 * s)} {f(y)}" fill="none" stroke="#D7261E" stroke-width="{f(4 * s)}" stroke-linejoin="round"></path>'

def wife(p, x, y=86, s=0.34, flip=False): return woman(p, x, y, s, W_C, flip=flip)

# ---- 5:5–10 restitution -----------------------------------------------------------------------------------------------
def pg_trespass(p):    return GND + offerer(p, 80) + spark(150, 50) + door(240, 84, 1.0)
def pg_restitution(p): return GND + offerer(p, 50) + coins(100, 70, 10) + label(170, 56, "+", "#FFD23F", 22) + coins(200, 70, 2) + man(p, 280, 86, 0.34, "#4A3A6A", flip=True) + label(170, 96, "IN FULL · AND THE FIFTH PART", CY, 7)
def pg_no_kinsman(p):  return GND + coins(60, 70, 6) + priest(p, 150, flip=True) + goat(240, 84, 0.42, color="#E8E2D6") + label(240, 96, "THE RAM OF THE ATONEMENT", CY, 6.5)
def pg_hallowed(p):    return GND + offerer(p, 60, up=REACH) + flour(120, 84, 0.9) + priest(p, 200, flip=True) + label(260, 40, "IT SHALL BE HIS", "#FFD23F", 8)

# ---- 5:11–31 the law of jealousy -------------------------------------------------------------------------------------
def pg_jealous(p):     return GND + man(p, 80, 86, 0.36, "#5A3A22") + spark(160, 44, 1.2) + wife(p, 240, flip=True) + label(160, 96, "THE SPIRIT OF JEALOUSY", CY, 7)
def pg_hid(p):         return GND + man(p, 70, 86, 0.36, "#5A3A22") + label(160, 46, "NO WITNESS", "#FFD23F", 9) + wife(p, 250, flip=True)
def pg_barley(p):      return (GND + man(p, 40, 86, 0.34, "#5A3A22") + wife(p, 80) + flour(150, 84, 1.0) + label(150, 96, "1/10 EPHAH OF BARLEY MEAL", CY, 6.5)
                               + jar(262, 72, 0.6) + ban(262, 54, 28) + label(262, 96, "NO OIL · NO FRANKINCENSE", CY, 6.5))
def pg_set_before(p):  return GND + door(60, 84, 1.0) + wife(p, 140) + priest(p, 210, flip=True)
def pg_holy_water(p):  return (GND + priest(p, 70, up=REACH) + earthen(160, 82, 1.4) + water(160, 64, 30)
                               + "".join(f'<circle cx="{150 + i * 5}" cy="{40 + (i % 3) * 5}" r="1.8" fill="#8A6A4A"></circle>' for i in range(5)) + label(240, 60, "DUST OF THE FLOOR", CY, 7))
def pg_bitter(p):      return GND + wife(p, 100) + flour(130, 54, 0.6) + priest(p, 200, flip=True) + earthen(240, 70, 1.0) + label(160, 96, "THE WATER OF BITTERNESS", CY, 7)
def pg_swear(p):       return GND + priest(p, 70) + scroll(160, 70, 1.0, "THE OATH") + wife(p, 250, flip=True)
def pg_amen(p):        return GND + wife(p, 90) + label(200, 50, "AMEN, AMEN", "#FFD23F", 14)
def pg_blot(p):        return GND + scroll(110, 60, 1.1) + '<path d="M150 64 C 170 70 180 74 190 80" fill="none" stroke="#2C9DB8" stroke-width="2" stroke-dasharray="3 3"></path>' + earthen(210, 86, 1.2) + water(210, 70, 30)
def pg_drink(p):       return GND + priest(p, 90) + earthen(160, 70, 0.9) + wife(p, 230, flip=True)
def pg_wave_meal(p):   return GND + priest(p, 90, up=REACH) + flour(150, 70, 0.8) + altar(250, 84, 1.0)
def pg_handful(p):     return GND + priest(p, 70, up=REACH) + flour(130, 84, 0.8) + altar(210, 84, 1.0) + wife(p, 280, flip=True)
def pg_defiled(p):     return GND + wife(p, 120) + verdict(220, 44, False)
def pg_free(p):        return GND + wife(p, 120) + verdict(220, 44, True) + label(220, 96, "SHE SHALL BE FREE", CY, 7)
def pg_law_jealousy(p): return GND + scroll(110, 74, 1.2, "THE LAW OF JEALOUSY") + door(240, 84, 1.0)
def pg_bear(p):        return GND + man(p, 100, 86, 0.36, "#5A3A22") + verdict(170, 44, True) + wife(p, 250, flip=True)

# ---- 6:1–21 the vow of a Nazirite ------------------------------------------------------------------------------------
def pg_vow(p):         return GND + locks(p, 100) + label(200, 40, "UNTO JEHOVAH", "#FFD23F", 9) + door(270, 84, 1.0)
def pg_no_wine(p):     return GND + N.grapes(90, 70, 0.5, 3) + cup(150, 84, 1.4) + ban(120, 56, 34) + jar(240, 84, 0.9) + ban(240, 64, 26) + label(160, 96, "WINE · STRONG DRINK · GRAPES", CY, 7)
def pg_kernels(p):     return GND + N.grapes(100, 70, 0.5, 5) + ban(100, 56, 32) + label(210, 56, "FROM THE KERNELS EVEN TO THE HUSK", CY, 7)
def pg_no_razor(p):    return GND + locks(p, 110) + razor(210, 60, 1.2) + ban(210, 56, 30) + label(210, 96, "NO RAZOR", CY, 8)
def pg_no_dead(p):     return GND + locks(p, 80) + shroud(220, 84, 1.2) + ban(220, 50, 26)
def pg_kin(p):         return GND + locks(p, 70) + shroud(200, 84, 1.0) + label(200, 50, "FATHER · MOTHER · BROTHER · SISTER", CY, 6.5)
def pg_holy_naz(p):    return GND + V.rays(150, 60, 18, 18, 70, color="#FFF4C2", op=0.5) + locks(p, 150)
def pg_sudden(p):      return GND + shroud(80, 84, 1.0) + locks(p, 170) + days(230, 40, 7, lit=7, w=9) + razor(260, 76, 0.9)
def pg_doves8(p):      return GND + man(p, 60, 86, 0.34, "#7A6A4A") + dove(130, 80, 1.1) + dove(170, 80, 1.1, flip=True) + priest(p, 250, flip=True)
def pg_void(p):        return GND + E3.lamb(70, 84, 0.36) + days(150, 40, 7, lit=0, w=9) + '<path d="M146 30 L 230 52" stroke="#D7261E" stroke-width="3"></path>' + label(190, 96, "THE FORMER DAYS SHALL BE VOID", CY, 7)
def pg_fulfilled(p):   return GND + locks(p, 120) + door(220, 84, 1.0) + label(170, 30, "THE DAYS FULFILLED", "#FFD23F", 8)
def pg_oblation(p):    return GND + E3.lamb(50, 84, 0.32) + E3.lamb(100, 84, 0.3) + goat(160, 84, 0.4, color="#E8E2D6") + cakes(230, 84, 0.9) + jar(285, 84, 0.7)
def pg_basket(p):      return GND + cakes(80, 84, 1.1) + flour(150, 84, 0.8) + jar(210, 84, 0.8) + altar(275, 84, 0.8)
def pg_present(p):     return GND + priest(p, 80, up=REACH) + altar(170, 84, 1.0) + goat(260, 84, 0.4, color="#E8E2D6")
def pg_hair_fire(p):   return (GND + man(p, 80, 86, 0.36, "#7A6A4A") + razor(130, 40, 0.8) + altar(220, 84, 1.1)
                               + '<path d="M196 50 C 206 40 226 46 236 36" fill="none" stroke="#1A1210" stroke-width="4" stroke-linecap="round"></path>')
def pg_wave_naz(p):    return GND + priest(p, 80, up=REACH) + man(p, 160, 86, 0.36, "#7A6A4A", flip=True, up=REACH) + cakes(150, 40, 0.6) + cup(260, 84, 1.3) + label(260, 96, "AFTER THAT · WINE", CY, 7)
def pg_law_naz(p):     return GND + scroll(100, 74, 1.2, "THE LAW OF THE NAZIRITE") + locks(p, 220)

# ---- scenes ------------------------------------------------------------------------------------------------------------
def without(p, w, h, seed):
    """Every leper, every one that hath an issue, and whosoever is unclean by the dead, put out without the camp."""
    r = random.Random(seed); b = h * 0.9
    o = [wilderness_camp(p, w, h, seed, standards=False, sinai=False)]
    o.append(f'<path d="M{f(w * 0.36)} {f(h * 0.5)} L {f(w * 0.2)} {f(h)}" stroke="#FFD23F" stroke-width="3" stroke-dasharray="10 7"></path>')
    for i, x in enumerate((0.04, 0.1, 0.16)):
        o.append(man(p, w * x, b - i * 4, fit(b, h * 0.56), "#6A6460", flip=True))
    return "".join(o)

def blessing(p, w, h, seed):
    """Aaron and his sons before the tent of meeting, their hands lifted up over the children of Israel."""
    r = random.Random(seed); b = h * 0.62
    o = [mk.defs(p, *ALL), V.rays(w * 0.5, h * 0.3, 44, 30, max(w, h) * 1.2, color="#FFF4C2", op=0.3),
         ground(w, h, h * 0.42, "#C8B080", dy=0), V.tabernacle(w * 0.5, h * 0.46, w * 0.42, uid=p + "tb")]
    s = fit(b, h * 0.3)
    o.append(Q.son_priest(p, w * 0.36, b, s * 0.95, up=BOTH) + Q.son_priest(p, w * 0.64, b, s * 0.95, up=BOTH, flip=True) + Q.high_priest(p, w * 0.5, b + 4, s, up=BOTH))
    for k in range(3):                                      # the congregation, backs to us, rank on rank
        y = h * (0.78 + k * 0.1)
        for i in range(12 + k * 2):
            x = w * (i + 0.5 * (k % 2)) / (12 + k * 2)
            o.append(man(p, x, y, fit(y, y - h * (0.16 + 0.05 * k)), r.choice(A.HEBREW)))
    return "".join(o)
