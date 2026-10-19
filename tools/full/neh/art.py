"""Drawings for the Nehemiah volume (chapter by chapter, added below), on top of 2 Chronicles' (chr2.art, which carries
chr1.art, kg2.art, kg1.art, and 2 Samuel's drawings as K2).

Nehemiah at a distance: a deep slate-blue robe and headcloth with a gold cord, black beard (neh_fig). Artaxerxes: purple
with the gold crown (persian_king). Shushan the palace: glazed blue brick, white-green-blue hangings and tall columns with
double-bull capitals (palace). Jerusalem's stone is pale limestone (STONE). The wall and its gates as a plan: wall_plan(),
north at the left."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from chr2.art import *
from chr2.art import f, K2, K3
import kg1.art as K1
from sa2.art import king_fig
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import man, woman, grid_bg, node, route, label, sun
import joshua1 as J, numbers1 as N, exodus as E, exodus3 as E3, exodus4 as E4, samuel3 as S3
from jos.art import crowd_at, warrior, WAR
from exo import art as A
from num.art import ALL

NEH_C, ART_C, STONE, STONE_D, CHAR = "#2A3A5A", "#5A1A6A", "#C8B08A", "#A8906A", "#2A1A14"
GOLD, CYAN, RED_C = "#FFD23F", "#8FD0E2", "#D7261E"

def neh_fig(p, x, y, s, flip=False, up=None, cloth=NEH_C):
    """Nehemiah at a distance: slate-blue robe and headcloth with a gold cord, black beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, kind="Robe", sw=3, flip=flip, up=up,
                     extra=A.headcloth(cloth, cord="#E8B830") + A.BLACK_BEARD)

def persian_king(p, x, y, s, flip=False, up=None):
    return king_fig(p, x, y, s, flip=flip, up=up, cloth=ART_C)

def jew(p, x, y, s, cloth, flip=False, up=None, beard=True):
    """A man of Judah at a distance: robe and headcloth of one colour, black beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, kind="Robe", sw=3, flip=flip, up=up,
                     extra=A.headcloth(cloth) + (A.BLACK_BEARD if beard else ""))

def horseman(p, x, y, s, cloth="#6A2A1A", flip=False, color="#3A2214", spear=True):
    """A horseman of the king's army: the rider set on the horse as numbers1.mount sets him on an ass."""
    sx = -1 if flip else 1
    rider = mk.person(p, round(x + sx * (-14) * s), round(y - 40 * s), round(s * 0.62, 3), body=SKIN, cloth=cloth, kind="Tunic", sw=3, flip=flip,
                      extra=A.headcloth(cloth) + (E4.SPEAR if spear else ""))
    return rider + E3.horse(x, y, s, color=color, flip=flip)

