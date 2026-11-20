"""Drawings for the 3 John volume: 2 John's drawings (`from jn2.art import *`, which carries 1 John's, Galatians' and the
epistle kit, and the house fronts) and the houses of Gaius and of the church where Diotrephes would be first.

3 John's cast (jn1.common, each the same everywhere): Gaius (gaius_fig) a grey beard, an off-white headcloth, a brown robe and
a slate mantle; Diotrephes (diotrephes_fig) a black beard, a near-black headcloth with a gold cord, a dark plum robe and a wine
mantle; Demetrius (demetrius_fig) a brown beard, a dark-teal headcloth, a teal-grey robe; the travelling brethren in plain
robes with staffs and satchels (traveller). John the elder only ever jn1.common.john_fig."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from jn2.art import *
from jn1.art import _defs
from jn1.common import GAIUS_LOOK, DIOTREPHES_LOOK, DEMETRIUS_LOOK

def _look(p, x, y, s, L, flip=False, up=None, extra="", pose="stand"):
    return robed(p, x, y, s, L["cloth"], head=L["head"], cord=L["cord"], beard=L["beard"], mantle=L["mantle"], belt="#2A1A10", flip=flip, up=up, extra=extra,
                 pose=pose, seat=None if pose == "sit" else "stool")
def gaius_fig(p, x, y, s, flip=False, up=None, extra="", pose="stand"): return _look(p, x, y, s, GAIUS_LOOK, flip, up, extra, pose)
def diotrephes_fig(p, x, y, s, flip=False, up=None, extra="", pose="stand"): return _look(p, x, y, s, DIOTREPHES_LOOK, flip, up, extra, pose)
def demetrius_fig(p, x, y, s, flip=False, up=None, extra="", pose="stand"): return _look(p, x, y, s, DEMETRIUS_LOOK, flip, up, extra, pose)

STAFF = ('<path d="M28 -182 L 33 0" stroke="#0D0D0F" stroke-width="7" stroke-linecap="round"></path>'
         '<path d="M28 -182 L 33 0" stroke="#6A4A2A" stroke-width="4" stroke-linecap="round"></path>')
BUNDLE = ('<path d="M-18 -164 L 20 -106" stroke="#0D0D0F" stroke-width="5"></path><path d="M-18 -164 L 20 -106" stroke="#8A6A3A" stroke-width="3"></path><path d="M10 -110 L 34 -110 L 32 -84 C 26 -80 16 -80 12 -84 Z" fill="#7A5A3A" stroke="#0D0D0F" stroke-width="1.6"></path>')   # a satchel on a strap across the chest, at the hip

def traveller(p, x, y, s, i=0, flip=False, up=None, pose="stand"):
    """One of the brethren travelling for the sake of the Name (7): a plain robe, a cool or off-white headcloth or bareheaded,
    a staff, a satchel on a strap at the hip."""
    c, hd, bd, hr = [("#5A5A4A", "#E8E2D6", "#3A2A1A", None), ("#4A5A6A", None, "#2A1A10", "#2A1A10"), ("#6A5A5A", "#2A3A4A", "#4A3A2A", None),
                     ("#5A6A5A", None, None, "#3A2214")][i % 4]
    return robed(p, x, y, s, c, head=hd, cord="#2A1A10" if hd else None, beard=bd, hair=hr, belt="#2A1A10", flip=flip, up=up,
                 extra=("" if up else STAFF) + BUNDLE, pose=pose)

def brethren_come(p, w, h, seed):
    """I rejoiced greatly, when brethren came and bare witness unto thy truth: John seated at his table by lamplight, two of
    the travelling brethren standing before him with their staffs, one with his hand out, telling him."""
    return elder_desk(p, w, h, seed, stage="laid", others=(lambda p_, x, y, s, flip=False: traveller(p_, x, y, s, 0, up=[(-22, -158), (-46, -150), (-66, -158)]),
                                                         lambda p_, x, y, s, flip=False: traveller(p_, x, y, s, 1)))

def gaius_door(p, w, h, seed):
    """Thou doest a faithful work in whatsoever thou doest toward them that are brethren and strangers withal: Gaius at the
    open door of his house at evening, his arms held out in welcome to travellers coming up the street with their staffs and
    satchels, the lamplit room and the table set behind him."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#4A2A5A", "#F0A870"), houses(w, h, h * 0.58, seed, hmin=0.12, hmax=0.2, lit=True), ground(w, h, h * 0.64, "#C0A47A", dy=0)]
    hx, hw, hh = w * 0.04, w * 0.46, h * 0.6
    o.append(house_front(hx, h * 0.7, hw, hh * 0.9, door="open", seed=seed))
    dx, dt, dw, dh = door_rect(hx, h * 0.7, hw, hh * 0.9)
    o.append(glow(dx + dw / 2, h * 0.62, h * 0.4, "#FFC14D", 0.4, f"{p}g"))
    o.append(f'<rect x="{f(dx + dw * 0.1)}" y="{f(dt + dh * 0.62)}" width="{f(dw * 0.8)}" height="{f(dh * 0.08)}" fill="#6A3A1E"></rect>')   # the table inside
    s = fit(b, max(h * 0.18, b - min(h * 0.64, 250)))
    o.append(gaius_fig(p, w * 0.32, b, s, flip=True, up=[(-22, -158), (-48, -164), (-74, -172)]))
    for i, x in enumerate((0.56, 0.68, 0.8)):
        o.append(traveller(p, w * x, b - i * 2, s * (0.98 - 0.02 * i), i, pose="walk"))
    return "".join(o)

