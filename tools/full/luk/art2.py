"""Drawings for Luke 3–4: the generations from Jesus back to Adam, the son of God, as one chart on the blueprint grid; the
synagogue at Nazareth, the book of Isaiah unrolled at the reading-desk; the widow of Zarephath and the famine (the words of
4:25–27); the brow of the hill whereon their city was built — the crowd and the cliff edge from below, no one falling — and
Jesus passing through the midst of them. Built on luk.art."""
from luk.art import *
from luk.art import f, INK, HEB, TWELVE, jesus_seated, disciple_seated, road_scene, LIE, on_bed, lying, bedroll, silhouette, jesus_risen, roman_fig, torch, \
    jesus_kneel, light_seated, WOMEN3, PURPLE, GOLD, kneel_w, boy_fig, zach_fig, elis_fig, shepherd_fig, swaddled
import random, math

# ---- Luke 3 -------------------------------------------------------------------------------------------------------------
LINE = [("JESUS", "JOSEPH", "HELI", "MATTHAT", "LEVI", "MELCHI", "JANNAI", "JOSEPH", "MATTATHIAS", "AMOS", "NAHUM", "ESLI", "NAGGAI", "MAATH",
         "MATTATHIAS", "SEMEIN", "JOSECH", "JODA", "JOANAN", "RHESA", "ZERUBBABEL"),
        ("SHEALTIEL", "NERI", "MELCHI", "ADDI", "COSAM", "ELMADAM", "ER", "JESUS", "ELIEZER", "JORIM", "MATTHAT", "LEVI", "SYMEON", "JUDAS", "JOSEPH",
         "JONAM", "ELIAKIM", "MELEA", "MENNA", "MATTATHA", "NATHAN"),
        ("DAVID", "JESSE", "OBED", "BOAZ", "SALMON", "NAHSHON", "AMMINADAB", "ARNI", "HEZRON", "PEREZ", "JUDAH", "JACOB", "ISAAC", "ABRAHAM"),
        ("TERAH", "NAHOR", "SERUG", "REU", "PELEG", "EBER", "SHELAH", "CAINAN", "ARPHAXAD", "SHEM", "NOAH", "LAMECH", "METHUSELAH", "ENOCH", "JARED",
         "MAHALALEEL", "CAINAN", "ENOS", "SETH", "ADAM", "GOD")]
BANDS = [("#F3EFE6", "FROM JESUS BACK TO ZERUBBABEL"), ("#8FD0E2", "FROM SHEALTIEL BACK TO NATHAN"), ("#FFD23F", "FROM DAVID BACK TO ABRAHAM"),
         ("#E8A0C8", "FROM TERAH BACK TO ADAM, THE SON OF GOD")]

def lineage(w, h, top=0.06, bot=0.9):
    """The son (as was supposed) of Joseph … the son of Adam, the son of God: every name of Luke 3:23–38 on one line,
    snaking seven to a row from JESUS at the top left down to GOD at the end — the generations in four colours (to
    Zerubbabel white, to Nathan cyan, David to Abraham gold, Terah to Adam rose), JESUS lit with a glow, GOD as light only
    (no figure)."""
    names = [(nm, c, t) for (c, t), band in zip(BANDS, LINE) for nm in band]
    cols = 7; rows_ = (len(names) + cols - 1) // cols
    o = [grid_bg(w, h)]
    y0, y1 = h * top, h * bot
    rh = (y1 - y0) / rows_
    pts = []
    for i, (nm, c, t) in enumerate(names):
        r_, k = divmod(i, cols)
        if r_ % 2: k = cols - 1 - k
        x = w * (0.07 + 0.86 * k / (cols - 1)); y = y0 + rh * (r_ + 0.62)
        pts.append((x, y, nm, c))
    for a, b in zip(pts, pts[1:]):
        o.append(route([(a[0], a[1]), (b[0], b[1])], color="#4A7A9A", sw=1.6, dash="4 4", arrow=False))
    seen = set()
    for (x, y, nm, c), (_, _, _, tag) in zip(pts, [(0, 0, 0, t) for (_, _, t) in names]):
        if tag not in seen:
            seen.add(tag); o.append(label(x - 30 if x > w * 0.5 else x + 30, y - rh * 0.56, tag, c, 8, anchor="end" if x > w * 0.5 else "start"))
    for x, y, nm, c in pts:
        if nm == "GOD":
            o.append(glow(x, y, 40, "#FFF4C2", 0.9, "lngod") + f'<circle cx="{f(x)}" cy="{f(y)}" r="7" fill="#FFFDF0" stroke="#FFD23F" stroke-width="2"></circle>' + label(x, y - 12, nm, "#FFF4C2", 11))
        elif (x, y) == pts[0][:2]:
            o.append(glow(x, y, 40, "#FFE680", 0.9, "lnjs") + node(x, y, nm, "#FFD23F", r=6, dy=-12, size=11))
        else:
            o.append(node(x, y, nm, c, r=3.5, dy=-9, size=8.5))
    return "".join(o)

