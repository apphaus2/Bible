"""Drawings for John 5–6. The pool of Bethesda by the sheep gate with its five porches, the sick lying under them; the man
of thirty and eight years on his pallet, then standing with his bed rolled on his shoulder and walking out; the Jews
stopping him in the street; the temple, where Jesus finds him. For the discourse of 5:17–47: the rock tombs on the
hillside with the light breaking over their stones (the dead that hear his voice are words only, no one drawn coming
forth); the lamp that burneth and shineth; the scrolls of the scriptures; the tables of Moses. John 6: the mountain over
the sea of Tiberias with the multitude coming up; the lad with his five barley loaves and two fishes; the companies on
the much grass, the loaves given out, the twelve baskets; the mountain alone at nightfall; the boat rowing in the dark and
the rising wind, Jesus walking on the sea, the boat at the land; the boats from Tiberias; the manna round the tents at dawn;
the bread out of heaven, a loaf in a shaft of light; the bread and the cup (for "eat my flesh and drink my blood": the
loaf and the cup only, nothing else); the synagogue at Capernaum; the disciples going back along the road; the twelve.
Built on jhn.art2."""
from jhn.art2 import *
from jhn.art2 import f, INK, HEB, TWELVE, P, coals, stone_pot, courtyard, LIE, on_bed, lying, bedroll
import random, math
import exodus4 as E4
from oba.minor import sea
import numbers1 as N
from ecc.art import loaf as _loaf

LAME_C = "#7A6E62"                                               # the man at Bethesda: a grey-brown mantle, grey hair and beard
GREY_HAIR = '<path d="M-13 -188 C -14 -204 14 -204 13 -188 L 14 -180 L 9 -184 L -9 -184 L -14 -180 Z" fill="#8A847A" stroke="#0D0D0F" stroke-width="1.4"></path>'

def lame_fig(p, x, y, s, flip=False, up=None, bed=False):
    """The man healed at Bethesda, standing: a grey-brown mantle, grey hair and a grey beard, no headcloth; bed=True his
    rolled pallet on his shoulder."""
    roll = '<path d="M-30 -168 C -40 -170 -46 -160 -40 -150 L 34 -128 C 44 -130 46 -142 38 -148 Z" fill="#C8B088" stroke="#0D0D0F" stroke-width="1.8"></path>' if bed else ""
    return mk.person(p, round(x), round(y), round(s, 3), body="#B98A6E", cloth=LAME_C, kind="Robe", sw=3, flip=flip, up=up, extra=GREY_HAIR + GREY_BEARD + roll)

