"""Drawings for the Lamentations volume, on top of Jeremiah's (jer.art and its chapter modules): the desolate city, restrained —
the city sitting solitary as a widow, the ways of Zion mourning, the gates sunk into the ground, the broken wall, the elders in
the dust, ashes, the dark dungeon, the dawn that is new every morning, the foxes upon Mount Zion. No one is drawn suffering."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from jer.art import *
from jer.art import f, K2
from jer.art5 import crowns_down, circling, dark_mountains, noon_dark
from jer.art7 import passers, beyond_gates, cursed_day
from jer.art8 import grape_tread, cup
from jer.art9 import yoke_iron
from jer.art10 import rachel
from jer.art13 import cells, dungeon
from jer.art14 import asa_pit
from jer.art16 import eagle
from jer.art17 import ostriches

def widow_city(p, w, h, seed, dusk=True, x=0.2):
    """How doth the city sit solitary, that was full of people! She is become as a widow: a woman in black seated alone on the
    ground before the broken gate of the empty city at dusk."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#2A2040" if dusk else "#6A6A7A", "#C88070" if dusk else "#C8C0B0"),
         jerusalem(w * 0.3, w + 10, h * 0.7, h * 0.22, seed, broken=True, color="#A89878"), ground(w, h, h * 0.7, "#6A5A4A", dy=0)]
    s = fit(b, max(h * 0.5, b - 200))
    o.append(E.kneel(w * x, b, s, color="#1E1A22", skin="#9A7A6A", flip=x > 0.5))
    return "".join(o)

def ways_mourn(w, h, seed):
    """The ways of Zion do mourn, because none come to the solemn assembly; all her gates are desolate: the road up to the gate,
    grass in its ruts, no traveller."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#6A6A7A", "#D8C8B0"), wall(-10, w + 10, h * 0.24, h * 0.56, seed, towers=4, gate=w * 0.5, color="#A89878"),
         ground(w, h, h * 0.56, "#8A8A5A", dy=0),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} L {f(w * 0.47)} {f(h * 0.56)} L {f(w * 0.53)} {f(h * 0.56)} L {f(w * 0.7)} {f(h + 10)} Z" fill="#B8A07A" stroke="#0D0D0F" stroke-width="2"></path>']
    o.append("".join(f'<path d="M{f(x)} {f(y)} l -2 -8 M{f(x + 3)} {f(y)} l 2 -7" stroke="#5A6A3A" stroke-width="1.6"></path>'
                     for x, y in ((r.uniform(w * 0.36, w * 0.64), r.uniform(h * 0.62, h)) for _ in range(40))))
    return "".join(o)

def gates_sunk(w, h, seed):
    """Her gates are sunk into the ground; he hath destroyed and broken her bars: a great gateway half buried in rubble and earth,
    its leaves fallen, the bar snapped."""
    o = [K2.sky(w, h, "#5A4A5A", "#C8A080"), wall(-10, w + 10, h * 0.34, h * 0.86, seed, towers=2, color="#A89878")]
    gx, gw = w * 0.5, w * 0.3
    o.append(f'<path d="M{f(gx - gw / 2)} {f(h * 0.86)} L {f(gx - gw / 2)} {f(h * 0.5)} Q {f(gx)} {f(h * 0.3)} {f(gx + gw / 2)} {f(h * 0.5)} L {f(gx + gw / 2)} {f(h * 0.86)} Z" fill="#1A1210" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(f'<g transform="rotate(-14 {f(gx - gw * 0.2)} {f(h * 0.8)})"><rect x="{f(gx - gw * 0.46)}" y="{f(h * 0.56)}" width="{f(gw * 0.44)}" height="{f(h * 0.3)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></rect></g>'
             f'<path d="M{f(gx - gw * 0.4)} {f(h * 0.7)} L {f(gx - gw * 0.05)} {f(h * 0.66)} M{f(gx + gw * 0.05)} {f(h * 0.7)} L {f(gx + gw * 0.42)} {f(h * 0.62)}" stroke="#3A3A3A" stroke-width="7" stroke-linecap="round"></path>')
    o.append(f'<path d="M-10 {f(h * 0.78)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.7)} {f(h * 0.72)} {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A7458" stroke="#0D0D0F" stroke-width="2.4"></path>')
    o.append(J.collapse(w * 0.06, w * 0.34, h * 0.9, h * 0.16, seed, color="#A89878") + J.collapse(w * 0.66, w * 0.94, h * 0.92, h * 0.14, seed + 1, color="#A89878"))
    return "".join(o)

def elders_dust(p, w, h, seed):
    """The elders of the daughter of Zion sit upon the ground, they keep silence; they have cast up dust upon their heads, girded
    with sackcloth; the virgins hang down their heads."""
    b = h * 0.94
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#4A4048", "#A8988A"), wall(-10, w + 10, h * 0.32, h * 0.66, seed, towers=3, color="#9A8A7A"), ground(w, h, h * 0.66, "#7A6E60", dy=0)]
    s = fit(b, max(h * 0.5, b - 180))
    for i in range(5):
        x = w * (0.1 + i * 0.2)
        o.append(E.kneel(x, b, s * (0.9 + (i % 2) * 0.1), color=["#3A3434", "#4A3E34", "#2E2A2C"][i % 3], skin="#8A7064", flip=i % 2 == 1))
        o.append("".join(f'<circle cx="{f(x + r.uniform(-16, 16) * s)}" cy="{f(b - r.uniform(110, 170) * s)}" r="{f(r.uniform(1.5, 3))}" fill="#B8A890" opacity="0.8"></circle>' for _ in range(8)))
    return "".join(o)

def breach_sea(w, h, seed):
    """Thy breach is great like the sea: who can heal thee?: a wall broken wide open, and beyond it the sea's horizon."""
    o = [K2.sky(w, h, "#4A5A7A", "#C8C8C8"), f'<rect x="-10" y="{f(h * 0.4)}" width="{f(w + 20)}" height="{f(h * 0.3)}" fill="#1F5A7A"></rect>',
         wall(-10, w + 10, h * 0.3, h * 0.8, seed, towers=2, color="#A89878", breach=(w * 0.16, w * 0.84)), ground(w, h, h * 0.8, "#6A5E50", dy=0)]
    return "".join(o)