# ---- Luke 4 -------------------------------------------------------------------------------------------------------------
def reading(p, w, h, seed, seated_=False):
    """He stood up to read, and there was delivered unto him the book of the prophet Isaiah: the synagogue of Nazareth on the
    sabbath, Jesus standing at the reading-desk with the scroll unrolled in his hands, the people seated along the walls,
    the attendant beside; seated_=True: the scroll given back, Jesus sitting down, every face turned to him."""
    b = h * 0.94
    o = [synagogue(p, w, h, seed, teaching=False, crowd_n=9)]
    s = fit(b, max(h * 0.2, b - 230))
    o.append(f'<rect x="{f(w * 0.5 - 30 * s)}" y="{f(b - 80 * s)}" width="{f(60 * s)}" height="{f(80 * s)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.5 - 40 * s)} {f(b - 80 * s)} L {f(w * 0.5 + 40 * s)} {f(b - 90 * s)}" stroke="#4A2A1A" stroke-width="{f(6 * s)}"></path>')
    if seated_:
        o.append(jesus_seated(w * 0.42, b, s * 0.86))
        o.append(man(p, w * 0.6, b, s * 0.94, "#5A4A3A", flip=False, up=[(-22, -158), (-36, -150), (-44, -140)])
                 + f'<rect x="{f(w * 0.6 - 48 * s * 0.94)}" y="{f(b - 150 * s * 0.94)}" width="{f(16 * s)}" height="{f(30 * s)}" rx="4" fill="#E8D8B0" stroke="{INK}" stroke-width="1.6"></rect>')
    else:
        o.append(glow(w * 0.42, b - 130 * s, 120 * s, "#FFF4C2", 0.6, f"{p}g"))
        o.append(jesus(p, w * 0.42, b, s, flip=True, up=[(-22, -158), (-44, -140), (-60, -134)]))
        o.append(scroll(w * 0.42 + 66 * s, b - 136 * s, 46 * s, 30 * s, lines=3))
        o.append(man(p, w * 0.62, b, s * 0.92, "#5A4A3A", flip=True))
    return "".join(o)

def zarephath(p, w, h, seed):
    """The heaven shut up three years and six months, a great famine: the gate of Zarephath under a hard white sky, the
    fields cracked and bare, a widow gathering sticks outside the gate."""
    b = h * 0.94
    r = random.Random(seed)
    o = [mk.defs(p, *ALL), sky(w, h, "#E8D8B0", "#F3E8C8"), sun(w * 0.8, h * 0.2, max(16, h * 0.06), color="#FFF4C2", op=0.6),
         walls(w * 0.5, w * 1.04, h * 0.66, h * 0.36, seed, towers=2, color="#C8B090"), ground(w, h, h * 0.66, "#C8A878", dy=0)]
    for _ in range(14):                                     # cracks in the dry ground
        x, y = r.uniform(0, w), r.uniform(h * 0.72, h)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(10, 24))} {f(r.uniform(-4, 4))} l {f(r.uniform(6, 14))} {f(r.uniform(4, 10))}" stroke="#8A6A4A" stroke-width="1.6" fill="none"></path>')
    s = fit(b, max(h * 0.3, b - 210))
    sticks = '<path d="M-56 -112 L -30 -126 M-58 -118 L -28 -116 M-54 -108 L -26 -132" stroke="#6A4A2A" stroke-width="3"></path>'
    o.append(woman_fig(p, w * 0.3, b, s, "#4A4A52", "#2A2A32", up=[(-22, -158), (-34, -132), (-42, -116)], extra=sticks))
    o.append(fig_tree(w * 0.12, b, max(0.5, h / 420), bare=True, fruit=False, seed=seed))
    return "".join(o)

