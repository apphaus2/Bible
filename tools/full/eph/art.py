"""Drawings for the Ephesians volume, chapter 1 (Ephesians 1–3); art2.py has chapter 2's. Ephesians starts from all of
Galatians' drawings (`from gal.art import *`, which carries Acts', Mark's and Matthew's drawings and the epistle kit) and
adds its own.

Ephesians' people at a distance, on the kit silhouettes: Paul only ever epistle.paul_fig (sitting on his bench, standing,
walking) or kneeling (paul_kneel); the soldier that guarded him epistle.roman_guard; Tychicus (tychicus) a slate-teal
headcloth with a dark cord, a short brown beard, a grey-blue robe and a grey travelling cloak; the scribe at Rome
(SCRIBE_LOOK) a dark slate headcloth and a black beard. God is never drawn (light); Christ is not drawn in this volume (the
head of the body is a disc of light on the plates). Every function takes (p, w, h, seed, ...) or (w, h, ...); p, a prefix
unique to the panel, names the figure defs and gradients. The kit clips every drawing to its panel (EpistleKit clip=True)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from gal.art import *
from gal.art import _person_mark
from act.art import f, INK
from epistle import (study, roman_guard, guard_hand, robed_hand, chain, rome_window, bench, stool, SEAT_Y, GUARD_LOOK, still_life, open_letter, reed_pen,
                     inkpot, lamp_glow, sealed_scroll, plate_bg, radiance, robed, paul_fig, letter_road, SEPIA, SEAL)
from exo.art import headcloth
from exo.art8 import tag, dim
import exo.art8 as B8
from act import geo
from eph.common import TYCHICUS_LOOK, SCRIBE_LOOK
from ntcast import ROBES

GOLD, CY, NAVY = "#FFD23F", "#8FD0E2", "#0B1A2E"
PRAY = [(-22, -158), (-34, -184), (-40, -214)]                     # an arm lifted up in prayer (robed up= points)

def art(fn, *a, **k):
    """A panel's drawing as fn(w, h): fn(p, w, h, seed, ...) when the first argument is a prefix string, else fn(w, h, ...)
    (the kit clips it to its panel)."""
    def draw(w, h):
        return fn(*a[:1], w, h, *a[1:], **k) if a and isinstance(a[0], str) else fn(w, h, *a, **k)
    draw.__name__ = fn.__name__
    return draw

def lab(x, y, text, color=GOLD, size=10, anchor="middle", halo_=NAVY):
    """A plate label with a dark halo (plate_label), the text escaped for the EPUB."""
    return plate_label(x, y, text.replace("&", "&amp;"), color, size, anchor, halo_)

def callout(x0, y0, x1, ty, lines, side=None):
    """A plate callout: a dot on the part, a leader to the margin at x1 (left or right of the part), and the label lines
    stacked there, anchored at the margin so they never run off the plate (lines: (text, color, size))."""
    side = side or ("l" if x1 < x0 else "r")
    anchor = "start" if side == "l" else "end"
    ex = x1 + (150 if side == "l" else -150)
    c = lines[0][1]
    out = [f'<circle cx="{f(x0)}" cy="{f(y0)}" r="3.2" fill="{c}"></circle><path d="M{f(x0)} {f(y0)} L {f(ex)} {f(ty)} L {f(x1 + (4 if side == "l" else -4))} {f(ty)}" stroke="{c}" stroke-width="1.2" fill="none"></path>']
    for j, (t, col, sz) in enumerate(lines):
        out.append(lab(x1, ty - 6 if j == 0 else ty + 8 + (j - 1) * 12, t, col, sz, anchor))
    return "".join(out)

# ---- Ephesians' cast at a distance ----------------------------------------------------------------------------------------
def tychicus(p, x, y, s, flip=False, up=None, extra="", pose="stand"):
    """Tychicus, the beloved brother and faithful minister (6:21): slate-teal headcloth, short brown beard, grey travelling cloak."""
    L = TYCHICUS_LOOK
    return robed(p, x, y, s, L["cloth"], head=L["head"], cord=L["cord"], beard=L["beard"], mantle=L["mantle"], belt="#2A2A30", flip=flip, up=up, extra=extra, pose=pose)

def prison(p, w, h, seed, stage="prison", **k):
    """Paul's own hired dwelling at Rome (epistle.study's prison stages) with Ephesians' people: the scribe at Rome on his
    mat, Tychicus the bearer."""
    k.setdefault("scribe", SCRIBE_LOOK)
    k.setdefault("fig_h", min(h * 0.72, w * 0.42))                 # a tall panel does not blow the room up past its width
    if stage == "prison_give": k.setdefault("bearer", tychicus)
    return study(p, w, h, seed, stage=stage, **k)

def paul_kneel(x, y, s, flip=False):
    """Paul kneeling (exodus.kneel's figure in his robe, his darker mantle over the back, his girdle, the sole of his foot
    behind; his headcloth and beard drawn in profile), his hands lifted before his face in prayer; facing right (left with
    flip=True)."""
    sx = -s if flip else s
    c = ROBES["paul"]
    cid = f"pk{abs(int(x))}x{abs(int(y))}"
    arm = "M-6 -100 L 20 -90 L 40 -112"
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">'
            f'<defs><clipPath id="{cid}"><path d="{E.KNEEL}"></path></clipPath></defs>'
            '<path d="M-58 -2 L -76 -6 C -80 -4 -80 0 -76 1 L -56 2 Z" fill="#C98E66" stroke="#0D0D0F" stroke-width="1.4"></path>'
            f'<path d="{E.KNEEL}" fill="{c}" stroke="{INK}" stroke-width="2"></path>'
            f'<path d="M-70 10 L -60 -60 C -54 -90 -40 -112 -10 -112 L 0 -102 C -20 -96 -34 -76 -40 -40 L -34 10 Z" fill="#3E3228" clip-path="url(#{cid})"></path>'
            '<path d="M-52 -46 C -30 -40 -6 -40 14 -36" fill="none" stroke="#2A1A10" stroke-width="3.4"></path>'
            f'<path d="{E.KNEEL}" fill="none" stroke="{INK}" stroke-width="2"></path>'
            f'<path d="{E.KNEEL_HEAD}" fill="{SKIN}" stroke="{INK}" stroke-width="2"></path>'
            '<path d="M29 -122 L 33 -117 L 29 -115" fill="#C98E66" stroke="#0D0D0F" stroke-width="1.2"></path>'
            # his beard, and his headcloth drawn in profile: over the crown and falling behind the neck, the cord about it
            f'<path d="M23 -115 C 31 -113 31 -104 25 -99 C 20 -100 17 -106 18 -112 Z" fill="#3A2A1A" stroke="{INK}" stroke-width="1.4"></path>'
            f'<path d="M27 -127 C 24 -138 8 -138 3 -126 C 0 -118 -2 -108 -10 -94 L 2 -98 C 6 -106 8 -114 10 -119 C 14 -124 22 -126 27 -125 Z" fill="#5A4A3A" stroke="{INK}" stroke-width="1.8"></path>'
            '<path d="M26 -128 C 20 -132 10 -132 4 -125" fill="none" stroke="#2A1A10" stroke-width="2.6"></path>'
            f'<path d="{arm}" fill="none" stroke="{INK}" stroke-width="13.5" stroke-linecap="round" stroke-linejoin="round"></path>'
            f'<path d="{arm}" fill="none" stroke="{c}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"></path>'
            f'<ellipse cx="42" cy="-116" rx="4.6" ry="7" transform="rotate(20 42 -116)" fill="{SKIN}" stroke="{INK}" stroke-width="1.6"></ellipse>'
            '<path d="M-44 -40 C -30 -30 -6 -24 24 -20 M-40 -80 C -30 -60 -20 -40 -4 -30" fill="none" stroke="#12090A" stroke-width="1.4" opacity="0.6"></path></g>')

def theatre_hill(cx, base, rw, color="#9A8A70", stone="#E8DCC0", tiers=6):
    """The theatre of Ephesus cut into its hill, far off: the hill, the half-bowl of tiers, the stage building below."""
    o = [f'<path d="M{f(cx - rw * 2.2)} {f(base)} C {f(cx - rw * 1.4)} {f(base - rw * 1.3)} {f(cx + rw * 0.6)} {f(base - rw * 1.5)} {f(cx + rw * 2.4)} {f(base)} Z" fill="{color}" stroke="{INK}" stroke-width="2"></path>']
    for k in range(tiers):
        r_ = rw * (1 - k * 0.12)
        o.append(f'<path d="M{f(cx - r_)} {f(base - rw * 0.2)} A {f(r_)} {f(r_ * 0.6)} 0 0 1 {f(cx + r_)} {f(base - rw * 0.2)}" fill="none" stroke="{stone}" stroke-width="{f(max(1.6, rw * 0.05))}"></path>')
    o.append(f'<rect x="{f(cx - rw * 0.7)}" y="{f(base - rw * 0.22)}" width="{f(rw * 1.4)}" height="{f(rw * 0.14)}" fill="{stone}" stroke="{INK}" stroke-width="1.4"></rect>')
    return "".join(o)

def ephesus_dawn(w, h, seed):
    """Ephesus at sunrise: the hills of Asia, the theatre cut into the hill above the city, the white roofs running down to
    the harbour, and far off on the plain the temple of Diana."""
    o = [sky(w, h, "#2A1E3A", "#FFB07A"), halo(w * 0.7, h * 0.4, h * 0.5, "#FFD08A", 0.5),
         f'<circle cx="{f(w * 0.7)}" cy="{f(h * 0.4)}" r="{f(h * 0.06)}" fill="#FFE6A0"></circle>',
         hills(w, h, h * 0.38, seed, color="#6A5A7A", amp=20, step=110), hills(w, h, h * 0.48, seed + 1, color="#8A6A6A", amp=14, step=90),
         diana_temple(w * 0.82, h * 0.58, w * 0.2), theatre_hill(w * 0.32, h * 0.6, w * 0.13),
         ground(w, h, h * 0.6, "#B08A5A", dy=0),
         houses(w, h, h * 0.74, seed, hmin=0.08, hmax=0.14, stairs=False), sea(w, h, h * 0.82, seed, color="#3A6A8A", deep="#1F4A6A"),
         birds(5, w * 0.1, w * 0.6, h * 0.12, h * 0.28, seed)]
    return "".join(o)

# ---- Ephesians 1 ----------------------------------------------------------------------------------------------------------
BRUNDISIUM = (17.94, 40.64)

def eph_road(w, h):
    """The letter's road (6:21–22): from Rome down the Appian Way to Brundisium, across the sea to Macedonia, along the road
    by Thessalonica and Philippi to Neapolis, over to Troas and down the coast of Asia to Ephesus — on Acts' map."""
    box = (11.4, 28.6, 36.8, 43.2)
    rt = ["ROME", (13.6, 41.4), (14.8, 41.13), (16.4, 40.9), BRUNDISIUM, (19.45, 41.32), (20.6, 41.1), (21.6, 40.9), "THESSALONICA", "AMPHIPOLIS",
          "PHILIPPI", "NEAPOLIS", (25.4, 40.3), "TROAS", (26.4, 39.2), (26.7, 38.5), "EPHESUS"]
    o = letter_road(w, h, rt, title="EPHESIANS 6:21 · FROM ROME TO EPHESUS", box=box,
                    places=("ROME", "THESSALONICA", "PHILIPPI", "NEAPOLIS", "TROAS", "EPHESUS"), hi=("ROME", "EPHESUS"),
                    regions=("ITALY", "MACEDONIA", "ACHAIA", "ASIA"))
    x, y = geo.Proj(w, h, box)(*BRUNDISIUM)
    return (o + f'<circle cx="{f(x)}" cy="{f(y)}" r="4" fill="#FFD23F" stroke="{INK}" stroke-width="1.4"></circle>'
            + lab(x + 8, y + 14, "BRUNDISIUM", "#FFD23F", 9, "start"))

