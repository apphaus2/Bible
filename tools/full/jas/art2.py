"""Drawings for James 2: the synagogue door, the royal law, faith without works, Abraham and Rahab (see jas/art.py)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from jas.art import *
from jas.art import art, plate_label, light_fig, _synagogue, _street, _road

RICH = dict(cloth="#5A1A6A", mantle="#E8B830", head="#F3EFE6", cord="#E8B830", beard="#2A1A10")    # fine clothing, a gold ring
def rich_man(p, x, y, s, flip=False, up=None, extra="", pose="stand"):
    """A rich man in fine clothing: a purple robe, a gold-bordered mantle, a white headcloth with a gold cord, a gold ring."""
    ring = '<circle cx="-62" cy="-150" r="3.4" fill="none" stroke="#FFD23F" stroke-width="2"></circle>' if up else ""
    return robed(p, x, y, s, RICH["cloth"], head=RICH["head"], cord=RICH["cord"], beard=RICH["beard"], mantle=RICH["mantle"], belt="#E8B830", flip=flip, up=up,
                 extra=ring + extra, pose=pose)

_PATCHES = ('<rect x="-12" y="-96" width="9" height="11" fill="#6A6050" stroke="#0D0D0F" stroke-width="1"></rect>'
            '<rect x="6" y="-50" width="10" height="9" fill="#5A5446" stroke="#0D0D0F" stroke-width="1"></rect>'
            '<path d="M-20 -6 l 6 -10 l 5 8 l 6 -9 l 5 9" fill="none" stroke="#0D0D0F" stroke-width="1.2"></path>')
def poor_man(p, x, y, s, flip=False, up=None, extra="", pose="stand"):
    """A poor man in vile clothing: a patched grey-brown robe, bareheaded, unkempt."""
    return robed(p, x, y, s, "#7A7262", hair="#3A2E24", beard="#3A2E24", flip=flip, up=up, extra=_PATCHES + extra, pose=pose)
def poor_woman(p, x, y, s, flip=False, up=None, extra=""):
    return robed(p, x, y, s * 0.94, "#6A6458", woman=True, veil="#3A3A40", flip=flip, up=up,
                 extra='<path d="M-14 -40 l 5 -9 l 5 8 l 5 -9 l 5 9 l 5 -8" fill="none" stroke="#0D0D0F" stroke-width="1.2"></path>' + extra)

def synagogue_door(p, w, h, seed):
    """If there come into your synagogue a man with a gold ring, in fine clothing, and a poor man in vile clothing: the
    synagogue's hall, the rich man led to the good cushioned seat (Sit thou here in a good place), the poor man by the door
    pointed to stand there."""
    bg, b = _synagogue(w, h, seed)
    s = fit(b, max(h * 0.16, b - 225))
    o = [D_(p), bg]
    sx = w * 0.14                                                   # the good seat: a carved chair with a cushion
    o.append(f'<rect x="{f(sx - 36 * s)}" y="{f(b - 170 * s)}" width="{f(10 * s)}" height="{f(170 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(sx + 26 * s)}" y="{f(b - 110 * s)}" width="{f(10 * s)}" height="{f(110 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(sx - 40 * s)}" y="{f(b - 98 * s)}" width="{f(80 * s)}" height="{f(10 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>'
             f'<rect x="{f(sx - 34 * s)}" y="{f(b - 112 * s)}" width="{f(68 * s)}" height="{f(16 * s)}" rx="{f(6 * s)}" fill="#A8322A" stroke="{INK}" stroke-width="2"></rect>'
             f'<path d="M{f(sx - 36 * s)} {f(b - 170 * s)} C {f(sx - 46 * s)} {f(b - 180 * s)} {f(sx - 46 * s)} {f(b - 192 * s)} {f(sx - 31 * s)} {f(b - 186 * s)}" stroke="#E8B830" stroke-width="3" fill="none"></path>'
             f'<rect x="{f(sx - 70 * s)}" y="{f(b - 20 * s)}" width="{f(40 * s)}" height="{f(20 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>')
    o.append(man_r(p, w * 0.42, b, s, 2, flip=False, up=[(-22, -158), (-50, -140), (-74, -132)]))       # Sit thou here
    o.append(rich_man(p, w * 0.29, b, s, flip=True))
    dx = w * 0.78                                                   # the door, and the poor man standing in it
    o.append(f'<rect x="{f(dx - 46 * s)}" y="{f(b - 232 * s)}" width="{f(92 * s)}" height="{f(232 * s)}" fill="#E8D8A8" stroke="{INK}" stroke-width="2.4"></rect>')
    o.append(man_r(p, w * 0.6, b, s, 3, flip=True, up=[(-22, -158), (-50, -150), (-76, -156)]))       # Stand thou there
    o.append(poor_man(p, dx, b, s * 0.97, flip=False))
    o.append(plate_label(w * 0.24, h * 0.06, "SIT THOU HERE IN A GOOD PLACE", "#3A1A0A", 9, halo_="#E8DCC0")
             + plate_label(w * 0.76, h * 0.06, "STAND THOU THERE", "#3A1A0A", 9, halo_="#E8DCC0"))
    return "".join(o)

def chain_law(w, h):
    """Whosoever shall keep the whole law, and yet stumble in one point, he is become guilty of all: the law as a chain of
    links hung between two posts, every link whole but one, broken."""
    o = [plate_bg(w, h, "JAMES 2:10 · STUMBLE IN ONE POINT · GUILTY OF ALL")]
    n = 11; x0, x1 = w * 0.09, w * 0.91; y = h * 0.44
    lw = (x1 - x0) / n
    for i in range(n):
        cx = x0 + lw * (i + 0.5)
        broken = i == 6
        col = "#FF6A4A" if broken else GOLD
        if i % 2 == 0:
            if broken:
                o.append(f'<path d="M{f(cx - lw * 0.15)} {f(y - h * 0.065)} A {f(lw * 0.62)} {f(h * 0.065)} 0 0 0 {f(cx - lw * 0.2)} {f(y + h * 0.065)}" fill="none" stroke="{col}" stroke-width="5"></path>'
                         f'<path d="M{f(cx + lw * 0.2)} {f(y - h * 0.065)} A {f(lw * 0.62)} {f(h * 0.065)} 0 0 1 {f(cx + lw * 0.15)} {f(y + h * 0.065)}" fill="none" stroke="{col}" stroke-width="5"></path>')
            else: o.append(f'<ellipse cx="{f(cx)}" cy="{f(y)}" rx="{f(lw * 0.62)}" ry="{f(h * 0.065)}" fill="none" stroke="{col}" stroke-width="5"></ellipse>')
        else:
            o.append(f'<ellipse cx="{f(cx)}" cy="{f(y)}" rx="{f(lw * 0.62)}" ry="{f(h * 0.02)}" fill="none" stroke="{col}" stroke-width="5"></ellipse>')
    for xx in (x0 - 10, x1 + 10):
        o.append(f'<rect x="{f(xx - 6)}" y="{f(y - h * 0.14)}" width="12" height="{f(h * 0.42)}" fill="#3A5A7A" stroke="{CY}" stroke-width="1.4"></rect>')
    bx = x0 + lw * 6.5
    o.append(tag(bx, y + h * 0.07, "ONE POINT", bx + w * 0.08, y + h * 0.22, color="#FF6A4A", size=10))
    o.append(dim(x0, y + h * 0.34, x1, y + h * 0.34, "THE WHOLE LAW", size=10, color=CY))
    o.append(label(w * 0.5, h * 0.94, "ONE LAWGIVER · THE ROYAL LAW · THE LAW OF LIBERTY", "#C8D8E8", 9))
    return "".join(o)

def sent_away(p, w, h, seed):
    """If a brother or sister be naked and in lack of daily food, and one of you say unto them, Go in peace, be ye warmed
    and filled: a cold night street, a well-fed man at the lit door of his house, his hand raised in farewell; the brother
    and sister in thin, ragged clothes going away empty-handed."""
    bg, b = _street(w, h, seed, "night")
    s = fit(b, max(h * 0.16, b - 225))
    o = [D_(p), bg]
    hx, hw = w * 0.04, w * 0.32
    o.append(f'<rect x="{f(hx)}" y="{f(b - 230 * s)}" width="{f(hw)}" height="{f(230 * s)}" fill="#8A7A6A" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<rect x="{f(hx + hw * 0.5)}" y="{f(b - 170 * s)}" width="{f(hw * 0.34)}" height="{f(170 * s)}" fill="#FFC14D" stroke="{INK}" stroke-width="2"></rect>'
             + lamp_glow(hx + hw * 0.67, b - 90 * s, 120 * s, f"{p}dg", op=0.5))
    o.append(robed(p, hx + hw * 0.67, b, s, "#8A5A3A", head="#E8E2D6", cord="#6A4A2A", beard="#2A1A10", mantle="#5A3A2A", belt="#E8B830",
                   flip=True, up=[(-22, -158), (-36, -190), (-36, -214)]))
    r = random.Random(seed)
    for i in range(14):                                              # the cold: frost in the air
        o.append(f'<circle cx="{f(w * r.uniform(0.4, 1.0))}" cy="{f(h * r.uniform(0.05, 0.6))}" r="1.8" fill="#E8F0F8" opacity="0.7"></circle>')
    o.append(poor_man(p, w * 0.6, b, s * 0.96, flip=True))
    o.append(poor_woman(p, w * 0.74, b, s * 0.96, flip=True))
    o.append(plate_label(w * 0.34, h * 0.1, "GO IN PEACE, BE YE WARMED AND FILLED", "#FFE6A0", 9, halo_="#0B0B2A"))
    return "".join(o)

def ram_thicket(x, y, s=1.0):
    """A ram caught in a thicket by his horns, (x, y) its feet."""
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">',
         '<path d="M-64 0 C -74 -44 -52 -76 -20 -82 C 10 -102 44 -86 60 -64 C 78 -42 74 -10 66 0 Z" fill="#3A5A2A" stroke="#0D0D0F" stroke-width="2.4"></path>',
         '<path d="M-20 -26 L -22 0 M-6 -24 L -6 0 M18 -24 L 20 0 M30 -28 L 32 0" stroke="#3A3A3A" stroke-width="3.4"></path>',
         '<path d="M-32 -36 C -36 -52 -16 -60 10 -58 C 30 -58 40 -50 38 -36 C 36 -26 22 -22 4 -24 C -14 -22 -30 -26 -32 -36 Z" fill="#E8E2D6" stroke="#0D0D0F" stroke-width="2"></path>',
         '<path d="M30 -48 C 40 -56 52 -54 56 -46 C 58 -38 52 -32 42 -34 Z" fill="#D8D2C6" stroke="#0D0D0F" stroke-width="2"></path>',
         '<path d="M44 -52 C 38 -66 52 -72 58 -62 C 62 -54 54 -48 50 -52" fill="none" stroke="#8A6A3A" stroke-width="4.4"></path>',
         '<circle cx="48" cy="-44" r="1.8" fill="#0D0D0F"></circle>',
         '<path d="M-58 -52 C -40 -62 -20 -68 0 -82 M20 -86 C 36 -72 52 -74 68 -66 M50 -62 C 62 -72 72 -62 64 -50 M56 -58 L 72 -78" fill="none" stroke="#2A3A1A" stroke-width="2.6"></path>']
    return "".join(o) + "</g>"

def stone_altar(x, y, s=1.0, wood=True):
    """An altar of unhewn stones with the wood laid in order upon it, (x, y) its foot."""
    o = [f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})">']
    for row, (yy, n) in enumerate(((0, 5), (-22, 5), (-44, 4))):
        for k in range(n):
            xx = -60 + k * 24 + (row % 2) * 12
            o.append(f'<path d="M{xx} {yy} L {xx + 2} {yy - 20} L {xx + 22} {yy - 21} L {xx + 23} {yy} Z" fill="{["#9A8A7A", "#8A7A6A", "#A89888"][(k + row) % 3]}" stroke="#0D0D0F" stroke-width="1.8"></path>')
    if wood:
        for k in range(4):
            o.append(f'<rect x="-56" y="{-72 - k * 7}" width="112" height="7" rx="3" fill="#7A4A22" stroke="#0D0D0F" stroke-width="1.4" transform="rotate({(-1) ** k * 3} 0 {-68 - k * 7})"></rect>')
    return "".join(o) + "</g>"

def akedah(p, w, h, seed):
    """Abraham offered up Isaac his son upon the altar (Genesis 22): the top of the mount in the land of Moriah at dawn, the
    altar built and the wood laid in order, Isaac standing by it, Abraham with his hand lifted to heaven, and behind them a
    ram caught in the thicket by his horns (no knife drawn)."""
    b = h * 0.9
    o = [D_(p), sky(w, h, "#3A2A6A", "#FFB07A"), halo(w * 0.7, h * 0.5, h * 0.6, "#FFE680", 0.5),
         hills(w, h, h * 0.62, seed, color="#5A4A6A", amp=14, step=90),
         f'<path d="M-10 {f(h + 10)} L -10 {f(b - h * 0.04)} C {f(w * 0.25)} {f(b - h * 0.1)} {f(w * 0.7)} {f(b - h * 0.1)} {f(w + 10)} {f(b - h * 0.02)} L {f(w + 10)} {f(h + 10)} Z" fill="#7A5A3A" stroke="{INK}" stroke-width="2"></path>']
    s = fit(b, max(h * 0.26, b - 200))
    o.append(stone_altar(w * 0.48, b - 2, s * 0.9))
    o.append(abraham_r(p, w * 0.28, b, s, flip=False, up=UP_HEAVEN))
    o.append(isaac_r(p, w * 0.64, b, s * 0.78, flip=True))
    o.append(ram_thicket(w * 0.85, b - 2, s * 0.85))
    o.append(plate_label(w * 0.5, h * 0.09, "IN THE MOUNT OF JEHOVAH IT SHALL BE PROVIDED", "#3A1A2A", 9, halo_="#FFE0B0"))
    return "".join(o)

def rahab_window(p, w, h, seed):
    """Rahab received the messengers, and sent them out another way: Jericho's wall by night, her house upon the wall with
    the lit window and the scarlet cord hanging from it (Joshua 2), and the two messengers going away along the foot of the
    wall toward the mountain."""
    b = h * 0.92
    o = [D_(p), sky(w, h, "#0B0B2A", "#2A2050"), mk.stars(40, w, h * 0.4, seed),
         f'<path d="M{f(w * 0.56)} {f(h * 0.66)} L {f(w * 0.8)} {f(h * 0.3)} L {f(w + 10)} {f(h * 0.46)} L {f(w + 10)} {f(h * 0.72)} Z" fill="#2A2440" stroke="{INK}" stroke-width="2"></path>',
         ground(w, h, b, "#3A3440", dy=0)]
    wx0, wx1, wt = -10, w * 0.6, h * 0.18                           # the wall, the house built on it
    o.append(f'<rect x="{f(wx0)}" y="{f(wt)}" width="{f(wx1 - wx0)}" height="{f(b - wt)}" fill="#8A6A4A" stroke="{INK}" stroke-width="2.4"></rect>')
    for k in range(1, 9):
        y = wt + (b - wt) * k / 9
        o.append(f'<path d="M{f(wx0)} {f(y)} L {f(wx1)} {f(y)}" stroke="#6A4A2A" stroke-width="1.4"></path>')
    o.append("".join(f'<rect x="{f(x)}" y="{f(wt - 14)}" width="18" height="14" fill="#8A6A4A" stroke="{INK}" stroke-width="2"></rect>' for x in range(0, int(wx1) - 10, 36)))
    hx, hy, hw, hh = w * 0.28, wt + (b - wt) * 0.14, w * 0.11, (b - wt) * 0.3
    o.append(f'<rect x="{f(hx)}" y="{f(hy)}" width="{f(hw)}" height="{f(hh)}" fill="#FFC14D" stroke="{INK}" stroke-width="2.4"></rect>'
             + lamp_glow(hx + hw / 2, hy + hh / 2, hh * 1.2, f"{p}rw", op=0.4))
    hs = hh / 80                                                    # Rahab at her window: head and shoulders, her scarlet veil
    o.append(f'<defs><clipPath id="{p}rc"><rect x="{f(hx)}" y="{f(hy)}" width="{f(hw)}" height="{f(hh)}"></rect></clipPath></defs>'
             f'<g clip-path="url(#{p}rc)">' + robed(p, hx + hw * 0.5, hy + hh + 125 * hs, hs, "#8A2A2A", woman=True, veil="#B5121B") + '</g>')
    o.append(f'<rect x="{f(hx - 6)}" y="{f(hy + hh)}" width="{f(hw + 12)}" height="7" fill="#5A3A22" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<path d="M{f(hx + hw * 0.85)} {f(hy + hh + 4)} C {f(hx + hw * 0.98)} {f(hy + hh + (b - hy) * 0.25)} {f(hx + hw * 0.8)} {f(hy + hh + (b - hy) * 0.42)} {f(hx + hw * 0.92)} {f(b - (b - hy) * 0.16)}" '
             f'fill="none" stroke="#D7261E" stroke-width="4" stroke-linecap="round"></path>')
    s = fit(b, max(h * 0.24, b - 190))
    o.append(robed(p, w * 0.66, b, s, "#5A5A4A", head="#3A3A2A", cord="#1A1210", beard="#2A1A10", flip=True, pose="walk"))
    o.append(robed(p, w * 0.78, b, s, "#4A4A5A", head="#2A2A3A", cord="#1A1210", beard="#3A2A1A", flip=True, pose="walk"))
    o.append(plate_label(w * 0.8, h * 0.16, "ANOTHER WAY", "#E8E2D6", 9, halo_="#0B0B2A") + plate_label(w * 0.3, h * 0.1, "JERICHO", "#FFE6A0", 9, halo_="#0B0B2A"))
    return "".join(o)
