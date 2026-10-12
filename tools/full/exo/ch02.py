"""Exodus volume, Chapter 2 — Let My People Go (Exodus 5–8). Every verse, word for word from ref/asv.
6:14–25 (the heads of the fathers' houses) is set as two scroll pages of clan cells, every verse in full."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus as E, exodus2 as E2
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from exo import G, art as A, art2 as B
from exo.kit import talk
from exo.ch01 import FIRE, bush_panel
from genesis import art as X, art2 as Y, art3 as Z, art10 as T
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import clan, hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch06 import RUST, GREENLIT, GOLDEN
from genesis.ch07 import RED, BLUE
from genesis.ch12 import NILE, COURT
from mk import defs, face

v, sp = G.v, G.span
B2 = "digest/exodus/book-02/"
D = [panels(B2 + n + ".dc.html") for n in ["EX2-P01-LetGo", "EX2-P02-Rods", "EX2-P03-Blood", "EX2-P04-Frogs"]]
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
REUBEN_C, SIMEON_C, LEVI_C = "#6A7AD8", "#8A6AB8", "#E8B830"
START = 21                                   # chapter 1 ends on page 20
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def night(w, h, over, extra=""):
    return new(NIGHT, w, h, X.cosmic(w, h) + extra, over)


@P("EXO-C02-00-Title", "Chapter 2 · Let My People Go")
def title():
    a = D[2][1]
    svg = f'<g transform="translate(-620 0) scale(2.62)">{a.svg}</g>'
    return chapter_title(2, "第二話", "Let My People Go", "Exodus 5 – 8", svg, a.bg,
                         v("5:1", frm="Let my people go,", to="in the wilderness."), "Exodus · Volume Two")


@P("EXO-C02-P01-WhoIsJehovah", "21 · Who Is Jehovah?")
def p01():
    t, h = rows(260, 300, None)
    r1 = use(D[0][0], over=cap(v("5:1", to="unto Pharaoh,"), "right: 12px; top: 12px", size=10.5, maxw=300)
             + balloon(v("5:1", frm="Thus saith"), "right: 20px; top: 70px", 330, size=13.5, pad="18px 26px") + mk.stamp(5, "right: 14px; bottom: 12px") + vref("EX 5:1", "left: 12px; bottom: 12px"))
    r2 = use(D[0][1], over=cap(v("5:2", to="And Pharaoh said,"), "left: 12px; top: 12px", size=11)
             + balloon(v("5:2", frm="Who is"), "left: 24px; top: 60px", 380, size=16, pad="26px 32px") + vref("EX 5:2", "left: 12px; bottom: 12px"))
    r3 = cols(talk(A.AARON, h[2], GOLDEN, [("cap", v("5:3", to="And they said,")), ("say", v("5:3", frm="The God"))], w=W2, ref="EX 5:3", size=12),
              talk(A.PHARAOH, h[2], RED, [("cap", v("5:4", to="unto them,")), ("say", v("5:4", frm="Wherefore")), ("cap", v("5:5", to="And Pharaoh said,")), ("say", v("5:5", frm="Behold,"))],
                   w=W2, ref="EX 5:4–5", size=12))
    return page("Exodus 5:1–5 — Who Is Jehovah?", t, r1 + r2 + r3, START + 0)


@P("EXO-C02-P02-Straw", "22 · Ye Shall No More Give the People Straw")
def p02():
    t, h = rows(360, 270, None)
    r1 = talk(A.PHARAOH, h[0], RED, [("cap", v("5:6")), ("say", v("5:7") + " " + v("5:8") + " " + v("5:9"))], ref="EX 5:6–9", size=13.5)
    r2 = talk(A.TASKMASTER, h[1], HOT, [("cap", v("5:10", to="saying,")), ("say", v("5:10", frm="Thus saith") + " " + v("5:11"))], ref="EX 5:10–11", size=14)
    r3 = new(SAND, W1, h[2], defs("x22b", *ALL) + B.stubble("x22b", W1, h[2], 222), cap(v("5:12"), "left: 12px; top: 12px", size=11.5, maxw=420) + vref("EX 5:12", "right: 12px; bottom: 12px"))
    return page("Exodus 5:6–12 — Ye Shall No More Give the People Straw", t, r1 + r2 + r3, START + 1)


@P("EXO-C02-P03-Beaten", "23 · Thy Servants Are Beaten")
def p03():
    t, h = rows(300, 250, None)
    r1 = new(HOT, W1, h[0], defs("x23a", *ALL) + B.beaten("x23a", W1, h[0], 231),
             cap(v("5:13", to="urgent saying,"), "left: 12px; top: 12px", size=10.5) + balloon(v("5:13", frm="Fulfil"), "left: 12px; top: 48px", 260, size=12.5, pad="14px 18px")
             + cap(v("5:14", to="and demanded,"), "right: 12px; top: 12px", size=10.5, maxw=360) + balloon(v("5:14", frm="Wherefore"), "right: 110px; top: 104px", 270, size=12.5, pad="20px 22px")
             + sfx("ビシッ", "BISHI!", "left: 300px; top: 170px", size=40, fill="#D7261E", rot=-8) + vref("EX 5:13–14", "left: 12px; bottom: 12px"))
    r2 = talk(B.OFFICER, h[1], GOLDEN, [("cap", v("5:15", to="saying,")), ("say", v("5:15", frm="Wherefore") + " " + v("5:16"))], ref="EX 5:15–16", size=13.5)
    r3 = cols(talk(A.PHARAOH, h[2], RED, [("cap", v("5:17", to="But he said,")), ("say", v("5:17", frm="Ye are idle,") + " " + v("5:18"))], w=W2, ref="EX 5:17–18", size=12),
              talk(B.OFFICER, h[2], COLD, [("cap", v("5:19"))], w=W2, flip=True, ref="EX 5:19"))
    return page("Exodus 5:13–19 — Thy Servants Are Beaten", t, r1 + r2 + r3, START + 2)


@P("EXO-C02-P04-Wherefore", "24 · Wherefore Hast Thou Dealt Ill with This People?")
def p04():
    t, h = rows(250, 250, None)
    r1 = new(SAND, W1, h[0], defs("x24a", *ALL) + B.palace_gate("x24a", W1, h[0], 241, [(A.aaron, 0.18, 0.42), (A.moses, 0.26, 0.4, False, "staff")]
                                                                 + [(B.officer, 0.62 + i * 0.08, 0.44, True) for i in range(4)]),
             cap(v("5:20"), "left: 12px; top: 12px", size=10.5, maxw=330) + vref("EX 5:20", "right: 12px; bottom: 12px"))
    r2 = talk(B.OFFICER_ANGRY, h[1], RED, [("cap", v("5:21", to="unto them,")), ("say", v("5:21", frm="Jehovah look"))], ref="EX 5:21", size=13.5)
    r3 = cols(talk(A.MOSES_OLD_PLEA, h[2], BLUE, [("cap", v("5:22", to="and said,")), ("say", v("5:22", frm="Lord,") + " " + v("5:23"))], w=W2, ref="EX 5:22–23", size=12),
              night(W2, h[2], cap(v("6:1", to="unto Moses,"), "left: 8px; top: 8px", size=10.5) + god(v("6:1", frm="Now shalt"), "left: 8px; top: 44px", size=15, maxw=320)
                    + mk.stamp(6, "right: 10px; bottom: 10px") + vref("EX 6:1", "left: 8px; bottom: 8px")))
    return page("Exodus 5:20–6:1 — Wherefore Hast Thou Dealt Ill with This People?", t, r1 + r2 + r3, START + 3)


@P("EXO-C02-P05-IAmJehovah", "25 · I Am Jehovah")
def p05():
    t, h = rows(330, 250, None)
    r1 = new(NIGHT, W1, h[0], defs("x25a", *ALL) + B.patriarchs("x25a", W1, h[0], 251),
             cap(v("6:2", to="said unto him,"), "left: 12px; top: 12px", size=11, maxw=230) + god(v("6:2", frm="I am Jehovah:"), "left: 12px; top: 70px", size=30)
             + god(v("6:3"), "right: 12px; top: 12px", size=15, maxw=340) + vref("EX 6:2–3", "right: 12px; bottom: 12px"))
    r2 = cols(new("#0B1A2E", W2, h[1], A.exodus_map(W2, h[1], names=["CANAAN"], cur="CANAAN"), god(v("6:4"), "left: 8px; bottom: 8px", size=13, maxw=320) + vref("EX 6:4", "right: 8px; top: 8px")),
              new(HOT, W2, h[1], defs("x25b", *ALL) + A.bricks("x25b", W2, h[1], 252), god(v("6:5"), "left: 8px; top: 8px", size=13, maxw=320) + vref("EX 6:5", "right: 8px; bottom: 8px")))
    r3 = new(NIGHT, W1, h[2], A.wonders(W1, h[2], 253), god(v("6:6"), "left: 12px; top: 12px", size=17, maxw=470) + vref("EX 6:6", "right: 12px; bottom: 12px"))
    return page("Exodus 6:2–6 — I Am Jehovah", t, r1 + r2 + r3, START + 4)


@P("EXO-C02-P06-Anguish", "26 · For Anguish of Spirit")
def p06():
    t, h = rows(250, 220, None)
    r1 = cols(new(SAND, W2, h[0], defs("x26a", *ALL) + A.elders("x26a", W2, h[0], 261), god(v("6:7"), "left: 8px; top: 8px", size=13, maxw=320) + vref("EX 6:7", "right: 8px; bottom: 8px")),
              new(SKY, W2, h[0], A.milk_honey(None, W2, h[0], 262), god(v("6:8"), "left: 8px; top: 8px", size=13, maxw=320) + vref("EX 6:8", "right: 8px; bottom: 8px")))
    r2 = talk(A.SLAVE, h[1], COLD, [("cap", v("6:9"))], ref="EX 6:9")
    r3 = cols(bush_panel(W2, h[2], 263, cap(v("6:10"), "left: 8px; top: 8px", size=10.5) + god(v("6:11"), "left: 8px; top: 44px", size=15, maxw=320) + vref("EX 6:10–11", "right: 8px; bottom: 8px"), cx=0.78, size=0.7),
              talk(A.MOSES_OLD_PLEA, h[2], BLUE, [("cap", v("6:12", to="saying,")), ("say", v("6:12", frm="Behold,"))], w=W2, ref="EX 6:12", size=12.5))
    return page("Exodus 6:7–12 — For Anguish of Spirit", t, r1 + r2 + r3, START + 5)


@P("EXO-C02-P07-Heads1", "27 · The Heads of Their Fathers' Houses")
def p07():
    t, h = rows(170, None)
    r1 = new(DUSK, W1, h[0], defs("x27a", *ALL) + T.stage("x27a", W1, h[0], 271, "dusk", [(A.aaron, 0.44, 0.34), (A.moses, 0.56, 0.34, True, "staff")]),
             cap(v("6:13"), "left: 12px; top: 12px", size=10.5, maxw=260) + vref("EX 6:13", "right: 12px; bottom: 12px"))
    cells = [clan("Reuben", v("6:14"), "EX 6:14", REUBEN_C, size=15),
             clan("Simeon", v("6:15"), "EX 6:15", SIMEON_C, size=15),
             clan("Levi", v("6:16"), "EX 6:16", LEVI_C, size=15),
             clan("Gershon", v("6:17"), "EX 6:17", LEVI_C, of="OF LEVI", size=16),
             clan("Kohath", v("6:18"), "EX 6:18", LEVI_C, of="OF LEVI", size=15),
             clan("Merari", v("6:19"), "EX 6:19", LEVI_C, of="OF LEVI", size=15)]
    return page("Exodus 6:13–19 — The Heads of Their Fathers' Houses", t, r1 + grid(cells, "repeat(3, minmax(0, 1fr))"), START + 6)


@P("EXO-C02-P08-Heads2", "28 · These Are That Aaron and Moses")
def p08():
    t, h = rows(None, 230)
    cells = [clan("Amram", v("6:20"), "EX 6:20", "#FFD23F", of="OF KOHATH", size=14),
             clan("Izhar · Uzziel", v("6:21") + " " + v("6:22"), "EX 6:21–22", LEVI_C, of="OF KOHATH", size=15),
             clan("Aaron", v("6:23"), "EX 6:23", "#8FB8E8", of="OF AMRAM", size=14),
             clan("Korah", v("6:24"), "EX 6:24", LEVI_C, of="OF IZHAR", size=15),
             clan("Eleazar", v("6:25"), "EX 6:25", "#8FB8E8", of="OF AARON", size=14)]
    r2 = new(DUSK, W1, h[1], defs("x28b", *ALL) + T.stage("x28b", W1, h[1], 282, "egypt", [(A.aaron, 0.62, 0.4), (A.moses, 0.72, 0.38, True, "staff")]),
             cap(v("6:26") + " " + v("6:27"), "left: 12px; top: 12px", size=11, maxw=380) + vref("EX 6:26–27", "right: 12px; bottom: 12px"))
    return page("Exodus 6:20–27 — These Are That Aaron and Moses", t, grid(cells + [levi_tree()], "repeat(3, minmax(0, 1fr))") + r2, START + 7)

def levi_tree():
    """A small family tree, Levi to Phinehas, with Moses and Aaron picked out (labels only: the verses are in the cells)."""
    L = lambda x, y, t, c="#F3EFE6": f'<text x="{x}" y="{y}" fill="{c}" font-family="IBM Plex Mono, monospace" font-weight="600" font-size="12" letter-spacing="0.1em" text-anchor="middle">{t}</text>'
    ln = lambda d: f'<path d="{d}" fill="none" stroke="#E8B830" stroke-width="2"></path>'
    svg = (ln("M160 22 L 160 30 M60 30 L 260 30 M60 30 L 60 38 M160 30 L 160 38 M260 30 L 260 38")
           + ln("M160 56 L 160 68") + ln("M160 86 L 160 96 M110 96 L 210 96 M110 96 L 110 104 M210 96 L 210 104") + ln("M110 122 L 110 134") + ln("M110 152 L 110 164")
           + L(160, 16, "LEVI", "#E8B830") + L(60, 50, "GERSHON") + L(160, 50, "KOHATH") + L(260, 50, "MERARI") + L(160, 80, "AMRAM")
           + L(110, 116, "AARON", "#8FB8E8") + L(210, 116, "MOSES", "#FFD23F") + L(110, 146, "ELEAZAR", "#8FB8E8") + L(110, 176, "PHINEHAS", "#8FB8E8"))
    return (f'\n    <div style="position: relative; min-height: 0; border: 3px solid #0D0D0F; background: #12113A; overflow: hidden">'
            f'<svg viewBox="0 0 320 190" preserveAspectRatio="xMidYMid meet" style="position: absolute; inset: 8px; width: calc(100% - 16px); height: calc(100% - 16px)">{svg}</svg></div>')


@P("EXO-C02-P09-AsGod", "29 · I Have Made Thee as God to Pharaoh")
def p09():
    t, h = rows(250, 200, None)
    r1 = night(W1, h[0], cap(v("6:28") + " " + v("6:29", to="saying,"), "left: 12px; top: 12px", size=11, maxw=460)
               + god(v("6:29", frm="I am Jehovah:"), "left: 12px; top: 80px", size=19, maxw=460) + vref("EX 6:28–29", "right: 12px; bottom: 12px"),
               extra=A.EG.pyramid(W1 * 0.86, h[0], W1 * 0.3, h[0] * 0.4))
    r2 = talk(A.MOSES_OLD_PLEA, h[1], BLUE, [("cap", v("6:30", to="before Jehovah,")), ("say", v("6:30", frm="Behold,"))], ref="EX 6:30", size=14)
    r3 = new(DUSK, W1, h[2], defs("x29c", *ALL) + T.stage("x29c", W1, h[2], 293, "egypt", [(A.moses, 0.68, 0.36, False, "staff"), (A.aaron, 0.8, 0.4, True)]),
             cap(v("7:1", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(v("7:1", frm="See,") + " " + v("7:2"), "left: 12px; top: 48px", size=17, maxw=400)
             + mk.stamp(7, "right: 14px; top: 12px") + vref("EX 7:1–2", "right: 12px; bottom: 12px"))
    return page("Exodus 6:28–7:2 — I Have Made Thee as God to Pharaoh", t, r1 + r2 + r3, START + 8)


@P("EXO-C02-P10-Fourscore", "30 · Fourscore Years Old")
def p10():
    t, h = rows(330, 240, None)
    r1 = new(NIGHT, W1, h[0], A.wonders(W1, h[0], 301), god(v("7:3") + " " + v("7:4"), "left: 12px; top: 12px", size=17, maxw=420) + vref("EX 7:3–4", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], defs("x210b", *ALL) + A.crowd("x210b", W1, h[1], 302, n=60), god(v("7:5"), "left: 12px; top: 12px", size=16, maxw=560) + vref("EX 7:5", "right: 12px; bottom: 12px"))
    r3 = new(GOLDEN, W1, h[2], defs("x210c", *ALL) + T.stage("x210c", W1, h[2], 303, "egypt", [(A.moses, 0.34, 0.34, False, "staff"), (A.aaron, 0.5, 0.36, True)]),
             cap(v("7:6") + " " + v("7:7"), "right: 12px; top: 12px", size=11.5, maxw=280) + hud("80", "left: 210px; top: 70px", size=30) + hud("83", "left: 322px; top: 70px", size=30)
             + vref("EX 7:6–7", "right: 12px; bottom: 12px"))
    return page("Exodus 7:3–7 — Fourscore Years Old", t, r1 + r2 + r3, START + 9)


@P("EXO-C02-P11-Serpents", "31 · Aaron's Rod Swallowed Up Their Rods")
def p11():
    t, h = rows(170, 310, 250, None)
    r1 = night(W1, h[0], cap(v("7:8"), "left: 12px; top: 12px", size=10.5) + god(v("7:9"), "left: 12px; top: 46px", size=14, maxw=640) + vref("EX 7:8–9", "right: 12px; bottom: 12px"))
    r2 = use(D[1][0], over=cap(v("7:10"), "left: 12px; top: 12px", size=10.5, maxw=400) + sfx("シュルル", "SHURURU", "left: 300px; bottom: 60px", size=36, fill="#9CCB5E", rot=-8) + vref("EX 7:10", "right: 12px; bottom: 12px"))
    r3 = cols(use(D[1][1], over=cap(v("7:11"), "right: 8px; bottom: 8px", size=10.5, maxw=220) + vref("EX 7:11", "left: 8px; top: 8px")),
              use(D[1][2], over=cap(v("7:12", to="became serpents:"), "left: 8px; top: 8px", size=11, maxw=320) + vref("EX 7:12", "right: 8px; bottom: 8px")))
    r4 = use(D[1][3], over=cap(v("7:12", frm="but Aaron's"), "left: 12px; top: 12px", size=11.5) + cap(v("7:13"), "right: 12px; bottom: 14px", size=11, maxw=330)
             + sfx("ゴクリ", "GOKURI", "left: 200px; top: 50px", size=46, fill="#F3EFE6", stroke="#0D0D0F", rot=-6) + vref("EX 7:12–13", "left: 12px; bottom: 12px"))
    return page("Exodus 7:8–13 — Aaron's Rod Swallowed Up Their Rods", t, r1 + r2 + r3 + r4, START + 10)


@P("EXO-C02-P12-River", "32 · By the River's Brink")
def p12():
    t, h = rows(330, 250, None)
    r1 = new(SKY, W1, h[0], defs("x212a", *ALL) + B.river("x212a", W1, h[0], 321, cast=[(A.pharaoh, 0.8, 0.5, True), (A.moses, 0.3, 0.48, False, "staff")]),
             cap(v("7:14", to="unto Moses,"), "left: 12px; top: 12px", size=10.5) + god(v("7:14", frm="Pharaoh's heart") + " " + v("7:15"), "left: 12px; top: 48px", size=14, maxw=640) + vref("EX 7:14–15", "right: 12px; bottom: 12px"))
    r2 = new(RED, W1, h[1], fc(A.MOSES_STERN, h[1]), god(v("7:16"), "left: 300px; top: 14px", size=16, maxw=380) + vref("EX 7:16", "left: 12px; bottom: 12px"))
    r3 = new(SKY, W1, h[2], B.river(None, W1, h[2], 323, blood=True, dead=True), god(v("7:17") + " " + v("7:18"), "left: 12px; top: 12px", size=15, maxw=640) + vref("EX 7:17–18", "right: 12px; bottom: 12px"))
    return page("Exodus 7:14–18 — By the River's Brink", t, r1 + r2 + r3, START + 11)


@P("EXO-C02-P13-Blood", "33 · The Waters Were Turned to Blood")
def p13():
    t, h = rows(250, 270, None)
    r1 = night(W1, h[0], cap(v("7:19", to="unto Moses,"), "left: 12px; top: 12px", size=10.5) + god(v("7:19", frm="Say unto Aaron,"), "left: 12px; top: 46px", size=15, maxw=660) + vref("EX 7:19", "right: 12px; bottom: 12px"))
    r2 = use(D[2][0], over=cap(v("7:20", to="servants;"), "left: 12px; top: 12px", size=10.5, maxw=440) + sfx("バシャッ", "BASHA!", "right: 120px; top: 110px", size=40, fill="#D7261E", rot=-6) + vref("EX 7:20", "right: 12px; bottom: 12px"))
    r3 = use(D[2][1], over=cap(v("7:20", frm="and all the waters"), "left: 12px; top: 12px", size=11.5) + cap(v("7:21"), "right: 12px; bottom: 14px", size=11, maxw=380)
             + sfx("ドロッ", "DORO", "left: 30px; top: 120px", size=48, fill="#D7261E", stroke="#F3EFE6", rot=-6) + vref("EX 7:20–21", "left: 12px; bottom: 12px"))
    return page("Exodus 7:19–21 — The Waters Were Turned to Blood", t, r1 + r2 + r3, START + 12)


@P("EXO-C02-P14-SevenDays", "34 · Seven Days Were Fulfilled")
def p14():
    t, h = rows(290, 280, None)
    r1 = cols(use(D[1][1], over=cap(v("7:22"), "right: 8px; bottom: 8px", size=10.5, maxw=220) + vref("EX 7:22", "left: 8px; top: 8px")),
              use(D[2][2], over=cap(v("7:23"), "left: 8px; bottom: 8px", size=11, maxw=320) + vref("EX 7:23", "right: 8px; top: 8px")))
    r2 = cols(use(D[2][3], over=cap(v("7:24"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 7:24", "right: 8px; bottom: 8px")),
              new(BLOOD, W2, h[1], B.river(None, W2, h[1], 342, blood=True, dead=True), cap(v("7:25"), "left: 8px; top: 8px", size=11, maxw=300) + hud("7 DAYS", "right: 10px; bottom: 30px", size=26) + vref("EX 7:25", "left: 8px; bottom: 8px")))
    r3 = new(NILE, W1, h[2], B.river(None, W1, h[2], 343) + E2.frogs(10, 0, W1, h[2] * 0.72, h[2], 344),
             cap(v("8:1", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(v("8:1", frm="Go in") + " " + v("8:2"), "left: 12px; top: 48px", size=17, maxw=560)
             + mk.stamp(8, "right: 14px; top: 12px") + vref("EX 8:1–2", "right: 12px; bottom: 12px"))
    return page("Exodus 7:22–8:2 — Seven Days Were Fulfilled", t, r1 + r2 + r3, START + 13)


@P("EXO-C02-P15-Frogs", "35 · The Frogs Came Up")
def p15():
    t, h = rows(300, 170, None)
    r1 = new(COURT, W1, h[0], B.bedchamber(W1, h[0], 351), god(v("8:3") + " " + v("8:4"), "left: 12px; top: 12px", size=15, maxw=640) + vref("EX 8:3–4", "right: 12px; bottom: 12px"))
    r2 = night(W1, h[1], cap(v("8:5", to="unto Moses,"), "left: 12px; top: 12px", size=10.5) + god(v("8:5", frm="Say unto Aaron,"), "left: 12px; top: 46px", size=14, maxw=660) + vref("EX 8:5", "right: 12px; bottom: 12px"))
    r3 = use(D[3][0], over=cap(v("8:6"), "left: 12px; top: 12px", size=11, maxw=440) + cap(v("8:7"), "right: 12px; bottom: 14px", size=11, maxw=300)
             + sfx("ゲコゲコ", "GEKO GEKO", "right: 20px; top: 20px", size=40, fill="#9CCB5E", rot=-6) + vref("EX 8:6–7", "left: 12px; bottom: 12px"))
    return page("Exodus 8:3–7 — The Frogs Came Up", t, r1 + r2 + r3, START + 14)


@P("EXO-C02-P16-Tomorrow", "36 · Against To-morrow")
def p16():
    t, h = rows(230, 280, None)
    r1 = talk(A.PHARAOH_FEAR, h[0], RED, [("cap", v("8:8", to="and said,")), ("say", v("8:8", frm="Entreat"))], ref="EX 8:8", size=14)
    r2 = talk(A.MOSES_CALM, h[1], GOLDEN, [("cap", v("8:9", to="unto Pharaoh,")), ("say", v("8:9", frm="Have thou"))], ref="EX 8:9", size=14)
    r3 = cols(talk(A.PHARAOH_FEAR, h[2], RED, [("cap", v("8:10", to="And he said,")), ("say", v("8:10", frm="Against", to="to-morrow."))], w=W2, ref="EX 8:10", size=14),
              talk(A.MOSES_CALM, h[2], GOLDEN, [("cap", v("8:10", frm="And he said, Be", to="said,")), ("say", v("8:10", frm="Be it") + " " + v("8:11"))], w=W2, flip=True, ref="EX 8:11", size=12))
    return page("Exodus 8:8–11 — Against To-morrow", t, r1 + r2 + r3, START + 15)


@P("EXO-C02-P17-Lice", "37 · The Dust of the Earth Became Lice")
def p17():
    t, h = rows(250, 210, None)
    r1 = cols(talk(A.MOSES, h[0], NIGHT, [("cap", v("8:12"))], w=W2, ref="EX 8:12"),
              new(SAND, W2, h[0], B.frog_heaps(W2, h[0], 371), cap(v("8:13") + " " + v("8:14"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 8:13–14", "right: 8px; bottom: 8px")))
    r2 = talk(A.PHARAOH, h[1], RED, [("cap", v("8:15"))], ref="EX 8:15")
    r3 = cols(night(W2, h[2], cap(v("8:16", to="unto Moses,"), "left: 8px; top: 8px", size=10.5) + god(v("8:16", frm="Say unto Aaron,"), "left: 8px; top: 44px", size=14, maxw=320) + vref("EX 8:16", "right: 8px; bottom: 8px"),
                    extra=E2.lice(300, 0, W2, h[2] * 0.7, h[2], 372)),
              new(SAND, W2, h[2], defs("x217c", *ALL) + T.stage("x217c", W2, h[2], 373, "sand", [(A.aaron, 0.36, 0.5, False, [(-22, -158), (-40, -120), (-62, -60)])],
                                                                 props=E2.lice(500, 0, W2, h[2] * 0.3, h[2], 374)),
                  cap(v("8:17"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 8:17", "right: 8px; bottom: 8px")))
    return page("Exodus 8:12–17 — The Dust of the Earth Became Lice", t, r1 + r2 + r3, START + 16)


@P("EXO-C02-P18-Finger", "38 · This Is the Finger of God")
def p18():
    t, h = rows(330, 250, None)
    r1 = cols(use(D[3][2], over=cap(v("8:18"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 8:18", "left: 8px; bottom: 8px")),
              talk(B.MAGICIAN_FEAR, h[0], "linear-gradient(180deg, #2A1A4E 0%, #7A3BA8 100%)",
                   [("cap", v("8:19", to="unto Pharaoh,")), ("say", v("8:19", frm="This is", to="finger of God:").rstrip(":")), ("cap", v("8:19", frm="and Pharaoh's heart"))], w=W2, flip=True, ref="EX 8:19", size=13))
    r2 = new(SKY, W1, h[1], defs("x218b", *ALL) + B.river("x218b", W1, h[1], 382, cast=[(A.pharaoh, 0.78, 0.46, True), (A.moses, 0.26, 0.44, False, "staff")]),
             cap(v("8:20", to="unto Moses,"), "left: 12px; top: 12px", size=10.5) + god(v("8:20", frm="Rise up"), "left: 12px; top: 46px", size=14, maxw=640) + vref("EX 8:20", "right: 12px; bottom: 12px"))
    r3 = new(GREY, W1, h[2], B.river(None, W1, h[2], 383) + E2.swarm(180, W1 * 0.5, h[2] * 0.5, W1 * 0.5, h[2] * 0.5, 384),
             god(v("8:21"), "left: 12px; top: 12px", size=16, maxw=560) + vref("EX 8:21", "right: 12px; bottom: 12px"))
    return page("Exodus 8:18–21 — This Is the Finger of God", t, r1 + r2 + r3, START + 17)


@P("EXO-C02-P19-Division", "39 · A Division Between My People and Thy People")
def p19():
    t, h = rows(300, 260, None)
    r1 = new(SKY, W1, h[0], B.goshen_divide(W1, h[0], 391), god(v("8:22") + " " + v("8:23"), "left: 12px; top: 12px", size=14, maxw=300) + vref("EX 8:22–23", "right: 12px; top: 12px"))
    r2 = use(D[3][3], over=cap(v("8:24"), "left: 12px; top: 12px", size=11, maxw=460) + sfx("ブウウン", "BUUUN", "right: 30px; bottom: 30px", size=40, fill="#F3EFE6", stroke="#0D0D0F", rot=-6) + vref("EX 8:24", "left: 12px; bottom: 12px"))
    r3 = cols(talk(A.PHARAOH_FEAR, h[2], RED, [("cap", v("8:25", to="and said,")), ("say", v("8:25", frm="Go ye,"))], w=W2, ref="EX 8:25", size=13),
              talk(A.MOSES_STERN, h[2], RED, [("cap", v("8:26", to="And Moses said,")), ("say", v("8:26", frm="It is not") + " " + v("8:27"))], w=W2, flip=True, ref="EX 8:26–27", size=11.5))
    return page("Exodus 8:22–27 — A Division Between My People and Thy People", t, r1 + r2 + r3, START + 18)


@P("EXO-C02-P20-NotOne", "40 · There Remained Not One")
def p20():
    t, h = rows(230, 300, None)
    r1 = talk(A.PHARAOH_FEAR, h[0], RED, [("cap", v("8:28", to="And Pharaoh said,")), ("say", v("8:28", frm="I will let"))], ref="EX 8:28", size=14)
    r2 = talk(A.MOSES_STERN, h[1], GOLDEN, [("cap", v("8:29", to="And Moses said,")), ("say", v("8:29", frm="Behold,"))], ref="EX 8:29", size=14)
    r3 = cols(new(SKY, W2, h[2], B.clear_sky(None, W2, h[2], 401), cap(v("8:30") + " " + v("8:31"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 8:30–31", "right: 8px; bottom: 8px")),
              talk(A.PHARAOH, h[2], RED, [("cap", v("8:32"))], w=W2, flip=True, ref="EX 8:32", extra=end_mark("NEXT · THE PASSOVER", "left: 12px; bottom: 12px")))
    return page("Exodus 8:28–32 — There Remained Not One", t, r1 + r2 + r3, START + 19)
