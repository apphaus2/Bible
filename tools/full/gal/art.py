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
from gal.common import TITUS_LOOK, BARNABAS, JAMES_LORD, HAGAR, SARAH
from oba.minor import grain
from mat.art5 import leaven
from ecc.art import race
from jer.art10 import yoke_off
from jhn.art2 import reaping

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

def art(fn, *a, **k):
    """A panel's drawing as fn(w, h): fn(p, w, h, seed, ...) when the first argument is a prefix string, else fn(w, h, ...);
    clipped to its own w × h so a glow or a ray never spills up behind the words."""
    import zlib
    def draw(w, h):
        svg = fn(*a[:1], w, h, *a[1:], **k) if a and isinstance(a[0], str) else fn(w, h, *a, **k)
        uid = f"gc{zlib.crc32(repr((fn.__name__, a, sorted(k.items()), round(w), round(h))).encode()) % 10 ** 8}"
        return (f'<defs><clipPath id="{uid}"><rect x="0" y="0" width="{f(w)}" height="{f(h)}"></rect></clipPath></defs>'
                f'<g clip-path="url(#{uid})">{svg}</g>')
    return draw

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

# ---- Galatians 4 ----------------------------------------------------------------------------------------------------------
def hall(w, h, b, seed):
    """The hall of a great house: a painted wall with a red dado, two columns, a doorway onto the court, a tiled floor."""
    o = [bgr(w, h, "#E8D8B8"), f'<rect x="-10" y="{f(b - h * 0.32)}" width="{f(w + 20)}" height="{f(h * 0.32)}" fill="#9A3A2A"></rect>',
         f'<path d="M-10 {f(b - h * 0.32)} L {f(w + 10)} {f(b - h * 0.32)}" stroke="{INK}" stroke-width="2"></path>',
         f'<rect x="-10" y="{f(h * 0.05)}" width="{f(w + 20)}" height="{f(h * 0.05)}" fill="#C8A060" stroke="{INK}" stroke-width="2"></rect>']
    for x in (0.08, 0.92):
        cw = w * 0.045
        o.append(f'<rect x="{f(w * x - cw / 2)}" y="{f(h * 0.1)}" width="{f(cw)}" height="{f(b - h * 0.1)}" fill="#F3EFE6" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="{f(w * x - cw * 0.75)}" y="{f(h * 0.1)}" width="{f(cw * 1.5)}" height="{f(h * 0.03)}" fill="#E8DCC0" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<rect x="{f(w * 0.44)}" y="{f(h * 0.2)}" width="{f(w * 0.12)}" height="{f(b - h * 0.2)}" fill="#8FD0E2" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(w * 0.44)}" y="{f(b - h * 0.16)}" width="{f(w * 0.12)}" height="{f(h * 0.16)}" fill="#C8B898"></rect>')
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#B8A07A" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<path d="M{f(x)} {f(b)} L {f(x - 20)} {f(h + 10)}" stroke="#9A8460" stroke-width="1.2"></path>' for x in range(0, int(w) + 40, 40)))
    return "".join(o)

def heir_child(p, w, h, seed):
    """So long as the heir is a child, he differeth nothing from a bondservant, but is under guardians and stewards: in the
    hall of his father's house, the boy heir in a white tunic with a purple border, a guardian's hand on his shoulder, the
    steward with his tablet and keys, and a bondservant going by with a water-jar."""
    b = h * 0.92
    o = [_defs(p), hall(w, h, b, seed)]
    s = fit(b, max(h * 0.18, b - 230))
    keys = '<path d="M14 -100 L 14 -84 M10 -84 L 18 -84 M12 -92 L 18 -92" stroke="#C8963E" stroke-width="2.4"></path><circle cx="14" cy="-104" r="4" fill="none" stroke="#C8963E" stroke-width="2"></circle>'
    tablet = '<rect x="-74" y="-170" width="26" height="20" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.4"></rect><rect x="-71" y="-167" width="20" height="14" fill="#C8A060"></rect>'
    bx = w * 0.46
    o.append(robed(p, bx - 120 * s, b, s, "#5A6A7A", head="#2A3A4A", cord="#C8963E", beard="#2A1A10", mantle="#3A4A5A", flip=True, up=[(-22, -158), (-48, -164), (-60, -160)], extra=tablet + keys))
    border = '<path d="M-30 -2 L 30 -2" stroke="#6A1A6A" stroke-width="5"></path>'
    o.append(boy(p, bx, b, s * 0.62, cloth="#F3EFE6", hair="#3A2214", extra=border))
    o.append(robed(p, bx + 92 * s, b, s, "#3A3A5A", head="#E8E2D6", cord="#3A2A1A", beard="#B8B2A6", mantle="#2A2A44", up=[(-22, -158), (-50, -136), (-76, -106)]))
    jar = '<path d="M28 -214 C 16 -214 12 -190 22 -182 L 34 -182 C 44 -190 40 -214 28 -214 Z" fill="#B8603A" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(robed(p, w * 0.84, b, s * 0.94, "#8A7A5A", hair="#1A1210", belt="#4A3A2A", up=[(22, -158), (30, -184), (28, -198)], extra=jar))
    o.append("".join(plate_label(x, h * 0.05 + 12, t, "#12113A", 9, halo_="#F3EFE6") for x, t in
                     ((bx - 120 * s, "A STEWARD"), (bx, "THE HEIR"), (bx + 92 * s, "A GUARDIAN"), (w * 0.84, "A BONDSERVANT"))))
    return "".join(o)

def fulness_star(p, w, h, seed):
    """When the fulness of the time came, God sent forth his Son, born of a woman: Bethlehem asleep on its hill under the
    stars, one star standing over a house, its light falling straight down on the roof (no one drawn)."""
    o = [night(w, h, seed, n=80, top="#05051A", bot="#2A2050"), hills(w, h, h * 0.62, seed, color="#1E1838", amp=14, step=80)]
    o.append(f'<path d="M{f(w * 0.2)} {f(h * 0.7)} C {f(w * 0.36)} {f(h * 0.5)} {f(w * 0.7)} {f(h * 0.48)} {f(w * 0.86)} {f(h * 0.7)} Z" fill="#2A2440" stroke="{INK}" stroke-width="2"></path>')
    hx = w * 0.56
    o.append(f'<path d="M{f(hx - w * 0.03)} {f(h * 0.18)} L {f(hx + w * 0.03)} {f(h * 0.18)} L {f(hx + w * 0.05)} {f(h * 0.6)} L {f(hx - w * 0.05)} {f(h * 0.6)} Z" fill="#FFF4C2" opacity="0.22"></path>')
    o.append(houses(w, h, h * 0.66, seed, x0=w * 0.3, x1=w * 0.78, hmin=0.08, hmax=0.14, lit=True))
    o.append(star_of(hx, h * 0.16, max(10, h * 0.05), uid=f"{p}st"))
    o.append(ground(w, h, h * 0.8, "#141024", dy=0))
    return "".join(o)

