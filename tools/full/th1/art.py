"""Drawings for the 1 Thessalonians volume. 1 Thessalonians starts from Galatians' drawings (`from gal.art import *`, which
carries all of Acts', Mark's and Matthew's drawings and the epistle kit) and adds its own.

1 Thessalonians' people at a distance, on the kit silhouettes (epistle.robed): Paul only ever epistle.paul_fig; Silvanus
(silvanus_r) Acts' Silas — a blue headcloth and robe, a black beard, a darker blue mantle; Timothy (timothy_r) as Acts and 2
Corinthians draw him — young, beardless, bareheaded, light-brown hair, a grey-blue tunic; Jason (jason_r), the church's
host at Thessalonica (Acts 17:5–9) — an off-white headcloth with a dark cord, a dark beard, an olive-grey robe and mantle;
the Thessalonians (folk) men in cool or off-white headcloths or bareheaded, women in cool veils. God is never drawn
(light); Satan is never drawn; the archangel is only words. Every function takes (p, w, h, seed, ...) or (w, h, ...); p, a
prefix unique to the panel, names the figure defs and gradients."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from gal.art import *
from gal.art import f, INK, _street, _house, _road, _gate, _prison, plate_label, night_window, light_fig, art
from epistle import study, stool, bench, SEAT_Y, _SIT, clipped, svg_stamp, city_window, low_table, still_life
from act.art8 import jupiter_temple
from act.art9 import stocks, night_road
from act.art10 import statue
from mat.art import room, houses, pavement, bgr
from co1.art4 import jp
from co1.art5 import sleepers
from rom.art5 import armour_stand
from num.art5 import trumpet
from kg1.art import ship
from genesis.art2 import hills, ground, fit
from genesis.art4 import clay_lamp
from jer.art import glow
from oba.minor import halo, rays, starfield, walls
import exo.art8 as B
import zlib
from act import geo

GOLD, CY = "#FFD23F", "#8FD0E2"

# ---- the cast at a distance -----------------------------------------------------------------------------------------------
SILVANUS_LOOK = dict(cloth="#2A4A6A", head="#2A4A6A", cord="#1A1210", beard="#2A1A10", mantle="#1A3048")
TIMOTHY_LOOK = dict(cloth="#7A8A9A", hair="#3A2214", belt="#3A4A5A")
JASON_LOOK = dict(cloth="#5A6450", head="#E8E2D6", cord="#3A2A1A", beard="#2A1A10", mantle="#3A4234")

def silvanus_r(p, x, y, s, flip=False, up=None, extra="", pose="stand", seat="stool"):
    """Silvanus (Silas, Acts 15:40): a blue headcloth and robe, a black beard, a darker blue mantle."""
    L = SILVANUS_LOOK
    return robed(p, x, y, s, L["cloth"], head=L["head"], cord=L["cord"], beard=L["beard"], mantle=L["mantle"], flip=flip, up=up, extra=extra, pose=pose, seat=seat)

def timothy_r(p, x, y, s, flip=False, up=None, extra="", pose="stand", seat="stool"):
    """Timothy: young, beardless, bareheaded, light-brown hair, a grey-blue tunic (Acts' colours)."""
    L = TIMOTHY_LOOK
    return robed(p, x, y, s, L["cloth"], hair=L["hair"], belt=L["belt"], flip=flip, up=up, extra=extra, pose=pose, seat=seat)

def jason_r(p, x, y, s, flip=False, up=None, extra="", pose="stand", seat="stool"):
    """Jason of Thessalonica (Acts 17:5–9), who received Paul and Silas: an off-white headcloth, a dark beard, olive-grey."""
    L = JASON_LOOK
    return robed(p, x, y, s, L["cloth"], head=L["head"], cord=L["cord"], beard=L["beard"], mantle=L["mantle"], flip=flip, up=up, extra=extra, pose=pose, seat=seat)

FOLK = [dict(cloth="#4A5A6A", head="#2A3A4A", beard="#2A1A10"), dict(cloth="#5A6A8A", woman=True, veil="#2A3A5A"),
        dict(cloth="#7A6A4A", hair="#2A1A10", beard="#3A2A1A"), dict(cloth="#6A5A4A", head="#E8E2D6", beard="#7A746A"),
        dict(cloth="#5A7A7A", woman=True, veil="#E8E2D6"), dict(cloth="#8A7A5A", hair="#3A2214"),
        dict(cloth="#5A4A5A", head="#3A3A4A", beard="#1A1210"), dict(cloth="#6A5A7A", woman=True, veil="#1F3A3A")]

def folk(p, x, y, s, i=0, flip=False, up=None, extra="", pose="stand", seat="stool"):
    """One of the church of the Thessalonians (FOLK[i]): men in cool or off-white headcloths or bareheaded, women veiled."""
    lk = dict(FOLK[i % len(FOLK)])
    woman = lk.pop("woman", False)
    return robed(p, x, y, s * (0.94 if woman else 1), lk.pop("cloth"), woman=woman, cord="#1A1210", flip=flip, up=up, extra=extra, pose=pose, seat=seat, **lk)

def child(p, x, y, s, i=0, flip=False, up=None):
    """A child (about half a grown figure's height), bareheaded, a plain tunic."""
    c, hr = [("#C8A060", "#2A1A10"), ("#8AA0B0", "#3A2214"), ("#B87A5A", "#1A1210")][i % 3]
    return robed(p, x, y, s, c, hair=hr, belt="#6A4A2A", flip=flip, up=up)

def _defs(p): return mk.defs(p, *ALL, "ManUp", "WomanUp")

def sit_up(*pts):
    """up= arm points for a seated robed() figure (the same frame as standing: robed lowers the arm with the torso)."""
    return list(pts)

def fig_s(h, frac=0.78, most=300):
    """A figure's scale in a drawing h tall: frac of the height, at most `most` px."""
    return min(h * frac, most) / 205

# ---- the letter written at Corinth ----------------------------------------------------------------------------------------
TIM_SCRIBE = dict(cloth=TIMOTHY_LOOK["cloth"], hair=TIMOTHY_LOOK["hair"])

def _silvanus_in(p, x, y, s, flip=False, up=None, extra=""):
    """Silvanus standing by in the study, set in a little from the right edge so his mantle is not cut."""
    return silvanus_r(p, x - (22 * s if flip else -22 * s), y, s, flip=flip, up=up, extra=extra)

def study_thess(p, w, h, seed, stage="dictate", fig_h=None, night=True):
    """Paul, and Silvanus, and Timothy (1:1): the study at Corinth by lamplight, the window on the Acrocorinth — Paul
    dictating (or listening as the letter is read back), Timothy on the mat writing, Silvanus standing by; stage="give"
    Timothy come back from Thessalonica at the open door with the church's letter in his hand (3:6), Silvanus by Paul."""
    fig_h = fig_h or min(h * 0.72, 260)
    if stage == "give":
        return study(p, w, h, seed, stage="give", scribe=False, bearer=timothy_r, others=(_silvanus_in,), fig_h=fig_h, night=night)
    return study(p, w, h, seed, stage=stage, scribe=TIM_SCRIBE, others=(_silvanus_in,), fig_h=fig_h, night=night)

def thess_road(w, h):
    """Unto the church of the Thessalonians: the letter's road from Corinth by Athens and Berœa to Thessalonica, Philippi
    beyond it, on Acts' map."""
    rt = ["CORINTH", (23.2, 38.0), "ATHENS", (23.0, 38.6), (22.6, 39.3), (22.4, 39.9), "BERŒA", "THESSALONICA"]
    return letter_road(w, h, rt, title="1 THESSALONIANS 1:1 · UNTO THE CHURCH OF THE THESSALONIANS", box=(20.4, 25.6, 37.4, 41.4),
                       places=("CORINTH", "ATHENS", "BERŒA", "THESSALONICA", "PHILIPPI"), hi=("CORINTH", "THESSALONICA"),
                       regions=("MACEDONIA", "ACHAIA"))

def sounded_forth(w, h, seed=1):
    """From you hath sounded forth the word of the Lord, not only in Macedonia and Achaia, but in every place: the harbour
    of Thessalonica in the morning, ships putting out across the gulf with their sails filled, the city climbing the slope
    behind (word of the church gone out with every ship and every traveller)."""
    o = [thess_view(w, h, seed)]
    for x, y, sc, fl in ((0.14, 0.6, 0.34, False), (0.3, 0.54, 0.22, False), (0.06, 0.5, 0.14, False)):
        o.append(ship(w * x, h * y, max(0.12, h / 640) * sc / 0.34 * 0.9, sail="#F3EFE6", flip=fl))
    return "".join(o)

def from_idols(p, w, h, seed):
    """Ye turned unto God from idols, to serve a living and true God, and to wait for his Son from heaven: a room of a house
    at Thessalonica, the household shrine in its niche empty, its idols taken down and lying on the floor; the man and his
    wife at the open door, turned to the morning light."""
    b = h * 0.92
    s = fig_s(h, 0.74)
    o = [_defs(p), room(w, h, b, wall="#C8A878", floor="#7A5A3A")]
    nx, nw, nt = w * 0.1, w * 0.18, h * 0.2                         # the niche
    o.append(f'<path d="M{f(nx)} {f(b - h * 0.3)} L {f(nx)} {f(nt + nw * 0.3)} Q {f(nx + nw / 2)} {f(nt - nw * 0.2)} {f(nx + nw)} {f(nt + nw * 0.3)} L {f(nx + nw)} {f(b - h * 0.3)} Z" fill="#5A3E2E" stroke="{INK}" stroke-width="2.4"></path>'
             f'<rect x="{f(nx - 10)}" y="{f(b - h * 0.3)}" width="{f(nw + 20)}" height="10" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(nx + nw * 0.2)} {f(b - h * 0.3)} l {f(nw * 0.2)} 0 M{f(nx + nw * 0.6)} {f(b - h * 0.3)} l {f(nw * 0.2)} 0" stroke="#A88A5A" stroke-width="3" opacity="0.6"></path>')
    k = s * 0.8
    for i, (x, rot, kind) in enumerate(((0.1, -90, 0), (0.24, 84, 1), (0.38, -80, 2))):   # the idols lying where they were put down
        xx = w * x
        o.append(f'<g transform="rotate({rot} {f(xx)} {f(b - 16 * k)})">' + statue(xx, b - 16 * k + 40 * k, k, kind=kind, color="#E8B830" if i == 1 else "#C8C0B0") + '</g>')
    dx, dw = w * 0.62, min(w * 0.22, 150)                              # the open door on the morning
    o.append(f'<defs><linearGradient id="{p}dn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF4C2"></stop><stop offset="1" stop-color="#FFC890"></stop></linearGradient></defs>'
             f'<rect x="{f(dx)}" y="{f(b - 210 * s)}" width="{f(dw)}" height="{f(210 * s)}" fill="url(#{p}dn)" stroke="{INK}" stroke-width="3"></rect>'
             + halo(dx + dw / 2, b - 150 * s, 120 * s, "#FFFFFF", 0.7)
             + f'<path d="M{f(dx)} {f(b)} L {f(dx + dw)} {f(b)} L {f(dx + dw + w * 0.1)} {f(h + 10)} L {f(dx - w * 0.2)} {f(h + 10)} Z" fill="#FFE6A0" opacity="0.35"></path>')
    o.append(folk(p, dx - w * 0.06, b, s, 3, flip=True) + folk(p, dx - w * 0.14, b, s, 4, flip=True))
    return "".join(o)

# ---- 1 Thessalonians 2 ----------------------------------------------------------------------------------------------------
def philippi_stocks(p, w, h, seed):
    """Shamefully treated at Philippi: the inner prison there, the stocks empty and the rods laid by them (Acts' drawing:
    the beating told in words only): close in on the stone floor of the cell, the heavy wooden stocks with their four
    holes, empty, the rods laid down beside them, a chain on its ring in the wall and a little light from the barred window
    high up."""
    b = h * 0.86
    o = [bgr(w, h, "#3A3238")]
    r = random.Random(seed)
    rh = max(26, h * 0.12)
    for row in range(int(b / rh) + 1):                                   # the stone courses
        y = row * rh; off = (row % 2) * w * 0.07
        o.append(f'<path d="M-10 {f(y)} L {f(w + 10)} {f(y)}" stroke="#2A2428" stroke-width="2"></path>')
        x = -off
        while x < w + 10:
            o.append(f'<path d="M{f(x)} {f(y)} L {f(x)} {f(y + rh)}" stroke="#2A2428" stroke-width="2"></path>'); x += w * 0.14
    wx, ww = w * 0.66, min(w * 0.12, h * 0.3)                             # the barred window and its light
    o.append(f'<path d="M{f(wx)} {f(h * 0.14 + ww * 0.6)} L {f(wx + ww)} {f(h * 0.14 + ww * 0.6)} L {f(wx - w * 0.12)} {f(b)} L {f(wx - w * 0.36)} {f(b)} Z" fill="#8FA8C8" opacity="0.18"></path>'
             f'<rect x="{f(wx)}" y="{f(h * 0.14)}" width="{f(ww)}" height="{f(ww * 0.6)}" fill="#14183A" stroke="{INK}" stroke-width="2.4"></rect>'
             + "".join(f'<path d="M{f(wx + ww * k / 4)} {f(h * 0.14)} L {f(wx + ww * k / 4)} {f(h * 0.14 + ww * 0.6)}" stroke="#6A6A74" stroke-width="3"></path>' for k in range(1, 4)))
    cx, cy = w * 0.16, h * 0.34                                          # the ring and the chain hanging
    o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(h * 0.03)}" fill="none" stroke="#8A8A94" stroke-width="4"></circle>'
             + "".join(f'<ellipse cx="{f(cx + k * 2)}" cy="{f(cy + h * 0.04 + k * h * 0.045)}" rx="{f(h * 0.012)}" ry="{f(h * 0.022)}" fill="none" stroke="#8A8A94" stroke-width="3"></ellipse>' for k in range(6)))
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h - b + 10)}" fill="#2A2228" stroke="{INK}" stroke-width="2"></rect>')
    sx, sw, sh = w * 0.26, w * 0.4, h * 0.2                               # the stocks: two beams, four holes
    st = b - sh
    o.append(f'<rect x="{f(sx)}" y="{f(st)}" width="{f(sw)}" height="{f(sh)}" fill="#6A4A2A" stroke="{INK}" stroke-width="3"></rect>'
             f'<path d="M{f(sx)} {f(st + sh * 0.5)} L {f(sx + sw)} {f(st + sh * 0.5)}" stroke="#3A2414" stroke-width="2.4"></path>'
             + "".join(f'<circle cx="{f(sx + sw * x_)}" cy="{f(st + sh * 0.5)}" r="{f(sh * 0.17)}" fill="#1A1210" stroke="{INK}" stroke-width="1.6"></circle>' for x_ in (0.18, 0.36, 0.64, 0.82))
             + "".join(f'<rect x="{f(sx + sw * x_ - sh * 0.1)}" y="{f(st - sh * 0.12)}" width="{f(sh * 0.2)}" height="{f(sh * 1.12)}" fill="#5A3A22" stroke="{INK}" stroke-width="2"></rect>' for x_ in (0.0, 1.0))
             + "".join(f'<path d="M{f(sx + sw * k / 6)} {f(st + 3)} l {f(r.uniform(-4, 4))} {f(sh * 0.3)}" stroke="#4A2E18" stroke-width="1.2"></path>' for k in range(1, 6)))
    for k in range(3):                                                   # the rods laid down
        y = b + (h - b) * (0.3 + 0.18 * k)
        o.append(f'<path d="M{f(w * 0.62)} {f(y)} L {f(w * 0.86)} {f(y - h * 0.03)}" stroke="#8A5A2A" stroke-width="{f(max(3, h * 0.014))}" stroke-linecap="round"></path>')
    return "".join(o)

