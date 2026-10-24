"""Drawings for Acts 16:1–17:15. Timothy (young, beardless, a grey-blue tunic) and his mother at Lystra; the vision at Troas —
Paul asleep, and in a soft light a man of Macedonia standing (a short cloak, the flat Macedonian cap) beseeching him; the
voyage by Samothrace and Neapolis on the map; the place of prayer by the river outside the gate of Philippi, the women
sitting, Lydia (a deep violet veil, the purple cloth of her trade over her arm); her household baptized; the maid's spirit
of divination is never drawn — the street of Philippi and Paul turning (16:16–18); the marketplace and the magistrates in
their togas with the serjeants and their rods; the beating (16:22–23) told in words only over the empty stocks and the rods
laid by; Paul and Silas in the stocks of the inner prison at midnight, singing, the prisoners listening; the earthquake,
the doors opened and the bands loosed; the jailor's sword (16:27) told in words only over the open doors; the jailor with
the lights fallen down before them; his house and his table; the serjeants at the prison gate; Lydia's house. Then
Thessalonica — the synagogue, the uproar at Jason's door (no blow drawn) and the rulers of the city; Berœa by night,
the scriptures searched; Paul sent to the sea. Built on act.art8."""
from act.art8 import *
from act.art import f, INK, HEB, TWELVE, LIE, _porch, _temple, _hall, _prison, _street, _upper, _house, _synagogue, _gate, _road
import random, math
from act.art6 import roman_house

LYDIA_ROBE, LYDIA_VEIL, PURPLE = "#4A2A6A", "#2A2A5A", "#6A1A6A"
def lydia(p, x, y, s, flip=False, up=None):
    cloth = f'<path d="M-30 -150 L -16 -150 L -18 -80 L -34 -84 Z" fill="{PURPLE}" stroke="#0D0D0F" stroke-width="1.6"></path>'
    return woman_fig(p, x, y, s * 0.94, LYDIA_ROBE, LYDIA_VEIL, flip=flip, up=up, extra=cloth)
def macedonian(p, x, y, s, flip=False, up=None):
    cap = '<path d="M-17 -196 C -16 -210 16 -210 17 -196 C 10 -192 -10 -192 -17 -196 Z" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="1.6"></path>'
    cloak = '<path d="M-24 -160 L 24 -160 L 30 -100 L -30 -100 Z" fill="#8A2A2A" stroke="#0D0D0F" stroke-width="1.6"></path>'
    return mk.person(p, round(x), round(y), round(s, 3), body=SKIN, cloth="#C8B080", kind="Tunic", sw=3, flip=flip, up=up, extra=cloak + cap + beard("#5A3A22"))
