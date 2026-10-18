"""New drawings for Numbers chapter 11 (Numbers 22–24): Moab looking down from its walls upon the camp in the plains,
Balak's messengers with the rewards of divination going to Balaam at Pethor by the River, Balaam's house at night, the seven
altars on the heights (the high places of Baal, the top of Pisgah, the top of Peor) with Balak by his burnt-offering, and the
vista of Israel dwelling according to their tribes, over which the parables are set in song boxes.
Faces: Balaam (numbers1 tokens: purple headcloth), Balak king of Moab (gold band, black beard), an elder of Moab."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus4 as E4, exodus5 as V, numbers1 as N, judges1 as J1
from faces_ex import F
from genesis.art2 import fit, ground, hills
from genesis.art3 import sun, label, man, king
from exo import art as A, art8 as B8
from lev.art import altar
from num.art import ALL, wilderness_camp, TRIBE_C, standard
def f(v): return f"{v:.1f}"
_T = N.tokens()
BALAAM, BALAAM_AWE = _T["__FACE_BALAAM__"], _T["__FACE_BALAAM_AWE__"]
BALAK = F("adam", skin="#B9785A", shadow="#5A2A1A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#C8A030", band=True, light="#FF8A3D")
BALAK_ANGRY = F("adam", skin="#B9785A", shadow="#5A2A1A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#C8A030", band=True, brow="scowl", sweat=True, light="#D7261E")
ELDER_MOAB = F("adam", skin="#B98A6E", shadow="#5A3A3A", hair="#B8B2A6", hl="#8A867E", beard=True, beard_color="#B8B2A6", scarf="#8A3A5A", cord=True, light="#FFC14D")
MOAB_C, BALAAM_C = "#C8A030", "#7A3BA8"

def balaam(p, x, y, s, flip=False, up=None):
    """Balaam at a distance: purple robe and headcloth with a dark cord."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#8A5A3E", cloth=BALAAM_C, sw=3, flip=flip, up=up, extra=A.headcloth("#7A3BA8"))

def balak(p, x, y, s, flip=False, up=None):
    return king(p, x, y, s, MOAB_C, flip=flip, up=up)

def moab_walls(p, w, h, seed):
    """Moab sore afraid: watchers on the walls of a Moabite city looking down on the camp spread over the plains of Moab."""
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), sun(w * 0.18, h * 0.16, 16, color="#FF8A3D", op=0.3), ground(w, h, h * 0.36, "#C8A06A", dy=0),
         N.camp(46, w * 0.0, w * 0.62, h * 0.38, h * 0.62, seed)]
    o.append(f'<path d="M{f(w * 0.56)} {f(h)} L {f(w * 0.62)} {f(h * 0.52)} L {f(w + 10)} {f(h * 0.46)} L {f(w + 10)} {f(h)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(f'<rect x="{f(w * 0.62)}" y="{f(h * 0.38)}" width="{f(w * 0.4)}" height="{f(h * 0.16)}" fill="#A8846A" stroke="#0D0D0F" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(w * 0.62 + i * w * 0.03)}" y="{f(h * 0.35)}" width="{f(w * 0.018)}" height="{f(h * 0.03)}" fill="#A8846A" stroke="#0D0D0F" stroke-width="1.4"></rect>' for i in range(14)))
    s = fit(h * 0.38, h * 0.18)
    o.append(balak(p, w * 0.7, h * 0.38, s, flip=True))
    for i in range(4): o.append(man(p, w * (0.78 + i * 0.05), h * 0.38, s * 0.95, r.choice(["#8A3A5A", "#6A5A3A", "#4A3A6A"]), flip=True))
    return "".join(o)

