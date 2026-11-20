"""Drawings for Revelation 8–11 (chapter 3 of the volume): the seventh seal and the seven trumpets, the little book, the two
witnesses. Judgment is drawn as land, sea, sky, fire and smoke, never as people struck: hail and fire on the trees, the
burning mountain falling into the sea, the star Wormwood over the rivers, the third part of the sun and moon darkened, the
smoke of the pit, the locusts and the horsemen as heraldic plates, the host beyond Euphrates far off; the two witnesses'
death is told over the empty street of the great city, their rising as light.

    seven_angels(p, w, h, seed, sound=None)    the seven angels that stand before God, each with a trumpet (sound=k sounding)
    censer(p, w, h, seed, cast=False)          the angel at the golden altar with the golden censer; cast= fire cast to the earth
    hail_fire(w, h, seed) · mountain_sea(w, h, seed) · wormwood(w, h, seed) · darkened(w, h, seed)   the first four trumpets
    eagle_woe(w, h, seed)                      an eagle flying in mid heaven over the darkened land
    pit(p, w, h, seed, stage=)                 the pit of the abyss: "key" (a star fallen, the key), "smoke", "locusts"
    locust_plate(w, h) · horse_plate(w, h)     the locusts and the horses of the vision as heraldic plates, their parts named
    altar_horns(p, w, h, seed)                 the golden altar's four horns and the sixth angel with his trumpet
    euphrates(w, h, seed)                      the great river and a host far off on the horizon
    idols(w, h, seed)                          idols of gold, silver, brass, stone and wood, which can neither see nor hear
    mighty_angel(p, w, h, seed, stage=)        the strong angel, one foot on the sea and one on the earth ("stand", "thunders",
                                               "oath", "book" — John taking the little book)
    measure(w, h)                              the temple of God, the altar and the court without, and the reed: a plate
    witnesses(p, w, h, seed, stage=)           the two witnesses in sackcloth between the olive trees and the candlesticks
                                               ("stand", "drought", "street" — the empty street of the great city, "rise", "quake")
    seventh(p, w, h, seed)                     the seventh angel sounding in great light
    ark_heaven(p, w, h, seed)                  the temple of God opened in heaven and the ark of his covenant seen"""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from rev.art2 import *
from rev.art import f, INK, GOLD, GOLD_L, WHITE
import exodus as E, joshua1 as J1
from num.art5 import trumpet
from oba.minor import bolt, fires, smokes, ruin, river
from job.art import smoke
from ezk.art2 import idol
from ecc.art import tree

UP_TRUMPET = [(-22, -158), (-40, -168), (-54, -176)]          # the trumpet raised to the lips

def trumpeter(p, x, b, s, flip=False, sounding=False):
    """An angel with a trumpet held at the side (sounding=True: raised and sounding, rings of sound)."""
    if sounding:
        ex = trumpet(-24, -182, 0.36, rot=200) + "".join(f'<path d="M{-120 - k * 14} {-216 - k * 8} q -10 30 0 60" fill="none" stroke="#FFF4C2" stroke-width="3" opacity="{0.8 - k * 0.2:.1f}"></path>' for k in range(3))
        return angel(p, x, b, s, up=UP_TRUMPET, flip=flip, extra=ex)
    return angel(p, x, b, s, flip=flip, extra=trumpet(26, -86, 0.3, rot=100))

def seven_angels(p, w, h, seed, sound=None):
    """The seven angels that stand before God, and there were given unto them seven trumpets (8:2, 8:6)."""
    o = [defs(p), sky(w, h, "#1A1440", "#5A4A8A"), halo(w * 0.5, h * 0.2, w * 0.6, "#FFF4C2", 0.7), rays(w * 0.5, h * 0.15, 30, h * 0.08, w, "#FFFDF0", 0.3, 4)]
    o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.96)}" rx="{f(w * 0.5)}" ry="{f(h * 0.08)}" fill="#C8ECF8" opacity="0.45"></ellipse>')
    s = h * 0.78 / 205
    for i in range(7):
        x = w * (0.08 + 0.84 * i / 6)
        o.append(trumpeter(p, x, h * 0.97 - (0 if i % 2 == 0 else h * 0.04), s * (1.0 if i % 2 == 0 else 0.92), flip=i >= 4, sounding=sound == i))
    return "".join(o)

def censer_cup(x, y, s=1.0, fire=True):
    """A golden censer swung on its chains, coals and incense in it."""
    o = (f'<path d="M{f(x)} {f(y - 40 * s)} L {f(x - 12 * s)} {f(y - 8 * s)} M{f(x)} {f(y - 40 * s)} L {f(x + 12 * s)} {f(y - 8 * s)}" stroke="#C8962E" stroke-width="{f(max(1, 1.4 * s))}"></path>'
         f'<path d="M{f(x - 14 * s)} {f(y - 8 * s)} C {f(x - 12 * s)} {f(y + 6 * s)} {f(x + 12 * s)} {f(y + 6 * s)} {f(x + 14 * s)} {f(y - 8 * s)} Z" fill="#E8B830" stroke="{INK}" stroke-width="{f(max(1, 1.6 * s))}"></path>')
    if fire: o += f'<path d="M{f(x - 8 * s)} {f(y - 8 * s)} C {f(x - 6 * s)} {f(y - 18 * s)} {f(x)} {f(y - 14 * s)} {f(x + 2 * s)} {f(y - 22 * s)} C {f(x + 6 * s)} {f(y - 14 * s)} {f(x + 8 * s)} {f(y - 12 * s)} {f(x + 8 * s)} {f(y - 8 * s)} Z" fill="#FF8A2E"></path>'
    return o