def nurse(p, w, h, seed):
    """Gentle in the midst of you, as when a nurse cherisheth her own children: a room by lamplight, a mother sitting on a
    stool, her hand on the head of the child standing at her knee, the smaller one beside him; the lamp on its ledge."""
    b = h * 0.92
    s = fig_s(h, 0.84)
    o = [_defs(p), room(w, h, b, wall="#6A4A3A", floor="#3A2A20"), glow(w * 0.44, b - 90 * s, max(w, h) * 0.5, "#FFC14D", 0.4, f"{p}lg")]
    o.append(f'<rect x="{f(w * 0.72)}" y="{f(b - 150 * s)}" width="{f(80 * s)}" height="{f(8 * s)}" fill="#6A4A2A" stroke="{INK}" stroke-width="1.6"></rect>'
             + clay_lamp(w * 0.72 + 40 * s, b - 152 * s, max(0.6, s * 0.7)))
    cx = w * 0.6
    o.append(child(p, cx - 146 * s, b, s * 0.46, 1, flip=True) + child(p, cx - 100 * s, b, s * 0.56, 0, flip=True))
    o.append(robed(p, cx, b, s, "#5A6A8A", woman=True, veil="#1F3A5A", pose="sit", up=[(-22, -158), (-58, -166), (-94, -164)]))
    return "".join(o)

