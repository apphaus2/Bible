"""Drawings for Matthew 21–22: Bethphage and the ass and colt tied; the entry into Jerusalem down the mount of Olives, the
garments and branches in the way; the city stirred at its gate; the temple court with the tables overthrown and the doves
loosed; the blind and the lame and the children crying Hosanna in the temple; Bethany at evening; the fig tree with leaves
only, and withered; the vineyard of the two sons; the householder's vineyard with its hedge, winepress and tower, then its
gate at dusk (the servants and the son are told in words only, nothing of the violence drawn); the stone at the head of the
corner; the king's marriage feast — the tables laid and empty, the far city burning in smoke, the guests gathered from the
highways, the man without a wedding-garment, the door onto the outer darkness; the denarius; seven tombs; the two tables of
the law; the psalm scroll. Built on mat.art7."""
from mat.art7 import *
from mat.art7 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE
from ntcast import JESUS_SKIN, JESUS_HAIR, JESUS_TUNIC, JESUS_MANTLE, ROBES
import random, math
from job.art import seated, smoke
from ecc.art import loaf
from genesis.art2 import dove as _dove
from oba.minor import smokes, cup
import exodus as E

def jesus_riding(p, x, b, s, flip=False):
    """Jesus riding upon the ass (seated: his figure scaled down onto its back), garments spread upon it."""
    d = -1 if flip else 1
    cloth = f'<path d="M{f(x - 50 * s)} {f(b - 74 * s)} L {f(x + 40 * s)} {f(b - 76 * s)} L {f(x + 34 * s)} {f(b - 50 * s)} L {f(x - 44 * s)} {f(b - 50 * s)} Z" fill="#B5121B" stroke="{INK}" stroke-width="2"></path>'
    return (N.ass(x, b, s, flip=flip, color="#8A8478") + cloth
            + jesus_fig(p, x - d * 4 * s, b - 64 * s, s * 0.66, flip=flip, glow=True))

def bethphage(p, w, h, seed):
    """Go into the village that is over against you, and ye shall find an ass tied, and a colt with her: a village door on
    the slope of the mount of Olives, the ass and her colt tied at it, two of the disciples loosing them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#8A9A6A", amp=12, step=90),
         houses(w, h, h * 0.82, seed, hmin=0.34, hmax=0.5), ground(w, h, h * 0.82, "#C8B07A", dy=0)]
    for x in (0.08, 0.92): o.append(olive(w * x, h * 0.86, h / 360, seed=seed + int(x * 10)))
    s = fit(b, max(h * 0.24, b - 230))
    o.append(N.ass(w * 0.46, b, s * 0.9, color="#8A8478") + N.ass(w * 0.6, b, s * 0.6, color="#A89A8A"))
    o.append(disciple(p, w * 0.28, b, s, "james", up=UP_TOUCH) + disciple(p, w * 0.78, b, s * 0.98, "john", flip=True))
    return "".join(o)

def entry(p, w, h, seed):
    """Hosanna to the son of David: the road down the mount of Olives, Jerusalem and the temple across the valley, Jesus
    riding upon the ass over garments spread in the way, the multitudes before and behind waving branches."""
    r = random.Random(seed); b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"),
         hills(w, h, h * 0.42, seed, color="#B89A6A", amp=10, step=90),
         walls(w * 0.46, w * 0.98, h * 0.46, h * 0.2, seed, towers=4), temple(w * 0.76, h * 0.32, w * 0.24),
         f'<path d="M-10 {f(h * 0.6)} C {f(w * 0.3)} {f(h * 0.5)} {f(w * 0.7)} {f(h * 0.56)} {f(w + 10)} {f(h * 0.62)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#9AAA6A" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M-10 {f(h * 0.92)} C {f(w * 0.3)} {f(h * 0.86)} {f(w * 0.6)} {f(h * 0.9)} {f(w + 10)} {f(h * 0.84)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#D8C8A0" stroke="{INK}" stroke-width="1.6"></path>']
    for _ in range(9):
        x = r.uniform(0, w)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.9 + r.uniform(-6, 10))}" width="{f(r.uniform(30, 60))}" height="8" fill="{r.choice(["#B5121B", "#1F5FAD", "#E8B830", "#5E8F26"])}" stroke="{INK}" stroke-width="1.2"></rect>')
    s = fit(b, max(h * 0.32, b - 220))
    o.append(jesus_riding(p, w * 0.44, b, s))
    branch = '<path d="M-40 -170 C -50 -200 -54 -220 -50 -240" stroke="#3A6A2A" stroke-width="4" fill="none"></path><path d="M-50 -240 c -16 4 -20 12 -14 18 M-50 -230 c 16 0 18 8 14 14 M-48 -214 c -14 2 -16 10 -12 14" stroke="#4A8A3A" stroke-width="5" fill="none"></path>'
    for i, x in enumerate((0.08, 0.18, 0.66, 0.76, 0.86, 0.96)):
        o.append(man(p, w * x, b - (i % 2) * 6, s * 0.94, r.choice(HEB), flip=x > 0.5, up=[(-22, -158), (-34, -176), (-40, -190)], extra=branch))
    return "".join(o)

def city_gate_stirred(p, w, h, seed):
    """All the city was stirred, saying, Who is this?: the gate of Jerusalem thronged, people on the walls and roofs
    looking down."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), walls(w * -0.02, w * 1.02, h * 0.7, h * 0.5, seed, towers=3), ground(w, h, h * 0.7, "#C8B07A", dy=0)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(crowd(p, w * 0.02, w * 0.98, b, b - 160 * s, 12, seed))
    for i in range(6):
        x = w * (0.1 + 0.16 * i); y = h * 0.36
        o.append(figure(p, x, y, y - h * 0.08, random.Random(seed + i).choice(HEB), "man" if i % 2 else "woman", flip=i > 2))
    return "".join(o)