def cloud_city(w, h, seed):
    """How hath the Lord covered the daughter of Zion with a cloud in his anger!: a black cloud low over the city."""
    o = [K2.sky(w, h, "#1A1A24", "#4A4A54"), jerusalem(w * 0.1, w * 0.9, h * 0.86, h * 0.4, seed, color="#8A8070"), ground(w, h, h * 0.86, "#2A2628", dy=0)]
    for i in range(7):
        o.append(f'<ellipse cx="{f(w * (0.06 + i * 0.15))}" cy="{f(h * (0.22 + (i % 2) * 0.06))}" rx="{f(w * 0.16)}" ry="{f(h * 0.12)}" fill="#14141C" opacity="0.92"></ellipse>')
    return "".join(o)

def booth_broken(w, h, seed):
    """He hath violently taken away his tabernacle, as if it were of a garden: a garden booth torn down, its poles fallen among
    the vines."""
    o = [vine(w, h, seed, wild=True)]
    bx = w * 0.5
    o.append(f'<path d="M{f(bx - w * 0.14)} {f(h * 0.94)} L {f(bx - w * 0.04)} {f(h * 0.6)} M{f(bx + w * 0.16)} {f(h * 0.94)} L {f(bx + w * 0.02)} {f(h * 0.7)} M{f(bx - w * 0.2)} {f(h * 0.86)} L {f(bx + w * 0.22)} {f(h * 0.9)}" stroke="#6A4A2A" stroke-width="6" stroke-linecap="round"></path>'
             f'<path d="M{f(bx - w * 0.12)} {f(h * 0.88)} q {f(w * 0.1)} {f(-h * 0.1)} {f(w * 0.24)} 0" stroke="#7A8A3A" stroke-width="10" fill="none"></path>')
    return "".join(o)

