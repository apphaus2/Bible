"""Isaiah 49–51 drawings (on top of isa.art13). The servant of Jehovah is never drawn: his words stand over his tokens — the
sharp sword and the polished shaft hid in the quiver (a plate), the morning that wakeneth the ear, the face set like a
flint. Also: the prison door opened, Zion's walls before him, the nursing mother, kings and queens bearing the sons, the bill
of divorcement, the heavens clothed with blackness, the garment and the moth, the walkers by their own firebrands, the rock
whence ye were hewn, Abraham and Sarah under the stars, the wilderness made like Eden, the heavens vanishing like smoke, the
cup of staggering, and the antelope in a net."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from isa.art13 import *
from isa.art import f, K2, K3, bg, rect, smoke, thorns, tower
from genesis.art2 import birds
from exo.art8 import bp, dim, tag, title_bar, box

def sword_shaft(w, h):
    """He hath made my mouth like a sharp sword; in the shadow of his hand hath he hid me: and he hath made me a polished shaft;
    in his quiver hath he kept me close (a plate: the sword, and the shaft in the quiver)."""
    o = [bp(w, h), title_bar(w, "A SHARP SWORD · A POLISHED SHAFT IN THE QUIVER")]
    s = min(1.2, h / 300); y = h * 0.68
    x0 = w * 0.08
    o.append(f'<path d="M{f(x0)} {f(y)} L {f(x0 + 60 * s)} {f(y)}" stroke="#8A5A2A" stroke-width="{f(8 * s)}" stroke-linecap="round"></path>'
             f'<rect x="{f(x0 + 58 * s)}" y="{f(y - 16 * s)}" width="{f(8 * s)}" height="{f(32 * s)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></rect>'
             f'<path d="M{f(x0 + 66 * s)} {f(y - 6 * s)} L {f(x0 + 250 * s)} {f(y - 3 * s)} L {f(x0 + 270 * s)} {f(y)} L {f(x0 + 250 * s)} {f(y + 3 * s)} L {f(x0 + 66 * s)} {f(y + 6 * s)} Z" fill="#E8F0F8" stroke="#8FD0E2" stroke-width="1.6"></path>'
             + tag(x0 + 200 * s, y - 4 * s, "A SHARP SWORD", x0 + 220 * s, y - 50 * s))
    qx = w * 0.76
    o.append(f'<path d="M{f(qx - 26 * s)} {f(y - 70 * s)} L {f(qx + 26 * s)} {f(y - 80 * s)} L {f(qx + 34 * s)} {f(y + 70 * s)} L {f(qx - 14 * s)} {f(y + 80 * s)} Z" fill="#8A4A2A" stroke="#0D0D0F" stroke-width="2"></path>')
    for k in range(4):
        x = qx - 14 * s + k * 12 * s
        o.append(f'<path d="M{f(x)} {f(y - 70 * s)} L {f(x + 4 * s)} {f(y - 130 * s)}" stroke="#C8A060" stroke-width="{f(3 * s)}"></path><path d="M{f(x + 4 * s)} {f(y - 130 * s)} l {f(-6 * s)} {f(8 * s)} m {f(6 * s)} {f(-8 * s)} l {f(6 * s)} {f(8 * s)}" stroke="#D7261E" stroke-width="2"></path>')
    o.append(f'<path d="M{f(qx + 40 * s)} {f(y - 140 * s)} L {f(qx + 46 * s)} {f(y - 60 * s)}" stroke="#FFD23F" stroke-width="{f(4 * s)}"></path>' + tag(qx + 44 * s, y - 120 * s, "A POLISHED SHAFT", qx - 40 * s, y - 150 * s, color=GOLD))
    return "".join(o)

def prison_open(p, w, h, seed):
    """Saying to them that are bound, Go forth; to them that are in darkness, Show yourselves: a prison door standing open, light
    pouring in, the bound coming out into the morning, fetters on the floor."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), rect(w, h, "#2A2430"), f'<path d="M{f(w * 0.4)} {f(h * 0.06)} L {f(w * 0.74)} {f(h * 0.06)} L {f(w * 0.74)} {f(b)} L {f(w * 0.4)} {f(b)} Z" fill="#FFE8B0" stroke="#0D0D0F" stroke-width="3"></path>',
         f'<path d="M{f(w * 0.74)} {f(h * 0.06)} L {f(w * 0.9)} {f(h * 0.12)} L {f(w * 0.9)} {f(b + 6)} L {f(w * 0.74)} {f(b)} Z" fill="#5A4A3A" stroke="#0D0D0F" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.4)} {f(b)} L {f(w * 0.74)} {f(b)} L {f(w * 0.9)} {f(h + 10)} L {f(w * 0.2)} {f(h + 10)} Z" fill="#FFE8B0" opacity="0.4"></path>']
    s = fit(b, max(h * 0.4, b - 210))
    for i in range(3):
        o.append(man(p, w * (0.48 + i * 0.09), b - i * 4, s * (1 - i * 0.08), ["#6A5A4A", "#5A4A6A", "#4A5A4A"][i], up=[(-22, -158), (-30, -190), (-24, -222)] if i == 1 else None))
    o.append(J2.fetters(w * 0.24, b, min(1.0, h / 300)))
    return "".join(o)

