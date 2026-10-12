"""Pictograms for Leviticus chapter 5 (Leviticus 14–15): the cleansing of the leper (the two birds, cedar, scarlet and
hyssop, the earthen vessel over running water, the bird let go), the eighth day with the log of oil, the plague in a house,
and the laws of issues — drawn only as household things (a bed, a seat, a saddle, a vessel, washing and bathing)."""
import sys, pathlib, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus5 as V, samuel1 as S1, numbers1 as N
from genesis import art2 as Y, art10 as T
from genesis.art3 import label, man, woman
from exo import art as A, art8 as B8, art9 as Q
from exo.art6 import GND
from exo.art7 import ban
from lev.art import altar, door, priest, offerer, dove, REACH, jar, flour
from lev.art4 import days, verdict, insp
def f(v): return f"{v:.1f}"

def cedar(x, y, s=1.0):  return f'<path d="M{f(x - 22 * s)} {f(y)} L {f(x + 22 * s)} {f(y - 6 * s)}" stroke="#8A4A2A" stroke-width="{f(5 * s)}" stroke-linecap="round"></path>'
def scarlet(x, y, s=1.0): return f'<path d="M{f(x - 18 * s)} {f(y)} C {f(x - 6 * s)} {f(y - 12 * s)} {f(x + 6 * s)} {f(y + 8 * s)} {f(x + 18 * s)} {f(y - 4 * s)}" fill="none" stroke="#D7261E" stroke-width="{f(3 * s)}"></path>'
def hyssop(x, y, s=1.0):  return E3.hyssop(x, y, s * 0.5, dipped=False)
def water(x, y, w=60):
    return (f'<path d="M{f(x - w / 2)} {f(y)} C {f(x - w / 4)} {f(y - 6)} {f(x + w / 4)} {f(y + 6)} {f(x + w / 2)} {f(y)}" fill="none" stroke="#2C9DB8" stroke-width="5" stroke-linecap="round"></path>'
            f'<path d="M{f(x - w / 2)} {f(y + 6)} C {f(x - w / 4)} {f(y)} {f(x + w / 4)} {f(y + 12)} {f(x + w / 2)} {f(y + 6)}" fill="none" stroke="#8FD0E2" stroke-width="3" stroke-linecap="round"></path>')
