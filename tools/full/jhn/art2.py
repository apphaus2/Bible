"""Drawings for John 3–4. Nicodemus by night on a Jerusalem roof under the lamp; the wind blowing through the dark olive
trees (no one drawn); the serpent of brass lifted up on its standard in the wilderness, the camp looking up to it; the
world under the dawn; John at Ænon by the water; the friend of the bridegroom at the door as the bridegroom comes with his
lamps. Samaria: the road between the mountains; Jacob's well at Sychar at the sixth hour, Jesus sitting by it wearied;
the woman of Samaria with her waterpot; the disciples come back from the city; the waterpot left by the well and the
woman gone running to the city; the Samaritans coming out over the fields white unto harvest; the reapers. Cana again: the
nobleman of Capernaum before Jesus; the road down to the lake, his servants running up to meet him; the house at
Capernaum, the son standing whole among them. Built on jhn.art."""
from jhn.art import *
from jhn.art import f, INK, HEB, TWELVE, P, coals, stone_pot, courtyard
import random, math
import numbers1 as N
from ecc.art import wind_lines

NICODEMUS_C, NICODEMUS_HEAD = "#22356A", "#22356A"
SAMARITAN_C, SAMARITAN_VEIL = "#7A4A6A", "#5A2E5E"
NOBLEMAN_C = "#4A2A6A"

def nicodemus_fig(p, x, y, s, flip=False, up=None):
    """Nicodemus at a distance: a deep-blue robe and headcloth with a gold cord, a grey beard (a ruler of the Jews)."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#C98E66", cloth=NICODEMUS_C, kind="Robe", sw=3, flip=flip, up=up,
                     extra=A.headcloth(NICODEMUS_HEAD, cord="#E8B830") + GREY_BEARD)

def nicodemus_seated(x, y, s, flip=False):
    return seated(x, y, s, NICODEMUS_C, head=NICODEMUS_HEAD, beard="#9A948A", flip=flip, band=True)

POT = '<path d="M-14 -214 C -6 -214 -2 -206 -6 -200 L -10 -196 C -2 -190 -2 -176 -12 -172 L -34 -172 C -44 -176 -44 -190 -36 -196 L -40 -200 C -44 -206 -40 -214 -32 -214 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.8"></path>'
def samaritan_fig(p, x, y, s, flip=False, up=None, pot=True):
    """The woman of Samaria: a mauve robe and a plum veil; pot=True her waterpot on her shoulder, steadied with her hand."""
    up = up if up is not None else ([(-22, -158), (-30, -176), (-24, -196)] if pot else None)
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth=SAMARITAN_C, woman=True, sw=3, flip=flip, up=up,
                     extra=veil(SAMARITAN_VEIL) + (POT if pot else ""))

def nobleman_fig(p, x, y, s, flip=False, up=None):
    """The nobleman of Capernaum: a purple robe and headcloth with a gold cord, a black beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#C98E66", cloth=NOBLEMAN_C, kind="Robe", sw=3, flip=flip, up=up,
                     extra=A.headcloth(NOBLEMAN_C, cord="#E8B830") + A.BLACK_BEARD)