def temple_court(p, w, h, seed, cleansed=False, healing=False):
    """The court of the temple: the colonnade and the sanctuary front; cleansed=True: the tables of the money-changers
    overthrown, coins scattered on the pavement, the doves loosed into the air, the sellers going out, Jesus with his arm
    lifted; healing=True: the blind and the lame about him, children with branches crying Hosanna."""
    r = random.Random(seed); b = h * 0.94
    o = [mk.defs(p, *ALL, *LIE), sky(w, h, "#8FD0E2", "#FFF4C2"), temple(w * 0.62, h * 0.56, w * 0.6), pavement(w, h, h * 0.56)]
    s = fit(b, max(h * 0.26, b - 230))
    if cleansed:
        for x, rot in ((0.36, -70), (0.6, 80)):
            o.append(f'<g transform="rotate({rot} {f(w * x)} {f(b - 20 * s)})"><rect x="{f(w * x - 50 * s)}" y="{f(b - 30 * s)}" width="{f(100 * s)}" height="{f(12 * s)}" fill="#7A4A2A" stroke="{INK}" stroke-width="2"></rect>'
                     f'<path d="M{f(w * x - 40 * s)} {f(b - 18 * s)} l 0 {f(30 * s)} M{f(w * x + 40 * s)} {f(b - 18 * s)} l 0 {f(30 * s)}" stroke="#5A3A1E" stroke-width="{f(6 * s)}"></path></g>')
        for _ in range(24):
            o.append(f'<circle cx="{f(r.uniform(w * 0.26, w * 0.8))}" cy="{f(b - r.uniform(0, 14))}" r="{f(4 * s)}" fill="#E8B830" stroke="{INK}" stroke-width="0.8"></circle>')
        for _ in range(6):
            o.append(_dove(r.uniform(w * 0.4, w * 0.9), r.uniform(h * 0.1, h * 0.4), r.uniform(0.6, 1.0) * max(0.5, h / 400), flip=r.random() < 0.5))
        o.append(jesus(p, w * 0.16, b, s, up=UP_HIGH))
        o.append(man(p, w * 0.86, b, s * 0.94, "#7A5A2A") + man(p, w * 0.95, b, s * 0.92, "#5A4A6A"))
    if healing:
        o.append(jesus(p, w * 0.24, b, s, up=UP_BLESS))
        staff = '<path d="M-30 -150 L -40 0" stroke="#5A3A22" stroke-width="5"></path>'
        o.append(man(p, w * 0.4, b, s * 0.94, "#7A7A80", flip=True, extra=staff) + man(p, w * 0.5, b, s * 0.94, "#6A5A3A", flip=True, up=UP_HIGH))
        branch = '<path d="M30 -150 C 40 -180 44 -200 40 -220" stroke="#3A6A2A" stroke-width="4" fill="none"></path><path d="M40 -220 c 16 4 20 12 14 18 M40 -206 c -14 2 -16 10 -12 14" stroke="#4A8A3A" stroke-width="5" fill="none"></path>'
        for x in (0.64, 0.72, 0.8):
            o.append(mk.person(p, round(w * x), round(b), round(s * 0.5, 3), body=SKIN, cloth=r.choice(["#C8783A", "#E8B830", "#C2456A"]), kind="Tunic", sw=3,
                               up=[(22, -158), (30, -180), (34, -200)], extra=branch))
        o.append(scribe_fig(p, w * 0.92, b, s * 0.96, white=True, flip=True))
    return "".join(o)