def _moon(x, y, r, phase, lit="#F3EFE6", dark="#1E3A5A"):
    """A moon of the given phase (0 new … 0.5 full … 1 new): a disc and its lit part."""
    o = f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{dark}" stroke="{CY}" stroke-width="1"></circle>'
    if phase in (0, 1): return o
    k = math.cos(phase * 2 * math.pi)                 # 1 new … -1 full
    right = phase < 0.5
    sweep = 1 if right else 0
    rx = abs(k) * r
    inner = 0 if (k > 0) == right else 1
    d = f"M{f(x)} {f(y - r)} A {f(r)} {f(r)} 0 0 {sweep} {f(x)} {f(y + r)} A {f(rx)} {f(r)} 0 0 {inner if right else 1 - inner} {f(x)} {f(y - r)} Z"
    return o + f'<path d="{d}" fill="{lit}"></path>'

def seasons(w, h):
    """Ye observe days, and months, and seasons, and years: a plate — the sun in the middle, the ring of the twelve new
    moons and their phases about it, the four seasons as quarters of the year, the round of the days marked on the rim."""
    o = [plate_bg(w, h, "GALATIANS 4:9–10 · THE WEAK AND BEGGARLY RUDIMENTS")]
    cx, cy = w * 0.5, h * 0.56
    R = min(w * 0.3, (h - 60) * 0.42)
    cols = ("#5E8F26", "#E8B830", "#C8682E", "#5A7A9A")
    for i, c in enumerate(cols):
        a0, a1 = math.radians(-90 + 90 * i), math.radians(-90 + 90 * (i + 1))
        x0, y0, x1, y1 = cx + R * 1.1 * math.cos(a0), cy + R * 1.1 * math.sin(a0), cx + R * 1.1 * math.cos(a1), cy + R * 1.1 * math.sin(a1)
        o.append(f'<path d="M{f(cx)} {f(cy)} L {f(x0)} {f(y0)} A {f(R * 1.1)} {f(R * 1.1)} 0 0 1 {f(x1)} {f(y1)} Z" fill="{c}" opacity="0.28" stroke="{c}" stroke-width="1.4"></path>')
    for i in range(60):
        a = math.radians(-90 + 6 * i)
        o.append(f'<path d="M{f(cx + R * 1.1 * math.cos(a))} {f(cy + R * 1.1 * math.sin(a))} L {f(cx + R * (1.16 if i % 5 == 0 else 1.13) * math.cos(a))} {f(cy + R * (1.16 if i % 5 == 0 else 1.13) * math.sin(a))}" stroke="{CY}" stroke-width="1.2"></path>')
    for i in range(12):
        a = math.radians(-90 + 30 * i + 15)
        o.append(_moon(cx + R * 0.78 * math.cos(a), cy + R * 0.78 * math.sin(a), R * 0.1, (i + 0.5) / 12))
    o.append(halo(cx, cy, R * 0.4, "#FFE680", 0.5) + f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R * 0.22)}" fill="{GOLD}" stroke="{INK}" stroke-width="1.6"></circle>'
             + rays(cx, cy, 16, R * 0.26, R * 0.4, GOLD, 0.6, 2))
    lx = cx + R * 1.3
    o.append(tag(cx + R * 1.12, cy - R * 0.2, "DAYS", w * 0.86, cy - R * 0.8, color=CY) + tag(cx + R * 0.78 * math.cos(math.radians(-45)), cy + R * 0.78 * math.sin(math.radians(-45)), "MONTHS", w * 0.86, cy - R * 0.3, color=CY)
             + tag(cx - R * 0.9, cy + R * 0.4, "SEASONS", w * 0.14, cy + R * 0.7, color=CY) + tag(cx - R * 1.1, cy - R * 0.1, "YEARS", w * 0.14, cy - R * 0.6, color=CY))
    return "".join(o)

def welcomed(p, w, h, seed):
    """Ye received me as an angel of God, even as Christ Jesus: the gate of a town of Galatia, Paul come in weak, leaning on
    his staff (his infirmity is told only in the words), the Galatians coming out to take him in — a man's arm held out, a
    woman bringing a cup."""
    bg, b = _gate(w, h, seed)
    o = [_defs(p), bg]
    s = fit(b, max(h * 0.18, b - 230))
    staff = '<path d="M-52 -176 L -46 4" stroke="#5A3A22" stroke-width="5" stroke-linecap="round"></path>'
    o.append(paul_fig(p, w * 0.16, b, s, up=[(-22, -158), (-38, -124), (-48, -96)], extra=staff))
    o.append(gentile(p, w * 0.32, b, s, 0, up=[(-22, -158), (-48, -146), (-72, -140)]))
    cup = '<path d="M-60 -150 L -48 -150 L -50 -138 L -58 -138 Z" fill="#C8963E" stroke="#0D0D0F" stroke-width="1.4"></path>'
    o.append(robed(p, w * 0.44, b, s * 0.94, "#5A7A7A", woman=True, veil="#1F3A3A", up=[(-22, -158), (-44, -152), (-56, -148)], extra=cup))
    o.append(gentile(p, w * 0.56, b, s * 0.98, 1) + gentile(p, w * 0.66, b, s * 0.94, 0, woman=True) + gentile(p, w * 0.76, b, s * 0.97, 2))
    return "".join(o)