def zion_walls(w, h, seed):
    """Behold, I have graven thee upon the palms of my hands; thy walls are continually before me; thy children make haste: the
    walls of Jerusalem drawn as a plan in gold, every course of them marked, children running up the road to the gate."""
    o = [grid_bg(w, h)]
    cx, cy = w * 0.5, h * 0.5; rx, ry = w * 0.32, h * 0.36
    pts = [(cx + rx * math.cos(a) * (1 + 0.08 * math.sin(3 * a)), cy + ry * math.sin(a) * (1 + 0.06 * math.cos(2 * a))) for a in [k * math.pi * 2 / 14 for k in range(14)]]
    o.append(f'<path d="M{" L ".join(f"{f(x)} {f(y)}" for x, y in pts)} Z" fill="none" stroke="#FFD23F" stroke-width="4"></path>'
             f'<path d="M{" L ".join(f"{f(cx + (x - cx) * 0.92)} {f(cy + (y - cy) * 0.92)}" for x, y in pts)} Z" fill="none" stroke="#FFD23F" stroke-width="1.2" stroke-dasharray="4 4"></path>')
    for x, y in pts[::2]:
        o.append(f'<rect x="{f(x - 7)}" y="{f(y - 7)}" width="14" height="14" fill="#0B1A2E" stroke="#FFD23F" stroke-width="2"></rect>')
    o.append(label(cx, cy + 4, "THY WALLS ARE CONTINUALLY BEFORE ME", GOLD, 10))
    return "".join(o)