def censer(p, w, h, seed, cast=False):
    """Another angel stood over the altar, having a golden censer (8:3–5): the golden altar before the throne in light, the
    smoke of the incense with the prayers of the saints going up; cast=True: the censer filled with the fire of the altar
    and cast upon the earth — fire falling from heaven to the dark earth below, thunders and lightnings."""
    o = [defs(p)]
    if not cast:
        o += [sky(w, h, "#1A1440", "#5A4A8A"), halo(w * 0.5, h * 0.1, w * 0.5, "#FFF4C2", 0.7)]
        s = h * 0.36 / 94
        o.append(f'<rect x="-10" y="{f(h * 0.9)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>')
        o.append(altar_gold(w * 0.4, h * 0.9, s))
        o.append(smoke(w * 0.42, h * 0.9 - 100 * s, 9, seed, color="#E8E2F0", op=0.65, k=h / 260))
        fs = h * 0.86 / 205
        o.append(angel(p, w * 0.66, h * 0.98, fs, up=[(-22, -158), (-46, -150), (-70, -140)], extra=censer_cup(-78, -112, 1.0)))
        return "".join(o)
    o += [sky(w, h, "#0B0B2A", "#3A2A4A"), starfield(w, h, seed, 40, 0.4)]
    hz = h * 0.72
    o.append(hills(w, h, hz - h * 0.04, seed, color="#2A2030", amp=12, step=80) + ground(w, h, hz, "#1A1418", dy=0))
    for i in range(4): o.append(bolt(w * (0.2 + 0.2 * i), 0, hz * 0.9, seed + i, sw=3))
    for i in range(6):
        x = w * (0.18 + 0.12 * i)
        o.append(f'<path d="M{f(x + 40)} {f(h * 0.12)} L {f(x)} {f(hz + h * 0.04)}" stroke="#FF8A2E" stroke-width="5" opacity="0.8"></path>'
                 + E.blaze(x, hz + h * 0.06, 28, h * 0.12, seed + i, n=5))
    fs = h * 0.36 / 205
    o.append(angel(p, w * 0.84, h * 0.42, fs, up=[(-22, -158), (-46, -176), (-70, -186)], flip=False, extra=censer_cup(-74, -170, 1.4)))
    for k in range(5): o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.95)} l {(k - 2) * 30} -10" stroke="#C8B080" stroke-width="2"></path>')
    return "".join(o)

def hail_fire(w, h, seed):
    """The first trumpet (8:7): hail and fire cast upon the earth, the trees and the grass burning (what is mingled with it
    is in the words)."""
    r = random.Random(seed)
    o = [sky(w, h, "#2A0A10", "#7A2A1A")]
    hz = h * 0.66
    o.append(hills(w, h, hz - h * 0.04, seed, color="#4A3A2A", amp=12, step=80) + ground(w, h, hz, "#5A5A2A", dy=0))
    for i in range(7):
        x = w * (0.06 + 0.15 * i)
        o.append(tree(x, h * 0.96, min(0.8, h / 380), color="#3A4A2A", seed=seed + i))
        if i % 2 == 0: o.append(E.blaze(x, h * 0.7, 46, h * 0.24, seed + i, n=6))
    o.append(E.blaze(w * 0.5, h * 0.99, w * 0.9, h * 0.12, seed, n=14))
    for _ in range(40):
        x, y = r.uniform(0, w), r.uniform(0, hz)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(2.5, 5))}" fill="#E8F4F8" stroke="#6A8A9A" stroke-width="1"></circle>'
                 f'<path d="M{f(x)} {f(y)} l -8 -22" stroke="#FFB02E" stroke-width="2" opacity="0.6"></path>')
    return "".join(o)

def mountain_sea(w, h, seed):
    """The second trumpet (8:8–9): as it were a great mountain burning with fire cast into the sea, the ships upon it."""
    o = [sky(w, h, "#2A0A10", "#C84A2A")]
    hz = h * 0.6
    o.append(sea(w, h, hz, seed, color="#3A3A5A", deep="#1A1A2A", rough=True))
    cx, cy = w * 0.42, h * 0.3
    o.append(f'<path d="M{f(cx - w * 0.16)} {f(cy + h * 0.16)} L {f(cx - w * 0.04)} {f(cy - h * 0.16)} L {f(cx + w * 0.06)} {f(cy - h * 0.1)} L {f(cx + w * 0.16)} {f(cy + h * 0.18)} Z" '
             f'fill="#3A2A2A" stroke="{INK}" stroke-width="2.6" transform="rotate(14 {f(cx)} {f(cy)})"></path>')
    o.append(E.blaze(cx, cy + h * 0.1, w * 0.3, h * 0.34, seed, n=9))
    o.append(f'<path d="M{f(cx + w * 0.2)} {f(cy - h * 0.2)} L {f(cx + w * 0.05)} {f(cy)}" stroke="#FFB02E" stroke-width="10" opacity="0.4"></path>')
    o.append(smoke(cx + 20, cy - h * 0.1, 6, seed, color="#3A2A2E", op=0.5, k=h / 300))
    o.append(f'<ellipse cx="{f(cx + 10)}" cy="{f(hz + 6)}" rx="{f(w * 0.2)}" ry="{f(h * 0.04)}" fill="#E8F4F8" opacity="0.7"></ellipse>')
    o.append(ship(w * 0.82, hz + h * 0.16, h / 600) + ship(w * 0.12, hz + h * 0.28, h / 520, flip=True))
    return "".join(o)