def altar_alone(w, h, seed):
    """The Lord hath cast off his altar, he hath abhorred his sanctuary: the altar standing cold among broken walls."""
    o = [K2.sky(w, h, "#3A3040", "#B8908A"), J.collapse(-10, w * 0.36, h * 0.84, h * 0.26, seed, color="#C8B898"), J.collapse(w * 0.66, w + 10, h * 0.86, h * 0.22, seed + 1, color="#C8B898"),
         ground(w, h, h * 0.84, "#5A5048", dy=0), horned_altar(w * 0.5, h * 0.9, min(1.0, h / 220))]
    return "".join(o)

def line_stretched(w, h, seed):
    """He hath stretched out the line, he hath not withdrawn his hand from destroying; the rampart and wall lament: a measuring
    line pegged along the foot of a broken wall."""
    o = [K2.sky(w, h, "#5A4A5A", "#C8A080"), wall(-10, w + 10, h * 0.3, h * 0.74, seed, towers=3, color="#A89878", breach=(w * 0.52, w * 0.74)), ground(w, h, h * 0.74, "#7A6A54", dy=0)]
    o.append(f'<path d="M{f(w * 0.04)} {f(h * 0.86)} L {f(w * 0.96)} {f(h * 0.82)}" stroke="#E8D8B0" stroke-width="2" stroke-dasharray="2 4"></path>')
    for x in (0.04, 0.96): o.append(f'<path d="M{f(w * x)} {f(h * (0.86 if x < 0.5 else 0.82))} l 0 -20" stroke="#5A3A1E" stroke-width="4"></path>')
    return "".join(o)

def empty_streets(w, h, seed, night_=False):
    """The streets of the city: shut doors, no one in them (the swooning children and the slain told in words only)."""
    return empty_city(w, h, seed, dusk=True)

def cold_hearth(w, h, seed):
    """Where is grain and wine?: a cold hearth in an empty house, an empty bowl and a dry jar."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A2420"></rect>', ground(w, h, h * 0.8, "#3A3028", dy=0),
         f'<path d="M{f(w * 0.36)} {f(h * 0.84)} L {f(w * 0.4)} {f(h * 0.64)} Q {f(w * 0.5)} {f(h * 0.54)} {f(w * 0.6)} {f(h * 0.64)} L {f(w * 0.64)} {f(h * 0.84)} Z" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="2.4"></path>'
         f'<path d="M{f(w * 0.44)} {f(h * 0.84)} L {f(w * 0.44)} {f(h * 0.72)} Q {f(w * 0.5)} {f(h * 0.66)} {f(w * 0.56)} {f(h * 0.72)} L {f(w * 0.56)} {f(h * 0.84)} Z" fill="#1A1410" stroke="#0D0D0F" stroke-width="2"></path>',
         J1.bowl(w * 0.24, h * 0.86, w * 0.12, full=False), jar(w * 0.78, h * 0.88, min(0.9, h / 260), color="#8A5A3A", stopper=None)]
    return "".join(o)

def passers_by(p, w, h, seed):
    return passers(p, w, h, seed)

def dark_places(w, h, seed):
    """He hath made me to dwell in dark places, as those that have been long dead; he hath walled me about, he hath made my chain
    heavy: a dark vault, a chain lying on the floor, one thin light from above."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#0E0C10"></rect>',
         f'<path d="M{f(w * 0.48)} -10 L {f(w * 0.52)} -10 L {f(w * 0.58)} {f(h * 0.86)} L {f(w * 0.42)} {f(h * 0.86)} Z" fill="#C8C0B0" opacity="0.12"></path>',
         ground(w, h, h * 0.86, "#1A1618", dy=0), JG2.fetters(w * 0.5, h * 0.9, min(1.4, h / 200))]
    return "".join(o)

def hewn_wall(w, h, seed):
    """He hath walled up my ways with hewn stone; he hath made my paths crooked: a path running into a wall of squared stones."""
    o = [K2.sky(w, h, "#5A5A6A", "#C8C0B0"), ground(w, h, h * 0.5, "#9A8A6A", dy=0),
         f'<path d="M{f(w * 0.2)} {f(h + 10)} C {f(w * 0.5)} {f(h * 0.86)} {f(w * 0.2)} {f(h * 0.7)} {f(w * 0.46)} {f(h * 0.6)}" stroke="#D8C8A0" stroke-width="{f(w * 0.05)}" fill="none"></path>']
    for r_ in range(6):
        for c in range(9):
            x = w * (0.04 + c * 0.11 + (r_ % 2) * 0.05); y = h * (0.26 + r_ * 0.06)
            o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.1)}" height="{f(h * 0.058)}" fill="#B8A890" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    return "".join(o)

