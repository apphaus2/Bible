"""Drawings for the Hebrews volume, chapter 1 (Hebrews 1–4). Hebrews starts from Galatians' drawings (`from gal.art import *`,
which carries all of Acts', Mark's and Matthew's drawings and the epistle kit's), takes what it needs from Romans, the
Corinthian letters and the Old Testament volumes, and adds its own.

No writer is drawn. God is never drawn: light, a throne standing empty in light, the Voice box. Angels are figures of white
light with a gold rim and no face (gal.art.light_fig, no wings: the text gives none). Jesus, where drawn, is the risen
Christ in white light (co1.art5.risen_fig). Every function takes (p, w, h, seed, ...) or (w, h, ...); p, a prefix unique to
the panel, names its figure defs and gradients."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from gal.art import *
from gal.art import art, plate_label, _defs, f, INK
from co1.art5 import risen_fig
from act.art4 import ot, throne_footstool
import mk

GOLD, CY, CREAM = "#FFD23F", "#8FD0E2", "#F3EFE6"

def defs_up(p): return mk.defs(p, *ALL, "ManUp", "WomanUp")

def angel_fig(p, x, y, s, flip=False, up=None, pose="stand"):
    """An angel: a figure of white light with a gold rim and no face (no wings: the text gives none), drawn on the kit's
    figure (epistle.robed) so the shoulders, arms and waist show, a soft light about it. Needs defs_up(p) in the panel."""
    return (f'<ellipse cx="{f(x)}" cy="{f(y - 105 * s)}" rx="{f(70 * s)}" ry="{f(125 * s)}" fill="#FFF4C2" opacity="0.4"></ellipse>'
            + robed(p, x, y, s, "#FFFFFF", skin="#FFFDF0", line="#E8B830", mantle="#FFF8E0", flip=flip, up=up, pose=pose))

def tag(x, y, text, tx, ty, color=CY, size=9, fit=False):
    """A callout (exo.art8.tag) whose label is kept inside the plate by its true width (the letter-spaced mono type runs
    about 0.8 em a letter); fit=True: a translation longer than the room left to the plate's edge is shrunk to it."""
    import exo.art8 as B
    est = len(text) * size * 0.8; right = tx >= x; W = B._W[0]
    if right and tx + 4 + est > W - 8: tx = W - 12 - est
    if not right and tx - 4 - est < 8: tx = 12 + est
    return (f'<circle cx="{f(x)}" cy="{f(y)}" r="3" fill="{color}"></circle><path d="M{f(x)} {f(y)} L {f(tx)} {f(ty)}" stroke="{color}" stroke-width="1.2"></path>'
            + label(tx + (4 if right else -4), ty + 3, text, color, size, "start" if right else "end",
                    fit=(W - 8 - tx - 4 if right else tx - 4 - 8) if fit else None))

# ---- small things shared by the volume ------------------------------------------------------------------------------------
def throne_of_light(cx, base, s, uid, lit=1.0):
    """A throne standing empty in light (God is never drawn): a high-backed seat of white and gold on three steps, a glow
    and rays about it; (cx, base) the middle of the lowest step, about 300 units tall at s = 1."""
    o = [glow(cx, base - 170 * s, 260 * s, "#FFFFFF", 0.85 * lit, f"{uid}g"), rays(cx, base - 170 * s, 36, 60 * s, 420 * s, "#FFF4C2", 0.3 * lit, 4)]
    for k, (wd, hh) in enumerate(((220, 22), (180, 22), (140, 22))):          # the steps
        y = base - 22 * k * s
        o.append(f'<rect x="{f(cx - wd / 2 * s)}" y="{f(y - hh * s)}" width="{f(wd * s)}" height="{f(hh * s)}" fill="#FFF8DC" stroke="#C8962A" stroke-width="{f(max(1.4, 2.4 * s))}"></rect>')
    y0 = base - 66 * s
    o.append(f'<path d="M{f(cx - 56 * s)} {f(y0)} L {f(cx - 56 * s)} {f(y0 - 230 * s)} C {f(cx - 50 * s)} {f(y0 - 262 * s)} {f(cx + 50 * s)} {f(y0 - 262 * s)} {f(cx + 56 * s)} {f(y0 - 230 * s)} '
             f'L {f(cx + 56 * s)} {f(y0)} Z" fill="#FFFBEA" stroke="#C8962A" stroke-width="{f(max(1.6, 3 * s))}"></path>'
             f'<path d="M{f(cx - 40 * s)} {f(y0 - 90 * s)} L {f(cx - 40 * s)} {f(y0 - 214 * s)} C {f(cx - 34 * s)} {f(y0 - 240 * s)} {f(cx + 34 * s)} {f(y0 - 240 * s)} {f(cx + 40 * s)} {f(y0 - 214 * s)} L {f(cx + 40 * s)} {f(y0 - 90 * s)} Z" '
             f'fill="#FFE9A8" stroke="#E8B830" stroke-width="{f(max(1, 1.6 * s))}"></path>'
             f'<rect x="{f(cx - 78 * s)}" y="{f(y0 - 96 * s)}" width="{f(156 * s)}" height="{f(26 * s)}" fill="#FFF8DC" stroke="#C8962A" stroke-width="{f(max(1.4, 2.6 * s))}"></rect>'
             f'<rect x="{f(cx - 70 * s)}" y="{f(y0 - 70 * s)}" width="{f(140 * s)}" height="{f(70 * s)}" fill="#FFF1C4" stroke="#C8962A" stroke-width="{f(max(1.4, 2.6 * s))}"></rect>')
    for sg in (-1, 1):                                                        # the arms
        o.append(f'<path d="M{f(cx + sg * 78 * s)} {f(y0 - 96 * s)} L {f(cx + sg * 78 * s)} {f(y0 - 150 * s)} C {f(cx + sg * 80 * s)} {f(y0 - 166 * s)} {f(cx + sg * 64 * s)} {f(y0 - 170 * s)} {f(cx + sg * 56 * s)} {f(y0 - 160 * s)}" '
                 f'fill="none" stroke="#C8962A" stroke-width="{f(max(2, 5 * s))}" stroke-linecap="round"></path>')
    o.append(glow(cx, base - 150 * s, 120 * s, "#FFFFFF", 0.55 * lit, f"{uid}h"))
    return "".join(o)

def cloud_bank(w, y, seed, color="#FFFDF0", op=0.9, k=1.0, base=True):
    """A bank of round-topped cloud across the panel at height y."""
    r = random.Random(seed); o = []; x = -30
    while x < w + 30:
        rr = r.uniform(26, 48) * k
        o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rr)}" fill="{color}" opacity="{op}"></circle>'); x += rr * 1.2
    if base: o.append(f'<rect x="-10" y="{f(y)}" width="{f(w + 20)}" height="{f(60 * k)}" fill="{color}" opacity="{op}"></rect>')
    return "".join(o)

