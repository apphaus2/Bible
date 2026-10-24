"""Drawings for John 9–10. The man blind from his birth sitting by the way at the temple steps, the disciples asking; the clay
put on his eyes — Jesus' hand to his brow, nothing more; the pool of Siloam with its steps, the man washing and coming up
seeing; the neighbours; the man before the Pharisees in their court; his father and mother brought in, afraid; the
synagogue door shut on him, and Jesus finding him outside; Lord, I believe — the man kneeling. John 10: the stone
sheepfold on the hillside and its door; the thief's ladder against the wall at night, no one on it; the porter opening the
door, the shepherd calling his sheep and going before them; the stranger they flee from; I am the door — Jesus standing in
the doorway of the fold; the good shepherd with a lamb on his shoulders; the hireling running and the wolf at the edge of
the scattering flock (no harm drawn); other sheep, one flock; Solomon's porch in winter at the feast of the dedication;
beyond the Jordan where John first baptized. Built on jhn.art4."""
from jhn.art4 import *
from jhn.art4 import f, INK, HEB, TWELVE, P, LIE, on_bed, lying, bedroll, lame_fig, porches, jesus_stoop
import random, math
from mat.art2 import wolf

BLIND_C, BLIND_HEAD = "#6A665E", "#8A8680"                        # the man born blind: an undyed grey robe and headcloth, a brown beard
BROWN_BEARD_ = A.BLACK_BEARD.replace("#2A1A10", "#3A2214")

def blind_fig(p, x, y, s, flip=False, up=None):
    """The man that was blind, standing: an undyed grey robe and headcloth with a cord, a dark-brown beard."""
    return mk.person(p, round(x), round(y), round(s, 3), body="#B98A6E", cloth=BLIND_C, kind="Robe", sw=3, flip=flip, up=up,
                     extra=A.headcloth(BLIND_HEAD, cord="#3A2214") + BROWN_BEARD_)

def blind_seated(x, y, s, flip=False):
    return seated(x, y, s, BLIND_C, head=BLIND_HEAD, beard="#3A2214", flip=flip)

def parents_fig(p, x, y, s, flip=False):
    """His father (white-bearded, a brown headcloth) and his mother (a dark-olive veil), standing close together."""
    return (mk.person(p, round(x), round(y), round(s, 3), body="#B98A6E", cloth="#6A5A44", kind="Robe", sw=3, flip=flip, extra=A.headcloth("#6A4A2A", cord="#3A2214") + A.WHITE_BEARD)
            + woman_fig(p, x + (-1 if flip else 1) * 56 * s, y, s * 0.94, "#5A5A44", "#4A5232", flip=flip))

