"""Drawings for John 1–2, and the helpers the later John drawings share. Built on Mark's drawings (mrk.art9, which carries
Matthew's: the lake and its boats, houses, synagogues, the temple, the garden, Golgotha and the tomb).

The prologue (1:1–13) draws no figure: the Word is light over the void, all things made through him under it, the light
shining in the darkness, the true light coming into the world over its sleeping towns, the doors shut against it and the
doors that open to it. The Word became flesh (1:14) is the first time Jesus is seen: walking into a village at dawn in a
soft gold light. Then John's witness at Bethany beyond the Jordan before the priests and Levites; Behold, the Lamb of God;
the Spirit descending as a dove of light; the two following; Andrew bringing Simon; Philip and Nathanael under the fig
tree; the heaven opened and the angels of light ascending and descending. The marriage in Cana: the courtyard and the
feast, the six stone waterpots filled to the brim, the ruler of the feast tasting. The temple: the scourge of cords lifted,
the sheep and oxen driven out, the tables overthrown and the money poured out, the doves freed; no one struck.
Every function takes (p, w, h, seed, ...) — p, a prefix unique to the panel, names the figure defs and gradients."""
from mrk.art9 import *
from mrk.art9 import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, jesus_risen, roman_fig, torch
import random, math
from genesis.art2 import dove as _dove
from genesis.art5 import well
from job.art import seated, clouds, smoke
from samuel1 import cow
import exodus as E, exodus3 as E3

# ---- shared helpers ---------------------------------------------------------------------------------------------------
def P(d, fill, sw=2.2, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="{sw}"{extra}></path>'

def coals(x, y, s=1.0, seed=1, fish=False, bread=False):
    """A fire of coals on the ground (18:18, 21:9): a ring of stones, the glowing coals, a low flame; fish=True a fish laid
    on it, bread=True a loaf beside it."""
    r = random.Random(seed)
    o = [glow(x, y - 20 * s, 90 * s, "#FF8A3D", 0.7, f"cl{seed}{int(x)}")]
    for k in range(9):
        a = math.pi * k / 8
        o.append(f'<ellipse cx="{f(x - 46 * s * math.cos(a))}" cy="{f(y - 2 * s + 4 * s * math.sin(a))}" rx="{f(9 * s)}" ry="{f(6 * s)}" fill="#6A6058" stroke="{INK}" stroke-width="1.4"></ellipse>')
    for _ in range(14):
        o.append(f'<circle cx="{f(x + r.uniform(-34, 34) * s)}" cy="{f(y - r.uniform(2, 10) * s)}" r="{f(r.uniform(3, 6) * s)}" fill="{r.choice(["#FF6A2A", "#FFB020", "#C8401A"])}" stroke="#3A0A08" stroke-width="0.8"></circle>')
    o.append(E.flame(x, y - 6 * s, 26 * s, 30 * s, 0))
    if fish:
        o.append(f'<g transform="translate({f(x)} {f(y - 8 * s)}) scale({f(s * 0.7)})"><path d="M-34 0 C -20 -12 14 -12 26 0 C 14 12 -20 12 -34 0 Z" fill="#C8C2D6" stroke="{INK}" stroke-width="1.6"></path>'
                 '<path d="M26 0 L 40 -10 L 40 10 Z" fill="#A8A2B6" stroke="#0D0D0F" stroke-width="1.4"></path><circle cx="-24" cy="-2" r="2" fill="#0D0D0F"></circle></g>')
    if bread:
        o.append(f'<ellipse cx="{f(x + 66 * s)}" cy="{f(y - 6 * s)}" rx="{f(20 * s)}" ry="{f(10 * s)}" fill="#D9A25A" stroke="{INK}" stroke-width="1.6"></ellipse>'
                 f'<path d="M{f(x + 54 * s)} {f(y - 8 * s)} q {f(12 * s)} -6 {f(24 * s)} 0" stroke="#8A5A2A" stroke-width="1.4" fill="none"></path>')
    return "".join(o)

def stone_pot(x, y, s=1.0, fill=None):
    """One of the six waterpots of stone (2:6): a tall grey stone jar with a wide mouth and a ridge; fill a colour shows it
    full to the brim (water "#5AA8C8", wine "#7A1A2A")."""
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">',
         P("M-26 0 C -34 -20 -36 -60 -30 -88 L -24 -96 L 24 -96 L 30 -88 C 36 -60 34 -20 26 0 Z", "#A8A298", 2.4),
         '<path d="M-32 -70 C -10 -66 10 -66 32 -70" stroke="#7A766E" stroke-width="2" fill="none"></path>',
         '<path d="M-22 -40 C -18 -30 -18 -16 -20 -6" stroke="#C8C2B8" stroke-width="3" fill="none" opacity="0.7"></path>',
         P("M-28 -96 L 28 -96 L 26 -104 L -26 -104 Z", "#8A847A", 2)]
    if fill: o.append(f'<ellipse cx="0" cy="-102" rx="23" ry="4" fill="{fill}" stroke="{INK}" stroke-width="1.2"></ellipse>')
    return "".join(o) + "</g>"

