"""Drawings for Matthew 15–17: the unwashen hands; the blind leading the blind toward the pit; the coast of Tyre and Sidon
and the woman crying after them; the little dogs under the table; the sick laid at his feet on the mountain; the seven
baskets; the red sky at evening; the boat without bread; the rock at Caesarea Philippi; the road to Jerusalem; the high
mountain of the transfiguration — Jesus in white light, Moses (exo.art) and Elijah (kg1.art) beside him, the three on their
faces — and the bright cloud (the Father's voice is the Voice box; nothing drawn in the cloud); the boy healed (no demon
drawn); the mountain removed; the half-shekel, the hook and the fish. Built on mat.art5."""
from mat.art5 import *
from mat.art5 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE
from ntcast import JESUS_SKIN, JESUS_HAIR, JESUS_TUNIC, JESUS_MANTLE, ROBES
import random, math
from job.art import seated, smoke
from ecc.art import loaf, dog
from lev.art3 import creature
import exodus as E

def unwashed(p, w, h, seed):
    """The disciples eating bread with unwashen hands: seated at a low table in a courtyard, the water-jar and basin
    standing by untouched; Pharisees and scribes from Jerusalem standing over them."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.66, seed, hmin=0.3, hmax=0.4, stairs=False), pavement(w, h, h * 0.66)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(f'<rect x="{f(w * 0.08)}" y="{f(b - 30 * s)}" width="{f(w * 0.4)}" height="{f(12 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(4): o.append(loaf(w * (0.12 + 0.1 * i), b - 34 * s, s * 0.7))
    for i, x in enumerate((0.1, 0.22, 0.34, 0.46)):
        o.append(disciple_seated(w * x, b, s * 0.72, i))
    o.append(f'<path d="M{f(w * 0.56)} {f(b)} C {f(w * 0.54)} {f(b - 40 * s)} {f(w * 0.56)} {f(b - 70 * s)} {f(w * 0.58)} {f(b - 70 * s)} C {f(w * 0.6)} {f(b - 70 * s)} {f(w * 0.62)} {f(b - 40 * s)} {f(w * 0.6)} {f(b)} Z" fill="#B5652E" stroke="{INK}" stroke-width="2"></path>'
             f'<ellipse cx="{f(w * 0.64)}" cy="{f(b - 6)}" rx="{f(24 * s)}" ry="{f(8 * s)}" fill="#8A8478" stroke="{INK}" stroke-width="1.6"></ellipse>')
    o.append(scribe_fig(p, w * 0.76, b, s, white=True, flip=True, up=UP_BLESS) + scribe_fig(p, w * 0.86, b, s * 0.98, flip=True) + scribe_fig(p, w * 0.95, b, s * 0.96, white=True, flip=True))
    return "".join(o)

def blind_pit(p, w, h, seed):
    """If the blind guide the blind, both shall fall into a pit: two men with staves, one leading the other by the hand,
    walking on toward the dark mouth of a pit in the road."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#C8A890", "#F3E8C8"), hills(w, h, h * 0.44, seed, color="#A8987A", amp=10, step=90), ground(w, h, h * 0.54, "#C8B07A", dy=0),
         f'<ellipse cx="{f(w * 0.74)}" cy="{f(b)}" rx="{f(w * 0.14)}" ry="{f(h * 0.06)}" fill="#1A1210" stroke="{INK}" stroke-width="2.4"></ellipse>']
    s = fit(b, max(h * 0.24, b - 230))
    staff = '<path d="M30 -150 L 40 0" stroke="#5A3A22" stroke-width="5"></path>'
    o.append(man(p, w * 0.46, b, s, "#7A7A80", up=UP_BLESS, extra=staff) + man(p, w * 0.32, b, s * 0.98, "#6A6A72", up=UP_BLESS))
    return "".join(o)