# ---- John 3 -------------------------------------------------------------------------------------------------------
def roof_night(p, w, h, seed, lamp_=True):
    """The same came unto him by night: a flat roof in Jerusalem under the stars, the low parapet, the city's roofs dark
    below and the temple far off; a lamp burning on the parapet; Jesus sitting on the roof, Nicodemus sitting before him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#1E1650"), mk.stars(70, w, h * 0.5, seed), moon(w * 0.86, h * 0.14, max(8, h * 0.035)),
         temple(w * 0.7, h * 0.56, min(w * 0.2, h * 0.4)),
         houses(w, h, h * 0.66, seed, hmin=0.12, hmax=0.2, color=("#3A3450", "#2E2A44", "#443E5A"), stairs=False),
         f'<rect x="-10" y="{f(h * 0.66)}" width="{f(w + 20)}" height="{f(h)}" fill="#4A4060" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(h * 0.6)}" width="{f(w + 20)}" height="{f(h * 0.08)}" fill="#5A5070" stroke="{INK}" stroke-width="2"></rect>']
    s = fit(b, max(h * 0.3, b - 220))
    if lamp_:
        o.append(glow(w * 0.5, h * 0.56, h * 0.36, "#FFC14D", 0.8, f"{p}g") + clay_lamp(w * 0.5, h * 0.6, min(1.1, max(0.6, h / 360))))
    o.append(jesus_seated(w * 0.32, b, s * 0.95, flip=False))
    o.append(nicodemus_seated(w * 0.7, b, s * 0.95, flip=True))
    return "".join(o)

def wind_night(p, w, h, seed):
    """The wind bloweth where it will: olive trees on a hillside at night bowing in the wind, the leaves torn away and
    flying, streaks of wind across the moonlit sky — no one drawn."""
    r = random.Random(seed)
    o = [sky(w, h, "#0B0B2A", "#2A2A5A"), mk.stars(40, w, h * 0.4, seed), moon(w * 0.16, h * 0.18, max(8, h * 0.04)),
         clouds(w, h * 0.22, seed, n=5, color="#3A3A6A", op=0.8, h=h), hills(w, h, h * 0.7, seed, color="#1A1A3A", amp=12, step=80),
         wind_lines(w, h, seed, n=12, color="#C8D0F0", op=0.6, y0=0.1, y1=0.8)]
    for i, x in enumerate((0.2, 0.5, 0.82)):
        o.append(f'<g transform="translate({f(w * x)} {f(h * 0.98)}) skewX(-10) translate({f(-w * x)} {f(-h * 0.98)})">{tree(w * x, h * 0.98, h / 330, color="#2A3A2A", lean=0.4, seed=seed + i)}</g>')
    for _ in range(18):
        x, y = r.uniform(0, w), r.uniform(h * 0.1, h * 0.8)
        o.append(f'<path d="M{f(x)} {f(y)} c 6 -6 14 -4 16 2 c -6 4 -12 4 -16 -2 Z" fill="#4A6A4A" stroke="{INK}" stroke-width="1" transform="rotate({r.randint(-40, 40)} {f(x)} {f(y)})"></path>')
    return "".join(o)

def serpent_lifted(p, w, h, seed):
    """As Moses lifted up the serpent in the wilderness: the serpent of brass on its standard against the evening sky, the
    tents of the camp below, the people standing and looking up to it."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#3A2A4A", "#E8A06A"), hills(w, h, h * 0.56, seed, color="#6A4A4A", amp=14, step=80), ground(w, h, h * 0.66, "#B8905A", dy=0)]
    from job.art import tents
    o.append(tents(w * 0.04, h * 0.7, max(0.4, h / 600), n=3, color="#4A3A30", seed=seed) + tents(w * 0.7, h * 0.72, max(0.4, h / 620), n=2, color="#5A4434", seed=seed + 1))
    top = h * 0.08; ph = b - top - h * 0.02
    o.append(glow(w * 0.5, top + 30, h * 0.3, "#FFE680", 0.6, f"{p}g") + N.brass_serpent(w * 0.5, top, ph, f"{p}bz"))
    s = fit(b, max(h * 0.4, b - 170))
    r = random.Random(seed)
    for i, x in enumerate((0.14, 0.24, 0.34, 0.66, 0.76, 0.88)):
        o.append(figure(p, w * x, b - (i % 2) * 6, b - (i % 2) * 6 - 200 * s, r.choice(HEB), "woman" if i % 3 == 1 else "man", flip=x > 0.5,
                        up=[(-22, -158), (-34, -186), (-40, -214)] if i % 2 == 0 else None))
    return "".join(o)