def pitcher_carry(x, y, s=1.0, color="#B5652E"):
    """A water-pitcher (held: x, y its foot)."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">' + P("M-12 0 C -20 -8 -20 -26 -10 -32 L -6 -40 L 6 -40 L 10 -32 C 20 -26 20 -8 12 0 Z", color, 1.8)
            + '<path d="M10 -30 C 22 -28 22 -14 12 -12" stroke="#0D0D0F" stroke-width="1.8" fill="none"></path></g>')

def courtyard(w, h, b, seed, night_=False, lamps=True):
    """The courtyard of a house of Galilee: plastered walls, a roof-beam, an arch, an awning, lamps on the ledge."""
    wall = "#3A2E3A" if night_ else "#D8C098"
    o = [bgr(w, h, "#1E1A3A" if night_ else "#8FD0E2"),
         f'<rect x="-10" y="{f(h * 0.12)}" width="{f(w + 20)}" height="{f(b - h * 0.12)}" fill="{wall}" stroke="{INK}" stroke-width="2"></rect>',
         f'<path d="M{f(w * 0.36)} {f(b)} L {f(w * 0.36)} {f(h * 0.42)} Q {f(w * 0.5)} {f(h * 0.24)} {f(w * 0.64)} {f(h * 0.42)} L {f(w * 0.64)} {f(b)} Z" fill="{"#14122A" if night_ else "#B8A07A"}" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M-10 {f(h * 0.12)} Q {f(w * 0.25)} {f(h * 0.2)} {f(w * 0.5)} {f(h * 0.12)} Q {f(w * 0.75)} {f(h * 0.2)} {f(w + 10)} {f(h * 0.12)}" stroke="#3A7A2A" stroke-width="7" fill="none"></path>',
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>']
    if lamps:
        for x in (0.14, 0.7):
            o.append(f'<rect x="{f(w * x - 30)}" y="{f(h * 0.3)}" width="60" height="8" fill="#6A4A2A" stroke="{INK}" stroke-width="1.6"></rect>' + clay_lamp(w * x, h * 0.3, max(0.5, h / 420)))
    return "".join(o)

# ---- John 1: the Word, the light ------------------------------------------------------------------------------------
def word_light(p, w, h, seed, kind="void"):
    """The Word before 1:14 — light, never a figure.
    void: the beginning — one point of white light in the black void, its rays going out, the darkness about it uneven.
    made: all things made through him — the light above, the stars sown about it, a world of sea and hills below.
    life: the life the light of men — the light falling on green hills, a tree, the birds, a town's first lamps.
    shineth: the light shineth in the darkness — a shaft of light breaking down through a mass of darkness, untouched.
    world: the true light coming into the world — the sleeping world at night, the light rising over its rim.
    glory: the only begotten from the Father — a blaze of gold light, full of grace and truth, over the hills."""
    r = random.Random(seed)
    if kind == "void":
        cx, cy = w * 0.5, h * 0.5
        o = [bgr(w, h, "#030308")]
        for _ in range(9):
            o.append(f'<ellipse cx="{f(r.uniform(0, w))}" cy="{f(r.uniform(0, h))}" rx="{f(r.uniform(80, 220))}" ry="{f(r.uniform(30, 90))}" fill="#14122A" opacity="{r.uniform(0.3, 0.7):.2f}"></ellipse>')
        o += [rays(cx, cy, 40, 18, max(w, h) * 0.9, color="#FFF4C2", op=0.22, sw=2), glow(cx, cy, min(w, h) * 0.7, "#FFE680", 0.75, f"{p}g"),
              glow(cx, cy, min(w, h) * 0.22, "#FFFFFF", 1.0, f"{p}g2"), f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(max(6, min(w, h) * 0.03))}" fill="#FFFFFF"></circle>']
        return "".join(o)
    if kind == "made":
        cx, cy = w * 0.5, h * 0.18
        o = [sky(w, h, "#05051A", "#1E1650"), mk.stars(90, w, h * 0.7, seed),
             rays(cx, cy, 36, 14, max(w, h), color="#FFF4C2", op=0.18, sw=2), glow(cx, cy, h * 0.5, "#FFE680", 0.7, f"{p}g"),
             f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(max(6, h * 0.03))}" fill="#FFFFFF"></circle>',
             moon(w * 0.84, h * 0.3, max(6, h * 0.03)), sun(w * 0.14, h * 0.36, max(8, h * 0.035), color="#FFD23F", op=0.25),
             f'<path d="M-10 {f(h * 0.78)} C {f(w * 0.3)} {f(h * 0.62)} {f(w * 0.7)} {f(h * 0.62)} {f(w + 10)} {f(h * 0.78)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1F6F9A" stroke="{INK}" stroke-width="2"></path>',
             hills(w, h, h * 0.8, seed, color="#3F7A34", amp=14, step=70),
             f'<path d="M{f(w * 0.3)} {f(h * 0.72)} C {f(w * 0.4)} {f(h * 0.66)} {f(w * 0.6)} {f(h * 0.66)} {f(w * 0.7)} {f(h * 0.72)}" stroke="#FFF4C2" stroke-width="3" fill="none" opacity="0.5"></path>']
        for i in range(3): o.append(tree(w * (0.12 + 0.36 * i), h * 0.98, h / 420, color="#2E6B3A", seed=seed + i))
        return "".join(o)
    if kind == "life":
        o = [sky(w, h, "#8FD0E2", "#FFF4C2"), shaft(w * 0.5, w, h, top_w=0.1, bot_w=0.4, color="#FFF4C2", op=0.45),
             glow(w * 0.5, 0, h * 0.7, "#FFFFFF", 0.8, f"{p}g"), hills(w, h, h * 0.56, seed, color="#7A9A5A", amp=14, step=90),
             hill_town(w * 0.72, h * 0.72, w * 0.32, h * 0.22, seed, hill="#8AAA5A"), ground(w, h, h * 0.76, "#9CCB5E", dy=-4),
             birds(5, w * 0.1, w * 0.5, h * 0.12, h * 0.36, seed)]
        o.append(tree(w * 0.16, h * 0.98, h / 330, color="#3F7A34", seed=seed))
        return "".join(o)
    if kind == "shineth":
        o = [bgr(w, h, "#05050E")]
        for _ in range(14):
            o.append(f'<ellipse cx="{f(r.uniform(-0.1, 1.1) * w)}" cy="{f(r.uniform(0, 1) * h)}" rx="{f(r.uniform(60, 180))}" ry="{f(r.uniform(30, 80))}" fill="{r.choice(["#14101E", "#1A1428", "#0E0A16"])}" opacity="0.9"></ellipse>')
        o += [shaft(w * 0.56, w, h, top_w=0.05, bot_w=0.26, color="#FFF4C2", op=0.55), shaft(w * 0.56, w, h, top_w=0.02, bot_w=0.1, color="#FFFFFF", op=0.6),
              glow(w * 0.56, h * 0.06, h * 0.4, "#FFFFFF", 0.95, f"{p}g"), glow(w * 0.56, h, h * 0.4, "#FFE680", 0.6, f"{p}g2")]
        return "".join(o)
    if kind == "world":
        o = [sky(w, h, "#05051A", "#2A2050"), mk.stars(70, w, h * 0.5, seed),
             f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.3)} {f(h * 0.5)} {f(w * 0.7)} {f(h * 0.5)} {f(w + 10)} {f(h * 0.62)}" stroke="#FFE680" stroke-width="{f(max(6, h * 0.03))}" fill="none" opacity="0.5"></path>',
             glow(w * 0.62, h * 0.54, h * 0.5, "#FFE680", 0.85, f"{p}g"),
             f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.3)} {f(h * 0.5)} {f(w * 0.7)} {f(h * 0.5)} {f(w + 10)} {f(h * 0.62)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#14142E" stroke="{INK}" stroke-width="2"></path>']
        for i, x in enumerate((0.16, 0.44, 0.8)):
            o.append(hill_town(w * x, h * (0.86 + 0.04 * (i % 2)), w * 0.24, h * 0.18, seed + i, hill="#1E1E3A", color=("#3A3A5A", "#2E2E4A", "#44445E")))
        return "".join(o)
    if kind == "glory":
        o = [sky(w, h, "#FFC14D", "#FFF4C2"), rays(w * 0.5, h * 0.42, 44, 20, max(w, h), color="#FFFFFF", op=0.35, sw=3),
             glow(w * 0.5, h * 0.42, h * 0.7, "#FFFFFF", 1.0, f"{p}g"), hills(w, h, h * 0.78, seed, color="#C8904A", amp=12, step=80),
             ground(w, h, h * 0.88, "#A8703A", dy=0)]
        return "".join(o)
    raise ValueError(kind)

def witness(p, w, h, seed):
    """There came a man, sent from God, whose name was John: John on a rock in the wilderness at first light, his arm
    stretched toward the light rising over the hills, to bear witness of it."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#2A2A5A", "#FFC890"), rays(w * 0.8, h * 0.5, 30, 20, w, color="#FFF4C2", op=0.25),
         glow(w * 0.8, h * 0.5, h * 0.5, "#FFE680", 0.8, f"{p}g"), hills(w, h, h * 0.52, seed, color="#6A4A5A", amp=20, step=70),
         hills(w, h, h * 0.68, seed + 1, color="#4A3440", amp=14, step=90), ground(w, h, h * 0.82, "#5A4038", dy=-6)]
    rx = w * 0.3
    o.append(f'<path d="M{f(rx - 80)} {f(b + 6)} C {f(rx - 66)} {f(b - 44)} {f(rx + 66)} {f(b - 50)} {f(rx + 80)} {f(b + 6)} Z" fill="#7A5A4A" stroke="{INK}" stroke-width="2.2"></path>')
    s = fit(b - 40, max(h * 0.16, b - 40 - 240))
    o.append(john_fig(p, rx, b - 40, s, flip=True, up=UP_BLESS))
    return "".join(o)