def tent_frame(x0, x1, top, b, s):
    """A tentmaker's frame by the wall, a length of dark goat-hair cloth on it, stitched in rows (Acts 18:3)."""
    return (f'<path d="M{f(x0)} {f(b)} L {f(x0 + 6 * s)} {f(top)} M{f(x1)} {f(b)} L {f(x1 - 6 * s)} {f(top)} M{f(x0 - 6)} {f(top)} L {f(x1 + 6)} {f(top)}" stroke="#5A3A22" stroke-width="{f(max(4, 6 * s))}"></path>'
            f'<path d="M{f(x0 + 8 * s)} {f(top + 4)} L {f(x1 - 8 * s)} {f(top + 4)} L {f(x1 - 12 * s)} {f(b - 70 * s)} C {f((x0 + x1) / 2)} {f(b - 62 * s)} {f((x0 + x1) / 2)} {f(b - 66 * s)} {f(x0 + 12 * s)} {f(b - 70 * s)} Z" fill="#2A221E" stroke="{INK}" stroke-width="2"></path>'
            + "".join(f'<path d="M{f(x0 + 12 * s)} {f(top + 4 + k * (b - 74 * s - top) / 5)} L {f(x1 - 12 * s)} {f(top + 4 + k * (b - 74 * s - top) / 5)}" stroke="#4A3E36" stroke-width="1.4" stroke-dasharray="6 4"></path>' for k in range(1, 5)))

def lap_cloth(x0, x1, y, s):
    """A length of the dark cloth across two laps."""
    return (f'<path d="M{f(x0)} {f(y)} C {f((x0 + x1) / 2)} {f(y + 14 * s)} {f((x0 + x1) / 2)} {f(y + 14 * s)} {f(x1)} {f(y)} L {f(x1)} {f(y + 12 * s)} '
            f'C {f((x0 + x1) / 2)} {f(y + 30 * s)} {f((x0 + x1) / 2)} {f(y + 30 * s)} {f(x0)} {f(y + 12 * s)} Z" fill="#2A221E" stroke="{INK}" stroke-width="1.8"></path>')

def night_toil(p, w, h, seed, who="silvanus"):
    """Our labor and travail, working night and day, that we might not burden any of you: a workroom at night, the lamp
    lit on its ledge, the window full of stars, the tentmaker's frame with its goat-hair cloth; Paul and Silvanus sitting
    face to face with a length of the cloth across their knees, stitching."""
    b = h * 0.92
    s = fig_s(h, 0.84)
    o = [_defs(p), room(w, h, b, wall="#3A2E2E", floor="#241C1A"), glow(w * 0.5, b - 110 * s, max(w, h) * 0.5, "#FFC14D", 0.36, f"{p}lg")]
    o.append(night_window(w * 0.06, b - 200 * s, min(w * 0.14, 100 * s), 80 * s, seed))
    o.append(tent_frame(w * 0.78, w * 0.98, b - 196 * s, b, s))
    o.append(f'<rect x="{f(w * 0.4)}" y="{f(b - 176 * s)}" width="{f(90 * s)}" height="{f(8 * s)}" fill="#6A4A2A" stroke="{INK}" stroke-width="1.6"></rect>'
             + clay_lamp(w * 0.4 + 45 * s, b - 178 * s, max(0.6, s * 0.7)))
    cx = w * 0.46
    lx, rx = cx - 116 * s, cx + 116 * s
    hand = sit_up((-22, -158), (-44, -128), (-60, -112))
    o.append(paul_fig(p, lx, b, s, flip=True, up=hand, pose="sit"))
    other = silvanus_r if who == "silvanus" else timothy_r
    o.append(other(p, rx, b, s, pose="sit", up=hand))
    o.append(lap_cloth(lx + 56 * s, rx - 56 * s, b - SEAT_Y * s - 8 * s, s))
    return "".join(o)

def jason_house(p, w, h, seed):
    """As a father with his own children, exhorting you, and encouraging you: the church gathered in Jason's house by
    lamplight, the brethren sitting along the bench, Paul standing before them with his hand held out, Jason by the door."""
    b = h * 0.92
    s = fig_s(h, 0.78)
    o = [_defs(p), room(w, h, b, wall="#5A4232", floor="#3A2A20"), glow(w * 0.4, b - 120 * s, max(w, h) * 0.5, "#FFC14D", 0.36, f"{p}lg")]
    o.append(f'<rect x="{f(w * 0.84)}" y="{f(b - 200 * s)}" width="{f(w * 0.12)}" height="{f(200 * s)}" fill="#0B0B2A" stroke="{INK}" stroke-width="2.4"></rect>'
             + f'<g transform="translate({f(w * 0.84)} {f(b - 200 * s)})">' + mk.stars(6, w * 0.12, 80 * s, seed) + '</g>')
    o.append(f'<rect x="{f(w * 0.24)}" y="{f(b - 186 * s)}" width="{f(80 * s)}" height="{f(8 * s)}" fill="#6A4A2A" stroke="{INK}" stroke-width="1.6"></rect>'
             + clay_lamp(w * 0.24 + 40 * s, b - 188 * s, max(0.6, s * 0.7)))
    n = 4
    step = min(w * 0.12, 96 * s)
    o.append(bench(w * 0.02, b, step * n + 40 * s, s))
    for i in range(n):
        o.append(folk(p, w * 0.02 + 30 * s + step * i, b, s * 0.98, i, flip=True, pose="sit", seat=None))
    o.append(paul_fig(p, w * 0.66, b, s, up=[(-22, -158), (-48, -150), (-72, -156)]))
    o.append(jason_r(p, w * 0.8, b, s * 0.98))
    return "".join(o)

def drove_out(p, w, h, seed):
    """And drove out us: the road out of the city by night, under the stars, Paul and Silas going (Acts' drawing, the
    brethren sending them away by night: Acts 17:10): the walls of Thessalonica behind them under the stars, the road
    going away west toward Berœa, Paul and Silas walking on it with their staves."""
    b = h * 0.9
    s = fig_s(h, 0.62, 240)
    o = [_defs(p), sky_(w, h, "#05051A", "#1E1650"), starfield(w, h, seed, 50, 0.5),
         f'<circle cx="{f(w * 0.12)}" cy="{f(h * 0.18)}" r="{f(max(8, h * 0.04))}" fill="#F3EFE6" stroke="{INK}" stroke-width="1.4"></circle>',
         walls(w * 0.58, w + 10, h * 0.6, h * 0.16, seed, color="#3A3450", lit=True, towers=2),
         hills(w, h, h * 0.58, seed, color="#14142E", amp=10, step=90), ground(w, h, h * 0.62, "#1E1E36", dy=0)]
    o.append(f'<path d="M{f(w * 0.8)} {f(h * 0.62)} C {f(w * 0.6)} {f(h * 0.7)} {f(w * 0.3)} {f(h * 0.8)} -10 {f(h * 0.86)} L -10 {f(h * 0.98)} C {f(w * 0.3)} {f(h * 0.94)} {f(w * 0.6)} {f(h * 0.78)} {f(w * 0.84)} {f(h * 0.62)} Z" fill="#34344E"></path>')
    staff = '<path d="M-72 -150 L -84 0" stroke="#6A4A2A" stroke-width="5" stroke-linecap="round"></path>'
    arm = [(-22, -158), (-46, -132), (-70, -124)]
    o.append(silvanus_r(p, w * 0.5, b - h * 0.04, s * 0.94, pose="walk", up=arm, extra=staff))
    o.append(paul_fig(p, w * 0.36, b, s, pose="walk", up=arm, extra=staff))
    return "".join(o)

def gate_shut(p, w, h, seed):
    """We would fain have come unto you, I Paul once and again; and Satan hindered us: the road north at dusk running up to a
    city gate, its doors shut and barred; no one on the road (Satan is never drawn: the words only)."""
    b = h * 0.94
    o = [sky_(w, h, "#2A1A3A", "#E89A6A"), halo(w * 0.78, h * 0.42, h * 0.5, "#FFC890", 0.5),
         hills(w, h, h * 0.46, seed, color="#4A3448", amp=12, step=80), ground(w, h, h * 0.58, "#6A4E44", dy=0)]
    gx, gw, gt = w * 0.5, min(w * 0.26, 180), h * 0.18
    o.append(f'<rect x="-10" y="{f(gt + h * 0.12)}" width="{f(w + 20)}" height="{f(h * 0.58 - gt - h * 0.12 + 2)}" fill="#8A6E5A" stroke="{INK}" stroke-width="2.4"></rect>')
    for xx in range(-10, int(w) + 20, 22):
        o.append(f'<rect x="{f(xx)}" y="{f(gt + h * 0.12 - 10)}" width="12" height="10" fill="#8A6E5A" stroke="{INK}" stroke-width="1.6"></rect>')
    for tx in (gx - gw * 0.72, gx + gw * 0.72):                        # the gate towers
        o.append(f'<rect x="{f(tx - gw * 0.22)}" y="{f(gt)}" width="{f(gw * 0.44)}" height="{f(h * 0.58 - gt)}" fill="#7A5E4A" stroke="{INK}" stroke-width="2.4"></rect>')
    o.append(f'<path d="M{f(gx - gw / 2)} {f(h * 0.58)} L {f(gx - gw / 2)} {f(gt + h * 0.2)} Q {f(gx)} {f(gt + h * 0.04)} {f(gx + gw / 2)} {f(gt + h * 0.2)} L {f(gx + gw / 2)} {f(h * 0.58)} Z" fill="#4A2E1E" stroke="{INK}" stroke-width="3"></path>'
             f'<path d="M{f(gx)} {f(gt + h * 0.1)} L {f(gx)} {f(h * 0.58)}" stroke="{INK}" stroke-width="3"></path>'
             + "".join(f'<path d="M{f(gx - gw / 2)} {f(gt + h * (0.22 + 0.08 * k))} L {f(gx + gw / 2)} {f(gt + h * (0.22 + 0.08 * k))}" stroke="#2A2A30" stroke-width="3"></path>' for k in range(4))
             + f'<rect x="{f(gx - gw * 0.56)}" y="{f(gt + h * 0.3)}" width="{f(gw * 1.12)}" height="{f(max(6, h * 0.025))}" fill="#3A2414" stroke="{INK}" stroke-width="2"></rect>')
    o.append(f'<path d="M{f(gx - gw * 0.4)} {f(h * 0.58)} L {f(gx + gw * 0.4)} {f(h * 0.58)} L {f(w * 0.86)} {f(h + 10)} L {f(w * 0.14)} {f(h + 10)} Z" fill="#9A7E64" stroke="{INK}" stroke-width="2"></path>')
    r = random.Random(seed)
    for _ in range(14):
        yy = r.uniform(h * 0.62, h * 0.98); xx = r.uniform(w * 0.2, w * 0.8)
        o.append(f'<path d="M{f(xx)} {f(yy)} l {f(r.uniform(8, 22))} 0" stroke="#7A604A" stroke-width="1.6"></path>')
    return "".join(o)

