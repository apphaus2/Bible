"""Genesis volume, Chapter 9 — Peniel (Genesis 31–33). Every verse, word for word from ref/eng-asv.
Reuses the digest's Book Four panels for the wrestling at the Jabbok and the meeting with Esau."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from genesis import G, art as X, art2 as Y, art3 as Z, art5 as K, art7 as J7, art8 as L, art9 as M
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import clan, hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch06 import RUST, GREENLIT, GOLDEN
from genesis.ch07 import LAMP, RED, BLUE
from genesis.ch08 import ROSE, OCHRE, PASTURE
from mk import defs, face

v, sp = G.v, G.span
B4 = "reference/genesis/book-04/"
Pen, Reu = (panels(B4 + n + ".dc.html") for n in ["B4-P07-Peniel", "B4-P08-Reunion"])
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
DREAM = "linear-gradient(180deg, #0B0B2A 0%, #2A1A5E 100%)"
START = 152                                  # chapter 8 ends on page 151
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def cosmic(w, h, cx=None): return X.cosmic(w, h, cx)

def jacob_face(h, tok=M.JACOB, w=W2, flip=False):
    return fc(tok, h, w=w, flip=flip)


@P("GEN-C09-00-Title", "Chapter 9 · Peniel")
def title():
    return chapter_title(9, "第九話", "Peniel", "Genesis 31 – 33", f'<g transform="translate(-200 120) scale(1.65)">{Pen[0].svg}</g>', NIGHT,
                         v("32:26", frm="I will not", to="bless me."), "Genesis · Volume One")


@P("GEN-C09-P01-Countenance", "152 · Return unto the Land of Thy Fathers")
def p01():
    t, h = rows(300, 170, None)
    r1 = new(PASTURE, W1, h[0], defs("c91a", *ALL) + M.muttering("c91a", W1, h[0], 911),
             cap(v("31:1", to="saying,"), "left: 12px; top: 12px", size=10.5, maxw=300)
             + balloon(v("31:1", frm="Jacob hath"), "right: 12px; top: 12px", 330, size=11.5, pad="20px 28px")
             + cap(v("31:2"), "left: 12px; top: 64px", size=10.5, maxw=300) + vref("GEN 31:1–2", "right: 12px; bottom: 12px"))
    r2 = new(NIGHT, W1, h[1], cosmic(W1, h[1]),
             cap(v("31:3", to="unto Jacob,"), "left: 12px; top: 12px", size=10.5)
             + god(v("31:3", frm="Return"), "left: 12px; top: 46px", size=18, maxw=640) + vref("GEN 31:3"))
    r3 = new(PASTURE, W1, h[2], defs("c91c", *ALL) + M.field_council("c91c", W1, h[2], 913),
             cap(v("31:4") + " " + v("31:5", to="unto them,"), "left: 12px; top: 12px", size=10.5, maxw=300)
             + balloon(v("31:5", frm="I see") + " " + v("31:6") + " " + v("31:7"), "right: 12px; top: 12px", 360, size=11.5, pad="26px 34px") + vref("GEN 31:4–7", "right: 12px; bottom: 12px"))
    return page("Genesis 31:1–7 — Return unto the Land of Thy Fathers", t, r1 + r2 + r3, START + 0)


@P("GEN-C09-P02-Dream", "153 · I Am the God of Beth-el")
def p02():
    t, h = rows(260, 230, None)
    r1 = new(BLUE, W1, h[0], jacob_face(h[0], w=W1),
             balloon(v("31:8") + " " + v("31:9"), "left: 270px; top: 20px", 410, size=12.5, pad="30px 40px") + vref("GEN 31:8–9", "left: 12px; bottom: 12px"))
    r2 = new(DREAM, W1, h[1], M.he_goats(None, W1, h[1], 922),
             balloon(v("31:10") + " " + v("31:11", to="said,"), "left: 12px; top: 12px", 420, size=11.5, pad="24px 34px")
             + balloon(v("31:11", frm="and I said,") , "right: 12px; top: 20px", 200, size=12, pad="14px 16px") + vref("GEN 31:10–11", "right: 12px; bottom: 12px"))
    r3 = new(NIGHT, W1, h[2], cosmic(W1, h[2]),
             god(v("31:12") + " " + v("31:13"), "left: 12px; top: 12px", size=15, maxw=660) + vref("GEN 31:12–13"))
    return page("Genesis 31:8–13 — I Am the God of Beth-el", t, r1 + r2 + r3, START + 1)


@P("GEN-C09-P03-Camels", "154 · Whatsoever God Hath Said unto Thee, Do")
def p03():
    t, h = rows(330, None)
    r1 = cols(new(ROSE, W2, h[0], fc(L.RACHEL, h[0]),
                  cap(v("31:14", to="unto him,"), "right: 8px; top: 8px", size=10, maxw=210)
                  + balloon(v("31:14", frm="Is there") + " " + v("31:15"), "right: 8px; bottom: 10px", 230, size=11, pad="22px 22px") + vref("GEN 31:14–15", "left: 8px; bottom: 8px")),
              new(OCHRE, W2, h[0], fc(L.LEAH, h[0]),
                  balloon(v("31:16"), "right: 8px; top: 12px", 230, size=11, pad="24px 22px") + vref("GEN 31:16", "left: 8px; bottom: 8px")))
    r2 = new(DAWN, W1, h[1], defs("c93b", *ALL) + M.camels_away("c93b", W1, h[1], 932),
             cap(v("31:17"), "left: 12px; top: 12px", size=11.5, maxw=360)
             + cap(v("31:18"), "right: 12px; top: 12px", size=10.5, maxw=300) + vref("GEN 31:17–18", "right: 12px; bottom: 12px"))
    return page("Genesis 31:14–18 — Whatsoever God Hath Said unto Thee, Do", t, r1 + r2, START + 2)


@P("GEN-C09-P04-Teraphim", "155 · Rachel Stole the Teraphim")
def p04():
    t, h = rows(250, 210, 210, None)
    r1 = new("#3A2214", W1, h[0], M.stolen_gods(None, W1, h[0], 941),
             cap(v("31:19"), "left: 12px; top: 12px", size=12, maxw=400) + vref("GEN 31:19", "right: 12px; top: 12px"))
    r2 = new("#0B1A2E", W1, h[1], M.gilead_map(W1, h[1], 942),
             cap(v("31:20") + " " + v("31:21"), "right: 12px; bottom: 12px", size=10.5, maxw=380) + vref("GEN 31:20–21", "left: 12px; bottom: 12px"))
    r3 = new(SAND, W1, h[2], M.overtake(None, W1, h[2], 943),
             cap(v("31:22"), "left: 12px; top: 12px", size=11, maxw=300)
             + cap(v("31:23"), "left: 12px; top: 66px", size=10.5, maxw=300) + hud("7 DAYS", "left: 14px; bottom: 14px", size=22) + vref("GEN 31:22–23", "right: 12px; bottom: 12px"))
    r4 = new("#0B0B2A", W1, h[3], defs("c94d", *ALL) + K.dreamer("c94d", W1, h[3], 944).replace("#1F5FAD", L.LABAN_ROBE),
             cap(v("31:24", to="and said unto him,"), "left: 12px; top: 12px", size=10.5, maxw=300)
             + god(v("31:24", frm="Take heed"), "right: 12px; top: 12px", size=14, maxw=320) + vref("GEN 31:24", "left: 12px; bottom: 12px"))
    return page("Genesis 31:19–24 — Rachel Stole the Teraphim", t, r1 + r2 + r3 + r4, START + 3)


@P("GEN-C09-P05-Gilead", "156 · Wherefore Hast Thou Stolen My Gods?")
def p05():
    t, h = rows(220, None)
    r1 = new(GREEN, W1, h[0], M.mount_camps(None, W1, h[0], 951),
             cap(v("31:25"), "left: 12px; top: 12px", size=11, maxw=500) + vref("GEN 31:25", "right: 12px; top: 12px"))
    r2 = new(RUST, W1, h[1], fc(M.LABAN_HOT, h[1], w=W1),
             cap(v("31:26", to="to Jacob,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("31:26", frm="What hast") + " " + v("31:27") + " " + v("31:28"), "left: 270px; top: 46px", 410, size=12, pad="30px 38px")
             + balloon(v("31:29") + " " + v("31:30"), "left: 270px; bottom: 14px", 410, size=12, pad="30px 38px") + vref("GEN 31:26–30", "left: 12px; bottom: 12px"))
    return page("Genesis 31:25–30 — Wherefore Hast Thou Stolen My Gods?", t, r1 + r2, START + 4)


@P("GEN-C09-P06-Search", "157 · He Searched, but Found Not")
def p06():
    t, h = rows(260, 230, None)
    r1 = new(BLUE, W1, h[0], jacob_face(h[0], w=W1),
             cap(v("31:31", to="to Laban,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("31:31", frm="Because") + " " + v("31:32", to="take it to thee."), "left: 270px; top: 46px", 410, size=12, pad="26px 36px")
             + cap(v("31:32", frm="For Jacob"), "right: 12px; bottom: 14px", size=11) + vref("GEN 31:31–32", "left: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], defs("c96b", *ALL) + M.tents_searched("c96b", W1, h[1], 962),
             cap(v("31:33"), "left: 12px; top: 12px", size=10.5, maxw=560) + vref("GEN 31:33", "right: 12px; bottom: 34px"))
    r3 = cols(new("#3A2214", W2, h[2], defs("c96c", *ALL) + M.saddle_seat("c96c", W2, h[2], 963),
                  cap(v("31:34"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 31:34", "left: 8px; bottom: 8px")),
              new(ROSE, W2, h[2], fc(M.RACHEL_SLY, h[2]),
                  cap(v("31:35", to="to her father,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("31:35", frm="Let not", to="upon me."), "right: 8px; top: 40px", 220, size=11.5, pad="22px 22px")
                  + cap(v("31:35", frm="And he searched"), "right: 8px; bottom: 8px", size=10.5, maxw=200) + vref("GEN 31:35", "left: 8px; bottom: 8px")))
    return page("Genesis 31:31–35 — He Searched, but Found Not", t, r1 + r2 + r3, START + 5)


@P("GEN-C09-P07-Chode", "158 · Jacob Was Wroth, and Chode with Laban")
def p07():
    t, h = rows(380, None)
    r1 = new(RED, W1, h[0], fc(M.JACOB_WROTH, h[0], w=W1),
             cap(v("31:36", to="to Laban,"), "left: 300px; top: 12px", size=10.5, maxw=380)
             + balloon(v("31:36", frm="What is my") + " " + v("31:37") + " " + v("31:38") + " " + v("31:39"), "left: 260px; top: 66px", 420, size=12, pad="34px 42px")
             + sfx("ドン", "DON", "left: 230px; top: 14px", size=40, fill="#D7261E", stroke="#F3EFE6", rot=-8) + vref("GEN 31:36–39", "left: 12px; bottom: 12px"))
    r2 = new("#E8A35A", W1, h[1], M.drought_frost(W1, h[1], 972),
             balloon(v("31:40"), "left: 50%; top: 16px; transform: translateX(-50%)", 430, size=13, pad="24px 34px") + vref("GEN 31:40", "right: 12px; bottom: 12px"))
    return page("Genesis 31:36–40 — Jacob Was Wroth, and Chode with Laban", t, r1 + r2, START + 6)


@P("GEN-C09-P08-Twenty", "159 · These Twenty Years")
def p08():
    t, h = rows(380, None)
    r1 = new(RED, W1, h[0], fc(M.JACOB_WROTH, h[0], w=W1),
             balloon(v("31:41") + " " + v("31:42"), "left: 260px; top: 20px", 420, size=12.5, pad="36px 44px")
             + hud("20 YEARS", "right: 14px; bottom: 14px", size=24) + vref("GEN 31:41–42", "left: 12px; bottom: 12px"))
    r2 = new(RUST, W1, h[1], fc(L.LABAN, h[1], w=W1),
             cap(v("31:43", to="unto Jacob,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("31:43", frm="The daughters") + " " + v("31:44"), "left: 270px; top: 46px", 410, size=12.5, pad="34px 40px") + vref("GEN 31:43–44", "left: 12px; bottom: 12px"))
    return page("Genesis 31:41–44 — These Twenty Years", t, r1 + r2, START + 7)


@P("GEN-C09-P09-Mizpah", "160 · Jehovah Watch between Me and Thee")
def p09():
    t, h = rows(300, 200, None)
    r1 = new(GREEN, W1, h[0], M.heap_of_witness(None, W1, h[0], 991),
             cap(v("31:45"), "left: 12px; top: 12px", size=11)
             + cap(v("31:46", to="unto his brethren,"), "left: 12px; top: 50px", size=10.5)
             + balloon(v("31:46", frm="Gather", to="stones;"), "left: 12px; top: 84px", 170, size=13, pad="14px 16px")
             + cap(v("31:46", frm="and they took"), "right: 12px; top: 12px", size=10.5, maxw=260)
             + cap(v("31:47"), "right: 12px; top: 84px", size=10.5, maxw=260) + vref("GEN 31:45–47", "left: 12px; bottom: 12px"))
    r2 = new("#0B1A2E", W1, h[1], M.mizpah(W1, h[1], 992),
             cap(v("31:48", to="Laban said,"), "left: 12px; top: 12px", size=10.5)
             + balloon(v("31:48", frm="This heap", to="this day."), "left: 12px; top: 46px", 260, size=12, pad="16px 22px")
             + cap(v("31:48", frm="Therefore") + " " + v("31:49", to="for he said,"), "right: 12px; top: 12px", size=10.5, maxw=260)
             + balloon(v("31:49", frm="Jehovah watch"), "right: 12px; bottom: 34px", 270, size=12, pad="18px 22px"))
    r3 = new(RUST, W1, h[2], fc(L.LABAN, h[2], w=W1),
             balloon(v("31:50"), "left: 270px; top: 24px", 410, size=13, pad="30px 40px") + vref("GEN 31:48–50", "left: 12px; bottom: 12px"))
    return page("Genesis 31:45–50 — Jehovah Watch between Me and Thee", t, r1 + r2 + r3, START + 8)


@P("GEN-C09-P10-Mahanaim", "161 · This Is God's Host")
def p10():
    t, h = rows(300, 200, None)
    r1 = new(RUST, W1, h[0], fc(L.LABAN_SLY, h[0], w=W1),
             cap(v("31:51", to="to Jacob,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("31:51", frm="Behold") + " " + v("31:52") + " " + v("31:53", to="judge betwixt us."), "left: 260px; top: 44px", 420, size=11.5, pad="32px 40px")
             + cap(v("31:53", frm="And Jacob sware"), "right: 12px; bottom: 14px", size=10.5, maxw=300) + vref("GEN 31:51–53", "left: 12px; bottom: 12px"))
    r2 = cols(new(GREEN, W2, h[1], M.heap_of_witness(None, W2, h[1], 9102),
                  cap(v("31:54"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 31:54", "right: 8px; bottom: 8px")),
              new(DAWN, W2, h[1], defs("c910b", *ALL) + M.kissed_goodbye("c910b", W2, h[1], 9103),
                  cap(v("31:55"), "left: 8px; top: 8px", size=10, maxw=320) + vref("GEN 31:55", "right: 8px; bottom: 8px")))
    r3 = new("#2A1A5E", W1, h[2], defs("c910c", *ALL) + M.gods_host("c910c", W1, h[2], 9104),
             cap(v("32:1"), "left: 12px; top: 12px", size=11.5, maxw=330)
             + cap(v("32:2", to="saw them,"), "right: 12px; top: 12px", size=10.5)
             + balloon(v("32:2", frm="This is", to="host:"), "right: 12px; top: 46px", 200, size=14, pad="14px 18px")
             + cap(v("32:2", frm="and he called"), "right: 12px; bottom: 14px", size=11) + vref("GEN 32:1–2", "left: 12px; bottom: 12px"))
    return page("Genesis 31:51–32:2 — This Is God's Host", t, r1 + r2 + r3, START + 9)


@P("GEN-C09-P11-FourHundred", "162 · Four Hundred Men with Him")
def p11():
    t, h = rows(250, 200, None)
    r1 = new(SAND, W1, h[0], defs("c911a", *ALL) + M.messengers("c911a", W1, h[0], 9111),
             cap(v("32:3") + " " + v("32:4", to="saying,"), "left: 12px; top: 12px", size=10.5, maxw=300)
             + balloon(v("32:4", frm="Thus shall") + " " + v("32:5"), "right: 12px; top: 12px", 330, size=10.5, pad="24px 30px") + vref("GEN 32:3–5", "left: 12px; bottom: 12px"))
    r2 = new(DUSK, W1, h[1], defs("c911b", *ALL) + M.four_hundred("c911b", W1, h[1], 9112),
             cap(v("32:6", to="saying,"), "left: 12px; top: 12px", size=10.5)
             + balloon(v("32:6", frm="We came"), "left: 12px; top: 46px", 380, size=12, pad="18px 28px")
             + hud("400", "right: 14px; top: 12px", size=32) + vref("GEN 32:6", "right: 12px; bottom: 12px"))
    r3 = cols(new("radial-gradient(circle at 70% 30%, #CFE0FF 0 20px, #4A3A8E 180px, #12113A 400px)", W2, h[2], fc(M.JACOB_AFRAID, h[2]),
                  cap(v("32:7"), "right: 8px; top: 8px", size=10, maxw=200) + vref("GEN 32:7", "left: 8px; bottom: 8px")),
              new(SAND, W2, h[2], M.two_companies(None, W2, h[2], 9113),
                  cap(v("32:8", to="he said,"), "left: 8px; top: 40px", size=10)
                  + balloon(v("32:8", frm="If Esau"), "left: 8px; top: 74px", 300, size=11.5, pad="20px 24px") + vref("GEN 32:8", "right: 8px; bottom: 8px")))
    return page("Genesis 32:3–8 — Four Hundred Men with Him", t, r1 + r2 + r3, START + 10)


@P("GEN-C09-P12-Prayer", "163 · Deliver Me, I Pray Thee")
def p12():
    t, h = rows(None)
    r1 = new("radial-gradient(circle at 70% 25%, #FFF4C2 0 40px, #6A5AAE 260px, #12113A 640px)", W1, h[0],
             face(M.JACOB_PRAY, -60, h[0] - 560, 1.4),
             cap(v("32:9", to="Jacob said,"), "left: 330px; top: 16px", size=11)
             + balloon(v("32:9", frm="O God") + " " + v("32:10"), "left: 300px; top: 56px", 380, size=12.5, pad="34px 40px")
             + balloon(v("32:11") + " " + v("32:12"), "left: 300px; top: 420px", 380, size=12.5, pad="34px 40px") + vref("GEN 32:9–12", "left: 12px; bottom: 12px"))
    return page("Genesis 32:9–12 — Deliver Me, I Pray Thee", t, r1, START + 11)


@P("GEN-C09-P13-Present", "164 · A Present for Esau")
def p13():
    t, h = rows(240, 290, None)
    r1 = new(SAND, W1, h[0], M.droves(None, W1, h[0], 9131),
             cap(v("32:13") + " " + v("32:14") + " " + v("32:15"), "left: 12px; top: 12px", size=10.5, maxw=500) + vref("GEN 32:13–15", "right: 12px; top: 12px"))
    r2 = new(BLUE, W1, h[1], jacob_face(h[1], w=W1),
             cap(v("32:16", to="unto his servants,"), "left: 300px; top: 12px", size=10.5, maxw=380)
             + balloon(v("32:16", frm="Pass over"), "left: 300px; top: 66px", 300, size=12, pad="16px 22px")
             + cap(v("32:17", to="saying,"), "left: 300px; top: 126px", size=10.5)
             + balloon(v("32:17", frm="When Esau") + " " + v("32:18"), "left: 270px; bottom: 10px", 410, size=11, pad="22px 30px") + vref("GEN 32:16–18", "left: 12px; bottom: 12px"))
    r3 = new(BLUE, W1, h[2], jacob_face(h[2], w=W1, flip=True),
             cap(v("32:19", to="saying,"), "left: 12px; top: 12px", size=10.5, maxw=400)
             + balloon(v("32:19", frm="On this") + " " + v("32:20", to="behind us."), "left: 12px; top: 66px", 400, size=11.5, pad="20px 30px")
             + cap(v("32:20", frm="For he said,", to="he said,"), "left: 12px; top: 170px", size=10.5)
             + balloon(v("32:20", frm="I will appease"), "left: 12px; top: 204px", 400, size=11.5, pad="18px 30px")
             + cap(v("32:21"), "left: 12px; bottom: 12px", size=10.5, maxw=400) + vref("GEN 32:19–21", "right: 12px; bottom: 12px"))
    return page("Genesis 32:13–21 — A Present for Esau", t, r1 + r2 + r3, START + 12)


@P("GEN-C09-P14-Wrestled", "165 · There Wrestled a Man with Him")
def p14():
    t, h = rows(200, 460, None)
    r1 = new(NIGHT, W1, h[0], defs("c914a", *ALL) + M.ford_jabbok("c914a", W1, h[0], 9141),
             cap(v("32:22") + " " + v("32:23"), "right: 12px; top: 12px", size=10.5, maxw=380) + vref("GEN 32:22–23", "left: 12px; top: 12px"))
    r2 = use(Pen[0], over=cap(v("32:24"), "left: 12px; top: 12px", size=11.5, maxw=340)
             + cap(v("32:25"), "left: 12px; bottom: 40px", size=10.5, maxw=300)
             + sfx("ググッ", "GUGU", "right: 24px; top: 20px", size=52, fill="#F3EFE6", stroke="#0D0D0F", rot=-6) + vref("GEN 32:24–25", "left: 12px; bottom: 12px"))
    r3 = use(Pen[1], over=cap(v("32:26", to="And he said,"), "right: 12px; top: 12px", size=10.5)
             + balloon(v("32:26", frm="Let me go", to="breaketh."), "right: 12px; top: 46px", 220, size=12, pad="14px 18px")
             + cap(v("32:26", frm="And he said, I", to="said,"), "left: 300px; top: 112px", size=10.5)
             + balloon(v("32:26", frm="I will not"), "left: 290px; bottom: 10px", 300, size=13.5, pad="16px 22px") + vref("GEN 32:26", "left: 12px; bottom: 12px"))
    return page("Genesis 32:22–26 — There Wrestled a Man with Him", t, r1 + r2 + r3, START + 13)


@P("GEN-C09-P15-Israel", "166 · I Have Seen God Face to Face")
def p15():
    t, h = rows(340, 300, None)
    r1 = cols(use(Pen[2], over=cap(v("32:27", to="unto him,"), "left: 8px; top: 8px", size=10)
                  + balloon(v("32:27", frm="What is"), "left: 8px; top: 40px", 160, size=12, pad="12px 14px")
                  + cap(v("32:27", frm="And he said, Jacob.", to="said,"), "right: 8px; top: 40px", size=10)
                  + balloon(v("32:27", frm="Jacob."), "right: 8px; top: 72px", 110, size=14, pad="10px 12px")
                  + cap(v("32:28", to="he said,"), "left: 8px; top: 120px", size=10)
                  + god(v("32:28", frm="Thy name"), "left: 8px; bottom: 8px", size=13, maxw=300)),
              new(NIGHT, W2, h[0], cosmic(W2, h[0]),
                  cap(v("32:29", to="and said,"), "left: 8px; top: 8px", size=10)
                  + balloon(v("32:29", frm="Tell me", to="thy name."), "left: 8px; top: 40px", 220, size=12, pad="16px 18px")
                  + cap(v("32:29", frm="And he said, Wherefore", to="said,"), "left: 8px; top: 120px", size=10)
                  + god(v("32:29", frm="Wherefore", to="my name?"), "left: 8px; top: 152px", size=14, maxw=320)
                  + cap(v("32:29", frm="And he blessed"), "left: 8px; bottom: 8px", size=11) + vref("GEN 32:27–29", "right: 8px; bottom: 8px")))
    r2 = new(DAWN, W1, h[1], defs("c915b", *ALL) + Y.ground(W1, h[1], h[1] * 0.86, "#7A6A5A", dy=0) + Z.sun(W1 * 0.6, h[1] * 0.82, 50, color="#FFC14D", op=0.35)
             + L.jacob_man("c915b", W1 * 0.3, h[1] * 0.86, Y.fit(h[1] * 0.86, h[1] * 0.4), staff=True, up=Z.HOLD_STAFF),
             cap(v("32:30", to="said he,"), "right: 12px; top: 12px", size=10.5, maxw=330)
             + balloon(v("32:30", frm="I have seen"), "right: 12px; top: 70px", 320, size=13, pad="20px 26px")
             + cap(v("32:31"), "right: 12px; bottom: 14px", size=11.5, maxw=340) + vref("GEN 32:30–31", "left: 12px; bottom: 12px"))
    r3 = new(DAWN, W1, h[2], M.unto_this_day(W1, h[2], 9153),
             cap(v("32:32"), "left: 12px; top: 12px", size=11, maxw=300) + vref("GEN 32:32", "right: 12px; bottom: 12px"))
    return page("Genesis 32:27–32 — I Have Seen God Face to Face", t, r1 + r2 + r3, START + 14)


@P("GEN-C09-P16-Esau", "167 · Esau Ran to Meet Him")
def p16():
    t, h = rows(300, None)
    r1 = use(Reu[0], over=cap(v("33:1"), "left: 12px; top: 12px", size=10.5, maxw=420)
             + cap(v("33:2") + " " + v("33:3"), "left: 12px; bottom: 60px", size=10.5, maxw=330) + vref("GEN 33:1–3", "right: 12px; bottom: 50px"))
    r2 = cols(use(Reu[1], over=cap(v("33:4"), "left: 8px; bottom: 8px", size=11.5, maxw=320) + vref("GEN 33:4", "left: 8px; top: 8px")),
              new(GOLDEN, W2, h[1], fc(M.ESAU_WEEP, h[1]),
                  cap(v("33:5", to="and said,"), "right: 8px; top: 8px", size=10, maxw=200)
                  + balloon(v("33:5", frm="Who are", to="with thee?"), "right: 8px; top: 76px", 180, size=12.5, pad="14px 16px")
                  + cap(v("33:5", frm="And he said,", to="said,"), "right: 8px; top: 156px", size=10)
                  + balloon(v("33:5", frm="The children"), "right: 8px; top: 188px", 210, size=11.5, pad="18px 20px") + vref("GEN 33:5", "left: 8px; bottom: 8px")))
    return page("Genesis 33:1–5 — Esau Ran to Meet Him", t, r1 + r2, START + 15)


@P("GEN-C09-P17-Gift", "168 · As One Seeth the Face of God")
def p17():
    t, h = rows(200, 260, None)
    r1 = new(SAND, W1, h[0], defs("c917a", *ALL) + M.bowing_all("c917a", W1, h[0], 9171),
             cap(v("33:6") + " " + v("33:7"), "left: 12px; top: 12px", size=10.5, maxw=500) + vref("GEN 33:6–7", "right: 12px; top: 12px"))
    r2 = cols(new(GOLDEN, W2, h[1], fc(M.ESAU_OLD, h[1]),
                  cap(v("33:8", to="he said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("33:8", frm="What meanest", to="which I met?"), "right: 8px; top: 40px", 210, size=11.5, pad="18px 20px")
                  + cap(v("33:9", to="Esau said,"), "right: 8px; top: 140px", size=10)
                  + balloon(v("33:9", frm="I have"), "right: 8px; top: 172px", 210, size=11.5, pad="16px 20px") + vref("GEN 33:8–9", "left: 8px; bottom: 8px")),
              new(BLUE, W2, h[1], jacob_face(h[1]),
                  cap(v("33:8", frm="And he said, To", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("33:8", frm="To find"), "right: 8px; top: 40px", 190, size=12, pad="16px 18px")
                  + cap(v("33:10", to="Jacob said,"), "right: 8px; top: 104px", size=10)
                  + balloon(v("33:10", frm="Nay"), "right: 8px; bottom: 8px", 240, size=10, pad="18px 20px")))
    r3 = cols(new(BLUE, W2, h[2], jacob_face(h[2]),
                  balloon(v("33:11", to="I have enough."), "right: 8px; top: 10px", 230, size=11, pad="22px 22px")
                  + cap(v("33:11", frm="And he urged"), "right: 8px; bottom: 8px", size=10.5) + vref("GEN 33:10–11", "left: 8px; bottom: 8px")),
              new(GOLDEN, W2, h[2], fc(M.ESAU_OLD, h[2]),
                  cap(v("33:12", to="he said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("33:12", frm="Let us"), "right: 8px; top: 40px", 210, size=12, pad="18px 20px") + vref("GEN 33:12", "left: 8px; bottom: 8px")))
    return page("Genesis 33:6–12 — As One Seeth the Face of God", t, r1 + r2 + r3, START + 16)


@P("GEN-C09-P18-Shechem", "169 · El-Elohe-Israel")
def p18():
    t, h = rows(300, 200, None)
    r1 = new(BLUE, W1, h[0], jacob_face(h[0], w=W1),
             cap(v("33:13", to="unto him,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("33:13", frm="My lord") + " " + v("33:14"), "left: 260px; top: 44px", 420, size=11.5, pad="32px 40px") + vref("GEN 33:13–14", "left: 12px; bottom: 12px"))
    r2 = cols(new(GOLDEN, W2, h[1], fc(M.ESAU_OLD, h[1]),
                  cap(v("33:15", to="Esau said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("33:15", frm="Let me now", to="with me."), "right: 8px; top: 40px", 210, size=11, pad="18px 18px") + vref("GEN 33:15", "left: 8px; bottom: 8px")),
              new(BLUE, W2, h[1], jacob_face(h[1]),
                  cap(v("33:15", frm="And he said, What", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("33:15", frm="What needeth"), "right: 8px; top: 40px", 210, size=11, pad="18px 18px")
                  + cap(v("33:16"), "right: 8px; bottom: 8px", size=10, maxw=200)))
    r3 = cols(new(GREEN, W2, h[2], M.succoth(None, W2, h[2], 9183),
                  cap(v("33:17"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 33:17", "right: 8px; bottom: 8px")),
              new(SKY, W2, h[2], defs("c918d", *ALL) + M.shechem_altar("c918d", W2, h[2], 9184),
                  cap(v("33:18") + " " + v("33:19") + " " + v("33:20"), "left: 8px; top: 8px", size=9.5, maxw=320)
                  + end_mark("NEXT · BETHEL AGAIN", "right: 10px; bottom: 10px")))
    return page("Genesis 33:13–20 — El-Elohe-Israel", t, r1 + r2 + r3, START + 17)
