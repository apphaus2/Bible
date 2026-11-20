"""Drawings for the 2 John volume (and, by `from jn2.art import *`, for 3 John): 1 John's drawings (`from jn1.art import *`,
which carries Galatians', Acts', Mark's and Matthew's and the epistle kit) and the elect lady's house.

The elect lady (jn1.common.LADY_LOOK): a slate-blue robe, a dark-blue veil, a darker mantle; her children grown and young,
in cool or off-white veils and headcloths or bareheaded. John the elder only ever jn1.common.john_fig. No antichrist or
deceiver is drawn as such: the one "that bringeth not this teaching" (10) is a traveller seen from behind, going away from a
shut door."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from jn1.art import *
from jn1.art import _defs
from jn1.common import LADY_LOOK, JOHN_LOOK

def lady_fig(p, x, y, s, flip=False, up=None, extra="", pose="stand"):
    """The elect lady: a slate-blue robe, a dark-blue veil, a darker mantle."""
    L = LADY_LOOK
    return robed(p, x, y, s * 0.94, L["cloth"], woman=True, veil=L["veil"], mantle=L["mantle"], flip=flip, up=up, extra=extra, pose=pose,
                 seat=None if pose == "sit" else "stool")

def grown(p, x, y, s, i=0, flip=False, up=None, pose="stand"):
    """One of the lady's children grown: a son bareheaded or in a cool headcloth, a daughter in a cool veil."""
    looks = [("#4A6A8A", None, "#2A1A10", None, False), ("#7A6A8A", "#2A3A5A", None, None, True), ("#5A6A4A", None, None, "#1F3A4A", False),
             ("#8A7A6A", "#E8E2D6", None, None, True)]
    c, vl, hr, hd, wo = looks[i % len(looks)]
    if wo: return robed(p, x, y, s * 0.92, c, woman=True, veil=vl, flip=flip, up=up, pose=pose)
    return robed(p, x, y, s * 0.98, c, hair=hr, head=hd, cord="#0D1A20" if hd else None, belt="#2A1A10", flip=flip, up=up, pose=pose)

SCROLL_HAND = '<rect x="-86" y="-162" width="30" height="22" fill="#EADBB4" stroke="#0D0D0F" stroke-width="1.6"></rect>'   # a letter held open in a raised hand

def house_front(x, base, wd, hh, door="open", lit=True, seed=1, color="#E8D8B0", night=False):
    """A house front of white stone: a flat roof with its parapet, a small window above, and a doorway (door "open": the
    door standing open on a lit room; "shut": the door shut and barred, the window dark). (x, base) the left of its foot."""
    wall = color if not night else "#5A5070"
    o = [f'<rect x="{f(x)}" y="{f(base - hh)}" width="{f(wd)}" height="{f(hh)}" fill="{wall}" stroke="{INK}" stroke-width="2.4"></rect>',
         f'<rect x="{f(x - 6)}" y="{f(base - hh - 10)}" width="{f(wd + 12)}" height="12" fill="#B8A07A" stroke="{INK}" stroke-width="2"></rect>']
    dx, dw, dh = x + wd * 0.36, wd * 0.28, hh * 0.62
    wx, ww = x + wd * 0.1, wd * 0.16
    win = "#FFC14D" if (lit and door == "open") or (lit and night and door == "shut") else "#2A2438"
    o.append(f'<rect x="{f(wx)}" y="{f(base - hh * 0.8)}" width="{f(ww)}" height="{f(hh * 0.2)}" fill="{win}" stroke="{INK}" stroke-width="1.8"></rect>')
    if door == "open":
        o.append(f'<rect x="{f(dx)}" y="{f(base - dh)}" width="{f(dw)}" height="{f(dh)}" fill="#FFD680" stroke="{INK}" stroke-width="2.4"></rect>'
                 f'<path d="M{f(dx)} {f(base - dh)} L {f(dx - dw * 0.4)} {f(base - dh * 0.94)} L {f(dx - dw * 0.4)} {f(base + 2)} L {f(dx)} {f(base)} Z" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></path>')
    else:
        o.append(f'<rect x="{f(dx)}" y="{f(base - dh)}" width="{f(dw)}" height="{f(dh)}" fill="#5A321A" stroke="{INK}" stroke-width="2.6"></rect>'
                 f'<path d="M{f(dx + dw / 2)} {f(base - dh)} L {f(dx + dw / 2)} {f(base)}" stroke="{INK}" stroke-width="2"></path>'
                 f'<rect x="{f(dx - dw * 0.12)}" y="{f(base - dh * 0.55)}" width="{f(dw * 1.24)}" height="{f(max(5, dh * 0.07))}" fill="#3A2A1A" stroke="{INK}" stroke-width="1.6"></rect>')
    return "".join(o)

