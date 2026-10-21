"""Drawings for Ezekiel 45–48: the holy oblation as a plan (the Levites' portion, the priests' with the sanctuary in the
midst, the city's with its suburbs and the fields for food, the prince's on either side); the land divided to the tribes
as a map (twelve bands from Dan to Gad, the oblation between Judah and Benjamin) with its borders (the way of Hethlon,
Hamath, Hazar-enon, the Jordan, Tamar, Meribah-kadesh, the brook of Egypt, the great sea); the city foursquare with its
twelve gates after the names of the tribes; the just measures and the oblations as charts; the feasts as a calendar;
the gate of the inner court opened on the sabbath, the prince at its post and the people bowing at its door; the
appointed ways through the north and south gates; the daily lamb morning by morning; the prince's inheritance; the
boiling-places; then the river from under the threshold, measured by thousands of cubits to the ankles, the knees, the
loins and a river to swim in; the trees on its banks; the sea healed and the fishers spreading their nets; and the city
whose name is Jehovah is there, under a great light (no figure). The man of light (art15.man_brass) has no face; God is
never drawn."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ezk.art16 import *
from ezk.art16 import f, K2, K3, P, rect, seated, clouds, smoke, house, INK, EZ_C, GB_BEARD, CAPT, bg, glow, vgrad, rgrad, KK2, JJ2, J1, LIT, LINE, FILL
from ezk.art15 import _VP
from num.art import TRIBE_C
from lev import art as LA
from psa.art import tree as ptree, fish
import exodus3 as E3

GOLD_ = "#FFD23F"
TC = dict(TRIBE_C, JOSEPH="#3A3A5A")

def _prince(p, x, y, s, flip=False, up=None):
    """The prince: a purple robe, a purple headcloth with a gold cord, a black beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#5A2A7A", sw=3, flip=flip, up=up, extra=A.headcloth("#5A2A7A", cord=GOLD_) + A.BLACK_BEARD)

# ---- the holy oblation (reeds; x east, y south; the square from -12,500 to 12,500) --------------------------------------
OBL = {"levites": (-12500, -12500, 25000, 10000), "priests": (-12500, -2500, 25000, 10000), "cityland": (-12500, 7500, 25000, 5000),
       "city": (-2250, 7750, 4500, 4500), "suburbs": (-2500, 7500, 5000, 5000), "food_w": (-12500, 7500, 10000, 5000), "food_e": (2500, 7500, 10000, 5000),
       "sanctuary": (-250, 2250, 500, 500)}
def oblation_plan(w, h, hi=(), title="THE HOLY OBLATION · FIVE AND TWENTY THOUSAND FOURSQUARE"):
    """The oblation foursquare, north up: the Levites' portion, the priests' (the sanctuary in the midst), the possession of
    the city (the city and its suburbs in the midst, the residue on either side for food), and the prince's portion on
    the one side and the other, reaching to the west border and the east. hi: levites, priests, sanctuary, city, food,
    prince."""
    o = [bp(w, h), title_bar(w, title)]
    top = 44; S = min(w * 0.6, h - top - 34)
    u = S / 25000
    cx, cy = w * 0.5, top + 8 + S / 2
    X = lambda x: cx + x * u; Y = lambda y: cy + y * u
    def R(k, fill, lit, sw=1.8, dash=None):
        x, y, a, b = OBL[k]
        return (f'<rect x="{f(X(x))}" y="{f(Y(y))}" width="{f(a * u)}" height="{f(b * u)}" fill="{"#5A4A1A" if lit else fill}" fill-opacity="0.9" stroke="{LIT if lit else LINE}" '
                f'stroke-width="{2.4 if lit else sw}"' + (f' stroke-dasharray="{dash}"' if dash else "") + '></rect>')
    pr = "prince" in hi
    for sx in (-1, 1):                                     # the prince's portion, on either side to the borders
        x0 = X(-12500) if sx < 0 else X(12500)
        x1 = 8 if sx < 0 else w - 8
        o.append(f'<rect x="{f(min(x0, x1))}" y="{f(Y(-12500))}" width="{f(abs(x1 - x0))}" height="{f(S)}" fill="{"#4A2A5A" if pr else "#14263A"}" stroke="{LIT if pr else "#4A7A9A"}" stroke-width="{2 if pr else 1.2}" stroke-dasharray="6 4"></rect>')
        lx = (x0 + x1) / 2
        o.append(label(lx, cy - 6, "THE PRINCE", LIT if pr else "#6A9ABA", 9) + label(lx, cy + 8, "← TO THE WEST BORDER" if sx < 0 else "TO THE EAST BORDER →", LIT if pr else "#6A9ABA", 7))
    o.append(R("levites", "#1E3A56", "levites" in hi) + R("priests", "#24405C", "priests" in hi) + R("cityland", "#1A3048", False))
    fd = "food" in hi
    o.append(R("food_w", "#2A4A3A", fd, sw=1.2) + R("food_e", "#2A4A3A", fd, sw=1.2))
    o.append(R("suburbs", "#203A54", "city" in hi, sw=1, dash="3 3") + R("city", "#3A5A7A", "city" in hi))
    sl = "sanctuary" in hi or "priests" in hi
    sx_, sy_ = X(0), Y(2500)
    o.append(f'<rect x="{f(sx_ - 9)}" y="{f(sy_ - 9)}" width="18" height="18" fill="{GOLD_ if sl else "#8A6A3A"}" stroke="{INK}" stroke-width="1.6"></rect>')
    if sl: o.append(glow("obg", sx_, sy_, 34, 34, "#FFE680", 0.7))
    lc = lambda k: LIT if k in hi else CY
    o.append(label(X(0), Y(-7500) + 4, "THE LEVITES · 25,000 × 10,000", lc("levites"), 9))
    o.append(label(X(-6250), Y(2500) + 4, "THE PRIESTS", lc("priests"), 9) + label(X(6250), Y(2500) + 4, "25,000 × 10,000", lc("priests"), 8))
    o.append(label(X(0), Y(2500) + 24, "THE SANCTUARY", LIT if sl else CY, 8))
    o.append(label(X(-7500), Y(10000) + 4, "FOR FOOD", LIT if fd else "#9CCB5E", 8) + label(X(7500), Y(10000) + 4, "FOR FOOD", LIT if fd else "#9CCB5E", 8))
    o.append(label(X(0), Y(10000) + 4, "THE CITY", lc("city"), 8))
    o.append(dim(X(-12500), Y(12500) + 14, X(12500), Y(12500) + 14, "25,000 REEDS", size=8))
    o.append(label(w - 16, h - 10, "N ↑", CY, 11, "end"))
    return "".join(o)

