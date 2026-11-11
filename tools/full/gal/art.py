"""Drawings for the Galatians volume. Galatians starts from all of Acts' drawings (`from act.art16 import *`, which carries
act.art … act.art15, Mark's and Matthew's drawings) and from the epistle kit (epistle.py: the study, the sealed scroll, the
letter's road, the radiance, the technical plate), and adds its own.

Galatians' people at a distance, on the kit silhouettes (epistle.robed): Paul only ever epistle.paul_fig; Titus (titus) a
Greek, bareheaded, short black hair, clean-shaven, a sand tunic and a blue mantle; Barnabas (barnabas_r) Acts' green
headcloth and robe and brown beard; Cephas (cephas) ntcast's brown robe, dark hair and grey-brown beard; John (john_r)
young, beardless, his rust robe; James the Lord's brother (james_r) Acts' white headcloth and grey beard; Hagar a cerulean
robe and veil, Sarah a mulberry robe and veil (as Genesis draws them). God is never drawn (light); the angel of 1:8 a figure
of white light with a gold rim and no face. Every function takes (p, w, h, seed, ...) or (w, h, ...); p, a prefix unique to
the panel, names the figure defs and gradients."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from act.art16 import *
from act.art import f, INK, _street, _house, _road, _gate, _prison
from act.art4 import tent_sojourn
from act.art5 import laid_waste, damascus_road
from act.art6 import antioch
from act.art8 import iconium
from epistle import (study, still_life, sealed_scroll, open_letter, reed_pen, inkpot, lamp_glow, letter_road, plate_bg, radiance, tag, dim, robed, paul_fig,
                     scribe_seated, mat as floor_mat, low_table, SEPIA, SEAL)
from oba.minor import vista, halo, rays, starfield, mount_zion
from genesis.art3 import label, node, route
from genesis.art4 import shining
from mat.art import veil as _veil, temple, houses, star_of, night
from mat.art11 import golgotha
from ntcast import PETER, JOHN, PAUL as PAUL_FACE
import exodus4 as E4, exodus5 as V
from gal.common import TITUS_LOOK, BARNABAS, JAMES_LORD

GOLD, CY = "#FFD23F", "#8FD0E2"

def plate_label(x, y, text, color=GOLD, size=10, anchor="middle", halo_="#0B1A2E"):
    """A label with a dark halo so it reads over a drawing."""
    return label(x, y, text, color, size, anchor).replace("<text ", f'<text stroke="{halo_}" stroke-width="3" paint-order="stroke" stroke-linejoin="round" ', 1)

# ---- Galatians' cast at a distance ----------------------------------------------------------------------------------------
def titus(p, x, y, s, flip=False, up=None, extra=""):
    return robed(p, x, y, s, TITUS_LOOK["cloth"], hair=TITUS_LOOK["hair"], mantle=TITUS_LOOK["mantle"], belt="#8A6A3A", flip=flip, up=up, extra=extra)
def barnabas_r(p, x, y, s, flip=False, up=None, extra=""):
    return robed(p, x, y, s, "#3A6A3A", head="#3A6A3A", cord="#2A1A10", beard="#4A2A1A", mantle="#2A4A2A", flip=flip, up=up, extra=extra)
def cephas(p, x, y, s, flip=False, up=None, extra=""):
    return robed(p, x, y, s, ROBES["peter"], hair="#2A2420", beard="#4A4440", mantle="#4A3420", flip=flip, up=up, extra=extra)
def john_r(p, x, y, s, flip=False, up=None, extra=""):
    return robed(p, x, y, s, ROBES["john"], hair="#2A1A10", belt="#6A2A1A", flip=flip, up=up, extra=extra)
def james_r(p, x, y, s, flip=False, up=None, extra=""):
    return robed(p, x, y, s, "#B8B0A0", head="#F3EFE6", cord="#6A5A3A", beard="#A8A296", mantle="#8A8478", flip=flip, up=up, extra=extra)
def brother(p, x, y, s, i=0, flip=False, up=None):
    """One of the brethren with Paul (1:2): plain robes and cool or off-white headcloths."""
    c, hd, bd = [("#4A5A6A", "#2A3A4A", "#2A1A10"), ("#6A5A4A", "#E8E2D6", "#6A645E"), ("#3A4A3A", "#1F2F2A", "#3A2A1A"), ("#5A4A5A", None, "#1A1210")][i % 4]
    return robed(p, x, y, s, c, head=hd, hair=None if hd else "#1A1210", beard=bd, flip=flip, up=up)
def gentile(p, x, y, s, i=0, flip=False, up=None, woman=False):
    """A Gentile believer of Galatia or Antioch: bareheaded (a man) in a himation, or a woman in a cool veil."""
    if woman:
        c, vl = [("#7A6A8A", "#2A3A5A"), ("#5A7A7A", "#1F3A3A"), ("#8A7A6A", "#E8E2D6")][i % 3]
        return robed(p, x, y, s * 0.94, c, woman=True, veil=vl, flip=flip, up=up)
    c, hr, bd, mn = [("#E8DCC0", "#3A2A1A", None, "#4A6A8A"), ("#C8B898", "#1A1210", "#1A1210", "#6A3A3A"), ("#D8D0C0", "#7A6A5A", "#8A7A6A", "#3A5A3A")][i % 3]
    return robed(p, x, y, s, c, hair=hr, beard=bd, mantle=mn, flip=flip, up=up)
def hagar_r(p, x, y, s, flip=False, up=None):
    return robed(p, x, y, s * 0.94, "#2A6A9A", woman=True, veil="#1F4F7A", flip=flip, up=up)
def sarah_r(p, x, y, s, flip=False, up=None):
    return robed(p, x, y, s * 0.94, "#8A3A5A", woman=True, veil="#8A3A5A", hair="#B8B2A6", flip=flip, up=up)
def boy(p, x, y, s, cloth="#C8A060", hair="#2A1A10", flip=False, up=None, extra=""):
    """A boy (the figure at about two-thirds height), bareheaded, a plain tunic."""
    return robed(p, x, y, s, cloth, hair=hair, belt="#6A4A2A", flip=flip, up=up, extra=extra)
WHO.update({"titus": titus, "barnabas_r": barnabas_r, "cephas": cephas, "john_r": john_r, "james_r": james_r})

def _defs(p): return mk.defs(p, *ALL, "ManUp", "WomanUp")

def light_fig(p, x, y, s, flip=False, up=None):
    """An angel: a figure of white light with a gold rim, no face, no wings (the text gives none), a soft light about it."""
    return (f'<ellipse cx="{f(x)}" cy="{f(y - 110 * s)}" rx="{f(80 * s)}" ry="{f(130 * s)}" fill="#FFF4C2" opacity="0.45"></ellipse>'
            + mk.person(p, round(x), round(y), round(s, 3), body="#FFFDF0", cloth="#FFFFFF", stroke="#E8B830", sw=3, flip=flip, up=up))

def black_tent(x, base, wd, hh, lit=True):
    """A goat-hair tent of the desert, low and wide, its roof drawn up on poles in three peaks, the front open on a lit
    doorway; (x, base) the middle of its foot."""
    l, r, t = x - wd / 2, x + wd / 2, base - hh
    roof = (f"M{f(l - wd * 0.04)} {f(base - hh * 0.3)} L {f(l + wd * 0.12)} {f(t + hh * 0.12)} L {f(x - wd * 0.22)} {f(t + hh * 0.2)} L {f(x)} {f(t)} "
            f"L {f(x + wd * 0.22)} {f(t + hh * 0.2)} L {f(r - wd * 0.12)} {f(t + hh * 0.12)} L {f(r + wd * 0.04)} {f(base - hh * 0.3)} Z")
    o = [f'<path d="M{f(l)} {f(base)} L {f(l)} {f(base - hh * 0.36)} L {f(r)} {f(base - hh * 0.36)} L {f(r)} {f(base)} Z" fill="#3A2418" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="{roof}" fill="#2A1A12" stroke="{INK}" stroke-width="2"></path>']
    o += [f'<path d="M{f(l + wd * k)} {f(base - hh * 0.36)} L {f(l + wd * k)} {f(base)}" stroke="#1A100A" stroke-width="1.6"></path>' for k in (0.2, 0.4, 0.6, 0.8)]
    o.append(f'<rect x="{f(x - wd * 0.09)}" y="{f(base - hh * 0.5)}" width="{f(wd * 0.18)}" height="{f(hh * 0.5)}" fill="{"#FFC14D" if lit else "#0D0D0F"}" stroke="{INK}" stroke-width="1.6"></rect>')
    o += [f'<path d="M{f(xx)} {f(base - hh * 0.3)} L {f(xx - wd * 0.06 * sg)} {f(base)}" stroke="#5A3A22" stroke-width="1.4"></path>' for xx, sg in ((l - wd * 0.04, 1), (r + wd * 0.04, -1))]
    return "".join(o)

def night_window(x, y, ww, hh, seed):
    """A small window on the night sky, stars and a hill, no city."""
    uid = f"nw{seed}"
    return (f'<defs><clipPath id="{uid}"><rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}"></rect></clipPath></defs>'
            f'<g clip-path="url(#{uid})"><rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}" fill="#141838"></rect>'
            f'<g transform="translate({f(x)} {f(y)})">' + mk.stars(int(ww * hh / 500) + 6, ww, hh * 0.6, seed) + '</g>'
            f'<path d="M{f(x - 4)} {f(y + hh * 0.78)} C {f(x + ww * 0.3)} {f(y + hh * 0.6)} {f(x + ww * 0.6)} {f(y + hh * 0.66)} {f(x + ww + 4)} {f(y + hh * 0.56)} L {f(x + ww + 4)} {f(y + hh + 4)} L {f(x - 4)} {f(y + hh + 4)} Z" fill="#2A2440"></path></g>'
            f'<rect x="{f(x)}" y="{f(y)}" width="{f(ww)}" height="{f(hh)}" fill="none" stroke="{INK}" stroke-width="3"></rect>'
            f'<path d="M{f(x + ww / 2)} {f(y)} L {f(x + ww / 2)} {f(y + hh)}" stroke="#5A3A22" stroke-width="4"></path>'
            f'<rect x="{f(x - 8)}" y="{f(y + hh)}" width="{f(ww + 16)}" height="8" fill="#6A4A2A" stroke="{INK}" stroke-width="1.6"></rect>')

# ---- Galatians 1 ----------------------------------------------------------------------------------------------------------
def study_brethren(p, w, h, seed, stage="dictate", n=2, fig_h=None):
    """Paul, and all the brethren that are with me: the study by lamplight (epistle.study, Paul dictating, the scribe on his
    mat), a night window (no city named), and the brethren standing at the right listening."""
    b = h * 0.95
    s = (fig_h or h * 0.72) / 205
    o = [study(p, w, h, seed, stage=stage, window=False, fig_h=fig_h)]
    o.insert(1, night_window(w * 0.42, b - 214 * s, min(w * 0.15, 104 * s), min(h * 0.36, 88 * s), seed))
    for i in range(n):
        o.append(brother(p, w * (0.94 - 0.11 * i), b, s * (0.98 - 0.02 * i), i, flip=True))
    return "".join(o)

def galatia_road(w, h):
    """Unto the churches of Galatia: the letter's road from Antioch of Syria through the Cilician gates to Derbe, Lystra,
    Iconium and Antioch of Pisidia — the cities of the first journey (Acts 13–14) — on Acts' map."""
    rt = ["ANTIOCH", (36.0, 36.6), "TARSUS", (34.6, 37.3), "DERBE", "LYSTRA", "ICONIUM", "ANTIOCH OF PISIDIA"]
    return letter_road(w, h, rt, title="GALATIANS 1:2 · UNTO THE CHURCHES OF GALATIA", box=(30.6, 36.4, 36.1, 39.7),
                       places=("ANTIOCH", "TARSUS", "DERBE", "LYSTRA", "ICONIUM", "ANTIOCH OF PISIDIA"), hi=("DERBE", "LYSTRA", "ICONIUM", "ANTIOCH OF PISIDIA"),
                       regions=("GALATIA", "PISIDIA", "PHRYGIA", "CILICIA", "SYRIA", "CYPRUS"))

