"""Drawings for Jeremiah chapter 5 (Jeremiah 13–15), on top of jer.art: the linen girdle by the Euphrates, the wine bottles,
the drought."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jer.art import *
from jer.art import f, K2

def girdle_band(x, y, s, marred=False):
    """A linen girdle about a figure's loins (local units of a standing figure at x, y)."""
    c = "#6A5A3A" if marred else "#F3EFE6"
    return f'<rect x="{f(x - 24 * s)}" y="{f(y - 104 * s)}" width="{f(48 * s)}" height="{f(10 * s)}" fill="{c}" stroke="#0D0D0F" stroke-width="1.6"></rect>'

def girdle_worn(p, w, h, seed):
    """So I bought a girdle and put it upon my loins: the prophet in the street, a new white linen girdle about his robe."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), empty_city(w, h, seed)]
    s = fit(b, max(h * 0.4, b - 240))
    o.append(jer_fig(p, w * 0.5, b, s, age=1) + girdle_band(w * 0.5, b, s))
    return "".join(o)

def euphrates(p, w, h, seed, stage=0):
    """The Euphrates among rocks; stage 0: the prophet hiding the girdle in a cleft of the rock; stage 1: after many days,
    digging, the girdle marred, profitable for nothing."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#E8A060" if stage == 0 else "#8A8A9A", "#F3D8A0" if stage == 0 else "#D8D0C0"),
         f'<rect x="-10" y="{f(h * 0.5)}" width="{f(w + 20)}" height="{f(h * 0.16)}" fill="#2C7A9A"></rect>'
         f'<path d="M-10 {f(h * 0.56)} ' + " ".join(f"q {f(w / 20)} -6 {f(w / 10)} 0" for _ in range(11)) + '" fill="none" stroke="#E8F6FA" stroke-width="1.6"></path>',
         ground(w, h, h * 0.66, "#B89A6A", dy=0), crag(w * 0.62, w * 0.98, h * 0.94, h * 0.34)]
    o.append(f'<path d="M{f(w * 0.8)} {f(h * 0.5)} L {f(w * 0.77)} {f(h * 0.66)} L {f(w * 0.81)} {f(h * 0.76)} L {f(w * 0.79)} {f(h * 0.9)} L {f(w * 0.83)} {f(h * 0.76)} L {f(w * 0.8)} {f(h * 0.64)} Z" fill="#1A1210" stroke="#0D0D0F" stroke-width="1.6"></path>')
    s = fit(b, max(h * 0.4, b - 230))
    if stage == 0:
        o.append(jer_fig(p, w * 0.5, b, s, age=1, up=[(22, -158), (40, -130), (62, -126)], flip=True))
        o.append(f'<rect x="{f(w * 0.5 - 70 * s)}" y="{f(b - 130 * s)}" width="{f(30 * s)}" height="{f(8 * s)}" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    else:
        o.append(E.kneel(w * 0.4, b, s * 0.9, color=JER_C, skin="#9A6A4A"))
        o.append(f'<path d="M{f(w * 0.5)} {f(b - 4)} q 20 -10 40 -2 q 20 8 40 -4" stroke="#5A4A2A" stroke-width="{f(9 * s)}" fill="none" stroke-linecap="round"></path>'
                 f'<path d="M{f(w * 0.5)} {f(b - 4)} q 20 -10 40 -2 q 20 8 40 -4" stroke="#3A2A1A" stroke-width="2" fill="none" stroke-dasharray="3 6"></path>')
    return "".join(o)

def bottles(w, h, seed):
    """Every bottle shall be filled with wine: a row of tall wine jars in a cellar, one tipped and spilling."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1A1A"></rect>', ground(w, h, h * 0.86, "#3A2A22", dy=0)]
    s = min(1.3, h / 200)
    o.append(f'<rect x="-10" y="{f(h * 0.44)}" width="{f(w + 20)}" height="{f(h * 0.04)}" fill="#5A3A22" stroke="#0D0D0F" stroke-width="2"></rect>')
    for i in range(6):
        o.append(jar(w * (0.1 + i * 0.16), h * 0.88, s, color=["#B8703A", "#A8603A", "#C8804A"][i % 3]))
    return "".join(o)

def dark_mountains(w, h, seed):
    """Before your feet stumble upon the dark mountains, and while ye look for light he turn it into gross darkness."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0E0E18"></rect>', glow(w * 0.8, h * 0.3, min(w, h) * 0.2, color="#6A6A8A", op=0.4, uid=f"dm{seed}"),
         hills(w, h, h * 0.42, seed, "#1E1E2A", amp=30, step=50), hills(w, h, h * 0.62, seed + 1, "#16161E", amp=20, step=60),
         f'<path d="M{f(w * 0.1)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.86)} {f(w * 0.4)} {f(h * 0.8)} {f(w * 0.6)} {f(h * 0.7)}" stroke="#3A3A4A" stroke-width="4" fill="none" stroke-dasharray="10 10"></path>']
    return "".join(o)

