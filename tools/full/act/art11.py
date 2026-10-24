"""Drawings for Acts 19–20. Ephesus: the twelve disciples and the hands laid on them (light falling from above); the school
of Tyrannus; the handkerchiefs and aprons carried from Paul to the sick (evil spirits never drawn); the sons of Sceva (19:16)
told in words only over the house door, shut, a torn cloak on the step; the books of the magical arts burning in a heap in
the street, the crowd watching; Demetrius' workshop and the little silver shrines; the temple of Diana far off (an object:
a great white temple); the theatre of Ephesus packed with the crowd crying out, Gaius and Aristarchus brought in (no blow
drawn), Alexander beckoning; the town-clerk quieting the multitude. The road through Macedonia on the map; Troas: the upper
chamber and its many lamps, Eutychus sitting in the window, then the window empty (his fall told in words over the window
and the lamps), then the lad brought alive at break of day; the voyage by Assos and Mitylene to Miletus on the map; the
elders of Ephesus on the shore at Miletus, the grievous wolves among the flock, and the farewell — kneeling on the shore,
the ship waiting. Built on act.art10."""
from act.art10 import *
from act.art import f, INK, HEB, TWELVE, LIE, _porch, _temple, _hall, _prison, _street, _upper, _house, _synagogue, _gate, _road
import random, math
from mat.art2 import wolves

def demetrius(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#7A5A3A", hr="#4A3A2A", bd="#4A3A2A", kind="Tunic", flip=flip, up=up,
                                                                extra='<path d="M-24 -100 L 24 -100 L 22 -40 L -22 -40 Z" fill="#5A3A22" stroke="#0D0D0F" stroke-width="1.6"></path>')
def townclerk(p, x, y, s, flip=False, up=None): return toga_fig(p, x, y, s, hr="#8A847A", border="#2A4A6A", flip=flip, up=up)
def eutychus(p, x, y, s, flip=False, up=None): return man_fig(p, x, y, s, "#C8A060", hr="#3A2214", kind="Tunic", flip=flip, up=up)
WHO.update({"demetrius": demetrius, "townclerk": townclerk, "eutychus": eutychus})

def tyrannus(p, w, h, seed):
    """Reasoning daily in the school of Tyrannus: a lecture hall with a raised chair and tiers of benches, Paul standing to
    teach, Jews and Greeks sitting before him."""
    bg, b = _hall(w, h, seed, "day")
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    o.append(paul(p, w * 0.18, b, s, flip=True, up=UP_BLESS))
    for i, x in enumerate((0.38, 0.5, 0.62, 0.74, 0.86)):
        if i % 2: o.append(seated(w * x, b, s * 0.78, ["#6A5A3A", "#E8E2D6", "#3A4A6A", "#C8C0B0", "#5A2A4A"][i], head=None, beard="#9A948A", flip=True))
        else: o.append(seated(w * x, b, s * 0.78, ["#6A5A3A", "#E8E2D6", "#3A4A6A", "#C8C0B0", "#5A2A4A"][i], head=["#E8E2D6", None, "#3A4A6A", None, "#2A2A3A"][i], beard="#2A1A10", flip=True))
    return "".join(o)

def handkerchiefs(p, w, h, seed):
    """Handkerchiefs or aprons carried from his body unto the sick: a house of the sick, a woman bringing in a white cloth to
    the one on the bed, light coming with it (the spirits are never drawn)."""
    bg, b = _house(w, h, seed)
    o = [mk.defs(p, *ALL, *LIE), bg, glow(w * 0.4, b - h * 0.2, h * 0.4, "#FFF4C2", 0.5, f"{p}h")]
    s = fit(b, max(h * 0.3, b - 200))
    o.append(on_bed(p, w * 0.6, b - 26 * s, 220 * s, cloth="#8A9AAA"))
    cloth = '<path d="M-66 -150 L -40 -152 L -42 -118 L -64 -116 Z" fill="#F8F4EC" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(woman_fig(p, w * 0.3, b, s, "#5A6A4A", "#2A4A5A", up=[(22, -158), (44, -150), (62, -150)], extra=cloth.replace("-66", "66").replace("-40", "40").replace("-42", "42").replace("-64", "64")))
    o.append(man_fig(p, w * 0.86, b, s, "#6A5A3A", head="#E8E2D6", bd="#6A645E", flip=True))
    return "".join(o)

