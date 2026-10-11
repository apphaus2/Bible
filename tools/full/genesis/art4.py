"""New drawings for Genesis chapter 4 (Genesis 16–19): Hagar and Ishmael, the covenant and the new names,
the three men at Mamre, Abraham pleading for Sodom, the night at Lot's door, the flight to Zoar and the cave."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3, exodus4 as E4, exodus5 as V, joshua1 as J, judges1 as G1, judges2 as S
import samuel1 as A, samuel2 as A2, samuel3 as A3, samuel4 as A4, numbers1 as N, ruth1 as R
from faces_ex import F
from genesis import art2 as Y, art3 as Z
from genesis.art2 import fit, ground, hills, birds, city, SKIN
from genesis.art3 import sun, label, man, woman, abram, sarai, lot, grid_bg, node, route, STAFF, HOLD_STAFF, GREY_BEARD, CROWN
def f(v): return f"{v:.1f}"

# ---- faces ----------------------------------------------------------------------------------------------
ABRAHAM, ABRAHAM_GRAVE, ABRAHAM_BOLD = Z.ABRAM, Z.ABRAM_GRAVE, Z.ABRAM_BOLD
ABRAHAM_AWE = F("adam", skin="#E3B08A", shadow="#8A5A3E", hair="#C8C2B6", hl="#8A867E", beard=True, light="#FFF4C2")
ABRAHAM_LAUGH = F("adam", skin="#D9A27A", shadow="#8A5A3E", hair="#C8C2B6", hl="#8A867E", beard=True, laugh=True, light="#FFE680")
ABRAHAM_PLEAD = F("adam", skin="#C98E66", shadow="#5A3A4A", hair="#C8C2B6", hl="#8A867E", beard=True, brow="sorrow", sweat=True, light="#FF8A3D")
SARAI_HURT = F("eve", skin="#C99A84", shadow="#6A3A3A", hair="#3A2A1E", scarf="#8A3A5A", light="#FF6A4A")
SARAH = F("eve", skin="#D9A684", shadow="#9A6A5A", hair="#C8C2B6", scarf="#8A3A5A", light="#FFE680")
SARAH_LAUGH = F("eve", skin="#D9A684", shadow="#9A6A5A", hair="#C8C2B6", scarf="#8A3A5A", laugh=True, light="#FFE680")
SARAH_AFRAID = F("eve", skin="#C99A84", shadow="#6A4A5A", hair="#C8C2B6", scarf="#8A3A5A", sweat=True)
HAGAR = F("eve", skin="#B9785A", shadow="#6A3A2A", hair="#0D0D0F", scarf="#2A6A9A", kohl=True, light="#FFC14D")
HAGAR_WEEP = F("eve", skin="#A8705A", shadow="#4A2A2A", hair="#0D0D0F", scarf="#2A6A9A", kohl=True, tear=True, light="#9FE0FF")
LOT, LOT_FEAR = Z.LOT, Z.LOT_TAKEN

# ---- people ---------------------------------------------------------------------------------------------
HAGAR_ROBE, SARAH_ROBE, LOT_WIFE_ROBE = "#2A6A9A", "#8A3A5A", "#5A6A8A"
DAUGHTERS = ("#B85A8A", "#D8A040")

def hagar(p, x, y, s, flip=False, up=None, extra=""):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=HAGAR_ROBE, woman=True, hair="#0D0D0F", sw=3, flip=flip, up=up, extra=extra)

def sarah(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=SARAH_ROBE, woman=True, hair="#B8B2A6", sw=3, flip=flip, up=up)

def abraham(p, x, y, s, flip=False, up=None, staff=False):
    return abram(p, x, y, s, flip=flip, up=up, staff=staff)

def shining(p, x, y, s, flip=False, up=None, glow=True):
    """One of the men from Jehovah: a man in white with a gold rim and a soft light about him; no wings, no face drawn."""
    halo = f'<ellipse cx="{f(x)}" cy="{f(y - 110 * s)}" rx="{f(80 * s)}" ry="{f(130 * s)}" fill="#FFF4C2" opacity="0.45"></ellipse>' if glow else ""
    return halo + mk.person(p, round(x), round(y), round(s, 3), body="#E8C8A0", cloth="#FFFFFF", stroke="#E8B830", sw=3, flip=flip, up=up)

def light_figure(x, y, s):
    """The angel of Jehovah at the fountain: a tall shape of white light (no face, no wings), rays behind."""
    return (V.rays(x, y - 120 * s, 36, 20 * s, 340 * s, color="#FFF4C2", op=0.5)
            + f'<ellipse cx="{f(x)}" cy="{f(y - 100 * s)}" rx="{f(46 * s)}" ry="{f(110 * s)}" fill="#FFFFFF" opacity="0.85"></ellipse>'
            + f'<ellipse cx="{f(x)}" cy="{f(y - 100 * s)}" rx="{f(30 * s)}" ry="{f(96 * s)}" fill="#FFFDF0"></ellipse>')

def daughters(p, x, y, s, flip=False):
    return woman(p, x, y, s, DAUGHTERS[0], flip=flip) + woman(p, x + 34 * s * (-1 if flip else 1), y + 2, s * 0.96, DAUGHTERS[1], flip=flip)

def lot_wife(p, x, y, s, flip=False):
    return woman(p, x, y, s, LOT_WIFE_ROBE, flip=flip)

def tent_door(p, w, h, seed, who=None):
    """A big goat-hair tent seen close, its door open, in the heat of the day."""
    base = h * 0.9
    return (sun(w * 0.86, h * 0.14, 16, color="#FFF4C2", op=0.35) + ground(w, h, base, "#C8A06A", dy=0)
            + A4.great_oak(w * 0.02, base, round(h / 300, 3), seed=seed) + G1.tent_big(w * 0.46, base, w * 0.56, h * 0.7, color="#3A2214", glow="#5A2A12"))

# ---- Genesis 16 -----------------------------------------------------------------------------------------
def tent_women(p, w, h, seed):
    """Sarai by the tent, and her Egyptian handmaid Hagar carrying water."""
    base = h * 0.88
    jar = '<path d="M-6 -214 C -16 -214 -18 -234 -10 -240 L -8 -248 L 8 -248 L 10 -240 C 18 -234 16 -214 6 -214 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>'
    return (sun(w * 0.86, h * 0.2, 16, op=0.25) + ground(w, h, base, "#C8A06A", dy=0)
            + G1.tent_big(w * 0.22, base, w * 0.3, h * 0.56, color="#3A2214", glow="#5A2A12")
            + sarai(p, w * 0.44, base, fit(base, h * 0.44)) + hagar(p, w * 0.68, base, fit(base, h * 0.46), flip=True, up=[(-22, -158), (-18, -196), (-10, -226)], extra=jar))

def given(p, w, h, seed):
    """Sarai leads Hagar by the hand to Abram at the tent door."""
    base = h * 0.88; s = fit(base, h * 0.46)
    return (sun(w * 0.5, h * 0.2, 14, color="#FFC14D", op=0.25) + ground(w, h, base, "#C8A06A", dy=0)
            + G1.tent_big(w * 0.84, base, w * 0.36, h * 0.6, color="#3A2214", glow="#5A2A12")
            + sarai(p, w * 0.2, base, s, up=[(-22, -158), (-2, -128), (20, -118)]) + hagar(p, w * 0.38, base, s * 0.98)
            + abraham(p, w * 0.64, base, s * 1.02, flip=True))

def flight(p, w, h, seed):
    """She fled from her face: Hagar running into the wilderness, the tents small behind her."""
    base = h * 0.84
    return (sun(w * 0.8, h * 0.2, 18, color="#FFF4C2", op=0.35) + ground(w, h, base, "#E8C88A", dy=0)
            + E4.tent(w * 0.1, base - 4, w * 0.08, h * 0.1) + E4.tent(w * 0.18, base - 2, w * 0.06, h * 0.08)
            + hagar(p, w * 0.62, base + 6, fit(base, h * 0.36), up=[(-22, -158), (-46, -140), (-60, -160)])
            + mk.speed(w * 0.5, base - h * 0.2, 14, 20, w * 0.3, seed, color="#C8A06A", op=0.7))

def fountain(p, w, h, seed):
    """By a fountain of water in the wilderness, in the way to Shur: a spring among rocks and palms; light standing by it."""
    base = h * 0.86
    pool = f'<ellipse cx="{f(w * 0.36)}" cy="{f(base + 4)}" rx="{f(w * 0.16)}" ry="{f(h * 0.05)}" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></ellipse>'
    rocks = "".join(f'<path d="M{f(x - 30)} {f(base + 6)} L {f(x - 20)} {f(base - 24)} L {f(x + 14)} {f(base - 30)} L {f(x + 30)} {f(base + 6)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>' for x in (w * 0.18, w * 0.54))
    return (ground(w, h, base - 10, "#E8C88A", dy=0) + G1.palm(w * 0.12, base - 6, 0.5) + G1.palm(w * 0.58, base - 8, 0.44) + rocks + pool
            + light_figure(w * 0.8, base, fit(base, h * 0.2)) + hagar(p, w * 0.42, base + 6, fit(base, h * 0.5), flip=False))

def wild_ass(w, h, seed):
    """He shall be as a wild ass among men: a wild ass galloping alone over the plain."""
    base = h * 0.84
    return (sun(w * 0.2, h * 0.3, 18, color="#FFC14D", op=0.3) + hills(w, h, base, seed, color="#8A6A4A", amp=6)
            + N.ass(w * 0.56, base + 6, round(h / 640, 3)) + mk.speed(w * 0.4, base - h * 0.2, 16, 20, w * 0.4, seed, color="#F3EFE6", op=0.6))

def well_roi(w, h, seed):
    """Beer-lahai-roi, between Kadesh and Bered: the well with a ring of stones, as a map marker."""
    o = [grid_bg(w, h, color="#3A2A1E", bg="#1A120A")]
    o.append(route([(w * 0.16, h * 0.4), (w * 0.5, h * 0.62), (w * 0.84, h * 0.4)], color="#C8A06A", sw=2, arrow=False))
    o.append(node(w * 0.16, h * 0.4, "KADESH", "#C8A06A", r=4) + node(w * 0.84, h * 0.4, "BERED", "#C8A06A", r=4))
    o.append(f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.62)}" r="22" fill="#2C9DB8" stroke="#FFD23F" stroke-width="3"></circle>'
             + label(w * 0.5, h * 0.62 + 44, "BEER-LAHAI-ROI", "#FFD23F", 11))
    return "".join(o)

def father_and_son(p, w, h, seed, tok=None):
    """Abram holds up his newborn son at the tent door."""
    base = h * 0.88
    hold = [(-22, -158), (-14, -196), (6, -230)]
    return (V.rays(w * 0.3, base - h * 0.4, 30, 30, w, color="#FFF4C2", op=0.3) + ground(w, h, base, "#C8A06A", dy=0)
            + G1.tent_big(w * 0.76, base, w * 0.36, h * 0.6, color="#3A2214", glow="#5A2A12")
            + abraham(p, w * 0.22, base, fit(base, h * 0.4), up=hold).replace("</g>", R.baby(16, -244, 0.8) + "</g>", 1)
            + hagar(p, w * 0.42, base, fit(base, h * 0.44), flip=True))

# ---- Genesis 17 -----------------------------------------------------------------------------------------
def fallen(p, w, h, seed):
    """Abram fell on his face: prostrate on the ground under a column of light."""
    base = h * 0.82
    return (V.rays(w * 0.5, -30, 36, 30, h * 1.6, color="#FFF4C2", op=0.35) + mk.stars(50, w, h * 0.6, seed)
            + ground(w, h, base, "#1A1430", dy=0) + N.prostrate(w * 0.38, base + 2, round(h / 300, 3), color=Z.ABRAM_ROBE, skin=SKIN))

def renamed(w, h, old, new, color="#FFD23F"):
    """A name being rewritten: the old name struck through, the new one lit beneath it."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#12113A"></rect>', mk.stars(40, w, h, len(new))]
    o.append(label(w * 0.5, h * 0.42, old, "#8A86A6", 40, ls=0.1) + f'<path d="M{f(w * 0.5 - len(old) * 14)} {f(h * 0.42 - 13)} L {f(w * 0.5 + len(old) * 14)} {f(h * 0.42 - 13)}" stroke="#D7261E" stroke-width="5"></path>')
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.48)} L {f(w * 0.5)} {f(h * 0.58)}" stroke="{color}" stroke-width="3"></path><path d="M{f(w * 0.5 - 8)} {f(h * 0.56)} L {f(w * 0.5)} {f(h * 0.6)} L {f(w * 0.5 + 8)} {f(h * 0.56)}" fill="none" stroke="{color}" stroke-width="3"></path>')
    o.append(label(w * 0.5, h * 0.78, new, color, 52, ls=0.1))
    return "".join(o).replace('font-family="IBM Plex Mono, monospace"', 'font-family="Anton, sans-serif"')