def messengers(p, w, h, seed, arrived=False):
    """The elders of Moab and of Midian going with the rewards of divination (arrived=True: before Balaam's house at
    Pethor by the River, palms and the water behind)."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), sun(w * 0.86, h * 0.16, 14, op=0.25)]
    if arrived:
        o.append(ground(w, h, h * 0.5, "#9CBB5E", dy=0) + f'<rect x="-10" y="{f(h * 0.5)}" width="{f(w + 20)}" height="{f(h * 0.08)}" fill="#2C9DB8" stroke="#0D0D0F" stroke-width="2"></rect>'
                 + label(w * 0.5, h * 0.56, "THE RIVER", "#E8F6FA", 9) + ground(w, h, h * 0.58, "#C8A06A", dy=0))
        o.append(J1.palm(w * 0.08, h * 0.6, min(1.2, h / 300)) + J1.palm(w * 0.94, h * 0.6, min(1.0, h / 340)))
        o.append(A.black_tent(w * 0.8, b - 6, w * 0.22, h * 0.3, color="#4A2A5A"))
        o.append(balaam(p, w * 0.66, b, fit(b, h * 0.42), flip=True))
        xs = (0.12, 0.2, 0.28, 0.36, 0.44)
    else:
        o.append(hills(w, h, h * 0.46, seed, color="#B5652E", amp=14) + ground(w, h, h * 0.56, "#D8B878", dy=0))
        xs = (0.2, 0.3, 0.4, 0.5, 0.6)
    for i, x in enumerate(xs):
        o.append(A.elder(r.choice(["#8A3A5A", "#6A5A3A", "#4A6A5A", "#7A4A2A"]), i)(p, w * x, b - (i % 2) * 4, fit(b, h * 0.48)))
        o.append(f'<rect x="{f(w * x + 14)}" y="{f(b - fit(b, h * 0.48) * 110)}" width="{f(14 * fit(b, h * 0.48) * 3)}" height="{f(10 * fit(b, h * 0.48) * 3)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2"></rect>' if i % 2 == 0 else "")
    return "".join(o)

def altars7(p, w, h, seed, place="baal", smoke=True):
    """Seven altars upon a height, a bullock and a ram upon every altar; Balak standing by his burnt-offering with the princes
    of Moab; far below, the utmost part of the camp of Israel. place: 'baal' / 'pisgah' / 'peor' (the light changes)."""
    r = random.Random(seed)
    sky = {"baal": "#E8B880", "pisgah": "#8FD0E2", "peor": "#E8886A"}[place]
    o = [mk.defs(p, *ALL), f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="{sky}"></rect>', sun(w * 0.86, h * 0.14, 16, color="#FFE680" if place != "peor" else "#FF6A2A", op=0.3)]
    o.append(ground(w, h, h * 0.5, "#C8A06A", dy=0) + N.camp(30, w * 0.0, w * 0.9, h * 0.52, h * 0.62, seed))
    o.append(f'<path d="M-10 {f(h)} L -10 {f(h * 0.7)} C {f(w * 0.3)} {f(h * 0.62)} {f(w * 0.7)} {f(h * 0.62)} {f(w + 10)} {f(h * 0.7)} L {f(w + 10)} {f(h)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    s = min(1.2, h / 280)
    for i in range(7):
        x = w * (0.08 + i * 0.13); y = h * 0.86
        o.append(altar(x, y, s * 1.1, fire=True, smoke=smoke))
    s2 = fit(h * 0.98, h * 0.6)
    o.append(balak(p, w * 0.12, h * 0.98, s2))
    for i in range(3): o.append(man(p, w * (0.2 + i * 0.05), h * 0.98, s2 * 0.95, r.choice(["#8A3A5A", "#6A5A3A", "#4A3A6A"])))
    return "".join(o)

def bare_height(p, w, h, seed):
    """Balaam gone alone to a bare height to meet Jehovah, the altars smoking far behind him."""
    o = [mk.defs(p, *ALL), f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#2A2458"></rect>', V.rays(w * 0.6, h * 0.1, 36, 20, max(w, h), color="#FFF4C2", op=0.3)]
    o.append(f'<path d="M-10 {f(h)} L {f(w * 0.5)} {f(h * 0.5)} L {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h)} Z" fill="#3A2A2A" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(balaam(p, w * 0.5, h * 0.52, fit(h * 0.52, h * 0.22), up=[(-22, -158), (-10, -196), (6, -226)]))
    return "".join(o)

def vista(w, h, seed, tribes=True):
    """Israel dwelling according to their tribes, seen from the heights: tents in their camps with the standards, the
    tabernacle in the midst, gardens and cedars by the river-side."""
    r = random.Random(seed)
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#E8C88A"></rect>', sun(w * 0.86, h * 0.14, 16, op=0.25), ground(w, h, h * 0.36, "#C8A06A", dy=0)]
    o.append(f'<path d="M-10 {f(h * 0.42)} C {f(w * 0.3)} {f(h * 0.4)} {f(w * 0.6)} {f(h * 0.46)} {f(w + 10)} {f(h * 0.42)}" fill="none" stroke="#2C9DB8" stroke-width="6"></path>')
    for i in range(10):
        x = w * (0.04 + i * 0.1)
        o.append(f'<path d="M{f(x)} {f(h * 0.42)} L {f(x)} {f(h * 0.36)}" stroke="#3A2214" stroke-width="2"></path><circle cx="{f(x)}" cy="{f(h * 0.34)}" r="{f(h * 0.03)}" fill="#2E6B3A" stroke="#0D0D0F" stroke-width="1.4"></circle>')
    for k, (x0, x1, y0, y1) in enumerate(((0.0, 0.3, 0.46, 0.66), (0.35, 0.65, 0.46, 0.6), (0.7, 1.0, 0.46, 0.66), (0.1, 0.9, 0.68, 0.96))):
        o.append(N.camp(16 if k < 3 else 30, w * x0, w * x1, h * y0, h * y1, seed + k))
    o.append(V.tabernacle(w * 0.5, h * 0.64, w * 0.2, uid=f"vs{seed}"))
    if tribes:
        for i, t in enumerate(("JUDAH", "REUBEN", "EPHRAIM", "DAN")):
            o.append(standard(w * (0.12 + i * 0.25), h * 0.7, min(1.2, h / 360), TRIBE_C[t], pole=60))
    return "".join(o)

def narrow(p, w, h, seed):
    """A narrow path between the vineyards, a wall on this side and a wall on that side; the angel of Jehovah standing in
    it with his sword drawn; Balaam upon his ass pressed against the wall."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#8FD0E2"></rect>', ground(w, h, h * 0.5, "#C8A06A", dy=0)]
    for side in (-1, 1):
        x0 = w * 0.5 + side * w * 0.5
        o.append(f'<path d="M{f(x0)} {f(h * 0.3)} L {f(w * 0.5 + side * w * 0.08)} {f(h * 0.48)} L {f(w * 0.5 + side * w * 0.08)} {f(h * 0.56)} L {f(x0)} {f(h)} Z" fill="#B8A88A" stroke="#0D0D0F" stroke-width="2.4"></path>')
        o.append(f'<path d="M{f(x0)} {f(h * 0.3)} L {f(w * 0.5 + side * w * 0.08)} {f(h * 0.48)}" stroke="#4A7A3A" stroke-width="{f(h * 0.05)}"></path>')
    o.append(N.angel(p, w * 0.5, h * 0.56, fit(h * 0.56, h * 0.24)))
    o.append(N.mount(w * 0.36, b, fit(b, h * 0.5) * 0.9, p=p))
    return "".join(o)
