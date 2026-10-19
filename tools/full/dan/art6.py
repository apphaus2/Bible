"""Drawings for Daniel chapter 6 (Daniel 11–12): the kings of the north and of the south as a technical map, lit by stage,
and a board of their turns; the time of the end; Michael standing up; them that sleep in the dust awaking, the wise
shining as the brightness of the firmament; the book shut up and sealed; the two on the banks and the man clothed in linen
above the waters (a figure of light, both hands held up unto heaven); the twelve hundred and ninety and the thirteen hundred
and five and thirty days as a chart."""
from dan.art import *
from dan.art import f, K2
from dan.art5 import hiddekel
from neh.art import sealed_scroll
import random, math

PLACES = {"NORTH": (0.62, 0.12), "SOUTH": (0.36, 0.86), "LAND": (0.46, 0.46), "PERSIA": (0.92, 0.3), "GREECE": (0.08, 0.24), "ISLES": (0.18, 0.34),
          "KITTIM": (0.2, 0.48), "EDOM": (0.6, 0.7), "MOAB": (0.68, 0.56), "AMMON": (0.76, 0.42), "EGYPT": (0.32, 0.78), "LIBYANS": (0.12, 0.84), "ETHIOPIANS": (0.42, 0.97)}
NAMES = {"NORTH": "THE KING OF THE NORTH", "SOUTH": "THE KING OF THE SOUTH", "LAND": "THE GLORIOUS LAND", "PERSIA": "PERSIA", "GREECE": "GREECE",
         "ISLES": "THE ISLES", "KITTIM": "SHIPS OF KITTIM", "EDOM": "EDOM", "MOAB": "MOAB", "AMMON": "AMMON", "EGYPT": "EGYPT", "LIBYANS": "THE LIBYANS",
         "ETHIOPIANS": "THE ETHIOPIANS"}

def north_south(w, h, show=("NORTH", "SOUTH", "LAND"), moves=(), hi=(), note=""):
    """The map: the great sea on the west, the king of the north above, the king of the south below, the glorious land
    between; moves = [(from, to, colour)] drawn as arrows; hi = places lit red."""
    o = [grid_bg(w, h)]
    o.append(f'<path d="M-10 -10 L {f(w * 0.26)} -10 C {f(w * 0.3)} {f(h * 0.3)} {f(w * 0.32)} {f(h * 0.5)} {f(w * 0.26)} {f(h * 0.66)} C {f(w * 0.2)} {f(h * 0.72)} {f(w * 0.1)} {f(h * 0.72)} -10 {f(h * 0.7)} Z" '
             f'fill="#0F3A5A" stroke="#8FD0E2" stroke-width="2"></path>' + label(w * 0.03, h * 0.62, "THE GREAT SEA", CYAN, 8, anchor="start"))
    o.append(f'<path d="M{f(w * 0.44)} {f(h + 10)} C {f(w * 0.42)} {f(h * 0.9)} {f(w * 0.36)} {f(h * 0.8)} {f(w * 0.3)} {f(h * 0.7)}" stroke="#2C9DB8" stroke-width="3" fill="none"></path>')
    for key in show:
        x, y = PLACES[key]
        big = key in ("NORTH", "SOUTH")
        c = "#FF8A6A" if key in hi else "#FFD23F" if big or key == "LAND" else CYAN
        o.append(node(w * x, h * y, NAMES[key], c, r=8 if big else 5, dy=-12 if y > 0.12 else 18, size=10 if big else 8))
    for a, b, c in moves:
        (x0, y0), (x1, y1) = PLACES[a], PLACES[b]
        o.append(route([(w * x0, h * y0), (w * (x0 + x1) / 2 + w * 0.05, h * (y0 + y1) / 2), (w * x1, h * y1)], color=c))
    if note: o.append(label(w * 0.98, h * 0.08, note, "#F3EFE6", 8, anchor="end"))
    return "".join(o)