def kings_of_thee(w, h, seed):
    """Kings shall come out of thee: a line of gold crowns rising out of the dark like a road."""
    o = [mk.stars(60, w, h, seed)]
    for i in range(9):
        t = i / 8; x = w * (0.08 + 0.84 * t); y = h * (0.9 - 0.6 * t)
        o.append(A2.crown(x, y, 0.4 + 0.5 * t))
    return "".join(o)

def covenant_seal(w, h, seed):
    """An everlasting covenant: two rings of gold locked together, turning, with a starfield behind."""
    cx, cy = w * 0.5, h * 0.56
    r = min(w, h) * 0.22
    o = [mk.stars(80, w, h, seed), V.rays(cx, cy, 40, r, w, color="#FFD23F", op=0.18)]
    for dx, c in [(-r * 0.5, "#FFD23F"), (r * 0.5, "#E8B830")]:
        o.append(f'<circle cx="{f(cx + dx)}" cy="{f(cy)}" r="{f(r)}" fill="none" stroke="#0D0D0F" stroke-width="16"></circle>'
                 f'<circle cx="{f(cx + dx)}" cy="{f(cy)}" r="{f(r)}" fill="none" stroke="{c}" stroke-width="10"></circle>')
    for k in range(24):
        a = k / 24 * 2 * math.pi
        o.append(f'<path d="M{f(cx + math.cos(a) * r * 1.7)} {f(cy + math.sin(a) * r * 1.7)} l {f(math.cos(a) * 10)} {f(math.sin(a) * 10)}" stroke="#FFD23F" stroke-width="2"></path>')
    return "".join(o)

