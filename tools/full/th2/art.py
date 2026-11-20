"""Drawings for the 2 Thessalonians volume. 2 Thessalonians starts from 1 Thessalonians' drawings (`from th1.art import *`,
which carries Galatians', Acts', Mark's and Matthew's drawings and the epistle kit) and adds its own. The cast is 1
Thessalonians' (Silvanus, Timothy, Jason, the Thessalonians); God is never drawn (light); the angels of 1:7 are not drawn,
only fire and light; the man of sin and Satan are never drawn. Every function takes (p, w, h, seed, ...) or (w, h, ...)."""
import sys, pathlib, math, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from th1.art import *
from th1.art import f, INK, sky_, fig_s, _defs, plate_label, night_window, art
from epistle import open_letter, sealed_scroll, inkpot, reed_pen, low_table
from ntcast import ROBES
from genesis.art4 import clay_lamp
from jer.art import glow
from oba.minor import halo, rays, starfield
from mat.art import room, houses, bgr
from genesis.art2 import hills, ground

GOLD, CY = "#FFD23F", "#8FD0E2"

# ---- 2 Thessalonians 1 ----------------------------------------------------------------------------------------------------
def balance(cx, cy, R, tilt=0.0, color="#E8B830"):
    """A balance of gold: the post, the beam (tilted by `tilt` radians) and the two pans on their cords."""
    o = [f'<path d="M{f(cx)} {f(cy - R * 0.9)} L {f(cx)} {f(cy + R * 0.9)} M{f(cx - R * 0.36)} {f(cy + R * 0.9)} L {f(cx + R * 0.36)} {f(cy + R * 0.9)}" stroke="{color}" stroke-width="{f(max(3, R * 0.06))}" stroke-linecap="round"></path>',
         f'<circle cx="{f(cx)}" cy="{f(cy - R * 0.92)}" r="{f(R * 0.06)}" fill="{color}" stroke="{INK}" stroke-width="1.4"></circle>']
    dx, dy = R * math.cos(tilt), R * math.sin(tilt)
    o.append(f'<path d="M{f(cx - dx)} {f(cy - R * 0.7 - dy)} L {f(cx + dx)} {f(cy - R * 0.7 + dy)}" stroke="{color}" stroke-width="{f(max(3, R * 0.05))}" stroke-linecap="round"></path>')
    for sg in (-1, 1):
        px, py = cx + sg * dx, cy - R * 0.7 + sg * dy
        o.append(f'<path d="M{f(px)} {f(py)} L {f(px - R * 0.26)} {f(py + R * 0.5)} M{f(px)} {f(py)} L {f(px + R * 0.26)} {f(py + R * 0.5)}" stroke="{color}" stroke-width="1.6"></path>'
                 f'<path d="M{f(px - R * 0.32)} {f(py + R * 0.5)} Q {f(px)} {f(py + R * 0.78)} {f(px + R * 0.32)} {f(py + R * 0.5)} Z" fill="{color}" stroke="{INK}" stroke-width="1.8"></path>')
    return "".join(o)

def judgment_balance(w, h, seed):
    """A manifest token of the righteous judgment of God: a balance of gold, level, in a light above the roofs of the city
    at night (no figure)."""
    o = [sky_(w, h, "#0B0B2A", "#2A2050"), starfield(w, h, seed, 36, 0.5), halo(w * 0.5, h * 0.44, max(w, h) * 0.36, "#FFE680", 0.55),
         rays(w * 0.5, h * 0.44, 28, h * 0.18, max(w, h), "#FFF4C2", 0.22, 4)]
    o.append(balance(w * 0.5, h * 0.46, min(h * 0.36, w * 0.2)))
    o.append(houses(w, h, h * 1.0, seed, hmin=0.12, hmax=0.22, lit=True, color=("#3A3050", "#2E2840", "#443A5A", "#382E4A"), stairs=False))
    return "".join(o)