def beggar_way(p, w, h, seed, stage="sit"):
    """By the way near the temple: the steps and a wall, the man blind from his birth sitting on the ground begging, his
    hand out. sit: Jesus and his disciples passing by, the disciples asking. anoint: Jesus stooping to him, his hand to the
    man's brow (the clay on his eyes, nothing more drawn). neighbours: the man standing up seeing, the neighbours about him
    wondering."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), walls(-w * 0.02, w * 1.02, h * 0.6, h * 0.4, seed, towers=3), ground(w, h, h * 0.62, "#C8B07A", dy=0)]
    for k in range(3):
        y = h * (0.62 + 0.04 * k)
        o.append(f'<rect x="{f(w * 0.5)}" y="{f(y)}" width="{f(w * 0.52)}" height="{f(h * 0.04)}" fill="#D8C8A8" stroke="{INK}" stroke-width="1.6"></rect>')
    s = fit(b, max(h * 0.26, b - 230))
    if stage == "neighbours":
        o.append(blind_fig(p, w * 0.42, b, s, up=UP_BLESS))
        o.append(woman_fig(p, w * 0.18, b, s * 0.94, "#7A4A3A", "#3A3A4A", flip=True) + man(p, w * 0.28, b - 6, s * 0.96, "#3A4A6A", flip=True))
        o.append(man(p, w * 0.62, b - 4, s * 0.96, "#6A5A3A", flip=False, up=UP_BLESS) + woman_fig(p, w * 0.74, b, s * 0.92, "#5A6A3A", "#2A3A4A") + man(p, w * 0.86, b - 6, s * 0.94, "#7A3A3A"))
        return "".join(o)
    o.append(blind_seated(w * 0.56, b, s * 0.88, flip=True))
    o.append(f'<path d="M{f(w * 0.56 - 50 * s)} {f(b - 4)} c 4 -6 14 -6 18 0 z" fill="#8A6A3A" stroke="{INK}" stroke-width="1.4"></path>')
    if stage == "sit":
        o.append(jesus(p, w * 0.24, b, s, flip=True))
        o.append(disciple(p, w * 0.12, b - 4, s * 0.96, "john", flip=True, up=UP_BLESS) + disciple(p, w * 0.04, b - 6, s * 0.95, "peter", flip=True))
    else:
        o.append(jesus(p, w * 0.42, b, s, flip=True, up=[(-22, -158), (-46, -132), (-70, -116)]))
        o.append(disciple(p, w * 0.2, b - 4, s * 0.96, "john", flip=True) + disciple(p, w * 0.1, b - 6, s * 0.95, "peter", flip=True))
    return "".join(o)

def siloam(p, w, h, seed, seeing=False):
    """Go, wash in the pool of Siloam: the pool below the city wall with its stone steps going down to the water; the man
    kneeling at the water's edge washing his face; seeing=True the man standing up on the steps with his arms lifted, the
    light of day full on him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), walls(-w * 0.02, w * 1.02, h * 0.36, h * 0.3, seed, towers=4),
         f'<rect x="-10" y="{f(h * 0.36)}" width="{f(w + 20)}" height="{f(h)}" fill="#D8C8A8" stroke="{INK}" stroke-width="2"></rect>']
    for k in range(5):
        y = h * (0.4 + 0.07 * k)
        o.append(f'<path d="M{f(w * (0.06 + 0.02 * k))} {f(y)} L {f(w * (0.94 - 0.02 * k))} {f(y)}" stroke="#A89878" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.14)} {f(h + 10)} L {f(w * 0.18)} {f(h * 0.76)} L {f(w * 0.82)} {f(h * 0.76)} L {f(w * 0.86)} {f(h + 10)} Z" fill="#3A8AA8" stroke="{INK}" stroke-width="2"></path>')
    for k in range(3):
        o.append(f'<path d="M{f(w * 0.24)} {f(h * (0.82 + 0.06 * k))} q {f(w * 0.1)} -4 {f(w * 0.2)} 0 t {f(w * 0.2)} 0" stroke="#BFE6F2" stroke-width="1.8" fill="none" opacity="0.7"></path>')
    s = fit(h * 0.76, max(h * 0.2, h * 0.76 - 220))
    if seeing:
        o.append(rays(w * 0.5, h * 0.3, 30, 20, w, color="#FFF4C2", op=0.25) + glow(w * 0.5, h * 0.5, h * 0.4, "#FFFFFF", 0.6, f"{p}g"))
        o.append(blind_fig(p, w * 0.5, h * 0.76, s, up=[(-22, -158), (-34, -190), (-38, -222)]))
    else:
        o.append(kneeler(w * 0.5, h * 0.78, s * 0.9, BLIND_C))
    return "".join(o)

