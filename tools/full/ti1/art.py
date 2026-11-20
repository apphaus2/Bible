"""Drawings for the 1 Timothy volume (and, by `from ti1.art import *`, for 2 Timothy and Titus). 1 Timothy starts from all of
Galatians' drawings (`from gal.art import *`, which carries Acts', Mark's and Matthew's drawings and the epistle kit) and
borrows from the Corinthian letters and Romans, and adds its own.

The pastoral letters' people at a distance, on the kit silhouettes (epistle.robed): Paul only ever epistle.paul_fig;
Timothy (timothy_fig) young, beardless, bareheaded, brown hair, a grey-blue tunic (Acts' colours); Titus (titus_fig) a
Greek, bareheaded, short black hair, clean-shaven, a sand tunic and a blue mantle; the elders and the church in cool and
off-white headcloths and veils. God is never drawn (light); Satan and demons are never drawn. Every function takes
(p, w, h, seed, ...) or (w, h, ...); p, a prefix unique to the panel, names the figure defs and gradients."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from gal.art import *
from gal.art import _defs, _person_mark
from co1.art import _eph_window, _seated_lap
from co2.art import timothy_fig, titus_fig
from co1.art5 import cells, risen_fig
from rom.art4 import crowd_back
from ntcast import jesus_fig, JESUS_SKIN
from epistle import low_table, stool, bench, inkpot, reed_pen, open_letter, sealed_scroll, lamp_glow, plate_bg, robed, paul_fig, pigeonholes, doorway, couch
from genesis.art4 import clay_lamp
from ti1.common import TIMOTHY_LOOK, TITUS_LOOK, LUKE_LOOK, LOIS_LOOK, EUNICE_LOOK
from act import geo

CREAM, PAPER_INK = "#F3EAD0", "#3A2A1A"

def elder(p, x, y, s, i=0, flip=False, up=None, extra=""):
    """An elder of the church at Ephesus: grey or white beard, a cool or off-white headcloth, a plain robe and mantle."""
    c, hd, bd, mn = [("#5A6A7A", "#E8E2D6", "#C8C2B6", "#3A4A5A"), ("#6A5A4A", "#2A3A4A", "#9A948A", "#4A3A2A"), ("#4A5A4A", "#F3EFE6", "#E8E2D6", "#2A3A2A"),
                     ("#5A4A5A", "#1F2F3A", "#7A746A", "#3A2A3A")][i % 4]
    return robed(p, x, y, s, c, head=hd, cord="#2A1A10", beard=bd, mantle=mn, flip=flip, up=up, extra=extra)

def woman(p, x, y, s, i=0, flip=False, up=None, old=False, extra=""):
    """A woman of the church: a plain robe and a cool, dark or off-white veil; old=True grey hair under it."""
    c, vl = [("#6A6A7A", "#1F2F4A"), ("#5A7A7A", "#E8E2D6"), ("#7A6A5A", "#2A2A3A"), ("#6A5A6A", "#3A4A5A")][i % 4]
    return robed(p, x, y, s * 0.94, c, woman=True, veil=vl, hair="#B8B2A6" if old else None, flip=flip, up=up, extra=extra)

def young_man(p, x, y, s, i=0, flip=False, up=None, extra=""):
    """A younger man: bareheaded or in a dark headcloth, beardless or a short dark beard."""
    c, hr, bd, hd = [("#8A7A5A", "#2A1A10", None, None), ("#4A5A6A", "#1A1210", "#1A1210", None), ("#6A4A3A", None, None, "#1F2F3A")][i % 3]
    return robed(p, x, y, s, c, hair=hr, beard=bd, head=hd, flip=flip, up=up, extra=extra)

def messenger(p, x, y, s, flip=False, up=None, extra=""):
    """The brother who carries the letter: a travelling cloak, an off-white headcloth, a short dark beard."""
    return robed(p, x, y, s, "#6A6A5A", head="#E8E2D6", cord="#4A3A2A", beard="#2A1A10", mantle="#4A4A3A", belt="#3A2A1A", flip=flip, up=up, extra=extra)

def _sheet(x, y, wd, hh, rot=0):
    """An open sheet of the letter held up, in a figure's own units (centre x, y)."""
    return (f'<g transform="rotate({rot} {f(x)} {f(y)})"><rect x="{f(x - wd / 2)}" y="{f(y - hh / 2)}" width="{f(wd)}" height="{f(hh)}" fill="#EADBB4" stroke="{INK}" stroke-width="1.8"></rect>'
            + "".join(f'<path d="M{f(x - wd / 2 + 5)} {f(y - hh / 2 + 6 + k * (hh - 10) / 5)} L {f(x + wd / 2 - 5 - (k % 2) * 6)} {f(y - hh / 2 + 6 + k * (hh - 10) / 5)}" stroke="#7A5A3A" stroke-width="1.4"></path>' for k in range(6))
            + f'<rect x="{f(x - wd / 2 - 3)}" y="{f(y - hh / 2 - 3)}" width="5" height="{f(hh + 6)}" rx="2" fill="#C8A878" stroke="{INK}" stroke-width="1.2"></rect>'
            f'<rect x="{f(x + wd / 2 - 2)}" y="{f(y - hh / 2 - 3)}" width="5" height="{f(hh + 6)}" rx="2" fill="#C8A878" stroke="{INK}" stroke-width="1.2"></rect></g>')

