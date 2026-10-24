"""Drawings for Matthew 18–20: the little child set in the midst; the millstone by the sea; the lost sheep on the mountains;
the king's reckoning and the unmerciful servant (the debtor seized by the cloak, the prison door shut — no torment drawn);
the borders of Judaea beyond the Jordan; the little children blessed; the rich young man going away; the camel and the
needle's eye; the twelve thrones in light (empty); the vineyard — the hiring at dawn and through the day, the marketplace of
the idle, the paying at even; the road up to Jerusalem; the mother of the sons of Zebedee; the cup; Jericho and the two
blind men by the way side. Built on mat.art6."""
from mat.art6 import *
from mat.art6 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE
from ntcast import JESUS_SKIN, JESUS_HAIR, JESUS_TUNIC, JESUS_MANTLE, ROBES
import random, math
from job.art import seated, smoke
from oba.minor import cup, sea
import exodus as E

def child_midst(p, w, h, seed):
    """He called to him a little child, and set him in the midst of them: in a courtyard, Jesus with his hand on a small
    child's shoulder, the disciples standing round."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.7, seed, hmin=0.34, hmax=0.46, stairs=False), pavement(w, h, h * 0.7)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(jesus(p, w * 0.42, b, s, up=[(-22, -158), (-36, -140), (-50, -120)]))
    o.append(mk.person(p, round(w * 0.42 - 64 * s), round(b), round(s * 0.5, 3), body=SKIN, cloth="#C8783A", kind="Tunic", sw=3, flip=True))
    for i, x in enumerate((0.12, 0.22, 0.62, 0.72, 0.82, 0.92)):
        o.append(disciple(p, w * x, b - 4 * (i % 2), s * 0.92, TWELVE[i] if i > 3 else ["peter", "andrew", "james", "john"][i], flip=x > 0.5))
    return "".join(o)

def millstone(p, w, h, seed):
    """A great millstone hanged about his neck, sunk in the depth of the sea: a heavy millstone on the rocks at the edge of
    a dark, deep sea, a rope coiled beside it — no one drawn."""
    o = [sky(w, h, "#2A2A4A", "#6A7A9A"), sea(w, h, h * 0.5, seed, color="#1A3A5A", deep="#0A1A2E", rough=True),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.62)} C {f(w * 0.2)} {f(h * 0.58)} {f(w * 0.36)} {f(h * 0.66)} {f(w * 0.46)} {f(h * 0.8)} L {f(w * 0.5)} {f(h + 10)} Z" fill="#5A5A62" stroke="{INK}" stroke-width="2.4"></path>']
    k = min(w, h) * 0.24
    cx, cy = w * 0.22, h * 0.72
    o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(k)}" ry="{f(k * 0.42)}" fill="#8A8478" stroke="{INK}" stroke-width="2.6"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy - k * 0.1)}" rx="{f(k)}" ry="{f(k * 0.42)}" fill="#A8A296" stroke="{INK}" stroke-width="2.6"></ellipse>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy - k * 0.1)}" rx="{f(k * 0.2)}" ry="{f(k * 0.08)}" fill="#2A2A2E"></ellipse>'
             f'<path d="M{f(cx + k * 1.1)} {f(cy + k * 0.2)} c 20 -10 40 10 20 20 c -20 10 -40 -10 -20 -20" stroke="#C8A878" stroke-width="4" fill="none"></path>')
    return "".join(o)

def lost_sheep(p, w, h, seed):
    """He leaveth the ninety and nine, and goeth unto the mountains, and seeketh that which goeth astray: high on the rocky
    mountain a shepherd bearing the found sheep on his shoulders; far below, the flock in the fold."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A6A", "#FFC890"),
         f'<path d="M{f(w * 0.2)} {f(h + 10)} L {f(w * 0.46)} {f(h * 0.24)} L {f(w * 0.56)} {f(h * 0.3)} L {f(w * 0.7)} {f(h * 0.16)} L {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h + 10)} Z" fill="#7A6A6A" stroke="{INK}" stroke-width="2.4"></path>',
         ground(w, h, h * 0.84, "#8AA84A", dy=0),
         f'<ellipse cx="{f(w * 0.14)}" cy="{f(h * 0.92)}" rx="{f(w * 0.12)}" ry="{f(h * 0.05)}" fill="none" stroke="#8A7A6A" stroke-width="5"></ellipse>']
    o.append(sheep_row(w * 0.04, w * 0.24, h * 0.94, 7, seed, s=max(0.12, h / 1800)))
    s = fit(h * 0.33, h * 0.12)
    sh = '<path d="M-26 -176 C -30 -196 -6 -204 10 -196 C 26 -196 34 -180 24 -170 C 10 -164 -16 -164 -26 -176 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2"></path>'
    o.append(man(p, w * 0.7, h * 0.33, s, "#6A4A2A", up=[(-22, -158), (-28, -180), (-18, -190)], extra=sh))
    return "".join(o)