def door_rect(x, base, wd, hh):
    """Where house_front() puts its doorway: (x, top, width, height)."""
    return x + wd * 0.36, base - hh * 0.62, wd * 0.28, hh * 0.62

def lady_house(p, w, h, seed, letter=True):
    """The elder unto the elect lady and her children: her house at evening, the door open on the lamplit room, the lady
    standing before it with the elder's letter open in her hand, her children about her — two grown, two young."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#3A2A5A", "#E8A070"), houses(w, h, h * 0.56, seed, hmin=0.1, hmax=0.18, lit=True), ground(w, h, h * 0.62, "#B8A07A", dy=0)]
    hx, hw, hh = w * 0.36, w * 0.5, h * 0.62
    o.append(house_front(hx, h * 0.66, hw, hh * 0.86, door="open", seed=seed))
    dx, dt, dw, dh = door_rect(hx, h * 0.66, hw, hh * 0.86)
    o.append(glow(dx + dw / 2, h * 0.6, h * 0.4, "#FFC14D", 0.35, f"{p}g"))
    s = fit(b, max(h * 0.18, b - h * 0.64))
    o.append(grown(p, w * 0.16, b, s, 0, flip=True) + grown(p, w * 0.27, b, s, 1, flip=True))
    o.append(lady_fig(p, w * 0.5, b, s, up=[(-22, -158), (-46, -150), (-64, -152)] if letter else None, extra=SCROLL_HAND if letter else ""))
    o.append(child(p, w * 0.64, b, s, 0) + child(p, w * 0.74, b, s, 1))
    return "".join(o)

def evening_street(w, h, seed, door="open", tone="dusk", staffs=0):
    """A street of white houses (the covers of 2 and 3 John): tone "dusk" the sky going from evening to the first stars, the
    windows lit; "morning" a clear sky and the early sun. One door stands open on its lamplit room (door="shut": shut and
    barred); staffs=n travellers' staffs leaning on the wall beside it, a water jar at the door (3 John 5–8); no one drawn."""
    dusk = tone == "dusk"
    o = [sky(w, h, "#1A1440", "#E8906A") if dusk else sky(w, h, "#6AA8D0", "#FFF0C8")]
    o.append(mk.stars(30, w, h * 0.3, seed) + halo(w * 0.2, h * 0.62, max(w, h) * 0.4, "#FFB070", 0.4) if dusk else halo(w * 0.16, h * 0.5, h * 0.3, "#FFFFFF", 0.7))
    o.append(houses(w, h, h * 0.62, seed, hmin=0.14, hmax=0.24, lit=dusk) + ground(w, h, h * 0.62, "#A8906A" if dusk else "#C8B07A", dy=0))
    hx, hb, hw, hh = w * 0.42, h * 0.9, w * 0.5, h * 0.56
    o.append(house_front(hx, hb, hw, hh, door=door, seed=seed))
    dx, dt, dw, dh = door_rect(hx, hb, hw, hh)
    if door == "open": o.append(glow(dx + dw / 2, h * 0.86, h * 0.36, "#FFC14D", 0.4 if dusk else 0.25, f"es{seed}"))
    for i in range(staffs):                                           # staffs leaning on the wall right of the door
        x0 = dx + dw + hw * (0.08 + 0.05 * i)
        o.append(f'<path d="M{f(x0)} {f(hb)} L {f(x0 + hw * 0.05)} {f(hb - hh * 0.6)}" stroke="#0D0D0F" stroke-width="8" stroke-linecap="round"></path>'
                 f'<path d="M{f(x0)} {f(hb)} L {f(x0 + hw * 0.05)} {f(hb - hh * 0.6)}" stroke="#8A6A3A" stroke-width="5" stroke-linecap="round"></path>')
    if staffs:
        jx = dx + dw + hw * (0.12 + 0.05 * staffs)
        o.append(f'<path d="M{f(jx - 16)} {f(hb)} C {f(jx - 22)} {f(hb - 30)} {f(jx - 12)} {f(hb - 46)} {f(jx)} {f(hb - 46)} C {f(jx + 12)} {f(hb - 46)} {f(jx + 22)} {f(hb - 30)} {f(jx + 16)} {f(hb)} Z" '
                 f'fill="#C8682E" stroke="{INK}" stroke-width="2"></path><rect x="{f(jx - 7)}" y="{f(hb - 54)}" width="14" height="9" fill="#C8682E" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<rect x="-10" y="{f(h * 0.9)}" width="{f(w + 20)}" height="{f(h * 0.12)}" fill="#7A6A52" stroke="{INK}" stroke-width="2"></rect>')
    return "".join(o)