def face_cell(tok, x, y, w, h, uid, light="#FFE680", ground=("#2A2440", "#8A5A4A"), name=None):
    """A portrait cell: a shaded profile face (a faces.face token) looking right over a soft light, framed; name a label across
    its top."""
    s = min(w / 300, (h + 10) / 380)
    o = [f'<defs><radialGradient id="{uid}" cx="0.7" cy="0.3" r="0.9"><stop offset="0" stop-color="{light}"></stop><stop offset="0.45" stop-color="{ground[1]}"></stop>'
         f'<stop offset="1" stop-color="{ground[0]}"></stop></radialGradient><clipPath id="{uid}c"><rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}"></rect></clipPath></defs>',
         f'<g clip-path="url(#{uid}c)"><rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="url(#{uid})"></rect>',
         f'<g transform="translate({f(x + w / 2 - 170 * s)} {f(y + h - 380 * s + 6)})">' + mk.face(tok, 0, 0, round(s, 3)) + '</g></g>',
         f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="none" stroke="{INK}" stroke-width="3"></rect>']
    if name:
        o.append(f'<rect x="{f(x)}" y="{f(y + 3)}" width="{f(w)}" height="20" fill="#0D0D0F" opacity="0.72"></rect>'      # the name across the top, clear of the verse ref
                 + label(x + w / 2, y + 17, name, GOLD, 9))
    return "".join(o)

# ---- the opening ----------------------------------------------------------------------------------------------------------
def bearer(p, x, y, s, flip=False):
    """The letter's bearer on the road: a traveller in a grey-blue cloak and a dark headcloth, a staff, the sealed scroll in
    his hand."""
    return robed(p, x, y, s, "#4A5A6A", head="#1F2A3A", cord="#0D1A2A", beard="#2A1A10", mantle="#2A3444", belt="#6A4A2A", flip=flip,
                 up=[(-22, -158), (-40, -126), (-56, -112)], extra=sealed_scroll(-60, -112, 0.3, rot=-20), pose="walk")

def letter_road(p, w, h, seed, dawn=True):
    """The letter carried: a road climbing through the hills at dawn to a walled city on its hill, the bearer walking it with
    the sealed scroll in his hand."""
    b = h * 0.95
    o = [_defs(p), sky(w, h, "#2A2A5A", "#FFB07A") if dawn else sky(w, h, "#8FD0E2", "#F3E8C8"), halo(w * 0.78, h * 0.42, h * 0.4, "#FFD08A", 0.55),
         f'<circle cx="{f(w * 0.78)}" cy="{f(h * 0.42)}" r="{f(max(10, h * 0.05))}" fill="#FFE6A0"></circle>',
         hills(w, h, h * 0.52, seed, color="#5A3A4A", amp=16, step=90), town_hill(w * 0.74, h * 0.6, w * 0.34, h * 0.2, seed, color="#7A5A4A", lit=True),
         hills(w, h, h * 0.66, seed + 1, color="#6A4A3A", amp=12, step=70), ground(w, h, h * 0.74, "#8A6A4A", dy=0)]
    o.append(f'<path d="M{f(w * 0.08)} {f(h + 10)} C {f(w * 0.3)} {f(h * 0.86)} {f(w * 0.5)} {f(h * 0.8)} {f(w * 0.66)} {f(h * 0.74)} L {f(w * 0.7)} {f(h * 0.74)} '
             f'C {f(w * 0.58)} {f(h * 0.82)} {f(w * 0.46)} {f(h * 0.9)} {f(w * 0.36)} {f(h + 10)} Z" fill="#C8A878" stroke="{INK}" stroke-width="2"></path>')
    s = fit(b, max(h * 0.3, b - 230))
    o.append(bearer(p, w * 0.3, b, s, flip=True))
    return "".join(o)

def prophets(w, h):
    """God spake of old time unto the fathers in the prophets, by divers portions and in divers manners: a strip of portrait
    cells — Moses, Samuel's successor prophets as their volumes draw them: Elijah, Isaiah, Jeremiah, Ezekiel, Daniel, Hosea,
    Amos — each a shaded profile face looking right (toward the next panel, the Son), named under it."""
    from exo.art import MOSES
    from kg1.common import ELIJAH
    from kg2.common import ISAIAH
    from jer.common import jer
    from ezk.common import EZEKIEL
    from dan.common import DANIEL_OLD
    from hos.common import HOSEA
    from amo.common import AMOS
    people = [(MOSES, "MOSES"), (ELIJAH, "ELIJAH"), (ISAIAH, "ISAIAH"), (jer(2, "calm"), "JEREMIAH"), (EZEKIEL, "EZEKIEL"), (DANIEL_OLD, "DANIEL"),
              (HOSEA, "HOSEA"), (AMOS, "AMOS")]
    n = 4 if w < 520 or h > w * 0.62 else 8
    rows = 2 if n == 4 else 1
    cw, chh = w / n if rows == 1 else w / 4, h / rows
    lights = ["#FFE680", "#FFC14D", "#FFE680", "#CFE0FF", "#FFB04A", "#FFF4C2", "#FFE680", "#FFC14D"]
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="#1A1028"></rect>']
    for i, (tok, nm) in enumerate(people[:n * rows] if rows == 1 else people):
        cx, cy = (i % 4) * cw if rows == 2 else i * cw, (i // 4) * chh if rows == 2 else 0
        o.append(face_cell(tok, cx, cy, cw, chh, f"pr{i}", light=lights[i], name=nm))
    return "".join(o)

def majesty(p, w, h, seed):
    """The effulgence of his glory, upholding all things by the word of his power; sat down on the right hand of the Majesty
    on high: the round of the earth in the dark among the stars (the worlds), and high above it a great light and a throne
    standing empty in it on a bank of cloud — no figure."""
    o = [sky(w, h, "#05051A", "#2A2050"), starfield(w, h, seed, 90, 0.95)]
    R = w * 0.9
    o.append(f'<defs><radialGradient id="{p}e" cx="0.5" cy="0.1" r="0.7"><stop offset="0" stop-color="#5A9AD0"></stop><stop offset="0.5" stop-color="#1F4A7A"></stop><stop offset="1" stop-color="#0B1A2E"></stop></radialGradient></defs>'
             f'<circle cx="{f(w * 0.5)}" cy="{f(h * 0.86 + R)}" r="{f(R)}" fill="url(#{p}e)" stroke="#8FD0E2" stroke-width="2"></circle>'
             f'<path d="M{f(w * 0.12)} {f(h * 0.95)} C {f(w * 0.24)} {f(h * 0.9)} {f(w * 0.34)} {f(h * 0.92)} {f(w * 0.42)} {f(h * 0.9)} L {f(w * 0.46)} {f(h + 10)} L {f(w * 0.08)} {f(h + 10)} Z" fill="#3A6A3A" opacity="0.8"></path>'
             f'<path d="M{f(w * 0.6)} {f(h * 0.9)} C {f(w * 0.7)} {f(h * 0.88)} {f(w * 0.8)} {f(h * 0.92)} {f(w * 0.9)} {f(h * 0.96)} L {f(w * 0.92)} {f(h + 10)} L {f(w * 0.58)} {f(h + 10)} Z" fill="#6A7A3A" opacity="0.8"></path>')
    o.append(rays(w * 0.5, h * 0.3, 48, h * 0.06, max(w, h) * 1.1, "#FFE680", 0.2, 4))
    s = min(h * 0.42 / 300, w * 0.3 / 220)
    o.append(f'<g transform="translate({f(w * 0.15)} 0)">' + cloud_bank(w * 0.7, h * 0.52, seed, "#FFF4C2", 0.6, k=min(1.0, h / 360), base=False) + '</g>')
    o.append(throne_of_light(w * 0.5, h * 0.54, s, f"{p}t"))
    return "".join(o)

def angels_worship(p, w, h, seed):
    """Let all the angels of God worship him: the throne in light high at the right, and coming toward it in rows across the
    clouds the angels, figures of white light with gold rims and no faces, their arms lifted."""
    o = [defs_up(p), sky(w, h, "#1A1440", "#C8A0D8"), starfield(w, h, seed, 30, 0.4)]
    o.append(cloud_bank(w, h * 0.86, seed, "#FFF4E8", 0.8, k=min(1.0, h / 300)))
    s0 = min(h * 0.5 / 300, w * 0.24 / 220)
    o.append(throne_of_light(w * 0.82, h * 0.62, s0, f"{p}t"))
    b = h * 0.92
    for row, (k, y0) in enumerate(((0.55, h * 0.74), (0.75, h * 0.84), (0.95, b))):
        s = fit(b, b - 210) * k * min(1.0, h / 300)
        n = 5 - row
        for i in range(n):
            x = w * (0.06 + 0.13 * i + 0.05 * row)
            o.append(angel_fig(p, x, y0, s, flip=True, up=[(-22, -158), (-34, -190), (-40, -222)]))
    return "".join(o)

def wind_fire(p, w, h, seed):
    """Who maketh his angels winds, and his ministers a flame of fire: a wind sweeping over the hills, the grass and the trees
    bowed by it; and in a flame of fire on the height a figure of white light with a gold rim, no face."""
    r = random.Random(seed)
    o = [_defs(p), sky(w, h, "#2A1A3A", "#E8803A"), hills(w, h, h * 0.62, seed, color="#3A2A3A", amp=14, step=80), ground(w, h, h * 0.76, "#4A3A2E", dy=0)]
    for i in range(14):                                                       # the wind
        y = h * r.uniform(0.08, 0.7); x0 = w * r.uniform(-0.2, 0.5); L = w * r.uniform(0.3, 0.6)
        o.append(f'<path d="M{f(x0)} {f(y)} C {f(x0 + L * 0.3)} {f(y - 18)} {f(x0 + L * 0.6)} {f(y + 14)} {f(x0 + L)} {f(y - 4)} c 14 -6 18 -20 6 -24" fill="none" stroke="#FFF4E8" stroke-width="{f(r.uniform(1.4, 3))}" opacity="0.55" stroke-linecap="round"></path>')
    for i in range(3):                                                        # trees bowed
        x = w * (0.08 + 0.14 * i); k = min(1.0, h / 320)
        o.append(f'<path d="M{f(x)} {f(h * 0.8)} C {f(x + 8 * k)} {f(h * 0.7)} {f(x + 30 * k)} {f(h * 0.62)} {f(x + 54 * k)} {f(h * 0.58)}" stroke="#2A1A12" stroke-width="{f(6 * k)}" fill="none"></path>'
                 f'<ellipse cx="{f(x + 70 * k)}" cy="{f(h * 0.56)}" rx="{f(44 * k)}" ry="{f(20 * k)}" fill="#3A4A2A" stroke="{INK}" stroke-width="1.6" transform="rotate(14 {f(x + 70 * k)} {f(h * 0.56)})"></ellipse>')
    fx, b = w * 0.72, h * 0.9
    o.append(halo(fx, b - h * 0.3, h * 0.45, "#FF8A3D", 0.5))
    for i in range(9):                                                        # the flame
        x = fx + (i - 4) * w * 0.035; hh = h * (0.5 - abs(i - 4) * 0.07) * r.uniform(0.85, 1.05)
        o.append(f'<path d="M{f(x - w * 0.035)} {f(b)} C {f(x - w * 0.04)} {f(b - hh * 0.5)} {f(x - w * 0.01)} {f(b - hh * 0.7)} {f(x)} {f(b - hh)} C {f(x + w * 0.01)} {f(b - hh * 0.7)} {f(x + w * 0.04)} {f(b - hh * 0.5)} {f(x + w * 0.035)} {f(b)} Z" '
                 f'fill="{["#FF6A2A", "#FFC14D", "#FFE680"][i % 3]}" opacity="0.85"></path>')
    s = fit(b, b - h * 0.5)
    o.append(angel_fig(p, fx, b, s, flip=True, up=[(-22, -158), (-34, -190), (-40, -222)]))
    return "".join(o)

def sceptre_plate(w, h):
    """Thy throne, O God, is for ever and ever; and the sceptre of uprightness is the sceptre of thy kingdom … God, thy God,
    hath anointed thee with the oil of gladness above thy fellows: a technical plate — the sceptre drawn full length, its
    knop and rod tagged; the horn of oil tipped and pouring; and the throne small in light behind them."""
    o = [plate_bg(w, h, "HEBREWS 1:8–9 · THE SCEPTRE OF THY KINGDOM")]
    k = min(w / 700, (h - 30) / 250)
    tc, ts = w * 0.54, min(1.0, (h - 40) / 330)                              # the throne, a little right of the middle
    o.append(throne_of_light(tc, h - 10, ts, "sp", lit=0.6))
    x0, x1, y = w * 0.1, w * 0.9, h * 0.62                                    # the sceptre, laid across
    o.append(f'<rect x="{f(x0)}" y="{f(y - 6 * k)}" width="{f(x1 - x0)}" height="{f(12 * k)}" rx="{f(6 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(x0 + (x1 - x0) * q)}" y="{f(y - 9 * k)}" width="{f(10 * k)}" height="{f(18 * k)}" fill="#FFD23F" stroke="{INK}" stroke-width="1.4"></rect>' for q in (0.2, 0.45, 0.7))
             + f'<circle cx="{f(x1 + 14 * k)}" cy="{f(y)}" r="{f(20 * k)}" fill="#FFD23F" stroke="{INK}" stroke-width="2"></circle>'
             f'<circle cx="{f(x1 + 14 * k)}" cy="{f(y)}" r="{f(9 * k)}" fill="#D7261E" stroke="{INK}" stroke-width="1.4"></circle>')
    o.append(tag(x0 + (x1 - x0) * 0.3, y + 8 * k, "THE SCEPTRE OF UPRIGHTNESS", x0 + 60 * k, y + 60 * k, GOLD, 10))
    o.append(tag(x1 + 14 * k, y - 22 * k, "THE KNOP", x1 - 40 * k, y - 70 * k, CY, 9))
    hx, hy = w * 0.17, h * 0.32                                               # the horn of oil
    o.append(f'<path d="M{f(hx - 50 * k)} {f(hy - 36 * k)} C {f(hx)} {f(hy - 48 * k)} {f(hx + 46 * k)} {f(hy - 14 * k)} {f(hx + 60 * k)} {f(hy + 22 * k)} L {f(hx + 46 * k)} {f(hy + 30 * k)} '
             f'C {f(hx + 32 * k)} {f(hy)} {f(hx)} {f(hy - 18 * k)} {f(hx - 50 * k)} {f(hy - 18 * k)} Z" fill="#E8D8B0" stroke="{INK}" stroke-width="2"></path>'
             + "".join(f'<circle cx="{f(hx + 56 * k + 4 * i * k)}" cy="{f(hy + 44 * k + 18 * i * k)}" r="{f((4 - i * 0.6) * k)}" fill="#FFE680" stroke="#7A5A1A" stroke-width="1"></circle>' for i in range(4))
             + halo(hx + 56 * k, hy + 40 * k, 40 * k, "#FFE680", 0.45))
    o.append(tag(hx + 40 * k, hy - 12 * k, "THE OIL OF GLADNESS", hx + 90 * k, hy - 26 * k, GOLD, 10))   # clear of the title
    o.append(tag(tc + 44 * ts, h - 10 - 266 * ts, "THY THRONE, O GOD · FOR EVER AND EVER", tc + 90 * ts, h * 0.2, CREAM, 9, fit=True))
    return "".join(o)

def rolled_heavens(p, w, h, seed):
    """Thou, Lord, in the beginning didst lay the foundation of the earth, and the heavens are the works of thy hands … as a
    mantle shalt thou roll them up: below, the earth on its foundations (layers of rock under the hills); above, the sky
    full of stars like a cloth being rolled up from the right, the bare light behind it."""
    o = [sky(w, h, "#FFF8DC", "#FFE6A0"), glow(w * 0.8, h * 0.2, h * 0.5, "#FFFFFF", 0.9, f"{p}g")]
    ry = h * 0.56; rx = w * 0.74                                              # the starry cloth, rolled up as far as rx
    o.append(f'<path d="M-10 -10 L {f(rx)} -10 L {f(rx)} {f(ry)} L -10 {f(ry)} Z" fill="#0B0B2A"></path>'
             + mk.stars(int(w * ry / 1400) + 20, int(rx), int(ry), seed))
    o.append(f'<path d="M-10 {f(ry)} C {f(w * 0.2)} {f(ry + 8)} {f(w * 0.5)} {f(ry - 6)} {f(rx)} {f(ry)}" fill="none" stroke="{INK}" stroke-width="2.4"></path>')
    rr = min(w * 0.06, h * 0.08)
    o.append(f'<rect x="{f(rx - rr * 0.2)}" y="-10" width="{f(rr * 1.6)}" height="{f(ry + 10)}" rx="{f(rr * 0.8)}" fill="#1E1650" stroke="{INK}" stroke-width="3"></rect>'
             + "".join(f'<path d="M{f(rx + rr * 0.6 + rr * 0.5 * math.cos(a))} 0 L {f(rx + rr * 0.6 + rr * 0.5 * math.cos(a))} {f(ry)}" stroke="#3A2A6A" stroke-width="1.4"></path>' for a in (0.6, 1.6, 2.6))
             + f'<ellipse cx="{f(rx + rr * 0.6)}" cy="{f(ry)}" rx="{f(rr * 0.8)}" ry="{f(rr * 0.3)}" fill="#3A2A6A" stroke="{INK}" stroke-width="2.4"></ellipse>')
    gy = h * 0.66                                                             # the earth on its foundations
    o.append(hills(w, h, gy, seed, color="#5A7A3A", amp=14, step=80))
    for k, c in enumerate(("#8A6A4A", "#6A4A3A", "#4A3428", "#2A1E18")):
        y = gy + h * 0.06 + k * h * 0.075
        o.append(f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y - 6)} {f(w * 0.6)} {f(y + 6)} {f(w + 10)} {f(y)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="{c}" stroke="{INK}" stroke-width="1.8"></path>')
    o.append(plate_label(w * 0.37, ry - 14, "THE HEAVENS · AS A MANTLE ROLLED UP", GOLD, 10) + plate_label(w * 0.5, h - 12, "THE FOUNDATION OF THE EARTH", CREAM, 10, halo_="#2A1E18"))
    return "".join(o)

def ministering(p, w, h, seed):
    """Ministering spirits, sent forth to do service for the sake of them that shall inherit salvation: a town at dusk, its
    lamps lit, and down a road of light out of the sky three figures of white light with gold rims, no faces, going to its
    doors."""
    o = [_defs(p), sky(w, h, "#1A1440", "#C8803A"), starfield(w, h, seed, 30, 0.4)]
    o.append(f'<path d="M{f(w * 0.62)} -10 L {f(w * 0.86)} -10 L {f(w * 0.56)} {f(h * 0.9)} L {f(w * 0.34)} {f(h * 0.9)} Z" fill="#FFF4C2" opacity="0.35"></path>')
    o.append(town_hill(w * 0.24, h * 0.86, w * 0.42, h * 0.3, seed, color="#5A4A4A", lit=True))
    o.append(ground(w, h, h * 0.86, "#3A2A2A", dy=0))
    for k, (x, y, sc) in enumerate(((0.7, 0.36, 0.34), (0.6, 0.6, 0.5), (0.48, 0.9, 0.72))):
        s = (h * sc) / 220
        o.append(angel_fig(p, w * x, h * y, s, flip=False))
    return "".join(o)

# ---- Hebrews 2 ------------------------------------------------------------------------------------------------------------
def drift(p, w, h, seed):
    """Lest haply we drift away from them: a harbour at evening, the boats made fast at the quay, and one boat loosed, its rope
    trailing in the water, carried out on the current past the harbour mouth toward the open sea — no one in it."""
    o = [sky(w, h, "#2A2A5A", "#E8A06A"), halo(w * 0.86, h * 0.44, h * 0.3, "#FFD08A", 0.5)]
    sy_ = h * 0.5
    o.append(f'<rect x="-10" y="{f(sy_)}" width="{f(w + 20)}" height="{f(h - sy_ + 10)}" fill="#1F4A6A"></rect>')
    r = random.Random(seed)
    for i in range(30):
        y = sy_ + (h - sy_) * r.random(); x = w * r.random()
        o.append(f'<path d="M{f(x)} {f(y)} l {f(r.uniform(10, 30))} 0" stroke="#5A8AAA" stroke-width="1.4"></path>')
    qx = w * 0.3                                                              # the quay and the mole
    o.append(f'<path d="M-10 {f(sy_ + 6)} L {f(qx)} {f(sy_ + 6)} L {f(qx)} {f(h * 0.78)} L -10 {f(h * 0.78)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>'
             + "".join(f'<path d="M-10 {f(sy_ + 6 + k * h * 0.06)} L {f(qx)} {f(sy_ + 6 + k * h * 0.06)}" stroke="#6A5A4A" stroke-width="1.4"></path>' for k in range(1, 5))
             + f'<path d="M{f(w * 0.56)} {f(sy_ - 2)} L {f(w * 0.74)} {f(sy_ - 2)} L {f(w * 0.74)} {f(sy_ + 14)} L {f(w * 0.56)} {f(sy_ + 14)} Z" fill="#7A6A5A" stroke="{INK}" stroke-width="2"></path>'
             + f'<rect x="{f(w * 0.7)}" y="{f(sy_ - h * 0.14)}" width="{f(w * 0.03)}" height="{f(h * 0.14)}" fill="#C8B898" stroke="{INK}" stroke-width="1.6"></rect>')
    def boat(x, y, k, rot=0):
        return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({f(k)})"><path d="M-60 -10 L 60 -10 C 52 8 30 16 0 16 C -30 16 -52 8 -60 -10 Z" fill="#6A3A22" stroke="{INK}" stroke-width="2.4"></path>'
                f'<path d="M-56 -10 L 56 -10" stroke="#C8A060" stroke-width="2"></path><path d="M0 -10 L 0 -70" stroke="{INK}" stroke-width="3"></path></g>')
    k = min(1.0, h / 300)
    for i in range(2):
        bx = qx + 50 * k; by = sy_ + h * (0.12 + 0.16 * i)
        o.append(boat(bx, by, k * 0.8) + f'<path d="M{f(bx - 40 * k)} {f(by - 8 * k)} C {f(qx + 10)} {f(by - 20 * k)} {f(qx)} {f(by - 30 * k)} {f(qx - 6)} {f(by - 30 * k)}" fill="none" stroke="#C8A060" stroke-width="1.6"></path>')
    dx, dy = w * 0.8, sy_ + h * 0.2                                           # the loosed boat
    o.append(boat(dx, dy, k * 0.7, rot=-12) + f'<path d="M{f(dx - 40 * k)} {f(dy)} C {f(dx - 80 * k)} {f(dy + 20 * k)} {f(dx - 120 * k)} {f(dy + 10 * k)} {f(dx - 150 * k)} {f(dy + 24 * k)}" fill="none" stroke="#C8A060" stroke-width="1.6" stroke-dasharray="5 4"></path>')
    for i in range(3):
        o.append(f'<path d="M{f(dx + 40 * k + i * 26 * k)} {f(dy + 18 * k)} l {f(30 * k)} {f(-6 * k)} l -8 -6 M{f(dx + 40 * k + i * 26 * k + 30 * k)} {f(dy + 12 * k)} l -8 6" stroke="#FFF4E8" stroke-width="2" fill="none" opacity="0.7"></path>')
    return "".join(o)