def sceva_door(p, w, h, seed):
    """The house of the sons of Sceva: its door shut, a torn cloak lying on the step — what was done within told in words
    only (the evil spirit is never drawn)."""
    bg, b = _street(w, h, seed, "dusk")
    o = [bg]
    k = max(0.6, h / 300)
    dx = w * 0.42
    o.append(f'<rect x="{f(dx - 10)}" y="{f(b - 200 * k)}" width="{f(w * 0.2)}" height="{f(200 * k)}" fill="#E8D8B0" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(dx + 10 * k)}" y="{f(b - 130 * k)}" width="{f(w * 0.2 - 40 * k)}" height="{f(130 * k)}" fill="#5A3A22" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M{f(dx + w * 0.1 - 10)} {f(b - 130 * k)} L {f(dx + w * 0.1 - 10)} {f(b)}" stroke="#2A1A10" stroke-width="2"></path>'
             f'<path d="M{f(dx + 30 * k)} {f(b + 2)} C {f(dx + 40 * k)} {f(b - 14 * k)} {f(dx + 90 * k)} {f(b - 16 * k)} {f(dx + 110 * k)} {f(b + 2)} L {f(dx + 80 * k)} {f(b - 4 * k)} L {f(dx + 66 * k)} {f(b + 2)} Z" fill="#8A7A9A" stroke="{INK}" stroke-width="1.6"></path>')
    return "".join(o)

def books_burned(p, w, h, seed):
    """They brought their books together and burned them in the sight of all: a heap of scrolls and codices burning in the
    street of Ephesus, those who had practised the arts bringing more, the people standing about."""
    bg, b = _street(w, h, seed, "dusk")
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.3, b - 200))
    cx = w * 0.5; k = s
    for i in range(10):
        x = cx + (i - 4.5) * 14 * k; y = b - (i % 3) * 10 * k
        o.append(f'<rect x="{f(x - 22 * k)}" y="{f(y - 12 * k)}" width="{f(44 * k)}" height="{f(12 * k)}" rx="{f(6 * k)}" fill="{["#E8D8B0", "#C8A878", "#8A5A3A"][i % 3]}" stroke="{INK}" stroke-width="1.4" transform="rotate({(i * 23) % 40 - 20} {f(x)} {f(y)})"></rect>')
    o.append(glow(cx, b - 60 * k, 160 * k, "#FF8A3D", 0.6, f"{p}f") + E.blaze(cx, b, 110 * k, 130 * k, seed, n=6))
    scrolls = '<rect x="-54" y="-136" width="30" height="12" rx="6" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.4"></rect>'
    o.append(man_fig(p, w * 0.24, b, s, "#4A2A5A", head="#2A1A3A", bd="#1A1210", up=[(22, -158), (40, -140), (56, -134)]) + man_fig(p, w * 0.12, b, s, "#6A4A3A", hr="#2A1A10", bd="#2A1A10", flip=True, extra=scrolls))
    o.append(crowd(p, w * 0.7, w * 0.96, b, b - 170 * s, 4, seed, flip=True))
    return "".join(o)

def silver_shrine(x, base, s, color="#C8C8D0"):
    """A little silver shrine of Diana: a model temple of silver with its columns and pediment, an object for sale."""
    u = s
    return (f'<rect x="{f(x - 22 * u)}" y="{f(base - 6 * u)}" width="{f(44 * u)}" height="{f(6 * u)}" fill="{color}" stroke="{INK}" stroke-width="1.2"></rect>'
            + "".join(f'<rect x="{f(x - 18 * u + 9 * j * u)}" y="{f(base - 30 * u)}" width="{f(3 * u)}" height="{f(24 * u)}" fill="{color}" stroke="{INK}" stroke-width="1"></rect>' for j in range(5))
            + f'<path d="M{f(x - 24 * u)} {f(base - 30 * u)} L {f(x)} {f(base - 42 * u)} L {f(x + 24 * u)} {f(base - 30 * u)} Z" fill="{color}" stroke="{INK}" stroke-width="1.2"></path>')

