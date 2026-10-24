"""Drawings for Acts 22:30–24:27. The council again, Ananias the high priest (a white headcloth with a gold band, black
beard) on his seat; the blow on the mouth (23:2) told in words only; the Pharisees and Sadducees divided, the scribes
standing up; the soldiers taking Paul out from among them into the castle; the night following — Paul in the castle by a
lamp, and a light standing by him (the Lord is not drawn); the forty banded together under a curse in a dark room, their
hands lifted; Paul's sister's son and the chief captain taking him aside by the hand; the escort by night — soldiers,
horsemen and spearmen on the road, Paul set on a horse; Lysias' letter; the road to Antipatris and Cæsarea on the map;
Felix (a Roman governor: a toga with a purple border, short dark hair and stubble) in Herod's palace at Cæsarea, reading;
Tertullus the orator accusing before him, the high priest and elders behind; Paul's defence; Felix and Drusilla (a deep
teal veil with a gold band) hearing Paul; Felix terrified; the two years in bonds. Built on act.art12."""
from act.art12 import *
from act.art import f, INK, HEB, TWELVE, LIE, _porch, _temple, _hall, _prison, _street, _upper, _house, _synagogue, _gate, _road
import random, math
import exodus3 as E3
from act.art8 import letter

def felix(p, x, y, s, flip=False, up=None): return toga_fig(p, x, y, s, hr="#4A3A2A", border="#5A1A6A", flip=flip, up=up, extra=beard("#4A3A2A").replace('fill="#4A3A2A"', 'fill="#4A3A2A" opacity="0.6"'))
def drusilla(p, x, y, s, flip=False, up=None):
    return woman_fig(p, x, y, s * 0.94, "#2A5A5A", "#1F5A5A", flip=flip, up=up, extra=band())
