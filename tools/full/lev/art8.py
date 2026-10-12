"""Drawings for Leviticus chapter 8 (Leviticus 23–25): the set feasts on a calendar strip, the sheaf of first-fruits and the
fifty days, the trumpets, the booths, the lamp and the showbread, the blasphemer (24:10–23: the quarrel, the ward, and the
heap of stones without the camp; the stoning itself is caption-only), the sabbath of the land and the jubilee."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus5 as V, ruth1 as R, samuel1 as S1, samuel4 as A4, numbers1 as N, judges1 as J1, joshua1 as J
from genesis import art2 as Y, art10 as T
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import label, man, woman
from exo import art as A, art8 as B8, art9 as Q
from exo.art6 import GND
from exo.art7 import ban, coins
from lev.art import altar, door, priest, offerer, goat, dove, REACH, jar, flour, cakes, A_ALL
from lev.art4 import days
def f(v): return f"{v:.1f}"
CY = B8.CY

def month(m, marks=(), lit=(), title=""):
    """A 30-day strip for month m (two rows of 15 cells): lit days gold, marked days ringed red."""
    o = [GND, label(14, 12, title or f"THE {['', 'FIRST', 'SECOND', 'THIRD', 'FOURTH', 'FIFTH', 'SIXTH', 'SEVENTH'][m]} MONTH", "#FFD23F", 8, "start")]
    for d in range(1, 31):
        x = 14 + ((d - 1) % 15) * 19.5; y = 20 + ((d - 1) // 15) * 34
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="17" height="30" fill="{"#FFD23F" if d in lit else "#12113A"}" stroke="{"#D7261E" if d in marks else "#2C9DB8"}" stroke-width="{2.4 if d in marks else 1}"></rect>'
                 + label(x + 8.5, y + 19, str(d), "#0D0D0F" if d in lit else CY, 8))
    return "".join(o)

def pg_sabbath(p):    return GND + days(40, 30, 7) + label(80, 60, "THE SEVENTH DAY", "#FFD23F", 8) + "".join(A.black_tent(170 + i * 40, 84, 32, 22) for i in range(4))
def pg_proclaim(p):   return GND + A.moses(p, 70, 86, 0.36, up=T.POSES["raise"]) + label(200, 40, "THE SET FEASTS OF JEHOVAH", "#FFD23F", 9) + label(200, 60, "HOLY CONVOCATIONS", CY, 8)
def pg_passover(p):   return month(1, marks=(14,), lit=range(15, 22))
def pg_unleavened(p): return month(1, marks=(15, 21), lit=range(15, 22), title="THE FEAST OF UNLEAVENED BREAD · SEVEN DAYS")
def pg_sheaf(p):      return GND + priest(p, 90, up=[(-22, -158), (-10, -190), (10, -210)]) + R.sheaf(96, 22, 0.5) + '<path d="M60 14 L 130 14" stroke="#FFD23F" stroke-width="2"></path>' + R.field(160, 310, 84, 30, 2, rows=1)
def pg_he_lamb(p):    return GND + E3.lamb(80, 84, 0.4) + flour(150, 84, 0.9) + jar(210, 84, 0.8) + N.grapes(270, 34, 0.4) + label(270, 96, "1/4 HIN OF WINE", CY, 7)
def pg_no_bread(p):   return GND + R.sheaf(80, 84, 0.6) + ban(150, 50, 30) + label(240, 50, "UNTIL THIS SELFSAME DAY", "#FFD23F", 8)
def pg_fifty(p):      return GND + "".join(f'<rect x="{14 + (i % 25) * 11.8}" y="{30 + (i // 25) * 22}" width="10" height="18" fill="{"#FFD23F" if i == 49 else "#12113A"}" stroke="#2C9DB8" stroke-width="0.8"></rect>' for i in range(50)) + label(160, 22, "SEVEN SABBATHS · FIFTY DAYS", "#FFD23F", 8) + label(290, 90, "50", "#FFD23F", 12)
def pg_loaves(p):     return GND + "".join(f'<ellipse cx="{90 + i * 40}" cy="70" rx="26" ry="9" fill="#C8902E" stroke="#0D0D0F" stroke-width="1.6"></ellipse>' for i in range(2)) + label(110, 96, "TWO WAVE-LOAVES · LEAVENED", CY, 7) + E3.lamb(220, 84, 0.3) + S1.cow(280, 84, 0.24, color="#5A3A22", patch="#3A2214")
def pg_seven_lambs(p): return GND + "".join(E3.lamb(30 + i * 34, 84, 0.24) for i in range(7)) + goat(270, 84, 0.3)
def pg_wave_bread(p): return GND + priest(p, 110, up=[(-22, -158), (-10, -190), (10, -210)]) + '<ellipse cx="116" cy="14" rx="20" ry="6" fill="#C8902E" stroke="#0D0D0F" stroke-width="1.2"></ellipse>' + '<path d="M80 6 L 150 6" stroke="#FFD23F" stroke-width="2"></path>' + label(230, 60, "HOLY TO JEHOVAH FOR THE PRIEST", CY, 7)
def pg_corners(p):    return GND + R.field(20, 300, 80, 30, 7, rows=1) + '<rect x="20" y="40" width="40" height="44" fill="#E8C88A" opacity="0.4" stroke="#FFD23F" stroke-width="1.4" stroke-dasharray="4 3"></rect><rect x="260" y="40" width="40" height="44" fill="#E8C88A" opacity="0.4" stroke="#FFD23F" stroke-width="1.4" stroke-dasharray="4 3"></rect>' + label(160, 96, "FOR THE POOR, AND FOR THE SOJOURNER", CY, 7)
def pg_trumpets(p):   return month(7, marks=(1,), lit=(1,), title="THE FIRST DAY · A MEMORIAL OF BLOWING OF TRUMPETS")
def pg_atonement(p):  return month(7, marks=(10,), lit=(10,), title="THE TENTH DAY · THE DAY OF ATONEMENT")
def pg_afflict(p):    return GND + E.kneel(110, 86, 0.38, color="#5A3A22", skin="#8A5A3E") + E.kneel(170, 86, 0.36, color="#4A3A6A", skin="#8A5A3E") + label(250, 40, "NO MANNER OF WORK", "#FFD23F", 8)
def pg_ninth(p):      return month(7, marks=(9, 10), lit=(10,), title="FROM EVEN UNTO EVEN · THE NINTH DAY AT EVEN")
def pg_booths(p):     return month(7, marks=(15, 22), lit=range(15, 23), title="THE FEAST OF TABERNACLES · SEVEN DAYS AND THE EIGHTH")
def pg_feasts_all(p): return (GND + "".join(f'<rect x="{20 + i * 74}" y="24" width="66" height="50" fill="#12113A" stroke="#FFD23F" stroke-width="1.4"></rect>' + label(53 + i * 74, 44, t1, "#FFD23F", 7) + label(53 + i * 74, 60, t2, CY, 6.5)
                                       for i, (t1, t2) in enumerate((("PASSOVER", "1ST MONTH"), ("WEEKS", "50 DAYS"), ("TRUMPETS", "7TH · 1ST"), ("ATONEMENT", "7TH · 10TH")))))
def booth(x, y, s=1.0):
    """A booth of branches: four poles, a roof of palm fronds and leafy boughs."""
    return (f'<path d="M{f(x - 28 * s)} {f(y)} L {f(x - 28 * s)} {f(y - 40 * s)} M{f(x + 28 * s)} {f(y)} L {f(x + 28 * s)} {f(y - 40 * s)}" stroke="#5A3A22" stroke-width="{f(3 * s)}"></path>'
            + "".join(f'<path d="M{f(x - 34 * s + i * 10 * s)} {f(y - 40 * s)} C {f(x - 30 * s + i * 10 * s)} {f(y - 52 * s)} {f(x - 20 * s + i * 10 * s)} {f(y - 52 * s)} {f(x - 16 * s + i * 10 * s)} {f(y - 40 * s)}" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="1"></path>' for i in range(7)))
def pg_branches(p):   return GND + J1.palm(70, 84, 0.35) + "".join(f'<path d="M{130 + i * 14} 84 C {126 + i * 14} 60 {140 + i * 14} 44 {136 + i * 14} 30" fill="none" stroke="#2E6B3A" stroke-width="4"></path>' for i in range(3)) + booth(250, 84, 1.2) + label(150, 96, "GOODLY TREES · PALMS · THICK TREES · WILLOWS", CY, 6.5)
def pg_dwell(p):      return GND + "".join(booth(50 + i * 72, 84, 0.9) for i in range(4)) + label(160, 14, "YE SHALL DWELL IN BOOTHS SEVEN DAYS", "#FFD23F", 8)
def pg_declared(p):   return GND + A.moses(p, 70, 86, 0.36, up=T.POSES["raise"]) + "".join(man(p, 140 + i * 34, 86, 0.32, A.HEBREW[i], flip=True) for i in range(5))
def pg_oil(p):        return GND + jar(80, 84, 1.0) + S1.lamp(200, 92, 0.5) + label(200, 14, "TO CAUSE A LAMP TO BURN CONTINUALLY", "#FFD23F", 7.5)
def pg_lamps(p):      return GND + priest(p, 90, high=True) + S1.lamp(210, 92, 0.5)
def pg_twelve(p):     return GND + "".join(f'<ellipse cx="{50 + (i % 6) * 44}" cy="{40 + (i // 6) * 26}" rx="18" ry="7" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.2"></ellipse>' for i in range(12)) + label(160, 96, "TWELVE CAKES · TWO ROWS, SIX ON A ROW", CY, 7)
def pg_frankincense(p): return GND + "".join(f'<ellipse cx="{50 + (i % 6) * 44}" cy="{40 + (i // 6) * 26}" rx="18" ry="7" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.2"></ellipse>' for i in range(12)) + "".join(f'<circle cx="{300}" cy="{36 + k * 26}" r="5" fill="#F8F4E0" stroke="#0D0D0F" stroke-width="1"></circle>' for k in range(2)) + label(160, 96, "EVERY SABBATH DAY", "#FFD23F", 7.5)
def pg_curse(p):      return GND + label(160, 50, "WHOSOEVER CURSETH HIS GOD", "#FFD23F", 9) + label(160, 70, "SHALL BEAR HIS SIN", CY, 8)
def pg_life(p):       return GND + '<path d="M160 18 L 160 80 M100 40 L 220 40" stroke="#E8B830" stroke-width="4"></path><path d="M140 82 L 180 82" stroke="#E8B830" stroke-width="5"></path>' + "".join(f'<path d="M{x - 22} 66 C {x - 22} 78 {x + 22} 78 {x + 22} 66 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path><path d="M{x} 40 L {x - 20} 66 M{x} 40 L {x + 20} 66" stroke="#E8B830" stroke-width="1.6"></path>' for x in (100, 220)) + label(160, 96, "LIFE FOR LIFE", CY, 8)
def pg_beast(p):      return GND + S1.cow(110, 84, 0.34, color="#8A5A30", patch="#5A3A22") + label(220, 50, "MAKE IT GOOD", "#FFD23F", 9)
def pg_one_law(p):    return GND + T.figure(p, ("man", "#7A5A3A"), 110, 86, 0.36, pose="staff") + man(p, 210, 86, 0.36, "#5A3A22", flip=True) + label(160, 22, "ONE MANNER OF LAW", "#FFD23F", 9)

# ---- the blasphemer ----
def strife(p, w, h, seed):
    """The son of an Israelitish woman and a man of Israel strove together in the camp."""
    b = h * 0.9
    return (mk.defs(p, *A_ALL) + T.stage(p, w, h, seed, "sand", [(A.hebrew("#7A3A22"), 0.42, 0.42, False, "raise"), (A.hebrew("#4A3A6A"), 0.56, 0.42, True, "point")])
            + "".join(A.black_tent(w * x, b - 4, w * 0.1, h * 0.14) for x in (0.08, 0.2, 0.84, 0.94)))

def ward(p, w, h, seed):
    """They put him in ward: a man sitting bound before a tent, two men standing guard, the tent of meeting beyond."""
    b = h * 0.9
    return (mk.defs(p, *A_ALL) + ground(w, h, h * 0.6, "#C8A06A", dy=0) + V.tabernacle(w * 0.78, h * 0.66, w * 0.34, uid=p + "t") + A.black_tent(w * 0.3, b - 2, w * 0.24, h * 0.3)
            + E.kneel(w * 0.3, b, fit(b, h * 0.62) * 0.9, color="#7A3A22", skin="#8A5A3E") + man(p, w * 0.14, b, fit(b, h * 0.44), "#5A3A22") + man(p, w * 0.46, b, fit(b, h * 0.44), "#4A3A6A", flip=True))

def heap_without(p, w, h, seed):
    """Without the camp: a heap of stones under an evening sky, the congregation going back to the tents (nothing else shown)."""
    b = h * 0.86
    return (mk.defs(p, *A_ALL) + f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A3E"></rect>' + Y.ground(w, h, b, "#4A3A3E", dy=0)
            + A4.stone_heap(w * 0.66, b, w * 0.22, h * 0.26) + "".join(A.black_tent(w * x, b, w * 0.08, h * 0.12, color="#2A2230") for x in (0.08, 0.18, 0.28))
            + "".join(man(p, w * (0.34 + i * 0.07), b, min(fit(b, h * 0.6), 0.9), A.HEBREW[i], flip=True) for i in range(4)))

# ---- Leviticus 25 ----
def pg_land_sabbath(p): return GND + "".join(R.sheaf(26 + i * 36, 84, 0.5) for i in range(6)) + '<rect x="234" y="78" width="70" height="6" fill="#6A5A3A"></rect>' + label(270, 40, "THE SEVENTH YEAR", "#FFD23F", 8) + label(270, 56, "A SABBATH FOR THE LAND", CY, 7)
def pg_of_itself(p):  return GND + '<rect x="40" y="78" width="240" height="6" fill="#6A5A3A"></rect>' + "".join(f'<path d="M{50 + i * 22} 80 L {52 + i * 22} {60 - (i % 3) * 6}" stroke="#9CCB5E" stroke-width="2.4"></path>' for i in range(11)) + label(160, 96, "THAT WHICH GROWETH OF ITSELF", CY, 7)
def pg_food_all(p):   return GND + man(p, 60, 86, 0.32, "#5A3A22") + woman(p, 100, 86, 0.32, "#7A3A5A") + T.figure(p, ("man", "#7A5A3A"), 140, 86, 0.32, pose="staff") + S1.cow(210, 84, 0.26, color="#8A5A30", patch="#5A3A22") + E.sheep(270, 84, 0.3)
def pg_49(p):         return GND + "".join(f'<rect x="{20 + (i % 7) * 18}" y="{14 + (i // 7) * 11}" width="15" height="9" fill="#12113A" stroke="#2C9DB8" stroke-width="0.8"></rect>' for i in range(49)) + '<rect x="160" y="40" width="40" height="30" fill="#FFD23F" stroke="#D7261E" stroke-width="2.4"></rect>' + label(180, 60, "50", "#0D0D0F", 12) + label(240, 50, "7 x 7 YEARS", CY, 8)
def pg_jubilee_horn(p): return GND + J.trumpeter(p, 120, 86, 0.36) + label(220, 40, "PROCLAIM LIBERTY", "#FFD23F", 10) + label(220, 58, "THROUGHOUT THE LAND", CY, 8)
def pg_jubilee(p):    return GND + "".join(A.black_tent(30 + i * 52, 84, 40, 26) for i in range(6)) + label(160, 18, "A JUBILEE · EVERY MAN UNTO HIS POSSESSION", "#FFD23F", 8)
def pg_price(p):      return GND + "".join(f'<rect x="{20 + i * 26}" y="{80 - (10 - i) * 6}" width="20" height="{(10 - i) * 6}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1"></rect>' for i in range(10)) + label(150, 14, "THE NUMBER OF THE YEARS OF THE CROPS", CY, 7) + label(290, 50, "→ 50", "#FFD23F", 10)
def pg_safety(p):     return GND + A.milk_honey(None, 320, 100, 9)
def pg_sixth(p):      return GND + "".join(f'<rect x="{20 + i * 40}" y="40" width="32" height="40" fill="{"#FFD23F" if i == 5 else "#12113A"}" stroke="#2C9DB8" stroke-width="1.2"></rect>' + label(36 + i * 40, 64, str(i + 1), "#0D0D0F" if i == 5 else CY, 10) for i in range(7)) + label(160, 22, "FRUIT FOR THE THREE YEARS", "#FFD23F", 8) + label(300, 64, "→ 9", CY, 9)
def pg_mine(p):       return GND + '<path d="M40 84 L 90 50 L 130 66 L 180 40 L 230 64 L 280 52 L 300 84 Z" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="1.6"></path>' + label(160, 22, "THE LAND IS MINE", "#FFD23F", 10) + T.figure(p, ("man", "#7A5A3A"), 260, 86, 0.3, pose="staff")
def pg_kinsman(p):    return GND + man(p, 60, 86, 0.34, "#8A7A6A") + coins(110, 70, 4) + man(p, 210, 86, 0.36, "#5A3A22", flip=True, up=[(-22, -158), (4, -150), (30, -150)]) + '<rect x="240" y="60" width="50" height="24" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="1.2"></rect>' + label(160, 22, "THE KINSMAN THAT IS NEXT", "#FFD23F", 8)
def pg_walled(p):     return GND + Y.city(120, 84, 120, 60, 3, color="#8A6A5A", lit="#FFC14D", wall="#9A7A6A") + label(250, 40, "A WALLED CITY", "#FFD23F", 8) + label(250, 56, "WITHIN A WHOLE YEAR", CY, 7)
def pg_villages(p):   return GND + "".join(f'<rect x="{50 + i * 40}" y="58" width="28" height="26" fill="#B88A5A" stroke="#0D0D0F" stroke-width="1.2"></rect>' for i in range(3)) + '<rect x="200" y="70" width="90" height="14" fill="#2E6B3A"></rect>' + label(160, 96, "VILLAGES · AS THE FIELDS", CY, 7)
def pg_levites(p):    return GND + Y.city(110, 84, 110, 54, 5, color="#8A6A5A", lit="#FFC14D", wall="#9A7A6A") + priest(p, 220) + label(260, 30, "THE LEVITES", "#FFD23F", 8)
def pg_uphold(p):     return GND + man(p, 120, 86, 0.36, "#8A7A6A", up=REACH) + man(p, 180, 86, 0.38, "#5A3A22", flip=True, up=[(-22, -158), (4, -136), (26, -124)]) + label(260, 40, "NO INTEREST", "#FFD23F", 8)
def pg_brought(p):    return GND + A.EG.pyramid(60, 84, 70, 44) + '<path d="M110 70 L 220 70" stroke="#FFD23F" stroke-width="2" stroke-dasharray="5 4"></path>' + '<path d="M230 84 L 260 50 L 300 84 Z" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="1.4"></path>' + label(265, 96, "CANAAN", CY, 7)
def pg_hired(p):      return GND + man(p, 110, 86, 0.36, "#8A7A6A") + man(p, 190, 86, 0.36, "#5A3A22", flip=True) + label(160, 22, "AS A HIRED SERVANT · NOT A BONDSERVANT", "#FFD23F", 7.5)
def pg_go_out(p):     return GND + man(p, 80, 86, 0.36, "#8A7A6A", up=T.POSES["raise"]) + woman(p, 120, 86, 0.32, "#7A3A5A") + T.figure(p, ("lad", "#C8A06A"), 150, 86, 0.22) + '<path d="M180 70 L 250 70" stroke="#FFD23F" stroke-width="2"></path>' + A.black_tent(280, 84, 40, 26)
def pg_my_servants(p): return GND + A.EG.pyramid(70, 84, 70, 44) + ban(70, 54, 30) + "".join(man(p, 160 + i * 34, 86, 0.32, A.HEBREW[i], flip=True) for i in range(4)) + label(220, 18, "MY SERVANTS", "#FFD23F", 9)
def pg_nations(p):    return GND + "".join(T.figure(p, ("man", c), 60 + i * 44, 86, 0.32) for i, c in enumerate(("#7A5A3A", "#5A6A3A", "#6A4A5A"))) + label(240, 40, "OF THE NATIONS ROUND ABOUT", "#FFD23F", 7.5)
def pg_redeem(p):     return GND + man(p, 60, 86, 0.34, "#8A7A6A") + T.figure(p, ("man", "#7A5A3A"), 120, 86, 0.36) + coins(160, 70, 3) + man(p, 240, 86, 0.36, "#5A3A22", flip=True, up=[(-22, -158), (4, -150), (30, -150)]) + label(220, 18, "ONE OF HIS BRETHREN MAY REDEEM HIM", "#FFD23F", 7)
def pg_reckon(p):     return GND + "".join(f'<rect x="{20 + i * 28}" y="40" width="22" height="30" fill="{"#FFD23F" if i < 3 else "#12113A"}" stroke="#2C9DB8" stroke-width="1"></rect>' for i in range(10)) + label(160, 22, "RECKON THE YEARS UNTO THE JUBILEE", "#FFD23F", 8) + coins(150, 92, 5, r=4)
def pg_go_out_jubilee(p): return pg_go_out(p) + label(160, 18, "IN THE YEAR OF JUBILEE", "#FFD23F", 8)
