"""Isaiah 60–62 drawings (on top of isa.art16): Zion shining while darkness covers the earth, the camels of Midian and Ephah
with gold and frankincense, the ships of Tarshish flying as doves to their windows, the gates open day and night, the glory of
Lebanon brought to the sanctuary, brass for gold (a plate), the city with no sun and no moon but everlasting light, the
anointed one's tokens (a scroll, a horn of oil, the opened prison) — never drawn himself, the garland for ashes, the bride's
garments and jewels, the crown of beauty, the watchmen on the walls, the grain garnered in the courts, and the highway cast up."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from isa.art16 import *
from isa.art import f, K2, K3, bg, rect, smoke, thorns, tower
from genesis.art2 import birds
from exo.art8 import bp, dim, tag, title_bar, box

def zion_shine(w, h, seed):
    """Arise, shine; for thy light is come; darkness shall cover the earth, and gross darkness the peoples; but Jehovah will arise
    upon thee: the whole land in darkness, and Zion alone on its hill bathed in a great light from above."""
    o = [rect(w, h, "#05050F"), f'<path d="M{f(w * 0.36)} -10 L {f(w * 0.64)} -10 L {f(w * 0.86)} {f(h * 0.76)} L {f(w * 0.14)} {f(h * 0.76)} Z" fill="#FFF4C2" opacity="0.25"></path>',
         V.rays(w * 0.5, h * 0.5, 40, 20, max(w, h) * 0.6, color="#FFE680", op=0.35), hills(w, h, h * 0.7, seed, color="#0D0D18", amp=12),
         J.city_hill(w * 0.5, h * 0.84, w * 0.3, h * 0.24, seed), K1.temple_front(w * 0.5, h * 0.62, min(w * 0.12, h * 0.26), seed),
         f'<rect x="-10" y="{f(h * 0.84)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#0D0D18"></rect>']
    return "".join(o)

def camels_gifts(p, w, h, seed):
    """The multitude of camels shall cover thee, the dromedaries of Midian and Ephah; all they from Sheba shall come; they shall
    bring gold and frankincense; the flocks of Kedar: a great train of laden camels and flocks coming up toward the city."""
    return K1.sheba_train(p, w, h, seed)

def doves_ships(w, h, seed):
    """Who are these that fly as a cloud, and as the doves to their windows? the ships of Tarshish first, to bring thy sons from
    far: white sails crowding in over the sea toward the coast, a cloud of doves above them flying toward the city."""
    r = random.Random(seed)
    o = [bg(w, h, "#8FC8E8", "#F8F0D8"), f'<rect x="-10" y="{f(h * 0.56)}" width="{f(w + 20)}" height="{f(h * 0.5)}" fill="#2C7DA8"></rect>',
         f'<path d="M{f(w * 0.74)} {f(h * 0.56)} L {f(w + 10)} {f(h * 0.4)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.86)} {f(h + 10)} Z" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></path>',
         J.city_hill(w * 0.94, h * 0.44, w * 0.08, h * 0.12, seed)]
    for i in range(7):
        o.append(K1.ship(w * (0.08 + i * 0.1) + r.uniform(-10, 10), h * (0.66 + (i % 3) * 0.1), min(0.5, h / 520) * (0.7 + (i % 3) * 0.2)))
    for _ in range(26):
        x = r.uniform(w * 0.1, w * 0.8); y = r.uniform(h * 0.06, h * 0.4)
        o.append(f'<path d="M{f(x - 8)} {f(y)} q 4 -6 8 0 q 4 -6 8 0" stroke="#F3EFE6" stroke-width="2.4" fill="none"></path>')
    return "".join(o)

def open_gates(p, w, h, seed):
    """Thy gates also shall be open continually; they shall not be shut day nor night; that men may bring unto thee the wealth of
    the nations; foreigners shall build up thy walls: the gate standing wide in the evening light, lamps lit in the towers, a
    stream of people and laden asses going in, masons on the wall."""
    b = h * 0.94
    o = [mk.defs(p, *ALL), bg(w, h, "#5A4A8A", "#FFC890")]
    o.append(S4.gatehouse(w * 0.5, h * 0.82, min(w * 0.7, h * 1.4), h * 0.66, lit=True))
    o.append(ground(w, h, h * 0.82, "#C8A878", dy=0))
    s = fit(b, max(h * 0.5, b - 140))
    r = random.Random(seed)
    for i in range(6):
        x = w * (0.1 + i * 0.14)
        if i % 3 == 2: o.append(N.ass(x, b, min(0.4, h / 700), flip=True))
        else: o.append((man if i % 2 else woman)(p, x, b - (i % 2) * 4, s, r.choice(["#7A2A6A", "#E8B830", "#1F5FAD", "#B5121B", "#2E8A5A"]), flip=True))
    return "".join(o)

def lebanon_sanctuary(w, h, seed):
    """The glory of Lebanon shall come unto thee, the fir-tree, the pine, and the box-tree together, to beautify the place of my
    sanctuary: great timbers of fir and pine carried on carts toward the house on the mount."""
    o = [bg(w, h, "#8FC8E8", "#FFF0C8"), ground(w, h, h * 0.62, "#C8B888", dy=0), K1.temple_front(w * 0.78, h * 0.62, min(w * 0.26, h * 0.6), seed)]
    k = min(0.6, h / 460)
    for i in range(2):
        x = w * (0.14 + i * 0.28); y = h * 0.92
        o.append(S1.cart(x, y, k) + f'<rect x="{f(x - 70 * k)}" y="{f(y - 70 * k)}" width="{f(150 * k)}" height="{f(14 * k)}" rx="{f(7 * k)}" fill="#B5793A" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 f'<rect x="{f(x - 60 * k)}" y="{f(y - 84 * k)}" width="{f(140 * k)}" height="{f(14 * k)}" rx="{f(7 * k)}" fill="#A86A2A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
        o.append(S1.cow(x + 130 * k, y, k * 0.8, color="#8A5A30"))
    return "".join(o)

def brass_gold(w, h):
    """For brass I will bring gold, and for iron I will bring silver, and for wood brass, and for stones iron (a plate of the
    exchanges); thy walls Salvation, and thy gates Praise."""
    o = [bp(w, h), title_bar(w, "FOR BRASS GOLD · FOR IRON SILVER · FOR WOOD BRASS · FOR STONES IRON")]
    s = min(1.8, h / 160); cw = w / 4; y = h * 0.52
    pairs = [(("BRASS", "#B87333"), ("GOLD", "#E8B830")), (("IRON", "#5A5A60"), ("SILVER", "#C8C8D0")), (("WOOD", "#8A5A2A"), ("BRASS", "#B87333")), (("STONES", "#8A8478"), ("IRON", "#5A5A60"))]
    for i, ((a, ca), (b_, cb)) in enumerate(pairs):
        cx = cw * (i + 0.5)
        o.append(f'<rect x="{f(cx - 50 * s)}" y="{f(y - 14 * s)}" width="{f(30 * s)}" height="{f(28 * s)}" fill="{ca}" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 + route([(cx - 14 * s, y), (cx + 14 * s, y)], color=GOLD)
                 + f'<rect x="{f(cx + 20 * s)}" y="{f(y - 14 * s)}" width="{f(30 * s)}" height="{f(28 * s)}" fill="{cb}" stroke="#0D0D0F" stroke-width="1.6"></rect>'
                 + label(cx - 35 * s, y + 34 * s, a, CYAN, 8) + label(cx + 35 * s, y + 34 * s, b_, GOLD, 8))
    o.append(label(w * 0.5, h * 0.9, "THY WALLS SALVATION · THY GATES PRAISE", GOLD, 10))
    return "".join(o)

def everlasting_light(w, h, seed):
    """The sun shall be no more thy light by day; neither for brightness shall the moon give light; but Jehovah will be unto thee
    an everlasting light: the city in a light that comes from no sun, the sky without sun or moon, the light shining from
    within the city itself (no one drawn)."""
    o = [bg(w, h, "#FFF4C2", "#FFE08A"), V.rays(w * 0.5, h * 0.66, 48, 20, max(w, h) * 1.2, color="#FFFFFF", op=0.45),
         J.city_hill(w * 0.5, h * 0.94, w * 0.46, h * 0.36, seed), K1.temple_front(w * 0.5, h * 0.62, min(w * 0.16, h * 0.34), seed),
         f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.6)}" r="{f(min(w, h) * 0.2)}" fill="#FFFFFF" opacity="0.4"></circle>']
    return "".join(o)

def anointed(w, h, seed):
    """The Spirit of the Lord Jehovah is upon me; because Jehovah hath anointed me to preach good tidings unto the meek; to
    proclaim liberty to the captives, and the opening of the prison: a horn of oil pouring, an unrolled scroll, and an open
    prison door with broken fetters (the anointed one is never drawn)."""
    o = [rect(w, h, "#2A1A2A"), V.rays(w * 0.5, -h * 0.1, 30, 10, max(w, h), color="#FFF4C2", op=0.2)]
    s = min(1.3, h / 240)
    o.append(S1.vial(w * 0.2, h * 0.42, 0.9 * s, rot=-40, pour=60) + S1.drops(w * 0.24, h * 0.62, 5, seed, spread=20 * s))
    o.append(f'<rect x="{f(w * 0.36)}" y="{f(h * 0.56)}" width="{f(w * 0.28)}" height="{f(h * 0.2)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<ellipse cx="{f(w * 0.36)}" cy="{f(h * 0.66)}" rx="{f(10 * s)}" ry="{f(h * 0.11)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             f'<ellipse cx="{f(w * 0.64)}" cy="{f(h * 0.66)}" rx="{f(10 * s)}" ry="{f(h * 0.11)}" fill="#C8A878" stroke="#0D0D0F" stroke-width="2"></ellipse>'
             + "".join(f'<path d="M{f(w * 0.39)} {f(h * (0.6 + k * 0.035))} L {f(w * 0.61)} {f(h * (0.6 + k * 0.035))}" stroke="#6A4A2A" stroke-width="2" stroke-dasharray="10 4"></path>' for k in range(4)))
    o.append(f'<path d="M{f(w * 0.72)} {f(h * 0.9)} L {f(w * 0.72)} {f(h * 0.36)} L {f(w * 0.92)} {f(h * 0.36)} L {f(w * 0.92)} {f(h * 0.9)} Z" fill="#FFE8B0" stroke="#0D0D0F" stroke-width="3"></path>'
             f'<path d="M{f(w * 0.92)} {f(h * 0.36)} L {f(w * 0.98)} {f(h * 0.4)} L {f(w * 0.98)} {f(h * 0.94)} L {f(w * 0.92)} {f(h * 0.9)} Z" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="2"></path>'
             + J2.fetters(w * 0.82, h * 0.96, 0.6 * s))
    return "".join(o)

def garland_ashes(w, h, seed):
    """To give unto them a garland for ashes, the oil of joy for mourning, the garment of praise for the spirit of heaviness; trees
    of righteousness, the planting of Jehovah: a heap of grey ashes and a torn sackcloth on the left; a green garland, a jar of
    oil and a bright robe on the right; oaks planted behind."""
    o = [f'<rect x="-10" y="-10" width="{f(w / 2 + 10)}" height="{f(h + 20)}" fill="#5A5A60"></rect>', f'<rect x="{f(w / 2)}" y="-10" width="{f(w / 2 + 10)}" height="{f(h + 20)}" fill="#FFE8B0"></rect>']
    s = min(1.2, h / 240); b = h * 0.86
    o.append(f'<path d="M{f(w * 0.08)} {f(b)} C {f(w * 0.12)} {f(b - 40 * s)} {f(w * 0.3)} {f(b - 40 * s)} {f(w * 0.36)} {f(b)} Z" fill="#8A8A8A" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.16)} {f(b - 50 * s)} L {f(w * 0.3)} {f(b - 54 * s)} L {f(w * 0.32)} {f(b - 90 * s)} L {f(w * 0.2)} {f(b - 96 * s)} Z" fill="#5A5040" stroke="#0D0D0F" stroke-width="1.6"></path>')
    gx = w * 0.62
    o.append(f'<ellipse cx="{f(gx)}" cy="{f(b - 20 * s)}" rx="{f(40 * s)}" ry="{f(12 * s)}" fill="none" stroke="#3E8A3A" stroke-width="{f(9 * s)}"></ellipse>'
             + "".join(f'<circle cx="{f(gx + math.cos(a) * 40 * s)}" cy="{f(b - 20 * s + math.sin(a) * 12 * s)}" r="{f(5 * s)}" fill="#E8406A"></circle>' for a in [k * math.pi / 4 for k in range(8)]))
    o.append(f'<path d="M{f(w * 0.76)} {f(b)} C {f(w * 0.74)} {f(b - 30 * s)} {f(w * 0.75)} {f(b - 50 * s)} {f(w * 0.77)} {f(b - 56 * s)} L {f(w * 0.8)} {f(b - 56 * s)} C {f(w * 0.82)} {f(b - 50 * s)} {f(w * 0.83)} {f(b - 30 * s)} {f(w * 0.81)} {f(b)} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path>'
             f'<path d="M{f(w * 0.86)} {f(b)} L {f(w * 0.88)} {f(b - 100 * s)} L {f(w * 0.96)} {f(b - 100 * s)} L {f(w * 0.98)} {f(b)} Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.6"></path>')
    for x in (0.58, 0.7, 0.9):
        o.append(f'<g opacity="0.6">{J.oak(w * x, h * 0.6, min(0.4, h / 600), seed=int(x * 100))}</g>')
    o.append(route([(w * 0.4, h * 0.5), (w * 0.56, h * 0.5)], color="#0D0D0F", sw=3))
    return "".join(o)

def strangers_flocks(p, w, h, seed):
    """Strangers shall stand and feed your flocks, and foreigners shall be your plowmen and your vine-dressers: shepherds in foreign
    dress with a flock, a plowman behind his oxen, vineyards on the slope."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8FC8E8", "#F3E8C8"), hills(w, h, h * 0.46, seed, color="#8AA05A", amp=8), vines(w * 0.5, w, h * 0.56, h * 0.44, seed, rows=2),
         ground(w, h, h * 0.66, "#B8A070", dy=0)]
    k = min(0.5, h / 560)
    for i in range(4):
        o.append(E.sheep(w * (0.1 + i * 0.07), b - (i % 2) * 6, k * 0.8))
    s = fit(b, max(h * 0.5, b - 150))
    o.append(man(p, w * 0.06, b, s, "#7A2A6A") + S1.cow(w * 0.56, b, k, color="#8A5A30") + man(p, w * 0.7, b, s, "#E8B830", up=[(-22, -158), (-40, -150), (-60, -146)]))
    return "".join(o)

