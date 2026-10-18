"""Numbers volume, Chapter 7 — The Twelve Spies (Numbers 13–14). Every verse, word for word from ref/asv.
Lifts the digest's spy pages (the night camp, the grapes of Eshcol, the twelve, Caleb, the frightened spy, the Nephilim,
the weeping, Joshua and Caleb, the forty years) and adds the names of the twelve, a map of their road, Moses' plea and the
presumption at Hormah. 14:37 and 14:45 are told over landscape and silhouettes only."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from exo import art as A, art5 as A5, art8 as B8
from exo.kit import talk
from num import G, art as K, art7 as K7
from num.pages import Pages
from genesis import art as X
from genesis.ch02 import rows, grid, W1, W2, NIGHT, SKY, DUSK
from genesis.ch03 import SAND, clan
from genesis.ch04 import COLD, EMBER
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED, BLUE
from num import ch06 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
B1 = "reference/numbers/book-01/"
D1, D2, D3, D4 = (panels(B1 + n + ".dc.html") for n in ["NU1-P01-Spies", "NU1-P02-Report", "NU1-P03-Wept", "NU1-P04-Forty"])

def night(h, over, w=W1): return new(NIGHT, w, h, X.cosmic(w, h), over)
def after(ref, to):
    t = v(ref); return v(ref, frm=t[t.index(to) + len(to):].strip())


@P("NUM-C07-00-Title", "Chapter 7 · The Twelve Spies", title=True)
def title(n):
    a = D1[1]
    svg = f'<g transform="translate(-300 300) scale(2.0)">{a.svg}</g>'
    return chapter_title(7, "第七話", "The Twelve Spies", "Numbers 13 – 14", svg, a.bg, v("13:30", frm="Let us go up at once,"), "Numbers · Volume Four")


@P("NUM-C07-P01-Send", "Send Thou Men")
def p01(n):
    t, h = rows(300, None)
    r1 = use(D1[0], over=cap(v("13:1"), "left: 12px; top: 12px", size=11) + god(v("13:2"), "left: 12px; top: 50px", size=18, maxw=470)
             + mk.stamp(13, "right: 14px; bottom: 12px") + vref("NUM 13:1–2", "right: 12px; top: 12px"))
    r2 = new(SAND, W1, h[1], K7.sending("s1b", W1, h[1], 711), cap(v("13:3"), "left: 12px; top: 12px", size=13, maxw=520) + vref("NUM 13:3", "right: 12px; bottom: 12px"))
    return page("Numbers 13:1–3 — Send Thou Men", t, r1 + r2, n)


@P("NUM-C07-P02-Names", "These Were Their Names")
def p02(n):
    t, h = rows(None, 240)
    names = [("REUBEN", v("13:4"), "13:4"), ("SIMEON", v("13:5"), "13:5"), ("JUDAH", v("13:6"), "13:6"), ("ISSACHAR", v("13:7"), "13:7"),
             ("EPHRAIM", v("13:8"), "13:8"), ("BENJAMIN", v("13:9"), "13:9"), ("ZEBULUN", v("13:10"), "13:10"), ("MANASSEH", v("13:11"), "13:11"),
             ("DAN", v("13:12"), "13:12"), ("ASHER", v("13:13"), "13:13"), ("NAPHTALI", v("13:14"), "13:14"), ("GAD", v("13:15"), "13:15")]
    cells = [clan(tr.title(), tx, "NUM " + rf, K.TRIBE_C[tr] if K.TRIBE_C[tr] not in ("#3A3A5A", "#6A6A8A") else "#B8C0E8", size=15 if len(tx) < 70 else 13) for tr, tx, rf in names]
    r2 = talk(K7.JOSHUA, h[1], GOLDEN, [("cap", v("13:16"))], ref="NUM 13:16", size=13)
    return page("Numbers 13:4–16 — These Were Their Names", t, grid(cells, "repeat(3, minmax(0, 1fr))", ncol=4) + r2, n)


@P("NUM-C07-P03-SeeTheLand", "See the Land, What It Is")
def p03(n):
    t, h = rows(None, 280)
    r1 = talk(A.MOSES, h[0], GOLDEN, [("cap", v("13:17", to="said unto them,")), ("say", after("13:17", "said unto them,") + " " + v("13:18") + " " + v("13:19") + " " + v("13:20", to="fruit of the land."))], ref="NUM 13:17–20", size=16)
    r2 = new(SKY, W1, h[1], K7.hill_country(W1, h[1], 731), cap(v("13:20", frm="Now the time"), "left: 12px; top: 12px", size=13, maxw=420) + vref("NUM 13:20", "right: 12px; bottom: 12px"))
    return page("Numbers 13:17–20 — See the Land, What It Is", t, r1 + r2, n)


@P("NUM-C07-P04-Eshcol", "The Valley of Eshcol")
def p04(n):
    t, h = rows(None, 392)
    r1 = new("#0B1A2E", W1, h[0], K7.spy_map(W1, h[0]), cap(v("13:21") + " " + v("13:22"), "right: 12px; top: 12px", size=11.5, maxw=340) + vref("NUM 13:21–22", "right: 12px; bottom: 12px"))
    r2 = use(D1[1], over=cap(v("13:23") + " " + v("13:24"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("NUM 13:23–24", "right: 12px; top: 12px"))
    return page("Numbers 13:21–24 — The Valley of Eshcol", t, r1 + r2, n)


@P("NUM-C07-P05-Report", "It Floweth with Milk and Honey")
def p05(n):
    t, h = rows(None, 294)
    r1 = new(DUSK, W1, h[0], K.wilderness_camp("s5a", W1, h[0], 751, dusk=True, sinai=False), cap(v("13:25") + " " + v("13:26"), "left: 12px; top: 12px", size=12, maxw=520) + vref("NUM 13:25–26", "right: 12px; bottom: 12px"))
    r2 = use(D2[0], over=cap(v("13:27", to="and said,"), "left: 12px; top: 12px", size=11) + balloon(after("13:27", "and said,"), "right: 16px; top: 12px", 360, size=14, pad="20px 28px")
             + vref("NUM 13:27", "right: 12px; bottom: 12px"))
    return page("Numbers 13:25–27 — It Floweth with Milk and Honey", t, r1 + r2, n)


@P("NUM-C07-P06-Anak", "The Children of Anak")
def p06(n):
    t, h = rows(294, 280, None)
    r1 = cols(use(D2[1], over=balloon(v("13:28"), "right: 8px; top: 12px", 200, size=11, pad="18px 18px") + vref("NUM 13:28", "left: 8px; bottom: 8px")),
              new("#0B1A2E", W2, h[0], A.peoples_map(W2, h[0], 761), cap(v("13:29"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("NUM 13:29", "right: 8px; bottom: 8px")))
    r2 = talk(K7.CALEB, h[1], GOLDEN, [("cap", v("13:30", to="and said,")), ("say", after("13:30", "and said,"))], ref="NUM 13:30", size=18, flip=True)
    r3 = talk(K7.SPY, h[2], COLD, [("cap", v("13:31", to="said,")), ("say", after("13:31", "said,"))], ref="NUM 13:31", size=18)
    return page("Numbers 13:28–31 — The Children of Anak", t, r1 + r2 + r3, n)


@P("NUM-C07-P07-Grasshoppers", "As Grasshoppers")
def p07(n):
    t, h = rows(None, 398)
    r1 = talk(K7.SPY, h[0], COLD, [("cap", v("13:32", to="saying,")), ("say", after("13:32", "saying,"))], ref="NUM 13:32", size=17)
    r2 = use(D2[3], over=balloon(v("13:33"), "left: 14px; top: 14px", 400, size=15, pad="26px 30px") + vref("NUM 13:33", "left: 12px; bottom: 12px"))
    return page("Numbers 13:32–33 — As Grasshoppers", t, r1 + r2, n)


@P("NUM-C07-P08-Wept", "The People Wept That Night")
def p08(n):
    t, h = rows(274, None, 230)
    r1 = use(D3[0], over=cap(v("14:1"), "left: 12px; top: 12px", size=12, maxw=320) + mk.stamp(14, "right: 14px; top: 12px") + vref("NUM 14:1", "left: 12px; bottom: 12px"))
    r2 = talk(K7.HEBREW_ANGRY, h[1], RED, [("cap", v("14:2", to="said unto them,")), ("say", after("14:2", "said unto them,") + " " + v("14:3"))], ref="NUM 14:2–3", size=16)
    r3 = talk(K7.HEBREW_FEAR, h[2], DUSK, [("cap", v("14:4", to="one to another,")), ("say", after("14:4", "one to another,"))], ref="NUM 14:4", size=19, flip=True)
    return page("Numbers 14:1–4 — The People Wept That Night", t, r1 + r2 + r3, n)


@P("NUM-C07-P09-Rent", "An Exceeding Good Land")
def p09(n):
    t, h = rows(220, 294, None)
    r1 = new("#3A2A3A", W1, h[0], K7.fallen("s9a", W1, h[0], 791), cap(v("14:5"), "left: 12px; top: 12px", size=12, maxw=480) + vref("NUM 14:5", "right: 12px; bottom: 12px"))
    r2 = cols(use(D3[1], over=cap(v("14:6"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("NUM 14:6", "right: 8px; bottom: 8px")),
              use(D3[2], over=cap(v("14:7", to="saying,"), "right: 8px; top: 8px", size=10.5, maxw=230) + balloon(after("14:7", "saying,"), "left: 10px; top: 110px", 200, size=12, pad="18px 18px") + vref("NUM 14:7", "left: 8px; bottom: 8px")))
    r3 = talk(K7.CALEB, h[2], GOLDEN, [("say", v("14:8") + " " + v("14:9"))], ref="NUM 14:8–9", size=18)
    return page("Numbers 14:5–9 — An Exceeding Good Land", t, r1 + r2 + r3, n)


@P("NUM-C07-P10-HowLong", "How Long Will This People Despise Me?")
def p10(n):
    t, h = rows(330, None)
    r1 = new(GOLDEN, W1, h[0], K7.stoning("s10a", W1, h[0], 7101), cap(v("14:10"), "left: 12px; top: 12px", size=12.5, maxw=460) + vref("NUM 14:10", "right: 12px; bottom: 12px"))
    r2 = night(h[1], cap(v("14:11", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(after("14:11", "unto Moses,") + " " + v("14:12"), "left: 12px; top: 50px", size=23, maxw=640) + vref("NUM 14:11–12", "right: 12px; bottom: 12px"))
    return page("Numbers 14:10–12 — How Long Will This People Despise Me?", t, r1 + r2, n)


@P("NUM-C07-P11-Plea", "Then the Egyptians Will Hear It")
def p11(n):
    t, h = rows(None, 300)
    r1 = talk(A.MOSES_AFRAID, h[0], BLUE, [("cap", v("14:13", to="unto Jehovah,")), ("say", after("14:13", "unto Jehovah,") + " " + v("14:14"))], ref="NUM 14:13–14", size=16.5)
    r2 = talk(A.MOSES_AFRAID, h[1], BLUE, [("say", v("14:15") + " " + v("14:16"))], ref="NUM 14:15–16", size=17, flip=True)
    return page("Numbers 14:13–16 — Then the Egyptians Will Hear It", t, r1 + r2, n)


@P("NUM-C07-P12-Pardon", "Pardon, I Pray Thee")
def p12(n):
    t, h = rows(None, 280)
    r1 = talk(A.MOSES_CALM, h[0], GOLDEN, [("say", v("14:17") + " " + v("14:18") + " " + v("14:19"))], ref="NUM 14:17–19", size=17)
    r2 = night(h[1], cap(v("14:20", to="And Jehovah said,"), "left: 12px; top: 12px", size=11) + god(after("14:20", "Jehovah said,") + " " + v("14:21"), "left: 12px; top: 50px", size=23, maxw=640) + vref("NUM 14:20–21", "right: 12px; bottom: 12px"))
    return page("Numbers 14:17–21 — Pardon, I Pray Thee", t, r1 + r2, n)


@P("NUM-C07-P13-Caleb", "My Servant Caleb")
def p13(n):
    t, h = rows(None, 330)
    r1 = night(h[0], god(v("14:22") + " " + v("14:23"), "left: 12px; top: 12px", size=21, maxw=660) + god(v("14:25"), "left: 12px; bottom: 12px", size=17, maxw=520) + vref("NUM 14:22–23, 25", "right: 12px; bottom: 12px"))
    r2 = new(GOLDEN, W1, h[1], mk.face(K7.CALEB, -40, h[1] - 380 * min(1, (h[1] + 10) / 380) + 8, min(1, (h[1] + 10) / 380)), god(v("14:24"), "right: 12px; top: 12px", size=19, maxw=380) + vref("NUM 14:24", "right: 12px; bottom: 12px"))
    t, h = rows(None, 330, None) if False else (t, h)
    return page("Numbers 14:22–25 — My Servant Caleb", t, r1 + r2, n)


@P("NUM-C07-P14-AsILive", "As I Live, Saith Jehovah")
def p14(n):
    t, h = rows(None, 300)
    r1 = night(h[0], cap(v("14:26"), "left: 12px; top: 12px", size=11) + god(sp("14:27-30"), "left: 12px; top: 50px", size=20, maxw=660) + vref("NUM 14:26–30", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], K.muster("s14b", W1, h[1], 7142, rows_=3, per=12, scribes=False), god(v("14:31"), "left: 12px; top: 12px", size=17, maxw=480) + vref("NUM 14:31", "right: 12px; bottom: 12px"))
    return page("Numbers 14:26–31 — As I Live, Saith Jehovah", t, r1 + r2, n)


@P("NUM-C07-P15-Forty", "Forty Years")
def p15(n):
    t, h = rows(324, None)
    r1 = use(D4[0], over=god(v("14:32") + " " + v("14:33"), "left: 12px; top: 12px", size=16, maxw=470) + vref("NUM 14:32–33", "right: 12px; bottom: 12px"))
    r2 = night(h[1], god(v("14:34") + " " + v("14:35"), "left: 12px; top: 12px", size=23, maxw=660) + vref("NUM 14:34–35", "right: 12px; bottom: 12px"))
    return page("Numbers 14:32–35 — Forty Years", t, r1 + r2, n)


@P("NUM-C07-P16-Remained", "Joshua and Caleb Remained Alive")
def p16(n):
    t, h = rows(300, 260, None)
    r1 = new(DUSK, W1, h[0], K7.empty_wilderness(W1, h[0], 7161), cap(v("14:36") + " " + v("14:37"), "left: 12px; top: 12px", size=13, maxw=520) + vref("NUM 14:36–37", "right: 12px; bottom: 12px"))
    r2 = cols(new(GOLDEN, W2, h[1], mk.face(K7.JOSHUA, -40, h[1] - 380 * min(1, (h[1] + 10) / 380) + 8, min(1, (h[1] + 10) / 380)), ""),
              new(GOLDEN, W2, h[1], mk.face(K7.CALEB, W2 + 40, h[1] - 380 * min(1, (h[1] + 10) / 380) + 8, min(1, (h[1] + 10) / 380), flip=True), ""))
    r3 = new("#2A2A4A", W1, h[2], K7.empty_wilderness(W1, h[2], 7163), cap(v("14:38"), "left: 12px; top: 12px", size=13, maxw=520)
             + cap(v("14:39"), "left: 12px; top: 110px", size=13, maxw=520) + vref("NUM 14:38–39", "right: 12px; bottom: 12px"))
    return page("Numbers 14:36–39 — Joshua and Caleb Remained Alive", t, r1 + r2 + r3, n)


@P("NUM-C07-P17-Hormah", "Even unto Hormah")
def p17(n):
    t, h = rows(300, 300, None)
    r1 = new(SKY, W1, h[0], K7.presumed("s17a", W1, h[0], 7171), cap(v("14:40", to="saying,"), "right: 12px; top: 12px", size=11.5, maxw=330)
             + balloon(after("14:40", "saying,"), "right: 16px; top: 96px", 320, size=13, pad="18px 22px") + vref("NUM 14:40", "right: 12px; bottom: 12px"))
    r2 = talk(A.MOSES_STERN, h[1], RED, [("cap", v("14:41", to="And Moses said,")), ("say", after("14:41", "Moses said,") + " " + v("14:42") + " " + v("14:43"))], ref="NUM 14:41–43", size=13)
    r3 = new("#3A1A1A", W1, h[2], K7.presumed("s17c", W1, h[2], 7173, smitten=True), cap(v("14:44") + " " + v("14:45"), "right: 12px; top: 12px", size=12, maxw=360)
             + vref("NUM 14:44–45", "left: 12px; bottom: 12px") + end_mark("NEXT · KORAH", "right: 10px; bottom: 10px"))
    return page("Numbers 14:40–45 — Even unto Hormah", t, r1 + r2 + r3, n)
