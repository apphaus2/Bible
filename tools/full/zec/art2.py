"""Drawings for Zechariah 5–8 (chapter 2 of the volume), on zec.art: the flying roll, the ephah, the four chariots between
the mountains of brass, the crowns, the fast in sackcloth, the widow and the sojourner at the gate, the whirlwind over the
desolate land, the old and the children in the streets of Jerusalem, the fasts become feasts, and the ten men holding the
skirt of a Jew."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from zec.art import *
from zec.art import f, vision, light_fig, GOLD, CY

def flying_roll(p, w, h, seed, houses=False):
    """A flying roll, the length thereof twenty cubits, and the breadth ten cubits (houses=True: going forth over the land
    and entering the house of the thief, consuming it, timber and stones)."""
    cx, cy = w * 0.5, h * (0.34 if houses else 0.5)
    k = min(w / 760, h / 300)
    body = [f'<g transform="rotate(-6 {f(cx)} {f(cy)})">' + scroll(cx, cy, 300 * k, 140 * k, color="#F3E8C8", lines=7) + '</g>',
            wind_lines(w, h, seed, n=8, color=CY, op=0.5, y0=0.2, y1=0.7)]
    if not houses:
        body += [f'<path d="M{f(cx - 150 * k)} {f(cy + 100 * k)} L {f(cx + 150 * k)} {f(cy + 100 * k)}" stroke="{GOLD}" stroke-width="1.6"></path>', label(cx, cy + 116 * k, "LENGTH · 20 CUBITS", GOLD, 10),
                 f'<path d="M{f(cx + 186 * k)} {f(cy - 70 * k)} L {f(cx + 186 * k)} {f(cy + 70 * k)}" stroke="{GOLD}" stroke-width="1.6"></path>', label(cx + 186 * k, cy - 80 * k, "BREADTH · 10", GOLD, 10)]
    else:
        for i in range(4):
            x = w * (0.12 + i * 0.25); b = h * 0.96
            body.append(f'<rect x="{f(x - 34)}" y="{f(b - 60 * k)}" width="68" height="{f(60 * k)}" fill="#3A3A4A" stroke="{CY}" stroke-width="1.4"></rect>')
        body.append(E.blaze(w * 0.62, h * 0.96, w * 0.16, h * 0.3, seed, n=6))
    return vision(p, w, h, "".join(body), "VI · THE FLYING ROLL", seed=seed)

def ephah(p, w, h, seed, shut=False, carried=False):
    """The ephah that goeth forth, a talent of lead lifted up, and a woman sitting in the midst of the ephah — Wickedness, a
    shadow with no face (shut=True: cast down into it and the weight of lead upon its mouth; carried=True: two women with
    wings like a stork lifting it between earth and heaven, toward the land of Shinar)."""
    k = min(2.6, h / 250, w / 420); cx, cy = w * 0.5, h * (0.6 if not carried else 0.5)
    basket = (f'<path d="M{f(cx - 60 * k)} {f(cy - 40 * k)} L {f(cx + 60 * k)} {f(cy - 40 * k)} L {f(cx + 48 * k)} {f(cy + 50 * k)} L {f(cx - 48 * k)} {f(cy + 50 * k)} Z" fill="#8A6A3A" stroke="{GOLD}" stroke-width="2"></path>'
              + "".join(f'<path d="M{f(cx - 58 * k + i * 4 * k)} {f(cy - 30 * k + i * 16 * k)} L {f(cx + 58 * k - i * 4 * k)} {f(cy - 30 * k + i * 16 * k)}" stroke="#5A4A2A" stroke-width="1.4"></path>' for i in range(5)))
    body = [basket]
    lx, ly = (cx, cy - 46 * k) if (shut or carried) else (cx + 110 * k, cy - 110 * k)
    body.append(f'<ellipse cx="{f(lx)}" cy="{f(ly)}" rx="{f(62 * k)}" ry="{f(12 * k)}" fill="#6A6A78" stroke="{CY}" stroke-width="1.6"></ellipse>')
    if not carried: body.append(label(lx, ly - 18 * k, "A TALENT OF LEAD", CY, 9))
    if carried:
        body.append(mk.defs(p, *ALL))
        s = 0.42 * k
        for side in (-1, 1):
            x = cx + side * 104 * k; yb = cy + 60 * k
            body.append(stork_wing(x - side * 6 * s, yb - 150 * s, s * 0.9, side)
                        + mk.person(p, round(x), round(yb), round(s, 3), body=SKIN, cloth="#5A5A8A", woman=True, hair="#1A1210", sw=3, flip=side > 0,
                                    up=[(22, -150), (46, -138), (70, -128)])
                        + f'<path d="M{f(x - side * 70 * s)} {f(yb - 128 * s)} L {f(cx + side * 56 * k)} {f(cy - 34 * k)}" stroke="#C8B890" stroke-width="2.4"></path>')
        body.append(wind_lines(w, h, seed, n=8, color=CY, op=0.5) + route([(w * 0.7, h * 0.86), (w * 0.94, h * 0.7)], color=GOLD) + label(w * 0.9, h * 0.62, "SHINAR", GOLD, 10))
    return vision(p, w, h, "".join(body), "VII · THE EPHAH", seed=seed)

def stork_wing(x, y, s, side):
    """A stork's wing spread from the shoulder at (x, y) toward side (+1 right, -1 left): white coverts, black flight
    feathers."""
    q = lambda a, b: f"{f(x + side * a * s)} {f(y + b * s)}"
    white = (f'<path d="M{q(0, 0)} C {q(30, -70)} {q(110, -120)} {q(200, -112)} L {q(150, -60)} C {q(110, -36)} {q(60, -10)} {q(8, 30)} Z" '
             'fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1.8"></path>')
    tips = [(200, -112), (186, -84), (196, -78), (172, -56), (180, -48), (150, -34), (156, -24), (120, -14)]
    black = (f'<path d="M{q(150, -60)} L {q(200, -112)} ' + " ".join(f"L {q(a, b)}" for a, b in tips[1:]) + f' C {q(110, -24)} {q(130, -44)} {q(150, -60)} Z" '
             'fill="#1A1A1E" stroke="#0D0D0F" stroke-width="1.4"></path>')
    lines = "".join(f'<path d="M{q(40 + i * 24, -40 - i * 10)} L {q(60 + i * 26, -20 - i * 9)}" stroke="#B8B2A6" stroke-width="1.2"></path>' for i in range(3))
    return white + black + lines

def chariots(p, w, h, seed, going=False):
    """Four chariots coming out from between two mountains of brass: red horses, black, white, and grizzled (going=True: the
    black toward the north country, the white after them, the grizzled toward the south, the strong to and fro)."""
    k = min(0.8, h / 340)
    body = []
    for side in (-1, 1):
        x0 = w * 0.5 + side * w * 0.14
        body.append(f'<path d="M{f(x0)} {f(h + 10)} L {f(x0 + side * w * 0.04)} {f(h * 0.14)} L {f(x0 + side * w * 0.3)} {f(h * 0.3)} L {f(x0 + side * w * 0.5)} {f(h + 10)} Z" fill="#B87A3A" stroke="{GOLD}" stroke-width="2"></path>'
                    + "".join(f'<path d="M{f(x0 + side * w * (0.06 + i * 0.06))} {f(h * 0.4)} L {f(x0 + side * w * (0.1 + i * 0.07))} {f(h * 0.9)}" stroke="#E8B860" stroke-width="1.4" opacity="0.6"></path>' for i in range(4)))
    body.append(label(w * 0.2, h * 0.24, "MOUNTAIN OF BRASS", GOLD, 9) + label(w * 0.8, h * 0.24, "MOUNTAIN OF BRASS", GOLD, 9))
    cols = [("#C8302A", "RED"), ("#2A2A34", "BLACK"), ("#F3EFE6", "WHITE"), ("#8A8A8A", "GRIZZLED")]
    if not going:
        for i, (c, n) in enumerate(cols):
            x = w * 0.5; y = h * (0.36 + i * 0.17)
            body.append(E3.chariot(x - 30 * k, y, k * (0.5 + i * 0.1), color=c, driver="#E8E2D6") + label(x + 90 * k, y - 30 * k, n, CY, 9))
    else:
        dirs = [("NORTH", 0.5, 0.1, "#8FD0E2"), ("AFTER THEM", 0.36, 0.18, "#F3EFE6"), ("SOUTH", 0.5, 0.96, "#8A8A8A"), ("TO AND FRO", 0.92, 0.56, "#C8302A")]
        for n, x, y, c in dirs:
            body.append(route([(w * 0.5, h * 0.55), (w * x, h * y)], color=c, sw=3))
        body.append(label(w * 0.5, h * 0.07, "THE NORTH COUNTRY", CY, 10) + label(w * 0.66, h * 0.92, "THE SOUTH COUNTRY", CY, 10))
        body.append(E3.chariot(w * 0.5, h * 0.62, k * 0.8, color="#2A2A34", driver="#E8E2D6"))
    return vision(p, w, h, "".join(body), "VIII · THE FOUR CHARIOTS", seed=seed)

def crowns(w, h, seed, hung=False):
    """Take of them silver and gold, and make crowns, and set them upon the head of Joshua the high priest (hung=True: the
    crowns a memorial in the temple of Jehovah, and they that are far off coming to build)."""
    import samuel2 as S2
    if not hung:
        o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#2A1E14"></rect>', halo(w * 0.5, h * 0.5, h * 0.6, "#FFC14D", 0.4),
             f'<rect x="-10" y="{f(h * 0.82)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#5A4030" stroke="#0D0D0F" stroke-width="2"></rect>']
        k = min(2.4, h / 120)
        o.append(S2.crown(w * 0.38, h * 0.8, k) + S2.crown(w * 0.62, h * 0.8, k * 0.9).replace("#E8B830", "#C8C8D0"))
        r = random.Random(seed)
        for i in range(6):
            o.append(f'<ellipse cx="{f(w * r.uniform(0.1, 0.9))}" cy="{f(h * r.uniform(0.86, 0.96))}" rx="8" ry="4" fill="{r.choice(["#E8B830", "#C8C8D0"])}" stroke="#0D0D0F" stroke-width="1"></ellipse>')
        return "".join(o)
    o = [sky(w, h, "#5A7AB8", "#F3E8C8"), ground(w, h, h * 0.8, "#C8B88A", dy=0), temple_front(w * 0.5, h * 0.8, w * 0.36, seed)]
    k = min(1.0, h / 260)
    o.append(halo(w * 0.5, h * 0.3, h * 0.16, "#FFF4C2", 0.5) + S2.crown(w * 0.44, h * 0.36, k * 0.8) + S2.crown(w * 0.56, h * 0.36, k * 0.8).replace("#E8B830", "#C8C8D0"))
    o.append(route([(w * 0.02, h * 0.9), (w * 0.22, h * 0.82)], color="#E8B830", dash="6 5") + route([(w * 0.98, h * 0.9), (w * 0.78, h * 0.82)], color="#E8B830", dash="6 5"))
    return "".join(o)

def fasting(p, w, h, seed):
    """When ye fasted and mourned in the fifth and in the seventh month, these seventy years, did ye at all fast unto me? —
    mourners in sackcloth sitting in the dust, a table set aside, the ruined city behind."""
    from job.art import seated
    b = h * 0.94
    o = [sky(w, h, "#6A6A7A", "#C8B8A0"), ruin(w * 0.3, w + 10, h * 0.56, h * 0.2, seed, color="#A8987A"), ground(w, h, h * 0.58, "#9A8A6A", dy=0)]
    k = min(1.0, h / 300)
    for i, x in enumerate((0.16, 0.34, 0.52)):
        o.append(seated(w * x, b, k * 0.8, "#6A5A48", head="#6A5A48", beard="#3A2A1E" if i != 1 else "#9A948A", bowed=True))
    o.append(f'<rect x="{f(w * 0.68)}" y="{f(b - 40 * k)}" width="{f(w * 0.24)}" height="{f(12 * k)}" fill="#8A5A30" stroke="#0D0D0F" stroke-width="2"></rect>'
             f'<path d="M{f(w * 0.7)} {f(b - 28 * k)} L {f(w * 0.7)} {f(b)} M{f(w * 0.9)} {f(b - 28 * k)} L {f(w * 0.9)} {f(b)}" stroke="#5A3A1E" stroke-width="5"></path>'
             + cup(w * 0.76, b - 40 * k, k * 0.4, color="#C8C8D0") + f'<ellipse cx="{f(w * 0.85)}" cy="{f(b - 44 * k)}" rx="{f(16 * k)}" ry="{f(6 * k)}" fill="#C8904A" stroke="#0D0D0F" stroke-width="1.4"></ellipse>')
    return "".join(o)

def widow_gate(p, w, h, seed):
    """Oppress not the widow, nor the fatherless, the sojourner, nor the poor: four figures waiting at the city gate — a
    widow in grey, a child, a traveller with his staff, a poor man with his hand held out."""
    from genesis.art3 import STAFF, HOLD_STAFF
    b = h * 0.95
    o = [mk.defs(p, *ALL), sky(w, h, "#8FB8D8", "#F3E8C8"), walls(-10, w + 10, h * 0.7, h * 0.5, seed, color="#C8A878", towers=2), ground(w, h, h * 0.7, "#B8A07A", dy=0)]
    s = fit(b, h * 0.42)
    o.append(woman(p, w * 0.16, b, s, "#5A5A62") + man(p, w * 0.3, b, s * 0.62, "#8A6A3A")
             + mk.person(p, round(w * 0.62), round(b), round(s, 3), body=SKIN, cloth="#3A5A4A", sw=3, up=HOLD_STAFF, extra=STAFF + A.headcloth("#3A5A4A"))
             + man(p, w * 0.82, b, s * 0.96, "#6A5A48", flip=True, up=[(22, -158), (40, -150), (56, -140)]))
    return "".join(o)

def adamant(w, h, seed):
    """They made their hearts as an adamant stone; I will scatter them with a whirlwind among all the nations; the pleasant
    land desolate: a whirlwind over an empty land, a hard grey stone in the foreground."""
    from job.art import whirl
    o = [sky(w, h, "#3A3A4A", "#A89A8A"), whirl(w * 0.6, h * 0.04, h * 0.7, w * 0.4, w * 0.04, seed, color="#C8C0C8", op=0.4),
         hills(w, h, h * 0.6, seed, color="#6A5A5A", amp=14), ground(w, h, h * 0.68, "#8A7A6A", dy=0), vines(w * 0.4, w * 0.98, h * 0.82, h * 0.92, seed, rows=2, bare=True)]
    k = min(1.2, h / 260)
    o.append(f'<path d="M{f(w * 0.1)} {f(h * 0.96)} L {f(w * 0.12)} {f(h * 0.96 - 50 * k)} L {f(w * 0.2)} {f(h * 0.96 - 70 * k)} L {f(w * 0.3)} {f(h * 0.96 - 46 * k)} L {f(w * 0.32)} {f(h * 0.96)} Z" fill="#6A6A78" stroke="#0D0D0F" stroke-width="2.4"></path>'
             f'<path d="M{f(w * 0.16)} {f(h * 0.96 - 40 * k)} L {f(w * 0.22)} {f(h * 0.96 - 52 * k)} M{f(w * 0.2)} {f(h * 0.96 - 20 * k)} L {f(w * 0.28)} {f(h * 0.96 - 30 * k)}" stroke="#B8B8C8" stroke-width="2"></path>')
    return "".join(o)

def streets_play(p, w, h, seed):
    """Old men and old women in the streets of Jerusalem, every man with his staff in his hand for very age; and the streets
    full of boys and girls playing: a sunny street, the old leaning on staves, children running with a hoop and a ball."""
    from genesis.art3 import STAFF, HOLD_STAFF
    b = h * 0.95
    o = [mk.defs(p, *ALL), sky(w, h, "#8FD0E2", "#F3E8C8")]
    for side in (0, 1):
        for i in range(3):
            x = (w * i * 0.12) if side == 0 else w * (0.64 + i * 0.12)
            o.append(f'<rect x="{f(x)}" y="{f(h * (0.12 + (i % 2) * 0.08))}" width="{f(w * 0.12)}" height="{f(h)}" fill="{["#E8D0A0", "#D8C090", "#E0C898"][i]}" stroke="#0D0D0F" stroke-width="2"></rect>'
                     f'<rect x="{f(x + w * 0.04)}" y="{f(h * 0.6)}" width="{f(w * 0.04)}" height="{f(h * 0.4)}" fill="#5A3A22"></rect>')
    o.append(ground(w, h, h * 0.82, "#D8C090", dy=0))
    s = fit(b, h * 0.4)
    o.append(mk.person(p, round(w * 0.12), round(b), round(s, 3), body=SKIN, cloth="#5A4A6A", sw=3, up=HOLD_STAFF, extra=STAFF + WHITE_BEARD)
             + mk.person(p, round(w * 0.86), round(b), round(s, 3), body=SKIN, cloth="#7A5A6A", woman=True, hair="#C8C2B6", sw=3, flip=True, up=HOLD_STAFF, extra=STAFF))
    for i, x in enumerate((0.34, 0.46, 0.58, 0.68)):
        o.append((man if i % 2 == 0 else woman)(p, w * x, b - (i % 2) * 6, s * 0.55, ["#B5421E", "#E8B830", "#1F5FAD", "#2E6B3A"][i], flip=i % 2 == 1, up=[(22, -158), (40, -176), (58, -196)] if i < 2 else None))
    o.append(f'<circle cx="{f(w * 0.52)}" cy="{f(b - 70 * s)}" r="{f(10 * s)}" fill="#D7261E" stroke="#0D0D0F" stroke-width="1.6"></circle>'
             f'<circle cx="{f(w * 0.76)}" cy="{f(b - 30 * s)}" r="{f(24 * s)}" fill="none" stroke="#8A5A30" stroke-width="{f(4 * s)}"></circle>')
    return "".join(o)

def east_west(w, h):
    """I will save my people from the east country, and from the west country, and bring them to dwell in Jerusalem: roads
    from the sunrise and the sunset converging on the city, as a technical map."""
    o = [grid_bg(w, h)]
    o.append(route([(w * 0.98, h * 0.5), (w * 0.7, h * 0.46), (w * 0.54, h * 0.5)], color=GOLD) + route([(w * 0.02, h * 0.5), (w * 0.3, h * 0.54), (w * 0.46, h * 0.5)], color=GOLD))
    o += [node(w * 0.5, h * 0.5, "JERUSALEM", color=GOLD, r=7), label(w * 0.94, h * 0.34, "THE EAST COUNTRY", CY, 9, anchor="end"), label(w * 0.06, h * 0.34, "THE WEST COUNTRY", CY, 9, anchor="start")]
    return "".join(o)

def gate_truth(p, w, h, seed):
    """Execute the judgment of truth and peace in your gates: elders seated in the gateway, scales level between them."""
    from ecc.art import scales
    from job.art import seated
    b = h * 0.95
    o = [sky(w, h, "#8FB8D8", "#F3E8C8"), walls(-10, w + 10, h * 0.66, h * 0.52, seed, color="#C8A878", towers=2), ground(w, h, h * 0.66, "#B8A07A", dy=0)]
    k = min(1.0, h / 300)
    o.append(seated(w * 0.2, b, k * 0.8, "#3A4A6A", head="#E8E2D6", beard="#E8E2D6") + seated(w * 0.8, b, k * 0.8, "#5A3A2A", head="#E8E2D6", beard="#B8B2A8", flip=True))
    o.append(scales(w * 0.5, b, k * 0.9, tilt=0))
    return "".join(o)

def feasts(p, w, h, seed):
    """The fast of the fourth month, of the fifth, of the seventh and of the tenth shall be joy and gladness, and cheerful
    feasts: four cells of the calendar, each with a lamp lit and a cup."""
    from genesis.art4 import clay_lamp
    body = []
    cw = w / 4
    for i, m in enumerate(("THE FOURTH MONTH", "THE FIFTH", "THE SEVENTH", "THE TENTH")):
        x0 = i * cw
        body.append(f'<rect x="{f(x0 + 8)}" y="{f(h * 0.1)}" width="{f(cw - 16)}" height="{f(h * 0.7)}" fill="#12113A" stroke="{GOLD}" stroke-width="1.6"></rect>'
                    + label(x0 + cw / 2, h * 0.2, m, GOLD, 9) + halo(x0 + cw * 0.36, h * 0.56, h * 0.12, "#FFC14D", 0.6)
                    + clay_lamp(x0 + cw * 0.36, h * 0.66, min(0.6, h / 400)) + cup(x0 + cw * 0.68, h * 0.72, min(0.4, h / 600), color="#E8B830"))
    return vision(p, w, h, "".join(body), "FASTS · JOY AND GLADNESS", seed=seed)

def ten_men(p, w, h, seed):
    """Ten men out of all the languages of the nations shall take hold of the skirt of him that is a Jew, saying, We will go
    with you: a man of Judah walking toward Jerusalem, ten men of many nations following, the first holding his hem."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), sky(w, h, "#5A7AB8", "#FFE6A0"), mount_zion(w * 0.12, h * 0.72, w * 0.16, h * 0.4, seed, color="#8A7A6A"), ground(w, h, h * 0.72, "#C8B080", dy=0)]
    s = fit(b, h * 0.42)
    o.append(mk.person(p, round(w * 0.32), round(b), round(s, 3), body=SKIN, cloth="#2C4A7A", sw=3, flip=True, extra=A.headcloth("#2C4A7A") + BLACK_BEARD))
    cols = ["#B5421E", "#E8B830", "#2E6B3A", "#6A1A5A", "#1F5FAD", "#8A6A3A", "#C8C8D0", "#7A1A2A", "#3A5A4A", "#5A4A6A"]
    for i in range(10):
        x = w * (0.42 + i * 0.056); bb = b - (i % 2) * h * 0.04
        o.append(man(p, x, bb, s * (0.9 - (i % 3) * 0.04), cols[i], flip=True, up=[(22, -158), (44, -130), (62, -118)] if i == 0 else None))
    return "".join(o)
