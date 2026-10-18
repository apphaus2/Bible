"""New drawings for Numbers chapter 16 (Numbers 34–36): the borders of the land of Canaan as a map (south, west, north,
east), the suburbs of a Levite city (a plan of two thousand cubits on every side), the six cities of refuge (a map), and
pictograms for the law of the manslayer: the instruments (iron, stone, wood), the avenger, the gate of the city of refuge
and the death of the high priest. No killing is drawn: the instruments lie on the ground."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus5 as V
from genesis.art2 import fit, ground, hills
from genesis.art3 import label, man, woman, grid_bg, node, route
from exo import art as A, art8 as B8, art9 as Q
from exo.art7 import ban, coins
from lev.art import GND, priest
from lev.art4 import verdict
from num.art import TRIBE_C
def f(v): return f"{v:.1f}"
CY = B8.CY

def borders(w, h, hi=None):
    """The land of Canaan according to the borders thereof: the south quarter from the wilderness of Zin and the Salt Sea,
    the great sea westward, the north border by mount Hor to the entrance of Hamath, the east border down by Chinnereth
    and the Jordan to the Salt Sea. hi = 'S' / 'W' / 'N' / 'E' lights one border."""
    o = [grid_bg(w, h)]
    sea = f'<path d="M-10 -10 L {f(w * 0.18)} -10 C {f(w * 0.16)} {f(h * 0.3)} {f(w * 0.12)} {f(h * 0.6)} {f(w * 0.08)} {f(h * 0.88)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>'
    o.append(sea + label(w * 0.05, h * 0.5, "THE GREAT SEA", "#8FD0E2", 9, "start"))
    o.append(f'<ellipse cx="{f(w * 0.56)}" cy="{f(h * 0.3)}" rx="{f(w * 0.02)}" ry="{f(h * 0.04)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></ellipse>' + label(w * 0.6, h * 0.3, "CHINNERETH", "#8FD0E2", 8, "start"))
    o.append(f'<path d="M{f(w * 0.56)} {f(h * 0.34)} C {f(w * 0.55)} {f(h * 0.48)} {f(w * 0.57)} {f(h * 0.6)} {f(w * 0.56)} {f(h * 0.66)}" fill="none" stroke="#8FD0E2" stroke-width="3"></path>')
    o.append(f'<ellipse cx="{f(w * 0.56)}" cy="{f(h * 0.74)}" rx="{f(w * 0.03)}" ry="{f(h * 0.08)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></ellipse>' + label(w * 0.6, h * 0.76, "THE SALT SEA", "#8FD0E2", 8, "start"))
    lines = {"S": [(0.58, 0.8), (0.46, 0.86), (0.36, 0.92), (0.24, 0.9), (0.12, 0.86)], "W": [(0.12, 0.86), (0.14, 0.5), (0.18, 0.06)],
             "N": [(0.18, 0.06), (0.36, 0.04), (0.58, 0.02), (0.72, 0.06)], "E": [(0.72, 0.06), (0.66, 0.18), (0.58, 0.28), (0.56, 0.66), (0.58, 0.8)]}
    for k, pts in lines.items():
        on = hi is None or hi == k
        o.append(route([(w * x, h * y) for x, y in pts], color="#FFD23F" if on else "#4A5A6A", sw=3.2 if on else 2, dash="9 5", arrow=False))
    places = {"S": [("ZIN", 0.42, 0.88), ("KADESH-BARNEA", 0.32, 0.93), ("AZMON", 0.2, 0.9), ("BROOK OF EGYPT", 0.12, 0.86)],
              "N": [("MOUNT HOR", 0.26, 0.05), ("HAMATH", 0.44, 0.04), ("ZEDAD", 0.56, 0.03), ("HAZAR-ENAN", 0.72, 0.06)],
              "E": [("SHEPHAM", 0.68, 0.14), ("RIBLAH", 0.62, 0.22)]}
    for k, ps in places.items():
        on = hi is None or hi == k
        for nm, x, y in ps: o.append(node(w * x, h * y, nm, "#FFD23F" if on else "#6A7A8A", r=3.5, dy=-7 if y > 0.1 else 15, size=7.5))
    o.append(label(w * 0.36, h * 0.48, "CANAAN", "#FFD23F", 16, ls=0.3))
    o.append(label(w * 0.84, h * 0.5, "BEYOND THE JORDAN", CY, 8) + label(w * 0.84, h * 0.54, "REUBEN · GAD · ½ MANASSEH", CY, 7))
    return "".join(o)

def suburbs(w, h):
    """A city of the Levites in the midst, its suburbs a thousand cubits from the wall outward, two thousand cubits
    measured on every side."""
    o = [B8.bp(w, h), B8.title_bar(w, "THE SUBURBS OF THE CITIES OF THE LEVITES")]
    cx, cy = w * 0.68, h * 0.56; u = min(w * 0.36, h * 0.8) / 2
    o.append(f'<rect x="{f(cx - u)}" y="{f(cy - u)}" width="{f(2 * u)}" height="{f(2 * u)}" fill="#9CCB5E" opacity="0.35" stroke="#9CCB5E" stroke-width="2" stroke-dasharray="6 4"></rect>')
    o.append(f'<rect x="{f(cx - u * 0.3)}" y="{f(cy - u * 0.3)}" width="{f(u * 0.6)}" height="{f(u * 0.6)}" fill="#B8A88A" stroke="#0D0D0F" stroke-width="2"></rect>' + label(cx, cy + 3, "THE CITY", "#0D0D0F", 8))
    o.append(B8.dim(cx - u, cy + u + 14, cx + u, cy + u + 14, "2,000 CUBITS", size=8) + B8.dim(cx + u * 0.3, cy - u * 0.42, cx + u, cy - u * 0.42, "1,000", size=8))
    for k, (dx, dy) in enumerate(((0, -1), (1, 0), (0, 1), (-1, 0))):
        o.append(label(cx + dx * (u + 18), cy + dy * (u + 18) + 3, ["N", "E", "S", "W"][k], "#FFD23F", 10))
    o.append(label(w * 0.68, h * 0.97, "48 CITIES · 6 OF THEM CITIES OF REFUGE", CY, 8))
    return "".join(o)

def refuge(w, h):
    """Six cities of refuge, three beyond the Jordan and three in the land of Canaan (the cities are named in Joshua 20;
    here only marked)."""
    o = [grid_bg(w, h), label(14, 18, "SIX CITIES OF REFUGE", "#FFD23F", 10, "start", ls=0.16)]
    jx = w * 0.56
    o.append(f'<path d="M{f(jx)} 0 C {f(jx - 8)} {f(h * 0.4)} {f(jx + 8)} {f(h * 0.7)} {f(jx)} {f(h)}" fill="none" stroke="#8FD0E2" stroke-width="3"></path>' + label(jx + 6, h * 0.5, "JORDAN", "#8FD0E2", 8, "start"))
    for i, y in enumerate((0.22, 0.5, 0.78)):
        o.append(node(w * 0.34, h * y, "", "#9CCB5E", r=8) + node(w * 0.74, h * y, "", "#9CCB5E", r=8))
    o.append(label(w * 0.34, h * 0.96, "IN THE LAND OF CANAAN", CY, 8) + label(w * 0.74, h * 0.96, "BEYOND THE JORDAN", CY, 8))
    return "".join(o)

# ---- pictograms (320 x 100) ------------------------------------------------------------------------------------------
def gate(x, y, s=1.0):
    return (f'<rect x="{f(x - 34 * s)}" y="{f(y - 56 * s)}" width="{f(68 * s)}" height="{f(56 * s)}" fill="#B8A88A" stroke="#0D0D0F" stroke-width="2"></rect>'
            f'<path d="M{f(x - 12 * s)} {f(y)} L {f(x - 12 * s)} {f(y - 30 * s)} C {f(x - 12 * s)} {f(y - 42 * s)} {f(x + 12 * s)} {f(y - 42 * s)} {f(x + 12 * s)} {f(y - 30 * s)} L {f(x + 12 * s)} {f(y)} Z" fill="#2A1A10" stroke="#0D0D0F" stroke-width="1.6"></path>'
            + "".join(f'<rect x="{f(x - 34 * s + i * 14 * s)}" y="{f(y - 64 * s)}" width="{f(8 * s)}" height="{f(8 * s)}" fill="#B8A88A" stroke="#0D0D0F" stroke-width="1.2"></rect>' for i in range(5)))
def iron(x, y): return f'<path d="M{f(x - 20)} {f(y - 4)} L {f(x + 14)} {f(y - 4)} L {f(x + 22)} {f(y - 10)} L {f(x + 22)} {f(y)} L {f(x - 20)} {f(y)} Z" fill="#6A6A72" stroke="#0D0D0F" stroke-width="1.4"></path>'
def stone(x, y): return f'<path d="M{f(x - 12)} {f(y)} C {f(x - 14)} {f(y - 12)} {f(x + 10)} {f(y - 16)} {f(x + 14)} {f(y)} Z" fill="#8A8478" stroke="#0D0D0F" stroke-width="1.4"></path>'
def wood(x, y): return f'<path d="M{f(x - 24)} {f(y - 2)} L {f(x + 24)} {f(y - 8)}" stroke="#5A3A22" stroke-width="6" stroke-linecap="round"></path>'
def runner(p, x, y=86, s=0.34, flip=False): return man(p, x, y, s, "#5A4A3A", flip=flip, up=[(-22, -158), (0, -140), (20, -150)])

def pg_levite_cities(p): return GND + gate(110, 84, 1.1) + "".join(man(p, 200 + i * 30, 86, 0.3, "#E8E2D6") for i in range(3))
def pg_cattle(p):        return GND + gate(70, 84, 0.9) + E.sheep(160, 84, 0.34) + E.sheep(210, 84, 0.3) + E3.lamb(260, 84, 0.3)
def pg_thousand(p):      return GND + gate(70, 84, 0.8) + '<path d="M110 70 L 300 70" stroke="#FFD23F" stroke-width="2" stroke-dasharray="6 4"></path>' + label(205, 62, "1,000 CUBITS · OUTWARD", "#FFD23F", 8)
def pg_forty_eight(p):   return GND + "".join(gate(30 + i * 37, 84, 0.42) for i in range(8)) + label(160, 96, "48 CITIES · 6 FOR REFUGE", CY, 7)
def pg_many_few(p):      return GND + gate(80, 84, 0.6) + gate(120, 84, 0.6) + gate(160, 84, 0.6) + label(200, 50, "→", "#FFD23F", 16) + gate(260, 84, 0.6)
def pg_refuge(p):        return GND + runner(p, 90) + '<path d="M130 70 L 200 70" stroke="#FFD23F" stroke-width="2" stroke-dasharray="5 4"></path>' + gate(260, 84, 1.0)
def pg_avenger(p):       return GND + man(p, 60, 86, 0.36, "#8A2A2A") + runner(p, 150) + gate(260, 84, 1.0) + label(60, 96, "THE AVENGER", CY, 7)
def pg_six(p):           return GND + "".join(gate(30 + i * 52, 84, 0.5) for i in range(6)) + label(160, 96, "THREE BEYOND THE JORDAN · THREE IN CANAAN", CY, 6.5)
def pg_stranger(p):      return GND + man(p, 90, 86, 0.34, "#5A3A22") + man(p, 140, 86, 0.34, "#6A6A8A") + gate(250, 84, 1.0)
def pg_iron(p):          return GND + iron(110, 84) + label(110, 96, "AN INSTRUMENT OF IRON", CY, 7) + ban(240, 50, 28)
def pg_stone(p):         return GND + stone(110, 84) + label(110, 96, "A STONE IN THE HAND", CY, 7) + ban(240, 50, 28)
def pg_wood(p):          return GND + wood(110, 84) + label(110, 96, "A WEAPON OF WOOD", CY, 7) + ban(240, 50, 28)
def pg_avenger2(p):      return GND + man(p, 120, 86, 0.38, "#8A2A2A") + label(220, 50, "THE AVENGER OF BLOOD", "#FFD23F", 9)
def pg_hatred(p):        return GND + label(160, 44, "OF HATRED · LYING IN WAIT · IN ENMITY", "#FFD23F", 8.5) + ban(160, 70, 18)
def pg_suddenly(p):      return GND + label(160, 44, "SUDDENLY · WITHOUT ENMITY · SEEING HIM NOT", "#FFD23F", 8) + stone(160, 84)
def pg_judge(p):         return GND + "".join(A.elder(c, i)(p, 50 + i * 36, 86, 0.3) for i, c in enumerate(A.CLOTHS[:4])) + man(p, 220, 86, 0.34, "#5A4A3A", flip=True) + man(p, 270, 86, 0.34, "#8A2A2A", flip=True)
def pg_until_hp(p):      return GND + gate(90, 84, 1.0) + runner(p, 90, s=0.24) + priest(p, 230, high=True) + label(230, 96, "UNTIL THE DEATH OF THE HIGH PRIEST", CY, 6.5)
def pg_border(p):        return GND + gate(70, 84, 0.9) + '<path d="M120 20 L 120 96" stroke="#FFD23F" stroke-width="2" stroke-dasharray="5 4"></path>' + runner(p, 170) + man(p, 260, 86, 0.36, "#8A2A2A", flip=True)
def pg_return(p):        return GND + gate(70, 84, 0.9) + '<path d="M110 70 L 220 70" stroke="#9CCB5E" stroke-width="2" stroke-dasharray="5 4"></path>' + A.black_tent(270, 84, 70, 44) + label(270, 96, "THE LAND OF HIS POSSESSION", CY, 6.5)
def pg_witnesses(p):     return GND + man(p, 80, 86, 0.34, "#5A3A22") + man(p, 120, 86, 0.34, "#4A3A6A") + label(220, 46, "AT THE MOUTH OF WITNESSES", "#FFD23F", 8) + label(220, 64, "NOT ONE WITNESS", CY, 7.5)
def pg_no_ransom(p):     return GND + coins(60, 70, 10) + ban(200, 50, 30) + label(200, 96, "NO RANSOM", CY, 8)
def pg_pollute(p):       return GND + hills(320, 100, 70, 3, color="#6A8A4A", amp=6) + label(160, 40, "BLOOD POLLUTETH THE LAND", "#FFD23F", 10)
def pg_dwell(p):         return GND + V.tabernacle(160, 84, 160, uid=p + "dw") + label(160, 30, "I, JEHOVAH, DWELL IN THE MIDST", "#FFD23F", 8)

def pg_suburbs(p):
    """Two thousand cubits measured on every side, the city in the midst."""
    return (GND + '<rect x="110" y="8" width="100" height="78" fill="#9CCB5E" opacity="0.35" stroke="#9CCB5E" stroke-width="2" stroke-dasharray="5 3"></rect>'
            + '<rect x="146" y="34" width="28" height="26" fill="#B8A88A" stroke="#0D0D0F" stroke-width="1.6"></rect>'
            + label(60, 50, "2,000", "#FFD23F", 11) + label(60, 64, "CUBITS", CY, 7) + label(262, 50, "EVERY SIDE", "#FFD23F", 9) + label(160, 96, "THE CITY BEING IN THE MIDST", CY, 7))

from faces_ex import F
GILEADITE = F("adam", skin="#B98A6E", shadow="#5A3A3A", hair="#B8B2A6", hl="#8A867E", beard=True, beard_color="#B8B2A6", scarf="#6A6A8A", cord=True, light="#FFC14D")
