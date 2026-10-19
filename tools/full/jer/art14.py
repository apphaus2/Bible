"""Drawings for Jeremiah chapter 14 (Jeremiah 40–42), on top of jer.art: the chains loosed at Ramah, Mizpah and Gedaliah, the
summer fruits gathered, the shut house at Mizpah (41:2–3 told in words), the fourscore men with their offerings, Asa's pit at
evening (no one drawn in it), the great waters in Gibeon, Geruth Chimham by Beth-lehem, and the remnant before the prophet."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jer.art import *
from jer.art import f, K2

GED_C = "#5A4A3A"
def chains_loosed(p, w, h, seed, age=3):
    """At Ramah, among the captives: the captain of the guard loosing the chains from the prophet's hands, the column of captives
    going on behind."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#6A5A6A", "#E8B890"), hills(w, h, h * 0.5, seed, "#7A6A5A", amp=10, step=90), ground(w, h, h * 0.58, "#A88A6A", dy=0)]
    for i in range(8):
        t = i / 7; x = w * (0.5 + 0.48 * t); y = h * (0.62 + 0.06 * t)
        o.append(mk.person(p, round(x), round(y), round(fit(y, y - h * 0.12), 3), body="#3A1E14", cloth=["#5A5A6A", "#6A5A4A", "#4A4A5A"][i % 3], sw=2, flip=True))
    s = fit(b, max(h * 0.4, b - 230))
    o.append(jer_fig(p, w * 0.26, b, s, age=age, up=[(-22, -158), (-40, -130), (-56, -116)]))
    o.append(man(p, w * 0.4, b, s, BABEL_C, flip=True, up=[(22, -158), (40, -130), (60, -116)], extra=A.headcloth(BABEL_C, cord="#E8B830") + A.BLACK_BEARD))
    o.append(JG2.fetters(w * 0.33, b - 6, min(0.8, s)))
    return "".join(o)

def summer_fruits(p, w, h, seed):
    """Gather ye wine and summer fruits and oil, and put them in your vessels: baskets of figs and grapes and jars of oil."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FC0E0", "#FFF0C8"), hills(w, h, h * 0.5, seed, "#6A9A4A", amp=12, step=80), ground(w, h, h * 0.6, "#B8B070", dy=0)]
    s = fit(b, max(h * 0.44, b - 210))
    o.append(man(p, w * 0.16, b, s, "#6A5A3A", up=[(-22, -158), (-26, -190), (-10, -206)]) + E4.basket(w * 0.16 - 6 * s, b - 196 * s, 0.6 * s))
    o.append(woman(p, w * 0.3, b, s * 0.94, "#8A5A6A"))
    o.append(jar(w * 0.5, b, s * 0.7, color="#C8A04A", stopper="#3A5A2A") + jar(w * 0.58, b, s * 0.6, color="#B8703A") + E4.basket(w * 0.7, b, s * 0.9)
             + N.grapes(w * 0.82, b - 60 * s, 0.4 * s, seed))
    return "".join(o)

def mizpah_harvest(p, w, h, seed):
    """Mizpah on its hill in the summer: the governor's town above, vines and baskets of summer fruits below, the people
    gathering, Gedaliah standing among them."""
    b = h * 0.96
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#6A9AC8", "#FFF0C8"), hills(w, h, h * 0.5, seed, "#6A8A4A", amp=12, step=80),
         J.city_hill(w * 0.64, h * 0.6, w * 0.34, h * 0.28, seed), ground(w, h, h * 0.62, "#B8B070", dy=0)]
    for k in range(6):
        x = w * (0.06 + k * 0.17)
        o.append(f'<path d="M{f(x)} {f(h * 0.8)} L {f(x)} {f(h * 0.66)}" stroke="#5A3A1E" stroke-width="3"></path>'
                 + "".join(f'<path d="M{f(x + dx)} {f(h * 0.68 + dy)} l 10 -4 l 2 9 Z" fill="#3E7A3A" stroke="#0D0D0F" stroke-width="1"></path>' for dx, dy in ((-14, 0), (6, -6), (-4, 8), (10, 10)))
                 + N.grapes(x + 4, h * 0.7, min(0.22, h / 3000), seed + k))
    s = fit(b, h * 0.74)
    o.append(man(p, w * 0.7, b, s, GED_C, extra=A.headcloth(GED_C) + A.BLACK_BEARD))
    o.append(man(p, w * 0.8, b, s * 0.96, "#6A5A3A", up=[(-22, -158), (-26, -190), (-10, -206)]) + E4.basket(w * 0.8 - 6 * s, b - 196 * s * 0.96, 0.55 * s))
    o.append(woman(p, w * 0.9, b, s * 0.92, "#8A5A6A") + jar(w * 0.6, b, s * 0.6, color="#C8A04A", stopper="#3A5A2A") + jar(w * 0.56, b, s * 0.5, color="#B8703A")
             + E4.basket(w * 0.5, b, s * 0.8))
    return "".join(o)

def jews_return(w, h):
    """All the Jews that were in Moab, and among the children of Ammon, and in Edom returned to Gedaliah unto Mizpah (a map)."""
    return near_east(w, h, ("MIZPAH", "MOAB", "AMMON", "EDOM"), hi=("MIZPAH",), arrows=[("MOAB", "MIZPAH"), ("AMMON", "MIZPAH"), ("EDOM", "MIZPAH")], lit="#FFD23F", box=(33.6, 37.6, 29.6, 32.6))

def eat_bread(p, w, h, seed):
    """There they did eat bread together in Mizpah: Gedaliah at table in his house with Ishmael and the ten men, lamplight."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), S3.cedar(w, h, h * 0.86), S3.table(w * 0.5, b, w * 0.6, min(1.2, h / 280))]
    from genesis.art4 import clay_lamp
    s = fit(b, max(h * 0.4, b - 220))
    o.append(man(p, w * 0.14, b, s, GED_C, extra=A.headcloth(GED_C) + A.BLACK_BEARD))
    for i in range(4):
        o.append(man(p, w * (0.66 + i * 0.09), b, s * (0.98 - i * 0.03), ["#3A1A2A", "#4A3A3A", "#3A3A4A", "#4A2A2A"][i], flip=True, extra=A.headcloth(["#3A1A2A", "#4A3A3A", "#3A3A4A", "#4A2A2A"][i])))
    o.append(clay_lamp(w * 0.5, b - 90 * min(1.2, h / 280), 0.9))
    return "".join(o)

