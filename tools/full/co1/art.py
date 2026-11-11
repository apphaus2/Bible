"""Drawings for the 1 Corinthians volume. Like Romans it starts from all of Acts' drawings (`from act.art16 import *`, which
carries act.art … act.art15, Mark's and Matthew's drawings) and from the epistle kit (epistle.py: the study, the sealed scroll,
the letter's road, the radiance, the technical plate), and adds its own (art2 … for the later chapters, each importing this).

The letter's people at a distance, on the kit silhouettes (epistle.robed): Paul only ever epistle.paul_fig; Sosthenes,
Stephanas, Fortunatus, Achaicus and Chloe's messenger in the looks of co1.common; Apollos, Aquila, Priscilla, Timothy and
Cephas in Acts' colours, redrawn on robed(). God is never drawn (light); Satan and demons are never drawn. Every function
takes (p, w, h, seed, ...) or (w, h, ...); p, a prefix unique to the panel, names the figure defs and gradients."""
import sys, pathlib, math, random, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from act.art16 import *
from act.art import f, INK
from act.art10 import philosopher, stoa, tentmakers, judgment_bema
from act.art11 import diana_temple, theatre
import epistle as EP
from epistle import (study, still_life, sealed_scroll, open_letter, reed_pen, inkpot, lamp_glow, letter_road, plate_bg, radiance, tag, dim, robed, paul_fig,
                     mat as floor_mat, SEPIA, SEAL)
from oba.minor import vista, halo, rays, starfield, bolt, rain
from genesis.art2 import fit, ground, hills, SKIN
from genesis.art3 import label, node, route
from genesis.art4 import clay_lamp
from jer.art import glow
from sa2.art import sky
from mat.art import temple, houses, pavement, room, UP_BLESS, UP_HIGH, UP_TOUCH, UP_CALL
from mat.art9 import steward
from jhn.art9 import dark_hill
from ecc.art import loaf
from num.art import ALL
from ntcast import ROBES
from co1.common import SOSTHENES_LOOK, STEPHANAS_LOOK, FORTUNATUS_LOOK, ACHAICUS_LOOK, CHLOE_LOOK
import mk, exodus as E

GOLD, CY = "#FFD23F", "#8FD0E2"

def plate_label(x, y, text, color=GOLD, size=10, anchor="middle", halo_="#0B1A2E"):
    """A label with a dark (or light) halo so it reads over a drawing."""
    return label(x, y, text, color, size, anchor).replace("<text ", f'<text stroke="{halo_}" stroke-width="3" paint-order="stroke" stroke-linejoin="round" ', 1)

# ---- the cast at a distance ---------------------------------------------------------------------------------------------
def sosthenes(p, x, y, s, flip=False, up=None, extra=""):
    L = SOSTHENES_LOOK
    return robed(p, x, y, s, L["cloth"], head=L["head"], cord=L["cord"], beard=L["beard"], belt="#1E242A", flip=flip, up=up, extra=extra)
def stephanas(p, x, y, s, flip=False, up=None, extra=""):
    L = STEPHANAS_LOOK
    return robed(p, x, y, s, L["cloth"], head=L["head"], cord=L["cord"], beard=L["beard"], mantle="#3A2E24", flip=flip, up=up, extra=extra)
def fortunatus(p, x, y, s, flip=False, up=None, extra=""):
    L = FORTUNATUS_LOOK
    return robed(p, x, y, s, L["cloth"], head=L["head"], cord=L["cord"], beard=L["beard"], belt="#0D1018", flip=flip, up=up, extra=extra)
def achaicus(p, x, y, s, flip=False, up=None, extra=""):
    L = ACHAICUS_LOOK
    return robed(p, x, y, s, L["cloth"], hair=L["hair"], belt="#3A2E4A", flip=flip, up=up, extra=extra)
def apollos_r(p, x, y, s, flip=False, up=None, extra=""):
    """Apollos as Acts draws him: dark-skinned, bareheaded, a black beard, a cream robe."""
    return robed(p, x, y, s, "#E8D8B0", skin="#A8704E", hair="#1A1210", beard="#1A1210", mantle="#B8A880", flip=flip, up=up, extra=extra)
def cephas_r(p, x, y, s, flip=False, up=None, extra=""):
    """Cephas (Peter) in ntcast's colours: bareheaded, dark-grey hair and beard, a brown robe."""
    return robed(p, x, y, s, ROBES["peter"], hair="#2A2420", beard="#4A4440", belt="#3A2A1A", flip=flip, up=up, extra=extra)
def timothy_r(p, x, y, s, flip=False, up=None, extra=""):
    return robed(p, x, y, s, "#7A8A9A", hair="#3A2214", belt="#4A5A6A", flip=flip, up=up, extra=extra)
def aquila_r(p, x, y, s, flip=False, up=None, extra=""):
    return robed(p, x, y, s, "#8A6A3A", head="#E0D4B0", cord="#6A4A2A", beard="#3A2214", flip=flip, up=up, extra=extra)
def priscilla_r(p, x, y, s, flip=False, up=None, extra=""):
    return robed(p, x, y, s * 0.94, "#5A6A8A", woman=True, veil="#3A6A8A", flip=flip, up=up, extra=extra)

# plain Corinthians: (cloth, head, beard, hair, woman, veil)
FOLK = [("#7A5A3A", "#3A4A5A", "#2A1A10", None, False, None), ("#5A6A8A", None, None, None, True, "#2A3A5A"),
        ("#6A7A4A", None, "#3A2A1A", "#2A1A10", False, None), ("#8A4A3A", "#E8E2D6", "#8A847A", None, False, None),
        ("#4A5A6A", None, None, None, True, "#E8E2D6"), ("#9A8A6A", None, None, "#3A2214", False, None),
        ("#6A4A5A", "#2A2A3A", "#1A1210", None, False, None), ("#7A6A5A", None, None, None, True, "#4A3A5A")]
def folk(p, x, y, s, i, flip=False, up=None):
    c, hd, bd, hr, wo, vl = FOLK[i % len(FOLK)]
    if wo: return robed(p, x, y, s * 0.94, c, woman=True, veil=vl, flip=flip, up=up)
    return robed(p, x, y, s, c, head=hd, beard=bd, hair=hr, flip=flip, up=up)

def philo(p, x, y, s, i=0, flip=False, up=None, extra=""):
    """A Greek philosopher on robed(): bareheaded, a white or grey beard, a pale robe and a coloured himation over the shoulder."""
    c = ["#E8E2D6", "#C8C0B0", "#D8D0E8", "#E0D8C0"][i % 4]
    bd = ["#E8E2D6", "#9A948A", "#C8C2B6", "#6A645E"][i % 4]
    return robed(p, x, y, s, c, skin="#E3B08A", hair=bd, beard=bd, mantle=["#8A7A6A", "#5A6A7A", "#7A6A8A", "#6A7A5A"][i % 4], flip=flip, up=up, extra=extra)

def steward_fig(p, x, y, s, flip=False, up=None, extra=""):
    """A steward of a household: a dark-blue headcloth, a black beard, a grey-blue robe, the keys at his girdle."""
    keys = '<path d="M14 -104 L 16 -84 M18 -104 L 22 -86" stroke="#C8963E" stroke-width="2.4"></path><circle cx="15" cy="-106" r="4" fill="none" stroke="#C8963E" stroke-width="2"></circle>'
    return robed(p, x, y, s, "#5A6A7A", head="#1F2F5A", cord="#0D1430", beard="#1A1210", belt="#2A1A10", flip=flip, up=up, extra=keys + extra)

WHO.update({"sosthenes": sosthenes, "stephanas": stephanas, "fortunatus": fortunatus, "achaicus": achaicus})

