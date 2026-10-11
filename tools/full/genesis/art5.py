"""New drawings for Genesis chapter 5 (Genesis 20–23): Abimelech of Gerar, the birth of Isaac, Hagar and the lad in
the wilderness of Beer-sheba, the oath at the well, Moriah, Nahor's house, and the cave of Machpelah."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, joshua1 as J, judges1 as G1, judges2 as S
import samuel1 as A, samuel2 as A2, samuel4 as A4, numbers1 as N, ruth1 as R
from faces_ex import F
from genesis import art2 as Y, art3 as Z, art4 as Q
from genesis.art2 import fit, ground, hills, birds, city, SKIN
from genesis.art3 import sun, label, man, woman, abram as abraham, grid_bg, node, route, STAFF, HOLD_STAFF, GREY_BEARD, CROWN
from genesis.art4 import hagar, sarah, shining
def f(v): return f"{v:.1f}"

# ---- faces ----------------------------------------------------------------------------------------------
ABRAHAM, ABRAHAM_GRAVE, ABRAHAM_AWE = Z.ABRAM, Z.ABRAM_GRAVE, Q.ABRAHAM_AWE
ABRAHAM_WEEP = F("adam", skin="#B98A6E", shadow="#5A4A5A", hair="#C8C2B6", hl="#8A867E", beard=True, brow="sorrow", tear=True)
ABIMELECH = F("adam", skin="#C98E66", shadow="#6A4A3A", hair="#1A1210", beard=True, beard_color="#1A1210", scarf="#1F5FAD", band=True, light="#FFC14D")
ABIMELECH_AFRAID = F("adam", skin="#A88A8A", shadow="#3A2A4A", hair="#1A1210", beard=True, beard_color="#1A1210", scarf="#1F5FAD", band=True, brow="sorrow", sweat=True, light="#9A8AFF")
ABIMELECH_STERN = F("adam", skin="#C47A5A", shadow="#5A1A16", hair="#1A1210", beard=True, beard_color="#1A1210", scarf="#1F5FAD", band=True, brow="scowl", light="#FF6A4A")
SARAH_JOY = F("eve", skin="#E3B08A", shadow="#A87050", hair="#C8C2B6", scarf="#8A3A5A", laugh=True, light="#FFF4C2")
SARAH_STERN = Q.SARAI_HURT
HAGAR, HAGAR_WEEP = Q.HAGAR, Q.HAGAR_WEEP
ISAAC = F("adam", skin="#E3B08A", shadow="#B97A58", hair="#5A3A22", hl="#8A6A4A", light="#FFE680")
EPHRON = F("adam", skin="#B98A6E", shadow="#6A4A3A", hair="#3A2A1E", hl="#6A5A4E", beard=True, beard_color="#3A2A1E", scarf="#B5652E", cord=True, light="#FFC14D")

# ---- people ---------------------------------------------------------------------------------------------
ABIMELECH_ROBE, ISAAC_TUNIC, ISHMAEL_TUNIC, HETH_ROBES = "#1F5FAD", "#E8D8B0", "#5A6A3A", ("#B5652E", "#7A5A3A", "#5A3A22", "#8A6A4A")

def abimelech(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=ABIMELECH_ROBE, sw=3, flip=flip, up=up, extra=CROWN)

def lad(p, x, y, s, cloth=ISHMAEL_TUNIC, flip=False, up=None, extra=""):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=cloth, kind="Tunic", sw=3, flip=flip, up=up, extra=extra)

def water_skin(x, y, s=1.0, empty=False):
    """A goatskin bottle of water (slack and folded when spent)."""
    if empty:
        return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-26 0 C -24 -8 20 -12 28 -2 C 22 4 -20 6 -26 0 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path></g>')
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-18 -4 C -28 -30 -10 -50 10 -46 C 28 -40 30 -14 18 0 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></path>'
            '<path d="M6 -46 L 10 -58 L 18 -56 L 14 -44" fill="#6A3A1E" stroke="#0D0D0F" stroke-width="1.6"></path></g>')

def shrub(x, y, s=1.0, seed=1):
    r = random.Random(seed)
    return "".join(f'<path d="M{f(x)} {f(y)} q {f(r.uniform(-30, 30) * s)} {f(-30 * s)} {f(r.uniform(-40, 40) * s)} {f(r.uniform(-50, -30) * s)}" fill="none" stroke="#5A6A3A" stroke-width="{f(3 * s)}" stroke-linecap="round"></path>' for _ in range(9))

def well(x, y, s=1.0, full=True):
    """A stone well-head with water in it."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><ellipse cx="0" cy="0" rx="46" ry="14" fill="#8A8478" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
            f'<ellipse cx="0" cy="-2" rx="34" ry="9" fill="{"#2C9DB8" if full else "#1A1410"}" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
            '<path d="M-46 0 L -46 18 C -30 30 30 30 46 18 L 46 0" fill="#A89E92" stroke="#0D0D0F" stroke-width="2.4"></path></g>')