# ---- Nehemiah 1–2 -------------------------------------------------------------------------------------------------------
def column(x, base, top, wd):
    """A Persian column: a fluted shaft on a bell base, crowned with a double-bull capital."""
    cap = wd * 0.9
    o = [f'<path d="M{f(x - wd)} {f(base)} C {f(x - wd)} {f(base - wd * 0.8)} {f(x - wd * 0.5)} {f(base - wd * 0.9)} {f(x - wd * 0.5)} {f(base - wd)} '
         f'L {f(x + wd * 0.5)} {f(base - wd)} C {f(x + wd * 0.5)} {f(base - wd * 0.9)} {f(x + wd)} {f(base - wd * 0.8)} {f(x + wd)} {f(base)} Z" fill="#D8CCB0" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<rect x="{f(x - wd / 2)}" y="{f(top + cap)}" width="{f(wd)}" height="{f(base - wd - top - cap)}" fill="#E8DCC0" stroke="#0D0D0F" stroke-width="2"></rect>']
    for k in (-0.25, 0, 0.25):
        o.append(f'<path d="M{f(x + wd * k)} {f(top + cap + 4)} L {f(x + wd * k)} {f(base - wd - 4)}" stroke="#B8AC90" stroke-width="1.6"></path>')
    for sgn in (-1, 1):                                   # two bull fore-parts back to back
        bx = x + sgn * wd * 1.1
        o.append(f'<path d="M{f(x)} {f(top + cap)} L {f(x)} {f(top + cap * 0.2)} L {f(bx)} {f(top + cap * 0.1)} '
                 f'C {f(bx + sgn * wd * 0.5)} {f(top + cap * 0.2)} {f(bx + sgn * wd * 0.5)} {f(top + cap * 0.7)} {f(bx)} {f(top + cap * 0.8)} Z" fill="#C8A060" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<path d="M{f(bx)} {f(top + cap * 0.15)} C {f(bx + sgn * wd * 0.2)} {f(top - cap * 0.3)} {f(bx + sgn * wd * 0.5)} {f(top - cap * 0.2)} {f(bx + sgn * wd * 0.6)} {f(top - cap * 0.1)}" fill="none" stroke="#0D0D0F" stroke-width="2.4"></path>'
                 f'<circle cx="{f(bx + sgn * wd * 0.15)}" cy="{f(top + cap * 0.35)}" r="{f(max(1.4, wd * 0.07))}" fill="#0D0D0F"></circle>'
                 f'<path d="M{f(bx - sgn * wd * 0.1)} {f(top + cap * 0.8)} L {f(bx - sgn * wd * 0.1)} {f(top + cap * 1.25)}" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(f'<rect x="{f(x - wd * 1.8)}" y="{f(top - 4)}" width="{f(wd * 3.6)}" height="{f(cap * 0.14 + 4)}" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    return "".join(o)

def palace(w, h, seed, floor=0.86, cols=4):
    """Shushan the palace: a wall of glazed blue brick with a frieze, white, green and blue hangings, tall columns."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1F4F8D"></rect>']
    for yy in range(0, int(h * floor), 14):
        o.append(f'<path d="M-10 {yy} L {f(w + 10)} {yy}" stroke="#17406F" stroke-width="1.2"></path>')
    fy = h * 0.5
    o.append(f'<rect x="-10" y="{f(fy)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    for k in range(int(w // 24) + 2):
        o.append(f'<circle cx="{f(k * 24 + 6)}" cy="{f(fy + h * 0.03)}" r="{f(min(5, h * 0.018))}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1"></circle>')
    for k, c in enumerate(("#F3EFE6", "#2E6B3A", "#8FD0E2")):          # hangings looped between the columns
        y0 = h * (0.06 + k * 0.03)
        o.append(f'<path d="M-10 {f(y0)} ' + " ".join(f'Q {f((i + 0.5) * w / cols)} {f(y0 + h * 0.1)} {f((i + 1) * w / cols)} {f(y0)}' for i in range(cols)) + f'" fill="none" stroke="{c}" stroke-width="{f(max(4, h * 0.02))}"></path>')
    o.append(f'<rect x="-10" y="{f(h * floor)}" width="{f(w + 20)}" height="{f(h * (1 - floor) + 10)}" fill="#D8CCB0" stroke="#0D0D0F" stroke-width="2"></rect>')
    for k in range(int(w // 40) + 2):
        o.append(f'<path d="M{f(k * 40)} {f(h * floor)} L {f(k * 40 - 30)} {f(h + 10)}" stroke="#B8AC90" stroke-width="1.4"></path>')
    wd = min(w * 0.04, h * 0.05)
    for i in range(cols):
        o.append(column(w * (i + 0.5) / cols, h * floor, h * 0.04, wd))
    return "".join(o)

def shushan(p, w, h, seed, men=True):
    """In Shushan the palace: Nehemiah in the colonnade, Hanani and certain men out of Judah come to him, dusty from the road."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), palace(w, h, seed, floor=0.84, cols=5)]
    s = fit(b, max(h * 0.36, b - 240))
    o.append(neh_fig(p, w * 0.3, b, s))
    if men:
        for i, c in enumerate(("#4A5A3A", "#6A5A4A", "#5A4A3A", "#7A6A5A")):
            o.append(jew(p, w * (0.42 + i * 0.08), b - (i % 2) * 4, s * (0.98 - i * 0.03), c, flip=True))
    return "".join(o)

def rubble(x0, x1, base, h, seed, color=STONE):
    """A wall long fallen: broken stumps and tumbled blocks, grass between, no dust."""
    r = random.Random(seed); o = []
    pts = [(x0, base)]; x = x0
    while x < x1:
        x += r.uniform(18, 46); pts.append((min(x, x1), base - r.uniform(h * 0.05, h * 0.3)))
    pts.append((x1, base))
    o.append('<path d="M' + " L ".join(f"{f(px)} {f(py)}" for px, py in pts) + f' Z" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></path>')
    for _ in range(int((x1 - x0) / 9)):
        cx, cy = r.uniform(x0, x1), base - r.uniform(0, h * 0.24); w, hh = r.uniform(12, 30), r.uniform(8, 16); a = r.uniform(-30, 30)
        o.append(f'<rect x="{f(-w / 2)}" y="{f(-hh / 2)}" width="{f(w)}" height="{f(hh)}" fill="{r.choice([color, STONE_D, "#D8C8A0"])}" stroke="#0D0D0F" stroke-width="1.8" transform="translate({f(cx)} {f(cy)}) rotate({f(a)})"></rect>')
    for _ in range(int((x1 - x0) / 30)):
        gx = r.uniform(x0, x1)
        o.append(f'<path d="M{f(gx)} {f(base)} l -4 -10 M{f(gx)} {f(base)} l 0 -12 M{f(gx)} {f(base)} l 4 -10" stroke="#5A7A3A" stroke-width="1.8"></path>')
    return "".join(o)

def burnt_gate(x, base, wd, ht, seed, embers=True):
    """A gate consumed with fire: the two tower stumps, the empty gateway, the door leaves fallen charred across it."""
    r = random.Random(seed)
    o = []
    for sgn in (-1, 1):
        tx = x + sgn * wd * 0.36
        o.append(f'<path d="M{f(tx - wd * 0.16)} {f(base)} L {f(tx - wd * 0.16)} {f(base - ht * 0.8)} L {f(tx - wd * 0.06)} {f(base - ht * 0.9)} L {f(tx + wd * 0.04)} {f(base - ht * 0.7)} '
                 f'L {f(tx + wd * 0.16)} {f(base - ht * 0.84)} L {f(tx + wd * 0.16)} {f(base)} Z" fill="{STONE}" stroke="#0D0D0F" stroke-width="2.4"></path>'
                 f'<path d="M{f(tx - wd * 0.12)} {f(base - ht * 0.7)} C {f(tx)} {f(base - ht * 0.5)} {f(tx - wd * 0.08)} {f(base - ht * 0.3)} {f(tx + wd * 0.02)} {f(base - ht * 0.1)}" stroke="#3A2A2A" stroke-width="{f(wd * 0.05)}" fill="none" opacity="0.5"></path>')
    for k, (dx, a) in enumerate(((-0.12, -8), (0.1, 12))):
        cx = x + wd * dx
        o.append(f'<g transform="translate({f(cx)} {f(base - ht * 0.06)}) rotate({a})"><rect x="{f(-wd * 0.16)}" y="{f(-ht * 0.06)}" width="{f(wd * 0.32)}" height="{f(ht * 0.1)}" fill="{CHAR}" stroke="#0D0D0F" stroke-width="2"></rect>'
                 + "".join(f'<path d="M{f(-wd * 0.16 + j * wd * 0.08)} {f(-ht * 0.06)} L {f(-wd * 0.16 + j * wd * 0.08)} {f(ht * 0.04)}" stroke="#4A3020" stroke-width="1.4"></path>' for j in range(1, 4)) + '</g>')
    if embers:
        for _ in range(10):
            o.append(f'<circle cx="{f(x + r.uniform(-wd * 0.26, wd * 0.26))}" cy="{f(base - r.uniform(0, ht * 0.14))}" r="{f(r.uniform(1.4, 3))}" fill="#FF6A2A"></circle>')
    return "".join(o)

def ruins(w, h, seed, night=False, gate=True):
    """Jerusalem's wall broken down and its gates burned with fire, seen from without (night=True: under the moon)."""
    base = h * 0.82
    if night:
        o = [K2.sky(w, h, "#0B0B2A", "#2A2A5A"), mk.stars(50, w, h * 0.5, seed), f'<circle cx="{f(w * 0.84)}" cy="{f(h * 0.16)}" r="{f(min(w, h) * 0.06)}" fill="#F3EFE6" opacity="0.9"></circle>']
        col = "#7A7A8A"
    else:
        o = [K2.sky(w, h, "#8A7A8A", "#E8C8A0")]
        col = STONE
    o.append(hills(w, h, h * 0.5, seed, "#5A4A5A" if night else "#A88A6A", amp=12, step=70))
    o.append(J.jericho(-10, w * 0.24, h * 0.42, base, seed, color=col, towers=1, houses=False))
    o.append(rubble(w * 0.24, w * 0.5, base, h * 0.5, seed, color=col))
    if gate: o.append(burnt_gate(w * 0.62, base, w * 0.22, h * 0.5, seed, embers=not night))
    else: o.append(rubble(w * 0.5, w * 0.74, base, h * 0.5, seed + 3, color=col))
    o.append(rubble(w * 0.74, w + 10, base, h * 0.4, seed + 1, color=col))
    o.append(ground(w, h, base, "#3A3040" if night else "#8A7A5A", dy=0))
    return "".join(o)

def cupbearer(p, w, h, seed, queen=False):
    """The king on his throne in the palace, wine before him; Nehemiah the cupbearer giving him the cup (queen=True: the
    queen also sitting by him)."""
    b = h * 0.94; k = min(1.1, h / 320)
    o = [mk.defs(p, *ALL), palace(w, h, seed, floor=0.84, cols=4)]
    tx = w * (0.36 if queen else 0.3)
    o.append(S3.throne(tx, b, k))
    if queen: o.append(S3.throne(w * 0.14, b, k * 0.9))
    s = fit(b, max(h * 0.36, b - 240))
    o.append(persian_king(p, tx, b - 40 * k, s * 0.86))
    if queen:
        o.append(mk.person(p, round(w * 0.14), round(b - 36 * k), round(s * 0.8, 3), body="#5A2A16", cloth=ART_C, woman=True, hair="#0D0D0F", sw=3, extra=CROWN))
    nx = w * 0.64
    o.append(neh_fig(p, nx, b, s, flip=True, up=[(22, -158), (44, -150), (62, -158)]))
    cx, cy = nx - 62 * s, b - 158 * s
    o.append(f'<path d="M{f(cx - 9 * s)} {f(cy - 14 * s)} L {f(cx + 9 * s)} {f(cy - 14 * s)} L {f(cx + 4 * s)} {f(cy)} L {f(cx - 4 * s)} {f(cy)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path>'
             f'<path d="M{f(cx)} {f(cy)} L {f(cx)} {f(cy + 8 * s)} M{f(cx - 6 * s)} {f(cy + 8 * s)} L {f(cx + 6 * s)} {f(cy + 8 * s)}" stroke="#0D0D0F" stroke-width="1.8"></path>')
    jx = w * 0.84                                          # the wine on its stand
    o.append(f'<rect x="{f(jx - 30 * k)}" y="{f(b - 60 * k)}" width="{f(60 * k)}" height="{f(60 * k)}" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<path d="M{f(jx - 14 * k)} {f(b - 60 * k)} C {f(jx - 26 * k)} {f(b - 90 * k)} {f(jx - 14 * k)} {f(b - 120 * k)} {f(jx - 6 * k)} {f(b - 124 * k)} L {f(jx - 6 * k)} {f(b - 134 * k)} '
             f'L {f(jx + 6 * k)} {f(b - 134 * k)} L {f(jx + 6 * k)} {f(b - 124 * k)} C {f(jx + 14 * k)} {f(b - 120 * k)} {f(jx + 26 * k)} {f(b - 90 * k)} {f(jx + 14 * k)} {f(b - 60 * k)} Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(jx - 22 * k)} {f(b - 96 * k)} L {f(jx + 22 * k)} {f(b - 96 * k)}" stroke="#E8B830" stroke-width="3"></path>')
    return "".join(o)

def letters_seal(w, h, seed):
    """The king's letters: three sealed scrolls with purple cords on a table, the winged seal of Persia pressed in clay."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A1A3A"></rect>', V.rays(w * 0.5, h * 0.5, 24, 12, max(w, h), color="#E8C88A", op=0.1),
         f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></rect>']
    k = min(1.4, h / 160)
    for i, (x, rot) in enumerate(((0.3, -8), (0.52, 4), (0.74, -3))):
        o.append(S3.letter(w * x, h * (0.7 + (i % 2) * 0.06), k, rot=rot))
    sx, sy, r = w * 0.12, h * 0.8, min(w, h) * 0.08
    o.append(f'<circle cx="{f(sx)}" cy="{f(sy)}" r="{f(r)}" fill="#B5121B" stroke="#0D0D0F" stroke-width="2"></circle>'
             f'<path d="M{f(sx - r * 0.7)} {f(sy)} C {f(sx - r * 0.4)} {f(sy - r * 0.5)} {f(sx - r * 0.2)} {f(sy - r * 0.2)} {f(sx)} {f(sy - r * 0.1)} C {f(sx + r * 0.2)} {f(sy - r * 0.2)} {f(sx + r * 0.4)} {f(sy - r * 0.5)} {f(sx + r * 0.7)} {f(sy)}" '
             f'fill="none" stroke="#E8B830" stroke-width="2"></path><circle cx="{f(sx)}" cy="{f(sy + r * 0.1)}" r="{f(r * 0.22)}" fill="none" stroke="#E8B830" stroke-width="2"></circle>')
    return "".join(o)

def escort(p, w, h, seed):
    """Nehemiah on the road beyond the River with the captains of the army and horsemen the king sent with him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#FFC890", "#F3E0B0"), sun(w * 0.86, h * 0.26, 18), hills(w, h, h * 0.5, seed, "#B08A6A", amp=12, step=80), ground(w, h, h * 0.62, "#D8B880", dy=0)]
    s = fit(b, max(h * 0.4, b - 220)) * 1.1
    for i in range(3):
        o.append(horseman(p, w * (0.1 + i * 0.13), b - (i % 2) * 6, s * 0.9, cloth=("#6A2A1A", "#5A3A22", "#7A3A1A")[i], color=("#3A2214", "#6A4A2A", "#2A1A14")[i]))
    o.append(N.mount(w * 0.6, b, s, rider_cloth=NEH_C, p=p, extra=A.headcloth(NEH_C, cord="#E8B830")))
    for i in range(2):
        o.append(horseman(p, w * (0.78 + i * 0.13), b - (i % 2) * 6, s * 0.9, cloth=("#6A2A1A", "#5A3A22")[i]))
    return "".join(o)

def night_ride(p, w, h, seed):
    """Nehemiah riding by night round the broken wall, a few men on foot with him, the moon over the ruins."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), ruins(w, h * 0.78, seed, night=True), f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w + 20)}" height="{f(h * 1.4)}" fill="#2A2438"></rect>',
         f'<path d="M-10 {f(h * 0.64)} L {f(w + 10)} {f(h * 0.64)}" stroke="#0D0D0F" stroke-width="2"></path>']
    s = fit(b, max(h * 0.48, b - 200))
    o.append(N.mount(w * 0.5, b, s * 1.2, rider_cloth=NEH_C, rider_body="#1A1420", color="#4A4A5A", p=p, extra=A.headcloth(NEH_C, cord="#E8B830")))
    for i in range(3):
        c = ("#5A5A7A", "#6A5A6A", "#4A5A6A")[i]
        o.append(mk.person(p, round(w * (0.14 + i * 0.09)), round(b - i * 3), round(s * (0.95 - i * 0.04), 3), body="#6A5048", cloth=c, kind="Robe", sw=3, extra=A.headcloth(c) + A.BLACK_BEARD))
    return "".join(o)

# The wall of Jerusalem in Nehemiah's day as a plan, north at the left (east at the top). Points in order round the wall
# from the sheep gate westward; kind: g gate, t tower, x a place on the wall. (name, x, y, kind, label dx, dy, anchor)
WALL = [("SHEEP GATE", 0.19, 0.22, "g", -9, 4, "end"),
        ("TOWER OF HAMMEAH", 0.14, 0.3, "t", 9, 4, "start"),
        ("TOWER OF HANANEL", 0.11, 0.44, "t", 9, 4, "start"),
        ("FISH GATE", 0.1, 0.58, "g", 9, 4, "start"),
        ("OLD GATE", 0.14, 0.74, "g", 9, 4, "start"),
        ("GATE OF EPHRAIM", 0.23, 0.84, "g", 0, 17, "middle"),
        ("BROAD WALL", 0.34, 0.87, "w", 0, 17, "middle"),
        ("TOWER OF THE FURNACES", 0.48, 0.87, "t", -4, -10, "end"),
        ("VALLEY GATE", 0.62, 0.82, "g", 0, 17, "middle"),
        ("DUNG GATE", 0.89, 0.6, "g", 9, 4, "start"),
        ("FOUNTAIN GATE", 0.85, 0.36, "g", 9, 4, "start"),
        ("POOL OF SHELAH", 0.79, 0.28, "x", 6, -7, "start"),
        ("SEPULCHRES OF DAVID", 0.7, 0.25, "x", 0, 16, "middle"),
        ("THE ARMORY", 0.61, 0.23, "x", 0, -9, "middle"),
        ("HOUSE OF ELIASHIB", 0.53, 0.22, "x", 0, 16, "middle"),
        ("WATER GATE", 0.46, 0.14, "g", 0, -10, "middle"),
        ("TOWER THAT STANDETH OUT", 0.41, 0.16, "x", 4, 17, "start"),
        ("HORSE GATE", 0.35, 0.15, "g", 0, -10, "middle"),
        ("EAST GATE", 0.3, 0.17, "g", 0, 17, "middle"),
        ("GATE OF HAMMIPHKAD", 0.245, 0.2, "g", -2, -10, "end")]
EXTRA = {"JACKAL'S WELL": (0.78, 0.92), "KING'S POOL": (0.95, 0.24), "STAIRS OF THE CITY OF DAVID": (0.76, 0.34), "GATE OF THE GUARD": (0.27, 0.27)}

def wall_plan(w, h, lit=(), night=False, companies=False, title=""):
    """Jerusalem's wall and gates as a technical plan, north at the left. lit: names on the wall (WALL) lit gold, with the
    stretches between two lit names drawn gold; night=True: the night ride of 2:13–15; companies=True: the two companies
    that gave thanks going round upon the wall (12:31–39)."""
    o = [grid_bg(w, h)]
    P = {n: (w * x, h * y) for n, x, y, *_ in WALL}
    P.update({n: (w * x, h * y) for n, (x, y) in EXTRA.items()})
    o.append(f'<path d="M-10 {f(h * 0.05)} C {f(w * 0.3)} {f(h * 0.02)} {f(w * 0.6)} {f(h * 0.08)} {f(w + 10)} {f(h * 0.06)}" stroke="#2C7DA8" stroke-width="3" fill="none"></path>'
             + label(w * 0.14, h * 0.04 + 12, "THE BROOK", "#2C7DA8", 8))
    o.append(f'<path d="M{f(w * 0.7)} {f(h + 10)} C {f(w * 0.84)} {f(h * 0.96)} {f(w * 0.98)} {f(h * 0.84)} {f(w + 10)} {f(h * 0.7)}" stroke="#4A7A9A" stroke-width="2" fill="none" stroke-dasharray="3 4"></path>')
    tx0, ty0 = w * 0.3, h * 0.3                          # the house of God
    o.append(f'<rect x="{f(tx0)}" y="{f(ty0)}" width="{f(w * 0.16)}" height="{f(h * 0.18)}" fill="#FFD23F" fill-opacity="0.08" stroke="#4A7A9A" stroke-width="1.6"></rect>'
             + label(tx0 + w * 0.08, ty0 + h * 0.1, "THE HOUSE OF GOD", "#8FD0E2", 8))
    o.append(label(w * 0.72, h * 0.5, "THE CITY OF DAVID", "#4A7A9A", 9) + label(w * 0.42, h * 0.58, "JERUSALEM", "#4A7A9A", 12))
    pts = [P[n] for n, *_ in WALL] + [P[WALL[0][0]]]
    o.append('<path d="M' + " L ".join(f"{f(x)} {f(y)}" for x, y in pts) + '" fill="none" stroke="#8FD0E2" stroke-width="3.2" stroke-linejoin="round"></path>')
    names = [n for n, *_ in WALL] + [WALL[0][0]]
    for a, b in zip(names, names[1:]):
        if a in lit and b in lit:
            o.append(f'<path d="M{f(P[a][0])} {f(P[a][1])} L {f(P[b][0])} {f(P[b][1])}" stroke="{GOLD}" stroke-width="5"></path>')
    if night:
        out = [P["VALLEY GATE"], (w * 0.66, h * 0.93), P["JACKAL'S WELL"], (w * 0.97, h * 0.66), (w * 0.95, h * 0.36), P["KING'S POOL"], (w * 0.86, h * 0.1), (w * 0.62, h * 0.09)]
        o.append(route(out, color=GOLD, sw=2.6))
        o.append(label(w * 0.62, h * 0.09 + 14, "TURNED BACK", GOLD, 8))
        for n in ("JACKAL'S WELL", "KING'S POOL"): o.append(node(*P[n], n, CYAN, r=4, dy=-9, size=8))
    if companies:
        a = [P["VALLEY GATE"], P["DUNG GATE"], P["FOUNTAIN GATE"], P["STAIRS OF THE CITY OF DAVID"], P["WATER GATE"]]
        bb = [P["VALLEY GATE"], P["TOWER OF THE FURNACES"], P["BROAD WALL"], P["GATE OF EPHRAIM"], P["OLD GATE"], P["FISH GATE"], P["TOWER OF HANANEL"], P["TOWER OF HAMMEAH"], P["SHEEP GATE"], P["GATE OF THE GUARD"]]
        o.append(route(a, color=GOLD, sw=3.4, dash="10 5") + route(bb, color="#FF8A6A", sw=3.4, dash="10 5"))
        o.append(node(*P["GATE OF THE GUARD"], "", "#FF8A6A", r=4) + label(P["GATE OF THE GUARD"][0] + 9, P["GATE OF THE GUARD"][1] + 4, "GATE OF THE GUARD", "#FF8A6A", 8, "start"))
        o.append(label(w * 0.82, h * 0.82, "THE FIRST COMPANY", GOLD, 9) + label(w * 0.36, h * 0.74, "THE OTHER COMPANY", "#FF8A6A", 9))
    for n, x, y, kd, dx, dy, anc in WALL:
        on = n in lit
        c = GOLD if on else ("#8FD0E2" if kd == "g" else "#4A7A9A")
        X, Y = w * x, h * y
        if kd == "g":
            o.append(f'<rect x="{f(X - 5)}" y="{f(Y - 5)}" width="10" height="10" fill="{c}" stroke="#0D0D0F" stroke-width="1.4"></rect>')
        elif kd == "t":
            o.append(f'<circle cx="{f(X)}" cy="{f(Y)}" r="5" fill="{c}" stroke="#0D0D0F" stroke-width="1.4"></circle>')
        else:
            o.append(f'<circle cx="{f(X)}" cy="{f(Y)}" r="3" fill="{c}"></circle>')
        if kd in "gtw" or on:
            o.append(label(X + dx, Y + dy, n, c, 9 if on else 7.5, anc, weight=700 if on else 600, ls=0.08))
    o.append(label(w * 0.035, h * 0.97, "N ←", "#8FD0E2", 9, "start") + (label(w * 0.5, h * 0.99, title, GOLD, 9) if title else ""))
    return "".join(o)

def gathering(p, w, h, seed):
    """Nehemiah telling the rulers, the priests and the nobles: let us build up the wall — the broken wall behind them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), ruins(w, h * 0.8, seed, gate=False), ground(w, h, h * 0.66, "#B8A07A", dy=0)]
    s = fit(b, max(h * 0.4, b - 230))
    o.append(neh_fig(p, w * 0.2, b, s, up=[(-22, -158), (-40, -190), (-52, -222)]))
    o.append(crowd_at(p, w, h, seed, w * 0.36, w * 0.98, h * 0.72, b, 16, s * 0.6, s * 1.0, flip=True))
    return "".join(o)

