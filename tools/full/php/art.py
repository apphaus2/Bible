"""Drawings for the Philippians volume, and the figures of the prison letters' cast (Colossians and Philemon draw from here
too: `from php.art import *`). Built on 1 Corinthians' drawings (`from co1.art5 import *`, which carries all of Acts',
Mark's and Matthew's drawings) and the epistle kit (the prison study, the sealed scroll, the letter's road, the plate).

The cast at a distance, on the kit silhouettes (epistle.robed), in the looks of php.common: Paul only ever epistle.paul_fig
(chained to the soldier of epistle.roman_guard at Rome); Timothy, Epaphroditus, Euodia, Syntyche, Epaphras, Onesimus,
Philemon, Apphia, Archippus, Tychicus, Mark, Luke, Aristarchus, Justus, Demas. Christ is drawn only as light, as ntcast's
Jesus (risen: co1.art5.risen_fig) or, at the cross, as three crosses far off; God is never drawn. Every function takes
(p, w, h, seed, ...) or (w, h, ...); p, a prefix unique to the panel, names the figure defs and gradients."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from co1.art5 import *
from co1.art5 import f, INK
import epistle as EP
from epistle import (study, still_life, sealed_scroll, open_letter, reed_pen, inkpot, lamp_glow, letter_road, plate_bg, radiance, tag, dim, robed, paul_fig,
                     roman_guard, guard_hand, robed_hand, chain, stool, bench, rome_window, mat as floor_mat, low_table, SEPIA, SEAL)
from co1.art import timothy_r
from co2.art import censer, triumph, jar
from co2.art3 import balance
from gal.art import dark_street, far_crosses, light_fig, town_hill
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import label, node, route
from genesis.art4 import clay_lamp
from oba.minor import halo, rays, starfield
from jer.art import glow
from sa2.art import sky
from mat.art import houses, pavement, room
from mrk.art import on_bed, lying
from gal.art import low_board
from act.art import toga_fig
from act.art15 import grain_ship
from num.art import ALL
import act.geo as geo
import mk, exodus as E
from php.common import (TIMOTHY_LOOK, EPAPHRODITUS_LOOK, EUODIA_LOOK, SYNTYCHE_LOOK, EPAPHRAS_LOOK, ONESIMUS_LOOK, PHILEMON_LOOK, APPHIA_LOOK,
                        ARCHIPPUS_LOOK, TYCHICUS_LOOK, MARK_LOOK, LUKE_LOOK, ARISTARCHUS_LOOK, JUSTUS_LOOK, DEMAS_LOOK)

GOLD, CY = "#FFD23F", "#8FD0E2"
for _nm, _ll in (("COLOSSÆ", (29.26, 37.79)), ("LAODICEA", (29.11, 37.84)), ("HIERAPOLIS", (29.13, 37.93)), ("BRUNDISIUM", (17.94, 40.64)),
                 ("DYRRACHIUM", (19.45, 41.32))):
    geo.PLACES.setdefault(_nm, _ll)                     # the prison letters' places, for their maps (act.geo has Acts' places)

def art(fn, *a, **k):
    """A panel's drawing as fn(w, h): fn(p, w, h, seed, ...) when the first argument is a prefix string, else fn(w, h, ...)."""
    def draw(w, h): return fn(*a[:1], w, h, *a[1:], **k) if a and isinstance(a[0], str) else fn(w, h, *a, **k)
    draw.__name__ = fn.__name__
    return draw

def plate_label(x, y, text, color=GOLD, size=10, anchor="middle", halo_="#0B1A2E", weight=600):
    """A label with a dark (or light) halo so it reads over a drawing (svg text: data, not scripture)."""
    return label(x, y, text, color, size, anchor, weight=weight).replace("<text ", f'<text stroke="{halo_}" stroke-width="3" paint-order="stroke" stroke-linejoin="round" ', 1)

def _defs(p): return mk.defs(p, *ALL, "ManUp", "WomanUp")

# ---- the cast at a distance -------------------------------------------------------------------------------------------------
def _man(L):
    def fig(p, x, y, s, flip=False, up=None, extra="", pose="stand", seat="stool"):
        return robed(p, x, y, s, L["cloth"], skin=L.get("skin", SKIN), head=L.get("head"), cord=L.get("cord", "#2A1A10"), hair=L.get("hair"),
                     beard=L.get("beard"), mantle=L.get("mantle"), belt=L.get("belt"), flip=flip, up=up, extra=extra, pose=pose, seat=seat)
    return fig
def _woman(L):
    def fig(p, x, y, s, flip=False, up=None, extra="", pose="stand", seat="stool"):
        return robed(p, x, y, s * 0.94, L["cloth"], woman=True, veil=L["veil"], mantle=L.get("mantle"), flip=flip, up=up, extra=extra, pose=pose, seat=seat)
    return fig
timothy = _man(TIMOTHY_LOOK)
epaphroditus = _man(EPAPHRODITUS_LOOK)
euodia, syntyche = _woman(EUODIA_LOOK), _woman(SYNTYCHE_LOOK)
epaphras = _man(EPAPHRAS_LOOK)
_onesimus = _man(ONESIMUS_LOOK)
def onesimus(p, x, y, s, flip=False, up=None, extra="", pose="stand", seat="stool"):
    """Onesimus, young: a little shorter than the men about him."""
    return _onesimus(p, x, y, s * 0.95, flip=flip, up=up, extra=extra, pose=pose, seat=seat)
philemon, apphia, archippus = _man(PHILEMON_LOOK), _woman(APPHIA_LOOK), _man(ARCHIPPUS_LOOK)
tychicus = _man(TYCHICUS_LOOK)
mark, luke, aristarchus, justus, demas = _man(MARK_LOOK), _man(LUKE_LOOK), _man(ARISTARCHUS_LOOK), _man(JUSTUS_LOOK), _man(DEMAS_LOOK)
TIMOTHY_SCRIBE = dict(cloth=TIMOTHY_LOOK["cloth"], hair=TIMOTHY_LOOK["hair"])        # Timothy writing the letter (1:1), bareheaded
WHO.update({"timothy_r": timothy, "epaphroditus": epaphroditus, "epaphras": epaphras, "onesimus": onesimus, "philemon": philemon, "tychicus": tychicus})

FOLKS = [("#7A5A3A", "#3A4A5A", "#2A1A10", None, False, None), ("#5A6A8A", None, None, None, True, "#2A3A5A"),
         ("#6A7A4A", None, "#3A2A1A", "#2A1A10", False, None), ("#8A4A3A", "#E8E2D6", "#8A847A", None, False, None),
         ("#4A5A6A", None, None, None, True, "#E8E2D6"), ("#9A8A6A", None, None, "#3A2214", False, None),
         ("#6A4A5A", "#2A2A3A", "#1A1210", None, False, None), ("#7A6A5A", None, None, None, True, "#4A3A5A")]
