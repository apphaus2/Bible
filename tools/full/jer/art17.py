"""Drawings for Jeremiah chapter 17 (Jeremiah 49–50), on top of jer.art: Ammon, Edom, Damascus, Kedar and Hazor, Elam as
maps; Edom's nest in the clefts of the rock; the tents and camels of Kedar; the bow of Elam broken and the four winds; then
Babylon taken: Bel and Merodach put to shame, the exiles going home weeping, the archers round about, the hammer of the whole
earth broken, the sword upon the Chaldeans, the drought upon her waters, the wild beasts in the ruins."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jer.art import *
from jer.art import f, K2
from jer.art10 import babylon
from jer.art16 import eagle, heshbon_fire
from jer.art4 import idol
from jer.art7 import cursed_day
from jer.art8 import flock

def petra(w, h, seed, eagle_=False):
    """O thou that dwellest in the clefts of the rock, that holdest the height of the hill; though thou make thy nest as high as
    the eagle: red rock cliffs with dwellings cut in their face, a nest on the summit."""
    o = [K2.sky(w, h, "#E8A060", "#F8E0B0"), crag(-10, w * 0.6, h + 10, h * 0.12, color="#B8503A", dark="#7A3020"), crag(w * 0.44, w + 10, h + 10, h * 0.26, color="#C8603A", dark="#8A3A24")]
    for i in range(5):
        x, y = w * (0.12 + i * 0.16), h * (0.5 + (i % 2) * 0.16)
        o.append(f'<path d="M{f(x - 14)} {f(y + 30)} L {f(x - 14)} {f(y)} Q {f(x)} {f(y - 16)} {f(x + 14)} {f(y)} L {f(x + 14)} {f(y + 30)} Z" fill="#3A1A12" stroke="#0D0D0F" stroke-width="1.8"></path>'
                 f'<rect x="{f(x - 22)}" y="{f(y - 22)}" width="44" height="6" fill="#D8784A" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    o.append(f'<ellipse cx="{f(w * 0.3)}" cy="{f(h * 0.13)}" rx="22" ry="7" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    return "".join(o)

def kedar_tents(p, w, h, seed, taken=False):
    """Kedar, the children of the east, a nation at ease that dwelleth without care, that hath neither gates nor bars: black tents
    and camels in the desert (taken=True: the tents struck, curtains and camels led away)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#E8A060", "#F8E0A8"), hills(w, h, h * 0.5, seed, "#C8946A", amp=10, step=90), ground(w, h, h * 0.58, "#E8C890", dy=0)]
    s = min(0.8, h / 380)
    if not taken:
        for i in range(4): o.append(E4.tent(w * (0.06 + i * 0.2), h * (0.84 - (i % 2) * 0.06), w * 0.16, h * 0.18, color="#1E1814"))
        for i in range(3): o.append(J1.camel(w * (0.2 + i * 0.26), h * 0.96, s * (0.9 + (i % 2) * 0.1), color="#B5844A"))
    else:
        for i in range(4): o.append(J1.camel(w * (0.86 - i * 0.2), h * (0.94 - (i % 2) * 0.04), s, flip=True, color="#B5844A"))
        sw = fit(b, h * 0.6)
        for i in range(3): o.append(warrior(p, w * (0.1 + i * 0.2), b, sw, BABEL_C, flip=True))
        for k in range(3): o.append(f'<path d="M{f(w * (0.12 + k * 0.3))} {f(h * 0.7)} l 30 -6 l 24 8" stroke="#1E1814" stroke-width="3" fill="none"></path>')
    return "".join(o)

def damascus_fire(w, h, seed):
    """I will kindle a fire in the wall of Damascus, and it shall devour the palaces of Ben-hadad (no one drawn)."""
    o = [K2.sky(w, h, "#2A0A0A", "#B8502A"), wall(-10, w + 10, h * 0.42, h * 0.78, seed, towers=4, gate=w * 0.5, color="#B8A07A"), ground(w, h, h * 0.78, "#2A1A14", dy=0)]
    o += [E.blaze(w * (0.14 + i * 0.24), h * 0.5, w * 0.12, h * 0.3, seed + i, n=5) for i in range(4)]
    o.append(smoke(w * 0.5, h * 0.24, 8, seed, w=0.8))
    return "".join(o)