# ---- the land and its tribes ------------------------------------------------------------------------------------------------
NORTH7 = ["DAN", "ASHER", "NAPHTALI", "MANASSEH", "EPHRAIM", "REUBEN", "JUDAH"]
SOUTH5 = ["BENJAMIN", "SIMEON", "ISSACHAR", "ZEBULUN", "GAD"]
def land_map(w, h, hi=(), bands=True, borders=(), title=None):
    """The land of the inheritance, north up: the great sea on the west, the Jordan and the east sea on the east; bands=True:
    the portions of the tribes from the east side unto the west side, Dan in the north to Gad in the south, and between
    Judah and Benjamin the oblation with the prince's portion on either side; hi lights tribes ("DAN" ...) or "OBLATION" /
    "PRINCE"; borders lights the borders ("N", "E", "S", "W") and names their places."""
    o = [grid_bg(w, h)]
    ny, sy = 30 + h * 0.08, h - 22 - h * 0.05
    coast = lambda y: w * 0.14 + (y - ny) / (sy - ny) * w * 0.12
    jordan = lambda y: w * 0.74 - (y - ny) / (sy - ny) * w * 0.06
    o.append(f'<path d="M-10 -10 L {f(coast(ny) + 4)} -10 L {f(coast(ny))} {f(ny)} L {f(coast(sy))} {f(sy)} L {f(coast(sy) - 8)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(label(w * 0.07, (ny + sy) / 2, "THE GREAT SEA", "#8FD0E2", 8, "middle") if not bands or w > 500 else "")
    if bands:
        names = NORTH7 + ["OBLATION"] + SOUTH5
        ws = [1.0] * 7 + [1.5] + [1.0] * 5
        tot = sum(ws); y = ny
        for nm, k in zip(names, ws):
            y1 = y + (sy - ny) * k / tot
            lit = nm in hi or (nm == "OBLATION" and ("PRINCE" in hi))
            x0, x1 = coast(y), jordan(y); x0b, x1b = coast(y1), jordan(y1)
            if nm == "OBLATION":
                fill = "#5A4A1A" if lit else "#2A2A1A"
                o.append(f'<path d="M{f(x0)} {f(y)} L {f(x1)} {f(y)} L {f(x1b)} {f(y1)} L {f(x0b)} {f(y1)} Z" fill="{fill}" stroke="{LIT if lit else "#8A7A4A"}" stroke-width="{2.2 if lit else 1.2}"></path>')
                mx = (x0 + x1) / 2; sq = (y1 - y) * 0.9; my = (y + y1) / 2
                o.append(f'<rect x="{f(mx - sq / 2)}" y="{f(my - sq / 2)}" width="{f(sq)}" height="{f(sq)}" fill="{"#7A6A2A" if "OBLATION" in hi else "#3A3A22"}" stroke="{LIT}" stroke-width="1.6"></rect>')
                o.append(f'<rect x="{f(mx - 4)}" y="{f(my - 4)}" width="8" height="8" fill="{GOLD_}" stroke="{INK}" stroke-width="1"></rect>')
                pc = LIT if "PRINCE" in hi else "#8A7A4A"
                o.append(label((x0 + mx - sq / 2) / 2 + 2, my + 3, "PRINCE", pc, 7) + label((x1 + mx + sq / 2) / 2, my + 3, "PRINCE", pc, 7))
                o.append(label(mx + sq / 2 + 4, y + 9, "THE OBLATION", LIT if "OBLATION" in hi else "#C8B878", 7, "start") if False else "")
            else:
                c = TC.get(nm, "#4A5A6A")
                o.append(f'<path d="M{f(x0)} {f(y)} L {f(x1)} {f(y)} L {f(x1b)} {f(y1)} L {f(x0b)} {f(y1)} Z" fill="{c if lit else "#16283C"}" fill-opacity="{0.85 if lit else 1}" stroke="{LIT if lit else "#3A5A7A"}" stroke-width="{2 if lit else 1}"></path>')
                o.append(label((x0 + x1 + x0b + x1b) / 4, (y + y1) / 2 + 3.5, nm, "#F3EFE6" if lit else "#6A8AA8", min(10, max(7, (y1 - y) * 0.5)), weight=700 if lit else 600))
            y = y1
    else:
        o.append(f'<path d="M{f(coast(ny))} {f(ny)} L {f(jordan(ny))} {f(ny)} L {f(jordan(sy))} {f(sy)} L {f(coast(sy))} {f(sy)} Z" fill="#1A3048" stroke="#3A5A7A" stroke-width="1"></path>'
                 + label((coast(ny) + jordan(sy)) / 2, (ny + sy) / 2, "THE LAND OF ISRAEL", "#6A8AA8", 10))
    jx0 = jordan(ny)                                       # the Jordan down the east side, the sea of Chinnereth, the east sea
    gy = ny + (sy - ny) * 0.22
    dy0, dy1 = ny + (sy - ny) * 0.46, ny + (sy - ny) * 0.64
    o.append(f'<path d="M{f(jx0)} {f(ny + (sy - ny) * 0.04)} L {f(jordan(dy0))} {f(dy0)}" fill="none" stroke="#8FD0E2" stroke-width="3"></path>')
    o.append(f'<ellipse cx="{f(jordan(gy))}" cy="{f(gy)}" rx="{f(w * 0.012)}" ry="{f((sy - ny) * 0.035)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="1.6"></ellipse>')
    o.append(f'<ellipse cx="{f(jordan((dy0 + dy1) / 2))}" cy="{f((dy0 + dy1) / 2)}" rx="{f(w * 0.018)}" ry="{f((dy1 - dy0) / 2)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="1.6"></ellipse>')
    jx1 = jordan(sy)
    on = lambda k: (k in borders)
    def line(pts, k):
        return route(pts, color=GOLD_ if on(k) else "#4A5A6A", sw=3.2 if on(k) else 1.6, dash="9 5", arrow=False)
    o.append(line([(coast(ny), ny), (jordan(ny) + w * 0.14, ny - h * 0.02)], "N"))
    o.append(line([(jordan(ny) + w * 0.14, ny - h * 0.02), (jordan(ny) + w * 0.02, ny + (sy - ny) * 0.1), (jx0, ny + (sy - ny) * 0.12)], "E"))
    o.append(line([(jordan(sy), sy + 2), (w * 0.48, sy + 6), (w * 0.34, sy + 4), (coast(sy), sy)], "S"))
    if on("E"): o.append(route([(jordan(gy), gy), (jordan(dy0), dy0)], color=GOLD_, sw=3.2, dash="9 5", arrow=False))
    o.append(line([(coast(sy), sy), (coast(ny), ny)], "W"))
    pl = lambda nm, x, y, k, dy=-8, anchor="middle": node(x, y, nm, GOLD_ if on(k) else "#6A7A8A", r=3 if on(k) else 2.4, dy=dy, size=7 if on(k) else 6.5, anchor=anchor)
    if "N" in borders or not bands:
        for i, nm in enumerate(["HETHLON", "ZEDAD", "HAMATH", "BEROTHAH", "SIBRAIM", "HAZER-HATTICON", "HAZAR-ENON"]):
            x = coast(ny) + (jordan(ny) + w * 0.14 - coast(ny)) * (i + 0.6) / 7.4
            o.append(pl(nm, x, ny - h * 0.003 * i, "N", dy=-7 if i % 2 == 0 else 15))
    if "E" in borders or not bands:
        o.append(pl("DAMASCUS", jordan(ny) + w * 0.16, ny + (sy - ny) * 0.05, "E", dy=14) + pl("HAURAN", jordan(ny) + w * 0.12, ny + (sy - ny) * 0.16, "E", dy=14)
                 + pl("GILEAD", jordan(ny) + w * 0.1, ny + (sy - ny) * 0.4, "E", dy=14) + label(jordan(ny + (sy - ny) * 0.34) + 8, ny + (sy - ny) * 0.34, "THE JORDAN", "#8FD0E2", 7, "start")
                 + label(jordan(dy1) + w * 0.03, (dy0 + dy1) / 2 + 3, "THE EAST SEA", "#8FD0E2", 7, "start"))
    if "S" in borders or not bands:
        o.append(pl("TAMAR", w * 0.64, sy + 6, "S", dy=14) + pl("MERIBOTH-KADESH", w * 0.5, sy + 6, "S", dy=14) + pl("THE BROOK OF EGYPT", coast(sy) + 4, sy + 2, "S", dy=14, anchor="end"))
    if not bands or "N" in borders: pass
    o.append(label(w - 14, h - 8, "N ↑", CY, 10, "end"))
    if title: o.append(title_bar(w, title))
    return "".join(o)

def city_plan(w, h, hi=("N", "E", "S", "W")):
    """The city foursquare, four thousand and five hundred reeds on every side, the suburbs two hundred and fifty, and three
    gates on every side after the names of the tribes; the sides in hi lit."""
    o = [bp(w, h), title_bar(w, "THE CITY · FOUR THOUSAND AND FIVE HUNDRED ON EVERY SIDE")]
    S = min(w * 0.5, h - 120)
    cx, cy = w * 0.5, 44 + (h - 44) / 2
    x0, y0 = cx - S / 2, cy - S / 2
    sb = S * 250 / 4500
    o.append(f'<rect x="{f(x0 - sb)}" y="{f(y0 - sb)}" width="{f(S + 2 * sb)}" height="{f(S + 2 * sb)}" fill="#203A54" stroke="#4A7A9A" stroke-width="1" stroke-dasharray="4 3"></rect>')
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(S)}" height="{f(S)}" fill="#24405C" stroke="{LINE}" stroke-width="3"></rect>')
    gates = {"N": ["REUBEN", "JUDAH", "LEVI"], "E": ["JOSEPH", "BENJAMIN", "DAN"], "S": ["SIMEON", "ISSACHAR", "ZEBULUN"], "W": ["GAD", "ASHER", "NAPHTALI"]}
    g = max(10, S * 0.07); fs = 9 if S > 260 else 8
    for side, names in gates.items():
        lit = side in hi
        for i, nm in enumerate(names):
            t = (i + 1) / 4
            if side == "N": gx, gy, lx, ly, an = x0 + S * t, y0, x0 + S * t, y0 - sb - 8, "middle"
            elif side == "S": gx, gy, lx, ly, an = x0 + S * t, y0 + S, x0 + S * t, y0 + S + sb + 16, "middle"
            elif side == "E": gx, gy, lx, ly, an = x0 + S, y0 + S * t, x0 + S + sb + 6, y0 + S * t + 3, "start"
            else: gx, gy, lx, ly, an = x0, y0 + S * t, x0 - sb - 6, y0 + S * t + 3, "end"
            c = TC.get(nm, "#E04A2A") if lit else "#4A6A8A"
            o.append(f'<rect x="{f(gx - g / 2)}" y="{f(gy - g / 2)}" width="{f(g)}" height="{f(g)}" fill="{c}" stroke="{LIT if lit else LINE}" stroke-width="1.6"></rect>')
            if S >= 240: o.append(label(lx, ly, nm, LIT if lit else "#6A8AA8", fs, an))
    o.append(dim(x0, y0 + S + sb + 30, x0 + S, y0 + S + sb + 30, "4,500 REEDS", size=8) if y0 + S + sb + 34 < h else "")
    o.append(label(cx, cy - 4, "THE CITY", CY, 10) + label(cx, cy + 12, "SUBURBS · 250 ROUND ABOUT", "#6A9ABA", 7))
    o.append(label(w - 16, h - 10, "N ↑", CY, 11, "end"))
    return "".join(o)

