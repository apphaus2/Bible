"""Drawings for Daniel chapter 5 (Daniel 9–10): the seventy years of Jeremiah as a chart, Daniel in sackcloth at his window,
Jerusalem's desolations, the sea divided (thou hast brought thy people forth out of the land of Egypt), Gabriel flying
swiftly at the time of the evening oblation (a figure of light), the seventy weeks as a chart, the great river Hiddekel and
the man clothed in linen (a figure of light girded with gold), and the princes of Persia and of Greece and Michael as a chart."""
from dan.art import *
from dan.art import f, K2
from dan.art3 import window_prayer
from neh.art import ruins, red_sea
import random, math

def seventy_years(w, h):
    """The number of the years by the books: Jeremiah's seventy years for the desolations of Jerusalem, as seventy marks."""
    o = [grid_bg(w, h)]
    for i in range(70):
        col, row = i % 35, i // 35
        x = w * 0.06 + col * w * 0.88 / 35; y = h * (0.34 + row * 0.2)
        o.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w * 0.88 / 35 * 0.7)}" height="{f(h * 0.14)}" fill="#FFD23F" fill-opacity="0.25" stroke="#FFD23F" stroke-width="1"></rect>')
    o.append(label(w * 0.5, h * 0.2, "THE WORD OF JEHOVAH TO JEREMIAH · SEVENTY YEARS", "#FFD23F", max(8, min(11, h / 20))))
    o.append(label(w * 0.5, h * 0.88, "FOR THE ACCOMPLISHING OF THE DESOLATIONS OF JERUSALEM", CYAN, max(8, min(10, h / 22))))
    return "".join(o)

def sackcloth(p, w, h, seed):
    """Daniel in sackcloth and ashes, kneeling at his window open toward Jerusalem, fasting."""
    o = window_prayer(p, w, h, seed).replace(f'fill="{DAN_C}"', 'fill="#6A5E4A"')
    r = random.Random(seed)
    o += "".join(f'<circle cx="{f(w * 0.52 + r.uniform(-30, 30))}" cy="{f(h * 0.86 + r.uniform(0, 8))}" r="{f(r.uniform(1.5, 3))}" fill="#8A847A"></circle>' for _ in range(24))
    return o