def saint(p, x, y, s, i=0, flip=False, up=None, pose="stand", seat="stool", extra=""):
    """One of the saints (at Philippi, Colossæ, Rome): men in cool or off-white headcloths or bareheaded, women in cool veils."""
    c, hd, bd, hr, wm, vl = FOLKS[i % len(FOLKS)]
    if wm: return robed(p, x, y, s * 0.94, c, woman=True, veil=vl, flip=flip, up=up, pose=pose, seat=seat, extra=extra)
    return robed(p, x, y, s, c, head=hd, hair=hr if not hd else None, beard=bd, flip=flip, up=up, pose=pose, seat=seat, extra=extra)

def toga_r(p, x, y, s, flip=False, up=None, border="#6A1A5A", hair="#4A3A2A", extra=""):
    """A Roman citizen or magistrate in his toga, on the kit silhouette (epistle.robed): white wool, the toga's fold over the
    shoulder edged with its coloured border, bareheaded, clean-shaven."""
    edge = f'<path d="M-25 -162 C -12 -150 6 -118 16 -58 C 18 -40 20 -20 22 -4" stroke="{border}" stroke-width="4" fill="none"></path>'
    return robed(p, x, y, s, "#F3EFE6", hair=hair, mantle="#E8E2D6", flip=flip, up=up, extra=edge + extra)

def guard_r(p, x, y, s, flip=False, up=None, spear=True):
    """A soldier of the prætorian guard (epistle.roman_guard)."""
    return roman_guard(p, x, y, s, flip=flip, up=up, spear=spear)

# ---- small things -------------------------------------------------------------------------------------------------------------
def frame(w, h, color="#FFD23F", inset=8):
    return f'<rect x="{inset}" y="{inset}" width="{f(w - 2 * inset)}" height="{f(h - 2 * inset)}" fill="none" stroke="{color}" stroke-width="2"></rect>'

def hand_pen(x, y, s, skin=SKIN, chained=True, flip=False):
    """Paul's own hand writing (close in): the sleeve, the hand holding the reed pen, its nib at (x, y); chained=True the iron
    cuff on the wrist and the chain running off (Col 4:18, 'Remember my bonds')."""
    sx = -s if flip else s
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(sx)} {f(s)})">']
    if chained:                                                  # the chain, from the cuff down off the table (under the sleeve)
        d = "M96 -36 C 130 -10 150 30 170 90 C 176 110 180 130 184 160"
        o.append(f'<path d="{d}" fill="none" stroke="#0D0D0F" stroke-width="9" stroke-dasharray="12 5" stroke-linecap="round"></path>'
                 f'<path d="{d}" fill="none" stroke="#9A9AA4" stroke-width="5" stroke-dasharray="12 5" stroke-linecap="round"></path>')
    o += ['<path d="M84 -70 C 140 -104 220 -150 330 -200 L 360 -130 C 260 -90 170 -46 110 -14 Z" fill="#6A4A36" stroke="#0D0D0F" stroke-width="3"></path>',   # the sleeve
          '<path d="M120 -60 C 170 -92 230 -122 300 -150" fill="none" stroke="#4A3022" stroke-width="2"></path>',
          f'<path d="M58 -56 C 70 -66 84 -70 96 -64 L 112 -28 C 100 -20 86 -16 74 -18 Z" fill="{skin}" stroke="#0D0D0F" stroke-width="2.6"></path>',      # the wrist
          f'<path d="M14 -10 C 12 -30 26 -50 48 -56 C 66 -60 80 -54 84 -40 C 88 -24 80 -10 64 -4 C 46 2 24 4 14 -10 Z" fill="{skin}" stroke="#0D0D0F" stroke-width="2.8"></path>',  # the hand
          f'<path d="M30 -46 C 22 -42 16 -34 16 -26 C 16 -18 22 -14 30 -16 C 36 -18 38 -26 34 -32" fill="{skin}" stroke="#0D0D0F" stroke-width="2.2"></path>',   # the thumb
          '<path d="M36 -10 C 44 -16 56 -18 66 -14 M40 -2 C 50 -6 60 -6 68 -2" fill="none" stroke="#0D0D0F" stroke-width="1.6"></path>',                        # the fingers' folds
          '<path d="M-1 3 L 3 -3 L 58 -84 L 52 -88 Z" fill="#C8A060" stroke="#0D0D0F" stroke-width="2"></path>',                                                 # the reed pen
          '<path d="M-1 3 L 3 -3 L 6 -8 L 2 -6 Z" fill="#2A1A10"></path>']
    if chained:                                                  # the iron cuff on the wrist
        o.append('<path d="M88 -72 L 104 -78 L 124 -30 L 108 -24 Z" fill="#6A6A74" stroke="#0D0D0F" stroke-width="2.6"></path>'
                 '<path d="M94 -66 L 112 -30" stroke="#9A9AA4" stroke-width="2"></path>')
    return "".join(o) + "</g>"

# ---- the prison at Rome --------------------------------------------------------------------------------------------------------
def prison_study(p, w, h, seed, stage="prison", scribe=None, bearer=None, others=(), night=True, up=None, sit=None, fig_h=None):
    """The letter written in Paul's bonds at Rome (epistle.study's prison stages): the soldier at the left chained to Paul,
    Timothy (bareheaded) writing on his mat, the window on Rome; others standing at the right listening."""
    return study(p, w, h, seed, stage=stage, scribe=TIMOTHY_SCRIBE if scribe is None else scribe, bearer=bearer, others=others, night=night,
                 window="rome", up=up, sit=sit, fig_h=fig_h or min(h * 0.72, 300))

def philippi_road(w, h):
    """To the saints at Philippi: the letter's road from Rome down the Appian Way to Brundisium, over the sea to
    Dyrrachium, and along the Egnatian Way by Thessalonica and Amphipolis to Philippi."""
    rt = ["ROME", (14.8, 41.1), "BRUNDISIUM", "DYRRACHIUM", (21.0, 41.0), "THESSALONICA", "AMPHIPOLIS", "PHILIPPI"]
    return letter_road(w, h, rt, title="PHILIPPIANS 1:1 · TO ALL THE SAINTS THAT ARE AT PHILIPPI", box=(11.5, 25.5, 38.6, 42.6),
                       places=("ROME", "BRUNDISIUM", "DYRRACHIUM", "THESSALONICA", "PHILIPPI"), hi=("ROME", "PHILIPPI"),
                       regions=("ITALY", ("MACEDONIA", 22.0, 41.9), "ACHAIA"))