def what_is_man(p, w, h, seed):
    """What is man, that thou art mindful of him? A man alone on a hill at night under the moon and the stars, looking up, his
    hand lifted; the sheepfold and his flock asleep below."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#05051A", "#2A2A5A"), starfield(w, h, seed, 120, 0.8), halo(w * 0.78, h * 0.18, h * 0.16, "#FFF4C2", 0.45),
         f'<circle cx="{f(w * 0.78)}" cy="{f(h * 0.18)}" r="{f(max(8, h * 0.05))}" fill="#FFF8DC"></circle>',
         hills(w, h, h * 0.7, seed, color="#14142E", amp=12, step=90)]
    o.append(f'<path d="M-10 {f(b - h * 0.04)} C {f(w * 0.2)} {f(h * 0.74)} {f(w * 0.45)} {f(h * 0.72)} {f(w * 0.62)} {f(h * 0.8)} C {f(w * 0.8)} {f(h * 0.88)} {f(w * 0.9)} {f(h * 0.9)} {f(w + 10)} {f(h * 0.9)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1E1A30" stroke="{INK}" stroke-width="2"></path>')
    s = fit(b, max(h * 0.28, b - 220)) * 0.92
    o.append(robed(p, w * 0.36, h * 0.8, s, "#6A5A4A", head="#2A3A4A", cord="#0D1A2A", beard="#2A1A10", mantle="#4A3A2A", flip=True,
                   up=[(-22, -158), (-34, -186), (-36, -214)]))
    return "".join(o)

def crowned(p, w, h, seed):
    """We behold him who hath been made a little lower than the angels, even Jesus, because of the suffering of death crowned
    with glory and honor: far below at the left, the hill of the three crosses small under a darkened sky; at the right, high
    on the clouds in a great light, Jesus risen in white light, his hand lifted."""
    o = [defs_up(p), f'<defs><linearGradient id="{p}sk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#0B0B12"></stop><stop offset="0.4" stop-color="#3A2A4A"></stop>'
         f'<stop offset="0.65" stop-color="#E8C890"></stop><stop offset="1" stop-color="#FFF8DC"></stop></linearGradient></defs><rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{p}sk)"></rect>']
    gy = h * 0.86                                                             # the hill and the crosses, far off
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(gy)} C {f(w * 0.08)} {f(gy - h * 0.1)} {f(w * 0.2)} {f(gy - h * 0.12)} {f(w * 0.3)} {f(gy - 2)} L {f(w * 0.46)} {f(h + 10)} Z" fill="#1A1218" stroke="{INK}" stroke-width="2"></path>')
    k = min(1.0, h / 360)
    for i, x in enumerate((w * 0.1, w * 0.16, w * 0.22)):
        top = gy - h * 0.1 - (h * 0.07 if i == 1 else h * 0.05)
        base_ = gy - h * 0.1 + abs(i - 1) * h * 0.012
        o.append(f'<path d="M{f(x)} {f(base_)} L {f(x)} {f(top)} M{f(x - 10 * k)} {f(top + 9 * k)} L {f(x + 10 * k)} {f(top + 9 * k)}" stroke="#0D0D0F" stroke-width="{f(3.2 * k)}"></path>')
    o.append(f'<g transform="translate({f(w * 0.42)} 0)">' + cloud_bank(w * 0.6, h * 0.8, seed, "#FFFDF0", 0.85, k=min(1.0, h / 320)) + '</g>')
    s = h * 0.68 / 205
    o.append(risen_fig(p, w * 0.7, h * 0.84, s, flip=True, up=[(-22, -158), (-40, -186), (-48, -214)]))
    o.append(plate_label(w * 0.17, h * 0.12, "THE SUFFERING OF DEATH", "#C8A0A0", 10, halo_="#0B0B12") + plate_label(w * 0.7, h * 0.08, "CROWNED WITH GLORY AND HONOR", "#7A4A10", 10, halo_="#FFF8DC"))
    return "".join(o)

def many_sons(p, w, h, seed):
    """In bringing many sons unto glory: a great company of men and women seen from behind on the plain at dawn, going toward
    the light (Romans' drawing)."""
    from rom.art4 import nations_dawn
    return nations_dawn(p, w, h, seed)

BRETHREN = [("#6A4A3A", "#2A3A4A", "#2A1A10", None), ("#4A5A6A", "#E8E2D6", "#6A645E", None), ("#5A6A4A", None, "#1A1210", None),
            ("#7A6A8A", None, None, "#2A3A5A"), ("#8A5A3A", "#1F2F2A", "#3A2A1A", None), ("#5A7A7A", None, None, "#1F3A3A")]

def brother_fig(p, x, y, s, i, flip=False, up=None, pose="stand", seat=None):
    """One of the brethren (men in cool or off-white headcloths or bareheaded, women veiled), each look fixed by i."""
    c, hd, bd, vl = BRETHREN[i % len(BRETHREN)]
    if vl: return robed(p, x, y, s * 0.94, c, woman=True, veil=vl, flip=flip, up=up, pose=pose, seat=seat)
    return robed(p, x, y, s, c, head=hd, hair=None if hd else "#1A1210", beard=bd, flip=flip, up=up, pose=pose, seat=seat)

def brethren(p, w, h, seed):
    """In the midst of the congregation will I sing thy praise … Behold, I and the children whom God hath given me: Jesus
    risen in white light (ntcast's look) standing on the hillside at morning, his hand out, and his brethren about him, men
    and women, some standing and some sitting on the grass."""
    b = h * 0.95
    o = [defs_up(p), sky(w, h, "#8FD0E2", "#FFF4C2"), hills(w, h, h * 0.5, seed, color="#9AA07A", amp=12, step=90), ground(w, h, h * 0.62, "#A8A86A", dy=0),
         olive(w * 0.94, h * 0.9, h / 380, seed=seed)]
    s = fit(b, max(h * 0.24, b - 230))
    o.append(risen_fig(p, w * 0.2, b, s, flip=True, up=[(-22, -158), (-48, -150), (-72, -156)]))
    for k, (x, pose) in enumerate(((0.4, "sit"), (0.5, "stand"), (0.6, "sit"), (0.7, "stand"), (0.8, "sit"), (0.88, "stand"))):
        o.append(brother_fig(p, w * x, b, s * (0.94 if pose == "stand" else 0.98), k, pose=pose, seat="stool" if pose == "sit" else None))
    return "".join(o)

def high_priest_mercy(w, h):
    """A merciful and faithful high priest, to make propitiation for the sins of the people: the ark of the covenant and the
    mercy-seat as a technical plate (Romans' drawing)."""
    from rom.art import propitiation
    return propitiation(w, h).replace("ROMANS 3:25 · A PROPITIATION · THE MERCY-SEAT", "HEBREWS 2:17 · TO MAKE PROPITIATION · THE MERCY-SEAT")

def chains_broken(w, h, seed):
    """Deliver all them who through fear of death were all their lifetime subject to bondage: a chain broken open on the
    stones in the morning light (Romans' drawing). The devil (2:14) is in the words only."""
    from rom.art2 import broken_chains
    return broken_chains(w, h, seed)

# ---- Hebrews 3 ------------------------------------------------------------------------------------------------------------
def moses_tent(p, w, h, seed):
    """Moses faithful in all his house: Moses (Exodus' look — off-white headcloth, black beard, brown robe, on the kit figure) standing
    before the tabernacle in its court of white linen in the wilderness, the pillar of cloud over it."""
    from co2.art import moses_fig as moses                             # Exodus' Moses on the kit figure (2 Corinthians)
    b = h * 0.94
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#8FD0E2", "#F3E0B0"), hills(w, h, h * 0.6, seed, color="#C8985A", amp=12, step=90), ground(w, h, h * 0.7, "#D8B880", dy=0)]
    k = min(w / 700, h / 300)
    cx, cb = w * 0.62, h * 0.8                                                # the court and the tent
    o.append(f'<rect x="{f(cx - 230 * k)}" y="{f(cb - 50 * k)}" width="{f(460 * k)}" height="{f(50 * k)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<path d="M{f(cx - 230 * k + 46 * k * i)} {f(cb - 56 * k)} L {f(cx - 230 * k + 46 * k * i)} {f(cb)}" stroke="#8A6A4A" stroke-width="{f(3 * k)}"></path>' for i in range(11)))
    o.append(f'<path d="M{f(cx - 110 * k)} {f(cb - 50 * k)} L {f(cx - 110 * k)} {f(cb - 130 * k)} L {f(cx + 150 * k)} {f(cb - 130 * k)} L {f(cx + 150 * k)} {f(cb - 50 * k)} Z" fill="#5A3A2A" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(cx - 118 * k)} {f(cb - 126 * k)} L {f(cx + 20 * k)} {f(cb - 156 * k)} L {f(cx + 158 * k)} {f(cb - 126 * k)} Z" fill="#7A3A2A" stroke="{INK}" stroke-width="2.4"></path>'
             f'<rect x="{f(cx - 110 * k)}" y="{f(cb - 120 * k)}" width="{f(20 * k)}" height="{f(70 * k)}" fill="#3A5A9A" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<rect x="{f(cx - 90 * k)}" y="{f(cb - 120 * k)}" width="{f(20 * k)}" height="{f(70 * k)}" fill="#6A3A7A" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<rect x="{f(cx - 70 * k)}" y="{f(cb - 120 * k)}" width="{f(20 * k)}" height="{f(70 * k)}" fill="#A82A2A" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<path d="M{f(cx + 20 * k)} {f(cb - 160 * k)} C {f(cx - 20 * k)} {f(h * 0.3)} {f(cx + 60 * k)} {f(h * 0.2)} {f(cx + 10 * k)} -10 L {f(cx + 90 * k)} -10 C {f(cx + 130 * k)} {f(h * 0.2)} {f(cx + 50 * k)} {f(h * 0.3)} {f(cx + 70 * k)} {f(cb - 160 * k)} Z" fill="#FFFDF0" opacity="0.75"></path>')
    s = fit(b, max(h * 0.25, b - 220))
    o.append(moses(p, w * 0.18, b, s, flip=True))
    return "".join(o)

