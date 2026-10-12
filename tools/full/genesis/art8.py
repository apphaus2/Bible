"""New drawings for Genesis chapter 8 (Genesis 28–30): Jacob sent to Paddan-aram, the stone for a pillow, the well
with the great stone, Laban's house, Leah and Rachel, the wedding feast, the mandrakes, the speckled flock and the rods."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus4 as E4, exodus5 as V, joshua1 as J, judges1 as G1, judges2 as S, samuel4 as A4, numbers1 as N, ruth1 as R
from faces_ex import F
from genesis import art2 as Y, art3 as Z, art4 as Q, art5 as K, art6 as R6, art7 as J7
from genesis.art2 import fit, ground, hills, birds, city, SKIN
from genesis.art3 import sun, label, man, woman, grid_bg, node, route, STAFF, HOLD_STAFF, GREY_BEARD
from genesis.art5 import well
from genesis.art7 import jacob, esau, old_isaac, goat, tent_inside, couch
def f(v): return f"{v:.1f}"

# ---- faces ----------------------------------------------------------------------------------------------
JACOB, JACOB_AFRAID = J7.JACOB, J7.JACOB_AFRAID
JACOB_AWE = F("adam", skin="#B9A6B8", shadow="#4A3A6E", hair="#1A1210", hl="#6A5A7E", brow="sorrow", light="#FFF4C2")
JACOB_WEEP = F("adam", skin="#D9A27A", shadow="#A8684A", hair="#2A1A10", hl="#5A4A3E", tear=True, light="#FFE680")
JACOB_MAN = F("adam", skin="#D9A27A", shadow="#8A5A3E", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", light="#FFC14D")
JACOB_ANGRY = F("adam", skin="#C98E66", shadow="#5A2A1E", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", brow="scowl", light="#FF6A4A")
LABAN = F("adam", skin="#C98E66", shadow="#6A3A2A", hair="#5A5650", hl="#8A867E", beard=True, beard_color="#4A4640", scarf="#9A3A1E", cord=True, light="#FFC14D")
LABAN_SLY = F("adam", skin="#C98E66", shadow="#5A2A1E", hair="#5A5650", hl="#8A867E", beard=True, beard_color="#4A4640", scarf="#9A3A1E", cord=True, brow="scowl", light="#FF8A3D")
RACHEL = F("eve", skin="#E3B08A", shadow="#B97A58", hair="#1A1210", light="#FFE680")
RACHEL_ENVY = F("eve", skin="#D99A7A", shadow="#6A3A3A", hair="#1A1210", brow="scowl", light="#FF6A4A")
RACHEL_JOY = F("eve", skin="#E3B08A", shadow="#B97A58", hair="#1A1210", laugh=True, light="#FFF4C2")
LEAH = F("eve", skin="#DDA684", shadow="#A87050", hair="#6A3A1E", scarf="#2A3A7A", light="#FFE680")
LEAH_SAD = F("eve", skin="#C99A84", shadow="#6A4A5A", hair="#6A3A1E", scarf="#2A3A7A", tear=True, light="#9FB8FF")
LEAH_VEIL = F("eve", skin="#DDA684", shadow="#A87050", hair="#6A3A1E", scarf="#F3EFE6", light="#FFE680")

# ---- people ---------------------------------------------------------------------------------------------
RACHEL_ROBE, LEAH_ROBE, BILHAH_ROBE, ZILPAH_ROBE, LABAN_ROBE = "#C2456A", "#2A3A7A", "#1F7A8C", "#8A6AB8", "#9A3A1E"
JACOB_BEARD = GREY_BEARD.replace("#B8B2A6", "#2A1A10")

def rachel(p, x, y, s, flip=False, up=None, staff=False):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=RACHEL_ROBE, woman=True, hair="#1A1210", sw=3, flip=flip, up=up,
                     extra=STAFF if staff else "")

def leah(p, x, y, s, flip=False, up=None, veil=False):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#F3EFE6" if veil else LEAH_ROBE, woman=True, hair="#F3EFE6" if veil else "#6A3A1E",
                     sw=3, flip=flip, up=up)

def laban(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=LABAN_ROBE, sw=3, flip=flip, up=up, extra=GREY_BEARD.replace("#B8B2A6", "#4A4640"))

def jacob_man(p, x, y, s, flip=False, up=None, staff=False):
    """Jacob grown, bearded, in Laban's service: slate-blue robe, a shepherd's staff."""
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=J7.JACOB_ROBE, sw=3, flip=flip, up=up, extra=JACOB_BEARD + (STAFF if staff else ""))

def spotted(x, y, s=1.0, flip=False, kind="goat", seed=1):
    """A speckled, spotted or ringstreaked beast: a sheep or goat with white and dark patches."""
    r = random.Random(seed)
    base = E.sheep(x, y, s, flip=flip, wool="#F3EFE6" if kind == "sheep" else "#8A6A4A", face="#2A1A10")
    dots = "".join(f'<ellipse cx="{f(x + r.uniform(-30, 30) * s)}" cy="{f(y - r.uniform(30, 60) * s)}" rx="{f(r.uniform(5, 10) * s)}" ry="{f(r.uniform(4, 7) * s)}" '
                   f'fill="{r.choice(["#2A1A10", "#F3EFE6", "#5A3A22"])}"></ellipse>' for _ in range(7))
    return base + dots

# ---- Genesis 28 -----------------------------------------------------------------------------------------
def sending(p, w, h, seed):
    """Isaac called Jacob, and blessed him, and charged him: the old father seated, his hand on the kneeling son."""
    base = h * 0.88
    return (tent_inside(w, h, 0.3) + ground(w, h, base, "#2A1408", dy=0) + couch(w * 0.36, base, w * 0.3)
            + E.kneel(w * 0.36, base - 24, round(h / 520, 3), color=R6.ISAAC_ROBE, skin=SKIN)
            + E.kneel(w * 0.62, base + 2, round(h / 420, 3), color=J7.JACOB_ROBE, skin=SKIN, flip=True))

def setting_out(p, w, h, seed):
    """Isaac sent away Jacob, and he went to Paddan-aram: a lone walker with a staff, the road north at dawn."""
    base = h * 0.86
    return (sun(w * 0.86, base - 10, h * 0.2, color="#FFC14D", op=0.3) + hills(w, h, base, seed, color="#5A4A3A", amp=8) + ground(w, h, base, "#C8A06A", dy=0)
            + f'<path d="M{f(w * 0.1)} {f(h + 10)} C {f(w * 0.4)} {f(base - 10)} {f(w * 0.6)} {f(base - 10)} {f(w * 0.9)} {f(base - 4)}" fill="none" stroke="#E8C88A" stroke-width="12" stroke-linecap="round"></path>'
            + jacob(p, w * 0.3, base + 4, fit(base, h * 0.4), up=HOLD_STAFF).replace("</g>", STAFF + "</g>", 1))

def esau_third(p, w, h, seed):
    """Esau went unto Ishmael and took Mahalath, besides the wives that he had."""
    base = h * 0.88; s = fit(base, h * 0.5)
    return (sun(w * 0.2, h * 0.2, 14, op=0.25) + ground(w, h, base, "#C8A06A", dy=0) + E4.tent(w * 0.86, base, w * 0.16, h * 0.24, color="#5A6A3A")
            + esau(p, w * 0.46, base, s, bow=False) + woman(p, w * 0.56, base, s * 0.95, "#5A6A3A", flip=True)
            + label(w * 0.56, base + 18, "MAHALATH", "#12113A", 9))

def stone_pillow(p, w, h, seed):
    """He took one of the stones of the place, and put it under his head, and lay down: sunset, a bare hillside."""
    base = h * 0.82
    return (sun(w * 0.76, base - 6, h * 0.22, color="#FF8A3D", op=0.35) + hills(w, h, base, seed, color="#3A2A3E", amp=10)
            + ground(w, h, base, "#5A4A4E", dy=0)
            + f'<ellipse cx="{f(w * 0.22)}" cy="{f(base + 4)}" rx="22" ry="12" fill="#8A8478" stroke="#0D0D0F" stroke-width="2"></ellipse>'
            + f'<g transform="translate({f(w * 0.56)} {f(base + 6)}) scale({f(h / 360)})" fill="{J7.JACOB_ROBE}" stroke="#0D0D0F" stroke-width="2"><use href="#{p}LieB"></use><use href="#{p}LieA"></use></g>')

def oil_pillar(p, w, h, seed):
    """He set up the stone for a pillar, and poured oil upon the top of it: Jacob pouring from a horn at dawn."""
    base = h * 0.86
    pillar = (f'<path d="M{f(w * 0.8)} {f(base)} L {f(w * 0.81)} {f(base - h * 0.4)} C {f(w * 0.82)} {f(base - h * 0.46)} {f(w * 0.9)} {f(base - h * 0.46)} {f(w * 0.91)} {f(base - h * 0.4)} L {f(w * 0.92)} {f(base)} Z" '
              f'fill="#8A8478" stroke="#0D0D0F" stroke-width="2.4"></path>'
              f'<path d="M{f(w * 0.83)} {f(base - h * 0.42)} C {f(w * 0.84)} {f(base - h * 0.3)} {f(w * 0.84)} {f(base - h * 0.2)} {f(w * 0.85)} {f(base - h * 0.1)}" fill="none" stroke="#E8B830" stroke-width="4"></path>')
    return (sun(w * 0.56, base - 10, h * 0.18, color="#FFE680", op=0.35) + ground(w, h, base, "#7A6A5A", dy=0) + pillar
            + jacob(p, w * 0.7, base, fit(base, h * 0.36), up=[(-22, -158), (0, -196), (20, -214)]).replace("</g>", '<g transform="translate(24 -222) rotate(120)">' + A1_vial() + '</g></g>', 1))

def A1_vial():
    import samuel1 as A
    return A.vial(0, 0, 0.8, pour=26)

def vow(w, h, seed):
    """If God will be with me … then this stone shall be God's house: the pillar alone under the stars, a tenth marked."""
    base = h * 0.86
    return (mk.stars(80, w, h * 0.7, seed) + ground(w, h, base, "#1A1430", dy=0)
            + f'<rect x="{f(w * 0.46)}" y="{f(base - h * 0.5)}" width="{f(w * 0.08)}" height="{f(h * 0.5)}" rx="6" fill="#5A5A6A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
            + V.rays(w * 0.5, base - h * 0.5, 24, 10, h * 0.5, color="#FFD23F", op=0.25))

