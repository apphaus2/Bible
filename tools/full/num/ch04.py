"""Numbers volume, Chapter 4 — The Offerings of the Princes (Numbers 7–8). Every verse, word for word from ref/eng-asv.
The wagons; then the twelve days of the dedication of the altar, one prince a day, two days to a page — each day's six
verses in full over a strip of his oblation (num/art4.oblation); the totals; the Voice from above the mercy-seat; the
seven lamps; and the cleansing of the Levites."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import new, vref, page, chapter_title, end_mark, cols, cap, god
from exo import art8 as B8
from num import G, art as K, art4 as K4
from num.pages import Pages
from genesis import art as X
from genesis.ch02 import rows, grid, W1, W2, NIGHT, SKY
from genesis.ch03 import SAND, hud
from num import ch03 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
INK = B8.INK
DAYS = [("JUDAH", "NAHSHON"), ("ISSACHAR", "NETHANEL"), ("ZEBULUN", "ELIAB"), ("REUBEN", "ELIZUR"), ("SIMEON", "SHELUMIEL"), ("GAD", "ELIASAPH"),
        ("EPHRAIM", "ELISHAMA"), ("MANASSEH", "GAMALIEL"), ("BENJAMIN", "ABIDAN"), ("DAN", "AHIEZER"), ("ASHER", "PAGIEL"), ("NAPHTALI", "AHIRA")]
ORD = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH", "SIXTH", "SEVENTH", "EIGHTH", "NINTH", "TENTH", "ELEVENTH", "TWELFTH"]
KAN = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二"]

def day_tag(d, tribe, prince, pos):
    c = K.TRIBE_C[tribe]
    return (f'    <div data-label style="position: absolute; {pos}; display: flex; align-items: center; gap: 10px; padding: 6px 12px; background: #F3EFE6; border: 2.5px solid #D7261E; transform: rotate(2deg)">'
            f'<span style="font-family: \'Noto Sans JP\', sans-serif; font-weight: 900; font-size: 22px; color: #D7261E; line-height: 1">第{KAN[d]}日</span>'
            f'<span style="display: flex; flex-direction: column; gap: 2px; font-size: 9px; font-weight: 600; letter-spacing: 0.16em; color: #0D0D0F">'
            f'<span>THE {ORD[d]} DAY</span><span style="color: {c if c not in ("#E8C840", "#B8C8D8", "#5AC8C8") else "#3A2A1A"}">{prince} · {tribe}</span></span></div>\n')

def day_panel(d, h):
    """One day of the dedication: the day's six verses over the strip of the prince's oblation."""
    tribe, prince = DAYS[d]; a = 12 + 6 * d; c = K.TRIBE_C[tribe]
    strip = 150
    svg = (f'<rect x="0" y="0" width="{W1}" height="{h}" fill="{c}" opacity="0.28"></rect>' + K.standard(W1 - 60, h - strip - 10, 2.2, c, pole=60)
           + f'<rect x="0" y="{h - strip}" width="{W1}" height="{strip}" fill="#F3EFE6"></rect>'
           + f'<g transform="translate(0 {h - strip + 4})">{K4.oblation(W1, strip - 8)}</g>')
    text = sp(f"7:{a}-{a + 5}")
    over = (cap(text, "left: 12px; top: 12px", size=12, maxw=430) + day_tag(d, tribe, prince, "right: 14px; top: 14px")
            + vref(f"NUM 7:{a}–{a + 5}", f"right: 12px; bottom: {strip + 8}px"))
    return new("linear-gradient(180deg, #2A2458 0%, #4A3A6A 100%)", W1, h, svg, over)

def days_page(n, d0, d1=None, extra=None):
    hs = [499, None] if d1 is not None else ([None] if not extra else [None, extra[0]])
    t, h = rows(*hs)
    body = day_panel(d0, h[0]) + (day_panel(d1, h[1]) if d1 is not None else (extra[1](h[1]) if extra else ""))
    a = 12 + 6 * d0; b = 12 + 6 * (d1 if d1 is not None else d0) + 5
    if extra: b = extra[2]
    return page(f"Numbers 7:{a}–{b} — The {ORD[d0].title()} Day" + (f" and the {ORD[d1].title()}" if d1 is not None else ""), t, body, n)


@P("NUM-C04-00-Title", "Chapter 4 · The Offerings of the Princes", title=True)
def title(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2A1A"></rect>' + f'<g transform="translate(0 420)">{K4.wagons("t4", 760, 660, 401)}</g>'
    return chapter_title(4, "第四話", "The Offerings of the Princes", "Numbers 7 – 8", svg, SAND,
                         v("7:11", frm="They shall offer"), "Numbers · Volume Four")


@P("NUM-C04-P01-Wagons", "Six Covered Wagons")
def p01(n):
    t, h = rows(None, 420)
    r1 = new(SAND, W1, h[0], K.levites_round("w1a", W1, h[0], 411), cap(sp("7:1-2"), "left: 12px; top: 12px", size=12.5, maxw=520) + mk.stamp(7, "right: 14px; top: 12px") + vref("NUM 7:1–2", "right: 12px; bottom: 12px"))
    r2 = new(SKY, W1, h[1], K4.wagons("w1b", W1, h[1], 412), cap(v("7:3"), "left: 12px; top: 12px", size=12.5, maxw=520) + vref("NUM 7:3", "right: 12px; bottom: 12px"))
    return page("Numbers 7:1–3 — Six Covered Wagons", t, r1 + r2, n)


@P("NUM-C04-P02-Service", "To Every Man According to His Service")
def p02(n):
    t, h = rows(260, None, 250)
    r1 = new(NIGHT, W1, h[0], X.cosmic(W1, h[0]), cap(v("7:4"), "left: 12px; top: 12px", size=11) + god(v("7:5"), "left: 12px; top: 50px", size=21, maxw=600) + vref("NUM 7:4–5", "right: 12px; bottom: 12px"))
    r2 = new(INK, W1, h[1], K4.wagons_chart(W1, h[1]), cap(sp("7:6-9"), "left: 12px; top: 34px", size=12, maxw=370) + vref("NUM 7:6–9", "right: 12px; bottom: 12px"))
    r3 = new(SAND, W1, h[2], K.princes("w2c", W1, h[2], 423), cap(v("7:10"), "left: 12px; top: 12px", size=11.5, maxw=440)
             + god(v("7:11", frm="They shall"), "right: 12px; bottom: 12px", size=15, maxw=300) + cap(v("7:11", to="unto Moses,"), "right: 12px; bottom: 90px", size=10, maxw=260))
    return page("Numbers 7:4–11 — To Every Man According to His Service", t, r1 + r2 + r3, n)


@P("NUM-C04-P03-Day1", "The First Day and the Second")
def p03(n): return days_page(n, 0, 1)
@P("NUM-C04-P04-Day3", "The Third Day and the Fourth")
def p04(n): return days_page(n, 2, 3)
@P("NUM-C04-P05-Day5", "The Fifth Day and the Sixth")
def p05(n): return days_page(n, 4, 5)
@P("NUM-C04-P06-Day7", "The Seventh Day and the Eighth")
def p06(n): return days_page(n, 6, 7)
@P("NUM-C04-P07-Day9", "The Ninth Day and the Tenth")
def p07(n): return days_page(n, 8, 9)
@P("NUM-C04-P08-Day11", "The Eleventh Day and the Twelfth")
def p08(n): return days_page(n, 10, 11)


@P("NUM-C04-P09-Dedication", "This Was the Dedication of the Altar")
def p09(n):
    t, h = rows(None, 150, 320)
    r1 = new("linear-gradient(180deg, #2A2458 0%, #4A3A6A 100%)", W1, h[0], K.princes("w9a", W1, h[0], 491),
             cap(sp("7:84-86"), "left: 12px; top: 12px", size=11.5, maxw=380) + cap(sp("7:87-88"), "right: 12px; top: 12px", size=11.5, maxw=250) + vref("NUM 7:84–88", "right: 12px; bottom: 12px"))
    r2 = new("#F3EFE6", W1, h[1], f'<g transform="translate(0 8)">{K4.oblation(W1, h[1] - 12, days_=12)}</g>', "")
    r3 = new("#1A0E12", W1, h[2], K4.voice("w9c", W1, h[2], 492), cap(v("7:89"), "left: 12px; top: 12px", size=12, maxw=460) + vref("NUM 7:89", "right: 12px; bottom: 12px"))
    return page("Numbers 7:84–89 — This Was the Dedication of the Altar", t, r1 + r2 + r3, n)


@P("NUM-C04-P10-Lamps", "When Thou Lightest the Lamps")
def p10(n):
    t, h = rows(None, 280)
    r1 = new("#1A0E12", W1, h[0], K4.lamps("w10a", W1, h[0], 4101), mk.stamp(8, "right: 14px; bottom: 12px") + cap(v("8:1"), "left: 12px; top: 12px", size=11)
             + god(v("8:2"), "left: 12px; top: 50px", size=19, maxw=360) + cap(v("8:3"), "left: 12px; bottom: 40px", size=12, maxw=320) + vref("NUM 8:1–3", "left: 12px; bottom: 14px"))
    r2 = new(INK, W1, h[1], B8.lampstand(W1, h[1]), cap(v("8:4"), "left: 12px; top: 12px", size=12, maxw=320) + vref("NUM 8:4", "right: 12px; bottom: 12px"))
    return page("Numbers 8:1–4 — When Thou Lightest the Lamps", t, r1 + r2, n)


@P("NUM-C04-P11-Cleanse", "Cleanse Them")
def p11(n):
    t, h = rows(None, 360)
    r1 = new(NIGHT, W1, h[0], X.cosmic(W1, h[0]), cap(v("8:5"), "left: 12px; top: 12px", size=11) + god(sp("8:6-8"), "left: 12px; top: 50px", size=19, maxw=620) + vref("NUM 8:5–8", "right: 12px; bottom: 12px"))
    r2 = new(SKY, W1, h[1], K4.cleansing("w11b", W1, h[1], 4112, "sprinkle"), "")
    return page("Numbers 8:5–8 — Cleanse Them", t, r1 + r2, n)


@P("NUM-C04-P12-Hands", "The Children of Israel Shall Lay Their Hands")
def p12(n):
    t, h = rows(499, None)
    r1 = new(SKY, W1, h[0], K4.cleansing("w12a", W1, h[0], 4121, "hands"), god(sp("8:9-10"), "left: 12px; top: 12px", size=17, maxw=640) + vref("NUM 8:9–10", "right: 12px; bottom: 12px"))
    r2 = new(SKY, W1, h[1], K4.cleansing("w12b", W1, h[1], 4122, "wave"), god(sp("8:11-13"), "left: 12px; top: 12px", size=16, maxw=640) + vref("NUM 8:11–13", "right: 12px; bottom: 12px"))
    return page("Numbers 8:9–13 — The Children of Israel Shall Lay Their Hands", t, r1 + r2, n)


@P("NUM-C04-P13-Mine", "The Levites Shall Be Mine")
def p13(n):
    t, h = rows(None, 330)
    r1 = new(NIGHT, W1, h[0], X.cosmic(W1, h[0]), god(sp("8:14-17"), "left: 12px; top: 12px", size=19, maxw=660) + vref("NUM 8:14–17", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], K.levites_round("w13b", W1, h[1], 4132), god(sp("8:18-19"), "left: 12px; top: 12px", size=14.5, maxw=660) + vref("NUM 8:18–19", "right: 12px; bottom: 12px"))
    return page("Numbers 8:14–19 — The Levites Shall Be Mine", t, r1 + r2, n)


@P("NUM-C04-P14-Service", "From Twenty and Five Years Old")
def p14(n):
    t, h = rows(None, 260, 250)
    r1 = new(SKY, W1, h[0], K4.cleansing("w14a", W1, h[0], 4141, "wave"), cap(sp("8:20-22"), "left: 12px; top: 12px", size=12, maxw=600) + vref("NUM 8:20–22", "right: 12px; bottom: 12px"))
    r2 = new(NIGHT, W1, h[1], X.cosmic(W1, h[1]), cap(v("8:23"), "left: 12px; top: 12px", size=11) + god(sp("8:24-26"), "left: 12px; top: 50px", size=16.5, maxw=660) + vref("NUM 8:23–26", "right: 12px; bottom: 12px"))
    r3 = new(INK, W1, h[2], K4.ages(W1, h[2]), end_mark("NEXT · THE CLOUD AND THE TRUMPETS", "right: 10px; bottom: 10px"))
    return page("Numbers 8:20–26 — From Twenty and Five Years Old", t, r1 + r2 + r3, n)