def sky_(w, h, top, bot):
    uid = f"sk{zlib.crc32(repr((top, bot, round(w), round(h))).encode()) % 10 ** 8}"
    return (f'<defs><linearGradient id="{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"></stop><stop offset="1" stop-color="{bot}"></stop></linearGradient></defs>'
            f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="url(#{uid})"></rect>')

def wreath(cx, cy, R, color="#E8B830", leaf="#C8962E"):
    """A victor's wreath of leaves (the crown of the games), tied with a ribbon at the foot."""
    o = [f'<path d="M{f(cx - R * 0.14)} {f(cy + R * 0.9)} A {f(R)} {f(R * 0.92)} 0 1 1 {f(cx + R * 0.14)} {f(cy + R * 0.9)}" fill="none" stroke="#8A5A1E" stroke-width="{f(max(2.5, R * 0.04))}"></path>']
    for side in (-1, 1):
        for k in range(9):
            a = math.radians(100 + k * 18) if side < 0 else math.radians(80 - k * 18)
            x, y = cx + R * math.cos(a), cy - R * math.sin(a) * 0.92
            rot = math.degrees(-a) + (90 if side < 0 else -90)
            o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(R * 0.2)}" ry="{f(R * 0.085)}" fill="{color if k % 2 else leaf}" stroke="{INK}" stroke-width="1.6" transform="rotate({f(rot + side * 30)} {f(x)} {f(y)})"></ellipse>')
    o.append(f'<path d="M{f(cx - R * 0.16)} {f(cy + R * 0.9)} L {f(cx - R * 0.3)} {f(cy + R * 1.3)} M{f(cx + R * 0.16)} {f(cy + R * 0.9)} L {f(cx + R * 0.32)} {f(cy + R * 1.26)}" stroke="#B5121B" stroke-width="{f(max(3, R * 0.06))}" stroke-linecap="round"></path>'
             f'<circle cx="{f(cx)}" cy="{f(cy + R * 0.9)}" r="{f(R * 0.08)}" fill="#B5121B" stroke="{INK}" stroke-width="1.4"></circle>')
    return "".join(o)

def crown_glory(w, h, seed):
    """What is our hope, or joy, or crown of glorying? Are not even ye: a victor's wreath of gold in a burst of light above
    the roofs of Thessalonica at night, the lamps lit in its houses."""
    o = [sky_(w, h, "#0B0B2A", "#3A2A6A"), starfield(w, h, seed, 40, 0.5), halo(w * 0.5, h * 0.4, max(w, h) * 0.4, "#FFE680", 0.55),
         rays(w * 0.5, h * 0.4, 30, h * 0.2, max(w, h), "#FFF4C2", 0.25, 4)]
    o.append(wreath(w * 0.5, h * 0.4, min(h * 0.28, w * 0.16)))
    o.append(houses(w, h, h * 1.0, seed, hmin=0.14, hmax=0.24, lit=True, color=("#3A3050", "#2E2840", "#443A5A", "#382E4A"), stairs=False))
    return "".join(o)

# ---- 1 Thessalonians 3 ----------------------------------------------------------------------------------------------------
def athens_alone(p, w, h, seed):
    """We thought it good to be left behind at Athens alone; and sent Timothy: the Acropolis on its rock above the city,
    Paul standing alone at the left; Timothy on the road going away north, his staff in his hand."""
    b = h * 0.94
    s = fig_s(h, 0.72, 280)
    o = [_defs(p), sky_(w, h, "#8FD0E2", "#F3E8C8"),
         f'<path d="M{f(w * 0.2)} {f(h * 0.5)} L {f(w * 0.28)} {f(h * 0.26)} L {f(w * 0.62)} {f(h * 0.24)} L {f(w * 0.7)} {f(h * 0.5)} Z" fill="#B8A07A" stroke="{INK}" stroke-width="2"></path>',
         jupiter_temple(w * 0.45, h * 0.25, w * 0.26), hills(w, h, h * 0.5, seed, color="#A89A7A", amp=8, step=90), ground(w, h, h * 0.56, "#D8C8A0", dy=0)]
    o.append(f'<path d="M{f(w * 0.3)} {f(h + 10)} C {f(w * 0.5)} {f(h * 0.8)} {f(w * 0.7)} {f(h * 0.66)} {f(w + 10)} {f(h * 0.6)}" stroke="#C8B080" stroke-width="{f(max(14, h * 0.08))}" fill="none"></path>')
    o.append(paul_fig(p, w * 0.16, b, s, flip=True))
    staff = '<path d="M-74 -150 L -86 0" stroke="#6A4A2A" stroke-width="5" stroke-linecap="round"></path>'
    o.append(timothy_r(p, w * 0.76, b - h * 0.08, s * 0.7, flip=True, pose="walk", up=[(-22, -158), (-46, -132), (-72, -124)], extra=staff))
    return "".join(o)

def timothy_back(p, w, h, seed):
    """When Timothy came even now unto us from you, and brought us glad tidings: the study at Corinth, Timothy in the open
    door with the church's letter in his hand, Paul reaching for it, Silvanus beside him."""
    return study_thess(p, w, h, seed, stage="give")

def night_prayer(p, w, h, seed):
    """Night and day praying exceedingly that we may see your face: the study at Corinth deep in the night, the lamp burned
    low on the table, the roll laid by; Paul standing at the window, his hand lifted, praying, the stars over the city."""
    b = h * 0.92
    s = fig_s(h, 0.7, 280)
    o = [_defs(p), room(w, h, b, wall="#2E2638", floor="#1E1824"), glow(w * 0.6, h * 0.4, max(w, h) * 0.45, "#8FA8E8", 0.25, f"{p}mg")]
    ww, wh = min(w * 0.3, 230 * s), min(h * 0.46, 150 * s)
    o.append(city_window(w * 0.5, b - 200 * s, ww, wh, True, seed))
    o.append(low_table(w * 0.14, b, 70 * s, s) + clay_lamp(w * 0.14 + 22 * s, b - 31 * s, s * 0.6) + inkpot(w * 0.14 + 52 * s, b - 30 * s, s * 0.6)
             + glow(w * 0.14 + 22 * s, b - 40 * s, 60 * s, "#FFC14D", 0.45, f"{p}lg"))
    o.append(sealed_scroll(w * 0.3, b - 6 * s, 0.4 * s, rot=4))
    o.append(paul_fig(p, w * 0.42, b, s, flip=True, up=[(-22, -158), (-40, -196), (-50, -232)]))
    return "".join(o)