def workshop(p, w, h, seed, gathered=True):
    """Demetrius the silversmith's workshop: the bench of little silver shrines of Diana, the furnace glowing; Demetrius in his
    leather apron haranguing the craftsmen gathered about him."""
    bg, b = _house(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    k = max(0.5, h / 320)
    ty = b - 70 * k
    o.append(f'<rect x="{f(w * 0.06)}" y="{f(ty)}" width="{f(w * 0.36)}" height="{f(12 * k)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(5):
        o.append(silver_shrine(w * (0.1 + 0.07 * i), ty, k * 0.8))
    o.append(glow(w * 0.9, b - 40 * k, 80 * k, "#FF8A3D", 0.6, f"{p}fn") + f'<path d="M{f(w * 0.84)} {f(b)} L {f(w * 0.84)} {f(b - 70 * k)} Q {f(w * 0.9)} {f(b - 100 * k)} {f(w * 0.96)} {f(b - 70 * k)} L {f(w * 0.96)} {f(b)} Z" fill="#6A4A3A" stroke="{INK}" stroke-width="2"></path>'
             + E.blaze(w * 0.9, b - 6 * k, 30 * k, 30 * k, seed, n=4))
    s = fit(b, max(h * 0.3, b - 200))
    o.append(demetrius(p, w * 0.5, b, s, flip=True, up=UP_HIGH))
    if gathered:
        for i, x in enumerate((0.62, 0.72, 0.8)):
            o.append(man_fig(p, w * x, b, s * 0.96, ["#6A5A3A", "#5A4A4A", "#7A6A4A"][i], hr="#2A1A10", bd=["#2A1A10", None, "#4A3A2A"][i], kind="Tunic", up=UP_HIGH if i == 1 else None))
    return "".join(o)

def diana_temple(x, base, wd):
    """The temple of the great goddess Diana at Ephesus, far off: a vast white temple of many columns on its platform."""
    u = wd / 100
    o = [f'<rect x="{f(x - 50 * u)}" y="{f(base - 8 * u)}" width="{f(100 * u)}" height="{f(8 * u)}" fill="#D8D0C0" stroke="{INK}" stroke-width="1.6"></rect>']
    for k in range(12):
        cx = x - 46 * u + k * 8.4 * u
        o.append(f'<rect x="{f(cx - 2 * u)}" y="{f(base - 40 * u)}" width="{f(4 * u)}" height="{f(32 * u)}" fill="#F8F4EC" stroke="{INK}" stroke-width="1"></rect>')
    o.append(f'<rect x="{f(x - 50 * u)}" y="{f(base - 46 * u)}" width="{f(100 * u)}" height="{f(6 * u)}" fill="#E8E0D0" stroke="{INK}" stroke-width="1.4"></rect>'
             f'<path d="M{f(x - 50 * u)} {f(base - 46 * u)} L {f(x)} {f(base - 60 * u)} L {f(x + 50 * u)} {f(base - 46 * u)} Z" fill="#E8E0D0" stroke="{INK}" stroke-width="1.6"></path>')
    return "".join(o)

def theatre(p, w, h, seed, alexander=False, quiet=False, empty=False):
    """The theatre of Ephesus: the great half-bowl of stone seats rising up the hill, packed with the multitude crying out with
    their hands lifted, the stage below, the temple of Diana far off beyond; alexander=True a man in a striped robe on the
    stage beckoning with his hand; quiet=True the town-clerk on the stage, the crowd's hands down; empty=True the theatre
    empty after the assembly was dismissed."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), diana_temple(w * 0.84, h * 0.2, w * 0.24)]
    r = random.Random(seed)
    rows = 7
    for i in range(rows):
        y0 = h * (0.24 + 0.08 * i)
        o.append(f'<path d="M-10 {f(y0)} C {f(w * 0.3)} {f(y0 + h * 0.06)} {f(w * 0.7)} {f(y0 + h * 0.06)} {f(w + 10)} {f(y0)} L {f(w + 10)} {f(y0 + h * 0.08)} C {f(w * 0.7)} {f(y0 + h * 0.14)} {f(w * 0.3)} {f(y0 + h * 0.14)} -10 {f(y0 + h * 0.08)} Z" fill="{"#D8D0C0" if i % 2 else "#C8C0B0"}" stroke="{INK}" stroke-width="1.4"></path>')
        if not empty:
            hp = h * (0.07 + 0.008 * i)
            n = int(w / (hp * 0.62))
            for j in range(n):
                t = (j + 0.5 + (i % 2) * 0.5) / n; x = w * t; y = y0 + h * 0.06 * (1 - (2 * t - 1) ** 2) + h * 0.075
                c = r.choice(["#8A2A2A", "#1F5A6A", "#5A2A7A", "#C8783A", "#2A4A2A", "#6A5A3A", "#3A3A6A", "#E8E2D6", "#B5583A"])
                up = (not quiet) and r.random() < 0.45
                hx = x + (hp * 0.22 if up else 0)
                o.append(f'<path d="M{f(x - hp * 0.24)} {f(y)} C {f(x - hp * 0.26)} {f(y - hp * 0.5)} {f(x - hp * 0.2)} {f(y - hp * 0.66)} {f(x)} {f(y - hp * 0.68)} '
                         f'C {f(x + hp * 0.2)} {f(y - hp * 0.66)} {f(x + hp * 0.26)} {f(y - hp * 0.5)} {f(x + hp * 0.24)} {f(y)} Z" fill="{c}" stroke="{INK}" stroke-width="1"></path>'
                         f'<circle cx="{f(x)}" cy="{f(y - hp * 0.82)}" r="{f(hp * 0.15)}" fill="#B98A6E" stroke="{INK}" stroke-width="1"></circle>'
                         + (f'<path d="M{f(x + hp * 0.14)} {f(y - hp * 0.56)} L {f(x + hp * 0.3)} {f(y - hp * 1.05)}" stroke="{INK}" stroke-width="{f(max(2.4, hp * 0.12))}" stroke-linecap="round"></path>'
                            f'<path d="M{f(x + hp * 0.14)} {f(y - hp * 0.56)} L {f(x + hp * 0.3)} {f(y - hp * 1.05)}" stroke="#B98A6E" stroke-width="{f(max(1.4, hp * 0.08))}" stroke-linecap="round"></path>' if up else ""))
    o.append(f'<rect x="-10" y="{f(b - h * 0.1)}" width="{f(w + 20)}" height="{f(h)}" fill="#B8A88A" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.5, b - 150))
    if alexander:
        o.append(man_fig(p, w * 0.5, b, s, "#3A4A6A", head="#E8E2D6", bd="#2A1A10", up=UP_HIGH))
    if quiet:
        o.append(townclerk(p, w * 0.5, b, s, up=UP_BLESS))
    return "".join(o)

def troas_chamber(p, w, h, seed, stage="sit"):
    """The upper chamber at Troas at night, three stories up, many lights burning; stage "sit" — Paul discoursing, the
    disciples about the table, Eutychus sitting in the open window; "fell" — the window empty, only the lamps (his fall told
    in words); "alive" — at break of day, the lad standing alive among them."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#4A3A3A", floor="#3A2E2A")]
    wx, wy, ww, wh = w * 0.72, h * 0.2, w * 0.18, h * 0.42
    o.append(f'<rect x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(wh)}" fill="{"#0B0B2A" if stage != "alive" else "#8A6AA0"}" stroke="{INK}" stroke-width="3"></rect>'
             f'<g transform="translate({f(wx)} {f(wy)})">' + mk.stars(8, ww, wh * 0.8, seed) + '</g>')
    for i, x in enumerate((0.1, 0.24, 0.38, 0.52)):
        o.append(glow(w * x, h * 0.26, h * 0.12, "#FFC14D", 0.5, f"{p}l{i}") + A.lamp(w * x, h * 0.26, max(0.5, h / 420)))
    s = fit(b, max(h * 0.3, b - 200))
    if stage == "sit":
        es = s * 0.6
        o.append(seated(wx + ww * 0.5, wy + wh, es * 0.9, "#C8A060", head=None, beard=None, bowed=True))
    o.append(paul(p, w * 0.18, b, s, flip=True, up=UP_BLESS if stage == "sit" else None))
    for i, x in enumerate((0.34, 0.46, 0.58)):
        o.append(seated(w * x, b, s * 0.76, TWELVE[i + 3], head=TWELVE[i + 3] if i % 2 else None, beard="#2A1A10", flip=True))
    if stage == "alive":
        o.append(glow(w * 0.68, b - 110 * s, 120 * s, "#FFF4C2", 0.6, f"{p}a") + eutychus(p, w * 0.68, b, s * 0.94, up=UP_HIGH))
    return "".join(o)