def bear_lion(w, h, seed):
    """As a bear lying in wait, as a lion in secret places: a bear and a lion half hidden in the thicket."""
    o = [K2.sky(w, h, "#3A3A2A", "#A8A070"), ground(w, h, h * 0.7, "#5A5A3A", dy=0), thicket(-10, w + 10, h * 0.8, h * 0.6, seed, color="#2A4A2A")]
    bx, by, s = w * 0.3, h * 0.92, min(1.2, h / 220)
    o.append(f'<g transform="translate({f(bx)} {f(by)}) scale({f(s)})"><path d="M-60 0 L -56 -50 Q -40 -80 0 -78 Q 34 -80 46 -60 L 64 -66 Q 76 -60 72 -46 L 58 -40 L 54 0 L 40 0 L 36 -30 L -30 -30 L -36 0 Z" fill="#4A3020" stroke="#0D0D0F" stroke-width="2.4"></path>'
             '<circle cx="58" cy="-70" r="6" fill="#4A3020" stroke="#0D0D0F" stroke-width="1.6"></circle><circle cx="66" cy="-54" r="2" fill="#0D0D0F"></circle></g>')
    o.append(JG2.lion(w * 0.72, h * 0.92, min(1.0, h / 260), flip=True, roar=False))
    return "".join(o)

def mark_arrow(w, h, seed):
    """He hath bent his bow, and set me as a mark for the arrow: a target post with arrows standing in it (no archer drawn)."""
    o = [K2.sky(w, h, "#5A4A4A", "#C8A080"), ground(w, h, h * 0.78, "#8A7A5A", dy=0)]
    cx, cy, R = w * 0.5, h * 0.5, min(w, h) * 0.24
    o.append(f'<rect x="{f(cx - 6)}" y="{f(cy)}" width="12" height="{f(h * 0.4)}" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="2"></rect>')
    for k, c in enumerate(("#E8D8B0", "#B5121B", "#E8D8B0", "#B5121B")):
        o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R * (1 - k * 0.24))}" fill="{c}" stroke="#0D0D0F" stroke-width="2"></circle>')
    for dx, dy in ((0.02, -0.04), (-0.06, 0.03), (0.07, 0.05)):
        x, y = cx + w * dx, cy + h * dy
        o.append(f'<path d="M{f(x)} {f(y)} l {f(-w * 0.12)} {f(-h * 0.08)}" stroke="#4A2A1A" stroke-width="3"></path>'
                 f'<path d="M{f(x - w * 0.12)} {f(y - h * 0.08)} l -8 -6 m 8 6 l -10 0" stroke="#E8E2D6" stroke-width="3"></path>')
    return "".join(o)

def new_morning(w, h, seed):
    """They are new every morning; great is thy faithfulness: dawn rising over the broken city, light on the hills."""
    o = [K2.sky(w, h, "#2A2A6A", "#FFD890"), sun(w * 0.5, h * 0.66, min(w, h) * 0.08, color="#FFE680", op=0.45), V.rays(w * 0.5, h * 0.66, 30, 20, max(w, h), color="#FFF4C2", op=0.2),
         jerusalem(w * 0.04, w * 0.96, h * 0.92, h * 0.6, seed, broken=True, color="#C8B090"), ground(w, h, h * 0.92, "#5A4A3A", dy=0)]
    return "".join(o)