def household(p, w, h, seed, n=16, dusk=True, youth=None):
    """All the men of Abraham's house, those born in the house and those bought with money, gathered before the tents."""
    r = random.Random(seed); base = h * 0.92
    o = [ground(w, h, h * 0.56, "#8A6A4A", dy=0)] + [E4.tent(w * x, h * 0.6, w * 0.1, h * 0.16, color=r.choice(["#3A2214", "#5A3A22"])) for x in (0.08, 0.22, 0.78, 0.92)]
    items = sorted((r.uniform(h * 0.64, base), r.uniform(w * 0.04, w * 0.96)) for _ in range(n))
    for y, x in items:
        s = 0.18 + 0.32 * (y - h * 0.64) / (base - h * 0.64)
        o.append(man(p, x, y, s, r.choice(["#5A3A22", "#3A2214", "#8A6A4A", "#2C4A7A", "#5A2A16"]), flip=r.random() < 0.5))
    return "".join(o)

def cut_off(p, w, h, seed):
    """That soul shall be cut off from his people: a crowd far off in light, one figure alone in the dark."""
    o = [f'<rect x="-10" y="-10" width="{f(w * 0.62)}" height="{f(h + 20)}" fill="#FFC14D" opacity="0.5"></rect>', ground(w, h, h * 0.86, "#2A1A2E", dy=0)]
    r = random.Random(seed)
    for i in range(9):
        o.append(man(p, w * (0.06 + i * 0.05), h * 0.86, 0.22 + r.uniform(-0.02, 0.02), "#5A3A22"))
    o.append(f'<path d="M{f(w * 0.62)} -10 L {f(w * 0.62)} {f(h + 10)}" stroke="#D7261E" stroke-width="3" stroke-dasharray="8 6"></path>')
    o.append(man(p, w * 0.84, h * 0.86, 0.3, "#3A3A4A", body="#12090A"))
    return "".join(o)