def tamarisk(x, y, s=1.0, seed=1):
    """A young tamarisk: a slim trunk and feathery grey-green sprays."""
    r = random.Random(seed)
    sprays = "".join(f'<ellipse cx="{f(r.uniform(-40, 40))}" cy="{f(r.uniform(-150, -90))}" rx="{f(r.uniform(16, 28))}" ry="{f(r.uniform(28, 44))}" fill="{r.choice(["#7A9A7A", "#8AAA8A", "#6A8A6A"])}" stroke="#0D0D0F" stroke-width="1.6"></ellipse>' for _ in range(9))
    return f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-4 0 L -2 -100 M2 -60 L 20 -110 M-2 -70 L -24 -110" stroke="#5A3A22" stroke-width="5"></path>{sprays}</g>'

# ---- Genesis 20 -----------------------------------------------------------------------------------------
def gerar(p, w, h, seed):
    """Gerar in the South, between Kadesh and Shur: Abraham's tents outside a walled Philistine town."""
    base = h * 0.86
    return (sun(w * 0.86, h * 0.2, 16, op=0.3) + city(w * 0.72, base, w * 0.4, h * 0.4, seed, color="#C8A06A", lit="#1F5FAD", wall="#B59A7A")
            + ground(w, h, base, "#E8C88A", dy=0) + E4.tent(w * 0.16, base, w * 0.14, h * 0.22) + E4.tent(w * 0.3, base, w * 0.1, h * 0.16)
            + label(w * 0.72, base + 22, "GERAR", "#12113A", 11))

def taken(p, w, h, seed):
    """Abimelech king of Gerar sent, and took Sarah: two of the king's men leading her toward the gate."""
    base = h * 0.88; s = fit(base, h * 0.42)
    return (sun(w * 0.2, h * 0.2, 14, op=0.25) + A4.gatehouse(w * 0.84, base, w * 0.28, h * 0.66) + ground(w, h, base, "#C8A06A", dy=0)
            + abraham(p, w * 0.12, base, s) + man(p, w * 0.42, base, s, "#1F5FAD", flip=False) + sarah(p, w * 0.54, base, s * 0.95)
            + man(p, w * 0.66, base, s, "#1F5FAD"))

def dreamer(p, w, h, seed):
    """God came to Abimelech in a dream of the night: the king asleep on his couch under a shaft of light."""
    base = h * 0.82
    couch = (f'<rect x="{f(w * 0.3)}" y="{f(base - 24)}" width="{f(w * 0.5)}" height="24" rx="6" fill="#1F3F7A" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<path d="M{f(w * 0.32)} {f(base)} L {f(w * 0.32)} {f(base + 26)} M{f(w * 0.78)} {f(base)} L {f(w * 0.78)} {f(base + 26)}" stroke="#E8B830" stroke-width="6"></path>')
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0B0B2A"></rect>' + mk.stars(70, w, h * 0.6, seed)
            + f'<path d="M{f(w * 0.48)} -10 L {f(w * 0.62)} -10 L {f(w * 0.74)} {f(base)} L {f(w * 0.36)} {f(base)} Z" fill="#FFF4C2" opacity="0.28"></path>'
            + couch + f'<g transform="translate({f(w * 0.74)} {f(base - 22)}) scale({f(h / 330)})" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="2"><use href="#{p}LieB"></use><use href="#{p}LieA"></use></g>'
            + ground(w, h, base + 26, "#12102A", dy=0))