def nursing(p, w, h, seed):
    """Can a woman forget her sucking child, that she should not have compassion on the son of her womb?: a mother sitting at
    her door at evening with her child held close."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#5A4A7A", "#F3C8A0"), ground(w, h, h * 0.8, "#A8886A", dy=0),
         f'<rect x="{f(w * 0.06)}" y="{f(h * 0.2)}" width="{f(w * 0.34)}" height="{f(h * 0.6)}" fill="#C8A88A" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<path d="M{f(w * 0.16)} {f(h * 0.8)} L {f(w * 0.16)} {f(h * 0.46)} Q {f(w * 0.22)} {f(h * 0.38)} {f(w * 0.28)} {f(h * 0.46)} L {f(w * 0.28)} {f(h * 0.8)} Z" fill="#FFC14D" opacity="0.7"></path>']
    s = fit(b, max(h * 0.35, b - 230))
    o.append(mk.person(p, round(w * 0.56), round(b), s, body="#3A1E14", cloth="#3A4A7A", woman=True, hair="#1A1210", sw=3, up=R1.HOLD_BABY, extra=R1.baby(10, -130, 0.8)))
    return "".join(o)

def kings_bear(p, w, h, seed):
    """They shall bring thy sons in their bosom, and thy daughters shall be carried upon their shoulders; kings shall be thy
    nursing fathers, and their queens thy nursing mothers: a procession of crowned figures from far countries coming up to
    Zion, bearing children."""
    r = random.Random(seed); b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#8FB0D8", "#FFE8B8"), J.city_hill(w * 0.86, h * 0.56, w * 0.14, h * 0.2, seed), ground(w, h, h * 0.6, "#C8B080", dy=0)]
    s = fit(b, max(h * 0.4, b - 200))
    cols = ["#7A2A6A", "#1F5FAD", "#B5121B", "#2E8A5A", "#E8B830"]
    for i in range(5):
        x = w * (0.08 + i * 0.14); sc = s * (1 - i * 0.08); y = b - i * h * 0.04
        crown = '<path d="M-14 -200 L -14 -214 L -7 -206 L 0 -218 L 7 -206 L 14 -214 L 14 -200 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.6"></path>'
        o.append(mk.person(p, round(x), round(y), round(sc, 3), body="#3A1E14", cloth=cols[i], woman=i % 2 == 1, hair="#1A1210" if i % 2 else False, sw=3,
                           up=R1.HOLD_BABY, extra=R1.baby(10, -130, 0.8) + crown))
    return "".join(o)

def divorcement(w, h, seed):
    """Where is the bill of your mother's divorcement, wherewith I have put her away?: an unrolled scroll with a seal, lying on
    a table, the writing struck through; no hand near it."""
    return EZ_letter(w, h, seed)

def EZ_letter(w, h, seed):
    from ezr.art import letter_scroll
    o = [letter_scroll(w, h, seed, seal="#B5121B", text_lines=6)]
    o.append(f'<path d="M{f(w * 0.24)} {f(h * 0.24)} L {f(w * 0.76)} {f(h * 0.74)}" stroke="#D7261E" stroke-width="3" opacity="0.7"></path>')
    return "".join(o)

def black_heavens(w, h, seed):
    """I dry up the sea, I make the rivers a wilderness: their fish stink; I clothe the heavens with blackness, and I make
    sackcloth their covering: a black sky over a dried river-bed, dead fish on the cracked mud."""
    r = random.Random(seed)
    o = [rect(w, h, "#0A0A0E"), f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h * 0.5)}" fill="#1A1814"></rect>']
    for k in range(10):
        o.append(f'<path d="M{f(-10)} {f(h * k * 0.05)} L {f(w + 10)} {f(h * k * 0.05 + 4)}" stroke="#2A2620" stroke-width="2"></path>')
    o.append(ground(w, h, h * 0.6, "#6A5A4A", dy=0))
    for _ in range(18):
        x = r.uniform(0, w); y = r.uniform(h * 0.64, h * 0.96)
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(10, 24))} {f(r.uniform(-4, 4))}" stroke="#3A2A1A" stroke-width="1.4"></path>')
    for i in range(5):
        o.append(E2.fish(w * (0.15 + i * 0.17), h * (0.8 + (i % 2) * 0.06), min(0.6, h / 400), rot=r.choice([170, 190, 10])))
    return "".join(o)

def morning_ear(w, h, seed):
    """The Lord Jehovah hath given me the tongue of them that are taught; he wakeneth morning by morning, he wakeneth mine ear to
    hear: the first light of morning breaking over the hills, a window open to it, a scroll on the sill."""
    o = [rect(w, h, "#3A2A3A"), f'<rect x="{f(w * 0.2)}" y="{f(h * 0.1)}" width="{f(w * 0.6)}" height="{f(h * 0.7)}" fill="#FFD8A0" stroke="#0D0D0F" stroke-width="4"></rect>',
         f'<g transform="translate({f(w * 0.2)} {f(h * 0.1)})">{bg(w * 0.6, h * 0.7, "#5A6ABA", "#FFD8A0")}{sun(w * 0.3, h * 0.5, min(24, h * 0.06), color="#FFF4C2", op=0.5)}{hills(w * 0.6, h * 0.7, h * 0.52, seed, color="#5A4A6A", amp=10)}</g>',
         f'<rect x="{f(w * 0.16)}" y="{f(h * 0.8)}" width="{f(w * 0.68)}" height="{f(h * 0.06)}" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></rect>',
         f'<rect x="{f(w * 0.4)}" y="{f(h * 0.76)}" width="{f(w * 0.2)}" height="{f(h * 0.04)}" rx="{f(h * 0.02)}" fill="#E8D8B0" stroke="#0D0D0F" stroke-width="1.6"></rect>']
    return "".join(o)

def flint_face(w, h, seed):
    """I gave my back to the smiters, and my cheeks to them that plucked off the hair; I hid not my face from shame and spitting;
    therefore have I set my face like a flint: no one drawn — a hard flint stone standing in a dark place, lit from one side."""
    o = [rect(w, h, "#14121A"), V.rays(w * 0.2, h * 0.3, 24, 10, max(w, h), color="#C8C8E8", op=0.12)]
    s = min(1.4, h / 220); cx, cy = w * 0.56, h * 0.62
    o.append(f'<path d="M{f(cx - 80 * s)} {f(cy + 60 * s)} L {f(cx - 70 * s)} {f(cy - 20 * s)} L {f(cx - 30 * s)} {f(cy - 70 * s)} L {f(cx + 40 * s)} {f(cy - 60 * s)} L {f(cx + 80 * s)} {f(cy - 10 * s)} L {f(cx + 70 * s)} {f(cy + 60 * s)} Z" fill="#4A4A5A" stroke="#0D0D0F" stroke-width="2.6"></path>'
             f'<path d="M{f(cx - 70 * s)} {f(cy - 20 * s)} L {f(cx - 30 * s)} {f(cy - 70 * s)} L {f(cx - 10 * s)} {f(cy - 10 * s)} L {f(cx - 40 * s)} {f(cy + 60 * s)} L {f(cx - 80 * s)} {f(cy + 60 * s)} Z" fill="#8A8AA0"></path>'
             f'<path d="M{f(cx - 10 * s)} {f(cy - 10 * s)} L {f(cx + 40 * s)} {f(cy - 60 * s)} M{f(cx - 10 * s)} {f(cy - 10 * s)} L {f(cx + 30 * s)} {f(cy + 60 * s)}" stroke="#2A2A36" stroke-width="2"></path>')
    o.append(ground(w, h, cy + 60 * s, "#1A1820", dy=0))
    return "".join(o)

def moth_garment(w, h, seed):
    """They all shall wax old as a garment; the moth shall eat them up: an old robe hung on a peg, holes eaten through it, moths
    about it."""
    r = random.Random(seed)
    o = [rect(w, h, "#5A4A3A"), f'<rect x="-10" y="{f(h * 0.1)}" width="{f(w + 20)}" height="{f(h * 0.8)}" fill="#8A7A6A"></rect>']
    s = min(1.3, h / 240); cx = w * 0.5
    o.append(f'<circle cx="{f(cx)}" cy="{f(h * 0.14)}" r="{f(6 * s)}" fill="#5A3A22"></circle>'
             f'<path d="M{f(cx - 30 * s)} {f(h * 0.16)} L {f(cx + 30 * s)} {f(h * 0.16)} L {f(cx + 70 * s)} {f(h * 0.9)} L {f(cx - 70 * s)} {f(h * 0.9)} Z" fill="#5A6A8A" stroke="#0D0D0F" stroke-width="2"></path>')
    for _ in range(10):
        x = cx + r.uniform(-40, 40) * s; y = r.uniform(h * 0.3, h * 0.85)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(r.uniform(3, 8) * s)}" ry="{f(r.uniform(2, 5) * s)}" fill="#8A7A6A"></ellipse>')
    for _ in range(5):
        x = r.uniform(w * 0.2, w * 0.8); y = r.uniform(h * 0.2, h * 0.7)
        o.append(f'<path d="M{f(x)} {f(y)} l -8 -6 l 0 10 Z M{f(x)} {f(y)} l 8 -6 l 0 10 Z" fill="#C8B8A0" stroke="#0D0D0F" stroke-width="1"></path>')
    return "".join(o)

def firebrand_walkers(p, w, h, seed):
    """All ye that kindle a fire, that gird yourselves about with firebrands; walk ye in the flame of your fire: figures in the
    dark each carrying a burning brand, walking apart among small fires they have kindled."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), rect(w, h, "#0A0810"), ground(w, h, h * 0.8, "#1A1418", dy=0)]
    s = fit(b, max(h * 0.5, b - 170))
    for i, x in enumerate((0.16, 0.42, 0.7)):
        o.append(E.blaze(w * (x + 0.1), b, w * 0.05, h * 0.12, seed + i, n=4))
        o.append(J1.torchbearer(p, w * x, b - (i % 2) * 6, s, body="#1A1010", cloth="#3A2A2A", seed=seed + i))
    return "".join(o)