def bethany(p, w, h, seed):
    """He went forth out of the city to Bethany, and lodged there: a small village on the far slope of the mount of Olives
    at evening, a lamp in a window, olive trees."""
    o = [sky(w, h, "#3A2A5A", "#FF9A5A"), hills(w, h, h * 0.5, seed, color="#5A4A5A", amp=12, step=80),
         hill_town(w * 0.56, h * 0.76, w * 0.5, h * 0.3, seed, lit=True, hill="#6A5A4A"), ground(w, h, h * 0.78, "#5A4A3A", dy=0)]
    for x in (0.1, 0.24, 0.9): o.append(olive(w * x, h * 0.98, h / 320, seed=seed + int(x * 10)))
    return "".join(o)

def fig_by_way(p, w, h, seed, withered=False):
    """A fig tree by the way side, leaves only, no fruit; withered=True: the same tree dried up, its leaves fallen brown
    about it; Jesus and the disciples on the road."""
    b = h * 0.94
    o = [road_scene(p, w, h, seed, "day")]
    k = max(0.6, (b - h * 0.2) / 160)
    if withered:
        o.append(fig_tree(w * 0.6, b, k, bare=True, seed=seed))
        r = random.Random(seed)
        for _ in range(10):
            x = w * 0.6 + r.uniform(-60, 60) * k
            o.append(f'<path d="M{f(x)} {f(b - 2)} c -6 -4 -10 2 -6 6 c 4 2 8 -2 6 -6" fill="#8A6A3A" stroke="{INK}" stroke-width="1"></path>')
    else:
        o.append(fig_tree(w * 0.6, b, k, fruit=False, seed=seed))
    s = fit(b, max(h * 0.24, b - 230))
    o.append(jesus(p, w * 0.3, b, s, up=UP_BLESS if not withered else None))
    o.append(disciple(p, w * 0.16, b, s * 0.96, "peter") + disciple(p, w * 0.06, b, s * 0.94, "john"))
    return "".join(o)

def vineyard_hedged(p, w, h, seed, tone="day", empty=False):
    """A householder planted a vineyard, and set a hedge about it, and digged a winepress in it, and built a tower: the
    walled vineyard on the hillside, the stone winepress, the watch-tower; empty=True: at dusk, the gate standing open, no
    one in it (what the husbandmen did is told in words only)."""
    top, bot = {"day": ("#8FD0E2", "#FFF4C2"), "dusk": ("#2A1A3A", "#C8503A")}[tone]
    o = [mk.defs(p, *ALL), sky(w, h, top, bot), hills(w, h, h * 0.36, seed, color="#8A7A6A" if tone == "day" else "#3A2A3A", amp=12, step=80),
         ground(w, h, h * 0.44, "#A8885A" if tone == "day" else "#5A3A3A", dy=0),
         vines(w * 0.1, w * 0.9, h * 0.56, h * 0.78, seed, rows=3)]
    o.append(f'<path d="M{f(w * 0.04)} {f(h * 0.9)} L {f(w * 0.96)} {f(h * 0.9)}" stroke="#8A7A6A" stroke-width="{f(h * 0.05)}"></path>'
             f'<rect x="{f(w * 0.44)}" y="{f(h * 0.84)}" width="{f(w * 0.1)}" height="{f(h * 0.1)}" fill="#3A2A1A" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="{f(w * 0.78)}" y="{f(h * 0.16)}" width="{f(w * 0.08)}" height="{f(h * 0.3)}" fill="#B89A6A" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.76)} {f(h * 0.16)} L {f(w * 0.82)} {f(h * 0.1)} L {f(w * 0.88)} {f(h * 0.16)} Z" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></path>'
             f'<ellipse cx="{f(w * 0.2)}" cy="{f(h * 0.48)}" rx="{f(w * 0.08)}" ry="{f(h * 0.03)}" fill="#7A6A5A" stroke="{INK}" stroke-width="2"></ellipse>'
             f'<ellipse cx="{f(w * 0.2)}" cy="{f(h * 0.48)}" rx="{f(w * 0.05)}" ry="{f(h * 0.018)}" fill="#5A1A3A"></ellipse>')
    if empty:
        o.append(f'<path d="M{f(w * 0.44)} {f(h * 0.84)} L {f(w * 0.38)} {f(h * 0.82)} L {f(w * 0.38)} {f(h * 0.96)} L {f(w * 0.44)} {f(h * 0.94)} Z" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></path>')
    return "".join(o)

