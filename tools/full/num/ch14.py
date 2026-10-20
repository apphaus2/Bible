"""Numbers volume, Chapter 14 — Vows and the War with Midian (Numbers 30–31). Every verse, word for word from ref/eng-asv.
The law of vows as law cells; the war with Midian told with restraint — the men going out, cities burning far off, the
prey coming to the camp; Moses' words to the officers (31:15–18) over his face and the empty plain; the purification; the
spoil divided (a chart); and the officers' gold."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import new, vref, page, chapter_title, end_mark, cols, cap, god, balloon
from exo import art as A, art8 as B8
from exo.kit import talk, law_pages, set_book
from num import G, art as K, art7 as K7, art10 as K10, art14 as K14
from exo import art2 as A2
from num.pages import Pages
from genesis import art as X
from genesis.ch02 import rows, grid, W1, W2, NIGHT, SKY, DUSK
from genesis.ch03 import SAND, hud
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from num import ch13 as _prev

v, sp = G.v, G.span
set_book(G)
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
INK = B8.INK

def night(h, over, w=W1): return new(NIGHT, w, h, X.cosmic(w, h), over)
def after(ref, to):
    t = v(ref); return v(ref, frm=t[t.index(to) + len(to):].strip())


@P("NUM-C14-00-Title", "Chapter 14 · Vows and the War with Midian", title=True)
def title(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#4A2A2A"></rect>' + f'<g transform="translate(0 420)">{K14.going_out("t14", 760, 660, 1401)}</g>'
    return chapter_title(14, "第十四話", "Vows and the War with Midian", "Numbers 30 – 31", svg, "#4A2A2A", v("30:2", frm="he shall not break his word;"), "Numbers · Volume Four")


LAWS = [
    ("THIS IS THE THING", "30:1", K14.pg_heads, "", "When a Man Voweth a Vow"),
    ("HE SHALL NOT BREAK HIS WORD", "30:2", K14.pg_man_vow, "", None),
    ("IN HER FATHER'S HOUSE", "30:3-4", K14.pg_father_peace, "", None),
    ("IF HER FATHER DISALLOW HER", "30:5", K14.pg_father_no, "", None),
    ("IF SHE BE MARRIED", "30:6-7", K14.pg_married, "", None),
    ("IF HER HUSBAND DISALLOW HER", "30:8", K14.pg_husband_no, "", None),
    ("A WIDOW · DIVORCED", "30:9", K14.pg_widow, "", None),
    ("IN HER HUSBAND'S HOUSE", "30:10-11", K14.pg_house, "", None),
    ("NULL AND VOID", "30:12-13", K14.pg_void, "", None),
    ("FROM DAY TO DAY", "30:14", K14.pg_day_to_day, "", None),
    ("HE SHALL BEAR HER INIQUITY", "30:15", K14.pg_bear, "", None),
    ("THESE ARE THE STATUTES", "30:16", K14.pg_statutes, "", None),
]
PG.extend(law_pages(LAWS, "NUM-C14-L", PG.next(), "When a Man Voweth a Vow", title_book="Numbers", carry=True))


@P("NUM-C14-P01-Avenge", "Avenge the Children of Israel")
def p01(n):
    t, h = rows(260, None)
    r1 = night(h[0], mk.stamp(31, "right: 14px; top: 12px") + cap(v("31:1"), "left: 12px; top: 12px", size=11) + god(v("31:2"), "left: 12px; top: 50px", size=22, maxw=560) + vref("NUM 31:1–2", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], K14.going_out("x1b", W1, h[1], 1412), cap(sp("31:3-6"), "left: 12px; top: 12px", size=12, maxw=560) + vref("NUM 31:3–6", "right: 12px; bottom: 12px"))
    return page("Numbers 31:1–6 — Avenge the Children of Israel", t, r1 + r2, n)


@P("NUM-C14-P02-Burnt", "All Their Cities")
def p02(n):
    t, h = rows(None, 330)
    r1 = new("#4A2A2A", W1, h[0], K14.burning(W1, h[0], 1421), cap(sp("31:7-10"), "left: 12px; top: 12px", size=13, maxw=560) + vref("NUM 31:7–10", "right: 12px; bottom: 12px"))
    r2 = new(DUSK, W1, h[1], K14.prey("x2b", W1, h[1], 1422), cap(v("31:11") + " " + v("31:12"), "left: 12px; top: 12px", size=12, maxw=520) + vref("NUM 31:11–12", "right: 12px; bottom: 12px"))
    return page("Numbers 31:7–12 — All Their Cities", t, r1 + r2, n)


@P("NUM-C14-P03-Wroth", "Moses Was Wroth with the Officers")
def p03(n):
    t, h = rows(300, None)
    r1 = new(SAND, W1, h[0], K14.prey("x3a", W1, h[0], 1431, meet=True), cap(v("31:13") + " " + v("31:14"), "right: 12px; top: 12px", size=12, maxw=380) + vref("NUM 31:13–14", "right: 12px; bottom: 12px"))
    r2 = talk(A.MOSES_STERN, h[1], RED, [("cap", v("31:15", to="unto them,")), ("say", after("31:15", "unto them,") + " " + v("31:16") + " " + v("31:17") + " " + v("31:18"))], ref="NUM 31:15–18", size=16)
    return page("Numbers 31:13–18 — Moses Was Wroth with the Officers", t, r1 + r2, n)


@P("NUM-C14-P04-Purify", "Through the Fire")
def p04(n):
    t, h = rows(250, 250, None)
    r1 = talk(A.MOSES, h[0], GOLDEN, [("say", v("31:19") + " " + v("31:20"))], ref="NUM 31:19–20", size=15)
    r2 = talk(K10.ELEAZAR, h[1], GOLDEN, [("cap", v("31:21", to="went to the battle,")), ("say", after("31:21", "went to the battle,"))], ref="NUM 31:21", size=15, flip=True)
    r3 = new(INK, W1, h[2], K14.through_fire(W1, h[2]), cap(v("31:22") + " " + v("31:23") + " " + v("31:24"), "left: 12px; top: 34px", size=12, maxw=320) + vref("NUM 31:22–24", "right: 12px; bottom: 12px"))
    return page("Numbers 31:19–24 — Through the Fire", t, r1 + r2 + r3, n)


@P("NUM-C14-P05-Tribute", "A Tribute unto Jehovah")
def p05(n):
    t, h = rows(340, None)
    r1 = night(h[0], cap(v("31:25"), "left: 12px; top: 12px", size=11) + god(sp("31:26-30"), "left: 12px; top: 50px", size=18.5, maxw=660) + vref("NUM 31:25–30", "right: 12px; bottom: 12px"))
    r2 = new(INK, W1, h[1], K14.spoil_chart(W1, h[1]), cap(v("31:31") + " " + v("31:32") + " " + v("31:33") + " " + v("31:34") + " " + v("31:35"), "left: 12px; top: 34px", size=11.5, maxw=300) + vref("NUM 31:31–35", "right: 12px; top: 8px"))
    return page("Numbers 31:25–35 — A Tribute unto Jehovah", t, r1 + r2, n)


@P("NUM-C14-P06-Halves", "The Half")
def p06(n):
    t, h = rows(None, 280)
    r1 = new(INK, W1, h[0], K14.spoil_chart(W1, h[0]), cap(sp("31:36-41"), "left: 12px; top: 34px", size=12, maxw=320) + vref("NUM 31:36–41", "right: 12px; top: 8px"))
    r2 = new(SAND, W1, h[1], K.levites_round("x6b", W1, h[1], 1462), cap(sp("31:42-47"), "left: 12px; top: 12px", size=11.5, maxw=560) + vref("NUM 31:42–47", "right: 12px; bottom: 12px"))
    return page("Numbers 31:36–47 — The Half", t, r1 + r2, n)


@P("NUM-C14-P07-Gold", "There Lacketh Not One Man of Us")
def p07(n):
    t, h = rows(300, None)
    r1 = talk(A2.OFFICER, h[0], GOLDEN, [("cap", v("31:48") + " " + v("31:49", to="said unto Moses,")), ("say", after("31:49", "said unto Moses,") + " " + v("31:50"))], ref="NUM 31:48–50", size=14)
    r2 = new(INK, W1, h[1], K14.gold(W1, h[1]), cap(sp("31:51-54"), "left: 12px; top: 34px", size=12.5, maxw=330)
             + vref("NUM 31:51–54", "left: 12px; bottom: 12px") + end_mark("NEXT · THE JOURNEYS", "right: 10px; bottom: 10px"))
    return page("Numbers 31:48–54 — There Lacketh Not One Man of Us", t, r1 + r2, n)