def fig_k(w, h, wfrac=0.32, hfrac=0.72):
    """A standing figure's scale in a scene: about hfrac of the drawing's height, but never wider a crowd than the panel
    holds (wfrac of its width), so a tall panel shows more wall or sky above the people instead of giants cut off."""
    return min(h * hfrac, w * wfrac) / 205

READ_UP = [(-22, -158), (-46, -136), (-62, -128)]               # an arm holding the open sheet before the face (seated)

def timothy_fig_(p, x, y, s, flip=False, up=None, extra="", pose="stand", seat="stool", beard=None):
    """Timothy on robed() in every pose (co2.art.timothy_fig stands only); beard= a short beard (2 Timothy)."""
    t = TIMOTHY_LOOK
    return robed(p, x, y, s, t["cloth"], hair=t["hair"], belt=t["belt"], beard=beard, flip=flip, up=up, extra=extra, pose=pose, seat=seat)

def titus_fig_(p, x, y, s, flip=False, up=None, extra="", pose="stand", seat="stool"):
    t = TITUS_LOOK
    return robed(p, x, y, s, t["cloth"], hair=t["hair"], mantle=t["mantle"], belt=t["belt"], flip=flip, up=up, extra=extra, pose=pose, seat=seat)

# ---- the letter written, carried and read --------------------------------------------------------------------------------
def paul_writes(p, w, h, seed, window=None):
    """The letter written in Macedonia (1:3): a plain room by lamplight, Paul alone, sitting on the floor at the low table with
    the reed pen in his own hand, the roll across his knee; a window on the night hills; his staff and travelling bag by the
    door (he is free and on the road)."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp"), room(w, h, b, wall="#5A3E2E", floor="#3A2A20"), lamp_glow(w * 0.5, b - h * 0.3, max(w, h) * 0.6, f"{p}pw", op=0.55)]
    k = min(1.2, h / 220)
    s = fit(b, b - min(h * 0.72, 196))
    o.append((window or night_window)(w * 0.62, b - 190 * k, min(w * 0.16, 96 * k), min(h * 0.34, 74 * k), seed))
    tx = w * 0.3
    o.append(low_table(tx, b, 150 * k, k) + clay_lamp(tx + 130 * k, b - 31 * k, k * 0.8) + inkpot(tx + 104 * k, b - 30 * k, k * 0.6))
    o.append(f'<g transform="rotate(-2 {f(tx + 50 * k)} {f(b - 34 * k)})">' + open_letter(tx + 10 * k, b - 40 * k, 80 * k, 10 * k, rows=2, seed=seed) + '</g>')
    pen = ('<path d="M10 -96 L 64 -60" stroke="#0D0D0F" stroke-width="10" stroke-linecap="round"></path><path d="M10 -96 L 64 -60" stroke="#6A4A2A" stroke-width="7" stroke-linecap="round"></path>'
           '<path d="M64 -60 L 76 -84" stroke="#C8A060" stroke-width="2.4"></path>')
    o.append(_seated_lap(tx - 6 * k, b, s * 0.8, ROBES["paul"], "#5A4A3A", "#3A2A1A", pen))
    dx = w * 0.86                                                   # the staff against the wall, the bag on the floor
    o.append(f'<path d="M{f(dx)} {f(b)} L {f(dx + 14 * k)} {f(b - 170 * k)}" stroke="{INK}" stroke-width="{f(7 * k)}" stroke-linecap="round"></path>'
             f'<path d="M{f(dx)} {f(b)} L {f(dx + 14 * k)} {f(b - 170 * k)}" stroke="#6A4A2A" stroke-width="{f(4.5 * k)}" stroke-linecap="round"></path>'
             f'<path d="M{f(dx + 22 * k)} {f(b)} C {f(dx + 18 * k)} {f(b - 30 * k)} {f(dx + 30 * k)} {f(b - 44 * k)} {f(dx + 46 * k)} {f(b - 44 * k)} C {f(dx + 62 * k)} {f(b - 44 * k)} {f(dx + 72 * k)} {f(b - 30 * k)} {f(dx + 68 * k)} {f(b)} Z" '
             f'fill="#7A5A3A" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(dx + 30 * k)} {f(b - 40 * k)} C {f(dx + 40 * k)} {f(b - 56 * k)} {f(dx + 52 * k)} {f(b - 56 * k)} {f(dx + 60 * k)} {f(b - 40 * k)}" fill="none" stroke="{INK}" stroke-width="2"></path>')
    return "".join(o)

def ephesus_road(w, h):
    """As I exhorted thee to tarry at Ephesus, when I was going into Macedonia: the letter's road from Macedonia (Philippi, the
    church Paul knew best there) by Neapolis and Troas across the sea to Ephesus, on Acts' map."""
    rt = ["PHILIPPI", "NEAPOLIS", (25.3, 40.3), "TROAS", (25.9, 39.4), (26.2, 38.7), (26.6, 38.2), "EPHESUS"]
    return letter_road(w, h, rt, title="1 TIMOTHY 1:3 · FROM MACEDONIA TO EPHESUS", box=(21.6, 29.4, 36.9, 41.6),
                       places=("PHILIPPI", "NEAPOLIS", "TROAS", "EPHESUS", "THESSALONICA", "CORINTH", "MILETUS"), hi=("PHILIPPI", "EPHESUS"),
                       regions=("MACEDONIA", "ACHAIA", "ASIA"))