def shut_doors(p, w, h, seed, open_=False):
    """He came unto his own, and they that were his own received him not: a village street at night, every door shut and
    barred, a light at the end of the street with no one in it; open_=True: as many as received him — doors standing open,
    lamplight in them, people in the doorways turned toward the light."""
    b = h * 0.9
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#1E1650"), mk.stars(40, w, h * 0.3, seed),
         houses(w, h, b, seed, hmin=0.4, hmax=0.6, lit=open_, shut=not open_, color=("#5A5070", "#4A4262", "#6A5E7A")),
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A2440" stroke="{INK}" stroke-width="2"></rect>',
         glow(w * 0.5, b - h * 0.1, h * 0.45, "#FFE680", 0.9, f"{p}g"),
         f'<path d="M{f(w * 0.42)} {f(h + 10)} L {f(w * 0.48)} {f(b)} L {f(w * 0.52)} {f(b)} L {f(w * 0.58)} {f(h + 10)} Z" fill="#FFE680" opacity="0.35"></path>']
    if open_:
        bb = h * 0.98; s = fit(bb, bb - min(h * 0.6, 220))
        r = random.Random(seed)
        for i, x in enumerate((0.1, 0.27, 0.73, 0.9)):
            o.append(glow(w * x, bb - 100 * s, 110 * s, "#FFC14D", 0.6, f"{p}d{i}"))
            o.append(figure(p, w * x, bb, bb - 200 * s, r.choice(HEB), "woman" if i % 2 else "man", flip=x > 0.5))
    return "".join(o)

