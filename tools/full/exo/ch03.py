"""Exodus volume, Chapter 3 — The Passover (Exodus 9–12). Every verse, word for word from ref/asv.
The ordinances of the first month (12:14–20) get a technical calendar of the feast of unleavened bread."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from exo import G, art as A, art2 as B, art3 as C
from exo.kit import talk
from exo.ch01 import FIRE, bush_panel
from exo.ch02 import night
from genesis import art as X, art2 as Y, art3 as Z, art10 as T, art12 as V12
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch06 import RUST, GREENLIT, GOLDEN
from genesis.ch07 import RED, BLUE
from genesis.ch12 import NILE, COURT
from mk import defs, face

v, sp = G.v, G.span
H, L, K, M = [panels("digest/exodus/book-02/" + n + ".dc.html") for n in ["EX2-P05-Hail", "EX2-P06-Locusts", "EX2-P07-Darkness", "EX2-P08-Midnight"]]
LB, BL, CR, EXO = [panels("digest/exodus/book-03/" + n + ".dc.html") for n in ["EX3-P01-Lamb", "EX3-P02-Blood", "EX3-P03-Cry", "EX3-P04-Exodus"]]
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
CAL = "#0B1A2E"
START = 41                                   # chapter 2 ends on page 40
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco


@P("EXO-C03-00-Title", "Chapter 3 · The Passover")
def title():
    a = BL[1]
    return chapter_title(3, "第三話", "The Passover", "Exodus 9 – 12", f'<g transform="translate(-520 0) scale(2.76)">{a.svg}</g>', a.bg,
                         v("12:13", frm="when I see the blood,", to="pass over you"), "Exodus · Volume Two")


@P("EXO-C03-P01-Murrain", "41 · A Very Grievous Murrain")
def p01():
    t, h = rows(330, 230, None)
    r1 = new(SKY, W1, h[0], C.herds(W1, h[0], 411), cap(v("9:1", to="unto Moses,"), "left: 12px; top: 12px", size=11)
             + god(v("9:1", frm="Go in") + " " + v("9:2") + " " + v("9:3"), "left: 12px; top: 48px", size=14, maxw=640) + mk.stamp(9, "right: 14px; bottom: 12px") + vref("EX 9:1–3", "left: 12px; bottom: 12px"))
    r2 = cols(new(SKY, W2, h[1], B.goshen_divide(W2, h[1], 412, plague="murrain"), god(v("9:4"), "left: 8px; top: 8px", size=12.5, maxw=320) + vref("EX 9:4", "right: 8px; top: 8px")),
              night(W2, h[1], cap(v("9:5", to="saying,"), "left: 8px; top: 8px", size=10.5) + god(v("9:5", frm="To-morrow"), "left: 8px; top: 44px", size=16, maxw=320) + vref("EX 9:5", "right: 8px; bottom: 8px")))
    r3 = cols(use(H[0], over=cap(v("9:6"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 9:6", "right: 8px; bottom: 8px")),
              talk(A.PHARAOH, h[2], RED, [("cap", v("9:7"))], w=W2, flip=True, ref="EX 9:7"))
    return page("Exodus 9:1–7 — A Very Grievous Murrain", t, r1 + r2 + r3, START + 0)


@P("EXO-C03-P02-Boils", "42 · Ashes of the Furnace")
def p02():
    t, h = rows(250, 300, None)
    r1 = night(W1, h[0], cap(v("9:8", to="unto Aaron,"), "left: 12px; top: 12px", size=11) + god(v("9:8", frm="Take to you") + " " + v("9:9"), "left: 12px; top: 48px", size=15, maxw=640) + vref("EX 9:8–9", "right: 12px; bottom: 12px"),
               extra=E.blaze(W1 * 0.88, h[0], 60, 60, 421))
    r2 = cols(use(H[1], over=cap(v("9:10"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 9:10", "right: 8px; bottom: 8px")),
              talk(C.MAGICIAN_BOILS, h[1], "linear-gradient(180deg, #2A1A4E 0%, #7A3BA8 100%)", [("cap", v("9:11"))], w=W2, flip=True, ref="EX 9:11"))
    r3 = cols(talk(A.PHARAOH, h[2], RED, [("cap", v("9:12"))], w=W2, ref="EX 9:12"),
              night(W2, h[2], cap(v("9:13", to="say unto him,"), "left: 8px; top: 8px", size=10.5, maxw=320) + god(v("9:13", frm="Thus saith"), "left: 8px; top: 80px", size=15, maxw=320) + vref("EX 9:13", "right: 8px; bottom: 8px")))
    return page("Exodus 9:8–13 — Ashes of the Furnace", t, r1 + r2 + r3, START + 1)


@P("EXO-C03-P03-Power", "43 · To Show Thee My Power")
def p03():
    t, h = rows(230, 260, 240, None)
    r1 = new(NIGHT, W1, h[0], A.wonders(W1, h[0], 431), god(v("9:14"), "left: 12px; top: 12px", size=16, maxw=470) + vref("EX 9:14", "right: 12px; bottom: 12px"))
    r2 = new(COURT, W1, h[1], defs("x33b", *ALL) + T.stage("x33b", W1, h[1], 432, "palace", [(A.moses, 0.22, 0.46, False, "staff"), (A.pharaoh, 0.78, 0.48, True)]),
             god(v("9:15") + " " + v("9:16"), "left: 50%; top: 12px; transform: translateX(-50%)", size=14.5, maxw=380) + vref("EX 9:15–16", "right: 12px; bottom: 12px"))
    r3 = new("#2A2A4A", W1, h[2], C.hail_field(W1, h[2], 433), god(v("9:17") + " " + v("9:18"), "left: 12px; top: 12px", size=15, maxw=470) + vref("EX 9:17–18", "right: 12px; bottom: 12px"))
    r4 = new(SKY, W1, h[3], C.herds(W1, h[3], 434), god(v("9:19"), "left: 12px; top: 12px", size=14, maxw=640) + vref("EX 9:19", "right: 12px; bottom: 12px"))
    return page("Exodus 9:14–19 — To Show Thee My Power", t, r1 + r2 + r3 + r4, START + 2)


@P("EXO-C03-P04-Hail", "44 · Thunder and Hail")
def p04():
    t, h = rows(250, 190, None)
    r1 = cols(new(SAND, W2, h[0], defs("x34a", *ALL) + T.stage("x34a", W2, h[0], 441, "egypt", [(("egypt", "#F3EFE6"), 0.2, 0.46, False, "point")], props=C.S1.cow(W2 * 0.46, h[0] * 0.88, 0.3, flip=True)),
              cap(v("9:20"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 9:20", "right: 8px; bottom: 8px")),
              new(SKY, W2, h[0], C.herds(W2, h[0], 442), cap(v("9:21"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 9:21", "right: 8px; bottom: 8px")))
    r2 = night(W1, h[1], cap(v("9:22", to="unto Moses,"), "left: 12px; top: 12px", size=10.5) + god(v("9:22", frm="Stretch forth"), "left: 12px; top: 46px", size=14, maxw=660) + vref("EX 9:22", "right: 12px; bottom: 12px"))
    r3 = use(H[3], over=cap(v("9:23"), "left: 12px; top: 12px", size=11, maxw=420) + cap(v("9:24"), "right: 12px; bottom: 14px", size=11, maxw=330)
             + sfx("ゴロゴロ", "GORO GORO", "right: 30px; top: 30px", size=44, fill="#FFF4C2", stroke="#0D0D0F", rot=-6) + vref("EX 9:23–24", "left: 12px; bottom: 12px"))
    return page("Exodus 9:20–24 — Thunder and Hail", t, r1 + r2 + r3, START + 3)


@P("EXO-C03-P05-Sinned", "45 · I Have Sinned This Time")
def p05():
    t, h = rows(250, 250, None)
    r1 = new("#2A2A4A", W1, h[0], C.hail_field(W1, h[0], 451), cap(v("9:25"), "left: 12px; top: 12px", size=11, maxw=430) + vref("EX 9:25", "right: 12px; bottom: 12px"))
    r2 = cols(new(SKY, W2, h[1], B.goshen_divide(W2, h[1], 452, plague="hail"), cap(v("9:26"), "left: 8px; top: 8px", size=11, maxw=150) + vref("EX 9:26", "right: 8px; top: 8px")),
              talk(A.PHARAOH_FEAR, h[1], RED, [("cap", v("9:27", to="said unto them,")), ("say", v("9:27", frm="I have sinned"))], w=W2, flip=True, ref="EX 9:27", size=12.5))
    r3 = cols(talk(A.PHARAOH_FEAR, h[2], RED, [("say", v("9:28"))], w=W2, ref="EX 9:28", size=13),
              talk(A.MOSES_CALM, h[2], GOLDEN, [("cap", v("9:29", to="unto him,")), ("say", v("9:29", frm="As soon"))], w=W2, flip=True, ref="EX 9:29", size=11.5))
    return page("Exodus 9:25–29 — I Have Sinned This Time", t, r1 + r2 + r3, START + 4)


@P("EXO-C03-P06-Flax", "46 · The Barley Was in the Ear")
def p06():
    t, h = rows(200, 240, 250, None)
    r1 = talk(A.MOSES_STERN, h[0], RED, [("say", v("9:30"))], ref="EX 9:30", size=15)
    r2 = new(SKY, W1, h[1], C.crops(W1, h[1], 461), cap(v("9:31"), "left: 12px; top: 12px", size=11, maxw=300) + cap(v("9:32"), "right: 12px; top: 12px", size=11, maxw=300) + vref("EX 9:31–32", "right: 12px; bottom: 30px"))
    r3 = new(GREY, W1, h[2], C.spread_hands("x36c", W1, h[2], 463), cap(v("9:33"), "left: 12px; top: 12px", size=11, maxw=420) + vref("EX 9:33", "right: 12px; bottom: 12px"))
    r4 = talk(A.PHARAOH, h[3], RED, [("cap", v("9:34")), ("cap", v("9:35"))], ref="EX 9:34–35")
    return page("Exodus 9:30–35 — The Barley Was in the Ear", t, r1 + r2 + r3 + r4, START + 5)


@P("EXO-C03-P07-HowLong", "47 · How Long Wilt Thou Refuse?")
def p07():
    t, h = rows(300, 260, None)
    r1 = new(TENT, W1, h[0], defs("x37a", *ALL) + C.father_son("x37a", W1, h[0], 471),
             cap(v("10:1", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(v("10:1", frm="Go in") + " " + v("10:2"), "right: 12px; top: 12px", size=14.5, maxw=380)
             + mk.stamp(10, "left: 14px; bottom: 14px") + vref("EX 10:1–2", "right: 12px; bottom: 12px"))
    r2 = use(L[0], over=cap(v("10:3", to="said unto him,"), "right: 12px; top: 12px", size=10.5, maxw=380) + balloon(v("10:3", frm="Thus saith"), "right: 20px; top: 70px", 380, size=13.5, pad="20px 28px") + vref("EX 10:3", "left: 12px; bottom: 12px"))
    r3 = talk(A.MOSES_STERN, h[2], RED, [("say", v("10:4"))], ref="EX 10:4", size=16, extra=E2.locusts(12, W1 * 0.5, W1, h[2] * 0.5, h[2], 473))
    return page("Exodus 10:1–4 — How Long Wilt Thou Refuse?", t, r1 + r2 + r3, START + 6)


@P("EXO-C03-P08-Snare", "48 · Knowest Thou Not Yet That Egypt Is Destroyed?")
def p08():
    t, h = rows(290, 260, None)
    r1 = new("#4A3A1A", W1, h[0], C.locust_land(W1, h[0], 481), balloon(v("10:5"), "left: 20px; top: 16px", 470, size=13.5, pad="22px 34px") + vref("EX 10:5", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], C.houses_filled(W1, h[1], 482), balloon(v("10:6", to="unto this day."), "left: 20px; top: 14px", 470, size=13, pad="20px 30px")
             + cap(v("10:6", frm="And he turned,"), "right: 12px; bottom: 14px", size=11, maxw=260) + vref("EX 10:6", "left: 12px; bottom: 12px"))
    r3 = talk(C.COURTIER, h[2], COURT, [("cap", v("10:7", to="said unto him,")), ("say", v("10:7", frm="How long"))], ref="EX 10:7", size=14)
    return page("Exodus 10:5–7 — Knowest Thou Not Yet That Egypt Is Destroyed?", t, r1 + r2 + r3, START + 7)


@P("EXO-C03-P09-WhoShallGo", "49 · Who Are They That Shall Go?")
def p09():
    t, h = rows(220, 250, None)
    r1 = talk(A.PHARAOH, h[0], RED, [("cap", v("10:8", to="said unto them,")), ("say", v("10:8", frm="Go, serve"))], ref="EX 10:8", size=14)
    r2 = talk(A.MOSES_STERN, h[1], GOLDEN, [("cap", v("10:9", to="And Moses said,")), ("say", v("10:9", frm="We will go"))], ref="EX 10:9", size=14)
    r3 = cols(talk(A.PHARAOH, h[2], RED, [("cap", v("10:10", to="unto them,")), ("say", v("10:10", frm="So be") + " " + v("10:11", to="ye desire."))], w=W2, ref="EX 10:10–11", size=12),
              new(COURT, W2, h[2], defs("x39c", *ALL) + C.driven_out("x39c", W2, h[2], 493), cap(v("10:11", frm="And they were driven"), "left: 8px; top: 8px", size=11, maxw=300) + vref("EX 10:11", "right: 8px; bottom: 8px")))
    return page("Exodus 10:8–11 — Who Are They That Shall Go?", t, r1 + r2 + r3, START + 8)


@P("EXO-C03-P10-Locusts", "50 · The East Wind Brought the Locusts")
def p10():
    t, h = rows(190, 430, None)
    r1 = night(W1, h[0], cap(v("10:12", to="unto Moses,"), "left: 12px; top: 12px", size=10.5) + god(v("10:12", frm="Stretch out"), "left: 12px; top: 46px", size=15, maxw=660) + vref("EX 10:12", "right: 12px; bottom: 12px"))
    r2 = use(L[1], over=cap(v("10:13"), "left: 12px; top: 12px", size=11, maxw=440) + cap(v("10:14"), "right: 12px; bottom: 14px", size=11, maxw=330)
             + sfx("ザザザザ", "ZAZAZAZA", "right: 30px; top: 40px", size=44, fill="#C8B870", stroke="#0D0D0F", rot=-6) + vref("EX 10:13–14", "left: 12px; bottom: 12px"))
    r3 = new("#4A3A1A", W1, h[2], C.locust_land(W1, h[2], 503), cap(v("10:15"), "left: 12px; top: 12px", size=11.5, maxw=560) + vref("EX 10:15", "right: 12px; bottom: 12px"))
    return page("Exodus 10:12–15 — The East Wind Brought the Locusts", t, r1 + r2 + r3, START + 9)


@P("EXO-C03-P11-WestWind", "51 · An Exceeding Strong West Wind")
def p11():
    t, h = rows(290, 220, None)
    r1 = cols(use(L[3], over=cap(v("10:16", to="and he said,"), "right: 8px; top: 8px", size=10, maxw=200) + balloon(v("10:16", frm="I have sinned"), "left: 10px; top: 80px", 190, size=12, pad="20px 16px") + vref("EX 10:16", "left: 8px; bottom: 8px")),
              talk(A.PHARAOH_FEAR, h[0], RED, [("say", v("10:17"))], w=W2, ref="EX 10:17", size=13))
    r2 = new(SKY, W1, h[1], C.west_wind(W1, h[1], 512), cap(v("10:18"), "left: 12px; top: 12px", size=11) + cap(v("10:19"), "left: 12px; bottom: 14px", size=11, maxw=330) + vref("EX 10:18–19", "right: 12px; bottom: 12px"))
    r3 = cols(talk(A.PHARAOH, h[2], RED, [("cap", v("10:20"))], w=W2, ref="EX 10:20"),
              night(W2, h[2], cap(v("10:21", to="unto Moses,"), "left: 8px; top: 8px", size=10.5) + god(v("10:21", frm="Stretch out"), "left: 8px; top: 44px", size=16, maxw=320) + vref("EX 10:21", "right: 8px; bottom: 8px")))
    return page("Exodus 10:16–21 — An Exceeding Strong West Wind", t, r1 + r2 + r3, START + 10)


@P("EXO-C03-P12-Darkness", "52 · Darkness Which May Be Felt")
def p12():
    t, h = rows(330, 210, None)
    r1 = use(K[0], over=cap(v("10:22"), "left: 12px; top: 12px", size=11, maxw=420) + cap(v("10:23", to="for three days:"), "right: 12px; bottom: 14px", size=11, maxw=300)
             + sfx("シーン", "SHIIN", "left: 300px; top: 120px", size=40, fill="#3A3A5A", stroke="#0D0D0F", rot=-4) + vref("EX 10:22–23", "left: 12px; bottom: 12px"))
    r2 = use(K[1], over=cap(v("10:23", frm="but all the children"), "left: 50%; top: 12px; transform: translateX(-50%)", size=11.5) + vref("EX 10:23", "right: 12px; bottom: 12px"))
    r3 = cols(talk(A.PHARAOH, h[2], RED, [("cap", v("10:24", to="and said,")), ("say", v("10:24", frm="Go ye,"))], w=W2, ref="EX 10:24", size=13),
              talk(A.MOSES_STERN, h[2], GOLDEN, [("cap", v("10:25", to="And Moses said,")), ("say", v("10:25", frm="Thou must") + " " + v("10:26"))], w=W2, flip=True, ref="EX 10:25–26", size=11.5))
    return page("Exodus 10:22–26 — Darkness Which May Be Felt", t, r1 + r2 + r3, START + 11)


@P("EXO-C03-P13-SeeMyFace", "53 · See My Face No More")
def p13():
    t, h = rows(380, 230, None)
    r1 = cols(use(K[2], over=cap(v("10:27") + " " + v("10:28", to="unto him,"), "right: 8px; top: 8px", size=10, maxw=220)
                  + balloon(v("10:28", frm="Get thee"), "left: 10px; bottom: 20px", 230, size=12.5, pad="22px 20px") + vref("EX 10:27–28", "left: 8px; top: 8px")),
              use(K[3], over=cap(v("10:29", to="And Moses said,"), "left: 8px; top: 8px", size=10.5) + balloon(v("10:29", frm="Thou hast"), "left: 10px; bottom: 30px", 200, size=13, pad="18px 18px") + vref("EX 10:29", "right: 8px; top: 8px")))
    r2 = night(W1, h[1], cap(v("11:1", to="unto Moses,"), "left: 12px; top: 12px", size=10.5) + god(v("11:1", frm="Yet one") + " " + v("11:2"), "left: 12px; top: 46px", size=15, maxw=660)
               + mk.stamp(11, "right: 14px; bottom: 12px") + vref("EX 11:1–2", "left: 12px; bottom: 12px"))
    r3 = new(SAND, W1, h[2], defs("x313c", *ALL) + T.stage("x313c", W1, h[2], 533, "egypt", [(A.moses, 0.12, 0.38, False, "staff")] + [(("egypt", "#F3EFE6"), 0.3 + i * 0.08, 0.46, True) for i in range(4)]),
             cap(v("11:3"), "right: 12px; top: 12px", size=11, maxw=380) + vref("EX 11:3", "right: 12px; bottom: 12px"))
    return page("Exodus 10:27–11:3 — See My Face No More", t, r1 + r2 + r3, START + 12)


@P("EXO-C03-P14-Midnight", "54 · About Midnight")
def p14():
    t, h = rows(240, 330, None)
    r1 = use(M[0], over=cap(v("11:4", to="And Moses said,"), "left: 12px; top: 12px", size=11) + balloon(v("11:4", frm="Thus saith"), "left: 20px; top: 50px", 380, size=15, pad="20px 28px") + vref("EX 11:4", "right: 12px; bottom: 12px"))
    r2 = use(M[1], over=balloon(v("11:5") + " " + v("11:6"), "right: 16px; top: 20px", 410, size=13.5, pad="38px 40px") + vref("EX 11:5–6", "right: 12px; bottom: 12px"))
    r3 = cols(new(NIGHT, W2, h[2], C.quiet_dog(W2, h[2], 543), balloon(v("11:7"), "left: 8px; top: 8px", 326, size=11.5, pad="22px 26px") + vref("EX 11:7", "right: 8px; bottom: 8px")),
              use(M[3], over=balloon(v("11:8", to="I will go out."), "left: 8px; top: 8px", 326, size=11.5, pad="24px 26px") + cap(v("11:8", frm="And he went out"), "left: 8px; bottom: 8px", size=10.5, maxw=320) + vref("EX 11:8", "right: 8px; top: 8px")))
    return page("Exodus 11:4–8 — About Midnight", t, r1 + r2 + r3, START + 13)


@P("EXO-C03-P15-FirstMonth", "55 · The Beginning of Months")
def p15():
    t, h = rows(220, 250, None)
    r1 = cols(night(W2, h[0], cap(v("11:9", to="unto Moses,"), "left: 8px; top: 8px", size=10.5) + god(v("11:9", frm="Pharaoh will"), "left: 8px; top: 44px", size=14, maxw=320) + mk.stamp(12, "right: 10px; bottom: 30px") + vref("EX 11:9", "right: 8px; bottom: 8px")),
              talk(A.PHARAOH, h[0], RED, [("cap", v("11:10"))], w=W2, flip=True, ref="EX 11:10"))
    r2 = new(CAL, W1, h[1], C.calendar(W1, h[1]), cap(v("12:1"), "left: 12px; bottom: 12px", size=10.5, maxw=220) + god(v("12:2"), "right: 12px; bottom: 12px", size=16, maxw=360)
             + vref("EX 12:1–2", "right: 12px; top: 8px"))
    r3 = new(SKY, W1, h[2], defs("x315c", *ALL) + C.lambs("x315c", W1, h[2], 553), god(v("12:3") + " " + v("12:4"), "left: 12px; top: 12px", size=14, maxw=640) + vref("EX 12:3–4", "right: 12px; bottom: 12px"))
    return page("Exodus 11:9–12:4 — The Beginning of Months", t, r1 + r2 + r3, START + 14)


@P("EXO-C03-P16-Lamb", "56 · Your Lamb Shall Be without Blemish")
def p16():
    t, h = rows(230, 330, None)
    r1 = new(CAL, W1, h[0], C.calendar(W1, h[0], mark=(10, 14), note="THE TENTH DAY · THE FOURTEENTH DAY"), god(v("12:5") + " " + v("12:6"), "right: 12px; bottom: 12px", size=13.5, maxw=440) + vref("EX 12:5–6", "left: 12px; bottom: 12px"))
    r2 = cols(use(LB[2], over=god(v("12:7"), "left: 8px; top: 8px", size=13, maxw=320) + vref("EX 12:7", "right: 8px; bottom: 8px")),
              new(EMBER, W2, h[1], C.roast(W2, h[1], 562), god(v("12:8"), "left: 8px; top: 8px", size=13.5, maxw=320) + vref("EX 12:8", "right: 8px; bottom: 8px")))
    r3 = new(DAWN, W1, h[2], C.dawn_fire(W1, h[2], 563), god(v("12:9") + " " + v("12:10"), "left: 12px; top: 12px", size=15, maxw=470) + vref("EX 12:9–10", "right: 12px; bottom: 12px"))
    return page("Exodus 12:5–10 — Your Lamb Shall Be without Blemish", t, r1 + r2 + r3, START + 15)


@P("EXO-C03-P17-PassOver", "57 · When I See the Blood")
def p17():
    t, h = rows(290, 260, None)
    r1 = use(LB[3], over=god(v("12:11"), "right: 12px; top: 12px", size=14.5, maxw=380) + vref("EX 12:11", "left: 12px; bottom: 12px"))
    r2 = use(BL[0], over=god(v("12:12"), "left: 12px; top: 12px", size=15, maxw=470) + vref("EX 12:12", "right: 12px; bottom: 12px"))
    r3 = use(BL[1], over=god(v("12:13"), "left: 12px; top: 12px", size=16, maxw=480) + sfx("ゴオオ", "GOOO", "right: 30px; top: 40px", size=44, fill="#F3EFE6", stroke="#12113A", rot=-6) + vref("EX 12:13", "right: 12px; bottom: 12px"))
    return page("Exodus 12:11–13 — When I See the Blood", t, r1 + r2 + r3, START + 16)


@P("EXO-C03-P18-Unleavened", "58 · A Feast by an Ordinance for Ever")
def p18():
    t, h = rows(220, 250, 220, None)
    r1 = new(TENT, W1, h[0], defs("x318a", *ALL) + C.household_meal("x318a", W1, h[0], 581), god(v("12:14"), "right: 12px; top: 12px", size=14, maxw=330) + vref("EX 12:14", "left: 12px; bottom: 12px"))
    r2 = new(CAL, W1, h[1], C.calendar(W1, h[1], hi=range(15, 22), mark=(15, 21), note="SEVEN DAYS · UNLEAVENED BREAD"), god(v("12:15"), "left: 12px; bottom: 12px", size=13.5, maxw=640) + vref("EX 12:15", "right: 12px; top: 8px"))
    r3 = new(CAL, W1, h[2], C.calendar(W1, h[2], hi=(15, 21), mark=(15, 21), note="TWO HOLY CONVOCATIONS"), god(v("12:16"), "left: 12px; bottom: 12px", size=13.5, maxw=640) + vref("EX 12:16", "right: 12px; top: 8px"))
    r4 = new(NIGHT, W1, h[3], defs("x318d", *ALL) + C.bundles("x318d", W1, h[3], 584), god(v("12:17"), "left: 12px; top: 12px", size=14, maxw=640) + vref("EX 12:17", "right: 12px; bottom: 12px"))
    return page("Exodus 12:14–17 — A Feast by an Ordinance for Ever", t, r1 + r2 + r3 + r4, START + 17)


@P("EXO-C03-P19-KillThePassover", "59 · Draw Out, and Kill the Passover")
def p19():
    t, h = rows(230, 300, None)
    r1 = new(CAL, W1, h[0], C.calendar(W1, h[0], hi=range(14, 22), mark=(14, 21), note="THE FOURTEENTH AT EVEN TO THE ONE AND TWENTIETH"), god(v("12:18"), "left: 12px; bottom: 12px", size=14, maxw=640) + vref("EX 12:18", "right: 12px; top: 8px"))
    r2 = new(NIGHT, W1, h[1], C.cakes(W1, h[1], 592), god(v("12:19") + " " + v("12:20"), "left: 12px; top: 12px", size=14, maxw=640) + vref("EX 12:19–20", "right: 12px; bottom: 12px"))
    r3 = new(SAND, W1, h[2], defs("x319c", *ALL) + A.elders("x319c", W1, h[2], 593, extra_cast=[(A.moses, 0.92, 0.5, True, "raise")], top=0.58),
             cap(v("12:21", to="said unto them,"), "left: 12px; top: 12px", size=11, maxw=420) + balloon(v("12:21", frm="Draw out,"), "left: 20px; top: 60px", 330, size=14, pad="18px 26px") + vref("EX 12:21", "right: 12px; bottom: 12px"))
    return page("Exodus 12:18–21 — Draw Out, and Kill the Passover", t, r1 + r2 + r3, START + 18)


@P("EXO-C03-P20-Hyssop", "60 · A Bunch of Hyssop")
def p20():
    t, h = rows(370, 290, None)
    r1 = cols(use(LB[1], over=balloon(v("12:22", to="until the morning."), "left: 8px; top: 8px", 326, size=11.5, pad="30px 30px") + vref("EX 12:22", "right: 8px; bottom: 8px")),
              use(BL[2], over=balloon(v("12:23"), "left: 8px; top: 8px", 326, size=11.5, pad="28px 30px") + vref("EX 12:23", "right: 8px; bottom: 8px")))
    r2 = use(BL[1], over=balloon(v("12:24") + " " + v("12:25"), "left: 20px; top: 16px", 420, size=13.5, pad="24px 32px") + vref("EX 12:24–25", "right: 12px; bottom: 12px"))
    r3 = talk(A.MOSES_CALM, h[2], GOLDEN, [("say", v("12:26"))], ref="EX 12:26", size=15)
    return page("Exodus 12:22–26 — A Bunch of Hyssop", t, r1 + r2 + r3, START + 19)


@P("EXO-C03-P21-AtMidnight", "61 · At Midnight")
def p21():
    t, h = rows(290, 200, None)
    r1 = new(TENT, W1, h[0], defs("x321a", *ALL) + C.household_meal("x321a", W1, h[0], 611),
             balloon(v("12:27", to="delivered our houses."), "right: 14px; top: 14px", 320, size=12.5, pad="26px 26px") + vref("EX 12:27", "left: 12px; bottom: 12px"))
    r2 = new(GOLDEN, W1, h[1], defs("x321b", *ALL) + A.elders("x321b", W1, h[1], 612, bow=True), cap(v("12:27", frm="And the people bowed") + " " + v("12:28"), "left: 12px; top: 12px", size=11, maxw=440) + vref("EX 12:27–28", "right: 12px; bottom: 12px"))
    r3 = use(CR[0], over=cap(v("12:29"), "left: 12px; top: 12px", size=11.5, maxw=480) + vref("EX 12:29", "right: 12px; bottom: 12px"))
    return page("Exodus 12:27–29 — At Midnight", t, r1 + r2 + r3, START + 20)


@P("EXO-C03-P22-GreatCry", "62 · A Great Cry in Egypt")
def p22():
    t, h = rows(330, 260, None)
    r1 = use(CR[1], over=cap(v("12:30"), "left: 12px; top: 12px", size=11, maxw=400) + sfx("ウワアア", "UWAAA", "left: 30px; bottom: 40px", size=50, fill="#F3EFE6", stroke="#8A0E16", rot=-6) + vref("EX 12:30", "right: 12px; bottom: 12px"))
    r2 = use(CR[2], over=cap(v("12:31", to="and said,"), "right: 12px; top: 12px", size=10.5) + balloon(v("12:31", frm="Rise up,") + " " + v("12:32"), "right: 20px; top: 50px", 400, size=13.5, pad="22px 30px") + vref("EX 12:31–32", "left: 12px; bottom: 12px"))
    r3 = cols(talk(C.COURTIER, h[2], RED, [("cap", v("12:33", to="for they said,")), ("say", v("12:33", frm="We are all"))], w=W2, ref="EX 12:33", size=14),
              new(NIGHT, W2, h[2], defs("x322c", *ALL) + C.bundles("x322c", W2, h[2], 623), cap(v("12:34"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 12:34", "right: 8px; bottom: 8px")))
    return page("Exodus 12:30–34 — A Great Cry in Egypt", t, r1 + r2 + r3, START + 21)


@P("EXO-C03-P23-Succoth", "63 · From Rameses to Succoth")
def p23():
    t, h = rows(230, 340, None)
    r1 = new(EMBER, W1, h[0], A.jewels(W1, h[0], 631), cap(v("12:35") + " " + v("12:36"), "left: 12px; top: 12px", size=11, maxw=560) + vref("EX 12:35–36", "right: 12px; bottom: 12px"))
    r2 = use(EXO[0], over=cap(v("12:37") + " " + v("12:38"), "left: 12px; top: 12px", size=11, maxw=420) + hud("600,000", "right: 14px; top: 14px", size=26) + vref("EX 12:37–38", "right: 12px; bottom: 12px"))
    r3 = new(NIGHT, W1, h[2], C.cakes(W1, h[2], 633), cap(v("12:39"), "left: 12px; top: 12px", size=11.5, maxw=500) + vref("EX 12:39", "right: 12px; bottom: 12px"))
    return page("Exodus 12:35–39 — From Rameses to Succoth", t, r1 + r2 + r3, START + 22)


@P("EXO-C03-P24-430", "64 · Four Hundred and Thirty Years")
def p24():
    t, h = rows(330, 220, None)
    r1 = cols(use(EXO[1], over=cap(v("12:40"), "left: 8px; bottom: 120px", size=10.5, maxw=200) + cap(v("12:41"), "left: 8px; bottom: 8px", size=10, maxw=320) + vref("EX 12:40–41", "right: 8px; bottom: 8px")),
              new("#0B1A2E", W2, h[0], A.exodus_map(W2, h[0], ["RAAMSES", "SUCCOTH"], cur="SUCCOTH", names=["GOSHEN"]), hud("430", "right: 10px; top: 10px", size=34) + vref("EX 12:41", "left: 8px; bottom: 8px")))
    r2 = new(NIGHT, W1, h[1], X.cosmic(W1, h[1]) + defs("x324b", *ALL) + C.bundles("x324b", W1, h[1], 642), cap(v("12:42"), "left: 12px; top: 12px", size=11.5, maxw=520) + vref("EX 12:42", "right: 12px; bottom: 12px"))
    r3 = night(W1, h[2], cap(v("12:43", to="unto Moses and Aaron,"), "left: 12px; top: 12px", size=11)
               + god(v("12:43", frm="This is") + " " + v("12:44") + " " + v("12:45"), "left: 12px; top: 48px", size=17, maxw=640) + vref("EX 12:43–45", "right: 12px; bottom: 12px"))
    return page("Exodus 12:40–45 — Four Hundred and Thirty Years", t, r1 + r2 + r3, START + 23)


@P("EXO-C03-P25-ByTheirHosts", "65 · By Their Hosts")
def p25():
    t, h = rows(260, 270, None)
    r1 = new(TENT, W1, h[0], defs("x325a", *ALL) + C.household_meal("x325a", W1, h[0], 651), god(v("12:46") + " " + v("12:47"), "right: 12px; top: 12px", size=14, maxw=340) + vref("EX 12:46–47", "left: 12px; bottom: 12px"))
    r2 = night(W1, h[1], god(v("12:48") + " " + v("12:49"), "left: 12px; top: 12px", size=15, maxw=660) + vref("EX 12:48–49", "right: 12px; bottom: 12px"))
    r3 = use(EXO[0], over=cap(v("12:50") + " " + v("12:51"), "left: 12px; top: 12px", size=12, maxw=460)
             + end_mark("NEXT · THE RED SEA", "left: 12px; bottom: 12px") + vref("EX 12:50–51", "right: 12px; bottom: 12px"))
    return page("Exodus 12:46–51 — By Their Hosts", t, r1 + r2 + r3, START + 24)
