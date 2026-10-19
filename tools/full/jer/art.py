"""Drawings for the Jeremiah volume, on top of 2 Chronicles' (chr2.art, which carries chr1.art, kg2.art, kg1.art and 2 Samuel's
drawings as K2). Jeremiah at a distance: jer_fig (a dark blue-grey robe and headcloth; beardless at his call, then a black
beard, then grey). The images of the prophecy are drawn as things (the almond rod, the caldron, the girdle, the potter's
wheel, the yoke); the oracles against the nations as technical maps (genesis.art3 grid_bg/node/route/label)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from chr2.art import *
from chr2.art import f, K2, K3
from genesis.art2 import fit, ground, hills, bird, SKIN, WHITE_BEARD
from genesis.art3 import man, woman, sun, label, grid_bg, node, route
from genesis import art as X
import joshua1 as J, judges1 as J1, judges2 as JG2, ruth1 as R1, exodus as E, exodus2 as E2, exodus3 as E3, exodus4 as E4, exodus5 as V
import samuel1 as S1, samuel2 as S2, samuel3 as S3, samuel4 as S4b, numbers1 as N
from exo import art as A
from num.art import ALL
from jos.art import crowd_at, warrior, WAR, night

JER_C = "#3A4656"
GREY_BEARD = WHITE_BEARD.replace("#E8E2D6", "#7A746E")
OLD_BEARD = WHITE_BEARD.replace("#E8E2D6", "#B8B2A6")
BABEL_C = "#2A4A6A"

def jer_fig(p, x, y, s, age=1, flip=False, up=None, kind="Robe"):
    """Jeremiah at a distance: dark blue-grey robe and headcloth; no beard at his call (age 0), black (1), greying (2), grey (3)."""
    beard = ["", A.BLACK_BEARD, GREY_BEARD, OLD_BEARD][age]
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=JER_C, kind=kind, sw=3, flip=flip, up=up, extra=A.headcloth(JER_C, cord="#1A2230") + beard)

def jer_kneel(x, y, s, flip=False):
    return E.kneel(x, y, s, color=JER_C, skin="#9A6A4A", flip=flip)

def glow(x, y, r, color="#FFF4C2", op=0.5, uid="gl"):
    return (f'<defs><radialGradient id="{uid}" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{color}" stop-opacity="{op}"></stop>'
            f'<stop offset="1" stop-color="{color}" stop-opacity="0"></stop></radialGradient></defs><circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="url(#{uid})"></circle>')

def shaft(x, w, h, top_w=0.08, bot_w=0.22, color="#FFF4C2", op=0.35):
    """A shaft of light from the sky (the word of Jehovah came — God is never drawn)."""
    return (f'<path d="M{f(x - w * top_w)} -10 L {f(x + w * top_w)} -10 L {f(x + w * bot_w)} {f(h + 10)} L {f(x - w * bot_w)} {f(h + 10)} Z" '
            f'fill="{color}" opacity="{op}"></path>')

def smoke(x, y, n, seed, r0=0.05, w=1.0, color="#3A2A2E", op=0.6, drift=8):
    r = random.Random(seed); o = []
    for i in range(n):
        o.append(f'<circle cx="{f(x + i * drift + r.uniform(-10, 10))}" cy="{f(y - i * 22 * w)}" r="{f((r0 * 400 + i * 4) * w)}" fill="{color}" opacity="{max(0.1, op - i * 0.04):.2f}"></circle>')
    return "".join(o)

def wall(x0, x1, top, base, seed, color="#C8A878", towers=4, gate=None, breach=None):
    """A city wall seen from outside: stone courses, battlements, square towers a little taller; gate=x puts a dark gateway
    there; breach=(xa, xb) breaks the wall down between those x."""
    r = random.Random(seed); hh = base - top; o = []
    dark = "#8A6A4A"
    def seg_(a, b):
        s = [f'<rect x="{f(a)}" y="{f(top)}" width="{f(b - a)}" height="{f(hh)}" fill="{color}" stroke="#0D0D0F" stroke-width="2.2"></rect>']
        for k in range(1, 5):
            y = top + hh * k / 5
            s.append(f'<path d="M{f(a)} {f(y)} L {f(b)} {f(y)}" stroke="{dark}" stroke-width="1.2"></path>')
        mw = max(6, hh * 0.12); x = a
        while x + mw < b:
            s.append(f'<rect x="{f(x)}" y="{f(top - mw * 0.8)}" width="{f(mw)}" height="{f(mw * 0.8)}" fill="{color}" stroke="#0D0D0F" stroke-width="1.6"></rect>'); x += mw * 2
        return "".join(s)
    if breach:
        o.append(seg_(x0, breach[0]) + seg_(breach[1], x1))
        o.append(J.collapse(breach[0] - 6, breach[1] + 6, base, hh * 0.9, seed, color=color))
    else:
        o.append(seg_(x0, x1))
    tw = max(16, (x1 - x0) * 0.05)
    for i in range(towers):
        tx = x0 + (x1 - x0) * (i + 0.5) / towers - tw / 2
        if breach and breach[0] - tw < tx < breach[1]: continue
        o.append(f'<rect x="{f(tx)}" y="{f(top - hh * 0.3)}" width="{f(tw)}" height="{f(hh * 1.3)}" fill="{color}" stroke="#0D0D0F" stroke-width="2.2"></rect>'
                 f'<rect x="{f(tx + tw * 0.38)}" y="{f(top - hh * 0.14)}" width="{f(tw * 0.24)}" height="{f(hh * 0.18)}" fill="#2A1E1A"></rect>')
    if gate is not None:
        gw = max(14, hh * 0.5)
        o.append(f'<path d="M{f(gate - gw / 2)} {f(base)} L {f(gate - gw / 2)} {f(base - hh * 0.6)} Q {f(gate)} {f(base - hh * 0.85)} {f(gate + gw / 2)} {f(base - hh * 0.6)} L {f(gate + gw / 2)} {f(base)} Z" fill="#1A1210" stroke="#0D0D0F" stroke-width="2"></path>')
    return "".join(o)

def jerusalem(x0, x1, base, top, seed, color="#B89A6A", temple=True, broken=False, fire=False):
    """Jerusalem on its hill: the wall and towers (joshua1.jericho), the house of Jehovah above; broken=True: the wall breached;
    fire=True: smoke and flames over it."""
    w, hh = x1 - x0, base - top
    r = random.Random(seed)
    o = [f'<path d="M{f(x0 - w * 0.25)} {f(base + 8)} C {f(x0 + w * 0.05)} {f(top + hh * 0.1)} {f(x1 - w * 0.05)} {f(top + hh * 0.1)} {f(x1 + w * 0.25)} {f(base + 8)} Z" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></path>']
    for _ in range(14):                       # houses climbing the hill inside the wall
        hx = r.uniform(x0 + w * 0.06, x1 - w * 0.1); hy = base - hh * r.uniform(0.38, 0.62); hw = w * r.uniform(0.05, 0.08)
        o.append(f'<rect x="{f(hx)}" y="{f(hy - hw * 0.7)}" width="{f(hw)}" height="{f(hw * 0.7)}" fill="{r.choice(["#E8D8B0", "#D8C098", "#C8B088"])}" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 + (f'<rect x="{f(hx + hw * 0.4)}" y="{f(hy - hw * 0.45)}" width="{f(hw * 0.2)}" height="{f(hw * 0.25)}" fill="#3A2A1E"></rect>' if not fire else ""))
    if temple: o.append(temple_front(x0 + w * 0.62, top + hh * 0.36, min(w * 0.24, hh * 0.6), seed))
    o.append(wall(x0, x1, base - hh * 0.26, base, seed, color=color, towers=5, gate=None if broken else x0 + w * 0.3,
                  breach=(x0 + w * 0.3, x0 + w * 0.48) if broken else None))
    if fire:
        o += [E.blaze(x0 + w * (0.16 + i * 0.22), base - hh * 0.5, w * 0.08, hh * 0.3, seed + i, n=5) for i in range(4)]
        o.append(smoke(x0 + w * 0.3, top + hh * 0.1, 9, seed, w=0.9) + smoke(x0 + w * 0.7, top + hh * 0.05, 8, seed + 3, w=0.8))
    return "".join(o)

# ---- Jeremiah 1–3 ---------------------------------------------------------------------------------------------------------
def anathoth_call(p, w, h, seed, age=0, kneel=False):
    """Jeremiah young on the hillside below Anathoth, a shaft of light falling on him from the sky (the word came)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#3A3A6A", "#E8C890"), J.city_hill(w * 0.8, h * 0.52, w * 0.22, h * 0.2, seed),
         hills(w, h, h * 0.56, seed, "#7A7A4A", amp=10, step=70), ground(w, h, h * 0.7, "#A8945A", dy=-8), shaft(w * 0.4, w, h)]
    s = fit(b, max(h * 0.36, b - 240))
    o.append(jer_kneel(w * 0.4, b, s * 0.9) if kneel else jer_fig(p, w * 0.4, b, s, age=age, up=[(-22, -158), (-38, -150), (-50, -136)]))
    o.append(glow(w * 0.4, b - 170 * s, 90 * s, uid=f"{p}g"))
    return "".join(o)

