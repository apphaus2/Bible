"""Exodus volume, Chapter 1 — The Bush That Burned (Exodus 1–4). Every verse, word for word from ref/asv.
The digest's Exodus Book One drawings are lifted where they fit; new drawings are in exo/art.py."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus as E
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from exo import G, art as A
from exo.kit import talk
from genesis import art as X, art2 as Y, art3 as Z, art10 as T
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch06 import RUST, GREENLIT, GOLDEN
from genesis.ch07 import RED, BLUE
from genesis.ch12 import NILE, COURT
from mk import defs, face

v, sp = G.v, G.span
B1 = "reference/exodus/book-01/"
D = [panels(B1 + n + ".dc.html") for n in ["EX1-P01-King", "EX1-P02-Ark", "EX1-P03-Drawn", "EX1-P04-Egyptian", "EX1-P05-Midian", "EX1-P06-Bush", "EX1-P07-IAM", "EX1-P08-Rod"]]
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
FIRE = "linear-gradient(180deg, #1A0408 0%, #6A1A1E 50%, #FF6A2A 100%)"
START = 1                                    # the volume cover and this chapter's title page come first
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def bush_panel(w, h, seed, over, cx=0.5, size=1.0):
    return new(NIGHT, w, h, A.burning(w, h, seed, cx=cx, size=size), over)


@P("EXO-C01-00-Title", "Chapter 1 · The Bush That Burned")
def title():
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#0B0B2A"></rect>' + A.burning(760, 1080, 101, cx=0.4, bw=560, bh=500)
           + E.kneel(640, 994, 1.3, color="#3A2214", rim="#FF8A3D", flip=True) + E.sandal(700, 1030, 0.8, -70) + E.sandal(730, 1036, 0.8, -80))
    return chapter_title(1, "第一話", "The Bush That Burned", "Exodus 1 – 4", svg, NIGHT,
                         v("3:2", frm="and, behold,"), "Exodus · Volume Two")


@P("EXO-C01-P01-Names", "1 · These Are the Names")
def p01():
    t, h = rows(330, 180, None)
    r1 = new(SAND, W1, h[0], defs("x11a", *ALL) + A.sons_row("x11a", W1, h[0], 111),
             cap(v("1:1") + " " + v("1:2") + " " + v("1:3") + " " + v("1:4"), "left: 12px; top: 12px", size=10.5, maxw=400)
             + cap(v("1:5"), "right: 12px; top: 12px", size=10.5, maxw=216) + vref("EX 1:1–5", "right: 12px; bottom: 8px"))
    r2 = cols(new(DUSK, W2, h[1], A.tombs(W2, h[1], 112), cap(v("1:6"), "left: 8px; top: 8px", size=10.5, maxw=300) + vref("EX 1:6", "right: 8px; bottom: 8px")),
              new(SAND, W2, h[1], defs("x11b", *ALL) + A.crowd("x11b", W2, h[1], 113), cap(v("1:7"), "left: 8px; top: 8px", size=10, maxw=320) + vref("EX 1:7", "right: 8px; bottom: 8px")))
    r3 = talk(A.PHARAOH, h[2], RED, [("cap", v("1:8")), ("cap", v("1:9", to="unto his people,")), ("say", v("1:9", frm="Behold,") + " " + v("1:10"))], ref="EX 1:8–10", size=14, extra=mk.stamp(1, "right: 14px; bottom: 14px"))
    return page("Exodus 1:1–10 — These Are the Names", t, r1 + r2 + r3, START + 0)


@P("EXO-C01-P02-Rigor", "2 · They Made Their Lives Bitter")
def p02():
    t, h = rows(356, 288, None)
    r1 = use(D[0][1], over=cap(v("1:11"), "left: 12px; top: 12px", size=11, maxw=420) + sfx("ビシッ", "BISHI!", "right: 140px; bottom: 60px", size=40, fill="#D7261E", rot=-8) + vref("EX 1:11", "right: 12px; bottom: 12px"))
    r2 = cols(use(D[0][2], over=cap(v("1:12"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 1:12", "right: 8px; bottom: 8px")),
              use(D[0][3], over=cap(v("1:13") + " " + v("1:14"), "right: 8px; bottom: 8px", size=10, maxw=230) + vref("EX 1:13–14", "left: 8px; top: 8px")))
    r3 = cols(new(GOLDEN, W2, h[2], fc(A.SHIPHRAH, h[2]),
                  cap(v("1:15"), "right: 8px; top: 8px", size=10.5, maxw=190) + vref("EX 1:15", "left: 8px; bottom: 8px")),
              talk(A.PHARAOH, h[2], RED, [("cap", v("1:16", to="and he said,")), ("say", v("1:16", frm="When ye do"))], w=W2, ref="EX 1:16", size=12.5))
    return page("Exodus 1:11–16 — They Made Their Lives Bitter", t, r1 + r2 + r3, START + 1)


@P("EXO-C01-P03-Midwives", "3 · The Midwives Feared God")
def p03():
    t, h = rows(220, 290, 190, None)
    r1 = new(GOLDEN, W1, h[0], face(A.SHIPHRAH_BOLD, -30, h[0] - 300, 0.8) + face(A.PUAH, W1 + 30, h[0] - 300, 0.8, flip=True),
             cap(v("1:17"), "left: 230px; top: 14px", size=11.5, maxw=250) + vref("EX 1:17", "left: 12px; bottom: 12px"))
    r2 = cols(talk(A.PHARAOH, h[1], RED, [("cap", v("1:18", to="said unto them,")), ("say", v("1:18", frm="Why have"))], w=W2, ref="EX 1:18", size=12.5),
              talk(A.SHIPHRAH, h[1], GOLDEN, [("cap", v("1:19", to="unto Pharaoh,")), ("say", v("1:19", frm="Because"))], w=W2, flip=True, ref="EX 1:19", size=12))
    r3 = new(SAND, W1, h[2], defs("x13c", *ALL) + A.households("x13c", W1, h[2], 133),
             cap(v("1:20") + " " + v("1:21"), "left: 12px; top: 12px", size=10.5, maxw=440) + vref("EX 1:20–21", "right: 12px; bottom: 12px"))
    r4 = use(D[1][0], over=cap(v("1:22", to="saying,"), "left: 12px; top: 12px", size=11)
             + balloon(v("1:22", frm="Every son"), "left: 40px; top: 60px", 360, size=15, pad="20px 28px") + vref("EX 1:22", "left: 12px; bottom: 12px"))
    return page("Exodus 1:17–22 — The Midwives Feared God", t, r1 + r2 + r3 + r4, START + 2)


@P("EXO-C01-P04-Ark", "4 · An Ark of Bulrushes")
def p04():
    t, h = rows(230, 380, None)
    r1 = new(EMBER, W1, h[0], face(A.LEVITE, -30, h[0] - 290, 0.78) + face(A.JOCHEBED, W1 + 30, h[0] - 290, 0.78, flip=True) + A.lamp(W1 * 0.5, h[0] * 0.72, 1.6),
             cap(v("2:1"), "left: 230px; top: 12px", size=11, maxw=240) + mk.stamp(2, "left: 50%; bottom: 14px; margin-left: -46px") + vref("EX 2:1", "left: 12px; bottom: 12px"))
    r2 = cols(use(D[1][1], over=cap(v("2:2"), "left: 8px; bottom: 8px", size=10.5, maxw=320) + vref("EX 2:2", "right: 8px; top: 8px")),
              use(D[1][2], over=cap(v("2:3", to="with pitch;"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 2:3", "right: 8px; bottom: 8px")))
    r3 = use(D[1][3], over=cap(v("2:3", frm="and she put"), "left: 12px; top: 12px", size=11, maxw=380)
             + cap(v("2:4"), "right: 12px; bottom: 14px", size=11, maxw=300) + sfx("チャプ", "CHAPU", "right: 60px; top: 70px", size=38, fill="#8FD0E2", stroke="#0D0D0F", rot=-6) + vref("EX 2:3–4", "left: 12px; bottom: 12px"))
    return page("Exodus 2:1–4 — An Ark of Bulrushes", t, r1 + r2 + r3, START + 3)


@P("EXO-C01-P05-Babe", "5 · Behold, the Babe Wept")
def p05():
    t, h = rows(320, 330, None)
    r1 = use(D[2][0], over=cap(v("2:5"), "left: 12px; top: 12px", size=11, maxw=500) + vref("EX 2:5", "right: 12px; bottom: 12px"))
    r2 = cols(use(D[2][1], over=cap(v("2:6", to="the babe wept."), "left: 8px; bottom: 8px", size=10.5, maxw=320)
                  + sfx("オギャア", "OGYAA!", "right: 10px; top: 14px", size=34, fill="#D7261E", rot=-6) + vref("EX 2:6", "left: 8px; top: 8px")),
              use(D[2][2], over=cap(v("2:6", frm="And she had compassion", to="and said,"), "right: 8px; bottom: 8px", size=10.5, maxw=220)
                  + balloon(v("2:6", frm="This is one"), "left: 10px; top: 30px", 160, size=12.5, pad="20px 16px")))
    r3 = talk(A.MIRIAM, h[2], GREEN, [("cap", v("2:7", to="to Pharaoh's daughter,")), ("say", v("2:7", frm="Shall I go")),
                                       ("cap", v("2:8", to="said to her,")), ("say", v("2:8", frm="Go.", to="Go.")), ("cap", v("2:8", frm="And the maiden"))], ref="EX 2:7–8", size=14)
    return page("Exodus 2:5–8 — Behold, the Babe Wept", t, r1 + r2 + r3, START + 4)


@P("EXO-C01-P06-Moses", "6 · I Drew Him Out of the Water")
def p06():
    t, h = rows(280, 290, None)
    r1 = cols(talk(A.PRINCESS, h[0], NILE, [("cap", v("2:9", to="said unto her,")), ("say", v("2:9", frm="Take this", to="thy wages."))], w=W2, ref="EX 2:9", size=12.5),
              new(EMBER, W2, h[0], Y.mother_and_child(W2, h[0], tok=A.JOCHEBED, baby_xy=(250, h[0] - 70)), cap(v("2:9", frm="And the woman"), "right: 8px; top: 8px", size=10.5, maxw=150)))
    r2 = cols(new(COURT, W2, h[1], defs("x16b", *ALL) + T.stage("x16b", W2, h[1], 162, "palace", [(A.princess, 0.2, 0.42), (("lad", "#F3EFE6"), 0.4, 0.6, True)]),
                  cap(v("2:10", to="and said,"), "left: 8px; top: 8px", size=10, maxw=320)
                  + balloon(v("2:10", frm="Because"), "right: 10px; top: 96px", 180, size=13, pad="16px 18px") + vref("EX 2:10", "right: 8px; bottom: 8px")),
              talk(A.MOSES_PRINCE, h[1], SAND, [("cap", v("2:11", to="their burdens:"))], w=W2, ref="EX 2:11"))
    r3 = cols(use(D[3][1], over=cap(v("2:11", frm="and he saw") + " " + v("2:12", to="no man,"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 2:11–12", "left: 8px; bottom: 8px")),
              use(D[3][2], over=cap(v("2:12", frm="he smote"), "left: 8px; bottom: 8px", size=11, maxw=220) + sfx("ドッ", "DOH!", "right: 16px; top: 20px", size=52, fill="#F3EFE6", stroke="#0D0D0F", rot=-8)))
    return page("Exodus 2:9–12 — I Drew Him Out of the Water", t, r1 + r2 + r3, START + 5)


@P("EXO-C01-P07-Fled", "7 · Who Made Thee a Prince and a Judge?")
def p07():
    t, h = rows(320, 300, None)
    arm = [(-22, -158), (4, -150), (30, -160)]
    r1 = new(SAND, W1, h[0], defs("x17a", *ALL) + T.stage("x17a", W1, h[0], 171, "sand", [(A.moses_prince, 0.24, 0.4), (A.hebrew("#5A3A22"), 0.58, 0.36, False, "raise"), (A.hebrew("#8A6A4A"), 0.68, 0.38, True, arm)]),
             cap(v("2:13", to="did the wrong,"), "right: 12px; top: 12px", size=11, maxw=420)
             + balloon(v("2:13", frm="Wherefore"), "left: 20px; top: 20px", 220, size=14, pad="16px 20px") + vref("EX 2:13", "right: 12px; bottom: 12px"))
    r2 = cols(use(D[3][3], over=cap(v("2:14", to="And he said,"), "left: 8px; top: 8px", size=10.5)
                  + balloon(v("2:14", frm="Who made", to="the Egyptian?"), "left: 10px; top: 44px", 200, size=12, pad="22px 18px") + vref("EX 2:14", "left: 8px; bottom: 8px")),
              talk(A.MOSES_PRINCE_AFRAID, h[1], RED, [("cap", v("2:14", frm="And Moses feared,", to="and said,")), ("say", v("2:14", frm="Surely"))], w=W2, size=13))
    r3 = cols(talk(A.PHARAOH, h[2], RED, [("cap", v("2:15", to="slay Moses."))], w=W2, ref="EX 2:15"),
              use(D[3][4], over=cap(v("2:15", frm="But Moses"), "left: 8px; top: 8px", size=10.5, maxw=320)))
    return page("Exodus 2:13–15 — Who Made Thee a Prince and a Judge?", t, r1 + r2 + r3, START + 6)


@P("EXO-C01-P08-Midian", "8 · The Priest of Midian")
def p08():
    t, h = rows(290, 240, 210, None)
    r1 = use(D[4][0], over=cap(v("2:16") + " " + v("2:17"), "left: 12px; top: 12px", size=10.5, maxw=440) + vref("EX 2:16–17", "right: 12px; bottom: 12px"))
    r2 = cols(talk(A.JETHRO, h[1], GOLDEN, [("cap", v("2:18", to="he said,")), ("say", v("2:18", frm="How is it"))], w=W2, ref="EX 2:18", size=12.5),
              talk(A.ZIPPORAH, h[1], GOLDEN, [("cap", v("2:19", to="And they said,")), ("say", v("2:19", frm="An Egyptian"))], w=W2, flip=True, ref="EX 2:19", size=12))
    r3 = talk(A.JETHRO, h[2], EMBER, [("cap", v("2:20", to="unto his daughters,")), ("say", v("2:20", frm="And where"))], ref="EX 2:20", size=14)
    r4 = cols(use(D[4][1], over=cap(v("2:21"), "right: 8px; bottom: 8px", size=10.5, maxw=200) + vref("EX 2:21", "left: 8px; top: 8px")),
              use(D[4][2], over=cap(v("2:22", to="for he said,"), "left: 8px; top: 8px", size=10, maxw=200)
                  + balloon(v("2:22", frm="I have been"), "left: 10px; bottom: 14px", 190, size=12, pad="16px 16px") + vref("EX 2:22", "right: 8px; bottom: 8px")))
    return page("Exodus 2:16–22 — The Priest of Midian", t, r1 + r2 + r3 + r4, START + 7)


@P("EXO-C01-P09-Horeb", "9 · The Bush Was Not Consumed")
def p09():
    t, h = rows(300, 220, None)
    r1 = use(D[4][3], over=cap(v("2:23"), "left: 12px; top: 12px", size=10.5, maxw=440) + cap(v("2:24") + " " + v("2:25"), "right: 12px; bottom: 14px", size=10.5, maxw=300) + vref("EX 2:23–25", "left: 12px; bottom: 12px"))
    r2 = use(D[5][0], over=cap(v("3:1"), "left: 12px; top: 12px", size=10.5, maxw=430) + mk.stamp(3, "right: 14px; top: 12px") + vref("EX 3:1", "right: 12px; bottom: 12px"))
    r3 = use(D[5][1], over=cap(v("3:2"), "left: 12px; top: 12px", size=11, maxw=500) + cap(v("3:3", to="said,"), "left: 12px; top: 100px", size=11)
             + balloon(v("3:3", frm="I will turn"), "left: 12px; top: 136px", 230, size=13, pad="14px 18px")
             + sfx("ゴオオオ", "GOOOO", "right: 20px; top: 90px", size=48, fill="#FFD23F", stroke="#D7261E", rot=-6) + vref("EX 3:2–3", "right: 12px; bottom: 12px"))
    return page("Exodus 2:23–3:3 — The Bush Was Not Consumed", t, r1 + r2 + r3, START + 8)


@P("EXO-C01-P10-HolyGround", "10 · Holy Ground")
def p10():
    t, h = rows(290, 300, None)
    r1 = cols(use(D[5][2], over=cap(v("3:4", to="and said,"), "left: 8px; top: 8px", size=10, maxw=320) + god(v("3:4", frm="Moses, Moses.", to="Moses."), "right: 10px; top: 96px", size=18)
                  + cap(v("3:4", frm="And he said,", to="said,"), "right: 10px; top: 160px", size=10) + balloon(v("3:4", frm="Here am I."), "right: 20px; top: 194px", 130, size=13, pad="12px 12px") + vref("EX 3:4", "left: 8px; bottom: 8px")),
              use(D[5][3], over=cap(v("3:5", to="And he said,"), "left: 8px; top: 8px", size=10) + god(v("3:5", frm="Draw not"), "left: 8px; top: 44px", size=14, maxw=320) + vref("EX 3:5", "right: 8px; bottom: 8px")))
    r2 = use(D[6][0], over=cap(v("3:6", to="Moreover he said,"), "right: 12px; top: 12px", size=10.5) + god(v("3:6", frm="I am the God", to="God of Jacob."), "right: 12px; top: 48px", size=17, maxw=340)
             + cap(v("3:6", frm="And Moses hid"), "left: 12px; top: 12px", size=10.5, maxw=260) + vref("EX 3:6", "right: 12px; bottom: 12px"))
    r3 = new(HOT, W1, h[2], defs("x110c", *ALL) + A.bricks("x110c", W1, h[2], 1103),
             cap(v("3:7", to="And Jehovah said,"), "left: 12px; top: 12px", size=11) + god(v("3:7", frm="I have surely"), "left: 12px; top: 48px", size=19, maxw=560) + vref("EX 3:7", "right: 12px; bottom: 12px"))
    return page("Exodus 3:4–7 — Holy Ground", t, r1 + r2 + r3, START + 9)


@P("EXO-C01-P11-MilkHoney", "11 · A Land Flowing with Milk and Honey")
def p11():
    t, h = rows(330, 260, None)
    r1 = new(SKY, W1, h[0], A.milk_honey(None, W1, h[0], 1111), god(v("3:8", to="milk and honey;"), "left: 12px; top: 12px", size=17, maxw=560) + vref("EX 3:8", "right: 12px; bottom: 12px"))
    r2 = new("#0B1A2E", W1, h[1], A.peoples_map(W1, h[1], 1112), god(v("3:8", frm="unto the place"), "right: 12px; top: 12px", size=14, maxw=200) + vref("EX 3:8", "left: 12px; top: 12px"))
    r3 = bush_panel(W1, h[2], 1113, god(v("3:9") + " " + v("3:10"), "left: 12px; top: 12px", size=18, maxw=360) + vref("EX 3:9–10", "right: 12px; bottom: 12px"), cx=0.76, size=0.9)
    return page("Exodus 3:8–10 — A Land Flowing with Milk and Honey", t, r1 + r2 + r3, START + 10)


@P("EXO-C01-P12-IAM", "12 · I AM THAT I AM")
def p12():
    t, h = rows(290, 220, None)
    r1 = cols(use(D[6][2], over=cap(v("3:11", to="unto God,"), "left: 8px; top: 8px", size=10.5) + balloon(v("3:11", frm="Who am I"), "left: 10px; top: 44px", 200, size=12, pad="24px 18px") + vref("EX 3:11", "left: 8px; bottom: 8px")),
              use(D[6][1], over=cap(v("3:12", to="And he said,"), "left: 8px; top: 8px", size=10.5) + god(v("3:12", frm="Certainly"), "left: 8px; top: 44px", size=14, maxw=320) + vref("EX 3:12", "right: 8px; bottom: 8px")))
    r2 = talk(A.MOSES_FIRE, h[1], FIRE, [("cap", v("3:13", to="unto God,")), ("say", v("3:13", frm="Behold,"))], ref="EX 3:13", size=13.5)
    r3 = use(D[6][3], over=cap(v("3:14", to="unto Moses,"), "left: 12px; top: 12px", size=11)
             + god(v("3:14", frm="I AM THAT", to="THAT I AM"), "left: 50%; top: 130px; transform: translateX(-50%); white-space: nowrap", size=54)
             + cap(v("3:14", frm="and he said,", to="and he said,"), "left: 12px; bottom: 96px", size=11)
             + god(v("3:14", frm="Thus shalt"), "left: 12px; bottom: 14px", size=17, maxw=520) + vref("EX 3:14", "right: 12px; bottom: 12px"))
    return page("Exodus 3:11–14 — I AM THAT I AM", t, r1 + r2 + r3, START + 11)


@P("EXO-C01-P13-Name", "13 · This Is My Name for Ever")
def p13():
    t, h = rows(290, 340, None)
    r1 = bush_panel(W1, h[0], 1131, cap(v("3:15", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(v("3:15", frm="Thus shalt"), "left: 12px; top: 48px", size=16, maxw=430) + vref("EX 3:15", "right: 12px; bottom: 12px"), cx=0.82, size=0.8)
    r2 = new(SAND, W1, h[1], defs("x113b", *ALL) + A.elders("x113b", W1, h[1], 1132),
             god(v("3:16"), "left: 12px; top: 12px", size=15, maxw=640) + vref("EX 3:16", "right: 12px; bottom: 12px"))
    r3 = new("#0B1A2E", W1, h[2], A.exodus_map(W1, h[2], ["GOSHEN", "THE WILDERNESS", "CANAAN"], cur="CANAAN"),
             god(v("3:17"), "left: 12px; bottom: 12px", size=14, maxw=330) + vref("EX 3:17", "right: 12px; top: 12px"))
    return page("Exodus 3:15–17 — This Is My Name for Ever", t, r1 + r2 + r3, START + 12)


@P("EXO-C01-P14-Despoil", "14 · Ye Shall Not Go Empty")
def p14():
    t, h = rows(330, 280, None)
    r1 = new(COURT, W1, h[0], defs("x114a", *ALL) + T.stage("x114a", W1, h[0], 1141, "palace", [(A.pharaoh, 0.8, 0.48, True)] + [(A.elder(c, i), 0.08 + i * 0.07, 0.56) for i, c in enumerate(A.HEBREW[:5])] + [(A.moses, 0.48, 0.52, False, "staff")]),
             god(v("3:18"), "left: 12px; top: 12px", size=14, maxw=640) + vref("EX 3:18", "right: 12px; bottom: 12px"))
    r2 = cols(new(NIGHT, W2, h[1], A.wonders(W2, h[1], 1142), god(v("3:19") + " " + v("3:20"), "left: 8px; top: 8px", size=13.5, maxw=320) + vref("EX 3:19–20", "right: 8px; bottom: 8px")),
              new(SAND, W2, h[1], defs("x114c", *ALL) + T.stage("x114c", W2, h[1], 1143, "egypt", [(("woman", "#5A6E8A"), 0.3, 0.5), (("egypt", "#F3EFE6"), 0.62, 0.5, True)]),
                  god(v("3:21"), "left: 8px; top: 8px", size=13.5, maxw=320) + vref("EX 3:21", "right: 8px; bottom: 8px")))
    r3 = new(EMBER, W1, h[2], A.jewels(W1, h[2], 1144), god(v("3:22"), "left: 12px; top: 12px", size=15, maxw=640) + vref("EX 3:22", "right: 12px; bottom: 12px"))
    return page("Exodus 3:18–22 — Ye Shall Not Go Empty", t, r1 + r2 + r3, START + 13)


@P("EXO-C01-P15-Rod", "15 · What Is That in Thy Hand?")
def p15():
    t, h = rows(220, 260, None)
    r1 = talk(A.MOSES_AFRAID, h[0], FIRE, [("cap", v("4:1", to="and said,")), ("say", v("4:1", frm="But, behold,"))], ref="EX 4:1", size=13.5, extra=mk.stamp(4, "right: 14px; bottom: 12px"))
    r2 = use(D[7][0], over=cap(v("4:2", to="unto him,"), "right: 12px; top: 12px", size=10.5) + god(v("4:2", frm="What is", to="thy hand?"), "right: 12px; top: 46px", size=20)
             + cap(v("4:2", frm="And he said,", to="said,"), "left: 330px; top: 110px", size=10.5) + balloon(v("4:2", frm="A rod."), "left: 330px; top: 144px", 110, size=15, pad="10px 12px")
             + cap(v("4:3", to="And he said,"), "right: 12px; top: 110px", size=10.5) + god(v("4:3", frm="Cast it", to="ground."), "right: 12px; top: 146px", size=18) + vref("EX 4:2–3", "right: 12px; bottom: 12px"))
    r3 = use(D[7][1], over=cap(v("4:3", frm="And he cast"), "left: 12px; top: 12px", size=11, maxw=360)
             + cap(v("4:4", to="unto Moses,"), "left: 12px; top: 90px", size=10.5) + god(v("4:4", frm="Put forth", to="by the tail:"), "left: 12px; top: 126px", size=16, maxw=300)
             + cap(v("4:4", frm="(and he put"), "right: 12px; bottom: 120px", size=10.5, maxw=260) + god(v("4:5"), "right: 12px; bottom: 14px", size=13, maxw=420)
             + sfx("シャーッ", "SHAAA!", "right: 30px; top: 16px", size=40, fill="#9CCB5E", stroke="#0D0D0F", rot=-8) + vref("EX 4:3–5", "left: 12px; bottom: 12px"))
    return page("Exodus 4:1–5 — What Is That in Thy Hand?", t, r1 + r2 + r3, START + 14)


@P("EXO-C01-P16-Hand", "16 · As White as Snow")
def p16():
    t, h = rows(330, 230, None)
    r1 = cols(use(D[7][2], over=cap(v("4:6", to="unto him,"), "left: 8px; top: 8px", size=10) + god(v("4:6", frm="Put now", to="thy bosom."), "left: 8px; top: 40px", size=14, maxw=200)
                  + cap(v("4:6", frm="And he put"), "right: 8px; bottom: 8px", size=10, maxw=200) + vref("EX 4:6", "left: 8px; bottom: 8px")),
              new(FIRE, W2, h[0], E.hand(W2 * 0.5, h[0] * 0.62, 1.6, uid="x116a"),
                  cap(v("4:7", to="And he said,"), "left: 8px; top: 8px", size=10) + god(v("4:7", frm="Put thy hand", to="again."), "left: 8px; top: 40px", size=14, maxw=220)
                  + cap(v("4:7", frm="(And he put"), "right: 8px; bottom: 8px", size=10, maxw=210) + vref("EX 4:7", "left: 8px; bottom: 8px")))
    r2 = bush_panel(W1, h[1], 1162, god(v("4:8"), "left: 12px; top: 12px", size=17, maxw=460) + vref("EX 4:8", "right: 12px; bottom: 12px"), cx=0.84, size=0.8)
    r3 = new(SKY, W1, h[2], defs("x116c", *ALL) + A.blood_ground("x116c", W1, h[2], 1163), god(v("4:9"), "right: 12px; top: 12px", size=15, maxw=330) + vref("EX 4:9", "left: 12px; bottom: 12px"))
    return page("Exodus 4:6–9 — As White as Snow", t, r1 + r2 + r3, START + 15)


@P("EXO-C01-P17-Mouth", "17 · Who Hath Made Man's Mouth?")
def p17():
    t, h = rows(250, 250, None)
    r1 = talk(A.MOSES_OLD_PLEA, h[0], BLUE, [("cap", v("4:10", to="unto Jehovah,")), ("say", v("4:10", frm="Oh, Lord,"))], ref="EX 4:10", size=14)
    r2 = bush_panel(W1, h[1], 1172, cap(v("4:11", to="unto him,"), "left: 12px; top: 12px", size=11) + god(v("4:11", frm="Who hath") + " " + v("4:12"), "left: 12px; top: 48px", size=16, maxw=470) + vref("EX 4:11–12", "right: 12px; bottom: 12px"), cx=0.84, size=0.8)
    r3 = cols(talk(A.MOSES_OLD_PLEA, h[2], BLUE, [("cap", v("4:13", to="And he said,")), ("say", v("4:13", frm="Oh, Lord,"))], w=W2, ref="EX 4:13", size=13.5),
              new(FIRE, W2, h[2], A.burning(W2, h[2], 1173, cx=0.7, size=0.9, sky=False),
                  cap(v("4:14", to="and he said,"), "left: 8px; top: 8px", size=10, maxw=320) + god(v("4:14", frm="Is there not"), "left: 8px; top: 62px", size=12.5, maxw=320) + vref("EX 4:14", "right: 8px; bottom: 8px")))
    return page("Exodus 4:10–14 — Who Hath Made Man's Mouth?", t, r1 + r2 + r3, START + 16)


@P("EXO-C01-P18-GoInPeace", "18 · Go in Peace")
def p18():
    t, h = rows(300, 220, None)
    r1 = new(NIGHT, W1, h[0], X.cosmic(W1, h[0]) + face(A.AARON_FIRE, W1 + 40, h[0] - 330, 0.86, flip=True),
             god(v("4:15") + " " + v("4:16") + " " + v("4:17"), "left: 12px; top: 12px", size=16, maxw=420) + vref("EX 4:15–17", "left: 12px; bottom: 12px"))
    r2 = cols(talk(A.MOSES, h[1], GOLDEN, [("cap", v("4:18", to="said unto him,")), ("say", v("4:18", frm="Let me go", to="yet alive."))], w=W2, ref="EX 4:18", size=12),
              talk(A.JETHRO, h[1], GOLDEN, [("cap", v("4:18", frm="And Jethro", to="to Moses,")), ("say", v("4:18", frm="Go in peace."))], w=W2, flip=True, size=14))
    r3 = new(SAND, W1, h[2], defs("x118c", *ALL) + A.journey("x118c", W1, h[2], 1183),
             cap(v("4:19", to="in Midian,"), "left: 12px; top: 12px", size=10.5) + god(v("4:19", frm="Go, return"), "left: 12px; top: 46px", size=15, maxw=330)
             + cap(v("4:20"), "right: 12px; top: 12px", size=10.5, maxw=300) + vref("EX 4:19–20", "right: 12px; bottom: 12px"))
    return page("Exodus 4:15–20 — Go in Peace", t, r1 + r2 + r3, START + 17)


@P("EXO-C01-P19-FirstBorn", "19 · Israel Is My Son, My First-Born")
def p19():
    t, h = rows(380, None)
    r1 = new(NIGHT, W1, h[0], X.cosmic(W1, h[0]) + Y.ground(W1, h[0], h[0] * 0.86, "#1A1430", dy=0) + A.EG.pyramid(W1 * 0.7, h[0] * 0.86, W1 * 0.4, h[0] * 0.42) + A.EG.pyramid(W1 * 0.92, h[0] * 0.86, W1 * 0.24, h[0] * 0.26),
             cap(v("4:21", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(v("4:21", frm="When thou"), "left: 12px; top: 48px", size=15, maxw=380)
             + cap(v("4:22", to="unto Pharaoh,"), "left: 12px; top: 200px", size=10.5) + god(v("4:22", frm="Thus saith") + " " + v("4:23"), "left: 12px; bottom: 14px", size=15, maxw=560) + vref("EX 4:21–23", "right: 12px; bottom: 12px"))
    r2 = cols(new(NIGHT, W2, h[1], A.lodging(W2, h[1], 1192), cap(v("4:24"), "left: 8px; top: 8px", size=11, maxw=300) + vref("EX 4:24", "right: 8px; bottom: 8px")),
              talk(A.ZIPPORAH_NIGHT, h[1], NIGHT, [("cap", v("4:25", to="and she said,")), ("say", v("4:25", frm="Surely")), ("cap", v("4:26", to="she said,")), ("say", v("4:26", frm="A bridegroom"))],
                   w=W2, flip=True, ref="EX 4:25–26", size=12.5))
    return page("Exodus 4:21–26 — Israel Is My Son, My First-Born", t, r1 + r2, START + 18)


@P("EXO-C01-P20-Believed", "20 · The People Believed")
def p20():
    t, h = rows(320, 270, None)
    r1 = new(SKY, W1, h[0], defs("x120a", *ALL) + A.meeting("x120a", W1, h[0], 1201),
             cap(v("4:27", to="said to Aaron,"), "left: 12px; top: 12px", size=11) + god(v("4:27", frm="Go into", to="meet Moses."), "left: 12px; top: 48px", size=16, maxw=280)
             + cap(v("4:27", frm="And he went,"), "right: 12px; top: 12px", size=11, maxw=240) + vref("EX 4:27", "right: 12px; bottom: 12px"))
    r2 = cols(talk(A.AARON, h[1], GOLDEN, [("cap", v("4:28"))], w=W2, ref="EX 4:28"),
              new(SAND, W2, h[1], defs("x120b", *ALL) + A.elders("x120b", W2, h[1], 1202, extra_cast=[(A.aaron, 0.86, 0.44, True), (A.moses, 0.94, 0.44, True)]),
                  cap(v("4:29"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("EX 4:29", "right: 8px; bottom: 8px")))
    r3 = new(GOLDEN, W1, h[2], defs("x120c", *ALL) + A.elders("x120c", W1, h[2], 1203, bow=True, extra_cast=[(A.aaron, 0.44, 0.5, False, "raise"), (A.moses, 0.54, 0.5, True, "staff")]),
             cap(v("4:30"), "left: 12px; top: 12px", size=11, maxw=420) + cap(v("4:31"), "right: 12px; top: 76px", size=11, maxw=300)
             + end_mark("NEXT · LET MY PEOPLE GO", "left: 12px; bottom: 12px") + vref("EX 4:30–31", "right: 12px; bottom: 12px"))
    return page("Exodus 4:27–31 — The People Believed", t, r1 + r2 + r3, START + 19)