def world_light(p, w, h, seed):
    """God so loved the world: the whole wide land from a height at dawn — the sea, the hills, the rivers and the towns —
    and the light pouring down over all of it."""
    o = [sky(w, h, "#3A4A8A", "#FFE6A0"), rays(w * 0.5, -h * 0.1, 40, 20, h * 1.4, color="#FFFFFF", op=0.25, sw=3, a0=20, a1=160),
         glow(w * 0.5, 0, h * 0.7, "#FFFFFF", 0.85, f"{p}g"),
         f'<path d="M-10 {f(h * 0.52)} C {f(w * 0.2)} {f(h * 0.5)} {f(w * 0.3)} {f(h * 0.6)} {f(w * 0.24)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2C7DA8" stroke="{INK}" stroke-width="2"></path>',
         hills(w, h, h * 0.48, seed, color="#8A9A6A", amp=12, step=90)]
    o.append(f'<path d="M-10 {f(h * 0.6)} C {f(w * 0.2)} {f(h * 0.58)} {f(w * 0.3)} {f(h * 0.66)} {f(w * 0.26)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2C7DA8" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.26)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.5)} {f(h * 0.64)} {f(w * 0.7)} {f(h * 0.6)} C {f(w * 0.8)} {f(h * 0.58)} {f(w * 0.9)} {f(h * 0.6)} {f(w + 10)} {f(h * 0.62)} L {f(w + 10)} {f(h + 10)} Z" fill="#B8B06A" stroke="{INK}" stroke-width="2"></path>')
    o.append(river(w, h * 0.78, h * 0.04, seed=seed))
    for i, (x, y) in enumerate(((0.44, 0.7), (0.66, 0.66), (0.86, 0.72), (0.56, 0.9))):
        o.append(hill_town(w * x, h * y, w * 0.12, h * 0.08, seed + i, hill="#A8A05A"))
    return "".join(o)

def judaea_water(p, w, h, seed, john=False):
    """Baptizing in the land of Judæa: a river with green banks and much water, the people going down into it two by two;
    john=False Jesus on the bank, his disciples in the water baptizing; john=True John baptizing at Ænon near to Salim."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.36, seed, color="#9A9A6A", amp=16, step=80),
         f'<path d="M-10 {f(h * 0.5)} C {f(w * 0.3)} {f(h * 0.46)} {f(w * 0.6)} {f(h * 0.54)} {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h * 0.84)} C {f(w * 0.6)} {f(h * 0.88)} {f(w * 0.3)} {f(h * 0.82)} -10 {f(h * 0.86)} Z" fill="#2C7DA8" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M-10 {f(h * 0.86)} C {f(w * 0.3)} {f(h * 0.82)} {f(w * 0.6)} {f(h * 0.88)} {f(w + 10)} {f(h * 0.84)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8AAA5A" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, max(h * 0.24, b - 240)); jy = h * 0.6; js = min(s * 0.6, (h * 0.82 - jy) / 96)
    def wading(x, cloth, kind="disciple"):
        fig = (john_fig(p, x, jy + 92 * js, js, flip=True, up=UP_BLESS) if kind == "john"
               else mk.person(p, round(x), round(jy + 92 * js), round(js, 3), body="#B98A6E", cloth=cloth, kind="Tunic", sw=3, flip=True, up=UP_BLESS))
        return (fig + f'<rect x="{f(x - 40 * js)}" y="{f(jy)}" width="{f(80 * js)}" height="{f(94 * js)}" fill="#2C7DA8"></rect>'
                + f'<path d="M{f(x - 44 * js)} {f(jy)} q {f(22 * js)} -5 {f(44 * js)} 0 t {f(44 * js)} 0" stroke="#BFE6F2" stroke-width="2.4" fill="none"></path>')
    if john:
        o.append(wading(w * 0.4, None, "john") + wading(w * 0.54, "#6A5A3A", "man"))
        o.append(crowd(p, w * 0.66, w * 0.98, b, max(h * 0.5, b - 160), 6, seed, flip=True))
    else:
        o.append(wading(w * 0.42, ROBES["peter"]) + wading(w * 0.62, ROBES["andrew"]))
        o.append(jesus(p, w * 0.14, b, s))
        o.append(crowd(p, w * 0.74, w * 0.98, b, max(h * 0.5, b - 160), 4, seed, flip=True))
    return "".join(o)

def bridegroom(p, w, h, seed):
    """The friend of the bridegroom, that standeth and heareth him: a street at night, the bridegroom in white with a
    garland coming with his lamps, and at the lit doorway of the house his friend standing, his arms lifted for joy."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#0B0B2A", "#2A2050"), mk.stars(40, w, h * 0.3, seed),
         houses(w, h, h * 0.86, seed, hmin=0.4, hmax=0.56, lit=True, color=("#5A5070", "#4A4262", "#6A5E7A")),
         f'<rect x="-10" y="{f(h * 0.86)}" width="{f(w + 20)}" height="{f(h)}" fill="#3A3048" stroke="{INK}" stroke-width="2"></rect>']
    s = fit(b, max(h * 0.24, b - 240))
    garland = '<path d="M-14 -192 C -6 -200 6 -200 14 -192" stroke="#5E8F26" stroke-width="5" fill="none"></path>'
    lampf = lambda x, y, i: glow(x, y, 50 * s, "#FFC14D", 0.8, f"{p}l{i}") + f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(5 * s)}" fill="#FFE680"></circle>'
    o.append(glow(w * 0.78, b - 120 * s, 140 * s, "#FFC14D", 0.6, f"{p}d"))
    o.append(mk.person(p, round(w * 0.78), round(b), round(s, 3), body="#C98E66", cloth="#6A5A3A", kind="Robe", sw=3, flip=True,
                       up=[(-22, -158), (-36, -190), (-40, -222)], extra=A.headcloth("#E8E2D6", cord="#3A2214") + A.BLACK_BEARD))
    o.append(mk.person(p, round(w * 0.4), round(b), round(s, 3), body="#C98E66", cloth="#F3EFE6", kind="Robe", sw=3, extra=garland + A.BLACK_BEARD))
    for i, x in enumerate((0.12, 0.22)):
        o.append(mk.person(p, round(w * x), round(b - 4), round(s * 0.9, 3), body="#B98A6E", cloth=random.Random(seed + i).choice(HEB), kind="Tunic", sw=3,
                           up=[(-22, -158), (-30, -186), (-28, -210)]) + lampf(w * x - 28 * s * 0.9, b - 214 * s * 0.9, i))
    return "".join(o)