def diotrephes_door(p, w, h, seed):
    """Diotrephes, who loveth to have the preeminence among them, receiveth us not … and casteth them out of the church: the
    door of the house where the church meets, Diotrephes standing in it with his arm out barring the way, two of the
    brethren turned away down the step, and the elder's letter lying unopened on the step."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#2A2040", "#9A6A6A"), houses(w, h, h * 0.56, seed, hmin=0.12, hmax=0.2), ground(w, h, h * 0.62, "#9A8A70", dy=0)]
    hx, hw, hh = w * 0.42, w * 0.56, h * 0.66
    o.append(house_front(hx, h * 0.8, hw, hh, door="open", lit=False, seed=seed, color="#D8C8A8"))
    dx, dt, dw, dh = door_rect(hx, h * 0.8, hw, hh)
    o.append(f'<rect x="{f(dx)}" y="{f(dt)}" width="{f(dw)}" height="{f(dh)}" fill="#2A2030" stroke="{INK}" stroke-width="2.4"></rect>')    # dark within
    o.append(f'<rect x="{f(hx - 10)}" y="{f(h * 0.8)}" width="{f(hw + 20)}" height="{f(h * 0.06)}" fill="#B8A88A" stroke="{INK}" stroke-width="2"></rect>')   # the step
    o.append(sealed_scroll(hx + hw * 0.12, h * 0.8 + h * 0.025, max(0.2, h / 1400), rot=8))
    s = fit(h * 0.8, max(h * 0.1, h * 0.8 - min(h * 0.62, 240)))
    o.append(diotrephes_fig(p, dx + dw / 2, h * 0.8, s, up=[(-22, -158), (-50, -156), (-78, -156)]))
    s2 = fit(b, max(h * 0.18, b - min(h * 0.6, 236)))
    o.append(traveller(p, w * 0.12, b, s2, 2, flip=False, pose="walk") + traveller(p, w * 0.26, b - 4, s2 * 0.98, 3, flip=False, pose="walk"))
    return "".join(o)

def demetrius_witness(p, w, h, seed):
    """Demetrius hath the witness of all men: Demetrius standing with his staff and the sealed letter (he brings it, it may
    be), the brethren about him with their hands raised, bearing him witness, John among them."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#6A8AB0", "#F3E2B8"), houses(w, h, h * 0.6, seed, hmin=0.12, hmax=0.2), ground(w, h, h * 0.64, "#C8B080", dy=0)]
    s = fit(b, max(h * 0.16, b - min(h * 0.62, 250)))
    o.append(believer(p, w * 0.1, b, s, 0, flip=True, up=UP_HIGH) + john_fig(p, w * 0.24, b, s, flip=True, up=UP_BLESS))
    o.append(demetrius_fig(p, w * 0.42, b, s, extra=STAFF + sealed_scroll(10, -100, 0.22, rot=-70)))
    o.append(believer(p, w * 0.58, b, s, 1, up=UP_HIGH) + believer(p, w * 0.7, b, s, 2, up=UP_HIGH) + believer(p, w * 0.81, b, s, 3))
    return "".join(o)

def friends_salute(p, w, h, seed):
    """I hope shortly to see thee, and we shall speak face to face. Peace be unto thee. The friends salute thee: John at his
    door at morning with his staff, the friends about him raising their hands in greeting, the road going out beyond toward
    Gaius."""
    b = h * 0.94
    o = [_defs(p), sky(w, h, "#8FD0E2", "#FFF0C8"), halo(w * 0.86, h * 0.36, h * 0.3, "#FFFFFF", 0.7), hills(w, h, h * 0.5, seed, color="#9AAA7A", amp=12, step=90),
         ground(w, h, h * 0.62, "#C8B07A", dy=0),
         f'<path d="M{f(w * 0.52)} {f(h + 10)} C {f(w * 0.6)} {f(h * 0.8)} {f(w * 0.76)} {f(h * 0.68)} {f(w + 10)} {f(h * 0.64)} L {f(w + 10)} {f(h * 0.7)} C {f(w * 0.82)} {f(h * 0.74)} {f(w * 0.72)} {f(h * 0.86)} {f(w * 0.7)} {f(h + 10)} Z" fill="#E0CC9A" stroke="{INK}" stroke-width="1.6"></path>']
    o.append(house_front(-w * 0.02, h * 0.74, w * 0.3, h * 0.56, door="open", seed=seed))
    s = fit(b, max(h * 0.16, b - min(h * 0.62, 250)))
    o.append(john_fig(p, w * 0.27, b, s, flip=True, up=UP_BLESS))
    o.append(believer(p, w * 0.4, b, s, 2, up=UP_HIGH) + child(p, w * 0.48, b, s, 0, up=UP_HIGH) + believer(p, w * 0.56, b, s, 5))
    return "".join(o)