def almond(w, h, seed, rod=True):
    """A rod of an almond-tree in blossom against the dawn (shaqed, the waking tree: I watch over my word)."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#3A3060", "#FFC890"), sun(w * 0.82, h * 0.86, min(w, h) * 0.06, color="#FFE680", op=0.25)]
    x0, y0, x1, y1 = w * 0.1, h * 0.92, w * 0.86, h * 0.2
    o.append(f'<path d="M{f(x0)} {f(y0)} C {f(w * 0.4)} {f(h * 0.7)} {f(w * 0.6)} {f(h * 0.42)} {f(x1)} {f(y1)}" stroke="#4A2A1A" stroke-width="{f(max(5, h * 0.03))}" fill="none" stroke-linecap="round"></path>'
             f'<path d="M{f(x0)} {f(y0)} C {f(w * 0.4)} {f(h * 0.7)} {f(w * 0.6)} {f(h * 0.42)} {f(x1)} {f(y1)}" stroke="#7A4A2A" stroke-width="{f(max(2, h * 0.008))}" fill="none"></path>')
    for i in range(9):
        t = (i + 0.6) / 10
        x = (1 - t) ** 3 * x0 + 3 * (1 - t) ** 2 * t * w * 0.4 + 3 * (1 - t) * t * t * w * 0.6 + t ** 3 * x1
        y = (1 - t) ** 3 * y0 + 3 * (1 - t) ** 2 * t * h * 0.7 + 3 * (1 - t) * t * t * h * 0.42 + t ** 3 * y1
        dx, dy = r.uniform(-1, 1) * w * 0.04, -abs(r.uniform(0.5, 1)) * h * 0.08
        o.append(f'<path d="M{f(x)} {f(y)} l {f(dx)} {f(dy)}" stroke="#4A2A1A" stroke-width="3" stroke-linecap="round"></path>')
        for k in range(3):
            bx, by = x + dx * (0.4 + k * 0.3) + r.uniform(-8, 8), y + dy * (0.4 + k * 0.3) + r.uniform(-6, 6)
            rr = min(w, h) * r.uniform(0.022, 0.034)
            o.append("".join(f'<ellipse cx="{f(bx + rr * 0.8 * math.cos(a))}" cy="{f(by + rr * 0.8 * math.sin(a))}" rx="{f(rr * 0.62)}" ry="{f(rr * 0.42)}" '
                             f'transform="rotate({a * 57.3:.0f} {f(bx + rr * 0.8 * math.cos(a))} {f(by + rr * 0.8 * math.sin(a))})" fill="#FFF0F2" stroke="#0D0D0F" stroke-width="1.2"></ellipse>'
                             for a in [j * 1.2566 for j in range(5)])
                     + f'<circle cx="{f(bx)}" cy="{f(by)}" r="{f(rr * 0.3)}" fill="#E8708A"></circle>')
    return "".join(o)

def caldron(w, h, seed):
    """A boiling caldron on its fire, its face toward the south: the steam pouring out from the north."""
    cx, by = w * 0.48, h * 0.86
    rw = min(w * 0.3, h * 0.55)
    o = [K2.sky(w, h, "#2A1A2A", "#8A3A2A"), ground(w, h, h * 0.86, "#3A2A1E", dy=0),
         E.blaze(cx, by + 4, rw * 1.3, rw * 0.6, seed, n=8),
         f'<path d="M{f(cx - rw)} {f(by - rw * 0.9)} C {f(cx - rw * 1.05)} {f(by - rw * 0.1)} {f(cx + rw * 1.05)} {f(by - rw * 0.1)} {f(cx + rw)} {f(by - rw * 0.9)} Z" fill="#3A3A3E" stroke="#0D0D0F" stroke-width="3"></path>'
         f'<ellipse cx="{f(cx)}" cy="{f(by - rw * 0.9)}" rx="{f(rw)}" ry="{f(rw * 0.22)}" fill="#5A5A60" stroke="#0D0D0F" stroke-width="3"></ellipse>'
         f'<ellipse cx="{f(cx)}" cy="{f(by - rw * 0.88)}" rx="{f(rw * 0.86)}" ry="{f(rw * 0.16)}" fill="#C8682E"></ellipse>'
         f'<path d="M{f(cx - rw * 0.9)} {f(by - rw * 0.5)} C {f(cx - rw * 0.4)} {f(by - rw * 0.4)} {f(cx + rw * 0.4)} {f(by - rw * 0.4)} {f(cx + rw * 0.9)} {f(by - rw * 0.5)}" stroke="#6A6A70" stroke-width="2" fill="none"></path>']
    r = random.Random(seed)
    for i in range(10):
        x = cx + r.uniform(-rw * 0.6, rw * 0.6) + i * rw * 0.12; y = by - rw * (1.1 + i * 0.16)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rw * (0.14 + i * 0.03))}" fill="#E8E2D6" opacity="{0.7 - i * 0.05:.2f}"></circle>')
    for i in range(5):
        x = cx + r.uniform(-rw * 0.7, rw * 0.7)
        o.append(f'<circle cx="{f(x)}" cy="{f(by - rw * 0.92 + r.uniform(-4, 4))}" r="{f(rw * 0.05)}" fill="#FFC14D" stroke="#0D0D0F" stroke-width="1"></circle>')
    ax, ay = w * 0.9, h * 0.16
    o.append(f'<circle cx="{f(ax)}" cy="{f(ay)}" r="20" fill="none" stroke="#FFD23F" stroke-width="1.6"></circle>'
             f'<path d="M{f(ax)} {f(ay - 28)} L {f(ax - 6)} {f(ay - 10)} L {f(ax + 6)} {f(ay - 10)} Z" fill="#FFD23F"></path>' + label(ax, ay + 40, "NORTH", "#FFD23F", 10))
    return "".join(o)

NORTH_PEOPLES = ["BABYLON", "THE CHALDEANS", "THE KINGS OF THE NORTH", "ARAM", "THE MEDES"]
def north_map(w, h, gates=True):
    """All the families of the kingdoms of the north coming down on Jerusalem, every one setting his throne at its gates."""
    o = [grid_bg(w, h)]
    jx, jy = w * 0.5, h * 0.74
    for i, nm in enumerate(NORTH_PEOPLES):
        x = w * (0.12 + i * 0.19); y = h * (0.14 + (i % 2) * 0.08)
        o.append(f'<rect x="{f(x - w * 0.08)}" y="{f(y - 12)}" width="{f(w * 0.16)}" height="22" fill="#D7261E" fill-opacity="0.2" stroke="#D7261E" stroke-width="1.6"></rect>'
                 + label(x, y + 4, nm, "#FF8A6A", 8))
        o.append(route([(x, y + 12), (jx + (x - jx) * 0.28, jy - h * 0.1)], color="#D7261E"))
    o.append(f'<circle cx="{f(jx)}" cy="{f(jy)}" r="{f(min(w, h) * 0.09)}" fill="#FFD23F" fill-opacity="0.15" stroke="#FFD23F" stroke-width="2"></circle>' + label(jx + min(w, h) * 0.17, jy + 4, "JERUSALEM", "#FFD23F", 11, anchor="start"))
    if gates:
        for a in range(8):
            t = a * math.pi / 4
            gx, gy = jx + math.cos(t) * min(w, h) * 0.13, jy + math.sin(t) * min(w, h) * 0.13
            o.append(f'<rect x="{f(gx - 5)}" y="{f(gy - 5)}" width="10" height="10" fill="#D7261E" stroke="#FF8A6A" stroke-width="1"></rect>')
    o.append(label(w * 0.5, h * 0.96, "OUT OF THE NORTH", "#8FD0E2", 9))
    return "".join(o)

def iron_pillar(p, w, h, seed, age=0):
    """A fortified city, an iron pillar and brazen walls: the prophet standing alone before the kings, princes, priests and
    people of the land, a wall of brass behind him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#4A3A5A", "#E8B880"), ground(w, h, h * 0.66, "#8A7A5A", dy=0),
         f'<rect x="{f(w * 0.02)}" y="{f(h * 0.3)}" width="{f(w * 0.36)}" height="{f(h * 0.38)}" fill="#B87333" stroke="#0D0D0F" stroke-width="2.6"></rect>']
    for i in range(6):
        o.append(f'<path d="M{f(w * 0.02)} {f(h * (0.36 + i * 0.055))} L {f(w * 0.38)} {f(h * (0.36 + i * 0.055))}" stroke="#7A4A1E" stroke-width="2"></path>')
    for i in range(7):
        o.append(f'<rect x="{f(w * (0.02 + i * 0.054))}" y="{f(h * 0.26)}" width="{f(w * 0.03)}" height="{f(h * 0.04)}" fill="#B87333" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(f'<rect x="{f(w * 0.3)}" y="{f(h * 0.16)}" width="{f(w * 0.035)}" height="{f(b - h * 0.16)}" fill="#4A4E58" stroke="#0D0D0F" stroke-width="2.4"></rect>')
    s = fit(b, max(h * 0.4, b - 240))
    o.append(jer_fig(p, w * 0.22, b, s, age=age))
    o.append(king_fig(p, w * 0.6, b, s * 0.96, cloth="#1F3A7A", flip=True))
    o.append(priest(p, w * 0.72, b, s * 0.94, flip=True))
    o.append(crowd_at(p, w, h, seed, w * 0.78, w * 0.98, h * 0.7, b, 8, s * 0.6, s * 0.9, flip=True))
    return "".join(o)

def wilderness(w, h, seed, pits=True, night_=False):
    """A land not sown: the wilderness, a land of deserts and of pits, of drought and of the shadow of death."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#1A1A3A" if night_ else "#E8A060", "#F3D8A0" if not night_ else "#5A4A6A"),
         hills(w, h, h * 0.5, seed, "#B8784A", amp=18, step=70), ground(w, h, h * 0.6, "#D8B07A", dy=-6)]
    if pits:
        for _ in range(6):
            x, y = r.uniform(w * 0.05, w * 0.95), r.uniform(h * 0.66, h * 0.94)
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * r.uniform(0.03, 0.06))}" ry="{f(h * 0.025)}" fill="#3A2214" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    for _ in range(14):
        x, y = r.uniform(0, w), r.uniform(h * 0.62, h)
        o.append(f'<path d="M{f(x)} {f(y)} l 6 -10 l 6 10" stroke="#8A5A30" stroke-width="1.6" fill="none"></path>')
    o.append(f'<path d="M{f(w * 0.1)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.8)} {f(w * 0.5)} {f(h * 0.7)} {f(w * 0.7)} {f(h * 0.62)}" stroke="#F3E0B0" stroke-width="5" fill="none" stroke-dasharray="14 10"></path>')
    if night_: o.append(mk.stars(30, w, h * 0.4, seed))
    return "".join(o)

def cisterns(w, h, seed):
    """The fountain of living waters forsaken, and cisterns hewn out: broken cisterns that can hold no water."""
    o = [K2.sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, h * 0.5, "#B89A6A", dy=0),
         E4.rock(w * 0.06, h * 0.32, w * 0.26, h * 0.3), E4.gush(w * 0.2, h * 0.5, seed, scale=min(1.2, h / 300)),
         f'<path d="M{f(w * 0.12)} {f(h * 0.66)} C {f(w * 0.2)} {f(h * 0.8)} {f(w * 0.3)} {f(h * 0.9)} {f(w * 0.36)} {f(h + 10)}" stroke="#2C9DB8" stroke-width="{f(h * 0.05)}" fill="none"></path>'
         f'<path d="M{f(w * 0.12)} {f(h * 0.66)} C {f(w * 0.2)} {f(h * 0.8)} {f(w * 0.3)} {f(h * 0.9)} {f(w * 0.36)} {f(h + 10)}" stroke="#E8F6FA" stroke-width="2" fill="none" stroke-dasharray="10 12"></path>']
    for i, x in enumerate((0.52, 0.7, 0.88)):
        cx, cy, rx, ry = w * x, h * (0.7 + (i % 2) * 0.08), w * 0.075, h * 0.07
        o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="#3A2A1E" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
                 f'<ellipse cx="{f(cx)}" cy="{f(cy + ry * 0.3)}" rx="{f(rx * 0.7)}" ry="{f(ry * 0.5)}" fill="#5A4030"></ellipse>'
                 f'<path d="M{f(cx - rx * 0.6)} {f(cy - ry * 0.4)} l {f(rx * 0.3)} {f(ry * 0.5)} l {f(rx * 0.2)} {f(-ry * 0.2)} l {f(rx * 0.3)} {f(ry * 0.7)} M{f(cx + rx * 0.2)} {f(cy - ry * 0.7)} l {f(rx * 0.2)} {f(ry * 0.6)}" stroke="#D8B07A" stroke-width="2" fill="none"></path>')
    return "".join(o)

def lions_waste(w, h, seed):
    """The young lions have roared upon him: a lion on a rise above the burned cities, without inhabitant."""
    o = [K2.sky(w, h, "#3A1A1A", "#C8703A"), J.collapse(w * 0.5, w + 10, h * 0.76, h * 0.26, seed, color="#8A6A4A"),
         J.collapse(-10, w * 0.2, h * 0.78, h * 0.2, seed + 1, color="#8A6A4A"), smoke(w * 0.72, h * 0.5, 8, seed), smoke(w * 0.08, h * 0.56, 6, seed + 2),
         f'<path d="M-10 {f(h * 0.82)} C {f(w * 0.2)} {f(h * 0.7)} {f(w * 0.4)} {f(h * 0.66)} {f(w * 0.5)} {f(h * 0.72)} L {f(w * 0.56)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         ground(w, h, h * 0.86, "#4A3020", dy=0), JG2.lion(w * 0.3, h * 0.72, min(1.1, h / 300), flip=False, roar=True)]
    return "".join(o)

def ways_map(w, h, hi=("EGYPT", "ASSYRIA")):
    """What hast thou to do in the way to Egypt, or in the way to Assyria? Judah between the Shihor and the River."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M{f(w * 0.1)} {f(h + 10)} C {f(w * 0.12)} {f(h * 0.7)} {f(w * 0.08)} {f(h * 0.5)} {f(w * 0.14)} {f(h * 0.36)}" stroke="#2C9DB8" stroke-width="5" fill="none"></path>'
             + label(w * 0.15, h * 0.46, "THE SHIHOR", "#8FD0E2", 9, anchor="start"))
    o.append(f'<path d="M{f(w * 0.96)} {f(h * 0.06)} C {f(w * 0.86)} {f(h * 0.3)} {f(w * 0.92)} {f(h * 0.5)} {f(w * 0.84)} {f(h * 0.9)}" stroke="#2C9DB8" stroke-width="5" fill="none"></path>'
             + label(w * 0.7, h * 0.9, "THE RIVER", "#8FD0E2", 9))
    jx, jy = w * 0.46, h * 0.66
    o.append(route([(jx, jy), (w * 0.17, h * 0.78)], color="#D7261E") + route([(jx, jy), (w * 0.78, h * 0.5)], color="#D7261E"))
    o.append(node(w * 0.18, h * 0.8, "EGYPT", "#FF8A6A", r=6, dy=18, size=10) + node(w * 0.8, h * 0.46, "ASSYRIA", "#FF8A6A", r=6, dy=-12, size=10))
    o.append(node(jx, jy, "JUDAH", "#FFD23F", r=7, dy=-14, size=11))
    return "".join(o)