def tyre(p, w, h, seed):
    """The parts of Tyre and Sidon: the coast road by the great sea, the island city white on the water; a woman in an orange
    headcloth running after the company, crying out; the disciples turning."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), lake(w, h, h * 0.4, seed, color="#1F6F9A"),
         walls(w * 0.62, w * 0.92, h * 0.5, h * 0.14, seed, towers=3, color="#E8DCC0"), ground(w, h, h * 0.6, "#D8C090", dy=0)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(jesus(p, w * 0.18, b, s) + disciple(p, w * 0.3, b, s * 0.96, "peter", flip=True) + disciple(p, w * 0.4, b, s * 0.94, "john", flip=True))
    o.append(woman_fig(p, w * 0.72, b, s * 0.92, "#A85A1A", "#E8903A", flip=True, up=UP_HIGH))
    return "".join(o)

def crumbs(p, w, h, seed):
    """Even the dogs eat of the crumbs which fall from their masters' table: under a laid table, the little dogs of the
    house eating the crumbs from the floor."""
    b = h * 0.94
    o = [room(w, h, b, wall="#C8A878"),
         f'<rect x="{f(w * 0.1)}" y="{f(h * 0.4)}" width="{f(w * 0.8)}" height="{f(h * 0.06)}" fill="#7A4A2A" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<path d="M{f(w * 0.14)} {f(h * 0.46)} L {f(w * 0.14)} {f(b)} M{f(w * 0.86)} {f(h * 0.46)} L {f(w * 0.86)} {f(b)}" stroke="#5A3A1E" stroke-width="8"></path>']
    k = max(0.5, h / 260)
    for i in range(5): o.append(loaf(w * (0.2 + 0.14 * i), h * 0.4 - 6 * k, k))
    r = random.Random(seed)
    for _ in range(18): o.append(f'<circle cx="{f(r.uniform(w * 0.2, w * 0.8))}" cy="{f(b - r.uniform(0, 6))}" r="2.4" fill="#D9A25A"></circle>')
    o.append(dog(w * 0.36, b, k * 0.55, color="#C8965A") + dog(w * 0.62, b, k * 0.5, flip=True, color="#8A6A4A"))
    return "".join(o)

def sick_laid(p, w, h, seed):
    """They cast them down at his feet, and he healed them: Jesus seated on the mountain-side, the lame and the blind and the
    maimed set down before him, staves and crutches thrown aside, some standing up with their arms raised."""
    b = h * 0.94
    o = [mk.defs(p, *ALL, *LIE), sky(w, h, "#8FD0E2", "#F3E8C8"), lake(w, h, h * 0.36, seed, n=6),
         f'<path d="M-10 {f(h * 0.4)} C {f(w * 0.3)} {f(h * 0.3)} {f(w * 0.6)} {f(h * 0.44)} {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8AB84A" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, max(h * 0.24, b - 230))
    o.append(jesus_seated(w * 0.18, b - 20 * s, s * 0.82))
    o.append(f'<g transform="translate({f(w * 0.46)} {f(b - 4)}) scale({f(s * 0.6)})" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="2"><use href="#{p}LieB"></use><use href="#{p}LieA"></use></g>')
    o.append(E.kneel(w * 0.56, b, s * 0.8, color="#6A5A3A", flip=True, skin=SKIN))
    o.append(man(p, w * 0.7, b, s * 0.96, "#5A6A3A", flip=True, up=UP_HIGH) + man(p, w * 0.84, b, s * 0.94, "#7A7A80", flip=True, up=UP_HIGH))
    o.append(f'<path d="M{f(w * 0.74)} {f(b)} L {f(w * 0.8)} {f(b - 50 * s)} M{f(w * 0.9)} {f(b)} L {f(w * 0.96)} {f(b - 6)}" stroke="#5A3A22" stroke-width="5"></path>')
    return "".join(o)

def red_sky(p, w, h, seed, morning=False):
    """When it is evening, ye say, it will be fair weather, for the heaven is red: the sky over the lake at sunset, glowing
    red; morning=True: red and lowering, heavy clouds."""
    if morning:
        o = [sky(w, h, "#5A2A2A", "#C8503A"), clouds(w, h * 0.16, seed, n=6, color="#3A2A2E", op=0.9, h=h)]
    else:
        o = [sky(w, h, "#3A1A4A", "#FF6A2A"), sun(w * 0.5, h * 0.62, max(14, h * 0.07), color="#FFC14D", op=0.4)]
    o += [hills(w, h, h * 0.62, seed, color="#3A2A3A", amp=10, step=90), lake(w, h, h * 0.68, seed, color="#6A3A4A", deep="#2A1A2A", n=8, op=0.5)]
    return "".join(o)

def no_bread(p, w, h, seed):
    """They forgot to take bread: the boat crossing the lake, the disciples looking into an empty basket, Jesus at the stern."""
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.36, seed, color="#8A9A7A", amp=10, step=90), lake(w, h, h * 0.44, seed, n=10)]
    s = min(1.1, (h * 0.8 - h * 0.2) / 140)
    o.append(boat(p, w * 0.5, h * 0.82, s, crew=[(-70, ROBES["peter"]), (-34, ROBES["andrew"]), (2, ROBES["thomas"]), (50, "jesus")], mast=True))
    return "".join(o)

def caesarea(p, w, h, seed):
    """The parts of Caesarea Philippi: under Hermon, a great wall of rock with a dark cave at its foot and the spring running
    out; Jesus and the twelve before it."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"),
         f'<path d="M{f(w * 0.3)} {f(h * 0.18)} L {f(w * 0.5)} {f(h * 0.04)} L {f(w * 0.64)} {f(h * 0.12)} L {f(w * 0.8)} {f(h * 0.02)} L {f(w + 10)} {f(h * 0.1)} L {f(w + 10)} {f(h * 0.4)} L {f(w * 0.3)} {f(h * 0.4)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.36)} {f(h * 0.84)} L {f(w * 0.38)} {f(h * 0.26)} C {f(w * 0.5)} {f(h * 0.2)} {f(w * 0.8)} {f(h * 0.22)} {f(w + 10)} {f(h * 0.26)} L {f(w + 10)} {f(h * 0.84)} Z" fill="#B8806A" stroke="{INK}" stroke-width="2.6"></path>',
         f'<path d="M{f(w * 0.56)} {f(h * 0.84)} L {f(w * 0.56)} {f(h * 0.56)} Q {f(w * 0.64)} {f(h * 0.44)} {f(w * 0.72)} {f(h * 0.56)} L {f(w * 0.72)} {f(h * 0.84)} Z" fill="#1A1210" stroke="{INK}" stroke-width="2"></path>']
    for k in range(1, 5):
        y = h * (0.26 + 0.14 * k)
        o.append(f'<path d="M{f(w * 0.38)} {f(y)} C {f(w * 0.6)} {f(y - 10)} {f(w * 0.8)} {f(y + 8)} {f(w + 10)} {f(y)}" stroke="#8A5A4A" stroke-width="2" fill="none"></path>')
    o.append(ground(w, h, h * 0.84, "#7AA84A", dy=0))
    o.append(f'<path d="M{f(w * 0.64)} {f(h * 0.84)} C {f(w * 0.6)} {f(h * 0.9)} {f(w * 0.7)} {f(h * 0.94)} {f(w * 0.66)} {f(h + 10)}" stroke="#4AA0D0" stroke-width="10" fill="none"></path>')
    s = fit(b, max(h * 0.3, b - 220))
    o.append(jesus(p, w * 0.16, b, s))
    for i, x in enumerate((0.26, 0.34, 0.42, 0.5)):
        o.append(disciple(p, w * x, b, s * 0.94, ["peter", "andrew", "james", "john"][i], flip=True))
    return "".join(o)