def flesh(p, w, h, seed):
    """The Word became flesh, and dwelt among us: the first time he is seen — a village of Galilee at sunrise, the white
    houses and the tents of the field, and Jesus walking into it in a soft gold light; the people at their doors looking."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A6A9A", "#FFE6A0"), sun(w * 0.5, h * 0.36, max(14, h * 0.05), color="#FFF4C2", op=0.4),
         glow(w * 0.5, h * 0.4, h * 0.6, "#FFF4C2", 0.7, f"{p}g"), hills(w, h, h * 0.46, seed, color="#8A8A6A", amp=12, step=90),
         houses(w, h, h * 0.74, seed, x0=-10, x1=w * 0.34, hmin=0.18, hmax=0.3), houses(w, h, h * 0.74, seed + 3, x0=w * 0.68, x1=w + 10, hmin=0.18, hmax=0.3),
         ground(w, h, h * 0.74, "#C8B07A", dy=0),
         f'<path d="M{f(w * 0.36)} {f(h + 10)} C {f(w * 0.42)} {f(h * 0.86)} {f(w * 0.46)} {f(h * 0.8)} {f(w * 0.48)} {f(h * 0.74)} L {f(w * 0.54)} {f(h * 0.74)} C {f(w * 0.56)} {f(h * 0.8)} {f(w * 0.62)} {f(h * 0.88)} {f(w * 0.7)} {f(h + 10)} Z" fill="#E0D0A8" stroke="{INK}" stroke-width="1.6"></path>']
    s = fit(b, max(h * 0.28, b - 240))
    o.append(jesus(p, w * 0.5, b, s))
    o.append(figure(p, w * 0.12, b - 12, b - 12 - 170 * s, "#6A4A3A", "woman", flip=False) + figure(p, w * 0.22, b - 4, b - 4 - 184 * s, "#3A4A6A", "man", flip=False))
    o.append(figure(p, w * 0.8, b - 8, b - 8 - 186 * s, "#5A6A3A", "man", flip=True) + figure(p, w * 0.9, b - 14, b - 14 - 160 * s, "#7A3A3A", "woman", flip=True))
    return "".join(o)

def inquiry(p, w, h, seed):
    """Bethany beyond the Jordan: John standing on the bank by the water, the priests and Levites sent from Jerusalem
    before him in white, asking, Who art thou?"""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.36, seed, color="#C8A06A", amp=18, step=80),
         f'<path d="M-10 {f(h * 0.46)} C {f(w * 0.3)} {f(h * 0.43)} {f(w * 0.6)} {f(h * 0.5)} {f(w + 10)} {f(h * 0.46)} L {f(w + 10)} {f(h * 0.64)} C {f(w * 0.6)} {f(h * 0.68)} {f(w * 0.3)} {f(h * 0.62)} -10 {f(h * 0.66)} Z" fill="#2C7DA8" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M-10 {f(h * 0.66)} C {f(w * 0.3)} {f(h * 0.62)} {f(w * 0.6)} {f(h * 0.68)} {f(w + 10)} {f(h * 0.64)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#B8A86A" stroke="{INK}" stroke-width="2"></path>']
    for k in range(10):
        x = w * (0.02 + 0.1 * k)
        o.append(f'<path d="M{f(x)} {f(h * 0.66)} l -4 -{f(h * 0.08)} M{f(x + 4)} {f(h * 0.66)} l 3 -{f(h * 0.1)}" stroke="#4A6A2A" stroke-width="2"></path>')
    s = fit(b, max(h * 0.24, b - 240))
    o.append(john_fig(p, w * 0.2, b, s, flip=True, up=UP_BLESS))
    for i, x in enumerate((0.56, 0.68, 0.8, 0.92)):
        o.append(scribe_fig(p, w * x, b - (i % 2) * 6, s * (0.98 - 0.02 * i), white=i % 2 == 0, flip=True))
    return "".join(o)

def behold_lamb(p, w, h, seed, two=False):
    """Behold, the Lamb of God: John on the bank of the Jordan, his arm stretched out toward Jesus walking along the river
    in the morning light; two=True: two of John's disciples turning from him to follow Jesus."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), glow(w * 0.76, h * 0.5, h * 0.5, "#FFF4C2", 0.6, f"{p}g"),
         hills(w, h, h * 0.36, seed, color="#C8A06A", amp=16, step=80), hills(w, h, h * 0.44, seed + 1, color="#7A9A5A", amp=10, step=60),
         f'<path d="M-10 {f(h * 0.5)} C {f(w * 0.3)} {f(h * 0.47)} {f(w * 0.6)} {f(h * 0.53)} {f(w + 10)} {f(h * 0.5)} L {f(w + 10)} {f(h * 0.66)} C {f(w * 0.6)} {f(h * 0.7)} {f(w * 0.3)} {f(h * 0.64)} -10 {f(h * 0.68)} Z" fill="#2C7DA8" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M-10 {f(h * 0.68)} C {f(w * 0.3)} {f(h * 0.64)} {f(w * 0.6)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.66)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#9AAA5A" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, max(h * 0.24, b - 240))
    o.append(john_fig(p, w * 0.18, b, s, flip=True, up=UP_BLESS))
    if two:
        o.append(disciple(p, w * 0.42, b - 4, s * 0.96, "andrew") + disciple(p, w * 0.52, b, s * 0.97, "john"))
    o.append(jesus(p, w * 0.78, b - 10, s * 0.9))
    return "".join(o)