def angel_gospel(p, w, h, seed):
    """Though we, or an angel from heaven, should preach any gospel other: at the left a figure of white light with a gold
    rim standing on the hill (no face, no wings — the text gives none), an open roll in its hand; at the right, on a stone,
    the gospel that was preached, the roll tied and sealed, lit gold; the other roll crossed out in red."""
    b = h * 0.92
    o = [_defs(p), sky(w, h, "#0B0B2A", "#3A2A5A"), starfield(w, h, seed, 50, 0.5), hills(w, h, h * 0.62, seed, color="#1E1838", amp=12, step=90),
         ground(w, h, h * 0.72, "#2A2440", dy=0)]
    s = fit(b, max(h * 0.12, b - 230))
    ax = w * 0.26
    o.append(halo(ax, b - 110 * s, 150 * s, "#FFF4C2", 0.45) + rays(ax, b - 110 * s, 24, 40 * s, 200 * s, "#FFF4C2", 0.25, 3))
    o.append(light_fig(p, ax, b, s, up=[(-22, -158), (-40, -140), (-58, -136)]))
    ox, oy = ax - 64 * s, b - 140 * s                        # the other gospel: an open roll, struck through
    o.append(f'<rect x="{f(ox - 26 * s)}" y="{f(oy - 18 * s)}" width="{f(52 * s)}" height="{f(30 * s)}" fill="#EADBB4" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<path d="M{f(ox - 34 * s)} {f(oy - 26 * s)} L {f(ox + 34 * s)} {f(oy + 20 * s)} M{f(ox + 34 * s)} {f(oy - 26 * s)} L {f(ox - 34 * s)} {f(oy + 20 * s)}" stroke="#D7261E" stroke-width="{f(6 * s)}" stroke-linecap="round"></path>')
    gx = w * 0.72
    o.append(halo(gx, b - 60 * s, 120 * s, "#FFE680", 0.55))
    o.append(f'<path d="M{f(gx - 90 * s)} {f(b)} L {f(gx - 80 * s)} {f(b - 50 * s)} L {f(gx + 80 * s)} {f(b - 50 * s)} L {f(gx + 90 * s)} {f(b)} Z" fill="#5A5060" stroke="{INK}" stroke-width="2.4"></path>')
    o.append(sealed_scroll(gx, b - 70 * s, 1.0 * s, rot=-4))
    o.append(plate_label(ax, h * 0.1, "AN ANGEL FROM HEAVEN · ANY OTHER GOSPEL", "#FF8A6A", 10)
             + plate_label(gx, h * 0.1, "THE GOSPEL WHICH WE PREACHED", GOLD, 10))
    o.append(plate_label(ox, oy + 44 * s, "ANATHEMA", "#FF6A4A", 12))
    return "".join(o)