def flaming_fire(w, h, seed):
    """At the revelation of the Lord Jesus from heaven with the angels of his power in flaming fire: the heavens opened in
    white light at the top of the sky, a curtain of flame falling from it on every side; below, an empty plain under the fire,
    no one on it (no figure in the light; the angels are not drawn)."""
    r = random.Random(seed)
    o = [sky_(w, h, "#FFF4C2", "#5A1A1A"), halo(w * 0.5, h * 0.02, max(w, h) * 0.7, "#FFFFFF", 0.85),
         rays(w * 0.5, -h * 0.05, 44, h * 0.1, max(w, h) * 1.3, "#FFFDF0", 0.32, 5)]
    for i in range(int(w / 26) + 2):                                     # the curtain of flame
        x = i * 26 + r.uniform(-8, 8)
        top = h * r.uniform(0.18, 0.3); bot = h * r.uniform(0.5, 0.62)
        wd = r.uniform(14, 26)
        o.append(f'<path d="M{f(x - wd / 2)} {f(bot)} C {f(x - wd)} {f(bot - (bot - top) * 0.5)} {f(x + wd * 0.3)} {f(top + (bot - top) * 0.3)} {f(x)} {f(top)} '
                 f'C {f(x + wd * 0.2)} {f(top + (bot - top) * 0.4)} {f(x + wd)} {f(bot - (bot - top) * 0.4)} {f(x + wd / 2)} {f(bot)} Z" fill="{r.choice(["#FF6A2A", "#FF8A2A", "#E8501E"])}" opacity="0.85"></path>'
                 f'<path d="M{f(x - wd / 4)} {f(bot)} C {f(x - wd / 3)} {f(bot - (bot - top) * 0.3)} {f(x)} {f(top + (bot - top) * 0.45)} {f(x)} {f(top + (bot - top) * 0.3)} '
                 f'C {f(x + wd * 0.1)} {f(top + (bot - top) * 0.5)} {f(x + wd / 3)} {f(bot - (bot - top) * 0.3)} {f(x + wd / 4)} {f(bot)} Z" fill="#FFD23F" opacity="0.9"></path>')
    o.append(f'<path d="M-10 {f(h * 0.6)} L {f(w + 10)} {f(h * 0.6)}" stroke="#FFC14D" stroke-width="3" opacity="0.6"></path>')
    o.append(hills(w, h, h * 0.62, seed, color="#3A1A18", amp=8, step=90) + ground(w, h, h * 0.7, "#2A1414", dy=0))
    for k in range(10):
        yy = h * r.uniform(0.74, 0.98); xx = w * r.uniform(0, 1)
        o.append(f'<path d="M{f(xx)} {f(yy)} l {f(r.uniform(10, 30))} 0" stroke="#5A2A1E" stroke-width="1.6"></path>')
    return "".join(o)

# ---- 2 Thessalonians 2 ----------------------------------------------------------------------------------------------------
def letter_as_from_us(p, w, h, seed):
    """Be not quickly shaken … by epistle as from us: Jason's house at night, a stranger at the open door holding out a
    rolled letter, Jason before him and the brethren standing behind, troubled, one with his hand lifted."""
    b = h * 0.92
    s = fig_s(h, 0.76, 260)
    o = [_defs(p), room(w, h, b, wall="#4A3A34", floor="#2E2420"), glow(w * 0.36, b - 120 * s, max(w, h) * 0.45, "#FFC14D", 0.34, f"{p}lg"),
         f'<rect x="{f(w * 0.08)}" y="{f(b - 236 * s)}" width="{f(80 * s)}" height="{f(8 * s)}" fill="#6A4A2A" stroke="{INK}" stroke-width="1.6"></rect>'
         + clay_lamp(w * 0.08 + 40 * s, b - 238 * s, max(0.6, s * 0.7))]
    dx, dw = w * 0.76, min(w * 0.18, 120 * s)                            # the door on the night street
    o.append(f'<rect x="{f(dx)}" y="{f(b - 206 * s)}" width="{f(dw)}" height="{f(206 * s)}" fill="#0B0B2A" stroke="{INK}" stroke-width="2.6"></rect>'
             + f'<g transform="translate({f(dx)} {f(b - 206 * s)})">' + mk.stars(8, dw, 90 * s, seed) + '</g>')
    scroll_ = '<g transform="translate(-74 -152) rotate(10)"><rect x="-16" y="-6" width="32" height="12" rx="2" fill="#EADBB4" stroke="#0D0D0F" stroke-width="1.4"></rect><circle cx="0" cy="3" r="4" fill="#3A3A44" stroke="#0D0D0F" stroke-width="1"></circle></g>'
    o.append(robed(p, dx + dw * 0.5, b, s, "#6A5A5A", head="#5A6A7A", cord="#1A1210", beard="#3A2A1A", mantle="#3A2E2E",
                   up=[(-22, -158), (-46, -150), (-70, -150)], extra=scroll_))
    o.append(jason_r(p, w * 0.58, b, s, flip=True))
    o.append(folk(p, w * 0.42, b, s * 0.98, 4, flip=True) + folk(p, w * 0.3, b, s, 0, flip=True, up=[(-22, -158), (-30, -186), (-26, -210)])
             + folk(p, w * 0.18, b, s * 0.98, 5, flip=True))
    return "".join(o)