def earthen(x, y, s=1.0): return f'<path d="M{f(x - 16 * s)} {f(y)} L {f(x - 20 * s)} {f(y - 24 * s)} L {f(x + 20 * s)} {f(y - 24 * s)} L {f(x + 16 * s)} {f(y)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.6"></path>'
def bed(x, y, s=1.0):     return (f'<rect x="{f(x - 40 * s)}" y="{f(y - 20 * s)}" width="{f(80 * s)}" height="{f(10 * s)}" rx="3" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                                  f'<path d="M{f(x - 36 * s)} {f(y - 10 * s)} L {f(x - 36 * s)} {f(y)} M{f(x + 36 * s)} {f(y - 10 * s)} L {f(x + 36 * s)} {f(y)}" stroke="#5A3A22" stroke-width="{f(3 * s)}"></path>')
def seat(x, y, s=1.0):    return (f'<rect x="{f(x - 16 * s)}" y="{f(y - 22 * s)}" width="{f(32 * s)}" height="{f(6 * s)}" fill="#8A5A3E" stroke="#0D0D0F" stroke-width="1.4"></rect>'
                                  f'<path d="M{f(x - 12 * s)} {f(y - 16 * s)} L {f(x - 12 * s)} {f(y)} M{f(x + 12 * s)} {f(y - 16 * s)} L {f(x + 12 * s)} {f(y)}" stroke="#5A3A22" stroke-width="{f(3 * s)}"></path>')
def saddle(x, y, s=1.0):  return f'<path d="M{f(x - 24 * s)} {f(y)} C {f(x - 20 * s)} {f(y - 22 * s)} {f(x + 20 * s)} {f(y - 22 * s)} {f(x + 24 * s)} {f(y)} Z" fill="#8A3A2A" stroke="#0D0D0F" stroke-width="1.6"></path>'
def bathe(p, x, y=86, s=0.34):
    return water(x, y - 6, 70) + man(p, x, y - 10, s, "#8FD0E2")
def even(x, y):           return label(x, y, "UNTIL THE EVEN", B8.CY, 8)

def house(x, y, w=90, h=60, spots=False, gone=None, new=False, broken=False):
    """A stone house: rows of stones; spots = greenish or reddish hollow strakes; gone = stones taken out; new = fresh plaster."""
    if broken:
        return "".join(f'<rect x="{f(x - w / 2 + i * 14)}" y="{f(y - 8 - (i % 3) * 6)}" width="13" height="9" fill="#A89E92" stroke="#0D0D0F" stroke-width="1" transform="rotate({(i * 23) % 40 - 20} {f(x - w / 2 + i * 14)} {f(y - 8)})"></rect>' for i in range(7))
    o = [f'<rect x="{f(x - w / 2)}" y="{f(y - h)}" width="{f(w)}" height="{f(h)}" fill="{"#E8E2D6" if new else "#B8AE9E"}" stroke="#0D0D0F" stroke-width="1.8"></rect>',
         f'<rect x="{f(x - 8)}" y="{f(y - 26)}" width="16" height="26" fill="#3A2214" stroke="#0D0D0F" stroke-width="1.4"></rect>']
    if not new:
        for row in range(int(h // 12)):
            for k in range(int(w // 18) + 1):
                o.append(f'<rect x="{f(x - w / 2 + k * 18 + (row % 2) * 9)}" y="{f(y - h + row * 12)}" width="18" height="12" fill="none" stroke="#8A8478" stroke-width="0.8"></rect>')
    if spots: o += [f'<ellipse cx="{f(x + dx)}" cy="{f(y - h + dy)}" rx="7" ry="5" fill="{c}" opacity="0.85"></ellipse>' for dx, dy, c in ((-26, 18, "#7A9A3A"), (24, 30, "#C8504A"), (-14, 40, "#7A9A3A"))]
    if gone: o.append(f'<rect x="{f(x - 34)}" y="{f(y - h + 12)}" width="18" height="24" fill="#12113A" stroke="#0D0D0F" stroke-width="1"></rect>')
    return "".join(o)

# ---- the leper's cleansing ----
def pg_out_camp(p):  return GND + insp(p, 80) + '<path d="M140 20 L 140 96" stroke="#FFD23F" stroke-width="2" stroke-dasharray="5 4"></path>' + man(p, 220, 86, 0.36, "#6A6460", flip=True) + verdict(280, 40, True)
def pg_two_birds(p): return GND + dove(60, 80, 1.1) + dove(100, 80, 1.1, flip=True) + cedar(160, 70) + scarlet(210, 70) + hyssop(260, 84, 1.0) + label(160, 96, "CEDAR · SCARLET · HYSSOP", B8.CY, 7)
def pg_vessel(p):    return GND + water(130, 80, 120) + earthen(130, 72, 1.2) + dove(220, 80, 1.1) + label(130, 96, "AN EARTHEN VESSEL OVER RUNNING WATER", B8.CY, 6.5)
def pg_let_go(p):    return GND + Y.ground(320, 100, 84, "#4A6A3A", dy=0) + dove(80, 80, 1.0) + '<path d="M110 70 C 160 30 220 40 280 20" fill="none" stroke="#FFD23F" stroke-width="2" stroke-dasharray="5 5"></path>' + dove(280, 24, 1.0) + label(200, 96, "INTO THE OPEN FIELD · SEVEN TIMES", B8.CY, 7)
def pg_shave(p):     return GND + '<path d="M60 70 L 100 50" stroke="#C8C8D0" stroke-width="4"></path>' + bathe(p, 170) + E3.basin(260, 82, 30)
def pg_seventh(p):   return GND + days(60, 40, 7) + label(100, 70, "HEAD · BEARD · EYEBROWS", B8.CY, 7) + bathe(p, 250)
def pg_eighth_lambs(p): return GND + E3.lamb(60, 84, 0.34) + E3.lamb(110, 84, 0.34) + E3.lamb(160, 84, 0.3) + flour(220, 84, 0.9) + jar(280, 84, 0.9) + label(280, 96, "A LOG OF OIL", B8.CY, 7)
def pg_before(p):    return GND + door(60, 84) + insp(p, 120) + man(p, 180, 86, 0.36, "#6A6460") + E3.lamb(250, 84, 0.34)
def pg_marks_oil(p): return GND + Q.son_priest(p, 80, 86, 0.36, up=REACH) + man(p, 160, 86, 0.36, "#6A6460", flip=True) + "".join(f'<circle cx="{x}" cy="{y}" r="3.6" fill="{c}"></circle>' for x, y, c in ((166, 22, "#B5121B"), (150, 52, "#B5121B"), (160, 84, "#B5121B"), (172, 24, "#FFD23F"), (156, 54, "#FFD23F"))) + label(250, 40, "EAR · THUMB · TOE", B8.CY, 8)
def pg_palm(p):      return GND + Q.son_priest(p, 100, 86, 0.38, up=[(-22, -158), (-6, -120), (14, -112)]) + jar(160, 84, 0.8) + "".join(f'<circle cx="{200 + i * 10}" cy="{40 + (i % 2) * 6}" r="3" fill="#FFD23F"></circle>' for i in range(7)) + label(250, 70, "SEVEN TIMES", B8.CY, 7)
def pg_head_oil(p):  return GND + man(p, 120, 86, 0.38, "#6A6460") + S1.vial(126, 10, 0.5, rot=-120, pour=14) + altar(240, 84, 1.0)
def pg_atone(p):     return GND + altar(110, 84, 1.3) + flour(220, 84, 0.9) + verdict(280, 40, True)
def pg_poor_lamb(p): return GND + E3.lamb(70, 84, 0.34) + flour(130, 84, 0.7) + jar(180, 84, 0.7) + dove(230, 80, 1.0) + dove(270, 80, 1.0, flip=True)

# ---- the house ----
def pg_canaan(p):    return GND + house(130, 84, spots=True) + man(p, 230, 86, 0.36, "#5A3A22", flip=True) + label(130, 18, "WHEN YE ARE COME INTO THE LAND OF CANAAN", "#FFD23F", 7)
def pg_empty(p):     return GND + house(120, 84) + E4_box(200) + E4_box(230) + insp(p, 280)
def E4_box(x):       return f'<rect x="{x - 12}" y="64" width="24" height="20" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="1.4"></rect>'
def pg_strakes(p):   return GND + house(110, 84, w=110, h=66, spots=True) + label(230, 40, "HOLLOW STRAKES", "#FFD23F", 9) + label(230, 56, "GREENISH OR REDDISH", B8.CY, 7) + days(190, 70, 7)
def pg_stones_out(p): return GND + house(100, 84, gone=True) + '<path d="M150 50 L 220 70" stroke="#FFD23F" stroke-width="2" stroke-dasharray="5 4"></path>' + "".join(f'<rect x="{230 + i * 10}" y="{70 - i * 4}" width="16" height="10" fill="#A89E92" stroke="#0D0D0F" stroke-width="1"></rect>' for i in range(4)) + label(260, 96, "WITHOUT THE CITY", B8.CY, 7)
def pg_scraped(p):   return GND + house(110, 84, new=True) + label(110, 96, "SCRAPED · NEW STONES · NEW MORTAR", B8.CY, 7) + man(p, 220, 86, 0.36, "#5A3A22", up=REACH)
def pg_fretting(p):  return GND + house(100, 84, spots=True) + label(170, 52, "→", "#FFD23F", 18) + house(250, 84, broken=True) + verdict(250, 40, False)
def pg_in_house(p):  return GND + house(100, 84) + man(p, 180, 86, 0.36, "#5A3A22") + E3.basin(250, 82, 28) + even(220, 96)
def pg_house_clean(p): return GND + house(110, 84, new=True) + verdict(220, 50, True) + insp(p, 280)
def pg_house_birds(p): return GND + house(80, 84, w=70, h=50) + dove(150, 80, 1.0) + cedar(200, 70, 0.8) + scarlet(240, 70, 0.8) + water(260, 86, 60)
def pg_field_bird(p): return GND + house(60, 84, w=60, h=46) + '<path d="M100 60 C 160 30 220 40 280 20" fill="none" stroke="#FFD23F" stroke-width="2" stroke-dasharray="5 5"></path>' + dove(280, 24, 1.0) + label(200, 96, "OUT OF THE CITY INTO THE OPEN FIELD", B8.CY, 7)
def pg_law_all(p):   return GND + Q_lens() + '<rect x="130" y="40" width="50" height="34" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.4"></rect>' + house(250, 84, w=70, h=50)
def Q_lens():
    from lev.art4 import lens
    return lens(70, 50, 28, spot="bright")

# ---- issues ----
def pg_issue(p):     return GND + man(p, 80, 86, 0.36, "#6A6460") + bed(180, 84) + label(180, 96, "THE BED · THE SEAT", B8.CY, 7) + seat(270, 84)
def pg_wash_bathe(p): return GND + bed(70, 84, 0.8) + E3.basin(150, 82, 30) + bathe(p, 230) + even(160, 22)
def pg_spit(p):      return GND + man(p, 80, 86, 0.36, "#6A6460") + man(p, 150, 86, 0.36, "#5A3A22", flip=True) + bathe(p, 250) + even(200, 22)
def pg_saddle(p):    return GND + N.ass(110, 84, 0.3) + saddle(108, 52, 0.9) + label(210, 50, "WHATSOEVER WAS UNDER HIM", B8.CY, 7) + even(210, 66)
def pg_rinse(p):     return GND + man(p, 80, 86, 0.36, "#6A6460", up=REACH) + E3.basin(130, 82, 24) + earthen(200, 84, 1.0) + '<path d="M190 66 L 200 76 L 196 84" stroke="#0D0D0F" stroke-width="2" fill="none"></path>' + '<rect x="240" y="60" width="40" height="24" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="1.4"></rect>' + label(200, 96, "EARTHEN · BROKEN", B8.CY, 7) + label(260, 96, "WOOD · RINSED", B8.CY, 7)
def pg_count7(p):    return GND + days(40, 40, 7) + label(80, 70, "SEVEN DAYS", B8.CY, 8) + water(200, 76, 60) + label(200, 96, "RUNNING WATER", B8.CY, 7) + verdict(280, 40, True)
def pg_eighth_doves(p): return GND + door(50, 84) + dove(110, 80, 1.1) + dove(150, 80, 1.1, flip=True) + priest(p, 220) + altar(280, 84, 0.8)
def pg_bathe(p):     return GND + bathe(p, 120) + E3.basin(220, 82, 30) + even(180, 22)
def pg_garment_wash(p): return GND + '<rect x="60" y="40" width="70" height="44" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1.6"></rect>' + E3.basin(180, 82, 34) + even(250, 50)
def pg_both(p):      return GND + water(160, 80, 160) + man(p, 130, 76, 0.32, "#8FD0E2") + woman(p, 190, 76, 0.32, "#8FD0E2", flip=True) + even(160, 22)
def pg_woman_seven(p): return GND + woman(p, 70, 86, 0.36, "#7A3A5A") + days(120, 40, 7) + bed(250, 84, 0.8)
def pg_her_bed(p):   return GND + bed(90, 84) + seat(180, 84) + E3.basin(250, 82, 28) + even(160, 22)
def pg_many_days(p): return GND + woman(p, 70, 86, 0.36, "#7A3A5A") + "".join(f'<rect x="{120 + (i % 12) * 14}" y="{30 + (i // 12) * 14}" width="12" height="12" fill="#12113A" stroke="#2C9DB8" stroke-width="1"></rect>' for i in range(24))
def pg_separate(p):  return GND + door(160, 84, 1.3) + "".join(A.black_tent(40 + i * 34, 84, 28, 20) for i in range(2)) + "".join(A.black_tent(220 + i * 34, 84, 28, 20) for i in range(3)) + label(160, 18, "THAT THEY DIE NOT", "#FFD23F", 8)
def pg_law_issue(p): return GND + bed(80, 84, 0.8) + seat(160, 84) + saddle(230, 84, 0.9) + E3.basin(290, 82, 22)