def two_sons(p, w, h, seed):
    """Abraham had two sons, one by the handmaid, and one by the freewoman: before Abraham's tents, Hagar (cerulean, a
    cerulean veil) with Ishmael, a lad, at the left; Sarah (her mulberry veil, grey hair) with the little boy Isaac at the
    right; the tents between them."""
    b = h * 0.92
    o = [_defs(p), sky(w, h, "#8FD0E2", "#F3E8C8"), hills(w, h, h * 0.5, seed, color="#B8A07A", amp=12, step=90), ground(w, h, h * 0.58, "#C8A06A", dy=0)]
    o.append(black_tent(w * 0.5, h * 0.62, w * 0.26, h * 0.2) + black_tent(w * 0.74, h * 0.6, w * 0.16, h * 0.13, lit=False))
    s = fit(b, max(h * 0.18, b - 230))
    o.append(hagar_r(p, w * 0.14, b, s, flip=True) + boy(p, w * 0.14 + 54 * s, b, s * 0.72, cloth="#8A6A3A", hair="#0D0D0F", flip=True))
    o.append(sarah_r(p, w * 0.86, b, s) + boy(p, w * 0.86 - 48 * s, b, s * 0.5, cloth="#E8DCC0", hair="#5A3A22"))
    o.append(plate_label(w * 0.17, h * 0.08, "THE HANDMAID · HAGAR · ISHMAEL", "#12113A", 9, halo_="#F3EFE6")
             + plate_label(w * 0.82, h * 0.08, "THE FREEWOMAN · SARAH · ISAAC", "#12113A", 9, halo_="#F3EFE6"))
    return "".join(o)

def _portrait(tok, x, y, wd, hh, uid, light="#FFE680", ground_=("#3A2A3A", "#8A5A4A"), flip=False):
    """A shaded profile face set in a framed square (a portrait inset on a plate)."""
    s = min(wd / 300, (hh + 10) / 380)
    fx = x + wd - (300 * s - 40 * s) if flip else x - 40 * s
    return (f'<defs><clipPath id="{uid}c"><rect x="{f(x)}" y="{f(y)}" width="{f(wd)}" height="{f(hh)}"></rect></clipPath>'
            f'<radialGradient id="{uid}g" cx="0.7" cy="0.3" r="0.9"><stop offset="0" stop-color="{light}"></stop><stop offset="0.45" stop-color="{ground_[1]}"></stop>'
            f'<stop offset="1" stop-color="{ground_[0]}"></stop></radialGradient></defs>'
            f'<g clip-path="url(#{uid}c)"><rect x="{f(x)}" y="{f(y)}" width="{f(wd)}" height="{f(hh)}" fill="url(#{uid}g)"></rect>'
            + mk.face(tok, f(fx + (300 * s if flip else 0)), f(y + hh - 380 * s + 6), round(s, 3), flip=flip) + '</g>'
            f'<rect x="{f(x)}" y="{f(y)}" width="{f(wd)}" height="{f(hh)}" fill="none" stroke="{INK}" stroke-width="3"></rect>')

def sinai_bondage(w, h, seed):
    """One from mount Sinai, bearing children unto bondage, which is Hagar; she answereth to the Jerusalem that now is: at
    the left Hagar's face in a framed portrait; mount Sinai in Arabia under a dark, stormy sky; at its foot the walls of the
    Jerusalem that now is, dark, a chain across the gate."""
    o = [sky(w, h, "#1A1424", "#6A2A2A"), clouds(w, h * 0.12, seed, n=5, color="#2A2030", op=0.85, h=h)]
    o.append(E4.sinai(w * 0.62, h * 0.86, w * 0.56, h * 0.62, seed, fire=False))
    o.append(ground(w, h, h * 0.84, "#3A2A2A", dy=0))
    o.append(walls(w * 0.74, w * 0.98, h * 0.9, h * 0.14, seed, color="#6A5A5A", towers=2))
    pw = min(w * 0.3, h * 0.7)
    o.append(_portrait(HAGAR, w * 0.03, h * 0.12, pw, h * 0.8, f"hp{seed}", light="#9FB8D8", ground_=("#14202E", "#2A4A6A")))
    o.append(plate_label(w * 0.03 + pw / 2, h * 0.08, "HAGAR · THE HANDMAID", "#9FD0FF", 10, halo_="#1A1424")
             + plate_label(w * 0.62, h * 0.08, "MOUNT SINAI IN ARABIA", "#FFB89A", 10, halo_="#1A1424")
             + plate_label(w * 0.86, h * 0.64, "THE JERUSALEM THAT NOW IS", "#FFB89A", 9, halo_="#1A1424"))
    return "".join(o)

def jerusalem_above(w, h, seed):
    """The Jerusalem that is above is free, which is our mother: a city of light above the clouds in a sky of gold and
    white (walls, gates and towers of light — no one drawn, God not drawn); at the right Sarah's face in a framed portrait
    (Rejoice, thou barren)."""
    o = [sky(w, h, "#3A2A6A", "#FFE6A0"), halo(w * 0.4, h * 0.42, max(w, h) * 0.5, "#FFFFFF", 0.6), rays(w * 0.4, h * 0.42, 30, h * 0.1, max(w, h), "#FFF4C2", 0.25, 4)]
    cx, cb, cw = w * 0.4, h * 0.6, w * 0.5
    o.append(walls(cx - cw / 2, cx + cw / 2, cb, h * 0.26, seed, color="#FFF4D8", towers=4).replace('fill="#FFC14D"', 'fill="#FFFFFF"'))
    o.append(halo(cx, cb - h * 0.12, cw * 0.5, "#FFFFFF", 0.55) + clouds(w, h * 0.62, seed, n=7, color="#FFFDF4", op=0.95, h=h))
    o.append(f'<rect x="-10" y="{f(h * 0.72)}" width="{f(w + 20)}" height="{f(h)}" fill="#FFF8E6" opacity="0.9"></rect>')
    pw = min(w * 0.3, h * 0.7)
    o.append(_portrait(SARAH, w * 0.97 - pw, h * 0.12, pw, h * 0.8, f"sp{seed}", light="#FFFFFF", ground_=("#8A5A4A", "#E8C08A"), flip=True))
    o.append(plate_label(w * 0.97 - pw / 2, h * 0.08, "SARAH · THE FREEWOMAN", "#7A3A2A", 10, halo_="#FFF8E6")
             + plate_label(w * 0.4, h * 0.08, "THE JERUSALEM THAT IS ABOVE", "#7A3A2A", 10, halo_="#FFF8E6"))
    return "".join(o)