def arabia(p, w, h, seed):
    """I went away into Arabia; and again I returned unto Damascus: the desert at evening, sand ridges and a black tent far
    off, Paul walking alone with his staff; at the right on the horizon the walls of Damascus."""
    b = h * 0.92
    o = [_defs(p), sky(w, h, "#4A2A5A", "#FFB07A"), halo(w * 0.2, h * 0.5, h * 0.4, "#FFD08A", 0.5),
         f'<circle cx="{f(w * 0.2)}" cy="{f(h * 0.5)}" r="{f(max(12, h * 0.05))}" fill="#FFE6A0"></circle>',
         walls(w * 0.74, w * 0.98, h * 0.56, h * 0.1, seed, towers=2, color="#B89A7A"),
         f'<path d="M-10 {f(h * 0.58)} C {f(w * 0.2)} {f(h * 0.52)} {f(w * 0.4)} {f(h * 0.6)} {f(w * 0.6)} {f(h * 0.55)} C {f(w * 0.8)} {f(h * 0.5)} {f(w * 0.9)} {f(h * 0.56)} {f(w + 10)} {f(h * 0.56)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#D8A86A" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M-10 {f(h * 0.74)} C {f(w * 0.25)} {f(h * 0.66)} {f(w * 0.5)} {f(h * 0.8)} {f(w * 0.75)} {f(h * 0.7)} C {f(w * 0.88)} {f(h * 0.66)} {f(w * 0.95)} {f(h * 0.7)} {f(w + 10)} {f(h * 0.7)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#C8904E" stroke="{INK}" stroke-width="2"></path>']
    o.append(black_tent(w * 0.12, h * 0.62, max(70, h * 0.24), max(26, h * 0.09), lit=False))
    s = fit(b, max(h * 0.2, b - 220))
    staff = '<path d="M-52 -176 L -46 4" stroke="#5A3A22" stroke-width="5" stroke-linecap="round"></path>'
    o.append(paul_fig(p, w * 0.46, b, s, up=[(-22, -158), (-38, -124), (-48, -96)], extra=staff))
    o.append(plate_label(w * 0.3, h * 0.12, "ARABIA", "#3A1E2A", 11, halo_="#FFE0B0") + plate_label(w * 0.86, h * 0.36, "DAMASCUS", "#3A1E2A", 10, halo_="#FFE0B0"))
    return "".join(o)

