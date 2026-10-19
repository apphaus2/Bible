"""Drawings for Jeremiah chapter 9 (Jeremiah 26–28), on top of jer.art: the prophet seized in the court, the princes in the new
gate, Zion ploughed as a field, the bonds and bars upon his neck, the envoys of the five kings, the vessels left in the house,
Hananiah breaking the bar."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jer.art import *
from jer.art import f, K2

def yoke_bar(x, y, s, broken=False, iron=False):
    """A yoke-bar across a standing figure's shoulders (x, y = the figure's feet, s its scale), with its two thongs."""
    c = "#4A4E58" if iron else "#8A5A2A"
    if broken: return ""
    return (f'<rect x="{f(x - 52 * s)}" y="{f(y - 166 * s)}" width="{f(104 * s)}" height="{f(10 * s)}" rx="{f(3 * s)}" fill="{c}" stroke="#0D0D0F" stroke-width="2"></rect>'
            f'<path d="M{f(x - 18 * s)} {f(y - 158 * s)} q {f(-4 * s)} {f(14 * s)} {f(6 * s)} {f(20 * s)} M{f(x + 18 * s)} {f(y - 158 * s)} q {f(4 * s)} {f(14 * s)} {f(-6 * s)} {f(20 * s)}" stroke="#3A2214" stroke-width="{f(2.4 * s)}" fill="none"></path>')

def seized(p, w, h, seed, age=2):
    """The priests and the prophets and all the people laid hold on him in the house of Jehovah: the prophet in the court, men
    pressing round him with raised arms."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#C8A880", "#F3E0B0"), temple_front(w * 0.5, h * 0.6, w * 0.6, seed), ground(w, h, h * 0.6, "#D8C8A0", dy=0)]
    s = fit(b, max(h * 0.4, b - 230))
    o.append(jer_fig(p, w * 0.5, b, s, age=age))
    o.append(priest(p, w * 0.34, b, s * 0.98, up=[(22, -158), (50, -170), (70, -160)]))
    o.append(man(p, w * 0.66, b, s * 0.98, "#5A3A5A", flip=True, up=[(22, -158), (50, -170), (70, -160)], extra=A.headcloth("#5A3A5A") + A.BLACK_BEARD))
    o.append(crowd_at(p, w, h, seed, w * 0.04, w * 0.26, h * 0.66, b, 6, s * 0.6, s * 0.92))
    o.append(crowd_at(p, w, h, seed + 1, w * 0.76, w * 0.98, h * 0.66, b, 6, s * 0.6, s * 0.92, flip=True))
    return "".join(o)

def new_gate(p, w, h, seed):
    """The princes of Judah came up from the king's house and sat in the entry of the new gate of Jehovah's house."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8", "#F3E0B0"), wall(-10, w + 10, h * 0.2, h * 0.7, seed, towers=3, gate=w * 0.5, color="#D8C8A0"),
         ground(w, h, h * 0.7, "#C8B080", dy=0)]
    s = fit(b, max(h * 0.4, b - 220))
    for i in range(4):
        o.append(E.kneel(w * (0.24 + i * 0.16), b, s * 0.78, color=["#6A2A3A", "#2A5A5A", "#5A3A6A", "#6A5A2A"][i], skin="#9A6A4A", flip=i >= 2))
    return "".join(o)

def zion_plowed(w, h, seed):
    """Zion shall be plowed as a field, and Jerusalem shall become heaps, and the mountain of the house as the high places of a
    forest: furrows over the hill, heaps of stones, scrub on the summit."""
    o = [K2.sky(w, h, "#8FB0C8", "#F3E0B0"),
         f'<path d="M-10 {f(h + 10)} C {f(w * 0.2)} {f(h * 0.36)} {f(w * 0.7)} {f(h * 0.3)} {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} Z" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    for k in range(9):
        y = h * (0.56 + k * 0.05)
        o.append(f'<path d="M{f(-10 + k * 6)} {f(y + 20)} C {f(w * 0.3)} {f(y - 30)} {f(w * 0.7)} {f(y - 30)} {f(w + 10)} {f(y + 10)}" stroke="#5A3A1E" stroke-width="2.4" fill="none"></path>')
    o.append(thicket(w * 0.36, w * 0.66, h * 0.4, h * 0.3, seed, color="#4A6A3A"))
    o.append(S4b.stone_heap(w * 0.18, h * 0.92, w * 0.16, h * 0.12, seed) + S4b.stone_heap(w * 0.8, h * 0.94, w * 0.14, h * 0.1, seed + 1))
    return "".join(o)

def common_graves(w, h, seed):
    """The graves of the common people: rows of low unmarked mounds in the valley (Uriah's death told in words only)."""
    o = [K2.sky(w, h, "#5A4A5A", "#C8A080"), hills(w, h, h * 0.5, seed, "#6A5A4A", amp=10, step=80), ground(w, h, h * 0.58, "#8A7A5A", dy=0)]
    for r_ in range(3):
        for c in range(7):
            x = w * (0.08 + c * 0.14 + (r_ % 2) * 0.05); y = h * (0.66 + r_ * 0.12)
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * 0.05)}" ry="{f(h * 0.025)}" fill="#6A5A40" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    return "".join(o)

