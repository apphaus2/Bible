"""Drawings for the 2 Peter volume. 2 Peter starts from all of 1 Peter's drawings (`from pe1.art2 import *`, which carries
James', Galatians', Acts', Mark's and Matthew's drawings, the epistle kit and the writers' figures) and adds its own.

The people at a distance: Peter only ever jas.art.peter_fig (old), sitting now in his study; Jesus only ever ntcast's figure
(on the holy mount in white light, as mat.art11.jesus_risen whitens it); Moses as 2 Corinthians draws him on the kit
silhouette (co2.art.moses_fig); Elijah bareheaded in his hairy brown mantle; Lot in maroon (Genesis); Balaam in his purple
headcloth on the grey ass (Numbers). God is never drawn (light, cloud, the Voice box); angels are words only here. Paul is
never drawn: 3:15–16 are his letters, rolled. Every function takes (p, w, h, seed, ...) or (w, h, ...)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from pe1.art2 import *
from jas.art import art, plate_label, _street, _road
from co2.art import moses_fig
from mat.art11 import jesus_risen
from epistle import pigeonholes
import numbers1 as N1

ROME_SCRIBE = dict(cloth="#5A5A6A", hair="#2A1A10")                 # a young scribe of the church at Rome, bareheaded

def peter_seated(p, x, y, s, flip=False, up=None, extra=""):
    return peter_fig(p, x, y, s, flip=flip, up=up, extra=extra, pose="sit", seat="stool")

def study_old(p, w, h, seed, stage="dictate", fig_h=None):
    """Peter old, writing at Rome by lamplight: the study (epistle.study, window "rome"), Peter sitting on his stool now,
    his hand out, a young scribe of the church on his mat writing."""
    return study(p, w, h, seed, stage=stage, scribe=ROME_SCRIBE, writer=peter_seated, window="rome", fig_h=fig_h)

def elijah_r(p, x, y, s, flip=False, up=None, extra=""):
    """Elijah as Kings draws him: bareheaded, a black beard, the hairy brown mantle."""
    fur = "".join(f'<path d="M{xx} -150 l -4 10 M{xx + 6} -120 l -4 10 M{xx - 4} -90 l -4 10" stroke="#3A1A0A" stroke-width="2"></path>' for xx in (-12, 0, 12))
    return robed(p, x, y, s, "#6A4A2A", hair="#2A1A10", beard="#2A1A10", mantle="#5A3A1A", belt="#3A2214", flip=flip, up=up, extra=fur + extra)

def lot_r(p, x, y, s, flip=False, up=None, extra="", pose="stand"):
    """Lot as Genesis draws him: a maroon robe, a dark headcloth, a beard."""
    return robed(p, x, y, s, "#7A2A2A", head="#3A2A2A", cord="#1A1210", beard="#3A2A1A", flip=flip, up=up, extra=extra, pose=pose)

# ---- 2 Peter 1 ------------------------------------------------------------------------------------------------------------
GRACES = ("FAITH", "VIRTUE", "KNOWLEDGE", "SELF-CONTROL", "PATIENCE", "GODLINESS", "BROTHERLY KINDNESS", "LOVE")
def graces_stair(w, h):
    """In your faith supply virtue; and in your virtue knowledge; … and in your brotherly kindness love: a plate of eight
    hewn steps going up from left to right, each named, faith at the foot and love at the top, lit."""
    o = [plate_bg(w, h, "2 PETER 1:5–7 · ADDING ON YOUR PART ALL DILIGENCE")]
    n = len(GRACES); x0, x1 = w * 0.04, w * 0.96; y0, y1 = h * 0.92, h * 0.2
    sw, sh = (x1 - x0) / n, (y0 - y1) / n
    for i, name in enumerate(GRACES):
        x = x0 + i * sw; top = y0 - (i + 1) * sh
        lit = i == n - 1
        o.append(f'<path d="M{f(x)} {f(y0)} L {f(x)} {f(top)} L {f(x + sw)} {f(top)} L {f(x + sw)} {f(y0)} Z" fill="{"#C8A040" if lit else "#2A4A6A"}" stroke="{CY}" stroke-width="1.4"></path>'
                 f'<path d="M{f(x)} {f(top)} L {f(x + 10)} {f(top - 8)} L {f(x + sw + 10)} {f(top - 8)} L {f(x + sw)} {f(top)} Z" fill="{"#FFD23F" if lit else "#3A5A7A"}" stroke="{CY}" stroke-width="1.2"></path>')
        o.append(f'<g transform="translate({f(x + sw / 2)} {f(top + 14)})">' + label(0, 0, name if len(name) < 12 else name.split()[0], GOLD if not lit else "#3A1A0A", 8) +
                 (label(0, 12, name.split()[1], GOLD, 8) if len(name) >= 12 and " " in name else "") + '</g>')
        if i < n - 1:
            o.append(f'<path d="M{f(x + sw * 0.6)} {f(top - 16)} L {f(x + sw * 1.3)} {f(top - sh - 12)}" stroke="#FFD23F" stroke-width="1.2" stroke-dasharray="3 3" opacity="0.7"></path>')
    o.append(halo(x1 - sw / 2, y1 - 10, sw, "#FFE680", 0.5))
    return "".join(o)

def tent_struck(p, w, h, seed):
    """The putting off of my tabernacle cometh swiftly: an old man's tent at night under the stars, its pegs drawn and laid by,
    the cords loosed and hanging, the cloth beginning to sag; at its door the lamp burning low, and a staff leaning there."""
    r = random.Random(seed)
    b = h * 0.88
    o = [sky(w, h, "#0B0B2A", "#2A2050"), mk.stars(50, w, h * 0.5, seed), hills(w, h, h * 0.58, seed, color="#1E1A34", amp=12, step=90),
         ground(w, h, h * 0.66, "#2A2430", dy=0)]
    cx, tw, th = w * 0.46, w * 0.42, h * 0.46
    l, rr, t = cx - tw / 2, cx + tw / 2, b - th
    o.append(f'<path d="M{f(l)} {f(b)} L {f(l + tw * 0.08)} {f(t + th * 0.34)} C {f(cx - tw * 0.2)} {f(t + th * 0.1)} {f(cx - tw * 0.08)} {f(t + th * 0.02)} {f(cx)} {f(t + th * 0.06)} '
             f'C {f(cx + tw * 0.12)} {f(t + th * 0.1)} {f(cx + tw * 0.26)} {f(t + th * 0.3)} {f(rr - tw * 0.04)} {f(t + th * 0.5)} L {f(rr + tw * 0.06)} {f(b)} Z" fill="#5A4A3A" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(cx)} {f(t + th * 0.06)} L {f(cx)} {f(b)}" stroke="#3A2A1A" stroke-width="3"></path>'
             f'<path d="M{f(cx - tw * 0.1)} {f(b)} L {f(cx - tw * 0.06)} {f(t + th * 0.4)} L {f(cx + tw * 0.06)} {f(t + th * 0.4)} L {f(cx + tw * 0.1)} {f(b)} Z" fill="#FFB04D" stroke="{INK}" stroke-width="2"></path>')
    for i in range(3):                                                # the loosed cords, slack on the ground; the drawn pegs
        x = rr + tw * (0.06 + i * 0.05)
        o.append(f'<path d="M{f(rr - tw * 0.04 - i * 6)} {f(t + th * (0.5 + i * 0.12))} C {f(x - 10)} {f(b - 10)} {f(x)} {f(b + 2)} {f(x + 14)} {f(b + 4)}" stroke="#C8B080" stroke-width="1.6" fill="none"></path>'
                 f'<path d="M{f(x + 16 + i * 10)} {f(b + 8)} l 18 -4" stroke="#8A6A3A" stroke-width="4" stroke-linecap="round"></path>')
    o.append(f'<path d="M{f(l + tw * 0.08)} {f(t + th * 0.34)} C {f(l - 10)} {f(b - th * 0.2)} {f(l - 20)} {f(b)} {f(l - 34)} {f(b + 2)}" stroke="#C8B080" stroke-width="1.6" fill="none"></path>')
    lx, ly = cx - tw * 0.18, b - 4
    o.append(lamp_glow(lx, ly - 10, h * 0.2, "tsl", op=0.55) + clay_lamp(lx, ly, h / 300))
    o.append(f'<path d="M{f(cx + tw * 0.16)} {f(b)} L {f(cx + tw * 0.2)} {f(b - h * 0.36)}" stroke="#6A4A2A" stroke-width="4" stroke-linecap="round"></path>')
    o.append(plate_label(w * 0.46, h * 0.08, "THE PUTTING OFF OF MY TABERNACLE", "#FFE6A0", 10, halo_="#0B0B2A"))
    return "".join(o)

def holy_mount(p, w, h, seed):
    """We were eyewitnesses of his majesty … when we were with him in the holy mount: the top of the high mountain, Jesus
    standing in white light with rays about him (ntcast's look, whitened), Moses at the left and Elijah at the right in the
    light, Peter, James and John fallen on their knees below, the bright cloud coming over (the Father's voice is the Voice
    box; nothing is drawn in the cloud)."""
    b = h * 0.94
    o = [D_(p), sky(w, h, "#2A2A6A", "#8FD0E2"),
         f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.72)} L {f(w * 0.3)} {f(h * 0.6)} L {f(w * 0.5)} {f(h * 0.56)} L {f(w * 0.72)} {f(h * 0.62)} L {f(w + 10)} {f(h * 0.7)} L {f(w + 10)} {f(h + 10)} Z" fill="#6A6A7A" stroke="{INK}" stroke-width="2.4"></path>',
         f'<ellipse cx="{f(w * 0.5)}" cy="{f(h * 0.04)}" rx="{f(w * 0.7)}" ry="{f(h * 0.24)}" fill="#FFFDF0" opacity="0.75"></ellipse>', clouds(w, h * 0.06, seed, n=6, color="#FFFFFF", op=0.85, h=h)]
    jy = h * 0.74
    s = fit(jy, max(h * 0.2, jy - 210))
    o.append(rays(w * 0.5, jy - 110 * s, 36, 40 * s, max(w, h), "#FFFDF0", 0.35))
    o.append(jesus_risen(p, w * 0.5, jy, s))
    o.append(halo(w * 0.24, jy - 100 * s, 110 * s, "#FFF4C2", 0.6) + moses_fig(p, w * 0.24, jy + 8 * s, s * 0.92))
    o.append(halo(w * 0.76, jy - 100 * s, 110 * s, "#FFF4C2", 0.6) + elijah_r(p, w * 0.76, jy + 8 * s, s * 0.92, flip=True))
    for i, x in enumerate((0.3, 0.5, 0.7)):
        o.append(E.kneel(w * x, b, s * 0.72, color=[ROBES["peter"], ROBES["james"], ROBES["john"]][i], skin="#B98A6E", flip=x > 0.5))
    return "".join(o)

def lamp_daystar(w, h, seed):
    """A lamp shining in a dark place, until the day dawn, and the day-star arise: at the left a dark room, a single clay lamp
    burning in a niche of the wall; through the opening at the right the hills at first light and the morning star above
    them."""
    o = [f'<defs><linearGradient id="ld{seed}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#14183A"></stop><stop offset="0.7" stop-color="#5A3A6A"></stop>'
         f'<stop offset="1" stop-color="#FFB07A"></stop></linearGradient></defs><rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#ld{seed})"></rect>']
    ox, ow = w * 0.52, w * 0.44                                       # the opening on the dawn
    o.append(starfield(w, h, seed, 30, 0.5))
    o.append(halo(ox + ow * 0.55, h * 0.24, h * 0.16, "#FFFFFF", 0.7) + f'<path d="M{f(ox + ow * 0.55)} {f(h * 0.24 - 14)} L {f(ox + ow * 0.55 + 4)} {f(h * 0.24 - 4)} L {f(ox + ow * 0.55 + 14)} {f(h * 0.24)} '
             f'L {f(ox + ow * 0.55 + 4)} {f(h * 0.24 + 4)} L {f(ox + ow * 0.55)} {f(h * 0.24 + 14)} L {f(ox + ow * 0.55 - 4)} {f(h * 0.24 + 4)} L {f(ox + ow * 0.55 - 14)} {f(h * 0.24)} L {f(ox + ow * 0.55 - 4)} {f(h * 0.24 - 4)} Z" fill="#FFFDF0"></path>')
    o.append(hills(w, h, h * 0.74, seed, color="#3A2A4A", amp=14, step=70))
    o.append(f'<path d="M-10 -10 L {f(ox)} -10 L {f(ox)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#1A1218" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(ox + ow)} -10 L {f(w + 10)} -10 L {f(w + 10)} {f(h + 10)} L {f(ox + ow)} {f(h + 10)} Z" fill="#1A1218" stroke="{INK}" stroke-width="2.4"></path>')
    k = h / 300
    nx, ny = w * 0.24, h * 0.56                                       # the niche and the lamp
    o.append(lamp_glow(nx, ny - 20 * k, h * 0.42, f"ldg{seed}", op=0.6)
             + f'<path d="M{f(nx - 50 * k)} {f(ny + 10 * k)} L {f(nx - 50 * k)} {f(ny - 50 * k)} C {f(nx - 50 * k)} {f(ny - 90 * k)} {f(nx + 50 * k)} {f(ny - 90 * k)} {f(nx + 50 * k)} {f(ny - 50 * k)} L {f(nx + 50 * k)} {f(ny + 10 * k)} Z" fill="#3A2418" stroke="{INK}" stroke-width="2"></path>'
             + clay_lamp(nx, ny + 6 * k, 1.4 * k))
    o.append(plate_label(w * 0.24, h * 0.1, "A LAMP IN A DARK PLACE", "#FFE6A0", 9, halo_="#1A1218") + plate_label(ox + ow * 0.5, h * 0.1, "THE DAY-STAR", "#FFFDF0", 9, halo_="#14183A"))
    return "".join(o)

# ---- 2 Peter 2 ------------------------------------------------------------------------------------------------------------
def two_ways(w, h, seed):
    """False teachers … by reason of whom the way of the truth shall be evil spoken of: a road at dusk dividing — the way of
    the truth going on straight toward the light, and a side way turning off into the dark ravine, a fallen signpost at the
    fork. No one on either."""
    o = [sky(w, h, "#2A1A3A", "#E8903A"), halo(w * 0.7, h * 0.5, h * 0.5, "#FFE6A0", 0.6), hills(w, h, h * 0.52, seed, color="#4A3A4A", amp=14, step=90),
         f'<path d="M{f(w * 0.3)} {f(h * 0.6)} L {f(w * 0.0)} {f(h * 0.62)} L -10 {f(h + 10)} L {f(w * 0.36)} {f(h + 10)} Z" fill="#14101A" stroke="{INK}" stroke-width="2"></path>',
         ground(w, h, h * 0.58, "#7A6A4A", dy=0).replace('M-10', f'M{f(w * 0.28)}', 1)]
    o.append(f'<path d="M{f(w * 0.5)} {f(h + 10)} C {f(w * 0.52)} {f(h * 0.8)} {f(w * 0.62)} {f(h * 0.66)} {f(w * 0.7)} {f(h * 0.58)}" stroke="#E8D8A0" stroke-width="{f(max(14, h * 0.12))}" fill="none"></path>'
             f'<path d="M{f(w * 0.52)} {f(h * 0.86)} C {f(w * 0.44)} {f(h * 0.78)} {f(w * 0.34)} {f(h * 0.7)} {f(w * 0.22)} {f(h * 0.66)}" stroke="#6A5A4A" stroke-width="{f(max(8, h * 0.06))}" fill="none"></path>')
    o.append(f'<path d="M{f(w * 0.56)} {f(h * 0.84)} L {f(w * 0.64)} {f(h * 0.76)}" stroke="#5A3A22" stroke-width="5"></path>'
             f'<rect x="{f(w * 0.6)}" y="{f(h * 0.7)}" width="{f(w * 0.08)}" height="{f(h * 0.05)}" fill="#8A6A3A" stroke="{INK}" stroke-width="1.6" transform="rotate(40 {f(w * 0.64)} {f(h * 0.72)})"></rect>')
    o.append(plate_label(w * 0.72, h * 0.14, "THE WAY OF THE TRUTH", "#3A1A0A", 10, halo_="#FFE6C0") + plate_label(w * 0.18, h * 0.5, "SWIFT DESTRUCTION", "#FF8A6A", 9, halo_="#14101A"))
    return "".join(o)

def ark_noah(w, h, seed):
    """God spared not the ancient world, but preserved Noah with seven others, a preacher of righteousness: the ark riding the
    flood (as 1 Peter draws it), eight at its window."""
    return ark_eight(w, h, seed).replace("EIGHT SOULS · SAVED THROUGH WATER", "NOAH WITH SEVEN OTHERS")

def ashes_plain(p, w, h, seed):
    """Turning the cities of Sodom and Gomorrah into ashes … and delivered righteous Lot: the plain at dawn, the smoke of the
    country going up as the smoke of a furnace over the empty, blackened ground where the cities stood; at the left Lot in his
    maroon robe going away toward the hills with his daughters (Genesis' look), his back to it."""
    b = h * 0.92
    o = [D_(p), sky(w, h, "#3A1A1A", "#C86A3A"), halo(w * 0.7, h * 0.6, h * 0.6, "#FF6A2A", 0.4),
         hills(w, h, h * 0.5, seed, color="#4A2A2A", amp=14, step=100),
         f'<path d="M{f(w * 0.36)} {f(h * 0.62)} L {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.36)} {f(h + 10)} Z" fill="#2A1A1A" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M-10 {f(h * 0.62)} L {f(w * 0.36)} {f(h * 0.62)} L {f(w * 0.36)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#7A5A3A" stroke="{INK}" stroke-width="2"></path>']
    r = random.Random(seed)
    for i in range(8):                                                # the ruins, low heaps of ash and stone
        x = w * r.uniform(0.42, 0.96); y = h * r.uniform(0.66, 0.88)
        o.append(f'<path d="M{f(x - 30)} {f(y)} C {f(x - 20)} {f(y - 14)} {f(x + 10)} {f(y - 16)} {f(x + 30)} {f(y)} Z" fill="#3A3030" stroke="{INK}" stroke-width="1.4"></path>')
    o.append(smoke(w * 0.62, h * 0.5, 7, seed, color="#3A3030", op=0.65, k=max(0.8, h / 240)) + smoke(w * 0.84, h * 0.52, 6, seed + 5, color="#4A3A3A", op=0.6, k=max(0.8, h / 260)))
    s = fit(b, max(h * 0.3, b - 180))
    o.append(lot_r(p, w * 0.12, b, s, flip=False, pose="walk"))
    o.append(robed(p, w * 0.22, b, s * 0.88, "#4A5A7A", woman=True, veil="#2A3A5A", pose="walk"))
    o.append(robed(p, w * 0.3, b, s * 0.86, "#5A6A5A", woman=True, veil="#2A3A3A", pose="walk"))
    o.append(plate_label(w * 0.68, h * 0.12, "SODOM AND GOMORRAH · ASHES", "#FFE0C0", 10, halo_="#3A1A1A"))
    return "".join(o)

def empty_feast(w, h, seed):
    """Men that count it pleasure to revel in the day-time, spots and blemishes, revelling in their deceivings while they feast
    with you: a feast-hall at noon, empty, the couches pushed askew, the cups overturned and the wine spilt dark across the
    table, a garland trodden on the floor. No one in it."""
    b = h * 0.92
    o = [room(w, h, b, wall="#B8987A", floor="#7A5A3A"), f'<rect x="{f(w * 0.72)}" y="{f(h * 0.14)}" width="{f(w * 0.16)}" height="{f(h * 0.4)}" fill="#FFF4C2" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<path d="M{f(w * 0.72)} {f(h * 0.54)} L {f(w * 0.5)} {f(b)} L {f(w * 0.98)} {f(b)} L {f(w * 0.88)} {f(h * 0.54)} Z" fill="#FFF4C2" opacity="0.35"></path>']
    k = h / 300
    o.append(couch(w * 0.04, b, w * 0.26, k) + f'<g transform="rotate(-8 {f(w * 0.7)} {f(b)})">' + couch(w * 0.56, b, w * 0.24, k) + '</g>')
    tx = w * 0.32
    o.append(low_table(tx, b, w * 0.24, k * 1.2)
             + f'<path d="M{f(tx + w * 0.04)} {f(b - 36 * k)} C {f(tx + w * 0.1)} {f(b - 30 * k)} {f(tx + w * 0.16)} {f(b - 40 * k)} {f(tx + w * 0.22)} {f(b - 34 * k)} L {f(tx + w * 0.24)} {f(b - 10 * k)}" stroke="#5A0E16" stroke-width="{f(4 * k)}" fill="none"></path>')
    for i, (x, rot) in enumerate(((0.38, 90), (0.46, 0), (0.6, 80))):
        o.append(f'<g transform="rotate({rot} {f(w * x)} {f(b - 40 * k if i == 1 else b - 6 * k)})">' + cup(w * x, b - 40 * k if i == 1 else b - 6 * k, 0.3 * k, color="#C8A040") + '</g>')
    o.append("".join(f'<ellipse cx="{f(w * 0.5 + j * 9 * k)}" cy="{f(b - 4 * k + (j % 2) * 3 * k)}" rx="{f(5 * k)}" ry="{f(3 * k)}" fill="#4A7A3A" stroke="{INK}" stroke-width="0.8"></ellipse>' for j in range(6)))
    o.append(plate_label(w * 0.36, h * 0.1, "REVELLING IN THE DAY-TIME", "#3A1A0A", 10, halo_="#E8D8B8"))
    return "".join(o)

from epistle import couch

def balaam_ass(p, w, h, seed):
    """The way of Balaam the son of Beor, who loved the hire of wrong-doing; but he was rebuked for his own transgression: a
    dumb ass spake with man's voice and stayed the madness of the prophet (Numbers 22): the narrow way between the vineyard
    walls, the grey ass fallen down under Balaam, Balaam in his purple headcloth astride it, his staff raised."""
    b = h * 0.92
    o = [D_(p), sky(w, h, "#8FD0E2", "#F3E8C8"), ground(w, h, h * 0.5, "#C8A06A", dy=0)]
    for side in (-1, 1):
        x0 = w * 0.5 + side * w * 0.56
        o.append(f'<path d="M{f(x0)} {f(h * 0.28)} L {f(w * 0.5 + side * w * 0.1)} {f(h * 0.46)} L {f(w * 0.5 + side * w * 0.1)} {f(h * 0.54)} L {f(x0)} {f(h + 10)} Z" fill="#B8A88A" stroke="{INK}" stroke-width="2.4"></path>'
                 f'<path d="M{f(x0)} {f(h * 0.28)} L {f(w * 0.5 + side * w * 0.1)} {f(h * 0.46)}" stroke="#4A7A3A" stroke-width="{f(h * 0.05)}"></path>')
    s = fit(b, max(h * 0.3, b - 190))
    ax = w * 0.42
    o.append(N1.ass(ax, b, s * 1.1, flip=False, color="#8A8478"))
    staff = '<path d="M-60 -200 L -40 -60" stroke="#5A3A22" stroke-width="5" stroke-linecap="round"></path>'
    o.append(robed(p, ax - 4 * s, b - 36 * s, s * 0.9, "#4A2A5A", head="#5A1A6A", cord="#E8B830", beard="#3A2A1A", flip=True, pose="sit", seat=None,
                   up=[(-22, -158), (-40, -186), (-56, -196)], extra=staff))
    o.append(plate_label(w * 0.5, h * 0.1, "A DUMB ASS SPAKE WITH MAN'S VOICE", "#3A1A0A", 10, halo_="#F3E8C8"))
    return "".join(o)

def dry_springs(w, h, seed):
    """These are springs without water, and mists driven by a storm: at the left the stone mouth of a spring gone dry, its
    basin cracked mud; across the hills the storm driving the mist before it, the sky darkening."""
    r = random.Random(seed)
    o = [sky(w, h, "#1A1A2A", "#6A6A7A"), clouds(w, h * 0.1, seed, n=7, color="#2A2A3A", op=0.95, ry=0.08, h=h),
         hills(w, h, h * 0.5, seed, color="#3A3A44", amp=14, step=90), ground(w, h, h * 0.62, "#8A7A5A", dy=0)]
    for i in range(6):
        y = h * r.uniform(0.3, 0.56); x = w * r.uniform(0.3, 0.9)
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(w * r.uniform(0.1, 0.2))}" ry="{f(h * 0.03)}" fill="#C8C8D0" opacity="0.45"></ellipse>'
                 f'<path d="M{f(x + w * 0.1)} {f(y - 4)} l {f(w * 0.08)} -6" stroke="#C8C8D0" stroke-width="2" opacity="0.6"></path>')
    k = h / 300
    sx, sy = w * 0.22, h * 0.86
    o.append(f'<path d="M{f(sx - 80 * k)} {f(sy)} L {f(sx - 70 * k)} {f(sy - 110 * k)} C {f(sx - 30 * k)} {f(sy - 140 * k)} {f(sx + 30 * k)} {f(sy - 136 * k)} {f(sx + 70 * k)} {f(sy - 100 * k)} L {f(sx + 80 * k)} {f(sy)} Z" fill="#6A6058" stroke="{INK}" stroke-width="2.4"></path>'
             f'<ellipse cx="{f(sx)}" cy="{f(sy - 70 * k)}" rx="{f(12 * k)}" ry="{f(9 * k)}" fill="#0D0D0F"></ellipse>'
             f'<ellipse cx="{f(sx + 10 * k)}" cy="{f(sy + 6 * k)}" rx="{f(90 * k)}" ry="{f(14 * k)}" fill="#A88A5A" stroke="{INK}" stroke-width="1.6"></ellipse>')
    for i in range(9):
        x = sx + r.uniform(-70, 80) * k
        o.append(f'<path d="M{f(x)} {f(sy + r.uniform(-6, 8) * k)} l {f(r.uniform(-12, 12) * k)} {f(r.uniform(-4, 4) * k)} l {f(r.uniform(-8, 8) * k)} {f(r.uniform(-4, 4) * k)}" stroke="#5A4A2A" stroke-width="1.4" fill="none"></path>')
    o.append(plate_label(w * 0.22, h * 0.12, "SPRINGS WITHOUT WATER", "#E8E2D6", 9, halo_="#1A1A2A") + plate_label(w * 0.66, h * 0.12, "MISTS DRIVEN BY A STORM", "#E8E2D6", 9, halo_="#1A1A2A"))
    return "".join(o)