# ---- the study at Ephesus -------------------------------------------------------------------------------------------------
def _eph_window(x, y, ww, hh, night, seed):
    """A window on Ephesus: the theatre's half-bowl cut into the hill, and far off on the plain the temple of Diana."""
    sky_ = ("#0B0B2A", "#2A2050") if night else ("#8FD0E2", "#F3E8C8")
    uid = f"ew{seed}"
    o = [f'<defs><clipPath id="{uid}"><rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}"></rect></clipPath>'
         f'<linearGradient id="{uid}g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sky_[0]}"></stop><stop offset="1" stop-color="{sky_[1]}"></stop></linearGradient></defs>',
         f'<g clip-path="url(#{uid})"><rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}" fill="url(#{uid}g)"></rect>']
    if night: o.append(f'<g transform="translate({f(x)} {f(y)})">' + mk.stars(int(ww * hh / 900) + 6, ww, hh * 0.45, seed) + '</g>')
    hill, stone = ("#2A2440", "#5A5070") if night else ("#9A8A6A", "#E8DCC0")
    o.append(f'<path d="M{f(x - 4)} {f(y + hh * 0.5)} C {f(x + ww * 0.2)} {f(y + hh * 0.3)} {f(x + ww * 0.5)} {f(y + hh * 0.26)} {f(x + ww * 0.7)} {f(y + hh * 0.42)} '
             f'L {f(x + ww + 4)} {f(y + hh * 0.56)} L {f(x + ww + 4)} {f(y + hh + 4)} L {f(x - 4)} {f(y + hh + 4)} Z" fill="{hill}" stroke="{INK}" stroke-width="1.6"></path>')
    cx, cy, rw = x + ww * 0.36, y + hh * 0.66, ww * 0.26                     # the theatre: tiers in a half-bowl
    for k in range(4):
        r_ = rw * (1 - k * 0.2)
        o.append(f'<path d="M{f(cx - r_)} {f(cy)} A {f(r_)} {f(r_ * 0.55)} 0 0 1 {f(cx + r_)} {f(cy)}" fill="none" stroke="{stone}" stroke-width="{f(max(1.4, hh * 0.025))}"></path>')
    o.append(f'<rect x="{f(cx - rw * 0.6)}" y="{f(cy)}" width="{f(rw * 1.2)}" height="{f(hh * 0.06)}" fill="{stone}" stroke="{INK}" stroke-width="1"></rect>')
    o.append(diana_temple(x + ww * 0.8, y + hh * 0.86, ww * 0.3).replace("#F3EFE6", stone) if night else diana_temple(x + ww * 0.8, y + hh * 0.86, ww * 0.3))
    o.append('</g>' + f'<rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}" fill="none" stroke="{INK}" stroke-width="3"></rect>'
             f'<path d="M{f(x + ww / 2)} {f(y)} L {f(x + ww / 2)} {f(y + hh)}" stroke="#5A3A22" stroke-width="4"></path>'
             f'<rect x="{f(x - 8)}" y="{f(y + hh)}" width="{f(ww + 16)}" height="8" fill="#6A4A2A" stroke="{INK}" stroke-width="1.6"></rect>')
    return "".join(o)

def _beard_scribe(svg, cord, stage):
    """Give the seated scribe (Sosthenes) his short grey-black beard: drawn in his own units just after his headcloth's cord."""
    hx, hy = (6, -118) if stage == "write" else (2, -122)
    bd = SOSTHENES_LOOK["beard"]
    beard = (f'<path d="M{hx - 8} {hy + 1} C {hx - 9} {hy + 14} {hx} {hy + 22} {hx + 9} {hy + 19} C {hx + 14} {hy + 16} {hx + 15} {hy + 10} {hx + 13} {hy + 6} '
             f'C {hx + 8} {hy + 9} {hx + 2} {hy + 8} {hx - 3} {hy + 3} Z" fill="{bd}" stroke="{INK}" stroke-width="1.4"></path>')
    key = f'stroke="{cord}" stroke-width="2.6"></path>'
    i = svg.find(key)
    return svg if i < 0 else svg[:i + len(key)] + beard + svg[i + len(key):]

def study_co1(p, w, h, seed, stage="dictate", bearer=None, night=True, fig_h=None):
    """The letter written at Ephesus (epistle.study): Paul dictating, Sosthenes cross-legged on the mat writing (his beard
    added), the window on Ephesus; stage "read" Sosthenes reads it back; "give" Paul hands the sealed scroll to the bearer
    at the door. bearer: a look dict (cloth, head, beard)."""
    sc = dict(cloth=SOSTHENES_LOOK["cloth"], head=SOSTHENES_LOOK["head"], cord=SOSTHENES_LOOK["cord"])
    b = h * 0.95
    k = (fig_h or h * 0.72) / 205
    fig = bearer if callable(bearer) else None                  # a figure function (timothy_r, stephanas …) drawn here
    o = study(p, w, h, seed, stage=stage, scribe=sc, bearer=None if fig else bearer, night=night, window=False, fig_h=fig_h)
    if fig:
        if stage == "give":
            dx, dw = w * 0.68, min(w * 0.22, 120 * k)
            o += fig(p, dx + dw * 0.5, b, k, up=[(-22, -158), (-42, -146), (-62, -146)], extra=sealed_scroll(-70, -150, 0.3, rot=12))
        else: o += fig(p, w * 0.92, b, k, flip=True)
    if stage == "give":
        win = _eph_window(w * 0.06, b - 200 * k, min(w * 0.16, 110 * k), min(h * 0.36, 90 * k), night, seed)
        m = floor_mat(w * 0.06, b, 110 * k, k)
    else:
        win = _eph_window(w * 0.4, b - 210 * k, min(w * 0.17, 115 * k), min(h * 0.38, 95 * k), night, seed)
        m = floor_mat(w * 0.44, b, 120 * k, k)
    i = o.find(m)
    o = o[:i] + win + o[i:] if i >= 0 else o
    return _beard_scribe(o, sc["cord"], "write" if stage in ("dictate", "give") else "read")

def aegean_road(w, h):
    """The letter's road: from Ephesus across the Aegean to Cenchreæ and up to Corinth (16:8, 16:17)."""
    rt = ["EPHESUS", (26.6, 37.75), (25.4, 37.45), (24.3, 37.5), (23.4, 37.7), "CENCHREÆ", "CORINTH"]
    return letter_road(w, h, rt, title="1 CORINTHIANS 16:8 · FROM EPHESUS TO CORINTH", box=(21.4, 28.6, 36.6, 39.9),
                       places=("EPHESUS", "CENCHREÆ", "CORINTH", "ATHENS", "TROAS", "MILETUS"), hi=("EPHESUS", "CORINTH"),
                       regions=("ACHAIA", "ASIA", "MACEDONIA"))