def scorners(p, w, h, seed):
    """Sanballat, Tobiah and Geshem laughing them to scorn: three figures in rich robes on a rise, pointing at the wall."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A3A4A", "#E8A06A"), hills(w, h, h * 0.56, seed, "#7A5A4A", amp=10, step=80), ground(w, h, h * 0.66, "#A88A6A", dy=0)]
    s = fit(b, max(h * 0.4, b - 230))
    for i, (c, cord) in enumerate((("#5A1A1E", "#E8B830"), ("#1F4A34", "#0D0D0F"), ("#E8E2D6", "#0D0D0F"))):
        x = w * (0.18 + i * 0.16)
        up = [(22, -158), (50, -176), (78, -184)] if i == 0 else None
        o.append(mk.person(p, round(x), round(b), round(s, 3), body="#5A2A16" if i == 2 else SKIN, cloth=c, kind="Robe", sw=3, up=up, extra=A.headcloth(c, cord=cord) + A.BLACK_BEARD))
    o.append(J.jericho(w * 0.72, w + 10, h * 0.5, h * 0.7, seed, color=STONE, towers=0, houses=False) + rubble(w * 0.62, w * 0.72, h * 0.7, h * 0.3, seed))
    return "".join(o)

# ---- Nehemiah 3–4 -------------------------------------------------------------------------------------------------------
def stone_wall(x0, x1, top, base, seed, color=STONE, course=None):
    """A wall of dressed stone seen from within: courses of blocks, the top uneven where the work goes on."""
    r = random.Random(seed); o = []
    ch = course or max(10, (base - top) / 9)
    o.append(f'<rect x="{f(x0)}" y="{f(top)}" width="{f(x1 - x0)}" height="{f(base - top)}" fill="{color}" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    y, k = top + ch, 0
    while y < base:
        o.append(f'<path d="M{f(x0)} {f(y)} L {f(x1)} {f(y)}" stroke="{STONE_D}" stroke-width="1.6"></path>')
        xx = x0 + (ch * 1.1 if k % 2 else 0)
        while xx < x1:
            o.append(f'<path d="M{f(xx)} {f(y - ch)} L {f(xx)} {f(y)}" stroke="{STONE_D}" stroke-width="1.4"></path>'); xx += ch * 2.2 + r.uniform(-4, 4)
        y += ch; k += 1
    return "".join(o)

def block(x, y, wd, ht, color=STONE):
    return f'<rect x="{f(x - wd / 2)}" y="{f(y - ht)}" width="{f(wd)}" height="{f(ht)}" fill="{color}" stroke="#0D0D0F" stroke-width="1.8"></rect>'

SWORD = '<path d="M14 -110 L 22 -40" stroke="#C8C2D6" stroke-width="4"></path><path d="M8 -112 L 22 -108" stroke="#3E2416" stroke-width="4"></path>'

def builders(p, w, h, seed, dusk=False, trumpet=True, top=0.56):
    """The builders upon the wall: every one with one of his hands wrought in the work and with the other held his weapon,
    his sword girded by his side; he that sounded the trumpet by Nehemiah. The seed picks one of three groupings, and some
    carry burdens (a basket on the head) up onto the wall."""
    wt = h * top
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A3A6A" if dusk else "#8FD0E2", "#FFB04A" if dusk else "#F3E8C8")]
    if dusk: o.append(sun(w * 0.82, h * 0.3, 22))
    o.append(hills(w, h, h * 0.44, seed, "#7A5A5A" if dusk else "#A8946A", amp=10, step=90))
    o.append(J.city_hill(w * (0.86 if trumpet else 0.6), h * 0.5, w * 0.2, h * 0.12, seed))
    o.append(stone_wall(-10, w + 10, wt, h + 10, seed))
    lay = [((0.2, 0.34, 0.62), 0.27, (0.06, 0.48)), ((0.1, 0.44, 0.56), 0.3, (0.2, 0.66)), ((0.16, 0.28, 0.5), 0.4, (0.06, 0.62))][seed % 3]
    if not trumpet: lay = (lay[0] + (0.78,), lay[1], lay[2] + (0.9,))
    for i, x in enumerate(lay[2]):                               # blocks waiting to be laid
        o.append(block(w * x, wt, w * 0.05, h * 0.05 * (1 + i % 2)))
    s = fit(wt, max(h * 0.08, wt - 200))
    lift = [(-22, -158), (-34, -190), (-30, -222)]
    cols = list(WAR); r.shuffle(cols)
    for i, x in enumerate(lay[0]):
        c = cols[i % 4]
        if i == 1 and seed % 2:                                 # a bearer of burdens, his weapon in the other hand
            o.append(mk.person(p, round(w * x), round(wt), round(s * 0.97, 3), body=SKIN, cloth=c, kind="Tunic", sw=3, up=[(-22, -158), (-26, -190), (-14, -214)],
                               extra=E4.SPEAR + SWORD) + E4.basket(w * x, wt - 206 * s, s * 1.5))
            continue
        o.append(mk.person(p, round(w * x), round(wt), round(s, 3), body=SKIN, cloth=c, kind="Tunic", sw=3, up=lift, extra=E4.SPEAR + SWORD + A.headcloth(c)))
        hx, hy = w * x - 30 * s, wt - 222 * s
        o.append(f'<rect x="{f(hx - 16 * s)}" y="{f(hy - 22 * s)}" width="{f(32 * s)}" height="{f(20 * s)}" fill="{STONE}" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    o.append(mk.person(p, round(w * lay[1]), round(wt), round(s * 0.96, 3), body=SKIN, cloth="#4A5A3A", kind="Tunic", sw=3, extra=E4.SHIELD + SWORD + A.headcloth("#4A5A3A")))
    if trumpet:
        o.append(neh_fig(p, w * 0.76, wt, s, flip=True))
        o.append(J.trumpeter(p, w * 0.92, wt, s * 0.96, flip=True))
    return "".join(o)

def cover_art(p, w, h, seed):
    return builders(p, w, h, seed, dusk=True, top=0.72)

def gate_build(p, w, h, seed, priests=False):
    """A gate rebuilt: the two towers of new stone, the beams laid, one door set up and the other raised by men with ropes,
    the bolts and bars at its foot (priests=True: the priests in white at the work)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.5, seed, "#A8946A", amp=10, step=90),
         stone_wall(-10, w * 0.26, h * 0.42, h * 0.8, seed), stone_wall(w * 0.74, w + 10, h * 0.42, h * 0.8, seed + 1),
         stone_wall(w * 0.3, w * 0.4, h * 0.18, h * 0.8, seed + 2, course=h * 0.05), stone_wall(w * 0.6, w * 0.7, h * 0.18, h * 0.8, seed + 3, course=h * 0.05),
         f'<rect x="{f(w * 0.28)}" y="{f(h * 0.15)}" width="{f(w * 0.44)}" height="{f(h * 0.05)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<rect x="{f(w * 0.4)}" y="{f(h * 0.2)}" width="{f(w * 0.2)}" height="{f(h * 0.6)}" fill="#3A2A1E" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<rect x="{f(w * 0.4)}" y="{f(h * 0.22)}" width="{f(w * 0.1)}" height="{f(h * 0.58)}" fill="#B5793A" stroke="#0D0D0F" stroke-width="2.2"></rect>'
         + "".join(f'<path d="M{f(w * 0.4)} {f(h * (0.3 + k * 0.15))} L {f(w * 0.5)} {f(h * (0.3 + k * 0.15))}" stroke="#5A3A1E" stroke-width="3"></path>' for k in range(4)),
         f'<g transform="rotate(-24 {f(w * 0.6)} {f(h * 0.8)})"><rect x="{f(w * 0.5)}" y="{f(h * 0.22)}" width="{f(w * 0.1)}" height="{f(h * 0.58)}" fill="#C8894A" stroke="#0D0D0F" stroke-width="2.2"></rect>'
         + "".join(f'<path d="M{f(w * 0.5)} {f(h * (0.3 + k * 0.15))} L {f(w * 0.6)} {f(h * (0.3 + k * 0.15))}" stroke="#5A3A1E" stroke-width="3"></path>' for k in range(4)) + '</g>',
         ground(w, h, h * 0.8, "#C8B88A", dy=0)]
    o.append(f'<path d="M{f(w * 0.52)} {f(h * 0.3)} L {f(w * 0.86)} {f(h * 0.62)}" stroke="#8A6A3A" stroke-width="2"></path>')
    o.append(f'<rect x="{f(w * 0.12)}" y="{f(b - h * 0.04)}" width="{f(w * 0.16)}" height="{f(h * 0.03)}" fill="#5A5A62" stroke="#0D0D0F" stroke-width="1.6"></rect>'
             f'<rect x="{f(w * 0.16)}" y="{f(b - h * 0.08)}" width="{f(w * 0.1)}" height="{f(h * 0.03)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    s = fit(b, max(h * 0.44, b - 220))
    pull = [(22, -158), (40, -186), (56, -206)]
    for i in range(2):
        x = w * (0.72 + i * 0.08)
        o.append(K1.priest(p, x, b, s, flip=True, up=pull) if priests else man(p, x, b, s, WAR[i], flip=True, up=pull))
    for i in range(2):
        x = w * (0.08 + i * 0.1)
        o.append(K1.priest(p, x, b, s * 0.96) if priests else man(p, x, b, s * 0.96, WAR[2 + i]))
    return "".join(o)

def daughters(p, w, h, seed):
    """Shallum the ruler, he and his daughters at the work: he lifts a stone onto the wall, they bring baskets on their heads."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, "#A8946A", amp=10, step=90),
         stone_wall(w * 0.6, w + 10, h * 0.42, h * 0.84, seed), block(w * 0.7, h * 0.42, w * 0.06, h * 0.06), ground(w, h, h * 0.84, "#C8B88A", dy=0)]
    s = fit(b, max(h * 0.3, b - 220))
    x = w * 0.5
    o.append(mk.person(p, round(x), round(b), round(s, 3), body=SKIN, cloth="#3A4A6A", kind="Robe", sw=3, up=[(22, -158), (36, -190), (34, -222)],
                       extra=A.headcloth("#3A4A6A") + A.BLACK_BEARD)
             + f'<rect x="{f(x + 34 * s - 18 * s)}" y="{f(b - 222 * s - 24 * s)}" width="{f(36 * s)}" height="{f(22 * s)}" fill="{STONE}" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    for i, c in enumerate(("#C2456A", "#2E6B8A", "#7A3BA8")):
        xx = w * (0.1 + i * 0.12); k = s * (0.92 - i * 0.03)
        o.append(woman(p, xx, b - (i % 2) * 4, k, c, up=[(-22, -158), (-26, -190), (-14, -206)]) + E4.basket(xx, b - (i % 2) * 4 - 200 * k, k * 1.5))
    return "".join(o)

FOES = [("SAMARIA", 0.5, 0.12, "SANBALLAT"), ("AMMON", 0.88, 0.5, "TOBIAH · THE AMMONITES"), ("ARABIA", 0.5, 0.9, "THE ARABIANS"), ("ASHDOD", 0.12, 0.5, "THE ASHDODITES")]
def foes_map(w, h):
    """They conspired all of them together to come and fight against Jerusalem: the adversaries on every side as a map."""
    o = [grid_bg(w, h)]
    cx, cy = w * 0.5, h * 0.5
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(min(w, h) * 0.12)}" fill="none" stroke="{GOLD}" stroke-width="2.4" stroke-dasharray="8 4"></circle>'
             + node(cx, cy, "JERUSALEM", GOLD, r=7, dy=-14, size=11))
    for nm, x, y, who in FOES:
        X, Y = w * x, h * y
        dx, dy = cx - X, cy - Y; L = math.hypot(dx, dy); k = 1 - min(w, h) * 0.15 / L
        o.append(route([(X, Y), (X + dx * k, Y + dy * k)], color=RED_C, sw=3, dash="9 5"))
        o.append(node(X, Y, nm, "#FF8A6A", r=5, dy=-11, size=9) + label(X, Y + 17, who, "#FF8A6A", 8))
    return "".join(o)

def watch_night(p, w, h, seed, water=False):
    """A watch set day and night: men on the wall with spears and a torch under the stars (water=True: going down to the
    water every one with his weapon, the wall behind them)."""
    b = h * 0.94; wt = h * (0.86 if water else 0.66)
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#0B0B2A", "#2A2A5A"), mk.stars(60, w, h * 0.5, seed)]
    if water:
        o.append(stone_wall(w * 0.68, w + 10, h * 0.3, h * 0.86, seed, color="#7A7A8A") + ground(w, h, h * 0.86, "#2A2438", dy=0)
                 + f'<ellipse cx="{f(w * 0.14)}" cy="{f(h * 0.92)}" rx="{f(w * 0.12)}" ry="{f(h * 0.04)}" fill="#2C5A7A" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    else:
        o.append(stone_wall(-10, w + 10, wt, h + 10, seed, color="#7A7A8A"))
    s = fit(wt, max(h * 0.24, wt - 200))
    for i in range(4):
        x = w * ((0.26 + i * 0.1) if water else (0.14 + i * 0.22))
        o.append(warrior(p, x, wt - (i % 2) * 3 * water, s * (0.9 - 0.03 * i * water if water else 1), ("#3A3450", "#4A3A3A", "#3A4A4A", "#4A4A5A")[i], flip=water))
    if not water:
        tx, ty = w * 0.46, wt - 150 * s
        o.append(f'<path d="M{f(tx)} {f(wt)} L {f(tx)} {f(ty)}" stroke="#3A2214" stroke-width="{f(5 * s)}"></path>' + E.flame(tx, ty, 26 * s, 60 * s, 0.1)
                 + f'<circle cx="{f(tx)}" cy="{f(ty - 20 * s)}" r="{f(80 * s)}" fill="#FFC14D" opacity="0.15"></circle>')
    return "".join(o)

def families_armed(p, w, h, seed):
    """In the lowest parts of the space behind the wall, in the open places, the people set after their families with their
    swords, their spears, and their bows."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8A7A8A", "#E8C8A0"), stone_wall(-10, w + 10, h * 0.2, h * 0.62, seed), ground(w, h, h * 0.62, "#B8A07A", dy=0)]
    s = fit(b, max(h * 0.4, b - 220))
    for i in range(7):
        x = w * (0.06 + i * 0.14)
        if i % 3 == 2:
            o.append(woman(p, x, b, s * 0.9, ("#C2456A", "#2E6B8A")[i % 2]) + mk.person(p, round(x + 26 * s), round(b), round(s * 0.55, 3), body=SKIN, cloth="#E8D8B0", kind="Tunic", sw=3))
        else:
            o.append(warrior(p, x, b - (i % 2) * 4, s, WAR[i % 4]) + (SWORD if False else ""))
            if i % 2:
                bx, by = x + 26 * s, b - 130 * s
                o.append(f'<path d="M{f(bx)} {f(by - 50 * s)} Q {f(bx + 24 * s)} {f(by)} {f(bx)} {f(by + 50 * s)}" fill="none" stroke="#5A3A1E" stroke-width="{f(4 * s)}"></path>'
                         f'<path d="M{f(bx)} {f(by - 50 * s)} L {f(bx)} {f(by + 50 * s)}" stroke="#E8E2D6" stroke-width="1.4"></path>')
    return "".join(o)

