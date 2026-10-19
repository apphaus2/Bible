"""Drawings for Ezekiel 17–19: the riddle of the two great eagles, the top of the cedar cropped and carried to a land of
traffic, the vine of low stature turning toward the second eagle, the vine withered by the east wind; the way to Babylon and
the ambassadors to Egypt (a map); the tender twig planted on the mountain of the height of Israel; the sour grapes; the
three generations (a plate); the lioness and her whelps taken in the pit and brought in a cage with hooks; the vine plucked
up and planted in the wilderness."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ezk.art5 import *
from ezk.art5 import f, K2, K3, P, rect, seated, clouds, smoke, house, INK, EZ_C, GB_BEARD, CAPT, bg, glow, vgrad, rgrad, KK2, JJ2

def eagle(x, y, s=1.0, colors=("#7A3A2A", "#C8863E", "#E8B830", "#3A5A8A"), flip=False, twig=False):
    """A great eagle with great wings and long pinions, full of feathers of divers colours, wings spread; twig=True: the
    cropped top of the cedar in its talons."""
    sx = -1 if flip else 1
    o = []
    for side in (-1, 1):
        for k, c in enumerate(colors):
            L = 150 - k * 22
            o.append(wing(x + side * 8 * s, y - 10 * s, x + side * L * s, y - (60 - k * 26) * s, bulge=0.22 * side * -1, n=6, fill=c, sw=2))
    o.append(P(f"M{f(x - 16 * s)} {f(y - 20 * s)} C {f(x - 20 * s)} {f(y + 30 * s)} {f(x + 20 * s)} {f(y + 30 * s)} {f(x + 16 * s)} {f(y - 20 * s)} Z", "#5A3A2A", 2.2))
    o.append(P(f"M{f(x - 14 * s)} {f(y + 22 * s)} L {f(x)} {f(y + 56 * s)} L {f(x + 14 * s)} {f(y + 22 * s)} Z", "#E8D8B0", 2))
    o.append(f'<circle cx="{f(x)}" cy="{f(y - 30 * s)}" r="{f(14 * s)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></circle>'
             + P(f"M{f(x + sx * 10 * s)} {f(y - 34 * s)} L {f(x + sx * 28 * s)} {f(y - 26 * s)} L {f(x + sx * 12 * s)} {f(y - 22 * s)} Z", "#E8B830", 1.6)
             + f'<circle cx="{f(x + sx * 5 * s)}" cy="{f(y - 33 * s)}" r="{f(2.4 * s)}" fill="{INK}"></circle>')
    if twig:
        o.append(f'<path d="M{f(x - 30 * s)} {f(y + 40 * s)} L {f(x + 30 * s)} {f(y + 36 * s)}" stroke="#5A3A1A" stroke-width="{f(4 * s)}"></path>'
                 + "".join(f'<path d="M{f(x - 26 * s + i * 10 * s)} {f(y + 38 * s)} l {f(-6 * s)} {f(-10 * s)} M{f(x - 26 * s + i * 10 * s)} {f(y + 38 * s)} l {f(6 * s)} {f(-10 * s)}" stroke="#2E5A2A" stroke-width="{f(3 * s)}"></path>' for i in range(6)))
    return "".join(o)

def cedar_tree(x, base, s=1.0, color="#2E5A3A", top=True):
    """A cedar of Lebanon: a thick trunk and level tiers of foliage (top=False: the topmost twig cropped)."""
    o = [f'<path d="M{f(x - 10 * s)} {f(base)} L {f(x - 6 * s)} {f(base - 200 * s)} L {f(x + 6 * s)} {f(base - 200 * s)} L {f(x + 10 * s)} {f(base)} Z" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></path>']
    for i in range(5):
        y = base - (60 + i * 36) * s; wd = (110 - i * 18) * s
        o.append(P(f"M{f(x - wd)} {f(y)} C {f(x - wd * 0.6)} {f(y - 22 * s)} {f(x + wd * 0.6)} {f(y - 22 * s)} {f(x + wd)} {f(y)} C {f(x + wd * 0.5)} {f(y + 10 * s)} {f(x - wd * 0.5)} {f(y + 10 * s)} {f(x - wd)} {f(y)} Z", color, 2))
    if top: o.append(P(f"M{f(x - 16 * s)} {f(base - 236 * s)} L {f(x)} {f(base - 266 * s)} L {f(x + 16 * s)} {f(base - 236 * s)} Z", color, 2))
    return "".join(o)

def eagle_cedar(w, h, seed):
    """A great eagle came unto Lebanon and took the top of the cedar: the eagle rising from the cedar with the cropped twig."""
    o = [bg(f"ec{seed}", w, h, [(0, "#4A7AB0"), (1, "#E8E0C8")]), hills(w, h, h * 0.78, seed, "#6A8A6A", amp=12, step=70)]
    k = min(1.0, h / 330)
    o.append(cedar_tree(w * 0.3, h * 0.98, k * 1.1, top=False))
    o.append(eagle(w * 0.64, h * 0.42, k * 0.9, twig=True))
    return "".join(o)

def low_vine(w, h, seed, eagle2=False, wither=False, bird=True):
    """The seed planted in a fruitful soil by great waters: a spreading vine of low stature whose branches turn toward the
    eagle (eagle2=True: the second eagle, the vine bending its roots toward him); wither=True: withered in the furrows
    where it grew, the east wind blowing."""
    r = random.Random(seed)
    o = [bg(f"lv{seed}{eagle2}{wither}", w, h, [(0, "#C88A5A" if wither else "#6AA0C8"), (1, "#F3D8A0")]), ground(w, h, h * 0.8, "#8A6A4A" if wither else "#6A7A4A", dy=0)]
    if not wither: o.append(f'<path d="M-10 {f(h * 0.9)} C {f(w * 0.3)} {f(h * 0.86)} {f(w * 0.6)} {f(h * 0.94)} {f(w + 10)} {f(h * 0.9)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#3A7A9A" stroke="{INK}" stroke-width="2"></path>')
    k = min(1.0, h / 300)
    cx = w * 0.32
    lean = 1 if eagle2 else 0.4
    for i in range(7):
        a = -math.pi / 2 + (i - 3) * 0.32 + lean * 0.4
        L = (120 + r.uniform(-20, 20)) * k
        o.append(vine_branch(cx, h * 0.82, cx + math.cos(a) * L * 1.6, h * 0.82 + math.sin(a) * L * 0.7, seed + i, sw=6))
        if not wither:
            for j in range(3):
                lx = cx + math.cos(a) * L * 1.6 * (0.4 + j * 0.25); ly = h * 0.82 + math.sin(a) * L * 0.7 * (0.4 + j * 0.25)
                o.append(f'<path d="M{f(lx)} {f(ly)} c -8 -10 8 -16 10 -4 c 4 -10 14 -2 6 6 Z" fill="#4E8A3A" stroke="{INK}" stroke-width="1.2"></path>')
        else:
            o.append(f'<circle cx="{f(cx + math.cos(a) * L * 1.5)}" cy="{f(h * 0.82 + math.sin(a) * L * 0.65)}" r="{f(4 * k)}" fill="#8A6A3A"></circle>')
    if eagle2: o.append(eagle(w * 0.78, h * 0.36, k * 0.7, colors=("#3A3A5A", "#6A6A8A", "#9A9AB8", "#5A3A6A"), flip=True))
    elif not wither and bird: o.append(eagle(w * 0.8, h * 0.3, k * 0.5))
    if wither: o.append(wind_lines(w, h, seed, n=8, color="#F3E0B0", op=0.6, y0=0.2, y1=0.7))
    return "".join(o)

def treaty_map(w, h):
    """The king of Babylon came to Jerusalem and took the king and the princes to Babylon; then the ambassadors sent into
    Egypt for horses and much people — as a map."""
    o = [grid_bg(w, h)]
    J0, B, Eg = (w * 0.3, h * 0.5), (w * 0.86, h * 0.58), (w * 0.1, h * 0.86)
    o.append(route([B, (w * 0.62, h * 0.3), J0], color="#FFD23F", sw=2.4) + route([J0, (w * 0.56, h * 0.28), B], color="#FF8A6A", sw=2, dash="4 6"))
    o.append(route([J0, Eg], color="#8FD0E2", sw=2.4))
    o.append(node(*J0, "JERUSALEM", "#D7261E", r=7, dy=-14, size=10) + node(*B, "BABYLON", "#FFD23F", r=6, dy=-14, size=10) + node(*Eg, "EGYPT", "#8FD0E2", r=6, dy=-14, size=10))
    o.append(label(w * 0.2, h * 0.7, "AMBASSADORS · HORSES", "#8FD0E2", 8, "start"))
    return "".join(o)

def cedar_mountain(w, h, seed):
    """I will crop off from the topmost of his young twigs a tender one, and plant it upon a high and lofty mountain: a goodly
    cedar on the mountain of the height of Israel, birds of every wing under it."""
    r = random.Random(seed)
    o = [bg(f"cm{seed}", w, h, [(0, "#5A9AD0"), (1, "#F3E8C8")])]
    o.append(P(f"M-10 {f(h + 10)} L {f(w * 0.3)} {f(h * 0.62)} L {f(w * 0.5)} {f(h * 0.5)} L {f(w * 0.7)} {f(h * 0.62)} L {f(w + 10)} {f(h + 10)} Z", "#6A8A5A", 2.4))
    k = min(0.9, h / 360)
    o.append(cedar_tree(w * 0.5, h * 0.54, k))
    for _ in range(7):
        x = w * 0.5 + r.uniform(-110, 110) * k; y = h * 0.54 - r.uniform(40, 200) * k
        o.append(f'<path d="M{f(x - 8)} {f(y)} q 8 -8 16 0 q -8 -4 -16 0" fill="#3A2A2A" stroke="#0D0D0F" stroke-width="1.2"></path>')
    return "".join(o)

def sour_grapes(w, h, seed):
    """The fathers have eaten sour grapes: a cluster of unripe green grapes on the vine."""
    r = random.Random(seed)
    o = [bg(f"sg{seed}", w, h, [(0, "#3A4A3A"), (1, "#A8B88A")])]
    o.append(vine_branch(-10, h * 0.3, w + 10, h * 0.36, seed, sw=12))
    k = min(1.6, h / 220)
    for cx in (w * 0.3, w * 0.62):
        for row in range(6):
            for c in range(6 - row):
                x = cx + (c - (5 - row) / 2) * 16 * k; y = h * 0.42 + row * 14 * k
                o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(8 * k)}" fill="#8AB84A" stroke="{INK}" stroke-width="1.4"></circle><circle cx="{f(x - 2 * k)}" cy="{f(y - 3 * k)}" r="{f(2 * k)}" fill="#D8F0A0"></circle>')
        o.append(f'<path d="M{f(cx)} {f(h * 0.33)} L {f(cx)} {f(h * 0.42)}" stroke="#5A3A1A" stroke-width="3"></path>')
    return "".join(o)

def generations(p, w, h):
    """The soul that sinneth, it shall die: a plate of three generations — the just father, the son a robber, the son's son
    who seeth his father's sins and doeth not such like — each bearing his own way."""
    o = [mk.defs(p, *ALL), bp(w, h), title_bar(w, "ALL SOULS ARE MINE · EVERY ONE ACCORDING TO HIS WAYS")]
    s = min(fit(h * 0.86, h * 0.36), 0.9)
    for i, (nm, cl, ok) in enumerate((("THE FATHER", "#3A5A8A", True), ("HIS SON", "#7A2A2A", False), ("THE SON'S SON", "#3A6A4A", True))):
        x = w * (0.2 + i * 0.3)
        o.append(f'<circle cx="{f(x)}" cy="{f(h * 0.86 - 100 * s)}" r="{f(120 * s)}" fill="none" stroke="{"#FFD23F" if ok else "#D7261E"}" stroke-width="2.4" stroke-dasharray="{"0" if ok else "6 5"}"></circle>')
        o.append(mk.person(p, round(x), round(h * 0.86), round(s, 3), body=SKIN, cloth=cl, sw=2.6, extra=A.headcloth(cl) + (A.WHITE_BEARD if i == 0 else A.BLACK_BEARD)))
        o.append(label(x, h * 0.95, nm, "#8FD0E2", 9))
        if i < 2: o.append(route([(x + 70 * s, h * 0.5), (x + w * 0.3 - 70 * s, h * 0.5)], color="#4A7A9A", sw=1.6))
    return "".join(o)