def bow_broken(w, h, seed):
    """I will break the bow of Elam, the chief of their might; the four winds from the four quarters of heaven: a great bow snapped
    in two, wind-lines from the four corners."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1A2A"></rect>']
    for (x, y) in ((0, 0), (w, 0), (0, h), (w, h)):
        for k in range(4):
            o.append(f'<path d="M{f(x)} {f(y + (k - 1.5) * 16)} Q {f(w * 0.5)} {f(h * 0.5 + (k - 1.5) * 20)} {f(w - x)} {f(h - y + (k - 1.5) * 16)}" stroke="#8A9AB8" stroke-width="1.6" fill="none" opacity="0.4"></path>')
    cx, cy, R = w * 0.5, h * 0.56, min(w * 0.3, h * 0.36)
    o.append(f'<path d="M{f(cx - R)} {f(cy)} Q {f(cx - R * 0.6)} {f(cy - R * 0.8)} {f(cx - 8)} {f(cy - R * 0.6)}" stroke="#8A5A2A" stroke-width="8" fill="none" stroke-linecap="round"></path>'
             f'<path d="M{f(cx + 8)} {f(cy - R * 0.5)} Q {f(cx + R * 0.6)} {f(cy - R * 0.7)} {f(cx + R)} {f(cy + 6)}" stroke="#8A5A2A" stroke-width="8" fill="none" stroke-linecap="round"></path>'
             f'<path d="M{f(cx - R)} {f(cy)} Q {f(cx)} {f(cy + R * 0.2)} {f(cx + R)} {f(cy + 6)}" stroke="#E8D8B0" stroke-width="1.6" fill="none" stroke-dasharray="8 6"></path>'
             f'<path d="M{f(cx - 10)} {f(cy - R * 0.62)} l 6 -14 l 8 10 l 6 -8" stroke="#FFE680" stroke-width="2.4" fill="none"></path>')
    return "".join(o)

def bel_shamed(w, h, seed):
    """Babylon is taken, Bel is put to shame, Merodach is dismayed; her images are put to shame: two great gilded images fallen
    on their faces before the temple tower."""
    o = [K2.sky(w, h, "#5A3A4A", "#E8A070"), ground(w, h, h * 0.66, "#C8A070", dy=0)]
    zx, zb = w * 0.5, h * 0.66
    for k in range(4):
        tw = w * (0.4 - k * 0.08); th = h * 0.1
        o.append(f'<rect x="{f(zx - tw / 2)}" y="{f(zb - th * (k + 1))}" width="{f(tw)}" height="{f(th)}" fill="{["#C8A070", "#D8B080"][k % 2]}" stroke="#0D0D0F" stroke-width="2"></rect>')
    s = min(1.0, h / 260)
    for x, rot in ((0.2, 88), (0.8, -92)):
        o.append(f'<g transform="rotate({rot} {f(w * x)} {f(h * 0.9)})">' + idol(w * x, h * 0.9, s, decked=True) + '</g>')
    return "".join(o)

def going_home(p, w, h, seed):
    """The children of Israel and the children of Judah together shall go on their way weeping, and shall seek Jehovah their God;
    they shall inquire concerning Zion with their faces thitherward: a company on the road west at dawn, heads bowed."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#4A4A7A", "#FFD8A0"), hills(w, h, h * 0.54, seed, "#7A7A5A", amp=10, step=90), ground(w, h, h * 0.62, "#C8B080", dy=0)]
    for i in range(8):
        t = i / 7; x = w * (0.94 - 0.8 * t); y = h * (0.96 - 0.28 * t)
        s = fit(y, y - h * (0.34 - 0.2 * t))
        o.append(man(p, x, y, s, ["#6A5A3A", "#5A4A6A", "#6A3A2A", "#4A5A3A"][i % 4], flip=True) if i % 2 == 0 else woman(p, x, y, s * 0.94, ["#8A5A6A", "#6A5A3A", "#5A3A5A"][i % 3], flip=True))
    return "".join(o)