def timothy_receives(p, w, h, seed):
    """Unto Timothy, my true child in faith: Timothy's room at Ephesus by day, the window on the theatre and the temple of
    Diana; the brother come from Macedonia standing in the open doorway with the sealed roll, Timothy reaching to take it."""
    return study(p, w, h, seed, stage="give", scribe=False, writer=timothy_fig_, bearer=messenger, window=_eph_window, night=False, fig_h=min(h * 0.72, w * 0.34))

def timothy_reads(p, w, h, seed, night=True, beard=None, window=None, sheet=True, x=0.58, tx=0.3):
    """Timothy reading the letter: his room at Ephesus (window= the window on the theatre and the temple of Diana), Timothy
    sitting on a stool holding the open sheet up before him, the lamp and the broken seal on the low table beside him, the
    pigeonholes of scrolls on the wall. beard= his short beard (2 Timothy); x=, tx= where he and the table stand (fractions of
    the width: an end panel moves him left, clear of the end mark)."""
    b = h * 0.95
    k = fig_k(w, h, 0.42)
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#5A3E2E" if night else "#D8C098", floor="#3A2A20" if night else "#8A6A4A")]
    if night: o.append(lamp_glow(w * 0.42, b - 70 * k, max(w, h) * 0.55, f"{p}tr", op=0.5))
    win = window or _eph_window
    o.append(win(w * 0.06, b - 205 * k, min(w * 0.2, 120 * k), min(h * 0.38, 92 * k), night, seed))
    o.append(pigeonholes(w * 0.74, b - 205 * k, min(w * 0.18, 120 * k), min(h * 0.3, 76 * k), seed))
    tx = w * tx
    o.append(low_table(tx, b, 60 * k, k) + clay_lamp(tx + 18 * k, b - 31 * k, k * 0.55) + sealed_scroll(tx + 46 * k, b - 32 * k, 0.32 * k, rot=-8))
    held = _sheet(-74, -132, 46, 34, rot=-8) if sheet else ""
    o.append(timothy_fig_(p, w * x, b, k, up=READ_UP if sheet else None, extra=held, pose="sit", beard=beard))
    return "".join(o)

def wreck_rocks(p, w, h, seed):
    """Which some having thrust from them made shipwreck concerning the faith: a ship broken on the rocks of a grey shore,
    her mast gone and her planks scattered on the swell — no one in the water."""
    o = [co2_wreck(p, w, h, seed)]
    r = random.Random(seed)
    for x0, x1, top in ((-0.04, 0.22, 0.6), (0.62, 0.84, 0.66), (0.8, 1.06, 0.56)):
        pts = [(w * x0, h + 4)]
        n = 5
        for i in range(n + 1):
            pts.append((w * (x0 + (x1 - x0) * i / n), h * (top + r.uniform(-0.04, 0.08) + (0.1 if i in (0, n) else 0))))
        pts.append((w * x1, h + 4))
        o.append(f'<path d="M' + " L ".join(f"{f(a)} {f(c)}" for a, c in pts) + f' Z" fill="#2A2830" stroke="{INK}" stroke-width="2.4"></path>')
        o.append(f'<path d="M{f(w * (x0 + 0.03))} {f(h * (top + 0.14))} L {f(w * (x0 + (x1 - x0) * 0.5))} {f(h * (top + 0.06))}" stroke="#4A4858" stroke-width="2"></path>')
    o.append(waves(w, h, h * 0.92, seed + 3))
    return "".join(o)