def heavenly(w, h, seed):
    """Every spiritual blessing in the heavenly places: light pouring down from above the heavens through tier on tier of
    luminous cloud, stars at the edges of the dark, and far below the dark rim of the earth (no figure)."""
    o = [sky(w, h, "#2A1E5A", "#0B0B2A"), starfield(w, h, seed, int(w * h / 3000) + 30, 0.95)]
    x, y = w * 0.5, -h * 0.08
    o.append(halo(x, y, max(w, h) * 0.9, "#FFE680", 0.5) + rays(x, y, 44, h * 0.1, max(w, h) * 1.4, "#FFF4C2", 0.22, 6))
    r = random.Random(seed)
    for i in range(5):
        cy = h * (0.18 + 0.13 * i); op = 0.55 - i * 0.08
        for _ in range(7):
            cx = r.uniform(-0.1, 1.1) * w; rw = w * r.uniform(0.14, 0.3); rh = h * r.uniform(0.025, 0.05)
            o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy + r.uniform(-8, 8))}" rx="{f(rw)}" ry="{f(rh)}" fill="#FFF4D8" opacity="{op:.2f}"></ellipse>')
    o.append(halo(x, y, max(w, h) * 0.3, "#FFFFFF", 0.9))
    o.append(f'<path d="M-10 {f(h + 10)} L -10 {f(h * 0.9)} C {f(w * 0.3)} {f(h * 0.84)} {f(w * 0.7)} {f(h * 0.84)} {f(w + 10)} {f(h * 0.9)} L {f(w + 10)} {f(h + 10)} Z" fill="#0D0B1E" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M-10 {f(h * 0.9)} C {f(w * 0.3)} {f(h * 0.84)} {f(w * 0.7)} {f(h * 0.84)} {f(w + 10)} {f(h * 0.9)}" fill="none" stroke="#FFC14D" stroke-width="2" opacity="0.7"></path>')
    return "".join(o)