def _sanctuary(w, h, b, seed, dark=True):
    """The inside of a temple: columns down both sides, the floor of stone flags, a dais at the back with steps."""
    o = [bgr(w, h, "#1A1018" if dark else "#3A2A30")]
    for i, x in enumerate((0.06, 0.2, 0.8, 0.94)):
        cw = w * (0.07 if i in (0, 3) else 0.05)
        o.append(f'<rect x="{f(w * x - cw / 2)}" y="{f(h * 0.04)}" width="{f(cw)}" height="{f(b - h * 0.04)}" fill="{"#3A2A34" if dark else "#6A5A60"}" stroke="{INK}" stroke-width="2"></rect>'
                 f'<rect x="{f(w * x - cw * 0.7)}" y="{f(h * 0.04)}" width="{f(cw * 1.4)}" height="{f(h * 0.04)}" fill="{"#4A3A44" if dark else "#7A6A70"}" stroke="{INK}" stroke-width="1.6"></rect>')
    o.append(f'<rect x="-10" y="{f(b)}" width="{f(w + 20)}" height="{f(h - b + 10)}" fill="{"#241820" if dark else "#4A3A40"}" stroke="{INK}" stroke-width="2"></rect>')
    for k in range(1, 6):
        o.append(f'<path d="M{f(w * 0.5 + (k - 3) * w * 0.12)} {f(b)} L {f(w * 0.5 + (k - 3) * w * 0.3)} {f(h + 10)}" stroke="#120C10" stroke-width="1.4"></path>')
    dw, dh = w * 0.36, h * 0.07                                          # the dais and its steps
    for k in range(3):
        o.append(f'<rect x="{f(w * 0.5 - dw / 2 + k * w * 0.02)}" y="{f(b - dh * (k + 1))}" width="{f(dw - k * w * 0.04)}" height="{f(dh)}" fill="{"#3A2A30" if dark else "#6A5A5A"}" stroke="{INK}" stroke-width="1.8"></rect>')
    return "".join(o), b - dh * 3

def seat(cx, base, s, color="#5A3A2A", gold="#8A6A2A", rot=0):
    """A great seat (a chair of state) with a high back and arms, empty; rot= degrees, turned over about its foot."""
    return (f'<g transform="translate({f(cx)} {f(base)}) rotate({rot}) scale({f(s)})">'
            '<path d="M-44 0 L -44 -70 L -54 -70 L -54 -86 L 54 -86 L 54 -70 L 44 -70 L 44 0 L 34 0 L 34 -50 L -34 -50 L -34 0 Z" fill="' + color + '" stroke="#0D0D0F" stroke-width="3"></path>'
            '<path d="M-38 -86 L -38 -190 C -38 -214 38 -214 38 -190 L 38 -86 Z" fill="' + color + '" stroke="#0D0D0F" stroke-width="3"></path>'
            '<path d="M-26 -96 L -26 -184 C -26 -200 26 -200 26 -184 L 26 -96 Z" fill="none" stroke="' + gold + '" stroke-width="3"></path>'
            '<rect x="-50" y="-60" width="100" height="10" fill="' + gold + '" stroke="#0D0D0F" stroke-width="1.6"></rect></g>')

