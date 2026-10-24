"""Drawings for John 7–8. Galilee and his brethren; the feast of tabernacles — Jerusalem full of booths of green branches on
the roofs and in the streets; Jesus going up in secret among the pilgrims; teaching in the temple court; the officers sent
to take him and standing back before the chief priests; the last great day — rivers of living water running down out of
the hills into the dry land and greening it (no figure); the city at night and the mount of Olives. The woman taken in
adultery (7:53–8:11): she is drawn only at a distance, veiled, standing in the midst; Jesus stooping and writing on the
ground with his finger; the accusers with their stones, then the stones laid down on the pavement one by one as they go
out, eldest first; Jesus and the woman left alone in the empty court — nothing more. The light of the world: the great
golden lampstands of the court blazing over the night city. The treasury; the broken fetters on the threshold of an open
door (the truth shall make you free); Abraham under the stars (genesis.art3's, his look unchanged); the stones taken up in
the porch and Jesus gone out by the far gate. Built on jhn.art3."""
from jhn.art3 import *
from jhn.art3 import f, INK, HEB, TWELVE, P, coals, stone_pot, courtyard, LIE, on_bed, lying, bedroll, lame_fig, porches
import random, math
from mrk.art3 import chains

BRETHREN = ["#4A5A6A", "#5A5A4A", "#3A4A5A", "#5A4A5A"]          # his brethren: plain cool robes and headcloths

def jesus_stoop(x, y, s, flip=False):
    """Jesus stooped down on the ground, writing with his finger (job.art.seated in his colours, bowed, the arm reaching down
    to the dust)."""
    from ntcast import JESUS_SKIN, JESUS_HAIR, JESUS_TUNIC, JESUS_MANTLE
    g = seated(x, y, s, JESUS_TUNIC, head=JESUS_HAIR, beard=JESUS_HAIR, flip=flip, bowed=True).replace(SKIN, JESUS_SKIN)
    g = g.replace("M-8 -90 L 10 -66 L 38 -62", "M-6 -88 L 30 -46 L 66 -8")
    mantle = (f'<path d="M-28 -92 C -16 -96 0 -96 6 -92 C 2 -70 -6 -40 -14 -2 L -34 -2 C -30 -40 -30 -70 -28 -92 Z" fill="{JESUS_MANTLE}" stroke="#0D0D0F" stroke-width="2.2"></path>')
    return g[:-4] + mantle + "</g>"

def booth(x, b, wd, ht, seed):
    """A booth of the feast of tabernacles: four poles and a roof of leafy branches."""
    r = random.Random(seed)
    o = [f'<path d="M{f(x - wd / 2)} {f(b)} L {f(x - wd / 2)} {f(b - ht)} M{f(x + wd / 2)} {f(b)} L {f(x + wd / 2)} {f(b - ht)}" stroke="#6A4A2A" stroke-width="{f(max(2, wd / 30))}"></path>']
    for _ in range(int(6 + wd / 14)):
        lx = x + r.uniform(-0.55, 0.55) * wd; ly = b - ht + r.uniform(-ht * 0.16, ht * 0.06)
        o.append(f'<ellipse cx="{f(lx)}" cy="{f(ly)}" rx="{f(wd * r.uniform(0.12, 0.2))}" ry="{f(ht * r.uniform(0.08, 0.14))}" fill="{r.choice(["#3F7A34", "#5E8F26", "#4A6A2A"])}" stroke="{INK}" stroke-width="1.2"></ellipse>')
    return "".join(o)