def _signet(x, y, s):
    """A signet ring seen from the side, its bezel down (pressing), (x, y) the bezel's face."""
    return (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">'
            f'<ellipse cx="0" cy="-34" rx="22" ry="26" fill="none" stroke="{INK}" stroke-width="9"></ellipse>'
            f'<ellipse cx="0" cy="-34" rx="22" ry="26" fill="none" stroke="#E8B830" stroke-width="5.5"></ellipse>'
            f'<rect x="-14" y="-12" width="28" height="12" rx="3" fill="#C8963E" stroke="{INK}" stroke-width="2"></rect></g>')

def seal_earnest(w, h):
    """Sealed with the Holy Spirit of promise, which is an earnest of our inheritance: a plate in two halves — at the left
    the seal, a deed with the red clay seal pressed on it and the signet ring lifted from it; at the right the earnest, the
    first coins of the price set down on a deed of purchase, a dimension line running from them to the full purse they
    pledge (the whole inheritance to come)."""
    o = [plate_bg(w, h, "EPHESIANS 1:13–14 · THE SEAL AND THE EARNEST")]
    top = 34; H = h - top
    k = min(H / 250, w / 702)
    o.append(f'<path d="M{f(w / 2)} {f(top + 12)} L {f(w / 2)} {f(h - 28)}" stroke="#2C5A7A" stroke-width="1.4" stroke-dasharray="5 5"></path>')
    # the seal
    cx, cy = w * 0.25, top + H * 0.58
    dw, dh = 170 * k, 100 * k
    o.append(lab(cx, top + 24, "THE SEAL · 1:13", GOLD, 11) + lab(cx, top + 39, "SEALED WITH THE HOLY SPIRIT OF PROMISE", CY, 8))
    o.append(f'<g transform="rotate(-4 {f(cx)} {f(cy)})">' + open_letter(cx - dw / 2, cy - dh / 2, dw, dh, rows=6, seed=3) + '</g>')
    sx_, sy_ = cx + dw * 0.3, cy + dh * 0.32
    o.append(halo(sx_, sy_, 40 * k, "#FFE680", 0.45)
             + f'<circle cx="{f(sx_)}" cy="{f(sy_)}" r="{f(16 * k)}" fill="{SEAL}" stroke="{INK}" stroke-width="2"></circle>'
             f'<circle cx="{f(sx_)}" cy="{f(sy_)}" r="{f(9 * k)}" fill="none" stroke="#7A0A10" stroke-width="2"></circle>'
             + _signet(sx_, sy_ - 34 * k, 0.9 * k)
             + f'<path d="M{f(sx_)} {f(sy_ - 30 * k)} L {f(sx_)} {f(sy_ - 18 * k)}" stroke="{GOLD}" stroke-width="1.4" stroke-dasharray="3 3"></path>')
    # the earnest
    ex, ey = w * 0.7, top + H * 0.62
    o.append(lab(w * 0.75, top + 24, "THE EARNEST · 1:14", GOLD, 11) + lab(w * 0.75, top + 39, "A PLEDGE OF OUR INHERITANCE", CY, 8))
    o.append(f'<g transform="rotate(3 {f(ex)} {f(ey)})">' + open_letter(ex - 75 * k, ey - 32 * k, 120 * k, 76 * k, rows=5, seed=8, color="#E0D0A8") + '</g>')
    for i in range(3):
        o.append(f'<ellipse cx="{f(ex - 30 * k + i * 15 * k)}" cy="{f(ey + 8 * k - i * 4 * k)}" rx="{f(11 * k)}" ry="{f(4.5 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="1.6"></ellipse>')
    px, py = w * 0.9, ey + 10 * k
    o.append(f'<path d="M{f(px - 34 * k)} {f(py + 36 * k)} C {f(px - 44 * k)} {f(py)} {f(px - 26 * k)} {f(py - 28 * k)} {f(px - 10 * k)} {f(py - 30 * k)} L {f(px + 10 * k)} {f(py - 30 * k)} '
             f'C {f(px + 26 * k)} {f(py - 28 * k)} {f(px + 44 * k)} {f(py)} {f(px + 34 * k)} {f(py + 36 * k)} Z" fill="#8A5A2A" stroke="{INK}" stroke-width="2.2"></path>'
             f'<path d="M{f(px - 12 * k)} {f(py - 30 * k)} C {f(px - 18 * k)} {f(py - 42 * k)} {f(px + 18 * k)} {f(py - 42 * k)} {f(px + 12 * k)} {f(py - 30 * k)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(px - 14 * k)} {f(py - 27 * k)} L {f(px + 14 * k)} {f(py - 27 * k)}" stroke="#E8B830" stroke-width="3"></path>'
             + "".join(f'<ellipse cx="{f(px + dx * k)}" cy="{f(py - 36 * k)}" rx="{f(6 * k)}" ry="{f(2.6 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="1.2"></ellipse>' for dx in (-5, 5)))
    o.append(dim(ex - 20 * k, ey - 48 * k, px, ey - 48 * k, "THE WHOLE TO COME", off=0, size=7.5, color=GOLD))
    o.append(lab(w * 0.5, h - 12, "UNTO THE REDEMPTION OF GOD'S OWN POSSESSION · UNTO THE PRAISE OF HIS GLORY", CY, 8))
    return "".join(o)