def king_hall(p, w, h, seed, kneel=True, angry=False):
    """A certain king making a reckoning with his servants: the king on his throne in his hall, the stewards with their
    tablets, the servant fallen down before him; angry=True: the king risen, his arm pointing to the door."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bgr(w, h, "#2A3A5A")]
    for x in (0.06, 0.34, 0.66, 0.94):
        o.append(f'<rect x="{f(w * x - 14)}" y="-10" width="28" height="{f(b + 10)}" fill="#C8963E" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#5A4A3A" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, max(h * 0.24, b - 230))
    o.append(f'<path d="M{f(w * 0.14)} {f(b)} L {f(w * 0.14)} {f(b - 150 * s)} L {f(w * 0.14 + 100 * s)} {f(b - 150 * s)} L {f(w * 0.14 + 100 * s)} {f(b)} Z" fill="#E8B830" stroke="{INK}" stroke-width="2.4"></path>')
    o.append(king(p, w * 0.14 + 50 * s, b, s, "#2A4A8A", up=UP_BLESS if angry else None))
    if kneel: o.append(E.kneel(w * 0.5, b, s * 0.86, color="#6A5A3A", flip=True, skin=SKIN))
    o.append(man(p, w * 0.72, b, s * 0.94, "#3A4A6A", flip=True) + man(p, w * 0.84, b, s * 0.92, "#6A5A4A", flip=True))
    return "".join(o)

def seized(p, w, h, seed):
    """That servant laid hold on his fellow-servant: in the street, one man gripping the other by his cloak, the other
    fallen to his knees pleading."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#C8A890", "#F3E8C8"), houses(w, h, h * 0.8, seed, hmin=0.36, hmax=0.5), pavement(w, h, h * 0.8)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(man(p, w * 0.4, b, s, "#6A5A3A", up=[(-22, -158), (-46, -140), (-66, -124)]))
    o.append(E.kneel(w * 0.4 + 90 * s, b, s * 0.86, color="#5A5A6A", flip=True, skin=SKIN))
    return "".join(o)