def wormwood(w, h, seed):
    """The third trumpet (8:10–11): a great star burning as a torch falling upon the rivers and the fountains of the
    waters; the name of the star is Wormwood."""
    o = [sky(w, h, "#0B0B2A", "#4A3A5A"), starfield(w, h, seed, 40, 0.5)]
    hz = h * 0.6
    o.append(hills(w, h, hz - h * 0.06, seed, color="#3A3A4A", amp=18, step=90) + ground(w, h, hz, "#4A4A3A", dy=0))
    o.append(river(w, hz + h * 0.14, h * 0.1, color="#3A6A7A", seed=seed))
    for fx in (0.2, 0.8):
        o.append(f'<ellipse cx="{f(w * fx)}" cy="{f(h * 0.9)}" rx="{f(w * 0.07)}" ry="{f(h * 0.03)}" fill="#3A6A7A" stroke="{INK}" stroke-width="1.6"></ellipse>')
    x, y = w * 0.62, h * 0.24
    o.append(f'<path d="M{f(x + w * 0.3)} {f(y - h * 0.3)} L {f(x)} {f(y)}" stroke="#FFB02E" stroke-width="{f(h * 0.06)}" opacity="0.35" stroke-linecap="round"></path>'
             f'<path d="M{f(x + w * 0.24)} {f(y - h * 0.24)} L {f(x)} {f(y)}" stroke="#FFE680" stroke-width="{f(h * 0.025)}" opacity="0.7" stroke-linecap="round"></path>')
    o.append(halo(x, y, h * 0.16, "#FFB02E", 0.7) + star(x, y, h * 0.07, "#FFF4C2", 1.4, "#C8401A"))
    o.append(label(w * 0.04, h * 0.1, "WORMWOOD", "#FFD23F", max(9, min(12, h / 22)), anchor="start"))
    return "".join(o)

def darkened(w, h, seed):
    """The fourth trumpet (8:12): the third part of the sun smitten, and the third part of the moon, and of the stars —
    the day and the night side by side, a third of each orb dark."""
    o = [f'<rect x="-10" y="-10" width="{f(w / 2 + 10)}" height="{f(h + 20)}" fill="#8A9AB0"></rect>', f'<rect x="{f(w / 2)}" y="-10" width="{f(w / 2 + 10)}" height="{f(h + 20)}" fill="#0B0B2A"></rect>']
    r = random.Random(seed)
    for _ in range(30):
        x, y = r.uniform(w / 2, w), r.uniform(0, h * 0.8)
        o.append(star(x, y, 3.5, "#F3EFE6" if r.random() < 0.67 else "#2A2A4A", 0.5, "#0D0D0F"))
    R = min(h * 0.24, w * 0.14)
    sx, sy, mx, my = w * 0.25, h * 0.42, w * 0.75, h * 0.42
    o.append(halo(sx, sy, R * 1.6, "#FFE680", 0.5) + f'<circle cx="{f(sx)}" cy="{f(sy)}" r="{f(R)}" fill="#FFE680" stroke="{INK}" stroke-width="2"></circle>'
             f'<path d="M{f(sx)} {f(sy)} L {f(sx)} {f(sy - R)} A {f(R)} {f(R)} 0 0 1 {f(sx + R * math.sin(math.radians(120)))} {f(sy - R * math.cos(math.radians(120)))} Z" fill="#1A1418" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<circle cx="{f(mx)}" cy="{f(my)}" r="{f(R * 0.8)}" fill="#E8E2D6" stroke="{INK}" stroke-width="2"></circle>'
             f'<path d="M{f(mx)} {f(my)} L {f(mx)} {f(my - R * 0.8)} A {f(R * 0.8)} {f(R * 0.8)} 0 0 1 {f(mx + R * 0.8 * math.sin(math.radians(120)))} {f(my - R * 0.8 * math.cos(math.radians(120)))} Z" fill="#1A1418" stroke="{INK}" stroke-width="2"></path>')
    o.append(hills(w, h, h * 0.86, seed, color="#2A2A3A", amp=10, step=80))
    sz = max(8, min(10, h / 24))
    o.append(label(sx, h * 0.12, "THE THIRD PART OF THE SUN", INK, sz) + label(mx, h * 0.12, "THE THIRD PART OF THE MOON", "#F3EFE6", sz))
    return "".join(o)

def eagle_woe(w, h, seed):
    """An eagle, flying in mid heaven, crying Woe, woe, woe (8:13): over the darkened land at dusk."""
    o = [sky(w, h, "#1A1028", "#8A4A3A"), halo(w * 0.2, h * 0.7, h * 0.4, "#C84A2A", 0.5)]
    o.append(hills(w, h, h * 0.78, seed, color="#2A1E2A", amp=16, step=90) + hills(w, h, h * 0.88, seed + 1, color="#1A1420", amp=10, step=70))
    o.append(eagle(w * 0.52, h * 0.38, min(2.2, h / 140), color="#3A2A1E"))
    for k in range(3):
        o.append(f'<path d="M{f(w * 0.62 + k * 26)} {f(h * 0.3 - k * 8)} q 14 20 0 40" fill="none" stroke="#FFD23F" stroke-width="3" opacity="{0.8 - k * 0.2:.1f}"></path>')
    return "".join(o)