def bride(w, h, seed):
    """He hath clothed me with the garments of salvation, he hath covered me with the robe of righteousness, as a bridegroom
    decketh himself with a garland, and as a bride adorneth herself with her jewels; as the earth bringeth forth its bud: a
    bridal robe, a bridegroom's garland and a bride's jewels laid out on a chest, flowers springing from the garden beyond."""
    r = random.Random(seed)
    o = [bg(w, h, "#FFE0C8", "#FFF8E8"), ground(w, h, h * 0.7, "#9CCB5E", dy=0)]
    s = min(1.2, h / 260); b = h * 0.9
    o.append(f'<rect x="{f(w * 0.2)}" y="{f(b - 60 * s)}" width="{f(w * 0.6)}" height="{f(60 * s)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>')
    o.append(f'<path d="M{f(w * 0.26)} {f(b - 60 * s)} L {f(w * 0.3)} {f(b - 160 * s)} L {f(w * 0.4)} {f(b - 160 * s)} L {f(w * 0.44)} {f(b - 60 * s)} Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></path>'
             f'<path d="M{f(w * 0.3)} {f(b - 150 * s)} L {f(w * 0.4)} {f(b - 150 * s)}" stroke="#E8B830" stroke-width="{f(4 * s)}"></path>')
    gx = w * 0.56
    o.append(f'<ellipse cx="{f(gx)}" cy="{f(b - 70 * s)}" rx="{f(30 * s)}" ry="{f(9 * s)}" fill="none" stroke="#3E8A3A" stroke-width="{f(7 * s)}"></ellipse>')
    for i in range(5):
        x = w * (0.66 + i * 0.025)
        o.append(f'<circle cx="{f(x)}" cy="{f(b - 70 * s - (i % 2) * 6)}" r="{f(5 * s)}" fill="{["#B5121B", "#1F5FAD", "#E8B830", "#2E8A5A", "#F3EFE6"][i]}" stroke="#0D0D0F" stroke-width="1.2"></circle>')
    for _ in range(30):
        x = r.uniform(0, w); y = r.uniform(h * 0.72, h)
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r.uniform(2, 4))}" fill="{r.choice(["#E8406A", "#FFD23F", "#F3EFE6"])}"></circle>')
    return "".join(o)

