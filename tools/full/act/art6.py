"""Drawings for Acts 10–11. Cornelius' house at Cæsarea: a Roman house (red walls, white columns, the court open to the
sky), Cornelius kneeling at the ninth hour in his red cloak and helmet, an angel of God (white light, a gold rim, no face)
coming in to him; his servants and the devout soldier sent to Joppa. Peter on the housetop by the sea at the sixth hour, and
the vessel let down from the opened heaven by its four corners, a great sheet full of fourfooted beasts and creeping things
(the serpent drawn with snake.py) and birds — the voice is the Voice box, God never drawn; the three men at the gate; the
road up the coast; Cornelius at Peter's feet; the Gentiles gathered, and the Holy Spirit falling on them as light from above
(nothing else of the Spirit drawn); the church at Jerusalem contending; the roads of the scattering to Phœnicia, Cyprus
and Antioch; Antioch's colonnaded street, Barnabas and Saul teaching; Agabus standing up; the relief carried to Judæa.
Built on act.art5."""
from act.art5 import *
from act.art import f, INK, HEB, TWELVE, LIE, _porch, _temple, _hall, _prison, _street, _upper, _house, _synagogue, _gate, _road
import random, math
from lev.art3 import creature
import judges1 as J1, judges2 as J2, samuel1 as S1, snake as SN
from genesis.art7 import goat

def cornelius(p, x, y, s, flip=False, up=None): return centurion(p, x, y, s, flip=flip, up=up)
WHO.update({"cornelius": cornelius})

def roman_house(w, h, seed, tone="day"):
    """A Roman house at Cæsarea: red plastered walls, white columns about the court, a dark doorway, the sky above."""
    b = h * 0.92
    o = [sky(w, h, "#8FD0E2", "#F3E8C8") if tone == "day" else sky(w, h, "#3A2A4A", "#E8A060"),
         f'<rect x="-10" y="{f(h * 0.16)}" width="{f(w + 20)}" height="{f(b - h * 0.16)}" fill="#A8382E" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(h * 0.12)}" width="{f(w + 20)}" height="{f(h * 0.05)}" fill="#C8A878" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(h * 0.5)}" width="{f(w + 20)}" height="{f(h * 0.04)}" fill="#6A1A16" opacity="0.6"></rect>']
    for x in (0.06, 0.3, 0.54, 0.78):
        o.append(f'<rect x="{f(w * x - 14)}" y="{f(h * 0.17)}" width="28" height="{f(b - h * 0.17)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="{f(w * x - 20)}" y="{f(h * 0.17)}" width="40" height="10" fill="#E8DCC0" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<rect x="{f(w * 0.86)}" y="{f(h * 0.3)}" width="{f(w * 0.1)}" height="{f(b - h * 0.3)}" fill="#2A1A10" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    for k in range(-2, 14):
        x = w * k / 10
        o.append(f'<path d="M{f(x)} {f(b)} L {f(x + w * 0.05)} {f(h + 10)}" stroke="#A89878" stroke-width="1.2"></path>')
    return "".join(o), b

def cornelius_house(p, w, h, seed, angel_=False, sending=False, gathered=False, peter_in=False, fell=False, spirit=False, kneel=True):
    """Cornelius at prayer in his house at the ninth hour (kneeling, his red cloak and brass helmet laid by him); angel_=True
    an angel of God, white light and no face, coming in to him; sending=True Cornelius standing, two household-servants and a
    devout soldier before him; gathered=True his kinsmen and near friends sitting in the court; peter_in=True Peter come in
    at the door; fell=True Cornelius fallen at Peter's feet; spirit=True light falling from above on all of them."""
    bg, b = roman_house(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 210))
    if spirit:
        o.append(f'<path d="M{f(w * 0.3)} -10 L {f(w * 0.7)} -10 L {f(w * 0.96)} {f(b)} L {f(w * 0.04)} {f(b)} Z" fill="#FFFFFF" opacity="0.28"></path>'
                 + glow(w * 0.5, h * 0.2, w * 0.4, "#FFF4C2", 0.7, f"{p}sp"))
    if angel_:
        o.append(angel(p, w * 0.66, b, s, flip=False, up=UP_BLESS) + glow(w * 0.66, b - 110 * s, 150 * s, "#FFFFFF", 0.8, f"{p}an"))
    if kneel and not (sending or fell or peter_in or gathered):
        o.append(E.kneel(w * 0.36, b, s * 0.9, color="#7A1A14", skin=SKIN, flip=True))
        o.append(f'<path d="M{f(w * 0.2)} {f(b)} C {f(w * 0.2)} {f(b - 22 * s)} {f(w * 0.24)} {f(b - 26 * s)} {f(w * 0.26)} {f(b - 26 * s)} L {f(w * 0.26)} {f(b)} Z" fill="#C8963E" stroke="{INK}" stroke-width="1.6"></path>')
    if sending:
        o.append(cornelius(p, w * 0.22, b, s, flip=True, up=UP_BLESS))
        o.append(man_fig(p, w * 0.46, b, s * 0.96, "#6A5A4A", hr="#3A2A1A", kind="Tunic") + man_fig(p, w * 0.56, b, s * 0.96, "#4A5A6A", hr="#2A1A10", kind="Tunic")
                 + soldier(p, w * 0.68, b, s))
    if gathered:
        for i, x in enumerate((0.46, 0.56, 0.66, 0.76)):
            o.append(seated(w * x, b, s * 0.78, ["#6A2A4A", "#1F5A6A", "#8A6A2A", "#4A4A6A"][i], head=None, beard=None if i % 2 else "#4A3A2A", flip=True))
        o.append(woman_fig(p, w * 0.9, b, s * 0.9, "#5A2A6A", "#2A2A4A", flip=True))
    if peter_in or fell:
        o.append(peter(p, w * 0.12, b, s, flip=True, up=UP_TOUCH if fell else UP_BLESS))
    if fell:
        o.append(E.kneel(w * 0.26, b, s * 0.86, color="#7A1A14", skin=SKIN, flip=False))
    elif peter_in or gathered:
        o.append(cornelius(p, w * 0.28, b, s, flip=False))
    if spirit:
        for i, x in enumerate((0.46, 0.56, 0.66, 0.76)):
            o.append(glow(w * x, b - 110 * s * 0.78, 50 * s, "#FFFFFF", 0.7, f"{p}g{i}"))
    return "".join(o)