def jailor(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#6A5A3A", hr="#3A2A1A", bd=None, kind="Tunic", flip=flip, up=up)
def serjeant(p, x, y, s, flip=False, up=None):
    rods = '<path d="M26 -150 L 30 -40" stroke="#8A5A2A" stroke-width="7"></path><path d="M22 -150 L 34 -150 M22 -130 L 34 -130 M22 -110 L 34 -110" stroke="#C8A878" stroke-width="2"></path>'
    return man_fig(p, x, y, s, "#F3EFE6", hr="#4A3A2A", kind="Tunic", flip=flip, up=up, extra=rods)
def magistrate(p, x, y, s, flip=False, up=None): return toga_fig(p, x, y, s, hr="#6A645E", border="#8A1A1A", flip=flip, up=up)
WHO.update({"lydia": lydia, "macedonian": macedonian, "jailor": jailor, "serjeant": serjeant, "magistrate": magistrate})

def timothy_joined(p, w, h, seed):
    """At Lystra, a certain disciple named Timothy: the town gate, Timothy standing with his mother (a believing Jewess, a
    teal veil), Paul's hand on his shoulder, Silas beside."""
    bg, b = _gate(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    o.append(silas(p, w * 0.12, b, s, flip=True) + paul(p, w * 0.24, b, s, up=[(22, -158), (42, -170), (60, -166)]))
    o.append(timothy(p, w * 0.36, b, s * 0.94) + woman_fig(p, w * 0.47, b, s * 0.9, "#3A5A5A", "#1F5A5A", flip=True))
    o.append(crowd(p, w * 0.62, w * 0.94, b, b - 170 * s, 3, seed, flip=True))
    return "".join(o)

def vision_troas(p, w, h, seed):
    """A vision appeared to Paul in the night: Paul asleep on his mat in a room at Troas, the window on the sea; beside him in
    a soft light a man of Macedonia standing, his hand stretched out, beseeching him."""
    bg, b = _house(w, h, seed, "night")
    o = [mk.defs(p, *ALL, *LIE), bg, f'<rect x="{f(w * 0.06)}" y="{f(h * 0.26)}" width="{f(w * 0.14)}" height="{f(h * 0.3)}" fill="#0B1A3A" stroke="{INK}" stroke-width="2"></rect>']
    s = fit(b, max(h * 0.3, b - 200))
    o.append(bedroll(w * 0.36, b - 10 * s, 220 * s, 14 * s) + lying(p, w * 0.36 + 80 * s, b - 8 * s, s * 0.9, cloth=ROBES["paul"]))
    o.append(glow(w * 0.7, b - 110 * s, 170 * s, "#FFF4C2", 0.7, f"{p}v") + macedonian(p, w * 0.7, b, s, up=UP_BLESS))
    return "".join(o)

def river_prayer(p, w, h, seed, lydia_up=False):
    """Without the gate by a river side, a place of prayer: the river under the trees outside Philippi, the women sitting on
    the bank, Lydia among them; Paul sitting with Silas, Timothy and Luke, speaking; lydia_up=True Lydia standing, her hand
    lifted, giving heed."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), walls(w * 0.7, w + 10, h * 0.5, h * 0.24, seed, towers=2), hills(w, h, h * 0.5, seed, color="#8A9A6A", amp=10, step=90),
         ground(w, h, h * 0.56, "#9AAA5A", dy=0), f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.3)} {f(h * 0.58)} {f(w * 0.6)} {f(h * 0.66)} {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h * 0.7)} C {f(w * 0.6)} {f(h * 0.76)} {f(w * 0.3)} {f(h * 0.68)} -10 {f(h * 0.72)} Z" fill="#2C7DA8" stroke="{INK}" stroke-width="2"></path>',
         olive(w * 0.08, h * 0.6, h / 520, seed=seed), olive(w * 0.94, h * 0.62, h / 560, seed=seed + 1)]
    s = fit(b, max(h * 0.3, b - 200))
    o.append(seated(w * 0.14, b, s * 0.8, ROBES["paul"], head="#5A4A3A", beard="#3A2A1A") + seated(w * 0.25, b, s * 0.78, "#2A4A6A", head="#2A4A6A", beard="#2A1A10"))
    if lydia_up: o.append(lydia(p, w * 0.42, b, s, flip=True, up=UP_HIGH))
    else: o.append(seated(w * 0.42, b, s * 0.78, LYDIA_ROBE, head=LYDIA_VEIL, beard=None, flip=True))
    for i, x in enumerate((0.56, 0.68, 0.8)):
        o.append(seated(w * x, b, s * 0.76, ["#6A4A5A", "#5A6A4A", "#4A4A6A"][i], head=["#3A3A5A", "#2A4A5A", "#5A5A6A"][i], beard=None, flip=True))
    return "".join(o)

def lydia_baptized(p, w, h, seed):
    """When she was baptized, and her household: in the river, Paul and Lydia standing in the water, her household waiting on
    the bank."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.44, seed, color="#8A9A6A", amp=14, step=90), ground(w, h, h * 0.54, "#9AAA5A", dy=0),
         f'<path d="M-10 {f(h * 0.72)} C {f(w * 0.3)} {f(h * 0.66)} {f(w * 0.6)} {f(h * 0.8)} {f(w + 10)} {f(h * 0.74)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2C7DA8" stroke="{INK}" stroke-width="2"></path>',
         lake(w, h, h * 0.8, seed, color="#2C7DA8", deep="#1F5F8A", n=8)]
    s = fit(b, max(h * 0.3, b - 200))
    o.append(paul(p, w * 0.42, b, s, flip=True, up=UP_HIGH) + lydia(p, w * 0.54, b + 6, s))
    for i, x in enumerate((0.08, 0.17, 0.26)):
        o.append(woman_fig(p, w * x, h * 0.72, s * 0.76, ["#6A4A5A", "#5A6A4A", "#4A4A6A"][i], ["#3A3A5A", "#2A4A5A", "#5A5A6A"][i], flip=True) if i != 1
                 else man_fig(p, w * x, h * 0.72, s * 0.8, "#6A5A3A", hr="#2A1A10", kind="Tunic", flip=True))
    o.append(f'<rect x="-10" y="{f(b - 30 * s)}" width="{f(w + 20)}" height="{f(h)}" fill="#2C7DA8" opacity="0.7"></rect>')
    return "".join(o)

def lydia_house(p, w, h, seed, brethren=False):
    """Lydia's house at Philippi: the court hung with lengths of purple cloth drying on a line, Lydia at the door bidding
    them in; brethren=True the brethren gathered, Paul and Silas come from the prison greeting them."""
    bg, b = _house(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    for i, x in enumerate((0.3, 0.44, 0.58)):
        o.append(f'<path d="M{f(w * x)} {f(h * 0.14)} L {f(w * (x + 0.1))} {f(h * 0.14)} L {f(w * (x + 0.095))} {f(h * 0.5)} L {f(w * (x + 0.005))} {f(h * 0.48)} Z" fill="{[PURPLE, "#5A1A6A", "#7A2A7A"][i]}" stroke="{INK}" stroke-width="1.8"></path>')
    o.append(f'<path d="M{f(w * 0.26)} {f(h * 0.14)} L {f(w * 0.72)} {f(h * 0.14)}" stroke="#6A4A2A" stroke-width="3"></path>')
    s = fit(b, max(h * 0.3, b - 200))
    if brethren:
        o.append(paul(p, w * 0.26, b, s, flip=True, up=UP_BLESS) + silas(p, w * 0.16, b, s, flip=True) + lydia(p, w * 0.46, b, s))
        o.append(crowd(p, w * 0.58, w * 0.8, b, b - 170 * s, 3, seed))
    else:
        o.append(lydia(p, w * 0.24, b, s, flip=True, up=UP_CALL) + paul(p, w * 0.46, b, s) + silas(p, w * 0.56, b, s) + timothy(p, w * 0.66, b, s * 0.94))
    return "".join(o)

def philippi_street(p, w, h, seed):
    """The street of Philippi going down to the place of prayer: Paul turning about, his hand lifted, Silas with him; the
    people of the city watching from their doors (the spirit is never drawn: what was cried and charged is in the words)."""
    bg, b = _street(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    o.append(silas(p, w * 0.22, b, s) + paul(p, w * 0.36, b, s, flip=True, up=UP_HIGH))
    o.append(crowd(p, w * 0.66, w * 0.94, b, b - 170 * s, 3, seed, flip=True))
    return "".join(o)

def agora(p, w, h, seed, accusing=True):
    """The marketplace of Philippi before the rulers: the magistrates in their togas on the tribunal, the serjeants with
    their rods; the masters of the maid pointing at Paul and Silas, the multitude rising up against them."""
    bg, b = _porch(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    st = b - 36 * s
    o.append(f'<rect x="{f(w * 0.68)}" y="{f(st)}" width="{f(w * 0.32)}" height="{f(b - st + 2)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    o.append(magistrate(p, w * 0.78, st, s * 0.96) + magistrate(p, w * 0.9, st, s * 0.96, flip=True) + serjeant(p, w * 0.64, b, s))
    o.append(paul(p, w * 0.44, b, s) + silas(p, w * 0.52, b, s))
    o.append(man_fig(p, w * 0.12, b, s, "#8A6A2A", head="#5A3A2A", bd="#2A1A10", flip=True, up=UP_BLESS if accusing else UP_HIGH)
             + man_fig(p, w * 0.24, b, s, "#5A2A2A", hr="#2A1A10", bd="#2A1A10", flip=True, up=UP_HIGH))
    return "".join(o)

def stocks(p, w, h, seed, held=False, singing=False, quake=False):
    """The inner prison: the heavy wooden stocks on the stone floor. held=False the stocks empty and the rods laid by them
    (the beating told in words only); held=True Paul and Silas sitting with their feet fast in the stocks; singing=True at
    midnight, a little light about them, their faces lifted, the prisoners in the dark cells listening; quake=True the great
    earthquake — the walls cracked, the doors fallen open, the stocks broken apart and the chains loosed."""
    bg, b = _prison(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    k = s
    cx = w * 0.5
    if quake:
        r = random.Random(seed)
        for _ in range(5):
            x = r.uniform(w * 0.05, w * 0.95); y0 = r.uniform(0, h * 0.3)
            o.append(f'<path d="M{f(x)} {f(y0)} l {f(r.uniform(-20, 20))} {f(h * 0.12)} l {f(r.uniform(-20, 20))} {f(h * 0.1)} l {f(r.uniform(-20, 20))} {f(h * 0.12)}" stroke="#0D0D0F" stroke-width="3" fill="none"></path>')
        o.append(f'<rect x="{f(w * 0.06)}" y="{f(h * 0.3)}" width="{f(w * 0.14)}" height="{f(b - h * 0.3)}" fill="#FFE6A0" stroke="{INK}" stroke-width="2"></rect>'
                 f'<path d="M{f(w * 0.2)} {f(h * 0.3)} L {f(w * 0.28)} {f(h * 0.34)} L {f(w * 0.28)} {f(b + 4)} L {f(w * 0.2)} {f(b)} Z" fill="#3A3A44" stroke="{INK}" stroke-width="2"></path>')
        o.append(f'<rect x="{f(cx - 120 * k)}" y="{f(b - 34 * k)}" width="{f(100 * k)}" height="{f(30 * k)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2" transform="rotate(-12 {f(cx - 70 * k)} {f(b)})"></rect>'
                 f'<rect x="{f(cx + 20 * k)}" y="{f(b - 34 * k)}" width="{f(100 * k)}" height="{f(30 * k)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2" transform="rotate(10 {f(cx + 70 * k)} {f(b)})"></rect>')
        o.append(paul(p, cx - 60 * k, b, s, up=UP_HIGH) + silas(p, cx + 60 * k, b, s, flip=True))
        return "".join(o)
    if singing:
        o.append(glow(cx, b - 80 * k, 200 * k, "#FFF4C2", 0.55, f"{p}m"))
        for x in (0.08, 0.92):
            o.append(f'<rect x="{f(w * x - 40)}" y="{f(h * 0.3)}" width="80" height="{f(b - h * 0.3)}" fill="#1A1418" stroke="{INK}" stroke-width="2"></rect>'
                     + "".join(f'<path d="M{f(w * x - 40 + 16 * j)} {f(h * 0.3)} L {f(w * x - 40 + 16 * j)} {f(b)}" stroke="#6A6A74" stroke-width="3"></path>' for j in range(1, 5)))
    if held or singing:
        o.append(seated(cx - 70 * k, b - 6, s * 0.84, ROBES["paul"], head="#5A4A3A", beard="#3A2A1A") + seated(cx + 70 * k, b - 6, s * 0.84, "#2A4A6A", head="#2A4A6A", beard="#2A1A10", flip=True))
    o.append(f'<rect x="{f(cx - 70 * k)}" y="{f(b - 30 * k)}" width="{f(140 * k)}" height="{f(30 * k)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M{f(cx - 70 * k)} {f(b - 15 * k)} L {f(cx + 70 * k)} {f(b - 15 * k)}" stroke="#3A2414" stroke-width="2"></path>'
             + "".join(f'<circle cx="{f(cx + dx * k)}" cy="{f(b - 15 * k)}" r="{f(6 * k)}" fill="#1A1210"></circle>' for dx in (-46, -22, 22, 46)))
    if not (held or singing):
        o.append(f'<path d="M{f(cx + 100 * k)} {f(b - 4)} L {f(cx + 220 * k)} {f(b - 12 * k)} M{f(cx + 104 * k)} {f(b - 2)} L {f(cx + 226 * k)} {f(b - 4 * k)}" stroke="#8A5A2A" stroke-width="{f(5 * k)}"></path>')
    return "".join(o)

def jailor_lights(p, w, h, seed, fallen=True, doors=True):
    """He called for lights and sprang in, and fell down before Paul and Silas: the prison doors standing open, a lamp held
    up, the jailor fallen on his knees before them; fallen=False the open doors only, the jailor's sword and what he was about
    to do told in words."""
    bg, b = _prison(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    if doors:
        for x in (0.1, 0.4, 0.7):
            o.append(f'<rect x="{f(w * x)}" y="{f(h * 0.3)}" width="{f(w * 0.12)}" height="{f(b - h * 0.3)}" fill="#0B0B12" stroke="{INK}" stroke-width="2"></rect>'
                     f'<path d="M{f(w * (x + 0.12))} {f(h * 0.3)} L {f(w * (x + 0.18))} {f(h * 0.34)} L {f(w * (x + 0.18))} {f(b + 4)} L {f(w * (x + 0.12))} {f(b)} Z" fill="#3A3A44" stroke="{INK}" stroke-width="2"></path>')
    if fallen:
        o.append(glow(w * 0.4, b - 60 * s, 180 * s, "#FFC14D", 0.6, f"{p}l"))
        o.append(E.kneel(w * 0.42, b, s * 0.9, color="#6A5A3A", skin=SKIN) + A.lamp(w * 0.42 + 40 * s, b - 120 * s, s * 0.8))
        o.append(paul(p, w * 0.6, b, s, flip=True, up=UP_BLESS) + silas(p, w * 0.72, b, s, flip=True))
    return "".join(o)

def jailor_table(p, w, h, seed):
    """He brought them up into his house, and set food before them, and rejoiced: the jailor's house by lamplight, a table
    with bread and a jug, Paul and Silas sitting at it, the jailor and his household about them."""
    from ecc.art import loaf
    bg, b = _house(w, h, seed, "night")
    o = [mk.defs(p, *ALL), bg, glow(w * 0.5, h * 0.5, w * 0.4, "#FFC14D", 0.35, f"{p}t")]
    s = fit(b, max(h * 0.3, b - 200))
    ty = b - 40 * s
    o.append(f'<rect x="{f(w * 0.3)}" y="{f(ty)}" width="{f(w * 0.4)}" height="{f(14 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>' + loaf(w * 0.42, ty - 2, s * 0.6) + loaf(w * 0.56, ty - 2, s * 0.6))
    o.append(seated(w * 0.26, b, s * 0.8, ROBES["paul"], head="#5A4A3A", beard="#3A2A1A") + seated(w * 0.74, b, s * 0.8, "#2A4A6A", head="#2A4A6A", beard="#2A1A10", flip=True))
    o.append(jailor(p, w * 0.5, b - 50 * s, s * 0.82, up=UP_HIGH) + woman_fig(p, w * 0.88, b, s * 0.9, "#6A4A3A", "#3A3A4A", flip=True))
    return "".join(o)

def prison_gate(p, w, h, seed, brought=False):
    """The prison gate of Philippi by day: the serjeants come with their rods; brought=True the magistrates themselves at
    the gate, besought, bringing Paul and Silas out."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), f'<rect x="-10" y="{f(h * 0.2)}" width="{f(w * 0.5)}" height="{f(b)}" fill="#6A5A54" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="{f(w * 0.14)}" y="{f(h * 0.44)}" width="{f(w * 0.16)}" height="{f(b - h * 0.44)}" fill="{"#1A1418" if brought else "#3A3A44"}" stroke="{INK}" stroke-width="2.4"></rect>',
         houses(w, h, h * 0.7, seed, x0=w * 0.5, hmin=0.24, hmax=0.34, stairs=False), pavement(w, h, h * 0.7)]
    s = fit(b, max(h * 0.3, b - 200))
    if brought:
        o.append(paul(p, w * 0.36, b, s) + silas(p, w * 0.46, b, s) + magistrate(p, w * 0.62, b, s, flip=True, up=UP_BLESS) + magistrate(p, w * 0.74, b, s, flip=True) + serjeant(p, w * 0.86, b, s, flip=True))
    else:
        o.append(serjeant(p, w * 0.6, b, s, flip=True) + serjeant(p, w * 0.7, b, s, flip=True) + jailor(p, w * 0.4, b, s))
    return "".join(o)

def jason_door(p, w, h, seed):
    """The uproar at Thessalonica: a crowd of the rabble at the shut door of Jason's house, fists lifted and torches; Jason
    and certain brethren led away before the rulers of the city (no blow drawn)."""
    bg, b = _street(w, h, seed, "dusk")
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    o.append(crowd(p, w * 0.06, w * 0.5, b, b - 170 * s, 7, seed, up=UP_HIGH))
    o.append(man_fig(p, w * 0.66, b, s, "#5A6A7A", hr="#2A1A10", bd="#2A1A10") + man_fig(p, w * 0.76, b, s * 0.98, "#6A4A3A", head="#6A5A3A", bd="#3A2A1A"))
    o.append(toga_fig(p, w * 0.9, b, s, hr="#6A645E", border="#1F5FAD", flip=True, up=UP_BLESS))
    return "".join(o)

def berea(p, w, h, seed):
    """At Berœa they examined the scriptures daily: the synagogue, the scrolls open on the reading-desk, men bending over
    them, Paul and Silas standing by."""
    bg, b = _synagogue(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    k = s
    o.append(f'<rect x="{f(w * 0.42)}" y="{f(b - 70 * k)}" width="{f(w * 0.22)}" height="{f(70 * k)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>'
             + scroll(w * 0.53, b - 78 * k, 120 * k, 26 * k, lines=3))
    o.append(paul(p, w * 0.2, b, s, flip=True, up=UP_BLESS) + silas(p, w * 0.1, b, s, flip=True))
    o.append(man_fig(p, w * 0.36, b, s * 0.98, "#3A4A6A", head="#3A4A6A", cord="#E8B830", bd="#6A645E", flip=True) + man_fig(p, w * 0.72, b, s * 0.98, "#6A5A3A", head="#E8E2D6", bd="#2A1A10")
             + woman_fig(p, w * 0.84, b, s * 0.9, "#5A2A4A", "#2A2A4A", flip=True))
    return "".join(o)

def night_road(p, w, h, seed, who=("paul", "silas"), harbour=False):
    """Sent away by night: the road out of the city under the stars, the travellers with their staves; harbour=True the road
    going down to the sea and a ship waiting (harbour=True)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#1E1650"), mk.stars(50, w, h * 0.5, seed), moon_(w * 0.84, h * 0.16, max(8, h * 0.035)),
         hills(w, h, h * 0.56, seed, color="#14142E", amp=14, step=90), ground(w, h, h * 0.64, "#1E1E36", dy=0)]
    if harbour:
        o.append(sea_(w, h, h * 0.62, seed, color="#0F2A4A", deep="#0B1A2E") + ship(w * 0.8, h * 0.7, max(0.4, h / 600)))
    o.append(f'<path d="M-10 {f(h + 10)} C {f(w * 0.3)} {f(h * 0.84)} {f(w * 0.5)} {f(h * 0.7)} {f(w * 0.66)} {f(h * 0.64)}" stroke="#3A3A56" stroke-width="{f(max(10, h * 0.07))}" fill="none"></path>')
    s = fit(b, max(h * 0.3, b - 200))
    for i, wh in enumerate(who):
        o.append(WHO[wh](p, w * (0.36 - 0.12 * i), b, s * (1 - 0.02 * i), flip=True))
    return "".join(o)