def lions(w, h, seed, stage=0):
    """The lioness among lions and her whelp become a young lion (stage 0); taken in their pit, the net spread (1); put in a
    cage with hooks and brought to Babylon (2)."""
    o = [bg(f"ln{seed}{stage}", w, h, [(0, "#C8803A" if stage == 0 else "#4A3A3A"), (1, "#F3D8A0" if stage == 0 else "#A8906A")]), hills(w, h, h * 0.66, seed, "#A8805A", amp=10, step=80),
         ground(w, h, h * 0.8, "#B8945A", dy=0)]
    k = min(1.0, h / 260)
    if stage == 0:
        o.append(JJ2.lion(w * 0.2, h * 0.96, k * 1.1, roar=False) + JJ2.lion(w * 0.52, h * 0.94, k * 0.9, roar=True) + JJ2.lion(w * 0.76, h * 0.98, k * 0.7, flip=True, roar=False))
    elif stage == 1:
        o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.9)}" rx="{f(w * 0.26)}" ry="{f(h * 0.1)}" fill="#2A1A10" stroke="{INK}" stroke-width="2.4"></ellipse>')
        o.append(JJ2.lion(w * 0.4, h * 0.94, k * 0.8, roar=True))
        for i in range(-6, 7):
            o.append(f'<path d="M{f(w * 0.5 + i * w * 0.04)} {f(h * 0.8)} L {f(w * 0.5 + i * w * 0.04 + 30)} {f(h * 0.98)}" stroke="#C8C8B0" stroke-width="1.6"></path>'
                     f'<path d="M{f(w * 0.5 + i * w * 0.04)} {f(h * 0.8)} L {f(w * 0.5 + i * w * 0.04 - 30)} {f(h * 0.98)}" stroke="#C8C8B0" stroke-width="1.6"></path>')
    else:
        x0, x1, y0, y1 = w * 0.3, w * 0.7, h * 0.56, h * 0.96
        o.append(JJ2.lion(w * 0.42, h * 0.94, k * 0.7, roar=True))
        o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(x1 - x0)}" height="{f(y1 - y0)}" fill="none" stroke="#3A3A3A" stroke-width="4"></rect>'
                 + "".join(f'<path d="M{f(x0 + i * (x1 - x0) / 8)} {f(y0)} L {f(x0 + i * (x1 - x0) / 8)} {f(y1)}" stroke="#3A3A3A" stroke-width="4"></path>' for i in range(9))
                 + "".join(f'<path d="M{f(x0 + i * (x1 - x0) / 4)} {f(y0)} q 6 -12 -2 -16" stroke="#7A7A7A" stroke-width="3" fill="none"></path>' for i in range(5)))
        o.append(label(w * 0.86, h * 0.6, "TO BABYLON", "#F3EFE6", 10))
    return "".join(o)