def dog_sow(w, h):
    """The true proverb (Proverbs 26:11): an emblem plate, plainly — at the left a dog turning back, at the right a sow, washed,
    going down to the mire."""
    o = [plate_bg(w, h, "2 PETER 2:22 · THE TRUE PROVERB")]
    k = min(w / 702, h / 300)
    dx, dy = w * 0.26, h * 0.78
    o.append(f'<g transform="translate({f(dx)} {f(dy)}) scale({f(k * 1.2)})">'
             '<path d="M-60 0 L -56 -34 C -60 -50 -40 -60 -10 -58 L 30 -58 C 40 -70 54 -76 66 -70 L 78 -64 L 70 -56 C 66 -50 58 -46 50 -46 L 46 -30 L 50 0 L 40 0 L 34 -26 L -30 -26 L -36 0 L -46 0 L -48 -28 C -60 -28 -70 -40 -78 -50 C -70 -46 -64 -42 -58 -40 Z" '
             'fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2.6"></path><circle cx="60" cy="-64" r="2.4" fill="#0D0D0F"></circle>'
             '<path d="M54 -72 L 50 -86 L 60 -76 Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="1.6"></path></g>')
    o.append(f'<path d="M{f(dx + 90 * k)} {f(dy - 90 * k)} C {f(dx + 120 * k)} {f(dy - 110 * k)} {f(dx + 120 * k)} {f(dy - 60 * k)} {f(dx + 96 * k)} {f(dy - 70 * k)}" stroke="{CY}" stroke-width="2" fill="none"></path>'
             f'<path d="M{f(dx + 96 * k)} {f(dy - 70 * k)} l 4 -10 M{f(dx + 96 * k)} {f(dy - 70 * k)} l 10 2" stroke="{CY}" stroke-width="2"></path>')
    sx, sy = w * 0.68, h * 0.78
    o.append(f'<ellipse cx="{f(sx + 30 * k)}" cy="{f(sy + 4 * k)}" rx="{f(110 * k)}" ry="{f(12 * k)}" fill="#3A2A1A" stroke="{CY}" stroke-width="1.2"></ellipse>')
    o.append(f'<g transform="translate({f(sx)} {f(sy)}) scale({f(k * 1.2)})">'
             '<path d="M-66 -10 C -70 -40 -40 -62 0 -62 C 40 -62 62 -46 66 -26 L 82 -24 L 82 -12 L 66 -12 C 60 -4 52 0 44 0 L 40 0 L 38 -8 L -30 -8 L -32 0 L -42 0 L -46 -10 Z" '
             'fill="#E8B8A8" stroke="#0D0D0F" stroke-width="2.6"></path><circle cx="58" cy="-34" r="2.4" fill="#0D0D0F"></circle>'
             '<path d="M44 -52 L 52 -66 L 56 -50 Z" fill="#D8A898" stroke="#0D0D0F" stroke-width="1.6"></path><path d="M-66 -24 C -76 -30 -78 -18 -70 -16" stroke="#0D0D0F" stroke-width="2" fill="none"></path></g>')
    o.append(label(dx, h * 0.94, "THE DOG · TO HIS OWN VOMIT AGAIN", CY, 9) + label(sx + 20 * k, h * 0.94, "THE SOW · TO THE MIRE", CY, 9))
    return "".join(o)

