"""Exodus volume, Chapter 4 — The Red Sea (Exodus 13–15). Every verse, word for word from ref/eng-asv.
The Song of Moses (15:1–18) and Miriam's answer are set in song boxes (kit.song), one or two lines to a panel."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus as E, exodus2 as E2, exodus3 as E3
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from exo import G, art as A, art2 as B, art3 as C, art4 as D4
from exo.kit import talk, song
from exo.ch02 import night
from genesis import art as X, art2 as Y, art3 as Z, art10 as T
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch06 import RUST, GREENLIT, GOLDEN
from genesis.ch07 import RED, BLUE
from genesis.ch12 import NILE, COURT
from mk import defs, face

v, sp = G.v, G.span
EXO, PU, SS, DG, SO = [panels("reference/exodus/book-03/" + n + ".dc.html") for n in ["EX3-P04-Exodus", "EX3-P05-Pursuit", "EX3-P06-StandStill", "EX3-P07-DryGround", "EX3-P08-Song"]]
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
SEA = "linear-gradient(180deg, #0B2E4A 0%, #1F6F9A 100%)"
MAP = "#0B1A2E"
MIRIAM_OLD = A.tok("MIRIAM_OLD")
START = 66                                   # chapter 3 ends on page 65
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco


@P("EXO-C04-00-Title", "Chapter 4 · The Red Sea")
def title():
    a = DG[0]
    return chapter_title(4, "第四話", "The Red Sea", "Exodus 13 – 15", f'<g transform="translate(-160 0) scale(1.48)">{a.svg}</g>', a.bg,
                         v("14:22", to="on their left."), "Exodus · Volume Two")


@P("EXO-C04-P01-Remember", "66 · Remember This Day")
def p01():
    t, h = rows(200, 230, 250, None)
    r1 = new(SKY, W1, h[0], defs("x41a", *ALL) + C.lambs("x41a", W1, h[0], 411), cap(v("13:1"), "left: 12px; top: 12px", size=10.5) + god(v("13:2"), "left: 12px; top: 46px", size=15, maxw=560)
             + mk.stamp(13, "right: 14px; bottom: 12px") + vref("EX 13:1–2", "left: 12px; bottom: 12px"))
    r2 = talk(A.MOSES_CALM, h[1], GOLDEN, [("cap", v("13:3", to="unto the people,")), ("say", v("13:3", frm="Remember") + " " + v("13:4"))], ref="EX 13:3–4", size=13.5)
    r3 = new(MAP, W1, h[2], A.peoples_map(W1, h[2], 413), balloon(v("13:5"), "right: 12px; top: 12px", 300, size=12, pad="30px 30px") + vref("EX 13:5", "left: 12px; top: 12px"))
    r4 = new(NIGHT, W1, h[3], C.cakes(W1, h[3], 414), balloon(v("13:6") + " " + v("13:7"), "left: 20px; top: 12px", 460, size=13, pad="20px 30px") + vref("EX 13:6–7", "right: 12px; bottom: 12px"))
    return page("Exodus 13:1–7 — Remember This Day", t, r1 + r2 + r3 + r4, START + 0)


@P("EXO-C04-P02-Sign", "67 · A Sign unto Thee upon Thy Hand")
def p02():
    t, h = rows(250, 230, 220, None)
    r1 = new(TENT, W1, h[0], defs("x42a", *ALL) + C.father_son("x42a", W1, h[0], 421), balloon(v("13:8"), "right: 14px; top: 14px", 330, size=13, pad="22px 26px") + vref("EX 13:8", "left: 12px; bottom: 12px"))
    r2 = new(GOLDEN, W1, h[1], D4.hand_sign(W1, h[1], 422), balloon(v("13:9") + " " + v("13:10"), "left: 14px; top: 14px", 300, size=12.5, pad="30px 28px") + vref("EX 13:9–10", "right: 12px; bottom: 12px"))
    r3 = new(SKY, W1, h[2], defs("x42c", *ALL) + C.lambs("x42c", W1, h[2], 423), balloon(v("13:11") + " " + v("13:12"), "left: 14px; top: 10px", 470, size=12.5, pad="22px 32px") + vref("EX 13:11–12", "right: 12px; bottom: 12px"))
    r4 = new(SKY, W1, h[3], D4.ass_lamb(W1, h[3], 424), balloon(v("13:13"), "right: 14px; top: 10px", 330, size=12.5, pad="26px 28px") + vref("EX 13:13", "left: 12px; bottom: 12px"))
    return page("Exodus 13:8–13 — A Sign unto Thee upon Thy Hand", t, r1 + r2 + r3 + r4, START + 1)


@P("EXO-C04-P03-WhatIsThis", "68 · What Is This?")
def p03():
    t, h = rows(330, 170, None)
    r1 = new(TENT, W1, h[0], defs("x43a", *ALL) + C.household_meal("x43a", W1, h[0], 431),
             balloon(v("13:14", to="What is this?"), "left: 12px; top: 12px", 250, size=12.5, pad="18px 20px")
             + balloon(v("13:14", frm="that thou shalt") + " " + v("13:15"), "right: 12px; top: 40px", 410, size=11.5, pad="26px 36px") + vref("EX 13:14–15", "left: 12px; bottom: 12px"))
    r2 = new(GOLDEN, W1, h[1], D4.hand_sign(W1, h[1], 432, cx=0.8), balloon(v("13:16"), "left: 14px; top: 12px", 360, size=12.5, pad="20px 28px") + vref("EX 13:16", "right: 12px; bottom: 12px"))
    r3 = new(MAP, W1, h[2], D4.sea_map(W1, h[2], ["SUCCOTH", "ETHAM"]), cap(v("13:17", to="for God said,"), "left: 12px; bottom: 12px", size=10.5, maxw=380)
             + god(v("13:17", frm="Lest peradventure"), "right: 12px; bottom: 12px", size=14, maxw=230) + vref("EX 13:17", "right: 12px; top: 40px"))
    return page("Exodus 13:14–17 — What Is This?", t, r1 + r2 + r3, START + 2)


@P("EXO-C04-P04-Pillar", "69 · A Pillar of Cloud, a Pillar of Fire")
def p04():
    t, h = rows(210, 300, None)
    r1 = new(SAND, W1, h[0], defs("x44a", *ALL) + D4.armed("x44a", W1, h[0], 441), cap(v("13:18"), "left: 12px; top: 12px", size=11, maxw=460) + vref("EX 13:18", "right: 12px; bottom: 12px"))
    r2 = cols(use(EXO[2], over=cap(v("13:19"), "left: 8px; top: 8px", size=10, maxw=320) + vref("EX 13:19", "right: 8px; bottom: 8px")),
              new(MAP, W2, h[1], D4.sea_map(W2, h[1], ["SUCCOTH", "ETHAM"], cur="ETHAM"), cap(v("13:20"), "left: 8px; bottom: 8px", size=10.5, maxw=320) + vref("EX 13:20", "right: 8px; top: 40px")))
    r3 = cols(use(EXO[3], over=cap(v("13:21", to="to lead them the way,"), "left: 8px; top: 8px", size=11, maxw=320) + vref("EX 13:21", "right: 8px; bottom: 8px")),
              use(EXO[4], over=cap(v("13:21", frm="and by night") + " " + v("13:22"), "left: 8px; top: 8px", size=11, maxw=320) + vref("EX 13:21–22", "right: 8px; bottom: 8px")))
    return page("Exodus 13:18–22 — A Pillar of Cloud, a Pillar of Fire", t, r1 + r2 + r3, START + 3)


@P("EXO-C04-P05-Entangled", "70 · They Are Entangled in the Land")
def p05():
    t, h = rows(300, 200, None)
    r1 = new(MAP, W1, h[0], D4.sea_map(W1, h[0], ["SUCCOTH", "ETHAM", "MIGDOL", "PI-HAHIROTH"], cur="PI-HAHIROTH"),
             cap(v("14:1"), "left: 12px; bottom: 12px", size=10.5) + god(v("14:2") + " " + v("14:3"), "right: 12px; bottom: 12px", size=13, maxw=250) + vref("EX 14:1–3", "right: 12px; top: 40px"))
    r2 = new(NIGHT, W1, h[1], A.wonders(W1, h[1], 452), god(v("14:4", to="I am Jehovah."), "left: 12px; top: 12px", size=15, maxw=470)
             + cap(v("14:4", frm="And they did so."), "right: 12px; bottom: 14px", size=11) + vref("EX 14:4", "left: 12px; bottom: 12px"))
    r3 = talk(A.PHARAOH, h[2], RED, [("cap", v("14:5", to="and they said,")), ("say", v("14:5", frm="What is this"))], ref="EX 14:5", size=15, extra=mk.stamp(14, "right: 14px; bottom: 12px"))
    return page("Exodus 14:1–5 — They Are Entangled in the Land", t, r1 + r2 + r3, START + 4)


@P("EXO-C04-P06-Pursued", "71 · Six Hundred Chosen Chariots")
def p06():
    t, h = rows(380, 220, None)
    r1 = use(PU[1], over=cap(v("14:6") + " " + v("14:7"), "left: 12px; top: 12px", size=11, maxw=420) + hud("600", "right: 14px; bottom: 14px", size=30)
             + sfx("ドドドド", "DODODODO", "right: 20px; top: 20px", size=44, fill="#D7261E", rot=-6) + vref("EX 14:6–7", "left: 12px; bottom: 12px"))
    r2 = new(MAP, W1, h[1], D4.sea_map(W1, h[1], ["SUCCOTH", "ETHAM", "MIGDOL", "PI-HAHIROTH"], cur="PI-HAHIROTH"), cap(v("14:8") + " " + v("14:9"), "left: 12px; bottom: 12px", size=10.5, maxw=380) + vref("EX 14:8–9", "right: 12px; top: 40px"))
    r3 = cols(use(PU[3], over=cap(v("14:10", to="marching after them;"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 14:10", "right: 8px; bottom: 8px")),
              use(PU[2], over=cap(v("14:10", frm="and they were sore afraid:"), "left: 8px; bottom: 8px", size=11, maxw=220)))
    return page("Exodus 14:6–10 — Six Hundred Chosen Chariots", t, r1 + r2 + r3, START + 5)


@P("EXO-C04-P07-StandStill", "72 · Fear Ye Not, Stand Still")
def p07():
    t, h = rows(320, 300, None)
    r1 = talk(C.HEBREW_FEAR, h[0], COLD, [("cap", v("14:11", to="unto Moses,")), ("say", v("14:11", frm="Because") + " " + v("14:12"))], ref="EX 14:11–12", size=14.5)
    r2 = talk(A.MOSES_CALM, h[1], GOLDEN, [("cap", v("14:13", to="unto the people,")), ("say", v("14:13", frm="Fear ye not,") + " " + v("14:14"))], ref="EX 14:13–14", size=15)
    r3 = use(SS[1], over=cap(v("14:15", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(v("14:15", frm="Wherefore") + " " + v("14:16"), "left: 12px; top: 48px", size=17, maxw=520) + vref("EX 14:15–16", "right: 12px; bottom: 12px"))
    return page("Exodus 14:11–16 — Fear Ye Not, Stand Still", t, r1 + r2 + r3, START + 6)


@P("EXO-C04-P08-GoForward", "73 · The Cloud and the Darkness")
def p08():
    t, h = rows(300, None)
    r1 = new(NIGHT, W1, h[0], X.cosmic(W1, h[0]) + Y.ground(W1, h[0], h[0] * 0.86, "#1A1430", dy=0) + "".join(E3.chariot(W1 * x, h[0] * 0.86, 0.5) for x in (0.5, 0.68, 0.86)),
             god(v("14:17") + " " + v("14:18"), "left: 12px; top: 12px", size=15, maxw=400) + vref("EX 14:17–18", "right: 12px; bottom: 12px"))
    r2 = new(NIGHT, W1, h[1], D4.cloud_between(None, W1, h[1], 483), cap(v("14:19"), "left: 12px; top: 12px", size=11.5, maxw=280) + cap(v("14:20"), "right: 12px; top: 12px", size=11.5, maxw=280) + vref("EX 14:19–20", "right: 12px; bottom: 12px"))
    return page("Exodus 14:17–20 — The Cloud and the Darkness", t, r1 + r2, START + 7)


@P("EXO-C04-P09-DryGround", "74 · The Waters Were a Wall unto Them")
def p09():
    t, h = rows(250, None)
    r1 = use(SS[2], over=cap(v("14:21"), "left: 12px; top: 12px", size=11.5, maxw=420) + sfx("ゴゴゴゴ", "GOGOGOGO", "right: 30px; bottom: 30px", size=44, fill="#F3EFE6", stroke="#0B2E4A", rot=-6) + vref("EX 14:21", "left: 12px; bottom: 12px"))
    r2 = use(DG[0], over=cap(v("14:22"), "left: 50%; top: 14px; transform: translateX(-50%)", size=12.5, maxw=440) + sfx("ザザーッ", "ZAZAA", "left: 24px; top: 200px", size=48, fill="#E8F6FA", stroke="#0B2E4A", rot=-8) + vref("EX 14:22", "right: 12px; bottom: 12px"))
    return page("Exodus 14:21–22 — The Waters Were a Wall unto Them", t, r1 + r2, START + 8)


@P("EXO-C04-P10-Wheels", "75 · He Took Off Their Chariot Wheels")
def p10():
    t, h = rows(300, 340, None)
    r1 = cols(use(DG[1], over=cap(v("14:23"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 14:23", "right: 8px; bottom: 8px")),
              new(SEA, W2, h[0], D4.morning_watch(W2, h[0], 4101), cap(v("14:24"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 14:24", "right: 8px; bottom: 8px")))
    r2 = new(SEA, W1, h[1], D4.wheels_off(None, W1, h[1], 4102), cap(v("14:25", to="the Egyptians said,"), "left: 12px; top: 12px", size=11, maxw=300)
             + balloon(v("14:25", frm="Let us flee"), "right: 14px; top: 14px", 300, size=14, pad="22px 26px") + sfx("ガタン", "GATAN", "left: 40px; bottom: 30px", size=40, fill="#E8B830", rot=-8) + vref("EX 14:25", "right: 12px; bottom: 12px"))
    r3 = new(SEA, W1, h[2], E3.crash(W1, h[2], 4103), cap(v("14:26", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(v("14:26", frm="Stretch out"), "left: 12px; top: 48px", size=17, maxw=420) + vref("EX 14:26", "right: 12px; bottom: 12px"))
    return page("Exodus 14:23–26 — He Took Off Their Chariot Wheels", t, r1 + r2 + r3, START + 9)


@P("EXO-C04-P11-Saved", "76 · Thus Jehovah Saved Israel That Day")
def p11():
    t, h = rows(380, 250, None)
    r1 = use(SO[0], over=cap(v("14:27"), "left: 12px; top: 12px", size=11, maxw=440) + cap(v("14:28"), "right: 12px; bottom: 14px", size=11, maxw=330)
             + sfx("ザッバーン", "ZABBAAN", "left: 20px; top: 150px", size=46, fill="#E8F6FA", stroke="#0B2E4A", rot=-8) + vref("EX 14:27–28", "left: 12px; bottom: 12px"))
    r2 = new(SEA, W1, h[1], defs("x411b", *ALL) + D4.dry_walk("x411b", W1, h[1], 4112), cap(v("14:29"), "left: 12px; top: 12px", size=11, maxw=300) + vref("EX 14:29", "right: 12px; bottom: 12px"))
    r3 = use(SO[1], over=cap(v("14:30"), "left: 12px; top: 12px", size=11, maxw=400) + cap(v("14:31"), "right: 12px; bottom: 14px", size=11, maxw=330) + vref("EX 14:30–31", "left: 12px; bottom: 12px"))
    return page("Exodus 14:27–31 — Thus Jehovah Saved Israel That Day", t, r1 + r2 + r3, START + 10)


@P("EXO-C04-P12-Song1", "77 · The Horse and His Rider")
def p12():
    t, h = rows(350, 250, None)
    r1 = new(SEA, W1, h[0], E3.crash(W1, h[0], 4121) + E3.chariot(W1 * 0.3, h[0] * 0.7, 0.7) + E3.horse(W1 * 0.56, h[0] * 0.8, 0.6, flip=True),
             cap(v("15:1", to="and spake, saying,"), "left: 12px; top: 12px", size=11, maxw=440) + song(v("15:1", frm="I will sing"), "left: 12px; top: 84px", size=21, maxw=430)
             + mk.stamp(15, "right: 14px; top: 12px") + vref("EX 15:1", "right: 12px; bottom: 12px"))
    r2 = new(DAWN, W1, h[1], D4.inheritance(W1, h[1], 4122), song(v("15:2") + " " + v("15:3"), "left: 12px; top: 12px", size=17, maxw=470) + vref("EX 15:2–3", "right: 12px; bottom: 12px"))
    r3 = new(SEA, W1, h[2], D4.sunk(W1, h[2], 4123), song(v("15:4") + " " + v("15:5"), "right: 12px; top: 12px", size=17, maxw=420) + vref("EX 15:4–5", "left: 12px; bottom: 12px"))
    return page("Exodus 15:1–5 — The Horse and His Rider", t, r1 + r2 + r3, START + 11)


@P("EXO-C04-P13-Song2", "78 · Who Is Like unto Thee, O Jehovah?")
def p13():
    t, h = rows(220, 230, 210, None)
    r1 = new(STORM, W1, h[0], A.wonders(W1, h[0], 4131), song(v("15:6") + " " + v("15:7"), "left: 12px; top: 12px", size=15.5, maxw=500) + vref("EX 15:6–7", "right: 12px; bottom: 12px"))
    r2 = use(DG[0], over=song(v("15:8"), "left: 12px; top: 12px", size=15.5, maxw=380) + vref("EX 15:8", "right: 12px; bottom: 12px"))
    r3 = cols(talk(A.PHARAOH, h[2], RED, [], w=W2, extra=song(v("15:9"), "left: 140px; top: 10px", size=13, maxw=190) + vref("EX 15:9", "left: 8px; bottom: 8px")),
              new(SEA, W2, h[2], D4.sunk(W2, h[2], 4133), song(v("15:10"), "left: 8px; top: 8px", size=14, maxw=320) + vref("EX 15:10", "right: 8px; bottom: 8px")))
    r4 = new(NIGHT, W1, h[3], X.cosmic(W1, h[3]) + E3.pillar_fire(W1 * 0.8, h[3], 0, W1 * 0.06, 4134), song(v("15:11"), "left: 12px; top: 12px", size=19, maxw=480) + vref("EX 15:11", "right: 12px; bottom: 12px"))
    return page("Exodus 15:6–11 — Who Is Like unto Thee, O Jehovah?", t, r1 + r2 + r3 + r4, START + 12)


@P("EXO-C04-P14-Song3", "79 · Jehovah Shall Reign for Ever and Ever")
def p14():
    t, h = rows(250, 270, None)
    r1 = cols(new(SEA, W2, h[0], E3.crash(W2, h[0], 4141), song(v("15:12"), "left: 8px; top: 8px", size=15, maxw=300) + vref("EX 15:12", "right: 8px; bottom: 8px")),
              use(EXO[3], over=song(v("15:13"), "left: 8px; top: 8px", size=13.5, maxw=320) + vref("EX 15:13", "right: 8px; bottom: 8px")))
    r2 = new(MAP, W1, h[1], D4.nations(W1, h[1], 4142), song(v("15:14") + " " + v("15:15") + " " + v("15:16"), "left: 12px; top: 12px", size=13, maxw=300) + vref("EX 15:14–16", "right: 12px; bottom: 12px"))
    r3 = new(DAWN, W1, h[2], D4.inheritance(W1, h[2], 4143), song(v("15:17"), "left: 12px; top: 12px", size=15, maxw=380)
             + song(v("15:18"), "right: 12px; bottom: 16px", size=24, maxw=400, color="#FFD23F") + vref("EX 15:17–18", "left: 12px; bottom: 12px"))
    return page("Exodus 15:12–18 — Jehovah Shall Reign for Ever and Ever", t, r1 + r2 + r3, START + 13)


@P("EXO-C04-P15-Miriam", "80 · Miriam the Prophetess")
def p15():
    t, h = rows(200, 330, None)
    r1 = new(SEA, W1, h[0], defs("x415a", *ALL) + D4.dry_walk("x415a", W1, h[0], 4151), cap(v("15:19"), "left: 12px; top: 12px", size=11, maxw=440) + vref("EX 15:19", "right: 12px; bottom: 12px"))
    r2 = cols(use(SO[2], over=cap(v("15:20"), "left: 8px; bottom: 8px", size=10.5, maxw=320) + vref("EX 15:20", "right: 8px; top: 8px")),
              use(SO[3], over=cap(v("15:21", to="answered them,"), "left: 8px; top: 8px", size=10.5) + song(v("15:21", frm="Sing ye"), "left: 8px; top: 44px", size=14, maxw=320)
                  + sfx("シャン", "SHAN", "right: 14px; bottom: 30px", size=34, fill="#E8B830", rot=-8) + vref("EX 15:21", "right: 8px; bottom: 8px")))
    r3 = new(SAND, W1, h[2], defs("x415c", *ALL) + D4.wilderness("x415c", W1, h[2], 4153, cast=[(A.moses, 0.62, 0.42, True, "staff"), (A.hebrew("#5A3A22"), 0.74, 0.46, True), (("woman", "#5A6E8A"), 0.82, 0.48, True), (A.hebrew("#8A6A4A"), 0.9, 0.44, True)]),
             cap(v("15:22"), "left: 12px; top: 12px", size=11, maxw=420) + cap(v("15:23"), "right: 12px; top: 100px", size=11, maxw=300)
             + cap(v("15:24", to="saying,"), "left: 12px; bottom: 70px", size=11) + balloon(v("15:24", frm="What shall"), "left: 30px; bottom: 16px", 230, size=14, pad="12px 18px") + vref("EX 15:22–24", "right: 12px; bottom: 12px"))
    return page("Exodus 15:19–24 — Miriam the Prophetess", t, r1 + r2 + r3, START + 14)


@P("EXO-C04-P16-Elim", "81 · Jehovah That Healeth Thee")
def p16():
    t, h = rows(300, 220, None)
    r1 = new(SAND, W1, h[0], defs("x416a", *ALL) + D4.marah("x416a", W1, h[0], 4161, sweet=True), cap(v("15:25"), "left: 12px; top: 12px", size=11, maxw=480) + vref("EX 15:25", "right: 12px; bottom: 12px"))
    r2 = night(W1, h[1], cap(v("15:26", to="and he said,"), "left: 12px; top: 12px", size=11) + god(v("15:26", frm="If thou wilt"), "left: 12px; top: 48px", size=15, maxw=640) + vref("EX 15:26", "right: 12px; bottom: 12px"))
    r3 = new(SKY, W1, h[2], D4.elim(None, W1, h[2], 4163), cap(v("15:27"), "left: 12px; top: 12px", size=11.5, maxw=420) + hud("12", "right: 120px; top: 14px", size=28) + hud("70", "right: 14px; top: 14px", size=28)
             + end_mark("NEXT · BREAD FROM HEAVEN", "left: 12px; bottom: 12px") + vref("EX 15:27", "right: 12px; bottom: 12px"))
    return page("Exodus 15:25–27 — Jehovah That Healeth Thee", t, r1 + r2 + r3, START + 15)
