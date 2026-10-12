"""New drawings for Genesis chapter 9 (Genesis 31–33): the flight from Laban, the teraphim, the pursuit to Gilead,
the heap of witness, Mahanaim, the present for Esau, the ford of the Jabbok, the meeting, Succoth and Shechem."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus4 as E4, exodus5 as V, joshua1 as J, judges1 as G1, judges2 as S, samuel1 as A, samuel4 as A4, numbers1 as N
from faces_ex import F
from genesis import art2 as Y, art3 as Z, art4 as Q, art5 as K, art6 as R6, art7 as J7, art8 as L
from genesis.art2 import fit, ground, hills, birds, city, SKIN
from genesis.art3 import sun, label, man, woman, grid_bg, node, route, STAFF, HOLD_STAFF, GREY_BEARD
from genesis.art7 import esau, goat, tent_inside
from genesis.art8 import rachel, leah, laban, jacob_man, spotted, RACHEL_ROBE, LEAH_ROBE, BILHAH_ROBE, ZILPAH_ROBE
def f(v): return f"{v:.1f}"

# ---- faces ----------------------------------------------------------------------------------------------
JACOB = L.JACOB_MAN
JACOB_AFRAID = F("adam", skin="#C98E66", shadow="#4A3A5A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", brow="sorrow", sweat=True, light="#9A8AFF")
JACOB_PRAY = F("adam", skin="#B9A6B8", shadow="#4A3A6E", hair="#2A1A10", hl="#6A5A7E", beard=True, beard_color="#2A1A10", brow="sorrow", light="#FFF4C2")
JACOB_WROTH = L.JACOB_ANGRY
LABAN, LABAN_SLY = L.LABAN, L.LABAN_SLY
LABAN_HOT = F("adam", skin="#C47A5A", shadow="#4A1A16", hair="#5A5650", hl="#8A867E", beard=True, beard_color="#4A4640", scarf="#9A3A1E", cord=True, brow="scowl", light="#FF6A4A")
RACHEL, LEAH = L.RACHEL, L.LEAH
RACHEL_SLY = F("eve", skin="#E3B08A", shadow="#8A5A4A", hair="#1A1210", brow="scowl", light="#FFC14D")
ESAU_OLD = F("adam", skin="#C47A5A", shadow="#8A4A32", hair="#B5421E", hl="#E06A3A", beard=True, beard_color="#B5421E", light="#FFC14D")
ESAU_WEEP = F("adam", skin="#C47A5A", shadow="#6A3A3A", hair="#B5421E", hl="#E06A3A", beard=True, beard_color="#B5421E", tear=True, light="#FFF4C2")

# ---- people ---------------------------------------------------------------------------------------------
def esau_old(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body="#8A4A2E", cloth=J7.ESAU_TUNIC, kind="Robe", sw=3, flip=flip, up=up,
                     extra=GREY_BEARD.replace("#B8B2A6", "#B5421E"))

def teraphim(x, y, s=1.0):
    """Small household figures of clay: three squat idols with folded arms (the teraphim)."""
    one = lambda dx, hh, c: (f'<g transform="translate({f(x + dx * s)} {f(y)}) scale({f(s)})"><path d="M-8 0 L -10 -{hh} C -10 -{hh + 10} 10 -{hh + 10} 10 -{hh} L 8 0 Z" fill="{c}" stroke="#0D0D0F" stroke-width="1.6"></path>'
                             f'<circle cx="0" cy="-{hh + 12}" r="7" fill="{c}" stroke="#0D0D0F" stroke-width="1.6"></circle>'
                             f'<path d="M-8 -{hh - 8} L 8 -{hh - 8}" stroke="#0D0D0F" stroke-width="1.6"></path><circle cx="-2" cy="-{hh + 13}" r="1.2" fill="#0D0D0F"></circle><circle cx="3" cy="-{hh + 13}" r="1.2" fill="#0D0D0F"></circle></g>')
    return one(-22, 22, "#B5652E") + one(0, 30, "#C8885A") + one(22, 24, "#9A5A3A")

# ---- Genesis 31 -----------------------------------------------------------------------------------------
def muttering(p, w, h, seed):
    """Laban's sons whispering together; Laban's face turned away; Jacob watching from the flock."""
    base = h * 0.88; s = fit(base, h * 0.58)
    return (sun(w * 0.86, h * 0.2, 14, op=0.25) + ground(w, h, base, "#8AAA5A", dy=0)
            + Z.flock(w * 0.02, w * 0.3, base - 4, base + 20, 6, seed, cows=0, smin=0.22, smax=0.28)
            + jacob_man(p, w * 0.22, base, s, staff=True, up=HOLD_STAFF)
            + man(p, w * 0.62, base, s, "#9A3A1E", flip=True) + man(p, w * 0.72, base, s, "#7A3A2A") + man(p, w * 0.82, base, s, "#B5652E", flip=True)
            + mk.speed(w * 0.72, base - h * 0.5, 10, 10, 40, seed, color="#D7261E", op=0.5))

def field_council(p, w, h, seed):
    """Jacob called Rachel and Leah to the field unto his flock."""
    base = h * 0.88; s = fit(base, h * 0.42)
    return (sun(w * 0.86, h * 0.2, 14, op=0.25) + ground(w, h, base, "#8AAA5A", dy=0)
            + Z.flock(w * 0.6, w * 0.98, base - 4, base + 20, 8, seed, cows=0, smin=0.2, smax=0.28)
            + rachel(p, w * 0.14, base, s * 0.95) + leah(p, w * 0.26, base, s * 0.95) + jacob_man(p, w * 0.44, base, s, flip=True, staff=True, up=HOLD_STAFF))

def he_goats(p, w, h, seed):
    """In a dream: the he-goats which leaped upon the flock were ringstreaked, speckled, and grizzled."""
    base = h * 0.84; r = random.Random(seed)
    o = [mk.stars(70, w, h * 0.6, seed), V.rays(w * 0.5, -30, 30, 30, h * 1.4, color="#FFF4C2", op=0.2), ground(w, h, base, "#1A2A1A", dy=0)]
    for i in range(7):
        o.append(spotted(w * (0.08 + i * 0.14), base + r.uniform(-6, 18), 0.42 + r.uniform(-0.04, 0.04), flip=i % 2 == 0, kind="goat", seed=seed + i)
                 + f'<path d="M{f(w * (0.08 + i * 0.14) + 20)} {f(base - 52)} c 10 -10 20 -4 18 6" fill="none" stroke="#8A6A3A" stroke-width="3"></path>')
    return "".join(o)

def camels_away(p, w, h, seed):
    """He set his sons and his wives upon the camels, and carried away all his cattle and all his substance."""
    base = h * 0.82; o = [sun(w * 0.9, base - 6, h * 0.2, color="#FFC14D", op=0.3), ground(w, h, base, "#C8A06A", dy=0)]
    for i, c in enumerate([RACHEL_ROBE, LEAH_ROBE, BILHAH_ROBE, ZILPAH_ROBE]):
        o.append(G1.camel(w * (0.2 + i * 0.15), base + (i % 2) * 6, 0.36, rider=c))
    o.append(jacob_man(p, w * 0.82, base + 4, fit(base, h * 0.4), staff=True, up=HOLD_STAFF))
    o.append(Z.flock(w * 0.04, w * 0.9, base + 12, h * 1.0, 14, seed, cows=0.3, smin=0.2, smax=0.3))
    return "".join(o)

def stolen_gods(p, w, h, seed):
    """Laban was gone to shear his sheep, and Rachel stole the teraphim: her hands closing on three small figures in the dark."""
    o = [tent_inside(w, h, 0.25), ground(w, h, h * 0.84, "#2A1408", dy=0), teraphim(w * 0.5, h * 0.84, h / 120)]
    hand = lambda x, flip: (f'<path d="M{f(x)} {f(h * 0.5)} C {f(x + (40 if not flip else -40))} {f(h * 0.56)} {f(x + (70 if not flip else -70))} {f(h * 0.62)} {f(x + (90 if not flip else -90))} {f(h * 0.62)}" '
                            f'fill="none" stroke="#0D0D0F" stroke-width="26" stroke-linecap="round"></path>'
                            f'<path d="M{f(x)} {f(h * 0.5)} C {f(x + (40 if not flip else -40))} {f(h * 0.56)} {f(x + (70 if not flip else -70))} {f(h * 0.62)} {f(x + (90 if not flip else -90))} {f(h * 0.62)}" '
                            f'fill="none" stroke="{RACHEL_ROBE}" stroke-width="20" stroke-linecap="round"></path>'
                            f'<ellipse cx="{f(x + (100 if not flip else -100))}" cy="{f(h * 0.62)}" rx="14" ry="10" fill="#E3B08A" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    return "".join(o) + hand(-10, False) + hand(w + 10, True)

def gilead_map(w, h, seed, pursue=False):
    """Haran, the River, the mountain of Gilead: Jacob's flight on the map, and Laban's pursuit behind him."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.5)} -10 C {f(w * 0.54)} {f(h * 0.3)} {f(w * 0.6)} {f(h * 0.6)} {f(w * 0.66)} {f(h + 10)}" fill="none" stroke="#2C9DB8" stroke-width="5" opacity="0.8"></path>')
    o.append(label(w * 0.6, h * 0.16, "THE RIVER", "#8FD0E2", 9, "start"))
    o.append(f'<path d="M{f(w * 0.1)} {f(h * 0.7)} L {f(w * 0.2)} {f(h * 0.5)} L {f(w * 0.3)} {f(h * 0.7)} Z" fill="#3A4A2E" stroke="#9CCB5E" stroke-width="2"></path>')
    o.append(route([(w * 0.86, h * 0.3), (w * 0.56, h * 0.42), (w * 0.22, h * 0.56)], color="#FFD23F", sw=3))
    if pursue: o.append(route([(w * 0.92, h * 0.4), (w * 0.6, h * 0.5), (w * 0.3, h * 0.6)], color="#D7261E", sw=2.4, dash="4 4"))
    o.append(node(w * 0.86, h * 0.3, "HARAN", "#FFD23F", r=5, dy=-12) + node(w * 0.2, h * 0.5, "GILEAD", "#9CCB5E", r=5, dy=-14))
    return "".join(o)

