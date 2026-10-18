"""Pictograms for Numbers chapter 9 (Numbers 18–19), 320 x 100 law cells like Leviticus: the charge of the priests and
the Levites, the priests' portions (the most holy things, the heave-offerings, the first-fruits, the firstlings and the
redemption-money, the covenant of salt), the tithe and the tithe of the tithe, and the red heifer and the water for
impurity. The heifer's slaying is not shown: she is drawn whole, then only the fire and the ashes."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus5 as V, samuel1 as S1, numbers1 as N, ruth1 as R
from genesis.art3 import label, man
from exo import art8 as B8
from exo.art7 import coins, ban
from lev.art import GND, priest, offerer, REACH, altar, flour, jar, cakes, salt, ears, door, goat, veil
from lev.art4 import verdict, days
from lev.art5 import cedar, scarlet, hyssop, water, earthen, bathe, even
from num.art3 import shroud
def f(v): return f"{v:.1f}"
CY = B8.CY

def levite(p, x, y=86, s=0.36, flip=False): return man(p, x, y, s, "#E8E2D6", flip=flip)
def heifer(x, y, s=1.0): return S1.cow(x, y, s, color="#B5402A", patch="#B5402A")
def fire(x, y, s=1.0): return E.blaze(x, y, 44 * s, 60 * s, 7, n=5)
def ashes(x, y, s=1.0): return f'<path d="M{f(x - 30 * s)} {f(y)} C {f(x - 20 * s)} {f(y - 18 * s)} {f(x + 20 * s)} {f(y - 18 * s)} {f(x + 30 * s)} {f(y)} Z" fill="#8A8478" stroke="#0D0D0F" stroke-width="1.4"></path>'
def tithe(x, y, s=1.0):
    return "".join(f'<rect x="{f(x - 40 * s + i * 8 * s)}" y="{f(y - 30 * s)}" width="{f(6 * s)}" height="{f(30 * s)}" fill="{"#E8B830" if i == 9 else "#C8A06A"}" stroke="#0D0D0F" stroke-width="1"></rect>' for i in range(10))

# ---- 18:1–7 the charge -------------------------------------------------------------------------------------------
def pg_bear(p):        return GND + door(70, 84, 1.1) + priest(p, 150, high=True) + priest(p, 200) + priest(p, 240)
def pg_joined(p):      return GND + priest(p, 70, high=True) + levite(p, 140) + levite(p, 180) + levite(p, 220) + door(285, 84, 1.0)
def pg_not_nigh(p):    return GND + levite(p, 70) + ban(170, 50, 30) + altar(250, 84, 1.0)
def pg_charge(p):      return GND + altar(110, 84, 1.1) + priest(p, 190) + priest(p, 240, flip=True)
def pg_gift(p):        return GND + levite(p, 80) + levite(p, 120) + label(200, 48, "A GIFT", "#FFD23F", 12) + door(280, 84, 1.0)
def pg_within_veil(p): return GND + priest(p, 90, high=True) + veil(200, 84, 1.0) + label(200, 96, "WITHIN THE VEIL", CY, 7)

# ---- 18:8–19 the priests' portion ----------------------------------------------------------------------------------
def pg_heave(p):       return GND + priest(p, 70, high=True) + flour(150, 84, 0.9) + cakes(210, 84, 0.9) + jar(270, 84, 0.8)
def pg_most_holy(p):   return GND + flour(90, 84, 1.0) + goat(170, 84, 0.42) + E.sheep(250, 84, 0.4) + label(170, 96, "MEAL · SIN · TRESPASS", CY, 7)
def pg_males(p):       return GND + priest(p, 100) + priest(p, 150) + priest(p, 200) + label(250, 50, "EVERY MALE", "#FFD23F", 9)
def pg_wave(p):        return GND + priest(p, 70, up=REACH) + man(p, 160, 86, 0.32, "#E8E2D6") + mk.person(p, 210, 86, 0.3, body="#8A5A3E", cloth="#C2456A", woman=True, hair="#1A1210", sw=3) + label(260, 40, "ALL THAT IS CLEAN", CY, 7)
def pg_best(p):        return GND + jar(60, 84, 0.9) + N.grapes(130, 60, 0.4, 2) + ears(200, 84, 1.0) + label(160, 96, "OIL · VINTAGE · GRAIN", CY, 7)
def pg_first_ripe(p):  return GND + N.grapes(80, 56, 0.4, 3) + R.sheaf(160, 84, 0.5) + priest(p, 250, flip=True)
def pg_devoted(p):     return GND + label(160, 56, "EVERYTHING DEVOTED", "#FFD23F", 12) + priest(p, 270, flip=True)
def pg_firstborn(p):   return GND + mk.person(p, 60, 86, 0.2, body="#8A5A3E", cloth="#E8E2D6", sw=2) + E3.lamb(130, 84, 0.34) + coins(200, 70, 5) + label(210, 96, "FIVE SHEKELS · REDEEMED", CY, 7)
def pg_firstling(p):   return GND + S1.cow(80, 84, 0.22, color="#8A5A30", patch="#E8E2D6") + E.sheep(150, 84, 0.36) + goat(210, 84, 0.36) + altar(280, 84, 0.8)
def pg_thigh(p):       return GND + priest(p, 120, up=REACH) + label(220, 50, "THE WAVE-BREAST · THE RIGHT THIGH", CY, 7)
def pg_salt(p):        return GND + salt(110, 84, 1.4) + label(210, 54, "A COVENANT OF SALT", "#FFD23F", 11) + label(210, 70, "FOR EVER", "#FFD23F", 9)

# ---- 18:20–32 the Levites' tithe ------------------------------------------------------------------------------------
def pg_portion(p):     return GND + priest(p, 100, high=True) + V.rays(220, 50, 16, 14, 50, color="#FFF4C2", op=0.5) + label(220, 54, "I AM THY PORTION", "#FFD23F", 10)
def pg_tithe(p):       return GND + tithe(100, 84) + label(100, 96, "THE TITHE IN ISRAEL", CY, 7) + levite(p, 220) + door(285, 84, 0.9)
def pg_no_nigh(p):     return GND + man(p, 80, 86, 0.36, "#5A3A22") + ban(170, 50, 28) + door(250, 84, 1.0)
def pg_no_inherit(p):  return GND + levite(p, 90) + label(200, 50, "NO INHERITANCE", "#FFD23F", 11) + label(200, 66, "AMONG THE CHILDREN OF ISRAEL", CY, 7)
def pg_tithe_tithe(p): return GND + tithe(90, 84) + label(150, 56, "→", "#FFD23F", 18) + f'<rect x="196" y="54" width="6" height="30" fill="#E8B830" stroke="#0D0D0F" stroke-width="1"></rect>' + label(200, 96, "A TITHE OF THE TITHE", CY, 7) + priest(p, 270, high=True, flip=True)
def pg_floor(p):       return GND + ears(80, 84, 1.0) + label(80, 96, "THE THRESHING-FLOOR", CY, 6.5) + N.grapes(200, 56, 0.5, 4) + label(200, 96, "THE WINEPRESS", CY, 6.5)
def pg_best_heave(p):  return GND + levite(p, 70, flip=False) + flour(140, 84, 0.9) + priest(p, 230, high=True, flip=True)
def pg_reward(p):      return GND + levite(p, 80) + mk.person(p, 130, 86, 0.3, body="#8A5A3E", cloth="#6A3A5A", woman=True, hair="#1A1210", sw=3) + cakes(220, 84, 1.0) + label(220, 96, "IN EVERY PLACE", CY, 7)
def pg_no_sin(p):      return GND + levite(p, 100) + verdict(200, 44, True)

# ---- 19 the red heifer ------------------------------------------------------------------------------------------
def pg_heifer(p):      return GND + heifer(140, 84, 0.42) + label(140, 96, "WITHOUT SPOT · NEVER YOKE", CY, 7) + S1.yoke(260, 70, 0.8) + ban(260, 64, 26)
def pg_eleazar(p):     return GND + priest(p, 70) + heifer(160, 84, 0.36) + '<path d="M230 20 L 230 96" stroke="#FFD23F" stroke-width="2" stroke-dasharray="5 4"></path>' + label(275, 50, "WITHOUT THE CAMP", CY, 7)
def pg_seven_toward(p): return GND + priest(p, 70, up=REACH) + "".join(f'<circle cx="{120 + i * 14}" cy="{50 + (i % 2) * 6}" r="3.2" fill="#B5121B"></circle>' for i in range(7)) + door(270, 84, 1.0) + label(190, 96, "SEVEN TIMES · TOWARD THE TENT", CY, 7)
def pg_burn(p):        return GND + fire(160, 86, 1.5) + priest(p, 260, flip=True)
def pg_cedar(p):       return GND + cedar(70, 74) + scarlet(120, 74) + hyssop(170, 84) + fire(250, 86, 1.2)
def pg_wash_even(p):   return GND + bathe(p, 90) + even(220, 56)
def pg_burner(p):      return GND + man(p, 70, 86, 0.36, "#6A5A3A") + water(160, 84, 60) + even(250, 56)
def pg_ashes(p):       return GND + man(p, 60, 86, 0.36, "#E8E2D6") + ashes(150, 84, 1.4) + label(240, 50, "A CLEAN PLACE", CY, 8) + label(240, 66, "WITHOUT THE CAMP", CY, 7)
def pg_gatherer(p):    return GND + man(p, 80, 86, 0.36, "#E8E2D6") + water(180, 84, 70) + even(260, 56) + label(160, 30, "AND THE STRANGER", CY, 7)
def pg_touch_dead(p):  return GND + shroud(90, 84, 1.0) + man(p, 170, 86, 0.36, "#5A3A22") + days(220, 40, 7, lit=7, w=10)
def pg_third(p):       return GND + days(30, 40, 7, lit=7, w=14) + label(65, 72, "THE THIRD DAY", "#FFD23F", 8) + label(115, 86, "THE SEVENTH", "#FFD23F", 8) + verdict(250, 44, True)
def pg_defileth(p):    return GND + man(p, 80, 86, 0.36, "#5A3A22") + door(170, 84, 1.0) + ban(260, 50, 28) + label(260, 96, "CUT OFF", CY, 8)
def pg_tent_dead(p):   return GND + '<path d="M60 84 L 110 40 L 160 84 Z" fill="#3A2A2A" stroke="#0D0D0F" stroke-width="2"></path>' + shroud(110, 82, 0.6) + days(190, 40, 7, lit=7, w=12)
def pg_vessel(p):      return GND + earthen(100, 84, 1.4) + label(100, 96, "NO COVERING BOUND UPON IT", CY, 7) + verdict(240, 44, False)
def pg_field(p):       return GND + R.graves(40, 84, 2, 0.6) + '<path d="M180 76 L 220 72" stroke="#E8E2D6" stroke-width="5" stroke-linecap="round"></path>' + days(230, 30, 7, lit=7, w=10) + label(160, 96, "THE SLAIN · A BONE · A GRAVE", CY, 7)
def pg_running(p):     return GND + ashes(80, 84, 1.0) + label(130, 60, "+", "#FFD23F", 18) + water(190, 80, 60) + earthen(260, 84, 1.2)
def pg_sprinkle(p):    return GND + man(p, 70, 86, 0.36, "#E8E2D6", up=REACH) + hyssop(110, 60, 0.8) + "".join(f'<circle cx="{140 + i * 12}" cy="{50 + (i % 3) * 6}" r="2.6" fill="#8FD0E2"></circle>' for i in range(6)) + '<path d="M220 84 L 260 46 L 300 84 Z" fill="#3A2A2A" stroke="#0D0D0F" stroke-width="2"></path>'
def pg_third_seventh(p): return GND + man(p, 70, 86, 0.36, "#E8E2D6", up=REACH) + days(120, 40, 7, lit=7, w=10) + bathe(p, 260)
def pg_not_purify(p):  return GND + man(p, 100, 86, 0.36, "#5A3A22") + ban(200, 50, 30) + label(200, 96, "CUT OFF", CY, 8)
def pg_perpetual(p):   return GND + man(p, 80, 86, 0.36, "#E8E2D6") + water(170, 84, 60) + even(260, 56)
def pg_toucheth(p):    return GND + man(p, 80, 86, 0.36, "#6A6460") + earthen(160, 84, 1.0) + even(250, 56)