def tally(x, y, n, s=1.0, color="#F3EFE6"):
    """Days counted on the wall in strokes of five."""
    o = []
    for g in range((n + 4) // 5):
        gx = x + g * 34 * s
        k = min(5, n - g * 5)
        for i in range(min(k, 4)):
            o.append(f'<path d="M{f(gx + i * 6 * s)} {f(y)} L {f(gx + i * 6 * s)} {f(y + 24 * s)}" stroke="{color}" stroke-width="{f(2.4 * s)}" stroke-linecap="round"></path>')
        if k == 5: o.append(f'<path d="M{f(gx - 4 * s)} {f(y + 18 * s)} L {f(gx + 22 * s)} {f(y + 4 * s)}" stroke="{color}" stroke-width="{f(2.4 * s)}" stroke-linecap="round"></path>')
    return "".join(o)

def with_cephas(p, w, h, seed):
    """I went up to Jerusalem to visit Cephas, and tarried with him fifteen days: a room in Jerusalem, the temple seen
    through the window; Paul and Cephas sitting on the mat face to face; fifteen days scored on the wall; James the Lord's
    brother standing in the doorway."""
    b = h * 0.92
    o = [_defs(p), room(w, h, b, wall="#D8C098", floor="#8A6A4A")]
    wx, wy, ww, wh = w * 0.36, h * 0.16, w * 0.22, h * 0.32
    o.append(f'<defs><clipPath id="{p}cw"><rect x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(wh)}"></rect></clipPath></defs>'
             f'<g clip-path="url(#{p}cw)">' + f'<rect x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(wh)}" fill="#8FD0E2"></rect>'
             + temple(wx + ww * 0.5, wy + wh * 0.95, ww * 0.9) + '</g>'
             f'<rect x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(wh)}" fill="none" stroke="{INK}" stroke-width="3"></rect>'
             f'<rect x="{f(wx - 8)}" y="{f(wy + wh)}" width="{f(ww + 16)}" height="8" fill="#6A4A2A" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(tally(w * 0.66, h * 0.2, 15, max(0.6, h / 300), color="#5A3A22") + plate_label(w * 0.66 + 46 * max(0.6, h / 300), h * 0.2 + 42 * max(0.6, h / 300), "FIFTEEN DAYS", "#5A3A22", 9, halo_="#E8D8B0"))
    dx, dw = w * 0.84, w * 0.12
    o.append(f'<rect x="{f(dx)}" y="{f(h * 0.22)}" width="{f(dw)}" height="{f(b - h * 0.22)}" fill="#FFE6A0" stroke="{INK}" stroke-width="2.4"></rect>')
    s = fit(b, max(h * 0.2, b - 220))
    o.append(floor_mat(w * 0.14, b, w * 0.46, s))
    o.append(seated(w * 0.24, b - 2, s * 0.8, ROBES["paul"], head="#5A4A3A", beard="#3A2A1A"))
    o.append(seated(w * 0.5, b - 2, s * 0.8, ROBES["peter"], beard="#4A4440", flip=True))
    o.append(james_r(p, dx + dw * 0.5, b, s * 0.98, flip=True))
    return "".join(o)

def syria_cilicia(w, h):
    """Then I came into the regions of Syria and Cilicia: from Jerusalem down to Cæsarea, by sea to Tarsus, and to
    Antioch (Acts 9:30, 11:25–26), the churches of Judæa behind."""
    return geo.med_map(w, h, box=(32.4, 37.8, 31.2, 37.4), places=("JERUSALEM", "CÆSAREA", "TARSUS", "ANTIOCH", "DAMASCUS"),
                       routes=[("JERUSALEM", "CÆSAREA", (34.4, 33.6), (34.4, 36.2), "TARSUS"), ("TARSUS", (35.8, 36.9), "ANTIOCH")], hi=("TARSUS", "ANTIOCH"),
                       regions=("SYRIA", "CILICIA", "JUDÆA", "CYPRUS"), lit_routes=[0, 1], size=10, rsize=11,
                       title="GALATIANS 1:21 · THE REGIONS OF SYRIA AND CILICIA")

# ---- Galatians 2 ----------------------------------------------------------------------------------------------------------
def going_up(p, w, h, seed):
    """I went up again to Jerusalem with Barnabas, taking Titus also with me: the road climbing through the hills to the
    city on its hill; Paul, Barnabas and Titus on the road."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.5, seed, color="#9A9A6A", amp=14, step=90),
         mount_zion(w * 0.78, h * 0.62, w * 0.24, h * 0.34, seed, color="#B8A06A"),
         ground(w, h, h * 0.62, "#C8B07A", dy=0),
         f'<path d="M-10 {f(h * 0.98)} C {f(w * 0.3)} {f(h * 0.84)} {f(w * 0.56)} {f(h * 0.72)} {f(w * 0.72)} {f(h * 0.62)}" stroke="#E8D8B0" stroke-width="{f(max(12, h * 0.08))}" fill="none"></path>']
    s = fit(b, max(h * 0.24, b - 220))
    o.append(titus(p, w * 0.12, b, s * 0.98, flip=True) + barnabas_r(p, w * 0.24, b, s, flip=True)
             + paul_fig(p, w * 0.37, b, s, flip=True, up=[(-22, -158), (-46, -170), (-70, -184)]))
    o.append(plate_label(w * 0.78, h * 0.12, "JERUSALEM", "#12113A", 10, halo_="#F3EFE6"))
    return "".join(o)

def _person_mark(px, base, s, color, head=False, woman=False, flip=False, stroke=CY):
    return mk.person("gp", round(px), round(base), round(s, 3), body="#1E4A6A", cloth=color, woman=woman, kind="Robe" if woman else "Tunic", stroke=stroke, sw=2.4, flip=flip,
                     extra=A.headcloth("#163A56", cord=None).replace('stroke="#0D0D0F"', f'stroke="{stroke}"') if head else "")

def two_apostleships(w, h):
    """The gospel of the uncircumcision and the gospel of the circumcision: a plate — Peter's face at the left, his arrow
    to a company in headcloths (the circumcision); Paul's face at the right, his arrow to a company bareheaded (the Gentiles)."""
    o = [plate_bg(w, h, "GALATIANS 2:7–8 · UNTO THE CIRCUMCISION · UNTO THE GENTILES"), mk.defs("gp", *ALL)]
    fs = min((h - 74) / 380, w / 900) * 0.9
    fy = 54 + (h - 64 - 380 * fs) / 2
    o.append(mk.face(PETER, f(w * 0.02), f(fy), round(fs, 3)))
    o.append(mk.face(PAUL_FACE, f(w * 0.98), f(fy), round(fs, 3), flip=True))
    base, top = h * 0.88, h * 0.36
    sc = (base - top) / 205
    for i in range(4):
        o.append(_person_mark(w * (0.3 + i * 0.045), base, sc * (0.92 + 0.04 * (i % 2)), "#163A56", head=True, flip=True))
    for i in range(4):
        o.append(_person_mark(w * (0.56 + i * 0.045), base, sc * (0.92 + 0.04 * (i % 2)), "#24506E", woman=i == 2))
    o.append(route([(w * 0.2, h * 0.3), (w * 0.3, h * 0.3)], color=GOLD, sw=3, dash="8 5") + route([(w * 0.8, h * 0.3), (w * 0.7, h * 0.3)], color=GOLD, sw=3, dash="8 5"))
    o.append(label(w * 0.37, min(base + 18, h - 6), "THE CIRCUMCISION", GOLD, 9.5) + label(w * 0.63, min(base + 18, h - 6), "THE GENTILES", GOLD, 9.5))
    o.append(label(w * 0.11, fy - 6, "PETER", CY, 9.5) + label(w * 0.89, fy - 6, "PAUL", CY, 9.5))
    o.append(f'<path d="M{f(w * 0.5)} {f(top)} L {f(w * 0.5)} {f(base)}" stroke="#2C5A7A" stroke-width="1.4" stroke-dasharray="5 5"></path>')
    return "".join(o)

def colonnade(w, h, b, seed, tone="day"):
    """A colonnade of a court in Jerusalem: the sky, a portico of tall columns on a stone floor."""
    o = [sky(w, h, "#8FD0E2", "#F3E8C8") if tone == "day" else sky(w, h, "#4A2A5A", "#FFB07A"),
         hills(w, h, h * 0.4, seed, color="#A8A07A", amp=10, step=90)]
    o.append(f'<rect x="-10" y="{f(h * 0.08)}" width="{f(w + 20)}" height="{f(h * 0.08)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="-10" y="{f(h * 0.16)}" width="{f(w + 20)}" height="{f(h * 0.025)}" fill="#C8B898" stroke="{INK}" stroke-width="1.6"></rect>')
    n = 6
    for k in range(n):
        x = w * (0.04 + 0.92 * k / (n - 1))
        cw = w * 0.04
        o.append(f'<rect x="{f(x - cw / 2)}" y="{f(h * 0.185)}" width="{f(cw)}" height="{f(b - h * 0.2)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="{f(x - cw * 0.7)}" y="{f(h * 0.185)}" width="{f(cw * 1.4)}" height="{f(h * 0.025)}" fill="#E8DCC0" stroke="{INK}" stroke-width="1.6"></rect>'
                 f'<rect x="{f(x - cw * 0.7)}" y="{f(b - h * 0.03)}" width="{f(cw * 1.4)}" height="{f(h * 0.03)}" fill="#E8DCC0" stroke="{INK}" stroke-width="1.6"></rect>'
                 + "".join(f'<path d="M{f(x - cw * 0.5 + cw * j / 4)} {f(h * 0.21)} L {f(x - cw * 0.5 + cw * j / 4)} {f(b - h * 0.03)}" stroke="#C8C0B0" stroke-width="1"></path>' for j in (1, 2, 3)))
    o.append(pavement(w, h, b - 2, color="#D8CCB0"))
    return "".join(o)

def right_hands(p, w, h, seed):
    """James and Cephas and John, they who were reputed to be pillars, gave to me and Barnabas the right hands of
    fellowship: in the colonnade of a court in Jerusalem, Paul and James clasping right hands in the middle, Barnabas
    behind Paul, Cephas and John behind James, a little light where the hands meet."""
    b = h * 0.94
    o = [_defs(p), colonnade(w, h, b, seed)]
    s = fit(b, max(h * 0.18, b - 230))
    cx = w * 0.5
    reach = [(-22, -158), (-48, -146), (-70, -140)]
    px, jx = cx - 72 * s, cx + 72 * s
    o.append(halo(cx, b - 140 * s, 40 * s, "#FFF4C2", 0.7))
    o.append(barnabas_r(p, px - 70 * s, b, s * 0.98, flip=True))
    o.append(paul_fig(p, px, b, s, flip=True, up=reach))
    o.append(john_r(p, jx + 132 * s, b, s * 0.96) + cephas(p, jx + 70 * s, b, s * 0.98) + james_r(p, jx, b, s, up=reach))
    o.append("".join(plate_label(x, h * 0.07, t, "#12113A", 9, halo_="#F3EFE6") for x, t in
                     ((px - 70 * s, "BARNABAS"), (px, "PAUL"), (jx, "JAMES"), (jx + 70 * s, "CEPHAS"), (jx + 132 * s, "JOHN"))))
    return "".join(o)

def antioch_court(w, h, seed):
    """The court of a house at Antioch of Syria: white columns and red roofs beyond the wall, the mountain behind, a stone
    floor (Acts' Antioch)."""
    b = h * 0.94
    o = [sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.24, seed, color="#8A9A7A", amp=22, step=120)]
    for k in range(6):
        x = w * (0.02 + 0.17 * k); hh = h * (0.14 + 0.05 * (k % 3))
        o.append(f'<rect x="{f(x)}" y="{f(h * 0.44 - hh)}" width="{f(w * 0.14)}" height="{f(hh)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>'
                 f'<path d="M{f(x - 6)} {f(h * 0.44 - hh)} L {f(x + w * 0.07)} {f(h * 0.44 - hh - 16)} L {f(x + w * 0.14 + 6)} {f(h * 0.44 - hh)} Z" fill="#B5583A" stroke="{INK}" stroke-width="2"></path>')
    o.append(f'<rect x="-10" y="{f(h * 0.42)}" width="{f(w + 20)}" height="{f(h * 0.2)}" fill="#D8C8A8" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="-10" y="{f(h * 0.42)}" width="{f(w + 20)}" height="{f(h * 0.025)}" fill="#C8B898" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(pavement(w, h, h * 0.62, color="#C8B898"))
    return "".join(o), b

def low_board(x0, x1, base, s):
    """A long low table on the floor with bread, a cup and a dish on it."""
    ty = base - 30 * s
    o = [f'<rect x="{f(x0)}" y="{f(ty)}" width="{f(x1 - x0)}" height="{f(8 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>']
    o += [f'<rect x="{f(lx)}" y="{f(ty + 8 * s)}" width="{f(7 * s)}" height="{f(22 * s)}" fill="#4A2A14" stroke="{INK}" stroke-width="1.6"></rect>' for lx in (x0 + 8 * s, x1 - 15 * s)]
    for i, xx in enumerate([x0 + (x1 - x0) * t for t in (0.16, 0.38, 0.6, 0.82)]):
        if i % 2 == 0: o.append(f'<ellipse cx="{f(xx)}" cy="{f(ty - 5 * s)}" rx="{f(13 * s)}" ry="{f(6 * s)}" fill="#C88A4A" stroke="{INK}" stroke-width="1.6"></ellipse>')
        else: o.append(f'<path d="M{f(xx - 7 * s)} {f(ty)} L {f(xx - 9 * s)} {f(ty - 16 * s)} L {f(xx + 9 * s)} {f(ty - 16 * s)} L {f(xx + 7 * s)} {f(ty)} Z" fill="#B85A3A" stroke="{INK}" stroke-width="1.6"></path>')
    return "".join(o)

def withdrew(p, w, h, seed):
    """When they came, he drew back and separated himself: the Gentile believers sitting at the low table in the court at
    Antioch, Cephas's place empty; Cephas walking away to the right to the men come from James (headcloths), Barnabas
    rising to follow him."""
    bg, b = antioch_court(w, h, seed)
    o = [_defs(p), bg]
    s = fit(b, max(h * 0.18, b - 230))
    o.append(low_board(w * 0.04, w * 0.5, b, s))
    for i, x in enumerate((0.08, 0.2, 0.32)):
        o.append(seated(w * x, b, s * 0.76, ["#E8DCC0", "#C8B898", "#7A6A8A"][i], beard=["#3A2A1A", None, "#1A1210"][i]))
    o.append(seated(w * 0.48, b, s * 0.76, "#D8D0C0", beard="#8A7A6A", flip=True))
    o.append(f'<ellipse cx="{f(w * 0.4)}" cy="{f(b - 3)}" rx="{f(18 * s)}" ry="{f(5 * s)}" fill="#8A3A2A" stroke="{INK}" stroke-width="1.6"></ellipse>')   # the empty cushion
    o.append(barnabas_r(p, w * 0.56, b, s * 0.98))
    o.append(cephas(p, w * 0.68, b, s))
    o.append(robed(p, w * 0.84, b, s * 0.98, "#E8E2D6", head="#F3EFE6", cord="#1F3A7A", beard="#3A2A1A", flip=True)
             + robed(p, w * 0.94, b, s * 0.97, "#3A3A4A", head="#2A2A3A", cord="#E8E2D6", beard="#6A645E", flip=True))
    o.append(plate_label(w * 0.89, h * 0.07, "CERTAIN FROM JAMES", "#12113A", 9, halo_="#F3EFE6") + plate_label(w * 0.26, h * 0.07, "THE GENTILES", "#12113A", 9, halo_="#F3EFE6"))
    return "".join(o)

def withstood(p, w, h, seed):
    """I said unto Cephas before them all: Paul standing in the court at Antioch, his hand out toward Cephas; Cephas
    facing him; the church at the table watching, Barnabas among them."""
    bg, b = antioch_court(w, h, seed + 1)
    o = [_defs(p), bg]
    s = fit(b, max(h * 0.18, b - 230))
    o.append(low_board(w * 0.5, w * 0.98, b, s))
    for i, x in enumerate((0.58, 0.7, 0.82, 0.94)):
        o.append(seated(w * x, b, s * 0.74, ["#E8DCC0", "#3A6A3A", "#7A6A8A", "#C8B898"][i], head="#3A6A3A" if i == 1 else None,
                        beard=["#3A2A1A", "#4A2A1A", None, "#1A1210"][i], flip=True))
    o.append(paul_fig(p, w * 0.14, b, s, flip=True, up=[(-22, -158), (-50, -156), (-78, -164)]))
    o.append(cephas(p, w * 0.36, b, s))
    return "".join(o)

# ---- Galatians 3 ----------------------------------------------------------------------------------------------------------
def nations_blessed(w, h):
    """In thee shall all the nations be blessed: rings of light going out from the land of Canaan over all the nations of
    the map."""
    return geo.med_map(w, h, box=(12.0, 50.0, 26.0, 44.0), places=("SHECHEM", "HARAN", "UR", "MEMPHIS", "ROME", "ATHENS"), hi=("SHECHEM",),
                       rings="SHECHEM", red=True, regions=("EGYPT", "MESOPOTAMIA", "ASIA", "ITALY", "ARABIA", "MEDIA", "LIBYA"),
                       title="GALATIANS 3:8 · ALL THE NATIONS")

def covenant_seed(w, h):
    """A man's covenant confirmed, and to thy seed, which is Christ: a plate — at the left a covenant roll tied and sealed
    with two seals, nothing added; at the right ABRAHAM, and from him not many seeds (struck through) but one line to a
    single gold node, the seed, Christ."""
    o = [plate_bg(w, h, "GALATIANS 3:15–16 · A COVENANT CONFIRMED · AS OF ONE")]
    k = min(w / 620, (h - 40) / 240)
    cy = h * 0.56
    o.append(sealed_scroll(w * 0.2, cy, 1.4 * k, rot=-6) + f'<circle cx="{f(w * 0.2 + 40 * k)}" cy="{f(cy + 10 * k)}" r="{f(12 * k)}" fill="{SEAL}" stroke="{INK}" stroke-width="2"></circle>')
    o.append(label(w * 0.2, min(cy + 70 * k, h - 10), "A MAN'S COVENANT · CONFIRMED", CY, 9.5))
    o.append(f'<path d="M{f(w * 0.4)} 40 L {f(w * 0.4)} {f(h - 8)}" stroke="#2C5A7A" stroke-width="1.4" stroke-dasharray="6 5"></path>')
    ax, ay = w * 0.5, cy
    o.append(f'<circle cx="{f(ax)}" cy="{f(ay)}" r="{f(9 * k)}" fill="{CY}" stroke="{INK}" stroke-width="1.6"></circle>' + label(ax, ay + 24 * k, "ABRAHAM", CY, 10))
    for i in range(7):                                            # seeds, as of many — struck through
        yy = h * 0.2 + (h * 0.3) * i / 6; xx = w * 0.72
        o.append(f'<path d="M{f(ax + 10 * k)} {f(ay - 4 * k)} L {f(xx)} {f(yy)}" stroke="#4A6A8A" stroke-width="1.4"></path>'
                 f'<circle cx="{f(xx)}" cy="{f(yy)}" r="{f(5 * k)}" fill="#4A6A8A"></circle>')
    o.append(f'<path d="M{f(w * 0.68)} {f(h * 0.17)} L {f(w * 0.76)} {f(h * 0.53)} M{f(w * 0.76)} {f(h * 0.17)} L {f(w * 0.68)} {f(h * 0.53)}" stroke="#FF6A4A" stroke-width="3"></path>'
             + label(w * 0.86, h * 0.36, "SEEDS · AS OF MANY", "#FF8A6A", 9.5))
    gy = h * 0.8
    o.append(route([(ax + 10 * k, ay + 6 * k), (w * 0.72, gy)], color=GOLD, sw=3) + halo(w * 0.72, gy, 26 * k, "#FFE680", 0.6)
             + f'<circle cx="{f(w * 0.72)}" cy="{f(gy)}" r="{f(10 * k)}" fill="{GOLD}" stroke="{INK}" stroke-width="1.6"></circle>'
             + label(w * 0.86, gy + 4, "THE SEED · CHRIST", GOLD, 10))
    return "".join(o)

def four_thirty(w, h):
    """The law, which came four hundred and thirty years after, doth not disannul the covenant confirmed beforehand by God:
    a timeline plate — at the left the promise to Abraham (the sealed roll, confirmed), at the right the law at Sinai (the
    two tables), 430 years measured between, and the promise standing unbroken."""
    o = [plate_bg(w, h, "GALATIANS 3:17 · FOUR HUNDRED AND THIRTY YEARS")]
    k = min(w / 620, (h - 40) / 230)
    ay = h * 0.7
    x0, x1 = w * 0.18, w * 0.76
    o.append(f'<path d="M{f(w * 0.06)} {f(ay)} L {f(w * 0.94)} {f(ay)}" stroke="{CY}" stroke-width="2.4"></path>')
    for i in range(11):
        x = x0 + (x1 - x0) * i / 10
        o.append(f'<path d="M{f(x)} {f(ay - 5)} L {f(x)} {f(ay + 5)}" stroke="{CY}" stroke-width="1.6"></path>')
    o.append(f'<circle cx="{f(x0)}" cy="{f(ay)}" r="{f(9 * k)}" fill="{GOLD}" stroke="{INK}" stroke-width="1.6"></circle>'
             f'<circle cx="{f(x1)}" cy="{f(ay)}" r="{f(9 * k)}" fill="{CY}" stroke="{INK}" stroke-width="1.6"></circle>')
    o.append(halo(x0, ay - 64 * k, 50 * k, "#FFE680", 0.5) + sealed_scroll(x0, ay - 64 * k, 0.9 * k, rot=-6))
    o.append(V.tables(x1, ay - 18 * k, min(0.5, 0.42 * k), uid="gt430"))
    o.append(dim(x0, ay + 30 * k, x1, ay + 30 * k, "430 YEARS", size=10, color=GOLD))
    o.append(label(x0, min(ay + 64 * k, h - 8), "THE PROMISE · TO ABRAHAM", GOLD, 9.5) + label(x1, min(ay + 64 * k, h - 8), "THE LAW · SINAI", CY, 9.5))
    o.append(route([(x0 + 70 * k, ay - 64 * k), (x1 - 70 * k, ay - 64 * k)], color=GOLD, sw=2, dash="6 5")
             + label(w * 0.5, ay - 74 * k, "DOTH NOT DISANNUL", GOLD, 9.5))
    return "".join(o)

def in_ward(p, w, h, seed):
    """Kept in ward under the law, shut up unto the faith which should afterwards be revealed: within a ward-room of stone
    at night, the iron-bound door shut and barred, a lamp; through the high barred window the first light of the dawn."""
    o = [bgr(w, h, "#3A3238")]
    for k in range(9):
        y = h * k / 8
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#2A2228" stroke-width="2"></path>')
        for j in range(9):
            x = w * (j + (k % 2) * 0.5) / 8
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y + h / 8)}" stroke="#2A2228" stroke-width="1.6"></path>')
    b = h * 0.92
    wx, wy, ww, wh = w * 0.62, h * 0.12, w * 0.16, h * 0.24
    o.append(f'<path d="M{f(wx)} {f(wy + wh)} L {f(wx + ww)} {f(wy + wh)} L {f(wx + ww * 0.4)} {f(b)} L {f(wx - ww * 1.6)} {f(b)} Z" fill="#FFE6A0" opacity="0.22"></path>'
             f'<rect x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(wh)}" fill="#FFC890" stroke="{INK}" stroke-width="2.4"></rect>'
             + "".join(f'<path d="M{f(wx + ww * t)} {f(wy)} L {f(wx + ww * t)} {f(wy + wh)}" stroke="#2A2228" stroke-width="4"></path>' for t in (0.25, 0.5, 0.75)))
    dx, dw = w * 0.16, w * 0.22
    o.append(f'<rect x="{f(dx)}" y="{f(h * 0.2)}" width="{f(dw)}" height="{f(b - h * 0.2)}" fill="#4A3020" stroke="{INK}" stroke-width="3"></rect>'
             + "".join(f'<rect x="{f(dx - 4)}" y="{f(h * 0.2 + (b - h * 0.2) * t)}" width="{f(dw + 8)}" height="{f(h * 0.03)}" fill="#5A5A60" stroke="{INK}" stroke-width="1.6"></rect>' for t in (0.15, 0.5, 0.85))
             + f'<rect x="{f(dx - 18)}" y="{f(h * 0.5)}" width="{f(dw + 36)}" height="{f(h * 0.05)}" fill="#3A2A1A" stroke="{INK}" stroke-width="2.2"></rect>')
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#2A2228" stroke="{INK}" stroke-width="2"></rect>')
    o.append(lamp_glow(w * 0.48, b - 10, h * 0.3, f"{p}lw", op=0.35) + A.lamp(w * 0.48, b - 2, max(0.5, h / 380)))
    return "".join(o)

