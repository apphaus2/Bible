"""Drawings for Revelation 12–14 (chapter 4 of the volume): the woman and the dragon, the beasts, the Lamb on mount Zion, the
three angels and the harvest. Satan is never drawn: the great red dragon is a red, star-torn sky, the war in heaven
Michael's angels in light against a darkness with no shape, the serpent's flood a river poured into the opened earth with
no one pouring it. The woman arrayed with the sun is a figure of light far off; the travail and the birth are in the words.
The beasts are heraldic plates in the manner of Daniel's beasts, standing still on a dark field; the mark and its number a
technical plate. The winepress is told over the empty plain.

    woman_sun(p, w, h, seed, stage=)     the woman arrayed with the sun, the moon under her feet, a crown of twelve stars
                                         ("sign"; "flee" into the wilderness with the child caught up as light; "wings" —
                                         borne on the two wings of the great eagle; "flood" — the earth swallowing the river)
    red_sky(w, h, seed)                  another sign: a red, star-torn sky, the third part of the stars falling (no dragon)
    war_heaven(p, w, h, seed, fall=)     Michael and his angels in light against a darkness of no shape; fall= cast down
    heaven_earth(w, h, seed)             rejoice, O heavens — woe for the earth and the sea
    beast_plate(w, h, which, ...)        the beast out of the sea ("sea"), out of the earth ("earth"), the scarlet beast
                                         ("scarlet", cup= the golden cup set by it) — heraldic, every part named
    months(w, h, n=42)                   forty and two months as a plate of cells
    emblem_sword(w, h, seed)             captivity and the sword: a chain and a sheathed sword crossed in a medallion
    image(p, w, h, seed)                 the image of the beast on its pedestal in a great square, the crowds far off
    mark_plate(w, h)                     the mark on the right hand or the forehead, the number of his name
    zion(p, w, h, seed)                  the Lamb standing on mount Zion and the hundred and forty and four thousand
    firstfruits(w, h)                    144 × 1,000: a numbered plate
    flying(p, w, h, seed, which)         an angel flying in mid heaven ("first", "second" — Babylon fallen far off, "third")
    tombs_dawn(w, h, seed)               blessed are the dead who die in the Lord: tombs in a garden at dawn
    harvest(p, w, h, seed, stage)        "cloud" — one like a son of man on a white cloud, a golden crown, a sharp sickle;
                                         "vine" — the angel with the sickle over the vine; "press" — the winepress without
                                         the city, the empty plain"""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from rev.art3 import *
from rev.art import f, INK, GOLD, GOLD_L, WHITE, GIRDLE
from ntcast import JESUS_SKIN, _HAIR_FIG, _BEARD_FIG
from mat.art import veil
from dan.art4 import field, wing, lion_walk
from oba.minor import cup, walls, ruin, vines
from ecc.art import tombs

LIGHT_W = "#FFF6DA"

def woman_light(p, x, b, s, flip=False, up=None):
    """The woman arrayed with the sun: a figure of light, robed and veiled in white and gold, the sun about her, the moon
    under her feet, a crown of twelve stars upon her head."""
    crown = "".join(star(18 * math.cos(math.radians(200 + i * 140 / 11)), -205 + 10 * math.sin(math.radians(200 + i * 140 / 11)), 3.4, "#FFF4C2", 0.6) for i in range(12))
    o = halo(x, b - 110 * s, 150 * s, "#FFE680", 0.75) + rays(x, b - 110 * s, 24, 80 * s, 210 * s, "#FFE680", 0.4, max(2, 3 * s))
    o += (f'<path d="M{f(x - 40 * s)} {f(b + 4 * s)} A {f(44 * s)} {f(30 * s)} 0 0 0 {f(x + 40 * s)} {f(b + 4 * s)} A {f(36 * s)} {f(20 * s)} 0 0 1 {f(x - 40 * s)} {f(b + 4 * s)} Z" '
          f'fill="#F3F0E0" stroke="#C8B080" stroke-width="{f(max(1, 2 * s))}"></path>')
    return o + robed(p, x, b, s, "#FFFDF0", skin=LIGHT_W, woman=True, line="#E8B830", flip=flip, up=up, mantle="#FFE680", extra=veil("#FFF8DC", "#E8D8A0") + crown)