def unclean_sheet(x, y, wd, s, seed, uid):
    """A great sheet let down by four corners, (x, y) its middle: four cords up to the opened heaven, the cloth sagging,
    full of fourfooted beasts (a swine, a camel's head, a hare, a lion), creeping things (a serpent, a lizard) and birds."""
    r = random.Random(seed)
    hw = wd / 2
    o = [f'<path d="M{f(x - hw)} {f(y - 20 * s)} L {f(x - hw * 0.4)} {f(y - 600 * s)} M{f(x + hw)} {f(y - 20 * s)} L {f(x + hw * 0.4)} {f(y - 600 * s)}" stroke="#FFF4C2" stroke-width="{f(2 * s + 1)}"></path>']
    # the animals in the sheet, drawn first so the near edge of the cloth covers their feet
    o.append(J2.lion(x - hw * 0.3, y - 10 * s, s * 0.32, roar=False))
    o.append(J1.camel(x + hw * 0.32, y - 6 * s, s * 0.26, color="#B5844A"))
    for kind, dx, dy, k in (("swine", -0.62, -2, 1.0), ("hare", 0.06, -6, 0.9), ("lizard", 0.62, -2, 0.9), ("mouse", -0.04, 4, 0.8)):
        o.append(creature(kind, x + hw * dx, y + dy * s, s * k))
    pts = [(x - hw * 0.16, y - 4 * s), (x - hw * 0.06, y - 24 * s), (x + hw * 0.04, y - 10 * s), (x + hw * 0.14, y - 30 * s), (x + hw * 0.22, y - 44 * s)]
    o.append(SN.snake(pts, 5 * s, f"{uid}sn", head_scale=0.4))
    for i in range(5):
        bx = x + hw * r.uniform(-0.8, 0.8); by = y - r.uniform(70, 150) * s
        o.append(bird(bx, by, s * r.uniform(1.0, 1.6), color="#2A2A3A"))
    o.append(f'<path d="M{f(x - hw)} {f(y - 20 * s)} C {f(x - hw * 0.5)} {f(y + 40 * s)} {f(x + hw * 0.5)} {f(y + 40 * s)} {f(x + hw)} {f(y - 20 * s)} '
             f'C {f(x + hw * 0.6)} {f(y + 6 * s)} {f(x - hw * 0.6)} {f(y + 6 * s)} {f(x - hw)} {f(y - 20 * s)} Z" fill="#F8F4EC" stroke="{INK}" stroke-width="2.4"></path>')
    return "".join(o)

