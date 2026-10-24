"""Drawings for Acts 3–6: the gate of the temple called Beautiful and the lame man; Solomon's porch; the ward at eventide;
the council (the rulers, elders and scribes seated in a half-circle about the high priest, the accused standing in the
midst); the company praying and the place shaken; the money laid at the apostles' feet; the empty floor and the door
(Ananias and Sapphira, told in words only); the prison doors opened by night; the council's door (the beating told in
words only); the seven chosen and the hands laid on them. Built on act.art."""
from act.art import *
from act.art import f, INK, HEB, TWELVE, LIE, _porch, _temple, _hall, _prison, _street, _upper, _house, _synagogue
import random, math

GATE_BRONZE = "#C8963E"

def beautiful_gate(p, w, h, seed, stage="ask"):
    """The door of the temple which is called Beautiful: the great doors of Corinthian brass in the white wall of the court,
    the lame man laid at the side on his mat. stage: "ask" — he sits holding out his hand to Peter and John coming up;
    "look" — Peter fastening his eyes on him, John beside; "raise" — Peter has taken him by the right hand and raised him up;
    "leap" — he leaps up, his arms lifted, and goes in with them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"),
         f'<rect x="-10" y="{f(h * 0.12)}" width="{f(w + 20)}" height="{f(b - h * 0.12)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(h * 0.08)}" width="{f(w + 20)}" height="{f(h * 0.05)}" fill="#D8C8A0" stroke="{INK}" stroke-width="2"></rect>']
    gx, gw = w * 0.3, w * 0.26
    o.append(f'<path d="M{f(gx - gw / 2 - 12)} {f(b)} L {f(gx - gw / 2 - 12)} {f(h * 0.3)} Q {f(gx)} {f(h * 0.1)} {f(gx + gw / 2 + 12)} {f(h * 0.3)} L {f(gx + gw / 2 + 12)} {f(b)} Z" fill="#D8C8A0" stroke="{INK}" stroke-width="2.4"></path>')
    o.append(f'<path d="M{f(gx - gw / 2)} {f(b)} L {f(gx - gw / 2)} {f(h * 0.34)} Q {f(gx)} {f(h * 0.17)} {f(gx + gw / 2)} {f(h * 0.34)} L {f(gx + gw / 2)} {f(b)} Z" fill="{GATE_BRONZE}" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(gx)} {f(h * 0.255)} L {f(gx)} {f(b)}" stroke="{INK}" stroke-width="2.4"></path>')
    for k in range(1, 4):
        y = h * 0.34 + (b - h * 0.34) * k / 4
        o.append(f'<path d="M{f(gx - gw / 2 + 6)} {f(y)} L {f(gx + gw / 2 - 6)} {f(y)}" stroke="#8A6A2A" stroke-width="2.4"></path>')
        o.append("".join(f'<circle cx="{f(gx - gw / 2 + gw * (j + 0.5) / 8)}" cy="{f(y - (b - h * 0.34) / 8)}" r="{f(max(2, h * 0.008))}" fill="#E8B830" stroke="{INK}" stroke-width="1"></circle>' for j in range(8)))
    o.append(pavement(w, h, b - h * 0.04, color="#C8B898"))
    s = fit(b, max(h * 0.26, b - 220))
    mx = w * 0.52
    if stage in ("ask", "look"):
        o.append(bedroll(mx + 20 * s, b - 6, 150 * s, 10 * s))
        o.append(f'<ellipse cx="{f(mx + 70 * s)}" cy="{f(b - 10)}" rx="{f(16 * s)}" ry="{f(6 * s)}" fill="#8A5A3A" stroke="{INK}" stroke-width="1.6"></ellipse>')
        o.append(seated(mx, b - 6, s * 0.8, "#8A7A5A", head="#6A5A3A", beard="#3A2A1E"))
        if stage == "ask":
            o.append(peter(p, w * 0.8, b, s) + john_ap(p, w * 0.9, b, s * 0.98))
            o.append(crowd(p, w * 0.04, w * 0.14, b, b - 180 * s, 2, seed))
        else:
            o.append(peter(p, w * 0.72, b, s, up=UP_TOUCH) + john_ap(p, w * 0.82, b, s * 0.98))
    elif stage == "raise":
        o.append(bedroll(mx - 30 * s, b - 6, 150 * s, 10 * s))
        o.append(man_fig(p, mx + 10 * s, b, s * 0.96, "#8A7A5A", head="#6A5A3A", bd="#3A2A1E", flip=True, up=[(22, -158), (36, -150), (52, -150)]))
        o.append(peter(p, mx + 120 * s, b, s, up=UP_BLESS) + john_ap(p, mx + 200 * s, b, s * 0.98))
    else:
        o.append(glow(w * 0.48, b - 120 * s, 140 * s, "#FFF4C2", 0.7, f"{p}j") + man_fig(p, w * 0.48, b - 30 * s, s, "#8A7A5A", head="#6A5A3A", bd="#3A2A1E", up=UP_HIGH))
        o.append(peter(p, w * 0.62, b, s) + john_ap(p, w * 0.72, b, s * 0.98))
        o.append(crowd(p, w * 0.82, w * 0.96, b, b - 180 * s, 2, seed, flip=True))
    return "".join(o)

def porch_crowd(p, w, h, seed, peter_up=True):
    """All the people ran together unto them in the porch that is called Solomon's: the colonnade, the healed man holding
    to Peter and John, the people pressing in from every side."""
    bg, b = _porch(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.28, b - 210))
    o.append(crowd(p, w * 0.5, w * 0.94, b - 40 * s, b - 40 * s - 170 * s, 7, seed + 1, flip=True))
    o.append(peter(p, w * 0.14, b, s, flip=True, up=UP_HIGH if peter_up else None) + man_fig(p, w * 0.25, b, s * 0.96, "#8A7A5A", head="#6A5A3A", bd="#3A2A1E")
             + john_ap(p, w * 0.34, b, s * 0.98))
    o.append(crowd(p, w * 0.46, w * 0.9, b, b - 180 * s, 5, seed + 2, flip=True))
    return "".join(o)

def ward(p, w, h, seed, who=("peter", "john")):
    """Put in ward unto the morrow, for it was now eventide: the stone cell, the last red light at the barred window, the
    two sitting on the straw."""
    bg, b = _prison(w, h, seed)
    o = [bg, glow(w * 0.75, h * 0.16, h * 0.3, "#FF8A3D", 0.5, f"{p}w")]
    s = fit(b, max(h * 0.3, b - 200))
    cols = {"peter": (ROBES["peter"], None, "#4A4440"), "john": (ROBES["john"], None, None), "paul": (ROBES["paul"], "#5A4A3A", "#3A2A1A"),
            "silas": ("#2A4A6A", "#2A4A6A", "#2A1A10")}
    for i, wh in enumerate(who):
        c, hd, bd = cols[wh]
        o.append(seated(w * (0.32 + 0.24 * i), b, s * 0.82, c, head=hd, beard=bd, flip=i == 1, bowed=False))
    return "".join(o)

def council(p, w, h, seed, accused=("peter", "john"), healed=False, empty=False, standing=None, tone="council"):
    """The council: the rulers, elders and scribes seated on the stone benches in a half-circle, the high priest in white on
    his seat in the midst at the back, under the lamp; the accused standing in the midst before them (accused: names in
    WHO); healed=True the man that was healed standing with them; empty=True the council alone, conferring; standing= one
    of the council standing up to speak (an x)."""
    bg, b = _hall(w, h, seed, tone)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.28, b - 210))
    # back row on a raised step
    st = b - 46 * s
    o.append(f'<rect x="-10" y="{f(st)}" width="{f(w + 20)}" height="{f(b - st + 2)}" fill="#6A5A54" stroke="{INK}" stroke-width="2"></rect>')
    r = random.Random(seed)
    for i, x in enumerate((0.1, 0.22, 0.34, 0.66, 0.78, 0.9)):
        hd = ["#F3EFE6", "#3A4A6A", "#3A2A4A", "#F3EFE6", "#6A2A3A", "#3A4A6A"][i]
        o.append(seated(w * x, st, s * 0.7, "#E8E2D6" if hd == "#F3EFE6" else hd, head=hd, beard=["#9A948A", "#3A2A1A", "#6A645E"][i % 3], flip=x > 0.5, band=True))
    o.append(f'<rect x="{f(w * 0.44)}" y="{f(st - 70 * s)}" width="{f(w * 0.12)}" height="{f(70 * s)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>')
    o.append(seated(w * 0.5, st - 40 * s, s * 0.74, "#E8E2D6", head="#F3EFE6", beard="#9A948A", band=True, flip=True))
    if standing is not None:
        o.append(man_fig(p, w * standing, b, s, "#2A3A5A", head="#2A3A5A", cord="#E8B830", bd="#E8E2D6", flip=standing < 0.5, up=UP_BLESS))
    if not empty:
        xs = [0.4, 0.5, 0.6][:len(accused)] if len(accused) < 3 else [0.36, 0.46, 0.56]
        if len(accused) == 1: xs = [0.5]
        if len(accused) == 2: xs = [0.44, 0.56]
        for x, who in zip(xs, accused):
            o.append(WHO[who](p, w * x, b, s, flip=x > 0.5))
        if healed: o.append(man_fig(p, w * 0.66, b, s * 0.96, "#8A7A5A", head="#6A5A3A", bd="#3A2A1E", flip=True))
    else:
        for x in (0.3, 0.42, 0.58, 0.7):
            o.append(scribe_fig(p, w * x, b, s * 0.94, white=x in (0.42, 0.7), flip=x > 0.5, up=UP_BLESS if x == 0.42 else None))
    return "".join(o)

def company_pray(p, w, h, seed, shaken=False):
    """They lifted up their voice to God with one accord: the company in the upper chamber standing with their hands lifted;
    shaken=True the place shaken — the lamps swinging, dust falling from the beams, a great light on them all."""
    bg, b = _upper(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    if shaken:
        r = random.Random(seed)
        o.append(f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#FFF4C2" opacity="0.25"></rect>' + glow(w * 0.5, h * 0.2, w * 0.5, "#FFFFFF", 0.7, f"{p}sh"))
        for _ in range(26):
            x = r.uniform(0, w); y = r.uniform(h * 0.12, h * 0.6)
            o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(1, 3))}" fill="#8A6A4A" opacity="0.7"></circle>')
        for x in (0.02, 0.98):
            o.append(f'<path d="M{f(w * x)} {f(h * 0.2)} l {f(8 if x < 0.5 else -8)} 10 l {f(-8 if x < 0.5 else 8)} 10 l {f(8 if x < 0.5 else -8)} 10" stroke="{INK}" stroke-width="3" fill="none"></path>')
    s = fit(b, max(h * 0.28, b - 210))
    for i in range(8):
        x = w * (0.08 + 0.12 * i)
        if i in (3, 6):
            o.append(woman_fig(p, x, b - (i % 2) * 6, s * 0.9, ["#6A4A5A", "#2A4A7A"][i == 6], ["#3A3A5A", "#3A6AA8"][i == 6], flip=i > 3, up=UP_HIGH))
        else:
            o.append(apostle(p, x, b - (i % 2) * 6, s * (0.96 + 0.04 * (i % 2)), i, flip=i > 3, up=UP_HIGH if i % 2 == 0 else None))
    return "".join(o)

def at_feet(p, w, h, seed, giver="barnabas", kneeling=True, money=True):
    """Laid it at the apostles' feet: the apostles standing in the porch, the giver kneeling before them setting down a purse of
    money; giver = "barnabas" (green), "ananias" (dull olive) or a colour."""
    bg, b = _porch(w, h, seed)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.28, b - 210))
    for i, x in enumerate((0.56, 0.66, 0.76, 0.86, 0.95)):
        o.append(apostle(p, w * x, b, s * (1 - 0.02 * i), i, flip=True))
    c = {"barnabas": "#3A6A3A", "ananias": "#5A5A3A"}.get(giver, giver)
    if kneeling:
        o.append(E.kneel(w * 0.38, b, s * 0.9, color=c, skin=SKIN))
    else:
        o.append(man_fig(p, w * 0.38, b, s, c, head=c, cord="#2A1A10", bd="#4A2A1A", flip=True, up=UP_TOUCH))
    if money:
        k = s
        o.append(f'<path d="M{f(w * 0.48)} {f(b)} C {f(w * 0.46)} {f(b - 26 * k)} {f(w * 0.5)} {f(b - 34 * k)} {f(w * 0.5)} {f(b - 40 * k)} L {f(w * 0.52)} {f(b - 40 * k)} C {f(w * 0.52)} {f(b - 34 * k)} {f(w * 0.56)} {f(b - 26 * k)} {f(w * 0.54)} {f(b)} Z" fill="#8A5A2A" stroke="{INK}" stroke-width="2"></path>')
        for j in range(5):
            o.append(f'<ellipse cx="{f(w * (0.44 + 0.02 * j))}" cy="{f(b - 2)}" rx="{f(6 * k)}" ry="{f(3 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="1"></ellipse>')
    return "".join(o)

def kings_array(p, w, h, seed):
    """The kings of the earth set themselves in array: against a red sky, kings in crowns and their spearmen ranged in lines
    on the ridge, banners lifted."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#3A0A10", "#C8401A"), hills(w, h, h * 0.62, seed, color="#3A1418", amp=14, step=80), ground(w, h, h * 0.72, "#2A1014", dy=0)]
    s = fit(b, max(h * 0.3, b - 200))
    r = random.Random(seed)
    for x in (0.18, 0.5, 0.82):
        o.append(f'<path d="M{f(w * x)} {f(h * 0.74)} L {f(w * x)} {f(h * 0.3)}" stroke="#1A0A0C" stroke-width="3"></path><path d="M{f(w * x)} {f(h * 0.3)} L {f(w * x + 50)} {f(h * 0.34)} L {f(w * x)} {f(h * 0.4)} Z" fill="#8A0E16" stroke="#0D0D0F" stroke-width="1.4"></path>')
    spear = '<path d="M24 -150 L 34 -250" stroke="#2A1A10" stroke-width="4"></path><path d="M34 -250 l -5 -14 l 9 3 Z" fill="#C8C8D0" stroke="#0D0D0F" stroke-width="1"></path>'
    for row, (y, k) in enumerate(((h * 0.74, 0.5), (b, 1.0))):
        n = 12 if row == 0 else 6
        for i in range(n):
            x = w * (0.04 + 0.92 * i / (n - 1)) + r.uniform(-6, 6)
            if row == 1 and i % 2 == 0:
                o.append(king_fig(p, x, y, s * k, cloth=r.choice(["#5A1A6A", "#8A1A1A", "#1F3A6A"]), bd=r.choice(["#2A1A10", "#6A645E"]), flip=i > 2))
            else:
                o.append(silhouette(mk.person(p, round(x), round(y), round(s * k, 3), body="#1A0A0C", cloth="#1A0A0C", kind="Tunic", sw=2, flip=i > n / 2, extra=spear), "#1A0A0C"))
    return "".join(o)