def sit_alone(p, w, h, seed):
    """Let him sit alone and keep silence; let him put his mouth in the dust, if so be there may be hope: a man bowed to the
    ground alone on a hillside at evening."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#3A3A6A", "#E8B880"), hills(w, h, h * 0.6, seed, "#5A5A4A", amp=12, step=80), ground(w, h, h * 0.72, "#8A7A5A", dy=0)]
    s = fit(b, max(h * 0.5, b - 200))
    o.append(E.kneel(w * 0.5, b, s, color="#3A3434", skin="#9A7A6A"))
    return "".join(o)

def prisoners(w, h, seed):
    """To crush under foot all the prisoners of the earth, to turn aside the right of a man: fetters lying by a barred door."""
    return cells(w, h, seed) + JG2.fetters(w * 0.5, h * 0.92, min(1.0, h / 260))

def lift_hands(p, w, h, seed):
    """Let us lift up our heart with our hands unto God in the heavens: a company standing with hands raised toward the sky at
    evening, the broken city behind."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#2A2A5A", "#E8A880"), jerusalem(w * 0.5, w + 10, h * 0.66, h * 0.3, seed, broken=True, color="#A89878"), ground(w, h, h * 0.66, "#6A5E50", dy=0)]
    s = fit(b, max(h * 0.44, b - 210))
    for i in range(4):
        x = w * (0.08 + i * 0.12)
        up = [(-22, -158), (-36, -192), (-40, -228)]
        o.append(man(p, x, b, s * (0.94 + (i % 2) * 0.06), ["#3A3434", "#4A3E34", "#3A3A44", "#4A4038"][i], up=up) if i % 2 == 0 else woman(p, x, b, s * 0.92, ["#3A3434", "#4A3E34", "#3A3A44", "#4A4038"][i], up=up))
    return "".join(o)

def thick_cloud(w, h, seed):
    """Thou hast covered thyself with a cloud, so that no prayer can pass through: a heavy wall of cloud over the land."""
    o = [K2.sky(w, h, "#1A1A24", "#3A3A44"), hills(w, h, h * 0.84, seed, "#2A2A2E", amp=8, step=90)]
    for r_ in range(3):
        for i in range(6):
            o.append(f'<ellipse cx="{f(w * (0.04 + i * 0.19 + r_ * 0.05))}" cy="{f(h * (0.2 + r_ * 0.14))}" rx="{f(w * 0.15)}" ry="{f(h * 0.1)}" fill="{["#2A2A34", "#34343E", "#3E3E48"][r_]}"></ellipse>')
    return "".join(o)

def tears(w, h, seed):
    """Mine eye runneth down with streams of water, without any intermission, till Jehovah look down: rain falling on the empty
    city at night."""
    r = random.Random(seed)
    o = [night(w, h, seed, "#14122A"), jerusalem(w * 0.06, w * 0.94, h * 0.9, h * 0.44, seed, broken=True, color="#6A6470"), ground(w, h, h * 0.9, "#1E1A22", dy=0)]
    o.append("".join(f'<path d="M{f(r.uniform(0, w))} {f(r.uniform(0, h * 0.86))} l -4 16" stroke="#8AA8C8" stroke-width="1.6" opacity="0.7"></path>' for _ in range(80)))
    return "".join(o)

def bird_chased(w, h, seed):
    """They have chased me sore like a bird, they that are mine enemies without cause: a small bird flying low before a cast net."""
    o = [K2.sky(w, h, "#8A8AA0", "#E8D0B0"), ground(w, h, h * 0.8, "#9A8A6A", dy=0),
         f'<path d="M{f(w * 0.56)} {f(h * 0.82)} Q {f(w * 0.74)} {f(h * 0.3)} {f(w * 0.96)} {f(h * 0.82)}" fill="none" stroke="#5A4A3A" stroke-width="3"></path>']
    for k in range(8):
        o.append(f'<path d="M{f(w * (0.56 + k * 0.05))} {f(h * 0.82)} L {f(w * 0.74)} {f(h * 0.4)}" stroke="#7A6A5A" stroke-width="1.4"></path>')
    o.append(bird(w * 0.3, h * 0.46, 2.4) + speed_lines(w, h, seed, 0.4, 0.52, color="#5A5A6A", n=6))
    return "".join(o)