def where_abide(p, w, h, seed):
    """Come, and ye shall see: the road at the tenth hour, the late sun low; Jesus turned round on the road beckoning, the
    two disciples coming after him, a house with its door open beyond."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A6A", "#FFC890"), sun(w * 0.86, h * 0.42, max(12, h * 0.05), color="#FFE680", op=0.4),
         hills(w, h, h * 0.46, seed, color="#8A6A5A", amp=12, step=80), ground(w, h, h * 0.6, "#C8A06A", dy=0),
         houses(w, h, h * 0.64, seed, x0=w * 0.66, x1=w + 10, hmin=0.2, hmax=0.3, lit=True),
         f'<path d="M-10 {f(h * 0.9)} C {f(w * 0.3)} {f(h * 0.8)} {f(w * 0.56)} {f(h * 0.7)} {f(w * 0.7)} {f(h * 0.64)}" stroke="#E0C898" stroke-width="{f(max(10, h * 0.07))}" fill="none"></path>']
    s = fit(b, max(h * 0.26, b - 230))
    o.append(jesus(p, w * 0.6, b, s, up=UP_CALL))
    o.append(disciple(p, w * 0.24, b, s * 0.96, "andrew") + disciple(p, w * 0.36, b - 6, s * 0.95, "john"))
    return "".join(o)

def brought(p, w, h, seed):
    """He brought him unto Jesus: Andrew leading his brother Simon by the arm along the shore, Jesus looking upon him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.34, seed, color="#7A8A6A", amp=14, step=90), lake(w, h, h * 0.42, seed),
         shore(w, h, h * 0.7)]
    s = fit(b, max(h * 0.26, b - 240))
    o.append(boat(p, w * 0.84, h * 0.6, s * 0.7, mast=True, flip=True))
    o.append(disciple(p, w * 0.42, b, s, "peter", flip=True) + disciple(p, w * 0.54, b, s * 0.98, "andrew", up=UP_BLESS))
    o.append(jesus(p, w * 0.18, b, s))
    return "".join(o)

def follow_me(p, w, h, seed):
    """He findeth Philip: and Jesus saith unto him, Follow me: the road out of Bethsaida by the lake, its white houses
    behind; Jesus beckoning, Philip turning from the town toward him."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.32, seed, color="#7A8A6A", amp=14, step=90), lake(w, h, h * 0.4, seed, n=8),
         shore(w, h, h * 0.56, color="#B8A06A"), houses(w, h, h * 0.62, seed, x0=w * 0.56, x1=w + 10, hmin=0.16, hmax=0.26), ground(w, h, h * 0.64, "#C8B07A", dy=0),
         f'<path d="M-10 {f(h * 0.88)} C {f(w * 0.3)} {f(h * 0.8)} {f(w * 0.5)} {f(h * 0.7)} {f(w * 0.6)} {f(h * 0.66)}" stroke="#E0D0A8" stroke-width="{f(max(10, h * 0.06))}" fill="none"></path>']
    s = fit(b, max(h * 0.26, b - 240))
    o.append(jesus(p, w * 0.22, b, s, flip=True, up=UP_CALL))
    o.append(mk.person(p, round(w * 0.56), round(b - 4), round(s * 0.97, 3), body="#C98E66", cloth="#7A6A3A", kind="Robe", sw=3, flip=True))
    return "".join(o)

def under_fig(p, w, h, seed, philip=True):
    """When thou wast under the fig tree, I saw thee: Nathanael sitting in the shade of a great fig tree outside a village;
    philip=True Philip coming along the path to him with his arm out."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.4, seed, color="#8A9A6A", amp=12, step=90),
         hill_town(w * 0.82, h * 0.6, w * 0.3, h * 0.2, seed, hill="#9AAA6A"), ground(w, h, h * 0.62, "#B8A86A", dy=0)]
    k = max(0.7, (b - h * 0.06) / 160)
    o.append(fig_tree(w * 0.26, b, k, fruit=True, seed=seed))
    s = fit(b, max(h * 0.26, b - 240))
    o.append(seated(w * 0.3, b, s * 0.85, "#5A6A5A", head="#2E5A5A", beard="#4A3A2A", flip=False))
    if philip:
        o.append(mk.person(p, round(w * 0.66), round(b), round(s, 3), body="#C98E66", cloth="#7A6A3A", kind="Robe", sw=3, up=UP_CALL))
    return "".join(o)