def tertullus(p, x, y, s, flip=False, up=None): return toga_fig(p, x, y, s, hr="#2A1A10", border="#8A6A2A", flip=flip, up=up)
def high_priest(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#E8E2D6", head="#F3EFE6", cord="#E8B830", bd="#3A2A1A", flip=flip, up=up)
def nephew(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#7A6A4A", hr="#2A1A10", kind="Tunic", flip=flip, up=up)
WHO.update({"felix": felix, "drusilla": drusilla, "tertullus": tertullus, "high_priest": high_priest, "nephew": nephew})

def council_divided(p, w, h, seed, taken=False):
    """The council divided: the scribes of the Pharisees' part (white headcloths) standing up on one side with their hands
    lifted, the Sadducees (dark red headcloths) on the other, Paul in the midst; taken=True the soldiers come down and
    taking him from among them."""
    bg, b = _hall(w, h, seed, "council")
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    for i, x in enumerate((0.06, 0.16, 0.26)):
        o.append(man_fig(p, w * x, b, s * (1 - 0.02 * i), "#E8E2D6", head="#F3EFE6", cord="#3A4A6A", bd=["#6A645E", "#9A948A", "#2A1A10"][i], flip=True, up=UP_HIGH if i != 1 else UP_BLESS))
    for i, x in enumerate((0.74, 0.84, 0.94)):
        o.append(man_fig(p, w * x, b, s * (1 - 0.02 * i), "#6A2A3A", head="#6A2A3A", cord="#E8B830", bd=["#1A1210", "#3A2A1A", "#1A1210"][i], up=UP_HIGH if i == 0 else UP_BLESS))
    o.append(paul(p, w * 0.5, b, s))
    if taken:
        o.append(soldier(p, w * 0.4, b, s, flip=True) + soldier(p, w * 0.6, b, s) + lysias(p, w * 0.32, b, s * 0.98, flip=True, up=UP_BLESS))
    return "".join(o)

def castle_night(p, w, h, seed):
    """The night following, in the castle: Paul sitting by a lamp in a stone chamber, and standing by him a light — the Lord
    not drawn, his words come from the light."""
    bg, b = _prison(w, h, seed)
    o = [mk.defs(p, *ALL), bg, glow(w * 0.62, b - h * 0.3, h * 0.5, "#FFFFFF", 0.9, f"{p}l"),
         f'<ellipse cx="{f(w * 0.62)}" cy="{f(b - h * 0.32)}" rx="{f(w * 0.08)}" ry="{f(h * 0.34)}" fill="#FFFFFF" opacity="0.4"></ellipse>']
    s = fit(b, max(h * 0.3, b - 200))
    o.append(seated(w * 0.36, b, s * 0.84, ROBES["paul"], head="#5A4A3A", beard="#3A2A1A") + A.lamp(w * 0.2, b - 10, s * 0.8))
    return "".join(o)

def forty(p, w, h, seed):
    """More than forty banded together under a curse: a dark room by one lamp, the men standing close with their right hands
    lifted to swear, their faces in shadow."""
    o = [mk.defs(p, *ALL), bgr(w, h, "#1E1420"), glow(w * 0.5, h * 0.3, h * 0.4, "#C8603A", 0.5, f"{p}l"), A.lamp(w * 0.5, h * 0.28, max(0.6, h / 360)),
         f'<rect x="-10" y="{f(h * 0.92)}" width="{f(w + 20)}" height="{f(h)}" fill="#120A10"></rect>']
    b = h * 0.94
    s = fit(b, max(h * 0.3, b - 200))
    r = random.Random(seed)
    for row, (y, k, n) in enumerate(((b - 30 * s, 0.84, 9), (b, 1.0, 7))):
        for i in range(n):
            x = w * (0.06 + 0.88 * i / (n - 1)) + r.uniform(-6, 6)
            o.append(silhouette(man_fig(p, x, y, s * k, "#2A1A2A", head="#2A1A2A", cord=None, kind="Robe", flip=x > w / 2, up=UP_HIGH if (i + row) % 2 else None), "#2A1A24"))
    return "".join(o)

def nephew_told(p, w, h, seed, captain=False):
    """Paul's sister's son in the castle: in the court within the barracks, the young man telling Paul, a centurion standing by;
    captain=True the chief captain taking him by the hand and going aside with him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bgr(w, h, "#B8A07A"), f'<rect x="-10" y="{f(h * 0.1)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(b - h * 0.04)}" width="{f(w + 20)}" height="{f(h)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></rect>']
    s = fit(b, max(h * 0.3, b - 200))
    if captain:
        o.append(lysias(p, w * 0.4, b, s, up=[(-22, -158), (-40, -136), (-56, -126)]) + nephew(p, w * 0.28, b, s * 0.94, up=[(22, -158), (40, -136), (52, -128)]))
        o.append(centurion(p, w * 0.78, b, s, flip=True))
    else:
        o.append(paul(p, w * 0.24, b, s, flip=True, up=UP_BLESS) + nephew(p, w * 0.38, b, s * 0.94) + centurion(p, w * 0.6, b, s, flip=True))
    return "".join(o)

def escort(p, w, h, seed):
    """At the third hour of the night: the escort going out on the road by moonlight — the spearmen, the soldiers, the
    horsemen, and Paul set upon a horse in their midst."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#1E1650"), mk.stars(50, w, h * 0.4, seed), moon_(w * 0.86, h * 0.14, max(8, h * 0.035)),
         hills(w, h, h * 0.54, seed, color="#14142E", amp=12, step=90), ground(w, h, h * 0.62, "#1E1E36", dy=0)]
    s = fit(b, max(h * 0.3, b - 180))
    for i, x in enumerate((0.04, 0.12, 0.2)):
        o.append(soldier(p, w * x, b, s * 0.9, flip=True))
    k = s * 0.85
    for i, x in enumerate((0.36, 0.58)):
        o.append(E3.horse(w * x, b, k, color=["#3A2214", "#5A3A22"][i]))
        o.append(mk.person(p, round(w * x - 10 * k), round(b - 70 * k), round(k * 0.7, 3), body=SKIN, cloth="#A8281E" if i else ROBES["paul"], kind="Tunic" if i else "Robe", sw=3,
                           extra=HELM if i else A.headcloth("#5A4A3A", cord="#2A1A10") + beard("#3A2A1A")))
    for i, x in enumerate((0.76, 0.86, 0.96)):
        o.append(soldier(p, w * x, b, s * 0.9, flip=True))
    return "".join(o)