# ---- 1 Thessalonians 4 ----------------------------------------------------------------------------------------------------
def house_front(w, h, seed):
    """This is the will of God, even your sanctification: a plain house front of white stone on a quiet street by day, its
    door shut, its window shuttered, a pot of herbs by the step; no one in the street."""
    b = h * 0.9
    o = [sky_(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.62, seed + 3, hmin=0.12, hmax=0.2)]
    hx, hw, ht = w * 0.28, w * 0.44, h * 0.1
    o.append(f'<rect x="{f(hx)}" y="{f(ht)}" width="{f(hw)}" height="{f(b - ht)}" fill="#EADFC6" stroke="{INK}" stroke-width="3"></rect>'
             f'<rect x="{f(hx - 8)}" y="{f(ht - 10)}" width="{f(hw + 16)}" height="12" fill="#B8A07A" stroke="{INK}" stroke-width="2.4"></rect>')
    dw, dh = hw * 0.24, (b - ht) * 0.6
    dx = hx + hw * 0.24
    o.append(f'<path d="M{f(dx)} {f(b)} L {f(dx)} {f(b - dh + dw * 0.3)} Q {f(dx + dw / 2)} {f(b - dh - dw * 0.1)} {f(dx + dw)} {f(b - dh + dw * 0.3)} L {f(dx + dw)} {f(b)} Z" fill="#6A3E22" stroke="{INK}" stroke-width="2.6"></path>'
             + "".join(f'<path d="M{f(dx + dw * k / 4)} {f(b - dh + dw * 0.2)} L {f(dx + dw * k / 4)} {f(b)}" stroke="#4A2A14" stroke-width="1.6"></path>' for k in range(1, 4))
             + f'<circle cx="{f(dx + dw * 0.8)}" cy="{f(b - dh * 0.45)}" r="{f(max(2.5, dw * 0.05))}" fill="#C8A060" stroke="{INK}" stroke-width="1.2"></circle>')
    wx, ww, wy = hx + hw * 0.62, hw * 0.2, ht + (b - ht) * 0.22
    o.append(f'<rect x="{f(wx)}" y="{f(wy)}" width="{f(ww)}" height="{f(ww * 0.9)}" fill="#3A5A6A" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M{f(wx + ww / 2)} {f(wy)} L {f(wx + ww / 2)} {f(wy + ww * 0.9)}" stroke="{INK}" stroke-width="2"></path>'
             + "".join(f'<path d="M{f(wx)} {f(wy + ww * 0.18 * k)} L {f(wx + ww)} {f(wy + ww * 0.18 * k)}" stroke="#2A4A5A" stroke-width="1.4"></path>' for k in range(1, 5)))
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h - b + 10)}" fill="#C8B894" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(dx - 10)}" y="{f(b)}" width="{f(dw + 20)}" height="{f(h * 0.03)}" fill="#B8A884" stroke="{INK}" stroke-width="1.6"></rect>')
    px = dx + dw + hw * 0.08                                           # the pot of herbs
    o.append(f'<path d="M{f(px)} {f(b)} L {f(px - 10)} {f(b - 26)} L {f(px + 26)} {f(b - 26)} L {f(px + 16)} {f(b)} Z" fill="#B5652E" stroke="{INK}" stroke-width="1.8"></path>'
             + "".join(f'<path d="M{f(px + 8)} {f(b - 26)} q {f(dx_)} -18 {f(dx_ * 1.6)} -30" stroke="#3A6A3A" stroke-width="2.4" fill="none"></path>' for dx_ in (-8, -2, 4, 10)))
    return "".join(o)

def welcome(p, w, h, seed):
    """Ye yourselves are taught of God to love one another; for indeed ye do it toward all the brethren that are in all
    Macedonia: a street of Thessalonica by day, brethren come in from another city walking up with their staves, and Jason
    at his open door, his hand held out to take them in."""
    b = h * 0.92
    s = fig_s(h, 0.72, 260)
    o = [_defs(p), sky_(w, h, "#8FD0E2", "#F3E8C8"), houses(w, h, h * 0.6, seed, hmin=0.14, hmax=0.24),
         f'<rect x="-10" y="{f(h * 0.6)}" width="{f(w + 20)}" height="{f(h)}" fill="#D8C8A0" stroke="{INK}" stroke-width="2"></rect>']
    hx, hw = w * 0.66, w * 0.36                                          # Jason's house front
    o.append(f'<rect x="{f(hx)}" y="{f(b - 250 * s)}" width="{f(hw)}" height="{f(250 * s)}" fill="#EADFC6" stroke="{INK}" stroke-width="3"></rect>'
             f'<rect x="{f(hx + hw * 0.14)}" y="{f(b - 200 * s)}" width="{f(110 * s)}" height="{f(200 * s)}" fill="#3A2418" stroke="{INK}" stroke-width="2.6"></rect>'
             + glow(hx + hw * 0.14 + 55 * s, b - 100 * s, 90 * s, "#FFC14D", 0.4, f"{p}dg"))
    o.append(jason_r(p, hx + hw * 0.14 + 55 * s, b, s, up=[(-22, -158), (-48, -150), (-74, -152)]))
    staff = '<path d="M-72 -150 L -84 0" stroke="#6A4A2A" stroke-width="5" stroke-linecap="round"></path>'
    arm = [(-22, -158), (-46, -132), (-70, -124)]
    o.append(folk(p, w * 0.2, b, s * 0.98, 6, flip=True, pose="walk", up=arm, extra=staff))
    o.append(folk(p, w * 0.36, b, s, 2, flip=True, pose="walk", up=[(-22, -158), (-48, -150), (-74, -154)]))
    return "".join(o)

def potter(p, w, h, seed):
    """Study to be quiet, and to do your own business, and to work with your hands: a potter's workshop by day, the potter
    sitting at his wheel shaping a jar, the shelves of his pots drying behind him, the door open on the street."""
    b = h * 0.92
    s = fig_s(h, 0.84)
    o = [_defs(p), room(w, h, b, wall="#D8C098", floor="#8A6A4A"),
         f'<rect x="{f(w * 0.82)}" y="{f(b - 200 * s)}" width="{f(w * 0.13)}" height="{f(200 * s)}" fill="#FFE6A0" stroke="{INK}" stroke-width="2.4"></rect>']
    r = random.Random(seed)
    for row in range(3):                                               # the shelves of pots
        y = b - (60 + row * 52) * s
        o.append(f'<rect x="{f(w * 0.04)}" y="{f(y)}" width="{f(w * 0.3)}" height="{f(6 * s)}" fill="#6A4A2A" stroke="{INK}" stroke-width="1.6"></rect>')
        x = w * 0.05
        while x < w * 0.32:
            ph = r.uniform(22, 36) * s; pw = r.uniform(16, 24) * s
            o.append(f'<path d="M{f(x)} {f(y)} C {f(x - pw * 0.2)} {f(y - ph * 0.5)} {f(x + pw * 0.1)} {f(y - ph * 0.8)} {f(x + pw * 0.3)} {f(y - ph)} L {f(x + pw * 0.7)} {f(y - ph)} '
                     f'C {f(x + pw * 0.9)} {f(y - ph * 0.8)} {f(x + pw * 1.2)} {f(y - ph * 0.5)} {f(x + pw)} {f(y)} Z" fill="{r.choice(["#B5652E", "#C8783A", "#A85A2A"])}" stroke="{INK}" stroke-width="1.4"></path>')
            x += pw + 8 * s
    cx = w * 0.56
    wx = cx - 92 * s                                                   # the wheel before his knees
    o.append(f'<rect x="{f(wx - 4 * s)}" y="{f(b - 46 * s)}" width="{f(8 * s)}" height="{f(46 * s)}" fill="#5A3A22" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<ellipse cx="{f(wx)}" cy="{f(b - 46 * s)}" rx="{f(30 * s)}" ry="{f(6 * s)}" fill="#7A5A3A" stroke="{INK}" stroke-width="1.8"></ellipse>'
             f'<path d="M{f(wx - 14 * s)} {f(b - 48 * s)} C {f(wx - 20 * s)} {f(b - 66 * s)} {f(wx - 8 * s)} {f(b - 76 * s)} {f(wx - 8 * s)} {f(b - 84 * s)} L {f(wx + 8 * s)} {f(b - 84 * s)} '
             f'C {f(wx + 8 * s)} {f(b - 76 * s)} {f(wx + 20 * s)} {f(b - 66 * s)} {f(wx + 14 * s)} {f(b - 48 * s)} Z" fill="#B87A4A" stroke="{INK}" stroke-width="1.8"></path>')
    o.append(robed(p, cx, b, s, "#8A6A4A", head="#E8E2D6", cord="#3A2A1A", beard="#3A2A1A", belt="#5A3A22", pose="sit", up=sit_up((-22, -158), (-50, -128), (-78, -114))))
    return "".join(o)

def tombs_dusk(w, h, seed):
    """Concerning them that fall asleep: the sepulchres hewn in the hillside at dusk, their stones rolled to (1 Corinthians'
    drawing)."""
    return sleepers(w, h, seed)

def cloud_bank(cx, cy, wd, hh, seed, fill="#FFF4E0", rim="#FFD23F"):
    """A bank of cloud: overlapping round puffs, a gold rim of light along the top."""
    r = random.Random(seed)
    n = max(4, int(wd / max(hh, 1) * 2))
    o = []
    for i in range(n):
        x = cx - wd / 2 + wd * (i + 0.5) / n + r.uniform(-wd * 0.03, wd * 0.03)
        rr = hh * r.uniform(0.5, 0.8)
        o.append(f'<circle cx="{f(x)}" cy="{f(cy - rr * 0.3)}" r="{f(rr)}" fill="{fill}" stroke="{rim}" stroke-width="2.4"></circle>')
    o.append(f'<rect x="{f(cx - wd / 2)}" y="{f(cy - hh * 0.2)}" width="{f(wd)}" height="{f(hh * 0.5)}" rx="{f(hh * 0.25)}" fill="{fill}"></rect>')
    return "".join(o)