# ---- Nehemiah 5–6 -------------------------------------------------------------------------------------------------------
NOBLE_C = ("#6A3A5A", "#2A5A5A", "#7A4A1E")

def noble(p, x, y, s, cloth, flip=False, up=None):
    """A noble or ruler of Judah at a distance: a rich robe and headcloth with a gold cord, black beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, kind="Robe", sw=3, flip=flip, up=up,
                     extra=A.headcloth(cloth, cord="#E8B830") + A.BLACK_BEARD)

def outcry(p, w, h, seed):
    """A great cry of the people and of their wives against their brethren: the poor with their arms raised and their
    children, the nobles before their houses, the empty grain sacks between them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#C8A890", "#F3E0B0"), J.city_hill(w * 0.82, h * 0.62, w * 0.3, h * 0.2, seed), ground(w, h, h * 0.62, "#C8A06A", dy=0)]
    s = fit(b, max(h * 0.4, b - 220))
    raise_ = [(-22, -158), (-40, -190), (-52, -222)]
    for i in range(5):
        x = w * (0.06 + i * 0.1)
        if i == 2:
            o.append(woman(p, x, b, s * 0.94, "#4A3A5A", up=raise_) + mk.person(p, round(x + 28 * s), round(b), round(s * 0.5, 3), body=SKIN, cloth="#E8D8B0", kind="Tunic", sw=3))
        else:
            o.append(man(p, x, b - (i % 2) * 4, s * (0.96 - (i % 2) * 0.04), ("#6A5A4A", "#5A5A4A", "#7A6A5A", "#4A4A3A", "#6A5040")[i], up=raise_ if i % 2 == 0 else None))
    for i in range(3):
        o.append(R1.sack(w * (0.56 + i * 0.05), b, s * 0.9))
    for i in range(3):
        o.append(noble(p, w * (0.66 + i * 0.08), b - (i % 2) * 4, s, NOBLE_C[i], flip=True))
    return "".join(o)

def shake_lap(p, w, h, seed):
    """Nehemiah shaking out his lap before the assembly — so God shake out every man that performeth not this promise —
    the priests by him, and all the assembly saying Amen."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), K1.temple_front(w * 0.5, h * 0.6, w * 0.4, seed), ground(w, h, h * 0.6, "#C8B88A", dy=0)]
    s = fit(b, max(h * 0.36, b - 240))
    x = w * 0.5
    o.append(neh_fig(p, x, b, s * 1.05, up=[(22, -158), (48, -132), (58, -104)]))
    lx, ly = x + 58 * s * 1.05, b - 104 * s * 1.05
    o.append(f'<path d="M{f(lx - 10 * s)} {f(ly)} C {f(lx + 20 * s)} {f(ly + 10 * s)} {f(lx + 26 * s)} {f(ly + 40 * s)} {f(lx + 14 * s)} {f(ly + 54 * s)} L {f(lx - 4 * s)} {f(ly + 30 * s)} Z" fill="{NEH_C}" stroke="#0D0D0F" stroke-width="2"></path>')
    r = random.Random(seed)
    for _ in range(8):
        o.append(f'<circle cx="{f(lx + r.uniform(0, 30) * s)}" cy="{f(ly + r.uniform(60, 110) * s)}" r="{f(r.uniform(1.4, 3) * s)}" fill="#8A6A3A"></circle>')
    for i in range(2): o.append(K1.priest(p, w * (0.28 + i * 0.09), b, s * 0.96))
    o.append(crowd_at(p, w, h, seed, w * 0.02, w * 0.16, h * 0.7, b, 4, s * 0.6, s * 0.9))
    o.append(crowd_at(p, w, h, seed + 1, w * 0.7, w * 0.98, h * 0.7, b, 6, s * 0.6, s * 0.9, flip=True))
    return "".join(o)

def ono_map(w, h, letter=False):
    """Come, let us meet together in one of the villages in the plain of Ono: Jerusalem in the hills, Ono in the plain to
    the north-west, the messengers going between four times (letter=True: the fifth time, with an open letter)."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.08)} -10 C {f(w * 0.1)} {f(h * 0.4)} {f(w * 0.06)} {f(h * 0.7)} {f(w * 0.04)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>'
             + label(w * 0.05, h * 0.5, "THE SEA", "#8FD0E2", 8, "start"))
    o.append(f'<path d="M{f(w * 0.48)} -10 C {f(w * 0.46)} {f(h * 0.4)} {f(w * 0.52)} {f(h * 0.7)} {f(w * 0.5)} {f(h + 10)}" stroke="#4A7A9A" stroke-width="1.6" stroke-dasharray="4 5" fill="none"></path>'
             + label(w * 0.53, h * 0.94, "THE HILL COUNTRY", "#4A7A9A", 8, "start") + label(w * 0.3, h * 0.94, "THE PLAIN", "#4A7A9A", 8))
    J_, O_ = (w * 0.7, h * 0.62), (w * 0.24, h * 0.36)
    o.append(f'<ellipse cx="{f(O_[0])}" cy="{f(O_[1])}" rx="{f(w * 0.1)}" ry="{f(h * 0.12)}" fill="#D7261E" fill-opacity="0.12" stroke="#D7261E" stroke-width="1.6" stroke-dasharray="5 4"></ellipse>')
    for k in range(4):
        dy = (k - 1.5) * h * 0.04
        o.append(route([(O_[0] + w * 0.06, O_[1] + dy), (J_[0] - w * 0.05, J_[1] + dy - h * 0.06)], color="#FF8A6A", sw=1.8, dash="6 5"))
    if letter:
        o.append(route([(O_[0] + w * 0.08, O_[1] + h * 0.16), (J_[0] - w * 0.04, J_[1] + h * 0.06)], color=GOLD, sw=3, dash="10 4")
                 + label((O_[0] + J_[0]) / 2, (O_[1] + J_[1]) / 2 + h * 0.2, "THE FIFTH TIME · AN OPEN LETTER", GOLD, 9))
    else:
        o.append(label((O_[0] + J_[0]) / 2 - w * 0.04, (O_[1] + J_[1]) / 2 - h * 0.14, "FOUR TIMES", "#FF8A6A", 9))
    o.append(node(*O_, "ONO", "#FF8A6A", r=5, dy=-12, size=10) + node(*J_, "JERUSALEM", GOLD, r=7, dy=-14, size=11)
             + node(w * 0.66, h * 0.12, "SAMARIA", "#FF8A6A", r=4, dy=-10, size=8))
    return "".join(o)

def wall_done(p, w, h, seed):
    """The wall finished in fifty and two days: the whole wall standing with its towers, a gate with its doors set up,
    Jerusalem's houses behind, the morning sun."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#FFC890", "#FFF4C2"), sun(w * 0.12, h * 0.2, 22), hills(w, h, h * 0.42, seed, "#B8A07A", amp=10, step=90),
         J.jericho(-10, w + 10, h * 0.42, h * 0.82, seed, color=STONE, towers=3, houses=True),
         S4b.gatehouse(w * 0.5, h * 0.82, w * 0.22, h * 0.5),
         f'<rect x="{f(w * 0.5 - w * 0.04)}" y="{f(h * 0.82 - h * 0.2)}" width="{f(w * 0.04)}" height="{f(h * 0.2)}" fill="#B5793A" stroke="#0D0D0F" stroke-width="2"></rect>'
         f'<rect x="{f(w * 0.5)}" y="{f(h * 0.82 - h * 0.2)}" width="{f(w * 0.04)}" height="{f(h * 0.2)}" fill="#B5793A" stroke="#0D0D0F" stroke-width="2"></rect>'
         f'<rect x="{f(w * 0.46)}" y="{f(h * 0.82 - h * 0.12)}" width="{f(w * 0.08)}" height="{f(h * 0.02)}" fill="#3A2A1A" stroke="#0D0D0F" stroke-width="1.4"></rect>',
         ground(w, h, h * 0.82, "#C8A06A", dy=0)]
    return "".join(o)

# ---- Nehemiah 7 ---------------------------------------------------------------------------------------------------------
def bars(w, h, rows, title="", ncol=2, color=CYAN, hi=None):
    """A census as a bar chart in columns: rows of (name, number); the bar's length is the number, written at its end."""
    o = [grid_bg(w, h, color="#3A2A5A", bg="#1A1430")]
    n = len(rows); per = math.ceil(n / ncol)
    top, bot = h * 0.06, h * (0.9 if title else 0.96)
    rh = (bot - top) / per
    mx = max(v for _, v in rows)
    cw = w / ncol
    size = max(7.5, min(10.5, rh * 0.42))
    for i, (nm, val) in enumerate(rows):
        c, r = divmod(i, per)
        x0 = c * cw + cw * 0.46; y = top + r * rh + rh * 0.5
        L = (cw * 0.36) * val / mx
        col = GOLD if hi and nm in hi else color
        o.append(label(x0 - 6, y + size * 0.36, nm, col, size, "end", ls=0.06)
                 + f'<rect x="{f(x0)}" y="{f(y - rh * 0.3)}" width="{f(max(2, L))}" height="{f(rh * 0.6)}" fill="{col}" fill-opacity="0.35" stroke="{col}" stroke-width="1.4"></rect>'
                 + label(x0 + L + 5, y + size * 0.36, f"{val:,}", col, size, "start", weight=700, ls=0.04))
    if title: o.append(label(w * 0.5, h * 0.96, title, "#C8C2D6", 9))
    return "".join(o)