def pharisees_court(p, w, h, seed, who="man"):
    """The court where the Pharisees sat: a colonnade, the Pharisees seated on a stone bench in white and slate-blue.
    who='man': the man that was blind standing before them; 'parents': his father and mother standing before them, afraid;
    'cast': the man being put out at the gate, a Pharisee pointing him out."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), pavement(w, h, h * 0.62)]
    for k in range(6):
        x = w * (0.04 + 0.184 * k)
        o.append(f'<rect x="{f(x - 12)}" y="{f(h * 0.06)}" width="24" height="{f(h * 0.56)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.0)}" width="{f(w + 20)}" height="{f(h * 0.07)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.26, b - 230))
    o.append(f'<rect x="{f(w * 0.5)}" y="{f(b - 46 * s)}" width="{f(w * 0.52)}" height="{f(46 * s)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    for i, x in enumerate((0.58, 0.7, 0.82, 0.94)):
        white = i % 2 == 0
        o.append(seated(w * x, b - 40 * s, s * 0.85, "#E8E2D6" if white else "#3A4A6A", head="#F3EFE6" if white else "#3A4A6A", beard="#8A847A" if white else "#2A1A10",
                        flip=True, band=True))
    if who == "man":
        o.append(blind_fig(p, w * 0.3, b, s, up=UP_BLESS if seed % 2 else None))
    elif who == "parents":
        o.append(parents_fig(p, w * 0.22, b, s))
    elif who == "cast":
        o.append(f'<path d="M{f(w * 0.02)} {f(b)} L {f(w * 0.02)} {f(h * 0.3)} Q {f(w * 0.1)} {f(h * 0.2)} {f(w * 0.18)} {f(h * 0.3)} L {f(w * 0.18)} {f(b)} Z" fill="#FFE6A0" stroke="{INK}" stroke-width="2"></path>')
        o.append(blind_fig(p, w * 0.12, b, s * 0.9, flip=True))
        o.append(scribe_fig(p, w * 0.36, b, s, white=True, up=UP_BLESS))
    return "".join(o)

def found_him(p, w, h, seed, worship=False):
    """Jesus heard that they had cast him out; and finding him: outside the shut door of the synagogue, the man standing
    alone, and Jesus come to him along the street; worship=True: the man kneeling before Jesus, worshipping him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A4A7A", "#FFC890"), houses(w, h, h * 0.74, seed, hmin=0.3, hmax=0.44, shut=True), ground(w, h, h * 0.74, "#B8A06A", dy=0),
         f'<rect x="{f(w * 0.66)}" y="{f(h * 0.2)}" width="{f(w * 0.3)}" height="{f(h * 0.54)}" fill="#C8B490" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<path d="M{f(w * 0.74)} {f(h * 0.74)} L {f(w * 0.74)} {f(h * 0.44)} Q {f(w * 0.81)} {f(h * 0.34)} {f(w * 0.88)} {f(h * 0.44)} L {f(w * 0.88)} {f(h * 0.74)} Z" fill="#5A3A22" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.74)} {f(h * 0.6)} L {f(w * 0.88)} {f(h * 0.6)}" stroke="#2A1A10" stroke-width="3"></path>']
    s = fit(b, max(h * 0.26, b - 230))
    if worship:
        o.append(jesus(p, w * 0.3, b, s, flip=True, up=UP_BLESS))
        o.append(kneeler(w * 0.5, b, s * 0.86, BLIND_C, flip=True))
    else:
        o.append(jesus(p, w * 0.22, b, s, flip=True, up=UP_BLESS))
        o.append(blind_fig(p, w * 0.54, b, s * 0.98))
    return "".join(o)

# ---- John 10: the fold and the shepherd ----------------------------------------------------------------------------
def fold(w, h, b, seed, tone="day", door_open=False):
    """A stone sheepfold on a hillside: a low round wall of fieldstones with a single doorway."""
    top, bot = {"day": ("#8FD0E2", "#F3E8C8"), "dawn": ("#3A3A7A", "#FFC890"), "night": ("#05051A", "#2A2050")}[tone]
    o = [sky(w, h, top, bot)]
    if tone == "night": o.append(mk.stars(50, w, h * 0.4, seed) + moon(w * 0.84, h * 0.14, max(8, h * 0.035)))
    o += [hills(w, h, h * 0.44, seed, color="#7A8A5A" if tone != "night" else "#1E1E3A", amp=14, step=90), ground(w, h, h * 0.5, "#9AAA5A" if tone != "night" else "#2A2A40", dy=0)]
    x0, x1, wt = w * 0.4, w * 0.98, min(h * 0.3, 150)
    r = random.Random(seed)
    o.append(f'<path d="M{f(x0)} {f(b)} L {f(x0)} {f(b - wt)} L {f(x1)} {f(b - wt - h * 0.06)} L {f(x1)} {f(b)} Z" fill="#A89A8A" stroke="{INK}" stroke-width="2.4"></path>')
    for k in range(30):
        xx = r.uniform(x0, x1); yy = r.uniform(b - wt - h * 0.06 * (xx - x0) / (x1 - x0) + 6, b - 4)
        o.append(f'<ellipse cx="{f(xx)}" cy="{f(yy)}" rx="{f(h * 0.018)}" ry="{f(h * 0.011)}" fill="#8A7E70" stroke="{INK}" stroke-width="1"></ellipse>')
    dx = x0 + (x1 - x0) * 0.2
    o.append(f'<rect x="{f(dx)}" y="{f(b - wt * 0.9)}" width="{f(wt * 0.5)}" height="{f(wt * 0.9)}" fill="{"#2A1A10" if door_open else "#6A4A2A"}" stroke="{INK}" stroke-width="2"></rect>')
    if door_open: o.append(f'<path d="M{f(dx)} {f(b - wt * 0.9)} L {f(dx - wt * 0.3)} {f(b - wt * 0.8)} L {f(dx - wt * 0.3)} {f(b + 4)} L {f(dx)} {f(b)} Z" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></path>')
    return "".join(o), dx