# ---- Philippi -------------------------------------------------------------------------------------------------------------------
def court(w, h, b, seed, tone="day"):
    """The court of a house at Philippi (Lydia's, where the church met: Acts 16:15, 40): plastered walls, a colonnade of two
    columns, a doorway, a vine over the wall; tone "day" or "night" (lamplight)."""
    day = tone == "day"
    o = [sky(w, h, "#8FD0E2", "#F3E8C8") if day else sky(w, h, "#0B0B2A", "#2A2050")]
    if not day: o.append(mk.stars(30, w, h * 0.16, seed))
    o.append(f'<rect x="-10" y="{f(h * 0.14)}" width="{f(w + 20)}" height="{f(b - h * 0.14)}" fill="{"#E8D8B0" if day else "#5A4638"}" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="-10" y="{f(b - h * 0.16)}" width="{f(w + 20)}" height="{f(h * 0.16)}" fill="{"#A8322A" if day else "#4A2420"}" opacity="0.7"></rect>')
    dx, dw = w * 0.44, min(w * 0.12, h * 0.3)
    o.append(f'<path d="M{f(dx)} {f(b)} L {f(dx)} {f(h * 0.4)} C {f(dx)} {f(h * 0.3)} {f(dx + dw)} {f(h * 0.3)} {f(dx + dw)} {f(h * 0.4)} L {f(dx + dw)} {f(b)} Z" '
             f'fill="{"#3A2214" if day else "#FFC14D"}" stroke="{INK}" stroke-width="2.4"></path>')
    for cx in (w * 0.08, w * 0.92):
        o.append(f'<rect x="{f(cx - w * 0.02)}" y="{f(h * 0.16)}" width="{f(w * 0.04)}" height="{f(b - h * 0.16)}" fill="{"#F3EFE6" if day else "#8A7A6A"}" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="{f(cx - w * 0.03)}" y="{f(h * 0.14)}" width="{f(w * 0.06)}" height="{f(h * 0.03)}" fill="{"#E8E2D6" if day else "#7A6A5A"}" stroke="{INK}" stroke-width="1.6"></rect>')
    r = random.Random(seed)
    for k in range(int(w / 26)):                              # the vine along the top of the wall
        x = k * 26 + r.uniform(-4, 4)
        o.append(f'<circle cx="{f(x)}" cy="{f(h * 0.15 + r.uniform(-4, 6))}" r="{f(max(6, h * 0.035))}" fill="{"#4A8A3A" if day else "#2A4A2A"}" stroke="{INK}" stroke-width="1.2"></circle>')
    if not day: o.append(lamp_glow(w * 0.5, b - h * 0.3, max(w, h) * 0.5, f"ct{seed}", op=0.4))
    o.append(ground(w, h, b, "#C8B080" if day else "#3A2E26", dy=0))
    return "".join(o)

def philippi_house(p, w, h, seed, stage="pray"):
    """The church at Philippi in the court of the house: stage "pray" — the saints standing with their hands lifted, an
    overseer with a roll before them (the bishops and deacons, 1:1, 9–11); "read" — by lamplight, Epaphroditus come home
    reading Paul's letter aloud to them (3:1); "welcome" — Epaphroditus come in at the door and the saints going to meet him
    with joy (2:28–29)."""
    b = h * 0.93
    o = [_defs(p), court(w, h, b, seed, "night" if stage == "read" else "day")]
    s = fit(b, b - min(h * 0.72, 210))
    if stage == "read":
        o.append(clay_lamp(w * 0.3, b - 52 * s, s * 0.9) + low_table(w * 0.24, b, 70 * s, s))
        o.append(epaphroditus(p, w * 0.17, b, s, flip=True, up=[(-22, -158), (-40, -150), (-58, -160)], extra=open_letter(-92, -196, 40, 52, rows=6, seed=seed)))
        o.append(bench(w * 0.52, b, w * 0.44, s))
        for i, x in enumerate((0.58, 0.68, 0.78, 0.88)):
            o.append(saint(p, w * x, b, s * (0.98 - 0.02 * i), i, pose="sit", seat=None))
        o.append(saint(p, w * 0.46, b, s * 0.96, 5))
        return "".join(o)
    if stage == "welcome":
        o.append(epaphroditus(p, w * 0.5, b, s, flip=True, extra=sealed_scroll(-60, -120, 0.3)))
        for i, x in enumerate((0.66, 0.77, 0.88)):
            o.append(saint(p, w * x, b, s * (0.98 - 0.02 * i), i + 1, up=[(-22, -158), (-46, -150), (-66, -156)] if i == 0 else None))
        for i, x in enumerate((0.3, 0.18)):
            o.append(saint(p, w * x, b, s * 0.97, i + 4, flip=True, up=[(-22, -158), (-44, -150), (-64, -152)] if i == 0 else None))
        return "".join(o)
    o.append(saint(p, w * 0.2, b, s, 3, flip=True, up=[(-22, -158), (-40, -150), (-58, -160)], extra=open_letter(-92, -196, 40, 52, rows=6, seed=seed)))
    for i, x in enumerate((0.36, 0.5, 0.62, 0.74, 0.86)):
        o.append(saint(p, w * x, b, s * (0.98 - 0.01 * i), [0, 1, 2, 4, 6][i], up=[(-22, -158), (-36, -188), (-40, -220)] if i % 2 == 0 else None))
    return "".join(o)

def camp(w, h, b, seed):
    """The camp of the prætorian guard at Rome: the long barracks of brick with their red-tiled roofs and arcades, the
    standards planted before them, the parade ground."""
    o = [sky(w, h, "#8FD0E2", "#F3E8C8")]
    o.append(f'<rect x="-10" y="{f(h * 0.18)}" width="{f(w + 20)}" height="{f(h * 0.44)}" fill="#B8603A" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M-10 {f(h * 0.18)} L {f(w + 10)} {f(h * 0.18)} L {f(w + 10)} {f(h * 0.12)} L -10 {f(h * 0.12)} Z" fill="#8A3A22" stroke="{INK}" stroke-width="2"></path>')
    for row, (y0, y1) in enumerate(((0.22, 0.36), (0.42, 0.62))):
        n = int(w / 46)
        for i in range(n + 1):
            x = i * 46 + 10
            o.append(f'<path d="M{f(x)} {f(h * y1)} L {f(x)} {f(h * (y0 + 0.04))} C {f(x)} {f(h * y0)} {f(x + 30)} {f(h * y0)} {f(x + 30)} {f(h * (y0 + 0.04))} L {f(x + 30)} {f(h * y1)} Z" '
                     f'fill="#3A2018" stroke="{INK}" stroke-width="1.6"></path>')
    o.append(f'<path d="M-10 {f(h * 0.39)} L {f(w + 10)} {f(h * 0.39)}" stroke="#8A3A22" stroke-width="6"></path>')
    o.append(ground(w, h, h * 0.62, "#D8C08A", dy=0))
    for x in (w * 0.46, w * 0.96):                              # the standards: a pole, an eagle, a wreath and discs
        o.append(f'<path d="M{f(x)} {f(b)} L {f(x)} {f(h * 0.26)}" stroke="#5A3A1E" stroke-width="4"></path>'
                 f'<path d="M{f(x - 12)} {f(h * 0.28)} L {f(x)} {f(h * 0.22)} L {f(x + 12)} {f(h * 0.28)} L {f(x)} {f(h * 0.26)} Z" fill="#E8B830" stroke="{INK}" stroke-width="1.4"></path>'
                 + "".join(f'<circle cx="{f(x)}" cy="{f(h * (0.32 + 0.06 * k))}" r="6" fill="#E8B830" stroke="{INK}" stroke-width="1.4"></circle>' for k in range(3))
                 + f'<rect x="{f(x - 14)}" y="{f(h * 0.52)}" width="28" height="18" fill="#B5121B" stroke="{INK}" stroke-width="1.4"></rect>')
    return "".join(o)