def risen_up(p, x, y, s, i=0):
    """One of the dead in Christ risen, or of them that are alive caught up: a small figure in white, arms raised, a soft
    light about it (no face at this size)."""
    c = ["#FFFDF0", "#F8F2E0", "#FFFFFF"][i % 3]
    hr = ["#3A2214", "#1A1210", "#6A5A4A", "#2A1A10"][i % 4]
    woman = i % 3 == 1
    fig = robed(p, x, y, s * (0.94 if woman else 1), c, woman=woman, veil="#E8E2D6" if woman else None, hair=None if woman else hr,
                up=[(-22, -158), (-30, -190), (-34, -222)], flip=i % 2 == 1, line="#8A7A5A")
    return halo(x, y - 110 * s, 110 * s, "#FFFFFF", 0.55) + fig

def caught_up(p, w, h, seed):
    """The Lord himself shall descend from heaven, with a shout, with the voice of the archangel, and with the trump of God:
    and the dead in Christ shall rise first; then we that are alive … caught up in the clouds: a great light breaking in the
    clouds at the top of the sky (no figure in it), the trumpet's blast across the sky with no one sounding it; below, the
    hillside of tombs with every stone rolled back, and the town; small figures in white rising toward the light."""
    o = [_defs(p), sky_(w, h, "#FFF4C2", "#2A2A6A"), halo(w * 0.56, h * 0.08, max(w, h) * 0.6, "#FFFFFF", 0.8),
         rays(w * 0.56, h * 0.06, 40, h * 0.08, max(w, h) * 1.2, "#FFFDF0", 0.35, 5)]
    o.append(cloud_bank(w * 0.2, h * 0.2, w * 0.36, h * 0.09, seed) + cloud_bank(w * 0.84, h * 0.17, w * 0.34, h * 0.08, seed + 1)
             + cloud_bank(w * 0.56, h * 0.26, w * 0.3, h * 0.07, seed + 2))
    tx, ty = w * 0.06, h * 0.42                                         # the trump: the blast across the sky
    for k in range(4):
        rr = h * (0.08 + 0.06 * k)
        o.append(f'<path d="M{f(tx + 150 * min(0.42, h / 900) + rr * 0.5)} {f(ty - rr * 0.6)} A {f(rr)} {f(rr * 0.9)} 0 0 1 {f(tx + 150 * min(0.42, h / 900) + rr * 0.5)} {f(ty + rr * 0.6)}" fill="none" stroke="#FFD23F" stroke-width="3" opacity="{0.9 - 0.15 * k:.2f}"></path>')
    o.append(trumpet(tx, ty, min(0.42, h / 900), rot=-14))
    o.append(jp(w * 0.22, h * 0.32, "パーッ", min(38, h * 0.08), fill="#FFD23F", stroke="#0D0D0F", rot=-6, roman="PAA"))
    hb = h * 0.8                                                        # the hillside: a face of rock with the tombs hewn in it
    o.append(f'<path d="M-10 {f(hb)} C {f(w * 0.2)} {f(hb - h * 0.06)} {f(w * 0.44)} {f(hb - h * 0.05)} {f(w * 0.62)} {f(hb - h * 0.02)} L {f(w * 0.62)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#7A6A6A" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(w * 0.6)} {f(hb + h * 0.02)} C {f(w * 0.75)} {f(hb - h * 0.01)} {f(w * 0.9)} {f(hb + h * 0.01)} {f(w + 10)} {f(hb - h * 0.01)} L {f(w + 10)} {f(h + 10)} L {f(w * 0.6)} {f(h + 10)} Z" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></path>')
    o.append(houses(w, h, h * 0.9, seed, x0=w * 0.64, hmin=0.05, hmax=0.08, color=("#C8B8A0", "#B8A890", "#D8C8B0", "#A89880"), stairs=False))
    tw = min(w * 0.07, h * 0.1)
    for i in range(4):                                                  # the tombs, the doors open and lit within, the stones rolled back
        x = w * (0.08 + 0.14 * i); y = hb + h * (0.13 + 0.03 * (i % 2))
        o.append(f'<path d="M{f(x - tw * 0.7)} {f(y + 4)} L {f(x - tw * 0.7)} {f(y - tw * 1.1)} L {f(x + tw * 0.7)} {f(y - tw * 1.1)} L {f(x + tw * 0.7)} {f(y + 4)} Z" fill="#5A4A4A" stroke="{INK}" stroke-width="1.6"></path>'
                 f'<path d="M{f(x - tw / 2)} {f(y)} L {f(x - tw / 2)} {f(y - tw * 0.7)} Q {f(x)} {f(y - tw * 1.05)} {f(x + tw / 2)} {f(y - tw * 0.7)} L {f(x + tw / 2)} {f(y)} Z" fill="#FFF4C2" stroke="{INK}" stroke-width="2"></path>'
                 + halo(x, y - tw * 0.4, tw * 0.9, "#FFF4C2", 0.45)
                 + f'<circle cx="{f(x + tw * 1.0)}" cy="{f(y - tw * 0.36)}" r="{f(tw * 0.4)}" fill="#A89A8A" stroke="{INK}" stroke-width="2"></circle>')
    pts = [(0.1, 0.64, 0.5), (0.24, 0.58, 0.46), (0.4, 0.62, 0.48), (0.54, 0.52, 0.42), (0.7, 0.6, 0.46), (0.86, 0.56, 0.44),
           (0.32, 0.44, 0.36), (0.62, 0.4, 0.34), (0.47, 0.36, 0.3), (0.8, 0.42, 0.34), (0.94, 0.66, 0.4)]
    for i, (x, y, sc) in enumerate(pts):
        o.append(risen_up(p, w * x, h * y, h * 0.16 * sc / 0.5 / 205, i))
    return "".join(o)

# ---- 1 Thessalonians 5 ----------------------------------------------------------------------------------------------------
def thief_night(w, h, seed):
    """The day of the Lord so cometh as a thief in the night: a street of houses at night, every window dark, and one
    door standing open on the black inside; no one in sight."""
    b = h * 0.9
    o = [sky_(w, h, "#05051A", "#1E1650"), starfield(w, h, seed, 40, 0.4),
         houses(w, h, b, seed, hmin=0.38, hmax=0.56, shut=True, color=("#2E2A44", "#26223A", "#34304C", "#2A2640"), stairs=False)]
    hx, hw, ht = w * 0.4, w * 0.24, h * 0.24                          # the house with the open door
    o.append(f'<rect x="{f(hx)}" y="{f(ht)}" width="{f(hw)}" height="{f(b - ht)}" fill="#3A3450" stroke="{INK}" stroke-width="3"></rect>'
             f'<rect x="{f(hx - 6)}" y="{f(ht - 8)}" width="{f(hw + 12)}" height="10" fill="#2A2440" stroke="{INK}" stroke-width="2"></rect>')
    dx, dw, dh = hx + hw * 0.3, hw * 0.34, (b - ht) * 0.66
    o.append(f'<rect x="{f(dx)}" y="{f(b - dh)}" width="{f(dw)}" height="{f(dh)}" fill="#020204" stroke="{INK}" stroke-width="2.6"></rect>'
             f'<path d="M{f(dx + dw)} {f(b - dh)} L {f(dx + dw + dw * 0.5)} {f(b - dh - dh * 0.06)} L {f(dx + dw + dw * 0.5)} {f(b + dh * 0.04)} L {f(dx + dw)} {f(b)} Z" fill="#4A3424" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(dx + dw + dw * 0.25)} {f(b - dh)} L {f(dx + dw + dw * 0.25)} {f(b + dh * 0.02)}" stroke="#2A1A10" stroke-width="1.6"></path>')
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h - b + 10)}" fill="#1A1828" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(dx)} {f(b)} L {f(dx + dw)} {f(b)} L {f(dx + dw * 1.6)} {f(h + 10)} L {f(dx - dw * 0.6)} {f(h + 10)} Z" fill="#020204" opacity="0.5"></path>')
    return "".join(o)

