"""Drawings for Jeremiah chapter 11 (Jeremiah 32–33), on top of jer.art: the court of the guard, the field at Anathoth bought
with seventeen shekels, the deeds sealed and put in an earthen vessel, the flocks passing under the hand of him that numbereth
them, the host of heaven and the sand of the sea."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jer.art import *
from jer.art import f, K2
from jer.art8 import branch, flock
from jer.art10 import ordinances, city_rebuilt, babylon
from jer.art7 import roofs_incense

def court_guard(p, w, h, seed, age=2, visitor=False):
    """The court of the guard in the king's house: a walled yard with a guard at the gate, the prophet within; over the wall,
    the smoke of the besiegers' camp (visitor=True: Hanamel come to him)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#6A5A6A", "#D8B090"), smoke(w * 0.2, h * 0.26, 7, seed, w=0.7), smoke(w * 0.8, h * 0.22, 6, seed + 1, w=0.6),
         f'<rect x="-10" y="{f(h * 0.34)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#C8B088" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.78)}" y="{f(h * 0.42)}" width="{f(w * 0.1)}" height="{f(h * 0.22)}" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></rect>',
         ground(w, h, h * 0.64, "#B8A07A", dy=0)]
    s = fit(b, max(h * 0.4, b - 230))
    o.append(warrior(p, w * 0.92, b, s * 0.96, "#6A2A3A", flip=True))
    o.append(jer_fig(p, w * 0.32, b, s, age=age))
    if visitor: o.append(man(p, w * 0.56, b, s * 0.98, "#6A5A3A", flip=True, up=[(22, -158), (44, -150), (66, -140)], extra=A.headcloth("#6A5A3A") + A.BLACK_BEARD))
    return "".join(o)