def praetorian(p, w, h, seed):
    """My bonds became manifest in Christ throughout the whole prætorian guard: the camp of the guard, Paul chained by the
    wrist to the soldier on watch, his hand out as he speaks; soldiers of the guard standing to hear him, one with his
    helmet under his arm."""
    b = h * 0.94
    o = [_defs(p), camp(w, h, b, seed)]
    s = fit(b, b - min(h * 0.74, 214))
    gx, px = w * 0.1, w * 0.28
    o.append(guard_r(p, gx, b, s) + paul_fig(p, px, b, s, flip=True, up=[(-22, -158), (-48, -150), (-72, -160)]))
    o.append(chain(*guard_hand(gx, b, s), *robed_hand(px, b, s, flip=True), s=s * 0.8))
    for i, x in enumerate((0.56, 0.7, 0.84)):
        o.append(guard_r(p, w * x, b, s * (0.99 - 0.02 * i), flip=True, spear=i != 1))
    return "".join(o)

def to_live(w, h):
    """For to me to live is Christ, and to die is gain: a plate in two halves — at the left the vine heavy with grapes,
    the fruit of his work (1:22), by the lamp; at the right the sun rising over the sea; between them the strait."""
    o = [plate_bg(w, h, "PHILIPPIANS 1:21 · TO LIVE IS CHRIST · TO DIE IS GAIN")]
    k = min(w / 600, (h - 40) / 230)
    cy = 30 + (h - 30) * 0.52
    lx, rx = w * 0.27, w * 0.73
    cw, ch = w * 0.4, (h - 60) * 0.8
    for x, top, bot in ((lx, "#2A3A2A", "#4A6A3A"), (rx, "#1F3A6A", "#FFB07A")):
        uid = f"tl{int(x)}"
        o.append(f'<defs><linearGradient id="{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"></stop><stop offset="1" stop-color="{bot}"></stop></linearGradient>'
                 f'<clipPath id="{uid}c"><rect x="{f(x - cw / 2)}" y="{f(cy - ch / 2)}" width="{f(cw)}" height="{f(ch)}"></rect></clipPath></defs>'
                 f'<rect x="{f(x - cw / 2)}" y="{f(cy - ch / 2)}" width="{f(cw)}" height="{f(ch)}" fill="url(#{uid})" stroke="{GOLD}" stroke-width="2"></rect>')
    # the vine: a trunk, its branches, leaves and clusters
    o.append(f'<g clip-path="url(#tl{int(lx)}c)">'
             f'<path d="M{f(lx - 40 * k)} {f(cy + ch / 2)} C {f(lx - 30 * k)} {f(cy + 20 * k)} {f(lx - 50 * k)} {f(cy - 20 * k)} {f(lx - 10 * k)} {f(cy - 50 * k)} '
             f'C {f(lx + 30 * k)} {f(cy - 70 * k)} {f(lx + 70 * k)} {f(cy - 40 * k)} {f(lx + 90 * k)} {f(cy - 60 * k)}" fill="none" stroke="#5A3A1E" stroke-width="{f(9 * k)}"></path>')
    for i, (dx, dy) in enumerate(((-40, -40), (-6, -62), (30, -66), (64, -50), (-56, -10), (90, -70))):
        x, y = lx + dx * k, cy + dy * k
        o.append(f'<path d="M{f(x)} {f(y)} c {f(10 * k)} {f(-14 * k)} {f(26 * k)} {f(-10 * k)} {f(22 * k)} {f(6 * k)} c {f(-6 * k)} {f(12 * k)} {f(-18 * k)} {f(10 * k)} {f(-22 * k)} {f(-6 * k)} Z" fill="#4A8A3A" stroke="{INK}" stroke-width="1.2"></path>')
    for i, (dx, dy) in enumerate(((-24, -30), (16, -48), (50, -34), (82, -50))):
        for j in range(10):
            x = lx + (dx + (j % 3 - 1) * 7 + (j // 3) * 1.5) * k; y = cy + (dy + (j // 3) * 8) * k
            o.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(4.4 * k)}" fill="#5A2A6A" stroke="{INK}" stroke-width="1"></circle>')
    o.append('</g>')
    # the sea and the rising sun
    sy = cy + ch * 0.18
    o.append(f'<g clip-path="url(#tl{int(rx)}c)">' + halo(rx, sy, 90 * k, "#FFE680", 0.6) + rays(rx, sy, 18, 30 * k, 160 * k, "#FFF4C2", 0.4, 3)
             + f'<circle cx="{f(rx)}" cy="{f(sy)}" r="{f(22 * k)}" fill="#FFF4C2"></circle>'
             + f'<rect x="{f(rx - cw / 2)}" y="{f(sy)}" width="{f(cw)}" height="{f(ch)}" fill="#1F4A6A"></rect>'
             + "".join(f'<path d="M{f(rx - cw * 0.3 + j * 7)} {f(sy + 8 + j * 9)} L {f(rx + cw * 0.3 - j * 7)} {f(sy + 8 + j * 9)}" stroke="#FFE680" stroke-width="2" opacity="{0.8 - j * 0.12:.2f}"></path>' for j in range(5))
             + '</g>')
    o.append(plate_label(lx, cy - ch / 2 - 8, "TO LIVE · CHRIST", CY, 11) + plate_label(rx, cy - ch / 2 - 8, "TO DIE · GAIN", GOLD, 11)
             + plate_label(lx, cy - ch / 2 + 18, "FRUIT FROM MY WORK", "#F3EFE6", 9) + plate_label(rx, cy - ch / 2 + 18, "VERY FAR BETTER", "#F3EFE6", 9))
    ax0, ax1 = lx + cw / 2 + 6, rx - cw / 2 - 6
    o.append(f'<path d="M{f(ax0)} {f(cy)} L {f(ax1)} {f(cy)} M{f(ax0 + 6)} {f(cy - 5)} L {f(ax0)} {f(cy)} L {f(ax0 + 6)} {f(cy + 5)} M{f(ax1 - 6)} {f(cy - 5)} L {f(ax1)} {f(cy)} L {f(ax1 - 6)} {f(cy + 5)}" '
             f'fill="none" stroke="{GOLD}" stroke-width="2"></path>')
    return "".join(o)

def depart(p, w, h, seed):
    """Having the desire to depart: a ship at the quay in the first light, her moorings cast off and her great sail filling,
    standing out to sea down a road of light on the water — the word is a ship loosed from her moorings."""
    b = h
    o = [sky(w, h, "#2A2A5A", "#FFC890"), halo(w * 0.78, h * 0.5, h * 0.7, "#FFE680", 0.5), rays(w * 0.78, h * 0.5, 22, h * 0.1, h * 1.2, "#FFF4C2", 0.25, 4)]
    hz = h * 0.56
    o.append(f'<circle cx="{f(w * 0.78)}" cy="{f(hz)}" r="{f(h * 0.08)}" fill="#FFF4C2"></circle>'
             f'<rect x="-10" y="{f(hz)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A4A6A"></rect>')
    for j in range(9):
        y = hz + 6 + j * (h - hz) / 9
        hw = w * (0.04 + j * 0.035)
        o.append(f'<path d="M{f(w * 0.78 - hw)} {f(y)} L {f(w * 0.78 + hw)} {f(y)}" stroke="#FFE680" stroke-width="{f(2 + j * 0.4)}" opacity="{0.85 - j * 0.06:.2f}"></path>')
    o.append(f'<path d="M-10 {f(h * 0.74)} L {f(w * 0.26)} {f(h * 0.74)} L {f(w * 0.26)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M-10 {f(h * 0.8)} L {f(w * 0.26)} {f(h * 0.8)}" stroke="#6A5A4A" stroke-width="2"></path>')
    bx, by = w * 0.2, h * 0.76                                  # the bollard and the loosed rope trailing in the water
    o.append(f'<rect x="{f(bx - 8)}" y="{f(by - 18)}" width="16" height="18" rx="4" fill="#4A4038" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(bx)} {f(by - 10)} C {f(bx + 30)} {f(by + 10)} {f(bx + 50)} {f(h * 0.82)} {f(bx + 80)} {f(h * 0.8)}" fill="none" stroke="#C8A060" stroke-width="3"></path>')
    s = min(w / 900, h / 360)
    o.append(grain_ship(p, w * 0.52, h * 0.7, s, sail="full"))
    return "".join(o)

def forum(w, h, b, seed):
    """The forum of Philippi: a colonnade along the far side, the magistrates' tribunal on its steps, the acropolis above."""
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"),
         f'<path d="M{f(w * 0.3)} {f(h * 0.4)} L {f(w * 0.5)} {f(h * 0.1)} L {f(w * 0.7)} {f(h * 0.06)} L {f(w * 1.05)} {f(h * 0.3)} L {f(w * 1.05)} {f(h * 0.4)} Z" fill="#9A8A6A" stroke="{INK}" stroke-width="2"></path>']
    o.append(f'<rect x="-10" y="{f(h * 0.3)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#E8E2D6" stroke="{INK}" stroke-width="2"></rect>')
    for i in range(int(w / 40) + 1):
        x = i * 40 + 12
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.36)}" width="10" height="{f(h * 0.24)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.4"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.36)}" width="{f(w + 20)}" height="{f(h * 0.24)}" fill="#6A5A4A" opacity="0.35"></rect>')
    o.append(ground(w, h, h * 0.6, "#D8C8A0", dy=0) + pavement(w, h, h * 0.6, color="#D8C8A0"))
    return "".join(o)

def stand_fast(p, w, h, seed):
    """That ye stand fast in one spirit, with one soul striving for the faith of the gospel; and in nothing affrighted by
    the adversaries: the saints of Philippi standing together in the forum, side by side; across the square the
    magistrates' tribunal, a magistrate in his toga between two lictors with their rods (Acts 16:20–22)."""
    b = h * 0.94
    o = [_defs(p), forum(w, h, b, seed)]
    tx = w * 0.82                                               # the tribunal on its steps, far off
    o.append(f'<rect x="{f(tx - w * 0.14)}" y="{f(h * 0.5)}" width="{f(w * 0.28)}" height="{f(h * 0.1)}" fill="#E8E2D6" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(tx - w * 0.12)}" y="{f(h * 0.56)}" width="{f(w * 0.24)}" height="{f(h * 0.04)}" fill="#D8D0C0" stroke="{INK}" stroke-width="1.4"></rect>')
    sf = fit(h * 0.5, h * 0.5 - min(h * 0.3, 90))
    o.append(toga_r(p, tx, h * 0.5, sf))
    for dx in (-0.09, 0.09):
        o.append(robed(p, tx + w * dx, h * 0.5, sf * 0.96, "#E8E2D6", hair="#3A2A1A", belt="#6A3A1E", flip=dx > 0,
                       extra='<path d="M-30 -10 L -30 -150" stroke="#6A3A1E" stroke-width="7"></path><path d="M-36 -150 L -24 -150 L -30 -170 Z" fill="#B8B8C0" stroke="#0D0D0F" stroke-width="1.4"></path>'))
    s = fit(b, b - min(h * 0.72, 206))
    for i, x in enumerate((0.1, 0.2, 0.3, 0.4, 0.5, 0.6)):
        o.append(saint(p, w * x, b, s * (1 - 0.012 * i), [3, 1, 0, 4, 2, 7][i], flip=True))
    return "".join(o)

# ---- Philippians 2 --------------------------------------------------------------------------------------------------------------
def one_mind(p, w, h, seed):
    """Each counting other better than himself; not looking each to his own things, but to the things of others: the saints
    at the table in the house at Philippi, one standing to serve the bread, another pouring water over a brother's hands."""
    b = h * 0.93
    o = [_defs(p), court(w, h, b, seed, "day")]
    s = fit(b, b - min(h * 0.72, 210))
    o.append(bench(w * 0.04, b, w * 0.26, s) + bench(w * 0.66, b, w * 0.3, s))
    o.append(saint(p, w * 0.1, b, s, 0, pose="sit", seat=None, flip=True) + saint(p, w * 0.22, b, s, 1, pose="sit", seat=None, flip=True))
    o.append(saint(p, w * 0.86, b, s, 2, pose="sit", seat=None) + saint(p, w * 0.74, b, s, 4, pose="sit", seat=None,
                                                                               up=[(-22, -158), (-40, -128), (-56, -118)]))
    o.append(low_board(w * 0.32, w * 0.64, b, s))
    o.append(saint(p, w * 0.42, b, s, 6, flip=True, up=[(-22, -158), (-44, -146), (-64, -150)],
                   extra='<ellipse cx="-66" cy="-152" rx="13" ry="6" fill="#C88A4A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'))
    o.append(saint(p, w * 0.6, b, s, 3, up=[(-22, -158), (-38, -136), (-58, -132)],
                   extra='<path d="M-50 -150 L -70 -150 L -74 -128 L -46 -128 Z" fill="#B85A3A" stroke="#0D0D0F" stroke-width="1.6"></path>'
                         '<path d="M-72 -134 C -78 -126 -80 -116 -80 -108" stroke="#8FD0E2" stroke-width="3" fill="none"></path>'))
    return "".join(o)

def _stairs(w, h, title, labels, down=True, foot=None):
    """A staircase on a plate: down=True from the upper left to the lower right, the label of each step above it and to its
    right; down=False from the lower left up to the upper right, each label above its step and to its left. Returns the
    svg and the steps' points (x, y) — the middle of each tread."""
    o = [plate_bg(w, h, title)]
    n = len(labels)
    x0, x1 = w * 0.06, w * 0.94
    sw = (x1 - x0) / (n + 1)                                    # the last tread leaves a step's width for the end of the way
    top, foot = 52, (h - 40 if foot is None else foot)
    rise = (foot - top - 70) / max(1, n - 1)
    pts = []
    for i in range(n):
        k = i if down else n - 1 - i                            # k: how high the step is (0 the highest)
        x = x0 + i * sw if down else x0 + (i + 1) * sw
        y = top + 40 + k * rise if k < n - 1 else foot - 36
        col, fill = (CY, "#16304A") if down else (GOLD, "#3A3018")
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(sw)}" height="{f(foot - y)}" fill="{fill}" stroke="{col}" stroke-width="1.6"></rect>')
        pts.append((x + sw / 2, y))
    for i, (lab, (x, y)) in enumerate(zip(labels, pts)):         # each step's name inside its block, in two lines if it must
        col = CY if down else GOLD
        words = lab.split(" "); lines = [lab]
        if len(lab) * 9 * 0.64 > sw - 6:
            cut = min(range(1, len(words)), key=lambda j: abs(len(" ".join(words[:j])) - len(" ".join(words[j:]))))
            lines = [" ".join(words[:cut]), " ".join(words[cut:])]
        for j, ln in enumerate(lines):
            o.append(plate_label(x, y + 16 + j * 12, ln, col, 8.5, halo_="#0B1A2E"))
    return "".join(o), pts, sw, foot