def woman_sun(p, w, h, seed, stage="sign"):
    """The woman (12:1–6, 12:13–16). "sign": high in heaven, a figure of light far off; "flee": the child caught up unto God
    and unto his throne as a light rising, and the woman far off fleeing into the wilderness; "wings": borne over the
    wilderness on the two wings of the great eagle; "flood": the river cast after her swallowed by the opened earth."""
    o = [defs(p)]
    if stage == "sign":
        o += [sky(w, h, "#0B0B2A", "#3A2A6A"), starfield(w, h, seed, 70, 1.0)]
        o.append(woman_light(p, w * 0.5, h * 0.82, h * 0.66 / 205))
        return "".join(o)
    hz = h * 0.66
    o += [sky(w, h, "#2A2A6A", "#E8B880")]
    o.append(hills(w, h, hz - h * 0.04, seed, color="#B8885A", amp=16, step=90) + ground(w, h, hz, "#D8B880", dy=0))
    if stage == "flee":
        o.append(halo(w * 0.7, h * 0.08, h * 0.3, WHITE, 0.9) + f'<path d="M{f(w * 0.7)} {f(h * 0.44)} L {f(w * 0.7)} {f(h * 0.08)}" stroke="#FFF4C2" stroke-width="10" opacity="0.6"></path>'
                 + halo(w * 0.7, h * 0.34, h * 0.06, WHITE, 0.95))
        o.append(woman_light(p, w * 0.3, hz + h * 0.16, h * 0.3 / 205, flip=True))
    elif stage == "wings":
        x, y = w * 0.46, h * 0.46; s = h * 0.34 / 205
        o.append(wing(x - 8, y - 100 * s, h / 180, color="#8A6A4A", flip=True, rot=-30) + wing(x + 8, y - 100 * s, h / 180, color="#8A6A4A", rot=30))
        o.append(woman_light(p, x, y, s, flip=True))
    elif stage == "flood":
        o.append(f'<path d="M-10 {f(hz + h * 0.06)} C {f(w * 0.2)} {f(hz + h * 0.04)} {f(w * 0.36)} {f(hz + h * 0.14)} {f(w * 0.5)} {f(hz + h * 0.16)} L {f(w * 0.5)} {f(hz + h * 0.26)} '
                 f'C {f(w * 0.34)} {f(hz + h * 0.26)} {f(w * 0.2)} {f(hz + h * 0.18)} -10 {f(hz + h * 0.2)} Z" fill="#3A7AA8" stroke="{INK}" stroke-width="2"></path>')
        o.append(f'<path d="M{f(w * 0.48)} {f(hz + h * 0.12)} L {f(w * 0.56)} {f(hz + h * 0.1)} L {f(w * 0.66)} {f(hz + h * 0.16)} L {f(w * 0.64)} {f(hz + h * 0.3)} L {f(w * 0.54)} {f(hz + h * 0.32)} Z" fill="#1A0E08" stroke="{INK}" stroke-width="2.4"></path>')
        o.append(foam(w * 0.5, hz + h * 0.15, seed, 5))
        o.append(woman_light(p, w * 0.86, hz + h * 0.02, h * 0.18 / 205, flip=True))
    return "".join(o)

def red_sky(w, h, seed):
    """Another sign in heaven (12:3–4): a great red sky, torn, the third part of the stars swept from it and falling to the
    earth as lights; the dragon himself is never drawn (his heads, horns and diadems are in the words)."""
    r = random.Random(seed)
    o = [sky(w, h, "#3A0408", "#B5281E"), halo(w * 0.5, h * 0.4, w * 0.6, "#D7261E", 0.5)]
    for k in range(5):
        x0 = w * r.uniform(0.05, 0.95)
        d = f"M{f(x0)} -10 L {f(x0 + r.uniform(-30, 30))} {f(h * 0.2)} L {f(x0 + r.uniform(-50, 50))} {f(h * 0.4)} L {f(x0 + r.uniform(-30, 30))} {f(h * 0.55)}"
        o.append(f'<path d="{d}" fill="none" stroke="#1A0204" stroke-width="{r.uniform(3, 7):.1f}" opacity="0.7"></path>')
    for _ in range(40):
        x, y = r.uniform(0, w), r.uniform(0, h * 0.5)
        o.append(star(x, y, r.uniform(2, 4), "#FFE6C0", 0.4, "#3A0408"))
    for _ in range(16):
        x, y = r.uniform(0.1, 0.9) * w, r.uniform(0.2, 0.8) * h; ln = r.uniform(30, 70)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x + ln * 0.3)} {f(y - ln)}" stroke="#FFE6A0" stroke-width="2" opacity="0.7"></path>' + star(x, y, 5, "#FFF4C2", 0.8, "#8A1A10"))
    o.append(hills(w, h, h * 0.86, seed, color="#2A0A0E", amp=10, step=80))
    return "".join(o)

def darkness(cx, cy, rw, rh, seed, op=0.95):
    """A darkness with no shape: a mass of black smoke-cloud, ragged, nothing in it."""
    r = random.Random(seed)
    return "".join(f'<ellipse cx="{f(cx + r.uniform(-rw, rw) * 0.8)}" cy="{f(cy + r.uniform(-rh, rh) * 0.8)}" rx="{f(rw * r.uniform(0.3, 0.6))}" ry="{f(rh * r.uniform(0.3, 0.6))}" '
                   f'fill="#0A0608" opacity="{op * r.uniform(0.6, 1.0):.2f}"></ellipse>' for _ in range(14))