def twelve_princes(w, h, seed):
    """Twelve princes shall he beget: twelve crowns in two rows."""
    o = [mk.stars(50, w, h, seed)]
    for i in range(12):
        x = w * (0.1 + (i % 6) * 0.16); y = h * (0.56 if i < 6 else 0.8)
        o.append(A2.crown(x, y, 0.5))
    return "".join(o)

def going_up(w, h, seed):
    """God went up from Abraham: a column of light lifting away from the ground, the tents dark."""
    base = h * 0.86
    return (f'<path d="M{f(w * 0.4)} {f(base)} L {f(w * 0.6)} {f(base)} L {f(w * 0.72)} -10 L {f(w * 0.28)} -10 Z" fill="#FFF4C2" opacity="0.4"></path>'
            + mk.stars(60, w, h * 0.6, seed) + ground(w, h, base, "#1A1430", dy=0)
            + E4.tent(w * 0.12, base, w * 0.14, h * 0.2, color="#2A1A14") + E4.tent(w * 0.88, base, w * 0.12, h * 0.18, color="#2A1A14")
            + "".join(f'<circle cx="{f(w * 0.5 + random.Random(seed + k).uniform(-40, 40))}" cy="{f(base - k * h * 0.08)}" r="2.6" fill="#FFF4C2"></circle>' for k in range(10)))

# ---- Genesis 18 -----------------------------------------------------------------------------------------
def bowing(p, w, h, seed):
    """He ran to meet them and bowed himself to the earth: Abraham bowed low before the three men under the oak."""
    base = h * 0.88; s = fit(base, h * 0.3)
    return (sun(w * 0.9, h * 0.16, 14, color="#FFF4C2", op=0.3) + ground(w, h, base, "#B5A06A", dy=0) + A4.great_oak(w * 0.02, base, round(h / 300, 3), seed=seed)
            + E.kneel(w * 0.36, base + 2, round(h / 400, 3), color=Z.ABRAM_ROBE, skin=SKIN)
            + shining(p, w * 0.6, base, s, flip=True) + shining(p, w * 0.72, base, s, flip=True) + shining(p, w * 0.84, base, s, flip=True))

def kneading(p, w, h, seed):
    """Make ready quickly three measures of fine meal: Sarah at a trough with the dough, cakes on the hot stones."""
    base = h * 0.86
    cakes = "".join(f'<ellipse cx="{f(w * x)}" cy="{f(base - 4)}" rx="18" ry="7" fill="#E8C88A" stroke="#0D0D0F" stroke-width="2"></ellipse>' for x in (0.62, 0.72, 0.82))
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2214"></rect>'
            + "".join(f'<path d="M{f(x)} -10 L {f(x - 40)} {f(h + 10)}" stroke="#2A1A0E" stroke-width="10"></path>' for x in range(0, int(w) + 60, 60))
            + f'<circle cx="{f(w * 0.72)}" cy="{f(base)}" r="{f(h * 0.3)}" fill="#FF8A3D" opacity="0.3"></circle>' + ground(w, h, base, "#5A3A22", dy=0)
            + E.blaze(w * 0.72, base + 2, 50, 40, seed) + cakes
            + f'<path d="M{f(w * 0.16)} {f(base - 30)} L {f(w * 0.44)} {f(base - 30)} L {f(w * 0.4)} {f(base)} L {f(w * 0.2)} {f(base)} Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>'
            + f'<ellipse cx="{f(w * 0.3)}" cy="{f(base - 32)}" rx="{f(w * 0.12)}" ry="8" fill="#F3E8D0" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
            + E.kneel(w * 0.3, base - 26, round(h / 520, 3), color=SARAH_ROBE, skin=SKIN, flip=True))

def to_the_herd(p, w, h, seed):
    """Abraham ran unto the herd, and fetched a calf tender and good."""
    base = h * 0.86
    return (sun(w * 0.86, h * 0.16, 14, op=0.3) + ground(w, h, base - 16, "#9AAA5A", dy=0)
            + Z.flock(w * 0.4, w * 0.98, base - 4, base + 30, 8, seed, cows=0.8, smin=0.2, smax=0.3)
            + abraham(p, w * 0.22, base + 4, fit(base, h * 0.36), up=[(-22, -158), (-46, -140), (-60, -160)])
            + A.calf(w * 0.34, base + 10, 0.4) + mk.speed(w * 0.12, base - h * 0.2, 10, 20, w * 0.2, seed, color="#F3EFE6", op=0.6))