def humbled(w, h):
    """Who, existing in the form of God … emptied himself, taking the form of a servant … he humbled himself, becoming
    obedient even unto death, yea, the death of the cross (2:5–8): a plate of the way down — five steps from the light of
    the form of God at the upper left, the light growing less at every step; on the fourth, in fashion as a man, ntcast's
    Jesus, small; and at the foot, at the lower right, the hill of the three crosses far off under a dark red sky."""
    from ntcast import jesus_fig
    svg, pts, sw, foot = _stairs(w, h, "PHILIPPIANS 2:5–8 · HE EMPTIED HIMSELF",
                                 ["IN THE FORM OF GOD", "EMPTIED HIMSELF", "THE FORM OF A SERVANT", "IN FASHION AS A MAN", "HUMBLED HIMSELF"], down=True)
    o = [svg, mk.defs("hb", *ALL)]
    for i, (x, y) in enumerate(pts):
        r = 22 - i * 4
        if i != 3: o.append(halo(x, y - 14, r * 1.8, "#FFF4C2", 0.3 + (0.35 if i == 0 else 0)) + f'<circle cx="{f(x)}" cy="{f(y - 14)}" r="{f(max(3, r * 0.4))}" fill="#FFFDF0"></circle>')
    o.append(rays(pts[0][0], pts[0][1] - 14, 16, 16, 60, "#FFF4C2", 0.5, 2))
    x3, y3 = pts[3]
    js = min(sw * 0.9, (y3 - 70)) / 230
    o.append(jesus_fig("hb", x3, y3, js, glow=True))
    # the end of the way: the hill and the three crosses far off, a dark red rim behind
    hx, hy = pts[-1][0] + sw, foot
    hw = sw * 0.9
    o.append(f'<defs><clipPath id="hbc"><rect x="{f(hx - sw / 2)}" y="{f(pts[-1][1] - 60)}" width="{f(sw)}" height="{f(foot - pts[-1][1] + 60)}"></rect></clipPath></defs>'
             f'<g clip-path="url(#hbc)"><rect x="{f(hx - sw / 2)}" y="{f(pts[-1][1] - 60)}" width="{f(sw)}" height="{f(foot)}" fill="#1A0A10"></rect>'
             + halo(hx, hy - 20, sw * 0.6, "#8A2A1A", 0.6)
             + f'<path d="M{f(hx - hw)} {f(hy)} C {f(hx - hw * 0.5)} {f(hy - 40)} {f(hx + hw * 0.5)} {f(hy - 40)} {f(hx + hw)} {f(hy)} Z" fill="#0D0D0F"></path>')
    for dx, hh in ((-0.28, 22), (0, 30), (0.28, 22)):
        x, y = hx + dx * sw, hy - 30 - (6 if dx == 0 else 0)
        o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y - hh)} M{f(x - hh * 0.32)} {f(y - hh * 0.72)} L {f(x + hh * 0.32)} {f(y - hh * 0.72)}" stroke="#0D0D0F" stroke-width="3.4"></path>')
    o.append('</g>' + f'<rect x="{f(hx - sw / 2)}" y="{f(pts[-1][1] - 60)}" width="{f(sw)}" height="{f(foot - pts[-1][1] + 60)}" fill="none" stroke="#FF8A6A" stroke-width="1.6"></rect>')
    o.append(plate_label(hx + sw * 0.42, pts[-1][1] - 72, "UNTO DEATH", "#FF8A6A", 9, anchor="end"))
    o.append(route([(x, y - 14) for i, (x, y) in enumerate(pts) if i != 3] + [(hx - sw * 0.36, pts[-1][1] - 30)], color=CY, sw=2))
    return "".join(o)