def far_above(w, h):
    """Far above all rule, and authority, and power, and dominion: a plate of ranks — at the top, a field of gold light
    marked "at his right hand, in the heavenly places" (no throne, no figure), a disc of light for Christ raised from the
    dead; below it, far down, the ranks as bands of dimmer light one under another, each named; a dimension line "far
    above" between; at the foot "all things in subjection under his feet", and the church, his body."""
    o = [plate_bg(w, h, "EPHESIANS 1:20–23 · FAR ABOVE ALL RULE")]
    top = 40
    gy0, gy1 = top + 8, top + (h - top) * 0.22
    o.append(halo(w * 0.5, gy0 + 20, (h - top) * 0.38, "#FFE680", 0.55)
             + f'<rect x="{f(w * 0.2)}" y="{f(gy0)}" width="{f(w * 0.6)}" height="{f(gy1 - gy0)}" fill="#FFE680" opacity="0.28" stroke="{GOLD}" stroke-width="2"></rect>'
             + halo(w * 0.5, (gy0 + gy1) / 2, (gy1 - gy0) * 0.55, "#FFFFFF", 0.95)
             + lab(w * 0.5, gy0 + 14, "AT HIS RIGHT HAND · IN THE HEAVENLY PLACES", "#12113A", 10, halo_="#FFF4C2")
             + lab(w * 0.5, gy1 - 8, "CHRIST · RAISED FROM THE DEAD", "#12113A", 9, halo_="#FFF4C2"))
    ranks = ["RULE", "AUTHORITY", "POWER", "DOMINION", "EVERY NAME THAT IS NAMED"]
    ry0, ry1 = top + (h - top) * 0.42, top + (h - top) * 0.8
    n = len(ranks); bh = (ry1 - ry0) / n
    for i, nm in enumerate(ranks):
        y = ry0 + i * bh; inset = w * (0.24 - 0.03 * i)
        o.append(f'<path d="M{f(inset)} {f(y + 4)} L {f(w - inset)} {f(y + 4)} L {f(w - inset + w * 0.03)} {f(y + bh - 4)} L {f(inset - w * 0.03)} {f(y + bh - 4)} Z" '
                 f'fill="#8FD0E2" opacity="{0.34 - 0.05 * i:.2f}" stroke="{CY}" stroke-width="1.4"></path>'
                 + lab(w * 0.5, y + bh / 2 + 4, nm, "#E8F6FA", 10))
    o.append(dim(w * 0.5, gy1 + 6, w * 0.5, ry0 - 6, "FAR ABOVE", size=9, color=GOLD))
    o.append(lab(w * 0.07, (ry0 + ry1) / 2 - 8, "NOT ONLY IN", CY, 8, "start") + lab(w * 0.07, (ry0 + ry1) / 2 + 6, "THIS WORLD", CY, 8, "start")
             + lab(w * 0.93, (ry0 + ry1) / 2 - 8, "BUT ALSO IN THAT", CY, 8, "end") + lab(w * 0.93, (ry0 + ry1) / 2 + 6, "WHICH IS TO COME", CY, 8, "end"))
    fy = ry1 + (h - ry1) * 0.42
    o.append(f'<path d="M{f(w * 0.1)} {f(ry1 + 6)} L {f(w * 0.9)} {f(ry1 + 6)}" stroke="{GOLD}" stroke-width="2"></path>'
             + lab(w * 0.5, fy, "ALL THINGS IN SUBJECTION UNDER HIS FEET · HEAD OVER ALL THINGS TO THE CHURCH", GOLD, 9)
             + lab(w * 0.5, fy + 16, "WHICH IS HIS BODY · THE FULNESS OF HIM THAT FILLETH ALL IN ALL", CY, 8))
    return "".join(o)

# ---- Ephesians 2 ----------------------------------------------------------------------------------------------------------
def air_dark(w, h, seed):
    """Dead through your trespasses … according to the prince of the powers of the air: the roofs of Ephesus by night under a
    low, heavy sky, the clouds driven by the wind, the temple of Diana dim on the plain — no figure in the sky, no one in
    the streets."""
    o = [sky(w, h, "#05040C", "#2A1E36"), starfield(w, h, seed, 14, 0.25)]
    r = random.Random(seed)
    for i in range(6):
        y = h * (0.06 + 0.09 * i)
        for _ in range(5):
            cx = r.uniform(-0.2, 1.2) * w; rw = w * r.uniform(0.2, 0.42)
            o.append(f'<path d="M{f(cx - rw)} {f(y + 14)} C {f(cx - rw * 0.6)} {f(y - 18)} {f(cx + rw * 0.2)} {f(y - 26)} {f(cx + rw)} {f(y + 10)} Z" fill="{r.choice(("#1A1424", "#221A2E", "#2E2438", "#16101E"))}" opacity="0.85"></path>')
    for _ in range(9):
        y = r.uniform(0.1, 0.5) * h; x = r.uniform(0, w)
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x + 40)} {f(y - 6)} {f(x + 90)} {f(y + 4)} {f(x + 150)} {f(y - 4)}" fill="none" stroke="#5A4A6A" stroke-width="1.6" opacity="0.6"></path>')
    o.append(diana_temple(w * 0.8, h * 0.66, w * 0.22).replace("#F8F4EC", "#545066").replace("#F3EFE6", "#4A4458").replace("#D8D0C0", "#3A3448").replace("#E8E0D0", "#443E52"))
    o.append(houses(w, h, h * 0.96, seed, hmin=0.2, hmax=0.34, shut=True, color=("#2E2838", "#262030", "#342C3E", "#2A2434")))
    return "".join(o)