def crowns_down(w, h, seed):
    """Say unto the king and to the queen-mother, Humble yourselves, sit down; for your headtires are come down: two empty
    seats, two crowns fallen on the floor before them."""
    o = [S3.cedar(w, h, h * 0.84), S3.throne(w * 0.36, h * 0.86, min(1.0, h / 300)), S3.throne(w * 0.64, h * 0.86, min(0.9, h / 330)),
         S2.crown(w * 0.4, h * 0.94, min(1.0, h / 260), rot=-30), S2.crown(w * 0.6, h * 0.95, min(0.8, h / 300), rot=40)]
    return "".join(o)

def shut_gate(w, h, seed):
    """The cities of the South are shut up, and there is none to open them: a city gate shut, the road empty."""
    o = [K2.sky(w, h, "#C8A070", "#F3E0B0"), hills(w, h, h * 0.4, seed, "#B8946A", amp=10, step=80), wall(-10, w + 10, h * 0.34, h * 0.8, seed, towers=4, color="#C8A878"),
         f'<path d="M{f(w * 0.44)} {f(h * 0.8)} L {f(w * 0.44)} {f(h * 0.56)} Q {f(w * 0.5)} {f(h * 0.46)} {f(w * 0.56)} {f(h * 0.56)} L {f(w * 0.56)} {f(h * 0.8)} Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2.4"></path>'
         f'<path d="M{f(w * 0.5)} {f(h * 0.5)} L {f(w * 0.5)} {f(h * 0.8)} M{f(w * 0.44)} {f(h * 0.68)} L {f(w * 0.56)} {f(h * 0.68)}" stroke="#0D0D0F" stroke-width="3"></path>',
         ground(w, h, h * 0.8, "#C8A870", dy=0)]
    return "".join(o)

def stubble_wind(w, h, seed):
    """I will scatter them, as the stubble that passeth away, by the wind of the wilderness."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#C8906A", "#F3D8A0"), hills(w, h, h * 0.6, seed, "#B8846A", amp=12, step=80), ground(w, h, h * 0.72, "#D8B07A", dy=0)]
    for _ in range(50):
        x, y = r.uniform(0, w), r.uniform(h * 0.2, h * 0.9); L = r.uniform(8, 18)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(L)} {f(-L * 0.3)}" stroke="#C8A050" stroke-width="2"></path>')
    o.append(speed_lines(w, h, seed, 0.2, 0.9, color="#F3E8C8", n=14))
    return "".join(o)

def gate_mourning(p, w, h, seed):
    """Judah mourneth, and the gates thereof languish; they sit in black upon the ground."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#C89A6A", "#F3D8A0"), wall(-10, w + 10, h * 0.34, h * 0.76, seed, towers=4, gate=w * 0.5, color="#C8A878"), ground(w, h, h * 0.76, "#C8A06A", dy=0)]
    s = fit(b, max(h * 0.56, b - 170))
    for i in range(6): o.append(E.kneel(w * (0.08 + i * 0.17), b, s, color="#1A1418", skin="#8A6A5A", flip=i >= 3))
    return "".join(o)