def he_goats(w, h, seed):
    """Flee out of the midst of Babylon, and be as the he-goats before the flocks: goats leading a flock out of a gate."""
    o = [K2.sky(w, h, "#8FB0C8", "#F3E0B0"), wall(w * 0.6, w + 10, h * 0.34, h * 0.76, seed, towers=2, gate=w * 0.8, color="#2A5A9A"), ground(w, h, h * 0.76, "#C8A870", dy=0)]
    s = min(0.8, h / 300)
    for i in range(3):
        x = w * (0.12 + i * 0.12)
        o.append(E.sheep(x, h * 0.94, s, flip=True, wool="#3A3028", face="#2A2018") + f'<path d="M{f(x - 22 * s)} {f(h * 0.94 - 40 * s)} q -10 -16 4 -24" stroke="#C8B88A" stroke-width="3" fill="none"></path>')
    for i in range(5): o.append(E.sheep(w * (0.5 + i * 0.08), h * (0.94 - (i % 2) * 0.03), s * 0.85, flip=True))
    return "".join(o)

def archers(p, w, h, seed):
    """Set yourselves in array against Babylon round about, all ye that bend the bow; shoot at her, spare no arrows: archers
    before the blue walls, arrows in the air."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), babylon(w, h * 0.86, seed)]
    s = fit(b, max(h * 0.5, b - 180))
    r = random.Random(seed)
    for i in range(6):
        x = w * (0.06 + i * 0.16)
        o.append(man(p, x, b, s, ["#5A3A2A", "#3A3A5A", "#6A4A2A"][i % 3], up=[(22, -158), (50, -176), (76, -190)], extra=A.headcloth(["#5A3A2A", "#3A3A5A", "#6A4A2A"][i % 3])))
        o.append(f'<path d="M{f(x + 70 * s)} {f(b - 220 * s)} Q {f(x + 90 * s)} {f(b - 186 * s)} {f(x + 70 * s)} {f(b - 150 * s)}" stroke="#4A2A1A" stroke-width="3" fill="none"></path>')
    for _ in range(14):
        x, y = r.uniform(0, w), r.uniform(h * 0.1, h * 0.5)
        o.append(f'<path d="M{f(x)} {f(y)} l 22 -10" stroke="#3A2A1A" stroke-width="2"></path><path d="M{f(x + 22)} {f(y - 10)} l -6 0 l 2 4 Z" fill="#3A2A1A"></path>')
    return "".join(o)

def hunted_sheep(w, h, seed):
    """Israel is a hunted sheep; the lions have driven him away: a lone sheep on the hillside, a lion's shape behind the rocks."""
    o = [K2.sky(w, h, "#8A7A8A", "#E8C8A0"), hills(w, h, h * 0.5, seed, "#8A7A5A", amp=14, step=70), ground(w, h, h * 0.66, "#B8A07A", dy=0),
         E4.rock(w * 0.56, h * 0.62, w * 0.26, h * 0.22), JG2.lion(w * 0.66, h * 0.66, min(0.6, h / 500), roar=False), E.sheep(w * 0.24, h * 0.92, min(1.0, h / 260))]
    return "".join(o)

def pasture(w, h, seed):
    """I will bring Israel again to his pasture, and he shall feed on Carmel and Bashan, upon the hills of Ephraim and in Gilead."""
    o = [K2.sky(w, h, "#8FC0E0", "#FFF0C8"), hills(w, h, h * 0.44, seed, "#5A8A4A", amp=16, step=70), hills(w, h, h * 0.58, seed + 1, "#6A9A4A", amp=10, step=90), ground(w, h, h * 0.7, "#9AC05A", dy=0)]
    s = min(0.7, h / 380)
    for i in range(8): o.append(E.sheep(w * (0.08 + i * 0.11), h * (0.9 - (i % 3) * 0.04), s))
    return "".join(o)