# ---- charts --------------------------------------------------------------------------------------------------------------------
def measures_plate(w, h):
    """Just balances, a just ephah, a just bath: the ephah and the bath of one measure, each the tenth part of a homer; the
    shekel twenty gerahs; twenty shekels, five and twenty shekels, fifteen shekels, your maneh."""
    o = [bp(w, h), title_bar(w, "JUST BALANCES · A JUST EPHAH · A JUST BATH")]
    k = min(1.0, (h - 40) / 240)
    bx, by = w * 0.14, 40 + 200 * k                       # the balance
    o.append(f'<path d="M{f(bx)} {f(by)} L {f(bx)} {f(by - 150 * k)} M{f(bx - 70 * k)} {f(by - 140 * k)} L {f(bx + 70 * k)} {f(by - 140 * k)}" stroke="#D8C070" stroke-width="{f(4 * k)}" fill="none"></path>'
             + "".join(f'<path d="M{f(bx + sx * 70 * k)} {f(by - 140 * k)} L {f(bx + sx * 54 * k)} {f(by - 80 * k)} M{f(bx + sx * 70 * k)} {f(by - 140 * k)} L {f(bx + sx * 86 * k)} {f(by - 80 * k)}" stroke="#D8C070" stroke-width="1.4"></path>'
                       f'<path d="M{f(bx + sx * 50 * k)} {f(by - 80 * k)} Q {f(bx + sx * 70 * k)} {f(by - 64 * k)} {f(bx + sx * 90 * k)} {f(by - 80 * k)} Z" fill="#D8C070" stroke="{INK}" stroke-width="1.4"></path>' for sx in (-1, 1))
             + f'<path d="M{f(bx - 30 * k)} {f(by)} L {f(bx + 30 * k)} {f(by)}" stroke="#D8C070" stroke-width="{f(6 * k)}"></path>' + label(bx, by + 18, "JUST BALANCES", LIT, 8))
    hx, hy, hw, hh = w * 0.32, 60, w * 0.62, max(26, 34 * k)  # the homer in tenths
    o.append(label(hx, hy - 6, "A HOMER", CY, 9, "start"))
    for i in range(10):
        lit = i == 0
        o.append(f'<rect x="{f(hx + i * hw / 10)}" y="{f(hy)}" width="{f(hw / 10)}" height="{f(hh)}" fill="{"#E8B830" if lit else "#24405C"}" stroke="{LINE}" stroke-width="1.4"></rect>')
    o.append(tag(hx + hw / 20, hy + hh, "THE TENTH PART · AN EPHAH = A BATH", hx + hw * 0.18, hy + hh + 26, color=LIT))
    wy = hy + hh + 64 * k + 30                              # the weights
    gw = hw / 60
    o.append(label(hx, wy - 8, "A SHEKEL = TWENTY GERAHS", CY, 9, "start"))
    for i in range(20):
        o.append(f'<circle cx="{f(hx + 6 + i * 11)}" cy="{f(wy + 8)}" r="4" fill="#C8A040" stroke="{INK}" stroke-width="1"></circle>')
    my = wy + 40 * k + 26
    o.append(label(hx, my - 8, "YOUR MANEH = 20 + 25 + 15 SHEKELS", CY, 9, "start"))
    x = hx
    for n, c in ((20, "#8FD0E2"), (25, "#E8B830"), (15, "#9CCB5E")):
        o.append(f'<rect x="{f(x)}" y="{f(my)}" width="{f(n * gw)}" height="{f(16 * k + 6)}" fill="{c}" fill-opacity="0.75" stroke="{INK}" stroke-width="1.2"></rect>'
                 + label(x + n * gw / 2, my + (16 * k + 6) / 2 + 3, str(n), INK, 9))
        x += n * gw
    return "".join(o)

def portions_plate(w, h):
    """The oblation that ye shall offer: the sixth part of an ephah from a homer of wheat and of barley; the tenth part of a
    bath of oil out of the cor (ten baths are a homer); one lamb out of two hundred."""
    o = [bp(w, h), title_bar(w, "THE OBLATION THAT YE SHALL OFFER")]
    rows = [("WHEAT", "THE SIXTH PART OF AN EPHAH FROM A HOMER", 1 / 60, "#E8C060"), ("BARLEY", "THE SIXTH PART OF AN EPHAH FROM A HOMER", 1 / 60, "#C8A060"),
            ("OIL", "THE TENTH PART OF A BATH OUT OF THE COR · TEN BATHS ARE A HOMER", 1 / 100, "#D8C040"), ("A LAMB", "ONE OUT OF TWO HUNDRED", 1 / 200, "#F3EFE6")]
    top = 44; rh = (h - top - 14) / 4
    bx, bw = w * 0.3, w * 0.62
    for i, (nm, txt, frac, c) in enumerate(rows):
        y = top + i * rh
        k = min(0.9, rh / 90)
        icon = {0: LA.ears(w * 0.08, y + rh * 0.86, k * 1.1, 3), 1: LA.ears(w * 0.08, y + rh * 0.86, k * 1.1, 2), 2: LA.jar(w * 0.09, y + rh * 0.86, k * 1.2), 3: E.sheep(w * 0.09, y + rh * 0.86, k * 0.7)}[i]
        o.append(icon + label(w * 0.17, y + rh * 0.5, nm, LIT, 10, "start"))
        o.append(f'<rect x="{f(bx)}" y="{f(y + rh * 0.42)}" width="{f(bw)}" height="{f(rh * 0.24)}" fill="#24405C" stroke="{LINE}" stroke-width="1.2"></rect>'
                 f'<rect x="{f(bx)}" y="{f(y + rh * 0.42)}" width="{f(max(3, bw * frac))}" height="{f(rh * 0.24)}" fill="{c}" stroke="{INK}" stroke-width="1"></rect>')
        o.append(label(bx, y + rh * 0.34, txt, CY, 8, "start"))
    return "".join(o)