def workmanship(w, h):
    """For we are his workmanship: a craftsman's plate — a turned and carved vessel drawn in elevation with its centre line
    and dimension lines, the maker's compasses, square and chisel laid by it; from its foot a dotted path of footsteps going
    on (the good works afore prepared, that we should walk in them)."""
    o = [plate_bg(w, h, "EPHESIANS 2:10 · HIS WORKMANSHIP")]
    top = 40; ch = h - top
    cx, by = w * 0.42, top + ch * 0.9
    k = min(ch / 260, w / 702)
    vh = 210 * k
    prof = [(0, 0), (34, 0), (30, 10), (44, 40), (62, 90), (60, 130), (40, 170), (26, 186), (30, 200), (40, 210), (0, 210)]
    right = " L ".join(f"{f(cx + x * k)} {f(by - y * k)}" for x, y in prof)
    left = " L ".join(f"{f(cx - x * k)} {f(by - y * k)}" for x, y in reversed(prof))
    o.append(halo(cx, by - vh * 0.55, vh * 0.7, "#FFE680", 0.3)
             + f'<path d="M{right} L {left} Z" fill="#C8783A" stroke="{GOLD}" stroke-width="2.4"></path>'
             + f'<path d="M{f(cx - 60 * k)} {f(by - 110 * k)} C {f(cx - 20 * k)} {f(by - 100 * k)} {f(cx + 20 * k)} {f(by - 100 * k)} {f(cx + 60 * k)} {f(by - 110 * k)}" fill="none" stroke="#FFE680" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(cx + dx * k)} {f(by - 70 * k)} l {f(8 * k)} {f(-16 * k)} l {f(8 * k)} {f(16 * k)}" fill="none" stroke="#FFE680" stroke-width="1.8"></path>' for dx in (-40, -20, 0, 20))
             + f'<path d="M{f(cx)} {f(by + 10)} L {f(cx)} {f(by - vh - 12)}" stroke="{CY}" stroke-width="1" stroke-dasharray="8 4 2 4"></path>')
    o.append(dim(cx + 84 * k, by, cx + 84 * k, by - vh, "CREATED IN CHRIST JESUS", off=0, size=8, color=GOLD))
    # the tools, in a column at the left
    kt = min(k, (ch - 24) / 270)
    tx, ty = w * 0.1, top + 16
    o.append(f'<g transform="translate({f(tx)} {f(ty)}) scale({f(kt)})"><path d="M0 0 L -22 90 M0 0 L 22 90" stroke="{CY}" stroke-width="3" fill="none"></path><circle cx="0" cy="0" r="6" fill="none" stroke="{CY}" stroke-width="2.4"></circle>'
             f'<path d="M-30 120 L 30 120 L 30 128 L -22 128 L -22 180 L -30 180 Z" fill="none" stroke="{CY}" stroke-width="2.4"></path>'
             f'<path d="M-10 200 L 10 200 L 6 250 L -6 250 Z M-3 250 L 0 266 L 3 250" fill="none" stroke="{CY}" stroke-width="2.4"></path></g>')
    o.append(lab(tx + 34 * kt, ty + 50 * kt, "COMPASSES", CY, 8, "start") + lab(tx + 38 * kt, ty + 150 * kt, "SQUARE", CY, 8, "start") + lab(tx + 20 * kt, ty + 230 * kt, "CHISEL", CY, 8, "start"))
    # footsteps on the path afore prepared
    for i in range(7):
        fx = cx + 120 * k + i * 30 * k; fy = by - 4 - i * 5 * k + (5 * k if i % 2 else 0)
        o.append(f'<ellipse cx="{f(fx)}" cy="{f(fy)}" rx="{f(8 * k)}" ry="{f(3.6 * k)}" fill="#FFE680" opacity="{0.9 - i * 0.1:.2f}"></ellipse>')
    o.append(f'<path d="M{f(cx + 110 * k)} {f(by + 4)} C {f(cx + 200 * k)} {f(by - 20 * k)} {f(w * 0.85)} {f(by - 50 * k)} {f(w + 10)} {f(by - 80 * k)}" fill="none" stroke="{GOLD}" stroke-width="1.6" stroke-dasharray="3 6"></path>'
             + lab(w * 0.8, by - 110 * k, "GOOD WORKS · AFORE PREPARED", GOLD, 9) + lab(w * 0.8, by - 95 * k, "THAT WE SHOULD WALK IN THEM", CY, 8))
    return "".join(o)