def exalted(w, h):
    """Wherefore also God highly exalted him, and gave unto him the name which is above every name; that in the name of
    Jesus every knee should bow … and every tongue confess that Jesus Christ is Lord (2:9–11): a plate of the way up — from
    the foot at the lower left, step by step up to the light at the upper right, the light growing at every step; at the
    foot of the plate the three ranks, in heaven, on earth and under the earth."""
    svg, pts, sw, foot = _stairs(w, h, "PHILIPPIANS 2:9–11 · GOD HIGHLY EXALTED HIM",
                                 ["GOD HIGHLY EXALTED HIM", "THE NAME ABOVE EVERY NAME", "EVERY KNEE SHOULD BOW", "EVERY TONGUE SHOULD CONFESS", "JESUS CHRIST IS LORD"],
                                 down=False)
    o = [svg]
    for i, (x, y) in enumerate(pts):
        r = 6 + i * 4
        o.append(halo(x, y - 14, r * 2, "#FFE680", 0.3 + 0.08 * i) + f'<circle cx="{f(x)}" cy="{f(y - 14)}" r="{f(r * 0.45)}" fill="#FFFDF0"></circle>')
    o.append(rays(pts[-1][0], pts[-1][1] - 14, 22, 18, 80, "#FFE680", 0.6, 2.4))
    o.append(route([(pts[0][0] - sw * 0.9, foot - 8)] + [(x, y - 14) for x, y in pts[:-1]] + [(pts[-1][0] - 16, pts[-1][1] - 18)], color=GOLD, sw=2.4))
    # every knee, in its three ranks: a legend at the upper left
    o.append(plate_label(14, 42, "EVERY KNEE · IN HEAVEN · ON EARTH · UNDER THE EARTH", "#F3EFE6", 8.5, anchor="start"))
    return "".join(o)