# ---- John 4 -------------------------------------------------------------------------------------------------------
def samaria_road(p, w, h, seed):
    """He must needs pass through Samaria: the road through the valley between the two mountains, Gerizim and Ebal, the
    town of Sychar on the slope; Jesus and his disciples walking on it."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"),
         f'<path d="M-10 {f(h * 0.62)} L {f(w * 0.12)} {f(h * 0.18)} L {f(w * 0.24)} {f(h * 0.12)} L {f(w * 0.46)} {f(h * 0.62)} Z" fill="#8A8A5A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.54)} {f(h * 0.62)} L {f(w * 0.78)} {f(h * 0.1)} L {f(w * 0.9)} {f(h * 0.16)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h * 0.62)} Z" fill="#7A8A5A" stroke="{INK}" stroke-width="2.4"></path>',
         hill_town(w * 0.62, h * 0.6, w * 0.16, h * 0.12, seed, hill="#8A9A5A"), ground(w, h, h * 0.6, "#C8B07A", dy=0),
         f'<path d="M{f(w * 0.2)} {f(h + 10)} C {f(w * 0.34)} {f(h * 0.8)} {f(w * 0.46)} {f(h * 0.7)} {f(w * 0.5)} {f(h * 0.6)} L {f(w * 0.54)} {f(h * 0.6)} C {f(w * 0.56)} {f(h * 0.72)} {f(w * 0.66)} {f(h * 0.86)} {f(w * 0.8)} {f(h + 10)} Z" fill="#E0D0A8" stroke="{INK}" stroke-width="1.6"></path>']
    s = fit(b, max(h * 0.28, b - 230))
    o.append(jesus(p, w * 0.5, b, s, flip=True))
    for i, who in enumerate(("peter", "andrew", "john", "james")):
        o.append(disciple(p, w * (0.62 + 0.09 * i), b - 4 * (i % 2), s * (0.96 - 0.03 * i), who, flip=True))
    return "".join(o)

def jacobs_well(p, w, h, seed, stage="alone"):
    """Jacob's well at Sychar at the sixth hour: the stone well-head in the noon glare, Mount Gerizim behind, the town on
    its slope. alone: Jesus sitting by the well wearied with his journey. woman: the woman of Samaria come to draw water,
    her waterpot on her shoulder, Jesus sitting. talk: the two of them, the woman standing by the well-head, her pot set
    down on its rim. disciples: the disciples come back from the city with food, marvelling. left: the waterpot left
    standing on the well-head, the woman far off running toward the city, Jesus with the disciples."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#7AC0E0", "#FFF4C2"), sun(w * 0.5, h * 0.06, max(12, h * 0.04), color="#FFF4C2", op=0.3),
         f'<path d="M{f(w * 0.4)} {f(h * 0.56)} L {f(w * 0.64)} {f(h * 0.12)} L {f(w * 0.76)} {f(h * 0.16)} L {f(w + 10)} {f(h * 0.46)} L {f(w + 10)} {f(h * 0.56)} Z" fill="#9A9A6A" stroke="{INK}" stroke-width="2.4"></path>',
         hills(w, h, h * 0.5, seed, color="#A8A06A", amp=10, step=90), hill_town(w * 0.84, h * 0.56, w * 0.22, h * 0.12, seed, hill="#B8A86A"),
         ground(w, h, h * 0.58, "#D8C08A", dy=0)]
    s = fit(b, max(h * 0.26, b - 230)); wx = w * 0.46
    o.append(well(wx, b - 10 * s, s * 1.6))
    if stage == "left":
        o.append(f'<g transform="translate({f(wx - 30 * s)} {f(b - 12 * s)}) scale({f(s)}) translate(23 172)">{POT}</g>')
    elif stage == "talk":
        o.append(f'<g transform="translate({f(wx + 50 * s)} {f(b - 12 * s)}) scale({f(s)}) translate(23 172)">{POT}</g>')
    o.append(jesus_seated(w * 0.24, b, s * 0.9))
    if stage == "woman":
        o.append(samaritan_fig(p, w * 0.74, b, s, flip=True))
    elif stage == "talk":
        o.append(samaritan_fig(p, w * 0.68, b, s, flip=True, pot=False, up=UP_BLESS))
    elif stage == "disciples":
        o.append(samaritan_fig(p, w * 0.64, b, s * 0.98, flip=True, pot=False))
        basket_ = '<path d="M-60 -120 L -30 -120 L -34 -96 L -56 -96 Z" fill="#B8904A" stroke="#0D0D0F" stroke-width="1.6"></path>'
        for i, who in enumerate(("peter", "andrew", "john")):
            o.append(disciple(p, w * (0.8 + 0.08 * i), b - 4 * (i % 2), s * (0.94 - 0.03 * i), who, flip=True))
        o.append(f'<g transform="translate({f(w * 0.8)} {f(b)}) scale({f(-s * 0.94)} {f(s * 0.94)})">{basket_}</g>')
    elif stage == "left":
        o.append(samaritan_fig(p, w * 0.9, h * 0.62, max(0.12, s * 0.32), pot=False, up=[(-22, -158), (-40, -176), (-56, -190)]))
        for i, who in enumerate(("peter", "andrew", "john")):
            o.append(disciple(p, w * (0.6 + 0.09 * i), b - 4 * (i % 2), s * (0.94 - 0.03 * i), who, flip=True))
    return "".join(o)