def war_heaven(p, w, h, seed, fall=False):
    """There was war in heaven (12:7–9): Michael and his angels — figures of white light, Michael foremost with a spear of
    light — going forth against a darkness with no shape; fall=True: the darkness cast down out of heaven to the earth, falling
    as a black streak, the angels standing in the light."""
    o = [defs(p), sky(w, h, "#1A1440", "#5A3A6A"), halo(w * 0.25, h * 0.3, w * 0.4, "#FFF4C2", 0.8), rays(w * 0.25, h * 0.3, 30, h * 0.1, w * 0.8, "#FFFDF0", 0.3, 4)]
    if fall:
        o.append(darkness(w * 0.74, h * 0.7, w * 0.16, h * 0.18, seed, 0.9))
        for k in range(5): o.append(f'<path d="M{f(w * (0.62 + 0.05 * k))} {f(h * 0.1)} L {f(w * (0.68 + 0.05 * k))} {f(h * 0.62)}" stroke="#0A0608" stroke-width="{6 - k}" opacity="0.6"></path>')
        o.append(hills(w, h, h * 0.9, seed, color="#2A1A2A", amp=10, step=80))
    else:
        o.append(darkness(w * 0.78, h * 0.46, w * 0.22, h * 0.36, seed))
    s = h * 0.62 / 205
    spear = '<path d="M-60 -200 L -60 -40" stroke="#FFF4C2" stroke-width="4"></path><path d="M-60 -212 L -54 -198 L -66 -198 Z" fill="#FFF4C2" stroke="#E8B830" stroke-width="1"></path>'
    for i, (x, b, k) in enumerate(((0.12, 0.76, 0.8), (0.22, 0.86, 0.9), (0.36, 0.96, 1.05), (0.06, 0.9, 0.85))):
        o.append(angel(p, w * x, h * b, s * k, up=[(-22, -158), (-44, -150), (-60, -150)], flip=True, extra=spear if i == 2 else ""))
    o.append(label(w * 0.36, h * 0.12, "MICHAEL AND HIS ANGELS", "#FFF4C2", max(8, min(10, h / 24))))
    return "".join(o)

def heaven_earth(w, h, seed):
    """Rejoice, O heavens; woe for the earth and for the sea (12:10–12): light above, the dark earth and sea below."""
    o = [sky(w, h, "#FFF4C2", "#5A4A8A"), halo(w * 0.5, 0, w * 0.6, WHITE, 0.9), rays(w * 0.5, -10, 30, h * 0.05, w, "#FFFDF0", 0.4, 4)]
    hz = h * 0.62
    o.append(f'<rect x="-10" y="{f(hz - h * 0.08)}" width="{f(w + 20)}" height="{f(h)}" fill="#1A1420"></rect>')
    o.append(sea(w * 0.55, h, hz, seed, color="#1A2A3A", deep="#0A0E14", rough=True))
    o.append(f'<path d="M{f(w * 0.5)} {f(h + 10)} L {f(w * 0.56)} {f(hz)} L {f(w + 10)} {f(hz - h * 0.02)} L {f(w + 10)} {f(h + 10)} Z" fill="#2A2026" stroke="{INK}" stroke-width="2"></path>')
    o.append(darkness(w * 0.6, hz - h * 0.04, w * 0.3, h * 0.08, seed, 0.6))
    return "".join(o)

def _heads(cx, cy, s, n=7, horns=(2, 1, 1, 2, 1, 2, 1), color="#E8A040", diadem_on="horns"):
    """Seven heads on their necks in a fan, ten horns among them; diadems on the horns (or on the heads)."""
    o = []
    for i in range(n):
        a = math.radians(-150 + i * 120 / (n - 1)); L = 46 * s
        hx, hy = cx + L * math.cos(a) * 1.1, cy + L * math.sin(a)
        o.append(f'<path d="M{f(cx)} {f(cy)} Q {f(cx + L * 0.5 * math.cos(a))} {f(cy + L * 0.6 * math.sin(a) + 6 * s)} {f(hx)} {f(hy)}" fill="none" stroke="#0D0D0F" stroke-width="{f(9 * s)}" stroke-linecap="round"></path>'
                 f'<path d="M{f(cx)} {f(cy)} Q {f(cx + L * 0.5 * math.cos(a))} {f(cy + L * 0.6 * math.sin(a) + 6 * s)} {f(hx)} {f(hy)}" fill="none" stroke="{color}" stroke-width="{f(6.4 * s)}" stroke-linecap="round"></path>'
                 f'<ellipse cx="{f(hx)}" cy="{f(hy)}" rx="{f(8 * s)}" ry="{f(6 * s)}" fill="{color}" stroke="#0D0D0F" stroke-width="{f(max(1, 1.6 * s))}"></ellipse>'
                 f'<circle cx="{f(hx + 3 * s)}" cy="{f(hy - 1.5 * s)}" r="{f(1.2 * s)}" fill="#0D0D0F"></circle>')
        for k in range(horns[i]):
            dx = (k - (horns[i] - 1) / 2) * 6 * s
            o.append(f'<path d="M{f(hx + dx - 2 * s)} {f(hy - 5 * s)} L {f(hx + dx)} {f(hy - 16 * s)} L {f(hx + dx + 2 * s)} {f(hy - 5 * s)} Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="{f(max(0.8, 1 * s))}"></path>')
            if diadem_on == "horns":
                o.append(f'<path d="M{f(hx + dx - 3 * s)} {f(hy - 15 * s)} L {f(hx + dx - 3 * s)} {f(hy - 20 * s)} L {f(hx + dx)} {f(hy - 17 * s)} L {f(hx + dx + 3 * s)} {f(hy - 20 * s)} L {f(hx + dx + 3 * s)} {f(hy - 15 * s)} Z" fill="#FFD23F" stroke="#0D0D0F" stroke-width="{f(max(0.6, 0.8 * s))}"></path>')
    return "".join(o)