def lights_world(w, h, seed):
    """Children of God … in the midst of a crooked and perverse generation, among whom ye are seen as lights in the world,
    holding forth the word of life: a city at night, its crooked streets dark, and here and there a window or a doorway
    with a lamp burning; the stars over it."""
    o = [sky(w, h, "#05051A", "#1E1650"), mk.stars(140, w, h * 0.5, seed), mk.stars(24, w, h * 0.42, seed + 3, color="#FFE680")]
    r = random.Random(seed)
    for row, (y0, k) in enumerate(((0.5, 0.7), (0.62, 0.85), (0.76, 1.0))):
        x = -20
        while x < w + 20:
            bw = r.uniform(50, 90) * k; bh = r.uniform(40, 80) * k
            tilt = r.uniform(-4, 4)
            base = h * y0 + r.uniform(-6, 6) + bh
            o.append(f'<g transform="rotate({tilt:.1f} {f(x + bw / 2)} {f(base)})"><rect x="{f(x)}" y="{f(base - bh)}" width="{f(bw)}" height="{f(bh + h)}" fill="{["#1A1830", "#14122A", "#221E3A"][row]}" stroke="{INK}" stroke-width="1.6"></rect>')
            if r.random() < 0.34:
                wx, wy = x + bw * r.uniform(0.2, 0.6), base - bh * r.uniform(0.4, 0.7)
                o.append(glow(wx + 6 * k, wy + 8 * k, 34 * k, "#FFC14D", 0.55, f"lw{seed}{row}{int(x)}") + f'<rect x="{f(wx)}" y="{f(wy)}" width="{f(12 * k)}" height="{f(16 * k)}" fill="#FFD27A" stroke="{INK}" stroke-width="1"></rect>')
            else:
                o.append(f'<rect x="{f(x + bw * 0.4)}" y="{f(base - bh * 0.6)}" width="{f(10 * k)}" height="{f(14 * k)}" fill="#0B0B1A" stroke="{INK}" stroke-width="1"></rect>')
            o.append('</g>')
            x += bw + r.uniform(-4, 6)
    # a crooked lane winding through
    o.append(f'<path d="M{f(w * 0.3)} {f(h + 10)} C {f(w * 0.46)} {f(h * 0.9)} {f(w * 0.36)} {f(h * 0.84)} {f(w * 0.52)} {f(h * 0.78)}" fill="none" stroke="#2A2840" stroke-width="{f(h * 0.06)}"></path>')
    lx, ly = w * 0.58, h * 0.9                                 # one holding a lamp up in a doorway
    o.append(glow(lx, ly - 30, 80, "#FFC14D", 0.6, f"lw{seed}d") + f'<rect x="{f(lx - 14)}" y="{f(ly - 60)}" width="28" height="60" fill="#FFC14D" stroke="{INK}" stroke-width="1.6"></rect>'
             + clay_lamp(lx, ly - 40, 0.6))
    return "".join(o)

def drink_offering(w, h, seed):
    """If I am offered upon the sacrifice and service of your faith (poured out as a drink-offering): the altar of stone
    with its fire, and a priest's hand in a white sleeve tilting a golden jug, the wine poured out on the sacrifice; the
    smoke going up."""
    o = [sky(w, h, "#3A2A4A", "#E8A060"), halo(w * 0.5, h * 0.5, h * 0.6, "#FFC14D", 0.35)]
    ax, ab, aw = w * 0.5, h * 0.98, min(w * 0.42, h * 0.9)
    at = ab - aw * 0.5
    o.append(f'<path d="M{f(ax - aw * 0.44)} {f(at)} C {f(ax - aw * 0.3)} {f(at - 100)} {f(ax - aw * 0.1)} {f(-20)} {f(ax - aw * 0.2)} {f(-30)} L {f(ax + aw * 0.3)} {f(-30)} C {f(ax + aw * 0.2)} {f(at - 120)} {f(ax + aw * 0.4)} {f(at - 60)} {f(ax + aw * 0.44)} {f(at)} Z" fill="#6A6070" opacity="0.4"></path>')
    o.append(E.blaze(ax, at, aw * 0.36, aw * 0.4, seed, n=6))
    o.append(f'<rect x="{f(ax - aw / 2)}" y="{f(at)}" width="{f(aw)}" height="{f(ab - at)}" fill="#A89880" stroke="{INK}" stroke-width="3"></rect>')
    for j in range(3):
        y = at + (ab - at) * (j + 1) / 4
        o.append(f'<path d="M{f(ax - aw / 2)} {f(y)} L {f(ax + aw / 2)} {f(y)}" stroke="#7A6A58" stroke-width="2"></path>')
        for i in range(4):
            x = ax - aw / 2 + aw * (i + (0.5 if j % 2 else 0)) / 4
            o.append(f'<path d="M{f(x)} {f(y - (ab - at) / 4)} L {f(x)} {f(y)}" stroke="#7A6A58" stroke-width="2"></path>')
    for sx in (-1, 1):                                          # the horns of the altar
        o.append(f'<path d="M{f(ax + sx * aw / 2)} {f(at)} L {f(ax + sx * (aw / 2 - 14))} {f(at - 20)} L {f(ax + sx * (aw / 2 - 26))} {f(at)} Z" fill="#A89880" stroke="{INK}" stroke-width="2"></path>')
    jx, jy = ax - aw * 0.62, at - aw * 0.42                      # the jug, tipped, and the sleeve and hand from the left
    k = aw / 260
    o.append(f'<path d="M-10 {f(jy - 70 * k)} C {f(jx - 120 * k)} {f(jy - 60 * k)} {f(jx - 60 * k)} {f(jy - 30 * k)} {f(jx - 20 * k)} {f(jy - 10 * k)} L {f(jx - 34 * k)} {f(jy + 26 * k)} '
             f'C {f(jx - 80 * k)} {f(jy + 10 * k)} {f(jx - 140 * k)} {f(jy + 10 * k)} -10 {f(jy + 20 * k)} Z" fill="#F3EFE6" stroke="{INK}" stroke-width="2.4"></path>')
    o.append(f'<g transform="translate({f(jx)} {f(jy)}) rotate(58) scale({f(k)})">'
             '<path d="M-22 40 C -30 10 -26 -20 -14 -34 L -10 -48 L 10 -48 L 14 -34 C 26 -20 30 10 22 40 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2.4"></path>'
             '<path d="M10 -46 L 26 -60 L 22 -44 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>'
             '<path d="M-24 -10 C -44 -12 -46 20 -24 22" fill="none" stroke="#B8860E" stroke-width="5"></path>'
             '<path d="M-20 0 L 20 0 M-22 14 L 22 14" stroke="#B8860E" stroke-width="2"></path></g>')
    o.append(f'<ellipse cx="{f(jx - 34 * k)}" cy="{f(jy + 4 * k)}" rx="{f(16 * k)}" ry="{f(12 * k)}" fill="{SKIN}" stroke="{INK}" stroke-width="2"></ellipse>')
    sx_, sy_ = jx + 52 * k, jy + 30 * k                       # the stream of wine falling on the fire
    o.append(f'<path d="M{f(sx_)} {f(sy_)} C {f(sx_ + 20 * k)} {f(sy_ + 40 * k)} {f(ax - aw * 0.2)} {f(at - 60 * k)} {f(ax - aw * 0.16)} {f(at - 4)}" fill="none" stroke="#8A0E26" stroke-width="{f(7 * k)}" stroke-linecap="round"></path>')
    return "".join(o)