def deeds(w, h, seed, vessel=False):
    """The deed of the purchase, sealed and open, and the silver weighed in the balances (vessel=True: both deeds put in an
    earthen vessel that they may continue many days)."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A22"></rect>', glow(w * 0.5, h * 0.5, min(w, h) * 0.6, color="#FFE680", op=0.2, uid=f"dd{seed}"),
         f'<rect x="-10" y="{f(h * 0.74)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></rect>']
    s = min(1.4, h / 200)
    def scroll(x, y, sealed):
        return (f'<rect x="{f(x - 44 * s)}" y="{f(y - 18 * s)}" width="{f(88 * s)}" height="{f(36 * s)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2"></rect>'
                f'<ellipse cx="{f(x - 44 * s)}" cy="{f(y)}" rx="{f(6 * s)}" ry="{f(18 * s)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
                f'<ellipse cx="{f(x + 44 * s)}" cy="{f(y)}" rx="{f(6 * s)}" ry="{f(18 * s)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
                + (f'<path d="M{f(x - 10 * s)} {f(y - 18 * s)} l 0 {f(36 * s)} M{f(x + 10 * s)} {f(y - 18 * s)} l 0 {f(36 * s)}" stroke="#6A4A2A" stroke-width="2"></path>'
                   f'<circle cx="{f(x)}" cy="{f(y + 18 * s)}" r="{f(7 * s)}" fill="#B5121B" stroke="#0D0D0F" stroke-width="1.6"></circle>' if sealed else
                   "".join(f'<path d="M{f(x - 34 * s)} {f(y - 8 * s + k * 8 * s)} l {f(68 * s)} 0" stroke="#6A4A2A" stroke-width="1.6"></path>' for k in range(3))))
    if vessel:
        jx, jy = w * 0.5, h * 0.8
        o.append(jar(jx, jy, s * 1.6, color="#B8703A", stopper=None))
        o.append(f'<g transform="rotate(-70 {f(jx - 4 * s)} {f(jy - 170 * s)})">{scroll(jx - 4 * s, jy - 170 * s, True)}</g>'
                 f'<g transform="rotate(-80 {f(jx + 14 * s)} {f(jy - 176 * s)})">{scroll(jx + 14 * s, jy - 176 * s, False)}</g>')
    else:
        o.append(scroll(w * 0.28, h * 0.66, True) + scroll(w * 0.28, h * 0.5, False))
        o.append(S4b.balance(w * 0.7, h * 0.76, s * 0.9))
        o.append(JG2.silver(w * 0.5, h * 0.76, 17, seed, spread=w * 0.06))
    return "".join(o)

def field_anathoth(p, w, h, seed, buyers=False):
    """The field that is in Anathoth in the land of Benjamin: a walled field below the village (buyers=True: men pacing the
    boundary with a deed in hand, witnesses by)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8", "#F3E8C8"), J.city_hill(w * 0.78, h * 0.5, w * 0.24, h * 0.2, seed), hills(w, h, h * 0.5, seed, "#8A9A6A", amp=10, step=90),
         ground(w, h, h * 0.58, "#A8B870", dy=0),
         f'<path d="M{f(w * 0.06)} {f(h * 0.92)} L {f(w * 0.2)} {f(h * 0.62)} L {f(w * 0.7)} {f(h * 0.62)} L {f(w * 0.86)} {f(h * 0.92)}" fill="none" stroke="#8A8478" stroke-width="{f(h * 0.025)}"></path>']
    for k in range(5):
        y = h * (0.66 + k * 0.05)
        o.append(f'<path d="M{f(w * (0.19 - k * 0.02))} {f(y)} L {f(w * (0.71 + k * 0.02))} {f(y)}" stroke="#7A8A4A" stroke-width="2"></path>')
    if buyers:
        s = fit(b, max(h * 0.44, b - 210))
        o.append(man(p, w * 0.3, b, s, "#6A5A3A", up=[(-22, -158), (-40, -150), (-60, -150)], extra=A.headcloth("#6A5A3A") + A.BLACK_BEARD)
                 + f'<rect x="{f(w * 0.3 - 74 * s)}" y="{f(b - 164 * s)}" width="{f(26 * s)}" height="{f(30 * s)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.4"></rect>')
        for i in range(2): o.append(man(p, w * (0.5 + i * 0.1), b, s * 0.96, ["#3A4A6A", "#5A3A2A"][i], flip=True, extra=A.headcloth(["#3A4A6A", "#5A3A2A"][i]) + A.WHITE_BEARD))
    return "".join(o)