def beast_plate(w, h, which="sea", cup_=False):
    """A beast as a heraldic emblem on a dark field, standing still, its parts named (13:1–2, 13:11, 17:3–4): "sea" — like
    a leopard, the feet of a bear, the mouth of a lion, seven heads and ten horns with ten diadems; "earth" — two horns like
    a lamb; "scarlet" — the scarlet-coloured beast, seven heads and ten horns, with the golden cup full of abominations set
    beside it (cup_=True; no woman drawn)."""
    import exo.art8 as B
    o = [field(w, h, 13)]
    B._W[0] = w
    s = min(h / 150, w / 300)
    x, y = w * 0.38, h * 0.86
    if which in ("sea", "scarlet"):
        col = "#E8A040" if which == "sea" else "#C8281E"
        o.append(lion_walk(x, y, s * 1.2, color=col))
        if which == "sea":
            r = random.Random(7)
            o.append("".join(f'<circle cx="{f(x + r.uniform(-44, 14) * s * 1.2)}" cy="{f(y - r.uniform(18, 36) * s * 1.2)}" r="{f(2.6 * s)}" fill="#3A2210"></circle>' for _ in range(16)))
            o.append("".join(f'<ellipse cx="{f(x + dx * s * 1.2)}" cy="{f(y - 2 * s)}" rx="{f(7 * s)}" ry="{f(4 * s)}" fill="#5A3A22" stroke="#0D0D0F" stroke-width="1.2"></ellipse>' for dx in (-30, -21, 27, 36)))
        o.append(_heads(x + 52 * s * 1.2, y - 40 * s * 1.2, s * 1.0, color=col))
        if cup_: o.append(cup(w * 0.8, h * 0.84, s * 0.7, spill=False))
        tx = w * 0.68
        if which == "sea":
            o.append(tag(x - 10 * s, y - 30 * s, "LIKE UNTO A LEOPARD", tx, h * 0.62))
            o.append(tag(x - 36 * s, y - 2 * s, "THE FEET OF A BEAR", tx, h * 0.76))
            o.append(tag(x + 100 * s, y - 70 * s, "SEVEN HEADS · TEN HORNS", tx, h * 0.2))
            o.append(tag(x + 66 * s, y - 92 * s, "TEN DIADEMS", tx, h * 0.27))
            o.append(tag(x + 92 * s, y - 50 * s, "THE MOUTH AS OF A LION", tx, h * 0.34))
            o.append(label(w * 0.04, h * 0.12, "THE BEAST OUT OF THE SEA", "#FFD23F", max(9, min(11, h / 22)), anchor="start"))
        else:
            o.append(tag(x - 10 * s, y - 30 * s, "SCARLET-COLORED", w * 0.62, h * 0.94))
            o.append(tag(x + 100 * s, y - 70 * s, "SEVEN HEADS · TEN HORNS", tx, h * 0.24))
            if cup_: o.append(tag(w * 0.8, h * 0.84 - 60 * s, "A GOLDEN CUP", w * 0.8, h * 0.44))
            o.append(label(w * 0.04, h * 0.12, "THE SCARLET-COLORED BEAST", "#FFD23F", max(9, min(11, h / 22)), anchor="start"))
    else:
        o.append(lion_walk(x, y, s * 1.2, color="#8A6A4A"))
        hx, hy = x + 60 * s * 1.2, y - 50 * s * 1.2
        o.append("".join(f'<path d="M{f(hx + d * 6 * s)} {f(hy - 2 * s)} C {f(hx + d * 14 * s)} {f(hy - 14 * s)} {f(hx + d * 20 * s)} {f(hy - 4 * s)} {f(hx + d * 14 * s)} {f(hy + 2 * s)}" fill="none" stroke="#E8E2D6" stroke-width="{f(4 * s)}" stroke-linecap="round"></path>' for d in (-1, 1)))
        o.append(tag(hx, hy - 8 * s, "TWO HORNS LIKE UNTO A LAMB", w * 0.66, h * 0.26))
        o.append(tag(x - 10 * s, y - 30 * s, "COMING UP OUT OF THE EARTH", w * 0.66, h * 0.6))
        o.append(label(w * 0.04, h * 0.12, "ANOTHER BEAST", "#FFD23F", max(9, min(11, h / 22)), anchor="start"))
    return "".join(o)