def pit_stone(w, h, seed):
    """They have cut off my life in the dungeon, and have cast a stone upon me; waters flowed over my head: the mouth of a pit with a
    great stone across it, water seeping (no one drawn)."""
    o = [K2.sky(w, h, "#2A2A3A", "#7A7A8A"), ground(w, h, h * 0.44, "#5A5048", dy=0)]
    cx, cy, rx, ry = w * 0.5, h * 0.72, w * 0.22, h * 0.12
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx * 1.2)}" ry="{f(ry * 1.3)}" fill="#7A7068" stroke="#0D0D0F" stroke-width="2.4"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" fill="#0A0806" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<path d="M{f(cx - rx * 0.8)} {f(cy - ry * 0.4)} L {f(cx + rx * 0.6)} {f(cy - ry * 0.9)} L {f(cx + rx * 0.9)} {f(cy + ry * 0.2)} L {f(cx - rx * 0.5)} {f(cy + ry * 0.7)} Z" fill="#9A9088" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(cx + rx * 0.7)} {f(cy + ry * 0.6)} q 10 16 2 30" stroke="#5A8AA8" stroke-width="3" fill="none"></path>')
    return "".join(o)

def dim_gold(w, h, seed):
    """How is the gold become dim! The stones of the sanctuary are poured out at the head of every street: carved stones of the
    house, their gold dulled, lying at a street corner."""
    o = [empty_city(w, h, seed, dusk=True)]
    s = min(1.0, h / 260)
    for i, (x, rot) in enumerate(((0.3, -20), (0.42, 10), (0.56, -6), (0.66, 24))):
        o.append(f'<g transform="rotate({rot} {f(w * x)} {f(h * 0.9)})"><rect x="{f(w * x - 30 * s)}" y="{f(h * 0.9 - 24 * s)}" width="{f(60 * s)}" height="{f(30 * s)}" fill="#C8B898" stroke="#0D0D0F" stroke-width="2"></rect>'
                 f'<rect x="{f(w * x - 24 * s)}" y="{f(h * 0.9 - 20 * s)}" width="{f(48 * s)}" height="{f(6 * s)}" fill="#8A7A4A"></rect></g>')
    return "".join(o)

def pitchers_row(w, h, seed):
    """The precious sons of Zion, comparable to fine gold, how are they esteemed as earthen pitchers, the work of the potter!"""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2A22"></rect>', ground(w, h, h * 0.86, "#2A1E18", dy=0)]
    s = min(1.2, h / 220)
    for i in range(5): o.append(jar(w * (0.14 + i * 0.18), h * 0.9, s, color=["#B8703A", "#A8603A", "#C8804A"][i % 3], stopper=None, handles=i % 2 == 0))
    return "".join(o)