def housetop(p, w, h, seed, sheet=False, men=False, perplexed=False):
    """Peter on the housetop at Joppa at the sixth hour: the flat roof with its parapet, the sea and the harbour beyond;
    sheet=True the heaven opened and the vessel let down to him, Peter kneeling; men=True the three men sent by Cornelius
    standing at the gate below."""
    b = h * 0.66
    o = [mk.defs(p, *ALL), sky(w, h, "#5AB0D8", "#FFF4C2"), sea_(w, h, h * 0.42, seed), ship(w * 0.86, h * 0.5, max(0.3, h / 900))]
    if sheet:
        o.append(rays(w * 0.62, -h * 0.1, 30, h * 0.06, h * 0.9, color="#FFFFFF", op=0.35, sw=4) + glow(w * 0.62, 0, h * 0.4, "#FFFFFF", 0.9, f"{p}o")
                 + clouds(w, h * 0.06, seed, n=5, color="#FFFDF0", op=0.9, h=h))
    o.append(f'<rect x="{f(w * 0.04)}" y="{f(b)}" width="{f(w * 0.6)}" height="{f(h)}" fill="#E8D8B0" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(w * 0.02)}" y="{f(b - 18)}" width="{f(w * 0.64)}" height="18" fill="#D8C8A0" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<path d="M{f(w * 0.64)} {f(h + 10)} L {f(w * 0.64)} {f(h * 0.8)} L {f(w + 10)} {f(h * 0.8)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></path>'
             f'<rect x="{f(w * 0.64)}" y="{f(h * 0.84)}" width="{f(w * 0.4)}" height="{f(h)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b - 18, max(h * 0.12, b - 18 - min(190, h * 0.4)))
    if sheet:
        o.append(unclean_sheet(w * 0.58, h * 0.42, w * 0.42, max(0.5, h / 520), seed, p))
        o.append(E.kneel(w * 0.24, b - 18, s * 0.9, color=ROBES["peter"], skin=SKIN, flip=True))
    else:
        o.append(peter(p, w * 0.24, b - 18, s, flip=True, up=UP_HIGH if not perplexed else None))
    o.append(f'<path d="M{f(w * 0.36)} {f(b + 30)} L {f(w * 0.36)} {f(h * 0.94)} L {f(w * 0.46)} {f(h * 0.94)} L {f(w * 0.46)} {f(b + 30)} Z" fill="#3A2A1E" stroke="{INK}" stroke-width="2"></path>')
    if men:
        s2 = fit(h * 0.98, h * 0.98 - min(160, h * 0.32))
        o.append(man_fig(p, w * 0.66, h * 0.98, s2, "#6A5A4A", hr="#3A2A1A", kind="Tunic") + man_fig(p, w * 0.73, h * 0.98, s2, "#4A5A6A", hr="#2A1A10", kind="Tunic")
                 + soldier(p, w * 0.8, h * 0.98, s2))
    return "".join(o)

def coast_road(w, h):
    """On the morrow they entered into Cæsarea: the coast road from Joppa north to Cæsarea on the map."""
    return geo.med_map(w, h, box=(33.9, 35.9, 31.4, 32.9), places=("JOPPA", "CÆSAREA", "LYDDA", "JERUSALEM", "ANTIPATRIS", "SAMARIA"),
                       routes=[("JOPPA", (34.8, 32.3), "CÆSAREA")], hi=("JOPPA", "CÆSAREA"), regions=(("THE GREAT SEA", 34.3, 32.2), ("SAMARIA", 35.4, 32.55)),
                       lit_routes=[0], size=10, rsize=10, title="ACTS 10:23–24 · JOPPA TO CÆSAREA")

def contended(p, w, h, seed):
    """They that were of the circumcision contended with him: in the house at Jerusalem, Peter standing before the brethren,
    elders in white headcloths with their hands lifted against him."""
    bg, b = _upper(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 210))
    o.append(peter(p, w * 0.3, b, s, flip=True, up=UP_BLESS))
    for i, x in enumerate((0.52, 0.63, 0.74, 0.85)):
        o.append(man_fig(p, w * x, b, s * (1 - 0.02 * i), ["#E8E2D6", "#3A4A6A", "#6A5A3A", "#E8E2D6"][i], head=["#F3EFE6", "#3A4A6A", "#E8E2D6", "#F3EFE6"][i], cord="#E8B830",
                         bd=["#6A645E", "#2A1A10", "#4A3A2A", "#9A948A"][i], up=UP_BLESS if i in (0, 2) else None))
    return "".join(o)