def corinth_view(p, w, h, seed, paul_=False, tone="dusk"):
    """Corinth under the Acrocorinth: the great rock with the temple on its top, the city's roofs and colonnades below, the
    road coming in; paul_=True Paul small on the road, walking into the city (2:1)."""
    tops = {"dusk": ("#3A2A5A", "#E8905A"), "day": ("#8FD0E2", "#F3E8C8"), "night": ("#0B0B2A", "#2A2050")}[tone]
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, *tops)]
    if tone == "night": o.append(mk.stars(40, w, h * 0.4, seed))
    rock = "#5A4A5A" if tone != "day" else "#9A8A6A"
    o.append(f'<path d="M-10 {f(h * 0.74)} L {f(w * 0.18)} {f(h * 0.44)} L {f(w * 0.34)} {f(h * 0.2)} L {f(w * 0.46)} {f(h * 0.14)} L {f(w * 0.6)} {f(h * 0.22)} '
             f'L {f(w * 0.76)} {f(h * 0.4)} L {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="{rock}" stroke="{INK}" stroke-width="2.4"></path>')
    tx, ty, tw = w * 0.46, h * 0.14, max(30, w * 0.08)                     # the temple on the summit
    col = "#E8DCC0"
    o.append(f'<rect x="{f(tx - tw / 2)}" y="{f(ty - tw * 0.36)}" width="{f(tw)}" height="{f(tw * 0.08)}" fill="{col}" stroke="{INK}" stroke-width="1.2"></rect>'
             f'<path d="M{f(tx - tw / 2 - 2)} {f(ty - tw * 0.36)} L {f(tx)} {f(ty - tw * 0.56)} L {f(tx + tw / 2 + 2)} {f(ty - tw * 0.36)} Z" fill="{col}" stroke="{INK}" stroke-width="1.2"></path>'
             + "".join(f'<rect x="{f(tx - tw / 2 + tw * k / 5)}" y="{f(ty - tw * 0.28)}" width="{f(tw * 0.06)}" height="{f(tw * 0.28)}" fill="{col}" stroke="{INK}" stroke-width="0.8"></rect>' for k in range(6)))
    o.append(houses(w, h, h * 0.86, seed, hmin=0.12, hmax=0.2, lit=tone != "day"))
    o.append(f'<path d="M-10 {f(h * 0.86)} L {f(w + 10)} {f(h * 0.86)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#8A7A5A" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<path d="M{f(w * 0.06)} {f(h + 10)} C {f(w * 0.2)} {f(h * 0.94)} {f(w * 0.4)} {f(h * 0.9)} {f(w * 0.56)} {f(h * 0.87)}" stroke="#C8B080" stroke-width="{f(max(10, h * 0.05))}" fill="none"></path>')
    if paul_:
        b = h * 0.97
        o.append(paul_fig(p, w * 0.2, b, fit(b, b - max(60, h * 0.34)), flip=True))
    return "".join(o)

# ---- 1 Corinthians 1 ---------------------------------------------------------------------------------------------------
def factions(p, w, h):
    """I am of Paul; and I of Apollos; and I of Cephas; and I of Christ: one panel split four ways by a crack, in each part a
    knot of Corinthians turned toward their own name — Paul, Apollos, Cephas — and the fourth toward a light with no
    figure in it (1:12–13, Is Christ divided?)."""
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp")]
    cols = [("#5A3A2A", "#C8803A", "PAUL"), ("#2A3A5A", "#7AA0C8", "APOLLOS"), ("#3A4A2A", "#9AB06A", "CEPHAS"), ("#3A2A4A", "#FFE6A0", "CHRIST")]
    n = len(cols); cw = w / n
    b = h * 0.95
    s = fit(b, b - min(h * 0.62, 160)); s2 = s * 0.78
    figs = [paul_fig, apollos_r, cephas_r, None]
    r = random.Random(112)
    for i, (dark, light, name) in enumerate(cols):
        x0 = i * cw; uid = f"{p}fc{i}"
        o.append(f'<defs><linearGradient id="{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{light}"></stop><stop offset="1" stop-color="{dark}"></stop></linearGradient></defs>'
                 f'<rect x="{f(x0)}" y="-10" width="{f(cw + 1)}" height="{f(h + 20)}" fill="url(#{uid})"></rect>'
                 f'<rect x="{f(x0)}" y="{f(b - 4)}" width="{f(cw + 1)}" height="{f(h)}" fill="{dark}" stroke="{INK}" stroke-width="1.6"></rect>')
        cx = x0 + cw * 0.62
        if figs[i]: o.append(figs[i](p, cx, b - 4, s, flip=True, up=UP_BLESS if i == 0 else None))
        else: o.append(halo(cx, b - 110 * s, 110 * s, "#FFFFFF", 0.85) + rays(cx, b - 110 * s, 16, 30 * s, 120 * s, "#FFF4C2", 0.45, 3))
        for j in range(2):                                     # their followers, nearer and smaller, turned toward the name
            o.append(folk(p, x0 + cw * (0.14 + 0.2 * j), b + 2, s2, i * 2 + j, up=UP_HIGH if j == 0 else None, flip=True))
        o.append(plate_label(x0 + cw / 2, 22, name, "#FFF8E6", 13, halo_="#0D0D0F"))
    pts = [(cw * k + r.uniform(-8, 8), y) for k in range(1, n) for y in (0,)]
    for k in range(1, n):                                       # the cracks between them
        x = cw * k; d = f"M{f(x)} -4"; y = 0
        while y < h:
            y += h / 7; d += f" L {f(x + r.uniform(-9, 9))} {f(y)}"
        o.append(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="5"></path><path d="{d}" fill="none" stroke="#D7261E" stroke-width="2"></path>')
    return "".join(o)

def chloe_word(p, w, h, seed):
    """It hath been signified unto me … by them that are of the household of Chloe: the study at Ephesus, Sosthenes reading
    the roll back, Paul listening, and Chloe's messenger standing at the right, come with the news."""
    return study_co1(p, w, h, seed, stage="read", bearer=CHLOE_LOOK)

def cross_far(p, w, h, seed):
    """The word of the cross: the hill of the three crosses far off under a darkened sky (John's drawing): nothing nearer."""
    return dark_hill(p, w, h, seed)

def signs_wisdom(p, w, h, seed):
    """Jews ask for signs, and Greeks seek after wisdom: at the left a Jew in a white headcloth, his arm lifted to a stormy
    sky; at the right a Greek philosopher with an open scroll before a colonnade; between them, far off on a hill against a
    red dusk, three small crosses (1:22–24)."""
    b = h * 0.94
    o = [mk.defs(p, *ALL, "ManUp"), f'<defs><linearGradient id="{p}sw" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#2A2A4A"></stop>'
         f'<stop offset="0.5" stop-color="#C8502A"></stop><stop offset="1" stop-color="#E8D8B0"></stop></linearGradient></defs>',
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{p}sw)"></rect>',
         bolt(w * 0.14, 0, h * 0.4, seed, color="#C8C8E8", sw=3)]
    o.append(f'<path d="M{f(w * 0.3)} {f(h * 0.7)} C {f(w * 0.42)} {f(h * 0.46)} {f(w * 0.58)} {f(h * 0.46)} {f(w * 0.7)} {f(h * 0.7)} Z" fill="#3A2028" stroke="{INK}" stroke-width="2"></path>')
    o.append(halo(w * 0.5, h * 0.5, h * 0.3, "#1A0A10", 0.5))
    for k, dx in enumerate((-0.035, 0, 0.035)):                # three small crosses on the hill, far off
        cx, top = w * (0.5 + dx), h * (0.4 if k == 1 else 0.42)
        bot = h * 0.5
        o.append(f'<path d="M{f(cx)} {f(bot)} L {f(cx)} {f(top)} M{f(cx - h * 0.025)} {f(top + h * 0.025)} L {f(cx + h * 0.025)} {f(top + h * 0.025)}" stroke="#0D0D0F" stroke-width="{f(max(2, h * 0.009))}"></path>')
    o.append(ground(w, h, h * 0.7, "#5A4838", dy=-4))
    for k in range(4):                                         # the colonnade behind the Greek
        x = w * (0.74 + k * 0.07)
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.2)}" width="{f(w * 0.026)}" height="{f(h * 0.5)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<rect x="{f(w * 0.72)}" y="{f(h * 0.15)}" width="{f(w * 0.3)}" height="{f(h * 0.05)}" fill="#E8DCC0" stroke="{INK}" stroke-width="1.8"></rect>')
    s = fit(b, b - min(h * 0.7, 190))
    o.append(robed(p, w * 0.16, b, s, "#E8E2D6", head="#F3EFE6", cord="#1F3A7A", beard="#3A2A1A", mantle="#3A4A7A", up=[(-22, -158), (-14, -196), (-6, -232)], flip=True))
    o.append(philo(p, w * 0.84, b, s, 1, flip=True))
    o.append(open_letter(w * 0.84 - 64 * s, b - 150 * s, 40 * s, 30 * s, rows=4, seed=seed))
    o.append(plate_label(w * 0.16, h * 0.08, "JEWS · SIGNS", "#FFF8E6", 11, halo_="#0D0D0F") + plate_label(w * 0.84, h * 0.08, "GREEKS · WISDOM", "#12113A", 11, halo_="#F3EFE6"))
    return "".join(o)

def wise_disputer(p, w, h, seed):
    """Where is the wise? where is the scribe? where is the disputer of this world? The colonnade of the philosophers (Acts'
    stoa at Athens redrawn), the disputers in their himations, one with an open scroll, one lifting his hand to argue."""
    b = h * 0.93
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#8FD0E2", "#F3E8C8"),
         f'<rect x="-10" y="{f(h * 0.06)}" width="{f(w + 20)}" height="{f(h * 0.07)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>',
         f'<rect x="-10" y="{f(h * 0.13)}" width="{f(w + 20)}" height="{f(h * 0.03)}" fill="#C8B898" stroke="{INK}" stroke-width="1.6"></rect>']
    n = 9
    for k in range(n):
        x = w * (0.03 + k / (n - 1) * 0.94)
        o.append(f'<rect x="{f(x - w * 0.016)}" y="{f(h * 0.16)}" width="{f(w * 0.032)}" height="{f(b - h * 0.2)}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.6"></rect>'
                 f'<rect x="{f(x - w * 0.024)}" y="{f(b - h * 0.05)}" width="{f(w * 0.048)}" height="{f(h * 0.05)}" fill="#D8CCB0" stroke="{INK}" stroke-width="1.4"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.16)}" width="{f(w + 20)}" height="{f(b - h * 0.16)}" fill="#3A3028" opacity="0.18"></rect>')
    o.append(pavement(w, h, b, color="#D8D0C0"))
    s = fit(b, b - min(h * 0.74, 200))
    o.append(philo(p, w * 0.12, b, s, 0, flip=True) + philo(p, w * 0.26, b, s * 0.98, 1, up=[(-22, -158), (-40, -176), (-50, -200)]))
    o.append(philo(p, w * 0.44, b, s, 2, flip=True, up=[(-22, -158), (-44, -150), (-60, -150)], extra=sealed_scroll(-66, -150, 0.22, rot=80)))
    o.append(philo(p, w * 0.6, b, s * 0.97, 3) + philo(p, w * 0.76, b, s, 1, flip=True, up=[(-22, -158), (-42, -170), (-62, -176)]) + philo(p, w * 0.9, b, s * 0.98, 0))
    return "".join(o)

