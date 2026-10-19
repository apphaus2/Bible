"""Drawings for Jeremiah chapter 15 (Jeremiah 43–45), on top of jer.art: the remnant going down into Egypt, Pharaoh's house at
Tahpanhes and the great stones hidden in the brickwork, the royal pavilion spread over them, the houses of the gods of Egypt
burning, the pillars of Beth-shemesh broken, the Jews of Pathros and the queen of heaven, and Baruch."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jer.art import *
from jer.art import f, K2
from jer.art7 import queen_heaven, roofs_incense

def into_egypt(p, w, h, seed, age=3):
    """Johanan and the captains took all the remnant of Judah into Egypt: a long column with asses and bundles on the desert
    road toward the palms of the Nile; the prophet and Baruch walking among them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#E8A060", "#F8E0A8"), f'<rect x="{f(w * 0.7)}" y="{f(h * 0.5)}" width="{f(w * 0.32)}" height="{f(h * 0.06)}" fill="#2C9DB8"></rect>',
         ground(w, h, h * 0.54, "#E8C890", dy=0)]
    for k in range(3): o.append(J1.palm(w * (0.76 + k * 0.08), h * 0.56, min(0.4, h / 900)))
    for i in range(10):
        t = i / 9; x = w * (0.06 + 0.66 * t); y = h * (0.96 - 0.36 * t)
        s = fit(y, y - h * (0.34 - 0.24 * t))
        if i == 1: o.append(jer_fig(p, x, y, s, age=age))
        elif i == 2: o.append(man(p, x, y, s, "#5A6A4A", extra=A.headcloth("#5A6A4A") + A.BLACK_BEARD))
        elif i in (4, 8): o.append(N.ass(x, y, s * 0.7, color="#A8946A"))
        else: o.append(woman(p, x, y, s * 0.94, ["#7A3A5A", "#5A4A7A", "#8A5A3A"][i % 3]) if i % 2 else man(p, x, y, s * 0.94, "#6A5A4A"))
    return "".join(o)