def pit(p, w, h, seed, stage="key"):
    """The pit of the abyss (9:1–6). "key": a star fallen from heaven unto the earth, a light upon the ground, and the key of
    the pit; "smoke": the pit opened, a smoke going up as of a great furnace and the sun darkened by it; "locusts": out of
    the smoke the locusts come forth over the land as a dark cloud (nothing stung is drawn; the trees and the grass
    green and untouched)."""
    hz = h * 0.66
    dark = stage != "key"
    o = [sky(w, h, "#1A1418" if dark else "#0B0B2A", "#4A3A3A" if dark else "#3A2A5A")]
    if not dark: o.append(starfield(w, h, seed, 50, 0.6))
    o.append(f'<circle cx="{f(w * 0.8)}" cy="{f(h * 0.18)}" r="{f(h * 0.08)}" fill="{"#5A4A3A" if dark else "#FFE6A0"}" opacity="{0.6 if dark else 0}"></circle>')
    o.append(hills(w, h, hz - h * 0.04, seed, color="#3A3A2A", amp=14, step=80) + ground(w, h, hz, "#4A5A2A", dy=0))
    cx, cy = w * 0.42, hz + h * 0.14
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(w * 0.12)}" ry="{f(h * 0.05)}" fill="#0B0606" stroke="{INK}" stroke-width="2.4"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(w * 0.14)}" ry="{f(h * 0.065)}" fill="none" stroke="#5A4A3A" stroke-width="5"></ellipse>')
    if stage == "key":
        o.append(f'<path d="M{f(w * 0.78)} {f(h * 0.02)} L {f(cx + w * 0.06)} {f(cy - h * 0.12)}" stroke="#FFE680" stroke-width="6" opacity="0.4" stroke-linecap="round"></path>')
        o.append(halo(cx + w * 0.06, cy - h * 0.14, h * 0.14, "#FFF4C2", 0.7) + star(cx + w * 0.06, cy - h * 0.14, h * 0.045, "#FFF4C2", 1, "#C8962E"))
        kx, ky = cx - w * 0.02, cy - h * 0.06
        o.append(f'<g transform="translate({f(kx)} {f(ky)}) rotate(-20) scale({f(h / 260)})"><circle cx="0" cy="0" r="10" fill="none" stroke="#E8B830" stroke-width="5"></circle>'
                 '<path d="M10 0 L 46 0 M34 0 L 34 10 M42 0 L 42 8" stroke="#E8B830" stroke-width="5"></path></g>')
        return "".join(o)
    o.append(smoke(cx, cy - 10, 12, seed, color="#2A2224", op=0.75, k=h / 220) + smoke(cx - 30, cy - 10, 10, seed + 1, color="#3A3034", op=0.6, k=h / 260))
    if stage == "locusts":
        r = random.Random(seed)
        for _ in range(70):
            x, y = r.uniform(w * 0.3, w), r.uniform(h * 0.08, hz)
            o.append(f'<path d="M{f(x)} {f(y)} l 6 -2 l 4 2 l -4 2 Z M{f(x + 3)} {f(y - 1)} l 3 -5 M{f(x + 4)} {f(y)} l 4 -4" fill="#3A3010" stroke="#1A1408" stroke-width="1"></path>')
        o.append(tree(w * 0.86, h * 0.98, h / 420, seed=seed) + tree(w * 0.1, h * 0.98, h / 460, seed=seed + 1))
    return "".join(o)

def locust_plate(w, h):
    """The shapes of the locusts (9:7–10) as a heraldic plate: like unto horses prepared for war, crowns like unto gold,
    breastplates as of iron, wings, a scorpion's tail — each named; their faces, hair and teeth are in the words."""
    import exo.art8 as B
    from epistle import plate_bg
    o = [plate_bg(w, h, "THE SHAPES OF THE LOCUSTS")]
    B._W[0] = w
    s = min(h / 170, w / 420)
    cx, cy = w * 0.4, h * 0.72
    o.append(f'<g transform="translate({f(cx)} {f(cy)}) scale({f(s)})">'
             '<path d="M-60 -60 C -30 -96 30 -110 70 -80 C 50 -100 10 -112 -30 -96 Z" fill="#B8C8D8" opacity="0.8" stroke="#8FD0E2" stroke-width="1.4"></path>'
             '<path d="M-50 -58 C -20 -92 40 -100 76 -70" fill="none" stroke="#8FD0E2" stroke-width="1.2"></path>'
             '<path d="M-110 -40 C -130 -60 -140 -40 -128 -20 C -122 -10 -112 -14 -108 -24" fill="none" stroke="#C8962E" stroke-width="6"></path>'
             '<path d="M-128 -20 L -138 -12 L -126 -14 Z" fill="#C8962E"></path>'
             '<path d="M-100 -30 C -100 -56 -70 -66 -40 -64 L 30 -64 C 48 -76 70 -84 84 -74 L 98 -54 C 100 -46 92 -42 86 -46 L 70 -50 L 56 -36 L 54 0 L 44 0 L 42 -28 L -60 -28 L -64 0 L -74 0 L -78 -26 C -90 -24 -100 -26 -100 -30 Z" '
             'fill="#6A6A4A" stroke="#0D0D0F" stroke-width="2.4" stroke-linejoin="round"></path>'
             '<path d="M-40 -64 L -36 -30 L 20 -30 L 26 -64 Z" fill="#8A8A9A" stroke="#0D0D0F" stroke-width="1.8"></path>'
             + "".join(f'<path d="M{-34 + k * 10} -62 L {-32 + k * 10} -32" stroke="#5A5A6A" stroke-width="1.4"></path>' for k in range(6))
             + '<path d="M70 -84 L 68 -96 L 76 -90 L 82 -100 L 86 -88 L 94 -94 L 90 -80 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path></g>')
    tx = w * 0.72
    o.append(tag(cx + 82 * s, cy - 92 * s, "CROWNS LIKE UNTO GOLD", tx, h * 0.2))
    o.append(tag(cx + 10 * s, cy - 96 * s, "WINGS · AS THE SOUND OF CHARIOTS", tx, h * 0.32))
    o.append(tag(cx - 6 * s, cy - 46 * s, "BREASTPLATES AS OF IRON", tx, h * 0.46))
    o.append(tag(cx + 30 * s, cy - 14 * s, "LIKE UNTO HORSES PREPARED FOR WAR", tx, h * 0.6))
    o.append(tag(cx - 128 * s, cy - 30 * s, "TAILS LIKE UNTO SCORPIONS", tx, h * 0.74))
    o.append(label(14, h - 12, "FIVE MONTHS", "#8FD0E2", 9, anchor="start"))
    return "".join(o)

