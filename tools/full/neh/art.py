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
EXTRA = {"JACKAL'S WELL": (0.78, 0.92), "KING'S POOL": (0.95, 0.24), "STAIRS OF THE CITY OF DAVID": (0.76, 0.34), "GATE OF THE GUARD": (0.26, 0.3)}

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
        o.append(node(*P["GATE OF THE GUARD"], "GATE OF THE GUARD", "#FF8A6A", r=4, dy=16, size=8))
        o.append(label(w * 0.8, h * 0.72, "THE FIRST COMPANY", GOLD, 9) + label(w * 0.36, h * 0.74, "THE OTHER COMPANY", "#FF8A6A", 9))
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