def children_blessed(p, w, h, seed):
    """Suffer the little children to come unto me: Jesus seated, his hands on the heads of the children about him, their
    mothers behind; two of the disciples standing aside."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#9AAA7A", amp=10, step=80), ground(w, h, h * 0.54, "#9AAA5A", dy=0)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(jesus_seated(w * 0.32, b, s * 0.9))
    r = random.Random(seed)
    for i, x in enumerate((0.16, 0.44, 0.52, 0.6)):
        o.append(mk.person(p, round(w * x), round(b), round(s * r.uniform(0.42, 0.52), 3), body=SKIN, cloth=r.choice(["#C8783A", "#E8B830", "#C2456A", "#5A8A3A"]), kind="Tunic", sw=3, flip=x < 0.3))
    o.append(woman_fig(p, w * 0.7, b, s * 0.9, "#6A3A5A", flip=True) + woman_fig(p, w * 0.78, b, s * 0.88, "#2A5A6A", "#4A7A8A", flip=True))
    o.append(disciple(p, w * 0.9, b, s * 0.94, "peter", flip=True) + disciple(p, w * 0.06, b, s * 0.94, "andrew"))
    return "".join(o)

def rich_away(p, w, h, seed):
    """He went away sorrowful, for he had great possessions: the young man in his fine purple-banded robe walking off down
    the road, head bowed; Jesus and the disciples watching him go."""
    b = h * 0.94
    o = [road_scene(p, w, h, seed, "dusk")]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(jesus(p, w * 0.2, b, s) + disciple(p, w * 0.1, b, s * 0.94, "peter"))
    o.append(man(p, w * 0.72, b, s * 0.96, "#7A2A6A", kind="Robe", extra=A.headcloth("#E8B830", cord="#7A2A6A")))
    return "".join(o)

def needle(p, w, h, seed):
    """A camel through a needle's eye: a great bronze needle standing upright like a pillar, its eye a narrow slit of light,
    a laden camel before it."""
    b = h * 0.9
    o = [sky(w, h, "#FFD89A", "#F3B870"), hills(w, h, h * 0.6, seed, color="#C8985A", amp=12, step=80), ground(w, h, h * 0.7, "#D8B07A", dy=0)]
    nx = w * 0.66
    o.append(f'<path d="M{f(nx - 14)} {f(b)} L {f(nx - 10)} {f(h * 0.1)} C {f(nx - 8)} {f(h * 0.04)} {f(nx + 8)} {f(h * 0.04)} {f(nx + 10)} {f(h * 0.1)} L {f(nx + 14)} {f(b)} L {f(nx)} {f(b + 14)} Z" fill="#C8963E" stroke="{INK}" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(nx)}" cy="{f(h * 0.16)}" rx="3" ry="{f(h * 0.04)}" fill="#FFF4C2" stroke="{INK}" stroke-width="1.2"></ellipse>')
    o.append(J1.camel(w * 0.3, b, min(1.0, (b - h * 0.3) / 200), color="#B5844A"))
    return "".join(o)

def thrones(p, w, h, seed):
    """Twelve thrones, judging the twelve tribes of Israel: twelve empty thrones in a curve of white and gold light — no
    one seated on them."""
    o = [bgr(w, h, "#12113A"), glow(w * 0.5, h * 0.5, max(w, h) * 0.6, "#FFE680", 0.4, f"{p}g"), rays(w * 0.5, h * 0.2, 30, 20, max(w, h), color="#FFF4C2", op=0.2)]
    for i in range(12):
        a = math.pi * (0.1 + 0.8 * i / 11)
        x = w * 0.5 - math.cos(a) * w * 0.44; y = h * 0.86 - math.sin(a) * h * 0.4
        k = max(0.4, h / 600)
        o.append(f'<path d="M{f(x - 18 * k)} {f(y)} L {f(x - 18 * k)} {f(y - 60 * k)} L {f(x + 18 * k)} {f(y - 60 * k)} L {f(x + 18 * k)} {f(y)} Z" fill="#F3EFE6" stroke="#E8B830" stroke-width="2"></path>'
                 f'<rect x="{f(x - 22 * k)}" y="{f(y - 24 * k)}" width="{f(44 * k)}" height="{f(8 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="1.2"></rect>')
    return "".join(o)

def vineyard(p, w, h, seed, tone="dawn", hire=True, pay=False):
    """The householder's vineyard: rows of vines on the hillside, the watch-tower, the laborers at work; hire=True: the
    householder at the gate in the morning with a man he hires; pay=True: at even, the steward at a table paying the
    laborers in a line, each a shilling."""
    b = h * 0.94
    top, bot = {"dawn": ("#3A3A7A", "#FFC890"), "day": ("#8FD0E2", "#FFF4C2"), "dusk": ("#4A2A5A", "#FF9A5A")}[tone]
    o = [mk.defs(p, *ALL), sky(w, h, top, bot), hills(w, h, h * 0.36, seed, color="#8A7A6A", amp=12, step=80), ground(w, h, h * 0.44, "#A8885A", dy=0),
         vines(w * 0.04, w * 0.96, h * 0.52, h * 0.72, seed, rows=3)]
    o.append(f'<rect x="{f(w * 0.82)}" y="{f(h * 0.2)}" width="{f(w * 0.08)}" height="{f(h * 0.24)}" fill="#B89A6A" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.8)} {f(h * 0.2)} L {f(w * 0.86)} {f(h * 0.14)} L {f(w * 0.92)} {f(h * 0.2)} Z" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></path>')
    s = fit(b, max(h * 0.4, b - 200))
    master = lambda x, fl=False, up=None: man(p, x, b, s, "#2A4A6A", kind="Robe", flip=fl, up=up, extra=A.headcloth("#E8E2D6", cord="#E8B830") + GREY_BEARD)
    if pay:
        o.append(f'<rect x="{f(w * 0.12)}" y="{f(b - 40 * s)}" width="{f(80 * s)}" height="{f(40 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>')
        o.append(master(w * 0.1))
        for i in range(6):
            o.append(man(p, w * (0.34 + 0.1 * i), b, s * (0.96 - 0.01 * i), random.Random(seed + i).choice(HEB), flip=True, up=UP_BLESS if i == 0 else None))
    elif hire:
        o.append(master(w * 0.3, up=UP_BLESS) + man(p, w * 0.46, b, s * 0.96, "#6A5A3A", flip=True))
    return "".join(o)

def idle(p, w, h, seed, late=False):
    """Others standing in the marketplace idle: men leaning by the wall in the empty market square, the sun high (late=True:
    low in the west, the eleventh hour)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5AB0D8", "#FFF4C2") if not late else sky(w, h, "#4A2A5A", "#FF9A5A"),
         sun(w * (0.5 if not late else 0.86), h * (0.12 if not late else 0.4), 14, color="#FFE680", op=0.3),
         houses(w, h, h * 0.8, seed, hmin=0.34, hmax=0.5, stairs=False), pavement(w, h, h * 0.8)]
    s = fit(b, max(h * 0.24, b - 230))
    for i in range(4):
        o.append(man(p, w * (0.5 + 0.1 * i), b, s * 0.94, random.Random(seed + i).choice(HEB), flip=True))
    o.append(man(p, w * 0.22, b, s, "#2A4A6A", kind="Robe", up=UP_BLESS, extra=A.headcloth("#E8E2D6", cord="#E8B830") + GREY_BEARD))
    return "".join(o)