def empty_seat(w, h, seed):
    """He sitteth in the temple of God, setting himself forth as God: the inside of a temple in shadow, the columns going
    up into the dark, and on a dais at the back a great seat, empty (the man of sin is never drawn: the words only)."""
    b = h * 0.9
    sc, top = _sanctuary(w, h, b, seed)
    s = min(h * 0.5, 200) / 210
    o = [sc, glow(w * 0.5, top - 100 * s, 160 * s, "#8A2A3A", 0.35, f"es{seed}"), seat(w * 0.5, top, s)]
    o.append(f'<path d="M-10 -10 L {f(w + 10)} -10 L {f(w + 10)} {f(h * 0.3)} C {f(w * 0.6)} {f(h * 0.2)} {f(w * 0.4)} {f(h * 0.2)} -10 {f(h * 0.3)} Z" fill="#05040A" opacity="0.6"></path>')
    return "".join(o)

def teaching(p, w, h, seed):
    """Remember ye not, that, when I was yet with you, I told you these things? The church in Jason's house by lamplight
    when Paul was with them, the brethren on the bench and Paul standing before them (1 Thessalonians' drawing)."""
    return jason_house(p, w, h, seed)

def light_breaks(w, h, seed):
    """Whom the Lord Jesus shall slay with the breath of his mouth, and bring to nought by the manifestation of his coming:
    the same dark sanctuary broken open by a great light pouring in from above, the seat thrown down off its dais and lying
    empty on the steps (no figure: the words only; Christ is not drawn, only the light)."""
    b = h * 0.9
    sc, top = _sanctuary(w, h, b, seed)
    s = min(h * 0.5, 200) / 210
    o = [sc, f'<path d="M{f(w * 0.36)} -10 L {f(w * 0.64)} -10 L {f(w * 0.84)} {f(h + 10)} L {f(w * 0.16)} {f(h + 10)} Z" fill="#FFF4C2" opacity="0.5"></path>',
         halo(w * 0.5, 0, max(w, h) * 0.6, "#FFFFFF", 0.8), rays(w * 0.5, -h * 0.05, 30, h * 0.1, max(w, h) * 1.2, "#FFFDF0", 0.32, 5)]
    o.append(seat(w * 0.66, b - h * 0.01, s * 0.9, rot=78))
    return "".join(o)