def brethren(p, w, h, seed):
    """His brethren said unto him, Depart hence, and go into Judæa: a village of Galilee, his brethren standing before
    Jesus, one pointing south along the road to Judæa."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.42, seed, color="#7A9A5A", amp=14, step=90),
         houses(w, h, h * 0.72, seed, x0=-10, x1=w * 0.4, hmin=0.24, hmax=0.36), ground(w, h, h * 0.72, "#B8A86A", dy=0)]
    s = fit(b, max(h * 0.26, b - 230))
    o.append(jesus(p, w * 0.2, b, s))
    for i, c in enumerate(BRETHREN):
        o.append(mk.person(p, round(w * (0.46 + 0.13 * i)), round(b - 4 * (i % 2)), round(s * (0.98 - 0.02 * i), 3), body="#C98E66", cloth=c, kind="Robe", sw=3,
                           flip=i == 3, up=UP_CALL if i == 3 else None, extra=A.headcloth(c, cord="#2A2A2A") + (A.BLACK_BEARD if i % 2 == 0 else "")))
    return "".join(o)

def booths(p, w, h, seed, secret=False):
    """The feast of tabernacles: Jerusalem's roofs and streets full of booths of green branches, the pilgrims going up to
    the temple on the hill; secret=True Jesus going up among the pilgrims on the road below the walls, not publicly."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.4, seed, color="#9A8A6A", amp=10, step=90),
         walls(w * 0.2, w * 1.02, h * 0.62, h * 0.3, seed, towers=3), temple(w * 0.66, h * 0.4, min(w * 0.24, h * 0.5))]
    r = random.Random(seed)
    for i in range(6):
        o.append(booth(w * (0.26 + 0.13 * i), h * 0.44 + r.uniform(-6, 6), w * 0.07, h * 0.08, seed + i))
    o.append(ground(w, h, h * 0.66, "#C8B07A", dy=0))
    for i in range(3):
        o.append(booth(w * (0.08 + 0.36 * i), h * 0.86, w * 0.16, h * 0.18, seed + 10 + i))
    s = fit(b, max(h * 0.26, b - 230))
    if secret:
        o.append(crowd(p, w * 0.34, w * 0.98, b - 10, b - 10 - 150 * s, 7, seed + 2, flip=True))
        o.append(jesus(p, w * 0.22, b, s * 0.98, flip=True, glow=False))
    else:
        o.append(crowd(p, w * 0.02, w * 0.98, b, b - 160 * s, 9, seed + 2))
    return "".join(o)

