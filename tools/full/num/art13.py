"""New drawings for Numbers chapter 13 (Numbers 27–29): the daughters of Zelophehad before the door of the tent, the line
of inheritance (a chart), Moses on the mountain of Abarim beholding the land, Joshua set before Eleazar, and pictograms
for the offerings of every day, sabbath, new moon and set feast (the beasts counted, with the calendar of the month)."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, samuel1 as S1
from faces_ex import F
from genesis.art2 import fit, ground, hills
from genesis.art3 import sun, label, man, woman
from exo import art as A, art5 as A5, art8 as B8, art9 as Q
from lev.art import GND, goat, flour, jar, altar
from lev.art8 import month
from num.art import ALL, wilderness_camp
def f(v): return f"{v:.1f}"
CY = B8.CY
DAUGHTERS_C = ["#C2456A", "#E8A030", "#5A8ACA", "#8A5AB8", "#3A9A6A"]
MAHLAH = F("eve", skin="#C98E66", shadow="#8A5A3E", hair="#1A1210", scarf="#C2456A", light="#FFC14D")
JOSHUA_LEADER = A5.JOSHUA

def daughters(p, w, h, seed):
    """Mahlah, Noah, Hoglah, Milcah and Tirzah standing before Moses, Eleazar, the princes and the congregation at the
    door of the tent of meeting."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), sun(w * 0.88, h * 0.15, 14, op=0.25), ground(w, h, h * 0.56, "#C8B080", dy=0), V.tabernacle(w * 0.72, h * 0.62, w * 0.46, uid=p + "tb")]
    s = fit(b, h * 0.42)
    o.append(A.moses(p, w * 0.62, b, s, flip=True) + Q.high_priest(p, w * 0.72, b, s * 0.98, flip=True))
    for i in range(3): o.append(A.elder(r.choice(A.CLOTHS), i)(p, w * (0.82 + i * 0.06), b, s * 0.95, flip=True))
    for i, c in enumerate(DAUGHTERS_C):
        o.append(woman(p, w * (0.08 + i * 0.09), b - (i % 2) * 4, s * 0.92, c))
    return "".join(o)

def inheritance(w, h):
    """If a man die and have no son: his daughter; no daughter: his brethren; no brethren: his father's brethren; else the
    kinsman next to him of his family."""
    o = [B8.bp(w, h), B8.title_bar(w, "A STATUTE AND ORDINANCE · THE INHERITANCE")]
    steps = ["SON", "DAUGHTER", "BRETHREN", "FATHER'S BRETHREN", "NEXT KINSMAN"]
    n = len(steps); bw = (w - 60) / n
    for i, t in enumerate(steps):
        x = 20 + i * (bw + 5); y = h * 0.42
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(bw - 10)}" height="{f(h * 0.3)}" fill="{"#FFD23F" if i == 1 else "#12113A"}" stroke="#2C9DB8" stroke-width="1.6"></rect>'
                 + label(x + (bw - 10) / 2, y + h * 0.17, t, "#0D0D0F" if i == 1 else CY, max(7, min(10, bw / 12)), ls=0.06))
        if i < n - 1: o.append(label(x + bw - 2, y + h * 0.17, "▸", "#FFD23F", 12))
    o.append(label(w * 0.5, h * 0.88, "IF THERE BE NONE · THEN THE NEXT", "#FFD23F", 9, ls=0.12))
    return "".join(o)

def abarim(p, w, h, seed):
    """Moses upon the mountain of Abarim beholding the land which Jehovah had given: green hills and the Jordan below."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#F3C88A"></rect>', sun(w * 0.86, h * 0.2, 22, color="#FF8A3D", op=0.35),
         hills(w, h, h * 0.44, seed, color="#5A8A4A", amp=18, step=70), hills(w, h, h * 0.56, seed + 1, color="#7AAA5A", amp=12)]
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.56)} C {f(w * 0.56)} {f(h * 0.62)} {f(w * 0.6)} {f(h * 0.7)} {f(w * 0.68)} {f(h)}" fill="none" stroke="#2C9DB8" stroke-width="5"></path>')
    o.append(f'<path d="M-10 {f(h)} L -10 {f(h * 0.58)} L {f(w * 0.3)} {f(h * 0.64)} L {f(w * 0.46)} {f(h)} Z" fill="#8A5A3A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(A.moses(p, w * 0.16, h * 0.64, fit(h * 0.64, h * 0.28), up=[(-22, -158), (8, -160), (36, -168)]))
    return "".join(o)

def joshua_set(p, w, h, seed):
    """Moses laying his hands upon Joshua before Eleazar the priest and all the congregation."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), V.rays(w * 0.5, h * 0.3, 36, 20, max(w, h), color="#FFF4C2", op=0.25), ground(w, h, h * 0.56, "#C8B080", dy=0)]
    s = fit(b, h * 0.42)
    o.append(Q.high_priest(p, w * 0.7, b, s, flip=True) + A5.joshua(p, w * 0.48, b, s * 0.96, flip=False) + A.moses(p, w * 0.32, b, s, up=[(-22, -158), (10, -170), (34, -176)]))
    for i in range(8): o.append(man(p, w * (0.02 + i * 0.03) if i < 4 else w * (0.84 + (i - 4) * 0.04), b - (i % 2) * 6, s * 0.86, r.choice(A.HEBREW), flip=i >= 4))
    return "".join(o)