def quarry(w, h, seed):
    """Look unto the rock whence ye were hewn, and to the hole of the pit whence ye were digged: a quarry face with a great
    block cut out of it, the cut block lying below, the dark pit beside."""
    o = [bg(w, h, "#8FB0D8", "#F3E8C8"), f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.2)} L {f(w * 0.7)} {f(h * 0.14)} L {f(w + 10)} {f(h * 0.3)} L {f(w + 10)} {f(h + 10)} Z" fill="#C8B898" stroke="#0D0D0F" stroke-width="2.4"></path>']
    o.append(f'<rect x="{f(w * 0.3)}" y="{f(h * 0.3)}" width="{f(w * 0.24)}" height="{f(h * 0.3)}" fill="#8A7A5A" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.3)} {f(h * 0.3)} L {f(w * 0.34)} {f(h * 0.34)} L {f(w * 0.34)} {f(h * 0.6)} M{f(w * 0.34)} {f(h * 0.34)} L {f(w * 0.54)} {f(h * 0.34)}" stroke="#6A5A3A" stroke-width="2"></path>')
    o.append(box(w * 0.36, h * 0.92, w * 0.22, w * 0.08, h * 0.24, fill="#D8C8A8", top="#E8DCC0", side="#B8A888"))
    o.append(f'<ellipse cx="{f(w * 0.82)}" cy="{f(h * 0.82)}" rx="{f(w * 0.1)}" ry="{f(h * 0.06)}" fill="#1A1210" stroke="#0D0D0F" stroke-width="2"></ellipse>')
    return "".join(o)