def overtake(p, w, h, seed):
    """Laban took his brethren with him and pursued after him seven days' journey."""
    base = h * 0.86; r = random.Random(seed)
    o = [sun(w * 0.1, h * 0.2, 14, op=0.25), hills(w, h, base - h * 0.2, seed, color="#5A6A4A", amp=12), ground(w, h, base, "#B5A06A", dy=0)]
    o.append(G1.camel(w * 0.66, base, 0.4, flip=True, rider=L.LABAN_ROBE))
    o += [G1.camel(w * (0.78 + i * 0.08), base + 4 + i * 2, 0.32, flip=True, rider=r.choice(["#7A3A2A", "#9A5A3A", "#5A3A22"])) for i in range(3)]
    o.append(mk.speed(w * 0.9, base - h * 0.2, 16, 20, w * 0.3, seed, color="#F3EFE6", op=0.6))
    return "".join(o)

def mount_camps(p, w, h, seed):
    """Jacob had pitched his tent in the mountain, and Laban with his brethren encamped in the mountain of Gilead."""
    base = h * 0.86
    return (sun(w * 0.5, h * 0.2, 14, color="#FFE680", op=0.25)
            + f'<path d="M-10 {f(base)} L {f(w * 0.3)} {f(h * 0.34)} L {f(w * 0.5)} {f(h * 0.46)} L {f(w * 0.7)} {f(h * 0.3)} L {f(w + 10)} {f(base)} Z" fill="#5A6A4A" stroke="#0D0D0F" stroke-width="2"></path>'
            + ground(w, h, base, "#7A8A5A", dy=0) + "".join(E4.tent(w * x, base - h * 0.08, w * 0.1, h * 0.18) for x in (0.14, 0.26))
            + "".join(E4.tent(w * x, base - h * 0.06, w * 0.1, h * 0.18, color="#7A3A2A") for x in (0.72, 0.84))
            + label(w * 0.2, base + 16, "JACOB", "#12113A", 10) + label(w * 0.78, base + 16, "LABAN", "#12113A", 10))