def tutor(p, w, h, seed):
    """The law is become our tutor to bring us unto Christ: a street of a Greek town in the morning, an old household slave
    (the tutor, grey-bearded, a short grey cloak, his staff) walking a boy to school, the boy with his writing tablet; the
    school's door open at the right."""
    bg, b = _street(w, h, seed, "dawn")
    o = [_defs(p), bg]
    s = fit(b, max(h * 0.2, b - 230))
    dx, dw = w * 0.78, w * 0.13
    o.append(f'<rect x="{f(dx - 10)}" y="{f(b - 180 * s)}" width="{f(dw + 20)}" height="{f(180 * s)}" fill="#E8DCC0" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(dx)}" y="{f(b - 150 * s)}" width="{f(dw)}" height="{f(150 * s)}" fill="#3A2A1E" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(dx + dw * 0.1)}" y="{f(b - 172 * s)}" width="{f(dw * 0.8)}" height="{f(16 * s)}" fill="#2A3A2A" stroke="{INK}" stroke-width="1.4"></rect>')
    staff = '<path d="M50 -176 L 46 4" stroke="#5A3A22" stroke-width="5" stroke-linecap="round"></path>'
    o.append(robed(p, w * 0.32, b, s, "#8A8478", hair="#B8B2A6", beard="#C8C2B6", mantle="#6A645E", belt="#4A4038", up=[(-22, -158), (-40, -120), (-54, -100)], extra=staff, flip=True))
    tablet = '<rect x="-40" y="-108" width="22" height="16" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.4"></rect><rect x="-37" y="-105" width="16" height="10" fill="#C8A060"></rect>'
    o.append(boy(p, w * 0.32 + 52 * s, b, s * 0.66, cloth="#E8DCC0", hair="#3A2214", flip=True, up=[(-22, -158), (-34, -126), (-36, -104)], extra=tablet))
    o.append(plate_label(dx + dw / 2, b - 184 * s, "THE SCHOOL", "#3A2A1E", 8.5, halo_="#F3E8C8"))
    return "".join(o)