def horse_plate(w, h):
    """The horses of the vision (9:17–19) as a heraldic plate: the heads of the horses as the heads of lions; the riders'
    breastplates as of fire, of hyacinth and of brimstone shown as three swatches; the rest is in the words."""
    import exo.art8 as B
    from epistle import plate_bg
    o = [plate_bg(w, h, "THE HORSES IN THE VISION · TWICE TEN THOUSAND TIMES TEN THOUSAND")]
    B._W[0] = w
    s = h * 0.55 / 110
    o.append(E3.horse(w * 0.3, h * 0.86, s, color="#5A4A3A"))
    hx, hy = w * 0.3 + 74 * s, h * 0.86 - 92 * s
    o.append(f'<circle cx="{f(hx)}" cy="{f(hy)}" r="{f(22 * s)}" fill="#C8902E" stroke="{INK}" stroke-width="2"></circle>'
             f'<circle cx="{f(hx + 6 * s)}" cy="{f(hy)}" r="{f(13 * s)}" fill="#E8B060" stroke="{INK}" stroke-width="1.6"></circle>'
             f'<circle cx="{f(hx + 9 * s)}" cy="{f(hy - 4 * s)}" r="{f(2 * s)}" fill="{INK}"></circle>')
    sw = min(70, w * 0.1)
    for i, (nm, c) in enumerate((("FIRE", "#D7261E"), ("HYACINTH", "#3A3A9A"), ("BRIMSTONE", "#E8D040"))):
        x = w * 0.62 + i * (sw + 14); y = h * 0.34
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(sw)}" height="{f(sw * 0.8)}" fill="{c}" stroke="#8FD0E2" stroke-width="1.4"></rect>' + label(x + sw / 2, y + sw * 0.8 + 16, nm, "#FFD23F", 9))
    o.append(label(w * 0.62 + (3 * sw + 28) / 2, h * 0.26, "BREASTPLATES AS OF", "#8FD0E2", 9))
    o.append(tag(hx + 10 * s, hy - 12 * s, "THE HEADS AS THE HEADS OF LIONS", w * 0.62, h * 0.72))
    return "".join(o)

def altar_horns(p, w, h, seed):
    """A voice from the horns of the golden altar which is before God (9:13–14): the golden altar in light, a voice going
    out from its four horns (rings of light), the sixth angel with his trumpet."""
    o = [defs(p), sky(w, h, "#1A1440", "#5A4A8A"), halo(w * 0.36, h * 0.4, w * 0.4, "#FFF4C2", 0.7)]
    s = h * 0.4 / 94
    o.append(f'<rect x="-10" y="{f(h * 0.92)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>')
    o.append(altar_gold(w * 0.36, h * 0.92, s))
    for d in (-1, 1):
        x, y = w * 0.36 + d * 52 * s, h * 0.92 - 92 * s
        o.append("".join(f'<path d="M{f(x - 16 - k * 12)} {f(y - 8 - k * 10)} q {f(16 + k * 12)} {f(-14 - k * 8)} {f(32 + k * 24)} 0" fill="none" stroke="#FFF4C2" stroke-width="3" opacity="{0.8 - k * 0.2:.1f}"></path>' for k in range(3)))
    o.append(trumpeter(p, w * 0.78, h * 0.98, h * 0.86 / 205, flip=True))
    return "".join(o)

def euphrates(w, h, seed):
    """The four angels loosed that were bound at the great river Euphrates (9:14–16): the great river at dusk, and far off
    on the horizon beyond it a host past numbering, the armies of the horsemen, a dark line of spears (nothing more)."""
    r = random.Random(seed)
    o = [sky(w, h, "#2A1028", "#C8703A"), halo(w * 0.7, h * 0.56, h * 0.3, "#FF8A3D", 0.5)]
    hz = h * 0.56
    o.append(f'<rect x="-10" y="{f(hz)}" width="{f(w + 20)}" height="{f(h)}" fill="#8A6A3A"></rect>')
    for k in range(260):
        x = r.uniform(-10, w + 10); y = hz - r.uniform(0, h * 0.03)
        o.append(f'<path d="M{f(x)} {f(hz + 2)} L {f(x)} {f(y - h * 0.04)}" stroke="#1A1010" stroke-width="1.2"></path>')
    o.append(f'<rect x="-10" y="{f(hz - h * 0.015)}" width="{f(w + 20)}" height="{f(h * 0.03)}" fill="#2A1A14"></rect>')
    o.append(f'<path d="M-10 {f(h * 0.7)} C {f(w * 0.3)} {f(h * 0.66)} {f(w * 0.7)} {f(h * 0.78)} {f(w + 10)} {f(h * 0.7)} L {f(w + 10)} {f(h * 0.88)} C {f(w * 0.7)} {f(h * 0.96)} {f(w * 0.3)} {f(h * 0.84)} -10 {f(h * 0.88)} Z" '
             f'fill="#3A6A8A" stroke="{INK}" stroke-width="2"></path>')
    o.append(ground(w, h, h * 0.9, "#6A5A3A", dy=0))
    o.append(label(w * 0.04, h * 0.8, "EUPHRATES", "#F3EFE6", max(9, min(12, h / 22)), anchor="start"))
    return "".join(o)