def miletus(p, w, h, seed, kneel=False):
    """The shore at Miletus: the elders of the church of Ephesus come down to Paul, standing about him on the beach; the
    ship at anchor; kneel=True Paul kneeling with them all in prayer, the elders weeping, then bringing him to the ship."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), sea_(w, h, h * 0.5, seed), ship(w * 0.82, h * 0.58, max(0.4, h / 560)), shore(w, h, h * 0.66, color="#D8C090")]
    s = fit(b, max(h * 0.3, b - 200))
    if kneel:
        o.append(E.kneel(w * 0.3, b, s * 0.86, color=ROBES["paul"], skin=SKIN, flip=True))
        for i, x in enumerate((0.44, 0.56, 0.68)):
            o.append(E.kneel(w * x, b, s * 0.84, color=["#6A5A3A", "#3A4A6A", "#E8E2D6"][i], skin=SKIN))
        o.append(elder(p, w * 0.14, b, s, up=[(22, -158), (14, -176), (8, -190)]))
    else:
        o.append(paul(p, w * 0.2, b, s, flip=True, up=UP_BLESS))
        for i, x in enumerate((0.36, 0.46, 0.56, 0.66)):
            o.append(man_fig(p, w * x, b, s * (1 - 0.02 * i), ["#6A5A3A", "#3A4A6A", "#E8E2D6", "#5A2A4A"][i], head=["#E8E2D6", "#3A4A6A", "#F3EFE6", None][i], hr="#2A1A10",
                             bd=["#6A645E", "#2A1A10", "#9A948A", "#3A2A1A"][i], flip=True))
    return "".join(o)