def one_in_christ(w, h):
    """Neither Jew nor Greek, neither bond nor free, no male and female: a plate — three pairs of figures in outline (a Jew
    in a headcloth and a bareheaded Greek; a bondservant bearing a jar and a free man with a scroll; a man and a woman),
    and over all six one band of gold light."""
    o = [plate_bg(w, h, "GALATIANS 3:28 · YE ALL ARE ONE"), mk.defs("oc", *ALL)]
    base, top = h * 0.84, h * 0.36
    sc = (base - top) / 205
    pairs = [("JEW", "GREEK"), ("BOND", "FREE"), ("MALE", "FEMALE")]
    jar = '<path d="M-30 -196 C -40 -196 -42 -176 -34 -170 L -26 -170 C -18 -176 -20 -196 -30 -196 Z" fill="#163A56" stroke="#8FD0E2" stroke-width="2"></path>'
    scrl = '<rect x="22" y="-110" width="10" height="26" fill="#163A56" stroke="#8FD0E2" stroke-width="2"></rect>'
    for i, (a, bb) in enumerate(pairs):
        cx = w * (0.2 + 0.3 * i)
        xa, xb = cx - 34 * sc, cx + 34 * sc
        ea = A.headcloth("#163A56", cord=None).replace('stroke="#0D0D0F"', f'stroke="{CY}"') if i == 0 else (jar if i == 1 else "")
        eb = scrl if i == 1 else ""
        o.append(mk.person("oc", round(xa), round(base), round(sc, 3), body="#1E4A6A", cloth="#163A56", kind="Tunic", stroke=CY, sw=2.4,
                           up=[(-22, -158), (-28, -180), (-30, -190)] if i == 1 else None, extra=ea))
        o.append(mk.person("oc", round(xb), round(base), round(sc * (0.94 if i == 2 else 1), 3), body="#1E4A6A", cloth="#24506E", woman=i == 2, kind="Robe" if i == 2 else "Tunic",
                           stroke=CY, sw=2.4, flip=True, extra=eb))
        o.append(label(xa, min(base + 18, h - 6), a, CY, 9.5) + label(xb, min(base + 18, h - 6), bb, CY, 9.5))
        if i < 2: o.append(f'<path d="M{f(cx + w * 0.15)} {f(top)} L {f(cx + w * 0.15)} {f(base)}" stroke="#2C5A7A" stroke-width="1.4" stroke-dasharray="5 5"></path>')
    o.append(halo(w * 0.5, top - h * 0.06, h * 0.2, "#FFE680", 0.35)
             + f'<rect x="{f(w * 0.05)}" y="{f(top - h * 0.12)}" width="{f(w * 0.9)}" height="{f(h * 0.06)}" fill="{GOLD}" opacity="0.92"></rect>'
             + label(w * 0.5, top - h * 0.075, "ONE IN CHRIST JESUS", "#12113A", 11))
    return "".join(o)