def tents_searched(p, w, h, seed):
    """Laban went into Jacob's tent, and Leah's tent, and the tent of the two maid-servants, and Rachel's tent."""
    base = h * 0.86; o = [sun(w * 0.9, h * 0.2, 14, op=0.25), ground(w, h, base, "#B5A06A", dy=0)]
    for i, (nm, c) in enumerate([("JACOB", "#5A6E8A"), ("LEAH", LEAH_ROBE), ("MAID-SERVANTS", BILHAH_ROBE), ("RACHEL", RACHEL_ROBE)]):
        x = w * (0.13 + i * 0.25)
        o.append(G1.tent_big(x, base, w * 0.2, h * 0.5, color="#3A2214", glow="#12090A" if i < 3 else "#FFC14D")
                 + f'<rect x="{f(x - w * 0.09)}" y="{f(base + 6)}" width="{f(w * 0.18)}" height="18" fill="{c}"></rect>' + label(x, base + 19, nm, "#F3EFE6", 9))
        if i < 3: o.append(f'<path d="M{f(x - 14)} {f(base - h * 0.3)} l 28 28 m 0 -28 l -28 28" stroke="#D7261E" stroke-width="5"></path>')
    o.append(laban(p, w * 0.68, base, fit(base, h * 0.36), up=[(-22, -158), (2, -150), (26, -150)]))
    return "".join(o)