def night_day(p, w, h, seed):
    """Ye are all sons of light, and sons of the day: we are not of the night, nor of darkness; let us not sleep, but let us
    watch: one panel in two lights — at the left, the town at night, every door shut, all asleep; at the right, the dawn,
    and a watchman awake on the wall, his spear in his hand, looking toward the morning."""
    b = h * 0.92
    mid = w * 0.46
    o = [_defs(p), f'<defs><clipPath id="{p}nl"><rect x="-10" y="-10" width="{f(mid + 10)}" height="{f(h + 20)}"></rect></clipPath>'
         f'<clipPath id="{p}dr"><rect x="{f(mid)}" y="-10" width="{f(w - mid + 10)}" height="{f(h + 20)}"></rect></clipPath></defs>']
    o.append(f'<g clip-path="url(#{p}nl)">' + sky_(w, h, "#05051A", "#1E1650") + starfield(w, h, seed, 30, 0.5)
             + houses(w, h, b, seed, x1=mid + 20, hmin=0.3, hmax=0.46, shut=True, color=("#2E2A44", "#26223A", "#34304C", "#2A2640"), stairs=False)
             + f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h)}" fill="#1A1828" stroke="{INK}" stroke-width="2"></rect></g>')
    o.append(f'<g clip-path="url(#{p}dr)">' + sky_(w, h, "#5A7AB0", "#FFD8A0") + halo(w * 0.94, h * 0.62, h * 0.6, "#FFF4C2", 0.8)
             + rays(w * 0.94, h * 0.62, 24, h * 0.1, max(w, h), "#FFF4C2", 0.25, 4))
    wt = h * 0.6                                                        # the wall and the watchman on it
    o.append(f'<rect x="{f(mid)}" y="{f(wt)}" width="{f(w - mid + 10)}" height="{f(h - wt + 10)}" fill="#C8A878" stroke="{INK}" stroke-width="2.4"></rect>'
             + "".join(f'<rect x="{f(xx)}" y="{f(wt - 12)}" width="14" height="12" fill="#C8A878" stroke="{INK}" stroke-width="1.6"></rect>' for xx in range(int(mid) + 6, int(w) + 10, 26))
             + "".join(f'<path d="M{f(mid)} {f(wt + k * (h - wt) / 4)} L {f(w + 10)} {f(wt + k * (h - wt) / 4)}" stroke="#A88A5A" stroke-width="1.4"></path>' for k in range(1, 4)) + '</g>')
    s = min(wt * 0.72, 200) / 205
    spear = '<path d="M-60 -230 L -62 0" stroke="#5A3A22" stroke-width="5"></path><path d="M-60 -244 L -54 -228 L -66 -228 Z" fill="#B8B8C0" stroke="#0D0D0F" stroke-width="1.4"></path>'
    o.append(folk(p, w * 0.76, wt - 2, s, 0, flip=True, up=[(-22, -158), (-44, -140), (-60, -132)], extra=spear))
    o.append(f'<path d="M{f(mid)} -10 L {f(mid)} {f(h + 10)}" stroke="{INK}" stroke-width="3"></path>')
    o.append(plate_label(mid * 0.5, h * 0.1, "OF THE NIGHT", "#C8C8E8", 11) + plate_label(mid + (w - mid) * 0.2, h * 0.1, "OF THE DAY", "#3A2418", 11, halo_="#FFE6C0"))
    return "".join(o)

def armour_plate(w, h):
    """Putting on the breastplate of faith and love; and for a helmet, the hope of salvation: a technical plate of the
    armour on its stand (Romans' drawing), the breastplate and the helmet called out."""
    B._W[0] = w
    o = [plate_bg(w, h, "1 THESSALONIANS 5:8 · THE ARMOUR OF THE DAY")]
    s = (h - 40) * 0.92 / 250
    x, base = w * 0.5, h * 0.97
    o.append(armour_stand(x, base, s))
    def call(px, py, lx, ly, head, sub, right):
        an = "start" if right else "end"
        return (f'<circle cx="{f(px)}" cy="{f(py)}" r="3.5" fill="{GOLD}"></circle><path d="M{f(px)} {f(py)} L {f(lx)} {f(ly)}" stroke="{GOLD}" stroke-width="1.4"></path>'
                + plate_label(lx + (6 if right else -6), ly - 4, head, GOLD, 11, an) + plate_label(lx + (6 if right else -6), ly + 12, sub, CY, 9.5, an))
    o.append(call(x - 26 * s, base - 120 * s, w * 0.3, base - 110 * s, "THE BREASTPLATE", "OF FAITH AND LOVE", False))
    o.append(call(x + 16 * s, base - 214 * s, w * 0.68, base - 214 * s, "THE HELMET", "THE HOPE OF SALVATION", True))
    return "".join(o)

def _icon(kind, cx, cy, R):
    """A medallion's emblem (no words)."""
    if kind == "sun":
        return (rays(cx, cy, 12, R * 0.4, R * 0.8, "#FFD23F", 0.9, 3) + f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R * 0.34)}" fill="#FFD23F" stroke="{INK}" stroke-width="1.6"></circle>')
    if kind == "hands":                                                 # hands lifted in prayer
        return "".join(f'<path d="M{f(cx + sg * R * 0.08)} {f(cy + R * 0.6)} L {f(cx + sg * R * 0.18)} {f(cy - R * 0.1)} C {f(cx + sg * R * 0.2)} {f(cy - R * 0.5)} {f(cx + sg * R * 0.34)} {f(cy - R * 0.62)} {f(cx + sg * R * 0.4)} {f(cy - R * 0.4)} '
                       f'L {f(cx + sg * R * 0.36)} {f(cy + R * 0.6)} Z" fill="#C98E66" stroke="{INK}" stroke-width="1.6"></path>' for sg in (-1, 1)) + halo(cx, cy - R * 0.5, R * 0.4, "#FFF4C2", 0.6)
    if kind == "bread":                                                 # a loaf and a cup: give thanks
        return (f'<ellipse cx="{f(cx - R * 0.2)}" cy="{f(cy + R * 0.2)}" rx="{f(R * 0.36)}" ry="{f(R * 0.2)}" fill="#C8963E" stroke="{INK}" stroke-width="1.6"></ellipse>'
                f'<path d="M{f(cx - R * 0.4)} {f(cy + R * 0.12)} l {f(R * 0.4)} 0" stroke="#8A5A22" stroke-width="1.4"></path>'
                f'<path d="M{f(cx + R * 0.18)} {f(cy - R * 0.4)} L {f(cx + R * 0.56)} {f(cy - R * 0.4)} L {f(cx + R * 0.46)} {f(cy)} L {f(cx + R * 0.28)} {f(cy)} Z M{f(cx + R * 0.37)} {f(cy)} L {f(cx + R * 0.37)} {f(cy + R * 0.32)} M{f(cx + R * 0.24)} {f(cy + R * 0.34)} L {f(cx + R * 0.5)} {f(cy + R * 0.34)}" fill="#C8C8D0" stroke="{INK}" stroke-width="1.6"></path>')
    if kind == "flame":
        return (f'<path d="M{f(cx)} {f(cy - R * 0.62)} C {f(cx + R * 0.4)} {f(cy - R * 0.2)} {f(cx + R * 0.4)} {f(cy + R * 0.4)} {f(cx)} {f(cy + R * 0.5)} C {f(cx - R * 0.4)} {f(cy + R * 0.4)} {f(cx - R * 0.4)} {f(cy - R * 0.1)} {f(cx)} {f(cy - R * 0.62)} Z" fill="#FF8A2A" stroke="{INK}" stroke-width="1.6"></path>'
                f'<path d="M{f(cx)} {f(cy - R * 0.2)} C {f(cx + R * 0.2)} {f(cy)} {f(cx + R * 0.18)} {f(cy + R * 0.34)} {f(cx)} {f(cy + R * 0.38)} C {f(cx - R * 0.18)} {f(cy + R * 0.34)} {f(cx - R * 0.16)} {f(cy)} {f(cx)} {f(cy - R * 0.2)} Z" fill="#FFE680"></path>')
    if kind == "scroll":
        return (f'<rect x="{f(cx - R * 0.42)}" y="{f(cy - R * 0.3)}" width="{f(R * 0.84)}" height="{f(R * 0.6)}" fill="#EADBB4" stroke="{INK}" stroke-width="1.6"></rect>'
                + "".join(f'<rect x="{f(cx + sg * R * 0.42 - R * 0.07)}" y="{f(cy - R * 0.38)}" width="{f(R * 0.14)}" height="{f(R * 0.76)}" rx="{f(R * 0.05)}" fill="#8A5A30" stroke="{INK}" stroke-width="1.4"></rect>' for sg in (-1, 1))
                + "".join(f'<path d="M{f(cx - R * 0.28)} {f(cy - R * 0.14 + k * R * 0.14)} l {f(R * 0.56)} 0" stroke="#4A3020" stroke-width="1.4"></path>' for k in range(3)))
    if kind == "scales":                                                # prove all things
        return (f'<path d="M{f(cx)} {f(cy - R * 0.5)} L {f(cx)} {f(cy + R * 0.5)} M{f(cx - R * 0.26)} {f(cy + R * 0.5)} L {f(cx + R * 0.26)} {f(cy + R * 0.5)} M{f(cx - R * 0.5)} {f(cy - R * 0.36)} L {f(cx + R * 0.5)} {f(cy - R * 0.36)}" stroke="#E8B830" stroke-width="2.4"></path>'
                + "".join(f'<path d="M{f(cx + sg * R * 0.5)} {f(cy - R * 0.36)} L {f(cx + sg * R * 0.5 - R * 0.18)} {f(cy + R * 0.06)} M{f(cx + sg * R * 0.5)} {f(cy - R * 0.36)} L {f(cx + sg * R * 0.5 + R * 0.18)} {f(cy + R * 0.06)}" stroke="#E8B830" stroke-width="1.4"></path>'
                          f'<path d="M{f(cx + sg * R * 0.5 - R * 0.22)} {f(cy + R * 0.06)} Q {f(cx + sg * R * 0.5)} {f(cy + R * 0.26)} {f(cx + sg * R * 0.5 + R * 0.22)} {f(cy + R * 0.06)} Z" fill="#E8B830" stroke="{INK}" stroke-width="1.4"></path>' for sg in (-1, 1)))
    if kind == "door":                                                  # abstain: the door shut against it
        return (f'<path d="M{f(cx - R * 0.3)} {f(cy + R * 0.5)} L {f(cx - R * 0.3)} {f(cy - R * 0.26)} Q {f(cx)} {f(cy - R * 0.62)} {f(cx + R * 0.3)} {f(cy - R * 0.26)} L {f(cx + R * 0.3)} {f(cy + R * 0.5)} Z" fill="#6A3E22" stroke="{INK}" stroke-width="1.8"></path>'
                f'<path d="M{f(cx - R * 0.4)} {f(cy + R * 0.04)} L {f(cx + R * 0.4)} {f(cy + R * 0.04)}" stroke="#2A2A30" stroke-width="3"></path>')
    return ""