def meal_under_tree(p, w, h, seed):
    """He set it before them, and he stood by them under the tree, and they did eat."""
    base = h * 0.88; s = fit(base, h * 0.34)
    table = (f'<rect x="{f(w * 0.24)}" y="{f(base - 40)}" width="{f(w * 0.4)}" height="10" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>'
             + "".join(f'<ellipse cx="{f(w * x)}" cy="{f(base - 44)}" rx="14" ry="6" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>' for x in (0.3, 0.4, 0.5))
             + f'<path d="M{f(w * 0.56)} {f(base - 40)} l -6 -18 l 18 0 l -6 18 Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></path>')
    return (A4.great_oak(w * 0.4, base, round(h / 240, 3), seed=seed) + ground(w, h, base, "#9AAA5A", dy=0)
            + E.kneel(w * 0.2, base, round(h / 560, 3), color="#FFFFFF", skin="#E8C8A0") + E.kneel(w * 0.44, base, round(h / 560, 3), color="#FFFFFF", skin="#E8C8A0", flip=True)
            + E.kneel(w * 0.66, base, round(h / 560, 3), color="#FFFFFF", skin="#E8C8A0", flip=True) + table
            + abraham(p, w * 0.86, base, s, flip=True))

def heard_behind(p, w, h, seed):
    """Sarah heard in the tent door, which was behind him: her face half in the dark of the doorway."""
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1408"></rect>'
            + f'<path d="M{f(w * 0.3)} -10 L {f(w * 0.7)} {f(h + 10)} L {f(w + 10)} {f(h + 10)} L {f(w + 10)} -10 Z" fill="#5A3A22"></path>'
            + mk.face(SARAH, -40, h - 380, 1.0)
            + "".join(f'<path d="M{f(x)} -10 L {f(x + 60)} {f(h + 10)}" stroke="#3A2214" stroke-width="6"></path>' for x in range(int(w * 0.4), int(w) + 40, 40)))

def toward_sodom(p, w, h, seed):
    """The men rose up from thence, and looked toward Sodom: on the height, the Plain far below, Abraham with them."""
    base = h * 0.6; s = fit(base, h * 0.12)
    return (sun(w * 0.86, h * 0.14, 12, color="#FFE680", op=0.25)
            + f'<path d="M-10 {f(base)} L {f(w * 0.5)} {f(base - 6)} L {f(w * 0.54)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#7A6A4A" stroke="#0D0D0F" stroke-width="2"></path>'
            + f'<path d="M{f(w * 0.54)} {f(h * 0.82)} L {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.54)} {f(h + 10)} Z" fill="#5E8F26" stroke="#0D0D0F" stroke-width="2"></path>'
            + "".join(city(w * x, h * 0.82, w * 0.08, h * 0.08, seed + i, color="#4A2A2A", lit="#FF6A2A") for i, x in enumerate((0.66, 0.8, 0.92)))
            + shining(p, w * 0.12, base, s, glow=False) + shining(p, w * 0.22, base, s, glow=False) + shining(p, w * 0.32, base, s, glow=False)
            + abraham(p, w * 0.44, base - 2, s, flip=True))

def cry_of_sodom(w, h, seed):
    """The cry of Sodom and Gomorrah is great: the cities red under black smoke, waves of sound going up."""
    base = h * 0.86; r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A0A0E"></rect>']
    for i in range(7):
        o.append(f'<path d="M{f(w * 0.1)} {f(base - 40 - i * h * 0.08)} C {f(w * 0.3)} {f(base - 70 - i * h * 0.08)} {f(w * 0.7)} {f(base - 10 - i * h * 0.08)} {f(w * 0.9)} {f(base - 40 - i * h * 0.08)}" fill="none" stroke="#D7261E" stroke-width="2" opacity="{0.8 - i * 0.1:.2f}"></path>')
    o.append(city(w * 0.34, base, w * 0.42, h * 0.4, seed, color="#12060A", lit="#FF6A2A", wall="#2A0A0E") + city(w * 0.78, base, w * 0.3, h * 0.3, seed + 1, color="#12060A", lit="#FF6A2A", wall="#2A0A0E"))
    o.append(ground(w, h, base, "#12060A", dy=0))
    return "".join(o)

def countdown(w, h, n, prev=None, compact=False):
    """The number of the righteous going down: a big counter, the old value struck out. compact puts it small in the
    lower right corner, so a Voice box can sit at the top left."""
    if compact:
        A_ = 'font-family="Anton, sans-serif"'
        o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#12113A"></rect>']
        o.append(label(w * 0.6, h * 0.9, f"{prev:02d}", "#8A86A6", 30).replace('font-family="IBM Plex Mono, monospace"', A_)
                 + f'<path d="M{f(w * 0.6 - 22)} {f(h * 0.9 - 11)} L {f(w * 0.6 + 22)} {f(h * 0.9 - 11)}" stroke="#D7261E" stroke-width="4"></path>')
        o.append(label(w * 0.84, h * 0.92, f"{n:02d}", "#FFD23F", 64).replace('font-family="IBM Plex Mono, monospace"', A_))
        return "".join(o)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#12113A"></rect>']
    for k in range(10):
        o.append(f'<rect x="{f(w * 0.06 + k * w * 0.088)}" y="{f(h * 0.82)}" width="{f(w * 0.07)}" height="10" fill="{"#FFD23F" if k < n / 5 else "#2A2A4A"}"></rect>')
    if prev: o.append(label(w * 0.22, h * 0.56, f"{prev:02d}", "#8A86A6", 40).replace('font-family="IBM Plex Mono, monospace"', 'font-family="Anton, sans-serif"')
                      + f'<path d="M{f(w * 0.22 - 30)} {f(h * 0.56 - 14)} L {f(w * 0.22 + 30)} {f(h * 0.56 - 14)}" stroke="#D7261E" stroke-width="5"></path>')
    o.append(label(w * 0.62, h * 0.66, f"{n:02d}", "#FFD23F", 88).replace('font-family="IBM Plex Mono, monospace"', 'font-family="Anton, sans-serif"'))
    o.append(label(w * 0.62, h * 0.76, "RIGHTEOUS", "#FFD23F", 11))
    return "".join(o)