# ---- Galatians 5 ----------------------------------------------------------------------------------------------------------
def dark_street(w, h, seed):
    """The works of the flesh: a street of a city at night, every door shut and every window dark, a cup overturned and a
    broken jar on the paving, a torch gone out in its bracket — no one in it."""
    b = h * 0.94
    o = [sky(w, h, "#05050E", "#1E1430"), mk.stars(24, w, h * 0.3, seed), houses(w, h, h * 0.66, seed, hmin=0.3, hmax=0.46, shut=True, color=("#4A4250", "#3E3848", "#544C5A", "#463E4E")),
         pavement(w, h, h * 0.66, color="#2E2834", line="#3E3644")]
    jx, jy = w * 0.36, h * 0.86
    o.append(f'<path d="M{f(jx - 24)} {f(jy)} C {f(jx - 30)} {f(jy - 30)} {f(jx - 10)} {f(jy - 40)} {f(jx + 4)} {f(jy - 30)} L {f(jx)} {f(jy - 14)} L {f(jx + 10)} {f(jy)} Z" fill="#5A3A2E" stroke="{INK}" stroke-width="1.8"></path>'
             f'<path d="M{f(jx + 26)} {f(jy + 2)} L {f(jx + 40)} {f(jy - 10)} L {f(jx + 48)} {f(jy + 4)} Z" fill="#5A3A2E" stroke="{INK}" stroke-width="1.6"></path>')
    cx_, cy_ = w * 0.62, h * 0.9
    o.append(f'<path d="M{f(cx_ - 14)} {f(cy_)} L {f(cx_ + 12)} {f(cy_ - 6)} L {f(cx_ + 14)} {f(cy_ + 4)} L {f(cx_ - 12)} {f(cy_ + 8)} Z" fill="#8A6A2A" stroke="{INK}" stroke-width="1.4"></path>'
             f'<path d="M{f(cx_ + 14)} {f(cy_ + 2)} C {f(cx_ + 40)} {f(cy_ + 4)} {f(cx_ + 60)} {f(cy_ + 10)} {f(cx_ + 80)} {f(cy_ + 6)}" stroke="#3A1A2A" stroke-width="6" opacity="0.7" fill="none"></path>')
    tx = w * 0.84
    o.append(f'<rect x="{f(tx - 3)}" y="{f(h * 0.4)}" width="6" height="{f(h * 0.1)}" fill="#2A2228" stroke="{INK}" stroke-width="1.4"></rect>'
             f'<path d="M{f(tx - 8)} {f(h * 0.4)} L {f(tx + 8)} {f(h * 0.4)} L {f(tx + 5)} {f(h * 0.35)} L {f(tx - 5)} {f(h * 0.35)} Z" fill="#1A1414" stroke="{INK}" stroke-width="1.4"></path>'
             + smoke(tx, h * 0.33, 3, seed, color="#4A4048", op=0.4))
    return "".join(o)

FRUITS = ("LOVE", "JOY", "PEACE", "LONGSUFFERING", "KINDNESS", "GOODNESS", "FAITHFULNESS", "MEEKNESS", "SELF-CONTROL")

def fruit_tree(w, h, seed=1, title=True):
    """The fruit of the Spirit: a botanical plate on cream paper — one tree, its trunk and boughs, its leaves, and nine
    fruits hanging in it, each drawn and named with a leader line to the margin (love, joy, peace, longsuffering, kindness,
    goodness, faithfulness, meekness, self-control); the ground and its roots below."""
    r = random.Random(seed)
    o = [bgr(w, h, "#F3EAD0"), f'<rect x="8" y="8" width="{f(w - 16)}" height="{f(h - 16)}" fill="none" stroke="#7A5A3A" stroke-width="1.4"></rect>']
    if title:
        o.append(f'<rect x="8" y="8" width="{f(w - 16)}" height="24" fill="#3A5A2A"></rect>' + label(20, 25, "GALATIANS 5:22–23 · THE FRUIT OF THE SPIRIT · ONE TREE, NINE FRUITS", "#F3EAD0", 10, "start"))
    top = 40 if title else 14
    cx, gy = w * 0.5, h - 26
    ch = gy - top
    k = ch / 300
    # roots and ground
    o.append(f'<path d="M{f(cx - w * 0.3)} {f(gy)} L {f(cx + w * 0.3)} {f(gy)}" stroke="#7A5A3A" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(cx + dx * k)} {f(gy)} C {f(cx + dx * 1.4 * k)} {f(gy + 8)} {f(cx + dx * 2 * k)} {f(gy + 12)} {f(cx + dx * 2.6 * k)} {f(gy + 14)}" stroke="#7A5A3A" stroke-width="1.6" fill="none"></path>' for dx in (-20, -8, 8, 20)))
    # trunk and boughs
    o.append(f'<path d="M{f(cx - 14 * k)} {f(gy)} C {f(cx - 12 * k)} {f(gy - 60 * k)} {f(cx - 10 * k)} {f(gy - 100 * k)} {f(cx - 8 * k)} {f(gy - 120 * k)} '
             f'L {f(cx + 8 * k)} {f(gy - 120 * k)} C {f(cx + 10 * k)} {f(gy - 100 * k)} {f(cx + 12 * k)} {f(gy - 60 * k)} {f(cx + 16 * k)} {f(gy)} Z" fill="#6A4A2A" stroke="{INK}" stroke-width="2"></path>')
    for dx, dy in ((-80, -190), (-50, -230), (0, -250), (50, -230), (80, -190), (-100, -150), (100, -150)):
        o.append(f'<path d="M{f(cx)} {f(gy - 116 * k)} C {f(cx + dx * 0.3 * k)} {f(gy - 150 * k)} {f(cx + dx * 0.7 * k)} {f(gy + dy * 0.85 * k)} {f(cx + dx * k)} {f(gy + dy * k)}" stroke="#6A4A2A" stroke-width="{f(5 * k)}" fill="none" stroke-linecap="round"></path>')
    # canopy of leaves
    cy = gy - 200 * k
    for _ in range(46):
        a = r.uniform(0, 2 * math.pi); rr = r.uniform(0.2, 1.0)
        lx, ly = cx + math.cos(a) * rr * 130 * k, cy + math.sin(a) * rr * 80 * k
        o.append(f'<ellipse cx="{f(lx)}" cy="{f(ly)}" rx="{f(16 * k)}" ry="{f(8 * k)}" transform="rotate({r.randint(-60, 60)} {f(lx)} {f(ly)})" fill="{r.choice(("#3F8A44", "#2E6B3A", "#5E8F26", "#4E7A3A"))}" stroke="#1E3A1E" stroke-width="1"></ellipse>')
    # nine fruits, labelled to the margins
    # fruits 1–5 down the left of the crown, 6–9 down the right, so the leader lines run out to the margins uncrossed
    spots = [(-40, -78), (-96, -50), (-118, -10), (-84, 30), (-34, 50), (40, -74), (98, -44), (114, 0), (64, 40)]
    colors = ("#D7261E", "#FFB020", "#7AB8E0", "#8A3A8A", "#E8682E", "#C8963E", "#B8202E", "#E8C8A0", "#5E8F26")
    fr = max(6, 11 * k)
    lab_w = 150                                                       # room for the longest name at 11 px
    for i, ((dx, dy), c) in enumerate(zip(spots, colors)):
        fx, fy = cx + dx * k, cy + dy * k
        o.append(f'<path d="M{f(fx)} {f(fy - fr)} l 0 {f(-5 * k)}" stroke="#4A3A2A" stroke-width="1.6"></path>'
                 f'<circle cx="{f(fx)}" cy="{f(fy)}" r="{f(fr)}" fill="{c}" stroke="{INK}" stroke-width="1.8"></circle>'
                 f'<ellipse cx="{f(fx - fr * 0.35)}" cy="{f(fy - fr * 0.35)}" rx="{f(fr * 0.28)}" ry="{f(fr * 0.18)}" fill="#FFFFFF" opacity="0.55"></ellipse>')
        left = i < 5
        j, n = (i, 5) if left else (i - 5, 4)
        ty = top + 24 + (gy - top - 70) * (j + 0.5) / n
        ex = 22 + lab_w if left else w - 22 - lab_w
        sx_ = fx + (-1 if left else 1) * (fr + 2)
        o.append(f'<path d="M{f(sx_)} {f(fy)} L {f(ex + (14 if left else -14))} {f(ty)} L {f(ex + (4 if left else -4))} {f(ty)}" stroke="#7A5A3A" stroke-width="1.2" fill="none"></path>'
                 f'<circle cx="{f(sx_)}" cy="{f(fy)}" r="2" fill="#7A5A3A"></circle>'
                 + label(22 if left else w - 22, ty + 4, f"{i + 1} · {FRUITS[i]}", "#3A2A1A", 11, "start" if left else "end"))
    return "".join(o)