# ---- 2 Peter 3 ------------------------------------------------------------------------------------------------------------
def two_epistles(w, h, seed):
    """This is now, beloved, the second epistle that I write unto you: the two letters on the table by lamplight, the first one
    worn and opened, the second rolled and sealed, the reed pen and the lamp."""
    o = [still_life(w, h, seed, sealed=True, night=True)]
    k = min(w / 520, h / 260)
    ty = h * 0.62
    o.append(f'<g transform="rotate(-4 {f(w * 0.2)} {f(ty)})">' + open_letter(w * 0.04, ty + h * 0.05, w * 0.22, h * 0.2, rows=5, seed=seed + 1, color="#D8C8A0") + '</g>')
    o.append(plate_label(w * 0.15, ty - h * 0.06, "THE FIRST", "#FFE6A0", 9, halo_="#3A2418") + plate_label(w * 0.44, ty - h * 0.06, "THE SECOND", "#FFE6A0", 9, halo_="#3A2418"))
    return "".join(o)

def overflowed(w, h, seed):
    """The world that then was, being overflowed with water, perished: the flood over all the earth under a dark sky, the rain
    falling, only the tops of the high hills showing above the waters, and they going under."""
    r = random.Random(seed)
    o = [sky(w, h, "#14182A", "#4A5A6E"), clouds(w, h * 0.1, seed, n=7, color="#2A3040", op=0.95, ry=0.08, h=h)]
    for i in range(60):
        x = w * r.uniform(0, 1); y = h * r.uniform(0.05, 0.6)
        o.append(f'<path d="M{f(x)} {f(y)} l -4 16" stroke="#9AB0C8" stroke-width="1.4" opacity="0.6"></path>')
    for i, (x, wd, ht) in enumerate(((0.2, 0.12, 0.08), (0.56, 0.16, 0.12), (0.84, 0.1, 0.05))):
        o.append(f'<path d="M{f(w * (x - wd))} {f(h * 0.62)} L {f(w * x)} {f(h * (0.62 - ht))} L {f(w * (x + wd))} {f(h * 0.62)} Z" fill="#4A4A4A" stroke="{INK}" stroke-width="2"></path>')
    o.append(sea_(w, h, h * 0.6, seed, rough=True))
    o.append(plate_label(w * 0.5, h * 0.94, "THE WORLD THAT THEN WAS · OVERFLOWED WITH WATER", "#E8F6FA", 9, halo_="#0B2E4A"))
    return "".join(o)