def feasts_plate(w, h, hi=("I1", "I7")):
    """The appointed days: in the first month, the first day (a young bullock; cleanse the sanctuary), the seventh day (for
    every one that erreth), the fourteenth (the passover, a feast of seven days, unleavened bread); in the seventh month,
    the fifteenth (the feast, seven days, the like)."""
    o = [bp(w, h), title_bar(w, "THE APPOINTED DAYS · THE FIRST MONTH AND THE SEVENTH")]
    top = 50; gw = w * 0.42; cw = gw / 7; ch = min(cw * 0.8, (h - top - 70) / 5)
    def month(x0, name, marks):
        out = label(x0, top - 6 + 12, name, CY, 9, "start")
        for d in range(30):
            r_, c_ = divmod(d, 7)
            day = d + 1
            m = next((m for m in marks if m[0] <= day <= m[1]), None)
            lit = m and m[2] in hi
            fill = (m[3] if lit else "#2A4A6A") if m else "#16283C"
            out += (f'<rect x="{f(x0 + c_ * cw)}" y="{f(top + 12 + r_ * ch)}" width="{f(cw - 2)}" height="{f(ch - 2)}" fill="{fill}" stroke="{LIT if lit else "#3A5A7A"}" stroke-width="{1.6 if lit else 1}"></rect>'
                    + label(x0 + c_ * cw + cw / 2 - 1, top + 12 + r_ * ch + ch / 2 + 3, str(day), INK if lit else "#6A8AA8", 8))
        return out
    I = [(1, 1, "I1", "#E8B830"), (7, 7, "I7", "#E8B830"), (14, 21, "PASS", "#C8202A")]
    o.append(month(w * 0.05, "THE FIRST MONTH", I) + month(w * 0.53, "THE SEVENTH MONTH", [(15, 21, "VII", "#2E9A4A")]))
    ly = top + 12 + 5 * ch + 18
    notes = [("I1", "1ST · A YOUNG BULLOCK · CLEANSE THE SANCTUARY"), ("I7", "7TH · FOR HIM THAT ERRETH AND IS SIMPLE"),
             ("PASS", "14TH · THE PASSOVER · SEVEN DAYS · UNLEAVENED BREAD"), ("VII", "15TH · THE FEAST · SEVEN DAYS · THE LIKE")]
    shown = [n for n in notes if n[0] in hi] or notes
    for i, (key, txt) in enumerate(shown):
        if ly + i * 14 < h - 6: o.append(label(w * 0.05, ly + i * 14, txt, LIT, 8, "start"))
    if "PASS" in hi or "VII" in hi:
        ox = w * 0.53
        for i, txt in enumerate(["DAILY · 7 BULLOCKS · 7 RAMS · A HE-GOAT", "AN EPHAH FOR A BULLOCK · AN EPHAH FOR A RAM", "A HIN OF OIL TO AN EPHAH"]):
            if ly + i * 14 < h - 6: o.append(label(ox, ly + i * 14, txt, CY, 8, "start"))
    return "".join(o)

def offerings_plate(w, h, hi=("SABBATH",)):
    """The prince's burnt-offerings: on the sabbath six lambs and a ram; on the new moon a young bullock, six lambs and a ram;
    the meal-offering an ephah for a bullock, an ephah for a ram, for the lambs as he is able, and a hin of oil to an ephah."""
    o = [bp(w, h), title_bar(w, "THE PRINCE'S OFFERINGS")]
    rows = [("SABBATH", 0, 6), ("NEW MOON", 1, 6)]
    top = 44; rh = (h - top - 30) / 2
    for i, (nm, bull, lambs) in enumerate(rows):
        lit = nm in hi
        y = top + i * rh
        o.append(f'<rect x="10" y="{f(y + 4)}" width="{f(w - 20)}" height="{f(rh - 8)}" fill="{"#2A3A2A" if lit else "#12243A"}" stroke="{LIT if lit else "#3A5A7A"}" stroke-width="{2 if lit else 1}"></rect>')
        o.append(label(22, y + 22, ("THE SABBATH DAY" if i == 0 else "THE DAY OF THE NEW MOON"), LIT if lit else "#6A8AA8", 9, "start"))
        k = min(0.5, (rh - 44) / 120, (w * 0.5) / (8 * 64 + 200))
        base = y + rh - 12; x = 30
        if bull:
            o.append(S1.cow(x + 70 * k, base, k * 0.8, color="#5A3A22", patch="#3A2214")); x += 170 * k
        for j in range(lambs):
            o.append(E3.lamb(x + 30 * k, base, k * 0.9)); x += 66 * k
        o.append(E.sheep(x + 46 * k, base, k * 1.1, wool="#D8C8A8")
                 + f'<path d="M{f(x + 70 * k)} {f(base - 44 * k)} c {f(10 * k)} {f(-8 * k)} {f(18 * k)} {f(4 * k)} {f(8 * k)} {f(10 * k)}" stroke="#8A6A3A" stroke-width="{f(4 * k)}" fill="none"></path>')
        x += 100 * k
        meal = ("AN EPHAH FOR THE RAM · FOR THE LAMBS AS HE IS ABLE" if i == 0 else "AN EPHAH FOR THE BULLOCK · AN EPHAH FOR THE RAM")
        o.append(label(w - 22, y + 22, ("6 LAMBS · A RAM" if i == 0 else "A YOUNG BULLOCK · 6 LAMBS · A RAM") + " · WITHOUT BLEMISH", CY, 8, "end"))
        o.append(label(w - 22, base - 2, meal, CY, 7.5, "end") + label(w - 22, base - 14, "A HIN OF OIL TO AN EPHAH", CY, 7.5, "end") if w > 600 else "")
    return "".join(o)

def flow_plan(w, h):
    """In the appointed feasts he that entereth by the way of the north gate shall go forth by the way of the south gate, and
    he that entereth by the south gate by the north: the plan of the whole with the two ways drawn through the outer court."""
    o = [vision_plan(w, h, hi=("north_gate", "south_gate"), zoom=False)]
    ax0, ay0, aw, ah = 12, 34, w - 24, h - 44
    u = min(aw, ah) / 560; cx, cy = ax0 + aw / 2, ay0 + ah / 2
    X = lambda x: cx + x * u; Y = lambda y: cy + y * u
    o.append(route([(X(-6), Y(-244)), (X(-6), Y(-160)), (X(140), Y(-160)), (X(140), Y(160)), (X(-6), Y(160)), (X(-6), Y(244))], color=GOLD_, sw=2.6, dash="8 5"))
    o.append(route([(X(6), Y(244)), (X(6), Y(180)), (X(172), Y(180)), (X(172), Y(-180)), (X(6), Y(-180)), (X(6), Y(-244))], color="#8FD0E2", sw=2.6, dash="8 5"))
    o.append(label(X(-262), Y(-160), "IN BY THE NORTH", GOLD_, 8, "end") + label(X(-262), Y(-160) + 12, "OUT BY THE SOUTH", GOLD_, 8, "end")
             + label(X(-262), Y(160), "IN BY THE SOUTH", "#8FD0E2", 8, "end") + label(X(-262), Y(160) + 12, "OUT BY THE NORTH", "#8FD0E2", 8, "end"))
    return "".join(o)