def saddle_seat(p, w, h, seed):
    """Rachel put the teraphim in the camel's saddle, and sat upon them: inside the tent, seated on the saddle."""
    base = h * 0.88
    saddle = (f'<path d="M{f(w * 0.3)} {f(base)} L {f(w * 0.32)} {f(base - 50)} C {f(w * 0.36)} {f(base - 70)} {f(w * 0.56)} {f(base - 70)} {f(w * 0.6)} {f(base - 50)} L {f(w * 0.62)} {f(base)} Z" '
              f'fill="#B5421E" stroke="#0D0D0F" stroke-width="2.4"></path>'
              + "".join(f'<path d="M{f(w * (0.33 + i * 0.07))} {f(base - 56)} L {f(w * (0.33 + i * 0.07))} {f(base)}" stroke="#E8B830" stroke-width="3"></path>' for i in range(5)))
    return (tent_inside(w, h, 0.32) + ground(w, h, base, "#2A1408", dy=0) + saddle
            + mk.person(p, round(w * 0.46), round(base - 56), fit(base - 56, h * 0.16) * 0.62, body=SKIN, cloth=RACHEL_ROBE, woman=True, hair="#1A1210", sw=3)
            + f'<rect x="{f(w * 0.4)}" y="{f(base - 70)}" width="{f(w * 0.12)}" height="16" fill="{RACHEL_ROBE}" stroke="#0D0D0F" stroke-width="2"></rect>'
            + laban(p, w * 0.82, base, fit(base, h * 0.36), flip=True, up=[(-22, -158), (-40, -126), (-58, -110)]))