def house_plate(w, h):
    """Moses faithful in all his house as a servant; but Christ as a son, over his house; whose house are we: a technical
    plate — a house in elevation, its builder's mark at the gable; at the left the servant within the house (MOSES · A SERVANT
    IN ALL HIS HOUSE), at the right the son over it (CHRIST · A SON OVER HIS HOUSE), and in its rooms the household: WHOSE
    HOUSE ARE WE."""
    o = [plate_bg(w, h, "HEBREWS 3:3–6 · HE THAT BUILT THE HOUSE HATH MORE HONOR THAN THE HOUSE")]
    k = min(w / 700, (h - 40) / 260)
    cx, b = w * 0.5, h - 28 * k
    hw, hh = 200 * k, 130 * k
    o.append(f'<path d="M{f(cx - hw / 2)} {f(b)} L {f(cx - hw / 2)} {f(b - hh)} L {f(cx)} {f(b - hh - 70 * k)} L {f(cx + hw / 2)} {f(b - hh)} L {f(cx + hw / 2)} {f(b)} Z" fill="none" stroke="{CY}" stroke-width="2.4"></path>'
             f'<path d="M{f(cx - hw / 2)} {f(b - hh / 2)} L {f(cx + hw / 2)} {f(b - hh / 2)} M{f(cx)} {f(b - hh)} L {f(cx)} {f(b)}" stroke="{CY}" stroke-width="1.4" stroke-dasharray="5 4"></path>'
             f'<rect x="{f(cx - 14 * k)}" y="{f(b - 40 * k)}" width="{f(28 * k)}" height="{f(40 * k)}" fill="none" stroke="{CY}" stroke-width="1.6"></rect>')
    for i in range(4):                                                        # the household in its rooms
        x = cx + (i - 1.5) * hw / 4; y = b - (hh / 2 + 4 if i % 2 else 4) + (0 if i % 2 else 0)
        y = b - hh / 2 - 4 if i in (1, 2) else b - 4
        o.append(f'<circle cx="{f(x)}" cy="{f(y - 30 * k)}" r="{f(6 * k)}" fill="{GOLD}"></circle><path d="M{f(x - 8 * k)} {f(y)} L {f(x - 5 * k)} {f(y - 22 * k)} L {f(x + 5 * k)} {f(y - 22 * k)} L {f(x + 8 * k)} {f(y)} Z" fill="{GOLD}"></path>')
    o.append(f'<circle cx="{f(cx)}" cy="{f(b - hh - 34 * k)}" r="{f(9 * k)}" fill="none" stroke="{GOLD}" stroke-width="2"></circle>')
    o.append(tag(cx, b - hh - 44 * k, "THE BUILDER · HE THAT BUILT ALL THINGS IS GOD", cx, 56 * k + 20, GOLD, 9))
    sx = cx - hw / 2 + 30 * k                                                 # the servant within, the son over
    o.append(f'<circle cx="{f(sx)}" cy="{f(b - 40 * k)}" r="{f(7 * k)}" fill="none" stroke="#FFFFFF" stroke-width="2"></circle><path d="M{f(sx - 9 * k)} {f(b - 4)} L {f(sx - 6 * k)} {f(b - 30 * k)} L {f(sx + 6 * k)} {f(b - 30 * k)} L {f(sx + 9 * k)} {f(b - 4)} Z" fill="none" stroke="#FFFFFF" stroke-width="2"></path>')
    o.append(tag(sx, b - 50 * k, "MOSES · A SERVANT IN ALL HIS HOUSE", w * 0.16, b - hh - 20 * k, "#FFFFFF", 9))
    ox, oy = cx + hw / 2 + 60 * k, b - hh - 30 * k
    o.append(halo(ox, oy, 40 * k, "#FFE680", 0.5) + f'<circle cx="{f(ox)}" cy="{f(oy - 14 * k)}" r="{f(8 * k)}" fill="#FFF8DC"></circle><path d="M{f(ox - 11 * k)} {f(oy + 22 * k)} L {f(ox - 7 * k)} {f(oy - 4 * k)} L {f(ox + 7 * k)} {f(oy - 4 * k)} L {f(ox + 11 * k)} {f(oy + 22 * k)} Z" fill="#FFF8DC"></path>')
    o.append(tag(ox, oy + 26 * k, "CHRIST · A SON OVER HIS HOUSE", w * 0.84, b - 30 * k, "#FFE680", 9))
    o.append(label(cx, b + 15, "WHOSE HOUSE ARE WE", GOLD, 9))              # under the house, its household
    return "".join(o)

