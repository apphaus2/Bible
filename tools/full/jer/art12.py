"""Drawings for Jeremiah chapter 12 (Jeremiah 34–36), on top of jer.art: Lachish and Azekah, the servants set free and brought
back, the calf cut in twain, the Rechabites before the bowls of wine, Baruch writing the roll, the roll read in the chamber of
Gemariah, the princes, and the king in the winter-house cutting the roll and casting it into the brazier."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jer.art import *
from jer.art import f, K2
from jer.art10 import book_writing
from jer.art11 import call_night

LACHISH = ("JERUSALEM", "LACHISH", "AZEKAH")
def lachish_map(w, h):
    """The king of Babylon's army fighting against Jerusalem, Lachish and Azekah, the last fortified cities of Judah."""
    pos = {"JERUSALEM": (0.62, 0.3), "AZEKAH": (0.36, 0.4), "LACHISH": (0.28, 0.66)}
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.08)} -10 C {f(w * 0.1)} {f(h * 0.4)} {f(w * 0.06)} {f(h * 0.7)} {f(w * 0.04)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>')
    for nm, (x, y) in pos.items():
        o.append(f'<circle cx="{f(w * x)}" cy="{f(h * y)}" r="{f(min(w, h) * 0.07)}" fill="none" stroke="#D7261E" stroke-width="2" stroke-dasharray="5 4"></circle>')
        o.append(node(w * x, h * y, nm, "#FFD23F", r=6, dy=-min(w, h) * 0.08 - 4, size=10))
    o.append(label(w * 0.5, h * 0.92, "THESE ALONE REMAINED OF THE CITIES OF JUDAH AS FORTIFIED CITIES", "#8FD0E2", 9))
    o.append(route([(w * 0.9, h * 0.1), (w * 0.7, h * 0.24)], color="#D7261E") + route([(w * 0.86, h * 0.7), (w * 0.36, h * 0.66)], color="#D7261E"))
    return "".join(o)

def set_free(p, w, h, seed, back=False):
    """The servants and handmaids let go free, walking out of the gate (back=True: brought back into subjection, led in again
    by their masters)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8" if not back else "#6A5A6A", "#F3E0B0" if not back else "#C8A080"),
         wall(-10, w * 0.5, h * 0.3, h * 0.74, seed, towers=2, gate=w * 0.24, color="#C8B088"), ground(w, h, h * 0.74, "#C8B080", dy=0)]
    s = fit(b, max(h * 0.42, b - 210))
    for i in range(4):
        x = w * (0.42 + i * 0.13)
        fig = woman(p, x, b, s * 0.94, ["#8A7A5A", "#7A6A5A"][i % 2], flip=back) if i % 2 else man(p, x, b, s * 0.94, "#8A7A5A", flip=back)
        o.append(fig)
        if back: o.append(man(p, x + w * 0.06, b, s, ["#5A3A5A", "#3A4A6A"][i % 2], flip=True, up=[(22, -158), (50, -140), (70, -130)], extra=A.headcloth(["#5A3A5A", "#3A4A6A"][i % 2]) + A.BLACK_BEARD))
    return "".join(o)

def calf_parts(p, w, h, seed):
    """When they cut the calf in twain and passed between the parts thereof: the covenant pieces laid on stones, covered, in two
    rows, the princes passing between (no carcass shown)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#C8A880", "#F3E0B0"), temple_front(w * 0.5, h * 0.5, w * 0.4, seed), ground(w, h, h * 0.5, "#C8B080", dy=0)]
    for side in (-1, 1):
        x = w * (0.5 + side * 0.2)
        o.append(f'<rect x="{f(x - w * 0.08)}" y="{f(h * 0.8)}" width="{f(w * 0.16)}" height="{f(h * 0.08)}" fill="#8A8478" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<path d="M{f(x - w * 0.07)} {f(h * 0.8)} Q {f(x)} {f(h * 0.66)} {f(x + w * 0.07)} {f(h * 0.8)} Z" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2"></path>')
    s = fit(b, max(h * 0.52, b - 170))
    for i in range(3): o.append(man(p, w * 0.5, b - i * h * 0.08, s * (1 - i * 0.18), ["#6A2A3A", "#2A5A5A", "#5A3A6A"][i], extra=A.headcloth(["#6A2A3A", "#2A5A5A", "#5A3A6A"][i])))
    return "".join(o)

def rechabites(p, w, h, seed, refuse=True, age=2):
    """The Rechabites in a chamber of the house of Jehovah, bowls full of wine and cups set before them; they lift their hands
    and will not drink."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), S3.table(w * 0.56, b, w * 0.4, min(1.2, h / 300))]
    s = fit(b, max(h * 0.4, b - 230))
    for i in range(3):
        x = w * (0.42 + i * 0.12)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(b - 74 * min(1.2, h / 300))}" rx="{f(w * 0.035)}" ry="{f(h * 0.02)}" fill="#7A0A2A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>')
    o.append(jer_fig(p, w * 0.14, b, s, age=age, up=[(-22, -158), (-46, -150), (-70, -140)], flip=True))
    for i in range(3):
        o.append(man(p, w * (0.76 + i * 0.08), b, s * (0.96 - i * 0.02), "#7A6A4A", flip=True, up=[(22, -158), (32, -190), (20, -214)] if refuse else None,
                     extra=A.headcloth("#7A6A4A") + A.BLACK_BEARD))
    return "".join(o)

def tents_rechab(w, h, seed):
    """All your days ye shall dwell in tents: the black tents of the Rechabites in the wilderness, no field, no vineyard."""
    o = [K2.sky(w, h, "#E8A060", "#F3D8A0"), hills(w, h, h * 0.5, seed, "#B8846A", amp=14, step=80), ground(w, h, h * 0.62, "#D8B07A", dy=0)]
    for i in range(4): o.append(E4.tent(w * (0.08 + i * 0.24), h * (0.88 - (i % 2) * 0.06), w * 0.18, h * 0.2, color="#2A2018"))
    s = min(0.7, h / 360)
    for i in range(4): o.append(E.sheep(w * (0.2 + i * 0.16), h * 0.96, s))
    return "".join(o)

def baruch_writes(p, w, h, seed, age=2):
    """Baruch wrote from the mouth of Jeremiah all the words of Jehovah upon a roll of a book: the scribe seated with the roll on
    his knee, the prophet standing and speaking, a lamp between them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#4A3424"></rect>', glow(w * 0.5, h * 0.5, min(w, h) * 0.6, color="#FFC14D", op=0.3, uid=f"bw{seed}"),
         ground(w, h, h * 0.84, "#3A2A1E", dy=0)]
    s = fit(b, max(h * 0.36, b - 250))
    o.append(jer_fig(p, w * 0.26, b, s, age=age, up=[(-22, -158), (-46, -176), (-60, -170)], flip=True))
    o.append(E.kneel(w * 0.66, b, s * 0.9, color="#5A6A4A", skin="#9A6A4A", flip=True))
    o.append(f'<rect x="{f(w * 0.66 - 90 * s)}" y="{f(b - 90 * s)}" width="{f(50 * s)}" height="{f(24 * s)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    from genesis.art4 import clay_lamp
    o.append(clay_lamp(w * 0.46, b - 6, min(1.4, s * 1.6)))
    return "".join(o)

def reading_people(p, w, h, seed):
    """Then read Baruch in the book in the chamber of Gemariah, at the entry of the new gate, in the ears of all the people on the
    fast-day: the scribe at a window above the court, the roll open, the people below."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8", "#F3E0B0"), f'<rect x="{f(w * 0.06)}" y="{f(h * 0.1)}" width="{f(w * 0.5)}" height="{f(h * 0.56)}" fill="#D8C8A0" stroke="#0D0D0F" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.2)}" y="{f(h * 0.2)}" width="{f(w * 0.22)}" height="{f(h * 0.2)}" fill="#3A2214" stroke="#0D0D0F" stroke-width="2"></rect>',
         ground(w, h, h * 0.66, "#C8B080", dy=0)]
    s0 = fit(h * 0.4, h * 0.22)
    o.append(man(p, w * 0.31, h * 0.42, s0, "#5A6A4A", up=[(-22, -158), (-40, -150), (-60, -150)], extra=A.headcloth("#5A6A4A") + A.BLACK_BEARD))
    o.append(f'<rect x="{f(w * 0.31 - 74 * s0)}" y="{f(h * 0.42 - 166 * s0)}" width="{f(30 * s0)}" height="{f(30 * s0)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    s = fit(b, max(h * 0.5, b - 180))
    o.append(crowd_at(p, w, h, seed, w * 0.04, w * 0.96, h * 0.72, b, 16, s * 0.6, s * 0.95))
    return "".join(o)

def princes_chamber(p, w, h, seed):
    """The scribe's chamber in the king's house, all the princes sitting there; Baruch seated before them reading the roll."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84)]
    s = fit(b, max(h * 0.4, b - 220))
    for i in range(4): o.append(E.kneel(w * (0.56 + i * 0.11), b, s * 0.82, color=["#6A2A3A", "#2A5A5A", "#5A3A6A", "#6A5A2A"][i], skin="#9A6A4A", flip=True))
    o.append(E.kneel(w * 0.24, b, s * 0.82, color="#5A6A4A", skin="#9A6A4A"))
    o.append(f'<rect x="{f(w * 0.24 + 40 * s)}" y="{f(b - 96 * s)}" width="{f(44 * s)}" height="{f(24 * s)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    return "".join(o)

def winter_house(p, w, h, seed, burning=True):
    """The king sitting in the winter-house in the ninth month, a fire in the brazier burning before him; Jehudi reading; the
    king cutting the roll with the penknife and casting it into the fire, leaf by leaf."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.84), f'<rect x="{f(w * 0.06)}" y="{f(h * 0.14)}" width="{f(w * 0.12)}" height="{f(h * 0.26)}" fill="#1A2A4A" stroke="#0D0D0F" stroke-width="2"></rect>',
         mk.stars(10, w * 0.12, h * 0.26, seed).replace("<g", f'<g transform="translate({f(w * 0.06)} {f(h * 0.14)})"', 1)]
    bx, by = w * 0.5, b
    o.append(f'<path d="M{f(bx - 50)} {f(by)} L {f(bx - 40)} {f(by - 40)} L {f(bx + 40)} {f(by - 40)} L {f(bx + 50)} {f(by)} Z" fill="#B87333" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(bx)}" cy="{f(by - 40)}" rx="44" ry="8" fill="#5A2A1A" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    o.append(E.blaze(bx, by - 42, 70, h * 0.16, seed, n=5))
    o.append(glow(bx, by - 60, min(w, h) * 0.4, color="#FF8A2A", op=0.3, uid=f"wh{seed}"))
    if burning:
        for i in range(3):
            o.append(f'<rect x="{f(bx - 20 + i * 14)}" y="{f(by - h * (0.2 + i * 0.06))}" width="16" height="12" transform="rotate({-20 + i * 25} {f(bx - 12 + i * 14)} {f(by - h * (0.2 + i * 0.06))})" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.2"></rect>')
    s = fit(b, max(h * 0.36, b - 240))
    o.append(S3.throne(w * 0.78, b, min(1.0, s * 1.1)))
    o.append(king_fig(p, w * 0.78, b - 10, s, flip=True, cloth="#1F3A7A", up=[(22, -158), (50, -140), (74, -150)]))
    o.append(man(p, w * 0.24, b, s, "#6A5A3A", up=[(-22, -158), (-40, -150), (-60, -150)], extra=A.headcloth("#6A5A3A") + A.BLACK_BEARD))
    o.append(f'<rect x="{f(w * 0.24 - 76 * s)}" y="{f(b - 166 * s)}" width="{f(32 * s)}" height="{f(30 * s)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    return "".join(o)

def hidden(w, h, seed):
    """But Jehovah hid them: a cleft among the rocks at night, empty, the city lights far off."""
    o = [night(w, h, seed, "#0F0E2A"), mk.stars(40, w, h * 0.5, seed + 1), crag(-10, w * 0.5, h + 10, h * 0.3, color="#2A2A3A", dark="#1A1A24"),
         crag(w * 0.46, w + 10, h + 10, h * 0.36, color="#2A2A3A", dark="#1A1A24")]
    for i in range(6): o.append(f'<circle cx="{f(w * (0.4 + i * 0.03))}" cy="{f(h * 0.66)}" r="2" fill="#FFC14D"></circle>')
    return "".join(o)

def cast_out(w, h, seed):
    """His dead body shall be cast out in the day to the heat, and in the night to the frost: a bare slope outside the wall, half
    under the sun and half under frost (no body drawn)."""
    o = [f'<rect x="-10" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="#E8A060"></rect>', f'<rect x="{f(w * 0.5)}" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="#14183A"></rect>',
         sun(w * 0.24, h * 0.24, min(w, h) * 0.06, color="#FFE680", op=0.4), J.moon(w * 0.76, h * 0.22, min(w, h) * 0.05), mk.stars(20, w * 0.5, h * 0.4, seed).replace("<g", f'<g transform="translate({f(w * 0.5)} 0)"', 1),
         wall(-10, w + 10, h * 0.44, h * 0.66, seed, towers=4, color="#B8A07A"),
         f'<path d="M-10 {f(h * 0.66)} L {f(w + 10)} {f(h * 0.66)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<rect x="{f(w * 0.5)}" y="{f(h * 0.66)}" width="{f(w * 0.5 + 10)}" height="{f(h * 0.4)}" fill="#C8D8E8" opacity="0.6"></rect>']
    return "".join(o)