def naaman(p, w, h, seed):
    """None was cleansed, but only Naaman the Syrian: the Jordan between its banks, a Syrian captain in a red cloak coming up
    out of the water, his chariot and horses waiting on the bank."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.4, seed, color="#C8A06A", amp=16, step=80),
         f'<path d="M-10 {f(h * 0.56)} C {f(w * 0.3)} {f(h * 0.52)} {f(w * 0.6)} {f(h * 0.6)} {f(w + 10)} {f(h * 0.56)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2C7DA8" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.6)} {f(h + 10)} C {f(w * 0.66)} {f(h * 0.7)} {f(w * 0.8)} {f(h * 0.62)} {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} Z" fill="#9AAA5A" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, max(h * 0.3, b - 210))
    o.append(mk.person(p, round(w * 0.36), round(b + 30 * s), round(s, 3), body="#D9A27A", cloth="#8A1A2A", kind="Robe", sw=3, up=UP_HIGH,
                       extra=A.headcloth("#E8E2D6", cord="#E8B830") + A.BLACK_BEARD))
    o.append(f'<rect x="{f(w * 0.2)}" y="{f(b - 10 * s)}" width="{f(w * 0.3)}" height="{f(h)}" fill="#2C7DA8"></rect>'
             f'<path d="M{f(w * 0.24)} {f(b - 8 * s)} q 20 -6 40 0 t 40 0 t 40 0" stroke="#BFE6F2" stroke-width="3" fill="none"></path>')
    for i in range(2):                                    # his horses waiting on the far bank
        o.append(f'<g transform="translate({f(w * (0.78 + 0.1 * i))} {f(h * 0.74)}) scale({f(max(0.3, h / 900))})">'
                 '<path d="M-50 0 L -46 -40 C -40 -60 30 -62 40 -44 L 60 -70 L 72 -64 L 54 -36 L 50 0 L 40 0 L 38 -26 L -30 -26 L -36 0 Z" fill="#6A4A3A" stroke="#0D0D0F" stroke-width="2"></path></g>')
    return "".join(o)

def brow(p, w, h, seed):
    """They cast him forth out of the city, and led him unto the brow of the hill whereon their city was built: Nazareth's
    houses on the height, the hill falling away in a cliff at the right; the crowd pressing Jesus up the slope toward the
    edge — seen from below, no one falls."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#5A3A5A", "#E8803A"), hills(w, h, h * 0.66, seed, color="#4A3A4A", amp=10, step=80)]
    edge = w * 0.74
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.5)} C {f(w * 0.2)} {f(h * 0.44)} {f(w * 0.5)} {f(h * 0.4)} {f(edge)} {f(h * 0.36)} L {f(edge + w * 0.02)} {f(h * 0.42)} '
             f'L {f(edge - w * 0.01)} {f(h * 0.6)} L {f(edge + w * 0.03)} {f(h * 0.8)} L {f(edge)} {f(h + 10)} Z" fill="#8A6A4A" stroke="{INK}" stroke-width="2.6"></path>')
    o.append(houses(w, h, h * 0.48, seed, x0=-10, x1=w * 0.34, hmin=0.14, hmax=0.22, stairs=False))
    o.append(f'<path d="M{f(edge)} {f(h * 0.36)} L {f(edge + w * 0.02)} {f(h * 0.42)} L {f(edge - w * 0.01)} {f(h * 0.6)} L {f(edge + w * 0.03)} {f(h * 0.8)}" stroke="#4A3A2A" stroke-width="4" fill="none"></path>')
    base = lambda x: h * 0.5 - (h * 0.14) * (x / edge)           # the slope's top line, rising to the edge
    s = max(0.2, h / 1700)
    r = random.Random(seed)
    for i in range(12):
        x = w * (0.3 + 0.032 * i) + r.uniform(-4, 4)
        o.append(man(p, x, base(x) + 2, s * r.uniform(0.9, 1.05), r.choice(HEB + ["#3A2A2A", "#4A3A3A"]), flip=True, up=UP_BLESS if i % 3 == 0 else None))
    xj = w * 0.68
    o.append(jesus(p, xj, base(xj) + 2, s * 1.04, flip=True))
    return "".join(o)

def through_midst(p, w, h, seed):
    """But he passing through the midst of them went his way: on the hill road below Nazareth at evening, Jesus walking away
    alone down the road, the crowd standing parted on either side behind him, still."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), sky(w, h, "#3A2A5A", "#E8803A"), hill_town(w * 0.5, h * 0.5, w * 0.5, h * 0.24, seed, hill="#5A4A4A"),
         hills(w, h, h * 0.58, seed, color="#5A4A4A", amp=8, step=80), ground(w, h, h * 0.62, "#8A6A4A", dy=0),
         f'<path d="M{f(w * 0.44)} {f(h * 0.62)} L {f(w * 0.56)} {f(h * 0.62)} L {f(w * 0.8)} {f(h + 10)} L {f(w * 0.2)} {f(h + 10)} Z" fill="#B8946A" stroke="{INK}" stroke-width="1.6"></path>']
    s1 = fit(h * 0.72, h * 0.72 - 120)
    o.append(crowd(p, w * 0.14, w * 0.4, h * 0.72, h * 0.72 - 120 * 1.0, 5, seed, flip=False))
    o.append(crowd(p, w * 0.6, w * 0.88, h * 0.72, h * 0.72 - 120 * 1.0, 5, seed + 1, flip=True))
    s = fit(b, max(h * 0.3, b - 220))
    o.append(jesus(p, w * 0.5, b, s))
    return "".join(o)