def servants_afraid(p, w, h, seed):
    """Abimelech rose early and told all these things in their ears, and the men were sore afraid."""
    base = h * 0.9; r = random.Random(seed)
    o = [sun(w * 0.86, base - h * 0.3, h * 0.12, color="#FFE680", op=0.3), ground(w, h, base, "#C8A06A", dy=0), abimelech(p, w * 0.16, base, fit(base, h * 0.36), up=[(-22, -158), (0, -170), (24, -186)])]
    for i in range(6):
        x = w * (0.4 + i * 0.1)
        o.append(E.kneel(x, base + 2, round(h / 560, 3), color=r.choice(["#F3EFE6", "#C8C2B6", "#8A6A4A"]), skin=SKIN, flip=True) if i % 2 else man(p, x, base, fit(base, h * 0.42), "#F3EFE6", flip=True))
    return "".join(o)

def restored(p, w, h, seed):
    """Abimelech took sheep and oxen, and men-servants and women-servants, and restored him Sarah his wife."""
    base = h * 0.86; s = fit(base, h * 0.42)
    return (ground(w, h, base, "#C8A06A", dy=0) + Z.flock(w * 0.46, w * 0.98, base - 4, base + 26, 10, seed, cows=0.4, smin=0.2, smax=0.32)
            + abraham(p, w * 0.12, base, s) + sarah(p, w * 0.24, base, s * 0.95, flip=True) + abimelech(p, w * 0.38, base, s, flip=True)
            + man(p, w * 0.9, base, s * 0.9, "#F3EFE6", flip=True) + woman(p, w * 0.8, base, s * 0.88, "#E8E2D6", flip=True))

def silver(w, h, seed):
    """A thousand pieces of silver: a heap of rings and bars, a counter."""
    r = random.Random(seed); o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#12113A"></rect>']
    for _ in range(90):
        x, y = w * 0.5 + r.gauss(0, w * 0.16), h * 0.8 - abs(r.gauss(0, h * 0.14))
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="9" ry="4" fill="{r.choice(["#C8C8D0", "#E8E8F0", "#A8A8B8"])}" stroke="#0D0D0F" stroke-width="1"></ellipse>')
    return "".join(o)

def prayer(p, w, h, seed):
    """Abraham prayed unto God, and God healed Abimelech: Abraham kneeling with hands up, light falling on the king's house."""
    base = h * 0.86
    return (V.rays(w * 0.7, -30, 30, 30, h * 1.4, color="#FFF4C2", op=0.35) + city(w * 0.78, base, w * 0.36, h * 0.36, seed, color="#C8A06A", lit="#FFD23F", wall="#B59A7A")
            + ground(w, h, base, "#C8A06A", dy=0) + E.kneel(w * 0.26, base + 2, round(h / 380, 3), color=Z.ABRAM_ROBE, skin=SKIN))

def mothers(p, w, h, seed):
    """And they bare children: women of the king's house, each with a newborn in her arms."""
    base = h * 0.88; s = fit(base, h * 0.42); o = [ground(w, h, base, "#C8A06A", dy=0)]
    for i, c in enumerate(["#1F5FAD", "#E8E2D6", "#C2456A", "#7A3BA8"]):
        x = w * (0.16 + i * 0.22)
        o.append(mk.person(p, round(x), round(base), s, body=SKIN, cloth=c, woman=True, hair="#1A1210", sw=3, flip=i % 2 == 1, up=R.HOLD_BABY, extra=R.baby(10, -130, 0.8)))
    return "".join(o)