def abraham_sarah(p, w, h, seed):
    """Look unto Abraham your father, and unto Sarah that bare you; for when he was but one I called him, and I blessed him, and
    made him many: an old man and an old woman outside their tent under a sky full of stars."""
    b = h * 0.92
    o = [mk.defs(p, *ALL), bg(w, h, "#05051A", "#2A2050"), mk.stars(120, w, h * 0.66, seed), ground(w, h, h * 0.82, "#2A2030", dy=0),
         J1.tent_big(w * 0.76, b, min(w * 0.3, h * 0.6), h * 0.36, color="#3A2A22", stripe="#6A5A3A", open_=True, glow="#FFC14D")]
    s = fit(b, max(h * 0.5, b - 170))
    o.append(man(p, w * 0.3, b, s, "#3A4A7A", up=[(-22, -158), (-30, -190), (-24, -222)]) + woman(p, w * 0.42, b, s * 0.94, "#6A2A4A"))
    return "".join(o)

def eden_garden(w, h, seed):
    """He hath made her wilderness like Eden, and her desert like the garden of Jehovah; joy and gladness, thanksgiving, and the
    voice of melody: ruined Zion on its hill with a green garden spreading over the desert around it, trees in fruit, a stream."""
    r = random.Random(seed)
    o = [bg(w, h, "#7AB8E8", "#FFF0C8"), J.city_hill(w * 0.5, h * 0.5, w * 0.24, h * 0.26, seed), ground(w, h, h * 0.5, "#7AAA4A", dy=0),
         f'<path d="M-10 {f(h * 0.8)} C {f(w * 0.3)} {f(h * 0.7)} {f(w * 0.6)} {f(h * 0.9)} {f(w + 10)} {f(h * 0.78)}" stroke="#2C9DB8" stroke-width="{f(max(5, h * 0.02))}" fill="none"></path>']
    for _ in range(14):
        x = r.uniform(0, w); y = r.uniform(h * 0.56, h * 0.98); s = 0.4 + (y / h) * 0.8
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - 30 * s)}" stroke="#5A3A22" stroke-width="{f(4 * s)}"></path><circle cx="{f(x)}" cy="{f(y - 40 * s)}" r="{f(18 * s)}" fill="{r.choice(["#3E8A3A", "#2E6A32", "#5E9F2A"])}" stroke="#0D0D0F" stroke-width="1.4"></circle>'
                 + "".join(f'<circle cx="{f(x + r.uniform(-12, 12) * s)}" cy="{f(y - 40 * s + r.uniform(-10, 10) * s)}" r="{f(2.6 * s)}" fill="{r.choice(["#D7261E", "#FFD23F", "#FF8A3D"])}"></circle>' for _ in range(3)))
    return "".join(o)

