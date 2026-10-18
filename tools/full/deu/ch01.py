"""Deuteronomy volume, Chapter 1 — These Are the Words (Deuteronomy 1–2). Every verse, word for word from ref/asv.
Moses' first discourse in speech panels (speech.orate): his words in rounded speech boxes, Jehovah's words quoted in Voice
boxes, the narrator's asides (2:10–12, 2:20–23) as captions. Flashbacks reuse the Numbers art: Horeb, the spies and
Eshcol, the presumption at Hormah, the way round Seir and Moab (a map), and the host of Sihon at a distance."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import new, vref, page, chapter_title, end_mark, cap
from deu import G, art as K
from deu.common import say, gd, cp, says, gods, caps, mo, voice, over, INK
from num import art7 as N7, art10 as N10
from num.pages import Pages
from genesis.ch02 import rows, W1, SKY, DUSK
from genesis.ch03 import SAND
from genesis.ch04 import COLD
from genesis.ch07 import RED

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("DEU-C01-00-Title", "Chapter 1 · These Are the Words", title=True)
def title(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A1A3A"></rect>' + f'<g transform="translate(0 360)">{K.address("t1", 760, 720, 101, raise_hand=True)}</g>'
    return chapter_title(1, "第一話", "These Are the Words", "Deuteronomy 1 – 2", svg, DUSK, v("1:1", to="beyond the Jordan"), "Deuteronomy · Volume Five")


@P("DEU-C01-P01-Words", "These Are the Words")
def p01(n):
    t, h = rows(480, None)
    r1 = new("#F3D8A0", W1, h[0], K.address("d1a", W1, h[0], 111), cap(sp("1:1-2"), "left: 12px; top: 12px", size=12.5, maxw=520) + mk.stamp(1, "right: 14px; top: 12px") + vref("DEUT 1:1–2", "right: 12px; bottom: 12px"))
    r2 = new(INK, W1, h[1], K.map_moab(W1, h[1]), cap(sp("1:3-5"), "left: 12px; top: 12px", size=12.5, maxw=330) + vref("DEUT 1:3–5", "left: 12px; bottom: 12px"))
    return page("Deuteronomy 1:1–5 — These Are the Words", t, r1 + r2, n)


@P("DEU-C01-P02-Horeb", "Ye Have Dwelt Long Enough in This Mountain")
def p02(n):
    t, h = rows(300, None)
    r1 = new("#5A6E8A", W1, h[0], K.horeb(W1, h[0], 121), vref("DEUT 1:6", "right: 12px; bottom: 12px"))
    r2 = mo(h[1], [say("1:6", to="saying,"), gd("1:6", frm="Ye have dwelt"), gods("1:7-8")], "DEUT 1:6–8")
    return page("Deuteronomy 1:6–8 — Ye Have Dwelt Long Enough in This Mountain", t, r1 + r2, n)


@P("DEU-C01-P03-Alone", "I Am Not Able to Bear You Myself Alone")
def p03(n):
    t, h = rows(None, 300)
    return page("Deuteronomy 1:9–14 — I Am Not Able to Bear You Myself Alone", t,
                mo(h[0], [says("1:9-12")], "DEUT 1:9–12") + mo(h[1], [says("1:13-14")], "DEUT 1:13–14", flip=True), n)


@P("DEU-C01-P04-Judges", "The Judgment Is God's")
def p04(n):
    t, h = rows(None, 280)
    r1 = mo(h[0], [says("1:15-17")], "DEUT 1:15–17")
    r2 = over(h[1], SAND, N7.sending("d4b", W1, h[1], 141), [says("1:18")], "DEUT 1:18")
    return page("Deuteronomy 1:15–18 — The Judgment Is God's", t, r1 + r2, n)


@P("DEU-C01-P05-Kadesh", "It Is a Good Land")
def p05(n):
    t, h = rows(260, None)
    r1 = new(SKY, W1, h[0], N7.hill_country(W1, h[0], 151), vref("DEUT 1:24–25", "right: 12px; bottom: 12px"))
    r2 = mo(h[1], [says("1:19-21"), says("1:22-25")], "DEUT 1:19–25")
    return page("Deuteronomy 1:19–25 — It Is a Good Land", t, r1 + r2, n)


@P("DEU-C01-P06-Murmured", "Ye Murmured in Your Tents")
def p06(n):
    t, h = rows(None, 300)
    return page("Deuteronomy 1:26–31 — Ye Murmured in Your Tents", t,
                mo(h[0], [says("1:26-28")], "DEUT 1:26–28", tok=K.MOSES_STERN, bg=RED) + mo(h[1], [says("1:29-31")], "DEUT 1:29–31", flip=True), n)


@P("DEU-C01-P07-Sware", "Jehovah Heard the Voice of Your Words")
def p07(n):
    t, h = rows(None, 300)
    return page("Deuteronomy 1:32–36 — Jehovah Heard the Voice of Your Words", t,
                mo(h[0], [says("1:32-34")], "DEUT 1:32–34", tok=K.MOSES_STERN, bg=RED) + voice(h[1], [gods("1:35-36")], "DEUT 1:35–36"), n)


@P("DEU-C01-P08-NotGoIn", "Thou Also Shalt Not Go In Thither")
def p08(n):
    t, h = rows(None, 360)
    return page("Deuteronomy 1:37–40 — Thou Also Shalt Not Go In Thither", t,
                mo(h[0], [say("1:37", to="saying,"), gd("1:37", frm="Thou also")], "DEUT 1:37", tok=K.MOSES_GRIEF, bg=COLD) + voice(h[1], [gods("1:38-40")], "DEUT 1:38–40"), n)


@P("DEU-C01-P09-Hormah", "As Bees Do")
def p09(n):
    t, h = rows(300, None)
    r1 = new("#3A1A1A", W1, h[0], N7.presumed("d9a", W1, h[0], 191, smitten=True), vref("DEUT 1:44", "right: 12px; bottom: 12px"))
    r2 = mo(h[1], [says("1:41"), say("1:42", to="unto me,"), gd("1:42", frm="Say unto them,"), says("1:43-46")], "DEUT 1:41–46", tok=K.MOSES_GRIEF, bg=COLD)
    return page("Deuteronomy 1:41–46 — As Bees Do", t, r1 + r2, n)


@P("DEU-C01-P10-Seir", "Ye Have Compassed This Mountain Long Enough")
def p10(n):
    t, h = rows(260, None)
    r1 = new(INK, W1, h[0], K.map_moab(W1, h[0], hi=("SEIR",)), mk.stamp(2, "right: 14px; top: 12px") + vref("DEUT 2:1–8", "right: 12px; bottom: 12px"))
    r2 = mo(h[1], [says("2:1-2"), gods("2:3-7")], "DEUT 2:1–7")
    return page("Deuteronomy 2:1–7 — Ye Have Compassed This Mountain Long Enough", t, r1 + r2, n)


@P("DEU-C01-P11-Moab", "Vex Not Moab")
def p11(n):
    t, h = rows(None, 280)
    r1 = mo(h[0], [say("2:8"), say("2:9", to="unto me,"), gd("2:9", frm="Vex not Moab,")], "DEUT 2:8–9")
    r2 = over(h[1], "#3A2A3A", K.giants(W1, h[1], 1112), [caps("2:10-12")], "DEUT 2:10–12")
    return page("Deuteronomy 2:8–12 — Vex Not Moab", t, r1 + r2, n)


@P("DEU-C01-P12-Zered", "Thirty and Eight Years")
def p12(n):
    t, h = rows(None, 280)
    r1 = mo(h[0], [gd("2:13", to="brook Zered."), say("2:13", frm="And we went"), says("2:14-16"), say("2:17")], "DEUT 2:13–17", tok=K.MOSES_GRIEF, bg=COLD)
    r2 = voice(h[1], [gods("2:18-19")], "DEUT 2:18–19")
    return page("Deuteronomy 2:13–19 — Thirty and Eight Years", t, r1 + r2, n)


@P("DEU-C01-P13-Rephaim", "Begin to Possess")
def p13(n):
    t, h = rows(None, 330)
    r1 = over(h[0], "#3A2A3A", K.giants(W1, h[0], 1131), [caps("2:20-23")], "DEUT 2:20–23")
    r2 = voice(h[1], [gods("2:24-25")], "DEUT 2:24–25")
    return page("Deuteronomy 2:20–25 — Begin to Possess", t, r1 + r2, n)


@P("DEU-C01-P14-Sihon", "Words of Peace")
def p14(n):
    t, h = rows(None, 300)
    r1 = mo(h[0], [says("2:26-29")], "DEUT 2:26–29")
    r2 = mo(h[1], [say("2:30"), say("2:31", to="unto me,"), gd("2:31", frm="Behold,")], "DEUT 2:30–31", flip=True)
    return page("Deuteronomy 2:26–31 — Words of Peace", t, r1 + r2, n)


@P("DEU-C01-P15-Jahaz", "Not a City Too High for Us")
def p15(n):
    t, h = rows(300, None)
    r1 = new(SAND, W1, h[0], N10.host("d15a", W1, h[0], 1151), vref("DEUT 2:32", "right: 12px; bottom: 12px"))
    r2 = mo(h[1], [says("2:32-37")], "DEUT 2:32–37", extra=end_mark("NEXT · TAKE HEED TO THYSELF", "right: 10px; bottom: 10px"))
    return page("Deuteronomy 2:32–37 — Not a City Too High for Us", t, r1 + r2, n)