# ---- Galatians 6 ----------------------------------------------------------------------------------------------------------
def burdens(p, w, h, seed):
    """Bear ye one another's burdens: on the road, a heavy bundle slung from a pole carried on two men's shoulders; and one
    lifting the sack from the back of a man sunk to his knees under it."""
    bg, b = _road(w, h, seed)
    o = [_defs(p), bg]
    s = fit(b, max(h * 0.18, b - 230))
    x1, x2 = w * 0.18, w * 0.42
    py = b - 161 * s
    o.append(robed(p, x1, b, s, "#6A5A4A", head="#3A3A3A", beard="#2A1A10", flip=True))
    o.append(robed(p, x2, b, s, "#4A5A6A", head="#E8E2D6", beard="#6A645E"))
    o.append(f'<path d="M{f(x1 - 10 * s)} {f(py)} L {f(x2 + 10 * s)} {f(py)}" stroke="#5A3A22" stroke-width="{f(7 * s)}" stroke-linecap="round"></path>'
             f'<path d="M{f((x1 + x2) / 2 - 8 * s)} {f(py)} L {f((x1 + x2) / 2 - 14 * s)} {f(py + 30 * s)} M{f((x1 + x2) / 2 + 8 * s)} {f(py)} L {f((x1 + x2) / 2 + 14 * s)} {f(py + 30 * s)}" stroke="#8A6A3A" stroke-width="2.4"></path>'
             f'<ellipse cx="{f((x1 + x2) / 2)}" cy="{f(py + 62 * s)}" rx="{f(46 * s)}" ry="{f(36 * s)}" fill="#B8986A" stroke="{INK}" stroke-width="2.4"></ellipse>'
             f'<path d="M{f((x1 + x2) / 2 - 40 * s)} {f(py + 50 * s)} C {f((x1 + x2) / 2)} {f(py + 64 * s)} {f((x1 + x2) / 2 + 20 * s)} {f(py + 60 * s)} {f((x1 + x2) / 2 + 42 * s)} {f(py + 52 * s)}" stroke="#7A5A3A" stroke-width="2" fill="none"></path>')
    # one helped up: kneeling under his sack, another lifting it from his back
    kx = w * 0.7
    o.append(E.kneel(kx, b, s * 0.92, color="#7A5A3A", skin=SKIN))
    o.append(f'<ellipse cx="{f(kx - 4 * s)}" cy="{f(b - 128 * s)}" rx="{f(30 * s)}" ry="{f(22 * s)}" fill="#C8A878" stroke="{INK}" stroke-width="2.2"></ellipse>')
    o.append(robed(p, kx + 58 * s, b, s, "#3A6A5A", hair="#2A1A10", beard="#2A1A10", up=[(-22, -158), (-46, -146), (-58, -136)]))
    return "".join(o)