def walking_truth(p, w, h, seed):
    """I have found certain of thy children walking in truth: three of her children walking together on the road in the
    morning light, the town behind them."""
    b = h * 0.92
    o = [_defs(p), sky(w, h, "#8FD0E2", "#FFF4C2"), halo(w * 0.86, h * 0.34, h * 0.32, "#FFFFFF", 0.7), rays(w * 0.86, h * 0.34, 20, h * 0.06, h * 0.32, "#FFF4C2", 0.3, 4),
         hills(w, h, h * 0.5, seed, color="#9AAA7A", amp=12, step=90), houses(w, h, h * 0.62, seed, x0=-10, x1=w * 0.34, hmin=0.12, hmax=0.2),
         ground(w, h, h * 0.62, "#C8B07A", dy=0),
         f'<path d="M-10 {f(h * 0.82)} C {f(w * 0.3)} {f(h * 0.78)} {f(w * 0.7)} {f(h * 0.74)} {f(w + 10)} {f(h * 0.7)} L {f(w + 10)} {f(h * 0.98)} C {f(w * 0.6)} {f(h + 2)} {f(w * 0.3)} {f(h + 4)} -10 {f(h + 6)} Z" fill="#E0CC9A" stroke="{INK}" stroke-width="1.6"></path>']
    s = fit(b, max(h * 0.18, b - 210))
    for i, x in enumerate((0.42, 0.54, 0.66)):
        o.append(grown(p, w * x, b - i * 2, s, i, flip=True, pose="walk"))
    return "".join(o)

def shut_door(p, w, h, seed):
    """Receive him not into your house, and give him no greeting: the lady's house by night, the door shut and barred, a
    lamp in the window; a traveller with his staff and satchel going away down the road, seen from behind, small."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#05051A", "#2A2050"), mk.stars(40, w, h * 0.4, seed), ground(w, h, h * 0.72, "#2A2438", dy=0)]
    hx, hw, hh = w * 0.06, w * 0.5, h * 0.66
    o.append(house_front(hx, h * 0.8, hw, hh, door="shut", lit=True, night=True, seed=seed))
    o.append(f'<path d="M{f(w * 0.56)} {f(h + 10)} C {f(w * 0.62)} {f(h * 0.86)} {f(w * 0.74)} {f(h * 0.78)} {f(w + 10)} {f(h * 0.74)} L {f(w + 10)} {f(h * 0.8)} C {f(w * 0.8)} {f(h * 0.84)} {f(w * 0.74)} {f(h * 0.92)} {f(w * 0.72)} {f(h + 10)} Z" fill="#3A3450" stroke="{INK}" stroke-width="1.6"></path>')
    s = fit(h * 0.8, h * 0.8 - h * 0.26)
    staff = '<path d="M28 -182 L 33 0" stroke="#0D0D0F" stroke-width="7" stroke-linecap="round"></path><path d="M28 -182 L 33 0" stroke="#6A4A2A" stroke-width="4" stroke-linecap="round"></path>'
    bundle = ('<path d="M-18 -164 L 20 -106" stroke="#0D0D0F" stroke-width="5"></path><path d="M-18 -164 L 20 -106" stroke="#8A6A3A" stroke-width="3"></path><path d="M10 -110 L 34 -110 L 32 -84 C 26 -80 16 -80 12 -84 Z" fill="#7A5A3A" stroke="#0D0D0F" stroke-width="1.6"></path>')   # a satchel on a strap across the chest, at the hip
    o.append(robed(p, w * 0.68, h * 0.8, s, "#3A3A4A", head="#2A2A36", cord="#0D0D0F", flip=True, pose="walk", extra=staff + bundle))
    return "".join(o)

def sister_children(p, w, h, seed):
    """The children of thine elect sister salute thee: John standing with his staff at a house door, the sister's children
    about him, their hands raised in greeting, the sealed letter in his hand."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#5A3A6A", "#F3C890"), houses(w, h, h * 0.6, seed, hmin=0.12, hmax=0.2, lit=True), ground(w, h, h * 0.66, "#C8A878", dy=0)]
    o.append(house_front(w * 0.56, h * 0.7, w * 0.4, h * 0.5, door="open", seed=seed))
    s = fit(b, max(h * 0.16, b - min(h * 0.62, 250)))
    sealed = sealed_scroll(-74, -150, 0.26, rot=10)
    o.append(grown(p, w * 0.08, b, s, 2, flip=True, up=UP_HIGH))
    o.append(john_fig(p, w * 0.23, b, s, flip=True, up=[(-22, -158), (-46, -150), (-68, -152)], extra=sealed))
    o.append(grown(p, w * 0.38, b, s, 3, up=UP_HIGH) + child(p, w * 0.465, b, s, 2, up=UP_HIGH) + grown(p, w * 0.54, b, s, 0, up=UP_HIGH))
    return "".join(o)