def dry_cistern(p, w, h, seed):
    """They come to the cisterns, and find no water; they return with their vessels empty, and cover their heads."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#E8A060", "#F8E0A8"), ground(w, h, h * 0.62, "#C8A06A", dy=0),
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.8)}" rx="{f(w * 0.12)}" ry="{f(h * 0.06)}" fill="#3A2A1E" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
         f'<path d="M{f(w * 0.38)} {f(h * 0.8)} L {f(w * 0.38)} {f(h * 0.74)} Q {f(w * 0.5)} {f(h * 0.7)} {f(w * 0.62)} {f(h * 0.74)} L {f(w * 0.62)} {f(h * 0.8)}" fill="none" stroke="#8A7A6A" stroke-width="4"></path>']
    s = fit(b, max(h * 0.4, b - 210))
    for i, x in enumerate((0.16, 0.28, 0.76, 0.88)):
        o.append(man(p, w * x, b, s * 0.84, ["#6A5A3A", "#5A4A6A", "#6A3A2A", "#4A5A3A"][i], flip=x > 0.5, up=[(-22, -158), (-14, -186), (2, -200)])
                 + J1.pitcher(w * x + (-30 if x > 0.5 else 30) * s, b, s * 0.5, torch=False))
    return "".join(o)

def cracked(w, h, seed):
    """The ground which is cracked, for that no rain hath been in the land: the plough left in the field."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#E8A060", "#F8E0A8"), sun(w * 0.8, h * 0.2, min(w, h) * 0.06, color="#FFE680", op=0.4), ground(w, h, h * 0.46, "#C8946A", dy=0)]
    for _ in range(40):
        x, y = r.uniform(0, w), r.uniform(h * 0.5, h)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(-30, 30))} {f(r.uniform(-8, 8))} l {f(r.uniform(-20, 20))} {f(r.uniform(-10, 10))}" stroke="#6A4A2A" stroke-width="2" fill="none"></path>')
    px, py = w * 0.3, h * 0.86
    o.append(f'<path d="M{f(px)} {f(py)} L {f(px - w * 0.1)} {f(py - h * 0.2)} M{f(px)} {f(py)} L {f(px + w * 0.05)} {f(py + 4)}" stroke="#4A2A1A" stroke-width="5" stroke-linecap="round"></path>')
    return "".join(o)

def hind(x, y, s=1.0, flip=False, fawn=False):
    sx = -s if flip else s
    k = 0.6 if fawn else 1.0
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx * k)} {f(s * k)})">'
            '<path d="M-40 -60 Q -20 -72 20 -66 L 34 -86 Q 40 -100 50 -96 L 54 -84 L 42 -78 L 34 -60 L 30 -40 L 34 0 L 28 0 L 22 -36 L -24 -40 L -28 0 L -34 0 L -36 -42 Q -48 -50 -40 -60 Z" fill="#B8844A" stroke="#0D0D0F" stroke-width="2.2"></path>'
            '<path d="M44 -96 L 42 -108 L 48 -98" fill="#B8844A" stroke="#0D0D0F" stroke-width="1.6"></path><circle cx="46" cy="-88" r="1.8" fill="#0D0D0F"></circle></g>')