def wilderness_years(p, w, h, seed):
    """Your fathers … saw my works forty years: the long file of the people in the wilderness under a white sun (Exodus'
    drawing)."""
    from exo.art4 import wilderness
    return mk.defs(p, *ALL) + wilderness(p, w, h, seed)

def to_day(p, w, h, seed):
    """Exhort one another day by day, so long as it is called To-day: a street of a town at sunrise, two neighbours met at a
    door, one with his hand on the other's shoulder, a woman at the next door with her jar."""
    b = h * 0.95
    o = [defs_up(p), sky(w, h, "#3A3A7A", "#FFC890"), halo(w * 0.86, h * 0.36, h * 0.4, "#FFD08A", 0.6),
         f'<circle cx="{f(w * 0.86)}" cy="{f(h * 0.36)}" r="{f(max(10, h * 0.06))}" fill="#FFE6A0"></circle>']
    r = random.Random(seed); x = -10
    while x < w * 0.72:                                                       # the house fronts
        bw = w * r.uniform(0.14, 0.2); bh = h * r.uniform(0.42, 0.56)
        o.append(f'<rect x="{f(x)}" y="{f(b - bh)}" width="{f(bw)}" height="{f(bh + 10)}" fill="{r.choice(["#D8C098", "#C8B088", "#E0CCA4"])}" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="{f(x + bw * 0.34)}" y="{f(b - bh * 0.46)}" width="{f(bw * 0.32)}" height="{f(bh * 0.46)}" fill="#5A3A22" stroke="{INK}" stroke-width="1.6"></rect>'
                 f'<rect x="{f(x + bw * 0.4)}" y="{f(b - bh * 0.86)}" width="{f(bw * 0.2)}" height="{f(bh * 0.14)}" fill="#3A2A2A" stroke="{INK}" stroke-width="1.4"></rect>')
        x += bw
    o.append(ground(w, h, b, "#B8A07A", dy=0))
    s = fit(b, max(h * 0.25, b - 220))
    o.append(robed(p, w * 0.3, b, s, "#4A5A6A", head="#E8E2D6", cord="#6A5A3A", beard="#6A645E", mantle="#2A3444", flip=True,
                   up=[(-22, -158), (-48, -150), (-72, -152)]))
    o.append(robed(p, w * 0.44, b, s, "#6A4A3A", head="#2A3A4A", cord="#0D1A2A", beard="#2A1A10"))
    o.append(robed(p, w * 0.62, b, s * 0.94, "#5A7A7A", woman=True, veil="#1F3A3A",
                   up=[(-22, -158), (-26, -186), (-24, -206)], extra='<path d="M-34 -230 C -40 -250 -14 -250 -18 -230 L -14 -206 L -38 -206 Z" fill="#A8603A" stroke="#0D0D0F" stroke-width="2"></path>'))
    return "".join(o)