def months(w, h, n=42, title="FORTY AND TWO MONTHS"):
    """A span of time as a plate: n cells in rows, the count at the foot."""
    from epistle import plate_bg
    o = [plate_bg(w, h, title)]
    cols = 14 if n == 42 else 12
    rows_ = math.ceil(n / cols)
    cw, ch = (w - 40) / cols, min((h - 80) / rows_, 40)
    for i in range(n):
        x = 20 + (i % cols) * cw; y = 40 + (i // cols) * ch
        o.append(f'<rect x="{f(x + 3)}" y="{f(y + 3)}" width="{f(cw - 6)}" height="{f(ch - 6)}" fill="#12223A" stroke="#8FD0E2" stroke-width="1.2"></rect>'
                 + label(x + cw / 2, y + ch / 2 + 4, str(i + 1), "#FFD23F", max(7, min(10, ch / 3))))
    return "".join(o)

def emblem_sword(w, h, seed):
    """If any man is for captivity … with the sword (13:10): a chain and a sword in its sheath crossed in a medallion."""
    inner = ('<path d="M-0.5 0.5 L 0.5 -0.5" stroke="#5A3A22" stroke-width="0.14" stroke-linecap="round"></path>'
             '<path d="M-0.36 0.24 L -0.24 0.36" stroke="#C8962E" stroke-width="0.08"></path>'
             + "".join(f'<ellipse cx="{f(0.5 - k * 0.17)}" cy="{f(0.5 - k * 0.17)}" rx="0.09" ry="0.05" transform="rotate(45 {f(0.5 - k * 0.17)} {f(0.5 - k * 0.17)})" fill="none" stroke="#B8C0C8" stroke-width="0.035"></ellipse>' for k in range(7)))
    return emblem_plate(w, h, seed, inner, bg=("#1A1A2A", "#3A3A4A"))

def image(p, w, h, seed):
    """The image of the beast (13:14–15): a great image on a pedestal in a square, under a dark sky, crowds far off bowed
    before it (no one killed is drawn)."""
    r = random.Random(seed)
    o = [defs(p), sky(w, h, "#1A1418", "#6A4A3A")]
    hz = h * 0.7
    o.append(houses(-10, w * 0.3, hz, h * 0.24, seed) + houses(w * 0.7, w + 10, hz, h * 0.24, seed + 1))
    o.append(f'<rect x="-10" y="{f(hz)}" width="{f(w + 20)}" height="{f(h)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2"></rect>')
    cx = w * 0.5; s = h * 0.5 / 64
    o.append(f'<rect x="{f(cx - 24 * s * 0.6)}" y="{f(hz - 20 * s * 0.6)}" width="{f(48 * s * 0.6)}" height="{f(20 * s * 0.6)}" fill="#5A4A3A" stroke="{INK}" stroke-width="2"></rect>')
    o.append(idol(cx, hz - 20 * s * 0.6, s * 1.1, color="#C8A040"))
    for i in range(8):
        x = w * (0.1 + 0.8 * i / 7)
        if abs(x - cx) < w * 0.12: continue
        c = r.choice(["#5A4A3A", "#3A3A4A", "#4A3A3A", "#5A3A4A"])
        o.append(elder_bow(x, h * 0.9 + (i % 2) * 5, h * 0.15 / 120, flip=x > cx, crown_cast=False, robe=c, legs=c, hair=r.choice(["#1A1210", "#3A2214"])))
    return "".join(o)

def mark_plate(w, h):
    """The mark (13:16–18) as a technical plate: a right hand and a forehead in outline, each with the place of the mark;
    buying and selling shut to all without it; the number of his name."""
    import exo.art8 as B
    from epistle import plate_bg
    o = [plate_bg(w, h, "THE MARK · THE NAME OF THE BEAST · THE NUMBER OF HIS NAME")]
    B._W[0] = w
    full_h = h
    y0 = max(0.0, (h - w * 0.5) / 2); h = min(h, w * 0.5)                 # a tall panel: the plate's parts kept in a band at its middle
    o.append(f'<g transform="translate(0 {f(y0)})">')
    s = min(h / 260, w / 700)
    hx, hy = w * 0.16, h * 0.62
    o.append(f'<g transform="translate({f(hx)} {f(hy)}) scale({f(s * 1.4)})"><path d="M-30 60 L -30 -10 C -34 -30 -40 -50 -36 -60 C -32 -66 -26 -62 -24 -54 L -18 -24 L -16 -80 C -16 -88 -6 -88 -6 -80 '
             'L -4 -30 L -2 -90 C -2 -98 8 -98 8 -90 L 10 -30 L 12 -80 C 12 -88 22 -88 22 -80 L 22 -26 L 26 -60 C 26 -68 36 -68 36 -60 L 34 -10 C 34 10 26 30 26 60 Z" '
             'fill="none" stroke="#8FD0E2" stroke-width="2"></path><circle cx="0" cy="10" r="10" fill="none" stroke="#FF6A4A" stroke-width="2.4" stroke-dasharray="4 3"></circle></g>')
    fx, fy = w * 0.36, h * 0.58
    o.append(f'<g transform="translate({f(fx)} {f(fy)}) scale({f(s * 1.4)})"><path d="M-30 70 C -34 30 -40 0 -36 -30 C -30 -70 20 -76 34 -40 C 38 -30 38 -20 36 -12 L 46 8 C 48 12 44 14 40 14 L 40 22 C 42 26 38 28 34 28 L 32 36 C 28 44 16 44 6 42 L 4 70" '
             'fill="none" stroke="#8FD0E2" stroke-width="2"></path><circle cx="14" cy="-40" r="10" fill="none" stroke="#FF6A4A" stroke-width="2.4" stroke-dasharray="4 3"></circle></g>')
    o.append(label(hx, h * 0.94, "ON THEIR RIGHT HAND", "#FFD23F", 9) + label(fx, h * 0.94, "OR UPON THEIR FOREHEAD", "#FFD23F", 9))
    o.append(f'<text x="{f(w * 0.72)}" y="{f(h * 0.66)}" text-anchor="middle" font-family="Anton, sans-serif" font-size="{f(min(h * 0.4, w * 0.16))}" fill="none" stroke="#FF6A4A" stroke-width="2.6">666</text>')
    o.append(label(w * 0.72, h * 0.8, "SIX HUNDRED AND SIXTY AND SIX", "#FFD23F", 9) + label(w * 0.72, h * 0.88, "THE NUMBER OF A MAN", "#8FD0E2", 9))
    o.append(label(w * 0.72, h * 0.2, "NO MAN ABLE TO BUY OR TO SELL", "#8FD0E2", 9))
    return "".join(o) + "</g>"

def zion(p, w, h, seed):
    """The Lamb standing on the mount Zion, and with him a hundred and forty and four thousand (14:1–3): the mount in light,
    the Lamb upon its height, the sealed in white about him row on row, harps among them."""
    r = random.Random(seed)
    o = [defs(p), sky(w, h, "#2A3A7A", "#FFE6B0"), halo(w * 0.5, h * 0.2, w * 0.5, WHITE, 0.85), rays(w * 0.5, h * 0.2, 30, h * 0.08, w, "#FFFDF0", 0.35, 4)]
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.8)} C {f(w * 0.2)} {f(h * 0.6)} {f(w * 0.36)} {f(h * 0.36)} {f(w * 0.5)} {f(h * 0.34)} C {f(w * 0.64)} {f(h * 0.36)} {f(w * 0.8)} {f(h * 0.6)} {f(w + 10)} {f(h * 0.8)} L {f(w + 10)} {f(h + 10)} Z" '
             f'fill="#9A8A6A" stroke="{INK}" stroke-width="2.4"></path>')
    o.append(lamb(w * 0.5 - 20 * h / 500, h * 0.36, h * 0.16 / 90))
    for row in range(4):
        k = 0.3 + row * 0.16; n = 9 + row * 3
        b = h * (0.52 + row * 0.13); s = h * 0.3 * k / 205
        span = 0.24 + row * 0.18
        for i in range(n):
            x = w * (0.5 - span + 2 * span * (i + 0.5) / n) + r.uniform(-4, 4)
            hp = r.random() < 0.35
            o.append(robed(p, x, b, s, "#FFFFFF", skin=r.choice(["#C98E66", "#D9A27A", "#A8704E", "#8A5A3A"]), hair=r.choice(["#1A1210", "#3A2214", "#5A3A22"]),
                           woman=False, flip=x > w * 0.5, line="#3A3A4A", up=UP_HARP if hp else None, extra=harp(-50, -112, 0.9) if hp else ""))
    o.append(label(w * 0.5, h * 0.97, "A HUNDRED AND FORTY AND FOUR THOUSAND", "#3A2A1A", max(8, min(10, h / 26))))
    return "".join(o)