def hammer_broken(w, h, seed):
    """How is the hammer of the whole earth cut asunder and broken!: a great war-hammer lying broken in two in the dust."""
    o = [K2.sky(w, h, "#3A2A2A", "#B8806A"), ground(w, h, h * 0.66, "#8A7A5A", dy=0), V.rays(w * 0.5, h * 0.84, 24, 10, max(w, h) * 0.6, color="#FFE680", op=0.08)]
    hx, hy, s = w * 0.36, h * 0.86, min(1.6, h / 160)
    o.append(f'<g transform="rotate(-12 {f(hx)} {f(hy)})"><rect x="{f(hx - 40 * s)}" y="{f(hy - 26 * s)}" width="{f(80 * s)}" height="{f(44 * s)}" fill="#5A5A62" stroke="#0D0D0F" stroke-width="2.6"></rect>'
             f'<rect x="{f(hx + 40 * s)}" y="{f(hy - 8 * s)}" width="{f(70 * s)}" height="{f(10 * s)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect></g>'
             f'<g transform="rotate(18 {f(w * 0.72)} {f(hy)})"><rect x="{f(w * 0.62)}" y="{f(hy - 6 * s)}" width="{f(110 * s)}" height="{f(10 * s)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect></g>')
    return "".join(o)

def snare_babylon(w, h, seed):
    """I have laid a snare for thee, and thou art also taken, O Babylon: a fowler's snare closed round the gate of the city."""
    o = [babylon(w, h, seed, dusk=True)]
    for k in range(9):
        o.append(f'<path d="M{f(w * (0.04 + k * 0.115))} {f(h * 0.4)} Q {f(w * 0.5)} {f(h * 0.0)} {f(w * (0.96 - k * 0.115))} {f(h * 0.4)}" stroke="#C8A878" stroke-width="1.2" fill="none" opacity="0.6"></path>')
    return "".join(o)