def sheepfold(p, w, h, seed, stage="door"):
    """The fold of the sheep. thief: at night, a ladder set against the fold's wall away from the door, no one on it.
    door: morning, the porter opening the door, the shepherd at it calling, the sheep coming out to him. lead: the shepherd
    going before on the hill path, the flock following him. stranger: a stranger at the fold, the sheep running from him
    the other way. jesus: I am the door — Jesus standing in the open doorway of the fold, the sheep about his feet,
    light behind him."""
    b = h * 0.9
    tone = "night" if stage == "thief" else ("dawn" if stage in ("door", "jesus") else "day")
    bg, dx = fold(w, h, b, seed, tone=tone, door_open=stage in ("door", "jesus", "lead"))
    o = [mk.defs(p, *ALL), bg]
    s = fit(b + h * 0.06, max(h * 0.2, b + h * 0.06 - 230)); r = random.Random(seed)
    staff = '<path d="M-36 -170 C -46 -190 -30 -200 -24 -186 M-36 -170 L -40 0" stroke="#5A3A22" stroke-width="5" fill="none"></path>'
    if stage == "thief":
        o.append(f'<path d="M{f(w * 0.8)} {f(b)} L {f(w * 0.86)} {f(b - h * 0.3)} M{f(w * 0.86)} {f(b)} L {f(w * 0.92)} {f(b - h * 0.3)}" stroke="#5A3A22" stroke-width="4"></path>'
                 + "".join(f'<path d="M{f(w * (0.8 + 0.06 * t))} {f(b - h * 0.3 * t)} L {f(w * (0.86 + 0.06 * t))} {f(b - h * 0.3 * t)}" stroke="#5A3A22" stroke-width="3"></path>' for t in (0.2, 0.4, 0.6, 0.8)))
        o.append(sheep_row(w * 0.06, w * 0.32, b + h * 0.04, 3, seed, s=min(0.6, h / 600)))
    elif stage == "door":
        o.append(mk.person(p, round(dx + w * 0.12), round(b + h * 0.06), round(s * 0.94, 3), body="#B98A6E", cloth="#6A5A44", kind="Tunic", sw=3, flip=True))
        o.append(mk.person(p, round(dx - w * 0.1), round(b + h * 0.06), round(s, 3), body="#B98A6E", cloth="#5A6A4A", kind="Robe", sw=3, up=UP_CALL, extra=A.headcloth("#E8E2D6", cord="#3A2214") + A.BLACK_BEARD))
        for i in range(5):
            o.append(E.sheep(dx + w * 0.02 - i * w * 0.06, b + h * 0.06 - (i % 2) * 6, min(0.7, s * 0.55), flip=True))
    elif stage == "lead":
        for i in range(8):
            o.append(E.sheep(w * (0.26 + 0.08 * i), b + h * (0.04 - 0.01 * (i % 3)), min(0.7, s * 0.5) * (1 - 0.03 * i), flip=True))
        o.append(mk.person(p, round(w * 0.12), round(b + h * 0.06), round(s, 3), body="#B98A6E", cloth="#5A6A4A", kind="Robe", sw=3, flip=True, extra=staff + A.headcloth("#E8E2D6", cord="#3A2214") + A.BLACK_BEARD))
    elif stage == "stranger":
        o.append(mk.person(p, round(w * 0.8), round(b + h * 0.06), round(s, 3), body="#B98A6E", cloth="#7A5A44", kind="Robe", sw=3, flip=True, up=UP_CALL, extra=A.headcloth("#5A5E6A", cord="#2A2A2A") + A.BLACK_BEARD))
        for i in range(6):
            o.append(E.sheep(w * (0.06 + 0.08 * i), b + h * (0.05 - 0.02 * (i % 2)), min(0.7, s * 0.5), flip=False))
    elif stage == "jesus":
        o.append(glow(dx + w * 0.04, b - h * 0.1, h * 0.4, "#FFF4C2", 0.8, f"{p}g"))
        o.append(jesus(p, dx + w * 0.04, b + h * 0.02, s))
        for i in range(5):
            o.append(E.sheep(dx - w * 0.06 - i * w * 0.07, b + h * 0.06 - (i % 2) * 6, min(0.7, s * 0.55), flip=True))
    return "".join(o)