def firstfruits(w, h):
    """The firstfruits unto God and unto the Lamb (14:4–5): 144 marks, each a thousand, in twelve rows of twelve."""
    from epistle import plate_bg
    o = [plate_bg(w, h, "FIRSTFRUITS UNTO GOD AND UNTO THE LAMB")]
    gx0, gy0 = w * 0.06, 40; cw = (w * 0.56) / 12; ch = (h - 70) / 12
    for i in range(144):
        x = gx0 + (i % 12) * cw + cw / 2; y = gy0 + (i // 12) * ch + ch / 2
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(min(cw, ch) * 0.3)}" fill="#F3EFE6" stroke="#E8B830" stroke-width="1"></circle>')
    o.append(label(w * 0.8, h * 0.42, "144 × 1,000", "#FFD23F", max(12, min(22, h / 10))) + label(w * 0.8, h * 0.56, "= 144,000", "#F3EFE6", max(10, min(16, h / 14))))
    o.append(label(w * 0.8, h * 0.72, "PURCHASED FROM AMONG MEN", "#8FD0E2", 9))
    return "".join(o)

def flying(p, w, h, seed, which="first"):
    """An angel flying in mid heaven (14:6–11): a figure of light high over the earth, arms out, streaks of light behind.
    "first": over the nations, morning; "second": Babylon the great fallen far off on the horizon, smoke over it; "third":
    far off, the smoke of fire and brimstone going up from a burning place (no one drawn in it)."""
    tones = {"first": ("#3A6AB0", "#F3E8C8"), "second": ("#3A2A4A", "#C8885A"), "third": ("#1A0A0A", "#7A2A1A")}
    o = [defs(p), sky(w, h, *tones[which])]
    hz = h * 0.76
    o.append(hills(w, h, hz, seed, color={"first": "#7A9A6A", "second": "#4A3A3A", "third": "#2A1414"}[which], amp=12, step=90))
    o.append(ground(w, h, hz + h * 0.06, {"first": "#9AA86A", "second": "#5A4A3A", "third": "#2A1A14"}[which], dy=0))
    if which == "first":
        o.append(houses(w * 0.05, w * 0.3, hz + h * 0.06, h * 0.08, seed) + houses(w * 0.66, w * 0.94, hz + h * 0.06, h * 0.08, seed + 1))
    if which == "second":
        o.append(ruin(w * 0.56, w * 0.92, hz + h * 0.06, h * 0.12, seed) + smoke(w * 0.72, hz - h * 0.02, 8, seed, color="#3A2A2E", op=0.6, k=h / 300))
    if which == "third":
        o.append(fires(w * 0.55, w * 0.95, hz + h * 0.08, h * 0.12, seed, n=4) + smoke(w * 0.72, hz - h * 0.04, 10, seed, color="#1A1010", op=0.7, k=h / 260))
    x, y = w * 0.3, h * 0.6; s = h * 0.44 / 205
    for k in range(4):
        o.append(f'<path d="M{f(x - 30 * s - k * 30)} {f(y - 100 * s + k * 12)} L {f(x - 160 * s - k * 40)} {f(y - 90 * s + k * 16)}" stroke="#FFF4C2" stroke-width="3" opacity="{0.7 - k * 0.15:.2f}"></path>')
    o.append(angel(p, x, y, s, up=[(-22, -158), (-50, -168), (-76, -176)], flip=True))
    return "".join(o)