def drought_frost(w, h, seed):
    """In the day the drought consumed me, and the frost by night: the day half burning, the night half frozen."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w / 2 + 10)}" height="{f(h + 20)}" fill="#E8A35A"></rect>',
         f'<rect x="{f(w / 2)}" y="-10" width="{f(w / 2 + 10)}" height="{f(h + 20)}" fill="#1A2440"></rect>',
         sun(w * 0.24, h * 0.3, 26, color="#FFF4C2", op=0.5), f'<circle cx="{f(w * 0.76)}" cy="{f(h * 0.3)}" r="18" fill="#E8E2D6"></circle>',
         mk.stars(40, w / 2, h * 0.6, seed).replace("<g ", f'<g transform="translate({f(w / 2)} 0)" ', 1)]
    o += [f'<g transform="translate({f(w * 0.5 + r.uniform(10, w * 0.48))} {f(r.uniform(h * 0.4, h * 0.95))})" stroke="#CFEFFF" stroke-width="2"><path d="M-6 0 L 6 0 M0 -6 L 0 6 M-4 -4 L 4 4 M-4 4 L 4 -4"></path></g>' for _ in range(10)]
    o.append(ground(w, h, h * 0.84, "#5A4A3A", dy=0) + Z.flock(w * 0.04, w * 0.96, h * 0.84, h * 0.96, 10, seed, cows=0, smin=0.2, smax=0.26))
    return "".join(o)

def heap_of_witness(p, w, h, seed, eating=True):
    """A pillar set up, and a heap of stones gathered by Jacob's brethren; they did eat there by the heap."""
    base = h * 0.86; r = random.Random(seed)
    o = [sun(w * 0.86, h * 0.2, 14, color="#FFE680", op=0.25), hills(w, h, base - h * 0.14, seed, color="#5A6A4A", amp=10), ground(w, h, base, "#8A8A6A", dy=0),
         A4.stone_heap(w * 0.46, base + 4, w * 0.26, h * 0.24),
         f'<rect x="{f(w * 0.62)}" y="{f(base - h * 0.4)}" width="{f(w * 0.05)}" height="{f(h * 0.4)}" rx="5" fill="#8A8478" stroke="#0D0D0F" stroke-width="2.2"></rect>']
    if eating:
        o += [E.kneel(w * x, base + 2, round(h / 620, 3), color=c, skin=SKIN, flip=x > 0.5) for x, c in [(0.12, "#5A6E8A"), (0.2, "#7A5A3A"), (0.28, "#5A3A22"), (0.78, "#9A3A1E"), (0.86, "#7A3A2A"), (0.94, "#B5652E")]]
    return "".join(o)