def desert_fallen(w, h, seed):
    """Whose bodies fell in the wilderness: the empty desert, the hills bare, no one in it (1 Corinthians' drawing)."""
    from co1.art3 import desert_empty
    return desert_empty(w, h, seed)

# ---- Hebrews 4 ------------------------------------------------------------------------------------------------------------
def land_of_rest(w, h, seed):
    """A promise being left of entering into his rest: the land beyond the Jordan seen from the heights of the wilderness at
    morning — the river winding through its green plain, the hills of the land rising beyond it in the light."""
    return vista(w, h, seed, tone="dawn", horizon=0.5, sun_at=(0.7, 0.3), hills_n=2, river_=True, trees=3, field="grain")

def sabbath(w, h, seed):
    """And God rested on the seventh day from all his works: the world finished and still at evening — the sun going down
    over the hills, the trees and the flock at rest in the field, no one at work."""
    return vista(w, h, seed, tone="dusk", horizon=0.56, sun_at=(0.74, 0.44), hills_n=2, trees=3, sheep=6, birds_=3)

def david_harp(w, h, seed):
    """Saying in David so long a time afterward: the king's harp and the open scroll of the psalm on a table by lamplight
    (Romans' drawing)."""
    from rom.art2 import harp
    return harp(w, h, seed)