def turns(w, h, seq, lit):
    """A board of turns: each cell an arrow, the king of the north against the south (down) or the south against the north
    (up); the current turn lit."""
    o = [grid_bg(w, h)]
    n = len(seq)
    cw = w * 0.9 / n
    for i, t in enumerate(seq):
        x = w * 0.05 + i * cw; cx = x + cw / 2
        on = i == lit
        o.append(f'<rect x="{f(x + 3)}" y="{f(h * 0.2)}" width="{f(cw - 6)}" height="{f(h * 0.6)}" fill="{"#D7261E" if on else "#12113A"}" fill-opacity="{0.5 if on else 0.6}" stroke="{"#FFD23F" if on else "#1E5A7A"}" stroke-width="{2 if on else 1.2}"></rect>')
        if t in ("N", "S"):
            y0, y1 = (h * 0.3, h * 0.7) if t == "N" else (h * 0.7, h * 0.3)
            o.append(route([(cx, y0), (cx, y1)], color="#FFD23F" if on else "#5A7A9A"))
        else:
            o.append(f'<circle cx="{f(cx)}" cy="{f(h * 0.5)}" r="{f(min(cw, h) * 0.12)}" fill="none" stroke="{"#FFD23F" if on else "#5A7A9A"}" stroke-width="2"></circle>')
        o.append(label(cx, h * 0.92, str(i + 1), "#FFD23F" if on else "#5A7A9A", 8))
    o.append(label(w * 0.05, h * 0.13, "NORTH", CYAN, 8, anchor="start") + label(w * 0.05, h * 0.99, "SOUTH", CYAN, 8, anchor="start"))
    return "".join(o)

def firmament(w, h, seed):
    """Many of them that sleep in the dust of the earth shall awake; they that are wise shall shine as the brightness of the
    firmament, and as the stars for ever and ever: the dark earth below, lights rising from it into a sky of stars."""
    r = random.Random(seed)
    o = [K2.sky(w, h, "#0B0B2A", "#3A2A5A"), mk.stars(80, w, h * 0.6, seed), hills(w, h, h * 0.78, seed, "#2A2230", amp=8, step=80), ground(w, h, h * 0.84, "#3A3034", dy=0)]
    for i in range(22):
        x = r.uniform(0.04, 0.96) * w; y0 = h * r.uniform(0.82, 0.96); y1 = h * r.uniform(0.12, 0.6)
        o.append(f'<path d="M{f(x)} {f(y0)} L {f(x)} {f(y1)}" stroke="#FFF4C2" stroke-width="1.4" opacity="0.4" stroke-dasharray="2 5"></path>'
                 f'<circle cx="{f(x)}" cy="{f(y1)}" r="{f(r.uniform(2, 4))}" fill="#FFF4C2"></circle><circle cx="{f(x)}" cy="{f(y1)}" r="{f(r.uniform(7, 12))}" fill="#FFF4C2" opacity="0.2"></circle>')
    o.append(V.rays(w * 0.5, -h * 0.1, 30, 20, h * 0.8, color="#FFF4C2", op=0.1))
    return "".join(o)

def michael(w, h, seed):
    """At that time shall Michael stand up, the great prince: a tall shape of light over the people, a book open below."""
    o = [K2.sky(w, h, "#1A1A4A", "#5A4A7A"), ground(w, h, h * 0.84, "#4A4A5A", dy=0)]
    s = h * 0.6 / 200
    o.append(V.rays(w * 0.5, h * 0.3, 30, 20, w * 0.6, color="#FFF4C2", op=0.22) + glow_fig(w * 0.5, h * 0.8, s))
    k = min(1.2, h / 260)
    o.append(f'<path d="M{f(w * 0.8 - 40 * k)} {f(h * 0.92)} L {f(w * 0.8)} {f(h * 0.92 + 8 * k)} L {f(w * 0.8 + 40 * k)} {f(h * 0.92)} L {f(w * 0.8 + 40 * k)} {f(h * 0.92 - 26 * k)} L {f(w * 0.8)} {f(h * 0.92 - 18 * k)} L {f(w * 0.8 - 40 * k)} {f(h * 0.92 - 26 * k)} Z" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="2"></path>')
    o.append(label(w * 0.8, h * 0.98, "WRITTEN IN THE BOOK", "#F3EFE6", 8))
    return "".join(o)