def inheritance_plate(w, h):
    """If the prince give a gift unto any of his sons, it is their possession by inheritance; if to one of his servants, it
    shall be his to the year of liberty, then return to the prince; the prince shall not take of the people's inheritance."""
    o = [bp(w, h), title_bar(w, "THE PRINCE'S INHERITANCE")]
    def box_(x, y, bw, bh, txt, c=CY, fill="#24405C"):
        return (f'<rect x="{f(x - bw / 2)}" y="{f(y - bh / 2)}" width="{f(bw)}" height="{f(bh)}" fill="{fill}" stroke="{c}" stroke-width="1.8"></rect>' + label(x, y + 3, txt, c, 8.5))
    top = 46; H = h - top - 10
    px, py = w * 0.16, top + H * 0.5
    o.append(box_(px, py, w * 0.2, 34, "THE PRINCE", LIT, "#4A2A5A"))
    sy, vy = top + H * 0.2, top + H * 0.62
    o.append(route([(px + w * 0.1, py - 6), (w * 0.38, sy)], color=GOLD_, sw=2, dash="6 4") + box_(w * 0.5, sy, w * 0.24, 30, "A GIFT TO HIS SONS", GOLD_)
             + route([(w * 0.62, sy), (w * 0.7, sy)], color=GOLD_, sw=2, dash="6 4") + box_(w * 0.84, sy, w * 0.26, 30, "THEIRS BY INHERITANCE", GOLD_))
    o.append(route([(px + w * 0.1, py + 6), (w * 0.38, vy)], color=CY, sw=2, dash="6 4") + box_(w * 0.5, vy, w * 0.24, 30, "A GIFT TO A SERVANT")
             + route([(w * 0.62, vy), (w * 0.7, vy)], color=CY, sw=2, dash="6 4") + box_(w * 0.84, vy, w * 0.26, 30, "TO THE YEAR OF LIBERTY"))
    ry = min(h - 14, vy + 46)
    o.append(route([(w * 0.84, vy + 15), (w * 0.84, ry), (px, ry), (px, py + 17)], color=CY, sw=1.6, dash="4 4") + label(w * 0.5, ry - 6, "THEN IT SHALL RETURN TO THE PRINCE", CY, 8))
    if top + H * 0.92 < ry - 20 or True:
        o.append(label(w * 0.5, top + 8 + 4, "NOT OF THE PEOPLE'S INHERITANCE · THAT MY PEOPLE BE NOT SCATTERED", "#FF8A6A", 8))
    return "".join(o)

def kitchens_plate(w, h):
    """In every corner of the court there was a court, forty cubits long and thirty broad, inclosed, with a wall round about,
    and boiling-places made under the walls round about: the outer court with its four corner courts, and one drawn large."""
    o = [bp(w, h), title_bar(w, "IN EVERY CORNER OF THE COURT · A COURT")]
    k = min(w * 0.3, h - 70) ; x0, y0 = w * 0.06, 50 + (h - 60 - k) / 2
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(k)}" height="{f(k)}" fill="#12243A" stroke="{LINE}" stroke-width="2"></rect>')
    c = k * 40 / 500; d = k * 30 / 500
    for cx_, cy_ in ((x0 + 2, y0 + 2), (x0 + k - c - 2, y0 + 2), (x0 + 2, y0 + k - d - 2), (x0 + k - c - 2, y0 + k - d - 2)):
        o.append(f'<rect x="{f(cx_)}" y="{f(cy_)}" width="{f(c)}" height="{f(d)}" fill="#E8B830" stroke="{LIT}" stroke-width="1.4"></rect>')
    o.append(f'<rect x="{f(x0 + k * 0.4)}" y="{f(y0 + k * 0.4)}" width="{f(k * 0.2)}" height="{f(k * 0.2)}" fill="#24405C" stroke="{LINE}" stroke-width="1.2"></rect>'
             + label(x0 + k / 2, y0 + k + 16, "THE OUTER COURT", CY, 8))
    W_ = w * 0.5; H_ = W_ * 30 / 40
    if H_ > h - 90: H_ = h - 90; W_ = H_ * 40 / 30
    bx, by = w * 0.44, 50 + (h - 50 - H_) / 2 - 6
    o.append(f'<rect x="{f(bx)}" y="{f(by)}" width="{f(W_)}" height="{f(H_)}" fill="#1A3450" stroke="{LIT}" stroke-width="3"></rect>')
    for i in range(6):
        for (hx, hy) in ((bx + W_ * (0.1 + i * 0.16), by + 8), (bx + W_ * (0.1 + i * 0.16), by + H_ - 22)):
            o.append(f'<rect x="{f(hx)}" y="{f(hy)}" width="{f(W_ * 0.1)}" height="14" fill="#5A3A22" stroke="{INK}" stroke-width="1.2"></rect>'
                     f'<path d="M{f(hx + W_ * 0.02)} {f(hy + 2)} q {f(W_ * 0.03)} -8 {f(W_ * 0.06)} 0" stroke="#FF8A3D" stroke-width="2" fill="none"></path>')
    o.append(dim(bx, by + H_ + 14, bx + W_, by + H_ + 14, "FORTY CUBITS", size=8) + dim(bx + W_ + 14, by, bx + W_ + 14, by + H_, "THIRTY", size=8))
    o.append(label(bx + W_ / 2, by + H_ / 2 + 3, "BOILING-PLACES UNDER THE WALLS", CY, 8))
    o.append(route([(x0 + k - c / 2, y0 + d), (bx, by + 6)], color=LIT, sw=1.2, dash="3 3", arrow=False))
    return "".join(o)

# ---- scenes ---------------------------------------------------------------------------------------------------------------------
def open_gate(p, w, h, seed):
    """The gate of the inner court that looketh toward the east, shut the six working days, opened on the sabbath and the new
    moon: its doors open, the priests' fire on the altar seen within, the prince standing by the post of the gate, the
    people of the land bowing at the door."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bg(f"og{seed}", w, h, [(0, "#3A4A7A"), (1, "#E8D8B8")])]
    gx, gw, gt = w * 0.5, w * 0.36, h * 0.2
    o.append(f'<rect x="{f(gx - gw / 2)}" y="{f(gt)}" width="{f(gw)}" height="{f(b - gt)}" fill="#C8B490" stroke="{INK}" stroke-width="2.4"></rect>'
             + "".join(f'<rect x="{f(gx - gw / 2 + i * gw / 8)}" y="{f(gt - 12)}" width="{f(gw / 16)}" height="12" fill="#C8B490" stroke="{INK}" stroke-width="1.6"></rect>' for i in range(8)))
    ow = gw * 0.44; ot = gt + (b - gt) * 0.3
    o.append(glow(f"ogg{seed}", gx, ot + (b - ot) * 0.5, ow * 0.8, (b - ot) * 0.7, "#FFE680", 0.6))
    o.append(P(f"M{f(gx - ow / 2)} {f(b)} L {f(gx - ow / 2)} {f(ot + ow * 0.3)} Q {f(gx)} {f(ot - ow * 0.1)} {f(gx + ow / 2)} {f(ot + ow * 0.3)} L {f(gx + ow / 2)} {f(b)} Z", "#F3D890", 2.4))
    o.append(K1.horned_altar(gx, b - (b - ot) * 0.12, min(0.5, (b - ot) / 320), fire=True, seed=seed))
    for sx in (-1, 1):                                      # the doors swung open
        o.append(P(f"M{f(gx + sx * ow / 2)} {f(b)} L {f(gx + sx * ow / 2)} {f(ot + ow * 0.3)} L {f(gx + sx * ow * 0.78)} {f(ot + ow * 0.36)} L {f(gx + sx * ow * 0.78)} {f(b + 4)} Z", "#6A4A2A", 2))
    o.append(ground(w, h, b, "#B8A888", dy=0))
    s = min(fit(b, h * 0.5), 0.7)
    o.append(_prince(p, gx - ow * 0.78, b + 2, s, flip=False))
    ks = s * 0.8
    for i in range(3):
        o.append(E.kneel(w * (0.04 + i * 0.1), b, ks, color=CAPT[i % len(CAPT)]))
        o.append(E.kneel(w * (0.96 - i * 0.1), b, ks, color=CAPT[(i + 3) % len(CAPT)], flip=True))
    return "".join(o)

def morning_altar(p, w, h, seed):
    """Thou shalt prepare a lamb a year old without blemish for a burnt-offering unto Jehovah daily, morning by morning: dawn
    over the court, the altar's smoke going up, a priest bringing the lamb, the fine flour and the oil beside it."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(f"ma{seed}", w, h, [(0, "#3A3A6A"), (0.55, "#E8906A"), (1, "#F3D8A0")])]
    o.append(sun(w * 0.84, h * 0.56, min(w, h) * 0.06, color="#FFE680", glow="#FFF4C2", op=0.3))
    o.append(K1.temple_front(w * 0.2, h * 0.6, w * 0.3, seed))
    o.append(ground(w, h, h * 0.6, "#D8C8A0", dy=0))
    k = min(0.75, h / 420)
    o.append(smoke(w * 0.56, b - 120 * k, 5, seed, color="#E8E2D6", op=0.7, k=k * 0.7))
    o.append(K1.horned_altar(w * 0.56, b, k, fire=True, seed=seed))
    s = min(fit(b, h * 0.4), 0.9)
    o.append(K1.priest(p, w * 0.82, b, s, flip=True) + E3.lamb(w * 0.72, b, s * 0.7, flip=True))
    o.append(LA.jar(w * 0.4, b, k * 0.8) + LA.cakes(w * 0.33, b, k * 0.8))
    return "".join(o)