def thousand_years(w, h):
    """One day is with the Lord as a thousand years, and a thousand years as one day: a balance on the plate, its beam level —
    in one pan the sun of a single day, in the other a thousand years written as a column of days."""
    o = [plate_bg(w, h, "2 PETER 3:8 · ONE DAY · A THOUSAND YEARS")]
    k = min(w / 702, h / 300)
    cx, top = w * 0.5, h * 0.24
    o.append(f'<path d="M{f(cx)} {f(top)} L {f(cx)} {f(h * 0.9)} M{f(cx - 40 * k)} {f(h * 0.9)} L {f(cx + 40 * k)} {f(h * 0.9)}" stroke="{GOLD}" stroke-width="4"></path>'
             f'<path d="M{f(cx - 200 * k)} {f(top + 10)} L {f(cx + 200 * k)} {f(top + 10)}" stroke="{GOLD}" stroke-width="5"></path>'
             f'<circle cx="{f(cx)}" cy="{f(top + 10)}" r="7" fill="{GOLD}"></circle>')
    for side in (-1, 1):
        px = cx + side * 200 * k; py = top + 10 + 110 * k
        o.append(f'<path d="M{f(px)} {f(top + 10)} L {f(px - 50 * k)} {f(py)} M{f(px)} {f(top + 10)} L {f(px + 50 * k)} {f(py)}" stroke="{CY}" stroke-width="1.4"></path>'
                 f'<path d="M{f(px - 60 * k)} {f(py)} C {f(px - 40 * k)} {f(py + 20 * k)} {f(px + 40 * k)} {f(py + 20 * k)} {f(px + 60 * k)} {f(py)} Z" fill="#2A4A6A" stroke="{CY}" stroke-width="1.6"></path>')
    lx, ly = cx - 200 * k, top + 10 + 90 * k
    o.append(halo(lx, ly - 10 * k, 40 * k, "#FFE680", 0.7) + f'<circle cx="{f(lx)}" cy="{f(ly - 10 * k)}" r="{f(18 * k)}" fill="#FFD23F" stroke="#FF8A3D" stroke-width="2"></circle>')
    rx, ry = cx + 200 * k, top + 10 + 100 * k
    for j in range(4):
        for i in range(10):
            o.append(f'<rect x="{f(rx - 46 * k + i * 9.4 * k)}" y="{f(ry - 14 * k - j * 10 * k)}" width="{f(7 * k)}" height="{f(7 * k)}" fill="{GOLD}" opacity="0.85"></rect>')
    o.append(label(lx, h * 0.92, "ONE DAY", GOLD, 10) + label(rx, h * 0.92, "A THOUSAND YEARS", GOLD, 10))
    return "".join(o)