def tombs_dawn(w, h, seed):
    """Blessed are the dead who die in the Lord (14:13): tombs hewn in a garden hillside at dawn, their stones rolled to,
    quiet, the light rising."""
    o = [sky(w, h, "#3A3A7A", "#FFD8A0"), halo(w * 0.78, h * 0.62, h * 0.5, "#FFF4C2", 0.8)]
    o.append(f'<path d="M-10 {f(h * 0.36)} C {f(w * 0.2)} {f(h * 0.3)} {f(w * 0.4)} {f(h * 0.4)} {f(w * 0.6)} {f(h * 0.62)} L {f(w * 0.6)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>')
    for i, (x, y) in enumerate(((0.1, 0.58), (0.26, 0.6), (0.42, 0.7))):
        cw, ch = w * 0.045, h * 0.12
        o.append(f'<path d="M{f(w * x - cw)} {f(h * y)} L {f(w * x - cw)} {f(h * y - ch * 0.6)} A {f(cw)} {f(cw)} 0 0 1 {f(w * x + cw)} {f(h * y - ch * 0.6)} L {f(w * x + cw)} {f(h * y)} Z" fill="#2A1E18" stroke="{INK}" stroke-width="2"></path>'
                 f'<circle cx="{f(w * x + cw * 1.3)}" cy="{f(h * y - cw * 0.9)}" r="{f(cw * 0.95)}" fill="#A89A8A" stroke="{INK}" stroke-width="2"></circle>')
    o.append(ground(w, h, h * 0.86, "#7A9A5A", dy=0))
    for x in (0.7, 0.84, 0.94): o.append(olive(w * x, h * 0.96, h / 420, seed=int(x * 100)))
    return "".join(o)

UP_SICKLE = [(-22, -158), (-46, -160), (-62, -172)]
SICKLE = ('<path d="M-62 -172 L -62 -150" stroke="#6A4A2A" stroke-width="4"></path>'
          '<path d="M-62 -172 C -66 -196 -90 -204 -104 -190 C -92 -196 -76 -190 -70 -172 Z" fill="#C8CCD4" stroke="#0D0D0F" stroke-width="1.6"></path>')