def temple_courts(w, h, broken=False):
    """The temple courts in plan (2:11–18), drawn at a fixed shape whatever the panel: the great outer court of the
    Gentiles, and within it the low stone balustrade (the soreg) about the inner courts — the court of the women, the court
    of Israel, the house with its holy place, the altar — the warning stones set on it; the Gentiles far off outside it,
    Israel within. broken=True: the middle wall of partition broken down, its stones fallen, light through the gaps, and
    both coming in together by one way to the altar."""
    title = "EPHESIANS 2:14–18 · THE MIDDLE WALL OF PARTITION BROKEN DOWN" if broken else "EPHESIANS 2:11–13 · THE TEMPLE COURTS · FAR OFF"
    o = [plate_bg(w, h, title), mk.defs("gp", *ALL)]
    top = 30
    PW = min(w * 0.9, (h - top - 30) * 2.0); PH = PW / 2.0
    x0 = (w - PW) / 2; y0 = top + (h - top - 22 - PH) / 2 + 4; x1, y1 = x0 + PW, y0 + PH
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(PW)}" height="{f(PH)}" fill="#3A4A5A" opacity="0.35" stroke="{CY}" stroke-width="2.4"></rect>'
             + "".join(f'<rect x="{f(x0 + 6 + i * (PW - 16) / 22)}" y="{f(y0 + 4)}" width="4" height="4" fill="{CY}"></rect><rect x="{f(x0 + 6 + i * (PW - 16) / 22)}" y="{f(y1 - 8)}" width="4" height="4" fill="{CY}"></rect>' for i in range(23)))
    sx0, sy0, sx1, sy1 = x0 + PW * 0.2, y0 + PH * 0.2, x0 + PW * 0.86, y0 + PH * 0.8
    if broken:
        r = random.Random(7)
        o.append(halo((sx0 + sx1) / 2, (sy0 + sy1) / 2, (sx1 - sx0) * 0.55, "#FFE680", 0.35))
        for (ax, ay, bx, by_) in ((sx0, sy0, sx1, sy0), (sx1, sy0, sx1, sy1), (sx1, sy1, sx0, sy1), (sx0, sy1, sx0, sy0)):
            t = 0.0
            while t < 1:
                t1 = min(1, t + r.uniform(0.08, 0.14))
                if r.random() < 0.4:
                    o.append(f'<path d="M{f(ax + (bx - ax) * t)} {f(ay + (by_ - ay) * t)} L {f(ax + (bx - ax) * t1)} {f(ay + (by_ - ay) * t1)}" stroke="#C8C0B0" stroke-width="5" stroke-dasharray="3 2"></path>')
                else:
                    for _ in range(3):
                        mx = ax + (bx - ax) * r.uniform(t, t1) + r.uniform(-9, 9); my = ay + (by_ - ay) * r.uniform(t, t1) + r.uniform(-9, 9)
                        o.append(f'<rect x="{f(mx)}" y="{f(my)}" width="7" height="5" fill="#8A8A90" stroke="{INK}" stroke-width="1" transform="rotate({r.randint(-40, 40)} {f(mx)} {f(my)})"></rect>')
                t = t1
    else:
        o.append(f'<rect x="{f(sx0)}" y="{f(sy0)}" width="{f(sx1 - sx0)}" height="{f(sy1 - sy0)}" fill="none" stroke="#C8C0B0" stroke-width="5" stroke-dasharray="3 2"></rect>')
        for (wx, wy) in ((sx0 + (sx1 - sx0) * 0.3, sy0), (sx0 + (sx1 - sx0) * 0.7, sy0), (sx1, (sy0 + sy1) / 2), (sx0 + (sx1 - sx0) * 0.5, sy1), (sx0, (sy0 + sy1) / 2)):
            o.append(f'<rect x="{f(wx - 7)}" y="{f(wy - 5)}" width="14" height="10" fill="{GOLD}" stroke="{INK}" stroke-width="1.2"></rect>')
    cw0, cw1 = sx0 + (sx1 - sx0) * 0.64, sx1 - 12
    iy0, iy1 = sy0 + 14, sy1 - 14
    o.append(f'<rect x="{f(cw0)}" y="{f(iy0 + 8)}" width="{f(cw1 - cw0)}" height="{f(iy1 - iy0 - 16)}" fill="#24506E" stroke="{CY}" stroke-width="2"></rect>'
             f'<rect x="{f(sx0 + 12)}" y="{f(iy0)}" width="{f(cw0 - sx0 - 20)}" height="{f(iy1 - iy0)}" fill="#1E4A6A" stroke="{CY}" stroke-width="2"></rect>')
    hx0, hx1 = sx0 + 26, sx0 + (cw0 - sx0) * 0.58
    hy0, hy1 = (iy0 + iy1) / 2 - (iy1 - iy0) * 0.2, (iy0 + iy1) / 2 + (iy1 - iy0) * 0.2
    o.append(f'<rect x="{f(hx0)}" y="{f(hy0)}" width="{f(hx1 - hx0)}" height="{f(hy1 - hy0)}" fill="#C8963E" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(hx0 + (hx1 - hx0) * 0.33)} {f(hy0)} L {f(hx0 + (hx1 - hx0) * 0.33)} {f(hy1)}" stroke="{INK}" stroke-width="2"></path>')
    ax_ = hx1 + (cw0 - hx1) * 0.45; ay_ = (hy0 + hy1) / 2
    o.append(f'<rect x="{f(ax_ - 9)}" y="{f(ay_ - 9)}" width="18" height="18" fill="#8A8A90" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(lab((hx0 + hx1) / 2, hy0 - 6, "THE HOUSE", GOLD, 8) + lab(ax_, ay_ + 22, "ALTAR", CY, 7) + lab((cw0 + cw1) / 2, iy0 + 22, "COURT OF", CY, 7.5)
             + lab((cw0 + cw1) / 2, iy0 + 33, "THE WOMEN", CY, 7.5) + lab((sx0 + cw0) / 2, iy1 - 7, "COURT OF ISRAEL", CY, 7.5))
    o.append(lab((x0 + sx0) / 2, y0 + PH * 0.42, "COURT OF", CY, 8) + lab((x0 + sx0) / 2, y0 + PH * 0.42 + 12, "THE", CY, 8)
             + lab((x0 + sx0) / 2, y0 + PH * 0.42 + 24, "GENTILES", CY, 8))
    s_ = PH / 1500
    if broken:
        o.append(lab(w * 0.5, sy0 - 7, "BROKEN DOWN · 2:14", GOLD, 9) + lab(w * 0.5, h - 10, "ONE NEW MAN · BOTH IN ONE BODY · ACCESS IN ONE SPIRIT", GOLD, 9))
        pts = ((x1 - 18, sy1 + PH * 0.12), (x1 - 40, sy1 + PH * 0.08), (sx1 - 30, sy1 - PH * 0.04), (sx1 - 54, sy1 - PH * 0.08))
        for i, (px, py) in enumerate(pts):
            o.append(_person_mark(px, py, s_ * 1.4, "#24506E" if i % 2 else "#2C5A7A", head=i % 2 == 0, flip=True, stroke=GOLD))
        o.append(f'<path d="M{f(x1 - 8)} {f(sy1 + PH * 0.06)} C {f(sx1 + 10)} {f(sy1 - 10)} {f(cw0 + 30)} {f(ay_ + 10)} {f(ax_ + 14)} {f(ay_)}" fill="none" stroke="{GOLD}" stroke-width="1.6" stroke-dasharray="6 4"></path>')
    else:
        o.append(tag(sx0 + (sx1 - sx0) * 0.7, sy0, "THE SOREG · THE MIDDLE WALL OF PARTITION", sx0 + (sx1 - sx0) * 0.46, y0 + 16, color=GOLD, size=8.5)
                 + lab(w * 0.5, h - 10, "THE GENTILES · FAR OFF · SEPARATE · STRANGERS FROM THE COVENANTS", CY, 8))
        for i, (px, py) in enumerate(((x0 + PW * 0.05, y1 - PH * 0.06), (x0 + PW * 0.12, y1 - PH * 0.04), (x1 - PW * 0.04, y0 + PH * 0.3), (x1 - PW * 0.08, y0 + PH * 0.36))):
            o.append(_person_mark(px, py, s_ * 1.4, "#2C5A7A", head=False, flip=i >= 2, stroke=CY))
        for i, px in enumerate((sx0 + 34, sx0 + 58)):
            o.append(_person_mark(px, iy1 - 14, s_ * 1.2, "#163A56", head=True, stroke=CY))
    return "".join(o)