# ---- Genesis 21 -----------------------------------------------------------------------------------------
def eighth_day(w, h, seed):
    """Isaac circumcised when he was eight days old: a swaddled infant on a blanket, eight lamps lit in a row."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A2E"></rect>']
    for i in range(8):
        x = w * (0.1 + i * 0.114)
        o.append(Q.clay_lamp(x, h * 0.32, 0.6))
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.74)}" rx="{f(w * 0.3)}" ry="{f(h * 0.1)}" fill="#8A3A5A" stroke="#0D0D0F" stroke-width="2"></ellipse>' + R.baby(w * 0.5, h * 0.7, 2.2))
    return "".join(o)

def weaning_feast(p, w, h, seed):
    """Abraham made a great feast on the day that Isaac was weaned: guests at a long cloth under the tents, music."""
    base = h * 0.9; r = random.Random(seed)
    o = [V.rays(w * 0.5, -30, 30, 30, h * 1.3, color="#FFF4C2", op=0.25), ground(w, h, h * 0.6, "#C8A06A", dy=0),
         G1.tent_big(w * 0.2, h * 0.62, w * 0.28, h * 0.4, color="#3A2214", glow="#FFC14D"), G1.tent_big(w * 0.8, h * 0.62, w * 0.28, h * 0.4, color="#3A2214", glow="#FFC14D"),
         f'<rect x="{f(w * 0.1)}" y="{f(h * 0.72)}" width="{f(w * 0.8)}" height="12" fill="#C2456A" stroke="#0D0D0F" stroke-width="2"></rect>']
    o += [f'<ellipse cx="{f(w * (0.14 + i * 0.07))}" cy="{f(h * 0.71)}" rx="12" ry="5" fill="#E8C88A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>' for i in range(11)]
    for i in range(9):
        x = w * (0.12 + i * 0.095)
        o.append(E.kneel(x, base, round(h / 560, 3), color=r.choice(["#5A3A22", "#2C4A7A", "#8A3A5A", "#5A6A3A", "#B5652E"]), skin=SKIN, flip=i % 2 == 1))
    return "".join(o)

def mocking(p, w, h, seed):
    """Sarah saw the son of Hagar mocking: a tall lad pointing and laughing at the little child by the tent."""
    base = h * 0.88
    return (ground(w, h, base, "#C8A06A", dy=0) + G1.tent_big(w * 0.86, base, w * 0.3, h * 0.6, color="#3A2214", glow="#5A2A12")
            + lad(p, w * 0.3, base, fit(base, h * 0.36), up=[(-22, -158), (4, -150), (30, -150)]) + lad(p, w * 0.58, base, fit(base, h * 0.66), cloth=ISAAC_TUNIC, flip=True)
            + sfx_marks(w * 0.3, h * 0.24))

def sfx_marks(x, y):
    return "".join(f'<path d="M{f(x + dx)} {f(y + dy)} l 10 -8" stroke="#D7261E" stroke-width="3" stroke-linecap="round"></path>' for dx, dy in [(30, 0), (40, 14), (34, 28)])

def sent_away(p, w, h, seed):
    """Abraham rose early, gave bread and a bottle of water to Hagar, putting it on her shoulder, and sent her away with the lad."""
    base = h * 0.88; s = fit(base, h * 0.42)
    return (sun(w * 0.9, base - 10, h * 0.16, color="#FFC14D", op=0.3) + ground(w, h, base, "#C8A06A", dy=0) + G1.tent_big(w * 0.12, base, w * 0.24, h * 0.56, color="#3A2214", glow="#5A2A12")
            + abraham(p, w * 0.3, base, s, up=[(-22, -158), (2, -150), (24, -164)])
            + hagar(p, w * 0.5, base, s * 0.95, flip=True, extra=water_skin(10, -160, 0.8).replace("translate(", "translate(", 1)) + lad(p, w * 0.64, base, s * 0.86, flip=True))

def bowshot(p, w, h, seed):
    """The water was spent; she cast the child under a shrub and sat a good way off, as it were a bowshot, and wept."""
    base = h * 0.86
    o = [sun(w * 0.5, h * 0.18, 20, color="#FFF4C2", op=0.45), ground(w, h, base, "#E8C88A", dy=0),
         shrub(w * 0.16, base, 1.3, seed), lad(p, w * 0.16, base + 6, fit(base, h * 0.56) * 0.8).replace("<g transform", '<g opacity="0.95" transform', 1),
         water_skin(w * 0.3, base + 8, 0.7, empty=True),
         f'<path d="M{f(w * 0.24)} {f(base + 10)} L {f(w * 0.72)} {f(base + 10)}" stroke="#8A6A4A" stroke-width="2" stroke-dasharray="8 6"></path>',
         label(w * 0.48, base + 26, "A BOWSHOT", "#12113A", 9),
         E.kneel(w * 0.78, base + 4, round(h / 420, 3), color=Q.HAGAR_ROBE, skin=SKIN, flip=True)]
    return "".join(o)

def well_opened(p, w, h, seed):
    """God opened her eyes, and she saw a well of water: she fills the bottle and gives the lad drink."""
    base = h * 0.86
    return (V.rays(w * 0.4, base - h * 0.2, 30, 30, w, color="#FFF4C2", op=0.4) + ground(w, h, base, "#E8C88A", dy=0) + well(w * 0.4, base - 6, h / 260)
            + hagar(p, w * 0.62, base + 4, fit(base, h * 0.36), flip=True, up=[(-22, -158), (-40, -126), (-58, -110)]) + lad(p, w * 0.82, base + 4, fit(base, h * 0.42), flip=True))

def archer(p, w, h, seed):
    """He grew, and dwelt in the wilderness, and became an archer: Ishmael with his bow in the wilderness of Paran."""
    return Z.hunter(p, w, h, seed).replace("#5A1A16", ISHMAEL_TUNIC)

def oath(p, w, h, seed):
    """Abimelech and Phicol the captain of his host speak unto Abraham at the well."""
    base = h * 0.88; s = fit(base, h * 0.42)
    phicol = '<path d="M14 -150 L 34 -270" stroke="#3A2214" stroke-width="4"></path><path d="M30 -270 L 38 -288 L 40 -268 Z" fill="#A8B0BA" stroke="#0D0D0F" stroke-width="1.2"></path>'
    return (sun(w * 0.5, h * 0.2, 14, op=0.25) + ground(w, h, base, "#C8A06A", dy=0) + well(w * 0.5, base - 2, h / 300)
            + abraham(p, w * 0.24, base, s) + abimelech(p, w * 0.72, base, s, flip=True) + man(p, w * 0.86, base, s, "#3A5A8A", flip=True, extra=phicol))

def seven_lambs(p, w, h, seed):
    """Seven ewe lambs of the flock set by themselves, a witness that Abraham had digged this well."""
    base = h * 0.84
    o = [ground(w, h, base - 20, "#9AAA5A", dy=0), well(w * 0.14, base - 10, h / 300),
         f'<ellipse cx="{f(w * 0.56)}" cy="{f(base + 6)}" rx="{f(w * 0.34)}" ry="{f(h * 0.1)}" fill="none" stroke="#FFD23F" stroke-width="2.4" stroke-dasharray="6 5"></ellipse>']
    o += [E3.lamb(w * (0.3 + i * 0.075), base + (8 if i % 2 else 0), 0.36) for i in range(7)]
    o += [label(w * (0.3 + i * 0.075), base - 40, f"{i + 1}", "#12113A", 10) for i in range(7)]
    return "".join(o)

def beersheba(p, w, h, seed):
    """Abraham planted a tamarisk tree in Beer-sheba, and called there on the name of Jehovah, the Everlasting God."""
    base = h * 0.86
    return (V.rays(w * 0.5, -30, 30, 30, h * 1.4, color="#FFF4C2", op=0.3) + ground(w, h, base, "#C8A06A", dy=0) + well(w * 0.18, base - 4, h / 320)
            + tamarisk(w * 0.62, base, h / 220, seed) + abraham(p, w * 0.82, base, fit(base, h * 0.42), up=[(-22, -158), (-30, -196), (-36, -232)], flip=True)
            + label(w * 0.18, base + 24, "BEER-SHEBA", "#12113A", 10))

# ---- Genesis 22 -----------------------------------------------------------------------------------------
def saddling(p, w, h, seed):
    """Abraham rose early and saddled his ass, and took two young men and Isaac, and clave the wood."""
    base = h * 0.88; s = fit(base, h * 0.42)
    wood = "".join(f'<path d="M{f(w * 0.12 + i * 8)} {f(base - 4 - i * 6)} l 70 -6" stroke="#8A5A30" stroke-width="7" stroke-linecap="round"></path>' for i in range(4))
    axe = '<path d="M14 -150 L 40 -220" stroke="#5A3A22" stroke-width="5"></path><path d="M34 -230 L 52 -220 L 44 -206 Z" fill="#A8B0BA" stroke="#0D0D0F" stroke-width="1.4"></path>'
    return (sun(w * 0.9, base - 6, h * 0.14, color="#FFC14D", op=0.3) + ground(w, h, base, "#9A8A6A", dy=0) + wood
            + abraham(p, w * 0.3, base, s, up=[(-22, -158), (4, -170), (14, -150)]).replace("</g>", axe + "</g>", 1)
            + N.ass(w * 0.52, base + 4, 0.24) + lad(p, w * 0.66, base, s * 0.85, cloth=ISAAC_TUNIC, flip=True)
            + man(p, w * 0.8, base, s * 0.96, "#5A3A22", flip=True) + man(p, w * 0.9, base, s * 0.96, "#8A6A4A", flip=True))

def afar_off(p, w, h, seed):
    """On the third day Abraham lifted up his eyes, and saw the place afar off: a lone mountain in the haze."""
    base = h * 0.88
    return (sun(w * 0.7, h * 0.3, 18, color="#FFE680", op=0.3)
            + f'<path d="M{f(w * 0.46)} {f(h * 0.7)} L {f(w * 0.7)} {f(h * 0.26)} L {f(w * 0.94)} {f(h * 0.7)} Z" fill="#9A8AAA" stroke="#0D0D0F" stroke-width="2" opacity="0.8"></path>'
            + hills(w, h, h * 0.72, seed, color="#8A7A5A", amp=8) + ground(w, h, base, "#7A6A4A", dy=0)
            + abraham(p, w * 0.2, base, fit(base, h * 0.36), staff=True, up=HOLD_STAFF) + hud_day(w * 0.86, h * 0.88))

def hud_day(x, y):
    return (f'<rect x="{f(x - 46)}" y="{f(y - 22)}" width="92" height="30" fill="#F3EFE6" stroke="#D7261E" stroke-width="2"></rect>'
            + label(x, y, "DAY 03", "#D7261E", 18).replace('font-family="IBM Plex Mono, monospace"', 'font-family="Anton, sans-serif"'))

def abide_here(p, w, h, seed):
    """Abide ye here with the ass: the two young men and the ass at the foot of the mountain; father and son going up."""
    base = h * 0.88
    return (f'<path d="M{f(w * 0.3)} {f(base)} L {f(w * 0.74)} {f(h * 0.1)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(base)} Z" fill="#7A6A5A" stroke="#0D0D0F" stroke-width="2"></path>'
            + ground(w, h, base, "#9A8A6A", dy=0) + N.ass(w * 0.12, base + 4, 0.2) + man(p, w * 0.2, base, fit(base, h * 0.5), "#5A3A22") + man(p, w * 0.27, base, fit(base, h * 0.5), "#8A6A4A")
            + abraham(p, w * 0.56, h * 0.56, 0.2, flip=True) + lad(p, w * 0.6, h * 0.52, 0.18, cloth=ISAAC_TUNIC, flip=True))

def altar_bound(p, w, h, seed):
    """Abraham built the altar there, and laid the wood in order, and bound Isaac and laid him on the altar: a silhouette on the summit."""
    base = h * 0.8
    return (V.rays(w * 0.5, base - 40, 36, 30, w, color="#FFD23F", op=0.3) + f'<circle cx="{f(w * 0.5)}" cy="{f(base - 30)}" r="{f(h * 0.3)}" fill="#FF8A3D" opacity="0.4"></circle>'
            + f'<path d="M-10 {f(h + 10)} L -10 {f(base + 20)} L {f(w * 0.3)} {f(base)} L {f(w * 0.7)} {f(base)} L {f(w + 10)} {f(base + 20)} L {f(w + 10)} {f(h + 10)} Z" fill="#2A140C" stroke="#0D0D0F" stroke-width="2"></path>'
            + A4.altar(w * 0.5, base, round(h / 300, 3), fire=False, seed=seed)
            + "".join(f'<path d="M{f(w * 0.36)} {f(base - 70 * h / 300 - i * 6)} L {f(w * 0.64)} {f(base - 70 * h / 300 - i * 6)}" stroke="#5A3418" stroke-width="5"></path>' for i in range(3))
            + f'<g transform="translate({f(w * 0.6)} {f(base - 84 * h / 300)}) scale({f(h / 520)})" fill="#12090A" stroke="#0D0D0F" stroke-width="2"><use href="#{p}LieB"></use></g>'
            + mk.person(p, round(w * 0.28), round(base), fit(base, h * 0.3), body="#12090A"))

def nahor_house(w, h, seed):
    """Milcah's eight sons to Nahor: eight nodes in a ring around one, Bethuel marked."""
    cx, cy = w * 0.7, h * 0.54; o = [mk.stars(50, w, h, seed)]
    names = ["UZ", "BUZ", "KEMUEL", "CHESED", "HAZO", "PILDASH", "JIDLAPH", "BETHUEL"]
    pts = []
    for i, nm in enumerate(names):                    # Bethuel, the last, lands lower right, clear of the caption
        a = -math.pi * 0.75 + i * 2 * math.pi / 8; x, y = cx + math.cos(a) * w * 0.24, cy + math.sin(a) * h * 0.36
        pts.append((nm, x, y))
        o.append(f'<path d="M{f(cx)} {f(cy)} L {f(x)} {f(y)}" stroke="#FFD23F" stroke-width="1.4" stroke-dasharray="4 4"></path>')
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="28" fill="#12113A" stroke="#FFD23F" stroke-width="3"></circle>' + label(cx, cy + 4, "NAHOR", "#FFD23F", 8.5, ls=0.06))
    for nm, x, y in pts:
        o.append(node(x, y, nm, "#D7261E" if nm == "BETHUEL" else "#FFD23F", r=5, dy=-10 if y < cy else 20, size=9))
    return "".join(o)