def white_fields(p, w, h, seed):
    """Lift up your eyes, and look on the fields, that they are white already unto harvest: the grain standing pale and
    ripe all down the valley under Sychar, and across it the people of the city coming out in their white garments."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF8DC"), hills(w, h, h * 0.36, seed, color="#9A9A6A", amp=12, step=80),
         hill_town(w * 0.78, h * 0.44, w * 0.3, h * 0.16, seed, hill="#A8A06A"), ground(w, h, h * 0.46, "#E8DCB0", dy=0),
         grain(-10, w + 10, h * 0.62, h * 0.1, seed, color="#F3EAC8"), grain(-10, w + 10, h * 0.8, h * 0.14, seed + 1, color="#F3EAC8")]
    s = fit(h * 0.62, h * 0.42)
    r = random.Random(seed)
    for i in range(7):
        x = w * (0.36 + 0.09 * i); y = h * (0.56 + 0.01 * (i % 2))
        o.append(figure(p, x, y, y - 200 * s * r.uniform(0.9, 1.0), "#F3EFE6" if i % 2 else "#E8E2D6", "woman" if i % 3 == 1 else "man", flip=True))
    o.append(grain(-10, w + 10, h * 0.98, h * 0.2, seed + 2, color="#F3EAC8"))
    sj = fit(b, max(h * 0.3, b - 220))
    o.append(jesus(p, w * 0.14, b, sj, flip=True, up=UP_BLESS))
    return "".join(o)

def nobleman_cana(p, w, h, seed):
    """A certain nobleman, whose son was sick at Capernaum: a street of Cana, the nobleman in purple come up from
    Capernaum, his hands held out to Jesus, beseeching him; his servant waiting behind."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.8, seed, hmin=0.34, hmax=0.5), ground(w, h, h * 0.8, "#C8B07A", dy=0)]
    s = fit(b, max(h * 0.26, b - 240))
    o.append(jesus(p, w * 0.3, b, s))
    o.append(nobleman_fig(p, w * 0.56, b, s * 0.98, up=UP_BLESS))
    o.append(man(p, w * 0.76, b - 4, s * 0.92, "#8A7A5A", flip=True))
    return "".join(o)