JOSHUA_LOOK = dict(cloth="#7A4A2A", head="#B5421E", cord="#2A1A10", beard="#1A1210", mantle="#4A2A1A")     # Joshua: rust-red headcloth, black beard

def joshua_land(p, w, h, seed):
    """If Joshua had given them rest, he would not have spoken afterward of another day: Joshua (his rust-red headcloth, black
    beard) on a height with his hand out over the land, the tents of the people below him and the hills of Canaan beyond."""
    b = h * 0.95
    o = [defs_up(p), sky(w, h, "#5AB0D8", "#FFF4C2"), hills(w, h, h * 0.5, seed, color="#8A9A6A", amp=16, step=90),
         hills(w, h, h * 0.62, seed + 1, color="#6A8A4A", amp=12, step=70), ground(w, h, h * 0.72, "#C8B87A", dy=0)]
    for i in range(9):
        x = w * (0.42 + 0.06 * i); y = h * (0.8 + 0.03 * (i % 3)); k = min(1.0, h / 400)
        o.append(f'<path d="M{f(x - 22 * k)} {f(y)} L {f(x - 10 * k)} {f(y - 20 * k)} L {f(x + 14 * k)} {f(y - 22 * k)} L {f(x + 24 * k)} {f(y)} Z" fill="#3A2A22" stroke="{INK}" stroke-width="1.4"></path>')
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.72)} C {f(w * 0.1)} {f(h * 0.68)} {f(w * 0.24)} {f(h * 0.7)} {f(w * 0.34)} {f(h * 0.82)} L {f(w * 0.4)} {f(h + 10)} Z" fill="#9A7A5A" stroke="{INK}" stroke-width="2"></path>')
    s = fit(b, max(h * 0.25, b - 230))
    L = JOSHUA_LOOK
    o.append(robed(p, w * 0.18, h * 0.78, s, L["cloth"], head=L["head"], cord=L["cord"], beard=L["beard"], mantle=L["mantle"], flip=True,
                   up=[(-22, -158), (-50, -156), (-78, -164)]))
    return "".join(o)