def boiling_houses(p, w, h, seed):
    """These are the boiling-houses, where the ministers of the house shall boil the sacrifice of the people: a corner court
    inclosed by its wall, the hearths under the walls with their pots and smoke, the Levites tending them."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(f"bh{seed}", w, h, [(0, "#4A5A8A"), (1, "#E8D0A8")])]
    top = h * 0.3
    o.append(f'<rect x="-10" y="{f(top)}" width="{f(w + 20)}" height="{f(b - top)}" fill="#C8B490" stroke="{INK}" stroke-width="2.4"></rect>'
             + "".join(f'<path d="M-10 {f(top + j * (b - top) / 5)} L {f(w + 10)} {f(top + j * (b - top) / 5)}" stroke="#A8946E" stroke-width="1.2"></path>' for j in range(1, 5)))
    o.append(ground(w, h, b, "#B8A47E", dy=0))
    k = min(1.0, h / 300)
    for i in range(4):
        x = w * (0.14 + i * 0.24)
        o.append(f'<path d="M{f(x - 40 * k)} {f(b)} L {f(x - 40 * k)} {f(b - 30 * k)} L {f(x + 40 * k)} {f(b - 30 * k)} L {f(x + 40 * k)} {f(b)} Z" fill="#7A5A3A" stroke="{INK}" stroke-width="2"></path>'
                 + E.blaze(x, b - 30 * k, 50 * k, 22 * k, seed + i, n=4)
                 + f'<path d="M{f(x - 26 * k)} {f(b - 34 * k)} C {f(x - 28 * k)} {f(b - 70 * k)} {f(x + 28 * k)} {f(b - 70 * k)} {f(x + 26 * k)} {f(b - 34 * k)} Z" fill="#4A3A30" stroke="{INK}" stroke-width="2"></path>'
                 + smoke(x, b - 74 * k, 3, seed + i, color="#E8E2D6", op=0.6, k=k * 0.5))
    s = min(fit(b + 4, h * 0.42), 0.8)
    o.append(mk.person(p, round(w * 0.27), round(b + 4), round(s, 3), body=SKIN, cloth="#5A6A8A", sw=3, extra=A.headcloth("#E8E2D6") + A.BLACK_BEARD))
    o.append(mk.person(p, round(w * 0.63), round(b + 4), round(s, 3), body=SKIN, cloth="#4A5A7A", sw=3, flip=True, extra=A.headcloth("#E8E2D6") + A.BLACK_BEARD))
    return "".join(o)

# ---- the river ---------------------------------------------------------------------------------------------------------------
WATER = "#2C9DB8"
def river_threshold(p, w, h, seed):
    """Waters issued out from under the threshold of the house eastward, from the right side of the house, on the south of
    the altar: the house at morning, the stream running out under its threshold past the altar toward the east."""
    b = h * 0.66
    o = [mk.defs(p, *ALL), bg(f"rt{seed}", w, h, [(0, "#5A7AB0"), (1, "#F3E0B8")])]
    o.append(K1.temple_front(w * 0.3, b, w * 0.42, seed))
    o.append(ground(w, h, b, "#E8D8B0", dy=0))
    o.append(f'<path d="M{f(w * 0.36)} {f(b)} C {f(w * 0.42)} {f(b + h * 0.06)} {f(w * 0.5)} {f(b + h * 0.1)} {f(w * 0.66)} {f(b + h * 0.16)} C {f(w * 0.8)} {f(b + h * 0.22)} {f(w * 0.9)} {f(h * 0.94)} {f(w + 10)} {f(h * 0.96)} '
             f'L {f(w + 10)} {f(h + 10)} C {f(w * 0.86)} {f(h + 10)} {f(w * 0.76)} {f(b + h * 0.28)} {f(w * 0.64)} {f(b + h * 0.2)} C {f(w * 0.5)} {f(b + h * 0.14)} {f(w * 0.42)} {f(b + h * 0.08)} {f(w * 0.36)} {f(b)} Z" '
             f'fill="{WATER}" stroke="{INK}" stroke-width="2"></path>')
    for i in range(7):
        x = w * (0.42 + i * 0.08); y = b + h * (0.06 + i * 0.045)
        o.append(f'<path d="M{f(x)} {f(y)} q 8 -4 16 0" stroke="#E8F6FA" stroke-width="1.6" fill="none"></path>')
    o.append(K1.horned_altar(w * 0.56, b + 2, min(0.7, h / 500), fire=False, seed=seed))
    s = min(fit(h * 0.98, h * 0.64), 0.7)
    o.append(man_brass(p, w * 0.76, h * 0.84, s * 0.9, flip=True) + ezek_fig(p, w * 0.1, h * 0.98, s))
    return "".join(o)

def depths(p, w, h, seed):
    """He measured a thousand cubits, and the waters were to the ankles; again a thousand, to the knees; again a thousand,
    to the loins; afterward a thousand, and it was a river that could not be passed through, waters to swim in: four
    scenes side by side, Ezekiel in the water, the man of light with his line on the bank."""
    o = [mk.defs(p, *ALL), bg(f"dp{seed}", w, h, [(0, "#6A9AC8"), (1, "#F3E8D0")])]
    n = 4; cw = w / n
    s = min(fit(h * 0.94, h * 0.2), (cw * 0.5) / 60, 0.9)
    base = h * 0.94
    for i, (lvl, txt) in enumerate(((10, "1,000 · THE ANKLES"), (55, "2,000 · THE KNEES"), (95, "3,000 · THE LOINS"), (None, "4,000 · TO SWIM IN"))):
        x0 = i * cw
        o.append(f'<rect x="{f(x0)}" y="0" width="{f(cw)}" height="{f(h)}" fill="none" stroke="#0D0D0F" stroke-width="1.2" opacity="0.35"></rect>')
        cx = x0 + cw * 0.5
        wl_ = base - (lvl if lvl is not None else 240) * s
        if lvl is not None: o.append(ezek_fig(p, cx, base, s))
        o.append(f'<rect x="{f(x0 + 1)}" y="{f(wl_)}" width="{f(cw - 2)}" height="{f(h - wl_ + 2)}" fill="{WATER}" opacity="{0.82 if lvl is None else 0.7}"></rect>'
                 + f'<path d="M{f(x0 + 4)} {f(wl_)} ' + " ".join(f"q {f(cw / 12)} -5 {f(cw / 6)} 0" for _ in range(6)) + '" stroke="#E8F6FA" stroke-width="1.6" fill="none"></path>')
        if lvl is None:
            for j in range(3):
                o.append(f'<path d="M{f(x0 + cw * 0.15)} {f(wl_ + 30 + j * 26)} ' + " ".join(f"q {f(cw / 10)} -6 {f(cw / 5)} 0" for _ in range(3)) + '" stroke="#E8F6FA" stroke-width="1.4" fill="none" opacity="0.7"></path>')
        o.append(f'<rect x="{f(x0 + 6)}" y="6" width="{f(cw - 12)}" height="18" fill="#F3EFE6" stroke="{INK}" stroke-width="1.4"></rect>' + label(cx, 19, txt, INK, 8 if cw > 150 else 7))
    return "".join(o)

def banks(p, w, h, seed):
    """Upon the bank of the river were very many trees on the one side and on the other: the river running from the house on
    the mountain down through the land, trees thick on both banks, Ezekiel on the bank."""
    o = [mk.defs(p, *ALL), bg(f"bk{seed}", w, h, [(0, "#6AA0D0"), (1, "#E8F0D0")])]
    hz = h * 0.34
    o.append(hills(w, h, hz, seed, "#7A9A6A", amp=10, step=90))
    o.append(K1.temple_front(w * 0.5, hz + 4, w * 0.12, seed))
    o.append(ground(w, h, hz + 4, "#9CCB5E", dy=0))
    o.append(f'<path d="M{f(w * 0.48)} {f(hz + 4)} L {f(w * 0.52)} {f(hz + 4)} C {f(w * 0.6)} {f(h * 0.6)} {f(w * 0.74)} {f(h * 0.8)} {f(w * 0.8)} {f(h + 10)} L {f(w * 0.2)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.8)} {f(w * 0.42)} {f(h * 0.6)} {f(w * 0.48)} {f(hz + 4)} Z" fill="{WATER}" stroke="{INK}" stroke-width="2"></path>')
    r = random.Random(seed)
    for row in range(5):
        t = row / 4; y = hz + 12 + (h - hz) * (0.08 + t * 0.85); sc = 0.08 + t * 0.32
        sc = min(sc, h / 900)
        lx = w * 0.46 - (w * 0.26) * t - 24 * sc * 4; rx = w * 0.54 + (w * 0.26) * t + 24 * sc * 4
        for side, x in ((-1, lx), (1, rx)):
            for j in range(2):
                o.append(ptree(x + side * j * 110 * sc, y, sc, seed + row * 7 + j + (side > 0) * 3, fruit=True))
    s = min(fit(h * 0.98, h * 0.6), 0.6)
    o.append(ezek_fig(p, w * 0.12, h * 0.98, s))
    return "".join(o)

def healed_sea(p, w, h, seed):
    """These waters go down into the Arabah and toward the sea, and the waters shall be healed; a very great multitude of fish;
    fishers shall stand by it from En-gedi unto En-eglaim, a place for the spreading of nets; the miry places and the
    marshes given up to salt."""
    o = [mk.defs(p, *ALL), bg(f"hs{seed}", w, h, [(0, "#7AA8D0"), (1, "#F3E0B8")])]
    sea_t = h * 0.42
    o.append(hills(w, h, sea_t - h * 0.04, seed, "#B8906A", amp=16, step=70))
    o.append(f'<rect x="-10" y="{f(sea_t)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="#1F7FA8" stroke="{INK}" stroke-width="2"></rect>')
    r = random.Random(seed)
    for _ in range(int(w / 26)):
        o.append(fish(r.uniform(20, w - 20), r.uniform(sea_t + 16, h * 0.8), r.uniform(0.4, 0.7), flip=r.random() < 0.5, color=r.choice(["#C8D8E0", "#E8C878", "#A8C8B8"])))
    o.append(f'<path d="M-10 {f(h * 0.8)} L {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#D8C090" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.74)} {f(h * 0.8)} C {f(w * 0.8)} {f(h * 0.86)} {f(w * 0.96)} {f(h * 0.84)} {f(w + 10)} {f(h * 0.88)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.7)} {f(h + 10)} Z" fill="#F3F0E8" stroke="#B8B0A0" stroke-width="1.6"></path>')
    for i in range(3):                                     # nets spread to dry on poles
        x = w * (0.1 + i * 0.16); y = h * 0.96
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - h * 0.12)} M{f(x + w * 0.1)} {f(y)} L {f(x + w * 0.1)} {f(y - h * 0.12)}" stroke="#5A3A22" stroke-width="3"></path>'
                 f'<path d="M{f(x)} {f(y - h * 0.12)} Q {f(x + w * 0.05)} {f(y - h * 0.02)} {f(x + w * 0.1)} {f(y - h * 0.12)}" stroke="#E8E2D6" stroke-width="1.4" fill="#3A5A6A" fill-opacity="0.35"></path>')
    s = min(fit(h * 0.98, h * 0.6), 0.6)
    for i in range(2):
        o.append(mk.person(p, round(w * (0.56 + i * 0.08)), round(h * 0.98), round(s, 3), body=SKIN, cloth=CAPT[i + 2], sw=3, flip=i == 1, extra=A.headcloth(CAPT[i + 2]) + A.BLACK_BEARD,
                           up=[(-22, -158), (-50, -150), (-80, -140)] if i == 0 else None))
    o.append(label(w * 0.03, h * 0.8 + 13, "EN-GEDI", "#0D0D0F", 8, "start") + label(w * 0.9, h * 0.8 + 30, "SALT", "#6A6458", 8))
    return "".join(o)

def healing_tree(p, w, h, seed):
    """By the river upon the bank shall grow every tree for food, whose leaf shall not wither, neither shall the fruit thereof
    fail; new fruit every month, because the waters thereof issue out of the sanctuary: fruit trees on the bank, laden, the
    river shining past them."""
    o = [mk.defs(p, *ALL), bg(f"ht{seed}", w, h, [(0, "#5A9AD0"), (1, "#F3F0C8")])]
    o.append(hills(w, h, h * 0.5, seed, "#8AB86A", amp=8, step=80))
    o.append(f'<path d="M-10 {f(h * 0.7)} C {f(w * 0.3)} {f(h * 0.62)} {f(w * 0.6)} {f(h * 0.76)} {f(w + 10)} {f(h * 0.68)} L {f(w + 10)} {f(h * 0.82)} C {f(w * 0.6)} {f(h * 0.9)} {f(w * 0.3)} {f(h * 0.78)} -10 {f(h * 0.86)} Z" fill="{WATER}" stroke="{INK}" stroke-width="2"></path>')
    o.append(ground(w, h, h * 0.86, "#7AB85A", dy=0) if False else "")
    for i, x in enumerate((0.12, 0.36, 0.64, 0.88)):
        s = min(h * 0.5 / 260, 1.0) * (1 if i % 2 else 0.85)
        o.append(ptree(w * x, h * (0.72 if i % 2 else 0.7), s, seed + i, fruit=True))
    o.append(f'<path d="M-10 {f(h * 0.86)} C {f(w * 0.3)} {f(h * 0.78)} {f(w * 0.6)} {f(h * 0.9)} {f(w + 10)} {f(h * 0.82)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#7AB85A" stroke="{INK}" stroke-width="2"></path>')
    for i in range(6):
        o.append(ptree(w * (0.06 + i * 0.18), h * 1.02, min(h * 0.32 / 260, 0.7), seed + 10 + i, fruit=True))
    return "".join(o)

def city_glory(p, w, h, seed, figures=True):
    """The name of the city from that day shall be, Jehovah is there: a city foursquare on a plain at dawn, three gates in
    each wall seen, a great light standing over it and filling the sky (no figure), Ezekiel looking on."""
    o = [mk.defs(p, *ALL), bg(f"cg{seed}", w, h, [(0, "#1A1A4A"), (0.45, "#E89A5A"), (1, "#F3E0B0")])]
    cx = w * 0.5; base = h * 0.78
    o.append(V.rays(cx, h * 0.3, 40, h * 0.06, max(w, h) * 1.2, color="#FFF4C2", op=0.2))
    o.append(glow(f"cgg{seed}", cx, h * 0.3, w * 0.5, h * 0.36, "#FFE680", 0.95, core="#FFFFFF"))
    o.append(hills(w, h, base - h * 0.08, seed, "#B8906A", amp=8, step=100))
    fw, fh = w * 0.62, h * 0.2                              # the front wall, the east (three gates), the north side receding
    x0 = cx - fw / 2; top = base - fh
    dx, dy = fw * 0.22, -fh * 0.42
    o.append(P(f"M{f(x0 + fw)} {f(base)} L {f(x0 + fw + dx)} {f(base + dy)} L {f(x0 + fw + dx)} {f(top + dy)} L {f(x0 + fw)} {f(top)} Z", "#C8A878", 2.4))
    o.append(P(f"M{f(x0)} {f(top)} L {f(x0 + dx)} {f(top + dy)} L {f(x0 + fw + dx)} {f(top + dy)} L {f(x0 + fw)} {f(top)} Z", "#E8D0A0", 2.4))
    r = random.Random(seed)
    for j in reversed(range(5)):                            # the houses within, seen over the wall (far rows first)
        for i in range(9):
            t_ = (j + 0.6) / 5.6
            hx = x0 + dx * t_ + fw * (0.04 + i * 0.105) + r.uniform(-4, 4); hy = top + dy * t_
            hw_, hh_ = fw * 0.07, fh * r.uniform(0.18, 0.34)
            o.append(f'<rect x="{f(hx)}" y="{f(hy - hh_)}" width="{f(hw_)}" height="{f(hh_)}" fill="{r.choice(["#E8D4A8", "#D8C090", "#F0DCB0"])}" stroke="{INK}" stroke-width="1.4"></rect>')
    o.append(f'<rect x="{f(x0)}" y="{f(top)}" width="{f(fw)}" height="{f(fh)}" fill="#E0C090" stroke="{INK}" stroke-width="2.6"></rect>'
             + "".join(f'<rect x="{f(x0 + i * fw / 24)}" y="{f(top - fh * 0.08)}" width="{f(fw / 48)}" height="{f(fh * 0.08)}" fill="#E0C090" stroke="{INK}" stroke-width="1.4"></rect>' for i in range(24)))
    for i in range(3):
        gx = x0 + fw * (i + 1) / 4; gw = fw * 0.07
        o.append(P(f"M{f(gx - gw / 2)} {f(base)} L {f(gx - gw / 2)} {f(base - fh * 0.5)} Q {f(gx)} {f(base - fh * 0.72)} {f(gx + gw / 2)} {f(base - fh * 0.5)} L {f(gx + gw / 2)} {f(base)} Z", "#FFE8A0", 2))
        o.append(f'<rect x="{f(gx - gw * 0.8)}" y="{f(top - fh * 0.18)}" width="{f(gw * 1.6)}" height="{f(fh * 0.18)}" fill="#E0C090" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(3):
        t = (i + 1) / 4
        gx = x0 + fw + dx * t; gy = base + dy * t
        o.append(f'<path d="M{f(gx - 4)} {f(gy)} L {f(gx - 4)} {f(gy - fh * 0.42)} L {f(gx + 6)} {f(gy - fh * 0.46)} L {f(gx + 6)} {f(gy - 2)} Z" fill="#FFE8A0" stroke="{INK}" stroke-width="1.6"></path>')
    o.append(ground(w, h, base, "#D8B880", dy=0))
    s = min(fit(h * 0.98, h * 0.7), 0.7)
    if figures: o.append(ezek_fig(p, w * 0.1, h * 0.98, s) + man_brass(p, w * 0.24, h * 0.98, s, flip=True))
    return "".join(o)

def passover(p, w, h, seed):
    """In the first month, in the fourteenth day, the passover, a feast of seven days; unleavened bread shall be eaten; the
    prince shall prepare for himself and for all the people of the land a bullock for a sin-offering: evening before the
    gate, the prince leading the bullock, the people with their unleavened cakes."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bg(f"pv{seed}", w, h, [(0, "#2A2A5A"), (0.6, "#C8705A"), (1, "#F0C890")])]
    o.append(sun(w * 0.86, h * 0.5, min(w, h) * 0.05, color="#FFD27A", glow="#FFE8B0", op=0.25))
    o.append(S4.gatehouse(w * 0.5, b - h * 0.06, w * 0.34, h * 0.5))
    o.append(ground(w, h, b - h * 0.06, "#C8A878", dy=0))
    s = min(fit(b, h * 0.42), 0.8)
    o.append(_prince(p, w * 0.32, b, s, flip=True) + S1.cow(w * 0.17, b, s * 0.8, color="#5A3A22", patch="#3A2214", flip=True))
    for i in range(4):
        x = w * (0.64 + i * 0.09)
        o.append(captive_fig(p, x, b - (i % 2) * 4, s * (0.94 - 0.03 * i), i=i + 1, flip=True))
    o.append(LA.cakes(w * 0.56, b, s * 1.2) + E4.basket(w * 0.47, b, s * 1.1))
    return "".join(o)