def antioch_map(w, h):
    """Phœnicia, and Cyprus, and Antioch: the roads of the scattering out of Judæa, north along the coast and over the sea."""
    return geo.med_map(w, h, box=(31.6, 38.4, 31.0, 37.4), places=("JERUSALEM", "TYRE", "SIDON", "SALAMIS", "ANTIOCH", "TARSUS", "DAMASCUS", "CÆSAREA"),
                       routes=[("JERUSALEM", "CÆSAREA", "TYRE", "SIDON", (35.8, 34.6), (35.8, 35.6), "ANTIOCH"), ("SIDON", (34.4, 34.6), "SALAMIS"), ("TARSUS", "ANTIOCH")],
                       hi=("ANTIOCH",), regions=(("PHŒNICIA", 36.0, 33.7), "CYPRUS", "SYRIA", "CILICIA"), lit_routes=[0, 1], size=10, rsize=10,
                       title="ACTS 11:19–26 · AS FAR AS ANTIOCH")

def antioch(p, w, h, seed, who=("barnabas", "paul"), crowd_n=6, tone="day"):
    """Antioch of Syria: the great colonnaded street of the Greek city, white columns and red roofs, the mountain behind;
    the teachers standing on the steps, the people of the church — Jews and Greeks — about them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8") if tone == "day" else sky(w, h, "#4A2A5A", "#FFB07A"),
         hills(w, h, h * 0.3, seed, color="#8A9A7A", amp=26, step=120)]
    for k in range(6):
        x = w * (0.04 + 0.18 * k); hh = h * (0.18 + 0.06 * (k % 3))
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.56 - hh)}" width="{f(w * 0.14)}" height="{f(hh)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>'
                 f'<path d="M{f(x - 6)} {f(h * 0.56 - hh)} L {f(x + w * 0.07)} {f(h * 0.56 - hh - 18)} L {f(x + w * 0.14 + 6)} {f(h * 0.56 - hh)} Z" fill="#B5583A" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<rect x="-10" y="{f(h * 0.3)}" width="{f(w + 20)}" height="{f(h * 0.04)}" fill="#D8C8A0" stroke="{INK}" stroke-width="2" opacity="0.0"></rect>')
    for k in range(10):
        x = w * (0.02 + 0.107 * k)
        o.append(f'<rect x="{f(x - 7)}" y="{f(h * 0.4)}" width="14" height="{f(h * 0.2)}" fill="#F8F4EC" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.38)}" width="{f(w + 20)}" height="{f(h * 0.03)}" fill="#E8DCC0" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(pavement(w, h, h * 0.6, color="#D8C8A8"))
    s = fit(b, max(h * 0.3, b - 210))
    for i, wh in enumerate(who):
        o.append(WHO[wh](p, w * (0.12 + 0.1 * i), b, s, flip=True, up=UP_BLESS if i == 0 else None))
    o.append(crowd(p, w * (0.18 + 0.1 * len(who)), w * 0.96, b, b - 180 * s, crowd_n, seed, flip=True))
    return "".join(o)

def agabus_stood(p, w, h, seed):
    """There stood up one of them named Agabus: the church at Antioch gathered in a house, Agabus (white beard, a dark-brown
    headcloth) standing with his arm lifted, Barnabas and Saul and the others seated listening."""
    bg, b = _house(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 210))
    o.append(man_fig(p, w * 0.24, b, s, "#6A5A4A", head="#4A3A2A", cord="#2A1A10", bd="#D8D2C6", flip=True, up=UP_HIGH))
    for i, (x, c, hd, bd) in enumerate(((0.44, "#3A6A3A", "#3A6A3A", "#4A2A1A"), (0.56, ROBES["paul"], "#5A4A3A", "#3A2A1A"), (0.68, "#6A4A3A", None, "#2A1A10"), (0.8, "#2A4A6A", "#2A4A6A", "#2A1A10"))):
        o.append(seated(w * x, b, s * 0.78, c, head=hd, beard=bd, flip=True))
    return "".join(o)

def relief(p, w, h, seed):
    """Sending relief to the elders by the hand of Barnabas and Saul: the road south out of Antioch, Barnabas and Saul
    walking beside an ass laden with sacks of grain."""
    import numbers1 as N1
    bg, b = _road(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 210))
    o.append(barnabas(p, w * 0.1, b, s) + N1.ass(w * 0.3, b, s * 0.9))
    k = s * 0.9
    o.append(f'<rect x="{f(w * 0.3 - 40 * k)}" y="{f(b - 108 * k)}" width="{f(46 * k)}" height="{f(40 * k)}" rx="{f(12 * k)}" fill="#C8A878" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(w * 0.3 + 2 * k)}" y="{f(b - 112 * k)}" width="{f(46 * k)}" height="{f(42 * k)}" rx="{f(12 * k)}" fill="#B8986A" stroke="{INK}" stroke-width="2"></rect>')
    o.append(paul(p, w * 0.5, b, s))
    return "".join(o)