def timothy_by(p, w, h, seed):
    """I hope in the Lord Jesus to send Timothy shortly unto you: the room at Rome, Paul sitting chained to the soldier,
    turned to Timothy standing ready with his staff and his cloak for the road."""
    staff = '<path d="M-60 -150 L -64 4" stroke="#6A4A2A" stroke-width="5"></path>'
    def tim(p_, x, y, s, flip=False):                          # facing Paul, the staff in his hand
        return robed(p_, x - 0.07 * w, y, s, TIMOTHY_LOOK["cloth"], hair=TIMOTHY_LOOK["hair"], belt=TIMOTHY_LOOK["belt"], mantle="#5A5A64",
                     up=[(-22, -158), (-40, -146), (-58, -150)], extra=staff)
    return study(p, w, h, seed, stage="prison", scribe=False, others=(tim,), window="rome", fig_h=min(h * 0.72, 300))

def sickbed(p, w, h, seed):
    """He was sick nigh unto death: but God had mercy on him: a room at Rome by lamplight, Epaphroditus lying on a bed under
    a blanket, Paul sitting beside him on a stool, chained to the soldier at the door, his hand on the sick man's shoulder."""
    b = h * 0.94
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp", "LieB", "LieA"), room(w, h, b, wall="#5E4A3C", floor="#3A2E26"),
         lamp_glow(w * 0.6, b - h * 0.3, max(w, h) * 0.55, f"{p}lg", op=0.45)]
    o.append(rome_window(w * 0.4, h * 0.14, min(w * 0.16, h * 0.4), h * 0.3, True, seed))
    s = fit(b, b - min(h * 0.72, 210))
    bx, bw = w * 0.74, min(w * 0.42, 300 * s)
    o.append(f'<rect x="{f(bx - bw / 2)}" y="{f(b - 46 * s)}" width="{f(bw)}" height="{f(14 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(xx)}" y="{f(b - 32 * s)}" width="{f(8 * s)}" height="{f(32 * s)}" fill="#4A2A14" stroke="{INK}" stroke-width="1.6"></rect>' for xx in (bx - bw / 2 + 4 * s, bx + bw / 2 - 12 * s)))
    by = b - 46 * s
    o.append(on_bed(p, bx, by - 12 * s, bw * 0.96, cloth="#E8E2D6", bed="#D8CCB0"))
    hx, hy, hr = bx - 0.417 * bw * 0.96, by - 12 * s - 0.057 * bw * 0.96, 0.057 * bw * 0.96   # his head on the pillow: skin, beard, headcloth
    L = EPAPHRODITUS_LOOK
    o.append(f'<circle cx="{f(hx)}" cy="{f(hy)}" r="{f(hr)}" fill="{SKIN}" stroke="{INK}" stroke-width="2"></circle>'
             f'<path d="M{f(hx - hr * 1.1)} {f(hy + hr * 0.2)} C {f(hx - hr * 1.2)} {f(hy - hr * 1.3)} {f(hx + hr * 0.6)} {f(hy - hr * 1.4)} {f(hx + hr * 0.5)} {f(hy - hr * 0.2)} '
             f'C {f(hx)} {f(hy - hr * 0.7)} {f(hx - hr * 0.6)} {f(hy - hr * 0.4)} {f(hx - hr * 1.1)} {f(hy + hr * 0.2)} Z" fill="{L["head"]}" stroke="{INK}" stroke-width="1.6"></path>'
             f'<path d="M{f(hx + hr * 0.2)} {f(hy + hr * 0.5)} C {f(hx + hr * 0.6)} {f(hy + hr * 1.2)} {f(hx + hr * 1.2)} {f(hy + hr * 0.9)} {f(hx + hr * 1.0)} {f(hy + hr * 0.2)} Z" fill="{L["beard"]}" stroke="{INK}" stroke-width="1.2"></path>')
    o.append(f'<path d="M{f(bx - bw * 0.3)} {f(by - 10 * s)} C {f(bx - bw * 0.26)} {f(by - 40 * s)} {f(bx + bw * 0.4)} {f(by - 42 * s)} {f(bx + bw * 0.48)} {f(by - 8 * s)} L {f(bx + bw * 0.48)} {f(by + 4 * s)} L {f(bx - bw * 0.3)} {f(by + 4 * s)} Z" '
             f'fill="#5A6A4A" stroke="{INK}" stroke-width="2"></path>')
    o.append(clay_lamp(w * 0.5, b - 52 * s, s * 0.8) + low_table(w * 0.46, b, 44 * s, s))
    gx, px = w * 0.08, w * 0.3
    o.append(guard_r(p, gx, b, s) + stool(px, b, s) + paul_fig(p, px, b, s, flip=True, pose="sit", seat=None, up=[(-22, -158), (-50, -146), (-80, -138)]))
    o.append(chain(*guard_hand(gx, b, s), *robed_hand(px, b, s, flip=True, pose="sit"), s=s * 0.8))
    return "".join(o)

def homeward(p, w, h, seed, who=None, scroll=True):
    """I have sent him therefore the more diligently: Epaphroditus walking home along the Egnatian Way in the morning, the
    sealed letter in his hand, a milestone at the roadside, Philippi on its hill far off."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#8FD0E2", "#FFE6B0"), hills(w, h, h * 0.42, seed, color="#9A9A7A", amp=16, step=90),
         town_hill(w * 0.82, h * 0.5, w * 0.14, h * 0.16, seed, color="#8A8A6A"),
         hills(w, h, h * 0.52, seed + 1, color="#B8A86A", amp=8, step=70), ground(w, h, h * 0.58, "#C8B87A", dy=0)]
    o.append(f'<path d="M{f(w * 0.74)} {f(h * 0.58)} L {f(w * 0.8)} {f(h * 0.58)} L {f(w * 0.98)} {f(h + 10)} L {f(-w * 0.1)} {f(h + 10)} Z" fill="#B8A890" stroke="{INK}" stroke-width="1.6"></path>')
    for j in range(6):
        y = h * 0.6 + j * h * 0.07
        o.append(f'<path d="M{f(w * (0.74 - j * 0.14))} {f(y)} L {f(w * (0.8 + j * 0.03))} {f(y)}" stroke="#9A8A72" stroke-width="1.4"></path>')
    o.append(f'<rect x="{f(w * 0.08)}" y="{f(b - 60)}" width="18" height="60" rx="6" fill="#D8D0C0" stroke="{INK}" stroke-width="2"></rect>')
    s = fit(b, b - min(h * 0.72, 210))
    fig = who or epaphroditus
    o.append(fig(p, w * 0.42, b, s, flip=True, pose="walk", up=[(-22, -158), (-36, -132), (-52, -124)] if scroll else None,
                 extra=sealed_scroll(-58, -124, 0.26, rot=-20) if scroll else ""))
    return "".join(o)