def sow_two(p, w, h, seed):
    """He that soweth unto his own flesh shall of the flesh reap corruption; he that soweth unto the Spirit shall of the
    Spirit reap eternal life: a sower in the middle of the field casting seed; at the left the field gone to thistles and
    blight under a grey sky, at the right the field green and golden under the light."""
    b = h * 0.94
    r = random.Random(seed)
    o = [_defs(p), f'<defs><linearGradient id="{p}sk" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#4A4450"></stop><stop offset="0.45" stop-color="#8A8A90"></stop>'
         f'<stop offset="0.55" stop-color="#8FD0E2"></stop><stop offset="1" stop-color="#FFF4C2"></stop></linearGradient></defs>',
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{p}sk)"></rect>', halo(w * 0.88, h * 0.16, h * 0.3, "#FFFFFF", 0.6),
         hills(w, h, h * 0.42, seed, color="#8A8A70", amp=10, step=90), ground(w, h, h * 0.52, "#7A6A4A", dy=0),
         f'<path d="M{f(w * 0.5)} {f(h * 0.52)} L {f(w + 10)} {f(h * 0.52)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.5)} {f(h + 10)} Z" fill="#6A8A3A"></path>']
    for _ in range(14):                                                # thistles and blighted stalks at the left
        x, y = r.uniform(0, w * 0.42), r.uniform(h * 0.6, h * 0.98)
        o.append(f'<path d="M{f(x)} {f(y)} l -8 -24 M{f(x)} {f(y)} l 2 -30 M{f(x)} {f(y)} l 10 -22" stroke="#4A4030" stroke-width="2.2"></path>'
                 f'<circle cx="{f(x + 2)}" cy="{f(y - 32)}" r="4" fill="#6A4A6A" stroke="{INK}" stroke-width="1"></circle>')
    o.append(grain(w * 0.58, w + 10, b, h * 0.3, seed, color="#E8C060"))
    s = fit(b, max(h * 0.18, b - 230))
    bag = '<path d="M14 -120 C 30 -116 34 -96 26 -84 C 16 -80 8 -90 10 -104 Z" fill="#C8A060" stroke="#0D0D0F" stroke-width="1.6"></path>'
    o.append(robed(p, w * 0.5, b, s, "#7A5A30", head="#E8E2D6", cord="#5A3A22", beard="#3A2A1A", up=[(-22, -158), (-48, -168), (-72, -160)], extra=bag))
    for _ in range(18):
        a = r.uniform(-2.8, -0.4); d = r.uniform(20, 90) * s
        o.append(f'<circle cx="{f(w * 0.5 - 72 * s + math.cos(a) * d)}" cy="{f(b - 160 * s - math.sin(a) * d * 0.4)}" r="1.8" fill="#E8D8A0"></circle>')
    o.append(plate_label(w * 0.2, h * 0.1, "OF THE FLESH · CORRUPTION", "#F3EFE6", 10, halo_="#3A3440")
             + plate_label(w * 0.8, h * 0.1, "OF THE SPIRIT · ETERNAL LIFE", "#5A3A1A", 10, halo_="#FFF8E6"))
    return "".join(o)