def shut_house(w, h, seed):
    """Mizpah at night: Gedaliah's house with its door shut and the lamp gone out (41:2–3 told in words; no one drawn)."""
    o = [night(w, h, seed, "#120E1E"), J.city_hill(w * 0.5, h * 0.9, w * 0.5, h * 0.36, seed),
         f'<rect x="{f(w * 0.36)}" y="{f(h * 0.42)}" width="{f(w * 0.28)}" height="{f(h * 0.3)}" fill="#3A3240" stroke="#0D0D0F" stroke-width="2.4"></rect>'
         f'<rect x="{f(w * 0.46)}" y="{f(h * 0.54)}" width="{f(w * 0.08)}" height="{f(h * 0.18)}" fill="#0D0B10" stroke="#0D0D0F" stroke-width="2"></rect>'
         f'<rect x="{f(w * 0.4)}" y="{f(h * 0.48)}" width="{f(w * 0.04)}" height="{f(h * 0.05)}" fill="#0D0B10"></rect>',
         ground(w, h, h * 0.9, "#1A1620", dy=0)]
    return "".join(o)

def fourscore(p, w, h, seed):
    """Fourscore men from Shechem, from Shiloh, and from Samaria, their beards shaven and their clothes rent, with meal-offerings
    and frankincense in their hand, on the road to Mizpah."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8A8A9A", "#E8C8A0"), J.city_hill(w * 0.86, h * 0.56, w * 0.2, h * 0.2, seed), hills(w, h, h * 0.52, seed, "#7A7A5A", amp=10, step=90),
         ground(w, h, h * 0.6, "#B8A07A", dy=0)]
    for i in range(9):
        t = i / 8; x = w * (0.04 + 0.6 * t); y = h * (0.96 - 0.3 * t)
        s = fit(y, y - h * (0.36 - 0.2 * t))
        o.append(man(p, x, y, s, ["#5A5048", "#6A5A4A", "#4A4A4A"][i % 3], up=[(-22, -158), (-30, -150), (-20, -140)]))
        if i % 3 == 0: o.append(E4.basket(x + 30 * s, y - 120 * s, 0.4 * s))
    return "".join(o)

def asa_pit(w, h, seed):
    """The pit which Asa the king had made for fear of Baasha, at Mizpah, at evening: its dark mouth among the stones (41:7–9
    told in words only)."""
    o = [K2.sky(w, h, "#2A1A2A", "#A84A2A"), J.city_hill(w * 0.76, h * 0.5, w * 0.3, h * 0.24, seed), ground(w, h, h * 0.52, "#5A4A3E", dy=0)]
    cx, cy, rx, ry = w * 0.4, h * 0.78, w * 0.18, h * 0.1
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx * 1.2)}" ry="{f(ry * 1.3)}" fill="#7A7068" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="#0A0806" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    return "".join(o)

def stores(w, h, seed):
    """We have stores hidden in the field, of wheat, and of barley, and of oil, and of honey: jars and sacks in a hidden pit
    under the field."""
    o = [K2.sky(w, h, "#8FB0C8", "#F3E0B0"), ground(w, h, h * 0.4, "#A89060", dy=0),
         f'<rect x="{f(w * 0.2)}" y="{f(h * 0.5)}" width="{f(w * 0.6)}" height="{f(h * 0.46)}" fill="#3A2A1E" stroke="#0D0D0F" stroke-width="2.4"></rect>']
    s = min(1.0, h / 260)
    o.append(R1.sack(w * 0.3, h * 0.94, s) + R1.sack(w * 0.4, h * 0.94, s * 0.9) + jar(w * 0.54, h * 0.94, s * 0.9, color="#C8A04A", stopper="#3A5A2A")
             + jar(w * 0.64, h * 0.94, s * 0.8, color="#B8703A") + jar(w * 0.72, h * 0.94, s * 0.7, color="#E8B830", stopper="#8A5A1A"))
    o.append(R1.field(-10, w + 10, h * 0.44, h * 0.14, seed, rows=1))
    return "".join(o)

def captives_ammon(p, w, h, seed):
    """Ishmael carried away captive all the residue of the people that were in Mizpah, even the king's daughters, and departed to
    go over to the children of Ammon: a column going east toward the hills beyond the Jordan."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#6A5A6A", "#E8B890"), hills(w, h, h * 0.46, seed, "#6A5A5A", amp=14, step=70), ground(w, h, h * 0.54, "#A88A6A", dy=0)]
    for i in range(10):
        t = i / 9; x = w * (0.08 + 0.84 * t); y = h * (0.92 - 0.3 * t)
        s = fit(y, y - h * (0.3 - 0.18 * t))
        if i % 4 == 0: o.append(man(p, x, y, s, "#3A1A2A", extra=A.headcloth("#3A1A2A")))
        else: o.append(woman(p, x, y, s * 0.94, ["#7A3A5A", "#5A4A7A", "#8A5A3A"][i % 3]) if i % 2 else man(p, x, y, s * 0.94, "#6A5A4A"))
    return "".join(o)

