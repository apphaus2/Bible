"""Deuteronomy volume, Chapter 2 — Take Heed to Thyself (Deuteronomy 3–4). Every verse, word for word from ref/asv.
Og and the land beyond the Jordan (Og's iron bedstead as a blueprint, the asides 3:9 and 3:11 as captions); Moses'
prayer to go over and the answer, Pisgah; then the great exhortation of chapter 4 in speech panels — Horeb, no manner of
form, the scattering and the return, is there any god beside him — and the cities of refuge and the setting of the law."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import new, vref, page, chapter_title, end_mark, cap
from deu import G, art as K, art2 as K2
from deu.common import say, gd, cp, says, gods, caps, mo, voice, over, INK
from num import art10 as N10, art12 as N12, art13 as N13, art15 as N15, art16 as N16
from num.pages import Pages
from genesis.ch02 import rows, W1, SKY, DUSK, NIGHT
from genesis.ch03 import SAND
from genesis.ch04 import COLD
from genesis.ch07 import RED
from deu import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("DEU-C02-00-Title", "Chapter 2 · Take Heed to Thyself", title=True)
def title(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A0A0A"></rect>' + f'<g transform="translate(0 340)">{K.horeb(760, 740, 201, fire=True)}</g>'
    return chapter_title(2, "第二話", "Take Heed to Thyself", "Deuteronomy 3 – 4", svg, "#2A0A0A", v("4:24"), "Deuteronomy · Volume Five")


@P("DEU-C02-P01-Og", "Og the King of Bashan")
def p01(n):
    t, h = rows(300, None)
    r1 = new(DUSK, W1, h[0], N10.host("e1a", W1, h[0], 211, foe="#2A2A3A", giant=True), mk.stamp(3, "right: 14px; top: 12px") + vref("DEUT 3:1", "right: 12px; bottom: 12px"))
    r2 = mo(h[1], [say("3:1"), say("3:2", to="unto me,"), gd("3:2", frm="Fear him not;"), says("3:3-5")], "DEUT 3:1–5")
    return page("Deuteronomy 3:1–5 — Og the King of Bashan", t, r1 + r2, n)


@P("DEU-C02-P02-Hermon", "From the Valley of the Arnon unto Mount Hermon")
def p02(n):
    t, h = rows(None, 300)
    r1 = mo(h[0], [says("3:6-8"), cp("3:9"), say("3:10")], "DEUT 3:6–10")
    r2 = over(h[1], INK, K2.bedstead(W1, h[1]), [cp("3:11")], "DEUT 3:11", hi=13)
    return page("Deuteronomy 3:6–11 — From the Valley of the Arnon unto Mount Hermon", t, r1 + r2, n)


@P("DEU-C02-P03-Gave", "This Land We Took in Possession")
def p03(n):
    t, h = rows(320, None)
    r1 = new(INK, W1, h[0], N15.beyond_jordan(W1, h[0]), vref("DEUT 3:12–17", "left: 12px; bottom: 12px"))
    r2 = mo(h[1], [says("3:12-17")], "DEUT 3:12–17")
    return page("Deuteronomy 3:12–17 — This Land We Took in Possession", t, r1 + r2, n)


@P("DEU-C02-P04-Joshua", "Ye Shall Not Fear Them")
def p04(n):
    t, h = rows(None, 300)
    return page("Deuteronomy 3:18–22 — Ye Shall Not Fear Them", t,
                mo(h[0], [says("3:18-20")], "DEUT 3:18–20") + mo(h[1], [says("3:21-22")], "DEUT 3:21–22", flip=True), n)


@P("DEU-C02-P05-Pisgah", "Let Me Go Over, I Pray Thee")
def p05(n):
    t, h = rows(None, 280)
    r1 = mo(h[0], [say("3:23"), says("3:24-25"), say("3:26", to="unto me,"), gd("3:26", frm="Let it suffice thee;"), gods("3:27-28")], "DEUT 3:23–28", tok=K.MOSES_GRIEF, bg=COLD)
    r2 = new("#F3C88A", W1, h[1], N13.abarim("e5b", W1, h[1], 251), cap(v("3:29"), "right: 12px; top: 12px", size=12.5, maxw=380) + vref("DEUT 3:29", "right: 12px; bottom: 12px"))
    return page("Deuteronomy 3:23–29 — Let Me Go Over, I Pray Thee", t, r1 + r2, n)


@P("DEU-C02-P06-Hearken", "Ye Shall Not Add unto the Word")
def p06(n):
    t, h = rows(280, None)
    r1 = new("#C85A3A", W1, h[0], N12.peor("e6a", W1, h[0], 261), mk.stamp(4, "right: 14px; top: 12px") + vref("DEUT 4:3", "right: 12px; bottom: 12px"))
    r2 = mo(h[1], [says("4:1-4")], "DEUT 4:1–4")
    return page("Deuteronomy 4:1–4 — Ye Shall Not Add unto the Word", t, r1 + r2, n)


@P("DEU-C02-P07-Nigh", "A God So Nigh unto Them")
def p07(n):
    t, h = rows(None, 280)
    r1 = mo(h[0], [says("4:5-8")], "DEUT 4:5–8")
    r2 = new("#F3D8A0", W1, h[1], K.address("e7b", W1, h[1], 272), "")
    return page("Deuteronomy 4:5–8 — A God So Nigh unto Them", t, r1 + r2, n)


@P("DEU-C02-P08-Fire", "The Mountain Burned with Fire")
def p08(n):
    t, h = rows(None, 330)
    r1 = mo(h[0], [say("4:9"), say("4:10", to="said unto me,"), gd("4:10", frm="Assemble me")], "DEUT 4:9–10")
    r2 = over(h[1], "#2A0A0A", K.horeb(W1, h[1], 282, fire=True), [says("4:11-12")], "DEUT 4:11–12", hi=17)
    return page("Deuteronomy 4:9–12 — The Mountain Burned with Fire", t, r1 + r2, n)


@P("DEU-C02-P09-NoForm", "Ye Saw No Manner of Form")
def p09(n):
    t, h = rows(None, 260)
    r1 = mo(h[0], [says("4:13-18")], "DEUT 4:13–18")
    r2 = new("#2A2458", W1, h[1], K2.likenesses(W1, h[1]), "")
    return page("Deuteronomy 4:13–18 — Ye Saw No Manner of Form", t, r1 + r2, n)


@P("DEU-C02-P10-Furnace", "Out of the Iron Furnace")
def p10(n):
    t, h = rows(230, None)
    r1 = new("#2A2458", W1, h[0], K2.likenesses(W1, h[0], heaven=True), "")
    r2 = mo(h[1], [says("4:19-22")], "DEUT 4:19–22", tok=K.MOSES_GRIEF, bg=COLD)
    return page("Deuteronomy 4:19–22 — Out of the Iron Furnace", t, r1 + r2, n)


@P("DEU-C02-P11-Devouring", "A Devouring Fire, a Jealous God")
def p11(n):
    t, h = rows(None, 280)
    r1 = mo(h[0], [says("4:23-26")], "DEUT 4:23–26", tok=K.MOSES_STERN, bg=RED)
    r2 = over(h[1], "#2A2A3A", K2.scattered(W1, h[1], 2112), [says("4:27-28")], "DEUT 4:27–28", hi=16)
    return page("Deuteronomy 4:23–28 — A Devouring Fire, a Jealous God", t, r1 + r2, n)


@P("DEU-C02-P12-Seek", "From Thence Ye Shall Seek Jehovah")
def p12(n):
    t, h = rows(500, None)
    return page("Deuteronomy 4:29–34 — From Thence Ye Shall Seek Jehovah", t,
                mo(h[0], [says("4:29-31")], "DEUT 4:29–31") + mo(h[1], [says("4:32-34")], "DEUT 4:32–34", flip=True), n)


@P("DEU-C02-P13-NoneElse", "There Is None Else")
def p13(n):
    t, h = rows(None, 320)
    return page("Deuteronomy 4:35–40 — There Is None Else", t,
                mo(h[0], [says("4:35-38")], "DEUT 4:35–38") + mo(h[1], [says("4:39-40")], "DEUT 4:39–40", flip=True), n)


@P("DEU-C02-P14-Law", "This Is the Law Which Moses Set")
def p14(n):
    t, h = rows(300, None)
    r1 = over(h[0], INK, N16.refuge(W1, h[0]), [caps("4:41-43")], "DEUT 4:41–43", hi=13)
    r2 = new("#F3D8A0", W1, h[1], K.address("e14b", W1, h[1], 2142), cap(sp("4:44-49"), "left: 12px; top: 12px", size=12, maxw=560)
             + vref("DEUT 4:44–49", "left: 12px; bottom: 12px") + end_mark("NEXT · HEAR, O ISRAEL", "right: 10px; bottom: 10px"))
    return page("Deuteronomy 4:41–49 — This Is the Law Which Moses Set", t, r1 + r2, n)