def good_shepherd(p, w, h, seed):
    """I am the good shepherd: Jesus on the green hillside at evening, a lamb carried on his shoulders, the flock gathered
    close about his feet."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A4A7A", "#FFC890"), sun(w * 0.84, h * 0.4, max(12, h * 0.04), color="#FFE680", op=0.4),
         hills(w, h, h * 0.46, seed, color="#6A8A4A", amp=14, step=90), ground(w, h, h * 0.56, "#8AAA4A", dy=-6)]
    s = fit(b, max(h * 0.28, b - 240))
    o.append(jesus(p, w * 0.46, b, s, up=[(-22, -158), (-34, -176), (-26, -196)]))
    o.append(f'<g transform="translate({f(w * 0.46)} {f(b - 200 * s)}) scale({f(s * 0.6)})">' + E3.lamb(0, 0, 1.0) + '</g>')
    for i in range(9):
        x = w * (0.12 + 0.09 * i) + (30 if i >= 4 else -30) * s
        if abs(x - w * 0.46) < 50 * s: continue
        o.append(E.sheep(x, b - (i % 2) * 8, min(0.8, s * 0.56), flip=x > w * 0.46))
    return "".join(o)

def hireling(p, w, h, seed):
    """The hireling beholdeth the wolf coming, and leaveth the sheep, and fleeth: the flock scattering across the hillside
    at dusk, the hireling running off over the ridge, and a grey wolf at the edge of the trees — no harm drawn."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#3A2A4A", "#E8906A"), hills(w, h, h * 0.42, seed, color="#5A4A4A", amp=14, step=80), ground(w, h, h * 0.52, "#7A7A4A", dy=-8)]
    for i in range(3): o.append(tree(w * (0.04 + 0.08 * i), h * 0.8, h / 400, color="#2A3A2A", seed=seed + i))
    s = fit(b, max(h * 0.28, b - 230)); r = random.Random(seed)
    o.append(wolf(w * 0.16, b - 6, min(1.0, s * 0.8)))
    for i in range(7):
        o.append(E.sheep(w * r.uniform(0.34, 0.8), b - r.uniform(0, h * 0.18), min(0.7, s * 0.5), flip=True))
    o.append(man(p, w * 0.9, h * 0.62, fit(h * 0.62, h * 0.62 - 120 * s), "#7A6A4A", flip=True, up=UP_HIGH))
    return "".join(o)

def one_flock(p, w, h, seed):
    """Other sheep I have, which are not of this fold: two flocks coming over two hills toward one fold in the valley,
    and Jesus standing between them calling."""
    b = h * 0.94
    bg, dx = fold(w * 1.0, h, h * 0.66, seed, tone="day", door_open=True)
    o = [mk.defs(p, *ALL), bg]
    s = fit(b, max(h * 0.28, b - 230))
    for i in range(5):
        o.append(E.sheep(w * (0.04 + 0.07 * i), b - h * (0.02 * i), min(0.7, s * 0.5)))
        o.append(E.sheep(w * (0.96 - 0.07 * i), b - h * (0.02 * i), min(0.7, s * 0.5), flip=True))
    o.append(jesus(p, w * 0.5, b, s, up=UP_CALL))
    return "".join(o)

def solomons_porch(p, w, h, seed, stones_=False):
    """It was winter; and Jesus was walking in the temple in Solomon's porch: the long colonnade under a grey winter sky,
    Jesus walking in it and the Jews come round about him; stones_=True they stooping to the stones of the pavement and
    holding them, Jesus standing apart."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A6A7A", "#C8C8C8"), pavement(w, h, h * 0.62, color="#B8B0A0")]
    for k in range(8):
        x = w * (0.04 + 0.13 * k)
        o.append(f'<rect x="{f(x - 11)}" y="{f(h * 0.1)}" width="22" height="{f(h * 0.52)}" fill="#E0D8C8" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.04)}" width="{f(w + 20)}" height="{f(h * 0.07)}" fill="#B8B0A0" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.26, b - 230)); r = random.Random(seed)
    o.append(jesus(p, w * 0.24, b, s, flip=True))
    held = '<ellipse cx="-36" cy="-86" rx="10" ry="8" fill="#B8B0A0" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'
    for i, x in enumerate((0.46, 0.58, 0.7, 0.82, 0.94)):
        c = r.choice(HEB)
        o.append(mk.person(p, round(w * x), round(b - 4 * (i % 2)), round(s * (0.98 - 0.02 * i), 3), body=SKIN, cloth=c, kind="Robe", sw=3, flip=False,
                           up=[(-22, -158), (-30, -120), (-34, -92)] if stones_ and i % 2 == 0 else (UP_BLESS if i == 0 else None),
                           extra=(held if stones_ and i % 2 == 0 else "") + A.headcloth(r.choice(["#5E626E", "#E8E2D6", "#3A4A6A"]), cord="#3A2214") + A.BLACK_BEARD))
    return "".join(o)