def crown_beauty(w, h, seed):
    """Thou shalt also be a crown of beauty in the hand of Jehovah, and a royal diadem in the hand of thy God; Hephzi-bah, Beulah:
    a crown of gold set with jewels, shining over the city (no hand drawn)."""
    o = [rect(w, h, "#1A1438"), V.rays(w * 0.5, h * 0.4, 40, 20, max(w, h), color="#FFD23F", op=0.25), J.city_hill(w * 0.5, h * 1.02, w * 0.5, h * 0.24, seed)]
    s = min(2.4, h / 120)
    o.append(S2.crown(w * 0.5, h * 0.46, 0.7 * s))
    o.append(label(w * 0.2, h * 0.3, "HEPHZI-BAH", GOLD, 12) + label(w * 0.8, h * 0.3, "BEULAH", GOLD, 12))
    return "".join(o)

def wall_watchmen(p, w, h, seed):
    """I have set watchmen upon thy walls, O Jerusalem; they shall never hold their peace day nor night: watchmen spaced along the
    walls under the stars, each with a lamp, crying out."""
    o = [mk.defs(p, *ALL), bg(w, h, "#05051A", "#2A2050"), mk.stars(50, w, h * 0.5, seed), f'<rect x="-10" y="{f(h * 0.56)}" width="{f(w + 20)}" height="{f(h * 0.5)}" fill="#6A5A58" stroke="#0D0D0F" stroke-width="2"></rect>']
    for i in range(14):
        o.append(f'<rect x="{f(i * w / 13 - 10)}" y="{f(h * 0.52)}" width="{f(w / 26)}" height="{f(h * 0.05)}" fill="#6A5A58" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    s = fit(h * 0.56, h * 0.3)
    for i in range(4):
        x = w * (0.12 + i * 0.25)
        o.append(man(p, x, h * 0.56, s, "#5A6A8A", up=[(-22, -158), (-30, -186), (-24, -214)] if i % 2 else None)
                 + f'<circle cx="{f(x + 20 * s)}" cy="{f(h * 0.56 - 100 * s)}" r="{f(10 * s)}" fill="#FFC14D" opacity="0.6"></circle>')
    return "".join(o)

def garnered(p, w, h, seed):
    """They that have garnered it shall eat it, and praise Jehovah; and they that have gathered it shall drink it in the courts of
    my sanctuary: sheaves and jars of new wine carried into the court of the house, the harvesters themselves eating there."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#FFC890", "#FFF0C8"), ground(w, h, h * 0.66, "#D8C8A0", dy=0), K1.temple_front(w * 0.76, h * 0.66, min(w * 0.3, h * 0.6), seed)]
    s = min(1.0, h / 300)
    o.append(R1.heap(w * 0.2, b, w * 0.2, h * 0.14) + R1.sheaf(w * 0.4, b, s * 0.8))
    fs = fit(b, max(h * 0.5, b - 150))
    o.append(R1.reaper(p, w * 0.08, b, fs, cloth="#8A6A4A") + man(p, w * 0.5, b, fs, "#5A6A3A", up=[(-22, -158), (-6, -176), (6, -190)]) + woman(p, w * 0.58, b, fs * 0.94, "#C2456A"))
    return "".join(o)

def cast_up(p, w, h, seed):
    """Go through, go through the gates; prepare ye the way of the people; cast up, cast up the highway; gather out the stones; lift
    up an ensign for the peoples: workers clearing stones from a raised road leading to the open city gate, an ensign raised."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), way_prepared(w, h, seed)]
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.5)} L {f(w * 0.5)} {f(h * 0.2)}" stroke="#3A2A1A" stroke-width="4"></path>'
             f'<path d="M{f(w * 0.5)} {f(h * 0.2)} C {f(w * 0.54)} {f(h * 0.18)} {f(w * 0.58)} {f(h * 0.24)} {f(w * 0.62)} {f(h * 0.22)} L {f(w * 0.62)} {f(h * 0.3)} C {f(w * 0.58)} {f(h * 0.32)} {f(w * 0.54)} {f(h * 0.26)} {f(w * 0.5)} {f(h * 0.28)} Z" fill="#D7261E" stroke="#0D0D0F" stroke-width="2"></path>')
    s = fit(b, max(h * 0.5, b - 150))
    o.append(man(p, w * 0.12, b, s, "#6A5A3A", up=[(-22, -158), (-10, -130), (8, -110)]) + man(p, w * 0.86, b, s, "#4A5A6A", flip=True, up=[(-22, -158), (-10, -130), (8, -110)]))
    for i in range(5):
        o.append(f'<ellipse cx="{f(w * (0.04 + i * 0.03))}" cy="{f(b - 4)}" rx="10" ry="6" fill="#8A7A6A" stroke="#0D0D0F" stroke-width="1.2"></ellipse>')
    return "".join(o)