def mizpah(w, h, seed):
    """Galeed and Mizpah: the heap and the pillar as a boundary on the map; neither shall pass over it for harm."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.5)} -10 L {f(w * 0.5)} {f(h + 10)}" stroke="#D7261E" stroke-width="3" stroke-dasharray="10 6"></path>')
    o.append(A4.stone_heap(w * 0.5, h * 0.66, w * 0.16, h * 0.2))
    o.append(label(w * 0.2, h * 0.9, "JACOB", "#FFD23F", 12) + label(w * 0.8, h * 0.9, "LABAN", "#FFD23F", 12))
    return "".join(o)

def kissed_goodbye(p, w, h, seed):
    """Early in the morning Laban kissed his sons and his daughters, and blessed them, and departed."""
    base = h * 0.86; s = fit(base, h * 0.42)
    return (sun(w * 0.9, base - 10, h * 0.2, color="#FFC14D", op=0.3) + ground(w, h, base, "#8A8A6A", dy=0)
            + laban(p, w * 0.3, base, s, up=[(-22, -158), (-30, -196), (-36, -232)]) + rachel(p, w * 0.42, base, s * 0.95, flip=True) + leah(p, w * 0.52, base, s * 0.95, flip=True)
            + "".join(K.lad(p, w * (0.62 + i * 0.07), base, s * (0.5 + 0.04 * i), cloth=c, flip=True) for i, c in enumerate(["#C8902E", "#5A6A3A", "#1F7A8C", "#8A6AB8"])))

def gods_host(p, w, h, seed):
    """The angels of God met him: figures of light in the sky over the road; Mahanaim."""
    base = h * 0.86; r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A5E"></rect>', V.rays(w * 0.5, -30, 30, 30, h * 1.4, color="#FFF4C2", op=0.3),
         ground(w, h, base, "#3A2A4E", dy=0)]
    for i in range(7):
        x, y, s = w * (0.1 + i * 0.13), h * (0.2 + r.uniform(0, 0.3)), r.uniform(0.6, 1.0)
        o.append(Q.light_figure(x, y + 60 * s, 0.3 * s))
    o.append(jacob_man(p, w * 0.5, base + 4, fit(base, h * 0.6), staff=True, up=HOLD_STAFF))
    return "".join(o)

# ---- Genesis 32 -----------------------------------------------------------------------------------------
def messengers(p, w, h, seed):
    """Jacob sent messengers before him to Esau his brother unto the land of Seir, the field of Edom."""
    base = h * 0.86
    return (sun(w * 0.1, h * 0.3, 16, color="#FF8A3D", op=0.3) + f'<path d="M{f(w * 0.6)} {f(base)} L {f(w * 0.8)} {f(h * 0.3)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(base)} Z" fill="#B5421E" stroke="#0D0D0F" stroke-width="2"></path>'
            + label(w * 0.86, h * 0.26, "SEIR", "#F3EFE6", 10) + ground(w, h, base, "#C8A06A", dy=0)
            + A4.runner(p, w * 0.4, base + 2, fit(base, h * 0.5), cloth="#F3EFE6") + A4.runner(p, w * 0.54, base + 4, fit(base, h * 0.52), cloth="#E8D8B0"))

def four_hundred(p, w, h, seed):
    """He cometh to meet thee, and four hundred men with him: a long dark line on the ridge."""
    base = h * 0.8
    return (sun(w * 0.86, h * 0.3, 16, color="#FF8A3D", op=0.3) + hills(w, h, base, seed, color="#8A4A2E", amp=6)
            + E4.warriors(p, 60, w * 0.04, w * 0.96, base - h * 0.06, base + 4, seed, 0.08, 0.12, cloth=("#5A2A16", "#8A3A1E", "#3A2214")))

def two_companies(p, w, h, seed):
    """He divided the people, the flocks, the herds and the camels into two companies."""
    base = h * 0.84
    o = [ground(w, h, base - 20, "#B5A06A", dy=0), f'<path d="M{f(w * 0.5)} {f(base - 30)} L {f(w * 0.5)} {f(h + 10)}" stroke="#F3EFE6" stroke-width="3" stroke-dasharray="10 8"></path>']
    for side in (0, 1):
        x0 = w * (0.04 + side * 0.52)
        o.append(G1.camel(x0 + w * 0.1, base - 6, 0.3, rider="#5A6E8A" if side else None) + G1.camel(x0 + w * 0.26, base - 4, 0.28)
                 + Z.flock(x0, x0 + w * 0.42, base + 4, h * 1.0, 8, seed + side, cows=0.4, smin=0.2, smax=0.3))
    o.append(label(w * 0.25, h * 0.56, "I", "#12113A", 24) + label(w * 0.75, h * 0.56, "II", "#12113A", 24))
    return "".join(o).replace('font-family="IBM Plex Mono, monospace" font-weight="600" font-size="24"', 'font-family="Anton, sans-serif" font-weight="400" font-size="24"')

def droves(p, w, h, seed):
    """Every drove by itself, with a space betwixt drove and drove: she-goats, ewes, camels, kine, asses."""
    base = h * 0.72; r = random.Random(seed)
    o = [sun(w * 0.9, h * 0.2, 14, op=0.25), ground(w, h, base - 30, "#B5A06A", dy=0)]
    groups = [("220 GOATS", lambda x, y: goat(x, y, 0.26)), ("220 SHEEP", lambda x, y: E.sheep(x, y, 0.26)),
              ("30 CAMELS", lambda x, y: G1.camel(x, y - 4, 0.18)), ("50 KINE", lambda x, y: A.cow(x, y, 0.18, color="#8A5A30")), ("30 ASSES", lambda x, y: N.ass(x, y, 0.11))]
    for i, (nm, draw) in enumerate(groups):
        x0 = w * (0.02 + i * 0.2)
        for k in range(4):
            o.append(draw(x0 + w * 0.03 + (k % 2) * w * 0.07, base + (k // 2) * 18 - 6))
        o.append(f'<rect x="{f(x0 + w * 0.01)}" y="{f(base + 30)}" width="{f(w * 0.17)}" height="16" fill="#12113A"></rect>' + label(x0 + w * 0.095, base + 42, nm, "#FFD23F", 8.5, ls=0.06))
    return "".join(o)

def ford_jabbok(p, w, h, seed):
    """He passed over the ford of the Jabbok by night, and sent over all that he had; and Jacob was left alone."""
    base = h * 0.84
    river = f'M-10 {f(h * 0.5)} C {f(w * 0.3)} {f(h * 0.44)} {f(w * 0.7)} {f(h * 0.62)} {f(w + 10)} {f(h * 0.54)} L {f(w + 10)} {f(h * 0.72)} C {f(w * 0.7)} {f(h * 0.8)} {f(w * 0.3)} {f(h * 0.62)} -10 {f(h * 0.68)} Z'
    o = [mk.stars(70, w, h * 0.4, seed), f'<circle cx="{f(w * 0.85)}" cy="{f(h * 0.14)}" r="14" fill="#E8E2D6"></circle>', ground(w, h, h * 0.46, "#1A1430", dy=0),
         f'<path d="{river}" fill="#1F3F5A" stroke="#0D0D0F" stroke-width="2"></path>']
    o += [mk.person(p, round(w * x), round(h * 0.46), 0.14, body="#12090A", woman=i % 2 == 0, flip=True) for i, x in enumerate((0.56, 0.62, 0.68, 0.74, 0.8))]
    o.append(jacob_man(p, w * 0.22, base, fit(base, h * 0.5)))
    return "".join(o)

def unto_this_day(w, h, seed):
    """Unto this day: the ford of the Jabbok in the morning light, empty."""
    river = f'M-10 {f(h * 0.6)} C {f(w * 0.3)} {f(h * 0.54)} {f(w * 0.7)} {f(h * 0.72)} {f(w + 10)} {f(h * 0.64)} L {f(w + 10)} {f(h * 0.82)} C {f(w * 0.7)} {f(h * 0.9)} {f(w * 0.3)} {f(h * 0.72)} -10 {f(h * 0.78)} Z'
    return (sun(w * 0.76, h * 0.5, 30, color="#FFC14D", op=0.35) + hills(w, h, h * 0.52, seed, color="#5A4A6A", amp=10)
            + ground(w, h, h * 0.56, "#7A6A5A", dy=0) + f'<path d="{river}" fill="#2C7DA0" stroke="#0D0D0F" stroke-width="2"></path>')

def sinew(w, h, seed):
    """The sinew of the hip upon the hollow of the thigh: a plain anatomical diagram, gold on indigo."""
    o = [grid_bg(w, h, color="#2A2A5A", bg="#12113A")]
    o.append(f'<path d="M{f(w * 0.36)} {f(h * 0.2)} C {f(w * 0.3)} {f(h * 0.4)} {f(w * 0.34)} {f(h * 0.7)} {f(w * 0.4)} {f(h * 0.9)} L {f(w * 0.52)} {f(h * 0.9)} C {f(w * 0.5)} {f(h * 0.7)} {f(w * 0.52)} {f(h * 0.4)} {f(w * 0.6)} {f(h * 0.2)} Z" fill="none" stroke="#8F9AFF" stroke-width="2.4"></path>')
    o.append(f'<path d="M{f(w * 0.44)} {f(h * 0.26)} C {f(w * 0.42)} {f(h * 0.46)} {f(w * 0.44)} {f(h * 0.66)} {f(w * 0.46)} {f(h * 0.86)}" fill="none" stroke="#FFD23F" stroke-width="4"></path>')
    o.append(f'<circle cx="{f(w * 0.45)}" cy="{f(h * 0.32)}" r="14" fill="none" stroke="#D7261E" stroke-width="3"></circle>' + label(w * 0.62, h * 0.33, "THE HOLLOW OF THE THIGH", "#FFD23F", 9, "start"))
    return "".join(o)

# ---- Genesis 33 -----------------------------------------------------------------------------------------
def ordered(p, w, h, seed):
    """The handmaids and their children foremost, Leah and her children after, and Rachel and Joseph hindermost."""
    base = h * 0.88; s = fit(base, h * 0.42); o = [ground(w, h, base, "#C8A06A", dy=0)]
    groups = [(0.82, BILHAH_ROBE, 2), (0.72, ZILPAH_ROBE, 2), (0.5, LEAH_ROBE, 7), (0.16, RACHEL_ROBE, 1)]
    for x, c, n in groups:
        o.append(woman(p, w * x, base, s * 0.95, c, flip=True))
        o += [K.lad(p, w * x - (16 + k * 12) * (1 if x > 0.3 else -1), base, s * 0.42, cloth=c, flip=True) for k in range(min(n, 4))]
    o.append(label(w * 0.16, base + 18, "RACHEL · JOSEPH", "#12113A", 9) + label(w * 0.5, base + 18, "LEAH", "#12113A", 9) + label(w * 0.77, base + 18, "THE HANDMAIDS", "#12113A", 9))
    return "".join(o)

def bowing_all(p, w, h, seed):
    """The handmaids came near with their children and bowed; Leah and her children; Joseph and Rachel."""
    base = h * 0.88; r = random.Random(seed); o = [ground(w, h, base, "#C8A06A", dy=0)]
    for i, c in enumerate([BILHAH_ROBE, ZILPAH_ROBE, LEAH_ROBE, LEAH_ROBE, LEAH_ROBE, RACHEL_ROBE]):
        o.append(E.kneel(w * (0.08 + i * 0.11), base + 2, round(h / (420 if i in (0, 1, 2, 5) else 640), 3), color=c, skin=SKIN))
    o.append(esau_old(p, w * 0.86, base, fit(base, h * 0.36), flip=True))
    return "".join(o)

def succoth(p, w, h, seed):
    """Jacob built him a house, and made booths for his cattle: therefore the place is called Succoth."""
    base = h * 0.86
    booth = lambda x: (f'<path d="M{f(x - 34)} {f(base)} L {f(x - 34)} {f(base - 50)} L {f(x + 34)} {f(base - 50)} L {f(x + 34)} {f(base)}" fill="none" stroke="#5A3A22" stroke-width="5"></path>'
                       f'<path d="M{f(x - 44)} {f(base - 50)} L {f(x + 44)} {f(base - 50)} L {f(x + 34)} {f(base - 64)} L {f(x - 34)} {f(base - 64)} Z" fill="#5E8F26" stroke="#0D0D0F" stroke-width="2"></path>')
    house = (f'<rect x="{f(w * 0.08)}" y="{f(base - h * 0.34)}" width="{f(w * 0.22)}" height="{f(h * 0.34)}" fill="#B59A7A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<rect x="{f(w * 0.16)}" y="{f(base - h * 0.16)}" width="{f(w * 0.06)}" height="{f(h * 0.16)}" fill="#3A2214"></rect>')
    return (sun(w * 0.86, h * 0.2, 14, op=0.25) + ground(w, h, base, "#9AAA5A", dy=0) + house + "".join(booth(w * x) for x in (0.46, 0.64, 0.82))
            + "".join(A.cow(w * x, base + 16, 0.22, color="#8A5A30") for x in (0.48, 0.66)) + E.sheep(w * 0.84, base + 18, 0.3))

def shechem_altar(p, w, h, seed):
    """He came in peace to the city of Shechem, bought the parcel of ground, and erected there an altar, El-Elohe-Israel."""
    base = h * 0.86
    return (sun(w * 0.5, h * 0.2, 16, color="#FFE680", op=0.3) + city(w * 0.84, base, w * 0.3, h * 0.46, seed, color="#8A6A5A", lit="#FFC14D", wall="#9A7A6A")
            + ground(w, h, base, "#9AAA5A", dy=0) + E4.tent(w * 0.16, base, w * 0.16, h * 0.24) + A4.altar(w * 0.44, base, round(h / 420, 3), seed=seed)
            + jacob_man(p, w * 0.6, base + 2, fit(base, h * 0.4), up=[(-22, -158), (-30, -196), (-36, -232)])
            + label(w * 0.84, base + 18, "SHECHEM", "#12113A", 10))