def traditions(w, h, seed):
    """Hold the traditions which ye were taught, whether by word, or by epistle of ours: on the table in lamplight the first
    epistle open, its lines of writing, and the second rolled and sealed beside it; the lamp and the inkpot."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#3A2418"></rect>', glow(w * 0.82, h * 0.3, max(w, h) * 0.45, "#FFC14D", 0.45, f"tr{seed}"),
         f'<rect x="-10" y="{f(h * 0.62)}" width="{f(w + 20)}" height="{f(h)}" fill="#6A4A2A" stroke="{INK}" stroke-width="2.4"></rect>']
    lw, lh = min(w * 0.46, h * 1.0), min(h * 0.52, w * 0.3)
    o.append(f'<g transform="rotate(-3 {f(w * 0.32)} {f(h * 0.6)})">' + open_letter(w * 0.32 - lw / 2, h * 0.7 - lh * 0.8, lw, lh, rows=7, seed=seed) + '</g>')
    s = min(h / 120, w / 300)
    o.append(sealed_scroll(w * 0.68, h * 0.78, s, rot=-6))
    o.append(clay_lamp(w * 0.86, h * 0.62, s * 0.8) + inkpot(w * 0.95, h * 0.66, s * 0.8))
    return "".join(o)

def word_runs(p, w, h, seed):
    """Pray for us, that the word of the Lord may run and be glorified: the road through the hills at morning, a messenger
    striding along it with the sealed roll in his hand, a city on its hill far off where the road is going."""
    b = h * 0.92
    s = fig_s(h, 0.7, 260)
    o = [_defs(p), sky_(w, h, "#6AB0D8", "#FFE8C0"), halo(w * 0.86, h * 0.3, h * 0.4, "#FFF4C2", 0.6),
         hills(w, h, h * 0.46, seed, color="#9A8A6A", amp=16, step=90), hills(w, h, h * 0.56, seed + 1, color="#B8A06A", amp=10, step=70),
         ground(w, h, h * 0.64, "#D8C08A", dy=0)]
    o.append(houses(w, h, h * 0.47, seed, x0=w * 0.78, x1=w * 0.98, hmin=0.05, hmax=0.08, stairs=False))
    o.append(f'<path d="M-10 {f(h + 10)} C {f(w * 0.3)} {f(h * 0.86)} {f(w * 0.6)} {f(h * 0.7)} {f(w * 0.84)} {f(h * 0.6)} L {f(w * 0.88)} {f(h * 0.62)} C {f(w * 0.64)} {f(h * 0.76)} {f(w * 0.4)} {f(h * 0.92)} {f(w * 0.2)} {f(h + 10)} Z" fill="#C8A878"></path>')
    roll = sealed_scroll(-58, -156, 0.32, rot=10)
    o.append(folk(p, w * 0.34, b, s, 5, flip=True, pose="walk", up=[(-22, -158), (-44, -150), (-54, -152)], extra=roll))
    return "".join(o)

# ---- 2 Thessalonians 3 ----------------------------------------------------------------------------------------------------
def bread(x, y, s=1.0):
    """A round loaf, scored."""
    return (f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(22 * s)}" ry="{f(12 * s)}" fill="#C8963E" stroke="{INK}" stroke-width="1.8"></ellipse>'
            f'<path d="M{f(x - 12 * s)} {f(y - 4 * s)} l {f(10 * s)} {f(-4 * s)} M{f(x + 2 * s)} {f(y - 2 * s)} l {f(10 * s)} {f(-4 * s)}" stroke="#8A5A22" stroke-width="1.4"></path>')

def work_bread(p, w, h, seed):
    """If any will not work, neither let him eat … that with quietness they work, and eat their own bread: a room at evening,
    a worker sitting at the table with his own bread before him, his mallet and chisel laid by on the bench; at the open door
    an idle man stands with empty hands, the street behind him."""
    b = h * 0.92
    s = fig_s(h, 0.78, 270)
    o = [_defs(p), room(w, h, b, wall="#8A6A4A", floor="#5A3E2A"), glow(w * 0.62, b - 110 * s, max(w, h) * 0.45, "#FFC14D", 0.36, f"{p}lg")]
    dx, dw = w * 0.08, min(w * 0.2, 130 * s)                             # the open door on the street at evening
    o.append(f'<defs><linearGradient id="{p}ev" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5A3A6A"></stop><stop offset="1" stop-color="#FFB07A"></stop></linearGradient></defs>'
             f'<rect x="{f(dx)}" y="{f(b - 210 * s)}" width="{f(dw)}" height="{f(210 * s)}" fill="url(#{p}ev)" stroke="{INK}" stroke-width="2.6"></rect>')
    o.append(folk(p, dx + dw * 0.5, b, s, 3, flip=True))
    tx, tw = w * 0.56, 150 * s                                            # the table, the bread and the cup
    o.append(f'<rect x="{f(tx - tw / 2)}" y="{f(b - 56 * s)}" width="{f(tw)}" height="{f(9 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="2"></rect>'
             + "".join(f'<rect x="{f(tx + k * (tw / 2 - 12 * s) - 4 * s)}" y="{f(b - 47 * s)}" width="{f(8 * s)}" height="{f(47 * s)}" fill="#4A2412" stroke="{INK}" stroke-width="1.4"></rect>' for k in (-1, 1))
             + bread(tx + 10 * s, b - 66 * s, s * 0.9) + f'<path d="M{f(tx - 40 * s)} {f(b - 56 * s)} L {f(tx - 44 * s)} {f(b - 78 * s)} L {f(tx - 24 * s)} {f(b - 78 * s)} L {f(tx - 28 * s)} {f(b - 56 * s)} Z" fill="#B5652E" stroke="{INK}" stroke-width="1.6"></path>')
    o.append(robed(p, tx + tw / 2 + 50 * s, b, s, "#7A5A3A", hair="#2A1A10", beard="#2A1A10", belt="#4A2E18", pose="sit",
                   up=[(-22, -158), (-50, -140), (-76, -146)]))
    rx, ry = tx - 10 * s, b - 170 * s                                        # his tools hung on the wall: a mallet and a chisel on their pegs
    o.append(f'<rect x="{f(rx - 46 * s)}" y="{f(ry)}" width="{f(92 * s)}" height="{f(7 * s)}" fill="#6A3A1E" stroke="{INK}" stroke-width="1.6"></rect>'
             f'<rect x="{f(rx - 34 * s)}" y="{f(ry + 7 * s)}" width="{f(26 * s)}" height="{f(14 * s)}" rx="{f(2 * s)}" fill="#8A6A3A" stroke="{INK}" stroke-width="1.4"></rect>'
             f'<path d="M{f(rx - 21 * s)} {f(ry + 21 * s)} L {f(rx - 21 * s)} {f(ry + 52 * s)}" stroke="#6A4A2A" stroke-width="{f(4 * s)}"></path>'
             f'<path d="M{f(rx + 16 * s)} {f(ry + 7 * s)} L {f(rx + 16 * s)} {f(ry + 30 * s)}" stroke="#6A4A2A" stroke-width="{f(5 * s)}"></path>'
             f'<path d="M{f(rx + 13 * s)} {f(ry + 30 * s)} L {f(rx + 19 * s)} {f(ry + 30 * s)} L {f(rx + 18 * s)} {f(ry + 56 * s)} L {f(rx + 16 * s)} {f(ry + 60 * s)} L {f(rx + 14 * s)} {f(ry + 56 * s)} Z" fill="#B8B8C0" stroke="{INK}" stroke-width="1.2"></path>')
    o.append(plate_label(dx + dw * 0.5, b - 220 * s, "IDLE HANDS", "#F3EFE6", 10, halo_="#3A2418") + plate_label(tx + 40 * s, b - 220 * s, "THEIR OWN BREAD", "#F3EFE6", 10, halo_="#3A2418"))
    return "".join(o)

def own_hand(w, h, seed):
    """The salutation of me Paul with mine own hand, which is the token in every epistle: so I write: close over the table,
    the foot of the sheet — the scribe's even lines of small writing, and under them a line in a larger, different hand still
    being written, Paul's hand with the reed pen at its end; the inkpot and the lamp."""
    o = [f'<rect x="-10" y="-10" width="{f(w + 20)}" height="{f(h + 20)}" fill="#4A2E1E"></rect>', glow(w * 0.88, h * 0.24, max(w, h) * 0.45, "#FFC14D", 0.5, f"oh{seed}")]
    sx, sy, sw, sh = w * 0.08, h * 0.08, w * 0.66, h * 0.86
    o.append(f'<g transform="rotate(-2 {f(sx + sw / 2)} {f(sy + sh / 2)})"><rect x="{f(sx)}" y="{f(sy)}" width="{f(sw)}" height="{f(sh)}" fill="#EADBB4" stroke="{INK}" stroke-width="2.4"></rect>'
             f'<path d="M{f(sx + sw * 0.33)} {f(sy)} L {f(sx + sw * 0.33)} {f(sy + sh)} M{f(sx + sw * 0.66)} {f(sy)} L {f(sx + sw * 0.66)} {f(sy + sh)}" stroke="#C8B488" stroke-width="1"></path>')
    r = random.Random(seed)
    for k in range(8):                                                    # the scribe's small even lines
        yy = sy + sh * (0.08 + k * 0.07); xx = sx + sw * 0.06
        while xx < sx + sw * 0.92:
            L = sw * r.uniform(0.04, 0.12)
            o.append(f'<path d="M{f(xx)} {f(yy)} l {f(min(L, sx + sw * 0.94 - xx))} 0" stroke="#4A3020" stroke-width="{f(max(1.2, h / 220))}"></path>'); xx += L + sw * 0.02
    B_ = sh * 0.1                                                          # Paul's own line: uncial strokes, larger and uneven (no words)
    yy = sy + sh * 0.74
    xx = sx + sw * 0.06
    shapes = [lambda x, y: f"M{f(x)} {f(y + B_)} L {f(x)} {f(y)} L {f(x + B_ * 0.6)} {f(y)} L {f(x + B_ * 0.6)} {f(y + B_)}",                 # Π
              lambda x, y: f"M{f(x)} {f(y + B_)} L {f(x + B_ * 0.35)} {f(y)} L {f(x + B_ * 0.7)} {f(y + B_)} M{f(x + B_ * 0.15)} {f(y + B_ * 0.6)} L {f(x + B_ * 0.55)} {f(y + B_ * 0.6)}",   # Α
              lambda x, y: f"M{f(x)} {f(y)} L {f(x + B_ * 0.35)} {f(y + B_ * 0.5)} L {f(x + B_ * 0.7)} {f(y)} M{f(x + B_ * 0.35)} {f(y + B_ * 0.5)} L {f(x + B_ * 0.35)} {f(y + B_)}",     # Υ
              lambda x, y: f"M{f(x)} {f(y + B_)} L {f(x + B_ * 0.35)} {f(y)} L {f(x + B_ * 0.7)} {f(y + B_)}",                                    # Λ
              lambda x, y: f"M{f(x + B_ * 0.35)} {f(y)} C {f(x - B_ * 0.05)} {f(y)} {f(x - B_ * 0.05)} {f(y + B_)} {f(x + B_ * 0.35)} {f(y + B_)} C {f(x + B_ * 0.75)} {f(y + B_)} {f(x + B_ * 0.75)} {f(y)} {f(x + B_ * 0.35)} {f(y)} Z",   # Ο
              lambda x, y: f"M{f(x + B_ * 0.65)} {f(y + B_ * 0.12)} C {f(x + B_ * 0.45)} {f(y - B_ * 0.05)} {f(x)} {f(y)} {f(x)} {f(y + B_ * 0.5)} C {f(x)} {f(y + B_)} {f(x + B_ * 0.45)} {f(y + B_ * 1.05)} {f(x + B_ * 0.65)} {f(y + B_ * 0.88)}"]   # C
    for i, sh_ in enumerate(shapes):
        dy = r.uniform(-B_ * 0.08, B_ * 0.08)
        o.append(f'<path d="{sh_(xx, yy + dy)}" stroke="#1A1008" stroke-width="{f(max(2.4, B_ * 0.1))}" fill="none" stroke-linecap="round" stroke-linejoin="round"></path>')
        xx += B_ * 0.95
    o.append('</g>')
    hx, hy = xx + B_ * 0.2, yy + B_ * 0.2                                 # the hand at the end of the line
    o.append(f'<path d="M{f(hx + 30)} {f(hy + 6)} C {f(hx + 80)} {f(hy + 20)} {f(hx + 140)} {f(hy + 40)} {f(w + 20)} {f(hy + 60)} L {f(w + 20)} {f(hy + 130)} C {f(hx + 140)} {f(hy + 110)} {f(hx + 80)} {f(hy + 80)} {f(hx + 34)} {f(hy + 50)} Z" '
             f'fill="{ROBES["paul"]}" stroke="{INK}" stroke-width="2.4"></path>'
             f'<path d="M{f(hx - 4)} {f(hy + 12)} C {f(hx - 6)} {f(hy - 2)} {f(hx + 8)} {f(hy - 10)} {f(hx + 24)} {f(hy - 6)} C {f(hx + 40)} {f(hy - 2)} {f(hx + 46)} {f(hy + 18)} {f(hx + 42)} {f(hy + 36)} '
             f'C {f(hx + 38)} {f(hy + 50)} {f(hx + 20)} {f(hy + 54)} {f(hx + 8)} {f(hy + 46)} C {f(hx)} {f(hy + 40)} {f(hx - 4)} {f(hy + 26)} {f(hx - 4)} {f(hy + 12)} Z" fill="#C98E66" stroke="{INK}" stroke-width="2.2"></path>'
             f'<path d="M{f(hx + 4)} {f(hy + 22)} C {f(hx + 10)} {f(hy + 26)} {f(hx + 14)} {f(hy + 34)} {f(hx + 12)} {f(hy + 42)} M{f(hx + 20)} {f(hy + 24)} C {f(hx + 26)} {f(hy + 30)} {f(hx + 28)} {f(hy + 38)} {f(hx + 26)} {f(hy + 48)}" fill="none" stroke="#7A4A2A" stroke-width="1.6"></path>'
             + reed_pen(hx - 2, hy + 4, max(0.8, h / 300), rot=-34))
    o.append(inkpot(w * 0.86, h * 0.72, max(1.0, h / 200)) + clay_lamp(w * 0.88, h * 0.4, max(1.0, h / 220)))
    return "".join(o)

def thess_dusk(w, h, seed):
    """Thessalonica on its gulf at dusk (the cover's view)."""
    return thess_view(w, h, seed, tone="dusk")