def zebedee_mother(p, w, h, seed):
    """The mother of the sons of Zebedee with her sons, worshipping him: the woman kneeling before Jesus on the road, James
    and John standing behind her."""
    b = h * 0.94
    o = [road_scene(p, w, h, seed)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(jesus(p, w * 0.26, b, s))
    o.append(E.kneel(w * 0.46, b, s * 0.86, color="#8A5A3A", flip=True, skin=SKIN))
    o.append(disciple(p, w * 0.62, b, s * 0.96, "james", flip=True) + disciple(p, w * 0.72, b, s * 0.94, "john", flip=True))
    o.append(disciple(p, w * 0.9, b, s * 0.9, "peter", flip=True))
    return "".join(o)

def the_cup(p, w, h, seed):
    """Are ye able to drink the cup that I am about to drink?: a single cup on a dark table, a cold light on it."""
    o = [bgr(w, h, "#1A1630"), glow(w * 0.5, h * 0.5, h * 0.6, "#9AA8C8", 0.5, f"{p}g"),
         f'<rect x="-10" y="{f(h * 0.78)}" width="{f(w + 20)}" height="{f(h)}" fill="#4A2A1E" stroke="{INK}" stroke-width="2"></rect>',
         cup(w * 0.5, h * 0.78, max(0.6, h / 220), color="#C8963E")]
    return "".join(o)

def jericho(p, w, h, seed, healed=False):
    """As they went out from Jericho: the palms of Jericho and its gate behind, the multitude on the road, two blind men in
    grey sitting by the way side crying out; healed=True: the two standing, Jesus' hand on their eyes."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), walls(w * 0.6, w + 10, h * 0.6, h * 0.28, seed, towers=2), ground(w, h, h * 0.6, "#D8C090", dy=0)]
    for x in (0.08, 0.18, 0.5):
        o.append(f'<g transform="translate({f(w * x)} {f(h * 0.62)}) scale({f(h * 0.3 / 210)})">' + J1.palm(0, 0, 1) + '</g>')
    s = fit(b, max(h * 0.24, b - 230))
    if healed:
        o.append(jesus(p, w * 0.22, b, s, up=UP_BLESS))
        o.append(man(p, w * 0.38, b, s * 0.96, "#7A7A80", flip=True, up=UP_HIGH) + man(p, w * 0.48, b, s * 0.94, "#6A6A72", flip=True))
    else:
        o.append(crowd(p, w * 0.56, w * 0.98, b, b - 160 * s, 6, seed, flip=True))
        o.append(jesus(p, w * 0.44, b, s, flip=True))
        o.append(seated(w * 0.14, b, s * 0.8, "#7A7A80", head="#6A6A72", beard="#4A3A2E") + seated(w * 0.26, b, s * 0.8, "#6A6A72", head="#7A7A80", beard="#3A2A1E"))
    return "".join(o)
