"""Drawings for Ezekiel 40–42 (and the plates of 43–46): the house of the vision as blueprint plates on exo.art8's grid
(bp, dim, tag): vision_plan() is the whole — the wall of five hundred, the three outer gates, the pavement and its thirty
chambers, the inner court with its gates and the altar, the house, the separate place and the building toward the west,
the priests' chambers, the kitchens in the corners — with the part in hand lit gold; gate_plan() the east gate with its
lodges; house_plan() the temple, the most holy place, the side-chambers; and the detail plates. The man whose appearance
was like brass (man_brass) is a bronze figure of light with his line of flax and measuring reed, no face drawn."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ezk.art14 import *
from ezk.art14 import f, K2, K3, P, rect, seated, clouds, smoke, house, INK, EZ_C, GB_BEARD, CAPT, bg, glow, vgrad, rgrad, KK2, JJ2, J1
from exo.art8 import bp, dim, tag, title_bar, box, INK as BINK, CY, GOLD as BGOLD, cherub
from exo.art8 import f as ff

LIT, LINE, FILL = "#FFD23F", "#8FD0E2", "#1E3A5A"

def man_brass(p, x, y, s, flip=False, reed=True):
    """The man whose appearance was like the appearance of brass, with a line of flax in his hand and a measuring reed: a
    gleaming bronze figure with a glow, no face detail."""
    o = glow(f"mb{p}{int(x)}{int(y)}", x, y - 100 * s, 90 * s, 140 * s, "#FFC14D", 0.6)
    o += (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'          # a figure of light with a bronze rim, no face
          f'<ellipse cx="0" cy="-100" rx="40" ry="100" fill="#FFE680" opacity="0.3"></ellipse>'
          f'<path d="M-26 0 C -28 -60 -24 -120 -16 -152 C -20 -172 -13 -192 0 -194 C 13 -192 20 -172 16 -152 C 24 -120 28 -60 26 0 Z" '
          f'fill="#FFF4D8" stroke="#C87A2E" stroke-width="3"></path>'
          f'<path d="M-10 -150 C -4 -110 -6 -50 -12 -4 M10 -150 C 4 -110 6 -50 12 -4" stroke="#E8B060" stroke-width="2" fill="none" opacity="0.7"></path></g>')
    sx = -1 if flip else 1
    if reed:
        o += (f'<path d="M{f(x - sx * 46 * s)} {f(y - 250 * s)} L {f(x - sx * 46 * s)} {f(y - 40 * s)}" stroke="#0D0D0F" stroke-width="{f(6 * s)}"></path>'
              f'<path d="M{f(x - sx * 46 * s)} {f(y - 250 * s)} L {f(x - sx * 46 * s)} {f(y - 40 * s)}" stroke="#D8C070" stroke-width="{f(3.6 * s)}"></path>'
              + "".join(f'<path d="M{f(x - sx * 50 * s)} {f(y - (60 + i * 32) * s)} l {f(sx * 8 * s)} 0" stroke="#5A3A1A" stroke-width="1.4"></path>' for i in range(6)))
    o += f'<ellipse cx="{f(x + sx * 24 * s)}" cy="{f(y - 100 * s)}" rx="{f(8 * s)}" ry="{f(12 * s)}" fill="none" stroke="#F3EFE6" stroke-width="{f(2.4 * s)}"></ellipse>'
    return o

def high_mountain(p, w, h, seed):
    """Set me down upon a very high mountain, whereon was as it were the frame of a city on the south: a great height above
    the clouds, the outline of walls and gates on its southern side, Ezekiel on the summit."""
    o = [mk.defs(p, *ALL), bg(f"hm{seed}", w, h, [(0, "#1A2A5A"), (0.6, "#8AA8D0"), (1, "#F3E0C0")])]
    o.append(clouds(w, h * 0.78, seed, n=8, color="#F3EFE6", op=0.85, ry=0.06))
    o.append(P(f"M{f(w * 0.06)} {f(h + 10)} L {f(w * 0.32)} {f(h * 0.3)} L {f(w * 0.44)} {f(h * 0.36)} L {f(w * 0.9)} {f(h + 10)} Z", "#6A6A7A", 2.4))
    o.append(P(f"M{f(w * 0.5)} {f(h * 0.62)} L {f(w * 0.96)} {f(h * 0.62)} L {f(w * 0.96)} {f(h * 0.86)} L {f(w * 0.5)} {f(h * 0.86)} Z", "none", 2))
    for i in range(5):
        x = w * (0.52 + i * 0.1)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.58)}" width="{f(w * 0.04)}" height="{f(h * 0.08)}" fill="none" stroke="#FFE680" stroke-width="2"></rect>')
    o.append(f'<rect x="{f(w * 0.5)}" y="{f(h * 0.62)}" width="{f(w * 0.46)}" height="{f(h * 0.24)}" fill="#FFE680" fill-opacity="0.15" stroke="#FFE680" stroke-width="2.4" stroke-dasharray="8 5"></rect>')
    s = min(h * 0.24 / 200, 0.7)
    o.append(ezek_fig(p, w * 0.33, h * 0.31, s))
    return "".join(o)

def at_gate(p, w, h, seed):
    """And, behold, there was a man, whose appearance was like the appearance of brass, and he stood in the gate: the east gate
    of the outer court, the man of brass standing in it with the reed, Ezekiel before him."""
    o = [mk.defs(p, *ALL), bg(f"ag{seed}", w, h, [(0, "#3A4A7A"), (1, "#E8D8B8")])]
    o.append(S4.gatehouse(w * 0.6, h * 0.92, w * 0.6, h * 0.66))
    o.append(f'<rect x="-10" y="{f(h * 0.92)}" width="{f(w + 20)}" height="{f(h * 0.1)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    s = min(h * 0.52 / 200, 1.0)
    o.append(man_brass(p, w * 0.6, h * 0.95, s))
    o.append(ezek_fig(p, w * 0.18, h * 0.97, s * 0.95))
    return "".join(o)

# ---- the plan of the whole (cubits; x east, y south; the outer square from -250 to 250) ----------------------------------
PARTS = {
    "outer_wall": [(-250, -250, 500, 500)],
    "pavement": [(-245, -245, 490, 45), (-245, 200, 490, 45), (200, -200, 45, 400)],
    "east_gate": [(200, -12.5, 50, 25)], "north_gate": [(-12.5, -250, 25, 50)], "south_gate": [(-12.5, 200, 25, 50)],
    "inner_court": [(-50, -50, 100, 100)],
    "inner_east": [(50, -12.5, 50, 25)], "inner_north": [(-12.5, -100, 25, 50)], "inner_south": [(-12.5, 50, 25, 50)],
    "house": [(-150, -25, 100, 50)], "separate": [(-150, -45, 100, 20), (-150, 25, 100, 20)],
    "building": [(-240, -45, 90, 90)],
    "priests_chambers": [(-150, -100, 100, 50), (-150, 50, 100, 50)],
    "kitchens": [(-245, -245, 40, 30), (205, -245, 40, 30), (-245, 215, 40, 30), (205, 215, 40, 30)],
    "boiling": [(-162, -100, 10, 50), (-162, 50, 10, 50)],
}
_VP = [0]
def vision_plan(w, h, hi=(), title="THE HOUSE OF THE VISION · PLAN", dims=False, altar=True, zoom=None):
    """The house of the vision as a plan, north up and east to the right: the parts named in hi lit gold. In a panel too
    low to show the whole at a readable scale, the plan is drawn closer, framed on the lit parts (zoom=None: when that
    doubles the scale; zoom=False: always the whole)."""
    _VP[0] += 1
    o = [bp(w, h)]
    ax0, ay0, aw, ah = 12, 34, w - 24, h - 44
    u = min(aw, ah) / 560
    cx, cy = ax0 + aw / 2, ay0 + ah / 2
    if hi and zoom is not False:
        rs = [r for n in hi if n in PARTS for r in PARTS[n]] + ([(-8, -8, 16, 16)] if "altar" in hi else [])
        bx0 = min(x for x, y, a, b in rs); by0 = min(y for x, y, a, b in rs)
        bx1 = max(x + a for x, y, a, b in rs); by1 = max(y + b for x, y, a, b in rs)
        pad = max(85, 0.45 * max(bx1 - bx0, by1 - by0))
        bx0, by0, bx1, by1 = bx0 - pad, by0 - pad, bx1 + pad, by1 + pad
        ex = max(0, 280 - (bx1 - bx0)) / 2; ey = max(0, 280 - (by1 - by0)) / 2   # never closer than about half the court
        bx0, bx1, by0, by1 = bx0 - ex, bx1 + ex, by0 - ey, by1 + ey
        uz = min(aw / (bx1 - bx0), ah / (by1 - by0))
        if zoom or uz > 1.8 * u:
            u = min(uz, 2.6)
            mx, my = (bx0 + bx1) / 2, (by0 + by1) / 2
            cx, cy = ax0 + aw / 2 - mx * u, ay0 + ah / 2 - my * u
            title = title.replace("· PLAN", "· DETAIL")
    X = lambda x: cx + x * u; Y = lambda y: cy + y * u
    cid = f"vpc{_VP[0]}"
    o.append(f'<defs><clipPath id="{cid}"><rect x="0" y="28" width="{f(w)}" height="{f(h - 28)}"></rect></clipPath></defs><g clip-path="url(#{cid})">')
    lsz = max(7, min(12, 5 + u * 2.4))
    def rects(name, fill=FILL, line=LINE, sw=1.6, dash=None):
        lit = name in hi
        out = ""
        for x, y, a, b in PARTS[name]:
            if a == 0: continue
            out += (f'<rect x="{f(X(x))}" y="{f(Y(y))}" width="{f(a * u)}" height="{f(b * u)}" fill="{("#5A4A1A" if lit else fill)}" fill-opacity="{0.9 if lit else 0.7}" '
                    f'stroke="{LIT if lit else line}" stroke-width="{2.4 if lit else sw}"' + (f' stroke-dasharray="{dash}"' if dash else "") + '></rect>')
        return out
    o.append(rects("outer_wall", fill="#12243A", sw=2.4))
    o.append(rects("pavement", fill="#203A54", sw=1))
    if "pavement" in hi or not hi:
        for i in range(10):
            for (x0, y0, dx, dy) in ((-230 + i * 46, -243, 0, 0), (-230 + i * 46, 231, 0, 0)):
                o.append(f'<rect x="{f(X(x0))}" y="{f(Y(y0))}" width="{f(30 * u)}" height="{f(12 * u)}" fill="none" stroke="{LIT if "pavement" in hi else "#4A7A9A"}" stroke-width="1"></rect>')
        for i in range(10):
            o.append(f'<rect x="{f(X(231))}" y="{f(Y(-180 + i * 36))}" width="{f(12 * u)}" height="{f(26 * u)}" fill="none" stroke="{LIT if "pavement" in hi else "#4A7A9A"}" stroke-width="1"></rect>')
    o.append(rects("kitchens", fill="#203A54", sw=1, dash="3 3"))
    for g in ("east_gate", "north_gate", "south_gate", "inner_east", "inner_north", "inner_south"): o.append(rects(g, fill="#2A4A6A", sw=1.8))
    o.append(rects("inner_court", fill="#1A3450", sw=2))
    o.append(rects("priests_chambers", fill="#24405C"))
    o.append(rects("separate", fill="#16304A", sw=1, dash="4 3"))
    o.append(rects("building", fill="#2A4A6A"))
    o.append(rects("house", fill="#3A5A7A", sw=2))
    o.append(rects("boiling", fill="#24405C", sw=1))
    hx = lambda x: X(x)
    o.append(f'<path d="M{f(X(-61))} {f(Y(-25))} L {f(X(-61))} {f(Y(25))} M{f(X(-81))} {f(Y(-25))} L {f(X(-81))} {f(Y(25))}" stroke="{LINE}" stroke-width="1"></path>')
    if altar:
        a_lit = "altar" in hi
        o.append(f'<rect x="{f(X(-8))}" y="{f(Y(-8))}" width="{f(16 * u)}" height="{f(16 * u)}" fill="{"#E8B830" if a_lit else "#8A6A3A"}" stroke="{LIT if a_lit else LINE}" stroke-width="2"></rect>')
    names = [("EAST GATE", 225, 36, "east_gate"), ("NORTH GATE", 0, -192, "north_gate"), ("SOUTH GATE", 0, 196, "south_gate"), ("INNER COURT", 0, 44, "inner_court"),
             ("HOUSE", -100, 4, "house"), ("BUILDING", -195, 4, "building"), ("ALTAR", 0, -12, "altar")]
    if u > 1.2:
        names += [("PAVEMENT", -120, -222, "pavement"), ("CHAMBERS", -100, -72, "priests_chambers"), ("CHAMBERS", -100, 78, "priests_chambers"),
                  ("INNER GATE", 75, -16, "inner_east"), ("INNER GATE", 0, -104, "inner_north"), ("INNER GATE", 0, 108, "inner_south"),
                  ("SEPARATE PLACE", -100, -32, "separate"), ("SEPARATE PLACE", -100, 40, "separate")]
    for nm, x, y, part in names:
        o.append(label(X(x), Y(y), nm, LIT if part in hi else "#6A9ABA", lsz))
    if dims:
        o.append(dim(X(-250), Y(-262), X(250), Y(-262), "500 REEDS", size=9) + dim(X(262), Y(-250), X(262), Y(250), "500", size=9))
    o.append('</g>' + title_bar(w, title) + label(w - 16, 19, "N ↑", CY, 11, "end"))
    return "".join(o)

def gate_plan(w, h, outer=True):
    """A gate of the court as a plan: the steps, the thresholds of a reed, three lodges on this side and three on that, each a
    reed square, five cubits between, the posts, the porch of eight cubits, the length fifty and the breadth five and twenty;
    closed windows, and palm-trees upon the posts."""
    o = [bp(w, h), title_bar(w, ("THE GATE WHICH LOOKETH TOWARD THE EAST" if outer else "A GATE OF THE INNER COURT") + " · PLAN")]
    u = min(w * 0.72 / 62, (h - 110) / 25)                 # room above for the callouts and below for the dimension and steps
    x0 = w * 0.5 - 25 * u; y0 = 34 + (h - 34 - 25 * u) * 0.5 - 6
    X = lambda x: x0 + x * u; Y = lambda y: y0 + y * u
    o.append(f'<rect x="{f(X(0))}" y="{f(Y(0))}" width="{f(50 * u)}" height="{f(25 * u)}" fill="{FILL}" stroke="{LINE}" stroke-width="2"></rect>')
    o.append(f'<rect x="{f(X(0))}" y="{f(Y(7.5))}" width="{f(50 * u)}" height="{f(10 * u)}" fill="#0F1E2E" stroke="{LINE}" stroke-width="1.4"></rect>')
    for i in range(3):
        lx = 6 + i * 11
        for ly in (1.5, 17.5):
            o.append(f'<rect x="{f(X(lx))}" y="{f(Y(ly))}" width="{f(6 * u)}" height="{f(6 * u)}" fill="#2A4A6A" stroke="{LIT}" stroke-width="1.6"></rect>')
        if i < 2:
            for ly in (1.5, 17.5):
                o.append(f'<path d="M{f(X(lx + 7))} {f(Y(ly + 1))} L {f(X(lx + 10))} {f(Y(ly + 5))}" stroke="#4A7A9A" stroke-width="1"></path>')
    o.append(f'<rect x="{f(X(42))}" y="{f(Y(0))}" width="{f(8 * u)}" height="{f(25 * u)}" fill="#2A4A6A" stroke="{LINE}" stroke-width="1.6"></rect>')
    for py in (0, 23):
        o.append(f'<rect x="{f(X(48))}" y="{f(Y(py))}" width="{f(2 * u)}" height="{f(2 * u)}" fill="{BGOLD}"></rect>')
        o.append(f'<path d="M{f(X(49))} {f(Y(py + 1))} l 0 -10 m -4 4 l 4 -4 l 4 4" stroke="#5ECB5E" stroke-width="1.6" fill="none"></path>')
    for i in range(7 if outer else 8):
        o.append(f'<path d="M{f(X(-1.5 - i * 1.2))} {f(Y(7.5))} L {f(X(-1.5 - i * 1.2))} {f(Y(17.5))}" stroke="{LINE}" stroke-width="1.2"></path>')
    o.append(dim(X(0), Y(28), X(50), Y(28), "FIFTY CUBITS", size=8))
    o.append(dim(X(53), Y(0), X(53), Y(25), "25", size=8))
    ty = max(44, Y(0) - 16); by = min(h - 10, Y(25) + 40)
    o.append(tag(X(9), Y(4.5), "LODGES · ONE REED", X(2), ty))
    o.append(tag(X(46), Y(12.5), "PORCH · 8 CUBITS", X(40), ty))
    o.append(tag(X(-4), Y(12.5), f"{'SEVEN' if outer else 'EIGHT'} STEPS", X(-6), by))
    o.append(tag(X(25), Y(12.5), "OPENING · 10 CUBITS", X(30), by))
    return "".join(o)

def reed_plate(w, h):
    """In the man's hand a measuring reed six cubits long, of a cubit and a handbreadth each; the wall one reed thick and one
    reed high."""
    o = [bp(w, h), title_bar(w, "THE MEASURING REED · SIX CUBITS OF A CUBIT AND A HANDBREADTH")]
    u = w * 0.8 / 6
    x0, y = w * 0.1, h * 0.36
    o.append(f'<rect x="{f(x0)}" y="{f(y - 8)}" width="{f(6 * u)}" height="16" rx="6" fill="#D8C070" stroke="#0D0D0F" stroke-width="2"></rect>')
    for i in range(7):
        o.append(f'<path d="M{f(x0 + i * u)} {f(y - 14)} L {f(x0 + i * u)} {f(y + 14)}" stroke="{CY}" stroke-width="1.6"></path>')
        if i < 6: o.append(label(x0 + (i + 0.5) * u, y + 30, f"{i + 1}", CY, 9))
    o.append(f'<path d="M{f(x0 + 5 * u)} {f(y + 40)} L {f(x0 + 5.86 * u)} {f(y + 40)} L {f(x0 + 5.86 * u)} {f(y + 46)}" stroke="{LIT}" stroke-width="1.6" fill="none"></path>'
             + label(x0 + 5.43 * u, y + 60, "A CUBIT", LIT, 8) + f'<path d="M{f(x0 + 5.86 * u)} {f(y + 40)} L {f(x0 + 6 * u)} {f(y + 40)}" stroke="#FF8A6A" stroke-width="3"></path>'
             + label(x0 + 6 * u, y + 74, "+ A HANDBREADTH", "#FF8A6A", 8, "end"))
    s = min(h * 0.3, w * 0.2)
    wx, wy = w * 0.5 - s / 2, h * 0.92 - s
    o.append(f'<rect x="{f(wx)}" y="{f(wy)}" width="{f(s)}" height="{f(s)}" fill="#3A5A7A" stroke="{LINE}" stroke-width="2"></rect>'
             + "".join(f'<path d="M{f(wx)} {f(wy + k * s / 4)} L {f(wx + s)} {f(wy + k * s / 4)}" stroke="#4A7A9A" stroke-width="1"></path>' for k in range(1, 4)))
    o.append(dim(wx, wy - 10, wx + s, wy - 10, "ONE REED", size=8) + dim(wx + s + 12, wy, wx + s + 12, wy + s, "ONE REED", size=8))
    o.append(label(wx - 12, wy + s / 2, "THE WALL", CY, 9, "end"))
    return "".join(o)

def tables_plate(w, h):
    """At the north gate eight tables whereupon they slew the sacrifices, four on this side and four on that side; four tables
    for the burnt-offering of hewn stone, a cubit and a half long, a cubit and a half broad, one cubit high; hooks a
    handbreadth long fastened within round about."""
    o = [bp(w, h), title_bar(w, "THE TABLES BY THE GATE · OF HEWN STONE")]
    gx, gy, gw, gh = w * 0.08, h * 0.3, w * 0.36, h * 0.5
    o.append(f'<rect x="{f(gx)}" y="{f(gy)}" width="{f(gw)}" height="{f(gh)}" fill="{FILL}" stroke="{LINE}" stroke-width="1.6"></rect>' + label(gx + gw / 2, gy + gh / 2, "THE PORCH OF THE GATE", "#4A7A9A", 8))
    for i in range(4):
        for side in (0, 1):
            x = gx + (gw * 0.1 if side == 0 else gw * 0.72) ; y = gy + gh * (0.08 + i * 0.23)
            o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(gw * 0.18)}" height="{f(gh * 0.14)}" fill="#8A7A6A" stroke="{LIT}" stroke-width="1.6"></rect>')
    o.append(label(gx + gw / 2, gy + gh + 22, "EIGHT TABLES", LIT, 9))
    bx, by = w * 0.66, h * 0.82; k = min(w * 0.12, h * 0.22)
    o.append(box(bx, by, k * 1.5, k * 1.5, k, fill="#9A8A7A"))
    for i in range(4): o.append(f'<path d="M{f(bx + k * 0.2 + i * k * 0.36)} {f(by - k)} l 0 {f(-k * 0.16)} q 0 -6 6 -6" stroke="#C8C8D0" stroke-width="2" fill="none"></path>')
    o.append(dim(bx, by + 14, bx + k * 1.5, by + 14, "1½ CUBITS", size=8) + dim(bx - 14, by, bx - 14, by - k, "1", size=8))
    o.append(tag(bx + k * 0.9, by - k * 1.1, "HOOKS · A HANDBREADTH", w * 0.6, h * 0.2))
    return "".join(o)

def porch_plan(w, h):
    """The porch of the house: each post of the porch five cubits on this side and five on that, the breadth of the gate three
    cubits on this side and three on that; the length twenty cubits and the breadth eleven, the steps, and the pillars by the
    posts."""
    o = [bp(w, h), title_bar(w, "THE PORCH OF THE HOUSE")]
    u = min(w * 0.6 / 20, (h - 92) / 20)                  # the porch, the posts, the pillars and the steps: 20 cubits deep
    x0, y0 = w * 0.5 - 10 * u, 52 + (h - 92 - 20 * u) / 2
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(20 * u)}" height="{f(11 * u)}" fill="{FILL}" stroke="{LINE}" stroke-width="2"></rect>')
    for px in (0, 15):
        o.append(f'<rect x="{f(x0 + px * u)}" y="{f(y0 + 11 * u)}" width="{f(5 * u)}" height="{f(2 * u)}" fill="#3A5A7A" stroke="{LIT}" stroke-width="1.6"></rect>')
    for px in (4, 16):
        o.append(f'<circle cx="{f(x0 + px * u)}" cy="{f(y0 + 14.5 * u)}" r="{f(1.2 * u)}" fill="{BGOLD}" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    for i in range(4): o.append(f'<path d="M{f(x0 + 6 * u)} {f(y0 + (16.5 + i * 0.8) * u)} L {f(x0 + 14 * u)} {f(y0 + (16.5 + i * 0.8) * u)}" stroke="{LINE}" stroke-width="1.2"></path>')
    o.append(dim(x0, y0 - 12, x0 + 20 * u, y0 - 12, "TWENTY CUBITS", size=8) + dim(x0 - 14, y0, x0 - 14, y0 + 11 * u, "ELEVEN", size=8))
    o.append(tag(x0 + 2.5 * u, y0 + 12 * u, "POST · 5 CUBITS", x0 - 30, y0 + 16 * u) + tag(x0 + 16 * u, y0 + 14.5 * u, "PILLARS BY THE POSTS", x0 + 24 * u, y0 + 17 * u)
             + tag(x0 + 10 * u, y0 + 17.7 * u, "THE STEPS", x0 + 24 * u, y0 + 20 * u))
    return "".join(o)

def house_plan(w, h, hi=()):
    """The house as a plan: the posts six cubits, the entrance ten; the temple forty by twenty; the most holy place twenty by
    twenty; the wall of the house six cubits; the side-chambers four cubits round about, three stories, thirty in order; the
    place that was left five cubits; the separate place twenty; hi: "temple", "holy", "chambers"."""
    o = [bp(w, h), title_bar(w, "THE HOUSE · A HUNDRED CUBITS LONG")]
    u = min(w * 0.86 / 100, h * 0.56 / 50)
    x0, y0 = w * 0.5 - 50 * u, h * 0.52 - 25 * u
    X = lambda x: x0 + x * u; Y = lambda y: y0 + y * u
    o.append(f'<rect x="{f(X(0))}" y="{f(Y(0))}" width="{f(100 * u)}" height="{f(50 * u)}" fill="none" stroke="#4A7A9A" stroke-width="1.4" stroke-dasharray="5 4"></rect>')
    ch = "chambers" in hi
    o.append(f'<rect x="{f(X(15))}" y="{f(Y(5))}" width="{f(80 * u)}" height="{f(40 * u)}" fill="{"#5A4A1A" if ch else FILL}" stroke="{LIT if ch else LINE}" stroke-width="2"></rect>')
    for i in range(10):
        x = 17 + i * 7.8
        for yy in (6, 39):
            o.append(f'<rect x="{f(X(x))}" y="{f(Y(yy))}" width="{f(6.6 * u)}" height="{f(4 * u)}" fill="none" stroke="{LIT if ch else "#4A7A9A"}" stroke-width="1"></rect>')
    o.append(f'<rect x="{f(X(21))}" y="{f(Y(11))}" width="{f(68 * u)}" height="{f(28 * u)}" fill="#24405C" stroke="{LINE}" stroke-width="2.4"></rect>')
    t = "temple" in hi; hl = "holy" in hi
    o.append(f'<rect x="{f(X(27))}" y="{f(Y(15))}" width="{f(40 * u)}" height="{f(20 * u)}" fill="{"#5A4A1A" if t else "#16304A"}" stroke="{LIT if t else LINE}" stroke-width="2"></rect>' + label(X(47), Y(26), "THE TEMPLE · 40 × 20", LIT if t else CY, 9))
    o.append(f'<rect x="{f(X(67))}" y="{f(Y(15))}" width="{f(20 * u)}" height="{f(20 * u)}" fill="{BGOLD if hl else "#16304A"}" stroke="{LIT if hl else LINE}" stroke-width="2.4"></rect>'
             + label(X(77), Y(24), "MOST HOLY", INK if hl else CY, 8) + label(X(77), Y(29), "20 × 20", INK if hl else CY, 8))
    o.append(f'<rect x="{f(X(4))}" y="{f(Y(14))}" width="{f(11 * u)}" height="{f(22 * u)}" fill="#2A4A6A" stroke="{LINE}" stroke-width="1.6"></rect>' + label(X(9.5), Y(26), "PORCH", CY, 7))
    o.append(dim(X(0), Y(53), X(100), Y(53), "A HUNDRED CUBITS", size=8))
    ty = max(36, Y(-5))
    o.append(tag(X(21), Y(30), "POSTS · 6 CUBITS", X(2), Y(58) if Y(58) < h - 8 else h - 10) + tag(X(50), Y(8), "SIDE-CHAMBERS · 4 · THREE STORIES · THIRTY", X(56), ty))
    return "".join(o)

def chambers_elev(w, h):
    """The side-chambers in three stories, broader as they went up, the house's wall stepping in; or the priests' chambers
    in three stories with their galleries, the upper chambers shorter: an elevation."""
    o = [bp(w, h), title_bar(w, "THREE STORIES · ONE OVER ANOTHER")]
    u = min(w * 0.7 / 40, h * 0.7 / 22)
    x0, base = w * 0.5 - 20 * u, h * 0.9
    for k in range(3):
        wd = 40 - k * 4; x = x0 + k * 2 * u
        o.append(box(x, base - k * 6 * u, wd * u, 6 * u, 6 * u, fill=["#3A5A7A", "#4A6A8A", "#5A7A9A"][k], line=LINE, k=0.4))
        o.append(label(x + wd * u / 2, base - k * 6 * u - 3 * u, ["LOWEST", "MIDDLEMOST", "UPPERMOST"][k], CY, 8))
    o.append(dim(x0 - 14, base, x0 - 14, base - 18 * u, "THREE STORIES", size=8))
    o.append(tag(x0 + 36 * u, base - 15 * u, "GALLERIES · THE UPPER SHORTER", w * 0.66, h * 0.2))
    return "".join(o)

def carvings(w, h):
    """Cherubim and palm-trees from the ground unto above the door: a palm-tree between cherub and cherub, and every cherub
    with two faces — the face of a man toward the palm-tree on the one side, the face of a young lion toward the palm-tree on
    the other — a frieze."""
    o = [bp(w, h), title_bar(w, "CHERUBIM AND PALM-TREES · THUS WAS THE WALL OF THE TEMPLE")]
    k = min(1.0, h / 220)
    n = 4; step = w / n
    for i in range(n):
        x = step * (i + 0.5); base = h * 0.86
        o.append(cherub(x - 30 * k, base, k * 0.9) + cherub(x + 30 * k, base, k * 0.9, flip=True) if False else cherub(x, base, k * 0.9, flip=i % 2 == 1))
        px = x + step / 2
        if i < n - 1:
            o.append(f'<path d="M{f(px)} {f(base)} L {f(px)} {f(base - 110 * k)}" stroke="#B8863E" stroke-width="{f(6 * k)}"></path>'
                     + "".join(f'<path d="M{f(px)} {f(base - 110 * k)} q {f(math.cos(a) * 30 * k)} {f(-14 * k)} {f(math.cos(a) * 46 * k)} {f(math.sin(a) * 30 * k)}" stroke="#5ECB5E" stroke-width="{f(4 * k)}" fill="none"></path>' for a in (0.3, 1.2, 2.0, 2.9, -0.4)))
    o.append(label(w * 0.5, h * 0.96, "A FACE OF A MAN TOWARD THE PALM-TREE · A FACE OF A YOUNG LION TOWARD THE OTHER", CY, 8))
    return "".join(o)

def wood_altar(w, h):
    """The altar was of wood, three cubits high, and the length thereof two cubits; and the corners thereof, and the length
    thereof, and the walls thereof, were of wood: the table that is before Jehovah."""
    o = [bp(w, h), title_bar(w, "THE TABLE THAT IS BEFORE JEHOVAH · OF WOOD")]
    u = min(w * 0.3 / 2, h * 0.6 / 3)
    x0, base = w * 0.5 - u, h * 0.86
    o.append(box(x0, base, 2 * u, 2 * u, 3 * u, fill="#A8743A", line="#0D0D0F", k=0.4))
    o.append(dim(x0, base + 14, x0 + 2 * u, base + 14, "TWO CUBITS", size=8) + dim(x0 - 16, base, x0 - 16, base - 3 * u, "THREE CUBITS", size=8))
    return "".join(o)

def doors_elev(w, h):
    """The temple and the sanctuary had two doors, and the doors had two leaves apiece, two turning leaves, with cherubim and
    palm-trees upon them: an elevation."""
    o = [bp(w, h), title_bar(w, "TWO DOORS · TWO TURNING LEAVES APIECE")]
    k = min(w * 0.18, h * 0.6)
    for d in range(2):
        cx = w * (0.28 + d * 0.44); top = h * 0.24
        for s in (-1, 1):
            x = cx + (0 if s > 0 else -k * 0.5)
            o.append(f'<rect x="{f(x)}" y="{f(top)}" width="{f(k * 0.5)}" height="{f(k * 1.1)}" fill="#8A6A3A" stroke="{LINE}" stroke-width="2"></rect>'
                     f'<path d="M{f(x + k * 0.25)} {f(top)} L {f(x + k * 0.25)} {f(top + k * 1.1)}" stroke="#5A3A1A" stroke-width="1.2"></path>')
            o.append(cherub(x + k * 0.25, top + k * 0.5, k / 300, flip=s < 0))
            o.append(f'<path d="M{f(x + k * 0.25)} {f(top + k * 1.05)} L {f(x + k * 0.25)} {f(top + k * 0.7)}" stroke="#5ECB5E" stroke-width="3"></path>')
        o.append(label(cx, top + k * 1.1 + 18, ["THE TEMPLE", "THE SANCTUARY"][d], CY, 9))
    return "".join(o)

def gate_elev(w, h):
    """The gate seen from without, an elevation: the posts threescore cubits with palm-trees upon them, the closed windows
    to the lodges and the posts round about, the arches, and seven steps going up to it."""
    o = [bp(w, h), title_bar(w, "THE GATE · POSTS, WINDOWS AND PALM-TREES")]
    base = h - 26; top = 52
    k = min((base - top) / 60, w * 0.6 / 60)
    cx = w * 0.5
    X = lambda x: cx + x * k; Y = lambda y: base - y * k
    o.append(f'<rect x="{f(X(-25))}" y="{f(Y(52))}" width="{f(50 * k)}" height="{f(48 * k)}" fill="{FILL}" stroke="{LINE}" stroke-width="2"></rect>')
    for px in (-25, 17):                                  # the posts, threescore cubits, with palm-trees upon them
        o.append(f'<rect x="{f(X(px))}" y="{f(Y(60))}" width="{f(8 * k)}" height="{f(56 * k)}" fill="#2A4A6A" stroke="{LIT}" stroke-width="1.8"></rect>')
        pxc = X(px + 4)
        o.append(f'<path d="M{f(pxc)} {f(Y(10))} L {f(pxc)} {f(Y(40))}" stroke="#B8863E" stroke-width="{f(1.2 * k)}"></path>'
                 + "".join(f'<path d="M{f(pxc)} {f(Y(40))} q {f(math.cos(a) * 4 * k)} {f(-2 * k)} {f(math.cos(a) * 7 * k)} {f(math.sin(a) * 4 * k)}" stroke="#5ECB5E" stroke-width="{f(0.8 * k)}" fill="none"></path>' for a in (0.3, 1.2, 2.0, 2.9, -0.4)))
    o.append(f'<path d="M{f(X(-6))} {f(Y(4))} L {f(X(-6))} {f(Y(30))} Q {f(X(0))} {f(Y(40))} {f(X(6))} {f(Y(30))} L {f(X(6))} {f(Y(4))} Z" fill="#0F1E2E" stroke="{LINE}" stroke-width="2"></path>')
    for i in range(3):                                     # closed windows, three on this side and three on that
        for sx in (-1, 1):
            wx = X(sx * 11.5) - 1.2 * k
            o.append(f'<rect x="{f(wx)}" y="{f(Y(46 - i * 13))}" width="{f(2.4 * k)}" height="{f(6 * k)}" fill="#0B1A2E" stroke="{LINE}" stroke-width="1.2"></rect>'
                     f'<path d="M{f(wx)} {f(Y(43 - i * 13))} l {f(2.4 * k)} 0" stroke="{LINE}" stroke-width="1"></path>')
    for i in range(7):                                     # seven steps
        o.append(f'<rect x="{f(X(-9 - i * 1.2))}" y="{f(Y(4 - i * 0.57))}" width="{f((18 + i * 2.4) * k)}" height="{f(0.57 * k)}" fill="#3A5A7A" stroke="{LINE}" stroke-width="0.8"></rect>')
    o.append(dim(X(-31), Y(0), X(-31), Y(60), "THREESCORE CUBITS", size=8))
    o.append(tag(X(-21), Y(30), "PALM-TREES UPON THE POSTS", X(-34), Y(50)) + tag(X(12.7), Y(40), "CLOSED WINDOWS", X(32), Y(50)) + tag(X(6), Y(2), "SEVEN STEPS", X(32), Y(8)))
    return "".join(o)

def round_wall(p, w, h, seed):
    """He measured it round about: the outer wall seen from without at evening, the gate toward the east, the man of light
    walking beside the wall with his reed, Ezekiel following."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), bg(f"rw{seed}", w, h, [(0, "#2A3A6A"), (0.65, "#E8A878"), (1, "#F3D8B0")])]
    o.append(hills(w, h, h * 0.42, seed, "#7A6A7A", amp=8, step=110))
    top = h * 0.44
    o.append(f'<rect x="-10" y="{f(top)}" width="{f(w + 20)}" height="{f(b - top)}" fill="#C8B490" stroke="{INK}" stroke-width="2.4"></rect>'
             + "".join(f'<path d="M-10 {f(top + k * (b - top) / 6)} L {f(w + 10)} {f(top + k * (b - top) / 6)}" stroke="#A8946E" stroke-width="1.2"></path>' for k in range(1, 6))
             + "".join(f'<rect x="{f(i * w / 14)}" y="{f(top - 12)}" width="{f(w / 28)}" height="12" fill="#C8B490" stroke="{INK}" stroke-width="1.6"></rect>' for i in range(15)))
    o.append(S4.gatehouse(w * 0.2, b, w * 0.24, (b - top) * 1.25))
    o.append(ground(w, h, b, "#B8A47E", dy=0))
    s = min(fit(h * 0.99, h * 0.36), 0.9)
    o.append(f'<path d="M{f(w * 0.36)} {f(h * 0.97)} L {f(w * 0.98)} {f(h * 0.97)}" stroke="#FFD23F" stroke-width="2" stroke-dasharray="7 5" opacity="0.85"></path>')
    o.append(man_brass(p, w * 0.58, h * 0.99, s))
    o.append(ezek_fig(p, w * 0.86, h * 0.99, s * 0.92, flip=True))
    return "".join(o)
