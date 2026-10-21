"""Drawings for Ezekiel 24–25: the name of the day written; the caldron set on the fire, then set empty on the coals with its
rust; the death of Ezekiel's wife told only as words over the empty house; the headtire and the shoes; the one that escapeth
coming on the road; and the nations round about as a map — Ammon, Moab, Edom, the Philistines — with Rabbah become a stable
for camels."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from ezk.art8 import *
from ezk.art8 import f, K2, K3, P, rect, seated, clouds, smoke, house, INK, EZ_C, GB_BEARD, CAPT, bg, glow, vgrad, rgrad, KK2, JJ2
import judges1 as J1

def day_tablet(w, h, seed):
    """Write thee the name of the day, even of this selfsame day: a clay tablet freshly written, the reed stylus beside it,
    by lamplight."""
    r = random.Random(seed)
    o = [bg(f"dt{seed}", w, h, [(0, "#2A1A1A"), (1, "#6A4A3A")]), glow(f"dg{seed}", w * 0.5, h * 0.6, w * 0.35, h * 0.4, "#FFC14D", 0.35)]
    o.append(f'<rect x="-10" y="{f(h * 0.78)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#5A3A2A" stroke="{INK}" stroke-width="2"></rect>')
    tw, th = min(w * 0.3, h * 0.9), min(h * 0.5, w * 0.24)
    x0, y0 = w * 0.5 - tw / 2, h * 0.78 - th
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(tw)}" height="{f(th)}" rx="10" fill="#C8986A" stroke="{INK}" stroke-width="2.4"></rect>')
    for row in range(5):
        y = y0 + th * (0.18 + row * 0.16)
        x = x0 + tw * 0.08
        while x < x0 + tw * 0.9:
            o.append(f'<path d="M{f(x)} {f(y)} l 4 0 l -2 6 Z" fill="#5A3A2A"></path>'); x += r.uniform(6, 12)
    o.append(f'<path d="M{f(x0 + tw + 20)} {f(h * 0.76)} L {f(x0 + tw + 90)} {f(h * 0.6)}" stroke="#0D0D0F" stroke-width="7" stroke-linecap="round"></path><path d="M{f(x0 + tw + 20)} {f(h * 0.76)} L {f(x0 + tw + 90)} {f(h * 0.6)}" stroke="#C8B070" stroke-width="4" stroke-linecap="round"></path>')
    return "".join(o)

def rusty_caldron(w, h, seed, empty=False):
    """Set on the caldron, heap on the wood, make the fire hot (empty=True: set empty upon the coals, that the rust of it may
    be consumed — red rust streaking the brass)."""
    o = [caldron(w, h, seed, city=False)]
    cx, cy, R = w * 0.5, h * 0.74, min(w * 0.22, h * 0.24)
    for i in range(6):
        x = cx - R * 0.7 + i * R * 0.28
        o.append(f'<path d="M{f(x)} {f(cy - R * 0.4)} q 4 {f(R * 0.2)} 0 {f(R * 0.5)}" stroke="#8A3A1A" stroke-width="{f(R * 0.06)}" fill="none" opacity="0.85"></path>')
    if not empty:
        o.append(rubble(cx - R * 1.6, cx - R * 1.1, h * 0.98, h * 0.08, seed))
    return "".join(o)

def empty_house(w, h, seed, dawn=False):
    """At even my wife died: the house at evening (dawn=True: in the morning), the door open on an empty room, a mat rolled
    against the wall, the lamp gone out — no one drawn."""
    o = [bg(f"eh{seed}{dawn}", w, h, [(0, "#3A3A6A" if dawn else "#1A1A3A"), (1, "#E8B890" if dawn else "#7A4A4A")])]
    o.append(f'<rect x="{f(w * 0.12)}" y="{f(h * 0.24)}" width="{f(w * 0.76)}" height="{f(h * 0.66)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2.6"></rect>')
    for i in range(1, 7):
        o.append(f'<path d="M{f(w * 0.12)} {f(h * 0.24 + i * h * 0.094)} L {f(w * 0.88)} {f(h * 0.24 + i * h * 0.094)}" stroke="#6A4A2A" stroke-width="1.2"></path>')
    dx0, dx1, dt = w * 0.4, w * 0.6, h * 0.4
    o.append(f'<rect x="{f(dx0)}" y="{f(dt)}" width="{f(dx1 - dx0)}" height="{f(h * 0.9 - dt)}" fill="#3A2A22" stroke="{INK}" stroke-width="2.4"></rect>')
    o.append(P(f"M{f(dx0 + w * 0.02)} {f(h * 0.88)} C {f(dx0 + w * 0.02)} {f(h * 0.84)} {f(dx1 - w * 0.02)} {f(h * 0.84)} {f(dx1 - w * 0.02)} {f(h * 0.88)} Z", "#B8946A", 1.6))
    o.append(P(f"M{f(dx1 - w * 0.03)} {f(h * 0.88)} L {f(dx1 - w * 0.03)} {f(h * 0.6)} L {f(dx1 - w * 0.01)} {f(h * 0.6)} L {f(dx1 - w * 0.01)} {f(h * 0.88)} Z", "#C8A878", 1.4))
    o.append(f'<path d="M{f(dx0 + w * 0.06)} {f(h * 0.6)} c 4 -4 10 -4 14 0 l -4 6 l -6 0 Z" fill="#8A6A5A" stroke="{INK}" stroke-width="1.2"></path>')
    o.append(P(f"M{f(dx1)} {f(h * 0.9)} L {f(dx1 + w * 0.08)} {f(h * 0.92)} L {f(dx1 + w * 0.08)} {f(h * 0.42)} L {f(dx1)} {f(dt)} Z", "#5A3A22", 2))
    o.append(ground(w, h, h * 0.9, "#5A4A3A", dy=0))
    return "".join(o)

def headtire(w, h, seed):
    """Bind thy headtire upon thee, and put thy shoes upon thy feet: the white headtire with its blue cord and a pair of
    sandals laid ready by the door, the bread of men untouched."""
    o = [bg(f"ht{seed}", w, h, [(0, "#2A2A3A"), (1, "#7A6A5A")]), f'<rect x="-10" y="{f(h * 0.72)}" width="{f(w + 20)}" height="{f(h * 0.4)}" fill="#5A4A3A" stroke="{INK}" stroke-width="2"></rect>']
    k = min(1.6, h / 220)
    o.append(f'<g transform="translate({f(w * 0.36)} {f(h * 0.8)}) scale({f(k)})">' + P("M-46 0 C -50 -30 -20 -44 0 -44 C 20 -44 50 -30 46 0 Z", "#F3EFE6", 2.2)
             + '<path d="M-44 -14 C -20 -24 20 -24 44 -14" stroke="#1F5FAD" stroke-width="5" fill="none"></path></g>')
    for i in range(2):
        o.append(f'<g transform="translate({f(w * (0.58 + i * 0.07))} {f(h * 0.84)}) scale({f(k)})"><path d="M-10 0 C -12 -30 12 -30 10 0 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.6"></path>'
                 '<path d="M-8 -14 L 8 -18 M-8 -8 L 8 -10" stroke="#3A2A1A" stroke-width="2"></path></g>')
    o.append(f'<ellipse cx="{f(w * 0.84)}" cy="{f(h * 0.82)}" rx="{f(24 * k)}" ry="{f(8 * k)}" fill="#C8A060" stroke="{INK}" stroke-width="1.6"></ellipse>')
    return "".join(o)

def escaped(p, w, h, seed):
    """He that escapeth shall come unto thee: one man coming alone on the road toward the captives' houses by the river."""
    o = [mk.defs(p, *ALL), bg(f"es{seed}", w, h, [(0, "#4A4A7A"), (1, "#E8B890")]), hills(w, h, h * 0.62, seed, "#8A7A6A", amp=8, step=90), ground(w, h, h * 0.7, "#B8A07A", dy=0)]
    o.append(f'<path d="M{f(w * 0.1)} {f(h + 10)} L {f(w * 0.48)} {f(h * 0.7)} L {f(w * 0.54)} {f(h * 0.7)} L {f(w * 0.5)} {f(h + 10)} Z" fill="#D8C8A0"></path>')
    for i in range(3): o.append(house(w * (0.7 + i * 0.09), h * 0.74, w * 0.08, h * 0.12, color="#B8946A"))
    s = min(fit(h * 0.9, h * 0.62), 0.8)
    o.append(mk.person(p, round(w * 0.42), round(h * 0.86), round(s, 3), body=SKIN, cloth="#6A5A4A", sw=2.6, flip=False, up=[(-22, -158), (-30, -120), (-36, -96)], extra=A.headcloth("#5A4A3A")))
    o.append(smoke(w * 0.36, h * 0.86, 3, seed, color="#D8C8A0", op=0.5, k=0.5))
    return "".join(o)