def temple_teach(p, w, h, seed, stage="sit"):
    """In the court of the temple at the feast. sit: Jesus seated teaching on the steps, the people about him on the
    pavement; stand: Jesus standing and crying out, his arm stretched forth, the people turned to him; officers: the
    officers of the chief priests in grey coming in at the colonnade, stopping short of him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), temple(w * 0.6, h * 0.5, min(w * 0.5, h * 0.9)), pavement(w, h, h * 0.5)]
    s = fit(b, max(h * 0.26, b - 230)); r = random.Random(seed)
    if stage == "sit":
        o.append(jesus_seated(w * 0.3, b, s * 0.95))
        for i, x in enumerate((0.08, 0.46, 0.6, 0.74, 0.88)):
            o.append(seated(w * x, b, s * 0.8, r.choice(HEB), head=r.choice(["#E8E2D6", "#3A4A6A", "#5E626E", None]), beard=r.choice(["#2A1A10", "#6A645E", None]), flip=x > 0.3))
    else:
        o.append(jesus(p, w * 0.24, b, s, flip=True, up=UP_BLESS if stage == "stand" else None))
        o.append(crowd(p, w * 0.42, w * 0.8, b, b - 160 * s, 5, seed, flip=False))
        if stage == "officers":
            for i, x in enumerate((0.86, 0.95)):
                o.append(mk.person(p, round(w * x), round(b - 4 * i), round(s * 0.98, 3), body="#B98A6E", cloth="#4A4A56", kind="Tunic", sw=3, flip=True,
                                   extra=A.headcloth("#3A3A46", cord="#1A1A1A") + A.BLACK_BEARD))
        else:
            o.append(crowd(p, w * 0.8, w * 0.98, b, b - 160 * s, 2, seed + 1, flip=False))
    return "".join(o)

def living_water(p, w, h, seed):
    """From within him shall flow rivers of living water: a spring of bright water breaking out high in the dry hills and
    running down in rivers through the dust, the land turning green along their banks (no figure)."""
    r = random.Random(seed)
    o = [sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.3, seed, color="#C8A06A", amp=18, step=80), ground(w, h, h * 0.4, "#D8B880", dy=0),
         glow(w * 0.5, h * 0.34, h * 0.3, "#FFFFFF", 0.9, f"{p}g")]
    for k, (x1, sw) in enumerate(((0.06, 0.07), (0.5, 0.09), (0.94, 0.07))):
        d = f"M{f(w * 0.5)} {f(h * 0.36)} C {f(w * (0.5 + (x1 - 0.5) * 0.3))} {f(h * 0.5)} {f(w * (0.5 + (x1 - 0.5) * 0.8))} {f(h * 0.7)} {f(w * x1)} {f(h + 10)}"
        o.append(f'<path d="{d}" stroke="#7AAA3A" stroke-width="{f(h * sw * 2.4)}" fill="none" stroke-linecap="round"></path>')
        o.append(f'<path d="{d}" stroke="{INK}" stroke-width="{f(h * sw + 4)}" fill="none"></path><path d="{d}" stroke="#3AA0D0" stroke-width="{f(h * sw)}" fill="none"></path>'
                 f'<path d="{d}" stroke="#BFE6F2" stroke-width="{f(h * sw * 0.2)}" fill="none" stroke-dasharray="14 18"></path>')
    for _ in range(10):
        x = r.uniform(0.05, 0.95) * w; y = r.uniform(0.6, 0.95) * h
        o.append(tree(x, y, h / 900 * r.uniform(0.7, 1.1), color="#3F7A34", seed=seed + _))
    o.append(f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.36)}" r="{f(h * 0.03)}" fill="#FFFFFF"></circle>')
    return "".join(o)

def taken_woman(p, w, h, seed, stage="brought"):
    """The woman taken in adultery — never close, never more than this. brought: in the court at early morning the scribes
    and Pharisees standing, the woman veiled and set in the midst some way off, Jesus seated. write: Jesus stooped down
    writing on the ground with his finger, the accusers standing with stones in their hands, the woman far off. gone: the
    stones laid down on the pavement, the accusers going out one by one, the eldest first, Jesus stooping. alone: the
    court empty, the stones lying where they were set down, Jesus standing, the woman standing veiled at a distance."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A6A9A", "#FFE6A0"), pavement(w, h, h * 0.5, color="#C8B898")]
    for k in range(6):
        x = w * (0.04 + 0.184 * k)
        o.append(f'<rect x="{f(x - 12)}" y="{f(h * 0.06)}" width="24" height="{f(h * 0.44)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.0)}" width="{f(w + 20)}" height="{f(h * 0.07)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.26, b - 230)); r = random.Random(seed)
    sw = fit(h * 0.62, h * 0.62 - 130 * s)                               # the woman, far off in the midst
    woman_at = lambda x: woman_fig(p, w * x, h * 0.62, sw, "#6A6A7A", "#3A3A4A", flip=True)
    stone = lambda x, y, k=1.0: f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(9 * s * k)}" ry="{f(6 * s * k)}" fill="#B8B0A0" stroke="{INK}" stroke-width="1.4"></ellipse>'
    held = '<ellipse cx="-62" cy="-118" rx="9" ry="7" fill="#B8B0A0" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'
    accusers = [(0.6, True), (0.72, False), (0.84, True), (0.95, False)]
    if stage == "brought":
        o.append(woman_at(0.5))
        o.append(jesus_seated(w * 0.18, b, s * 0.95))
        for i, (x, white) in enumerate(accusers):
            o.append(scribe_fig(p, w * x, b - 4 * (i % 2), s * (0.98 - 0.02 * i), white=white, flip=True, up=UP_BLESS if i == 0 else None))
    elif stage == "write":
        o.append(woman_at(0.46))
        o.append(jesus_stoop(w * 0.22, b, s * 0.9))
        o.append(f'<path d="M{f(w * 0.22 + 40 * s)} {f(b - 4)} q 10 -6 20 0 t 20 0 m 6 -2 l 12 4" stroke="#6A5A44" stroke-width="2" fill="none"></path>')
        for i, (x, white) in enumerate(accusers):
            o.append(mk.person(p, round(w * x), round(b - 4 * (i % 2)), round(s * (0.98 - 0.02 * i), 3), body=SKIN, cloth="#E8E2D6" if white else "#3A4A6A", kind="Robe", sw=3,
                               flip=True, up=[(-22, -158), (-42, -136), (-58, -122)], extra=held + A.headcloth("#F3EFE6" if white else "#3A4A6A", cord="#E8B830") + (GREY_BEARD if white else A.BLACK_BEARD)))
    elif stage == "gone":
        o.append(woman_at(0.46))
        o.append(jesus_stoop(w * 0.22, b, s * 0.9))
        for i in range(5): o.append(stone(w * (0.56 + 0.07 * i), b - 4 - (i % 2) * 8))
        o.append(scribe_fig(p, w * 0.86, h * 0.6, fit(h * 0.6, h * 0.6 - 120 * s), white=True))
        o.append(scribe_fig(p, w * 0.96, h * 0.56, fit(h * 0.56, h * 0.56 - 100 * s)))
    elif stage == "alone":
        o.append(woman_at(0.62))
        for i in range(7): o.append(stone(w * (0.34 + 0.06 * i), b - 4 - (i % 3) * 8))
        o.append(jesus(p, w * 0.2, b, s, flip=True, up=UP_BLESS))
    return "".join(o)