def tally_grid(w, h, rows, cols=4, title=""):
    """A tally board in rows and columns: (name, number, colour) boxes, the number large."""
    o = [grid_bg(w, h, color="#3A2A5A", bg="#1A1430")]
    n = len(rows); nr = math.ceil(n / cols)
    top, bot = h * 0.06, h * (0.88 if title else 0.96)
    bh = (bot - top - (nr - 1) * h * 0.04) / nr
    for i, (nm, num, c) in enumerate(rows):
        r, k = divmod(i, cols)
        m = min(cols, n - r * cols)
        bw = w * 0.9 / cols - w * 0.02
        x = w * 0.5 + (k - (m - 1) / 2) * (w * 0.9 / cols)
        y = top + r * (bh + h * 0.04)
        o.append(f'<rect x="{f(x - bw / 2)}" y="{f(y)}" width="{f(bw)}" height="{f(bh)}" fill="none" stroke="{c}" stroke-width="2"></rect>'
                 + label(x, y + bh * 0.28, nm, c, max(7.5, min(11, bw / (len(nm) * 0.75 + 2))), ls=0.06)
                 + f'<text x="{f(x)}" y="{f(y + bh * 0.78)}" fill="{c}" font-family="Anton, sans-serif" font-size="{f(min(bw / (len(num) * 0.62 + 1), bh * 0.42))}" text-anchor="middle">{num}</text>')
    if title: o.append(label(w * 0.5, h * 0.95, title, "#C8C2D6", 9))
    return "".join(o)

def names_board(w, h, names, title="", cols=6, color=GOLD):
    """Names set out on a board of tiles (the leaders who came with Zerubbabel, the men who stood by Ezra)."""
    o = [grid_bg(w, h, color="#3A2A5A", bg="#1A1430")]
    n = len(names); rows = math.ceil(n / cols)
    top, bot = h * 0.08, h * (0.86 if title else 0.94)
    gx = w * 0.02; tw = (w * 0.94 - gx * (cols - 1)) / cols; th = (bot - top - h * 0.04 * (rows - 1)) / rows
    for i, nm in enumerate(names):
        r, c = divmod(i, cols)
        m = min(cols, n - r * cols)
        x = w * 0.03 + (c + (cols - m) / 2) * (tw + gx); y = top + r * (th + h * 0.04)
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(tw)}" height="{f(th)}" rx="4" fill="{color}" fill-opacity="0.12" stroke="{color}" stroke-width="1.6"></rect>'
                 + label(x + tw / 2, y + th * 0.6, nm, color, max(7.5, min(12, tw / (len(nm) * 0.7 + 1))), ls=0.06))
    if title: o.append(label(w * 0.5, h * 0.95, title, "#C8C2D6", 9))
    return "".join(o)

def genealogy_book(w, h, seed, gaps=False):
    """The book of the genealogy of them that came up at the first: a long scroll unrolled, ruled with rows of names and
    numbers (gaps=True: blank places where a register was sought and not found)."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A2A"></rect>', V.rays(w * 0.5, h * 0.5, 24, 12, max(w, h), color="#E8C88A", op=0.1)]
    x0, x1, y0, y1 = w * 0.12, w * 0.88, h * 0.14, h * 0.86
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(x1 - x0)}" height="{f(y1 - y0)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    for side in (x0, x1):
        o.append(f'<ellipse cx="{f(side)}" cy="{f((y0 + y1) / 2)}" rx="{f(w * 0.025)}" ry="{f((y1 - y0) * 0.54)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    rows = max(4, int((y1 - y0) / 16))
    for c in range(3):
        cx0 = x0 + w * 0.05 + c * (x1 - x0 - w * 0.06) / 3
        for k in range(rows):
            y = y0 + (k + 0.8) * (y1 - y0) / (rows + 0.4)
            if gaps and r.random() < 0.18:
                o.append(f'<rect x="{f(cx0)}" y="{f(y - 5)}" width="{f(w * 0.16)}" height="8" fill="none" stroke="#B5121B" stroke-width="1.4" stroke-dasharray="3 3"></rect>')
                continue
            o.append(f'<path d="M{f(cx0)} {f(y)} L {f(cx0 + w * r.uniform(0.08, 0.13))} {f(y)}" stroke="#5A3A22" stroke-width="2"></path>'
                     f'<path d="M{f(cx0 + w * 0.15)} {f(y)} L {f(cx0 + w * 0.19)} {f(y)}" stroke="#8A5A30" stroke-width="2"></path>')
    return "".join(o)

def empty_city(w, h, seed):
    """The city wide and large, but the people few therein, and the houses not builded: the new wall round a broad empty
    city, a few houses, the house of God."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.3, seed, "#B8A07A", amp=10, step=90), ground(w, h, h * 0.38, "#C8B88A", dy=0)]
    o.append(K1.temple_front(w * 0.22, h * 0.5, w * 0.2, seed))
    for _ in range(int(w / 50)):
        x, y = r.uniform(w * 0.36, w * 0.96), r.uniform(h * 0.42, h * 0.7)
        if r.random() < 0.3:
            o.append(f'<rect x="{f(x)}" y="{f(y - 18)}" width="34" height="20" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.6"></rect><rect x="{f(x + 12)}" y="{f(y - 12)}" width="7" height="10" fill="#3A2214"></rect>')
        else:
            o.append(f'<path d="M{f(x)} {f(y)} l 8 -6 l 10 2 l 6 4 Z" fill="{STONE_D}" stroke="#0D0D0F" stroke-width="1.2"></path>')
    o.append(stone_wall(-10, w + 10, h * 0.72, h + 10, seed))
    o.append(S4b.gatehouse(w * 0.62, h * 0.98, w * 0.16, h * 0.32))
    return "".join(o)

def villages(p, w, h, seed):
    """All Israel dwelt in their cities: walled towns on the hills of Judah, the seventh month, people going up the roads."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#FFC890", "#F3E8C8"), hills(w, h, h * 0.4, seed, "#9A9A6A", amp=14, step=90),
         J.city_hill(w * 0.2, h * 0.56, w * 0.18, h * 0.16, seed), J.city_hill(w * 0.56, h * 0.5, w * 0.16, h * 0.14, seed + 1), J.city_hill(w * 0.86, h * 0.58, w * 0.18, h * 0.16, seed + 2),
         hills(w, h, h * 0.62, seed + 3, "#8AA05A", amp=8, step=70), ground(w, h, h * 0.74, "#C8B07A", dy=0)]
    s = fit(b, max(h * 0.5, b - 200))
    for i in range(5):
        x = w * (0.08 + i * 0.2)
        o.append(man(p, x, b - (i % 2) * 5, s * 0.8, ("#5A4A3A", "#3A4A6A", "#6A3A2A", "#4A5A3A", "#5A3A5A")[i]) if i % 2 == 0 else woman(p, x, b - 5, s * 0.78, ("#C2456A", "#2E6B8A")[i // 2 % 2]))
    return "".join(o)

# ---- Nehemiah 8–9 -------------------------------------------------------------------------------------------------------
EZRA_C = "#2A2A6A"

def ezra_fig(p, x, y, s, flip=False, up=None):
    """Ezra the priest the scribe at a distance: a white robe, the indigo headcloth with a gold band, white beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#F3EFE6", kind="Robe", sw=3, flip=flip, up=up,
                     extra=A.headcloth(EZRA_C, cord="#E8B830") + A.WHITE_BEARD)