COMMANDS = [("5:16", "REJOICE", "sun"), ("5:17", "PRAY", "hands"), ("5:18", "GIVE THANKS", "bread"), ("5:19", "QUENCH NOT", "flame"),
            ("5:20", "PROPHESYINGS", "scroll"), ("5:21", "PROVE ALL THINGS", "scales"), ("5:22", "ABSTAIN", "door")]

def commands_plate(w, h):
    """Rejoice always; pray without ceasing; in everything give thanks … abstain from every form of evil: the short
    commands as a plate of seven medallions, each with its emblem and its verse — the sun, hands lifted, a loaf and a cup,
    a flame, a scroll, a balance, a shut door."""
    B._W[0] = w
    o = [plate_bg(w, h, "1 THESSALONIANS 5:16–22 · SEVEN SHORT COMMANDS")]
    n = len(COMMANDS)
    rows = 2 if h > 300 else 1
    per = (4, 3) if rows == 2 else (n,)
    R = min((w - 40) / per[0] * (0.3 if rows == 2 else 0.4), (h - 60) / rows * 0.28)
    for i, (ref, name, kind) in enumerate(COMMANDS):
        row = 0 if rows == 1 or i < 4 else 1
        j, m = (i, per[0]) if row == 0 else (i - 4, per[1])
        cx = 20 + (w - 40) * (j + 0.5) / m
        cy = 30 + (h - 30) * (row + 0.5) / rows
        o.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R)}" fill="#14284A" stroke="{GOLD}" stroke-width="2.4"></circle>'
                 f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(R - 5)}" fill="none" stroke="{CY}" stroke-width="1" stroke-dasharray="3 3"></circle>'
                 + _icon(kind, cx, cy, R * 0.8)
                 + label(cx, cy - R - 10, ref, CY, 10) + label(cx, cy + R + 18, name, GOLD, 8.5 if len(name) > 10 else 9.5, ls=0.06))
    return "".join(o)

def read_to_all(p, w, h, seed):
    """Salute all the brethren with a holy kiss. I adjure you by the Lord that this epistle be read unto all the brethren:
    the church in Jason's house, one standing to read the letter from the open roll, the brethren sitting along the bench
    listening; at the right two brethren greeting each other, a hand on each one's shoulder."""
    b = h * 0.92
    s = fig_s(h, 0.74, 250)
    o = [_defs(p), room(w, h, b, wall="#C8A878", floor="#7A5A3A"), glow(w * 0.3, b - 120 * s, max(w, h) * 0.4, "#FFE6A0", 0.3, f"{p}lg"),
         f'<rect x="{f(w * 0.86)}" y="{f(b - 200 * s)}" width="{f(min(w * 0.1, 80 * s))}" height="{f(200 * s)}" fill="#FFE6A0" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="{f(w * 0.2)}" y="{f(b - 186 * s)}" width="{f(80 * s)}" height="{f(8 * s)}" fill="#6A4A2A" stroke="{INK}" stroke-width="1.6"></rect>'
         + clay_lamp(w * 0.2 + 40 * s, b - 188 * s, max(0.6, s * 0.7))]
    step = 92 * s
    o.append(bench(w * 0.02, b, 2 * step + 70 * s, s))
    for i in range(3):
        o.append(folk(p, w * 0.02 + 30 * s + step * i, b, s * 0.98, i + 1, flip=True, pose="sit", seat=None))
    roll = '<path d="M-82 -150 L -58 -150 L -58 -132 L -82 -132 Z" fill="#EADBB4" stroke="#0D0D0F" stroke-width="1.4"></path><rect x="-86" y="-154" width="6" height="26" rx="2" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.2"></rect>'
    o.append(folk(p, w * 0.02 + 30 * s + step * 2 + 134 * s, b, s, 6, up=[(-22, -158), (-44, -146), (-62, -142)], extra=roll))
    o.append(jason_r(p, w * 0.8 + 70 * s, b, s * 0.98, up=[(-22, -158), (-40, -164), (-52, -160)]))
    o.append(folk(p, w * 0.8, b, s, 2, flip=True, up=[(-22, -158), (-40, -164), (-52, -160)]))
    return "".join(o)

# ---- the cover and the openers --------------------------------------------------------------------------------------------
def thess_view(w, h, seed, tone="dawn"):
    """Thessalonica on its gulf: the city's walls and white houses climbing the slope above the harbour, the sea of the
    Thermaic gulf, and across it far off the snow of mount Olympus, the sky at dawn (tone="dawn") or dusk."""
    top, bot = {"dawn": ("#3A3A7A", "#FFC890"), "dusk": ("#2A1E3A", "#E8906A")}[tone]
    o = [sky_(w, h, top, bot), halo(w * 0.62, h * 0.44, h * 0.34, "#FFE6A0", 0.5)]
    o.append(f'<path d="M-10 {f(h * 0.46)} L {f(w * 0.08)} {f(h * 0.38)} L {f(w * 0.14)} {f(h * 0.33)} L {f(w * 0.19)} {f(h * 0.355)} L {f(w * 0.25)} {f(h * 0.32)} L {f(w * 0.33)} {f(h * 0.39)} L {f(w * 0.44)} {f(h * 0.46)} Z" fill="#7A7A9A" stroke="{INK}" stroke-width="1.6"></path>'
             f'<path d="M{f(w * 0.11)} {f(h * 0.355)} L {f(w * 0.14)} {f(h * 0.33)} L {f(w * 0.19)} {f(h * 0.355)} L {f(w * 0.25)} {f(h * 0.32)} L {f(w * 0.29)} {f(h * 0.355)} L {f(w * 0.25)} {f(h * 0.35)} L {f(w * 0.19)} {f(h * 0.37)} L {f(w * 0.14)} {f(h * 0.355)} Z" fill="#F3EFE6"></path>')
    o.append(f'<rect x="-10" y="{f(h * 0.46)}" width="{f(w + 20)}" height="{f(h * 0.56)}" fill="#3A6A8A" stroke="{INK}" stroke-width="1.6"></rect>')
    r = random.Random(seed)
    for _ in range(26):
        yy = r.uniform(h * 0.48, h * 0.98); xx = r.uniform(0, w)
        o.append(f'<path d="M{f(xx)} {f(yy)} l {f(r.uniform(14, 40))} 0" stroke="#8FD0E2" stroke-width="1.6" opacity="0.7"></path>')
    o.append(f'<path d="M{f(w * 0.36)} {f(h + 10)} L {f(w * 0.4)} {f(h * 0.6)} C {f(w * 0.56)} {f(h * 0.5)} {f(w * 0.8)} {f(h * 0.3)} {f(w + 10)} {f(h * 0.22)} L {f(w + 10)} {f(h + 10)} Z" fill="#9A8A6A" stroke="{INK}" stroke-width="2"></path>')
    for row in range(4):                                                # the houses climbing the slope, the wall along the top
        y = h * (0.66 - row * 0.1); x0 = w * (0.44 + row * 0.09)
        o.append(houses(w, h, y, seed + row, x0=x0, hmin=0.04, hmax=0.07, stairs=False))
    o.append(walls(w * 0.78, w + 10, h * 0.3, h * 0.07, seed, color="#C8A878", gate=False, houses=False, towers=2))
    return "".join(o)