def bare_beasts(w, h, seed):
    """The hind in the field calveth and forsaketh her young, because there is no grass; the wild asses stand on the bare
    heights, they pant for air."""
    o = [K2.sky(w, h, "#E8A060", "#F8E0A8"), f'<path d="M{f(w * 0.5)} {f(h + 10)} L {f(w * 0.74)} {f(h * 0.4)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} Z" fill="#B8846A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.76, "#C8A070", dy=0)]
    s = min(1.0, h / 260)
    o.append(hind(w * 0.18, h * 0.94, s) + hind(w * 0.36, h * 0.94, s, fawn=True, flip=True))
    o.append(N.ass(w * 0.8, h * 0.5, s * 0.6, flip=True, color="#A8946A") + N.ass(w * 0.92, h * 0.54, s * 0.5, color="#988A64"))
    return "".join(o)

def rain_clouds(w, h, seed):
    """Are there any among the vanities of the nations that can cause rain? or can the heavens give showers?: clouds gathering
    over the parched hills."""
    o = [K2.sky(w, h, "#5A6A8A", "#E8C8A0")]
    for i in range(5):
        o.append(f'<ellipse cx="{f(w * (0.1 + i * 0.2))}" cy="{f(h * 0.3)}" rx="{f(w * 0.14)}" ry="{f(h * 0.12)}" fill="#7A8098" opacity="0.9"></ellipse>')
    o.append(hills(w, h, h * 0.66, seed, "#B8946A", amp=12, step=80))
    return "".join(o)

def circling(w, h, seed):
    """Four kinds appointed over them: the plain empty at dusk, birds of the heavens circling (told in words only)."""
    o = [K2.sky(w, h, "#2A1A2A", "#B8603A"), hills(w, h, h * 0.66, seed, "#3A2A2A", amp=10, step=80), ground(w, h, h * 0.76, "#4A3A2E", dy=0)]
    for i in range(9):
        a = i * 2 * math.pi / 9
        o.append(bird(w * 0.5 + math.cos(a) * w * 0.2, h * 0.36 + math.sin(a) * h * 0.14, 1.4))
    return "".join(o)

def winnowing(p, w, h, seed):
    """I have winnowed them with a fan in the gates of the land: a winnower tossing grain at the gate, the chaff driven away."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8", "#F3E0B0"), wall(w * 0.5, w + 10, h * 0.34, h * 0.76, seed, towers=2, gate=w * 0.76), ground(w, h, h * 0.76, "#C8A070", dy=0),
         S4b.threshing_floor(w * 0.3, b, w * 0.4)]
    s = fit(b, max(h * 0.4, b - 220))
    o.append(man(p, w * 0.3, b - 6, s, "#6A4A2A", up=[(-22, -158), (-50, -190), (-70, -230)]))
    o.append(f'<path d="M{f(w * 0.3 - 70 * s)} {f(b - 230 * s)} L {f(w * 0.3 - 20 * s)} {f(b - 110 * s)}" stroke="#8A6A3A" stroke-width="{f(4 * s)}"></path>')
    o.append(J1.chaff(40, -10, w * 0.24, h * 0.2, h * 0.6, seed))
    return "".join(o)

def noon_dark(w, h, seed):
    """Her sun is gone down while it was yet day: the sun darkened at noon over the city, a destroyer at noonday."""
    o = [K2.sky(w, h, "#1A1018", "#5A3A3A"), f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.26)}" r="{f(min(w, h) * 0.1)}" fill="#0D0D0F" stroke="#FFC14D" stroke-width="4"></circle>',
         V.rays(w * 0.5, h * 0.26, 24, min(w, h) * 0.11, min(w, h) * 0.2, color="#FFC14D", op=0.4), jerusalem(w * 0.1, w * 0.9, h * 0.86, h * 0.5, seed, color="#8A7A6A"),
         ground(w, h, h * 0.86, "#2A2024", dy=0)]
    return "".join(o)

def dry_brook(w, h, seed):
    """Wilt thou be unto me as a deceitful brook, as waters that fail?: a dry stream-bed of white stones in a wadi."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#E8A060", "#F8E0A8"), hills(w, h, h * 0.42, seed, "#B8846A", amp=16, step=70), ground(w, h, h * 0.52, "#C8A070", dy=0),
         f'<path d="M{f(w * 0.3)} {f(h * 0.52)} C {f(w * 0.4)} {f(h * 0.7)} {f(w * 0.2)} {f(h * 0.82)} {f(w * 0.36)} {f(h + 10)} L {f(w * 0.62)} {f(h + 10)} C {f(w * 0.46)} {f(h * 0.82)} {f(w * 0.6)} {f(h * 0.7)} {f(w * 0.4)} {f(h * 0.52)} Z" fill="#D8C8A8" stroke="#0D0D0F" stroke-width="2"></path>']
    o.append("".join(f'<ellipse cx="{f(w * r.uniform(0.32, 0.56))}" cy="{f(h * r.uniform(0.6, 0.98))}" rx="{f(r.uniform(4, 10))}" ry="{f(r.uniform(3, 6))}" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="1"></ellipse>' for _ in range(24)))
    return "".join(o)