def porches(w, h, b, seed, dusk=False):
    """The pool of Bethesda: the colonnades of its porches round the water, the stone steps going down; (b: the floor)."""
    o = [sky(w, h, "#8FD0E2" if not dusk else "#3A2A5A", "#FFF4C2" if not dusk else "#FF9A5A")]
    top = h * 0.16
    o.append(f'<rect x="-10" y="{f(top)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    for k in range(9):
        x = w * (0.04 + 0.115 * k)
        o.append(f'<rect x="{f(x - 9)}" y="{f(top + h * 0.06)}" width="18" height="{f(b - top - h * 0.06)}" fill="#E8DCC0" stroke="{INK}" stroke-width="1.8"></rect>')
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#B8A888" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<path d="M{f(w * 0.16)} {f(h + 10)} L {f(w * 0.24)} {f(b + h * 0.04)} L {f(w * 0.76)} {f(b + h * 0.04)} L {f(w * 0.84)} {f(h + 10)} Z" fill="#3A8AA8" stroke="{INK}" stroke-width="2"></path>')
    for k in range(4):
        y = b + h * 0.04 + (h - b) * 0.2 * (k + 1)
        o.append(f'<path d="M{f(w * 0.24 - 6 * k)} {f(y)} q {f(w * 0.1)} -4 {f(w * 0.2)} 0 t {f(w * 0.2)} 0" stroke="#BFE6F2" stroke-width="1.8" fill="none" opacity="0.7"></path>')
    return "".join(o)

def bethesda(p, w, h, seed, stage="pool"):
    """The pool by the sheep gate. pool: the multitude of the sick lying under the five porches, the halt with their staves.
    man: the man of thirty and eight years on his pallet by the steps, and Jesus standing over him. rise: the man standing
    with his bed rolled on his shoulder, Jesus beside him, the sick about them looking."""
    b = h * 0.66
    o = [mk.defs(p, *ALL, *LIE), porches(w, h, b, seed)]
    s = fit(b, max(h * 0.08, b - 220)); r = random.Random(seed)
    if stage == "pool":
        for i, x in enumerate((0.08, 0.26, 0.44, 0.62, 0.8)):
            o.append(on_bed(p, w * x + 30 * s, b - 14 * s, 120 * s, cloth=r.choice(["#C8B898", "#8A7A6A", "#A89A8A"]), flip=i % 2 == 1))
        staff = '<path d="M-30 -150 L -40 0" stroke="#5A3A22" stroke-width="5"></path>'
        o.append(seated(w * 0.92, b, s * 0.8, "#7A7A80", head="#8A847A", beard="#8A847A", flip=True) + man(p, w * 0.54, b, s * 0.94, "#6A5A3A", extra=staff))
    elif stage == "man":
        o.append(on_bed(p, w * 0.56, b - 14 * s, 190 * s, cloth=LAME_C, flip=True))
        o.append(jesus(p, w * 0.28, b, s, up=None))
        for i, x in enumerate((0.84, 0.94)):
            o.append(on_bed(p, w * x, b - 12 * s, 100 * s, cloth=r.choice(["#C8B898", "#8A7A6A"]), flip=True))
    elif stage == "rise":
        o.append(jesus(p, w * 0.3, b, s))
        o.append(lame_fig(p, w * 0.56, b, s, flip=True, bed=True))
        o.append(seated(w * 0.84, b, s * 0.8, "#7A7A80", head="#8A847A", beard="#8A847A", flip=True) + seated(w * 0.08, b, s * 0.78, "#8A7A6A", head=None, beard="#2A1A10"))
    return "".join(o)

def sabbath_street(p, w, h, seed):
    """It is the sabbath: a street of Jerusalem by the sheep gate, the healed man carrying his rolled bed, two of the Jews
    stopping him with their hands raised, the multitude behind."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), walls(-w * 0.02, w * 0.5, h * 0.66, h * 0.4, seed, towers=2), houses(w, h, h * 0.68, seed, x0=w * 0.5, x1=w + 10, hmin=0.3, hmax=0.44),
         ground(w, h, h * 0.68, "#C8B07A", dy=0)]
    s = fit(b, max(h * 0.26, b - 230))
    o.append(lame_fig(p, w * 0.3, b, s, bed=True))
    o.append(scribe_fig(p, w * 0.56, b, s * 0.98, flip=True, up=UP_BLESS) + scribe_fig(p, w * 0.7, b - 4, s * 0.96, white=True, flip=True))
    o.append(crowd(p, w * 0.78, w * 0.98, b - 20 * s, b - 20 * s - 150 * s, 3, seed, flip=True))
    return "".join(o)

def temple_found(p, w, h, seed):
    """Afterward Jesus findeth him in the temple: the colonnade of the temple court in the afternoon light, Jesus and the
    healed man standing together by a pillar."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), pavement(w, h, h * 0.72)]
    for k in range(7):
        x = w * (0.06 + 0.15 * k)
        o.append(f'<rect x="{f(x - 14)}" y="{f(h * 0.08)}" width="28" height="{f(h * 0.66)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.02)}" width="{f(w + 20)}" height="{f(h * 0.07)}" fill="#C8B898" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.26, b - 230))
    o.append(jesus(p, w * 0.36, b, s, flip=True, up=UP_BLESS))
    o.append(lame_fig(p, w * 0.6, b, s * 0.98, flip=True))
    return "".join(o)

def tombs_light(p, w, h, seed):
    """The hour cometh, in which all that are in the tombs shall hear his voice: the rock tombs cut in the hillside at
    dawn, each with its stone at the door, and the light breaking over the hill upon them — no one drawn."""
    o = [sky(w, h, "#2A2A5A", "#FFD89A"), rays(w * 0.7, h * 0.3, 36, 20, w, color="#FFF4C2", op=0.3), glow(w * 0.7, h * 0.3, h * 0.6, "#FFFFFF", 0.85, f"{p}g"),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.4)} C {f(w * 0.3)} {f(h * 0.3)} {f(w * 0.6)} {f(h * 0.4)} {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>']
    for i, (x, y) in enumerate(((0.12, 0.62), (0.34, 0.58), (0.56, 0.66), (0.8, 0.72), (0.24, 0.88), (0.66, 0.92))):
        k = max(0.5, h / 360) * (0.8 + 0.2 * (y > 0.8))
        cx, cy = w * x, h * y
        o.append(f'<path d="M{f(cx - 22 * k)} {f(cy)} L {f(cx - 22 * k)} {f(cy - 30 * k)} Q {f(cx)} {f(cy - 50 * k)} {f(cx + 22 * k)} {f(cy - 30 * k)} L {f(cx + 22 * k)} {f(cy)} Z" fill="#1A1210" stroke="{INK}" stroke-width="2"></path>'
                 f'<circle cx="{f(cx + 30 * k)}" cy="{f(cy - 24 * k)}" r="{f(26 * k)}" fill="#A89A8A" stroke="{INK}" stroke-width="2"></circle>'
                 f'<path d="M{f(cx - 40 * k)} {f(cy)} L {f(cx + 60 * k)} {f(cy)}" stroke="#6A5A4A" stroke-width="3"></path>')
    return "".join(o)

def lamp_shining(p, w, h, seed):
    """He was the lamp that burneth and shineth: a clay lamp burning on a stone ledge in the dark, its light filling the
    room for a season."""
    k = min(3.0, max(1.0, h / 120))
    o = [bgr(w, h, "#1A1222"), glow(w * 0.5, h * 0.56, h * 0.9, "#FFC14D", 0.8, f"{p}g"),
         f'<rect x="{f(w * 0.2)}" y="{f(h * 0.7)}" width="{f(w * 0.6)}" height="{f(h * 0.06)}" fill="#5A4030" stroke="{INK}" stroke-width="2"></rect>',
         clay_lamp(w * 0.5, h * 0.7, k)]
    return "".join(o)

def scriptures(p, w, h, seed):
    """Ye search the scriptures: scrolls in a niche of the synagogue, one unrolled on the reading-desk under the lamp."""
    o = [prophecy(p, w, h, seed, tone="day")]
    for i in range(5):
        x = w * (0.08 + 0.04 * i); y = h * 0.3
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.03)}" height="{f(h * 0.3)}" rx="6" fill="#E8D8B0" stroke="{INK}" stroke-width="1.8"></rect>')
    return "".join(o)