def masonry(w, h):
    """The household of God, built upon the foundation: a mason's plate of a corner of a building drawn in oblique — the
    great stones of the foundation course, the chief corner stone lit gold where the two walls meet, the courses above laid
    true to it (a plumb line hangs from above down to the corner stone), the walls stepping up unfinished, the rest of the
    holy temple dotted in above, growing."""
    o = [plate_bg(w, h, "EPHESIANS 2:19–22 · THE FOUNDATION AND THE CHIEF CORNER STONE")]
    top = 40; ch = h - top
    u = min(w / 702, ch / 330)
    by = top + ch * 0.86
    fw, dep, ang = 320 * u, 200 * u, math.radians(26)
    bx = w * 0.5 - 30 * u
    ddx, ddy = -dep * math.cos(ang), -dep * math.sin(ang)
    course = 30 * u; n = 5
    r = random.Random(5)
    side, front = [], []
    for row in range(n):
        y = by - row * course - (course * 0.25 if row else 0)
        hh = course * (1.25 if row == 0 else 1.0)
        lenf = fw * (1 - row * 0.13); lens = 1 - row * 0.15
        x = bx; first = True
        while x < bx + lenf - 4:
            sw_ = min(fw * r.uniform(0.14, 0.22) * (1.4 if row == 0 else 1), bx + lenf - x)
            gold = row == 0 and first; first = False
            front.append(f'<rect x="{f(x)}" y="{f(y - hh)}" width="{f(sw_)}" height="{f(hh)}" fill="{"#E8B830" if gold else ("#6A7A8A" if row == 0 else "#4A5A6A")}" stroke="{GOLD if gold else CY}" stroke-width="{2.6 if gold else 1.6}"></rect>')
            x += sw_
        t = 0.0; first = True
        while t < lens - 0.02:
            t1 = min(lens, t + r.uniform(0.18, 0.3) * (1.3 if row == 0 else 1))
            gold = row == 0 and first; first = False
            ax, ay = bx + ddx * t, y + ddy * t; cx_, cy_ = bx + ddx * t1, y + ddy * t1
            side.append(f'<path d="M{f(ax)} {f(ay)} L {f(cx_)} {f(cy_)} L {f(cx_)} {f(cy_ - hh)} L {f(ax)} {f(ay - hh)} Z" fill="{"#C8963E" if gold else ("#5A6A7A" if row == 0 else "#3E4E5E")}" stroke="{GOLD if gold else CY}" stroke-width="{2.6 if gold else 1.6}"></path>')
            t = t1
    o += side + front
    roof = max(top + 30 - ddy, by - 8 * course)
    o.append(f'<path d="M{f(bx)} {f(by - n * course)} L {f(bx)} {f(roof)} M{f(bx + fw)} {f(by - course * 1.3)} L {f(bx + fw)} {f(roof)} M{f(bx + ddx)} {f(by + ddy - course * 1.3)} L {f(bx + ddx)} {f(roof + ddy)} '
             f'M{f(bx + ddx)} {f(roof + ddy)} L {f(bx)} {f(roof)} L {f(bx + fw)} {f(roof)}" stroke="{CY}" stroke-width="1.2" stroke-dasharray="4 5" fill="none"></path>')
    o.append(halo(bx + 16 * u, by - course * 0.6, course * 1.6, "#FFE680", 0.4))
    o.append(f'<path d="M{f(bx)} {f(roof)} L {f(bx)} {f(by - course * 1.5)}" stroke="{GOLD}" stroke-width="1.2"></path>'
             f'<path d="M{f(bx - 5)} {f(by - course * 1.5)} L {f(bx + 5)} {f(by - course * 1.5)} L {f(bx)} {f(by - course * 1.5 + 11)} Z" fill="{GOLD}"></path>')
    lx = w * 0.04
    o.append(f'<path d="M{f(bx - 4)} {f(by - course * 0.5)} L {f(lx + 150)} {f(by - course * 2.6)}" stroke="{GOLD}" stroke-width="1.2"></path><circle cx="{f(bx - 4)}" cy="{f(by - course * 0.5)}" r="3" fill="{GOLD}"></circle>'
             + lab(lx, by - course * 2.6 - 18, "THE CHIEF CORNER STONE", GOLD, 9.5, "start") + lab(lx, by - course * 2.6 - 4, "CHRIST JESUS HIMSELF", GOLD, 8.5, "start"))
    o.append(lab(bx + fw * 0.5, by + 18, "THE FOUNDATION OF THE APOSTLES AND PROPHETS", CY, 8.5)
             + tag(bx + fw * 0.45, by - course * 3.2, "FITLY FRAMED TOGETHER", bx + fw * 0.82, by - course * 6.2, color=CY, size=8.5)
             + lab(w * 0.5, top + 18, "A HOLY TEMPLE IN THE LORD · A HABITATION OF GOD IN THE SPIRIT", GOLD, 9))
    return "".join(o)

# ---- Ephesians 3 ----------------------------------------------------------------------------------------------------------
def prisoner_still(w, h, seed):
    """I Paul, the prisoner of Christ Jesus: the table in his dwelling by lamplight under the window on Rome, the letter lying
    open on it with the reed pen and the inkpot, and across the table and the sheet the iron chain from his wrist (the cuff
    at the panel's edge)."""
    o = [still_life(w, h, seed, sealed=False, night=True)]
    ty = h * 0.62
    ww, wh = min(w * 0.22, ty * 0.9), min(ty * 0.72, w * 0.18)
    o.insert(1, rome_window(w * 0.62, ty - wh - 20, ww, wh, True, seed))
    o.append(chain(-6, ty + h * 0.08, w * 0.62, ty + h * 0.3, s=max(1.0, h / 180), sag=0.08))
    o.append(f'<rect x="-20" y="{f(ty + h * 0.08 - 14)}" width="30" height="26" rx="5" fill="#5A4A3A" stroke="{INK}" stroke-width="2"></rect>')
    return "".join(o)

def mystery_scroll(w, h, seed):
    """The mystery which for ages hath been hid in God, now revealed: a long scroll unrolled across the panel from the dark
    at the left into the light at the right; on the opened sheet three seals broken and named — fellow-heirs,
    fellow-members of the body, fellow-partakers of the promise (3:6)."""
    o = [f'<defs><linearGradient id="ms{seed}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#05051A"></stop><stop offset="0.45" stop-color="#2A2050"></stop>'
         f'<stop offset="0.8" stop-color="#C8803A"></stop><stop offset="1" stop-color="#FFE6A0"></stop></linearGradient></defs>'
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#ms{seed})"></rect>',
         starfield(w * 0.45, h, seed, 30, 1.0), halo(w * 1.02, h * 0.45, h * 1.2, "#FFF4C2", 0.5), rays(w * 1.02, h * 0.45, 24, h * 0.2, w, "#FFF4C2", 0.2, 5, 100, 260)]
    sy0, sy1 = h * 0.18, h * 0.7
    xl, xr = w * 0.08, w * 0.92
    dark = w * 0.26
    o.append(f'<rect x="{f(xl)}" y="{f(sy0)}" width="{f(xr - xl)}" height="{f(sy1 - sy0)}" fill="#EADBB4" stroke="{INK}" stroke-width="2.4"></rect>')
    r = random.Random(seed)
    for k in range(4):
        yy = sy0 + (sy1 - sy0) * (k + 0.6) / 9; xx = xl + dark + 16
        while xx < xr - 20:
            L = w * r.uniform(0.02, 0.06)
            o.append(f'<path d="M{f(xx)} {f(yy)} l {f(min(L, xr - 20 - xx))} 0" stroke="#4A3020" stroke-width="2" opacity="0.45"></path>'); xx += L + 8
    o.append(f'<rect x="{f(xl)}" y="{f(sy0)}" width="{f(dark)}" height="{f(sy1 - sy0)}" fill="#05051A" opacity="0.8"></rect>')
    for x in (xl, xr):
        o.append(f'<rect x="{f(x - 12)}" y="{f(sy0 - 10)}" width="24" height="{f(sy1 - sy0 + 20)}" rx="10" fill="#D8C49A" stroke="{INK}" stroke-width="2.4"></rect>'
                 f'<rect x="{f(x - 5)}" y="{f(sy0 - 22)}" width="10" height="14" fill="#6A3A1E" stroke="{INK}" stroke-width="1.6"></rect>'
                 f'<rect x="{f(x - 5)}" y="{f(sy1 + 8)}" width="10" height="14" fill="#6A3A1E" stroke="{INK}" stroke-width="1.6"></rect>')
    names = (("FELLOW-HEIRS",), ("FELLOW-MEMBERS", "OF THE BODY"), ("FELLOW-PARTAKERS", "OF THE PROMISE"))
    a, b_ = xl + dark + 10, xr - 16
    cy = sy0 + (sy1 - sy0) * 0.56
    for i, nm in enumerate(names):
        cx = a + (b_ - a) * (i + 0.5) / 3
        o.append(f'<circle cx="{f(cx - 8)}" cy="{f(cy)}" r="12" fill="{SEAL}" stroke="{INK}" stroke-width="1.8"></circle>'
                 f'<circle cx="{f(cx + 8)}" cy="{f(cy + 3)}" r="11" fill="{SEAL}" stroke="{INK}" stroke-width="1.8"></circle>'
                 f'<path d="M{f(cx)} {f(cy - 13)} L {f(cx - 3)} {f(cy)} L {f(cx + 2)} {f(cy + 14)}" stroke="#EADBB4" stroke-width="3" fill="none"></path>')
        for j, line in enumerate(nm):
            o.append(plate_label(cx, cy + 30 + j * 12, line, "#3A2A1A", 8.5, halo_="#EADBB4"))
    o.append(plate_label(xl + dark / 2, sy1 + 40, "HID FOR AGES IN GOD · 3:9", "#E8E2F6", 9, halo_="#05051A")
             + plate_label(w * 0.66, sy1 + 40, "NOW REVEALED IN THE SPIRIT · 3:5", "#FFF8E8", 9, halo_="#3A2A3A"))
    return "".join(o)