# ---- the cover ------------------------------------------------------------------------------------------------------------
def galatia_dawn(w, h, seed):
    """The hill country of Galatia at sunrise: a walled town on its hill (Iconium on the road), the road winding up to it,
    the high plain beyond."""
    o = [sky(w, h, "#2A1E3A", "#FFB07A"), halo(w * 0.66, h * 0.42, h * 0.5, "#FFD08A", 0.5),
         f'<circle cx="{f(w * 0.66)}" cy="{f(h * 0.42)}" r="{f(h * 0.06)}" fill="#FFE6A0"></circle>',
         hills(w, h, h * 0.4, seed, color="#6A5A7A", amp=20, step=110), hills(w, h, h * 0.5, seed + 1, color="#8A6A6A", amp=14, step=90),
         town_hill(w * 0.4, h * 0.66, w * 0.3, h * 0.28, seed, color="#9A7A5A"),
         ground(w, h, h * 0.66, "#B08A5A", dy=0),
         f'<path d="M{f(w * 0.9)} {f(h + 10)} C {f(w * 0.8)} {f(h * 0.86)} {f(w * 0.56)} {f(h * 0.76)} {f(w * 0.46)} {f(h * 0.66)}" stroke="#D8B88A" stroke-width="{f(h * 0.05)}" fill="none"></path>',
         birds(5, w * 0.1, w * 0.6, h * 0.14, h * 0.3, seed)]
    return "".join(o)