from co2.art3 import wreck as co2_wreck

# ---- 1 Timothy 2 -----------------------------------------------------------------------------------------------------------
def hall_on_hill(cx, base, wd, seed, banner="#5A1A6A"):
    """The governor's hall on its hill: a broad colonnaded front on a podium, a low pediment, purple banners; (cx, base) the
    middle of its foot."""
    u = wd / 100; o = []
    o.append(f'<rect x="{f(cx - 52 * u)}" y="{f(base - 10 * u)}" width="{f(104 * u)}" height="{f(10 * u)}" fill="#D8D0C0" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<rect x="{f(cx - 46 * u)}" y="{f(base - 40 * u)}" width="{f(92 * u)}" height="{f(30 * u)}" fill="#C8BCA8" stroke="{INK}" stroke-width="1.6"></rect>')
    for i in range(9):
        x = cx - 42 * u + i * 10.5 * u
        o.append(f'<rect x="{f(x)}" y="{f(base - 40 * u)}" width="{f(4 * u)}" height="{f(30 * u)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1"></rect>')
    o.append(f'<path d="M{f(cx - 50 * u)} {f(base - 40 * u)} L {f(cx)} {f(base - 54 * u)} L {f(cx + 50 * u)} {f(base - 40 * u)} Z" fill="#E8DCC0" stroke="{INK}" stroke-width="1.6"></path>')
    for x in (cx - 30 * u, cx + 30 * u):
        o.append(f'<path d="M{f(x)} {f(base - 40 * u)} L {f(x)} {f(base - 24 * u)} L {f(x + 4 * u)} {f(base - 27 * u)} L {f(x + 8 * u)} {f(base - 24 * u)} L {f(x + 8 * u)} {f(base - 40 * u)} Z" fill="{banner}" stroke="{INK}" stroke-width="1"></path>')
    return "".join(o)

def prayer_kings(p, w, h, seed):
    """Supplications, prayers, intercessions, thanksgivings … for kings and all that are in high place: the church at Ephesus
    on a roof at morning, seen from behind, some with their hands lifted, looking out over the city to the governor's hall
    on its hill."""
    o = [sky(w, h, "#6A8AC0", "#FFE0A8"), halo(w * 0.7, h * 0.3, max(w, h) * 0.4, "#FFF4C2", 0.5),
         hills(w, h, h * 0.36, seed, color="#8A8A7A", amp=12, step=90),
         f'<path d="M{f(w * 0.48)} {f(h * 0.42)} C {f(w * 0.58)} {f(h * 0.3)} {f(w * 0.8)} {f(h * 0.28)} {f(w * 0.94)} {f(h * 0.42)} Z" fill="#A8987A" stroke="{INK}" stroke-width="1.8"></path>',
         hall_on_hill(w * 0.71, h * 0.33, min(w * 0.3, h * 0.6), seed),
         houses(w, h, h * 0.5, seed, hmin=0.08, hmax=0.14),
         f'<rect x="-10" y="{f(h * 0.5)}" width="{f(w + 20)}" height="{f(h * 0.6)}" fill="#C8B08A" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(h * 0.5)}" width="{f(w + 20)}" height="{f(h * 0.04)}" fill="#A8906A" stroke="{INK}" stroke-width="1.6"></rect>']
    o.append(crowd_back(p, w, h, seed, rows=2, height=0.44, ups=0.45))
    o.append(plate_label(w * 0.3, h * 0.24, "FOR KINGS AND ALL THAT ARE IN HIGH PLACE", "#12113A", 10, halo_="#FFF4C2"))
    return "".join(o)