def temple_lamps(p, w, h, seed):
    """I am the light of the world: the court of the temple at night in the feast, three great golden lampstands standing
    high above the court wall, their bowls blazing, and the light falling on the whole dark city below."""
    o = [sky(w, h, "#05051A", "#1E1650"), mk.stars(60, w, h * 0.4, seed),
         houses(w, h, h * 0.86, seed, hmin=0.08, hmax=0.14, lit=True, color=("#3A3450", "#2E2A44", "#443E5A"), stairs=False),
         f'<rect x="-10" y="{f(h * 0.86)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A2440" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(h * 0.66)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(h * 0.72)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#A89878" stroke="{INK}" stroke-width="2"></rect>']
    k = min(w, h) / 300
    for i, x in enumerate((0.2, 0.5, 0.8)):
        top = h * (0.14 + 0.04 * (i % 2)); base = h * 0.66
        o.append(glow(w * x, top, h * 0.4, "#FFC14D", 0.9, f"{p}g{i}"))
        o.append(f'<path d="M{f(w * x)} {f(base)} L {f(w * x)} {f(top + 20 * k)}" stroke="{INK}" stroke-width="{f(9 * k)}"></path><path d="M{f(w * x)} {f(base)} L {f(w * x)} {f(top + 20 * k)}" stroke="#E8B830" stroke-width="{f(5 * k)}"></path>'
                 f'<path d="M{f(w * x - 16 * k)} {f(base)} L {f(w * x + 16 * k)} {f(base)} L {f(w * x + 6 * k)} {f(base - 14 * k)} L {f(w * x - 6 * k)} {f(base - 14 * k)} Z" fill="#E8B830" stroke="{INK}" stroke-width="1.6"></path>'
                 f'<path d="M{f(w * x - 40 * k)} {f(top + 22 * k)} L {f(w * x + 40 * k)} {f(top + 22 * k)}" stroke="{INK}" stroke-width="{f(7 * k)}"></path><path d="M{f(w * x - 40 * k)} {f(top + 22 * k)} L {f(w * x + 40 * k)} {f(top + 22 * k)}" stroke="#E8B830" stroke-width="{f(4 * k)}"></path>')
        for dx in (-36, -12, 12, 36):
            cx = w * x + dx * k
            o.append(f'<path d="M{f(cx - 9 * k)} {f(top + 8 * k)} L {f(cx + 9 * k)} {f(top + 8 * k)} L {f(cx + 6 * k)} {f(top + 20 * k)} L {f(cx - 6 * k)} {f(top + 20 * k)} Z" fill="#FFD23F" stroke="{INK}" stroke-width="1.4"></path>'
                     + E.flame(cx, top + 10 * k, 14 * k, 34 * k, 0))
    return "".join(o)

def freed(p, w, h, seed):
    """The truth shall make you free: an open door with the morning light pouring through it, the broken fetters and chains
    lying on the threshold."""
    o = [bgr(w, h, "#2A2228"),
         f'<rect x="{f(w * 0.36)}" y="{f(h * 0.1)}" width="{f(w * 0.28)}" height="{f(h * 0.8)}" fill="#FFF4C2" stroke="{INK}" stroke-width="3"></rect>',
         f'<path d="M{f(w * 0.36)} {f(h * 0.1)} L {f(w * 0.24)} {f(h * 0.04)} L {f(w * 0.24)} {f(h * 0.96)} L {f(w * 0.36)} {f(h * 0.9)} Z" fill="#6A4A2A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.36)} {f(h * 0.9)} L {f(w * 0.64)} {f(h * 0.9)} L {f(w * 0.9)} {f(h + 10)} L {f(w * 0.1)} {f(h + 10)} Z" fill="#FFE680" opacity="0.4"></path>',
         glow(w * 0.5, h * 0.5, h * 0.6, "#FFFFFF", 0.7, f"{p}g"),
         f'<rect x="-10" y="{f(h * 0.9)}" width="{f(w + 20)}" height="{f(h)}" fill="#4A3E38" opacity="0.6"></rect>',
         chains(w * 0.5, h * 0.92, max(0.6, h / 300), seed, n=2)]
    return "".join(o)