def wanderers(p, w, h, seed):
    """They wander as blind men in the streets; Depart ye, Unclean! depart, depart: figures walking away down the road out of the
    city, apart from one another."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A4A5A", "#C8A080"), wall(w * 0.6, w + 10, h * 0.3, h * 0.66, seed, towers=2, gate=w * 0.8, color="#A89878"),
         ground(w, h, h * 0.66, "#8A7A5A", dy=0)]
    for i in range(4):
        t = i / 3; x = w * (0.66 - 0.56 * t); y = h * (0.7 + 0.24 * t)
        s = fit(y, y - h * (0.12 + 0.22 * t))
        o.append(man(p, x, y, s, ["#4A4038", "#3A3434", "#5A4A3A", "#3A3A44"][i], flip=True))
    return "".join(o)

def empty_pit(w, h, seed):
    """The anointed of Jehovah was taken in their pits: a covered pit in the wilderness, its brush cover broken through."""
    o = [K2.sky(w, h, "#E8A060", "#F8E0A8"), hills(w, h, h * 0.5, seed, "#B8846A", amp=14, step=80), ground(w, h, h * 0.6, "#D8B07A", dy=0),
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.8)}" rx="{f(w * 0.16)}" ry="{f(h * 0.08)}" fill="#1A1210" stroke="#0D0D0F" stroke-width="2"></ellipse>']
    for k in range(7):
        o.append(f'<path d="M{f(w * (0.36 + k * 0.04))} {f(h * 0.76)} l {f(w * 0.03)} {f(h * 0.06)}" stroke="#6A4A2A" stroke-width="3"></path>')
    return "".join(o)

def water_money(w, h, seed):
    """We have drunken our water for money; our wood is sold unto us: a water jar and a bundle of sticks beside pieces of silver."""
    o = [K2.sky(w, h, "#8A7A6A", "#E8D0B0"), ground(w, h, h * 0.7, "#9A8A6A", dy=0), jar(w * 0.3, h * 0.92, min(1.2, h / 220), color="#8A5A3A"),
         JG2.silver(w * 0.5, h * 0.9, 9, seed, spread=w * 0.05)]
    for k in range(6):
        o.append(f'<path d="M{f(w * 0.64)} {f(h * (0.86 - k * 0.012))} L {f(w * 0.9)} {f(h * (0.84 - k * 0.012))}" stroke="#6A4A2A" stroke-width="5" stroke-linecap="round"></path>')
    o.append(f'<path d="M{f(w * 0.76)} {f(h * 0.78)} L {f(w * 0.76)} {f(h * 0.88)}" stroke="#C8A878" stroke-width="3"></path>')
    return "".join(o)

def mill_wood(w, h, seed):
    """The young men bare the mill; and the children stumbled under the wood: a heavy millstone and a load of wood left on the
    road."""
    o = [K2.sky(w, h, "#5A5A6A", "#C8B8A0"), ground(w, h, h * 0.66, "#8A7A5A", dy=0), JG2.mill(w * 0.32, h * 0.92, min(1.2, h / 220))]
    for k in range(5):
        o.append(f'<path d="M{f(w * 0.6)} {f(h * (0.9 - k * 0.02))} L {f(w * 0.88)} {f(h * (0.88 - k * 0.02))}" stroke="#6A4A2A" stroke-width="6" stroke-linecap="round"></path>')
    return "".join(o)

def gate_empty(w, h, seed):
    """The elders have ceased from the gate, the young men from their music: the stone bench of the gate empty, a harp left there."""
    o = [K2.sky(w, h, "#6A6A7A", "#D8C8B0"), S4b.gatehouse(w * 0.5, h * 0.84, w * 0.8, h * 0.72), ground(w, h, h * 0.84, "#8A7A5A", dy=0),
         f'<rect x="{f(w * 0.1)}" y="{f(h * 0.78)}" width="{f(w * 0.22)}" height="{f(h * 0.06)}" fill="#B8A890" stroke="#0D0D0F" stroke-width="2"></rect>',
         S2.harp(w * 0.76, h * 0.86, min(0.7, h / 360), rot=-60)]
    return "".join(o)

def crown_fallen(w, h, seed):
    """The crown is fallen from our head: a gold crown lying in the dust."""
    o = [K2.sky(w, h, "#3A3040", "#A8908A"), ground(w, h, h * 0.66, "#6A5E50", dy=0), S2.crown(w * 0.5, h * 0.88, min(2.4, h / 100), rot=-24)]
    return "".join(o)

def foxes_zion(w, h, seed):
    """For the mountain of Zion, which is desolate: the foxes walk upon it."""
    o = [K2.sky(w, h, "#3A3A6A", "#E8A880"),
         f'<path d="M-10 {f(h + 10)} C {f(w * 0.2)} {f(h * 0.5)} {f(w * 0.7)} {f(h * 0.42)} {f(w + 10)} {f(h * 0.7)} L {f(w + 10)} {f(h + 10)} Z" fill="#7A6A4A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         J.collapse(w * 0.3, w * 0.7, h * 0.58, h * 0.18, seed, color="#A89878"), thicket(w * 0.1, w * 0.3, h * 0.7, h * 0.2, seed, color="#4A5A3A")]
    s = min(1.0, h / 300)
    o.append(JG2.fox(w * 0.36, h * 0.8, s, brand=False) + JG2.fox(w * 0.66, h * 0.76, s * 0.9, flip=True, brand=False))
    return "".join(o)

def throne_ever(w, h, seed):
    """Thou, O Jehovah, abidest for ever; thy throne is from generation to generation: a high night sky full of stars over the
    ruins, a light above (no figure)."""
    return (night(w, h, seed, "#0F0E2A") + mk.stars(120, w, h * 0.7, seed + 1) + glow(w * 0.5, h * 0.18, min(w, h) * 0.5, color="#FFF4C2", op=0.3, uid=f"te{seed}")
            + jerusalem(w * 0.1, w * 0.9, h * 0.96, h * 0.7, seed, broken=True, color="#5A5460") + ground(w, h, h * 0.96, "#14121A", dy=0))
