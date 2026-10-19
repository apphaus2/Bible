"""Drawings for Jeremiah chapter 16 (Jeremiah 46–48), on top of jer.art: the burdens of Egypt, the Philistines and Moab, as
technical maps with drawings of their images — the army of Egypt arrayed at Carchemish, the Nile rising, the fair heifer, the
hewers cutting down the forest, the waters out of the north, the sword of Jehovah, Moab settled on his lees, the vine of Sibmah,
the eagle, the fear and the pit and the snare, the fire out of Heshbon."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jer.art import *
from jer.art import f, K2
from jer.art8 import tempest
from jer.art6 import pit_snares

EGY = "#E8B830"
def egypt_army(p, w, h, seed, fleeing=False):
    """Prepare ye the buckler and shield; harness the horses: the army of Pharaoh-neco by the Euphrates, chariots and shield-
    bearers in their array (fleeing=True: turned backward, the chariots wheeling away)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#E8A060", "#F8E0A8"), f'<rect x="-10" y="{f(h * 0.52)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#2C7A9A"></rect>',
         ground(w, h, h * 0.58, "#D8B880", dy=0)]
    s = min(0.8, h / 400)
    for i in range(3):
        o.append(E3.chariot(w * (0.1 + i * 0.3), h * (0.8 + (i % 2) * 0.04), s * (0.9 + (i % 2) * 0.1), flip=fleeing, color="#3A2214", driver=EGY))
    sw = fit(b, h * 0.7)
    for i in range(8):
        x = w * (0.04 + i * 0.12)
        o.append(warrior(p, x, b, sw, "#F3EFE6", flip=fleeing) + f'<ellipse cx="{f(x + (-14 if fleeing else 14) * sw)}" cy="{f(b - 110 * sw)}" rx="{f(14 * sw)}" ry="{f(30 * sw)}" fill="#B87333" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    if fleeing: o.append(speed_lines(w, h, seed, 0.6, 0.95, n=14))
    return "".join(o)

def nile_rising(w, h, seed):
    """Egypt riseth up like the Nile, and his waters toss themselves like the rivers: the river in flood over its banks, palms
    standing in the water."""
    o = [K2.sky(w, h, "#5A6A8A", "#E8C8A0"), f'<rect x="-10" y="{f(h * 0.46)}" width="{f(w + 20)}" height="{f(h * 0.6)}" fill="#3A7A8A"></rect>']
    for k in range(6):
        y = h * (0.5 + k * 0.08)
        o.append(f'<path d="M-10 {f(y)} ' + " ".join(f"q {f(w / 14)} -16 {f(w / 7)} 0" for _ in range(8)) + '" fill="none" stroke="#E8F6FA" stroke-width="2.4"></path>')
    for k in range(4): o.append(J1.palm(w * (0.12 + k * 0.26), h * (0.7 + (k % 2) * 0.1), min(0.6, h / 500)))
    return "".join(o)

def heifer(w, h, seed):
    """Egypt is a very fair heifer; but destruction out of the north is come: a sleek heifer in a green field, a gadfly over her."""
    o = [K2.sky(w, h, "#8FC0E0", "#F3F0D0"), ground(w, h, h * 0.62, "#8AB85A", dy=0), J1.palm(w * 0.86, h * 0.66, min(0.6, h / 500))]
    o.append(S1.cow(w * 0.42, h * 0.94, min(1.6, h / 170), color="#D8A060", patch="#F3EFE6"))
    o.append(E2.fly(w * 0.62, h * 0.34, 2.0, rot=-20))
    return "".join(o)

def hewers_forest(p, w, h, seed):
    """They shall come against her with axes, as hewers of wood, and cut down her forest, though it cannot be searched; more
    than the locusts: felled palms, men with axes, a cloud of locusts behind."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#C8A070", "#F3E0B0"), E2.locusts(40, 0, w, h * 0.06, h * 0.36, seed), ground(w, h, h * 0.66, "#B8A070", dy=0)]
    for k in range(4): o.append(J1.palm(w * (0.56 + k * 0.12), h * 0.7, min(0.6, h / 500)))
    for k in range(3): o.append(f'<path d="M{f(w * (0.1 + k * 0.12))} {f(b - 4)} l {f(w * 0.1)} -8" stroke="#6A4A2A" stroke-width="9" stroke-linecap="round"></path>')
    s = fit(b, max(h * 0.44, b - 210))
    for i in range(3):
        x = w * (0.2 + i * 0.14)
        o.append(man(p, x, b, s, BABEL_C, up=[(-22, -158), (-30, -196), (-10, -226)]) + f'<path d="M{f(x - 10 * s)} {f(b - 226 * s)} l {f(-14 * s)} {f(-8 * s)} l {f(4 * s)} {f(18 * s)} Z" fill="#8A8A90" stroke="#0D0D0F" stroke-width="1.4"></path>')
    return "".join(o)

EGYPT_P = ("MIGDOL", "NOPH", "TAHPANHES", "NO", "PATHROS")
def egypt_cities(w, h):
    return near_east(w, h, EGYPT_P, hi=EGYPT_P, box=(28.0, 36.4, 24.6, 33.8), under=("MIGDOL", "NOPH"))

def carchemish_map(w, h):
    return near_east(w, h, ("CARCHEMISH", "EGYPT", "JERUSALEM", "BABYLON"), hi=("CARCHEMISH",), arrows=[("EGYPT", "CARCHEMISH"), ("BABYLON", "CARCHEMISH")], box=(28.0, 47.0, 26.6, 39.6))

def tabor_carmel(w, h, seed):
    """Surely like Tabor among the mountains, and like Carmel by the sea, so shall he come: the round mountain over the plain,
    the long ridge of Carmel against the sea."""
    o = [K2.sky(w, h, "#8FB0C8", "#F3E0B0"), f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w * 0.3)}" height="{f(h * 0.4)}" fill="#2C7A9A"></rect>',
         f'<path d="M-10 {f(h * 0.7)} L {f(w * 0.06)} {f(h * 0.5)} L {f(w * 0.38)} {f(h * 0.56)} L {f(w * 0.5)} {f(h * 0.72)} Z" fill="#4A6A3A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         J1.tabor(w * 0.72, h * 0.8, w * 0.36, h * 0.5, seed=seed), ground(w, h, h * 0.8, "#9AAA5A", dy=0)]
    return "".join(o)

def north_flood(w, h, seed):
    """Waters rise up out of the north, and shall become an overflowing stream, and shall overflow the land and the city: a dark
    flood running over the plain toward a walled town."""
    o = [K2.sky(w, h, "#3A3A4A", "#9A9AA0"), hills(w, h, h * 0.46, seed, "#5A5A4A", amp=12, step=80),
         wall(w * 0.62, w + 10, h * 0.44, h * 0.66, seed, towers=2, color="#B8A07A"), ground(w, h, h * 0.66, "#7A7A5A", dy=0),
         f'<path d="M-10 {f(h * 0.6)} C {f(w * 0.3)} {f(h * 0.62)} {f(w * 0.5)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.72)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2A5A7A" opacity="0.92"></path>']
    for k in range(4):
        y = h * (0.7 + k * 0.07)
        o.append(f'<path d="M-10 {f(y)} ' + " ".join(f"q {f(w / 16)} -10 {f(w / 8)} 0" for _ in range(9)) + '" fill="none" stroke="#C8E0E8" stroke-width="2"></path>')
    return "".join(o)

PHIL = ("GAZA", "ASHKELON", "ASHDOD", "EKRON", "TYRE", "SIDON")
def philistia_map(w, h):
    return near_east(w, h, PHIL, hi=PHIL, box=(33.6, 36.0, 31.1, 33.9), under=("EKRON", "SIDON", "GAZA"))

def sword_still(w, h, seed):
    """O thou sword of Jehovah, how long will it be ere thou be quiet? put up thyself into thy scabbard: a sword hanging above
    the sea-shore of Ashkelon, its scabbard empty beneath it (no hand)."""
    o = [K2.sky(w, h, "#3A1A2A", "#B8603A"), f'<rect x="-10" y="{f(h * 0.66)}" width="{f(w * 0.5)}" height="{f(h * 0.4)}" fill="#1F4A6A"></rect>',
         f'<path d="M{f(w * 0.36)} {f(h + 10)} C {f(w * 0.42)} {f(h * 0.76)} {f(w * 0.5)} {f(h * 0.68)} {f(w + 10)} {f(h * 0.66)} L {f(w + 10)} {f(h + 10)} Z" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></path>',
         wall(w * 0.6, w + 10, h * 0.5, h * 0.7, seed, towers=2, color="#B8A07A"), V.rays(w * 0.4, h * 0.36, 20, 10, min(w, h) * 0.5, color="#FFF4C2", op=0.2)]
    cx, cy, L = w * 0.4, h * 0.36, min(h * 0.5, w * 0.3)
    o.append(f'<g transform="rotate(30 {f(cx)} {f(cy)})"><path d="M{f(cx - 5)} {f(cy - L * 0.5)} L {f(cx)} {f(cy - L * 0.62)} L {f(cx + 5)} {f(cy - L * 0.5)} L {f(cx + 5)} {f(cy + L * 0.3)} L {f(cx - 5)} {f(cy + L * 0.3)} Z" fill="#D8D8E0" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<rect x="{f(cx - 18)}" y="{f(cy + L * 0.3)}" width="36" height="7" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></rect>'
             f'<rect x="{f(cx - 4)}" y="{f(cy + L * 0.3 + 7)}" width="8" height="{f(L * 0.16)}" fill="#6A3A1E" stroke="#0D0D0F" stroke-width="1.6"></rect></g>')
    return "".join(o)

MOAB_1 = ("NEBO", "KIRIATHAIM", "MISGAB", "HESHBON", "MADMEN", "HORONAIM", "LUHITH")
MOAB_2 = ("DIBON", "AROER", "THE ARNON", "HOLON", "JAHZAH", "MEPHAATH", "BETH-DIBLATHAIM", "BETH-GAMUL", "BETH-MEON", "KERIOTH", "BOZRAH OF MOAB")
MOAB_3 = ("KIR-HERES", "JAZER", "SIBMAH", "HESHBON", "ELEALEH", "JAHAZ", "ZOAR", "HORONAIM", "NIMRIM", "EGLATH-SHELISHIYAH")
def moab_map(w, h, names, size=9, box=(35.1, 36.4, 30.92, 32.05)):
    return near_east(w, h, names, hi=names, box=box, size=size, under=("KIRIATHAIM", "AROER", "HOLON", "BETH-GAMUL", "LUHITH", "NIMRIM", "SIBMAH", "MEPHAATH", "KERIOTH", "DIBON"))

def lees(w, h, seed, broken=False):
    """Moab hath settled on his lees, and hath not been emptied from vessel to vessel; them that pour off shall empty his vessels
    and break their bottles in pieces."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A22"></rect>', ground(w, h, h * 0.84, "#2A1E18", dy=0)]
    s = min(1.3, h / 200)
    for i in range(5):
        x = w * (0.14 + i * 0.18)
        o.append(jar(x, h * 0.88, s, color=["#B8703A", "#A8603A", "#C8804A"][i % 3], broken=broken and i % 2 == 1))
    return "".join(o)

def chemosh(w, h, seed):
    """Chemosh shall go forth into captivity, his priests and his princes together: the idol lashed on a cart, being hauled off."""
    o = [K2.sky(w, h, "#C8906A", "#F3D8A0"), hills(w, h, h * 0.5, seed, "#9A7A5A", amp=12, step=80), ground(w, h, h * 0.62, "#C8A070", dy=0)]
    s = min(1.0, h / 300)
    o.append(S1.cart(w * 0.5, h * 0.94, s, load=f'<g transform="translate(0 -70) scale(0.7)"><path d="M-16 -14 L -12 -150 Q 0 -168 12 -150 L 16 -14 Z" fill="#6A6A70" stroke="#0D0D0F" stroke-width="2.4"></path><circle cx="0" cy="-160" r="14" fill="#6A6A70" stroke="#0D0D0F" stroke-width="2.4"></circle></g>'))
    return "".join(o)

def dove_rock(w, h, seed):
    """Leave the cities, and dwell in the rock; and be like the dove that maketh her nest over the mouth of the abyss."""
    o = [K2.sky(w, h, "#8FB0C8", "#F3E0B0"), crag(w * 0.1, w * 0.9, h + 10, h * 0.14, color="#A8846A", dark="#6A5040"),
         f'<path d="M{f(w * 0.36)} {f(h * 0.7)} Q {f(w * 0.5)} {f(h * 0.54)} {f(w * 0.64)} {f(h * 0.7)} L {f(w * 0.6)} {f(h + 10)} L {f(w * 0.4)} {f(h + 10)} Z" fill="#14100E" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.56)}" rx="22" ry="7" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>',
         f'<g transform="translate({f(w * 0.5)} {f(h * 0.54)})"><path d="M-14 0 Q -10 -14 4 -12 L 12 -16 L 14 -12 L 8 -8 Q 10 2 -14 0 Z" fill="#E8E8F0" stroke="#0D0D0F" stroke-width="1.4"></path></g>']
    return "".join(o)

def sibmah(w, h, seed):
    """O vine of Sibmah, thy branches passed over the sea; upon thy summer fruits and upon thy vintage the destroyer is fallen;
    wine to cease from the winepresses: trampled vines and an empty winepress."""
    o = [vine(w, h, seed, wild=True), J1.winepress(w * 0.78, h * 0.9, w * 0.26, h * 0.12)]
    return "".join(o)

def bald_mourners(p, w, h, seed):
    """Every head is bald, and every beard clipped, and upon the loins sackcloth; lamentation on all the housetops of Moab: dark
    figures on the flat roofs."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#4A3A4A", "#B8908A")]
    r = random.Random(seed)
    x = -10
    while x < w:
        bw = w * r.uniform(0.14, 0.2); top = h * r.uniform(0.56, 0.66)
        o.append(f'<rect x="{f(x)}" y="{f(top)}" width="{f(bw)}" height="{f(h - top)}" fill="#B8A07A" stroke="#0D0D0F" stroke-width="2"></rect>')
        s = fit(top, top - h * 0.2)
        o.append(E.kneel(x + bw * 0.5, top, s, color="#2E2A2A", skin="#8A6A5A", flip=r.random() < 0.5))
        x += bw + 6
    return "".join(o)

def eagle(w, h, seed):
    """He shall fly as an eagle, and shall spread out his wings against Moab."""
    o = [K2.sky(w, h, "#5A6A8A", "#E8C8A0"), hills(w, h, h * 0.78, seed, "#7A5A4A", amp=14, step=70)]
    cx, cy, s = w * 0.5, h * 0.42, min(w, h) * 0.008
    o.append(f'<g transform="translate({f(cx)} {f(cy)}) scale({f(s)})">'
             '<path d="M0 0 C -30 -30 -70 -40 -110 -30 C -90 -20 -80 -10 -70 0 C -60 -6 -40 -2 -20 8 Z" fill="#3A2A1E" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M0 0 C 30 -30 70 -40 110 -30 C 90 -20 80 -10 70 0 C 60 -6 40 -2 20 8 Z" fill="#3A2A1E" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M-14 4 Q 0 -12 14 4 L 8 30 L 0 40 L -8 30 Z" fill="#4A3424" stroke="#0D0D0F" stroke-width="2"></path>'
             '<circle cx="0" cy="-8" r="9" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></circle><path d="M0 -6 l 0 10 l 6 -6 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path></g>')
    return "".join(o)

def heshbon_fire(w, h, seed):
    """A fire is gone forth out of Heshbon, and a flame from the midst of Sihon, and hath devoured the corner of Moab: the city on
    its hill burning, those that fled standing without strength in its shadow (told in words)."""
    o = [K2.sky(w, h, "#2A0A0A", "#B8502A"), J.city_hill(w * 0.5, h * 0.7, w * 0.36, h * 0.3, seed), ground(w, h, h * 0.7, "#3A2418", dy=0)]
    o += [E.blaze(w * (0.34 + i * 0.16), h * 0.5, w * 0.12, h * 0.26, seed + i, n=5) for i in range(3)]
    o.append(smoke(w * 0.5, h * 0.22, 8, seed, w=0.8))
    return "".join(o)