def two_banks(p, w, h, seed):
    """Other two standing, one on the brink of the river on this side, one on that side; the man clothed in linen above the
    waters, both hands held up unto heaven (all three shapes of light); Daniel watching."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A7AA8", "#E8E2D6"), ground(w, h, h * 0.6, "#8A9A6A", dy=0),
         f'<path d="M-10 {f(h * 0.66)} L {f(w + 10)} {f(h * 0.66)} L {f(w + 10)} {f(h * 0.84)} L -10 {f(h * 0.84)} Z" fill="#2C7DA0" stroke="#0D0D0F" stroke-width="2"></path>']
    s = fit(h * 0.66, h * 0.16)
    o.append(glow_fig(w * 0.14, h * 0.66, s * 0.8) + glow_fig(w * 0.86, h * 0.86, s * 0.8))
    gx, gy = w * 0.5, h * 0.6
    o.append(V.rays(gx, h * 0.2, 30, 20, w * 0.5, color="#FFF4C2", op=0.25) + glow_fig(gx, gy, s))
    for sx in (-1, 1):
        o.append(f'<path d="M{f(gx + sx * 14 * s)} {f(gy - 150 * s)} L {f(gx + sx * 40 * s)} {f(gy - 210 * s)}" stroke="#FFFFFF" stroke-width="{f(10 * s)}" stroke-linecap="round"></path>')
    o.append(dan_fig(p, w * 0.32, h * 0.98, s * 0.6, age=3))
    return "".join(o)

def days_chart(w, h):
    """From the continual burnt-offering taken away: a thousand two hundred and ninety days; blessed is he that waiteth to the
    thousand three hundred and five and thirty days."""
    o = [grid_bg(w, h)]
    x0, ww = w * 0.06, w * 0.86
    for i, (n, t, c) in enumerate(((1290, "1,290 DAYS", "#FFD23F"), (1335, "1,335 DAYS · BLESSED IS HE THAT WAITETH", "#8FD0E2"))):
        y = h * (0.3 + i * 0.3)
        o.append(f'<rect x="{f(x0)}" y="{f(y)}" width="{f(ww * n / 1335)}" height="{f(h * 0.14)}" fill="{c}" fill-opacity="0.3" stroke="{c}" stroke-width="2"></rect>'
                 + label(x0, y - 8, t, c, max(8, min(10, h / 22)), anchor="start"))
    o.append(dim(x0 + ww * 1290 / 1335, h * 0.86, x0 + ww, h * 0.86, "45", color="#F3EFE6"))
    return "".join(o)

def rest(w, h, seed):
    """Go thou thy way till the end be: the great river at evening, the sun going down, all still."""
    o = [K2.sky(w, h, "#3A2A5A", "#FFB070"), sun(w * 0.5, h * 0.62, max(12, h * 0.07), color="#FFC14D", op=0.35),
         f'<path d="M-10 {f(h * 0.64)} L {f(w + 10)} {f(h * 0.64)} L {f(w + 10)} {f(h + 10)} L -10 {f(h + 10)} Z" fill="#3A4A6A" stroke="#0D0D0F" stroke-width="2"></path>']
    for i in range(6):
        o.append(f'<path d="M{f(w * 0.5 - (30 - i * 4) * 2)} {f(h * (0.68 + i * 0.05))} l {f((30 - i * 4) * 4)} 0" stroke="#FFC14D" stroke-width="2" opacity="0.6"></path>')
    o.append(J1.palm(w * 0.1, h * 0.66, min(0.8, h / 400)) + J1.palm(w * 0.9, h * 0.66, min(0.7, h / 420)))
    return "".join(o)

def shut_book(w, h, seed):
    return sealed_scroll(w, h, seed, n=7)