def bonds_bars(p, w, h, seed, age=2):
    """Make thee bonds and bars, and put them upon thy neck: the prophet walking in the street with a wooden yoke-bar on his
    shoulders."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), empty_city(w, h, seed)]
    s = fit(b, max(h * 0.4, b - 240))
    o.append(jer_fig(p, w * 0.5, b, s, age=age) + yoke_bar(w * 0.5, b, s))
    return "".join(o)

ENVOYS = ("EDOM", "MOAB", "AMMON", "TYRE", "SIDON")
def envoys_map(w, h):
    return near_east(w, h, ("JERUSALEM", "BABYLON") + ENVOYS, hi=ENVOYS, arrows=[(n, "JERUSALEM") for n in ENVOYS], lit="#FF8A6A", box=(31.5, 46.5, 28.0, 35.4))

def yoke_iron(w, h, seed):
    """I have put a yoke of iron upon the neck of all these nations: a yoke of iron on a dark ground, the broken wooden bar
    beside it."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#1A1820"></rect>', V.rays(w * 0.5, h * 0.5, 24, 10, max(w, h), color="#8A8A9A", op=0.08)]
    cx, cy, s = w * 0.5, h * 0.5, min(2.4, h / 120)
    o.append(f'<rect x="{f(cx - 80 * s)}" y="{f(cy - 8 * s)}" width="{f(160 * s)}" height="{f(16 * s)}" rx="{f(4 * s)}" fill="#4A4E58" stroke="#0D0D0F" stroke-width="2.6"></rect>'
             + "".join(f'<path d="M{f(cx + dx * s)} {f(cy + 8 * s)} q {f(-14 * s)} {f(34 * s)} 0 {f(46 * s)} q {f(14 * s)} {f(-12 * s)} 0 {f(-46 * s)}" stroke="#6A6E78" stroke-width="{f(5 * s)}" fill="none"></path>' for dx in (-44, 44)))
    o.append(f'<path d="M{f(cx - 70 * s)} {f(h * 0.88)} l {f(60 * s)} -6 M{f(cx + 10 * s)} {f(h * 0.9)} l {f(56 * s)} 4" stroke="#8A5A2A" stroke-width="{f(9 * s)}" stroke-linecap="round"></path>')
    return "".join(o)

def bar_broken(p, w, h, seed, age=2):
    """Hananiah took the bar from off the prophet Jeremiah's neck, and brake it: Hananiah with the two halves raised, the prophet
    standing, priests and people looking on in the house of Jehovah."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#C8A880", "#F3E0B0"), temple_front(w * 0.5, h * 0.6, w * 0.6, seed), ground(w, h, h * 0.6, "#D8C8A0", dy=0)]
    s = fit(b, max(h * 0.4, b - 230))
    o.append(jer_fig(p, w * 0.34, b, s, age=age))
    hx = w * 0.6
    o.append(man(p, hx, b, s, "#5A3A5A", flip=True, up=[(22, -158), (44, -196), (40, -236)], extra=A.headcloth("#5A3A5A") + A.BLACK_BEARD))
    o.append(f'<path d="M{f(hx - 40 * s)} {f(b - 236 * s)} l {f(-46 * s)} {f(-14 * s)}" stroke="#8A5A2A" stroke-width="{f(9 * s)}" stroke-linecap="round"></path>'
             f'<path d="M{f(hx + 22 * s)} {f(b - 160 * s)} l {f(40 * s)} {f(-24 * s)}" stroke="#8A5A2A" stroke-width="{f(9 * s)}" stroke-linecap="round"></path>')
    o.append(priest(p, w * 0.86, b, s * 0.92, flip=True) + crowd_at(p, w, h, seed, w * 0.02, w * 0.2, h * 0.66, b, 5, s * 0.6, s * 0.9))
    return "".join(o)

def vessels_left(w, h):
    """The pillars, the sea, the bases and the residue of the vessels left in the city: Solomon's brass as a blueprint plate."""
    return molten_sea(w, h)