def heavens_vanish(w, h, seed):
    """The heavens shall vanish away like smoke, and the earth shall wax old like a garment; but my salvation shall be for ever:
    the sky above the hills dissolving into drifting smoke, the land grey and worn."""
    o = [bg(w, h, "#6A6A7A", "#C8C0B8")]
    o.append(smoke(w * 0.3, h * 0.6, 9, seed, r0=h * 0.06, spread=w * 0.2, color="#8A8A98", op=0.7, rise=0.5) + smoke(w * 0.74, h * 0.56, 8, seed + 1, r0=h * 0.06, spread=w * 0.2, color="#9A9AA8", op=0.6, rise=0.5))
    o.append(hills(w, h, h * 0.72, seed, color="#8A8478", amp=10) + ground(w, h, h * 0.82, "#9A9488", dy=0))
    return "".join(o)

def rahab_sea(w, h, seed):
    """Awake, awake, put on strength, O arm of Jehovah; is it not thou that didst cut Rahab in pieces, that didst pierce the
    monster? that driedst up the sea, the waters of the great deep: a storm over the great deep, a sea-monster's coils broken
    in the waves, and beyond, a dry path through the sea (no arm drawn)."""
    r = random.Random(seed)
    o = [bg(w, h, "#0B1428", "#3A4A6A"), E2.bolt(w * 0.2, 0, h * 0.4, seed)]
    pts = [(w * 0.06, h * 0.7), (w * 0.16, h * 0.54), (w * 0.26, h * 0.68)]
    o.append(SN.snake(pts, min(w, h) * 0.05, f"rh{seed}a", head_scale=1.4))
    pts2 = [(w * 0.34, h * 0.72), (w * 0.42, h * 0.58), (w * 0.5, h * 0.74)]
    o.append(SN.snake(pts2, min(w, h) * 0.05, f"rh{seed}b", head_scale=0.01))
    for k in range(3):
        y = h * (0.66 + k * 0.12)
        d = f"M-10 {f(y)} " + " ".join(f"Q {f(x + 30)} {f(y - 18 + r.uniform(-6, 6))} {f(x + 60)} {f(y)}" for x in range(-10, int(w * 0.62), 60))
        o.append(f'<path d="{d} L {f(w * 0.62)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="{["#1F4A6A", "#163A5A", "#102A48"][k]}" stroke="#E8F6FA" stroke-width="1.6" opacity="0.92"></path>')
    o.append(f'<g transform="translate({f(w * 0.62)} 0)">{E3.sea_corridor(w * 0.38, h, (w * 0.19, h * 0.3), w * 0.1, w * 0.28, seed, uid=f"rs{seed}")}</g>')
    return "".join(o)