def gibeon_waters(p, w, h, seed):
    """By the great waters that are in Gibeon: the pool cut in the rock below the city, Johanan's men come upon them, and the
    people turning back to them glad."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8FB0C8", "#F3E0B0"), J.city_hill(w * 0.5, h * 0.48, w * 0.3, h * 0.24, seed), ground(w, h, h * 0.5, "#B8A07A", dy=0),
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.66)}" rx="{f(w * 0.18)}" ry="{f(h * 0.08)}" fill="#2C7A9A" stroke="#0D0D0F" stroke-width="2.4"></ellipse>']
    s = fit(b, max(h * 0.44, b - 210))
    for i in range(3): o.append(warrior(p, w * (0.06 + i * 0.08), b, s, "#6A4A2A"))
    for i in range(3): o.append(woman(p, w * (0.66 + i * 0.09), b, s * 0.92, ["#7A3A5A", "#5A4A7A", "#8A5A3A"][i]) if i % 2 == 0 else man(p, w * (0.66 + i * 0.09), b, s * 0.92, "#6A5A4A"))
    return "".join(o)

def geruth(w, h):
    """They departed, and dwelt in Geruth Chimham, which is by Beth-lehem, to go to enter into Egypt (a map)."""
    return near_east(w, h, ("MIZPAH", "BETH-LEHEM", "EGYPT", "TAHPANHES"), hi=("BETH-LEHEM",), arrows=[("MIZPAH", "BETH-LEHEM"), ("BETH-LEHEM", "TAHPANHES")], lit="#FF8A6A",
                     box=(30.0, 37.0, 28.6, 33.4))

def remnant(p, w, h, seed, age=3):
    """All the captains of the forces and all the people, from the least even unto the greatest, came near to the prophet."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#8A8A9A", "#E8C8A0"), hills(w, h, h * 0.5, seed, "#7A7A5A", amp=10, step=90), ground(w, h, h * 0.58, "#B8A07A", dy=0)]
    s = fit(b, max(h * 0.4, b - 230))
    o.append(jer_fig(p, w * 0.18, b, s, age=age))
    o.append(man(p, w * 0.4, b, s, "#6A4A2A", flip=True, extra=A.headcloth("#6A4A2A") + A.BLACK_BEARD))
    o.append(crowd_at(p, w, h, seed, w * 0.5, w * 0.98, h * 0.64, b, 14, s * 0.55, s * 0.95, flip=True))
    return "".join(o)

def egypt_road(w, h, seed):
    """We will go into the land of Egypt, where we shall see no war: the road south into the desert, a palm far off, the sword
    and the famine following hard after (told in words)."""
    o = [K2.sky(w, h, "#E8A060", "#F8E0A8"), sun(w * 0.8, h * 0.3, min(w, h) * 0.06, color="#FFE680", op=0.35), hills(w, h, h * 0.62, seed, "#C8946A", amp=8, step=90),
         ground(w, h, h * 0.68, "#E8C890", dy=0), J1.palm(w * 0.7, h * 0.7, min(0.5, h / 600)),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.48)} {f(h * 0.68)} L {f(w * 0.52)} {f(h * 0.68)} L {f(w * 0.76)} {f(h + 10)} Z" fill="#D8B880" stroke="#0D0D0F" stroke-width="2"></path>']
    return "".join(o)