def day_fire(w, h, seed):
    """The day of the Lord will come as a thief; in the which the heavens shall pass away with a great noise, and the elements
    shall be dissolved with fervent heat: the sky rolled back in fire and light, the earth below melting in flame, hills
    running like wax. No one drawn."""
    r = random.Random(seed)
    o = [sky(w, h, "#2A0A0A", "#FF6A2A"), halo(w * 0.5, h * 0.2, h * 0.7, "#FFF4C2", 0.7), rays(w * 0.5, h * 0.18, 40, h * 0.06, max(w, h), "#FFE680", 0.35, 5)]
    for i in range(10):                                               # the heavens rolling away like a scroll, edges burning
        y = h * (0.05 + i * 0.05); x0 = w * r.uniform(-0.1, 0.2); x1 = w * r.uniform(0.8, 1.1)
        o.append(f'<path d="M{f(x0)} {f(y)} C {f(w * 0.3)} {f(y - 12)} {f(w * 0.7)} {f(y + 12)} {f(x1)} {f(y)}" stroke="#FFD23F" stroke-width="2" fill="none" opacity="0.5"></path>')
    o.append(hills(w, h, h * 0.64, seed, color="#5A1A10", amp=20, step=80))
    for i in range(int(w / 30)):
        x = i * 30 + r.uniform(-8, 8)
        o.append(flame(x, h * 0.7 + r.uniform(-10, 10), h / 220 * r.uniform(0.6, 1.2), seed + i))
    o.append(f'<path d="M-10 {f(h * 0.78)} C {f(w * 0.3)} {f(h * 0.74)} {f(w * 0.7)} {f(h * 0.8)} {f(w + 10)} {f(h * 0.76)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#C8401A" stroke="{INK}" stroke-width="2"></path>')
    for i in range(6):
        x = w * r.uniform(0.05, 0.95)
        o.append(f'<path d="M{f(x)} {f(h * 0.78)} C {f(x + 6)} {f(h * 0.86)} {f(x - 4)} {f(h * 0.92)} {f(x + 4)} {f(h + 10)}" stroke="#FFD23F" stroke-width="4" fill="none" opacity="0.8"></path>')
    o.append(plate_label(w * 0.5, h * 0.94, "THE ELEMENTS SHALL MELT WITH FERVENT HEAT", "#FFF4C2", 10, halo_="#5A1A10"))
    return "".join(o)