# ---- Genesis 23 -----------------------------------------------------------------------------------------
def mourning(p, w, h, seed):
    """Sarah died in Kiriath-arba, Hebron: the tent at dusk, Abraham bowed beside it."""
    base = h * 0.86
    return (sun(w * 0.82, base - 10, h * 0.2, color="#C2456A", op=0.2) + hills(w, h, base, seed, color="#2A1A2E", amp=6)
            + G1.tent_big(w * 0.36, base, w * 0.36, h * 0.6, color="#2A1A14", glow="#5A2A12") + E.kneel(w * 0.66, base + 2, round(h / 420, 3), color=Z.ABRAM_ROBE, skin=SKIN, flip=True)
            + label(w * 0.86, base + 22, "KIRIATH-ARBA", "#F3EFE6", 9))

def heth_gate(p, w, h, seed, ephron=False, bowing=False):
    """The children of Heth sitting at the gate of their city; Abraham standing (or bowing) before them."""
    base = h * 0.9; r = random.Random(seed)
    o = [A4.gatehouse(w * 0.62, base - h * 0.06, w * 0.5, h * 0.72), ground(w, h, base - h * 0.06, "#B59A7A", dy=0)]
    for i in range(7):
        x = w * (0.4 + i * 0.085)
        o.append(E.kneel(x, base, round(h / 600, 3), color=r.choice(HETH_ROBES), skin=SKIN, flip=True))
    if ephron: o.append(man(p, w * 0.32, base, fit(base, h * 0.36), "#B5652E", flip=True, kind="Robe"))
    o.append(E.kneel(w * 0.18, base + 2, round(h / 420, 3), color=Z.ABRAM_ROBE, skin=SKIN) if bowing else abraham(p, w * 0.16, base, fit(base, h * 0.36)))
    return "".join(o)