def to_jerusalem(p, w, h, seed):
    """He must go unto Jerusalem: the road climbing through the hills toward the city on its height far off, the evening
    light on the walls."""
    o = [jerusalem_far(w, h, seed, tone="dusk", lit=True)]
    o.append(f'<path d="M{f(w * 0.1)} {f(h + 10)} C {f(w * 0.2)} {f(h * 0.9)} {f(w * 0.4)} {f(h * 0.86)} {f(w * 0.5)} {f(h * 0.8)}" stroke="#C8A878" stroke-width="{f(max(6, h * 0.04))}" fill="none"></path>')
    return "".join(o)

def transfigured(p, w, h, seed, cloud=False, after=False):
    """The high mountain apart: Jesus transfigured, standing in white light with rays about him, Moses (off-white headcloth,
    black beard) and Elijah (hairy mantle, bareheaded) in the light on either side, Peter, James and John kneeling below;
    cloud=True: a bright cloud overshadowing all, the three fallen on their faces, nothing drawn in the cloud; after=True:
    no one but Jesus only, the three rising."""
    from exo.art import moses
    from kg1.art import elijah_fig
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#2A2A6A", "#8FD0E2"),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.7)} L {f(w * 0.3)} {f(h * 0.52)} L {f(w * 0.5)} {f(h * 0.48)} L {f(w * 0.72)} {f(h * 0.54)} L {f(w + 10)} {f(h * 0.68)} L {f(w + 10)} {f(h + 10)} Z" fill="#6A6A7A" stroke="{INK}" stroke-width="2.4"></path>']
    s = fit(h * 0.66, max(h * 0.16, h * 0.66 - 230))
    jx, jy = w * 0.5, h * 0.66
    if not after:
        o.append(rays(jx, jy - 110 * s, 40, 40 * s, max(w, h), color="#FFFDF0", op=0.35))
        o.append(glow(jx, jy - 110 * s, 220 * s, "#FFFFFF", 0.95, f"{p}g"))
    if cloud:
        o.append(f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.4)}" rx="{f(w * 0.7)}" ry="{f(h * 0.42)}" fill="#FFFDF0" opacity="0.8"></ellipse>'
                 + clouds(w, h * 0.3, seed, n=6, color="#FFFFFF", op=0.85, h=h))
        for i, x in enumerate((0.3, 0.5, 0.7)):
            o.append(E.kneel(w * x, b, s * 0.8, color=[ROBES["peter"], ROBES["james"], ROBES["john"]][i], skin="#B98A6E"))
        return "".join(o)
    o.append(jesus(p, jx, jy, s, glow=False))
    if not after:
        o.append(f'<ellipse cx="{f(jx)}" cy="{f(jy - 96 * s)}" rx="{f(34 * s)}" ry="{f(100 * s)}" fill="#FFFFFF" opacity="0.55"></ellipse>')
        o.append(glow(w * 0.24, jy - 100 * s, 120 * s, "#FFF4C2", 0.7, f"{p}m") + moses(p, w * 0.24, jy + 10 * s, s * 0.92))
        o.append(glow(w * 0.76, jy - 100 * s, 120 * s, "#FFF4C2", 0.7, f"{p}e") + elijah_fig(p, w * 0.76, jy + 10 * s, s * 0.92, flip=True))
        for i, x in enumerate((0.3, 0.5, 0.7)):
            o.append(E.kneel(w * x, b, s * 0.7, color=[ROBES["peter"], ROBES["james"], ROBES["john"]][i], skin="#B98A6E", flip=x > 0.5))
    else:
        for i, x in enumerate((0.26, 0.74, 0.84)):
            o.append(disciple(p, w * x, b, s * 0.9, ["peter", "james", "john"][i], flip=x > 0.5))
    return "".join(o)