def ladder_light(p, w, h, seed):
    """Ye shall see the heaven opened, and the angels of God ascending and descending upon the Son of man: the night sky
    rent open in light, a stair of light coming down to the earth, small figures of white light going up and coming down
    upon it; below, the Son of man a small figure on the dark hill (God never drawn: the light only)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), sky(w, h, "#05051A", "#2A2050"), mk.stars(60, w, h * 0.6, seed),
         f'<path d="M{f(w * 0.3)} -10 C {f(w * 0.4)} {f(h * 0.1)} {f(w * 0.6)} {f(h * 0.1)} {f(w * 0.7)} -10 Z" fill="#FFF4C2"></path>',
         glow(w * 0.5, 0, h * 0.5, "#FFFFFF", 0.9, f"{p}g"),
         f'<path d="M{f(w * 0.44)} -10 L {f(w * 0.56)} -10 L {f(w * 0.53)} {f(b - h * 0.1)} L {f(w * 0.47)} {f(b - h * 0.1)} Z" fill="#FFF4C2" opacity="0.5"></path>',
         f'<path d="M-10 {f(b - h * 0.06)} C {f(w * 0.3)} {f(b - h * 0.16)} {f(w * 0.7)} {f(b - h * 0.16)} {f(w + 10)} {f(b - h * 0.06)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#14142E" stroke="{INK}" stroke-width="2"></path>']
    n = 6
    for i in range(n):
        t = (i + 0.5) / n; y = h * 0.06 + (b - h * 0.2) * t
        x = w * (0.5 + (0.05 if i % 2 else -0.05)); s = max(0.12, h / 1400) * (0.6 + 0.5 * t)
        o.append(angel(p, x, y + 200 * s, s, flip=i % 2 == 1))
    sj = max(0.14, h / 1300)
    o.append(jesus(p, w * 0.5, b - h * 0.08, sj))
    return "".join(o)

# ---- John 2: Cana, the temple ---------------------------------------------------------------------------------------
def cana(p, w, h, seed, stage="feast"):
    """The marriage in Cana of Galilee. feast: the courtyard hung with garlands and lamps, the guests seated, the mother of
    Jesus come to him; pots: the six waterpots of stone by the wall, the servants filling them to the brim with pitchers,
    Jesus standing by; wine: the ruler of the feast with the cup lifted, tasting, the pots full of red wine, the bridegroom
    in his garland called to him."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), courtyard(w, h, b, seed)]
    s = fit(b, max(h * 0.24, b - 240))
    if stage == "feast":
        o.append(f'<rect x="{f(w * 0.3)}" y="{f(b - 40 * s)}" width="{f(w * 0.66)}" height="{f(14 * s)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>')
        for i in range(5):
            x = w * (0.36 + 0.13 * i); o.append(cup(x, b - 40 * s, s * 0.14, color="#B5652E"))
        r = random.Random(seed)
        for i, x in enumerate((0.34, 0.48, 0.62, 0.76, 0.9)):
            o.append(seated(w * x, b, s * 0.8, r.choice(HEB), head=r.choice(["#E8E2D6", None, "#C8B898"]), beard=r.choice(["#2A1A10", "#6A645E", ""]), flip=x > 0.6))
        o.append(woman_fig(p, w * 0.2, b, s * 0.94, MARY_C, "#3A6AA8", up=UP_BLESS) + jesus(p, w * 0.08, b, s))
    elif stage == "pots":
        for i in range(6):
            o.append(stone_pot(w * (0.3 + 0.1 * i), b, s * 0.7, fill="#5AA8C8" if i < 4 else None))
        o.append(jesus(p, w * 0.1, b, s, flip=True, up=UP_BLESS))
        jar_ = '<path d="M-48 -122 C -56 -112 -54 -98 -46 -96 L -34 -96 C -26 -98 -24 -112 -32 -122 Z" fill="#B5652E" stroke="#0D0D0F" stroke-width="1.6"></path>'
        o.append(mk.person(p, round(w * 0.86), round(b), round(s * 0.92, 3), body="#B98A6E", cloth="#8A7A5A", kind="Tunic", sw=3, flip=False,
                           up=[(-22, -158), (-40, -140), (-50, -128)], extra=jar_))
        o.append(f'<path d="M{f(w * 0.86 - 48 * s * 0.92)} {f(b - 100 * s * 0.92)} C {f(w * 0.83 - 52 * s)} {f(b - 90 * s)} {f(w * 0.8 - 30 * s)} {f(b - 80 * s)} {f(w * 0.8)} {f(b - 72 * s)}" stroke="#5AA8C8" stroke-width="{f(5 * s)}" fill="none"></path>')
        o.append(mk.person(p, round(w * 0.2), round(b), round(s * 0.92, 3), body="#B98A6E", cloth="#6A5A3A", kind="Tunic", sw=3, flip=True,
                           up=[(-22, -158), (-40, -140), (-50, -128)], extra=jar_))
    elif stage == "wine":
        for i in range(6):
            o.append(stone_pot(w * (0.06 + 0.07 * i), b, s * 0.5, fill="#7A1A2A"))
        o.append(f'<g transform="translate({f(w * 0.58)} {f(b)})">' + mk.person(p, 0, 0, round(s, 3), body="#D9A27A", cloth="#E8D8B0", kind="Robe", sw=3, flip=False,
                 up=[(-22, -158), (-36, -176), (-40, -196)], extra=A.headcloth("#E8D8B0", cord="#3A2214") + GREY_BEARD) + '</g>')
        o.append(cup(w * 0.58 - 40 * s, b - 196 * s, s * 0.2, color="#E8B830"))
        garland = '<path d="M-14 -192 C -6 -200 6 -200 14 -192" stroke="#3A7A2A" stroke-width="5" fill="none"></path>'
        o.append(mk.person(p, round(w * 0.8), round(b), round(s * 0.98, 3), body="#C98E66", cloth="#F3EFE6", kind="Robe", sw=3, flip=True, extra=garland + A.BLACK_BEARD))
        o.append(mk.person(p, round(w * 0.4), round(b), round(s * 0.9, 3), body="#B98A6E", cloth="#8A7A5A", kind="Tunic", sw=3))
    return "".join(o)