def to_caesarea(w, h):
    """By night to Antipatris, and on to Cæsarea: the map."""
    return geo.med_map(w, h, box=(34.3, 35.7, 31.5, 32.8), places=("JERUSALEM", "ANTIPATRIS", "CÆSAREA", "LYDDA", "JOPPA"),
                       routes=[("JERUSALEM", "ANTIPATRIS"), ("ANTIPATRIS", "CÆSAREA")], hi=("ANTIPATRIS", "CÆSAREA"), regions=(("THE GREAT SEA", 34.5, 32.2), ("SAMARIA", 35.3, 32.55)),
                       lit_routes=[0, 1], size=10, rsize=10, title="ACTS 23:31–33 · TO ANTIPATRIS AND CÆSAREA")

def praetorium(p, w, h, seed, governor="felix", seated_=True, accused=True, accusers=True, orator=None, queen=None, paul_speak=False):
    """The governor's hall in Herod's palace at Cæsarea: red hangings, white columns, the governor on his raised seat;
    orator= "tertullus" standing to accuse with his hand out; accusers=True the high priest and elders behind him;
    accused=True Paul standing with a soldier; queen= "drusilla" or "bernice" sitting beside the governor; governor=
    "felix", "festus" or "agrippa" (with "festus" beside him)."""
    bg, b = _hall(w, h, seed, "roman")
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.4, b - 190))
    st = b - 40 * s
    o.append(f'<rect x="{f(w * 0.62)}" y="{f(st)}" width="{f(w * 0.4)}" height="{f(b - st + 2)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    gx = w * 0.78
    gfig = {"felix": felix, "festus": lambda p, x, y, s, flip=False, up=None: toga_fig(p, x, y, s, hr="#8A7A6A", border="#5A1A6A", flip=flip, up=up),
            "agrippa": lambda p, x, y, s, flip=False, up=None: king_fig(p, x, y, s, cloth="#4A1A6A", bd=None, flip=flip, up=up)}[governor]
    o.append(gfig(p, gx, st, s * 0.96, flip=True, up=UP_BLESS if not orator and not paul_speak else None))
    if governor == "agrippa":
        o.append(toga_fig(p, w * 0.68, st, s * 0.94, hr="#8A7A6A", border="#5A1A6A", flip=True))
    if queen:
        o.append(woman_fig(p, w * 0.9, st, s * 0.9, *({"drusilla": ("#2A5A5A", "#1F5A5A"), "bernice": ("#2A3A6A", "#2A3A6A")}[queen]), flip=True, extra=band()))
    if accused:
        o.append(soldier(p, w * 0.08, b, s) + paul(p, w * 0.2, b, s, flip=True, up=UP_BLESS if paul_speak else None))
    if accusers:
        o.append(high_priest(p, w * 0.34, b, s * 0.98, flip=True) + elder(p, w * 0.44, b, s * 0.96, flip=True))
    if orator == "tertullus":
        o.append(tertullus(p, w * 0.54, b, s, flip=True, up=UP_BLESS))
    return "".join(o)

def two_years(p, w, h, seed):
    """When two years were fulfilled: Paul in custody in Herod's palace at Cæsarea, at a barred window over the harbour, a
    soldier at the door, a friend bringing him bread; the sea beyond."""
    from ecc.art import loaf
    bg, b = _house(w, h, seed)
    o = [mk.defs(p, *ALL), bg, f'<rect x="{f(w * 0.06)}" y="{f(h * 0.2)}" width="{f(w * 0.2)}" height="{f(h * 0.32)}" fill="#8FD0E2" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<g transform="translate({f(w * 0.06)} {f(h * 0.36)})">' + sea_(w * 0.2, h * 0.16, 0, seed) + '</g>']
    o.append("".join(f'<path d="M{f(w * (0.06 + 0.05 * k))} {f(h * 0.2)} L {f(w * (0.06 + 0.05 * k))} {f(h * 0.52)}" stroke="#3A3A44" stroke-width="4"></path>' for k in range(1, 4)))
    s = fit(b, max(h * 0.3, b - 200))
    o.append(seated(w * 0.32, b, s * 0.84, ROBES["paul"], head="#5A4A3A", beard="#3A2A1A", flip=True))
    o.append(man_fig(p, w * 0.5, b, s, "#6A5A3A", hr="#2A1A10", bd="#2A1A10", up=[(22, -158), (40, -140), (56, -136)]) + loaf(w * 0.5 - 56 * s, b - 140 * s, s * 0.5))
    o.append(soldier(p, w * 0.64, b, s, flip=True))
    return "".join(o)