# ---- Genesis 29 -----------------------------------------------------------------------------------------
def three_flocks(p, w, h, seed):
    """A well in the field, and three flocks of sheep lying there by it; the stone upon the well's mouth was great."""
    base = h * 0.86
    stone = f'<ellipse cx="{f(w * 0.5)}" cy="{f(base - 34)}" rx="{f(w * 0.12)}" ry="{f(h * 0.06)}" fill="#7A7468" stroke="#0D0D0F" stroke-width="2.6"></ellipse>'
    return (sun(w * 0.86, h * 0.18, 16, op=0.3) + ground(w, h, base - 30, "#8AAA5A", dy=0) + well(w * 0.5, base - 20, h / 260) + stone
            + Z.flock(w * 0.04, w * 0.3, base - 10, base + 20, 6, seed, cows=0, smin=0.24, smax=0.32)
            + Z.flock(w * 0.66, w * 0.96, base - 10, base + 20, 6, seed + 1, cows=0, smin=0.24, smax=0.32)
            + man(p, w * 0.34, base, fit(base, h * 0.44), "#8A6A4A") + man(p, w * 0.66, base, fit(base, h * 0.44), "#5A6A3A", flip=True)
            + man(p, w * 0.78, base, fit(base, h * 0.46), "#7A5A3A", flip=True) + jacob(p, w * 0.12, base, fit(base, h * 0.42)))