# ---- offering pictograms (320 x 100) -----------------------------------------------------------------------------
def herd(bullocks=0, rams=0, lambs=0, goats=0, x0=10, title=""):
    """The beasts counted: a bullock, a ram, a he-lamb, a he-goat, each with ×N above it."""
    o = [GND]; x = x0 + 30
    for n, draw, nm in ((bullocks, lambda X: S1.cow(X, 84, 0.2, color="#8A5A30", patch="#E8E2D6"), "BULLOCKS"), (rams, lambda X: E.sheep(X, 84, 0.34), "RAMS"),
                        (lambs, lambda X: E3.lamb(X, 84, 0.3), "HE-LAMBS"), (goats, lambda X: goat(X, 84, 0.34), "HE-GOAT")):
        if not n: continue
        o.append(draw(x) + label(x, 40, f"×{n}", "#D7261E", 13) + label(x, 96, nm, CY, 6.5))
        x += 70
    if title: o.append(label(316, 14, title, "#FFD23F", 7.5, "end"))
    return "".join(o)

def pg_my_food(p):     return GND + altar(110, 84, 1.2) + label(220, 50, "IN THEIR DUE SEASON", "#FFD23F", 10)
def pg_continual(p):   return herd(lambs=2, title="DAY BY DAY") + label(250, 60, "MORNING · EVEN", "#FFD23F", 9)
def pg_morning(p):     return GND + E3.lamb(60, 84, 0.34) + flour(130, 84, 0.8) + jar(190, 84, 0.8) + label(260, 50, "1/10 EPHAH · 1/4 HIN", CY, 7)
def pg_sinai(p):       return GND + E4.sinai(160, 92, 220, 70, 3, fire=False) + label(160, 96, "ORDAINED IN MOUNT SINAI", "#FFD23F", 7.5)
def pg_drink(p):       return GND + jar(100, 84, 1.1) + label(100, 96, "1/4 HIN · STRONG DRINK", CY, 7) + E3.lamb(220, 84, 0.34) + label(220, 96, "AT EVEN", CY, 7)
def pg_sabbath(p):     return herd(lambs=2, title="ON THE SABBATH DAY") + label(250, 60, "BESIDES THE CONTINUAL", "#FFD23F", 7)
def pg_new_moon(p):    return herd(bullocks=2, rams=1, lambs=7, title="IN THE BEGINNINGS OF YOUR MONTHS")
def pg_new_moon_meal(p): return GND + flour(60, 84, 0.9) + label(60, 96, "3/10 · 2/10 · 1/10", CY, 6.5) + jar(150, 84, 0.9) + label(150, 96, "1/2 · 1/3 · 1/4 HIN", CY, 6.5) + label(250, 50, "EACH MONTH", "#FFD23F", 10)
def pg_goat(p):        return herd(goats=1, title="A SIN-OFFERING")
def pg_passover(p):    return month(1, marks=(14,), lit=(14,), title="THE FOURTEENTH DAY · JEHOVAH'S PASSOVER")
def pg_unleavened(p):  return month(1, marks=(15, 21), lit=range(15, 22), title="SEVEN DAYS · UNLEAVENED BREAD")
def pg_feast_herd(p):  return herd(bullocks=2, rams=1, lambs=7, goats=1, title="EVERY DAY OF THE SEVEN")
def pg_daily7(p):      return GND + "".join(f'<rect x="{20 + i * 42}" y="30" width="36" height="40" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.2"></rect>' + label(38 + i * 42, 56, str(i + 1), "#0D0D0F", 11) for i in range(7)) + label(160, 92, "AFTER THIS MANNER · DAILY", CY, 7.5)
def pg_firstfruits(p): return GND + flour(40, 84, 0.8) + label(40, 96, "NEW MEAL", CY, 6.5) + herd(bullocks=2, rams=1, lambs=7, x0=60)[len(GND):]
def pg_trumpets(p):    return month(7, marks=(1,), lit=(1,), title="THE FIRST DAY · A DAY OF BLOWING OF TRUMPETS")
def pg_seventh_herd(p): return herd(bullocks=1, rams=1, lambs=7, goats=1, title="THE SEVENTH MONTH")
def pg_atonement(p):   return month(7, marks=(10,), lit=(10,), title="THE TENTH DAY · AFFLICT YOUR SOULS")
def pg_booths(p):      return month(7, marks=(15, 22), lit=range(15, 23), title="THE FIFTEENTH DAY · SEVEN DAYS AND THE EIGHTH")
def day_herd(day, bullocks):
    return lambda p: herd(bullocks=bullocks, rams=2, lambs=14, goats=1, title=f"THE {day} DAY")
def pg_eighth(p):      return herd(bullocks=1, rams=1, lambs=7, goats=1, title="THE EIGHTH DAY · A SOLEMN ASSEMBLY")
def pg_set_feasts(p):  return GND + altar(80, 84, 1.0) + label(200, 40, "BESIDES YOUR VOWS", "#FFD23F", 9) + label(200, 60, "AND YOUR FREEWILL-OFFERINGS", CY, 8)
def pg_told(p):        return GND + A.moses(p, 120, 86, 0.36, up=[(-22, -158), (-6, -196), (8, -228)]) + label(230, 50, "ACCORDING TO ALL", "#FFD23F", 9)