def bow_knees(p, w, h, seed):
    """For this cause I bow my knees unto the Father: Paul kneeling on the floor of his dwelling in the lamplight, his face
    toward the window and the light, the soldier standing behind him with his spear, the chain from his wrist to Paul's."""
    b = h * 0.95
    o = [mk.defs(p, *ALL), room(w, h, b, wall="#5E4A3C", floor="#3A2E26"), lamp_glow(w * 0.58, b - h * 0.3, max(w, h) * 0.6, f"{p}g", op=0.42)]
    s = (h * 0.7) / 205
    o.append(rome_window(w * 0.62, b - 210 * s, min(w * 0.18, 120 * s), min(h * 0.4, 96 * s), True, seed))
    o.append(halo(w * 0.72, b - 160 * s, 120 * s, "#FFE680", 0.35))
    o.append(low_table(w * 0.82, b, 50 * s, s) + clay_lamp(w * 0.82 + 25 * s, b - 31 * s, s * 0.5))
    gx = w * 0.2
    o.append(roman_guard(p, gx, b, s))
    kx = w * 0.4
    o.append(paul_kneel(kx, b, s * 1.1))
    o.append(chain(*guard_hand(gx, b, s), kx - 16 * s * 1.1, b - 62 * s * 1.1, s=s * 0.8, sag=0.15))
    return "".join(o)

def dimensions(w, h):
    """That ye may be strong to apprehend … what is the breadth and length and height and depth, and to know the love of
    Christ which passeth knowledge: a diagram — at the centre a measure of light (a cube drawn in oblique), and from it four
    measuring lines, breadth and length and height and depth, run out past every edge of the plate, their ends never drawn."""
    o = [plate_bg(w, h, "EPHESIANS 3:18–19 · THE BREADTH AND LENGTH AND HEIGHT AND DEPTH")]
    top = 34; cx, cy = w * 0.5, top + (h - top) * 0.54
    a = min(w, h - top) * 0.2
    dx, dy = a * 0.6, -a * 0.45
    o.append(halo(cx, cy, a * 3.2, "#FFE680", 0.42))
    fr = [(cx - a / 2, cy + a / 2), (cx + a / 2, cy + a / 2), (cx + a / 2, cy - a / 2), (cx - a / 2, cy - a / 2)]
    bk = [(x + dx, y + dy) for x, y in fr]
    poly = lambda pts: "M" + " L ".join(f"{f(x)} {f(y)}" for x, y in pts) + " Z"
    o.append(f'<path d="{poly(bk)}" fill="#FFE680" opacity="0.25" stroke="{GOLD}" stroke-width="1.6"></path>'
             + "".join(f'<path d="M{f(p1[0])} {f(p1[1])} L {f(p2[0])} {f(p2[1])}" stroke="{GOLD}" stroke-width="1.6"></path>' for p1, p2 in zip(fr, bk))
             + f'<path d="{poly(fr)}" fill="#FFF4C2" opacity="0.5" stroke="{GOLD}" stroke-width="2.4"></path>' + halo(cx + dx / 2, cy + dy / 2, a * 0.5, "#FFFFFF", 0.9))
    def ray(x1, y1, x2, y2, text, tx, ty, anchor="middle"):
        L = math.hypot(x2 - x1, y2 - y1)
        return (f'<path d="M{f(x1)} {f(y1)} L {f(x2)} {f(y2)}" stroke="{CY}" stroke-width="2" stroke-dasharray="10 4"></path>'
                + "".join(f'<path d="M{f(x1 + (x2 - x1) * t)} {f(y1 + (y2 - y1) * t)} l {f(-(y2 - y1) / L * 6)} {f((x2 - x1) / L * 6)}" stroke="{CY}" stroke-width="1.4"></path>' for t in (0.25, 0.45, 0.65, 0.85))
                + lab(tx, ty, text, CY, 11, anchor))
    hx = cx - a * 0.1
    o.append(ray(cx - a / 2 - 6, cy + a * 0.1, -20, cy + a * 0.1, "BREADTH", w * 0.04, cy + a * 0.1 - 10, "start")
             + ray(cx + a / 2 + 6, cy + a * 0.1, w + 20, cy + a * 0.1, "BREADTH", w * 0.96, cy + a * 0.1 - 10, "end")
             + ray(cx + dx + a * 0.1, cy + dy - a * 0.2, w + 20, top - 30, "LENGTH", w * 0.86, top + 34, "end")
             + ray(hx, cy - a / 2 - 6, hx, top - 20, "HEIGHT", hx + 12, top + 30, "start")
             + ray(hx, cy + a / 2 + 6, hx, h + 20, "DEPTH", hx + 12, h - 14, "start"))
    o.append(lab(cx + a * 1.25, cy + a * 1.0, "THE LOVE OF CHRIST", GOLD, 10, "start") + lab(cx + a * 1.25, cy + a * 1.0 + 15, "WHICH PASSETH KNOWLEDGE", GOLD, 9, "start"))
    return "".join(o)