def vine(w, h, seed, wild=False):
    """A noble vine, wholly a right seed, on its stakes (wild=True: turned into the degenerate branches of a foreign vine)."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#8FD0E2" if not wild else "#8A7A6A", "#F3E8C8" if not wild else "#C8A880"), hills(w, h, h * 0.5, seed, "#7A8A4A", amp=8, step=90),
         ground(w, h, h * 0.62, "#8A6A3A", dy=0)]
    for k in range(4):
        x = w * (0.14 + k * 0.24)
        o.append(f'<path d="M{f(x)} {f(h * 0.95)} L {f(x)} {f(h * 0.4)}" stroke="#5A3A1E" stroke-width="4"></path>')
        o.append(f'<path d="M{f(x)} {f(h * 0.9)} C {f(x + w * 0.04)} {f(h * 0.7)} {f(x - w * 0.04)} {f(h * 0.55)} {f(x + w * 0.02)} {f(h * 0.42)}" stroke="#4A2A1A" stroke-width="5" fill="none"></path>')
        for _ in range(7):
            lx, ly = x + r.uniform(-w * 0.09, w * 0.09), h * r.uniform(0.38, 0.7)
            col = "#3E7A3A" if not wild else r.choice(["#8A7A3A", "#6A5A2A", "#4A3A2A"])
            o.append(f'<path d="M{f(lx)} {f(ly)} l {f(w * 0.03)} -8 l 4 14 l -10 8 Z" fill="{col}" stroke="#0D0D0F" stroke-width="1.4"></path>')
        if not wild: o.append(N.grapes(x + w * 0.04, h * 0.6, min(0.5, h / 700), seed + k))
        else:
            for _ in range(3):
                o.append(f'<path d="M{f(x)} {f(h * r.uniform(0.45, 0.8))} l {f(r.uniform(-1, 1) * w * 0.08)} {f(r.uniform(-20, 20))}" stroke="#3A2214" stroke-width="2.4"></path>')
    return "".join(o)

def wild_ass(w, h, seed):
    """A swift dromedary traversing her ways; a wild ass used to the wilderness, that snuffeth up the wind."""
    o = [K2.sky(w, h, "#E8A060", "#F3D8A0"), hills(w, h, h * 0.52, seed, "#B8784A", amp=14, step=80), ground(w, h, h * 0.66, "#D8B07A", dy=-4)]
    s = min(1.2, h / 300)
    o.append(J1.camel(w * 0.26, h * 0.92, s * 0.9, flip=False, color="#B5844A"))
    o.append(N.ass(w * 0.7, h * 0.92, s * 1.0, flip=True, color="#A8946A"))
    for i in range(5):
        o.append(f'<path d="M{f(w * 0.86 + i * 10)} {f(h * (0.5 + i * 0.04))} q 20 -8 40 0" stroke="#F3E0B0" stroke-width="2" fill="none" opacity="0.8"></path>')
    return "".join(o)

def high_hill(w, h, seed, smoke_=True):
    """Upon every high hill and under every green tree: a hilltop with a green tree, a wooden stock and a standing stone,
    and the smoke of incense."""
    o = [K2.sky(w, h, "#5A3A5A", "#E8A880"),
         f'<path d="M-10 {f(h + 10)} C {f(w * 0.2)} {f(h * 0.5)} {f(w * 0.6)} {f(h * 0.36)} {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} Z" fill="#6A7A3A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         J.oak(w * 0.66, h * 0.52, min(1.0, h / 360), seed)]
    o.append(f'<rect x="{f(w * 0.4)}" y="{f(h * 0.3)}" width="{f(w * 0.022)}" height="{f(h * 0.2)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.32)} {f(h * 0.5)} L {f(w * 0.335)} {f(h * 0.3)} L {f(w * 0.365)} {f(h * 0.28)} L {f(w * 0.375)} {f(h * 0.5)} Z" fill="#8A8478" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<rect x="{f(w * 0.46)}" y="{f(h * 0.44)}" width="{f(w * 0.05)}" height="{f(h * 0.06)}" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></rect>')
    if smoke_: o.append(smoke(w * 0.485, h * 0.42, 7, seed, r0=0.02, w=0.6, color="#E8E2D6", op=0.5))
    return "".join(o)

def bare_heights(w, h, seed, weeping=False, rain=False):
    """The bare heights, the showers withholden; weeping=True: the weeping and supplications of the children of Israel."""
    p = f"bh{seed}"
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#C8A880" if not rain else "#5A6A8A", "#F3E0B0" if not rain else "#A8B8C8"),
         hills(w, h, h * 0.5, seed, "#B8946A", amp=24, step=60), ground(w, h, h * 0.72, "#C8A878", dy=-8)]
    if weeping:
        s = fit(h * 0.94, h * 0.6)
        for i in range(6): o.append(E.kneel(w * (0.12 + i * 0.15), h * 0.94, s * 0.9, color=["#5A4A3A", "#3A4A6A", "#6A3A2A", "#4A5A3A", "#5A3A5A", "#6A5A3A"][i], skin="#9A6A4A", flip=i % 2 == 1))
    else:
        o.append(E4.tent(w * 0.66, h * 0.8, w * 0.16, h * 0.14, color="#3A2A1E"))
        o.append(J1.camel(w * 0.4, h * 0.86, min(0.7, h / 500), color="#B5844A"))
    return "".join(o)

def return_map(w, h, sisters=False):
    """Return, O backsliding children: from the land of the north to Zion, the house of Judah walking with the house of Israel
    (sisters=True: backsliding Israel carried away, treacherous Judah looking on)."""
    o = [grid_bg(w, h)]
    zx, zy = w * 0.5, h * 0.74
    if sisters:
        o.append(f'<rect x="{f(w * 0.2)}" y="{f(h * 0.2)}" width="{f(w * 0.6)}" height="{f(h * 0.3)}" fill="#5A5A6A" fill-opacity="0.25" stroke="#8A8A9A" stroke-width="2" stroke-dasharray="6 5"></rect>'
                 + label(w * 0.5, h * 0.36, "BACKSLIDING ISRAEL · PUT AWAY", "#B8B8C8", 10))
        o.append(f'<rect x="{f(w * 0.3)}" y="{f(h * 0.58)}" width="{f(w * 0.4)}" height="{f(h * 0.28)}" fill="#D7261E" fill-opacity="0.15" stroke="#D7261E" stroke-width="2"></rect>'
                 + label(w * 0.5, h * 0.73, "TREACHEROUS JUDAH", "#FF8A6A", 10))
        o.append(route([(w * 0.5, h * 0.2), (w * 0.5, h * 0.04)], color="#8A8A9A") + label(w * 0.66, h * 0.08, "TO THE NORTH", "#B8B8C8", 8))
        return "".join(o)
    o.append(f'<rect x="{f(w * 0.1)}" y="{f(h * 0.06)}" width="{f(w * 0.8)}" height="{f(h * 0.16)}" fill="#5A5A6A" fill-opacity="0.25" stroke="#8A8A9A" stroke-width="2"></rect>'
             + label(w * 0.5, h * 0.15, "THE LAND OF THE NORTH", "#B8B8C8", 10))
    for i, x in enumerate((0.28, 0.5, 0.72)):
        o.append(route([(w * x, h * 0.24), (zx + (w * x - zx) * 0.2, zy - h * 0.08)], color="#FFD23F"))
    o.append(label(w * 0.2, h * 0.48, "ISRAEL", "#8FD0E2", 10) + label(w * 0.8, h * 0.48, "JUDAH", "#8FD0E2", 10))
    o.append(node(zx, zy, "ZION · THE THRONE OF JEHOVAH", "#FFD23F", r=8, dy=24, size=10))
    return "".join(o)

def weeping_prophet(p, w, h, seed, age=3, smoke_=True):
    """The prophet bowed on a hill over Jerusalem, the city below under smoke."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#1A1028", "#8A3A2A"), jerusalem(w * 0.36, w * 0.98, h * 0.7, h * 0.36, seed, fire=smoke_), ground(w, h, h * 0.7, "#4A2A2A", dy=0),
         f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.2)} {f(h * 0.6)} {f(w * 0.36)} {f(h * 0.74)} {f(w * 0.5)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#3A2A2A" stroke="#0D0D0F" stroke-width="2.4"></path>']
    s = fit(b, max(h * 0.5, b - 260))
    o.append(E.kneel(w * 0.2, b, s, color=JER_C, skin="#9A6A4A"))
    return "".join(o)

def ark_forgotten(w, h, seed):
    """The ark of the covenant of Jehovah: it shall not come to mind, neither shall it be made any more — the ark alone in a
    dim and empty place, fading."""
    o = [K2.sky(w, h, "#1A1428", "#3A2A4A"), ground(w, h, h * 0.8, "#2A2030", dy=0), glow(w * 0.5, h * 0.66, min(w, h) * 0.5, color="#FFE680", op=0.25, uid=f"af{seed}"),
         f'<g opacity="0.55">{J.ark(w * 0.5, h * 0.8, min(1.2, h / 260), uid=f"afk{seed}", glow=False)}</g>']
    return "".join(o)

# ---- Jeremiah 4–6 ---------------------------------------------------------------------------------------------------------