# ---- John 6 -------------------------------------------------------------------------------------------------------
def mountain_sea(p, w, h, seed):
    """Jesus went up into the mountain, and there he sat with his disciples: the green mountain above the sea of Tiberias,
    Jesus sitting with the disciples on its shoulder, and the great multitude coming up the slope from the shore."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), lake(w, h, h * 0.32, seed, n=8),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.5)} C {f(w * 0.2)} {f(h * 0.4)} {f(w * 0.4)} {f(h * 0.44)} {f(w * 0.6)} {f(h * 0.6)} C {f(w * 0.8)} {f(h * 0.72)} {f(w * 0.9)} {f(h * 0.8)} {f(w + 10)} {f(h * 0.82)} L {f(w + 10)} {f(h + 10)} Z" fill="#7AAA4A" stroke="{INK}" stroke-width="2.4"></path>']
    s = fit(h * 0.6, h * 0.36)
    o.append(jesus_seated(w * 0.24, h * 0.5, s))
    for i in range(4):
        o.append(seated(w * (0.34 + 0.07 * i), h * (0.52 + 0.02 * i), s * 0.9, TWELVE[i], head=TWELVE[i] if i % 2 else None, beard="#2A1A10", flip=True))
    o.append(crowd(p, w * 0.6, w * 0.98, b, b - 150 * fit(b, b - 160) * 0.75, 7, seed, flip=True))
    return "".join(o)

def lad_loaves(p, w, h, seed):
    """There is a lad here, who hath five barley loaves, and two fishes: on the grass a boy holding out his basket — the
    five small barley loaves and two fishes in it — Andrew beside him with his hand on his shoulder."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#8AAA5A", amp=12, step=90), ground(w, h, h * 0.5, "#8AB04A", dy=0)]
    s = fit(b, max(h * 0.26, b - 230))
    o.append(disciple(p, w * 0.36, b, s, "andrew", flip=True, up=UP_TOUCH))
    ls = s * 0.66
    o.append(mk.person(p, round(w * 0.5), round(b), round(ls, 3), body="#C98E66", cloth="#C8783A", kind="Tunic", sw=3, flip=True, up=[(-22, -158), (-46, -140), (-66, -136)]))
    bx, by = w * 0.5 - 70 * ls, b - 136 * ls
    o.append(f'<path d="M{f(bx - 40 * ls)} {f(by)} L {f(bx + 40 * ls)} {f(by)} L {f(bx + 30 * ls)} {f(by + 30 * ls)} L {f(bx - 30 * ls)} {f(by + 30 * ls)} Z" fill="#B8904A" stroke="{INK}" stroke-width="2"></path>')
    for i in range(5): o.append(_loaf(bx - 28 * ls + 14 * ls * i, by - 4 * ls - (i % 2) * 6 * ls, ls * 0.6))
    o.append(f'<path d="M{f(bx - 30 * ls)} {f(by - 14 * ls)} c 10 -8 30 -8 40 0 c -10 8 -30 8 -40 0 Z M{f(bx)} {f(by - 20 * ls)} c 10 -8 30 -8 40 0 c -10 8 -30 8 -40 0 Z" fill="#C8C2D6" stroke="{INK}" stroke-width="1.4"></path>')
    o.append(jesus(p, w * 0.8, b, s, flip=True))
    return "".join(o)