def new_heavens(w, h, seed):
    """We look for new heavens and a new earth, wherein dwelleth righteousness: a clear dawn over a land renewed, green hills,
    a river running through it, trees in leaf and fruit, the light filling the sky."""
    o = [vista(w, h, seed, tone="day", horizon=0.56, sun_at=(0.5, 0.46), hills_n=2, trees=6)]
    o.append(halo(w * 0.5, h * 0.5, h * 0.8, "#FFF4C2", 0.6))
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.6)} C {f(w * 0.46)} {f(h * 0.7)} {f(w * 0.56)} {f(h * 0.8)} {f(w * 0.48)} {f(h + 10)}" stroke="#8FD0E2" stroke-width="{f(max(12, h * 0.08))}" fill="none"></path>')
    o.append(olive(w * 0.16, h * 0.86, h / 360, seed=seed) + fig_tree(w * 0.84, h * 0.88, h / 380, fruit=True, seed=seed))
    o.append(plate_label(w * 0.5, h * 0.1, "NEW HEAVENS AND A NEW EARTH", "#3A1A2A", 10, halo_="#FFE6C8"))
    return "".join(o)

PAULS = ("ROMANS", "1 CORINTHIANS", "2 CORINTHIANS", "GALATIANS", "EPHESIANS", "PHILIPPIANS", "COLOSSIANS", "1 THESSALONIANS", "2 THESSALONIANS",
         "1 TIMOTHY", "2 TIMOTHY", "TITUS", "PHILEMON")