def shekels(w, h, seed):
    """Four hundred shekels of silver, current money with the merchant, weighed out on a balance."""
    r = random.Random(seed); cx, base = w * 0.5, h * 0.84
    beam = (f'<path d="M{f(cx)} {f(base)} L {f(cx)} {f(h * 0.3)}" stroke="#5A3A22" stroke-width="8"></path>'
            f'<path d="M{f(cx - w * 0.3)} {f(h * 0.34)} L {f(cx + w * 0.3)} {f(h * 0.3)}" stroke="#C8962E" stroke-width="6"></path>')
    pans = ""
    for dx, dy in [(-w * 0.3, h * 0.34), (w * 0.3, h * 0.3)]:
        pans += (f'<path d="M{f(cx + dx)} {f(dy)} L {f(cx + dx - 30)} {f(dy + 70)} M{f(cx + dx)} {f(dy)} L {f(cx + dx + 30)} {f(dy + 70)}" stroke="#0D0D0F" stroke-width="1.6"></path>'
                 f'<path d="M{f(cx + dx - 46)} {f(dy + 70)} C {f(cx + dx - 34)} {f(dy + 92)} {f(cx + dx + 34)} {f(dy + 92)} {f(cx + dx + 46)} {f(dy + 70)} Z" fill="#C8962E" stroke="#0D0D0F" stroke-width="2"></path>')
    coins = "".join(f'<ellipse cx="{f(cx - w * 0.3 + r.uniform(-30, 30))}" cy="{f(h * 0.34 + 66 - r.uniform(0, 26))}" rx="8" ry="3.4" fill="#E8E8F0" stroke="#0D0D0F" stroke-width="1"></ellipse>' for _ in range(30))
    weights = "".join(f'<rect x="{f(cx + w * 0.3 - 24 + i * 16)}" y="{f(h * 0.3 + 52)}" width="14" height="16" fill="#6A6A74" stroke="#0D0D0F" stroke-width="1.4"></rect>' for i in range(3))
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#12113A"></rect>' + beam + pans + coins + weights
            + f'<rect x="{f(cx - 60)}" y="{f(base)}" width="120" height="12" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></rect>')