def gate_names(p, w, h, seed, sides=("S", "W")):
    """Three gates on every side after the names of the tribes: a stretch of the city wall for each side named, three gate
    towers in it, each with its tribe's banner and name (Simeon, Issachar, Zebulun on the south; Gad, Asher, Naphtali on
    the west)."""
    names = {"N": ["REUBEN", "JUDAH", "LEVI"], "E": ["JOSEPH", "BENJAMIN", "DAN"], "S": ["SIMEON", "ISSACHAR", "ZEBULUN"], "W": ["GAD", "ASHER", "NAPHTALI"]}
    side_nm = {"N": "THE NORTH SIDE", "E": "THE EAST SIDE", "S": "THE SOUTH SIDE", "W": "THE WEST SIDE"}
    o = [mk.defs(p, *ALL), bg(f"gn{seed}", w, h, [(0, "#4A7AB8"), (1, "#F3E4C0")])]
    n = len(sides); cw = w / n
    b = h * 0.9; top = h * 0.5
    for k, sd in enumerate(sides):
        x0 = k * cw
        o.append(f'<rect x="{f(x0 + 4)}" y="{f(top)}" width="{f(cw - 8)}" height="{f(b - top)}" fill="#D8BC8C" stroke="{INK}" stroke-width="2.2"></rect>'
                 + "".join(f'<rect x="{f(x0 + 4 + i * (cw - 8) / 16)}" y="{f(top - 10)}" width="{f((cw - 8) / 32)}" height="10" fill="#D8BC8C" stroke="{INK}" stroke-width="1.4"></rect>' for i in range(16)))
        for i, nm in enumerate(names[sd]):
            gx = x0 + cw * (i + 1) / 4; tw = cw * 0.18; tt = top - h * 0.14
            o.append(f'<rect x="{f(gx - tw / 2)}" y="{f(tt)}" width="{f(tw)}" height="{f(b - tt)}" fill="#E8D0A0" stroke="{INK}" stroke-width="2.2"></rect>'
                     + P(f"M{f(gx - tw * 0.3)} {f(b)} L {f(gx - tw * 0.3)} {f(b - (b - top) * 0.5)} Q {f(gx)} {f(b - (b - top) * 0.72)} {f(gx + tw * 0.3)} {f(b - (b - top) * 0.5)} L {f(gx + tw * 0.3)} {f(b)} Z", "#3A2A1A", 2))
            fx = gx - tw * 0.1; fy = tt - h * 0.18
            o.append(f'<path d="M{f(fx)} {f(tt)} L {f(fx)} {f(fy)}" stroke="#3A2A1A" stroke-width="2.4"></path>'
                     f'<path d="M{f(fx)} {f(fy)} L {f(fx + tw * 0.8)} {f(fy + h * 0.035)} L {f(fx)} {f(fy + h * 0.07)} Z" fill="{TC.get(nm, "#C8202A")}" stroke="{INK}" stroke-width="1.6"></path>')
            o.append(f'<rect x="{f(gx - tw * 0.66)}" y="{f(tt + 6)}" width="{f(tw * 1.32)}" height="15" fill="#F3EFE6" stroke="{INK}" stroke-width="1.2"></rect>' + label(gx, tt + 17, nm, INK, 7.5 if tw > 56 else 6.5, ls=0.06))
    o.append(ground(w, h, b, "#C8B080", dy=0))
    o.append("".join(f'<rect x="{f(k * cw + cw / 2 - 58)}" y="{f(h - 21)}" width="116" height="16" fill="#12113A"></rect>' + label(k * cw + cw / 2, h - 9, side_nm[sd], GOLD_, 8.5) for k, sd in enumerate(sides)))
    return "".join(o)