def pauls_letters(w, h, seed):
    """Our beloved brother Paul also, according to the wisdom given to him, wrote unto you; as also in all his epistles: the
    church's case of pigeonholes by lamplight, each holding one of Paul's letters rolled and tagged with its name (Paul is not
    drawn); one taken down and lying open on the table."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2418"></rect>', lamp_glow(w * 0.8, h * 0.6, h * 0.8, "pl", op=0.5)]
    cols, rows_ = 5, 3
    x0, y0, cw, ch = w * 0.04, h * 0.1, w * 0.12, h * 0.22
    o.append(f'<rect x="{f(x0 - 8)}" y="{f(y0 - 8)}" width="{f(cw * cols + 16)}" height="{f(ch * rows_ + 16)}" fill="#5A3418" stroke="{INK}" stroke-width="2.4"></rect>')
    for i in range(cols * rows_):
        c, r_ = i % cols, i // cols
        x, y = x0 + c * cw, y0 + r_ * ch
        o.append(f'<rect x="{f(x + 2)}" y="{f(y + 2)}" width="{f(cw - 4)}" height="{f(ch - 4)}" fill="#1E120A" stroke="{INK}" stroke-width="1.2"></rect>')
        if i < len(PAULS):
            o.append(f'<circle cx="{f(x + cw / 2)}" cy="{f(y + ch * 0.42)}" r="{f(min(cw, ch) * 0.24)}" fill="#E0CFA4" stroke="{INK}" stroke-width="1.2"></circle>'
                     f'<circle cx="{f(x + cw / 2)}" cy="{f(y + ch * 0.42)}" r="{f(min(cw, ch) * 0.08)}" fill="#C8B488"></circle>'
                     + label(x + cw / 2, y + ch * 0.86, PAULS[i], "#E8C060", 6.5 if len(PAULS[i]) > 11 else 7))
    k = min(w / 520, h / 260)
    o.append(f'<path d="M{f(w * 0.66)} {f(h * 0.7)} L {f(w * 0.97)} {f(h * 0.7)} L {f(w * 0.97)} {f(h * 0.76)} L {f(w * 0.66)} {f(h * 0.76)} Z" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></path>'
             + "".join(f'<rect x="{f(lx)}" y="{f(h * 0.76)}" width="{f(w * 0.02)}" height="{f(h * 0.1)}" fill="#4A2412" stroke="{INK}" stroke-width="1.4"></rect>' for lx in (w * 0.68, w * 0.93))
             + open_letter(w * 0.69, h * 0.58, w * 0.17, h * 0.11, rows=4, seed=seed) + clay_lamp(w * 0.92, h * 0.7, k))
    o.append(plate_label(w * 0.34, h * 0.86, "IN ALL HIS EPISTLES", "#FFE6A0", 10, halo_="#3A2418"))
    return "".join(o)