def machpelah(p, w, h, seed, burial=False):
    """The field of Ephron in Machpelah before Mamre: trees in a walled field, the cave in the rock at its end."""
    base = h * 0.88; r = random.Random(seed)
    o = [sun(w * 0.86, h * 0.2, 14, color="#FFE680", op=0.25),
         f'<path d="M{f(w * 0.56)} {f(base)} L {f(w * 0.62)} {f(h * 0.3)} L {f(w * 0.9)} {f(h * 0.24)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(base)} Z" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.7)} {f(base)} C {f(w * 0.7)} {f(h * 0.5)} {f(w * 0.86)} {f(h * 0.5)} {f(w * 0.86)} {f(base)} Z" fill="#12090A" stroke="#0D0D0F" stroke-width="2"></path>',
         ground(w, h, base, "#7A9A4A", dy=0)]
    o += [J.oak(w * x, base - r.uniform(0, 6), 0.32 + r.uniform(-0.04, 0.04), seed=int(x * 100)) for x in (0.08, 0.2, 0.32, 0.44)]
    o.append(f'<path d="M-10 {f(base + 10)} L {f(w * 0.68)} {f(base + 10)}" stroke="#B59A7A" stroke-width="8" stroke-dasharray="18 6"></path>')
    if burial:
        o.append(mk.person(p, round(w * 0.6), round(base), fit(base, h * 0.42), body=SKIN, cloth=Z.ABRAM_ROBE, sw=3, flip=True, extra=GREY_BEARD))
        o += [man(p, w * x, base, fit(base, h * 0.46), c, flip=True) for x, c in [(0.5, "#5A3A22"), (0.44, "#8A6A4A")]]
    o.append(label(w * 0.78, base + 22, "MACHPELAH", "#12113A", 10))
    return "".join(o)