def mediator(p, w, h):
    """One God, one mediator also between God and men, himself man, Christ Jesus: a plate — at the top a band of light (God is
    never drawn: light, and the label ONE GOD); at the foot a company of men in outline; between them, standing on the gold
    line that joins them, Christ Jesus in ntcast's look, his hands out."""
    o = [plate_bg(w, h, "1 TIMOTHY 2:5–6 · ONE GOD, ONE MEDIATOR"), mk.defs(p, *ALL, "ManUp"), mk.defs("gp", *ALL)]
    top = 40
    uid = f"{p}lg"
    o.append(f'<defs><linearGradient id="{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"></stop><stop offset="0.5" stop-color="#FFE680" stop-opacity="0.8"></stop>'
             f'<stop offset="1" stop-color="#FFE680" stop-opacity="0"></stop></linearGradient></defs>'
             f'<rect x="10" y="{top}" width="{f(w - 20)}" height="{f(h * 0.22)}" fill="url(#{uid})"></rect>')
    o.append(label(w * 0.5, top + h * 0.08, "ONE GOD", "#5A3A10", 12))
    base = h * 0.92
    sc = h * 0.26 / 205
    for i in range(10):
        x = w * (0.06 + i * 0.098)
        if abs(x - w * 0.5) < w * 0.07: continue
        o.append(_person_mark(x, base, sc * (0.9 + 0.08 * (i % 2)), "#163A56", head=i % 3 == 0, woman=i % 4 == 2, flip=i < 5))
    o.append(label(w * 0.2, min(base + 14, h - 4), "MEN", GOLD, 10) + label(w * 0.8, min(base + 14, h - 4), "ALL MEN", GOLD, 10))
    o.append(f'<path d="M{f(w * 0.5)} {f(top + h * 0.16)} L {f(w * 0.5)} {f(base - h * 0.06)}" stroke="{GOLD}" stroke-width="3" stroke-dasharray="7 5"></path>')
    js = (base - top - h * 0.2) / 215
    jb = base - h * 0.02
    o.append(halo(w * 0.5, jb - 110 * js, 120 * js, "#FFF4C2", 0.6))
    o.append(robed(p, w * 0.5, jb, js, "#E8E2D6", skin=JESUS_SKIN, mantle="#7A8A9A", up=[(-22, -158), (-50, -150), (-76, -146)], extra=_JESUS_HEAD))
    o.append(plate_label(w * 0.5 + 70 * js, jb - 120 * js, "HIMSELF MAN", CY, 9.5, anchor="start"))
    o.append(plate_label(w * 0.5 + 70 * js, jb - 104 * js, "CHRIST JESUS", GOLD, 10, anchor="start"))
    o.append(plate_label(w * 0.5 + 70 * js, jb - 84 * js, "A RANSOM FOR ALL", CY, 9.5, anchor="start"))
    return "".join(o)

from ntcast import _HAIR_FIG, _BEARD_FIG
_JESUS_HEAD = _HAIR_FIG + _BEARD_FIG

def holy_hands(p, w, h, seed):
    """I desire therefore that the men pray in every place, lifting up holy hands: three cells — a man on a housetop at
    morning, a man in a field at noon, a man in a room by lamplight — each standing with his hand lifted."""
    def roof(pp, cw, ch):
        b = ch * 0.92; s = fit(b, b - ch * 0.7)
        return (_defs(pp) + sky(cw, ch, "#8FD0E2", "#FFE6B0") + houses(cw, ch, ch * 0.62, seed, hmin=0.08, hmax=0.16)
                + f'<rect x="-4" y="{f(ch * 0.7)}" width="{f(cw + 8)}" height="{f(ch)}" fill="#D8C098" stroke="{INK}" stroke-width="2"></rect>'
                + elder(pp, cw * 0.5, b, s, 0, up=UP_HIGH, flip=True))
    def field(pp, cw, ch):
        b = ch * 0.92; s = fit(b, b - ch * 0.7)
        return (_defs(pp) + sky(cw, ch, "#5AB0D8", "#E8F0C8") + hills(cw, ch, ch * 0.56, seed, color="#7A9A5A", amp=8, step=50)
                + ground(cw, ch, ch * 0.66, "#9CCB5E", dy=0) + young_man(pp, cw * 0.5, b, s, 1, up=UP_HIGH))
    def lamp(pp, cw, ch):
        b = ch * 0.92; s = fit(b, b - ch * 0.7)
        return (_defs(pp) + room(cw, ch, b, wall="#5A3E2E", floor="#3A2A20") + lamp_glow(cw * 0.3, b - ch * 0.3, ch * 0.7, f"{pp}lg", op=0.5)
                + low_table(cw * 0.1, b, 40 * s, s) + clay_lamp(cw * 0.1 + 20 * s, b - 31 * s, s * 0.5) + elder(pp, cw * 0.6, b, s, 2, up=UP_HIGH, flip=True))
    o = [cells(p, w, h, [roof, field, lamp])]
    o += [plate_label(w * (i + 0.5) / 3, h * 0.1, t, "#12113A", 9.5, halo_="#F3EFE6") for i, t in enumerate(("ON THE HOUSETOP", "IN THE FIELD", "IN THE HOUSE"))]
    return "".join(o)

