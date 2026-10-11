"""New drawings for Genesis chapter 6 (Genesis 24:1–25:18): Abraham's servant, the well at the city of Nahor,
Rebekah and her pitcher, Laban, the journey back, Isaac in the field at eventide, Keturah, Abraham's death, Ishmael's princes."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus4 as E4, exodus5 as V, joshua1 as J, judges1 as G1, samuel4 as A4, numbers1 as N, ruth1 as R
from faces_ex import F
from genesis import art2 as Y, art3 as Z, art4 as Q, art5 as K
from genesis.art2 import fit, ground, hills, birds, city, SKIN
from genesis.art3 import sun, label, man, woman, abram as abraham, grid_bg, node, route, STAFF, HOLD_STAFF, GREY_BEARD
from genesis.art5 import well, lad
def f(v): return f"{v:.1f}"

# ---- faces ----------------------------------------------------------------------------------------------
SERVANT = F("adam", skin="#B98A6E", shadow="#6A4A3A", hair="#5A5650", hl="#8A867E", beard=True, beard_color="#6A665E", scarf="#8A6A3A", cord=True, light="#FFC14D")
SERVANT_PRAY = F("adam", skin="#C98E66", shadow="#5A4A5A", hair="#5A5650", hl="#8A867E", beard=True, beard_color="#6A665E", scarf="#8A6A3A", cord=True, brow="sorrow", light="#FFF4C2")
REBEKAH = F("eve", skin="#E3B08A", shadow="#B97A58", hair="#2A1A10", scarf="#2E7A4A", light="#FFE680")
REBEKAH_VEIL = F("eve", skin="#E3B08A", shadow="#9A6A5A", hair="#2A1A10", scarf="#E8E2D6", light="#FF8A3D")
LABAN = F("adam", skin="#C98E66", shadow="#6A3A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#9A3A1E", cord=True, light="#FFC14D")
BETHUEL = F("adam", skin="#B98A6E", shadow="#6A4A5A", hair="#E8E2D6", hl="#B8B2A6", beard=True, scarf="#5A4A6A", cord=True)
ISAAC = F("adam", skin="#E3B08A", shadow="#B97A58", hair="#5A3A22", hl="#8A6A4A", beard=True, beard_color="#5A3A22", light="#FF8A3D")
ISAAC_LOVE = F("adam", skin="#E3B08A", shadow="#B97A58", hair="#5A3A22", hl="#8A6A4A", beard=True, beard_color="#5A3A22", light="#FFE680")
ABRAHAM_OLD = F("adam", skin="#C98E66", shadow="#6A4A5A", hair="#F3EFE6", hl="#C8C2B6", beard=True, beard_color="#F3EFE6", light="#FFE680")

# ---- people ---------------------------------------------------------------------------------------------
SERVANT_ROBE, REBEKAH_ROBE, LABAN_ROBE, ISAAC_ROBE = "#8A6A3A", "#2E7A4A", "#9A3A1E", "#E8D8B0"
SERVANT_BEARD = GREY_BEARD.replace("#B8B2A6", "#6A665E")
JAR = '<path d="M-6 -214 C -16 -214 -18 -234 -10 -240 L -8 -248 L 8 -248 L 10 -240 C 18 -234 16 -214 6 -214 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path>'
JAR_UP = [(-22, -158), (-18, -196), (-10, -226)]

def servant(p, x, y, s, flip=False, up=None, staff=False):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=SERVANT_ROBE, sw=3, flip=flip, up=up, extra=SERVANT_BEARD + (STAFF if staff else ""))

def rebekah(p, x, y, s, flip=False, up=None, jar=False):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=REBEKAH_ROBE, woman=True, hair="#2A1A10", sw=3, flip=flip,
                     up=JAR_UP if jar else up, extra=JAR if jar else "")

def laban(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=LABAN_ROBE, sw=3, flip=flip, up=up, extra=GREY_BEARD.replace("#B8B2A6", "#1A1210"))

def isaac(p, x, y, s, flip=False, up=None):
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=ISAAC_ROBE, sw=3, flip=flip, up=up, extra=GREY_BEARD.replace("#B8B2A6", "#5A3A22"))

def kneeling_camel(x, y, s=1.0, flip=False, color="#B5844A", load="#8A3A1E"):
    """A camel couched on the ground: folded legs under the body, neck up."""
    sx = -s if flip else s
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            f'<path d="M-90 0 C -100 -30 -70 -70 -30 -74 C -10 -110 30 -110 44 -74 C 60 -70 70 -50 70 -30 L 70 0 Z" fill="{color}" stroke="#0D0D0F" stroke-width="3"></path>'
            f'<path d="M60 -40 C 80 -60 84 -100 92 -130 C 96 -142 120 -146 128 -136 C 132 -128 124 -120 114 -122 C 108 -100 104 -60 80 -20 Z" fill="{color}" stroke="#0D0D0F" stroke-width="3"></path>'
            f'<path d="M-40 -74 C -30 -86 30 -86 40 -74 L 34 -40 L -34 -40 Z" fill="{load}" stroke="#0D0D0F" stroke-width="2.4"></path>'
            '<path d="M-80 0 C -70 -14 -40 -14 -30 0 M20 0 C 30 -14 60 -14 66 0" fill="none" stroke="#0D0D0F" stroke-width="2.4"></path>'
            '<circle cx="118" cy="-134" r="3" fill="#0D0D0F"></circle></g>')

def trough(x, y, w, water=True):
    return (f'<path d="M{f(x - w / 2)} {f(y - 26)} L {f(x + w / 2)} {f(y - 26)} L {f(x + w / 2 - 10)} {f(y)} L {f(x - w / 2 + 10)} {f(y)} Z" fill="#8A8478" stroke="#0D0D0F" stroke-width="2.4"></path>'
            + (f'<path d="M{f(x - w / 2 + 6)} {f(y - 22)} L {f(x + w / 2 - 6)} {f(y - 22)}" stroke="#2C9DB8" stroke-width="5"></path>' if water else ""))

def steps_well(w, h, base):
    """The fountain below the city: stone steps going down to the water."""
    o = [f'<path d="M{f(w * 0.08)} {f(base)} L {f(w * 0.08)} {f(base - h * 0.06)} L {f(w * 0.92)} {f(base - h * 0.06)} L {f(w * 0.92)} {f(base)} Z" fill="#A89E92" stroke="#0D0D0F" stroke-width="2"></path>']
    return "".join(o)

# ---- Genesis 24 -----------------------------------------------------------------------------------------
def master_and_servant(p, w, h, seed):
    """Abraham, very old, seated at his tent door; his servant, the elder of his house, standing before him."""
    base = h * 0.88; s = fit(base, h * 0.42)
    seat = f'<rect x="{f(w * 0.22)}" y="{f(base - 40)}" width="{f(w * 0.16)}" height="40" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></rect>'
    return (sun(w * 0.88, h * 0.2, 14, op=0.25) + ground(w, h, base, "#C8A06A", dy=0) + G1.tent_big(w * 0.14, base, w * 0.26, h * 0.62, color="#3A2214", glow="#5A2A12")
            + seat + E.kneel(w * 0.3, base - 30, round(h / 520, 3), color=Z.ABRAM_ROBE, skin=SKIN)
            + servant(p, w * 0.6, base, s, flip=True, up=[(-22, -158), (-40, -126), (-62, -110)]))

def ten_camels(p, w, h, seed):
    """The servant took ten camels and departed: a line of ten laden camels going north into the haze."""
    base = h * 0.84; o = [sun(w * 0.12, h * 0.24, 16, color="#FFE680", op=0.3), ground(w, h, base - 10, "#E8C88A", dy=0)]
    r = random.Random(seed)
    for i in range(10):
        t = i / 9; x = w * (0.94 - 0.84 * t); y = base + 10 - t * h * 0.3
        o.append(G1.camel(x, y, 0.42 - 0.26 * t, flip=True, color=r.choice(["#B5844A", "#C99A5A"]), rider="#8A6A3A" if i == 0 else None))
    o.append(hud_count(w * 0.86, h * 0.2, "10"))
    return "".join(o)

def hud_count(x, y, t):
    return (f'<rect x="{f(x - 30)}" y="{f(y - 26)}" width="60" height="34" fill="#F3EFE6" stroke="#D7261E" stroke-width="2"></rect>'
            + label(x, y + 2, t, "#D7261E", 24).replace('font-family="IBM Plex Mono, monospace"', 'font-family="Anton, sans-serif"'))

def to_mesopotamia(w, h, seed):
    """From the land of Canaan to Mesopotamia, unto the city of Nahor: the route north on the grid map."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.46)} -10 C {f(w * 0.58)} {f(h * 0.3)} {f(w * 0.72)} {f(h * 0.6)} {f(w * 0.98)} {f(h + 10)}" fill="none" stroke="#2C9DB8" stroke-width="4" opacity="0.7"></path>')
    o.append(f'<path d="M{f(w * 0.1)} -10 C {f(w * 0.08)} {f(h * 0.4)} {f(w * 0.06)} {f(h * 0.7)} {f(w * 0.0)} {f(h + 10)} L -10 {f(h + 10)} L -10 -10 Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(route([(w * 0.2, h * 0.82), (w * 0.3, h * 0.4), (w * 0.54, h * 0.18)], color="#FFD23F", sw=3))
    o.append(node(w * 0.2, h * 0.82, "HEBRON", "#FFD23F", r=5, dy=20) + node(w * 0.54, h * 0.18, "CITY OF NAHOR", "#D7261E", r=6, dy=-12))
    o.append(label(w * 0.8, h * 0.34, "MESOPOTAMIA", "#8FD0E2", 10))
    return "".join(o)

def evening_well(p, w, h, seed, women=True, pray=False):
    """By the well of water without the city at evening: the camels couched, the women coming out to draw."""
    base = h * 0.88; r = random.Random(seed)
    o = [sun(w * 0.8, h * 0.62, h * 0.18, color="#FF8A3D", op=0.25), city(w * 0.74, h * 0.62, w * 0.46, h * 0.36, seed, color="#5A3A3E", lit="#FFC14D", wall="#7A5A4A"),
         ground(w, h, h * 0.62, "#B5865A", dy=0), well(w * 0.42, base - 20, h / 300)]
    o += [kneeling_camel(w * x, base + 4, 0.34, flip=x > 0.5, color=r.choice(["#B5844A", "#C99A5A"])) for x in (0.08, 0.2)]
    if pray: o.append(servant(p, w * 0.3, base, fit(base, h * 0.4), up=[(-22, -158), (-28, -196), (-34, -232)]))
    if women:
        for i, x in enumerate((0.66, 0.76, 0.86)):
            o.append(mk.person(p, round(w * x), round(h * 0.66 + i * 6), round(0.2 + i * 0.02, 3), body=SKIN, cloth=r.choice(["#C2456A", "#7A3BA8", "#E8E2D6"]),
                               woman=True, hair="#1A1210", sw=3, flip=True, up=JAR_UP, extra=JAR))
    return "".join(o)

def rebekah_comes(p, w, h, seed):
    """Rebekah came out with her pitcher upon her shoulder, and went down to the fountain: down the steps in the evening light."""
    base = h * 0.9
    stairs = "".join(f'<rect x="{f(w * 0.3 + i * 26)}" y="{f(h * 0.4 + i * 22)}" width="{f(w * 0.7)}" height="22" fill="{"#A89E92" if i % 2 else "#B8AE9E"}" stroke="#0D0D0F" stroke-width="1.6"></rect>' for i in range(int(h * 0.5 / 22)))
    return (sun(w * 0.18, h * 0.24, h * 0.14, color="#FF8A3D", op=0.3) + ground(w, h, h * 0.4, "#B5865A", dy=0) + stairs
            + f'<ellipse cx="{f(w * 0.2)}" cy="{f(base)}" rx="{f(w * 0.2)}" ry="{f(h * 0.06)}" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></ellipse>'
            + rebekah(p, w * 0.5, h * 0.4 + 5 * 22, fit(h * 0.4 + 110, h * 0.46), flip=True, jar=True))

def give_drink(p, w, h, seed, top=0.5):
    """She let down her pitcher upon her hand, and gave him drink."""
    base = h * 0.88; s = fit(base, h * top)
    pour = [(-22, -158), (4, -150), (30, -150)]
    jar_hand = '<g transform="translate(40 -150) rotate(70)"><path d="M-10 0 C -20 0 -22 -20 -14 -26 L -12 -34 L 4 -34 L 6 -26 C 14 -20 12 0 2 0 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="2"></path></g>'
    return (sun(w * 0.86, h * 0.6, h * 0.16, color="#FF8A3D", op=0.25) + ground(w, h, base, "#B5865A", dy=0) + well(w * 0.82, base - 10, h / 360)
            + servant(p, w * 0.32, base, s, up=[(-22, -158), (-6, -140), (14, -150)]) + rebekah(p, w * 0.5, base, s * 0.96, flip=True, up=pour).replace("</g>", jar_hand + "</g>", 1))

def camels_drink(p, w, h, seed):
    """She emptied her pitcher into the trough, and ran again unto the well to draw, and drew for all his camels."""
    base = h * 0.88; r = random.Random(seed)
    o = [sun(w * 0.9, h * 0.5, h * 0.16, color="#FF8A3D", op=0.25), ground(w, h, base, "#B5865A", dy=0), trough(w * 0.5, base, w * 0.5), well(w * 0.1, base - 10, h / 360)]
    o += [G1.camel(w * x, base - 2, 0.3, flip=x > 0.5, color=r.choice(["#B5844A", "#C99A5A"])) for x in (0.32, 0.44, 0.58, 0.7, 0.84)]
    o.append(rebekah(p, w * 0.2, base, fit(base, h * 0.44), jar=True))
    o.append(mk.speed(w * 0.16, base - h * 0.2, 10, 20, w * 0.16, seed, color="#F3EFE6", op=0.6))
    return "".join(o)

def ring_bracelets(w, h, seed):
    """A golden ring of half a shekel weight, and two bracelets of ten shekels weight of gold."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#12113A"></rect>', V.rays(w * 0.5, h * 0.5, 36, 20, w, color="#FFD23F", op=0.18)]
    o.append(f'<circle cx="{f(w * 0.24)}" cy="{f(h * 0.5)}" r="{f(h * 0.1)}" fill="none" stroke="#0D0D0F" stroke-width="11"></circle><circle cx="{f(w * 0.24)}" cy="{f(h * 0.5)}" r="{f(h * 0.1)}" fill="none" stroke="#E8B830" stroke-width="7"></circle>')
    for x in (0.56, 0.78):
        o.append(f'<ellipse cx="{f(w * x)}" cy="{f(h * 0.52)}" rx="{f(h * 0.16)}" ry="{f(h * 0.08)}" fill="none" stroke="#0D0D0F" stroke-width="16"></ellipse><ellipse cx="{f(w * x)}" cy="{f(h * 0.52)}" rx="{f(h * 0.16)}" ry="{f(h * 0.08)}" fill="none" stroke="#FFD23F" stroke-width="11"></ellipse>')
    o.append(label(w * 0.24, h * 0.78, "½ SHEKEL", "#FFD23F", 10) + label(w * 0.67, h * 0.78, "10 SHEKELS", "#FFD23F", 10))
    return "".join(o)

def worship(p, w, h, seed):
    """The man bowed his head, and worshipped Jehovah: the servant bowed by the well, the camels resting, the first stars."""
    base = h * 0.86
    return (mk.stars(40, w, h * 0.4, seed) + ground(w, h, base, "#8A6A4A", dy=0) + well(w * 0.66, base - 8, h / 320)
            + kneeling_camel(w * 0.88, base + 4, 0.3, flip=True) + E.kneel(w * 0.4, base + 2, round(h / 380, 3), color=SERVANT_ROBE, skin=SKIN))

def runs_home(p, w, h, seed):
    """The damsel ran, and told her mother's house: Rebekah running up to a house in the city at dusk."""
    base = h * 0.88
    return (city(w * 0.7, base, w * 0.5, h * 0.5, seed, color="#5A3A3E", lit="#FFC14D", wall="#7A5A4A") + ground(w, h, base, "#8A6A4A", dy=0)
            + rebekah(p, w * 0.36, base, fit(base, h * 0.42), up=[(-22, -158), (-46, -140), (-60, -160)])
            + mk.speed(w * 0.24, base - h * 0.2, 12, 20, w * 0.2, seed, color="#F3EFE6", op=0.6))

def laban_runs(p, w, h, seed):
    """Laban ran out unto the man, unto the fountain: he sees the ring and the bracelets on his sister's hands."""
    base = h * 0.88; s = fit(base, h * 0.52)
    return (sun(w * 0.86, h * 0.6, h * 0.12, color="#FF8A3D", op=0.2) + ground(w, h, base, "#8A6A4A", dy=0) + well(w * 0.74, base - 8, h / 360)
            + laban(p, w * 0.3, base, s, up=[(-22, -158), (-46, -140), (-60, -160)]) + mk.speed(w * 0.18, base - h * 0.2, 12, 20, w * 0.2, seed, color="#F3EFE6", op=0.6)
            + servant(p, w * 0.6, base, s, flip=True) + G1.camel(w * 0.9, base - 2, 0.3, flip=True))

def lodging(p, w, h, seed):
    """He ungirded the camels, and gave straw and provender, and water to wash his feet and the feet of the men with him."""
    base = h * 0.88
    straw = "".join(f'<path d="M{f(w * 0.64 + i * 6)} {f(base)} l {f(random.Random(seed + i).uniform(-20, 20))} -18" stroke="#E8C88A" stroke-width="3"></path>' for i in range(30))
    return (f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#5A3A2E"></rect>'
            + f'<rect x="{f(w * 0.02)}" y="{f(h * 0.1)}" width="{f(w * 0.3)}" height="{f(base - h * 0.1)}" fill="#FFC14D" stroke="#0D0D0F" stroke-width="3"></rect>'
            + ground(w, h, base, "#3A2418", dy=0) + straw + kneeling_camel(w * 0.78, base + 2, 0.36, flip=True, load="#3A2418")
            + K.E3.basin(w * 0.44, base - 6, w * 0.14) + E.kneel(w * 0.5, base, round(h / 560, 3), color=SERVANT_ROBE, skin=SKIN, flip=True)
            + laban(p, w * 0.24, base, fit(base, h * 0.4)))

def depart(p, w, h, seed):
    """Rebekah arose, and her damsels, and they rode upon the camels, and followed the man."""
    base = h * 0.84
    return (sun(w * 0.9, base - 10, h * 0.2, color="#FFC14D", op=0.3) + city(w * 0.1, base, w * 0.2, h * 0.36, seed, color="#5A3A3E", lit="#FFC14D", wall="#7A5A4A")
            + ground(w, h, base, "#C8A06A", dy=0)
            + G1.camel(w * 0.36, base, 0.4, rider=REBEKAH_ROBE) + G1.camel(w * 0.52, base + 2, 0.36, rider="#C2456A") + G1.camel(w * 0.66, base + 4, 0.36, rider="#7A3BA8")
            + G1.camel(w * 0.82, base + 2, 0.4, rider=SERVANT_ROBE))

def family_blessing(p, w, h, seed):
    """They blessed Rebekah: her mother and Laban with raised hands at the house door, Rebekah turning to go."""
    base = h * 0.88; s = fit(base, h * 0.4); up = [(-22, -158), (-30, -196), (-36, -232)]
    return (sun(w * 0.86, h * 0.2, 14, color="#FFE680", op=0.3) + city(w * 0.2, base, w * 0.4, h * 0.6, seed, color="#7A5A4A", lit="#FFC14D", wall="#8A6A5A")
            + ground(w, h, base, "#C8A06A", dy=0)
            + woman(p, w * 0.14, base, s * 0.95, "#5A4A6A", up=up) + laban(p, w * 0.28, base, s, up=up) + rebekah(p, w * 0.46, base, s * 0.95, flip=True)
            + mk.person(p, round(w * 0.56), round(base), round(s * 0.92, 3), body=SKIN, cloth="#8A6A5A", woman=True, hair="#B8B2A6", sw=3, flip=True))

def meditate(p, w, h, seed):
    """Isaac went out to meditate in the field at the eventide, and saw camels coming."""
    base = h * 0.86
    return (sun(w * 0.7, base - 10, h * 0.2, color="#FF8A3D", op=0.3) + hills(w, h, base, seed, color="#5A4A3A", amp=6)
            + ground(w, h, base, "#8A9A5A", dy=0) + "".join(f'<path d="M{f(x)} {f(base + 10)} l 4 -20 M{f(x + 6)} {f(base + 10)} l -2 -16" stroke="#5E7A3A" stroke-width="2"></path>' for x in range(0, int(w), 26))
            + isaac(p, w * 0.22, base + 4, fit(base, h * 0.52))
            + "".join(G1.camel(w * x, base - h * 0.12, 0.16, flip=True) for x in (0.72, 0.78, 0.84, 0.9)))

def alight(p, w, h, seed):
    """Rebekah lifted up her eyes, and when she saw Isaac, she alighted from the camel."""
    base = h * 0.88
    return (sun(w * 0.86, base - 10, h * 0.2, color="#FF8A3D", op=0.25) + ground(w, h, base, "#8A9A5A", dy=0)
            + G1.camel(w * 0.66, base, 0.46, flip=True) + rebekah(p, w * 0.44, base, fit(base, h * 0.4), flip=True, up=[(-22, -158), (-6, -194), (12, -226)])
            + G1.camel(w * 0.9, base, 0.4, flip=True, rider=SERVANT_ROBE))

def sarahs_tent(p, w, h, seed):
    """Isaac brought her into his mother Sarah's tent: the two at the lit doorway at night."""
    base = h * 0.88; s = fit(base, h * 0.56)
    return (mk.stars(70, w, h * 0.5, seed) + ground(w, h, base, "#1A1430", dy=0) + G1.tent_big(w * 0.5, base, w * 0.5, h * 0.66, color="#3A2214", glow="#FFC14D")
            + f'<circle cx="{f(w * 0.5)}" cy="{f(base - h * 0.2)}" r="{f(h * 0.3)}" fill="#FFC14D" opacity="0.15"></circle>'
            + isaac(p, w * 0.42, base, s) + rebekah(p, w * 0.56, base, s * 0.95, flip=True))

# ---- Genesis 25:1–18 ------------------------------------------------------------------------------------
def east_country(p, w, h, seed):
    """Abraham gave gifts to the sons of the concubines and sent them away eastward, unto the east country."""
    base = h * 0.84
    return (sun(w * 0.88, h * 0.3, 18, color="#FFE680", op=0.3) + ground(w, h, base, "#C8A06A", dy=0)
            + abraham(p, w * 0.12, base, fit(base, h * 0.36), staff=True, up=HOLD_STAFF) + isaac(p, w * 0.22, base, fit(base, h * 0.36))
            + Z.caravan(p, w * 0.42, w * 0.94, base + 4, 0.6, seed))

def gathered(p, w, h, seed):
    """Abraham gave up the ghost, and died in a good old age, full of years: his empty seat at the tent door at sunset."""
    base = h * 0.86
    seat = f'<rect x="{f(w * 0.56)}" y="{f(base - 40)}" width="{f(w * 0.1)}" height="40" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></rect>'
    return (sun(w * 0.22, base - 10, h * 0.22, color="#FF8A3D", op=0.3) + hills(w, h, base, seed, color="#2A1A2E", amp=6)
            + G1.tent_big(w * 0.8, base, w * 0.3, h * 0.6, color="#2A1A14", glow="#5A2A12") + seat
            + f'<path d="M{f(w * 0.6)} {f(base - 40)} l 0 -50" stroke="#5A3A22" stroke-width="5"></path>')

def buried_by_sons(p, w, h, seed):
    """Isaac and Ishmael his sons buried him in the cave of Machpelah."""
    return K.machpelah(p, w, h, seed) + (
        isaac(p, w * 0.56, h * 0.88, fit(h * 0.88, h * 0.42), flip=True) + lad(p, w * 0.46, h * 0.88, fit(h * 0.88, h * 0.4), cloth=K.ISHMAEL_TUNIC, flip=True,
                                                                              extra='<path d="M34 -230 C 60 -200 60 -120 34 -90" fill="none" stroke="#8A5A30" stroke-width="4"></path>'))

def ishmael_lands(w, h, seed):
    """They dwelt from Havilah unto Shur that is before Egypt, as thou goest toward Assyria."""
    o = [grid_bg(w, h, color="#3A2A1E", bg="#1A120A")]
    o.append(route([(w * 0.12, h * 0.7), (w * 0.5, h * 0.56), (w * 0.88, h * 0.3)], color="#C8A06A", sw=2.6, arrow=False))
    o.append(node(w * 0.12, h * 0.7, "SHUR", "#FFD23F", r=5, dy=22) + node(w * 0.88, h * 0.3, "HAVILAH", "#FFD23F", r=5, dy=22))
    o.append(label(w * 0.06, h * 0.92, "← EGYPT", "#8FD0E2", 10, "start") + label(w * 0.94, h * 0.12, "ASSYRIA →", "#8FD0E2", 10, "end"))
    for i in range(12):
        t = i / 11; x = w * (0.16 + 0.68 * t); y = h * (0.66 - 0.32 * t) - 18
        o.append(E4.tent(x, y, w * 0.04, h * 0.08, color="#5A3A22"))
    return "".join(o)