def harvest(p, w, h, seed, stage="cloud"):
    """The harvest of the earth (14:14–20). "cloud": a white cloud, and upon it one sitting like unto a son of man (ntcast's
    Jesus, risen, in light), a golden crown upon his head and a sharp sickle in his hand, the ripe wheat below, an angel
    out of the temple crying to him; "vine": an angel of light with a sharp sickle over the vine of the earth, another from
    the altar calling; "press": the great winepress trodden without the city — the press of stone on an empty plain at a red
    dusk, the city walls far off; nothing else drawn (what came out of it is in the words)."""
    o = [defs(p)]
    if stage == "cloud":
        o += [sky(w, h, "#5A8AC8", "#F3E8C8"), halo(w * 0.42, h * 0.3, w * 0.4, WHITE, 0.8)]
        hz = h * 0.7
        o.append(ground(w, h, hz, "#C8A050", dy=0) + grain(-10, w + 10, hz + h * 0.14, h * 0.1, seed) + grain(-10, w + 10, h * 0.99, h * 0.16, seed + 1))
        cx, cy = w * 0.42, h * 0.5
        for dx, dy, rr in ((-70, 0, 60), (0, 10, 70), (70, 0, 60), (-30, -16, 50), (40, -14, 50)):
            o.append(f'<ellipse cx="{f(cx + dx * h / 300)}" cy="{f(cy + dy * h / 300)}" rx="{f(rr * h / 300)}" ry="{f(rr * 0.42 * h / 300)}" fill="#FFFFFF" stroke="#B8C0D8" stroke-width="2"></ellipse>')
        s = h * 0.36 / 157
        crown = '<path d="M-13 -197 L -14 -210 L -7 -203 L 0 -214 L 7 -203 L 14 -210 L 13 -197 Z" fill="#FFD23F" stroke="#0D0D0F" stroke-width="1.4"></path>'
        o.append(halo(cx, cy - 80 * s, 120 * s, WHITE, 0.9))
        o.append(robed(p, cx + 10 * s, cy + 6 * h / 300, s, WHITE, skin=JESUS_SKIN, mantle="#C8D2E6", up=UP_SICKLE, pose="sit", seat=None,
                       extra=_HAIR_FIG + _BEARD_FIG + crown + SICKLE))
        o.append(angel(p, w * 0.86, h * 0.56, h * 0.4 / 205, up=[(-22, -158), (-40, -176), (-56, -192)], flip=False))
        return "".join(o)
    if stage == "vine":
        o += [sky(w, h, "#5A4A8A", "#E8C8A0"), halo(w * 0.3, h * 0.24, w * 0.3, "#FFF4C2", 0.7)]
        hz = h * 0.6
        o.append(hills(w, h, hz - h * 0.04, seed, color="#7A6A5A", amp=10, step=90) + ground(w, h, hz, "#8A7A4A", dy=0))
        o.append(vines(w * 0.04, w * 0.96, hz + h * 0.12, h * 0.96, seed, rows=3))
        o.append(angel(p, w * 0.3, h * 0.5, h * 0.42 / 205, up=UP_SICKLE, flip=True, extra=SICKLE))
        flame = ('<path d="M-56 -224 C -46 -212 -46 -200 -56 -194 C -66 -200 -66 -212 -56 -224 Z" fill="#FF8A2E" stroke="#C8401A" stroke-width="1.4"></path>'
                 '<path d="M-56 -214 C -52 -208 -52 -202 -56 -199 C -60 -202 -60 -208 -56 -214 Z" fill="#FFF4C2"></path>')
        o.append(angel(p, w * 0.78, h * 0.46, h * 0.36 / 205, up=[(-22, -158), (-40, -176), (-56, -192)], extra=flame))
        return "".join(o)
    o += [sky(w, h, "#2A0A10", "#C8502A"), halo(w * 0.2, h * 0.62, h * 0.4, "#FF6A2A", 0.5)]
    hz = h * 0.62
    o.append(walls(w * 0.62, w * 0.96, hz + h * 0.02, h * 0.14, seed, color="#6A4A3A", towers=2))
    o.append(ground(w, h, hz, "#5A3A2A", dy=0))
    px, pw = w * 0.32, w * 0.24
    o.append(f'<path d="M{f(px - pw / 2)} {f(h * 0.86)} L {f(px - pw / 2)} {f(h * 0.74)} L {f(px + pw / 2)} {f(h * 0.74)} L {f(px + pw / 2)} {f(h * 0.86)} Z" fill="#7A6A5A" stroke="{INK}" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(px)}" cy="{f(h * 0.74)}" rx="{f(pw / 2)}" ry="{f(h * 0.03)}" fill="#3A1A1A" stroke="{INK}" stroke-width="2"></ellipse>'
             f'<rect x="{f(px + pw / 2)}" y="{f(h * 0.82)}" width="{f(w * 0.06)}" height="{f(h * 0.05)}" fill="#6A5A4A" stroke="{INK}" stroke-width="2"></rect>')
    o.append(label(w * 0.04, h * 0.94, "WITHOUT THE CITY · A THOUSAND AND SIX HUNDRED FURLONGS", "#F3D8A0", max(8, min(10, h / 26)), anchor="start"))
    return "".join(o)