def book_open(x, y, s):
    """An open book of the law held up: two pages with ruled lines."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-30 -10 L 0 -4 L 30 -10 L 30 12 L 0 18 L -30 12 Z" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M0 -4 L 0 18" stroke="#0D0D0F" stroke-width="1.6"></path>'
            + "".join(f'<path d="M{-26 + k * 30} {-2 + j * 5} L {-6 + k * 30} {j * 5}" stroke="#8A6A4A" stroke-width="1.2"></path>' for k in (0, 1) for j in range(3)) + '</g>')

RIGHT8 = ["MATTITHIAH", "SHEMA", "ANAIAH", "URIAH", "HILKIAH", "MAASEIAH"]
LEFT8 = ["PEDAIAH", "MISHAEL", "MALCHIJAH", "HASHUM", "HASHBADDANAH", "ZECHARIAH", "MESHULLAM"]

def pulpit(p, w, h, seed, names=False, crowd=True, read=True):
    """Ezra upon the pulpit of wood which they had made for the purpose, before the broad place at the water gate, the book
    open, six men beside him on his right hand and seven on his left (names=True: their names beside them), the people
    standing."""
    b = h * 0.96
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#FFE6B0", "#F3E8C8"), J.jericho(-10, w + 10, h * 0.16, h * 0.4, seed, color=STONE, towers=2, houses=False),
         S4b.gatehouse(w * 0.5, h * 0.4, w * 0.2, h * 0.3), ground(w, h, h * 0.4, "#D8C8A0", dy=0)]
    pw, ph_ = w * 0.3, h * 0.14                                 # the pulpit: a broad raised platform of wood
    px, py = w * 0.5, h * 0.66
    o.append(f'<rect x="{f(px - pw)}" y="{f(py)}" width="{f(pw * 2)}" height="{f(ph_)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             + "".join(f'<path d="M{f(px - pw)} {f(py + ph_ * k / 3)} L {f(px + pw)} {f(py + ph_ * k / 3)}" stroke="#5A3A1E" stroke-width="1.6"></path>' for k in range(1, 3))
             + f'<rect x="{f(px - pw * 1.03)}" y="{f(py - 6)}" width="{f(pw * 2.06)}" height="8" fill="#B5793A" stroke="#0D0D0F" stroke-width="2"></rect>')
    s = fit(py, py - h * 0.42)
    up = [(22, -158), (40, -186), (44, -214)] if read else None
    o.append(ezra_fig(p, px, py, s, up=up))
    if read: o.append(book_open(px + 44 * s, py - 222 * s, s * 0.9))
    k = s * 0.66
    for i in range(6):                                          # Ezra's right hand is the viewer's left
        o.append(man(p, px - pw * 0.24 - i * pw * 0.13, py, k, ("#3A4A6A", "#5A4A3A", "#4A5A3A", "#6A3A2A", "#3A3A5A", "#5A5A3A")[i], flip=True))
    for i in range(7):
        o.append(man(p, px + pw * 0.24 + i * pw * 0.115, py, k, ("#5A3A5A", "#3A5A5A", "#6A5A3A", "#3A4A6A", "#5A4A3A", "#4A3A5A", "#6A4A3A")[i]))
    if names:
        for i, nm in enumerate(RIGHT8): o.append(label(px - pw * 0.24 - i * pw * 0.13, py + ph_ * (0.42 + (i % 2) * 0.36), nm, GOLD, 7.5, ls=0.04))
        for i, nm in enumerate(LEFT8): o.append(label(px + pw * 0.24 + i * pw * 0.115, py + ph_ * (0.42 + (i % 2) * 0.36), nm, GOLD, 7.5, ls=0.04))
    if crowd:
        o.append(crowd_at(p, w, h, seed, w * 0.0, w * 0.2, h * 0.78, b, 6, s * 0.7, s * 1.0))
        o.append(crowd_at(p, w, h, seed + 1, w * 0.8, w * 1.0, h * 0.78, b, 6, s * 0.7, s * 1.0, flip=True))
    return "".join(o)

def amen(p, w, h, seed):
    """All the people answered, Amen, Amen, with the lifting up of their hands; and they bowed their heads and worshipped
    with their faces to the ground."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#FFE6B0", "#F3E8C8"), J.jericho(-10, w + 10, h * 0.2, h * 0.44, seed, color=STONE, towers=2, houses=False), ground(w, h, h * 0.44, "#D8C8A0", dy=0)]
    s = fit(b, max(h * 0.4, b - 220))
    raise2 = [(-22, -158), (-40, -190), (-50, -224)]
    cl = ("#5A4A3A", "#3A4A6A", "#6A3A2A", "#4A5A3A", "#5A3A5A")
    for i in range(5):
        x = w * (0.05 + i * 0.09)
        o.append(man(p, x, b - (i % 2) * 6, s * 0.95, cl[i], up=raise2) if i % 2 == 0 else woman(p, x, b - 6, s * 0.9, ("#C2456A", "#2E6B8A")[i // 2 % 2], up=raise2))
    for i in range(4):
        o.append(N.prostrate(w * (0.5 + i * 0.12), b - (i % 2) * 8, s * 0.95, color=cl[i], skin="#9A6A4A"))
    return "".join(o)

def branches(w, h, seed):
    """Olive branches, and branches of wild olive, and myrtle, and palm, and branches of thick trees: the five kinds laid
    out as a plate, each labelled."""
    o = [bp(w, h)]
    kinds = [("OLIVE", "#7A9A4A", "#C8D8A0"), ("WILD OLIVE", "#5A7A3A", "#9AB06A"), ("MYRTLE", "#2E6B3A", "#5A9A5A"), ("PALM", "#3A7A3A", "#9CCB5E"), ("THICK TREES", "#1F4A34", "#3F8A44")]
    for i, (nm, dark, light) in enumerate(kinds):
        cx = w * (0.1 + i * 0.2); base, top = h * 0.82, h * 0.12
        o.append(f'<path d="M{f(cx)} {f(base)} C {f(cx - 6)} {f((base + top) / 2)} {f(cx + 6)} {f(top + h * 0.1)} {f(cx)} {f(top)}" stroke="#8A6A3A" stroke-width="3" fill="none"></path>')
        r = random.Random(seed + i)
        if nm == "PALM":
            for k in range(14):
                y = top + k * (base - top) * 0.05; L = w * 0.06 * (1 - k * 0.03)
                for sg in (-1, 1):
                    o.append(f'<path d="M{f(cx)} {f(y)} Q {f(cx + sg * L * 0.6)} {f(y - 4)} {f(cx + sg * L)} {f(y + 10)}" stroke="{light}" stroke-width="2.4" fill="none"></path>')
        else:
            for k in range(16 if nm != "THICK TREES" else 24):
                y = r.uniform(top + h * 0.02, base - h * 0.12); sg = r.choice((-1, 1)); lx = cx + sg * r.uniform(4, w * 0.05)
                rx, ry = (w * 0.016, h * 0.012) if nm != "THICK TREES" else (w * 0.022, h * 0.022)
                o.append(f'<ellipse cx="{f(lx)}" cy="{f(y)}" rx="{f(rx)}" ry="{f(ry)}" fill="{r.choice((dark, light))}" stroke="#0D0D0F" stroke-width="1" transform="rotate({f(sg * 30)} {f(lx)} {f(y)})"></ellipse>')
        o.append(label(cx, h * 0.93, nm, "#8FD0E2", 9))
    return "".join(o)

def booth(x, base, wd, ht, seed):
    """A booth of branches: four poles of new wood, a thick roof of leafy boughs with fronds hanging down at the front."""
    r = random.Random(seed)
    o = [f'<rect x="{f(x - wd / 2)}" y="{f(base - ht)}" width="{f(wd)}" height="{f(ht)}" fill="#3A5A2A" opacity="0.35"></rect>']
    for dx in (-0.5, -0.3, 0.3, 0.5):
        o.append(f'<path d="M{f(x + dx * wd)} {f(base)} L {f(x + dx * wd)} {f(base - ht)}" stroke="#6A4A2A" stroke-width="{f(max(2.4, wd * 0.035))}"></path>')
    rt = ht * 0.3
    o.append(f'<rect x="{f(x - wd * 0.58)}" y="{f(base - ht - rt * 0.6)}" width="{f(wd * 1.16)}" height="{f(rt)}" rx="{f(rt * 0.4)}" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="1.8"></rect>')
    for _ in range(int(wd / 5) + 6):
        cx, cy = r.uniform(x - wd * 0.56, x + wd * 0.56), base - ht - rt * 0.6 + r.uniform(0, rt)
        o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(wd * 0.07)}" ry="{f(rt * 0.22)}" fill="{r.choice(("#3F8A44", "#5E8F26", "#9CCB5E", "#7A9A4A"))}" stroke="#0D0D0F" stroke-width="1" transform="rotate({f(r.uniform(-40, 40))} {f(cx)} {f(cy)})"></ellipse>')
    for k in range(int(wd / 14) + 2):
        fx = x - wd * 0.5 + k * wd / (int(wd / 14) + 1)
        o.append(f'<path d="M{f(fx)} {f(base - ht + rt * 0.3)} q {f(wd * 0.02)} {f(ht * 0.14)} {f(-wd * 0.01)} {f(ht * 0.24)}" stroke="#5E8F26" stroke-width="2.4" fill="none"></path>')
    return "".join(o)

def booths(p, w, h, seed):
    """Booths every one upon the roof of his house, and in their courts, and in the broad place of the water gate: a family
    sitting under one in the foreground."""
    r = random.Random(seed); b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.3, seed, "#9AAA6A", amp=10, step=90)]
    for i in range(5):                                        # flat-roofed houses with a booth on each roof
        x = w * (0.42 + i * 0.12); top = h * r.uniform(0.4, 0.48); wd = w * 0.11
        o.append(f'<rect x="{f(x)}" y="{f(top)}" width="{f(wd)}" height="{f(h * 0.7 - top)}" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<rect x="{f(x + wd * 0.4)}" y="{f(h * 0.58)}" width="{f(wd * 0.2)}" height="{f(h * 0.12)}" fill="#3A2214"></rect>' + booth(x + wd / 2, top, wd * 0.8, h * 0.13, seed + i))
    o.append(ground(w, h, h * 0.7, "#D8C8A0", dy=0))
    s = fit(b, max(h * 0.4, b - 220))
    bx, bw = w * 0.2, w * 0.34
    o.append(booth(bx, b, bw, 230 * s, seed + 10))
    for i, (c, k) in enumerate((("#3A4A6A", 1.0), ("#C2456A", 0.94), ("#E8D8B0", 0.55))):
        x = bx - bw * 0.3 + i * bw * 0.28
        o.append(man(p, x, b, s * k, c) if i != 1 else woman(p, x, b, s * k, c))
    return "".join(o)

def fasting(p, w, h, seed):
    """The children of Israel assembled with fasting, and with sackcloth, and earth upon them: figures kneeling in
    sackcloth, dust upon their heads, before the house of God."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#6A6A7A", "#C8B8A0"), K1.temple_front(w * 0.5, h * 0.56, w * 0.36, seed), ground(w, h, h * 0.56, "#A89A7A", dy=0)]
    s = fit(b, max(h * 0.4, b - 220))
    r = random.Random(seed)
    for i in range(7):
        x = w * (0.06 + i * 0.145)
        o.append(E.kneel(x, b - (i % 2) * 6, s * 0.7, color="#6A5A44", skin="#9A6A4A", flip=i >= 4))
        for _ in range(5):
            o.append(f'<circle cx="{f(x + r.uniform(-16, 16) * s + (0 if i < 4 else -20 * s))}" cy="{f(b - r.uniform(120, 170) * s * 0.7)}" r="{f(r.uniform(1.4, 2.6))}" fill="#7A6A54"></circle>')
    return "".join(o)

def stairs(p, w, h, seed):
    """The Levites standing up upon the stairs, crying with a loud voice unto Jehovah their God."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), K1.temple_front(w * 0.5, h * 0.42, w * 0.44, seed), ground(w, h, h * 0.42, "#C8B88A", dy=0)]
    for k in range(5):
        y0 = h * 0.44 + k * h * 0.11; x0 = w * (0.2 - k * 0.03); x1 = w * (0.8 + k * 0.03)
        o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(x1 - x0)}" height="{f(h * 0.11)}" fill="#D8CCB0" stroke="#0D0D0F" stroke-width="2"></rect>')
    y = h * 0.55
    s = fit(y, h * 0.2)
    for i in range(8):
        o.append(K1.priest(p, w * (0.26 + i * 0.068), y, s, up=[(-22, -158), (-36, -190), (-44, -222)] if i % 2 else [(22, -158), (36, -190), (44, -222)]))
    return "".join(o)

def heavens(w, h, seed):
    """Thou hast made heaven, the heaven of heavens, with all their host, the earth and the seas."""
    return "".join([K2.sky(w, h, "#0B0B2A", "#5B2470"), mk.stars(140, w, h * 0.7, seed), mk.stars(30, w, h * 0.6, seed + 1, color="#FFE680"),
                    V.rays(w * 0.5, -h * 0.2, 30, 30, max(w, h) * 1.4, color="#FFF4C2", op=0.12),
                    f'<path d="M-10 {f(h * 0.8)} Q {f(w * 0.5)} {f(h * 0.6)} {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1F6F9A" stroke="#0D0D0F" stroke-width="2"></path>',
                    f'<path d="M{f(w * 0.12)} {f(h * 0.76)} Q {f(w * 0.4)} {f(h * 0.62)} {f(w * 0.62)} {f(h * 0.68)} L {f(w * 0.66)} {f(h + 10)} L {f(w * 0.1)} {f(h + 10)} Z" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="2"></path>'])

def abram_stars(p, w, h, seed):
    """Abram brought forth out of Ur of the Chaldees: a lone figure on a hill under the stars."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#0B0B2A", "#3A2A5A"), mk.stars(110, w, h * 0.7, seed), hills(w, h, h * 0.8, seed, "#1A1430", amp=10, step=80)]
    s = fit(h * 0.86, h * 0.12)
    o.append(mk.person(p, round(w * 0.3), round(h * 0.86), round(s, 3), body="#2A1A14", cloth="#3A4A6A", kind="Robe", sw=3, up=[(-22, -158), (-40, -190), (-50, -222)],
                       extra=A.headcloth("#3A4A6A") + A.WHITE_BEARD))
    return "".join(o)

def red_sea(w, h, seed):
    """Thou didst divide the sea before them, so that they went through the midst of the sea on the dry land."""
    return E3.sea_corridor(w, h, (w * 0.5, h * 0.36), w * 0.24, w * 0.76, seed, uid=f"rs{seed}")

def pillars(w, h, seed):
    """In a pillar of cloud by day, and in a pillar of fire by night: the cloud and the fire over the camp, the tents below."""
    o = [K2.sky(w, h, "#2A2A5A", "#E8A06A"), ground(w, h, h * 0.76, "#B89A6A", dy=0),
         E3.pillar_cloud(w * 0.3, h * 0.76, h * 0.04, w * 0.08, seed), E3.pillar_fire(w * 0.72, h * 0.76, h * 0.04, w * 0.06, seed)]
    for i in range(9):
        o.append(E4.tent(w * (0.06 + i * 0.11), h * (0.88 + (i % 2) * 0.06), w * 0.08, h * 0.1, color=("#5A3A22", "#6B4A2A", "#3A2214")[i % 3]))
    return "".join(o)

def sinai_scene(w, h, seed):
    """Thou camest down also upon mount Sinai, and spakest with them from heaven: the mountain on fire, the two tables."""
    return "".join([K2.sky(w, h, "#2A1A2A", "#8A3A2A"), E4.sinai(w * 0.46, h * 0.98, w * 0.7, h * 0.72, seed), V.tables(w * 0.86, h * 0.94, min(0.6, h / 400), uid=f"tb{seed}")])

def manna_rock(w, h, seed):
    """Bread from heaven for their hunger, and water out of the rock for their thirst."""
    return "".join([K2.sky(w, h, "#FFC890", "#F3E8C8"), ground(w, h, h * 0.66, "#D8C08A", dy=0), E4.manna(160, 0, w * 0.56, h * 0.7, h * 0.98, seed),
                    E4.rock(w * 0.62, h * 0.96, w * 0.32, h * 0.6), E4.gush(w * 0.7, h * 0.56, seed, scale=min(1.0, h / 300))])

def calf_scene(w, h, seed):
    """They had made them a molten calf: the gold calf on its pedestal in the camp."""
    return "".join([K2.sky(w, h, "#5A2A1A", "#E8A06A"), ground(w, h, h * 0.8, "#A88A5A", dy=0), V.calf(w * 0.5, h * 0.92, min(1.2, h / 220), uid=f"cf{seed}"),
                    E4.tent(w * 0.12, h * 0.9, w * 0.14, h * 0.18), E4.tent(w * 0.86, h * 0.9, w * 0.14, h * 0.18, color="#6B4A2A")])

def good_land(w, h, seed):
    """Fortified cities, and a fat land, cisterns hewn out, vineyards, and oliveyards, and fruit-trees in abundance."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.36, seed, "#8AA05A", amp=12, step=90), J.city_hill(w * 0.72, h * 0.48, w * 0.24, h * 0.18, seed),
         ground(w, h, h * 0.5, "#9CCB5E", dy=0)]
    for row in range(3):                                      # vineyard rows
        y = h * (0.62 + row * 0.1)
        o.append(f'<path d="M{f(w * 0.04)} {f(y)} L {f(w * 0.46)} {f(y)}" stroke="#6A4A2A" stroke-width="2"></path>')
        for k in range(10):
            cx = w * (0.06 + k * 0.042)
            o.append(f'<circle cx="{f(cx)}" cy="{f(y - 8)}" r="{f(min(w, h) * 0.022)}" fill="{r.choice(("#2E6B3A", "#3F8A44"))}" stroke="#0D0D0F" stroke-width="1.2"></circle>'
                     + (f'<circle cx="{f(cx + 4)}" cy="{f(y - 2)}" r="3" fill="#6A2A6A"></circle>' if k % 2 else ""))
    for k in range(5):                                        # olive trees
        x = w * (0.56 + k * 0.09); y = h * 0.86
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - h * 0.12)}" stroke="#5A4A3A" stroke-width="4"></path>'
                 f'<ellipse cx="{f(x)}" cy="{f(y - h * 0.16)}" rx="{f(w * 0.04)}" ry="{f(h * 0.06)}" fill="#8AA06A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.95)}" rx="{f(w * 0.05)}" ry="{f(h * 0.025)}" fill="#2C5A7A" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    return "".join(o)