def stood_before(p, w, h, seed):
    """The men went toward Sodom, but Abraham stood yet before Jehovah: two figures going down the road, one standing in light."""
    base = h * 0.84
    return (V.rays(w * 0.3, -30, 30, 30, h * 1.4, color="#FFF4C2", op=0.35) + ground(w, h, base, "#8A7A5A", dy=0)
            + f'<path d="M{f(w * 0.4)} {f(h + 10)} L {f(w * 0.86)} {f(base - 2)} L {f(w * 0.92)} {f(base - 2)} L {f(w * 0.6)} {f(h + 10)} Z" fill="#B5A06A"></path>'
            + shining(p, w * 0.8, base - 4, 0.17, glow=False) + shining(p, w * 0.86, base - 4, 0.17, glow=False)
            + abraham(p, w * 0.28, base + 4, fit(base, h * 0.36)))

def dust_ashes(w, h, seed):
    """Who am but dust and ashes: grey ash drifting up through a beam of light."""
    r = random.Random(seed)
    return (V.rays(w * 0.5, -30, 30, 30, h * 1.4, color="#FFF4C2", op=0.3)
            + "".join(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(0, h))}" r="{f(r.uniform(0.8, 3))}" fill="{r.choice(["#8A867E", "#B8B2A6", "#5A5650"])}"></circle>' for _ in range(260)))

def returned(p, w, h, seed):
    """Jehovah went his way, and Abraham returned unto his place: a lone figure walking back to the tents at dusk."""
    base = h * 0.84
    return (sun(w * 0.8, base - 10, h * 0.2, color="#FF8A3D", op=0.25) + hills(w, h, base, seed, color="#2A1A2E", amp=6)
            + E4.tent(w * 0.16, base, w * 0.12, h * 0.2, color="#2A1A14") + E4.tent(w * 0.26, base, w * 0.08, h * 0.14, color="#2A1A14")
            + abraham(p, w * 0.5, base + 4, fit(base, h * 0.4), flip=True, staff=True, up=HOLD_STAFF))