def plain_folk(p, w, h, seed):
    """Not many wise, not many mighty, not many noble: the church at Corinth — a porter, a slave girl, a potter with his
    clay-stained apron, an old man, a woman of the household — standing together by lamplight in a plain room."""
    b = h * 0.93
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#6A4A3A", floor="#3A2A20"),
         lamp_glow(w * 0.5, h * 0.3, max(w, h) * 0.5, f"{p}lg", op=0.5), clay_lamp(w * 0.5, h * 0.3, max(0.6, h / 300))]
    s = fit(b, b - min(h * 0.74, 200))
    xs = [0.1, 0.24, 0.38, 0.62, 0.76, 0.9]
    for i, x in enumerate(xs):
        o.append(folk(p, w * x, b, s * (0.97 + 0.03 * (i % 2)), [5, 1, 2, 3, 4, 6][i], flip=x > 0.5))
    o.append(f'<rect x="{f(w * 0.1 - 20 * s)}" y="{f(b - 196 * s)}" width="{f(40 * s)}" height="{f(22 * s)}" rx="{f(6 * s)}" fill="#C8A878" stroke="{INK}" stroke-width="1.6"></rect>')  # the porter's sack
    return "".join(o)

# ---- 1 Corinthians 2 ---------------------------------------------------------------------------------------------------
def rulers_seat(p, w, h, seed):
    """The rulers of this world, who are coming to nought: the judgment-seat in the forum, empty (Acts' bema at Corinth)."""
    return judgment_bema(p, w, h, seed, gallio_=False, accusers=False, paul_=False)

def prepared(w, h, seed):
    """Things which eye saw not, and ear heard not: a dark land at night, and above it a bank of cloud with a great light
    behind it, its edges burning gold, rays breaking through — what lies beyond not shown."""
    o = [sky(w, h, "#0B0B2A", "#2A2050"), starfield(w, h, seed, int(w * h / 6000) + 20, 0.5),
         halo(w * 0.55, h * 0.3, max(w, h) * 0.45, "#FFE680", 0.6), rays(w * 0.55, h * 0.3, 28, h * 0.15, max(w, h), "#FFF4C2", 0.32, 4)]
    r = random.Random(seed)
    for k in range(9):                                         # the cloud bank, lit from behind
        cx, cy, rx = w * (0.1 + 0.1 * k + r.uniform(-0.03, 0.03)), h * (0.34 + r.uniform(-0.05, 0.05)), w * r.uniform(0.08, 0.12)
        o.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(rx * 0.5)}" fill="#2A2050" stroke="#FFD23F" stroke-width="2.4"></ellipse>')
    o.append(f'<rect x="-10" y="{f(h * 0.36)}" width="{f(w + 20)}" height="{f(h * 0.06)}" fill="#2A2050"></rect>')
    o.append(hills(w, h, h * 0.66, seed, color="#141028", amp=18, step=80) + ground(w, h, h * 0.84, "#0B0818", dy=0))
    return "".join(o)

def deep_light(w, h, seed):
    """The Spirit searcheth all things, yea, the deep things of God: a shaft of light going down from the surface into the
    dark depths of the sea, the rocks of the floor lit far below."""
    sy = h * 0.16
    o = [sky(w, h, "#2A4A7A", "#8FD0E2"), f'<defs><linearGradient id="dl{seed}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1F6F9A"></stop>'
         f'<stop offset="0.5" stop-color="#0F2E4A"></stop><stop offset="1" stop-color="#030812"></stop></linearGradient>'
         f'<linearGradient id="dlb{seed}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF4C2" stop-opacity="0.85"></stop><stop offset="1" stop-color="#FFF4C2" stop-opacity="0.1"></stop></linearGradient></defs>',
         f'<rect x="-10" y="{f(sy)}" width="{f(w + 20)}" height="{f(h)}" fill="url(#dl{seed})" stroke="{INK}" stroke-width="2"></rect>',
         f'<path d="M{f(w * 0.46)} -10 L {f(w * 0.54)} -10 L {f(w * 0.72)} {f(h * 0.94)} L {f(w * 0.3)} {f(h * 0.94)} Z" fill="url(#dlb{seed})"></path>']
    r = random.Random(seed)
    for k in range(14):
        x = w * r.uniform(0, 1)
        o.append(f'<path d="M{f(x)} {f(sy + 4)} q {f(10)} -5 {f(20)} 0" fill="none" stroke="#CFEFFF" stroke-width="1.6" opacity="0.7"></path>')
    for k in range(7):
        x = w * (k / 6); hh = h * r.uniform(0.04, 0.12)
        lit = 0.3 < k / 6 < 0.72
        o.append(f'<path d="M{f(x - w * 0.1)} {f(h + 10)} L {f(x - w * 0.04)} {f(h * 0.94 - hh)} L {f(x + w * 0.05)} {f(h * 0.95 - hh * 0.7)} L {f(x + w * 0.1)} {f(h + 10)} Z" '
                 f'fill="{"#8A7A5A" if lit else "#0B1420"}" stroke="{INK}" stroke-width="1.6"></path>')
    o.append(halo(w * 0.51, h * 0.92, h * 0.2, "#FFF4C2", 0.6))
    return "".join(o)