def idols(w, h, seed):
    """The idols of gold, and of silver, and of brass, and of stone, and of wood, which can neither see, nor hear, nor walk
    (9:20): five graven images on their pedestals in a dark shrine, each named."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1418"></rect>', halo(w * 0.5, h * 0.2, w * 0.4, "#C8703A", 0.3)]
    o.append(f'<rect x="-10" y="{f(h * 0.8)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#3A2A22" stroke="{INK}" stroke-width="2"></rect>')
    s = h * 0.6 / 64
    for i, (nm, c) in enumerate((("GOLD", "#E8B830"), ("SILVER", "#C8CCD4"), ("BRASS", "#B5652E"), ("STONE", "#8A8478"), ("WOOD", "#7A4A2A"))):
        x = w * (0.12 + 0.19 * i)
        o.append(idol(x, h * 0.8, s, color=c) + label(x, h * 0.92, nm, "#C8B080", max(8, min(10, h / 24))))
    return "".join(o)

def mighty_angel(p, w, h, seed, stage="stand"):
    """Another strong angel coming down out of heaven (10:1–11): a great figure of white light arrayed with a cloud, the
    rainbow upon his head, his face as the sun (a sun's disc, no features), his feet as pillars of fire — the right foot
    upon the sea and the left upon the earth — a little book open in his hand. stage "thunders" (the seven thunders over the
    sea), "oath" (his right hand lifted up to heaven), "book" (John on the shore taking the little book out of his hand)."""
    o = [defs(p), sky(w, h, "#2A3A6A", "#E8C8A0")]
    if stage == "thunders":
        o[1] = sky(w, h, "#14141E", "#4A4A6A")
        for i in range(7): o.append(bolt(w * (0.06 + 0.13 * i), 0, h * 0.6, seed + i, sw=3))
    hz = h * 0.66
    o.append(sea(w, h, hz, seed, color="#2A6A9A", deep="#0F4C68"))
    cx = w * 0.46 if stage != "book" else w * 0.4
    s = h * 0.82 / 205
    b = h * 0.95
    lx = cx + 4 * s                                           # the shore: his left foot on the earth, his right on the sea
    o.append(f'<path d="M{f(lx - 30)} {f(h + 10)} L {f(lx)} {f(hz)} C {f(lx + w * 0.12)} {f(hz - h * 0.04)} {f(w * 0.86)} {f(hz - h * 0.02)} {f(w + 10)} {f(hz - h * 0.04)} L {f(w + 10)} {f(h + 10)} Z" '
             f'fill="#8A7A5A" stroke="{INK}" stroke-width="2.4"></path>')
    o.append(halo(cx, b - 110 * s, 160 * s, "#FFF4C2", 0.6))
    for k, c in enumerate(("#D7261E", "#FF8A2E", "#FFD23F", "#2E9A5A", "#3A6AB0", "#7A3BA8")):
        rr = (52 - k * 4) * s
        o.append(f'<path d="M{f(cx - rr)} {f(b - 186 * s)} A {f(rr)} {f(rr)} 0 0 1 {f(cx + rr)} {f(b - 186 * s)}" fill="none" stroke="{c}" stroke-width="{f(4 * s)}" opacity="0.9"></path>')
    for dx, dy, rr in ((-60, -60, 46), (60, -70, 44), (-80, -120, 36), (80, -126, 34), (-20, -40, 40), (30, -30, 38)):
        o.append(f'<ellipse cx="{f(cx + dx * s)}" cy="{f(b + dy * s)}" rx="{f(rr * s)}" ry="{f(rr * 0.5 * s)}" fill="#F3EEF4" stroke="#B8A8C8" stroke-width="2" opacity="0.85"></ellipse>')
    up = {"oath": [(-22, -158), (-30, -186), (-34, -214)], "book": [(-22, -158), (-46, -140), (-66, -126)]}.get(stage, [(-22, -158), (-46, -150), (-66, -146)])
    bk = '<path d="M-82 -126 L -66 -120 L -50 -126 L -50 -138 L -66 -132 L -82 -138 Z" fill="#F3E8C8" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(angel(p, cx, b, s, up=up, flip=stage != "book", glow=False, extra=bk if stage != "oath" else ""))
    o.append(halo(cx, b - 188 * s, 26 * s, "#FFE680", 0.9) + f'<circle cx="{f(cx)}" cy="{f(b - 188 * s)}" r="{f(13 * s)}" fill="#FFE680" stroke="#E8B830" stroke-width="2"></circle>'
             + rays(cx, b - 188 * s, 16, 16 * s, 34 * s, "#FFE680", 0.8, 2))
    for d in (-1, 1):                                         # his feet as pillars of fire, at the hem of the robe
        o.append(E.blaze(cx + d * 22 * s, b + 2, 30 * s, 64 * s, seed + d, n=4))
    for k in range(3):
        o.append(f'<ellipse cx="{f(cx - 22 * s)}" cy="{f(b + 2 + k * 5)}" rx="{f(24 * s + k * 12)}" ry="{f(3 + k * 2)}" fill="none" stroke="#E8F4F8" stroke-width="2" opacity="{0.8 - k * 0.2:.1f}"></ellipse>')
    if stage == "book":
        js = h * 0.32 / 205
        o.append(john_fig(p, w * 0.82, hz + h * 0.2, js, flip=True, up=[(-22, -158), (-40, -170), (-56, -184)]))
    return "".join(o)

def measure(w, h):
    """Rise, and measure the temple of God, and the altar, and them that worship therein (11:1–2): a plate — the temple and
    the altar within the measured line, the court without left unmeasured (given unto the nations), the reed like a rod."""
    import exo.art8 as B
    from epistle import plate_bg
    o = [plate_bg(w, h, "THE TEMPLE OF GOD · MEASURED WITH A REED LIKE UNTO A ROD")]
    B._W[0] = w
    x0, y0, x1, y1 = w * 0.06, h * 0.16, w * 0.62, h * 0.9
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(x1 - x0)}" height="{f(y1 - y0)}" fill="#3A1A2A" opacity="0.5" stroke="#FF6A4A" stroke-width="1.6" stroke-dasharray="6 4"></rect>')
    ix0, iy0, ix1, iy1 = x0 + (x1 - x0) * 0.2, y0 + (y1 - y0) * 0.16, x1 - (x1 - x0) * 0.2, y1 - (y1 - y0) * 0.16
    o.append(f'<rect x="{f(ix0)}" y="{f(iy0)}" width="{f(ix1 - ix0)}" height="{f(iy1 - iy0)}" fill="#12223A" stroke="#FFD23F" stroke-width="2.4"></rect>')
    tw, th = (ix1 - ix0) * 0.3, (iy1 - iy0) * 0.6
    o.append(f'<rect x="{f(ix0 + (ix1 - ix0) * 0.58)}" y="{f(iy0 + (iy1 - iy0) * 0.2)}" width="{f(tw)}" height="{f(th)}" fill="#E8D8A0" stroke="#FFD23F" stroke-width="2"></rect>')
    o.append(f'<rect x="{f(ix0 + (ix1 - ix0) * 0.2)}" y="{f(iy0 + (iy1 - iy0) * 0.42)}" width="{f((ix1 - ix0) * 0.12)}" height="{f((iy1 - iy0) * 0.16)}" fill="#E8B830" stroke="#FFD23F" stroke-width="1.6"></rect>')
    o.append(dim(ix0, iy1 + 12, ix1, iy1 + 12, "MEASURED", size=8))
    o.append(f'<path d="M{f(w * 0.68)} {f(h * 0.82)} L {f(w * 0.96)} {f(h * 0.3)}" stroke="#C8A060" stroke-width="7" stroke-linecap="round"></path>'
             + "".join(f'<path d="M{f(w * 0.68 + (w * 0.28) * k / 6 - 6)} {f(h * 0.82 - (h * 0.52) * k / 6 - 3)} l 12 6" stroke="#0D0D0F" stroke-width="1.4"></path>' for k in range(1, 6)))
    tx = w * 0.66
    o.append(tag(ix0 + (ix1 - ix0) * 0.73, iy0 + (iy1 - iy0) * 0.3, "THE TEMPLE OF GOD", tx, h * 0.2))
    o.append(tag(ix0 + (ix1 - ix0) * 0.26, iy0 + (iy1 - iy0) * 0.5, "THE ALTAR", x0 + 8, y0 + 18))
    o.append(label((x0 + x1) / 2, y1 - 8, "THE COURT WHICH IS WITHOUT · MEASURE IT NOT", "#FF6A4A", 8))
    o.append(label(w * 0.83, h * 0.9, "A REED LIKE UNTO A ROD", "#C8A060", 9))
    return "".join(o)

SACK = "#7A6A50"

def witness(p, x, b, s, flip=False, up=None, light=False):
    """One of the two witnesses: clothed in sackcloth (a coarse brown robe with its weave), a dark headcloth, a beard."""
    if light:
        return angel(p, x, b, s, up=up, flip=flip)
    weave = "".join(f'<path d="M-16 {y} L 16 {y}" stroke="#5A4A38" stroke-width="1" opacity="0.6"></path>' for y in range(-100, 0, 9))
    return robed(p, x, b, s, SACK, head="#B8A888", cord="#5A4A38", beard="#3A2A1A", up=up, flip=flip, extra=weave)

def witnesses(p, w, h, seed, stage="stand"):
    """The two witnesses (11:3–13). "stand": the two in sackcloth before the Lord of the earth, between the two olive trees
    and the two candlesticks; "drought": the heaven shut — a brazen sky over cracked earth, the two small on a hill;
    "street": the street of the great city at evening, empty — no one lying in it (what lies there is in the words), its
    people far off on the roofs; "rise": two figures of light going up into a cloud over the city; "quake": the tenth part
    of the city fallen."""
    o = [defs(p)]
    if stage == "stand":
        o += [sky(w, h, "#3A3A6A", "#E8D0A0"), halo(w * 0.5, h * 0.2, w * 0.5, "#FFF4C2", 0.7)]
        o.append(hills(w, h, h * 0.8, seed, color="#7A8A5A", amp=10, step=90) + ground(w, h, h * 0.86, "#9A9A6A", dy=0))
        for x in (0.1, 0.9): o.append(olive(w * x, h * 0.98, h * 0.8 / 150, seed=int(x * 10)))
        for x in (0.26, 0.74): o.append(candlestick(w * x, h * 0.96, h * 0.62 / 128))
        s = h * 0.8 / 205
        o.append(witness(p, w * 0.42, h * 0.97, s, flip=True) + witness(p, w * 0.58, h * 0.97, s, up=[(-22, -158), (-36, -180), (-44, -202)]))
        return "".join(o)
    if stage == "drought":
        o += [sky(w, h, "#C8702A", "#F3D8A0"), halo(w * 0.7, h * 0.2, h * 0.3, "#FFF4C2", 0.8)]
        o.append(ground(w, h, h * 0.62, "#C8A06A", dy=0))
        r = random.Random(seed)
        for _ in range(16):
            x, y = r.uniform(0, w), r.uniform(h * 0.66, h)
            o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-30, 30))} {f(r.uniform(8, 20))} l {f(r.uniform(-20, 20))} {f(r.uniform(6, 16))}" fill="none" stroke="#7A5A3A" stroke-width="2"></path>')
        o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.64)} C {f(w * 0.4)} {f(h * 0.5)} {f(w * 0.6)} {f(h * 0.5)} {f(w * 0.7)} {f(h * 0.64)} Z" fill="#B88A5A" stroke="{INK}" stroke-width="2"></path>')
        s = h * 0.26 / 205
        o.append(witness(p, w * 0.46, h * 0.56, s, flip=True, up=[(-22, -158), (-36, -180), (-44, -202)]) + witness(p, w * 0.54, h * 0.56, s))
        o.append(tree(w * 0.12, h * 0.98, h / 420, kind="bare", seed=seed) + tree(w * 0.88, h * 0.98, h / 460, kind="bare", seed=seed + 1))
        return "".join(o)
    # the great city
    tone = {"street": ("#1A1028", "#8A4A5A"), "rise": ("#2A3A7A", "#E8C8A0"), "quake": ("#2A1A1A", "#8A5A4A")}[stage]
    o += [sky(w, h, *tone)]
    hz = h * 0.6
    r = random.Random(seed)
    o.append(houses(-10, w * 0.3, hz + h * 0.05, h * 0.3, seed, lit=stage == "street") + houses(w * 0.7, w + 10, hz + h * 0.05, h * 0.3, seed + 1, lit=stage == "street"))
    o.append(f'<path d="M{f(w * 0.3)} {f(hz + h * 0.05)} L {f(w * 0.7)} {f(hz + h * 0.05)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></path>')
    for k in range(1, 6):
        y = hz + h * 0.05 + (h * 0.4) * (k / 6) ** 1.4
        o.append(f'<path d="M{f(w * 0.3 - (w * 0.4) * (k / 6) ** 1.4)} {f(y)} L {f(w * 0.7 + (w * 0.4) * (k / 6) ** 1.4)} {f(y)}" stroke="#6A5A4A" stroke-width="1.4"></path>')
    o.append(f'<rect x="{f(-10)}" y="{f(hz - h * 0.2)}" width="{f(w * 0.24)}" height="{f(h * 0.3)}" fill="#C8B090" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(w * 0.76)}" y="{f(hz - h * 0.22)}" width="{f(w * 0.26)}" height="{f(h * 0.32)}" fill="#C0A888" stroke="{INK}" stroke-width="2"></rect>')
    if stage == "street":
        for i in range(8):
            x = (r.uniform(0.02, 0.2) if i < 4 else r.uniform(0.8, 0.98)) * w
            o.append(f'<circle cx="{f(x)}" cy="{f(hz - h * 0.22 - 6)}" r="4" fill="#2A1A10"></circle><rect x="{f(x - 4)}" y="{f(hz - h * 0.22 - 2)}" width="8" height="10" fill="#4A3A5A"></rect>')
    if stage == "rise":
        o.append(halo(w * 0.5, h * 0.18, h * 0.3, WHITE, 0.85))
        for dx, rr in ((-0.1, 40), (0.08, 46), (0.0, 36)):
            o.append(f'<ellipse cx="{f(w * (0.5 + dx))}" cy="{f(h * 0.14)}" rx="{f(rr * h / 200)}" ry="{f(rr * h / 500)}" fill="#F3EEF4" stroke="#B8A8C8" stroke-width="1.6" opacity="0.9"></ellipse>')
        s = h * 0.24 / 205
        o.append(witness(p, w * 0.46, h * 0.42, s, light=True, up=[(-22, -158), (-36, -180), (-44, -202)]) + witness(p, w * 0.54, h * 0.38, s, light=True, flip=True, up=[(-22, -158), (-36, -180), (-44, -202)]))
    if stage == "quake":
        o.append(ruin(w * 0.76, w + 10, hz + h * 0.05, h * 0.26, seed) + smoke(w * 0.86, hz - h * 0.1, 7, seed, color="#8A7A6A", op=0.5, k=h / 300))
        for k in range(4):
            x0 = w * (0.36 + 0.08 * k)
            o.append(f'<path d="M{f(x0)} {f(hz + h * 0.08)} L {f(x0 + 10)} {f(hz + h * 0.2)} L {f(x0 - 4)} {f(hz + h * 0.3)} L {f(x0 + 14)} {f(h + 10)}" fill="none" stroke="#2A1A10" stroke-width="3"></path>')
    return "".join(o)

def seventh(p, w, h, seed):
    """The seventh angel sounded (11:15): an angel of light sounding in a great light over the earth."""
    o = [defs(p), sky(w, h, "#1A1440", "#E8C8A0"), halo(w * 0.5, h * 0.3, w * 0.7, "#FFF4C2", 0.85), rays(w * 0.5, h * 0.3, 40, h * 0.1, w, "#FFFDF0", 0.35, 5)]
    o.append(hills(w, h, h * 0.86, seed, color="#5A6A8A", amp=12, step=90))
    o.append(trumpeter(p, w * 0.5, h * 0.9, h * 0.8 / 205, sounding=True))
    return "".join(o)

def ark_heaven(p, w, h, seed):
    """There was opened the temple of God that is in heaven, and there was seen in his temple the ark of his covenant
    (11:19): the doors of the temple opened on light, the ark of gold within (joshua1.ark), lightnings and great hail."""
    r = random.Random(seed)
    o = [defs(p), sky(w, h, "#14141E", "#3A3A5A")]
    for i in range(3): o.append(bolt(w * (0.1 + 0.4 * i), 0, h * 0.5, seed + i, sw=3))
    tx0, tx1 = w * 0.22, w * 0.78
    o.append(f'<rect x="{f(tx0)}" y="{f(h * 0.16)}" width="{f(tx1 - tx0)}" height="{f(h * 0.8)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2.6"></rect>'
             f'<path d="M{f(tx0 - 20)} {f(h * 0.17)} L {f((tx0 + tx1) / 2)} {f(h * 0.02)} L {f(tx1 + 20)} {f(h * 0.17)} Z" fill="#D8CCB0" stroke="{INK}" stroke-width="2.6"></path>')
    dx0, dx1 = w * 0.36, w * 0.64
    o.append(f'<rect x="{f(dx0)}" y="{f(h * 0.3)}" width="{f(dx1 - dx0)}" height="{f(h * 0.66)}" fill="#FFF8DC" stroke="{INK}" stroke-width="2"></rect>'
             + halo((dx0 + dx1) / 2, h * 0.66, h * 0.4, WHITE, 0.9))
    for d, x in ((-1, dx0), (1, dx1)):
        o.append(f'<path d="M{f(x)} {f(h * 0.3)} L {f(x + d * w * 0.08)} {f(h * 0.34)} L {f(x + d * w * 0.08)} {f(h * 0.94)} L {f(x)} {f(h * 0.96)} Z" fill="#C8962E" stroke="{INK}" stroke-width="2"></path>')
    o.append(J1.ark((dx0 + dx1) / 2, h * 0.94, h * 0.36 / 110, uid=f"{p}ak", pole=90))
    for _ in range(30):
        x, y = r.uniform(0, w), r.uniform(0, h)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(2, 4))}" fill="#E8F4F8" stroke="#6A8A9A" stroke-width="1"></circle>')
    return "".join(o)