def servants_meet(p, w, h, seed):
    """As he was now going down, his servants met him: the road coming down from the hills toward the lake and Capernaum,
    the nobleman going down it, two servants running up to meet him with their arms raised."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.3, seed, color="#7A8A6A", amp=12, step=90), lake(w, h, h * 0.36, seed, n=8),
         houses(w, h, h * 0.5, seed, x0=w * 0.6, x1=w + 10, hmin=0.08, hmax=0.14), ground(w, h, h * 0.52, "#9AAA5A", dy=-6),
         f'<path d="M-10 {f(h * 0.8)} C {f(w * 0.3)} {f(h * 0.76)} {f(w * 0.6)} {f(h * 0.62)} {f(w * 0.8)} {f(h * 0.52)}" stroke="#E0D0A8" stroke-width="{f(max(10, h * 0.08))}" fill="none"></path>']
    s = fit(b, max(h * 0.28, b - 230))
    o.append(nobleman_fig(p, w * 0.3, b, s, flip=True))
    o.append(man(p, w * 0.56, b - 6, s * 0.92, "#8A7A5A", up=UP_HIGH) + man(p, w * 0.68, b - 10, s * 0.88, "#6A5A3A", up=UP_BLESS))
    return "".join(o)

def whole_house(p, w, h, seed):
    """Himself believed, and his whole house: within the nobleman's house at Capernaum, the lamp lit, the son standing up
    whole from his bed, his mother beside him, the nobleman come in at the door, the household about them."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#C8A878", floor="#8A6A4A"), clay_lamp(w * 0.5, h * 0.24, max(0.6, h / 300)),
         f'<rect x="{f(w * 0.04)}" y="{f(h * 0.22)}" width="{f(w * 0.14)}" height="{f(b - h * 0.22)}" fill="#FFE6A0" stroke="{INK}" stroke-width="2"></rect>',
         bedroll(w * 0.72, b, w * 0.24, 14)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(nobleman_fig(p, w * 0.12, b, s, flip=True, up=UP_BLESS))
    o.append(mk.person(p, round(w * 0.56), round(b), round(s * 0.7, 3), body="#C98E66", cloth="#F3EFE6", kind="Tunic", sw=3))
    o.append(woman_fig(p, w * 0.66, b, s * 0.94, "#6A4A6A", "#3A2A5A", flip=True, up=UP_TOUCH))
    o.append(man(p, w * 0.86, b, s * 0.9, "#8A7A5A", flip=True) + woman_fig(p, w * 0.32, b, s * 0.9, "#7A6A4A", "#5A4A3A", flip=True))
    return "".join(o)