def boat_dark(p, w, h, seed, jesus_=False, land=False):
    """It was now dark, and Jesus had not yet come to them: the boat on the black sea, the twelve rowing against a great
    wind, the waves rising; jesus_=True Jesus walking on the sea toward the boat in his soft light, the men afraid;
    land=True the boat run up on the shore of Capernaum at dawn, Jesus in it with them."""
    if land:
        o = [mk.defs(p, *ALL), sky(w, h, "#3A3A7A", "#FFC890"), hills(w, h, h * 0.36, seed, color="#5A4A6A", amp=12, step=90), lake(w, h, h * 0.44, seed, color="#4A6A9A"),
             shore(w, h, h * 0.66, x0=-10, x1=w * 0.6), houses(w, h, h * 0.7, seed, x0=-10, x1=w * 0.44, hmin=0.14, hmax=0.24)]
        s = fit(h * 0.72, h * 0.4)
        o.append(boat(p, w * 0.64, h * 0.72, s * 0.95, crew=[(-50, "jesus"), (0, ROBES["peter"]), (46, ROBES["john"])], mast=True))
        return "".join(o)
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#1A1A3A"), mk.stars(20, w, h * 0.2, seed), clouds(w, h * 0.16, seed, n=6, color="#2A2A4A", op=0.9, h=h),
         wind_lines(w, h, seed, n=10, color="#8A9ABA", op=0.5, y0=0.1, y1=0.5), sea(w, h, h * 0.5, seed, color="#14304A", deep="#0A1A2A", foam="#8AB0C8", rough=True)]
    s = fit(h * 0.72, h * 0.4)
    oar = '<path d="M-30 -120 L -90 -40" stroke="#6A4A2A" stroke-width="5"></path>'
    o.append(boat(p, w * 0.62, h * 0.74, s, crew=[(-50, ("up", ROBES["peter"])), (-4, ROBES["andrew"]), (40, ROBES["john"])], mast=True, tilt=-6))
    if jesus_:
        o.append(glow(w * 0.18, h * 0.6, h * 0.4, "#FFF4C2", 0.7, f"{p}g") + jesus(p, w * 0.18, h * 0.8, fit(h * 0.8, h * 0.4) * 0.8, flip=True))
        o.append(f'<path d="M{f(w * 0.1)} {f(h * 0.8)} q {f(w * 0.04)} -4 {f(w * 0.08)} 0 t {f(w * 0.08)} 0" stroke="#BFE6F2" stroke-width="2.4" fill="none"></path>')
    return "".join(o)