def embrace(p, w, h, seed):
    """Laban ran to meet him, and embraced him, and kissed him, and brought him to his house."""
    base = h * 0.88; s = fit(base, h * 0.36)
    return (sun(w * 0.2, h * 0.2, 14, color="#FFE680", op=0.25) + city(w * 0.86, base, w * 0.3, h * 0.5, seed, color="#8A6A5A", lit="#FFC14D", wall="#9A7A6A")
            + ground(w, h, base, "#B59A7A", dy=0)
            + jacob(p, w * 0.46, base, s, up=[(-22, -158), (2, -150), (22, -164)]) + laban(p, w * 0.56, base, s * 1.02, flip=True, up=[(-22, -158), (2, -150), (22, -164)])
            + rachel(p, w * 0.24, base, s * 0.95))

def seven_years(w, h, seed, n=7, hi=None):
    """Seven years for Rachel: seven seasons as bands of colour, numbered."""
    cols = ["#7AA05A", "#FFC14D", "#C8683E", "#9FC8E2", "#7AA05A", "#FFC14D", "#C2456A"]
    bw = w / n; o = []
    for i in range(n):
        c = cols[i % 7]
        o.append(f'<rect x="{f(i * bw)}" y="-10" width="{f(bw + 1)}" height="{f(h + 20)}" fill="{c}"></rect>'
                 + label(i * bw + bw / 2, h * 0.9, str(i + 1), "#F3EFE6" if hi != i else "#D7261E", 22).replace('font-family="IBM Plex Mono, monospace"', 'font-family="Anton, sans-serif"'))
    return "".join(o)