def servants(p, w, h, seed):
    """We are servants this day in the land: men bowed at the harvest, the grain in sacks for the kings, an overseer with
    a spear."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#C8A890", "#F3E0B0"), hills(w, h, h * 0.44, seed, "#A89A6A", amp=10, step=90), ground(w, h, h * 0.62, "#D8C08A", dy=0)]
    s = fit(b, max(h * 0.4, b - 220))
    for i in range(3):
        o.append(E.kneel(w * (0.08 + i * 0.14), b, s * 0.7, color="#6A5A44", skin="#9A6A4A"))
    for i in range(3): o.append(R1.sack(w * (0.52 + i * 0.06), b, s * 0.8))
    o.append(warrior(p, w * 0.86, b, s, "#5A1A6A", flip=True))
    return "".join(o)

def sealed_scroll(w, h, seed, n=7):
    """A sure covenant, written and sealed: a scroll, a row of clay seals hanging from its foot."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A2A"></rect>', V.rays(w * 0.5, h * 0.5, 24, 12, max(w, h), color="#E8C88A", op=0.1)]
    x0, x1, y0, y1 = w * 0.16, w * 0.84, h * 0.08, h * 0.74
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(x1 - x0)}" height="{f(y1 - y0)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    for k in range(6):
        y = y0 + (k + 1) * (y1 - y0) * 0.13
        o.append(f'<path d="M{f(x0 + w * 0.04)} {f(y)} L {f(x1 - w * (0.04 + (k == 5) * 0.2))} {f(y)}" stroke="#8A6A4A" stroke-width="2"></path>')
    for i in range(n):
        x = x0 + (i + 0.5) * (x1 - x0) / n
        o.append(f'<path d="M{f(x)} {f(y1)} L {f(x)} {f(y1 + h * 0.08)}" stroke="#7A2A6A" stroke-width="2"></path>'
                 f'<circle cx="{f(x)}" cy="{f(y1 + h * 0.12)}" r="{f(min(w / n * 0.3, h * 0.05))}" fill="#B5121B" stroke="#0D0D0F" stroke-width="1.8"></circle>')
    return "".join(o)

# ---- Nehemiah 10–11 -----------------------------------------------------------------------------------------------------
def sealing(p, w, h, seed):
    """They that sealed the covenant: the written covenant on a table, Nehemiah the governor pressing his seal, the priests
    and chiefs waiting their turn."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#C8A890", "#F3E0B0"), K1.temple_front(w * 0.74, h * 0.6, w * 0.36, seed), ground(w, h, h * 0.6, "#C8B88A", dy=0)]
    tx, ty = w * 0.42, h * 0.78
    o.append(f'<rect x="{f(tx - w * 0.12)}" y="{f(ty)}" width="{f(w * 0.24)}" height="{f(h * 0.05)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<path d="M{f(tx - w * 0.1)} {f(b)} L {f(tx - w * 0.1)} {f(ty + h * 0.05)} M{f(tx + w * 0.1)} {f(b)} L {f(tx + w * 0.1)} {f(ty + h * 0.05)}" stroke="#5A3A1E" stroke-width="4"></path>'
             f'<rect x="{f(tx - w * 0.08)}" y="{f(ty - h * 0.02)}" width="{f(w * 0.16)}" height="{f(h * 0.025)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.6"></rect>'
             + "".join(f'<circle cx="{f(tx - w * 0.06 + k * w * 0.03)}" cy="{f(ty - h * 0.008)}" r="{f(min(w, h) * 0.012)}" fill="#B5121B" stroke="#0D0D0F" stroke-width="1"></circle>' for k in range(4)))
    s = fit(b, max(h * 0.4, b - 220))
    o.append(neh_fig(p, tx - w * 0.18, b, s, up=[(22, -158), (50, -150), (70, -130)]))
    for i in range(3): o.append(K1.priest(p, w * (0.66 + i * 0.08), b, s * 0.96, flip=True))
    for i in range(2): o.append(noble(p, w * (0.06 + i * 0.08), b, s * 0.96, NOBLE_C[i]))
    return "".join(o)

def shekel(w, h):
    """The third part of a shekel yearly for the service of the house: a shekel drawn as a coin divided in three, one part
    lit, with the things it buys listed as tags."""
    o = [bp(w, h)]
    cx, cy, r = w * 0.24, h * 0.52, min(w * 0.16, h * 0.36)
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="none" stroke="#8FD0E2" stroke-width="2.4"></circle>')
    a0, a1 = math.radians(-90), math.radians(30)
    o.append(f'<path d="M{f(cx)} {f(cy)} L {f(cx + r * math.cos(a0))} {f(cy + r * math.sin(a0))} A {f(r)} {f(r)} 0 0 1 {f(cx + r * math.cos(a1))} {f(cy + r * math.sin(a1))} Z" fill="#FFD23F" fill-opacity="0.45" stroke="#FFD23F" stroke-width="2.4"></path>')
    for a in (-90, 30, 150):
        o.append(f'<path d="M{f(cx)} {f(cy)} L {f(cx + r * math.cos(math.radians(a)))} {f(cy + r * math.sin(math.radians(a)))}" stroke="#8FD0E2" stroke-width="1.6"></path>')
    o.append(label(cx, cy + r + 18, "THE THIRD PART OF A SHEKEL", "#FFD23F", 10))
    items = ["THE SHOWBREAD", "THE CONTINUAL MEAL-OFFERING", "THE CONTINUAL BURNT-OFFERING", "SABBATHS · NEW MOONS · SET FEASTS", "THE HOLY THINGS", "THE SIN-OFFERINGS"]
    for i, t in enumerate(items):
        y = h * (0.16 + i * 0.13)
        o.append(f'<path d="M{f(cx + r + 8)} {f(cy)} L {f(w * 0.5)} {f(y)} L {f(w * 0.53)} {f(y)}" fill="none" stroke="#4A7A9A" stroke-width="1.4"></path>'
                 + label(w * 0.54, y + 4, t, "#8FD0E2", 9, "start"))
    return "".join(o)

def wood_bearers(p, w, h, seed):
    """The wood-offering brought into the house of God at times appointed, by lot, house by house: men bearing bundles of
    wood up to the altar, the fire burning."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), K1.temple_front(w * 0.7, h * 0.56, w * 0.4, seed), ground(w, h, h * 0.56, "#C8B88A", dy=0),
         K1.horned_altar(w * 0.7, h * 0.86, min(0.8, h / 380), fire=True, seed=seed)]
    s = fit(b, max(h * 0.4, b - 220))
    for i in range(4):
        x = w * (0.08 + i * 0.12)
        o.append(man(p, x, b - (i % 2) * 5, s * 0.95, WAR[i % 4], up=[(22, -158), (30, -190), (14, -214)]))
        bx, by = x + 14 * s, b - (i % 2) * 5 - 222 * s
        o.append("".join(f'<rect x="{f(bx - 34 * s)}" y="{f(by - k * 7 * s)}" width="{f(68 * s)}" height="{f(7 * s)}" rx="{f(3 * s)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.2"></rect>' for k in range(3)))
    return "".join(o)