def pharaoh_house(p, w, h, seed, stones=True, pavilion=False, age=3):
    """The entry of Pharaoh's house in Tahpanhes: a pylon gate of painted brick, the brick pavement before it; the prophet hiding
    great stones in the mortar of the brickwork in the sight of the men of Judah (pavilion=True: a royal pavilion spread over
    the place, no one under it)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#E8A060", "#F8E0A8"), ground(w, h, h * 0.72, "#D8B880", dy=0)]
    for side in (-1, 1):
        x0 = w * (0.5 + side * 0.22)
        o.append(f'<path d="M{f(x0 - w * 0.13)} {f(h * 0.72)} L {f(x0 - w * 0.1)} {f(h * 0.2)} L {f(x0 + w * 0.1)} {f(h * 0.2)} L {f(x0 + w * 0.13)} {f(h * 0.72)} Z" fill="#E8D0A0" stroke="#0D0D0F" stroke-width="2.6"></path>'
                 f'<rect x="{f(x0 - w * 0.1)}" y="{f(h * 0.2)}" width="{f(w * 0.2)}" height="{f(h * 0.04)}" fill="#1F5FAD" stroke="#0D0D0F" stroke-width="2"></rect>'
                 + "".join(f'<path d="M{f(x0 - w * 0.08)} {f(h * (0.3 + k * 0.1))} L {f(x0 + w * 0.08)} {f(h * (0.3 + k * 0.1))}" stroke="#C8A060" stroke-width="2"></path>' for k in range(4)))
    o.append(f'<rect x="{f(w * 0.4)}" y="{f(h * 0.36)}" width="{f(w * 0.2)}" height="{f(h * 0.36)}" fill="#3A2214" stroke="#0D0D0F" stroke-width="2.4"></rect>'
             f'<rect x="{f(w * 0.38)}" y="{f(h * 0.3)}" width="{f(w * 0.24)}" height="{f(h * 0.06)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></rect>')
    for r_ in range(4):
        for c in range(14):
            o.append(f'<rect x="{f(w * (c / 14) + (r_ % 2) * w * 0.035 - 10)}" y="{f(h * (0.74 + r_ * 0.05))}" width="{f(w / 14 - 3)}" height="{f(h * 0.045)}" fill="#C8784A" stroke="#6A3A1E" stroke-width="1.2"></rect>')
    if pavilion:
        o.append(f'<path d="M{f(w * 0.24)} {f(h * 0.84)} L {f(w * 0.24)} {f(h * 0.56)} L {f(w * 0.5)} {f(h * 0.44)} L {f(w * 0.76)} {f(h * 0.56)} L {f(w * 0.76)} {f(h * 0.84)}" fill="none" stroke="#0D0D0F" stroke-width="3"></path>'
                 f'<path d="M{f(w * 0.2)} {f(h * 0.58)} L {f(w * 0.5)} {f(h * 0.42)} L {f(w * 0.8)} {f(h * 0.58)} Z" fill="#2A4A8A" stroke="#0D0D0F" stroke-width="2.4"></path>'
                 + "".join(f'<path d="M{f(w * (0.2 + k * 0.1))} {f(h * 0.58)} l {f(w * 0.05)} {f(h * 0.04)} l {f(w * 0.05)} {f(-h * 0.04)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></path>' for k in range(6))
                 + S3.throne(w * 0.5, h * 0.84, min(0.8, h / 400)))
    elif stones:
        s = fit(b, max(h * 0.4, b - 230))
        o.append(E.kneel(w * 0.36, b, s * 0.9, color=JER_C, skin="#9A6A4A"))
        for k in range(3): o.append(f'<path d="M{f(w * (0.44 + k * 0.05))} {f(h * 0.82)} l 10 -14 l 16 2 l 6 14 Z" fill="#8A8478" stroke="#0D0D0F" stroke-width="1.8"></path>')
        o.append(crowd_at(p, w, h, seed, w * 0.64, w * 0.98, h * 0.78, b, 6, s * 0.7, s * 0.95, flip=True))
    return "".join(o)

def egypt_temples(w, h, seed, burning=True):
    """The houses of the gods of Egypt burned with fire, and the pillars of Beth-shemesh broken: obelisks fallen before a temple
    in flames (no one drawn)."""
    o = [K2.sky(w, h, "#2A0A0A", "#B8502A") if burning else K2.sky(w, h, "#E8A060", "#F8E0A8"), ground(w, h, h * 0.8, "#5A3A2A" if burning else "#D8B880", dy=0)]
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.8)} L {f(w * 0.33)} {f(h * 0.36)} L {f(w * 0.67)} {f(h * 0.36)} L {f(w * 0.7)} {f(h * 0.8)} Z" fill="#C8A878" stroke="#0D0D0F" stroke-width="2.6"></path>')
    for k in range(4):
        o.append(f'<rect x="{f(w * (0.37 + k * 0.08))}" y="{f(h * 0.44)}" width="{f(w * 0.04)}" height="{f(h * 0.36)}" fill="#E8D0A0" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(f'<g transform="rotate(-70 {f(w * 0.14)} {f(h * 0.82)})"><path d="M{f(w * 0.12)} {f(h * 0.82)} L {f(w * 0.13)} {f(h * 0.4)} L {f(w * 0.14)} {f(h * 0.37)} L {f(w * 0.15)} {f(h * 0.4)} L {f(w * 0.16)} {f(h * 0.82)} Z" fill="#B89A7A" stroke="#0D0D0F" stroke-width="2"></path></g>'
             f'<path d="M{f(w * 0.84)} {f(h * 0.82)} L {f(w * 0.845)} {f(h * 0.6)} L {f(w * 0.87)} {f(h * 0.56)} L {f(w * 0.88)} {f(h * 0.82)} Z" fill="#B89A7A" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.86)} {f(h * 0.56)} l 10 -10 l 4 8" stroke="#0D0D0F" stroke-width="2" fill="none"></path>')
    if burning:
        o += [E.blaze(w * (0.36 + i * 0.14), h * 0.8, w * 0.12, h * 0.4, seed + i, n=6) for i in range(3)]
        o.append(smoke(w * 0.5, h * 0.26, 8, seed, w=0.9))
    return "".join(o)

EGYPT_JEWS = ("MIGDOL", "TAHPANHES", "NOPH", "PATHROS")
def egypt_map(w, h):
    """All the Jews that dwelt in the land of Egypt, at Migdol, and at Tahpanhes, and at Memphis, and in the country of Pathros."""
    return near_east(w, h, ("JERUSALEM",) + EGYPT_JEWS, hi=EGYPT_JEWS, arrows=[("JERUSALEM", "TAHPANHES")], lit="#FF8A6A", box=(29.0, 36.0, 24.6, 32.4))

def women_vows(p, w, h, seed):
    """All the women that stood by, a great assembly in Pathros: women with cakes and drink-offerings lifting them up toward the
    moon, smoke of incense rising."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), night(w, h, seed, "#1A1430"), J.moon(w * 0.8, h * 0.16, min(w, h) * 0.06), ground(w, h, h * 0.7, "#3A2E28", dy=0),
         f'<rect x="{f(w * 0.46)}" y="{f(h * 0.74)}" width="{f(w * 0.08)}" height="{f(h * 0.08)}" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="1.8"></rect>',
         smoke(w * 0.5, h * 0.66, 7, seed, r0=0.02, w=0.6, color="#C8C0D0", op=0.5)]
    s = fit(b, max(h * 0.44, b - 210))
    for i in range(6):
        x = w * (0.08 + i * 0.15) + (w * 0.08 if i >= 3 else 0)
        o.append(woman(p, x, b, s * (0.9 + (i % 2) * 0.06), ["#7A2A4A", "#5A4A7A", "#8A5A3A", "#3A5A6A", "#6A3A5A", "#8A6A3A"][i], flip=i >= 3,
                       ))
    return "".join(o)

def baruch_weary(p, w, h, seed):
    """Baruch writing these words in a book, in the fourth year of Jehoiakim: the scribe bent over the roll at night, weary."""
    b = h * 0.94
    from genesis.art4 import clay_lamp
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A2028"></rect>', glow(w * 0.5, h * 0.66, min(w, h) * 0.5, color="#FFC14D", op=0.3, uid=f"bw{seed}"),
         ground(w, h, h * 0.84, "#3A2A22", dy=0), clay_lamp(w * 0.5, h * 0.84, 1.2)]
    s = fit(b, max(h * 0.4, b - 240))
    o.append(E.kneel(w * 0.68, b, s, color="#5A6A4A", skin="#9A6A4A", flip=True))
    o.append(f'<rect x="{f(w * 0.68 - 96 * s)}" y="{f(b - 90 * s)}" width="{f(54 * s)}" height="{f(26 * s)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    return "".join(o)