def reaping(p, w, h, seed):
    """He that reapeth receiveth wages: the harvest in a golden field at evening, two reapers with their sickles and a
    binder with a sheaf, and far off across the next field a sower walking with his seed-bag."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A6A", "#FFC890"), sun(w * 0.86, h * 0.36, max(12, h * 0.04), color="#FFE680", op=0.4),
         hills(w, h, h * 0.4, seed, color="#8A7A5A", amp=10, step=90), ground(w, h, h * 0.48, "#8A6A3A", dy=0),
         grain(w * 0.3, w + 10, h * 0.8, h * 0.18, seed, color="#E8C060"), grain(w * 0.36, w + 10, h * 0.98, h * 0.2, seed + 1, color="#E8C060")]
    s = fit(b, max(h * 0.28, b - 220))
    sickle = '<path d="M-60 -150 C -80 -150 -86 -128 -74 -116" stroke="#C8C8D0" stroke-width="4" fill="none"></path>'
    o.append(man(p, w * 0.42, b, s, "#6A5A3A", up=[(-22, -158), (-44, -150), (-60, -150)], extra=sickle))
    o.append(man(p, w * 0.62, b - 6, s * 0.96, "#5A4A3A", up=[(-22, -158), (-44, -150), (-60, -150)], extra=sickle))
    sheaf = '<path d="M-44 -160 L -18 -160 L -22 -90 L -40 -90 Z" fill="#E8C060" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(man(p, w * 0.16, b, s * 0.98, "#7A5A3A", flip=False, up=[(-22, -158), (-30, -140), (-30, -120)], extra=sheaf))
    ss = fit(h * 0.5, h * 0.38)
    bag = '<path d="M18 -120 C 34 -116 36 -96 22 -90" fill="#C8A878" stroke="#0D0D0F" stroke-width="1.4"></path>'
    o.append(man(p, w * 0.12, h * 0.5, ss, "#5A6A3A", flip=True, up=UP_BLESS, extra=bag))
    return "".join(o)

def sychar_gate(p, w, h, seed, believe=False):
    """The Samaritans came unto him, and besought him to abide with them: the gate of Sychar under Mount Gerizim, the men
    of the city come out to Jesus, the woman among them; believe=True: they standing about him in the gate, the woman a
    little apart."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"),
         f'<path d="M{f(w * 0.3)} {f(h * 0.5)} L {f(w * 0.56)} {f(h * 0.08)} L {f(w * 0.7)} {f(h * 0.12)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h * 0.5)} Z" fill="#9A9A6A" stroke="{INK}" stroke-width="2.4"></path>',
         walls(w * 0.46, w * 1.02, h * 0.7, h * 0.36, seed, towers=2), ground(w, h, h * 0.7, "#D8C08A", dy=0)]
    s = fit(b, max(h * 0.26, b - 230))
    o.append(jesus(p, w * 0.2, b, s))
    r = random.Random(seed)
    for i, x in enumerate((0.42, 0.52, 0.62, 0.72) if not believe else (0.36, 0.48, 0.6, 0.7)):
        o.append(mk.person(p, round(w * x), round(b - 4 * (i % 2)), round(s * (0.97 - 0.02 * i), 3), body="#B98A6E", cloth=r.choice(HEB), kind="Robe", sw=3,
                           up=UP_BLESS if i == 0 and not believe else None, extra=A.headcloth(r.choice(["#E8E2D6", "#6A5A3A", "#8A7A6A"]), cord="#3A2214") + A.BLACK_BEARD))
    o.append(samaritan_fig(p, w * (0.86 if believe else 0.82), b, s * 0.94, flip=True, pot=False))
    return "".join(o)