def sword_plate(w, h):
    """The word of God is living, and active, and sharper than any two-edged sword, piercing even to the dividing of soul and
    spirit, of both joints and marrow: a technical plate — the two-edged sword drawn full length, both edges tagged, and at
    its point the four it divides: SOUL · SPIRIT · JOINTS · MARROW; under it THE THOUGHTS AND INTENTS OF THE HEART."""
    o = [plate_bg(w, h, "HEBREWS 4:12 · SHARPER THAN ANY TWO-EDGED SWORD")]
    k = min(w / 700, (h - 30) / 240)
    y = h * 0.52; x0, x1 = w * 0.08, w * 0.7
    o.append(f'<rect x="{f(x0)}" y="{f(y - 7 * k)}" width="{f(80 * k)}" height="{f(14 * k)}" rx="{f(5 * k)}" fill="#5A3A22" stroke="{GOLD}" stroke-width="1.6"></rect>'
             f'<circle cx="{f(x0 - 6 * k)}" cy="{f(y)}" r="{f(10 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="1.6"></circle>'
             f'<rect x="{f(x0 + 80 * k)}" y="{f(y - 34 * k)}" width="{f(14 * k)}" height="{f(68 * k)}" rx="{f(4 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<path d="M{f(x0 + 94 * k)} {f(y - 16 * k)} L {f(x1)} {f(y - 10 * k)} L {f(x1 + 60 * k)} {f(y)} L {f(x1)} {f(y + 10 * k)} L {f(x0 + 94 * k)} {f(y + 16 * k)} Z" fill="#D8E4EE" stroke="{CY}" stroke-width="2"></path>'
             f'<path d="M{f(x0 + 94 * k)} {f(y)} L {f(x1 + 50 * k)} {f(y)}" stroke="#8AA0B8" stroke-width="2"></path>')
    o.append(tag(x0 + 300 * k, y - 14 * k, "THE ONE EDGE", x0 + 260 * k, y - 70 * k, CY, 9) + tag(x0 + 380 * k, y + 14 * k, "AND THE OTHER", x0 + 420 * k, y + 74 * k, CY, 9))
    px = x1 + 60 * k
    for i, nm in enumerate(("SOUL", "SPIRIT", "JOINTS", "MARROW")):
        ty = y - 66 * k + i * 44 * k
        o.append(f'<path d="M{f(px)} {f(y)} L {f(px + 40 * k)} {f(ty)}" stroke="{GOLD}" stroke-width="1.4" stroke-dasharray="4 3"></path>' + label(px + 46 * k, ty + 4, nm, GOLD, 11, anchor="start"))
    o.append(label(w * 0.5, h - 14, "QUICK TO DISCERN THE THOUGHTS AND INTENTS OF THE HEART", CREAM, 10))
    o.append(dim(x0 - 16 * k, y + 50 * k, x1 + 60 * k, y + 50 * k, "LIVING · AND ACTIVE", off=0, size=9, color=CY))
    return "".join(o)

def throne_grace(p, w, h, seed):
    """Let us draw near with boldness unto the throne of grace: the throne standing empty in a great light above the clouds,
    and a road of light going up to it from the dark earth below."""
    o = [sky(w, h, "#1A1440", "#FFE6C0"), starfield(w, h, seed, 30, 0.4)]
    s = min(h * 0.6 / 300, w * 0.4 / 220)
    o.append(f'<path d="M{f(w * 0.2)} {f(h + 10)} L {f(w * 0.44)} {f(h * 0.6)} L {f(w * 0.56)} {f(h * 0.6)} L {f(w * 0.8)} {f(h + 10)} Z" fill="#FFF4C2" opacity="0.6"></path>')
    o.append(f'<path d="M-10 {f(h * 0.86)} C {f(w * 0.2)} {f(h * 0.82)} {f(w * 0.36)} {f(h * 0.9)} {f(w * 0.3)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#2A1E30" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(w + 10)} {f(h * 0.84)} C {f(w * 0.8)} {f(h * 0.82)} {f(w * 0.66)} {f(h * 0.9)} {f(w * 0.72)} {f(h + 10)} L {f(w + 10)} {f(h + 10)} Z" fill="#2A1E30" stroke="{INK}" stroke-width="2"></path>')
    o.append(cloud_bank(w, h * 0.62, seed, "#FFF8E8", 0.7, k=min(1.0, h / 320)))
    o.append(throne_of_light(w * 0.5, h * 0.64, s, f"{p}t"))
    return "".join(o)

def through_heavens(p, w, h, seed):
    """A great high priest, who hath passed through the heavens: the heavens one above another — the blue of the air, the
    clouds, the night of the stars — and a road of light going up through them all from the hills below, to a light above
    (no figure)."""
    o = [f'<defs><linearGradient id="{p}sk" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#8FD0E2"></stop><stop offset="0.35" stop-color="#3A5A9A"></stop>'
         f'<stop offset="0.65" stop-color="#14123A"></stop><stop offset="1" stop-color="#05051A"></stop></linearGradient></defs><rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{p}sk)"></rect>',
         starfield(w, h, seed, 70, 0.4)]
    o.append(f'<path d="M{f(w * 0.4)} {f(h + 10)} L {f(w * 0.48)} -10 L {f(w * 0.52)} -10 L {f(w * 0.6)} {f(h + 10)} Z" fill="#FFF4C2" opacity="0.5"></path>'
             f'<path d="M{f(w * 0.46)} {f(h + 10)} L {f(w * 0.495)} -10 L {f(w * 0.505)} -10 L {f(w * 0.54)} {f(h + 10)} Z" fill="#FFFFFF" opacity="0.7"></path>')
    for k, (y, c, op) in enumerate(((h * 0.62, "#E8ECF8", 0.75), (h * 0.36, "#B8C0E0", 0.45))):
        o.append(cloud_bank(w, y, seed + k, c, op, k=min(1.0, h / 340) * (1 - 0.25 * k)))
    o.append(halo(w * 0.5, 0, h * 0.3, "#FFFFFF", 0.8))
    o.append(hills(w, h, h * 0.88, seed, color="#3A4A3A", amp=14, step=90) + ground(w, h, h * 0.94, "#2A3A2A", dy=0))
    return "".join(o)