def wedding(p, w, h, seed):
    """Laban gathered all the men of the place, and made a feast; in the evening he brought Leah, veiled, to Jacob."""
    base = h * 0.9; r = random.Random(seed)
    o = [mk.stars(30, w, h * 0.3, seed), f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.4)}" r="{f(h * 0.6)}" fill="#FFC14D" opacity="0.2"></circle>', ground(w, h, base, "#2A1A14", dy=0)]
    for i in range(8):
        o.append(E.kneel(w * (0.06 + i * 0.06), base, round(h / 620, 3), color=r.choice(["#5A3A22", "#9A3A1E", "#3A2214", "#7A5A3A"]), skin=SKIN))
    o.append(laban(p, w * 0.7, base, fit(base, h * 0.6), flip=True, up=[(-22, -158), (-40, -126), (-58, -110)]))
    o.append(leah(p, w * 0.84, base, fit(base, h * 0.62), flip=True, veil=True))
    o.append(E.flame(w * 0.56, base - 4, 16, 40, 2))
    return "".join(o)

def sons_ring(w, h, seed, names, hi=None):
    """Jacob's sons so far, as a row of numbered nodes; the newest lit."""
    o = [mk.stars(30, w, h, seed)]
    n = len(names)
    for i, nm in enumerate(names):
        x = w * (0.06 + 0.88 * i / 11); y = h * 0.36
        c = "#D7261E" if i == hi else "#FFD23F"
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="8" fill="#12113A" stroke="{c}" stroke-width="2.4"></circle>'
                 + label(x, y + 3, f"{i + 1}", c, 8, ls=0) + label(x, h * 0.86, nm, c, 7.5, ls=0.04))
    for i in range(n, 12):
        x = w * (0.06 + 0.88 * i / 11)
        o.append(f'<circle cx="{f(x)}" cy="{f(h * 0.36)}" r="8" fill="none" stroke="#3A3A5A" stroke-width="2" stroke-dasharray="3 3"></circle>')
    return "".join(o)

# ---- Genesis 30 -----------------------------------------------------------------------------------------
def handmaid(p, w, h, seed, giver="rachel"):
    """She gave him her handmaid to wife: the mistress leading her maid by the hand to Jacob's tent."""
    base = h * 0.88; s = fit(base, h * 0.42)
    mis = rachel(p, w * 0.5, base, s, up=[(-22, -158), (-2, -128), (20, -118)]) if giver == "rachel" else leah(p, w * 0.5, base, s, up=[(-22, -158), (-2, -128), (20, -118)])
    maid = woman(p, w * 0.64, base, s * 0.96, BILHAH_ROBE if giver == "rachel" else ZILPAH_ROBE)
    return (ground(w, h, base, "#C8A06A", dy=0) + G1.tent_big(w * 0.86, base, w * 0.26, h * 0.62, color="#3A2214", glow="#5A2A12") + mis + maid
            + label(w * 0.64, base + 18, "BILHAH" if giver == "rachel" else "ZILPAH", "#12113A", 9))

def mandrakes(p, w, h, seed):
    """Reuben went in the days of wheat harvest, and found mandrakes in the field."""
    base = h * 0.86
    plant = lambda x, y: (f'<g transform="translate({f(x)} {f(y)})">' + "".join(f'<path d="M0 0 C {dx} -20 {dx * 1.6} -30 {dx * 2} -24" fill="#3F6A2A" stroke="#0D0D0F" stroke-width="1.6"></path>' for dx in (-14, -6, 6, 14))
                          + '<circle cx="-6" cy="-10" r="5" fill="#E8A317" stroke="#0D0D0F" stroke-width="1.2"></circle><circle cx="6" cy="-12" r="5" fill="#E8A317" stroke="#0D0D0F" stroke-width="1.2"></circle></g>')
    return (sun(w * 0.86, h * 0.2, 16, color="#FFE680", op=0.35) + ground(w, h, base, "#C8A06A", dy=0) + S.grain(-10, w * 0.5, base + 6, h * 0.3, seed)
            + plant(w * 0.66, base + 4) + plant(w * 0.76, base + 8)
            + K.lad(p, w * 0.86, base + 4, fit(base, h * 0.5), cloth="#C8902E", flip=True, up=[(-22, -158), (-40, -130), (-56, -116)]))