def large_letters(w, h, seed):
    """See with how large letters I write unto you with mine own hand: close over the table, the sheet of the letter —
    the scribe's even lines of small writing above, and below them the great strokes of Paul's own hand, still wet; his
    hand with the reed pen at the last stroke, the inkpot and the lamp."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#5A341E"></rect>', lamp_glow(w * 0.86, h * 0.2, max(w, h) * 0.5, f"ll{seed}", op=0.5)]
    sx, sy, sw, sh = w * 0.1, h * 0.08, w * 0.64, h * 0.86
    o.append(f'<g transform="rotate(-2 {f(sx + sw / 2)} {f(sy + sh / 2)})"><rect x="{f(sx)}" y="{f(sy)}" width="{f(sw)}" height="{f(sh)}" fill="#EADBB4" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M{f(sx + sw * 0.33)} {f(sy)} L {f(sx + sw * 0.33)} {f(sy + sh)} M{f(sx + sw * 0.66)} {f(sy)} L {f(sx + sw * 0.66)} {f(sy + sh)}" stroke="#C8B488" stroke-width="1"></path>')
    r = random.Random(seed)
    for k in range(6):                                              # the scribe's small even lines
        yy = sy + sh * (0.07 + k * 0.065); xx = sx + sw * 0.06
        while xx < sx + sw * 0.92:
            L = sw * r.uniform(0.04, 0.12)
            o.append(f'<path d="M{f(xx)} {f(yy)} l {f(min(L, sx + sw * 0.94 - xx))} 0" stroke="#4A3020" stroke-width="{f(max(1.2, h / 220))}"></path>'); xx += L + sw * 0.02
    ink = "#1A1008"
    big = sh * 0.17
    yy = sy + sh * 0.52
    shapes = {                                                      # uncial letter-shapes, one stroke-path each
        "LAMBDA": lambda x, y, B: f"M{f(x)} {f(y + B)} L {f(x + B * 0.4)} {f(y)} L {f(x + B * 0.8)} {f(y + B)}",
        "PI": lambda x, y, B: f"M{f(x - B * 0.05)} {f(y)} L {f(x + B * 0.75)} {f(y)} M{f(x + B * 0.1)} {f(y)} L {f(x + B * 0.1)} {f(y + B)} M{f(x + B * 0.6)} {f(y)} L {f(x + B * 0.6)} {f(y + B)}",
        "SIGMA": lambda x, y, B: f"M{f(x + B * 0.7)} {f(y + B * 0.15)} C {f(x + B * 0.5)} {f(y - B * 0.05)} {f(x)} {f(y)} {f(x)} {f(y + B * 0.5)} C {f(x)} {f(y + B)} {f(x + B * 0.5)} {f(y + B * 1.05)} {f(x + B * 0.7)} {f(y + B * 0.85)}",
        "OMICRON": lambda x, y, B: f"M{f(x + B * 0.35)} {f(y)} C {f(x - B * 0.05)} {f(y)} {f(x - B * 0.05)} {f(y + B)} {f(x + B * 0.35)} {f(y + B)} C {f(x + B * 0.75)} {f(y + B)} {f(x + B * 0.75)} {f(y)} {f(x + B * 0.35)} {f(y)} Z",
        "DELTA": lambda x, y, B: f"M{f(x)} {f(y + B)} L {f(x + B * 0.4)} {f(y)} L {f(x + B * 0.8)} {f(y + B)} Z",
        "EPSILON": lambda x, y, B: f"M{f(x + B * 0.65)} {f(y + B * 0.1)} C {f(x + B * 0.3)} {f(y - B * 0.05)} {f(x)} {f(y + B * 0.2)} {f(x)} {f(y + B * 0.5)} C {f(x)} {f(y + B * 0.8)} {f(x + B * 0.3)} {f(y + B * 1.05)} {f(x + B * 0.65)} {f(y + B * 0.9)} M{f(x)} {f(y + B * 0.5)} L {f(x + B * 0.45)} {f(y + B * 0.5)}",
        "TAU": lambda x, y, B: f"M{f(x - B * 0.05)} {f(y)} L {f(x + B * 0.75)} {f(y)} M{f(x + B * 0.35)} {f(y)} L {f(x + B * 0.35)} {f(y + B)}",
        "OMEGA": lambda x, y, B: f"M{f(x)} {f(y + B * 0.2)} L {f(x + B * 0.12)} {f(y + B)} L {f(x + B * 0.4)} {f(y + B * 0.55)} L {f(x + B * 0.68)} {f(y + B)} L {f(x + B * 0.8)} {f(y + B * 0.2)}",
    }
    seq = ["DELTA", "EPSILON", "PI", "LAMBDA", "OMICRON", "SIGMA", "TAU", "OMICRON"]
    for row in range(2):                                            # Paul's great strokes (letter-shapes, no words)
        xx = sx + sw * 0.08
        for j in range(5 if row == 0 else 3):
            x0, y0 = xx, yy + row * big * 1.4
            d = shapes[seq[(row * 5 + j) % len(seq)]](x0, y0, big)
            o.append(f'<path d="{d}" stroke="{ink}" stroke-width="{f(max(3, big * 0.11))}" fill="none" stroke-linecap="round" stroke-linejoin="round"></path>')
            xx += big * 1.05
    o.append('</g>')
    hx, hy = sx + sw * 0.08 + big * 1.05 * 3 + big * 0.8, sy + sh * 0.52 + big * 1.4 + big * 0.2   # the hand at the last stroke
    o.append(f'<path d="M{f(hx + 30)} {f(hy + 6)} C {f(hx + 80)} {f(hy + 20)} {f(hx + 140)} {f(hy + 40)} {f(w + 20)} {f(hy + 60)} L {f(w + 20)} {f(hy + 130)} C {f(hx + 140)} {f(hy + 110)} {f(hx + 80)} {f(hy + 80)} {f(hx + 34)} {f(hy + 50)} Z" '
             f'fill="{ROBES["paul"]}" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(hx - 4)} {f(hy + 12)} C {f(hx - 6)} {f(hy - 2)} {f(hx + 8)} {f(hy - 10)} {f(hx + 24)} {f(hy - 6)} C {f(hx + 40)} {f(hy - 2)} {f(hx + 46)} {f(hy + 18)} {f(hx + 42)} {f(hy + 36)} '
             f'C {f(hx + 38)} {f(hy + 50)} {f(hx + 20)} {f(hy + 54)} {f(hx + 8)} {f(hy + 46)} C {f(hx)} {f(hy + 40)} {f(hx - 4)} {f(hy + 26)} {f(hx - 4)} {f(hy + 12)} Z" fill="#C98E66" stroke="{INK}" stroke-width="2.2"></path>'
             f'<path d="M{f(hx + 4)} {f(hy + 22)} C {f(hx + 10)} {f(hy + 26)} {f(hx + 14)} {f(hy + 34)} {f(hx + 12)} {f(hy + 42)} M{f(hx + 20)} {f(hy + 24)} C {f(hx + 26)} {f(hy + 30)} {f(hx + 28)} {f(hy + 38)} {f(hx + 26)} {f(hy + 48)} '
             f'M{f(hx + 2)} {f(hy + 8)} C {f(hx + 10)} {f(hy + 2)} {f(hx + 18)} {f(hy + 4)} {f(hx + 22)} {f(hy + 12)}" fill="none" stroke="#7A4A2A" stroke-width="1.6"></path>'
             + reed_pen(hx - 2, hy + 4, max(0.8, h / 300), rot=-34))
    o.append(inkpot(w * 0.84, h * 0.7, max(1.0, h / 200)) + clay_lamp(w * 0.86, h * 0.36, max(1.0, h / 220)))
    return "".join(o)

def new_creation(w, h, seed):
    """But a new creature: the sun rising over a sown field, the first green shoots standing up in the furrows."""
    o = [sky(w, h, "#3A3A7A", "#FFC890"), halo(w * 0.62, h * 0.46, max(w, h) * 0.5, "#FFE6A0", 0.55),
         f'<circle cx="{f(w * 0.62)}" cy="{f(h * 0.46)}" r="{f(max(14, h * 0.07))}" fill="#FFF4C2"></circle>',
         rays(w * 0.62, h * 0.46, 24, h * 0.1, max(w, h), "#FFF4C2", 0.2, 3),
         hills(w, h, h * 0.46, seed, color="#6A5A6A", amp=10, step=90), ground(w, h, h * 0.52, "#6A4A2E", dy=0), birds(4, w * 0.2, w * 0.5, h * 0.12, h * 0.3, seed)]
    for i in range(9):                                         # the furrows in perspective
        t = (i + 1) / 9
        y = h * 0.52 + (h * 0.5) * t * t
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#4A3220" stroke-width="{f(1 + 3 * t)}"></path>')
        n = int(8 + 10 * (1 - t))
        for j in range(n):
            x = w * (j + 0.5 * (i % 2)) / n; sz = 3 + 12 * t
            o.append(f'<path d="M{f(x)} {f(y)} C {f(x - sz * 0.2)} {f(y - sz * 0.6)} {f(x - sz * 0.6)} {f(y - sz * 0.9)} {f(x - sz * 0.8)} {f(y - sz)} M{f(x)} {f(y)} C {f(x + sz * 0.2)} {f(y - sz * 0.7)} {f(x + sz * 0.6)} {f(y - sz)} {f(x + sz * 0.7)} {f(y - sz * 1.2)}" '
                     f'stroke="#7AB84A" stroke-width="{f(1 + 1.4 * t)}" fill="none" stroke-linecap="round"></path>')
    return "".join(o)

def love_one_word(w, h):
    """The whole law is fulfilled in one word: a plate — the two tables of the law at the left, their rows of writing
    gathered by lines into one point, and at the right two neighbours, one giving the other bread at his door."""
    o = [plate_bg(w, h, "GALATIANS 5:14 · THE WHOLE LAW · IN ONE WORD"), mk.defs("lw", *ALL)]
    k = min(w / 620, (h - 44) / 230)
    cy = h * 0.58
    o.append(V.tables(w * 0.2, cy + 70 * k, min(0.6, 0.5 * k), uid="lwtb"))
    for i in range(6):
        yy = cy - 50 * k + i * 20 * k
        o.append(f'<path d="M{f(w * 0.3)} {f(yy)} C {f(w * 0.4)} {f(yy)} {f(w * 0.44)} {f(cy)} {f(w * 0.52)} {f(cy)}" stroke="{GOLD}" stroke-width="1.4" fill="none" opacity="0.8"></path>')
    o.append(halo(w * 0.53, cy, 26 * k, "#FFE680", 0.7) + f'<circle cx="{f(w * 0.53)}" cy="{f(cy)}" r="{f(8 * k)}" fill="{GOLD}" stroke="{INK}" stroke-width="1.4"></circle>')
    base = h - 22; sc = (base - (h * 0.3)) / 205
    loaf = '<ellipse cx="-62" cy="-150" rx="12" ry="7" fill="#163A56" stroke="#8FD0E2" stroke-width="2"></ellipse>'
    o.append(mk.person("lw", round(w * 0.68), round(base), round(sc, 3), body="#1E4A6A", cloth="#163A56", kind="Robe", stroke=CY, sw=2.4, flip=True, up=[(-22, -158), (-46, -152), (-58, -150)], extra=loaf))
    o.append(mk.person("lw", round(w * 0.82), round(base), round(sc, 3), body="#1E4A6A", cloth="#24506E", kind="Tunic", stroke=CY, sw=2.4, up=[(-22, -158), (-40, -152), (-50, -152)]))
    o.append(label(w * 0.2, min(cy + 92 * k, h - 8), "THE LAW", CY, 9.5) + label(w * 0.75, 56, "LEVITICUS 19:18 · THE NEIGHBOR", GOLD, 9.5))
    return "".join(o)

def two_ways(p, w, h, seed):
    """Walk by the Spirit, and ye shall not fulfil the lust of the flesh: a man walking on a road that parts in two — the
    way at the left going down into the dark, the way at the right climbing into the light of the morning, his face set
    toward the light."""
    b = h * 0.94
    o = [_defs(p), f'<defs><linearGradient id="{p}tw" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#14101E"></stop><stop offset="0.45" stop-color="#3A3048"></stop>'
         f'<stop offset="0.6" stop-color="#C8B080"></stop><stop offset="1" stop-color="#FFF4C2"></stop></linearGradient></defs>',
         f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{p}tw)"></rect>', mk.stars(20, w * 0.4, h * 0.4, seed),
         halo(w * 0.86, h * 0.3, max(w, h) * 0.34, "#FFFFFF", 0.7), rays(w * 0.86, h * 0.3, 20, h * 0.06, max(w, h) * 0.5, "#FFF4C2", 0.3, 4),
         f'<path d="M-10 {f(h * 0.6)} C {f(w * 0.3)} {f(h * 0.52)} {f(w * 0.6)} {f(h * 0.56)} {f(w + 10)} {f(h * 0.48)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#5A5048" stroke="{INK}" stroke-width="2"></path>',
         f'<path d="M{f(w * 0.3)} {f(h + 10)} C {f(w * 0.34)} {f(h * 0.86)} {f(w * 0.4)} {f(h * 0.78)} {f(w * 0.46)} {f(h * 0.72)}" stroke="#D8C8A0" stroke-width="{f(max(16, h * 0.1))}" fill="none"></path>',
         f'<path d="M{f(w * 0.46)} {f(h * 0.72)} C {f(w * 0.58)} {f(h * 0.64)} {f(w * 0.72)} {f(h * 0.52)} {f(w * 0.84)} {f(h * 0.46)}" stroke="#F3E8C8" stroke-width="{f(max(8, h * 0.05))}" fill="none"></path>',
         f'<path d="M{f(w * 0.46)} {f(h * 0.72)} C {f(w * 0.36)} {f(h * 0.68)} {f(w * 0.22)} {f(h * 0.64)} {f(w * 0.06)} {f(h * 0.66)}" stroke="#4A4250" stroke-width="{f(max(8, h * 0.05))}" fill="none"></path>']
    s = fit(b, max(h * 0.2, b - 230))
    o.append(robed(p, w * 0.4, b, s, "#5A6A4A", head="#E8E2D6", cord="#3A2A1A", beard="#3A2A1A", flip=True))
    o.append(plate_label(w * 0.16, h * 0.08, "THE LUST OF THE FLESH", "#C8C8E8", 10, halo_="#14101E")
             + plate_label(w * 0.82, h * 0.08, "THE SPIRIT", "#7A4A2A", 10, halo_="#FFF8E6"))
    return "".join(o)

def yoke_broken(p, w, h, seed):
    """For freedom did Christ set us free: the yoke of bondage broken — an ox-yoke snapped in the middle, its two halves and
    its bows thrown down on the ground, the thongs burst, in a burst of morning light; a man standing upright beside it."""
    b = h * 0.92
    o = [_defs(p), sky(w, h, "#3A3A7A", "#FFE0A0"), halo(w * 0.5, h * 0.6, max(w, h) * 0.5, "#FFF4C2", 0.5), rays(w * 0.5, h * 0.62, 30, h * 0.1, max(w, h), "#FFF4C2", 0.28, 4),
         hills(w, h, h * 0.62, seed, color="#8A7A6A", amp=10, step=90), ground(w, h, h * 0.7, "#9A8460", dy=0)]
    k = min(w / 700, h / 260)
    def half(x, y, rot, flip):
        sx = -1 if flip else 1
        return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({f(sx * k)} {f(k)})">'
                '<path d="M0 -10 C 30 -16 60 -14 90 -22 C 110 -28 130 -26 150 -18 L 150 4 C 130 -4 110 -6 90 0 C 60 8 30 10 0 12 L -8 6 L 4 0 L -6 -6 Z" fill="#8A5A2A" stroke="#0D0D0F" stroke-width="3"></path>'
                '<path d="M86 0 C 84 30 92 52 112 54 C 132 52 138 30 134 -2" fill="none" stroke="#0D0D0F" stroke-width="10"></path>'
                '<path d="M86 0 C 84 30 92 52 112 54 C 132 52 138 30 134 -2" fill="none" stroke="#B8864A" stroke-width="6"></path>'
                '<path d="M150 -6 C 166 -2 176 10 170 24 M150 0 C 160 8 162 20 156 30" fill="none" stroke="#5A3A1A" stroke-width="3"></path></g>')
    o.append(half(w * 0.5 - 20 * k, b - 74 * k, -14, True) + half(w * 0.5 + 20 * k, b - 68 * k, 12, False))
    o.append(f'<path d="M{f(w * 0.5 - 8 * k)} {f(b - 98 * k)} L {f(w * 0.5)} {f(b - 118 * k)} L {f(w * 0.5 + 6 * k)} {f(b - 96 * k)}" stroke="#FFF4C2" stroke-width="3" fill="none"></path>')
    s_ = fit(b, max(h * 0.2, b - 230))
    o.append(gentile(p, w * 0.86, b, s_, 0, flip=True))
    return "".join(o)