def staggering_cup(w, h, seed, others=False):
    """Thou hast drunk at the hand of Jehovah the cup of his wrath; the bowl of the cup of staggering: a great bowl overturned on
    the steps of an empty street, its dregs spilled (others=True: the cup set before the gate of the oppressors' city)."""
    o = [bg(w, h, "#3A2A3A", "#B8806A"), ground(w, h, h * 0.66, "#8A7A6A", dy=0)]
    if others:
        o.append(ziggurat(w * 0.76, h * 0.66, w * 0.3, h * 0.4, color="#8A5A3A", seed=seed))
    else:
        for i in range(5):
            o.append(f'<rect x="{f(w * (0.5 + i * 0.1))}" y="{f(h * 0.3)}" width="{f(w * 0.1)}" height="{f(h * 0.36)}" fill="#B8A88A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    s = min(1.2, h / 240); cx, cy = w * 0.3, h * 0.84
    o.append(f'<g transform="rotate({0 if others else 70} {f(cx)} {f(cy)})"><path d="M{f(cx - 50 * s)} {f(cy - 40 * s)} L {f(cx + 50 * s)} {f(cy - 40 * s)} C {f(cx + 46 * s)} {f(cy)} {f(cx + 20 * s)} {f(cy + 10 * s)} {f(cx)} {f(cy + 10 * s)} C {f(cx - 20 * s)} {f(cy + 10 * s)} {f(cx - 46 * s)} {f(cy)} {f(cx - 50 * s)} {f(cy - 40 * s)} Z" fill="#B87333" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(cx)}" cy="{f(cy - 40 * s)}" rx="{f(50 * s)}" ry="{f(10 * s)}" fill="#5A0A1A" stroke="#0D0D0F" stroke-width="2"></ellipse></g>')
    if not others:
        o.append(f'<path d="M{f(cx + 30 * s)} {f(cy + 4)} C {f(cx + 70 * s)} {f(cy + 14 * s)} {f(cx + 110 * s)} {f(cy + 4 * s)} {f(cx + 150 * s)} {f(cy + 12 * s)}" stroke="#5A0A1A" stroke-width="{f(8 * s)}" fill="none" stroke-linecap="round"></path>')
    return "".join(o)

def antelope_net(w, h, seed):
    """Thy sons have fainted, they lie at the head of all the streets, as an antelope in a net: an antelope caught in a net at the
    corner of an empty street (the sons told in words only)."""
    o = [bg(w, h, "#5A4A5A", "#C8A088"), ground(w, h, h * 0.7, "#8A7A6A", dy=0)]
    for i in range(4):
        o.append(f'<rect x="{f(w * (0.58 + i * 0.11))}" y="{f(h * 0.24)}" width="{f(w * 0.11)}" height="{f(h * 0.46)}" fill="#A8987A" stroke="#0D0D0F" stroke-width="1.6"></rect>')
    k = min(0.7, h / 360)
    ax, ay = w * 0.3, h * 0.9
    o.append(f'<g transform="translate({f(ax)} {f(ay)}) scale({f(k)})">'
             '<path d="M-40 -60 L -44 0 M-30 -58 L -26 0 M30 -58 L 26 0 M40 -60 L 44 0" stroke="#0D0D0F" stroke-width="6" stroke-linecap="round"></path>'
             '<path d="M-40 -60 L -44 0 M-30 -58 L -26 0 M30 -58 L 26 0 M40 -60 L 44 0" stroke="#C8905A" stroke-width="3" stroke-linecap="round"></path>'
             '<ellipse cx="0" cy="-70" rx="52" ry="20" fill="#C8905A" stroke="#0D0D0F" stroke-width="2.4"></ellipse><path d="M-40 -64 C -20 -56 20 -56 40 -64" stroke="#F3EFE6" stroke-width="4" fill="none"></path>'
             '<path d="M40 -80 L 58 -116 L 70 -112 L 54 -76 Z" fill="#C8905A" stroke="#0D0D0F" stroke-width="2"></path>'
             '<ellipse cx="68" cy="-118" rx="14" ry="8" fill="#C8905A" stroke="#0D0D0F" stroke-width="2"></ellipse><circle cx="70" cy="-121" r="1.8" fill="#0D0D0F"></circle>'
             '<path d="M62 -124 C 58 -140 62 -152 70 -160 M68 -125 C 66 -140 72 -150 80 -156" stroke="#2A1A10" stroke-width="3" fill="none"></path></g>')
    for i in range(9):
        o.append(f'<path d="M{f(w * 0.14 + i * w * 0.04)} {f(h * 0.6)} L {f(w * 0.12 + i * w * 0.044)} {f(h * 0.96)}" stroke="#E8D8A8" stroke-width="1.6"></path>')
    for k2 in range(6):
        o.append(f'<path d="M{f(w * 0.12)} {f(h * (0.62 + k2 * 0.06))} C {f(w * 0.3)} {f(h * (0.58 + k2 * 0.06))} {f(w * 0.4)} {f(h * (0.66 + k2 * 0.06))} {f(w * 0.5)} {f(h * (0.62 + k2 * 0.06))}" stroke="#E8D8A8" stroke-width="1.6" fill="none"></path>')
    return "".join(o)