def table_over(x, b, s, flip=False):
    """A changer's table overthrown: the board on its edge, the legs sticking out sideways."""
    d = -1 if flip else 1
    return (f'<rect x="{f(x - 7 * s)}" y="{f(b - 64 * s)}" width="{f(14 * s)}" height="{f(64 * s)}" fill="#7A4A2A" stroke="{INK}" stroke-width="2" transform="rotate({8 * d} {f(x)} {f(b)})"></rect>'
            + "".join(f'<path d="M{f(x + d * 6 * s)} {f(b - k * s)} l {f(d * 34 * s)} {f(-4 * s)}" stroke="#5A3A1E" stroke-width="{f(6 * s)}" stroke-linecap="round"></path>' for k in (14, 50)))

def table_set(x, b, s):
    """A changer's table standing, the coins stacked on it."""
    return (f'<rect x="{f(x - 46 * s)}" y="{f(b - 44 * s)}" width="{f(92 * s)}" height="{f(10 * s)}" fill="#7A4A2A" stroke="{INK}" stroke-width="2"></rect>'
            + "".join(f'<path d="M{f(x + dx * s)} {f(b - 34 * s)} l 0 {f(34 * s)}" stroke="#5A3A1E" stroke-width="{f(5 * s)}"></path>' for dx in (-38, 38))
            + "".join(f'<rect x="{f(x + dx * s - 6 * s)}" y="{f(b - 44 * s - hh * s)}" width="{f(12 * s)}" height="{f(hh * s)}" fill="#E8B830" stroke="{INK}" stroke-width="1"></rect>' for dx, hh in ((-24, 10), (-6, 16), (14, 8), (30, 12))))

def cage(x, b, s, open_=False):
    """A dove-seller's wicker cage; open_=True its door hanging open."""
    o = (f'<rect x="{f(x)}" y="{f(b - 30 * s)}" width="{f(40 * s)}" height="{f(30 * s)}" fill="#C8A060" fill-opacity="0.25" stroke="#8A6A3A" stroke-width="{f(2.4 * s)}"></rect>'
         + "".join(f'<path d="M{f(x + k * 10 * s)} {f(b - 30 * s)} l 0 {f(30 * s)}" stroke="#8A6A3A" stroke-width="{f(1.6 * s)}"></path>' for k in range(1, 4)))
    if open_: o += f'<path d="M{f(x)} {f(b - 30 * s)} l {f(-12 * s)} {f(-20 * s)}" stroke="#8A6A3A" stroke-width="{f(2.4 * s)}"></path>'
    return o

def temple_market(p, w, h, seed, cleansed=False):
    """The court of the temple at the passover. Not cleansed: the changers of money sitting at their tables, the oxen and
    sheep in their pens, the dove-sellers with their cages. cleansed=True: he made a scourge of cords, and cast all out —
    Jesus with the scourge of cords lifted high (striking no one), the oxen and the sheep running out before him, the
    changers' tables overthrown and their money poured out on the pavement, the cages open and the doves flying free."""
    r = random.Random(seed); b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), temple(w * 0.5, h * 0.5, min(w * 0.5, h * 0.9)), pavement(w, h, h * 0.5)]
    s = fit(b, max(h * 0.26, b - 230))
    if not cleansed:
        o.append(table_set(w * 0.3, b, s) + table_set(w * 0.52, b - 6, s * 0.94))
        o.append(seated(w * 0.24, b, s * 0.8, "#6A4A3A", head="#8A7A6A", beard="#2A1A10") + seated(w * 0.58, b - 6, s * 0.76, "#3A4A6A", head="#C8B898", beard="#6A645E", flip=True))
        o.append(f'<path d="M{f(w * 0.68)} {f(b - 40 * s)} L {f(w * 0.98)} {f(b - 40 * s)}" stroke="#8A6A3A" stroke-width="{f(4 * s)}"></path>'
                 + "".join(f'<path d="M{f(w * (0.68 + 0.06 * k))} {f(b - 50 * s)} l 0 {f(50 * s)}" stroke="#8A6A3A" stroke-width="{f(4 * s)}"></path>' for k in range(6)))
        o.append(cow(w * 0.8, b - 14 * s, s * 0.6, color="#8A5A3A", patch="#E8E2D6") + E.sheep(w * 0.9, b + 4 * s, s * 0.5) + E.sheep(w * 0.72, b + 2 * s, s * 0.46, flip=True))
        o.append(cage(w * 0.06, b, s) + cage(w * 0.06 + 44 * s, b, s) + cage(w * 0.08 + 20 * s, b - 30 * s, s))
        for i in range(3): o.append(_dove(w * 0.06 + (10 + 44 * i) * s, b - 12 * s - (i == 2) * 30 * s, 0.3 * s))
        o.append(man(p, w * 0.42, b, s * 0.96, "#7A5A2A", flip=True))
        return "".join(o)
    o.append(table_over(w * 0.4, b, s) + table_over(w * 0.56, b - 4, s * 0.94, flip=True))
    for _ in range(26):
        o.append(f'<circle cx="{f(r.uniform(w * 0.32, w * 0.66))}" cy="{f(b - r.uniform(0, 14))}" r="{f(4 * s)}" fill="#E8B830" stroke="{INK}" stroke-width="0.8"></circle>')
    o.append(cow(w * 0.82, b - 30 * s, s * 0.66, color="#8A5A3A", patch="#E8E2D6") + cow(w * 0.94, b - 8 * s, s * 0.6, color="#6A4A30", patch="#C8B898"))
    o.append(E.sheep(w * 0.72, b - 4 * s, s * 0.52) + E.sheep(w * 0.68, b - 30 * s, s * 0.48) + E.sheep(w * 0.84, b + 6 * s, s * 0.5))
    o.append(cage(w * 0.26, b, s, open_=True) + cage(w * 0.26 + 44 * s, b, s, open_=True))
    for _ in range(7):
        o.append(_dove(r.uniform(w * 0.3, w * 0.9), r.uniform(h * 0.08, h * 0.4), r.uniform(0.32, 0.5) * max(0.6, h / 400), flip=r.random() < 0.5))
    hx, hy = w * 0.12 + 46 * s, b - 226 * s
    o.append(jesus(p, w * 0.12, b, s, flip=True, up=[(-22, -158), (-38, -190), (-46, -226)]))
    o.append("".join(f'<path d="M{f(hx)} {f(hy)} C {f(hx + 20 * s + k * 8 * s)} {f(hy - 30 * s)} {f(hx + 50 * s + k * 10 * s)} {f(hy - 10 * s + k * 12 * s)} {f(hx + 70 * s + k * 6 * s)} {f(hy + 20 * s + k * 14 * s)}" stroke="#6A4A2A" stroke-width="{f(3 * s)}" fill="none"></path>' for k in range(4)))
    return "".join(o)

