"""Numbers volume, Chapter 10 — Meribah and the Serpent of Brass (Numbers 20–21). Every verse, word for word from ref/eng-asv.
Miriam's death at Kadesh; the waters of Meribah (the digest's rock panels); Edom's refusal; Aaron on mount Hor (his death a
caption over the empty summit); Arad and Hormah; the fiery serpents and the serpent of brass (the digest's panels); the
journeys to Pisgah with the songs of the Arnon, of the well and of Heshbon in song boxes; Sihon and Og."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from exo import art as A, art8 as B8
from exo.kit import talk, song
from num import G, art as K, art7 as K7, art10 as K10
from num.pages import Pages
from genesis import art as X
from genesis.ch02 import rows, grid, W1, W2, NIGHT, SKY, DUSK
from genesis.ch03 import SAND
from genesis.ch04 import COLD, EMBER
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED, BLUE
from num import ch09 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
B1 = "reference/numbers/book-01/"
D4, D5, D6 = (panels(B1 + n + ".dc.html") for n in ["NU1-P04-Forty", "NU1-P05-Rock", "NU1-P06-Serpent"])
INK = "#0B1A2E"

def night(h, over, w=W1): return new(NIGHT, w, h, X.cosmic(w, h), over)
def after(ref, to):
    t = v(ref); return v(ref, frm=t[t.index(to) + len(to):].strip())


@P("NUM-C10-00-Title", "Chapter 10 · Meribah and the Serpent of Brass", title=True)
def title(n):
    a = D6[3]
    svg = f'<g transform="translate(-160 280) scale(1.6)">{a.svg}</g>'
    return chapter_title(10, "第十話", "Meribah and the Serpent of Brass", "Numbers 20 – 21", svg, a.bg, v("21:8", frm="every one that is bitten,"), "Numbers · Volume Four")


@P("NUM-C10-P01-Miriam", "Miriam Died There")
def p01(n):
    t, h = rows(330, None)
    r1 = new(DUSK, W1, h[0], K10.miriam_grave("r1a", W1, h[0], 1011), cap(v("20:1"), "left: 12px; top: 12px", size=13, maxw=480) + mk.stamp(20, "right: 14px; top: 12px") + vref("NUM 20:1", "right: 12px; bottom: 12px"))
    r2 = talk(A.HEBREW_ANGRY, h[1], RED, [("cap", v("20:2") + " " + v("20:3", to="saying,")), ("say", after("20:3", "saying,") + " " + v("20:4") + " " + v("20:5"))], ref="NUM 20:2–5", size=16)
    return page("Numbers 20:1–5 — Miriam Died There", t, r1 + r2, n)


@P("NUM-C10-P02-Speak", "Speak Ye unto the Rock")
def p02(n):
    t, h = rows(220, None, 274)
    r1 = new("#3A2A3A", W1, h[0], K7.fallen("r2a", W1, h[0], 1021), cap(v("20:6"), "left: 12px; top: 12px", size=12, maxw=520) + vref("NUM 20:6", "right: 12px; bottom: 12px"))
    r2 = night(h[1], cap(v("20:7"), "left: 12px; top: 12px", size=11) + god(v("20:8"), "left: 12px; top: 50px", size=21, maxw=640) + vref("NUM 20:7–8", "right: 12px; bottom: 12px"))
    r3 = use(D4[2], over=cap(v("20:9"), "left: 12px; bottom: 12px", size=12, maxw=380))
    return page("Numbers 20:6–9 — Speak Ye unto the Rock", t, r1 + r2 + r3, n)


@P("NUM-C10-P03-Rebels", "Hear Now, Ye Rebels")
def p03(n):
    t, h = rows(294, 434, None)
    r1 = use(D5[0], over=cap(v("20:10", to="said unto them,"), "right: 12px; top: 12px", size=11, maxw=300) + balloon(after("20:10", "said unto them,"), "right: 24px; top: 90px", 320, size=17, pad="24px 30px") + vref("NUM 20:10", "left: 12px; bottom: 12px"))
    r2 = use(D5[1], over=cap(v("20:11"), "left: 12px; top: 12px", size=12, maxw=320) + sfx("ガン！", "GAN!", "left: 320px; top: 30px", size=44, fill="#F3EFE6", stroke="#0D0D0F", rot=-8) + vref("NUM 20:11", "right: 12px; bottom: 12px"))
    r3 = use(D5[2], over=cap(v("20:12", to="Moses and Aaron,"), "left: 12px; top: 12px", size=11) + god(after("20:12", "Moses and Aaron,"), "left: 12px; top: 48px", size=15, maxw=470)
             + cap(v("20:13"), "right: 12px; bottom: 34px", size=11, maxw=300) + vref("NUM 20:12–13", "right: 12px; bottom: 10px"))
    return page("Numbers 20:10–13 — Hear Now, Ye Rebels", t, r1 + r2 + r3, n)


@P("NUM-C10-P04-Edom", "Let Us Pass, I Pray Thee")
def p04(n):
    t, h = rows(None, 300)
    r1 = talk(A.MOSES, h[0], GOLDEN, [("cap", v("20:14", to="unto the king of Edom,")), ("say", after("20:14", "unto the king of Edom,") + " " + v("20:15") + " " + v("20:16") + " " + v("20:17"))], ref="NUM 20:14–17", size=15)
    r2 = new(SKY, W1, h[1], K10.edom("r4b", W1, h[1], 1042), cap(v("20:18", to="said unto him,"), "left: 12px; top: 12px", size=11)
             + balloon(after("20:18", "said unto him,"), "left: 18px; top: 52px", 360, size=15, pad="20px 26px") + vref("NUM 20:18", "right: 12px; bottom: 12px"))
    return page("Numbers 20:14–18 — Let Us Pass, I Pray Thee", t, r1 + r2, n)


@P("NUM-C10-P05-Refused", "Thus Edom Refused")
def p05(n):
    t, h = rows(250, None)
    r1 = talk(A.MOSES, h[0], GOLDEN, [("cap", v("20:19", to="said unto him,")), ("say", after("20:19", "said unto him,"))], ref="NUM 20:19", size=15)
    r2 = new(RED, W1, h[1], K10.edom("r5b", W1, h[1], 1052, army=True),
             cap(v("20:20", to="And he said,"), "left: 12px; top: 12px", size=11) + balloon(after("20:20", "And he said,").split(" And Edom")[0], "left: 18px; top: 52px", 300, size=16, pad="18px 24px")
             + cap(v("20:20", frm="And Edom came out") + " " + v("20:21"), "left: 12px; bottom: 34px", size=12, maxw=360) + vref("NUM 20:20–21", "right: 12px; bottom: 12px"))
    return page("Numbers 20:19–21 — Thus Edom Refused", t, r1 + r2, n)


@P("NUM-C10-P06-Hor", "Mount Hor")
def p06(n):
    t, h = rows(None, 380)
    r1 = night(h[0], cap(v("20:22") + " " + v("20:23"), "left: 12px; top: 12px", size=11.5, maxw=560) + god(sp("20:24-26"), "left: 12px; top: 80px", size=20, maxw=640) + vref("NUM 20:22–26", "right: 12px; bottom: 12px"))
    r2 = new("#E8B880", W1, h[1], K10.hor("r6b", W1, h[1], 1062, stage=0), cap(v("20:27"), "right: 12px; top: 12px", size=12.5, maxw=360) + vref("NUM 20:27", "right: 12px; bottom: 12px"))
    return page("Numbers 20:22–27 — Mount Hor", t, r1 + r2, n)


@P("NUM-C10-P07-Aaron", "They Wept for Aaron Thirty Days")
def p07(n):
    t, h = rows(300, 280, None)
    r1 = new("#5B2470", W1, h[0], K10.hor("r7a", W1, h[0], 1071, stage=1), cap(v("20:28", to="his son;"), "left: 12px; top: 12px", size=12.5, maxw=420)
             + cap(v("20:28", frm="and Aaron died"), "left: 12px; bottom: 30px", size=13, maxw=420) + vref("NUM 20:28", "right: 12px; bottom: 12px"))
    r2 = cols(new("#E8B880", W2, h[1], K10.hor("r7b", W2, h[1], 1072, stage=2), ""),
              new(GOLDEN, W2, h[1], mk.face(K10.ELEAZAR, W2 + 40, h[1] - 380 * min(1, (h[1] + 10) / 380) + 8, min(1, (h[1] + 10) / 380), flip=True), ""))
    r3 = new("#3A2A4A", W1, h[2], K10.mourning("r7c", W1, h[2], 1073), cap(v("20:29"), "left: 12px; top: 12px", size=13, maxw=480) + vref("NUM 20:29", "right: 12px; bottom: 12px"))
    return page("Numbers 20:28–29 — They Wept for Aaron Thirty Days", t, r1 + r2 + r3, n)


@P("NUM-C10-P08-Arad", "Hormah")
def p08(n):
    t, h = rows(None, 330)
    r1 = new(SAND, W1, h[0], K10.host("r8a", W1, h[0], 1081, foe="#4A2A3A"), mk.stamp(21, "right: 14px; bottom: 12px") + cap(v("21:1") + " " + v("21:2") + " " + v("21:3"), "left: 12px; top: 12px", size=12.5, maxw=520) + vref("NUM 21:1–3", "left: 12px; bottom: 12px"))
    r2 = use(D6[0], over=cap(v("21:4"), "left: 12px; bottom: 12px", size=11.5, maxw=360) + cap(v("21:5", to="against Moses,"), "left: 12px; top: 12px", size=11, maxw=260)
             + balloon(after("21:5", "against Moses,"), "right: 16px; top: 12px", 360, size=12.5, pad="18px 24px") + vref("NUM 21:4–5", "right: 12px; bottom: 12px"))
    return page("Numbers 21:1–5 — Hormah", t, r1 + r2, n)


@P("NUM-C10-P09-Serpents", "Fiery Serpents")
def p09(n):
    t, h = rows(274, None)
    r1 = cols(use(D6[1], over=cap(v("21:6"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("NUM 21:6", "right: 8px; bottom: 8px")),
              use(D6[2], over=cap(v("21:7", to="and said,"), "left: 8px; top: 8px", size=10.5) + balloon(v("21:7", frm="We have sinned,", to="serpents from us."), "left: 10px; top: 44px", 230, size=10.5, pad="16px 18px")
                  + cap(v("21:7", frm="And Moses prayed"), "right: 8px; bottom: 8px", size=10.5)))
    r2 = use(D6[3], over=cap(v("21:8", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(after("21:8", "unto Moses,"), "left: 12px; top: 50px", size=15, maxw=330)
             + cap(v("21:9"), "right: 12px; top: 12px", size=11.5, maxw=290) + vref("NUM 21:8–9", "right: 12px; bottom: 12px"))
    return page("Numbers 21:6–9 — Fiery Serpents", t, r1 + r2, n)


@P("NUM-C10-P10-Journeys", "The Valleys of the Arnon")
def p10(n):
    t, h = rows(None, 300)
    r1 = new(INK, W1, h[0], K10.journeys(W1, h[0], hi=("MOUNT HOR", "OBOTH", "IYE-ABARIM", "ZERED", "ARNON")),
             cap(v("21:10") + " " + v("21:11") + " " + v("21:12") + " " + v("21:13"), "right: 12px; top: 12px", size=11.5, maxw=300) + vref("NUM 21:10–13", "right: 12px; bottom: 12px"))
    r2 = new(DUSK, W1, h[1], K7.empty_wilderness(W1, h[1], 10102),
             cap(v("21:14", to="Wars of Jehovah,"), "left: 12px; top: 12px", size=11, maxw=520)
             + song(v("21:14", frm="Vaheb") + " " + v("21:15"), "left: 12px; top: 64px", size=17, maxw=520) + vref("NUM 21:14–15", "right: 12px; bottom: 12px"))
    return page("Numbers 21:10–15 — The Valleys of the Arnon", t, r1 + r2, n)


@P("NUM-C10-P11-Well", "Spring Up, O Well")
def p11(n):
    t, h = rows(None, 260)
    r1 = new(SKY, W1, h[0], K10.well("r11a", W1, h[0], 1111), cap(v("21:16"), "left: 12px; top: 12px", size=12, maxw=520)
             + cap(v("21:17", to="this song:"), "left: 12px; top: 100px", size=11) + song(v("21:17", frm="Spring up,") + " " + v("21:18", to="their staves."), "left: 12px; top: 140px", size=18, maxw=400)
             + vref("NUM 21:16–18", "right: 12px; bottom: 12px"))
    r2 = new(INK, W1, h[1], K10.journeys(W1, h[1], hi=("BEER", "MATTANAH", "NAHALIEL", "BAMOTH", "PISGAH")),
             cap(v("21:18", frm="And from the wilderness") + " " + v("21:19") + " " + v("21:20"), "right: 12px; top: 12px", size=11, maxw=300) + vref("NUM 21:18–20", "right: 12px; bottom: 12px"))
    return page("Numbers 21:16–20 — Spring Up, O Well", t, r1 + r2, n)


@P("NUM-C10-P12-Sihon", "Sihon King of the Amorites")
def p12(n):
    t, h = rows(250, None)
    r1 = talk(A.MOSES, h[0], GOLDEN, [("cap", v("21:21")), ("say", v("21:22"))], ref="NUM 21:21–22", size=15)
    r2 = new(SAND, W1, h[1], K10.host("r12b", W1, h[1], 1122), cap(sp("21:23-26"), "left: 12px; top: 12px", size=12, maxw=500) + vref("NUM 21:23–26", "right: 12px; bottom: 12px"))
    return page("Numbers 21:21–26 — Sihon King of the Amorites", t, r1 + r2, n)


@P("NUM-C10-P13-Heshbon", "Come Ye to Heshbon")
def p13(n):
    t, h = rows(None, 300)
    r1 = new(EMBER, W1, h[0], K10.host("r13a", W1, h[0], 1131, foe="#3A1A1A"), cap(v("21:27", to="say,"), "left: 12px; top: 12px", size=11)
             + song(v("21:27", frm="Come ye") + " " + v("21:28") + " " + v("21:29") + " " + v("21:30"), "left: 12px; top: 50px", size=16, maxw=480) + vref("NUM 21:27–30", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], K.wilderness_camp("r13b", W1, h[1], 1132, sinai=False), cap(v("21:31") + " " + v("21:32"), "left: 12px; top: 12px", size=12.5, maxw=480) + vref("NUM 21:31–32", "right: 12px; bottom: 12px"))
    return page("Numbers 21:27–32 — Come Ye to Heshbon", t, r1 + r2, n)


@P("NUM-C10-P14-Og", "Og the King of Bashan")
def p14(n):
    t, h = rows(None, 280)
    r1 = new(DUSK, W1, h[0], K10.host("r14a", W1, h[0], 1141, foe="#2A2A3A", giant=True), cap(v("21:33"), "left: 12px; top: 12px", size=12.5, maxw=460) + vref("NUM 21:33", "right: 12px; bottom: 12px"))
    r2 = night(h[1], cap(v("21:34", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(after("21:34", "unto Moses,"), "left: 12px; top: 50px", size=17, maxw=640)
               + cap(v("21:35"), "left: 12px; bottom: 12px", size=11.5, maxw=420) + end_mark("NEXT · BALAAM", "right: 10px; bottom: 10px"))
    return page("Numbers 21:33–35 — Og the King of Bashan", t, r1 + r2, n)