def _robe_item(x, y, s, cloth, veil=None):
    """A plain robe hung on a peg, its sleeves and skirt flat (no one wearing it); veil= a veil hung beside it."""
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">',
         '<path d="M-4 -6 L 4 -6 L 4 4 L -4 4 Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="1.4"></path>',
         f'<path d="M0 0 C -10 2 -26 8 -40 16 L -58 52 L -46 58 L -32 34 L -34 150 L 34 150 L 32 34 L 46 58 L 58 52 L 40 16 C 26 8 10 2 0 0 Z" fill="{cloth}" stroke="#0D0D0F" stroke-width="2.4"></path>',
         '<path d="M-8 6 L 0 18 L 8 6" fill="none" stroke="#0D0D0F" stroke-width="1.6"></path><path d="M-30 70 C -26 70 26 70 30 70" stroke="#5A4A3A" stroke-width="3"></path>',
         '<path d="M-14 80 C -16 110 -18 130 -20 148 M12 84 C 14 110 16 130 18 148" fill="none" stroke="#0D0D0F" stroke-width="1.2" opacity="0.4"></path>']
    if veil:
        o.append(f'<path d="M70 -2 L 76 -6 L 84 -2 L 98 120 C 90 126 70 126 60 120 Z" fill="{veil}" stroke="#0D0D0F" stroke-width="2.2"></path>'
                 '<path d="M74 -6 L 84 -6 L 84 2 L 74 2 Z" fill="#6A4A2A" stroke="#0D0D0F" stroke-width="1.2"></path>')
    return "".join(o) + "</g>"