def temple_building(p, w, h, seed, dusk=False):
    """Forty and six years was this temple in building: Herod's temple on its mount, the sanctuary white and gold, the
    scaffolding and a crane still on its eastern wall, the great dressed stones piled below (no one drawn)."""
    top, bot = ("#3A2A5A", "#FF9A5A") if dusk else ("#8FD0E2", "#FFF4C2")
    b = h * 0.92
    o = [sky(w, h, top, bot), hills(w, h, h * 0.62, seed, color="#8A7A6A" if not dusk else "#5A4A5A", amp=10, step=80),
         f'<path d="M{f(w * 0.1)} {f(h * 0.9)} L {f(w * 0.14)} {f(h * 0.64)} L {f(w * 0.86)} {f(h * 0.64)} L {f(w * 0.9)} {f(h * 0.9)} Z" fill="#C8B898" stroke="{INK}" stroke-width="2.4"></path>']
    for k in range(1, 6):
        y = h * 0.64 + h * 0.26 * k / 6
        o.append(f'<path d="M{f(w * 0.14 - 0.04 * w * k / 6)} {f(y)} L {f(w * 0.86 + 0.04 * w * k / 6)} {f(y)}" stroke="#A89878" stroke-width="1.4"></path>')
    o.append(temple(w * 0.5, h * 0.64, min(w * 0.5, h * 0.7), lit=dusk))
    sx = w * 0.72
    o.append("".join(f'<path d="M{f(sx + k * 18)} {f(h * 0.64)} L {f(sx + k * 18)} {f(h * 0.28)}" stroke="#6A4A2A" stroke-width="3"></path>' for k in range(4))
             + "".join(f'<path d="M{f(sx - 4)} {f(h * (0.34 + 0.08 * k))} L {f(sx + 58)} {f(h * (0.34 + 0.08 * k))}" stroke="#6A4A2A" stroke-width="3"></path>' for k in range(4))
             + f'<path d="M{f(w * 0.88)} {f(h * 0.9)} L {f(w * 0.86)} {f(h * 0.2)} L {f(w * 0.66)} {f(h * 0.26)}" stroke="#5A3A1E" stroke-width="5" fill="none"></path>'
             f'<path d="M{f(w * 0.7)} {f(h * 0.25)} L {f(w * 0.7)} {f(h * 0.4)}" stroke="#3A2A1A" stroke-width="1.6"></path>'
             f'<rect x="{f(w * 0.68)}" y="{f(h * 0.4)}" width="{f(w * 0.04)}" height="{f(h * 0.04)}" fill="#D8C8A8" stroke="{INK}" stroke-width="1.6"></rect>')
    r = random.Random(seed)
    for _ in range(7):
        x = r.uniform(w * 0.02, w * 0.3); y = b + r.uniform(-h * 0.03, h * 0.04)
        o.append(f'<rect x="{f(x)}" y="{f(y - 18)}" width="{f(r.uniform(30, 50))}" height="18" fill="#D8C8A8" stroke="{INK}" stroke-width="1.4"></rect>')
    o.append(ground(w, h, h * 0.9, "#B8A07A" if not dusk else "#6A5A4A", dy=0))
    return "".join(o)

def passover_city(p, w, h, seed):
    """Many believed on his name, beholding his signs: Jerusalem at the passover, its streets full of pilgrims, the lambs
    led up, the temple above; Jesus among them, apart."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#FFF4C2"), walls(-w * 0.02, w * 1.02, h * 0.56, h * 0.36, seed, towers=4), temple(w * 0.64, h * 0.3, w * 0.24),
         ground(w, h, h * 0.62, "#C8B07A", dy=0)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(crowd(p, w * 0.36, w * 0.98, b - 50 * s, b - 50 * s - 120 * s, 9, seed + 1))
    o.append(E3.lamb(w * 0.4, b, s * 0.5) + E3.lamb(w * 0.54, b + 4, s * 0.46, flip=True))
    o.append(jesus(p, w * 0.12, b, s))
    return "".join(o)
