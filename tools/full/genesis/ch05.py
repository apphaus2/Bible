"""Genesis volume, Chapter 5 — The Son of Promise (Genesis 20–23). Every verse, word for word from ref/eng-asv.
22:20–24 (the house of Nahor) is set as scroll cells. The binding of Isaac (22:9–10) is drawn as a silhouette on the
summit and the raised hand against the sky; the angel of Jehovah speaks from heaven in the Voice box."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from genesis import G, art as X, art2 as Y, art3 as Z, art4 as Q, art5 as K
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import clan, hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from mk import defs, face

v, sp = G.v, G.span
B3 = "reference/genesis/book-03/"
Mor, Prov = (panels(B3 + n + ".dc.html") for n in ["B3-P07-Moriah", "B3-P08-Provide"])
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
PALACE = "linear-gradient(180deg, #8FD0E2 0%, #FFE3B8 100%)"
WARM = "radial-gradient(circle at 70% 30%, #FFE680 0 20px, #C8885A 180px, #3A2214 400px)"
KING = "radial-gradient(circle at 70% 30%, #FFE680 0 20px, #5A8AC8 180px, #12305A 420px)"
START = 87                                   # chapter 4 ends on page 86
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def cosmic(w, h, cx=None): return X.cosmic(w, h, cx)


@P("GEN-C05-00-Title", "Chapter 5 · The Son of Promise")
def title():
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#0B0B2A"></rect>' + mk.stars(320, 760, 760, 51) + mk.stars(60, 760, 600, 52, color="#FFE680")
           + Z.sun(380, 900, 150, color="#FFC14D", glow="#FFF4C2", op=0.25)
           + '<path d="M-10 1090 L -10 860 L 300 700 L 420 680 L 770 880 L 770 1090 Z" fill="#2A140C" stroke="#0D0D0F" stroke-width="3"></path>'
           + '<path d="M0 1090 L 0 1000 C 200 980 560 980 760 1000 L 760 1090 Z" fill="#C8A06A"></path>')
    return chapter_title(5, "第五話", "The Son of Promise", "Genesis 20 – 23", svg, NIGHT,
                         v("22:8", to="my son:"), "Genesis · Volume One")


@P("GEN-C05-P01-Gerar", "87 · She Is My Sister")
def p01():
    t, h = rows(190, 210, 230, None)
    r1 = new(SAND, W1, h[0], K.gerar(None, W1, h[0], 511),
             cap(v("20:1"), "left: 12px; top: 12px", size=11.5, maxw=420) + vref("GEN 20:1", "left: 12px; bottom: 10px"))
    r2 = new(SAND, W1, h[1], defs("c52b", *ALL) + K.taken("c52b", W1, h[1], 512),
             cap(v("20:2", to="his wife,"), "left: 12px; top: 12px", size=10.5)
             + balloon(v("20:2", frm="She is", to="sister:"), "left: 12px; top: 46px", 170, size=13, pad="14px 18px")
             + cap(v("20:2", frm="and Abimelech"), "right: 12px; top: 12px", size=11, maxw=300) + vref("GEN 20:2", "right: 12px; bottom: 10px"))
    r3 = new("#0B0B2A", W1, h[2], defs("c52c", *ALL) + K.dreamer("c52c", W1, h[2], 513),
             cap(v("20:3", to="said to him,"), "left: 12px; top: 12px", size=10.5, maxw=300)
             + god(v("20:3", frm="Behold"), "right: 12px; top: 12px", size=14.5, maxw=340) + vref("GEN 20:3", "left: 12px; bottom: 12px"))
    r4 = new(KING, W1, h[3], fc(K.ABIMELECH_AFRAID, h[3], w=W1),
             cap(v("20:4", to="and he said,"), "left: 320px; top: 12px", size=10.5, maxw=360)
             + balloon(v("20:4", frm="Lord,"), "left: 300px; top: 66px", 260, size=12.5, pad="18px 22px")
             + balloon(v("20:5"), "right: 12px; bottom: 12px", 380, size=12, pad="26px 36px") + vref("GEN 20:4–5", "left: 12px; bottom: 12px"))
    return page("Genesis 20:1–5 — She Is My Sister", t, r1 + r2 + r3 + r4, START + 0)


@P("GEN-C05-P02-Dream", "88 · Restore the Man's Wife")
def p02():
    t, h = rows(330, 210, None)
    r1 = new(NIGHT, W1, h[0], cosmic(W1, h[0]),
             cap(v("20:6", to="in the dream,"), "left: 12px; top: 12px", size=10.5)
             + god(v("20:6", frm="Yea") + " " + v("20:7"), "left: 12px; top: 46px", size=15, maxw=660) + vref("GEN 20:6–7"))
    r2 = new(PALACE, W1, h[1], defs("c52b2", *ALL) + K.servants_afraid("c52b2", W1, h[1], 522),
             cap(v("20:8"), "right: 12px; top: 12px", size=11, maxw=400) + vref("GEN 20:8", "left: 12px; bottom: 10px"))
    r3 = new(EMBER, W1, h[2], fc(K.ABIMELECH_STERN, h[2], w=W1),
             cap(v("20:9", to="said unto him,"), "left: 320px; top: 12px", size=10.5)
             + balloon(v("20:9", frm="What hast"), "left: 290px; top: 46px", 390, size=13, pad="30px 40px") + vref("GEN 20:9", "left: 12px; bottom: 12px"))
    return page("Genesis 20:6–9 — Restore the Man's Wife", t, r1 + r2 + r3, START + 1)


@P("GEN-C05-P03-Sister", "89 · She Is Indeed My Sister")
def p03():
    t, h = rows(300, None)
    r1 = cols(new(EMBER, W2, h[0], fc(K.ABIMELECH_STERN, h[0]),
                  cap(v("20:10", to="unto Abraham,"), "right: 8px; top: 8px", size=10, maxw=200)
                  + balloon(v("20:10", frm="What sawest"), "right: 8px; top: 64px", 190, size=12.5, pad="20px 18px") + vref("GEN 20:10", "left: 8px; bottom: 8px")),
              new(WARM, W2, h[0], fc(K.ABRAHAM_GRAVE, h[0]),
                  cap(v("20:11", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("20:11", frm="Because"), "right: 8px; top: 44px", 200, size=12, pad="22px 20px") + vref("GEN 20:11", "left: 8px; bottom: 8px")))
    r2 = new("linear-gradient(90deg, #2C4A7A 0%, #C8885A 55%, #8A3A5A 100%)", W1, h[1],
             fc(K.ABRAHAM, h[1], w=W1) + fc(Q.SARAH, h[1], w=W1, flip=True),
             balloon(v("20:12"), "left: 220px; top: 16px", 300, size=12.5, pad="24px 30px")
             + balloon(v("20:13"), "left: 200px; top: 170px", 340, size=12, pad="30px 38px") + vref("GEN 20:12–13", "left: 12px; top: 12px"))
    return page("Genesis 20:10–13 — She Is Indeed My Sister", t, r1 + r2, START + 2)


@P("GEN-C05-P04-Healed", "90 · God Healed Abimelech")
def p04():
    t, h = rows(230, 280, None)
    r1 = new(SAND, W1, h[0], defs("c54a", *ALL) + K.restored("c54a", W1, h[0], 541),
             cap(v("20:14"), "left: 12px; top: 12px", size=11, maxw=420) + vref("GEN 20:14", "right: 12px; top: 12px"))
    r2 = cols(new(KING, W2, h[1], fc(K.ABIMELECH, h[1]),
                  cap(v("20:15", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("20:15", frm="Behold"), "right: 8px; top: 44px", 180, size=12, pad="20px 18px") + vref("GEN 20:15", "left: 8px; bottom: 8px")),
              new("#12113A", W2, h[1], K.silver(W2, h[1], 542),
                  cap(v("20:16", to="he said,"), "left: 8px; top: 8px", size=10)
                  + balloon(v("20:16", frm="Behold, I"), "left: 8px; top: 40px", 320, size=11.5, pad="22px 28px")
                  + hud("1000", "right: 10px; bottom: 10px", size=26) + vref("GEN 20:16", "left: 8px; bottom: 8px")))
    r3 = cols(new(PALACE, W2, h[2], K.prayer(None, W2, h[2], 543),
                  cap(v("20:17"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 20:17", "right: 8px; bottom: 8px")),
              new(SAND, W2, h[2], defs("c54d", *ALL) + K.mothers("c54d", W2, h[2], 544),
                  cap(v("20:18"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 20:18", "right: 8px; bottom: 8px")))
    return page("Genesis 20:14–18 — God Healed Abimelech", t, r1 + r2 + r3, START + 3)


@P("GEN-C05-P05-Isaac", "91 · God Hath Made Me to Laugh")
def p05():
    t, h = rows(280, 240, None)
    r1 = new("radial-gradient(circle at 30% 40%, #FFF4C2 0 30px, #FFC14D 160px, #FF8A3D 400px)", W1, h[0], Y.mother_and_child(W1, h[0], tok=K.SARAH_JOY, baby_xy=(300, 230)),
             cap(v("21:1"), "right: 12px; top: 12px", size=11, maxw=330)
             + cap(v("21:2"), "right: 12px; top: 84px", size=11, maxw=330) + vref("GEN 21:1–2", "left: 12px; bottom: 12px"))
    r2 = cols(new("#2A1A2E", W2, h[1], K.eighth_day(W2, h[1], 552),
                  cap(v("21:3"), "left: 8px; top: 8px", size=10, maxw=320)
                  + cap(v("21:4"), "left: 8px; bottom: 8px", size=10, maxw=320) + vref("GEN 21:3–4", "right: 8px; top: 84px")),
              new(GLOW, W2, h[1], fc(K.ABRAHAM_AWE, h[1]),
                  cap(v("21:5"), "right: 8px; top: 8px", size=11, maxw=180) + hud("100", "right: 10px; bottom: 10px", size=30)))
    r3 = new(GLOW, W1, h[2], fc(K.SARAH_JOY, h[2], w=W1),
             cap(v("21:6", to="said,"), "left: 330px; top: 12px", size=10.5)
             + balloon(v("21:6", frm="God hath"), "left: 310px; top: 46px", 320, size=13.5, pad="22px 30px")
             + cap(v("21:7", to="she said,"), "right: 12px; top: 150px", size=10.5)
             + balloon(v("21:7", frm="Who would"), "right: 12px; top: 186px", 330, size=12.5, pad="24px 30px") + vref("GEN 21:6–7", "left: 12px; bottom: 12px"))
    return page("Genesis 21:1–7 — God Hath Made Me to Laugh", t, r1 + r2 + r3, START + 4)


@P("GEN-C05-P06-CastOut", "92 · Cast Out This Handmaid")
def p06():
    t, h = rows(220, 290, None)
    r1 = new(TENT, W1, h[0], defs("c56a", *ALL) + K.weaning_feast("c56a", W1, h[0], 561),
             cap(v("21:8"), "left: 12px; top: 12px", size=11, maxw=420) + vref("GEN 21:8", "right: 12px; top: 12px"))
    r2 = cols(new(TENT, W2, h[1], defs("c56b", *ALL) + K.mocking("c56b", W2, h[1], 562),
                  cap(v("21:9"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 21:9", "right: 8px; bottom: 8px")),
              new(EMBER, W2, h[1], fc(K.SARAH_STERN, h[1]),
                  cap(v("21:10", to="unto Abraham,"), "right: 8px; top: 8px", size=10, maxw=200)
                  + balloon(v("21:10", frm="Cast out"), "right: 8px; top: 64px", 210, size=11.5, pad="22px 22px") + vref("GEN 21:10", "left: 8px; bottom: 8px")))
    r3 = cols(new(WARM, W2, h[2], fc(K.ABRAHAM_GRAVE, h[2]),
                  cap(v("21:11"), "right: 8px; top: 8px", size=11, maxw=200) + vref("GEN 21:11", "left: 8px; bottom: 8px")),
              new(NIGHT, W2, h[2], cosmic(W2, h[2]),
                  cap(v("21:12", to="unto Abraham,"), "left: 8px; top: 8px", size=10)
                  + god(v("21:12", frm="Let it not") + " " + v("21:13"), "left: 8px; top: 40px", size=12.5, maxw=320) + vref("GEN 21:12–13", "right: 8px; bottom: 8px")))
    return page("Genesis 21:8–13 — Cast Out This Handmaid", t, r1 + r2 + r3, START + 5)


@P("GEN-C05-P07-Bowshot", "93 · As It Were a Bowshot")
def p07():
    t, h = rows(290, 250, None)
    r1 = new(DAWN, W1, h[0], defs("c57a", *ALL) + K.sent_away("c57a", W1, h[0], 571),
             cap(v("21:14"), "right: 12px; top: 12px", size=11, maxw=380) + vref("GEN 21:14", "left: 12px; bottom: 12px"))
    r2 = new(HOT, W1, h[1], defs("c57b", *ALL) + K.bowshot("c57b", W1, h[1], 572),
             cap(v("21:15"), "left: 12px; top: 12px", size=12, maxw=420) + vref("GEN 21:15", "right: 12px; top: 12px"))
    r3 = new("radial-gradient(circle at 70% 30%, #CFEFFF 0 20px, #5A8AAA 180px, #12305A 400px)", W1, h[2], fc(K.HAGAR_WEEP, h[2], w=W1),
             cap(v("21:16", to="bowshot:"), "left: 330px; top: 12px", size=10.5, maxw=350)
             + cap(v("21:16", frm="for she said,", to="said,"), "left: 330px; top: 84px", size=10.5)
             + balloon(v("21:16", frm="Let me not", to="the child."), "left: 320px; top: 118px", 260, size=14, pad="20px 26px")
             + cap(v("21:16", frm="And she sat"), "right: 12px; bottom: 14px", size=11, maxw=340)
             + sfx("ううっ", "UU", "left: 250px; bottom: 80px", size=34, fill="#CFEFFF", stroke="#12305A", rot=-6) + vref("GEN 21:16", "left: 12px; bottom: 12px"))
    return page("Genesis 21:14–16 — As It Were a Bowshot", t, r1 + r2 + r3, START + 6)


@P("GEN-C05-P08-Archer", "94 · God Heard the Voice of the Lad")
def p08():
    t, h = rows(250, 270, None)
    r1 = new(NIGHT, W1, h[0], cosmic(W1, h[0]),
             cap(v("21:17", to="said unto her,"), "left: 12px; top: 12px", size=10.5, maxw=660)
             + god(v("21:17", frm="What aileth") + " " + v("21:18"), "left: 12px; top: 64px", size=15, maxw=660) + vref("GEN 21:17–18"))
    r2 = new(HOT, W1, h[1], defs("c58b", *ALL) + K.well_opened("c58b", W1, h[1], 582),
             cap(v("21:19"), "left: 12px; top: 12px", size=11.5, maxw=400) + vref("GEN 21:19", "right: 12px; top: 12px"))
    r3 = new(DUSK, W1, h[2], defs("c58c", *ALL) + K.archer("c58c", W1, h[2], 583),
             cap(v("21:20"), "right: 12px; top: 12px", size=11, maxw=340)
             + cap(v("21:21"), "right: 12px; top: 96px", size=11, maxw=340) + vref("GEN 21:20–21", "left: 12px; bottom: 12px"))
    return page("Genesis 21:17–21 — God Heard the Voice of the Lad", t, r1 + r2 + r3, START + 7)


@P("GEN-C05-P09-Oath", "95 · Swear unto Me Here by God")
def p09():
    t, h = rows(220, 250, 260, None)
    r1 = new(SAND, W1, h[0], defs("c59a", *ALL) + K.oath("c59a", W1, h[0], 591),
             cap(v("21:22", to="saying,"), "left: 12px; top: 12px", size=10.5, maxw=420)
             + balloon(v("21:22", frm="God is with"), "left: 230px; top: 64px", 240, size=12, pad="16px 20px") + vref("GEN 21:22", "right: 12px; top: 12px"))
    r2 = new(KING, W1, h[1], fc(K.ABIMELECH, h[1], w=W1),
             balloon(v("21:23"), "left: 270px; top: 14px", 410, size=12, pad="30px 40px") + vref("GEN 21:23", "left: 12px; bottom: 12px"))
    r3 = cols(new(WARM, W2, h[2], fc(K.ABRAHAM, h[2]),
                  cap(v("21:24", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("21:24", frm="I will"), "right: 8px; top: 40px", 150, size=14, pad="14px 14px")
                  + cap(v("21:25"), "right: 8px; bottom: 8px", size=10, maxw=210) + vref("GEN 21:24–25", "left: 8px; top: 8px")),
              new(KING, W2, h[2], fc(K.ABIMELECH_AFRAID, h[2]),
                  cap(v("21:26", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("21:26", frm="I know not"), "right: 8px; top: 40px", 200, size=12, pad="22px 20px") + vref("GEN 21:26", "left: 8px; bottom: 8px")))
    r4 = new(SAND, W1, h[3], defs("c59d", *ALL) + K.oath("c59d", W1, h[3], 594) + Z.flock(W1 * 0.3, W1 * 0.64, h[3] * 0.84, h[3] * 0.98, 7, 594, cows=0.5, smin=0.2, smax=0.3),
             cap(v("21:27"), "left: 12px; top: 12px", size=11.5, maxw=460) + vref("GEN 21:27", "right: 12px; top: 12px"))
    return page("Genesis 21:22–27 — Swear unto Me Here by God", t, r1 + r2 + r3 + r4, START + 8)


@P("GEN-C05-P10-Beersheba", "96 · The Everlasting God")
def p10():
    t, h = rows(200, 260, 300, None)
    r1 = new(GREEN, W1, h[0], K.seven_lambs(None, W1, h[0], 5101),
             cap(v("21:28"), "left: 12px; top: 12px", size=11.5, maxw=400) + vref("GEN 21:28", "right: 12px; top: 12px"))
    r2 = cols(new(KING, W2, h[1], fc(K.ABIMELECH, h[1]),
                  cap(v("21:29", to="unto Abraham,"), "right: 8px; top: 8px", size=10, maxw=200)
                  + balloon(v("21:29", frm="What mean"), "right: 8px; top: 64px", 200, size=12, pad="20px 20px") + vref("GEN 21:29", "left: 8px; bottom: 8px")),
              new(WARM, W2, h[1], fc(K.ABRAHAM, h[1]),
                  cap(v("21:30", to="he said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("21:30", frm="These seven"), "right: 8px; top: 40px", 210, size=12, pad="22px 22px") + vref("GEN 21:30", "left: 8px; bottom: 8px")))
    r3 = new(SKY, W1, h[2], defs("c510c", *ALL) + K.beersheba("c510c", W1, h[2], 5103),
             cap(v("21:31"), "left: 12px; top: 12px", size=11, maxw=330)
             + cap(v("21:32"), "left: 12px; top: 84px", size=10.5, maxw=330)
             + cap(v("21:33"), "right: 12px; top: 12px", size=11, maxw=280) + vref("GEN 21:31–33", "right: 12px; bottom: 12px"))
    r4 = new(DUSK, W1, h[3], Y.hills(W1, h[3], h[3] * 0.7, 5104, color="#2A1A2E", amp=8) + Z.sun(W1 * 0.8, h[3] * 0.7, 20, color="#FF8A3D", op=0.25)
             + "".join(Z.E4.tent(W1 * x, h[3] * 0.72, W1 * 0.08, h[3] * 0.24, color="#2A1A14") for x in (0.2, 0.3, 0.38)),
             cap(v("21:34"), "left: 12px; top: 12px", size=12.5, maxw=420) + vref("GEN 21:34", "right: 12px; bottom: 10px"))
    return page("Genesis 21:28–34 — The Everlasting God", t, r1 + r2 + r3 + r4, START + 9)


@P("GEN-C05-P11-Moriah", "97 · Take Now Thy Son")
def p11():
    t, h = rows(290, 170, 250, None)
    r1 = use(Mor[0], over=cap(v("22:1", to="said unto him,"), "right: 12px; top: 12px", size=10.5, maxw=380)
             + god(v("22:1", frm="Abraham;", to="Abraham;"), "right: 12px; top: 84px", size=22, maxw=380)
             + cap(v("22:1", frm="and he said,", to="he said,"), "right: 160px; bottom: 60px", size=10.5)
             + balloon(v("22:1", frm="Here am I."), "right: 12px; bottom: 14px", 150, size=14, pad="14px 16px") + vref("GEN 22:1", "left: 12px; bottom: 12px"))
    r2 = new(NIGHT, W1, h[1], cosmic(W1, h[1]),
             cap(v("22:2", to="said,"), "left: 12px; top: 10px", size=10.5)
             + god(v("22:2", frm="Take now"), "left: 12px; top: 42px", size=14.5, maxw=660) + vref("GEN 22:2"))
    r3 = new(DAWN, W1, h[2], defs("c511c", *ALL) + K.saddling("c511c", W1, h[2], 5113),
             cap(v("22:3"), "right: 12px; top: 12px", size=10.5, maxw=380) + vref("GEN 22:3", "left: 12px; bottom: 12px"))
    r4 = cols(new(SAND, W2, h[3], defs("c511d", *ALL) + K.afar_off("c511d", W2, h[3], 5114),
                  cap(v("22:4"), "left: 8px; top: 8px", size=11, maxw=320) + vref("GEN 22:4", "left: 8px; bottom: 8px")),
              new(SAND, W2, h[3], defs("c511e", *ALL) + K.abide_here("c511e", W2, h[3], 5115),
                  cap(v("22:5", to="young men,"), "left: 8px; top: 8px", size=10, maxw=320)
                  + balloon(v("22:5", frm="Abide"), "left: 8px; top: 40px", 220, size=11.5, pad="20px 22px") + vref("GEN 22:5", "right: 8px; bottom: 8px")))
    return page("Genesis 22:1–5 — Take Now Thy Son", t, r1 + r2 + r3 + r4, START + 10)


@P("GEN-C05-P12-Lamb", "98 · God Will Provide Himself the Lamb")
def p12():
    t, h = rows(230, 330, 230, None)
    r1 = use(Mor[1], over=cap(v("22:6"), "right: 12px; bottom: 26px", size=11, maxw=330) + vref("GEN 22:6", "left: 12px; bottom: 12px"))
    r2 = cols(use(Mor[2], over=cap(v("22:7", to="and said,"), "left: 8px; top: 8px", size=10, maxw=320)
                  + balloon(v("22:7", frm="My father:", to="father:"), "right: 8px; top: 60px", 140, size=13, pad="14px 14px")
                  + cap(v("22:7", frm="And he said,", to="said,"), "right: 8px; top: 124px", size=10)
                  + balloon(v("22:7", frm="Behold"), "right: 8px; top: 158px", 200, size=12, pad="20px 20px") + vref("GEN 22:7", "left: 8px; bottom: 8px")),
              use(Mor[3], over=cap(v("22:7", frm="and he said,", to="he said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("22:7", frm="Here am I", to="my son."), "right: 8px; top: 40px", 170, size=12.5, pad="14px 16px")
                  + cap(v("22:8", to="Abraham said,"), "right: 8px; top: 100px", size=10)
                  + balloon(v("22:8", frm="God will", to="my son:"), "right: 8px; top: 134px", 200, size=12.5, pad="20px 20px")
                  + cap(v("22:8", frm="so they went"), "right: 8px; bottom: 8px", size=10, maxw=200) + vref("GEN 22:8", "left: 8px; bottom: 8px")))
    r3 = new("linear-gradient(180deg, #4A1D55 0%, #FF8A3D 100%)", W1, h[2], defs("c512c", *ALL) + K.altar_bound("c512c", W1, h[2], 5123),
             cap(v("22:9"), "right: 12px; top: 12px", size=10.5, maxw=290) + vref("GEN 22:9", "left: 12px; bottom: 10px"))
    r4 = use(Prov[0], over=cap(v("22:10"), "left: 12px; bottom: 12px", size=12, maxw=330) + vref("GEN 22:10", "right: 12px; bottom: 12px"))
    return page("Genesis 22:6–10 — God Will Provide Himself the Lamb", t, r1 + r2 + r3 + r4, START + 11)


@P("GEN-C05-P13-Ram", "99 · Jehovah-jireh")
def p13():
    t, h = rows(180, 190, 250, None)
    r1 = new(NIGHT, W1, h[0], cosmic(W1, h[0]),
             cap(v("22:11", to="and said,"), "left: 12px; top: 12px", size=10.5, maxw=420)
             + god(v("22:11", frm="Abraham, Abraham:", to="Abraham:"), "left: 12px; top: 66px", size=26, maxw=420)
             + cap(v("22:11", frm="and he said,", to="he said,"), "right: 12px; top: 66px", size=10.5)
             + balloon(v("22:11", frm="Here am I."), "right: 12px; bottom: 12px", 150, size=14, pad="14px 16px") + vref("GEN 22:11", "left: 12px; bottom: 10px"))
    r2 = new(NIGHT, W1, h[1], cosmic(W1, h[1]),
             cap(v("22:12", to="he said,"), "left: 12px; top: 12px", size=10.5)
             + god(v("22:12", frm="Lay not"), "left: 12px; top: 46px", size=15, maxw=660) + vref("GEN 22:12"))
    r3 = use(Prov[1], over=cap(v("22:13"), "left: 12px; top: 12px", size=10.5, maxw=440)
             + sfx("ガサッ", "GASA", "right: 20px; bottom: 30px", size=44, fill="#0D0D0F", stroke="#F3EFE6", rot=-6) + vref("GEN 22:13", "right: 12px; top: 12px"))
    r4 = cols(use(Prov[2], over=cap(v("22:14"), "left: 8px; top: 8px", size=10.5, maxw=320)
                  + hud("JEHOVAH-JIREH", "left: 50%; bottom: 40px; transform: translateX(-50%)", color="#12113A", size=22) + vref("GEN 22:14", "left: 8px; bottom: 8px")),
              new(GLOW, W2, h[3], fc(K.ABRAHAM_AWE, h[3]), ""))
    return page("Genesis 22:11–14 — Jehovah-jireh", t, r1 + r2 + r3 + r4, START + 12)


@P("GEN-C05-P14-Sand", "100 · As the Stars and as the Sand")
def p14():
    t, h = rows(220, 330, None)
    r1 = new(NIGHT, W1, h[0], cosmic(W1, h[0]),
             cap(v("22:15"), "left: 12px; top: 12px", size=10.5, maxw=520)
             + cap(v("22:16", to="and said,"), "left: 12px; top: 50px", size=10.5)
             + god(v("22:16", frm="By myself"), "left: 12px; top: 84px", size=16, maxw=640) + vref("GEN 22:15–16"))
    r2 = cols(use(Prov[3], over=god(v("22:17"), "left: 8px; top: 8px", size=13.5, maxw=320) + vref("GEN 22:17", "left: 8px; bottom: 8px")),
              new(NIGHT, W2, h[1], Q.kings_of_thee(W2, h[1], 5142), god(v("22:18"), "left: 8px; top: 8px", size=15, maxw=320) + vref("GEN 22:18", "right: 8px; bottom: 8px")))
    r3 = new(DUSK, W1, h[2], defs("c514c", *ALL) + Y.ground(W1, h[2], h[2] * 0.86, "#8A6A4A", dy=0) + Z.sun(W1 * 0.86, h[2] * 0.7, 22, color="#FF8A3D", op=0.25)
             + K.abraham("c514c", W1 * 0.3, h[2] * 0.86, Y.fit(h[2] * 0.86, h[2] * 0.4), flip=True, staff=True, up=Z.HOLD_STAFF)
             + K.lad("c514c", W1 * 0.4, h[2] * 0.86, Y.fit(h[2] * 0.86, h[2] * 0.46), cloth=K.ISAAC_TUNIC, flip=True)
             + Z.N.ass(W1 * 0.52, h[2] * 0.86 + 4, 0.22, flip=True) + K.man("c514c", W1 * 0.62, h[2] * 0.86, Y.fit(h[2] * 0.86, h[2] * 0.42), "#5A3A22", flip=True)
             + K.man("c514c", W1 * 0.7, h[2] * 0.86, Y.fit(h[2] * 0.86, h[2] * 0.42), "#8A6A4A", flip=True),
             cap(v("22:19"), "right: 12px; top: 12px", size=12, maxw=380) + vref("GEN 22:19", "left: 12px; bottom: 12px"))
    return page("Genesis 22:15–19 — As the Stars and as the Sand", t, r1 + r2 + r3, START + 13)


@P("GEN-C05-P15-Nahor", "101 · Bethuel Begat Rebekah")
def p15():
    t, h = rows(230, 320, None)
    r1 = new(NIGHT, W1, h[0], K.nahor_house(W1, h[0], 5151),
             cap(v("22:20", to="saying,"), "left: 12px; top: 12px", size=10.5, maxw=300)
             + balloon(v("22:20", frm="Behold,"), "left: 12px; top: 72px", 230, size=12, pad="18px 22px") + vref("GEN 22:20", "right: 12px; bottom: 12px"))
    cells = [clan("Uz · Buz · Kemuel", v("22:21"), "GEN 22:21", "#FFD23F", of="OF NAHOR", size=14),
             clan("Chesed … Bethuel", v("22:22"), "GEN 22:22", "#FFD23F", of="OF NAHOR", size=14),
             clan("Rebekah", v("22:23"), "GEN 22:23", "#D7261E", of="OF BETHUEL", size=13.5),
             clan("Reumah", v("22:24"), "GEN 22:24", "#C2456A", of="NAHOR'S CONCUBINE", size=13.5)]
    r2 = grid(cells, "1fr 1fr")
    r3 = new(DUSK, W1, h[2], defs("c515c", *ALL) + K.mourning("c515c", W1, h[2], 5153),
             cap(v("23:1"), "left: 12px; top: 12px", size=11.5, maxw=420)
             + cap(v("23:2"), "left: 12px; top: 74px", size=11.5, maxw=420) + hud("127", "right: 14px; top: 12px", size=28) + vref("GEN 23:1–2", "left: 12px; bottom: 12px"))
    return page("Genesis 22:20–23:2 — Bethuel Begat Rebekah", t, r1 + r2 + r3, START + 14)


@P("GEN-C05-P16-Heth", "102 · A Stranger and a Sojourner")
def p16():
    t, h = rows(220, 230, 300, None)
    r1 = new(SAND, W1, h[0], defs("c516a", *ALL) + K.heth_gate("c516a", W1, h[0], 5161),
             cap(v("23:3"), "right: 12px; top: 12px", size=11, maxw=330) + vref("GEN 23:3", "left: 12px; bottom: 10px"))
    r2 = new("radial-gradient(circle at 70% 30%, #E8D8C8 0 20px, #8A6A7A 180px, #2A1A2E 400px)", W1, h[1], fc(K.ABRAHAM_WEEP, h[1], w=W1),
             balloon(v("23:4"), "left: 250px; top: 20px", 400, size=13, pad="28px 40px") + vref("GEN 23:4", "left: 12px; bottom: 12px"))
    r3 = new(SAND, W1, h[2], defs("c516c", *ALL) + K.heth_gate("c516c", W1, h[2], 5163),
             cap(v("23:5"), "right: 12px; top: 12px", size=10.5, maxw=330)
             + balloon(v("23:6"), "right: 12px; top: 56px", 380, size=12, pad="28px 38px") + vref("GEN 23:5–6", "left: 12px; bottom: 12px"))
    r4 = new(SAND, W1, h[3], defs("c516d", *ALL) + K.heth_gate("c516d", W1, h[3], 5164, bowing=True),
             cap(v("23:7"), "right: 12px; top: 12px", size=11, maxw=360) + vref("GEN 23:7", "left: 12px; bottom: 10px"))
    return page("Genesis 23:3–7 — A Stranger and a Sojourner", t, r1 + r2 + r3 + r4, START + 15)


@P("GEN-C05-P17-Ephron", "103 · The Cave of Machpelah")
def p17():
    t, h = rows(300, 280, None)
    r1 = new(WARM, W1, h[0], fc(K.ABRAHAM, h[0], w=W1),
             cap(v("23:8", to="saying,"), "left: 320px; top: 12px", size=10.5, maxw=360)
             + balloon(v("23:8", frm="If it be") + " " + v("23:9"), "left: 270px; top: 66px", 410, size=12.5, pad="32px 42px") + vref("GEN 23:8–9", "left: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], defs("c517b", *ALL) + K.heth_gate("c517b", W1, h[1], 5172, ephron=True),
             cap(v("23:10"), "right: 12px; top: 12px", size=10.5, maxw=300) + vref("GEN 23:10", "left: 12px; bottom: 10px"))
    r3 = new("radial-gradient(circle at 70% 30%, #FFE680 0 20px, #C8885A 180px, #5A3A22 420px)", W1, h[2], fc(K.EPHRON, h[2], w=W1),
             balloon(v("23:11"), "left: 280px; top: 30px", 400, size=13, pad="30px 40px") + vref("GEN 23:11", "left: 12px; bottom: 12px"))
    return page("Genesis 23:8–11 — The Cave of Machpelah", t, r1 + r2 + r3, START + 16)


@P("GEN-C05-P18-Shekels", "104 · Four Hundred Shekels of Silver")
def p18():
    t, h = rows(190, 270, None)
    r1 = new(SAND, W1, h[0], defs("c518a", *ALL) + K.heth_gate("c518a", W1, h[0], 5181, bowing=True),
             cap(v("23:12"), "right: 12px; top: 12px", size=11.5, maxw=330) + vref("GEN 23:12", "left: 12px; bottom: 10px"))
    r2 = new(WARM, W1, h[1], fc(K.ABRAHAM, h[1], w=W1),
             cap(v("23:13", to="saying,"), "left: 300px; top: 12px", size=10.5, maxw=380)
             + balloon(v("23:13", frm="But if"), "left: 280px; top: 66px", 390, size=12.5, pad="26px 36px") + vref("GEN 23:13", "left: 12px; bottom: 12px"))
    r3 = cols(new("radial-gradient(circle at 70% 30%, #FFE680 0 20px, #C8885A 180px, #5A3A22 420px)", W2, h[2], fc(K.EPHRON, h[2]),
                  cap(v("23:14"), "right: 8px; top: 8px", size=10, maxw=200)
                  + balloon(v("23:15"), "right: 8px; top: 64px", 220, size=11.5, pad="24px 24px") + vref("GEN 23:14–15", "left: 8px; bottom: 8px")),
              new("#12113A", W2, h[2], K.shekels(W2, h[2], 5184),
                  cap(v("23:16"), "left: 8px; top: 8px", size=10.5, maxw=320) + hud("400", "right: 10px; bottom: 10px", size=30) + vref("GEN 23:16", "left: 8px; bottom: 8px")))
    return page("Genesis 23:12–16 — Four Hundred Shekels of Silver", t, r1 + r2 + r3, START + 17)


@P("GEN-C05-P19-Buried", "105 · Abraham Buried Sarah His Wife")
def p19():
    t, h = rows(320, 300, None)
    r1 = new(GREEN, W1, h[0], K.machpelah(None, W1, h[0], 5191),
             cap(v("23:17") + " " + v("23:18"), "left: 12px; top: 12px", size=11, maxw=500) + vref("GEN 23:17–18", "left: 12px; bottom: 12px"))
    r2 = new(DUSK, W1, h[1], defs("c519b", *ALL) + K.machpelah("c519b", W1, h[1], 5192, burial=True),
             cap(v("23:19"), "left: 12px; top: 12px", size=12, maxw=420) + vref("GEN 23:19", "left: 12px; bottom: 12px"))
    r3 = new("linear-gradient(180deg, #12113A 0%, #4A1D55 60%, #C2456A 100%)", W1, h[2], mk.stars(60, W1, h[2] * 0.6, 5193)
             + Y.hills(W1, h[2], h[2] * 0.8, 5193, color="#12090A", amp=8),
             cap(v("23:20"), "left: 12px; top: 12px", size=12.5, maxw=440)
             + end_mark("NEXT · ISAAC AND REBEKAH", "right: 14px; bottom: 12px") + vref("GEN 23:20", "left: 12px; bottom: 12px"))
    return page("Genesis 23:17–20 — Abraham Buried Sarah His Wife", t, r1 + r2 + r3, START + 18)