def armory(w, h, seed):
    """Jehovah hath opened his armory, and hath brought forth the weapons of his indignation: an open storehouse of spears, bows
    and shields under a stormy sky (no hand)."""
    o = [K2.sky(w, h, "#1A1A2A", "#5A5A6A"), E2.bolt(w * 0.8, h * 0.06, h * 0.4, seed), ground(w, h, h * 0.86, "#3A3438", dy=0),
         f'<rect x="{f(w * 0.2)}" y="{f(h * 0.36)}" width="{f(w * 0.5)}" height="{f(h * 0.5)}" fill="#2A2228" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<path d="M{f(w * 0.16)} {f(h * 0.36)} L {f(w * 0.45)} {f(h * 0.2)} L {f(w * 0.74)} {f(h * 0.36)} Z" fill="#4A4048" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for k in range(7):
        x = w * (0.24 + k * 0.06)
        o.append(f'<path d="M{f(x)} {f(h * 0.84)} L {f(x)} {f(h * 0.44)}" stroke="#8A5A30" stroke-width="3"></path><path d="M{f(x - 5)} {f(h * 0.46)} L {f(x)} {f(h * 0.4)} L {f(x + 5)} {f(h * 0.46)} Z" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="1.2"></path>')
    for k in range(2):
        o.append(f'<ellipse cx="{f(w * (0.6 + k * 0.05))}" cy="{f(h * 0.74)}" rx="{f(w * 0.03)}" ry="{f(h * 0.08)}" fill="#B87333" stroke="#0D0D0F" stroke-width="1.8"></ellipse>')
    return "".join(o)

def bullocks(w, h, seed):
    """Open her store-houses; cast her up as heaps: storehouses broken open, the grain heaped and scattered."""
    o = [K2.sky(w, h, "#5A3A3A", "#D8A070"), ground(w, h, h * 0.7, "#B8946A", dy=0),
         S4b.stone_heap(w * 0.3, h * 0.94, w * 0.3, h * 0.2, seed), R1.heap(w * 0.72, h * 0.94, w * 0.3, h * 0.24)]
    return "".join(o)

def sword_upon(w, h, seed):
    """A sword is upon the Chaldeans, upon her princes and her wise men, upon her horses and chariots, upon her treasures: a drawn
    sword over Babylon's walls at dusk (no hand)."""
    o = [babylon(w, h, seed, dusk=True)]
    cx, cy, L = w * 0.5, h * 0.24, min(w * 0.5, h * 0.36)
    o.append(f'<g transform="rotate(90 {f(cx)} {f(cy)})"><path d="M{f(cx - 6)} {f(cy - L * 0.6)} L {f(cx)} {f(cy - L * 0.72)} L {f(cx + 6)} {f(cy - L * 0.6)} L {f(cx + 6)} {f(cy + L * 0.3)} L {f(cx - 6)} {f(cy + L * 0.3)} Z" fill="#D8D8E0" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<rect x="{f(cx - 20)}" y="{f(cy + L * 0.3)}" width="40" height="8" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></rect>'
             f'<rect x="{f(cx - 5)}" y="{f(cy + L * 0.3 + 8)}" width="10" height="{f(L * 0.18)}" fill="#6A3A1E" stroke="#0D0D0F" stroke-width="1.6"></rect></g>')
    return "".join(o)

def dry_river(w, h, seed):
    """A drought is upon her waters, and they shall be dried up: the river-bed of Babylon cracked and dry under the walls."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#E8A060", "#F8E0A8"), wall(-10, w + 10, h * 0.3, h * 0.56, seed, towers=4, color="#2A5A9A"), ground(w, h, h * 0.56, "#C8A070", dy=0),
         f'<path d="M-10 {f(h * 0.7)} C {f(w * 0.3)} {f(h * 0.66)} {f(w * 0.6)} {f(h * 0.76)} {f(w + 10)} {f(h * 0.7)} L {f(w + 10)} {f(h * 0.92)} C {f(w * 0.6)} {f(h * 0.98)} {f(w * 0.3)} {f(h * 0.88)} -10 {f(h * 0.92)} Z" fill="#D8C090" stroke="#0D0D0F" stroke-width="2"></path>']
    for _ in range(26):
        x, y = r.uniform(0, w), r.uniform(h * 0.72, h * 0.9)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-20, 20))} {f(r.uniform(-5, 5))} l {f(r.uniform(-14, 14))} {f(r.uniform(-6, 6))}" stroke="#8A6A3A" stroke-width="1.6" fill="none"></path>')
    return "".join(o)

def ostriches(w, h, seed):
    """The wild beasts of the desert with the wolves shall dwell there, and the ostriches: broken walls in the desert, an ostrich
    and a jackal among them."""
    o = [K2.sky(w, h, "#E8A060", "#F8E0A8"), J.collapse(-10, w * 0.5, h * 0.78, h * 0.28, seed, color="#2A5A9A"), J.collapse(w * 0.6, w + 10, h * 0.8, h * 0.2, seed + 1, color="#C8A070"),
         ground(w, h, h * 0.8, "#D8B880", dy=0), grey_fox(w * 0.3, h * 0.94, min(1.0, h / 280))]
    x, y, s = w * 0.72, h * 0.94, min(1.3, h / 200)
    o.append(f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-30 -60 Q -10 -80 20 -66 Q 30 -50 10 -40 Q -20 -36 -30 -60 Z" fill="#2A2420" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M10 -64 L 18 -120 M18 -120 q 6 -4 10 0 l -4 4" stroke="#C8A890" stroke-width="5" fill="none"></path>'
             '<path d="M-6 -40 L -10 0 M6 -40 L 8 0" stroke="#C8A890" stroke-width="4"></path>'
             '<path d="M-34 -58 q -10 -6 -4 -14 q 6 6 10 4" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.4"></path></g>')
    return "".join(o)

def babylon_king(p, w, h, seed):
    """The king of Babylon hath heard the tidings of them, and his hands wax feeble: the king alone on his throne, a messenger
    kneeling, the lamps low."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84).replace("#8A5A30", "#2A4A7A"), S3.throne(w * 0.66, b, min(1.0, h / 300))]
    s = fit(b, max(h * 0.4, b - 220))
    o.append(king_fig(p, w * 0.66, b - 10, s, flip=True, cloth=BABEL_C))
    o.append(E.kneel(w * 0.3, b, s * 0.8, color="#5A4A3A", skin="#9A6A4A"))
    return "".join(o)

AMMON_P = ("RABBAH", "HESHBON", "AI", "GILEAD")
EDOM_P = ("TEMAN", "BOZRAH", "DEDAN")
DAM_P = ("DAMASCUS", "HAMATH", "ARPAD")
KEDAR_P = ("KEDAR", "HAZOR", "BABYLON")
ELAM_P = ("ELAM", "BABYLON", "THE MEDES")