# ---- Genesis 19 -----------------------------------------------------------------------------------------
def clay_lamp(x, y, s=1.0):
    """A small clay oil lamp on a ledge, its wick burning."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-30 0 L 30 0 L 26 6 L -26 6 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M-20 0 C -22 -12 6 -16 18 -8 L 30 -10 L 24 -2 L 16 0 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>'
            '<circle cx="-4" cy="-9" r="3" fill="#2A1408"></circle></g>' + E.flame(x + 27 * s, y - 10 * s, 6 * s, 18 * s, 4))

def city_gate(p, w, h, seed, top=0.4):
    """Lot sat in the gate of Sodom at even: the gatehouse, the two men coming up the road, Lot bowing."""
    base = h * 0.88; s = fit(base, h * top)
    return (sun(w * 0.86, base - h * 0.2, h * 0.14, color="#FF6A2A", op=0.2) + A4.gatehouse(w * 0.26, base, w * 0.4, h * 0.72, lit=True)
            + ground(w, h, base, "#5A3A2A", dy=0) + E.kneel(w * 0.54, base + 2, round(h / 520, 3), color=Z.LOT_ROBE, skin=SKIN)
            + shining(p, w * 0.74, base, s, flip=True) + shining(p, w * 0.86, base, s, flip=True))

def feast(p, w, h, seed):
    """He made them a feast, and did bake unleavened bread, and they did eat: a lamp-lit room, flat loaves, the men in white."""
    base = h * 0.88
    loaves = "".join(f'<ellipse cx="{f(w * x)}" cy="{f(base - 46)}" rx="16" ry="5" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.6"></ellipse>' for x in (0.36, 0.46, 0.56))
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A1E14"></rect>' + f'<circle cx="{f(w * 0.46)}" cy="{f(h * 0.3)}" r="{f(h * 0.4)}" fill="#FFC14D" opacity="0.25"></circle>'
            + clay_lamp(w * 0.46, h * 0.4, 1.4) + ground(w, h, base, "#2A140C", dy=0)
            + f'<rect x="{f(w * 0.28)}" y="{f(base - 42)}" width="{f(w * 0.36)}" height="10" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>' + loaves
            + E.kneel(w * 0.2, base, round(h / 540, 3), color="#FFFFFF", skin="#E8C8A0") + E.kneel(w * 0.72, base, round(h / 540, 3), color="#FFFFFF", skin="#E8C8A0", flip=True)
            + lot(p, w * 0.88, base, fit(base, h * 0.36), flip=True))

def mob_at_door(p, w, h, seed):
    """The men of the city compassed the house round, young and old: a crowd with torches before a shut door at night."""
    r = random.Random(seed); base = h * 0.92
    o = [mk.stars(40, w, h * 0.3, seed),
         f'<rect x="{f(w * 0.34)}" y="{f(h * 0.12)}" width="{f(w * 0.32)}" height="{f(base - h * 0.12)}" fill="#4A3A2E" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.44)}" y="{f(h * 0.4)}" width="{f(w * 0.12)}" height="{f(base - h * 0.4)}" fill="#2A1A10" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         ground(w, h, base, "#1A1018", dy=0)]
    items = sorted((r.uniform(h * 0.6, h * 1.04), r.uniform(-10, w + 10)) for _ in range(30))
    for y, x in items:
        if abs(x - w * 0.5) < w * 0.07 and y < h * 0.9: continue
        s = 0.2 + 0.36 * (y - h * 0.6) / (h * 0.44)
        o.append(man(p, x, y, s, "#12090A", body="#12090A", flip=x > w * 0.5))
        if r.random() < 0.18:
            o.append(f'<path d="M{f(x + 14 * s)} {f(y - 150 * s)} L {f(x + 18 * s)} {f(y - 230 * s)}" stroke="#5A3A22" stroke-width="{f(5 * s + 1)}"></path>' + E.flame(x + 18 * s, y - 226 * s, 10 * s + 3, 34 * s + 8, r.uniform(-8, 8)))
    return "".join(o)

def at_the_door(p, w, h, seed):
    """Lot went out unto them to the door, and shut the door after him: Lot alone with his back to the shut door."""
    base = h * 0.92
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#4A3A2E"></rect>'
            + f'<rect x="{f(w * 0.3)}" y="{f(h * 0.1)}" width="{f(w * 0.4)}" height="{f(base - h * 0.1)}" fill="#2A1A10" stroke="#0D0D0F" stroke-width="3"></rect>'
            + "".join(f'<path d="M{f(w * 0.3)} {f(y)} L {f(w * 0.7)} {f(y)}" stroke="#1A0E08" stroke-width="3"></path>' for y in range(int(h * 0.2), int(base), 30))
            + ground(w, h, base, "#1A1018", dy=0) + f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.5)}" r="{f(h * 0.6)}" fill="#FF8A3D" opacity="0.18"></circle>'
            + lot(p, w * 0.5, base, fit(base, h * 0.26), up=[(-22, -158), (-40, -150), (-60, -164)]))

def pulled_in(p, w, h, seed):
    """The men put forth their hand, and brought Lot into the house to them: two white arms reaching out of the doorway."""
    base = h * 0.92
    arm = lambda y, c: (f'<path d="M{f(w * 0.36)} {f(y)} L {f(w * 0.56)} {f(y + 10)}" stroke="#0D0D0F" stroke-width="22" stroke-linecap="round"></path>'
                        f'<path d="M{f(w * 0.36)} {f(y)} L {f(w * 0.56)} {f(y + 10)}" stroke="{c}" stroke-width="17" stroke-linecap="round"></path>')
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#4A3A2E"></rect>'
            + f'<rect x="{f(w * 0.12)}" y="{f(h * 0.08)}" width="{f(w * 0.3)}" height="{f(base - h * 0.08)}" fill="#FFF4C2" stroke="#0D0D0F" stroke-width="3"></rect>'
            + V.rays(w * 0.26, h * 0.5, 24, 20, w * 0.6, color="#FFF4C2", op=0.4)
            + lot(p, w * 0.64, base, fit(base, h * 0.42), flip=True, up=[(-22, -158), (-40, -150), (-58, -150)])
            + arm(h * 0.5, "#FFFFFF") + arm(h * 0.6, "#FFFFFF")
            + "".join(f'<circle cx="{f(w * 0.565)}" cy="{f(y + 10)}" r="10" fill="#E8C8A0" stroke="#0D0D0F" stroke-width="2"></circle>' for y in (h * 0.5, h * 0.6))
            + ground(w, h, base, "#1A1018", dy=0))

def blindness(p, w, h, seed):
    """They smote the men at the door with blindness, small and great: a white flash; figures groping, hands out."""
    r = random.Random(seed); base = h * 0.9
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#FFFDF0"></rect>', mk.speed(w * 0.5, h * 0.4, 70, 20, w, seed, color="#C8C2B6", sw=1.6, op=0.8)]
    for i in range(8):
        x = w * (0.06 + i * 0.125)
        o.append(man(p, x, base + r.uniform(-6, 8), 0.3 + r.uniform(-0.03, 0.03), "#3A3A4A", body="#2A2A3A", flip=i % 2 == 1, up=[(-22, -158), (-46, -150), (-70, -156)]))
    return "".join(o)

def mockers(p, w, h, seed):
    """He seemed unto his sons-in-law as one that mocked: Lot urging two young men who turn away laughing."""
    base = h * 0.88; s = fit(base, h * 0.5)
    return (mk.stars(40, w, h * 0.5, seed) + ground(w, h, base, "#2A1A2E", dy=0) + city(w * 0.5, base - 2, w * 1.2, h * 0.36, seed, color="#1A0E18", lit="#FF8A3D", wall="#241420")
            + lot(p, w * 0.26, base, s, up=[(-22, -158), (0, -170), (24, -186)])
            + man(p, w * 0.62, base, s, "#5A3A6A", flip=True) + man(p, w * 0.76, base, s * 1.02, "#3A5A6A"))

def by_the_hand(p, w, h, seed):
    """The men laid hold upon his hand, and the hand of his wife and of his two daughters: a chain of hands out through the gate at dawn."""
    base = h * 0.88; s = fit(base, h * 0.36)
    hand = [(-22, -158), (-40, -120), (-52, -100)]
    return (sun(w * 0.9, base - 10, h * 0.2, color="#FFC14D", op=0.3) + A4.gatehouse(w * 0.08, base, w * 0.22, h * 0.6) + ground(w, h, base, "#8A6A4A", dy=0)
            + daughters(p, w * 0.3, base, s * 0.92, flip=True) + lot_wife(p, w * 0.46, base, s * 0.94, flip=True)
            + lot(p, w * 0.6, base, s, flip=True) + shining(p, w * 0.76, base, s * 1.02, flip=True, up=hand) + shining(p, w * 0.9, base, s * 1.02, flip=True, up=hand))

def escape_map(w, h, seed):
    """Escape to the mountain: a route away from the city across the Plain, with the warning 'LOOK NOT BEHIND'."""
    o = [grid_bg(w, h, color="#3A1A1E", bg="#1A0A0E")]
    o.append(node(w * 0.14, h * 0.5, "SODOM", "#D7261E", r=7, dy=-16) + node(w * 0.62, h * 0.56, "ZOAR", "#FFD23F", r=5, dy=-14))
    o.append(f'<path d="M{f(w * 0.72)} {f(h * 0.5)} L {f(w * 0.86)} {f(h * 0.12)} L {f(w * 1.0)} {f(h * 0.5)} Z" fill="#3A2A2E" stroke="#8FD0E2" stroke-width="2"></path>' + label(w * 0.86, h * 0.6, "THE MOUNTAIN", "#8FD0E2", 10))
    o.append(route([(w * 0.18, h * 0.5), (w * 0.5, h * 0.5), (w * 0.82, h * 0.26)], color="#FFD23F", sw=3))
    return "".join(o)

def little_city(w, h, seed):
    """The sun was risen upon the earth when Lot came unto Zoar: a little walled town in the sunrise."""
    base = h * 0.8
    return (sun(w * 0.7, base - 10, h * 0.24, color="#FFD23F", op=0.4) + hills(w, h, base, seed, color="#5A3A2E", amp=6)
            + city(w * 0.4, base, w * 0.24, h * 0.24, seed, color="#8A5A3E") + label(w * 0.4, base + 24, "ZOAR", "#12113A", 11))

def at_the_place(p, w, h, seed):
    """Abraham gat up early in the morning to the place where he had stood before Jehovah."""
    base = h * 0.82
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#C8A0A0"></rect>' + f'<path d="M{f(w * 0.6)} {f(h + 10)} C {f(w * 0.7)} {f(h * 0.5)} {f(w * 0.9)} {f(h * 0.2)} {f(w * 0.86)} -10" fill="none" stroke="#3A2A2E" stroke-width="70" opacity="0.6"></path>'
            + ground(w, h, base, "#6A5A4A", dy=0) + abraham(p, w * 0.3, base + 4, fit(base, h * 0.36)))

def cave_mouth(p, w, h, seed, fire=True, figures=True):
    """A cave in the mountain at night, a small fire in its mouth; seen from outside."""
    base = h * 0.88
    o = [mk.stars(60, w, h * 0.5, seed), f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.3)} L {f(w * 0.3)} {f(h * 0.16)} L {f(w * 0.7)} {f(h * 0.24)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} Z" fill="#3A2A2E" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.3)} {f(base)} C {f(w * 0.3)} {f(h * 0.46)} {f(w * 0.66)} {f(h * 0.42)} {f(w * 0.7)} {f(base)} Z" fill="#12090A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    if fire: o.append(f'<circle cx="{f(w * 0.5)}" cy="{f(base - 10)}" r="{f(h * 0.2)}" fill="#FF8A3D" opacity="0.25"></circle>' + E.blaze(w * 0.5, base, 24, 30, seed))
    if figures: o.append(daughters(p, w * 0.4, base, fit(base, h * 0.6) * 0.9))
    o.append(ground(w, h, base, "#2A1A1E", dy=0))
    return "".join(o)

def wine_jar(w, h, seed):
    """They made their father drink wine that night: a wine jar and a cup by the fire in the dark."""
    base = h * 0.84
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#12090A"></rect>' + f'<circle cx="{f(w * 0.62)}" cy="{f(base)}" r="{f(h * 0.4)}" fill="#FF8A3D" opacity="0.18"></circle>'
            + E.blaze(w * 0.72, base + 4, 30, 34, seed) + ground(w, h, base, "#2A1A1E", dy=0)
            + f'<path d="M{f(w * 0.36)} {f(base)} C {f(w * 0.24)} {f(base - 40)} {f(w * 0.28)} {f(base - 110)} {f(w * 0.36)} {f(base - 120)} L {f(w * 0.36)} {f(base - 140)} L {f(w * 0.46)} {f(base - 140)} L {f(w * 0.46)} {f(base - 120)} C {f(w * 0.54)} {f(base - 110)} {f(w * 0.58)} {f(base - 40)} {f(w * 0.46)} {f(base)} Z" fill="#7A2A3A" stroke="#0D0D0F" stroke-width="2.4"></path>'
            + f'<path d="M{f(w * 0.56)} {f(base)} l -8 -26 l 26 0 l -8 26 Z" fill="#C9A86A" stroke="#0D0D0F" stroke-width="1.6"></path>')