def firstfruits(p, w, h, seed):
    """The first-fruits of the ground and of every tree, the firstlings of herd and flock, the first of the dough, the new
    wine and the oil, brought to the priests at the chambers of the house."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#FFC890", "#F3E8C8"), K1.temple_front(w * 0.78, h * 0.58, w * 0.34, seed), ground(w, h, h * 0.58, "#C8B88A", dy=0)]
    s = fit(b, max(h * 0.4, b - 220))
    o.append(K1.priest(p, w * 0.66, b, s, flip=True))
    o.append(R1.sheaf(w * 0.12, b, s * 1.2) + R1.sheaf(w * 0.17, b, s * 1.1))
    for i, c in enumerate(("#B5121B", "#E8B830", "#6A2A6A")):
        x = w * (0.26 + i * 0.06)
        o.append(E4.basket(x, b, s * 1.6) + f'<circle cx="{f(x - 6 * s)}" cy="{f(b - 26 * s)}" r="{f(7 * s)}" fill="{c}" stroke="#0D0D0F" stroke-width="1"></circle>'
                 f'<circle cx="{f(x + 6 * s)}" cy="{f(b - 26 * s)}" r="{f(7 * s)}" fill="{c}" stroke="#0D0D0F" stroke-width="1"></circle>')
    o.append(E3.lamb(w * 0.48, b, s * 0.6))
    for i in range(2):
        x = w * (0.55 + i * 0.04)
        o.append(f'<path d="M{f(x - 10 * s)} {f(b)} C {f(x - 22 * s)} {f(b - 30 * s)} {f(x - 12 * s)} {f(b - 60 * s)} {f(x - 5 * s)} {f(b - 64 * s)} L {f(x + 5 * s)} {f(b - 64 * s)} '
                 f'C {f(x + 12 * s)} {f(b - 60 * s)} {f(x + 22 * s)} {f(b - 30 * s)} {f(x + 10 * s)} {f(b)} Z" fill="{("#B5652E", "#C8A060")[i]}" stroke="#0D0D0F" stroke-width="1.8"></path>')
    return "".join(o)

def sabbath_gate(p, w, h, seed, shut=True, merchants=True):
    """The gates of Jerusalem at dusk before the sabbath: the doors shut and barred, servants set over them, the merchants
    with their laden asses lodging without the wall."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#3A2A5A", "#E8906A"), sun(w * 0.86, h * 0.5, 18), hills(w, h, h * 0.5, seed, "#6A5A6A", amp=8, step=90),
         J.jericho(-10, w * 0.62, h * 0.24, h * 0.76, seed, color=STONE, towers=1, houses=True), S4b.gatehouse(w * 0.36, h * 0.76, w * 0.22, h * 0.56)]
    dx0, dx1 = w * 0.36 - w * 0.22 * 0.18, w * 0.36 + w * 0.22 * 0.18
    if shut:
        o.append(f'<rect x="{f(dx0)}" y="{f(h * 0.76 - h * 0.56 * 0.5)}" width="{f(dx1 - dx0)}" height="{f(h * 0.56 * 0.5)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<path d="M{f((dx0 + dx1) / 2)} {f(h * 0.76 - h * 0.56 * 0.5)} L {f((dx0 + dx1) / 2)} {f(h * 0.76)}" stroke="#0D0D0F" stroke-width="2"></path>'
                 f'<rect x="{f(dx0 - 4)}" y="{f(h * 0.62)}" width="{f(dx1 - dx0 + 8)}" height="8" fill="#3A2A1A" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    o.append(ground(w, h, h * 0.76, "#8A7A5A", dy=0))
    s = fit(b, max(h * 0.44, b - 220))
    o.append(warrior(p, w * 0.24, b, s * 0.9, "#3A4A6A") + warrior(p, w * 0.48, b, s * 0.9, "#4A3A3A", flip=True))
    if merchants:
        for i in range(2):
            x = w * (0.66 + i * 0.16)
            o.append(N.ass(x, b, s * 0.55, flip=True, color="#7A6A5A") + R1.sack(x - 6 * s, b - 66 * s, s * 0.7)
                     + man(p, x + 40 * s, b, s * 0.9, ("#7A3A1E", "#2A5A6A")[i], flip=True))
    return "".join(o)

VILL_J = [("KIRIATH-ARBA", 0.36, 0.62), ("DIBON", 0.48, 0.74), ("JEKABZEEL", 0.56, 0.84), ("JESHUA", 0.42, 0.8), ("MOLADAH", 0.4, 0.88), ("BETH-PELET", 0.3, 0.86),
          ("HAZAR-SHUAL", 0.24, 0.9), ("BEER-SHEBA", 0.32, 0.95), ("ZIKLAG", 0.16, 0.84), ("MECONAH", 0.22, 0.78), ("EN-RIMMON", 0.28, 0.74), ("ZORAH", 0.2, 0.42),
          ("JARMUTH", 0.18, 0.5), ("ZANOAH", 0.28, 0.46), ("ADULLAM", 0.26, 0.54), ("LACHISH", 0.12, 0.62), ("AZEKAH", 0.14, 0.4)]
VILL_B = [("GEBA", 0.56, 0.2), ("MICHMASH", 0.62, 0.16), ("AIJA", 0.6, 0.1), ("BETH-EL", 0.52, 0.06), ("ANATHOTH", 0.58, 0.28), ("NOB", 0.5, 0.3), ("ANANIAH", 0.54, 0.34),
          ("HAZOR", 0.44, 0.18), ("RAMAH", 0.48, 0.22), ("GITTAIM", 0.3, 0.2), ("HADID", 0.24, 0.14), ("ZEBOIM", 0.68, 0.24), ("NEBALLAT", 0.28, 0.1), ("LOD", 0.16, 0.12), ("ONO", 0.12, 0.2)]

def villages_map(w, h, judah=True, benjamin=True):
    """Where the rest dwelt: the villages of Judah from Beer-sheba unto the valley of Hinnom (gold), and of Benjamin from Geba
    onward to Lod and Ono, the valley of craftsmen (cyan), Jerusalem between."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.06)} -10 C {f(w * 0.08)} {f(h * 0.4)} {f(w * 0.05)} {f(h * 0.7)} {f(w * 0.03)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.8)} -10 C {f(w * 0.78)} {f(h * 0.3)} {f(w * 0.82)} {f(h * 0.5)} {f(w * 0.78)} {f(h * 0.62)}" stroke="#2C9DB8" stroke-width="4" fill="none"></path>'
             f'<ellipse cx="{f(w * 0.78)}" cy="{f(h * 0.78)}" rx="{f(w * 0.03)}" ry="{f(h * 0.16)}" fill="#2C9DB8"></ellipse>')
    for on, rows, col in ((judah, VILL_J, GOLD), (benjamin, VILL_B, CYAN)):
        for nm, x, y in rows:
            o.append(node(w * x, h * y, nm, col if on else "#4A5A7A", r=3.5, dy=-7, size=7.5))
    o.append(node(w * 0.5, h * 0.4, "JERUSALEM", "#FFFFFF", r=6, dy=-11, size=10) + label(w * 0.5, h * 0.47, "THE VALLEY OF HINNOM", "#FF8A6A", 7.5))
    o.append(label(w * 0.96, h * 0.9, "JUDAH", GOLD, 10, "end") + label(w * 0.96, h * 0.1, "BENJAMIN", CYAN, 10, "end"))
    return "".join(o)

# ---- Nehemiah 12–13 -----------------------------------------------------------------------------------------------------
def procession(p, w, h, seed, second=False):
    """A company that gave thanks going in procession upon the wall: priests' sons with trumpets, singers with harps and
    cymbals, the princes of Judah, walking along the top of the wall above the city (second=True: the other company, with
    Nehemiah after them, the tower of the furnaces behind)."""
    wt = h * 0.6
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#FFC890", "#FFF4C2"), hills(w, h, h * 0.4, seed, "#A8946A", amp=10, step=90)]
    if second:
        o.append(f'<rect x="{f(w * 0.78)}" y="{f(wt - h * 0.34)}" width="{f(w * 0.1)}" height="{f(h * 0.34)}" fill="#B5652E" stroke="#0D0D0F" stroke-width="2.4"></rect>'
                 + "".join(f'<rect x="{f(w * 0.78 + k * w * 0.026)}" y="{f(wt - h * 0.38)}" width="{f(w * 0.016)}" height="{f(h * 0.04)}" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></rect>' for k in range(4)))
    o.append(stone_wall(-10, w + 10, wt, h + 10, seed))
    s = fit(wt, max(h * 0.12, wt - 190))
    xs = [0.06 + i * 0.105 for i in range(9)]
    for i, x in enumerate(xs):
        X = w * x; y = wt
        if i < 3:
            o.append(J.trumpeter(p, X, y, s * 0.95))
        elif i < 6:
            o.append(S3.musician(p, X, y, s * 0.95, kind=("harp", "cymbals", "harp")[i - 3], cloth="#F3EFE6", woman=False, seed=seed + i))
        elif i == 7 and second:
            o.append(neh_fig(p, X, y, s))
        else:
            o.append(noble(p, X, y, s, NOBLE_C[i % 3]))
    return "".join(o)

def chamber_tobiah(p, w, h, seed):
    """The great chamber in the courts of the house of God, where they laid the meal-offerings, the frankincense and the
    vessels, made over to Tobiah: his couches, rugs and chests within, the stores gone."""
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#E8DCC0"></rect>']
    for k in range(int(w // 50) + 2):
        o.append(f'<path d="M{f(k * 50)} -10 L {f(k * 50)} {f(h * 0.8)}" stroke="#D8CCB0" stroke-width="3"></path>')
    o.append(ground(w, h, h * 0.8, "#B8A07A", dy=0))
    o.append(f'<rect x="{f(w * 0.08)}" y="{f(h * 0.62)}" width="{f(w * 0.3)}" height="{f(h * 0.12)}" rx="6" fill="#2E5A4A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<rect x="{f(w * 0.06)}" y="{f(h * 0.5)}" width="{f(w * 0.05)}" height="{f(h * 0.26)}" rx="6" fill="#1F4A34" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.08)} {f(h * 0.74)} L {f(w * 0.08)} {f(h * 0.8)} M{f(w * 0.36)} {f(h * 0.74)} L {f(w * 0.36)} {f(h * 0.8)}" stroke="#5A3A1E" stroke-width="4"></path>')
    o.append(f'<ellipse cx="{f(w * 0.56)}" cy="{f(h * 0.88)}" rx="{f(w * 0.16)}" ry="{f(h * 0.05)}" fill="#7A2A3A" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    for i in range(3):
        x = w * (0.72 + i * 0.08)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.62)}" width="{f(w * 0.07)}" height="{f(h * 0.18)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<rect x="{f(x)}" y="{f(h * 0.62)}" width="{f(w * 0.07)}" height="{f(h * 0.04)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    o.append(f'<path d="M{f(w * 0.46)} {f(h * 0.3)} L {f(w * 0.66)} {f(h * 0.3)}" stroke="#8A6A3A" stroke-width="3"></path>'
             + "".join(f'<path d="M{f(w * (0.48 + k * 0.04))} {f(h * 0.3)} l 0 {f(h * 0.1)}" stroke="#1F4A34" stroke-width="4"></path>' for k in range(5)))
    return "".join(o)

def cast_out(p, w, h, seed):
    """All the household stuff of Tobiah cast forth out of the chamber: the couch, the chests and the rugs in the court,
    Nehemiah at the door."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), stone_wall(w * 0.5, w + 10, h * 0.16, h * 0.7, seed),
         f'<rect x="{f(w * 0.66)}" y="{f(h * 0.36)}" width="{f(w * 0.12)}" height="{f(h * 0.34)}" fill="#2A1A14" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         ground(w, h, h * 0.7, "#C8B88A", dy=0)]
    o.append(f'<g transform="rotate(-14 {f(w * 0.3)} {f(h * 0.86)})"><rect x="{f(w * 0.18)}" y="{f(h * 0.8)}" width="{f(w * 0.24)}" height="{f(h * 0.08)}" rx="6" fill="#2E5A4A" stroke="#0D0D0F" stroke-width="2"></rect></g>'
             f'<g transform="rotate(20 {f(w * 0.08)} {f(h * 0.86)})"><rect x="{f(w * 0.04)}" y="{f(h * 0.78)}" width="{f(w * 0.07)}" height="{f(h * 0.12)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect></g>'
             f'<path d="M{f(w * 0.42)} {f(h * 0.92)} q {f(w * 0.06)} {f(-h * 0.08)} {f(w * 0.14)} {f(-h * 0.02)} l {f(-w * 0.02)} {f(h * 0.06)} Z" fill="#7A2A3A" stroke="#0D0D0F" stroke-width="2"></path>')
    s = fit(b, max(h * 0.36, b - 230))
    o.append(neh_fig(p, w * 0.6, b, s, flip=True, up=[(22, -158), (48, -166), (74, -172)], cloth="#3A4A6A"))
    return "".join(o)

def sabbath_work(p, w, h, seed):
    """On the sabbath, men treading winepresses and bringing in sheaves, lading asses with wine, grapes and figs; men of
    Tyre selling fish at the gate."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), J.jericho(w * 0.56, w + 10, h * 0.3, h * 0.66, seed, color=STONE, towers=1, houses=True),
         S4b.gatehouse(w * 0.78, h * 0.66, w * 0.18, h * 0.44), ground(w, h, h * 0.66, "#C8B07A", dy=0), J1.winepress(w * 0.16, h * 0.86, w * 0.2, h * 0.1)]
    s = fit(b, max(h * 0.4, b - 220))
    o.append(man(p, w * 0.16, h * 0.84, s * 0.8, "#6A3A2A", up=[(-22, -158), (-36, -180), (-30, -200)]))
    o.append(N.ass(w * 0.38, b, s * 0.6, color="#7A6A5A") + R1.sheaf(w * 0.36, b - 64 * s, s * 0.7) + R1.sack(w * 0.42, b - 60 * s, s * 0.5))
    o.append(R1.sheaf(w * 0.5, b, s) + R1.sheaf(w * 0.53, b, s * 0.9))
    o.append(man(p, w * 0.66, b, s * 0.9, "#2A5A6A", flip=True))
    for k in range(3):
        fx = w * (0.58 + k * 0.03); fy = b - h * 0.02
        o.append(f'<path d="M{f(fx - 12)} {f(fy)} q 10 -8 20 0 l 6 -5 l 0 10 l -6 -5 q -10 8 -20 0 Z" fill="#8FA8B8" stroke="#0D0D0F" stroke-width="1.2"></path>')
    return "".join(o)

def strange_wives(p, w, h, seed):
    """Jews that had married women of Ashdod, of Ammon and of Moab: mothers in foreign dress with their children before
    the houses, the children speaking half in the speech of Ashdod."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#C8B8A0", "#F3E0B0"), J.jericho(-10, w + 10, h * 0.3, h * 0.62, seed, color=STONE, towers=0, houses=True), ground(w, h, h * 0.62, "#C8B07A", dy=0)]
    s = fit(b, max(h * 0.26, b - 260))
    for i, c in enumerate(("#7A1A5A", "#1A5A7A", "#7A5A1A")):
        x = w * (0.18 + i * 0.3)
        o.append(woman(p, x, b, s, c) + man(p, x + 36 * s, b, s * 0.55, "#E8D8B0") + man(p, x - 34 * s, b, s * 0.5, "#C8D8E8"))
    return "".join(o)

def departing(p, w, h, seed):
    """Chased from me: a lone figure in a priest's white robe going away down the road from the city at dusk."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#3A2A4A", "#E8906A"), J.city_hill(w * 0.2, h * 0.6, w * 0.3, h * 0.24, seed), ground(w, h, h * 0.6, "#8A7A5A", dy=0),
         f'<path d="M{f(w * 0.3)} {f(h * 0.62)} C {f(w * 0.5)} {f(h * 0.7)} {f(w * 0.6)} {f(h * 0.86)} {f(w * 0.9)} {f(h + 10)}" stroke="#B8A07A" stroke-width="{f(w * 0.05)}" fill="none"></path>']
    y = h * 0.8
    o.append(K1.priest(p, w * 0.66, y, fit(y, y - h * 0.4), flip=False))
    return "".join(o)

def heaps(p, w, h, seed):
    """The heaps of the grain, the new wine and the oil brought into the chambers of the house of God, a Levite in white
    standing by as treasurer (no king in Nehemiah's Jerusalem)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FD0E2", "#F3E8C8"), K1.temple_front(w * 0.5, h * 0.56, w * 0.5, seed), ground(w, h, h * 0.56, "#C8B88A", dy=0)]
    for i, c in enumerate(("#E8C88A", "#C8A060", "#D9A25A", "#E8D8A0")):
        o.append(R1.heap(w * (0.24 + i * 0.18), h * 0.86, w * 0.14, h * 0.16, color=c))
    s = fit(b, max(h * 0.42, b - 230))
    o.append(K1.priest(p, w * 0.08, b, s))
    for i in range(2):
        x = w * (0.9 + i * 0.05)
        o.append(f'<path d="M{f(x - 10 * s)} {f(b)} C {f(x - 22 * s)} {f(b - 30 * s)} {f(x - 12 * s)} {f(b - 60 * s)} {f(x - 5 * s)} {f(b - 64 * s)} L {f(x + 5 * s)} {f(b - 64 * s)} '
                 f'C {f(x + 12 * s)} {f(b - 60 * s)} {f(x + 22 * s)} {f(b - 30 * s)} {f(x + 10 * s)} {f(b)} Z" fill="{("#B5652E", "#C8A060")[i]}" stroke="#0D0D0F" stroke-width="1.8"></path>')
    return "".join(o)

def musicians_court(p, w, h, seed):
    """The singers and Levites with cymbals, psalteries and harps, and the priests with trumpets, before the house of God."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#FFB04A", "#FFE6B0"), K1.temple_front(w * 0.5, h * 0.56, w * 0.46, seed), ground(w, h, h * 0.56, "#C8B88A", dy=0)]
    s = fit(b, max(h * 0.38, b - 230))
    for i in range(8):
        x = w * (0.06 + i * 0.125)
        if i in (0, 7):
            o.append(J.trumpeter(p, x, b, s * 0.95, flip=i == 7))
        else:
            o.append(S3.musician(p, x, b - (i % 2) * 5, s * 0.95, kind=("harp", "cymbals")[i % 2], cloth="#F3EFE6", woman=False, seed=seed + i))
    return "".join(o)
