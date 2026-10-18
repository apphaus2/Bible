"""Numbers volume, Chapter 5 — The Cloud and the Trumpets (Numbers 9–10). Every verse, word for word from ref/asv.
The passover in the wilderness and the men unclean by the dead; the cloud upon the tabernacle, by day and by night; the
two trumpets of silver; the order of march out of the wilderness of Sinai (a plan); Hobab; and Moses' words when the
ark set forward and when it rested."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import new, vref, page, chapter_title, end_mark, cols, cap, god, balloon
from exo import art as A, art3 as A3, art8 as B8
from exo.kit import talk, song
from num import G, art as K, art5 as K5
from num.pages import Pages
from genesis import art as X
from genesis.ch02 import rows, grid, W1, W2, NIGHT, SKY, DUSK
from genesis.ch03 import SAND
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from num import ch04 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
INK = B8.INK

def night(h, over, w=W1): return new(NIGHT, w, h, X.cosmic(w, h), over)
def after(ref, to):
    t = v(ref); return v(ref, frm=t[t.index(to) + len(to):].strip())


@P("NUM-C05-00-Title", "Chapter 5 · The Cloud and the Trumpets", title=True)
def title(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#0B0B2A"></rect>' + f'<g transform="translate(0 300)">{K5.cloud_tab("t5", 760, 780, 501, night=True)}</g>'
    return chapter_title(5, "第五話", "The Cloud and the Trumpets", "Numbers 9 – 10", svg, NIGHT,
                         v("9:23", to="journeyed:"), "Numbers · Volume Four")


@P("NUM-C05-P01-Passover", "Keep the Passover in Its Appointed Season")
def p01(n):
    t, h = rows(None, 380)
    r1 = night(h[0], mk.stamp(9, "right: 14px; top: 12px") + cap(v("9:1"), "left: 12px; top: 12px", size=11.5, maxw=520)
               + god(sp("9:2-3"), "left: 12px; top: 84px", size=20, maxw=620) + vref("NUM 9:1–3", "right: 12px; bottom: 12px"))
    r2 = new(DUSK, W1, h[1], mk.defs("p5b", *K.ALL) + A3.household_meal("p5b", W1, h[1], 512), cap(sp("9:4-5"), "left: 12px; top: 12px", size=12, maxw=470) + vref("NUM 9:4–5", "right: 12px; bottom: 12px"))
    return page("Numbers 9:1–5 — Keep the Passover in Its Appointed Season", t, r1 + r2, n)


@P("NUM-C05-P02-Unclean", "Wherefore Are We Kept Back?")
def p02(n):
    t, h = rows(250, None, 250)
    r1 = new(SAND, W1, h[0], K.levites_round("p5c", W1, h[0], 521), cap(v("9:6"), "left: 12px; top: 12px", size=12, maxw=480) + vref("NUM 9:6", "right: 12px; bottom: 12px"))
    r2 = talk(K5.UNCLEAN, h[1], COLD, [("cap", v("9:7", to="said unto him,")), ("say", after("9:7", "said unto him,"))], ref="NUM 9:7", size=15)
    r3 = talk(A.MOSES_CALM, h[2], GOLDEN, [("cap", v("9:8", to="unto them,")), ("say", after("9:8", "unto them,"))], ref="NUM 9:8", size=17, flip=True)
    return page("Numbers 9:6–8 — Wherefore Are We Kept Back?", t, r1 + r2 + r3, n)


@P("NUM-C05-P03-Second", "In the Second Month")
def p03(n):
    t, h = rows(420, None)
    r1 = night(h[0], cap(v("9:9"), "left: 12px; top: 12px", size=11) + god(sp("9:10-12"), "left: 12px; top: 50px", size=19, maxw=640) + vref("NUM 9:9–12", "right: 12px; bottom: 12px"))
    r2 = cols(new("#2A1408", W2, h[1], A3.roast(W2, h[1], 532), god(v("9:13"), "left: 8px; top: 8px", size=13, maxw=320) + vref("NUM 9:13", "right: 8px; bottom: 8px")),
              new(SAND, W2, h[1], K.wilderness_camp("p5d", W2, h[1], 533, standards=False), god(v("9:14"), "left: 8px; top: 8px", size=12.5, maxw=320) + vref("NUM 9:14", "right: 8px; bottom: 8px")))
    return page("Numbers 9:9–14 — In the Second Month", t, r1 + r2, n)


@P("NUM-C05-P04-Cloud", "The Appearance of Fire by Night")
def p04(n):
    t, h = rows(500, None)
    r1 = new(SKY, W1, h[0], K5.cloud_tab("p5e", W1, h[0], 541), cap(v("9:15"), "left: 12px; top: 12px", size=12.5, maxw=440) + vref("NUM 9:15", "right: 12px; bottom: 12px"))
    r2 = cols(new(NIGHT, W2, h[1], K5.cloud_tab("p5f", W2, h[1], 542, night=True), cap(v("9:16"), "left: 8px; top: 8px", size=12, maxw=300) + vref("NUM 9:16", "right: 8px; bottom: 8px")),
              new(SKY, W2, h[1], K.wilderness_camp("p5g", W2, h[1], 543, cloud=True), cap(sp("9:17-18"), "left: 8px; top: 8px", size=11, maxw=320) + vref("NUM 9:17–18", "right: 8px; bottom: 8px")))
    return page("Numbers 9:15–18 — The Appearance of Fire by Night", t, r1 + r2, n)


@P("NUM-C05-P05-Tarried", "When the Cloud Tarried")
def p05(n):
    t, h = rows(None, 300)
    r1 = new(SKY, W1, h[0], K5.cloud_tab("p5h", W1, h[0], 551), cap(sp("9:19-21"), "left: 12px; top: 12px", size=12, maxw=470) + cap(sp("9:22-23"), "right: 12px; top: 220px", size=12, maxw=420) + vref("NUM 9:19–23", "right: 12px; bottom: 12px"))
    r2 = new(INK, W1, h[1], K5.tarry(W1, h[1]), "")
    return page("Numbers 9:19–23 — When the Cloud Tarried", t, r1 + r2, n)


@P("NUM-C05-P06-Trumpets", "Two Trumpets of Silver")
def p06(n):
    t, h = rows(330, None)
    r1 = new(INK, W1, h[0], K5.trumpets_plate(W1, h[0]), mk.stamp(10, "right: 14px; top: 30px") + cap(v("10:1"), "left: 12px; top: 30px", size=11)
             + god(v("10:2"), "left: 12px; top: 68px", size=15, maxw=330) + vref("NUM 10:1–2", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], K5.blowing("p5i", W1, h[1], 561), god(sp("10:3-6"), "right: 12px; top: 12px", size=17, maxw=360) + vref("NUM 10:3–6", "right: 12px; bottom: 12px"))
    return page("Numbers 10:1–6 — Two Trumpets of Silver", t, r1 + r2, n)


@P("NUM-C05-P07-Alarm", "Ye Shall Be Remembered before Jehovah")
def p07(n):
    t, h = rows(280, None)
    r1 = night(h[0], god(sp("10:7-8"), "left: 12px; top: 12px", size=19, maxw=640) + vref("NUM 10:7–8", "right: 12px; bottom: 12px"))
    r2 = cols(new(SAND, W2, h[1], K5.blowing("p5j", W2, h[1], 571, war=True), god(v("10:9"), "left: 8px; top: 8px", size=12.5, maxw=320) + vref("NUM 10:9", "right: 8px; bottom: 8px")),
              new(GOLDEN, W2, h[1], K5.blowing("p5k", W2, h[1], 572), god(v("10:10"), "left: 8px; top: 8px", size=12, maxw=320) + vref("NUM 10:10", "right: 8px; bottom: 8px")))
    return page("Numbers 10:7–10 — Ye Shall Be Remembered before Jehovah", t, r1 + r2, n)


@P("NUM-C05-P08-SetForward", "Out of the Wilderness of Sinai")
def p08(n):
    t, h = rows(330, 250, None)
    r1 = new(SKY, W1, h[0], K5.procession("p5l", W1, h[0], 581), cap(sp("10:11-13"), "left: 12px; top: 12px", size=12, maxw=470) + vref("NUM 10:11–13", "right: 12px; bottom: 12px"))
    r2 = new(INK, W1, h[1], K5.march_plan(W1, h[1], hi=(0,)), "")
    r3 = new(SAND, W1, h[2], K5.procession("p5m", W1, h[2], 582, ark=False), cap(sp("10:14-16"), "left: 12px; top: 12px", size=12, maxw=470) + vref("NUM 10:14–16", "right: 12px; bottom: 12px"))
    return page("Numbers 10:11–16 — Out of the Wilderness of Sinai", t, r1 + r2 + r3, n)


@P("NUM-C05-P09-Order", "And They Set Forward")
def p09(n):
    t, h = rows(230, 380, None)
    r1 = new(INK, W1, h[0], K5.march_plan(W1, h[0], hi=(1, 2, 3)), "")
    r2 = new(SAND, W1, h[1], K5.procession("p5n", W1, h[1], 592, ark=False, tribes=("REUBEN", "SIMEON", "GAD")),
             cap(sp("10:17-21"), "left: 12px; top: 12px", size=12, maxw=470) + vref("NUM 10:17–21", "right: 12px; bottom: 12px"))
    r3 = new(SAND, W1, h[2], K5.procession("p5o", W1, h[2], 593, ark=False, cloud=False, tribes=("EPHRAIM", "MANASSEH", "BENJAMIN")),
             cap(sp("10:22-24"), "left: 12px; top: 12px", size=12, maxw=470) + vref("NUM 10:22–24", "right: 12px; bottom: 12px"))
    return page("Numbers 10:17–24 — And They Set Forward", t, r1 + r2 + r3, n)


@P("NUM-C05-P10-Rearward", "The Rearward of All the Camps")
def p10(n):
    t, h = rows(None, 260)
    r1 = new(SAND, W1, h[0], K5.procession("p5p", W1, h[0], 5101, ark=False, cloud=False, tribes=("DAN", "ASHER", "NAPHTALI")),
             cap(sp("10:25-28"), "left: 12px; top: 12px", size=12.5, maxw=470) + vref("NUM 10:25–28", "right: 12px; bottom: 12px"))
    r2 = new(INK, W1, h[1], K5.march_plan(W1, h[1], hi=(4, 5)), "")
    return page("Numbers 10:25–28 — The Rearward of All the Camps", t, r1 + r2, n)


@P("NUM-C05-P11-Hobab", "Thou Shalt Be to Us instead of Eyes")
def p11(n):
    t, h = rows(330, 230, None)
    r1 = talk(A.MOSES_CALM, h[0], GOLDEN, [("cap", v("10:29", to="Moses' father-in-law,")), ("say", after("10:29", "father-in-law,"))], ref="NUM 10:29", size=14)
    r2 = talk(K5.HOBAB, h[1], DUSK, [("cap", v("10:30", to="unto him,")), ("say", after("10:30", "unto him,"))], ref="NUM 10:30", size=17, flip=True)
    r3 = talk(A.MOSES, h[2], GOLDEN, [("cap", v("10:31", to="And he said,")), ("say", after("10:31", "he said,") + " " + v("10:32"))], ref="NUM 10:31–32", size=15)
    return page("Numbers 10:29–32 — Thou Shalt Be to Us instead of Eyes", t, r1 + r2 + r3, n)


@P("NUM-C05-P12-RiseUp", "Rise Up, O Jehovah")
def p12(n):
    t, h = rows(None, 230)
    r1 = new(SKY, W1, h[0], K5.procession("p5q", W1, h[0], 5121),
             cap(v("10:33") + " " + v("10:34"), "left: 12px; top: 12px", size=12, maxw=470)
             + cap(v("10:35", to="Moses said,"), "left: 12px; top: 150px", size=11, maxw=360)
             + balloon(after("10:35", "Moses said,"), "left: 24px; top: 196px", 380, size=17, pad="26px 30px") + vref("NUM 10:33–35", "right: 12px; bottom: 12px"))
    r2 = new(DUSK, W1, h[1], K5.cloud_tab("p5r", W1, h[1], 5122, night=True),
             cap(v("10:36", to="he said,"), "left: 12px; top: 12px", size=11) + balloon(after("10:36", "he said,"), "left: 24px; top: 52px", 400, size=17, pad="22px 28px")
             + vref("NUM 10:36", "left: 12px; bottom: 12px") + end_mark("NEXT · GRAVES OF LUST", "right: 10px; bottom: 10px"))
    return page("Numbers 10:33–36 — Rise Up, O Jehovah", t, r1 + r2, n)