# ---- 1 Corinthians 3 ---------------------------------------------------------------------------------------------------
def milk_meat(w, h, seed):
    """I fed you with milk, not with meat: on a low table by lamplight, a small jug and a cup of milk at the left, and at
    the right, set aside, a platter of meat and bread."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2418"></rect>', lamp_glow(w * 0.5, h * 0.3, max(w, h) * 0.6, f"mm{seed}", op=0.5)]
    ty = h * 0.6
    o.append(f'<path d="M-10 {f(ty)} L {f(w + 10)} {f(ty)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#6A3A1E" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M-10 {f(ty + 8)} L {f(w + 10)} {f(ty + 8)}" stroke="#8A5A30" stroke-width="2"></path>')
    k = min(w / 520, h / 240)
    jx, cx = w * 0.22, w * 0.34                                # the jug and the cup of milk
    o.append(f'<path d="M{f(jx - 22 * k)} {f(ty + 10 * k)} C {f(jx - 34 * k)} {f(ty - 30 * k)} {f(jx - 18 * k)} {f(ty - 62 * k)} {f(jx - 10 * k)} {f(ty - 76 * k)} L {f(jx + 10 * k)} {f(ty - 76 * k)} '
             f'C {f(jx + 18 * k)} {f(ty - 62 * k)} {f(jx + 34 * k)} {f(ty - 30 * k)} {f(jx + 22 * k)} {f(ty + 10 * k)} Z" fill="#B8784A" stroke="{INK}" stroke-width="2.2"></path>'
             f'<path d="M{f(jx + 12 * k)} {f(ty - 66 * k)} C {f(jx + 30 * k)} {f(ty - 66 * k)} {f(jx + 30 * k)} {f(ty - 40 * k)} {f(jx + 20 * k)} {f(ty - 36 * k)}" fill="none" stroke="{INK}" stroke-width="{f(4 * k)}"></path>'
             f'<path d="M{f(cx - 16 * k)} {f(ty - 30 * k)} L {f(cx + 16 * k)} {f(ty - 30 * k)} L {f(cx + 12 * k)} {f(ty + 8 * k)} L {f(cx - 12 * k)} {f(ty + 8 * k)} Z" fill="#C8905A" stroke="{INK}" stroke-width="2"></path>'
             f'<ellipse cx="{f(cx)}" cy="{f(ty - 30 * k)}" rx="{f(16 * k)}" ry="{f(4 * k)}" fill="#FFFDF4" stroke="{INK}" stroke-width="1.6"></ellipse>')
    px = w * 0.7                                              # the platter of meat, set aside
    o.append(f'<ellipse cx="{f(px)}" cy="{f(ty + 8 * k)}" rx="{f(80 * k)}" ry="{f(16 * k)}" fill="#C8B488" stroke="{INK}" stroke-width="2.2"></ellipse>'
             f'<path d="M{f(px - 44 * k)} {f(ty + 4 * k)} C {f(px - 40 * k)} {f(ty - 26 * k)} {f(px + 10 * k)} {f(ty - 34 * k)} {f(px + 30 * k)} {f(ty - 4 * k)} Z" fill="#8A3A22" stroke="{INK}" stroke-width="2"></path>'
             f'<path d="M{f(px - 30 * k)} {f(ty - 12 * k)} C {f(px - 16 * k)} {f(ty - 20 * k)} {f(px)} {f(ty - 20 * k)} {f(px + 14 * k)} {f(ty - 10 * k)}" fill="none" stroke="#C8705A" stroke-width="{f(2 * k)}"></path>'
             + loaf(px + 50 * k, ty, k * 1.2) + loaf(px + 36 * k, ty + 10 * k, k))
    o.append(clay_lamp(w * 0.5, ty - 2, k * 1.1))
    return "".join(o)

def husbandry(p, w, h, seed):
    """I planted, Apollos watered; but God gave the increase: a field at morning — Paul stooping to set a young plant in the
    furrow, Apollos pouring water from a jar, and between them the plant grown up green and tall in a shaft of light from
    above (no figure in the light)."""
    b = h * 0.93
    o = [mk.defs(p, *ALL, "ManUp"), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.52, seed, color="#9AB06A", amp=12, step=90),
         ground(w, h, h * 0.62, "#8A6A3A", dy=-4)]
    for k in range(6):                                         # the furrows
        y = h * (0.66 + k * 0.055)
        o.append(f'<path d="M-10 {f(y)} C {f(w * 0.3)} {f(y - 4)} {f(w * 0.7)} {f(y + 4)} {f(w + 10)} {f(y)}" stroke="#6A4A22" stroke-width="2" fill="none"></path>')
    px = w * 0.5
    o.append(f'<path d="M{f(px - 40)} -10 L {f(px + 40)} -10 L {f(px + 70)} {f(b)} L {f(px - 70)} {f(b)} Z" fill="#FFF4C2" opacity="0.45"></path>' + halo(px, h * 0.04, h * 0.3, "#FFFFFF", 0.7))
    sh = min(h * 0.62, 170)                                    # the plant grown up
    o.append(f'<path d="M{f(px)} {f(b)} C {f(px - 4)} {f(b - sh * 0.4)} {f(px + 4)} {f(b - sh * 0.7)} {f(px)} {f(b - sh)}" stroke="#2E6B3A" stroke-width="5" fill="none"></path>')
    for k in range(7):
        y = b - sh * (0.2 + 0.11 * k); side = 1 if k % 2 else -1; L = sh * (0.22 - 0.015 * k)
        o.append(f'<path d="M{f(px)} {f(y)} C {f(px + side * L * 0.4)} {f(y - L * 0.5)} {f(px + side * L)} {f(y - L * 0.4)} {f(px + side * L * 1.1)} {f(y - L * 0.2)} '
                 f'C {f(px + side * L * 0.7)} {f(y + L * 0.05)} {f(px + side * L * 0.3)} {f(y + L * 0.02)} {f(px)} {f(y)} Z" fill="#9CCB5E" stroke="{INK}" stroke-width="1.4"></path>')
    s = fit(b, b - min(h * 0.72, 190))
    o.append(paul_fig(p, w * 0.22, b, s, flip=True, up=[(-22, -158), (-40, -124), (-58, -98)]))
    o.append(f'<path d="M{f(w * 0.22 + 58 * s)} {f(b - 98 * s)} l {f(4 * s)} {f(30 * s)}" stroke="#2E6B3A" stroke-width="{f(3 * s)}"></path>')
    jar = ('<path d="M-82 -150 C -92 -150 -96 -130 -90 -116 C -84 -104 -64 -104 -58 -116 C -52 -130 -56 -150 -66 -150 Z" fill="#B8784A" stroke="#0D0D0F" stroke-width="2"></path>'
           '<path d="M-90 -122 C -100 -114 -104 -100 -102 -84" stroke="#8FD0E2" stroke-width="5" fill="none" stroke-linecap="round"></path>')
    o.append(apollos_r(p, w * 0.8, b, s, up=[(-22, -158), (-46, -150), (-66, -140)], extra=jar))
    o.append(plate_label(w * 0.22, h * 0.08, "PAUL", "#12113A", 11, halo_="#F3EFE6") + plate_label(w * 0.8, h * 0.08, "APOLLOS", "#12113A", 11, halo_="#F3EFE6"))
    return "".join(o)

MATERIALS = [("GOLD", "#E8B830", "#FFE680"), ("SILVER", "#C8CCD4", "#F3F6FA"), ("COSTLY STONES", "#5A6A8A", "#8FD0E2"),
             ("WOOD", "#8A5A30", "#B8844A"), ("HAY", "#C8A84A", "#E8D080"), ("STUBBLE", "#A8904A", "#C8B070")]

def _material(i, x, y, bw, bh, burnt=False):
    """One block of building stuff on the foundation; burnt=True: wood, hay and stubble gone to ash and embers."""
    name, c, hi = MATERIALS[i]
    if burnt and i >= 3:
        return (f'<path d="M{f(x)} {f(y)} C {f(x + bw * 0.2)} {f(y - bh * 0.24)} {f(x + bw * 0.7)} {f(y - bh * 0.3)} {f(x + bw)} {f(y)} Z" fill="#3A3434" stroke="{INK}" stroke-width="1.6"></path>'
                + "".join(f'<circle cx="{f(x + bw * (0.25 + 0.2 * k))}" cy="{f(y - bh * 0.1)}" r="{f(max(1.6, bw * 0.03))}" fill="#FF6A2A"></circle>' for k in range(3)))
    o = []
    if i <= 1:                                                 # gold and silver: stacked ingots
        for r_ in range(3):
            for k in range(3 - r_):
                xx = x + bw * (0.06 + 0.31 * k + 0.155 * r_); yy = y - bh * 0.3 * (r_ + 1)
                o.append(f'<path d="M{f(xx)} {f(yy + bh * 0.3)} L {f(xx + bw * 0.04)} {f(yy)} L {f(xx + bw * 0.24)} {f(yy)} L {f(xx + bw * 0.28)} {f(yy + bh * 0.3)} Z" fill="{c}" stroke="{INK}" stroke-width="1.4"></path>'
                         f'<path d="M{f(xx + bw * 0.07)} {f(yy + bh * 0.08)} l {f(bw * 0.12)} 0" stroke="{hi}" stroke-width="2"></path>')
    elif i == 2:                                               # costly stones: cut blocks with gems set in them
        o.append(f'<rect x="{f(x)}" y="{f(y - bh * 0.9)}" width="{f(bw)}" height="{f(bh * 0.9)}" fill="#8A8AA0" stroke="{INK}" stroke-width="1.8"></rect>'
                 f'<path d="M{f(x)} {f(y - bh * 0.45)} L {f(x + bw)} {f(y - bh * 0.45)} M{f(x + bw * 0.5)} {f(y - bh * 0.9)} L {f(x + bw * 0.5)} {f(y - bh * 0.45)}" stroke="{INK}" stroke-width="1.2"></path>')
        for k, gc in enumerate(("#D7261E", "#1F8A5A", "#3A6AD7", "#E8B830")):
            gx, gy = x + bw * (0.25 + 0.5 * (k % 2)), y - bh * (0.68 if k < 2 else 0.22)
            o.append(f'<path d="M{f(gx)} {f(gy - bh * 0.1)} L {f(gx + bw * 0.08)} {f(gy)} L {f(gx)} {f(gy + bh * 0.1)} L {f(gx - bw * 0.08)} {f(gy)} Z" fill="{gc}" stroke="{INK}" stroke-width="1.2"></path>')
    elif i == 3:                                               # wood: squared beams
        for k in range(3):
            o.append(f'<rect x="{f(x)}" y="{f(y - bh * 0.3 * (k + 1))}" width="{f(bw)}" height="{f(bh * 0.28)}" fill="{c}" stroke="{INK}" stroke-width="1.4"></rect>'
                     f'<path d="M{f(x + bw * 0.1)} {f(y - bh * (0.3 * k + 0.15))} C {f(x + bw * 0.4)} {f(y - bh * (0.3 * k + 0.2))} {f(x + bw * 0.6)} {f(y - bh * (0.3 * k + 0.1))} {f(x + bw * 0.9)} {f(y - bh * (0.3 * k + 0.15))}" stroke="#5A3A1A" stroke-width="1" fill="none"></path>')
    else:                                                      # hay and stubble: a heap of stalks
        o.append(f'<path d="M{f(x)} {f(y)} C {f(x + bw * 0.1)} {f(y - bh * 0.9)} {f(x + bw * 0.9)} {f(y - bh * 0.9)} {f(x + bw)} {f(y)} Z" fill="{c}" stroke="{INK}" stroke-width="1.6"></path>')
        r = random.Random(i)
        for k in range(12):
            sx_ = x + bw * r.uniform(0.15, 0.85)
            o.append(f'<path d="M{f(sx_)} {f(y - 2)} l {f(r.uniform(-8, 8))} {f(-bh * r.uniform(0.3, 0.75 if i == 4 else 0.5))}" stroke="{hi}" stroke-width="1.4"></path>')
    return "".join(o)

def foundation_plate(w, h, fire=False):
    """Other foundation can no man lay than that which is laid, which is Jesus Christ: a technical plate — the foundation
    laid in squared stone across the foot of the plate, and on it six blocks of building stuff: gold, silver, costly stones,
    wood, hay, stubble (3:10–12). fire=True: the day revealed in fire — flames along the whole work; the gold, the silver and
    the stones standing in the fire shining, the wood, the hay and the stubble burned to ash (3:13–15)."""
    o = [plate_bg(w, h, "1 CORINTHIANS 3:13 · THE FIRE SHALL PROVE EACH MAN'S WORK" if fire else "1 CORINTHIANS 3:10–12 · A WISE MASTERBUILDER")]
    fy = h * 0.82; fh = h * 0.1
    o.append(f'<rect x="{f(w * 0.04)}" y="{f(fy)}" width="{f(w * 0.92)}" height="{f(fh)}" fill="#6A6A7A" stroke="{CY}" stroke-width="1.8"></rect>')
    for k in range(1, 12):
        o.append(f'<path d="M{f(w * (0.04 + 0.92 * k / 12))} {f(fy)} l 0 {f(fh)}" stroke="#2A2A3A" stroke-width="1.4"></path>')
    o.append(plate_label(w * 0.5, fy + fh * 0.7, "THE FOUNDATION · JESUS CHRIST", GOLD, 10))
    n = 6; gap = w * 0.02; bw = (w * 0.88 - gap * (n - 1)) / n; bh = min(h * (0.36 if fire else 0.44), bw * 0.9)
    if fire:
        o.append(halo(w * 0.5, fy, h * 0.6, "#FF8A3D", 0.4))
    for i in range(n):
        x = w * 0.06 + i * (bw + gap)
        if fire: o.append(E.blaze(x + bw / 2, fy, bw * 1.0, bh * (1.5 if i >= 3 else 1.15), 300 + i, n=6))
        o.append(_material(i, x, fy, bw, bh, burnt=fire))
        if fire and i < 3: o.append(halo(x + bw / 2, fy - bh * 0.4, bw * 0.6, "#FFF4C2", 0.5))
        if not fire: o.append(plate_label(x + bw / 2, fy - bh - 8, MATERIALS[i][0], CY, 9.5))
    if fire:
        o.append(plate_label(w * 0.06 + 1.5 * (bw + gap) - gap / 2, fy + fh + 16 if fy + fh + 16 < h - 4 else h * 0.2, "GOLD · SILVER · COSTLY STONES — SHALL ABIDE", "#FFF4C2", 9.5)
                 + plate_label(w * 0.06 + 4.5 * (bw + gap) - gap / 2, fy + fh + 16 if fy + fh + 16 < h - 4 else h * 0.2, "WOOD · HAY · STUBBLE — BURNED", "#FF8A6A", 9.5))
    return "".join(o)

def temple_of_god(p, w, h, seed):
    """Know ye not that ye are a temple of God: the white-and-gold sanctuary across its court, light falling on it from
    above, no one drawn."""
    b = h * 0.92
    o = [sky(w, h, "#5A7AB0", "#F3E8C8"), halo(w * 0.5, h * 0.1, max(w, h) * 0.5, "#FFF4C2", 0.6),
         rays(w * 0.5, -h * 0.1, 20, h * 0.2, max(w, h) * 1.2, "#FFF4C2", 0.25, 5), hills(w, h, h * 0.66, seed, color="#9A8A6A", amp=10, step=90)]
    u = min(w * 0.94 / 220, h * 0.74 / 79)
    o.append(temple(w * 0.5, b, 100 * u, lit=True))
    o.append(pavement(w, h, b, color="#E8DCC0"))
    return "".join(o)

# ---- 1 Corinthians 4 ---------------------------------------------------------------------------------------------------
def stewards(p, w, h, seed):
    """Stewards of the mysteries of God … it is required in stewards, that a man be found faithful (Matthew's faithful
    steward of the house): the storehouse door open, its jars and sacks within; the steward with the keys at his girdle
    handing out a loaf to each of the household, who wait in a line."""
    b = h * 0.93
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), sky(w, h, "#8FD0E2", "#F3E8C8"),
         f'<rect x="-10" y="{f(h * 0.1)}" width="{f(w * 0.44)}" height="{f(b - h * 0.1)}" fill="#E0CFA8" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="-10" y="{f(h * 0.06)}" width="{f(w * 0.46)}" height="{f(h * 0.05)}" fill="#B8A07A" stroke="{INK}" stroke-width="2"></rect>']
    dx, dw = w * 0.08, w * 0.2
    o.append(f'<rect x="{f(dx)}" y="{f(h * 0.24)}" width="{f(dw)}" height="{f(b - h * 0.24)}" fill="#2A1E14" stroke="{INK}" stroke-width="2.4"></rect>')
    r = random.Random(seed)
    for k in range(4):                                         # jars and sacks inside the store
        x = dx + dw * (0.15 + 0.23 * k); hh = h * r.uniform(0.16, 0.24)
        o.append(f'<path d="M{f(x - hh * 0.2)} {f(b)} C {f(x - hh * 0.36)} {f(b - hh * 0.6)} {f(x - hh * 0.16)} {f(b - hh)} {f(x)} {f(b - hh)} C {f(x + hh * 0.16)} {f(b - hh)} {f(x + hh * 0.36)} {f(b - hh * 0.6)} {f(x + hh * 0.2)} {f(b)} Z" '
                 f'fill="{["#A8683A", "#C8B080", "#8A5A30", "#C8B080"][k]}" stroke="{INK}" stroke-width="1.6"></path>')
    o.append(ground(w, h, b, "#C8B080", dy=0))
    s = fit(b, b - min(h * 0.74, 200))
    o.append(steward_fig(p, w * 0.38, b, s, flip=True, up=[(-22, -158), (-46, -146), (-70, -144)], extra='<ellipse cx="-74" cy="-146" rx="12" ry="6" fill="#D9A25A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'))
    for i, x in enumerate((0.54, 0.66, 0.78, 0.9)):
        o.append(folk(p, w * x, b, s * (0.96 if i % 2 else 1.0), [0, 1, 5, 4][i], up=[(-22, -158), (-42, -140), (-58, -136)] if i == 0 else None))
    o.append(loaf(w * 0.31, b - 12, s * 1.1) + loaf(w * 0.29, b - 4, s))
    return "".join(o)

def hidden_things(w, h, seed):
    """Until the Lord come, who will both bring to light the hidden things of darkness: a dark storeroom, its door flung
    open and the morning streaming in across the floor, the jars and the corners lit (no one drawn)."""
    b = h * 0.8
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#141018"></rect>',
         f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#1E1810" stroke="{INK}" stroke-width="2"></rect>']
    dx, dw, dt = w * 0.1, w * 0.14, h * 0.08
    o.append(lamp_glow(w * 0.4, b - h * 0.2, h * 0.9, f"ht{seed}", color="#FFE6A0", op=0.3)
             + f'<path d="M{f(dx)} {f(b)} L {f(dx + dw)} {f(b)} L {f(w * 0.92)} {f(h + 10)} L {f(w * 0.3)} {f(h + 10)} Z" fill="#FFE6A0" opacity="0.5"></path>'
             f'<rect x="{f(dx)}" y="{f(dt)}" width="{f(dw)}" height="{f(b - dt)}" fill="#FFF4C2" stroke="{INK}" stroke-width="3"></rect>'
             f'<path d="M{f(dx)} {f(dt)} L {f(dx - dw * 0.5)} {f(dt - h * 0.04)} L {f(dx - dw * 0.5)} {f(b + h * 0.06)} L {f(dx)} {f(b)} Z" fill="#5A3A22" stroke="{INK}" stroke-width="2.4"></path>')
    r = random.Random(seed)
    for k in range(6):                                         # jars, lit where the light falls
        x = w * (0.4 + 0.1 * k); hh = h * r.uniform(0.2, 0.3); lit = k < 4
        o.append(f'<path d="M{f(x - hh * 0.22)} {f(b)} C {f(x - hh * 0.4)} {f(b - hh * 0.6)} {f(x - hh * 0.2)} {f(b - hh * 0.9)} {f(x - hh * 0.1)} {f(b - hh)} L {f(x + hh * 0.1)} {f(b - hh)} '
                 f'C {f(x + hh * 0.2)} {f(b - hh * 0.9)} {f(x + hh * 0.4)} {f(b - hh * 0.6)} {f(x + hh * 0.22)} {f(b)} Z" fill="{"#C8784A" if lit else "#3A2418"}" stroke="{INK}" stroke-width="1.8"></path>')
    return "".join(o)

def arena(p, w, h, seed):
    """A spectacle unto the world: the arena of a city, its tiers of seats rising all round, the crowds a dark mass of heads
    in the stands, the sand of the floor empty in the hot light, the gate below standing open — no one on the sand."""
    o = [sky(w, h, "#E8905A", "#F3D8A0")]
    cy = h * 0.82; rx = w * 0.62
    for k in range(6):                                         # the tiers, far side
        y0 = h * (0.0 + k * 0.09)
        o.append(f'<path d="M-10 {f(y0 + h * 0.1)} C {f(w * 0.2)} {f(y0)} {f(w * 0.8)} {f(y0)} {f(w + 10)} {f(y0 + h * 0.1)} L {f(w + 10)} {f(y0 + h * 0.18)} '
                 f'C {f(w * 0.8)} {f(y0 + h * 0.08)} {f(w * 0.2)} {f(y0 + h * 0.08)} -10 {f(y0 + h * 0.18)} Z" fill="{["#C8B08A", "#B8A07A"][k % 2]}" stroke="{INK}" stroke-width="1.4"></path>')
    r = random.Random(seed)
    for k in range(6):                                         # the crowd: heads along the tiers
        y0 = h * (0.0 + k * 0.09) + h * 0.06
        n = int(w / 14)
        for i in range(n):
            t = i / (n - 1); x = -10 + (w + 20) * t
            y = y0 + h * 0.1 * (2 * t - 1) ** 2 - h * 0.035
            if r.random() < 0.8:
                o.append(f'<circle cx="{f(x + r.uniform(-3, 3))}" cy="{f(y)}" r="{f(max(2.4, h * 0.014))}" fill="{r.choice(["#3A2A2A", "#5A3A2A", "#2A2A3A", "#6A4A3A"])}"></circle>')
    o.append(f'<path d="M-10 {f(h * 0.6)} C {f(w * 0.2)} {f(h * 0.54)} {f(w * 0.8)} {f(h * 0.54)} {f(w + 10)} {f(h * 0.6)} L {f(w + 10)} {f(h * 0.66)} C {f(w * 0.8)} {f(h * 0.6)} {f(w * 0.2)} {f(h * 0.6)} -10 {f(h * 0.66)} Z" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<path d="M-10 {f(h * 0.66)} C {f(w * 0.2)} {f(h * 0.6)} {f(w * 0.8)} {f(h * 0.6)} {f(w + 10)} {f(h * 0.66)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#E8C890" stroke="{INK}" stroke-width="2"></path>')
    gx, gw = w * 0.5, w * 0.08                                  # the gate, open and dark
    o.append(f'<path d="M{f(gx - gw / 2)} {f(h * 0.66)} L {f(gx - gw / 2)} {f(h * 0.58)} Q {f(gx)} {f(h * 0.5)} {f(gx + gw / 2)} {f(h * 0.58)} L {f(gx + gw / 2)} {f(h * 0.66)} Z" fill="#1A1010" stroke="{INK}" stroke-width="2"></path>')
    for k in range(9):
        o.append(f'<path d="M{f(w * r.uniform(0.05, 0.95))} {f(h * r.uniform(0.72, 0.96))} l {f(r.uniform(10, 30))} 0" stroke="#C8A870" stroke-width="1.6"></path>')
    return "".join(o)

def toil(p, w, h, seed):
    """We toil, working with our own hands: the tentmakers' workshop — a length of dark goat-hair cloth stretched on its
    frame, Paul and Aquila sitting on the floor with the cloth across their knees, stitching, Priscilla standing with a
    folded length over her arm, the lamp on its ledge."""
    b = h * 0.92
    o = [mk.defs(p, *ALL, "ManUp", "WomanUp"), room(w, h, b, wall="#C8A878", floor="#7A5A3A"),
         f'<rect x="{f(w * 0.04)}" y="{f(h * 0.22)}" width="{f(w * 0.1)}" height="{f(b - h * 0.22)}" fill="#FFE6A0" stroke="{INK}" stroke-width="2.4"></rect>']
    fx0, fx1, ft = w * 0.2, w * 0.66, h * 0.18                 # the frame with the cloth on it
    o.append(f'<path d="M{f(fx0)} {f(b)} L {f(fx0 + w * 0.02)} {f(ft)} M{f(fx1)} {f(b)} L {f(fx1 - w * 0.02)} {f(ft)} M{f(fx0 - 6)} {f(ft)} L {f(fx1 + 6)} {f(ft)}" stroke="#5A3A22" stroke-width="5"></path>'
             f'<path d="M{f(fx0 + w * 0.025)} {f(ft + 4)} L {f(fx1 - w * 0.025)} {f(ft + 4)} L {f(fx1 - w * 0.04)} {f(b - h * 0.36)} C {f((fx0 + fx1) / 2)} {f(b - h * 0.3)} {f((fx0 + fx1) / 2)} {f(b - h * 0.34)} {f(fx0 + w * 0.04)} {f(b - h * 0.36)} Z" fill="#2A221E" stroke="{INK}" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(fx0 + w * 0.03)} {f(ft + 10 + k * h * 0.07)} L {f(fx1 - w * 0.03)} {f(ft + 10 + k * h * 0.07)}" stroke="#4A3E36" stroke-width="1.4" stroke-dasharray="6 4"></path>' for k in range(1, 5)))
    s = fit(b, b - min(h * 0.74, 200))
    lap = '<path d="M-40 -40 C -10 -52 40 -52 76 -36 L 80 -28 C 40 -40 -10 -40 -40 -30 Z" fill="#2A221E" stroke="#0D0D0F" stroke-width="1.4"></path><path d="M40 -46 L 52 -72" stroke="#C8C2B6" stroke-width="1.6"></path>'
    o.append(_seated_lap(w * 0.3, b, s * 0.82, ROBES["paul"], "#5A4A3A", "#3A2A1A", lap))
    o.append(_seated_lap(w * 0.6, b, s * 0.82, "#8A6A3A", "#E0D4B0", "#3A2214", lap, flip=True))
    o.append(priscilla_r(p, w * 0.84, b, s, flip=True, up=[(-22, -158), (-38, -130), (-56, -120)],
                         extra='<path d="M-70 -128 L -44 -128 L -44 -100 L -70 -96 Z" fill="#2A221E" stroke="#0D0D0F" stroke-width="1.6"></path>'))
    o.append(clay_lamp(w * 0.76, h * 0.34, max(0.6, h / 320)))
    return "".join(o)

def _seated_lap(x, y, s, cloth, head, beard, lap, flip=False):
    """job.art.seated (a man sitting on the floor, knees drawn up) with work across his knees, drawn in his own units."""
    g = seated(x, y, s, cloth, head=head, beard=beard, flip=flip)
    i = g.rfind("</g>")
    return g[:i] + lap + g[i:]

def timothy_sent(p, w, h, seed):
    """For this cause have I sent unto you Timothy: the study at Ephesus, Paul handing a sealed scroll to Timothy at the
    door, the night street beyond."""
    return study_co1(p, w, h, seed, stage="give", bearer=timothy_r)

def rod_or_love(w, h, seed):
    """Shall I come unto you with a rod, or in love and a spirit of gentleness? One panel in two lights: at the left, on
    cold stone under a red sky, a rod lying; at the right, warm lamplight in an open doorway, a lamp on the threshold."""
    o = [f'<defs><linearGradient id="rl{seed}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5A1A1A"></stop><stop offset="1" stop-color="#D7261E"></stop></linearGradient>'
         f'<linearGradient id="rm{seed}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3A2418"></stop><stop offset="1" stop-color="#C8803A"></stop></linearGradient></defs>',
         f'<rect x="-10" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="url(#rl{seed})"></rect>',
         f'<rect x="{f(w * 0.5)}" y="-10" width="{f(w * 0.5 + 10)}" height="{f(h + 20)}" fill="url(#rm{seed})"></rect>']
    b = h * 0.7
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w * 0.5 + 10)}" height="{f(h)}" fill="#4A4A54" stroke="{INK}" stroke-width="2"></rect>')
    k = min(w / 600, h / 220)
    o.append(f'<path d="M{f(w * 0.06)} {f(b + h * 0.12)} L {f(w * 0.44)} {f(b - h * 0.02)}" stroke="{INK}" stroke-width="{f(16 * k)}" stroke-linecap="round"></path>'
             f'<path d="M{f(w * 0.06)} {f(b + h * 0.12)} L {f(w * 0.44)} {f(b - h * 0.02)}" stroke="#7A4A22" stroke-width="{f(11 * k)}" stroke-linecap="round"></path>'
             + "".join(f'<path d="M{f(w * (0.06 + 0.38 * t))} {f(b + h * (0.12 - 0.14 * t) - 2 * k)} l {f(6 * k)} {f(-3 * k)}" stroke="#4A2A12" stroke-width="{f(2 * k)}"></path>' for t in (0.2, 0.45, 0.7)))
    dx, dw = w * 0.56, w * 0.14
    o.append(f'<rect x="{f(w * 0.5)}" y="{f(b)}" width="{f(w * 0.5 + 10)}" height="{f(h)}" fill="#5A3A22" stroke="{INK}" stroke-width="2"></rect>'
             + lamp_glow(dx + dw / 2, h * 0.4, h * 0.6, f"rg{seed}", op=0.6)
             + f'<rect x="{f(dx)}" y="{f(h * 0.12)}" width="{f(dw)}" height="{f(b - h * 0.12)}" fill="#FFE6A0" stroke="{INK}" stroke-width="3"></rect>'
             + f'<path d="M{f(dx + dw)} {f(h * 0.12)} L {f(dx + dw * 1.5)} {f(h * 0.08)} L {f(dx + dw * 1.5)} {f(b + h * 0.04)} L {f(dx + dw)} {f(b)} Z" fill="#7A4A2A" stroke="{INK}" stroke-width="2.4"></path>'
             + f'<path d="M{f(dx)} {f(b)} L {f(dx + dw)} {f(b)} L {f(dx + dw * 1.6)} {f(h + 10)} L {f(dx - dw * 0.6)} {f(h + 10)} Z" fill="#FFE6A0" opacity="0.45"></path>'
             + clay_lamp(dx + dw * 0.5, b + h * 0.08, k * 1.3))
    o.append(f'<path d="M{f(w * 0.5)} -10 L {f(w * 0.5)} {f(h + 10)}" stroke="{INK}" stroke-width="4"></path>')
    o.append(plate_label(w * 0.25, h * 0.12, "A ROD", "#FFF8E6", 12, halo_="#0D0D0F") + plate_label(w * 0.75, h * 0.08, "IN LOVE", "#FFF8E6", 12, halo_="#3A2418"))
    return "".join(o)