NATIONS = {"AMMON · RABBAH": (0.74, 0.3, -10, "middle"), "MOAB": (0.68, 0.6, -10, "middle"), "BETH-JESHIMOTH": (0.55, 0.4, -10, "start"),
           "BAAL-MEON": (0.66, 0.5, -10, "start"), "KIRIATHAIM": (0.7, 0.68, 16, "middle"), "EDOM · TEMAN": (0.6, 0.84, -10, "middle"),
           "DEDAN": (0.8, 0.8, -10, "middle"), "THE PHILISTINES": (0.16, 0.58, -10, "start"), "THE CHERETHITES": (0.12, 0.7, -10, "start"),
           "TYRE": (0.24, 0.14, -10, "middle"), "SIDON": (0.28, 0.06, 14, "start"), "THE CHILDREN OF THE EAST": (0.9, 0.24, -10, "end")}
def nations_map(w, h, hi=()):
    """The land of Israel among the nations round about as a technical map: the Salt Sea and the Jordan, Jerusalem, and the
    peoples about her; those in hi lit gold."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.14)} -10 C {f(w * 0.12)} {f(h * 0.3)} {f(w * 0.06)} {f(h * 0.6)} {f(w * 0.02)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.08)} C {f(w * 0.48)} {f(h * 0.2)} {f(w * 0.52)} {f(h * 0.32)} {f(w * 0.5)} {f(h * 0.44)}" stroke="#2C9DB8" stroke-width="3" fill="none"></path>'
             f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.56)}" rx="{f(w * 0.03)}" ry="{f(h * 0.12)}" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></ellipse>')
    o.append(node(w * 0.4, h * 0.48, "JERUSALEM", "#D7261E", r=6, dy=-12, size=9))
    for nm, (x, y, dy, an) in NATIONS.items():                # labels placed so none runs off the panel or into another
        on = any(nm.startswith(k) for k in hi)
        o.append(node(w * x, h * y, nm, "#FFD23F" if on else "#4A7A9A", r=5 if on else 3, dy=dy, size=9 if on else 7, anchor=an))
    return "".join(o)

def camels_rabbah(w, h, seed):
    """I will make Rabbah a stable for camels, and the children of Ammon a couching-place for flocks: the broken city, camels
    couched among the ruins, the black tents of the children of the east."""
    o = [bg(f"cr{seed}", w, h, [(0, "#C8803A"), (1, "#F3D8A0")]), hills(w, h, h * 0.56, seed, "#A8805A", amp=10, step=80)]
    o.append(rubble(w * 0.1, w * 0.5, h * 0.74, h * 0.18, seed) + J.jericho(w * 0.5, w * 0.7, h * 0.5, h * 0.74, seed, color="#B8946A", towers=1, houses=False))
    o.append(ground(w, h, h * 0.74, "#C8A06A", dy=0))
    o.append(A.black_tent(w * 0.82, h * 0.8, w * 0.16, h * 0.14))
    k = min(0.7, h / 400)
    for i in range(3): o.append(J1.camel(w * (0.2 + i * 0.22), h * 0.96 - i * 4, k, flip=i % 2 == 1))
    o.append(flock(w * 0.6, w * 0.95, h * 0.86, h * 0.98, 6, seed, cows=0.0))
    return "".join(o)