def two_sons(p, w, h, seed):
    """A man had two sons: in the vineyard at morning, one son walking away from the gate, the other going in with his
    pruning-hook (the one that repented)."""
    b = h * 0.94
    o = [vineyard(p, w, h, seed, tone="day", hire=False)]
    s = fit(b, max(h * 0.4, b - 200))
    hook = '<path d="M30 -150 L 44 -90 C 50 -80 60 -84 58 -94" stroke="#5A4A3A" stroke-width="4" fill="none"></path>'
    o.append(man(p, w * 0.3, b, s, "#6A5A3A", extra=hook) + man(p, w * 0.7, b, s, "#3A4A6A", flip=True))
    return "".join(o)

def corner_stone(p, w, h, seed):
    """The stone which the builders rejected, the same was made the head of the corner: a wall rising at a corner, its
    great corner-stone set in place, gold light on it; the heap of the builders' stones beside."""
    r = random.Random(seed); b = h * 0.92
    o = [sky(w, h, "#FFC890", "#FFF4C2"), ground(w, h, b, "#C8B07A", dy=0)]
    cx = w * 0.56
    for row in range(6):
        y = b - (row + 1) * h * 0.1
        for k in range(5):
            x = cx - w * 0.3 + k * w * 0.06 + (w * 0.03 if row % 2 else 0)
            if x > cx - w * 0.06: continue
            o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.058)}" height="{f(h * 0.1)}" fill="#D8C8A8" stroke="{INK}" stroke-width="1.6"></rect>')
        for k in range(3):
            x = cx + k * w * 0.05; yy = y
            o.append(f'<path d="M{f(x)} {f(yy)} L {f(x + w * 0.05)} {f(yy - h * 0.01)} L {f(x + w * 0.05)} {f(yy + h * 0.09)} L {f(x)} {f(yy + h * 0.1)} Z" fill="#B8A888" stroke="{INK}" stroke-width="1.6"></path>')
    top = b - 6 * h * 0.1
    o.append(glow(cx, top, h * 0.24, "#FFE680", 0.8, f"{p}g")
             + f'<rect x="{f(cx - w * 0.07)}" y="{f(top - h * 0.12)}" width="{f(w * 0.12)}" height="{f(h * 0.12)}" fill="#F3E8C8" stroke="{INK}" stroke-width="2.4"></rect>')
    for _ in range(9):
        x = r.uniform(w * 0.02, w * 0.2); y = b - r.uniform(0, h * 0.08)
        o.append(f'<rect x="{f(x)}" y="{f(y - 14)}" width="{f(r.uniform(20, 36))}" height="14" fill="#C8B898" stroke="{INK}" stroke-width="1.4" transform="rotate({r.randint(-12, 12)} {f(x)} {f(y)})"></rect>')
    return "".join(o)