def stones_up(p, w, h, seed):
    """They took up stones therefore to cast at him: but Jesus hid himself, and went out of the temple: the porch of the
    temple, men stooping for the stones of the pavement and standing with them in their hands, and far off at the end of
    the colonnade Jesus going out by the gate."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A4A6A", "#E8A06A"), pavement(w, h, h * 0.5, color="#B8A888")]
    for k in range(6):
        x = w * (0.04 + 0.184 * k)
        o.append(f'<rect x="{f(x - 12)}" y="{f(h * 0.06)}" width="24" height="{f(h * 0.44)}" fill="#D8CCB0" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.0)}" width="{f(w + 20)}" height="{f(h * 0.07)}" fill="#B8A888" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<path d="M{f(w * 0.82)} {f(h * 0.5)} L {f(w * 0.82)} {f(h * 0.3)} Q {f(w * 0.88)} {f(h * 0.22)} {f(w * 0.94)} {f(h * 0.3)} L {f(w * 0.94)} {f(h * 0.5)} Z" fill="#FFE6A0" stroke="{INK}" stroke-width="2"></path>')
    s = fit(b, max(h * 0.26, b - 230))
    o.append(jesus(p, w * 0.88, h * 0.5, fit(h * 0.5, h * 0.5 - 100 * s), glow=False))
    held = '<ellipse cx="-62" cy="-118" rx="10" ry="8" fill="#B8B0A0" stroke="#0D0D0F" stroke-width="1.4"></ellipse>'
    r = random.Random(seed)
    for i, x in enumerate((0.08, 0.2, 0.34, 0.62)):
        o.append(mk.person(p, round(w * x), round(b - 4 * (i % 2)), round(s * (0.98 - 0.02 * i), 3), body=SKIN, cloth=r.choice(HEB), kind="Robe", sw=3, flip=True,
                           up=[(-22, -158), (-42, -136), (-58, -122)], extra=held + A.headcloth(r.choice(["#5E626E", "#E8E2D6", "#3A4A6A"]), cord="#3A2214") + A.BLACK_BEARD))
    o.append(kneeler(w * 0.48, b, s * 0.8, "#6A5A3A"))
    return "".join(o)

def abraham_night(p, w, h, seed):
    """Your father Abraham rejoiced to see my day: Abraham in his old age, white-robed, grey-haired and grey-bearded, standing
    at the door of his tent on the hill under the countless stars, looking up, his arm lifted, a dawn glow on the far rim."""
    b = h * 0.92
    from job.art import tents
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#2A2050"), mk.stars(220, w, h * 0.8, seed), mk.stars(40, w, h * 0.6, seed + 1, color="#FFE680"),
         glow(w * 0.86, h * 0.8, h * 0.4, "#FFC14D", 0.5, f"{p}g"),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.78)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.6)} {f(h * 0.74)} {f(w + 10)} {f(h * 0.86)} L {f(w + 10)} {f(h + 10)} Z" fill="#14142E" stroke="{INK}" stroke-width="2"></path>',
         tents(w * 0.06, h * 0.84, max(0.5, h / 420), n=2, color="#3A2A30", seed=seed)]
    s = fit(b, max(h * 0.3, b - 230))
    hair = '<path d="M-13 -188 C -14 -204 14 -204 13 -188 L 14 -180 L 9 -184 L -9 -184 L -14 -180 Z" fill="#9A948A" stroke="#0D0D0F" stroke-width="1.4"></path>'
    o.append(mk.person(p, round(w * 0.56), round(b), round(s, 3), body="#C98E66", cloth="#E8E2D6", kind="Robe", sw=3, flip=True,
                       up=[(-22, -158), (-34, -190), (-38, -222)], extra=hair + GREY_BEARD))
    return "".join(o)
