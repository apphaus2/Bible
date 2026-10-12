"""Pictograms for Leviticus chapter 9 (Leviticus 26–27): the blessings (rain, harvest, peace, five chasing a hundred), the
curses drawn as the land under judgment (an iron sky, a brass earth, empty cities, the people scattered) — never the
famine of 26:26–29 itself, only the broken staff of bread and the one oven — and the estimations of vows as technical charts."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3, exodus5 as V, ruth1 as R, samuel1 as S1, numbers1 as N
from genesis import art2 as Y, art10 as T
from genesis.art2 import ground
from genesis.art3 import label, man, woman
from exo import art as A, art8 as B8
from exo.art6 import GND
from exo.art7 import ban, coins
from lev.art import altar, priest, offerer, goat, REACH, jar, flour, A_ALL
from lev.art4 import days
from lev.art8 import month
def f(v): return f"{v:.1f}"
CY = B8.CY
DARK = '<rect x="-200" y="-400" width="720" height="500" fill="#2A1A1E"></rect><rect x="-200" y="84" width="720" height="16" fill="#1A0E10"></rect>'

def pg_no_idols(p):   return GND + '<path d="M146 84 L 150 34 C 150 24 170 24 170 34 L 174 84 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path><circle cx="160" cy="22" r="10" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></circle>' + ban(160, 52, 40) + days(230, 40, 7)
def pg_rain(p):       return GND + "".join(f'<path d="M{x} 10 l -6 14" stroke="#8FD0E2" stroke-width="2"></path>' for x in range(30, 300, 18)) + R.field(20, 300, 84, 30, 3, rows=1) + "".join(f'<circle cx="{x}" cy="40" r="12" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="1.2"></circle>' for x in (60, 260))
def pg_threshing(p):  return GND + R.heap(100, 84, 90, 30) + N.grapes(200, 30, 0.5) + R.sheaf(270, 84, 0.6) + label(160, 96, "THRESHING · VINTAGE · SOWING", CY, 7)
def pg_peace(p):      return GND + mk.stars(20, 320, 50, 3) + "".join(A.black_tent(40 + i * 60, 84, 46, 30) for i in range(5)) + label(160, 14, "NONE SHALL MAKE YOU AFRAID", "#FFD23F", 8)
def pg_chase(p):      return GND + "".join(man(p, 30 + i * 16, 86, 0.22, A.HEBREW[i % 6]) for i in range(5)) + '<path d="M120 60 L 160 60" stroke="#FFD23F" stroke-width="2"></path>' + "".join(f'<circle cx="{180 + (i % 10) * 12}" cy="{40 + (i // 10) * 12}" r="3.4" fill="#8A6A5A"></circle>' for i in range(30)) + label(80, 96, "FIVE", "#FFD23F", 8) + label(240, 96, "A HUNDRED", CY, 8)
def pg_fruitful(p):   return GND + "".join(man(p, 30 + i * 30, 86, 0.3, A.HEBREW[i % 6]) if i % 2 else woman(p, 30 + i * 30, 86, 0.28, "#7A3A5A") for i in range(10)) + label(160, 14, "FRUITFUL · MULTIPLY", "#FFD23F", 8)
def pg_old_store(p):  return GND + R.sack(100, 84, 0.7) + R.sack(140, 84, 0.7) + R.heap(230, 84, 80, 28) + label(160, 96, "OLD STORE LONG KEPT", CY, 7)
def pg_tabernacle(p): return GND + V.rays(160, 40, 20, 10, 100, color="#FFF4C2", op=0.3) + V.tabernacle(160, 84, 130, uid=p + "t") + label(160, 14, "I WILL WALK AMONG YOU", "#FFD23F", 8)
def pg_yoke(p):       return GND + '<path d="M60 50 C 100 30 140 30 180 50" fill="none" stroke="#5A3A22" stroke-width="8"></path><path d="M120 34 L 132 58" stroke="#F3EFE6" stroke-width="3"></path>' + man(p, 240, 86, 0.38, "#5A3A22", up=T.POSES["raise"]) + label(120, 80, "THE BARS OF YOUR YOKE", CY, 7)
def pg_reject(p):     return DARK + label(160, 40, "IF YE WILL NOT HEARKEN", "#D7261E", 10) + "".join(A.black_tent(60 + i * 50, 84, 36, 22, color="#2A2230", lit="#5A1A1E") for i in range(5))
def pg_terror(p):     return DARK + man(p, 100, 86, 0.36, "#4A3A3E") + E.kneel(160, 86, 0.32, color="#4A3A3E", skin="#6A4A3A") + R.field(200, 310, 84, 24, 2, rows=1) + label(255, 30, "YE SHALL SOW IN VAIN", "#D7261E", 7.5)
def pg_iron(p):       return ('<rect x="-200" y="-400" width="720" height="460" fill="#4A4A54"></rect><rect x="-200" y="60" width="720" height="40" fill="#8A5A2A"></rect>'
                              + label(160, 30, "YOUR HEAVEN AS IRON", "#E8E2D6", 10) + label(160, 84, "YOUR EARTH AS BRASS", "#FFD23F", 10))
def pg_seven_more(p): return DARK + "".join(f'<rect x="{40 + i * 36}" y="40" width="28" height="28" fill="#5A1A1E" stroke="#D7261E" stroke-width="1.6"></rect>' for i in range(7)) + label(160, 84, "SEVEN TIMES MORE", "#D7261E", 9)
def pg_beasts(p):     return DARK + "".join(f'<path d="M{x} 84 C {x - 4} 70 {x + 30} 64 {x + 40} 74 L {x + 48} 70 L {x + 46} 84 Z" fill="#3A2A2A" stroke="#0D0D0F" stroke-width="1.4"></path>' for x in (60, 150)) + label(250, 50, "YOUR WAYS DESOLATE", "#D7261E", 8)
def pg_sword(p):      return DARK + '<path d="M80 80 L 240 20" stroke="#C8C8D0" stroke-width="6" stroke-linecap="round"></path><path d="M90 72 L 70 54" stroke="#5A3A22" stroke-width="8"></path>' + Y.city(250, 84, 80, 40, 3, color="#3A2A2E", lit="#5A1A1E", wall="#4A3A3E")
def pg_bread(p):      return (DARK + '<path d="M120 84 C 118 46 180 46 178 84 Z" fill="#6A3A22" stroke="#0D0D0F" stroke-width="1.8"></path>' + "".join(woman(p, 30 + i * 18, 86, 0.22, "#4A3A3E") for i in range(5))
                              + '<path d="M220 30 L 290 70" stroke="#8A6A3A" stroke-width="6"></path><path d="M250 44 L 262 56" stroke="#1A0E10" stroke-width="5"></path>' + label(255, 90, "THE STAFF OF BREAD BROKEN", "#D7261E", 7))
def pg_wrath(p):      return DARK + E.blaze(160, 84, 60, 40, 9, n=6) + label(160, 22, "IN WRATH · SEVEN TIMES", "#D7261E", 9)
def pg_high_places(p): return DARK + '<path d="M60 84 L 100 40 L 140 84 Z" fill="#3A2A2E" stroke="#0D0D0F" stroke-width="1.4"></path>' + ban(100, 60, 22) + '<rect x="180" y="40" width="18" height="44" fill="#6A5A4A" transform="rotate(30 189 84)"></rect>' + Y.city(270, 84, 70, 40, 5, color="#2A1A1E", lit="#2A1A1E", wall="#3A2A2E")
def pg_waste(p):      return DARK + Y.city(160, 84, 240, 60, 7, color="#2A1A1E", lit="#2A1A1E", wall="#3A2A2E") + label(160, 14, "YOUR CITIES A WASTE", "#D7261E", 9)
def pg_scatter(p):    return DARK + "".join(f'<path d="M160 60 L {160 + 120 * __import__("math").cos(a):.1f} {60 + 34 * __import__("math").sin(a):.1f}" stroke="#D7261E" stroke-width="1.6" stroke-dasharray="4 4"></path>' for a in [i * 0.79 for i in range(8)]) + label(160, 64, "●", "#FFD23F", 14) + label(160, 96, "SCATTERED AMONG THE NATIONS", "#D7261E", 7)
def pg_rest(p):       return GND + '<rect x="40" y="78" width="240" height="6" fill="#6A5A3A"></rect>' + "".join(f'<path d="M{50 + i * 22} 80 L {52 + i * 22} {64 - (i % 3) * 6}" stroke="#9CCB5E" stroke-width="2.4"></path>' for i in range(11)) + label(160, 30, "THE LAND SHALL ENJOY ITS SABBATHS", "#FFD23F", 8)
def pg_leaf(p):       return DARK + '<path d="M120 50 C 140 30 180 30 196 46 C 180 62 140 66 120 50 Z" fill="#8A7A3A" stroke="#0D0D0F" stroke-width="1.4" transform="rotate(-20 158 48)"></path>' + label(160, 84, "THE SOUND OF A DRIVEN LEAF", "#D7261E", 8)
def pg_pine(p):       return DARK + "".join(E.kneel(80 + i * 50, 86, 0.3, color="#3A2A2E", skin="#5A4A4A", flip=i % 2 == 1) for i in range(4))
def pg_confess(p):    return GND + "".join(E.kneel(70 + i * 50, 86, 0.32, color=A.HEBREW[i], skin="#8A5A3E") for i in range(4)) + label(160, 18, "THEY SHALL CONFESS THEIR INIQUITY", "#FFD23F", 8)
def pg_remember(p):   return GND + V.rays(160, 0, 20, 10, 100, color="#FFF4C2", op=0.3) + "".join(label(70 + i * 90, 56, t, "#FFD23F", 11) for i, t in enumerate(("JACOB", "ISAAC", "ABRAHAM"))) + label(160, 84, "I WILL REMEMBER MY COVENANT", CY, 8)
def pg_not_reject(p): return GND + A.EG.pyramid(60, 84, 70, 44) + '<path d="M110 70 L 220 70" stroke="#FFD23F" stroke-width="2"></path><path d="M220 70 l -8 -5 l 0 10 Z" fill="#FFD23F"></path>' + "".join(A.black_tent(240 + i * 30, 84, 24, 18) for i in range(3)) + label(160, 18, "I WILL NOT REJECT THEM", "#FFD23F", 8)
def pg_sinai(p):      return GND + A.E4.sinai(200, 84, 160, 80, 4, fire=False) + A.moses(p, 70, 86, 0.36, up=T.POSES["raise"])

# ---- Leviticus 27: the estimations ----
def estim(rows_, title):
    """A bar chart of the estimation in shekels: rows_ = [(label, shekels, colour)]."""
    o = [GND, label(14, 12, title, "#FFD23F", 7.5, "start")]
    mx = max(r[1] for r in rows_); rh = 72 / len(rows_)
    for i, (t, val, c) in enumerate(rows_):
        y = 20 + i * rh
        o.append(label(116, y + rh * 0.66, t, CY, 7, "end") + f'<rect x="122" y="{f(y + rh * 0.15)}" width="{f(160 * val / mx)}" height="{f(rh * 0.6)}" fill="{c}" stroke="#0D0D0F" stroke-width="1"></rect>'
                 + label(128 + 160 * val / mx, y + rh * 0.66, str(val), "#FFD23F", 7.5, "start"))
    return "".join(o)
M, W = "#8FB8E8", "#E07A9A"
def pg_20_60(p):      return estim([("MALE 20–60", 50, M), ("FEMALE 20–60", 30, W)], "THE ESTIMATION · SHEKELS OF SILVER")
def pg_5_20(p):       return estim([("MALE 5–20", 20, M), ("FEMALE 5–20", 10, W)], "FROM FIVE YEARS OLD UNTO TWENTY")
def pg_child(p):      return estim([("MALE 1 MONTH–5", 5, M), ("FEMALE 1 MONTH–5", 3, W)], "FROM A MONTH OLD UNTO FIVE YEARS")
def pg_60(p):         return estim([("MALE 60 +", 15, M), ("FEMALE 60 +", 10, W)], "FROM SIXTY YEARS OLD AND UPWARD")
def pg_poor(p):       return GND + man(p, 100, 86, 0.36, "#8A7A6A") + priest(p, 180, flip=True) + label(250, 40, "ACCORDING TO HIS ABILITY", "#FFD23F", 7.5)
def pg_beast_vow(p):  return GND + S1.cow(100, 84, 0.34, color="#8A5A30", patch="#5A3A22") + label(180, 52, "⇄", "#D7261E", 18) + ban(180, 50, 18) + E.sheep(260, 84, 0.36) + label(180, 96, "A GOOD FOR A BAD · BOTH HOLY", CY, 7)
def pg_unclean_beast(p): return GND + N.ass(110, 84, 0.3) + priest(p, 210) + coins(250, 60, 3) + label(270, 90, "+ 1/5", "#FFD23F", 9)
def pg_house(p):      return GND + '<rect x="60" y="40" width="90" height="44" fill="#B8AE9E" stroke="#0D0D0F" stroke-width="1.6"></rect><rect x="96" y="58" width="16" height="26" fill="#3A2214"></rect>' + priest(p, 200) + coins(240, 60, 3) + label(270, 90, "+ 1/5", "#FFD23F", 9)
def pg_homer(p):      return GND + R.field(20, 200, 84, 30, 9, rows=1) + label(250, 40, "A HOMER OF BARLEY SEED", "#FFD23F", 7.5) + label(250, 58, "= 50 SHEKELS", CY, 9)
def pg_jubilee_field(p): return GND + "".join(f'<rect x="{20 + i * 28}" y="40" width="22" height="30" fill="{"#FFD23F" if i < 4 else "#12113A"}" stroke="#2C9DB8" stroke-width="1"></rect>' for i in range(10)) + label(160, 22, "THE YEARS THAT REMAIN UNTO THE JUBILEE", "#FFD23F", 7.5) + coins(150, 92, 4, r=4)
def pg_devoted_field(p): return GND + R.field(20, 200, 84, 30, 11, rows=1) + priest(p, 260) + label(160, 22, "A FIELD DEVOTED · THE PRIEST'S", "#FFD23F", 8)
def pg_bought_field(p): return GND + R.field(20, 160, 84, 30, 12, rows=1) + man(p, 210, 86, 0.34, "#5A3A22") + '<path d="M230 60 L 290 60" stroke="#FFD23F" stroke-width="2"></path>' + man(p, 300, 86, 0.32, "#4A3A6A", flip=True) + label(160, 14, "IN THE YEAR OF JUBILEE IT SHALL RETURN", CY, 7)
def pg_gerahs(p):     return GND + '<circle cx="100" cy="56" r="26" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="2"></circle>' + label(100, 60, "1", "#0D0D0F", 12) + label(150, 60, "=", "#FFD23F", 16) + "".join(f'<circle cx="{180 + (i % 10) * 12}" cy="{46 + (i // 10) * 14}" r="5" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="0.8"></circle>' for i in range(20)) + label(240, 90, "20 GERAHS", CY, 8)
def pg_firstling(p):  return GND + S1.cow(100, 84, 0.34, color="#8A5A30", patch="#5A3A22") + S1.calf(150, 84, 0.34) + label(240, 40, "IT IS JEHOVAH'S", "#FFD23F", 9)
def pg_ransom(p):     return GND + N.ass(100, 84, 0.3) + coins(160, 70, 3) + label(200, 60, "+ 1/5", "#FFD23F", 10)
def pg_devoted(p):    return GND + '<rect x="60" y="30" width="200" height="40" fill="#12113A" stroke="#D7261E" stroke-width="2"></rect>' + label(160, 56, "DEVOTED · MOST HOLY", "#D7261E", 11)
def pg_tithe(p):      return GND + "".join(R.sheaf(30 + i * 28, 84, 0.42) for i in range(9)) + '<rect x="276" y="40" width="30" height="46" fill="none" stroke="#FFD23F" stroke-width="2"></rect>' + R.sheaf(291, 84, 0.42) + label(160, 14, "THE TITHE IS JEHOVAH'S", "#FFD23F", 8)
def pg_rod(p):        return GND + "".join(E.sheep(30 + i * 30, 84, 0.26) for i in range(9)) + '<path d="M286 20 L 286 84" stroke="#5A3A22" stroke-width="4"></path>' + E.sheep(300, 84, 0.26, wool="#FFD23F") + label(160, 14, "WHATSOEVER PASSETH UNDER THE ROD · THE TENTH", "#FFD23F", 7)
def pg_commandments(p): return pg_sinai(p)