def prayer(p, w, h, seed, age=2):
    """I prayed unto Jehovah: the prophet kneeling in the court of the guard at evening, his hands raised."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#2A2A5A", "#E8A880"), f'<rect x="-10" y="{f(h * 0.4)}" width="{f(w + 20)}" height="{f(h * 0.26)}" fill="#A89070" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         ground(w, h, h * 0.66, "#8A7A5A", dy=0), glow(w * 0.5, h * 0.1, min(w, h) * 0.5, color="#FFF4C2", op=0.3, uid=f"pr{seed}")]
    s = fit(b, max(h * 0.4, b - 240))
    o.append(E.kneel(w * 0.5, b, s, color=JER_C, skin="#9A6A4A"))
    return "".join(o)

def egypt_wonders(w, h, seed):
    """Signs and wonders in the land of Egypt, a strong hand and an outstretched arm: the Red Sea parted, the way through the
    midst (no hand drawn)."""
    return E3.sea_corridor(w, h, (w * 0.5, h * 0.36), w * 0.2, w * 0.8, seed, uid=f"sc{seed}")

def milk_honey(w, h, seed):
    """A land flowing with milk and honey: green hills, flocks, and bees about a hive."""
    o = [K2.sky(w, h, "#8FC0E0", "#FFF0C8"), hills(w, h, h * 0.44, seed, "#6A9A4A", amp=14, step=80), ground(w, h, h * 0.58, "#9AC05A", dy=0)]
    s = min(0.7, h / 380)
    for i in range(6): o.append(E.sheep(w * (0.08 + i * 0.1), h * (0.86 - (i % 2) * 0.04), s))
    hx, hy = w * 0.78, h * 0.92
    o.append(f'<path d="M{f(hx - 30)} {f(hy)} Q {f(hx - 34)} {f(hy - 50)} {f(hx)} {f(hy - 56)} Q {f(hx + 34)} {f(hy - 50)} {f(hx + 30)} {f(hy)} Z" fill="#C8A050" stroke="#0D0D0F" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(hx - 26)} {f(hy - 12 - k * 12)} L {f(hx + 26)} {f(hy - 12 - k * 12)}" stroke="#8A6A2A" stroke-width="1.6"></path>' for k in range(3))
             + "".join(f'<ellipse cx="{f(hx + dx)}" cy="{f(hy - 70 + dy)}" rx="4" ry="3" fill="#E8B830" stroke="#0D0D0F" stroke-width="1"></ellipse>' for dx, dy in ((-30, 0), (10, -14), (34, 6), (-6, -24))))
    return "".join(o)

def numbering(p, w, h, seed):
    """The flocks shall again pass under the hands of him that numbereth them: a shepherd at the gap of the fold, his rod over
    each sheep as it passes."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8", "#F3E8C8"), hills(w, h, h * 0.5, seed, "#8A9A6A", amp=12, step=80), ground(w, h, h * 0.6, "#A8B870", dy=0),
         f'<path d="M{f(w * 0.56)} {f(h * 0.94)} L {f(w * 0.56)} {f(h * 0.72)} L {f(w + 10)} {f(h * 0.72)}" fill="none" stroke="#8A8478" stroke-width="{f(h * 0.04)}"></path>']
    s = fit(b, max(h * 0.4, b - 220))
    o.append(man(p, w * 0.48, b, s, "#6A5A3A", flip=True, up=[(22, -158), (44, -130), (60, -100)], extra=A.headcloth("#6A5A3A") + A.BLACK_BEARD))
    o.append(f'<path d="M{f(w * 0.48 - 60 * s)} {f(b - 100 * s)} L {f(w * 0.48 - 120 * s)} {f(b - 40 * s)}" stroke="#5A3A1E" stroke-width="{f(4 * s)}"></path>')
    for i in range(4): o.append(E.sheep(w * (0.08 + i * 0.1), b - (i % 2) * 4, min(0.8, s * 0.9)))
    return "".join(o)

def levites(p, w, h, seed):
    """Neither shall the priests the Levites want a man before me to offer burnt-offerings continually."""
    return altar_service(p, w, h, seed)

def stars_sand(w, h, seed):
    """As the host of heaven cannot be numbered, neither the sand of the sea measured: a night full of stars over the shore."""
    r = random.Random(seed)
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0B0B2A"></rect>', mk.stars(160, w, h * 0.6, seed),
         f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w + 20)}" height="{f(h * 0.14)}" fill="#1A2A4A"></rect>',
         f'<path d="M-10 {f(h * 0.76)} C {f(w * 0.3)} {f(h * 0.72)} {f(w * 0.6)} {f(h * 0.78)} {f(w + 10)} {f(h * 0.74)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#B8A07A" stroke="#0D0D0F" stroke-width="2"></path>']
    o.append("".join(f'<circle cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(h * 0.8, h))}" r="1.2" fill="#E8D8B0"></circle>' for _ in range(200)))
    return "".join(o)

def call_night(w, h, seed):
    """Call unto me, and I will answer thee, and will show thee great things: the night sky over the court of the guard."""
    return (night(w, h, seed, "#0F0E2A") + mk.stars(80, w, h * 0.7, seed + 1) + glow(w * 0.5, h * 0.2, min(w, h) * 0.5, color="#FFF4C2", op=0.25, uid=f"cn{seed}")
            + f'<rect x="-10" y="{f(h * 0.7)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="#3A3040" stroke="#0D0D0F" stroke-width="2"></rect>')