def wedding_hall(p, w, h, seed, guests=False, stranger=False, door=False):
    """The king's marriage feast: a hall hung with garlands, the long tables laid with bread and cups; empty (the bidden
    would not come), or guests=True, filled with guests of every kind in white wedding-garments; stranger=True: one guest in
    a dark everyday cloak among them, the king standing over him; door=True: the door at the end of the hall open onto the
    outer darkness."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bgr(w, h, "#5A2A3A")]
    for x in (0.06, 0.94):
        o.append(f'<rect x="{f(w * x - 14)}" y="-10" width="28" height="{f(b + 10)}" fill="#E8B830" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<path d="M-10 {f(h * 0.08)} Q {f(w * 0.25)} {f(h * 0.2)} {f(w * 0.5)} {f(h * 0.08)} Q {f(w * 0.75)} {f(h * 0.2)} {f(w + 10)} {f(h * 0.08)}" stroke="#3A7A2A" stroke-width="8" fill="none"></path>')
    if door:
        o.append(f'<rect x="{f(w * 0.42)}" y="{f(h * 0.24)}" width="{f(w * 0.16)}" height="{f(b - h * 0.24)}" fill="#05050A" stroke="{INK}" stroke-width="2.4"></rect>')
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#6A4A3A" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.24, b - 230))
    o.append(f'<rect x="{f(w * 0.06)}" y="{f(b - 40 * s)}" width="{f(w * 0.88)}" height="{f(14 * s)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(8):
        x = w * (0.1 + 0.11 * i)
        o.append(loaf(x, b - 44 * s, s * 0.6) + cup(x + 18 * s, b - 40 * s, s * 0.14))
    if guests or stranger:
        r = random.Random(seed)
        for i, x in enumerate((0.08, 0.2, 0.32, 0.68, 0.8, 0.92)):
            o.append(seated(w * x, b, s * 0.8, "#F3EFE6", head=r.choice(["#E8E2D6", None, "#C8B898"]), beard=r.choice(["#2A1A10", "#6A645E", ""]), flip=x > 0.5))
        if stranger:
            o.append(seated(w * 0.5, b, s * 0.8, "#3A3A3A", head="#2A2A2A", beard="#1A1210"))
            o.append(king(p, w * 0.62, b, s, "#2A4A8A", flip=True, up=UP_BLESS))
    return "".join(o)

def city_smoke(p, w, h, seed):
    """He sent his armies, and burned their city: a walled city far off on its hill, smoke going up from it into a red sky
    (no one drawn)."""
    o = [sky(w, h, "#3A1A1A", "#C8502A"), hills(w, h, h * 0.6, seed, color="#3A2A2A", amp=12, step=80),
         walls(w * 0.3, w * 0.72, h * 0.7, h * 0.2, seed, towers=3, color="#6A5A4A"), smokes([w * 0.4, w * 0.52, w * 0.64], h * 0.5, seed, k=max(0.6, h / 300)),
         ground(w, h, h * 0.72, "#3A2A2A", dy=0)]
    return "".join(o)

def highways(p, w, h, seed):
    """Go ye unto the partings of the highways: a crossing of roads outside a town, a servant beckoning, travellers of every
    kind turning toward the feast — a lame man on a staff, a shepherd, a beggar, a merchant."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#9AAA7A", amp=10, step=80), ground(w, h, h * 0.5, "#C8B07A", dy=0)]
    for ex in (-0.1, 1.1):
        o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.5)} L {f(w * ex)} {f(h + 10)}" stroke="#D8C8A0" stroke-width="{f(max(8, h * 0.06))}"></path>')
    s = fit(b, max(h * 0.24, b - 230))
    o.append(man(p, w * 0.5, b, s, "#2A4A8A", up=UP_CALL))
    staff = '<path d="M-30 -150 L -40 0" stroke="#5A3A22" stroke-width="5"></path>'
    o.append(man(p, w * 0.24, b, s * 0.94, "#7A7A80", extra=staff) + man(p, w * 0.12, b, s * 0.92, "#6A5A3A") + man(p, w * 0.76, b, s * 0.94, "#1F5A6A", flip=True)
             + woman_fig(p, w * 0.88, b, s * 0.9, "#8A3A5A", flip=True))
    return "".join(o)

def denarius(p, w, h, seed):
    """Whose is this image and superscription?: a silver denarius held up in the light, a laurelled head in profile on it
    and the lettering round the rim."""
    o = [bgr(w, h, "#2A1A2A"), glow(w * 0.5, h * 0.5, h * 0.6, "#FFF4C2", 0.4, f"{p}g")]
    cx, cy, r = w * 0.5, h * 0.52, min(w, h) * 0.32
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="#C8C8D0" stroke="{INK}" stroke-width="3"></circle>'
             f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r * 0.86)}" fill="none" stroke="#8A8A94" stroke-width="2"></circle>')
    k = r / 100
    o.append(f'<g transform="translate({f(cx)} {f(cy)}) scale({f(k)})"><path d="M-10 -56 C 20 -60 36 -40 36 -16 C 40 -10 46 0 40 4 L 34 6 C 36 16 32 24 24 26 L 20 44 L -30 44 C -24 20 -40 0 -36 -24 C -34 -44 -26 -54 -10 -56 Z" fill="#A8A8B4" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M-30 -40 c 6 -6 12 -6 16 -2 c 4 -8 12 -8 16 -2 c 6 -6 14 -4 16 2" stroke="#5A7A3A" stroke-width="5" fill="none"></path></g>')
    for i in range(18):
        a = math.pi * (0.85 + 1.3 * i / 17)
        o.append(f'<rect x="{f(cx + math.cos(a) * r * 0.93 - 2)}" y="{f(cy + math.sin(a) * r * 0.93 - 4)}" width="4" height="8" fill="#5A5A64" transform="rotate({f(math.degrees(a) + 90)} {f(cx + math.cos(a) * r * 0.93)} {f(cy + math.sin(a) * r * 0.93)})"></rect>')
    return "".join(o)

