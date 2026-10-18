"""Exodus volume, Chapter 5 — Bread from Heaven (Exodus 16–18). Every verse, word for word from ref/asv."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3, exodus4 as E4
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from exo import G, art as A, art2 as B, art3 as C, art4 as D4, art5 as F5
from exo.kit import talk
from exo.ch02 import night
from genesis import art as X, art2 as Y, art3 as Z, art10 as T
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch06 import RUST, GREENLIT, GOLDEN
from genesis.ch07 import RED, BLUE
from mk import defs, face

v, sp = G.v, G.span
MU, MA, RO, AM = [panels("reference/exodus/book-04/" + n + ".dc.html") for n in ["EX4-P01-Murmur", "EX4-P02-Manna", "EX4-P03-Rock", "EX4-P04-Amalek"]]
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
MAP, OMER = "#0B1A2E", "#2A1A10"
START = 82                                   # chapter 4 ends on page 81
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco


@P("EXO-C05-00-Title", "Chapter 5 · Bread from Heaven")
def title():
    a = MA[1]
    return chapter_title(5, "第五話", "Bread from Heaven", "Exodus 16 – 18", f'<g transform="translate(-520 0) scale(2.76)">{a.svg}</g>', a.bg,
                         v("16:15", frm="It is the bread"), "Exodus · Volume Two")


@P("EXO-C05-P01-FleshPots", "82 · Would That We Had Died in the Land of Egypt")
def p01():
    t, h = rows(280, 300, None)
    r1 = new(MAP, W1, h[0], A.exodus_map(W1, h[0], ["SUCCOTH", "THE RED SEA", "MARAH", "ELIM", "SINAI"], cur="ELIM"),
             cap(v("16:1"), "left: 12px; bottom: 12px", size=10.5, maxw=380) + mk.stamp(16, "right: 14px; top: 12px") + vref("EX 16:1", "right: 12px; bottom: 12px"))
    r2 = use(MU[0], over=cap(v("16:2"), "left: 12px; top: 12px", size=11, maxw=420) + sfx("ザワザワ", "ZAWA ZAWA", "right: 30px; top: 30px", size=40, fill="#F3EFE6", stroke="#0D0D0F", rot=-6) + vref("EX 16:2", "right: 12px; bottom: 12px"))
    r3 = cols(new(NIGHT, W2, h[2], F5.flesh_pots(W2, h[2], 823), cap(v("16:3", to="said unto them,"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 16:3", "right: 8px; bottom: 8px")),
              talk(C.HEBREW_FEAR, h[2], RED, [("say", v("16:3", frm="Would that"))], w=W2, flip=True, size=12))
    return page("Exodus 16:1–3 — Would That We Had Died in the Land of Egypt", t, r1 + r2 + r3, START + 0)


@P("EXO-C05-P02-RainBread", "83 · I Will Rain Bread from Heaven")
def p02():
    t, h = rows(260, 210, None)
    r1 = use(MU[2], over=cap(v("16:4", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(v("16:4", frm="Behold,") + " " + v("16:5"), "left: 12px; top: 48px", size=15, maxw=640) + vref("EX 16:4–5", "right: 12px; bottom: 12px"))
    r2 = talk(A.AARON, h[1], GOLDEN, [("cap", v("16:6", to="children of Israel,")), ("say", v("16:6", frm="At even,") + " " + v("16:7"))], ref="EX 16:6–7", size=13)
    r3 = talk(A.MOSES_STERN, h[2], RED, [("cap", v("16:8", to="And Moses said,")), ("say", v("16:8", frm="This shall be,"))], ref="EX 16:8", size=14)
    return page("Exodus 16:4–8 — I Will Rain Bread from Heaven", t, r1 + r2 + r3, START + 1)


@P("EXO-C05-P03-Glory", "84 · The Glory of Jehovah Appeared in the Cloud")
def p03():
    t, h = rows(220, 310, None)
    r1 = talk(A.MOSES, h[0], GOLDEN, [("cap", v("16:9", to="unto Aaron,")), ("say", v("16:9", frm="Say unto all"))], ref="EX 16:9", size=14)
    r2 = new(SAND, W1, h[1], defs("x53b", *ALL) + F5.glory_cloud("x53b", W1, h[1], 832), cap(v("16:10"), "left: 12px; top: 12px", size=11, maxw=380) + vref("EX 16:10", "right: 12px; bottom: 12px"))
    r3 = night(W1, h[2], cap(v("16:11"), "left: 12px; top: 12px", size=11) + god(v("16:12"), "left: 12px; top: 48px", size=18, maxw=560) + vref("EX 16:11–12", "right: 12px; bottom: 12px"))
    return page("Exodus 16:9–12 — The Glory of Jehovah Appeared in the Cloud", t, r1 + r2 + r3, START + 2)


@P("EXO-C05-P04-WhatIsIt", "85 · What Is It?")
def p04():
    t, h = rows(250, 230, None)
    r1 = use(MA[0], over=cap(v("16:13", to="covered the camp:"), "left: 12px; top: 12px", size=11, maxw=420) + sfx("バサバサ", "BASA BASA", "right: 20px; bottom: 30px", size=40, fill="#F3EFE6", stroke="#3A2214", rot=-6) + vref("EX 16:13", "left: 12px; bottom: 12px"))
    r2 = new(DAWN, W1, h[1], F5.dew_camp(W1, h[1], 842), cap(v("16:13", frm="and in the morning"), "left: 12px; top: 12px", size=11) + cap(v("16:14"), "right: 12px; bottom: 14px", size=11, maxw=380) + vref("EX 16:13–14", "left: 12px; bottom: 12px"))
    r3 = cols(use(MA[2], over=cap(v("16:15", to="one to another,"), "left: 8px; top: 8px", size=10.5, maxw=320) + balloon(v("16:15", frm="What is it?", to="What is it?"), "left: 150px; top: 120px", 130, size=15, pad="14px 12px")
                  + cap(v("16:15", frm="for they knew", to="what it was."), "left: 8px; bottom: 8px", size=10.5, maxw=200) + vref("EX 16:15", "right: 8px; bottom: 8px")),
              use(MA[3], over=cap(v("16:15", frm="And Moses said", to="unto them,"), "left: 8px; top: 8px", size=10.5) + balloon(v("16:15", frm="It is the bread"), "left: 10px; top: 60px", 190, size=13, pad="20px 18px")))
    return page("Exodus 16:13–15 — What Is It?", t, r1 + r2 + r3, START + 3)


@P("EXO-C05-P05-Omer", "86 · An Omer a Head")
def p05():
    t, h = rows(200, 280, None)
    r1 = talk(A.MOSES_CALM, h[0], GOLDEN, [("say", v("16:16"))], ref="EX 16:16", size=14)
    r2 = new(SAND, W1, h[1], defs("x55b", *ALL) + F5.gathering("x55b", W1, h[1], 852), cap(v("16:17"), "left: 12px; top: 12px", size=11.5) + vref("EX 16:17", "right: 12px; bottom: 12px"))
    r3 = new(OMER, W1, h[2], F5.omers(W1, h[2], 853), cap(v("16:18"), "left: 12px; top: 12px", size=11.5, maxw=560) + vref("EX 16:18", "right: 12px; bottom: 12px"))
    return page("Exodus 16:16–18 — An Omer a Head", t, r1 + r2 + r3, START + 4)


@P("EXO-C05-P06-Worms", "87 · It Bred Worms")
def p06():
    t, h = rows(240, 270, None)
    r1 = cols(talk(A.MOSES, h[0], GOLDEN, [("cap", v("16:19", to="unto them,")), ("say", v("16:19", frm="Let no man"))], w=W2, ref="EX 16:19", size=13),
              new("#3A3A2A", W2, h[0], F5.worms(W2, h[0], 861), cap(v("16:20"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 16:20", "right: 8px; bottom: 8px")))
    r2 = new(SAND, W1, h[1], defs("x56b", *ALL) + F5.melted(W1, h[1], 862, p="x56b", people=4), cap(v("16:21"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("EX 16:21", "right: 12px; bottom: 12px"))
    r3 = new(OMER, W1, h[2], F5.omers(W1, h[2], 863, n=5, double=True), cap(v("16:22"), "left: 12px; top: 12px", size=11.5, maxw=560) + vref("EX 16:22", "right: 12px; bottom: 12px"))
    return page("Exodus 16:19–22 — It Bred Worms", t, r1 + r2 + r3, START + 5)


@P("EXO-C05-P07-Sabbath", "88 · To-morrow Is a Solemn Rest")
def p07():
    t, h = rows(260, 200, 220, None)
    r1 = talk(A.MOSES_CALM, h[0], GOLDEN, [("cap", v("16:23", to="unto them,")), ("say", v("16:23", frm="This is"))], ref="EX 16:23", size=14)
    r2 = new(TENT, W1, h[1], T.J7.tent_inside(W1, h[1], 0.3) + E4.basket(W1 * 0.5, h[1] * 0.9, 3.4) + E4.manna(60, W1 * 0.44, W1 * 0.56, h[1] * 0.62, h[1] * 0.7, 872), cap(v("16:24"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("EX 16:24", "right: 12px; bottom: 12px"))
    r3 = talk(A.MOSES, h[2], GOLDEN, [("cap", v("16:25", to="And Moses said,")), ("say", v("16:25", frm="Eat that") + " " + v("16:26"))], ref="EX 16:25–26", size=14)
    r4 = new(SAND, W1, h[3], defs("x57d", *ALL) + F5.melted(W1, h[3], 874, p="x57d", people=3), cap(v("16:27"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("EX 16:27", "right: 12px; bottom: 12px"))
    return page("Exodus 16:23–27 — To-morrow Is a Solemn Rest", t, r1 + r2 + r3 + r4, START + 6)


@P("EXO-C05-P08-Manna", "89 · Like Coriander Seed, White")
def p08():
    t, h = rows(270, 170, None)
    r1 = night(W1, h[0], cap(v("16:28", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(v("16:28", frm="How long") + " " + v("16:29"), "left: 12px; top: 48px", size=17, maxw=560) + vref("EX 16:28–29", "right: 12px; bottom: 12px"))
    r2 = new(SKY, W1, h[1], F5.sabbath_camp(W1, h[1], 882), cap(v("16:30"), "left: 12px; top: 12px", size=12) + vref("EX 16:30", "right: 12px; bottom: 12px"))
    r3 = use(MA[1], over=cap(v("16:31"), "left: 12px; top: 12px", size=12, maxw=440) + vref("EX 16:31", "right: 12px; bottom: 12px"))
    return page("Exodus 16:28–31 — Like Coriander Seed, White", t, r1 + r2 + r3, START + 7)


@P("EXO-C05-P09-Pot", "90 · Forty Years")
def p09():
    t, h = rows(250, 250, None)
    r1 = talk(A.MOSES_CALM, h[0], GOLDEN, [("cap", v("16:32", to="And Moses said,")), ("say", v("16:32", frm="This is"))], ref="EX 16:32", size=13.5)
    r2 = cols(new(NIGHT, W2, h[1], F5.pot(W2, h[1], 902), cap(v("16:33", to="unto Aaron,"), "left: 8px; top: 8px", size=10.5) + balloon(v("16:33", frm="Take a pot,"), "left: 8px; top: 44px", 326, size=11.5, pad="16px 22px") + vref("EX 16:33", "right: 8px; bottom: 8px")),
              new(NIGHT, W2, h[1], F5.pot(W2, h[1], 903), cap(v("16:34"), "left: 8px; top: 8px", size=11, maxw=320) + vref("EX 16:34", "right: 8px; bottom: 8px")))
    r3 = cols(new(MAP, W2, h[2], A.exodus_map(W2, h[2], ["ELIM", "SINAI", "KADESH", "CANAAN"], cur="CANAAN"), cap(v("16:35"), "left: 8px; bottom: 8px", size=10, maxw=320) + hud("40", "right: 10px; top: 10px", size=30) + vref("EX 16:35", "left: 8px; top: 8px")),
              new(MAP, W2, h[2], F5.ephah(W2, h[2], 905), cap(v("16:36"), "left: 8px; bottom: 8px", size=11, maxw=320) + vref("EX 16:36", "right: 8px; top: 8px")))
    return page("Exodus 16:32–36 — Forty Years", t, r1 + r2 + r3, START + 8)


@P("EXO-C05-P10-Rephidim", "91 · Is Jehovah among Us, or Not?")
def p10():
    t, h = rows(250, 230, None)
    r1 = new(HOT, W1, h[0], defs("x510a", *ALL) + F5.rephidim("x510a", W1, h[0], 911), cap(v("17:1"), "left: 12px; top: 12px", size=11, maxw=460) + mk.stamp(17, "right: 14px; bottom: 12px") + vref("EX 17:1", "left: 12px; bottom: 12px"))
    r2 = new(HOT, W1, h[1], defs("x510b", *ALL) + F5.rephidim("x510b", W1, h[1], 912, strive=True),
             cap(v("17:2", to="and said,"), "left: 12px; top: 12px", size=10.5) + balloon(v("17:2", frm="Give us", to="drink."), "left: 12px; top: 44px", 200, size=12.5, pad="14px 18px")
             + cap(v("17:2", frm="And Moses said", to="unto them,"), "right: 12px; top: 12px", size=10.5) + balloon(v("17:2", frm="Why strive"), "right: 12px; top: 44px", 240, size=12.5, pad="14px 18px") + vref("EX 17:2", "right: 12px; bottom: 12px"))
    r3 = cols(use(RO[0], over=cap(v("17:3", to="and said,"), "left: 8px; top: 8px", size=10, maxw=320) + balloon(v("17:3", frm="Wherefore"), "left: 10px; top: 80px", 260, size=12, pad="22px 22px") + vref("EX 17:3", "right: 8px; bottom: 8px")),
              use(RO[1], over=cap(v("17:4", to="saying,"), "left: 8px; top: 8px", size=10.5) + balloon(v("17:4", frm="What shall"), "right: 8px; top: 80px", 170, size=12, pad="22px 16px") + vref("EX 17:4", "left: 8px; bottom: 8px")))
    return page("Exodus 17:1–4 — Is Jehovah among Us, or Not?", t, r1 + r2 + r3, START + 9)


@P("EXO-C05-P11-Rock", "92 · Thou Shalt Smite the Rock")
def p11():
    t, h = rows(250, 370, None)
    r1 = use(RO[2], over=cap(v("17:5", to="unto Moses,"), "left: 12px; top: 12px", size=10.5) + god(v("17:5", frm="Pass on") + " " + v("17:6", to="may drink."), "left: 12px; top: 46px", size=14, maxw=330) + vref("EX 17:5–6", "right: 12px; bottom: 12px"))
    r2 = use(RO[3], over=cap(v("17:6", frm="And Moses did so"), "left: 12px; top: 12px", size=11.5) + sfx("ドバッ", "DOBA!", "right: 30px; top: 30px", size=54, fill="#8FD0E2", stroke="#0D0D0F", rot=-6) + vref("EX 17:6", "right: 12px; bottom: 12px"))
    r3 = new(HOT, W1, h[2], defs("x511c", *ALL) + F5.rephidim("x511c", W1, h[2], 923, strive=True), cap(v("17:7", to="saying,"), "left: 12px; top: 12px", size=11, maxw=430)
             + balloon(v("17:7", frm="Is Jehovah"), "right: 14px; top: 14px", 220, size=14, pad="14px 18px") + vref("EX 17:7", "right: 12px; bottom: 12px"))
    return page("Exodus 17:5–7 — Thou Shalt Smite the Rock", t, r1 + r2 + r3, START + 10)


@P("EXO-C05-P12-Amalek", "93 · Then Came Amalek")
def p12():
    t, h = rows(240, 240, None)
    r1 = use(AM[0], over=cap(v("17:8"), "left: 12px; top: 12px", size=12) + sfx("ウオオオ", "UOOO", "left: 20px; top: 70px", size=44, fill="#D7261E", rot=-6) + vref("EX 17:8", "right: 12px; bottom: 12px"))
    r2 = cols(talk(A.MOSES_STERN, h[1], RED, [("cap", v("17:9", to="unto Joshua,")), ("say", v("17:9", frm="Choose us"))], w=W2, ref="EX 17:9", size=12),
              talk(F5.JOSHUA, h[1], RED, [("cap", v("17:10", to="fought with Amalek:"))], w=W2, flip=True, ref="EX 17:10"))
    r3 = new(DUSK, W1, h[2], defs("x512c", *ALL) + F5.hill_top("x512c", W1, h[2], 933), cap(v("17:10", frm="and Moses, Aaron,"), "left: 12px; top: 12px", size=11, maxw=300)
             + cap(v("17:11"), "right: 12px; top: 12px", size=11, maxw=280) + vref("EX 17:10–11", "right: 12px; bottom: 12px"))
    return page("Exodus 17:8–11 — Then Came Amalek", t, r1 + r2 + r3, START + 11)


@P("EXO-C05-P13-Hands", "94 · His Hands Were Steady")
def p13():
    t, h = rows(380, 250, None)
    r1 = use(AM[1], over=cap(v("17:12", to="the other side;"), "left: 12px; top: 12px", size=11, maxw=440) + vref("EX 17:12", "right: 12px; bottom: 12px"))
    r2 = cols(use(AM[3], over=cap(v("17:12", frm="and his hands"), "left: 8px; top: 8px", size=11, maxw=320) + vref("EX 17:12", "right: 8px; bottom: 8px")),
              use(AM[2], over=cap(v("17:13"), "right: 8px; bottom: 8px", size=11, maxw=200) + vref("EX 17:13", "left: 8px; top: 8px")))
    r3 = new("#2A1A10", W1, h[2], F5.book(W1, h[2], 943), cap(v("17:14", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(v("17:14", frm="Write this"), "left: 12px; top: 48px", size=15, maxw=300) + vref("EX 17:14", "right: 12px; bottom: 12px"))
    return page("Exodus 17:12–14 — His Hands Were Steady", t, r1 + r2 + r3, START + 12)


@P("EXO-C05-P14-Jethro", "95 · Jehovah-nissi")
def p14():
    t, h = rows(300, 220, None)
    r1 = new(DUSK, W1, h[0], defs("x514a", *ALL) + F5.nissi("x514a", W1, h[0], 951), cap(v("17:15") + " " + v("17:16", to="and he said,"), "left: 12px; top: 12px", size=11, maxw=420)
             + balloon(v("17:16", frm="Jehovah hath"), "right: 14px; top: 60px", 260, size=13, pad="20px 22px") + vref("EX 17:15–16", "left: 12px; bottom: 12px"))
    r2 = talk(A.JETHRO, h[1], GOLDEN, [("cap", v("18:1"))], ref="EX 18:1", extra=mk.stamp(18, "right: 14px; bottom: 12px"))
    r3 = cols(talk(A.ZIPPORAH, h[2], GOLDEN, [("cap", v("18:2") + " " + v("18:3", to="for he said,")), ("say", v("18:3", frm="I have been"))], w=W2, ref="EX 18:2–3", size=11.5),
              new(GREENLIT, W2, h[2], fc(F5.ELIEZER, h[2], flip=True),
                  cap(v("18:4", to="for he said,"), "left: 8px; top: 8px", size=10, maxw=180) + balloon(v("18:4", frm="The God"), "left: 8px; top: 70px", 180, size=11.5, pad="20px 16px") + vref("EX 18:4", "right: 8px; bottom: 8px")))
    return page("Exodus 17:15–18:4 — Jehovah-nissi", t, r1 + r2 + r3, START + 13)


@P("EXO-C05-P15-Rejoiced", "96 · Now I Know That Jehovah Is Greater than All Gods")
def p15():
    t, h = rows(250, 230, 220, None)
    r1 = new(SAND, W1, h[0], defs("x515a", *ALL) + F5.family_coming("x515a", W1, h[0], 961), cap(v("18:5"), "left: 12px; top: 12px", size=10.5, maxw=380)
             + cap(v("18:6", to="unto Moses,"), "right: 12px; top: 12px", size=10.5) + balloon(v("18:6", frm="I, thy"), "right: 12px; top: 46px", 240, size=12, pad="16px 20px") + vref("EX 18:5–6", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], defs("x515b", *ALL) + F5.obeisance("x515b", W1, h[1], 962), cap(v("18:7"), "right: 12px; top: 12px", size=11, maxw=330) + vref("EX 18:7", "left: 12px; bottom: 12px"))
    r3 = talk(A.MOSES_CALM, h[2], GOLDEN, [("cap", v("18:8")), ("cap", v("18:9"))], ref="EX 18:8–9")
    r4 = talk(F5.JETHRO_JOY, h[3], GOLDEN, [("cap", v("18:10", to="And Jethro said,")), ("say", v("18:10", frm="Blessed be") + " " + v("18:11"))], ref="EX 18:10–11", size=13)
    return page("Exodus 18:5–11 — Now I Know That Jehovah Is Greater than All Gods", t, r1 + r2 + r3 + r4, START + 14)


@P("EXO-C05-P16-Judge", "97 · Why Sittest Thou Thyself Alone?")
def p16():
    t, h = rows(250, 260, None)
    r1 = new(DUSK, W1, h[0], defs("x516a", *ALL) + F5.feast("x516a", W1, h[0], 971), cap(v("18:12"), "left: 12px; top: 12px", size=11, maxw=440) + vref("EX 18:12", "right: 12px; bottom: 12px"))
    r2 = new(DUSK, W1, h[1], defs("x516b", *ALL) + F5.judging("x516b", W1, h[1], 972), cap(v("18:13"), "left: 12px; top: 12px", size=11, maxw=400) + vref("EX 18:13", "right: 12px; bottom: 12px"))
    r3 = cols(talk(A.JETHRO, h[2], GOLDEN, [("cap", v("18:14", to="he said,")), ("say", v("18:14", frm="What is this"))], w=W2, ref="EX 18:14", size=11.5),
              talk(F5.MOSES_TIRED, h[2], GOLDEN, [("cap", v("18:15", to="father-in-law,")), ("say", v("18:15", frm="Because") + " " + v("18:16"))], w=W2, flip=True, ref="EX 18:15–16", size=11.5))
    return page("Exodus 18:12–16 — Why Sittest Thou Thyself Alone?", t, r1 + r2 + r3, START + 15)


@P("EXO-C05-P17-Counsel", "98 · Hearken Now unto My Voice")
def p17():
    t, h = rows(None)
    r1 = talk(A.JETHRO, h[0], GOLDEN, [("cap", v("18:17", to="said unto him,")), ("say", v("18:17", frm="The thing") + " " + v("18:18") + " " + v("18:19") + " " + v("18:20")),
                                       ("say", v("18:21") + " " + v("18:22") + " " + v("18:23"))], ref="EX 18:17–23", size=13)
    return page("Exodus 18:17–23 — Hearken Now unto My Voice", t, r1, START + 16)


@P("EXO-C05-P18-Rulers", "99 · Rulers of Thousands")
def p18():
    t, h = rows(400, None)
    r1 = new(MAP, W1, h[0], F5.rulers(W1, h[0], 991), cap(v("18:24") + " " + v("18:25"), "right: 12px; bottom: 12px", size=11, maxw=250) + vref("EX 18:24–25", "right: 12px; top: 12px"))
    r2 = cols(new(DUSK, W2, h[1], defs("x518b", *ALL) + F5.judging("x518b", W2, h[1], 992), cap(v("18:26"), "left: 8px; top: 8px", size=11, maxw=320) + vref("EX 18:26", "right: 8px; bottom: 8px")),
              new(SAND, W2, h[1], defs("x518c", *ALL) + T.stage("x518c", W2, h[1], 993, "sand", [(A.jethro, 0.7, 0.62, False, "staff"), (A.moses, 0.22, 0.56, True, "raise")]), cap(v("18:27"), "left: 8px; top: 8px", size=11, maxw=320)
                  + end_mark("NEXT · SINAI", "left: 8px; bottom: 8px") + vref("EX 18:27", "right: 8px; bottom: 8px")))
    return page("Exodus 18:24–27 — Rulers of Thousands", t, r1 + r2, START + 17)