def boats_tiberias(p, w, h, seed):
    """There came boats from Tiberias: the morning shore on the far side, the multitude getting into the boats and pushing
    off across the sea toward Capernaum, seeking Jesus."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.3, seed, color="#7A8A6A", amp=12, step=90), lake(w, h, h * 0.36, seed),
         hill_town(w * 0.82, h * 0.38, w * 0.18, h * 0.08, seed, hill="#8A9A6A"), shore(w, h, h * 0.8, x0=-10, x1=w * 0.5)]
    s = fit(h * 0.7, h * 0.46)
    for i, x in enumerate((0.36, 0.58, 0.8)):
        o.append(boat(p, w * x, h * (0.62 + 0.06 * (i % 2)), s * (0.9 - 0.1 * i), crew=[(-30, random.Random(seed + i).choice(HEB)), (20, random.Random(seed + 7 * i).choice(HEB))], mast=True))
    o.append(crowd(p, w * 0.02, w * 0.4, b, b - 150 * fit(b, b - 160) * 0.8, 5, seed))
    return "".join(o)

def manna_camp(p, w, h, seed):
    """Our fathers ate the manna in the wilderness: the tents of the camp at dawn and the small round white grains lying on
    the ground all about, and falling out of the sky."""
    o = [sky(w, h, "#3A2A5A", "#FFB07A"), ground(w, h, h * 0.62, "#C8A87A", dy=0), N.camp(10, w * 0.05, w * 0.95, h * 0.64, h * 0.78, seed),
         E4.manna(160, 0, w, h * 0.8, h * 0.99, seed), E4.manna(60, 0, w, h * 0.06, h * 0.56, seed + 1)]
    return "".join(o)

def bread_heaven(p, w, h, seed, cup_=False, broken=False):
    """The bread of God is that which cometh down out of heaven: a round loaf on a white cloth upon the table, a shaft of
    light falling on it out of the dark; broken=True the loaf broken in two; cup_=True the cup beside it (for "my flesh
    and my blood": the bread and the cup only)."""
    b = h * 0.78
    o = [bgr(w, h, "#14122A"), shaft(w * 0.5, w, h, top_w=0.06, bot_w=0.24, color="#FFF4C2", op=0.45), glow(w * 0.5, b - h * 0.1, h * 0.6, "#FFE680", 0.7, f"{p}g"),
         f'<path d="M{f(w * 0.14)} {f(b)} L {f(w * 0.86)} {f(b)} L {f(w * 0.94)} {f(h + 10)} L {f(w * 0.06)} {f(h + 10)} Z" fill="#6A4A2A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.28)} {f(b)} L {f(w * 0.72)} {f(b)} L {f(w * 0.78)} {f(h + 10)} L {f(w * 0.22)} {f(h + 10)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></path>']
    k = min(w, h) / 180
    if broken:
        for dx, rot in ((-34, -12), (34, 12)):
            o.append(f'<g transform="translate({f(w * 0.5 + dx * k - (14 * k if cup_ else 0))} {f(b + 8 * k)}) rotate({rot})"><path d="M-30 0 C -30 -26 30 -26 30 0 Z" fill="#D9A25A" stroke="{INK}" stroke-width="2"></path>'
                     f'<path d="M-30 0 L 30 0" stroke="#F3E0B8" stroke-width="3"></path></g>')
    else:
        x = w * 0.5 - (40 * k if cup_ else 0)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(b + 4 * k)}" rx="{f(44 * k)}" ry="{f(22 * k)}" fill="#D9A25A" stroke="{INK}" stroke-width="2.4"></ellipse>'
                 f'<path d="M{f(x - 26 * k)} {f(b - 2 * k)} q {f(26 * k)} -10 {f(52 * k)} 0 M{f(x - 30 * k)} {f(b + 6 * k)} q {f(30 * k)} -10 {f(60 * k)} 0" stroke="#8A5A2A" stroke-width="2" fill="none"></path>')
    if cup_:
        o.append(cup(w * 0.5 + 58 * k, b + 16 * k, k * 0.5, color="#E8B830"))
    return "".join(o)

def went_back(p, w, h, seed):
    """Many of his disciples went back, and walked no more with him: the road out of Capernaum, a straggle of men walking
    away along it into the hills, and Jesus with the twelve standing still by the town, watching them go."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A4A7A", "#FFC890"), hills(w, h, h * 0.4, seed, color="#7A6A6A", amp=14, step=90), ground(w, h, h * 0.5, "#B8A06A", dy=0),
         houses(w, h, h * 0.62, seed, x0=-10, x1=w * 0.3, hmin=0.18, hmax=0.3),
         f'<path d="M{f(w * 0.3)} {f(h + 10)} C {f(w * 0.5)} {f(h * 0.7)} {f(w * 0.74)} {f(h * 0.56)} {f(w + 10)} {f(h * 0.5)}" stroke="#E0D0A8" stroke-width="{f(max(10, h * 0.07))}" fill="none"></path>']
    r = random.Random(seed)
    for i in range(6):
        t = i / 5; x = w * (0.52 + 0.4 * t); y = h * (0.82 - 0.26 * t)
        o.append(man(p, x, y, fit(y, y - h * (0.36 - 0.24 * t)), r.choice(HEB), flip=False))
    s = fit(b, max(h * 0.3, b - 220))
    o.append(jesus(p, w * 0.16, b, s, flip=True))
    for i in range(3):
        o.append(disciple(p, w * (0.27 + 0.07 * i), b - 4 * (i % 2), s * (0.95 - 0.02 * i), ["peter", "john", "andrew"][i], flip=True))
    return "".join(o)