def apparel(w, h):
    """Women adorn themselves in modest apparel … not with braided hair, and gold or pearls or costly raiment; but … through good
    works: a plate on cream paper — at the left a plain robe and veil hung on their pegs (MODEST APPAREL); in the middle the
    things set aside, lying on a cloth and worn by no one — a comb and pins for braiding, gold armlets and a necklace, a
    string of pearls, a fold of purple silk; at the right good works — a basket of loaves, a jug, a basin and a towel."""
    o = [f'<rect x="0" y="0" width="{f(w)}" height="{f(h)}" fill="{CREAM}"></rect>',
         f'<rect x="8" y="8" width="{f(w - 16)}" height="{f(h - 16)}" fill="none" stroke="{PAPER_INK}" stroke-width="1.4"></rect>',
         title_bar_cream(w, "1 TIMOTHY 2:9–10 · MODEST APPAREL · GOOD WORKS")]
    k = min(w / 600, (h - 60) / 210)
    cy = 40 + (h - 40) * 0.46
    ly = min(h - 36, cy + 96 * k)
    # modest apparel
    ax = w * 0.15
    o.append(_robe_item(ax - 14 * k, cy - 80 * k, k * 0.9, "#7A7A8A", veil="#2A3A5A"))
    o.append(two_lines(ax, ly, "MODEST APPAREL", PAPER_INK, 10))
    # the things set aside, on a cloth, struck through
    mx = w * 0.5
    cw_, ch_ = 230 * k, 120 * k
    o.append(f'<rect x="{f(mx - cw_ / 2)}" y="{f(cy - ch_ / 2)}" width="{f(cw_)}" height="{f(ch_)}" fill="#E0D4B8" stroke="{PAPER_INK}" stroke-width="1.6"></rect>')
    gx, gy = mx - 70 * k, cy - 22 * k                           # gold: a necklace and two armlets
    o.append(f'<path d="M{f(gx - 34 * k)} {f(gy - 10 * k)} C {f(gx - 30 * k)} {f(gy + 26 * k)} {f(gx + 30 * k)} {f(gy + 26 * k)} {f(gx + 34 * k)} {f(gy - 10 * k)}" fill="none" stroke="#E8B830" stroke-width="{f(5 * k)}"></path>'
             + "".join(f'<circle cx="{f(gx + 34 * k * math.cos(math.radians(a)))}" cy="{f(gy - 2 * k + 24 * k * math.sin(math.radians(a)))}" r="{f(3.6 * k)}" fill="#E8B830" stroke="{INK}" stroke-width="1"></circle>' for a in range(20, 170, 25))
             + f'<ellipse cx="{f(gx - 10 * k)}" cy="{f(gy + 44 * k)}" rx="{f(16 * k)}" ry="{f(7 * k)}" fill="none" stroke="#E8B830" stroke-width="{f(4.5 * k)}"></ellipse>'
             f'<ellipse cx="{f(gx + 20 * k)}" cy="{f(gy + 46 * k)}" rx="{f(16 * k)}" ry="{f(7 * k)}" fill="none" stroke="#C8981E" stroke-width="{f(4.5 * k)}"></ellipse>')
    px, py = mx + 10 * k, cy - 30 * k                           # pearls
    o.append("".join(f'<circle cx="{f(px + 50 * k * math.cos(math.radians(a)) * 0.6)}" cy="{f(py + 22 * k * math.sin(math.radians(a)))}" r="{f(4 * k)}" fill="#F8F4EC" stroke="#8A847A" stroke-width="1"></circle>' for a in range(0, 360, 18)))
    o.append(f'<path d="M{f(mx + 50 * k)} {f(cy + 4 * k)} L {f(mx + 104 * k)} {f(cy - 8 * k)} L {f(mx + 110 * k)} {f(cy + 40 * k)} L {f(mx + 58 * k)} {f(cy + 52 * k)} Z" fill="#6A1A6A" stroke="{INK}" stroke-width="1.6"></path>'
             f'<path d="M{f(mx + 56 * k)} {f(cy + 16 * k)} L {f(mx + 106 * k)} {f(cy + 4 * k)}" stroke="#E8B830" stroke-width="{f(2.4 * k)}"></path>')
    cx_, cy_ = mx + 10 * k, cy + 30 * k                          # a comb and pins for braiding
    o.append(f'<rect x="{f(cx_ - 22 * k)}" y="{f(cy_ - 6 * k)}" width="{f(44 * k)}" height="{f(9 * k)}" fill="#C8A060" stroke="{INK}" stroke-width="1.2"></rect>'
             + "".join(f'<path d="M{f(cx_ - 20 * k + i * 4.4 * k)} {f(cy_ + 3 * k)} L {f(cx_ - 20 * k + i * 4.4 * k)} {f(cy_ + 16 * k)}" stroke="#A8803A" stroke-width="{f(1.6 * k)}"></path>' for i in range(10))
             + f'<path d="M{f(cx_ + 30 * k)} {f(cy_ - 8 * k)} L {f(cx_ + 44 * k)} {f(cy_ + 18 * k)} M{f(cx_ + 38 * k)} {f(cy_ - 10 * k)} L {f(cx_ + 52 * k)} {f(cy_ + 16 * k)}" stroke="#8A6A3A" stroke-width="{f(2.4 * k)}"></path>')
    o.append(f'<path d="M{f(mx - cw_ / 2 - 6)} {f(cy + ch_ / 2 + 6)} L {f(mx + cw_ / 2 + 6)} {f(cy - ch_ / 2 - 6)}" stroke="#B5121B" stroke-width="{f(max(3, 5 * k))}" stroke-linecap="round" opacity="0.85"></path>')
    o.append(two_lines(mx, ly, "NOT WITH BRAIDED HAIR, GOLD, PEARLS, COSTLY RAIMENT", PAPER_INK, 9.5))
    # good works
    gx2 = w * 0.85
    bb = cy + 50 * k
    o.append(f'<path d="M{f(gx2 - 70 * k)} {f(bb - 30 * k)} L {f(gx2 - 20 * k)} {f(bb - 30 * k)} L {f(gx2 - 26 * k)} {f(bb)} L {f(gx2 - 64 * k)} {f(bb)} Z" fill="#B8884A" stroke="{INK}" stroke-width="1.8"></path>'
             + "".join(f'<ellipse cx="{f(gx2 - 56 * k + i * 13 * k)}" cy="{f(bb - 34 * k)}" rx="{f(9 * k)}" ry="{f(6 * k)}" fill="#D8A060" stroke="{INK}" stroke-width="1.2"></ellipse>' for i in range(3))
             + f'<path d="M{f(gx2 + 4 * k)} {f(bb)} C {f(gx2 - 6 * k)} {f(bb - 30 * k)} {f(gx2)} {f(bb - 50 * k)} {f(gx2 + 10 * k)} {f(bb - 60 * k)} L {f(gx2 + 22 * k)} {f(bb - 60 * k)} C {f(gx2 + 32 * k)} {f(bb - 50 * k)} {f(gx2 + 38 * k)} {f(bb - 30 * k)} {f(gx2 + 28 * k)} {f(bb)} Z" fill="#B85A32" stroke="{INK}" stroke-width="1.8"></path>'
             f'<ellipse cx="{f(gx2 - 10 * k)}" cy="{f(bb - 70 * k)}" rx="{f(40 * k)}" ry="{f(9 * k)}" fill="#C8C8D0" stroke="{INK}" stroke-width="1.6"></ellipse>'
             f'<path d="M{f(gx2 - 44 * k)} {f(bb - 72 * k)} L {f(gx2 - 50 * k)} {f(bb - 110 * k)} L {f(gx2 - 30 * k)} {f(bb - 112 * k)} L {f(gx2 - 30 * k)} {f(bb - 74 * k)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.4"></path>')
    o.append(two_lines(gx2, ly, "GOOD WORKS", PAPER_INK, 10))
    return "".join(o)