def speckled(p, w, h, seed, labels=True):
    """Every speckled and spotted one, and every black one among the sheep: a flock sorted into two."""
    base = h * 0.86; r = random.Random(seed); o = [ground(w, h, base - 30, "#8AAA5A", dy=0)]
    o.append(f'<path d="M{f(w * 0.5)} {f(base - 40)} L {f(w * 0.5)} {f(h + 10)}" stroke="#F3EFE6" stroke-width="3" stroke-dasharray="10 8"></path>')
    for i in range(9):
        o.append(E.sheep(w * r.uniform(0.04, 0.44), base + r.uniform(-20, 20), 0.3, flip=r.random() < 0.5, wool="#F3EFE6"))
    for i in range(9):
        k = r.choice(["goat", "sheep", "black"])
        o.append(E.sheep(w * r.uniform(0.56, 0.96), base + r.uniform(-20, 20), 0.3, flip=r.random() < 0.5, wool="#1A1210", face="#0D0D0F") if k == "black"
                 else spotted(w * r.uniform(0.56, 0.96), base + r.uniform(-20, 20), 0.3, flip=r.random() < 0.5, kind=k, seed=seed + i))
    if labels: o.append(label(w * 0.25, base - 46, "LABAN'S", "#12113A", 11) + label(w * 0.75, base - 46, "JACOB'S HIRE", "#12113A", 11))
    return "".join(o)

def three_days(w, h, seed):
    """He set three days' journey betwixt himself and Jacob: two flocks on the map, three day-marks between."""
    o = [grid_bg(w, h, color="#2A3A1E", bg="#0E1A0A")]
    o.append(route([(w * 0.14, h * 0.6), (w * 0.86, h * 0.6)], color="#9CCB5E", sw=2.4, arrow=False))
    o.append(node(w * 0.14, h * 0.6, "JACOB", "#FFD23F", r=6, dy=-14) + node(w * 0.86, h * 0.6, "LABAN'S SONS", "#D7261E", r=6, dy=-14))
    for i in range(3):
        x = w * (0.32 + i * 0.18)
        o.append(f'<path d="M{f(x)} {f(h * 0.56)} L {f(x)} {f(h * 0.64)}" stroke="#9CCB5E" stroke-width="3"></path>' + label(x, h * 0.74, f"DAY {i + 1}", "#9CCB5E", 9))
    return "".join(o)

def rods(p, w, h, seed):
    """Rods of poplar, almond and plane, peeled in white streaks, set in the watering-troughs before the flocks."""
    base = h * 0.86; r = random.Random(seed)
    o = [sun(w * 0.86, h * 0.18, 14, op=0.3), ground(w, h, base - 20, "#8AAA5A", dy=0), R6.trough(w * 0.5, base, w * 0.7)]
    for i in range(7):
        x = w * (0.2 + i * 0.1)
        o.append(f'<path d="M{f(x)} {f(base - 20)} L {f(x + 6)} {f(base - h * 0.5)}" stroke="#5A3A22" stroke-width="7" stroke-linecap="round"></path>')
        o += [f'<path d="M{f(x + 6 * t)} {f(base - 20 - (h * 0.5 - 20) * t)} l 6 -8" stroke="#F3EFE6" stroke-width="3"></path>' for t in (0.2, 0.4, 0.6, 0.8)]
    for i in range(6):
        o.append(spotted(w * (0.16 + i * 0.14), base + 18, 0.3, flip=i % 2 == 1, kind=r.choice(["goat", "sheep"]), seed=seed + i))
    return "".join(o)

def increase(p, w, h, seed):
    """The man increased exceedingly, and had large flocks, and maid-servants and men-servants, and camels and asses."""
    base = h * 0.66
    return (sun(w * 0.86, h * 0.2, 18, color="#FFE680", op=0.3) + ground(w, h, base, "#8AAA5A", dy=0)
            + Z.caravan(p, w * 0.5, w * 0.96, base + 10, 0.7, seed)
            + "".join(spotted(w * (0.04 + i * 0.07), base + 30 + (i % 3) * 22, 0.28 + (i % 3) * 0.04, flip=i % 2 == 0, kind=("goat", "sheep")[i % 2], seed=seed + i) for i in range(13))
            + jacob_man(p, w * 0.12, h * 0.96, fit(h * 0.96, h * 0.5), staff=True, up=HOLD_STAFF))