def gabriel_fly(p, w, h, seed):
    """About the time of the evening oblation: Gabriel, a figure of light, caused to fly swiftly, coming down to Daniel at
    prayer on his roof under the evening sky."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#3A2A5A", "#E8A06A"), sun(w * 0.12, h * 0.72, max(10, h * 0.05), color="#FF8A3D", op=0.3),
         f'<rect x="-10" y="{f(h * 0.8)}" width="{f(w + 20)}" height="{f(h * 0.22)}" fill="#8A6A4A" stroke="#0D0D0F" stroke-width="2"></rect>']
    s = fit(h * 0.8, h * 0.2)
    o.append(E.kneel(w * 0.36, h * 0.82, h * 0.36 / 130, color=DAN_C, skin="#C98E66"))
    gx, gy = w * 0.68, h * 0.62
    for i in range(5):
        o.append(f'<path d="M{f(gx + 30 + i * 14)} {f(gy - 150 * s - i * 10)} L {f(gx + 120 + i * 30)} {f(gy - 220 * s - i * 20)}" stroke="#FFF4C2" stroke-width="2.4" opacity="0.6"></path>')
    o.append(V.rays(gx, gy - 100 * s, 24, 20, w * 0.4, color="#FFF4C2", op=0.2) + glow_fig(gx, gy, s * 0.9))
    return "".join(o)

def weeks_chart(w, h):
    """Seventy weeks decreed: seven weeks, and threescore and two weeks, and one week, as a chart of seventy cells."""
    o = [grid_bg(w, h)]
    x0, ww = w * 0.05, w * 0.9
    cw = ww / 70
    y = h * 0.4
    for i in range(70):
        c = "#8FD0E2" if i < 7 else "#FFD23F" if i < 69 else "#FF8A6A"
        o.append(f'<rect x="{f(x0 + i * cw)}" y="{f(y)}" width="{f(cw * 0.8)}" height="{f(h * 0.2)}" fill="{c}" fill-opacity="0.3" stroke="{c}" stroke-width="1"></rect>')
    for a, b, t, c in ((0, 7, "SEVEN WEEKS", "#8FD0E2"), (7, 69, "THREESCORE AND TWO WEEKS", "#FFD23F"), (69, 70, "ONE WEEK", "#FF8A6A")):
        o.append(dim(x0 + a * cw, y - h * 0.06, x0 + b * cw - cw * 0.2, y - h * 0.06, "", color=c) + label(x0 + (a + b) / 2 * cw, y - h * 0.1, t, c, max(7, min(10, h / 24))))
    o.append(label(w * 0.5, h * 0.14, "SEVENTY WEEKS ARE DECREED UPON THY PEOPLE AND UPON THY HOLY CITY", "#F3EFE6", max(8, min(10, h / 24))))
    o.append(label(x0 + 3.5 * cw, h * 0.74, "TO RESTORE AND TO BUILD JERUSALEM", "#8FD0E2", 8, anchor="start") + label(x0 + 69.5 * cw, h * 0.74, "IN THE MIDST OF THE WEEK", "#FF8A6A", 8, anchor="end"))
    return "".join(o)

def hiddekel(p, w, h, seed, stage="see"):
    """By the side of the great river, Hiddekel: the man clothed in linen as a tall figure of light girded with gold, his face
    as lightning (drawn only as light). stage "see": Daniel standing, the men with him; "fled": the men fled to hide
    themselves, Daniel fallen on his face; "knees": Daniel set upon his knees and the palms of his hands; "stand": Daniel
    standing trembling."""
    o = [mk.defs(p, *ALL), K2.sky(w, h, "#5A7AA8", "#E8E2D6"), ground(w, h, h * 0.62, "#8A9A6A", dy=0),
         f'<path d="M-10 {f(h * 0.66)} C {f(w * 0.3)} {f(h * 0.62)} {f(w * 0.7)} {f(h * 0.72)} {f(w + 10)} {f(h * 0.66)} L {f(w + 10)} {f(h * 0.8)} C {f(w * 0.7)} {f(h * 0.86)} {f(w * 0.3)} {f(h * 0.76)} -10 {f(h * 0.8)} Z" fill="#2C7DA0" stroke="#0D0D0F" stroke-width="2"></path>']
    s = fit(h * 0.95, h * 0.2)
    gx = w * 0.7
    o.append(V.rays(gx, h * 0.35, 30, 20, w * 0.6, color="#FFF4C2", op=0.25) + glow_fig(gx, h * 0.68, s * 1.05))
    o.append(f'<rect x="{f(gx - 26 * s)}" y="{f(h * 0.68 - 104 * s)}" width="{f(52 * s)}" height="{f(8 * s)}" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.4"></rect>')
    b = h * 0.97
    if stage == "see":
        o.append(dan_fig(p, w * 0.24, b, s * 0.9, age=3))
        for i in range(2): o.append(man(p, w * (0.08 + i * 0.06), b, s * 0.86, ("#5A4A3A", "#6A5A4A")[i]))
    if stage == "fled":
        o.append(N.prostrate(w * 0.3, b, s * 0.7, color=DAN_C, skin="#C98E66"))
        for i in range(3): o.append(man(p, w * (0.04 + i * 0.05), b - 10, s * 0.7, ("#5A4A3A", "#6A5A4A", "#4A3A2A")[i], flip=True))
    if stage == "knees":
        o.append(E.kneel(w * 0.32, b, s * 1.2, color=DAN_C, skin="#C98E66"))
    if stage == "stand":
        o.append(dan_fig(p, w * 0.32, b, s * 0.9, age=3))
    return "".join(o)

def princes_chart(w, h):
    """The warfare in the heavens as a chart: the prince of the kingdom of Persia withstanding one and twenty days, Michael
    one of the chief princes coming to help; afterward the prince of Greece."""
    o = [grid_bg(w, h)]
    o.append(node(w * 0.5, h * 0.5, "THE MESSENGER", "#FFF4C2", r=8, dy=-14, size=10))
    o.append(node(w * 0.16, h * 0.5, "THE PRINCE OF PERSIA", "#FF8A6A", r=7, dy=-14, size=9))
    o.append(node(w * 0.84, h * 0.5, "THE PRINCE OF GREECE", "#FF8A6A", r=7, dy=-14, size=9))
    o.append(node(w * 0.5, h * 0.84, "MICHAEL · YOUR PRINCE", "#FFD23F", r=7, dy=20, size=9))
    o.append(route([(w * 0.46, h * 0.5), (w * 0.2, h * 0.5)], color="#FF8A6A") + route([(w * 0.5, h * 0.8), (w * 0.5, h * 0.56)], color="#FFD23F")
             + route([(w * 0.54, h * 0.5), (w * 0.8, h * 0.5)], color="#FF8A6A", arrow=False))
    o.append(label(w * 0.33, h * 0.44, "WITHSTOOD ME 21 DAYS", "#FF8A6A", 8) + label(w * 0.67, h * 0.44, "SHALL COME", "#FF8A6A", 8))
    return "".join(o)

def jerusalem_desolate(w, h, seed):
    """Thy sanctuary that is desolate: Jerusalem's walls broken and the gates burned, seen from without."""
    return ruins(w, h, seed)

def exodus_sea(w, h, seed):
    return red_sea(w, h, seed)

def law_scroll(w, h, seed):
    """The curse and the oath written in the law of Moses: an open scroll."""
    return letter_scroll(w, h, seed, seal="#5A3A22", text_lines=9)

from ezr.art import letter_scroll