def two_lines(x, y, text, color, size):
    """A label in one or two centred lines (split at the middle word gap), its top at y."""
    if len(text) < 16: return label(x, y + size + 3, text, color, size)
    ws = text.split(" "); best = min(range(1, len(ws)), key=lambda i: abs(len(" ".join(ws[:i])) - len(" ".join(ws[i:]))))
    return label(x, y + size + 3, " ".join(ws[:best]), color, size) + label(x, y + 2 * size + 8, " ".join(ws[best:]), color, size)

def title_bar_cream(w, text):
    """A plate title in ink on cream paper (a label)."""
    return (f'<rect x="8" y="8" width="{f(w - 16)}" height="24" fill="{PAPER_INK}"></rect>' + label(18, 25, text, "#F3EAD0", 10, anchor="start"))

from act.art11 import diana_temple

def ephesus_dawn(w, h, seed):
    """Ephesus at sunrise (the cover): mount Pion at the left with the theatre's great bowl cut into its side, the city's
    roofs going down toward the sea at the right, and far off on the plain the temple of Diana; the sun coming up behind
    the hills."""
    o = [sky(w, h, "#3A2A5A", "#FFC890"), halo(w * 0.72, h * 0.3, max(w, h) * 0.45, "#FFE6B0", 0.55),
         f'<circle cx="{f(w * 0.72)}" cy="{f(h * 0.3)}" r="{f(h * 0.05)}" fill="#FFF4C2"></circle>',
         hills(w, h, h * 0.36, seed, color="#6A5A7A", amp=14, step=90)]
    o.append(f'<path d="M{f(w * 0.5)} {f(h * 0.5)} L {f(w * 0.76)} {f(h * 0.47)} L {f(w * 0.78)} {f(h * 0.5)} Z" fill="#8A8A6A" stroke="{INK}" stroke-width="1.6"></path>' + diana_temple(w * 0.68, h * 0.485, w * 0.14))
    o.append(f'<path d="M{f(w * 0.55)} {f(h * 0.5)} C {f(w * 0.7)} {f(h * 0.47)} {f(w * 0.9)} {f(h * 0.48)} {f(w + 10)} {f(h * 0.47)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.55)} {f(h + 10)} Z" fill="#3A6A8A" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<path d="M-10 {f(h * 0.62)} C {f(w * 0.06)} {f(h * 0.3)} {f(w * 0.22)} {f(h * 0.2)} {f(w * 0.4)} {f(h * 0.3)} C {f(w * 0.5)} {f(h * 0.36)} {f(w * 0.56)} {f(h * 0.48)} {f(w * 0.62)} {f(h * 0.6)} '
             f'L {f(w * 0.62)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>')
    cx, cy, rw = w * 0.26, h * 0.5, w * 0.17                       # the theatre: tiers in a half-bowl, the stage building before it
    o.append(f'<path d="M{f(cx - rw)} {f(cy)} A {f(rw)} {f(rw * 0.62)} 0 0 1 {f(cx + rw)} {f(cy)} Z" fill="#C8B898" stroke="{INK}" stroke-width="2"></path>')
    for k in range(1, 6):
        r_ = rw * (1 - k * 0.15)
        o.append(f'<path d="M{f(cx - r_)} {f(cy)} A {f(r_)} {f(r_ * 0.62)} 0 0 1 {f(cx + r_)} {f(cy)}" fill="none" stroke="#9A8A6A" stroke-width="2"></path>')
    o.append(f'<rect x="{f(cx - rw * 0.8)}" y="{f(cy)}" width="{f(rw * 1.6)}" height="{f(h * 0.05)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>')
    o.append(houses(w, h, h * 0.78, seed, x0=-10, x1=w * 0.62, hmin=0.07, hmax=0.12))
    o.append(houses(w, h, h * 0.92, seed + 1, x0=-10, x1=w * 0.66, hmin=0.08, hmax=0.14))
    return "".join(o)