def town_hill(cx, base, wd, hh, seed, color="#8A6A4A", lit=False):
    """A town of Galatia or Judæa on its hill: the hill, the wall with its towers and gate, the houses within (no temple)."""
    return (f'<path d="M{f(cx - wd)} {f(base)} C {f(cx - wd * 0.5)} {f(base - hh)} {f(cx + wd * 0.5)} {f(base - hh)} {f(cx + wd)} {f(base)} Z" fill="{color}" stroke="{INK}" stroke-width="2.2"></path>'
            + walls(cx - wd * 0.62, cx + wd * 0.62, base - hh * 0.5, hh * 0.36, seed, lit=lit, towers=3))

# ---- Galatians 3 (more) ---------------------------------------------------------------------------------------------------
ABRAHAM_ROBE = "#2C4A7A"                                                                   # Genesis: slate-blue robe, grey hair and beard

def abraham_r(p, x, y, s, flip=False, up=None, extra=""):
    return robed(p, x, y, s, ABRAHAM_ROBE, hair="#B8B2A6", beard="#B8B2A6", mantle="#1F3458", belt="#5A4A3A", flip=flip, up=up, extra=extra)

def abraham_stars(p, w, h, seed):
    """Abraham believed God: Abraham standing before his tent at night, his hand lifted to a sky crowded with stars (look
    now toward heaven, and number the stars — Genesis 15:5), the tent dark behind him, the hills."""
    b = h * 0.92
    o = [_defs(p), sky(w, h, "#05051A", "#2A2050"),
         f'<path d="M-10 {f(h * 0.6)} C {f(w * 0.3)} {f(h * 0.2)} {f(w * 0.6)} {f(h * 0.1)} {f(w + 10)} {f(-10)}" fill="none" stroke="#5B2470" stroke-width="{f(h * 0.3)}" opacity="0.35"></path>',
         mk.stars(260, w, h * 0.7, seed), mk.stars(50, w, h * 0.6, seed + 1, color="#FFE680"),
         hills(w, h, h * 0.66, seed, color="#1A1A3A", amp=12, step=90), ground(w, h, h * 0.74, "#2A2440", dy=0)]
    o.append(black_tent(w * 0.66, b - 2, min(w * 0.4, h * 1.1), h * 0.36))
    s = fit(b, max(h * 0.2, b - 230))
    o.append(abraham_r(p, w * 0.3, b, s, up=[(-22, -158), (-40, -190), (-52, -222)]))
    return "".join(o)

def far_crosses(w, h, seed):
    """Cursed is every one that hangeth on a tree: Golgotha from far off under a darkened sky, a dull red rim low behind the
    hill; three crosses on its top, small and dark against it (nothing in detail, no wounds), no one near."""
    o = [sky(w, h, "#05050E", "#5A1E1A"), halo(w * 0.56, h * 0.5, h * 0.5, "#8A2A1A", 0.35)]
    hx = w * 0.56
    o.append(f'<path d="M{f(hx - w * 0.56)} {f(h * 0.82)} C {f(hx - w * 0.24)} {f(h * 0.52)} {f(hx + w * 0.2)} {f(h * 0.5)} {f(hx + w * 0.56)} {f(h * 0.82)} Z" fill="#1A1418" stroke="{INK}" stroke-width="2"></path>')
    k = max(0.35, h / 520)
    for dx, tall in ((-0.1, 0.88), (0, 1.0), (0.1, 0.88)):
        x = hx + dx * w; base = h * 0.56 + abs(dx) * h * 0.06; ch = 110 * k * tall
        o.append(f'<path d="M{f(x)} {f(base)} L {f(x)} {f(base - ch)} M{f(x - 26 * k)} {f(base - ch * 0.78)} L {f(x + 26 * k)} {f(base - ch * 0.78)}" stroke="#0D0D0F" stroke-width="{f(5 * k + 1)}"></path>')
    o.append(ground(w, h, h * 0.84, "#141014", dy=0))
    return "".join(o)