def boy_healed(p, w, h, seed, kneeling=True):
    """A man kneeling before Jesus for his son; healed: the boy standing quiet beside his father, the father's hand on his
    shoulder, the multitude behind (no demon drawn)."""
    b = h * 0.94
    o = [road_scene(p, w, h, seed)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(crowd(p, w * 0.62, w * 0.98, b - 30 * s, b - 30 * s - 150 * s, 7, seed, flip=True))
    o.append(jesus(p, w * 0.24, b, s, up=UP_BLESS if not kneeling else None))
    if kneeling:
        o.append(E.kneel(w * 0.42, b, s * 0.86, color="#6A5A3A", flip=True, skin=SKIN))
    else:
        o.append(man(p, w * 0.5, b, s * 0.98, "#6A5A3A", flip=True, up=[(-22, -158), (-34, -150), (-50, -130)]))
        o.append(mk.person(p, round(w * 0.42), round(b), round(s * 0.62, 3), body=SKIN, cloth="#C8B898", kind="Tunic", sw=3, flip=True))
    return "".join(o)

def mountain_move(p, w, h, seed):
    """Faith as a grain of mustard seed, and ye shall say unto this mountain, Remove hence to yonder place: a great mountain
    lifted off its place over the plain, its root-shadow left behind; the tiny seed in a circle of light."""
    o = [sky(w, h, "#5A3A6A", "#FFC890"), ground(w, h, h * 0.8, "#A88A5A", dy=0),
         f'<ellipse cx="{f(w * 0.36)}" cy="{f(h * 0.82)}" rx="{f(w * 0.2)}" ry="{f(h * 0.03)}" fill="#5A4030"></ellipse>',
         f'<path d="M{f(w * 0.36)} {f(h * 0.56)} L {f(w * 0.5)} {f(h * 0.2)} L {f(w * 0.58)} {f(h * 0.26)} L {f(w * 0.7)} {f(h * 0.14)} L {f(w * 0.86)} {f(h * 0.56)} C {f(w * 0.7)} {f(h * 0.62)} {f(w * 0.5)} {f(h * 0.62)} {f(w * 0.36)} {f(h * 0.56)} Z" fill="#7A6A7A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<path d="M{f(w * 0.34)} {f(h * 0.74)} L {f(w * 0.46)} {f(h * 0.66)} M{f(w * 0.42)} {f(h * 0.76)} L {f(w * 0.54)} {f(h * 0.68)}" stroke="#F3EFE6" stroke-width="2" opacity="0.6"></path>',
         glow(w * 0.12, h * 0.3, h * 0.16, "#FFF4C2", 0.9, f"{p}g"), f'<circle cx="{f(w * 0.12)}" cy="{f(h * 0.3)}" r="3" fill="#5A3A1A"></circle>']
    return "".join(o)

def tribute(p, w, h, seed):
    """They that received the half-shekel came to Peter: in the street of Capernaum, two collectors with a money-bag and a
    tablet before Peter at the door of the house."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.86, seed, hmin=0.4, hmax=0.56), pavement(w, h, h * 0.86)]
    s = fit(b, max(h * 0.24, b - 230))
    bag = '<path d="M-60 -110 C -70 -96 -64 -80 -52 -80 C -40 -80 -36 -96 -46 -110 Z" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(disciple(p, w * 0.3, b, s, "peter"))
    o.append(man(p, w * 0.5, b, s * 0.96, "#3A4A6A", flip=True, up=[(-22, -158), (-40, -130), (-56, -112)], extra=bag) + man(p, w * 0.62, b, s * 0.94, "#5A4A3A", flip=True))
    return "".join(o)

def hook_fish(p, w, h, seed):
    """Go thou to the sea, and cast a hook, and take up the fish that first cometh up: Peter on the rocks at the water's edge
    with his line, the fish drawn up on the hook, a silver shekel shining in its mouth."""
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.36, seed, color="#8A9A7A", amp=10, step=90), lake(w, h, h * 0.44, seed, n=10),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.6)} C {f(w * 0.1)} {f(h * 0.56)} {f(w * 0.24)} {f(h * 0.62)} {f(w * 0.34)} {f(h * 0.72)} L {f(w * 0.4)} {f(h + 10)} Z" fill="#8A8478" stroke="{INK}" stroke-width="2.4"></path>']
    s = fit(h * 0.62, max(h * 0.1, h * 0.62 - 220))
    rod = '<path d="M-40 -150 L -120 -230" stroke="#5A3A22" stroke-width="4"></path>'
    o.append(disciple(p, w * 0.2, h * 0.62, s, "peter", up=[(-22, -158), (-36, -150), (-44, -150)]))
    fx, fy = w * 0.52, h * 0.52
    o.append(f'<path d="M{f(w * 0.2 - 120 * s)} {f(h * 0.62 - 230 * s)} L {f(w * 0.2 - 44 * s)} {f(h * 0.62 - 150 * s)}" stroke="#5A3A22" stroke-width="{f(4 * s)}"></path>'
             f'<path d="M{f(w * 0.2 - 120 * s)} {f(h * 0.62 - 230 * s)} Q {f(fx - 40)} {f(fy - h * 0.3)} {f(fx)} {f(fy - 10)}" stroke="#E8E2D6" stroke-width="1.4" fill="none"></path>')
    k = max(1.0, h / 160)
    o.append(creature("fish", fx, fy, k, color="#8FB8C8") + glow(fx + 26 * k, fy - 6 * k, 14 * k, "#FFFDF0", 0.9, f"{p}c")
             + f'<circle cx="{f(fx + 26 * k)}" cy="{f(fy - 6 * k)}" r="{f(4 * k)}" fill="#D8D8E0" stroke="{INK}" stroke-width="1"></circle>')
    return "".join(o)

def baskets_n(p, w, h, seed, n=7):
    """Seven baskets full (baskets, with n of them)."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#3A2A5A", "#E8A86A"), hills(w, h, h * 0.4, seed, color="#5A5A5A", amp=12, step=90), ground(w, h, h * 0.5, "#B8A06A", dy=0)]
    o.append(crowd(p, w * 0.04, w * 0.96, h * 0.6, h * 0.6 - h * 0.12, 16, seed))
    k = min(w / (n + 2) / 50, (b - h * 0.6) / 60)
    for i in range(n):
        x = w * (0.5 + (i - (n - 1) / 2) * 0.1)
        o.append(f'<path d="M{f(x - 22 * k)} {f(b - 40 * k)} L {f(x + 22 * k)} {f(b - 40 * k)} L {f(x + 16 * k)} {f(b)} L {f(x - 16 * k)} {f(b)} Z" fill="#C8A060" stroke="{INK}" stroke-width="1.8"></path>'
                 f'<path d="M{f(x - 22 * k)} {f(b - 40 * k)} C {f(x - 16 * k)} {f(b - 56 * k)} {f(x + 16 * k)} {f(b - 56 * k)} {f(x + 22 * k)} {f(b - 40 * k)} Z" fill="#D9A25A" stroke="{INK}" stroke-width="1.6"></path>')
    return "".join(o)