def seven_tombs(p, w, h, seed):
    """Seven brethren, and after them all the woman died: a hillside of eight rock-cut tombs side by side at evening, their
    stones rolled to — no one drawn."""
    o = [sky(w, h, "#3A2A4A", "#C8906A"), f'<path d="M-10 {f(h * 0.3)} C {f(w * 0.3)} {f(h * 0.22)} {f(w * 0.7)} {f(h * 0.26)} {f(w + 10)} {f(h * 0.3)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>']
    for i in range(8):
        x = w * (0.08 + 0.12 * i); y = h * (0.62 + 0.04 * (i % 2)); rr = min(w * 0.045, h * 0.1)
        o.append(f'<path d="M{f(x - rr)} {f(y + rr)} L {f(x - rr)} {f(y - rr * 0.4)} Q {f(x)} {f(y - rr * 1.4)} {f(x + rr)} {f(y - rr * 0.4)} L {f(x + rr)} {f(y + rr)} Z" fill="#1A1210" stroke="{INK}" stroke-width="1.6"></path>'
                 f'<circle cx="{f(x + rr * 0.3)}" cy="{f(y + rr * 0.2)}" r="{f(rr * 0.9)}" fill="#A89A8A" stroke="{INK}" stroke-width="1.8"></circle>')
    return "".join(o)

def tables_law(p, w, h, seed):
    """The great commandment: the two tables of the law in a soft gold light, with no letters drawn."""
    o = [bgr(w, h, "#12113A"), glow(w * 0.5, h * 0.5, max(w, h) * 0.5, "#FFE680", 0.45, f"{p}g")]
    k = min(w, h) / 300
    for dx in (-1, 1):
        x = w * 0.5 + dx * 56 * k
        o.append(f'<path d="M{f(x - 48 * k)} {f(h * 0.5 + 100 * k)} L {f(x - 48 * k)} {f(h * 0.5 - 70 * k)} C {f(x - 48 * k)} {f(h * 0.5 - 110 * k)} {f(x + 48 * k)} {f(h * 0.5 - 110 * k)} {f(x + 48 * k)} {f(h * 0.5 - 70 * k)} L {f(x + 48 * k)} {f(h * 0.5 + 100 * k)} Z" fill="#D8D0C0" stroke="{INK}" stroke-width="2.4"></path>')
        for row in range(5):
            y = h * 0.5 - 50 * k + row * 30 * k
            o.append(f'<path d="M{f(x - 34 * k)} {f(y)} L {f(x + 34 * k)} {f(y)}" stroke="#8A8270" stroke-width="{f(3 * k)}" stroke-dasharray="{f(8 * k)} {f(4 * k)}"></path>')
    return "".join(o)

def psalm_scroll(p, w, h, seed):
    """David in the Spirit: the scroll of the psalms open under a lamp, a harp beside it."""
    o = [prophecy(p, w, h, seed)]
    k = max(0.5, h / 300)
    hx, hy = w * 0.16, h * 0.86
    o.append(f'<path d="M{f(hx)} {f(hy)} L {f(hx)} {f(hy - 110 * k)} C {f(hx + 40 * k)} {f(hy - 120 * k)} {f(hx + 60 * k)} {f(hy - 80 * k)} {f(hx + 50 * k)} {f(hy)} Z" fill="none" stroke="#C8963E" stroke-width="{f(6 * k)}"></path>'
             + "".join(f'<path d="M{f(hx + i * 10 * k)} {f(hy)} L {f(hx + i * 10 * k)} {f(hy - (104 - i * 4) * k)}" stroke="#F3E8C8" stroke-width="1.2"></path>' for i in range(1, 5)))
    return "".join(o)
