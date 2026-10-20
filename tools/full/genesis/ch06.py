"""Genesis volume, Chapter 6 — A Wife for Isaac (Genesis 24:1–25:18). Word for word from ref/eng-asv.
The servant's retelling (24:34–49) is abridged on one page: its opening (24:34–37) and close (24:48–49) in full,
the repeated middle cut with "…" (24:38–44 and 24:46 omitted, 24:45 and 24:47 partial). Every other verse is in full.
25:1–4 (Keturah's sons) and 25:12–16 (Ishmael's princes) are set as scroll cells."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from faces_ex import F
from genesis import G, art as X, art2 as Y, art3 as Z, art4 as Q, art5 as K, art6 as R6
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import clan, hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch05 import WARM
from mk import defs, face

v, sp = G.v, G.span
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
EVE = "linear-gradient(180deg, #4A1D55 0%, #C2456A 50%, #FFB45A 100%)"
GOLDEN = "radial-gradient(circle at 70% 30%, #FFF4C2 0 30px, #FFC14D 160px, #8A4A3A 420px)"
GREENLIT = "radial-gradient(circle at 70% 30%, #FFF4C2 0 20px, #8AC88A 180px, #1F4A34 420px)"
RUST = "radial-gradient(circle at 70% 30%, #FFE680 0 20px, #C8683E 180px, #4A1A10 420px)"
ISHMAEL = F("adam", skin="#B9785A", shadow="#5A3A2A", hair="#E8E2D6", hl="#B8B2A6", beard=True, scarf="#5A6A3A", cord=True, light="#FFC14D")
START = 106                                  # chapter 5 ends on page 105
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco


@P("GEN-C06-00-Title", "Chapter 6 · A Wife for Isaac")
def title():
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#2A1430"></rect>' + defs("tt6", *ALL)
           + '<g transform="translate(0 150)">' + R6.evening_well("tt6", 760, 1080, 61) + '</g>')
    return chapter_title(6, "第六話", "A Wife for Isaac", "Genesis 24:1 – 25:18", svg, EVE,
                         v("24:67", frm="and he loved her.", to="her."), "Genesis · Volume One")


@P("GEN-C06-P01-Oath", "106 · Put Thy Hand under My Thigh")
def p01():
    t, h = rows(230, 330, None)
    r1 = new(TENT, W1, h[0], defs("c61a", *ALL) + R6.master_and_servant("c61a", W1, h[0], 611),
             cap(v("24:1"), "left: 12px; top: 12px", size=11, maxw=330)
             + cap(v("24:2", to="that he had,"), "right: 12px; top: 12px", size=10.5, maxw=300) + vref("GEN 24:1–2", "right: 12px; bottom: 10px"))
    r2 = new(GOLDEN, W1, h[1], fc(R6.ABRAHAM_OLD, h[1], w=W1),
             balloon(v("24:2", frm="Put, I pray") + " " + v("24:3") + " " + v("24:4"), "left: 270px; top: 20px", 410, size=12.5, pad="34px 42px")
             + vref("GEN 24:2–4", "left: 12px; bottom: 12px"))
    r3 = cols(new(RUST, W2, h[2], fc(R6.SERVANT, h[2]),
                  cap(v("24:5", to="said unto him,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("24:5", frm="Peradventure"), "right: 8px; top: 40px", 220, size=11.5, pad="24px 22px") + vref("GEN 24:5", "left: 8px; bottom: 8px")),
              new(GOLDEN, W2, h[2], fc(R6.ABRAHAM_OLD, h[2]),
                  cap(v("24:6", to="said unto him,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("24:6", frm="Beware"), "right: 8px; top: 40px", 200, size=12.5, pad="20px 20px") + vref("GEN 24:6", "left: 8px; bottom: 8px")))
    return page("Genesis 24:1–6 — Put Thy Hand under My Thigh", t, r1 + r2 + r3, START + 0)


@P("GEN-C06-P02-Camels", "107 · He Will Send His Angel before Thee")
def p02():
    t, h = rows(330, 190, 220, None)
    r1 = new(GOLDEN, W1, h[0], fc(R6.ABRAHAM_OLD, h[0], w=W1),
             balloon(v("24:7") + " " + v("24:8"), "left: 260px; top: 20px", 420, size=12.5, pad="36px 42px") + vref("GEN 24:7–8", "left: 12px; bottom: 12px"))
    r2 = new(TENT, W1, h[1], defs("c62b", *ALL) + R6.master_and_servant("c62b", W1, h[1], 622),
             cap(v("24:9"), "right: 12px; top: 12px", size=11.5, maxw=360) + vref("GEN 24:9", "right: 12px; bottom: 10px"))
    r3 = cols(new(SAND, W2, h[2], R6.ten_camels(None, W2, h[2], 623),
                  cap(v("24:10", to="in his hand:"), "left: 8px; top: 8px", size=10.5, maxw=230) + vref("GEN 24:10", "left: 8px; bottom: 8px")),
              new("#0B1A2E", W2, h[2], R6.to_mesopotamia(W2, h[2], 624),
                  cap(v("24:10", frm="and he arose"), "right: 8px; bottom: 8px", size=10.5, maxw=230)))
    r4 = new(EVE, W1, h[3], defs("c62d", *ALL) + R6.evening_well("c62d", W1, h[3], 625),
             cap(v("24:11"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("GEN 24:11", "left: 12px; bottom: 12px"))
    return page("Genesis 24:7–11 — He Will Send His Angel before Thee", t, r1 + r2 + r3 + r4, START + 1)


@P("GEN-C06-P03-Pitcher", "108 · Let Down Thy Pitcher")
def p03():
    t, h = rows(380, 300, None)
    r1 = new(GOLDEN, W1, h[0], fc(R6.SERVANT_PRAY, h[0], w=W1),
             cap(v("24:12", to="said,"), "left: 330px; top: 12px", size=10.5)
             + balloon(v("24:12", frm="O Jehovah") + " " + v("24:13") + " " + v("24:14"), "left: 250px; top: 46px", 440, size=12, pad="38px 44px")
             + vref("GEN 24:12–14", "left: 12px; bottom: 12px"))
    r2 = new(EVE, W1, h[1], defs("c63b", *ALL) + R6.rebekah_comes("c63b", W1, h[1], 632),
             cap(v("24:15"), "right: 12px; top: 12px", size=11, maxw=330) + vref("GEN 24:15", "right: 12px; bottom: 12px"))
    r3 = new(GREENLIT, W1, h[2], fc(R6.REBEKAH, h[2], w=W1),
             cap(v("24:16"), "right: 12px; top: 12px", size=12.5, maxw=340) + vref("GEN 24:16", "left: 12px; bottom: 12px"))
    return page("Genesis 24:12–16 — Let Down Thy Pitcher", t, r1 + r2 + r3, START + 2)


@P("GEN-C06-P04-Trough", "109 · I Will Draw for Thy Camels Also")
def p04():
    t, h = rows(280, 290, None)
    r1 = new(EVE, W1, h[0], defs("c64a", *ALL) + R6.give_drink("c64a", W1, h[0], 641),
             cap(v("24:17", to="said,"), "left: 12px; top: 12px", size=10.5)
             + balloon(v("24:17", frm="Give me"), "left: 12px; top: 46px", 240, size=12, pad="18px 22px")
             + cap(v("24:18", to="said,"), "right: 12px; top: 12px", size=10.5)
             + balloon(v("24:18", frm="Drink, my lord:", to="lord:"), "right: 12px; top: 46px", 190, size=13, pad="14px 18px")
             + cap(v("24:18", frm="and she hasted"), "right: 12px; top: 110px", size=10.5, maxw=230) + vref("GEN 24:17–18", "left: 12px; bottom: 12px"))
    r2 = cols(new(GREENLIT, W2, h[1], fc(R6.REBEKAH, h[1]),
                  cap(v("24:19", to="she said,"), "right: 8px; top: 8px", size=10, maxw=200)
                  + balloon(v("24:19", frm="I will draw"), "right: 8px; top: 64px", 200, size=12, pad="20px 20px") + vref("GEN 24:19", "left: 8px; bottom: 8px")),
              new(EVE, W2, h[1], defs("c64b", *ALL) + R6.camels_drink("c64b", W2, h[1], 642),
                  cap(v("24:20"), "left: 8px; top: 8px", size=10.5, maxw=320)
                  + sfx("ザバッ", "ZABA", "right: 12px; top: 96px", size=32, fill="#8FD0E2", stroke="#0D0D0F", rot=6) + vref("GEN 24:20", "right: 8px; bottom: 8px")))
    r3 = cols(new(RUST, W2, h[2], fc(R6.SERVANT, h[2]), cap(v("24:21"), "right: 8px; top: 8px", size=11, maxw=200) + vref("GEN 24:21", "left: 8px; bottom: 8px")),
              new("#12113A", W2, h[2], R6.ring_bracelets(W2, h[2], 643), cap(v("24:22"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 24:22", "right: 8px; bottom: 8px")))
    return page("Genesis 24:17–22 — I Will Draw for Thy Camels Also", t, r1 + r2 + r3, START + 3)


@P("GEN-C06-P05-Bethuel", "110 · Whose Daughter Art Thou?")
def p05():
    t, h = rows(320, 260, None)
    r1 = cols(new(RUST, W2, h[0], fc(R6.SERVANT, h[0]),
                  cap(v("24:23", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("24:23", frm="Whose"), "right: 8px; top: 40px", 220, size=12, pad="22px 22px") + vref("GEN 24:23", "left: 8px; bottom: 8px")),
              new(GREENLIT, W2, h[0], fc(R6.REBEKAH, h[0]),
                  cap(v("24:24", to="unto him,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("24:24", frm="I am the"), "right: 8px; top: 40px", 200, size=11.5, pad="18px 18px")
                  + cap(v("24:25", to="unto him,"), "right: 8px; top: 140px", size=10)
                  + balloon(v("24:25", frm="We have"), "right: 8px; top: 172px", 200, size=11.5, pad="18px 18px") + vref("GEN 24:24–25", "left: 8px; bottom: 8px")))
    r2 = new(NIGHT, W1, h[1], R6.worship(None, W1, h[1], 652),
             cap(v("24:26"), "left: 12px; top: 12px", size=11.5, maxw=330)
             + cap(v("24:27", to="said,"), "right: 12px; top: 12px", size=10.5)
             + balloon(v("24:27", frm="Blessed"), "right: 12px; top: 46px", 380, size=12, pad="26px 36px") + vref("GEN 24:26–27", "left: 12px; bottom: 12px"))
    r3 = new(EVE, W1, h[2], defs("c65c", *ALL) + R6.runs_home("c65c", W1, h[2], 653),
             cap(v("24:28"), "left: 12px; top: 12px", size=12, maxw=360) + vref("GEN 24:28", "right: 12px; bottom: 12px"))
    return page("Genesis 24:23–28 — Whose Daughter Art Thou?", t, r1 + r2 + r3, START + 4)


@P("GEN-C06-P06-Laban", "111 · Thou Blessed of Jehovah")
def p06():
    t, h = rows(260, 260, None)
    r1 = new(EVE, W1, h[0], defs("c66a", *ALL) + R6.laban_runs("c66a", W1, h[0], 661),
             cap(v("24:29"), "left: 12px; top: 12px", size=11, maxw=290)
             + cap(v("24:30"), "right: 12px; top: 12px", size=10.5, maxw=360) + vref("GEN 24:29–30", "left: 12px; bottom: 12px"))
    r2 = new(RUST, W1, h[1], fc(R6.LABAN, h[1], w=W1),
             cap(v("24:31", to="said,"), "left: 320px; top: 12px", size=10.5)
             + balloon(v("24:31", frm="Come in"), "left: 290px; top: 46px", 380, size=13, pad="26px 36px") + vref("GEN 24:31", "left: 12px; bottom: 12px"))
    r3 = new("#5A3A2E", W1, h[2], defs("c66c", *ALL) + R6.lodging("c66c", W1, h[2], 663),
             cap(v("24:32"), "right: 12px; top: 12px", size=10.5, maxw=380)
             + cap(v("24:33", to="but he said,"), "right: 12px; top: 102px", size=10.5, maxw=380)
             + balloon(v("24:33", frm="I will not eat", to="errand."), "right: 12px; top: 154px", 270, size=12.5, pad="18px 22px")
             + cap(v("24:33", frm="And he said, Speak", to="said,"), "right: 12px; bottom: 62px", size=10.5)
             + balloon(v("24:33", frm="Speak on."), "right: 12px; bottom: 12px", 150, size=14, pad="12px 14px") + vref("GEN 24:32–33", "left: 12px; bottom: 12px"))
    return page("Genesis 24:29–33 — Thou Blessed of Jehovah", t, r1 + r2 + r3, START + 5)


@P("GEN-C06-P07-Errand", "112 · I Am Abraham's Servant")
def p07():
    t, h = rows(340, 300, None)
    r1 = new(RUST, W1, h[0], fc(R6.SERVANT, h[0], w=W1),
             cap(v("24:34", to="said,"), "left: 320px; top: 12px", size=10.5)
             + balloon(v("24:34", frm="I am"), "left: 300px; top: 46px", 230, size=14, pad="16px 20px")
             + balloon(v("24:35") + " " + v("24:36"), "right: 12px; bottom: 12px", 400, size=12, pad="30px 40px") + vref("GEN 24:34–36", "left: 12px; bottom: 12px"))
    told = (v("24:37") + " … " + v("24:45", frm="behold, Rebekah", to="on her shoulder;") + " … " + v("24:47", frm="and I put the ring"))
    r2 = new("linear-gradient(180deg, #6A5A7A 0%, #C8A0A0 100%)", W1, h[1], defs("c67b", *ALL) + R6.give_drink("c67b", W1, h[1], 672, top=0.62),
             f'    <span data-label style="position: absolute; left: 14px; bottom: 12px; padding: 3px 8px; background: #12113A; color: #FFD23F; font-size: 9px; font-weight: 600; letter-spacing: 0.18em">AS HE TOLD IT · GEN 24:37–47 ABRIDGED</span>\n'
             + balloon(told, "left: 12px; top: 12px", 460, size=12, pad="30px 40px"))
    r3 = new(RUST, W1, h[2], fc(R6.SERVANT, h[2], w=W1, flip=True),
             balloon(v("24:48"), "left: 12px; top: 14px", 400, size=12, pad="28px 38px")
             + balloon(v("24:49"), "left: 40px; bottom: 14px", 360, size=12, pad="24px 34px") + vref("GEN 24:48–49", "right: 12px; bottom: 12px"))
    return page("Genesis 24:34–49 — I Am Abraham's Servant", t, r1 + r2 + r3, START + 6)


@P("GEN-C06-P08-Proceedeth", "113 · The Thing Proceedeth from Jehovah")
def p08():
    t, h = rows(280, 170, 190, None)
    r1 = cols(new(RUST, W2, h[0], fc(R6.LABAN, h[0]),
                  cap(v("24:50", to="said,"), "right: 8px; top: 8px", size=10, maxw=200)
                  + balloon(v("24:50", frm="The thing"), "right: 8px; top: 64px", 210, size=12, pad="22px 20px") + vref("GEN 24:50", "left: 8px; bottom: 8px")),
              new("radial-gradient(circle at 70% 30%, #E8D8C8 0 20px, #8A6A7A 180px, #2A1A2E 400px)", W2, h[0], fc(R6.BETHUEL, h[0]),
                  balloon(v("24:51"), "right: 8px; top: 12px", 220, size=12, pad="24px 22px") + vref("GEN 24:51", "left: 8px; bottom: 8px")))
    r2 = new(NIGHT, W1, h[1], R6.worship(None, W1, h[1], 682), cap(v("24:52"), "right: 12px; top: 12px", size=11.5, maxw=380) + vref("GEN 24:52", "left: 12px; bottom: 10px"))
    r3 = new("#12113A", W1, h[2], K.silver(W1, h[2], 683), cap(v("24:53"), "left: 12px; top: 12px", size=11, maxw=560) + vref("GEN 24:53", "right: 12px; bottom: 10px"))
    r4 = cols(new(RUST, W2, h[3], fc(R6.SERVANT, h[3]),
                  cap(v("24:54", to="and he said,"), "right: 8px; top: 8px", size=10, maxw=210)
                  + balloon(v("24:54", frm="Send me"), "right: 8px; top: 100px", 190, size=12, pad="18px 18px")
                  + cap(v("24:56", to="unto them,"), "right: 8px; top: 186px", size=10)
                  + balloon(v("24:56", frm="Hinder"), "right: 8px; top: 220px", 210, size=11.5, pad="22px 22px") + vref("GEN 24:54, 56", "left: 8px; bottom: 8px")),
              new("radial-gradient(circle at 70% 30%, #E8D8C8 0 20px, #6A5A7A 180px, #2A1A2E 400px)", W2, h[3],
                  face(R6.LABAN, -40, h[3] - 330, 0.8) + face(Q.SARAH, W2 + 60, h[3] - 300, 0.72, flip=True).replace("#8A3A5A", "#5A4A6A"),
                  cap(v("24:55", to="said,"), "left: 8px; top: 8px", size=10, maxw=320)
                  + balloon(v("24:55", frm="Let the"), "left: 60px; top: 44px", 230, size=12, pad="20px 22px") + vref("GEN 24:55", "right: 8px; top: 8px")))
    return page("Genesis 24:50–56 — The Thing Proceedeth from Jehovah", t, r1 + r2 + r3 + r4, START + 7)


@P("GEN-C06-P09-IWillGo", "114 · I Will Go")
def p09():
    t, h = rows(300, 290, None)
    r1 = cols(new(RUST, W2, h[0], fc(R6.LABAN, h[0]),
                  cap(v("24:57", to="they said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("24:57", frm="We will"), "right: 8px; top: 40px", 200, size=12, pad="18px 20px")
                  + cap(v("24:58", to="unto her,"), "right: 8px; top: 150px", size=10, maxw=200)
                  + balloon(v("24:58", frm="Wilt thou", to="man?"), "right: 8px; top: 206px", 180, size=12.5, pad="16px 16px") + vref("GEN 24:57–58", "left: 8px; bottom: 8px")),
              new(GREENLIT, W2, h[0], fc(R6.REBEKAH, h[0]),
                  cap(v("24:58", frm="And she said,", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("24:58", frm="I will go."), "right: 8px; top: 44px", 180, size=20, pad="18px 18px")))
    r2 = new(TENT, W1, h[1], defs("c69b", *ALL) + R6.family_blessing("c69b", W1, h[1], 692),
             cap(v("24:59"), "right: 12px; top: 12px", size=10.5, maxw=270)
             + cap(v("24:60", to="unto her,"), "right: 12px; top: 92px", size=10.5, maxw=270)
             + balloon(v("24:60", frm="Our sister"), "right: 12px; top: 150px", 250, size=11.5, pad="22px 26px") + vref("GEN 24:59–60", "left: 12px; bottom: 12px"))
    r3 = new(DAWN, W1, h[2], R6.depart(None, W1, h[2], 693),
             cap(v("24:61"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("GEN 24:61", "right: 12px; top: 12px"))
    return page("Genesis 24:57–61 — I Will Go", t, r1 + r2 + r3, START + 8)


@P("GEN-C06-P10-Field", "115 · Isaac Went Out to Meditate")
def p10():
    t, h = rows(240, 270, 230, None)
    r1 = new(EVE, W1, h[0], defs("c610a", *ALL) + R6.meditate("c610a", W1, h[0], 6101),
             cap(v("24:62"), "left: 12px; top: 12px", size=11, maxw=330)
             + cap(v("24:63"), "right: 12px; top: 12px", size=11, maxw=330) + vref("GEN 24:62–63", "right: 12px; bottom: 12px"))
    r2 = cols(new(EVE, W2, h[1], defs("c610b", *ALL) + R6.alight("c610b", W2, h[1], 6102),
                  cap(v("24:64"), "left: 8px; top: 8px", size=11, maxw=320) + vref("GEN 24:64", "right: 8px; bottom: 8px")),
              new(RUST, W2, h[1], fc(R6.REBEKAH, h[1]),
                  cap(v("24:65", to="unto the servant,"), "right: 8px; top: 8px", size=10, maxw=200)
                  + balloon(v("24:65", frm="What man", to="meet us?"), "right: 8px; top: 64px", 210, size=12, pad="20px 20px") + vref("GEN 24:65", "left: 8px; bottom: 8px")))
    r3 = cols(new(RUST, W2, h[2], fc(R6.SERVANT, h[2]),
                  cap(v("24:65", frm="And the servant said,", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("24:65", frm="It is my master:", to="master:"), "right: 8px; top: 42px", 170, size=13, pad="16px 16px")
                  + cap(v("24:66"), "right: 8px; bottom: 8px", size=10, maxw=210)),
              new(EVE, W2, h[2], fc(R6.REBEKAH_VEIL, h[2]),
                  cap(v("24:65", frm="and she took her veil"), "right: 8px; top: 8px", size=11.5, maxw=190) + vref("GEN 24:65–66", "left: 8px; bottom: 8px")))
    r4 = new(NIGHT, W1, h[3], defs("c610d", *ALL) + R6.sarahs_tent("c610d", W1, h[3], 6104),
             cap(v("24:67"), "left: 12px; top: 12px", size=11, maxw=300) + vref("GEN 24:67", "right: 12px; bottom: 12px"))
    return page("Genesis 24:62–67 — Isaac Went Out to Meditate", t, r1 + r2 + r3 + r4, START + 9)


@P("GEN-C06-P11-Keturah", "116 · Keturah")
def p11():
    t, h = rows(290, None, 340)
    r1 = new(TENT, W1, h[0], defs("c611a", *ALL) + Y.ground(W1, h[0], h[0] * 0.86, "#C8A06A", dy=0)
             + G1_tent(W1 * 0.8, h[0] * 0.86, W1 * 0.24, h[0] * 0.66)
             + Z.abram("c611a", W1 * 0.5, h[0] * 0.86, Y.fit(h[0] * 0.86, h[0] * 0.3), flip=True)
             + Z.woman("c611a", W1 * 0.6, h[0] * 0.86, Y.fit(h[0] * 0.86, h[0] * 0.34), "#B5652E", flip=True),
             cap(v("25:1"), "left: 12px; top: 12px", size=12, maxw=320) + vref("GEN 25:1", "left: 12px; bottom: 10px"))
    cells = [clan("Keturah", v("25:2"), "GEN 25:2", "#E8A317", size=16),
             clan("Jokshan", v("25:3"), "GEN 25:3", "#E8A317", size=16),
             clan("Midian", v("25:4"), "GEN 25:4", "#E8A317", size=16)]
    r2 = grid(cells, "minmax(0, 1fr)", ncol=3)
    r3 = new(SAND, W1, h[2], defs("c611c", *ALL) + R6.east_country("c611c", W1, h[2], 6113),
             cap(v("25:5"), "left: 12px; top: 12px", size=12, maxw=300)
             + cap(v("25:6"), "right: 12px; top: 40px", size=11, maxw=340) + vref("GEN 25:5–6", "left: 12px; bottom: 12px"))
    return page("Genesis 25:1–6 — Keturah", t, r1 + r2 + r3, START + 10)

def G1_tent(x, y, w, h):
    import judges1 as G1
    return G1.tent_big(x, y, w, h, color="#3A2214", glow="#5A2A12")


@P("GEN-C06-P12-FullOfYears", "117 · Full of Years")
def p12():
    t, h = rows(290, 320, None)
    r1 = cols(new(GOLDEN, W2, h[0], fc(R6.ABRAHAM_OLD, h[0]),
                  cap(v("25:7"), "right: 8px; top: 8px", size=10.5, maxw=200) + hud("175", "right: 10px; bottom: 10px", size=30) + vref("GEN 25:7", "left: 8px; bottom: 8px")),
              new(DUSK, W2, h[0], R6.gathered(None, W2, h[0], 6122),
                  cap(v("25:8"), "left: 8px; top: 8px", size=11.5, maxw=320) + vref("GEN 25:8", "right: 8px; bottom: 8px")))
    r2 = new(DUSK, W1, h[1], defs("c612b", *ALL) + R6.buried_by_sons("c612b", W1, h[1], 6123),
             cap(v("25:9") + " " + v("25:10"), "left: 12px; top: 12px", size=11, maxw=460) + vref("GEN 25:9–10", "left: 12px; bottom: 12px"))
    r3 = new(SAND, W1, h[2], defs("c612c", *ALL) + Y.ground(W1, h[2], h[2] * 0.86, "#E8C88A", dy=0) + Z.sun(W1 * 0.8, h[2] * 0.3, 18, op=0.3)
             + K.well(W1 * 0.6, h[2] * 0.86 - 8, h[2] / 300) + R6.isaac("c612c", W1 * 0.4, h[2] * 0.86, Y.fit(h[2] * 0.86, h[2] * 0.4)),
             cap(v("25:11"), "left: 12px; top: 12px", size=12, maxw=420) + vref("GEN 25:11", "right: 12px; bottom: 12px"))
    return page("Genesis 25:7–11 — Full of Years", t, r1 + r2 + r3, START + 11)


@P("GEN-C06-P13-Ishmael", "118 · Twelve Princes")
def p13():
    t, h = rows(200, 300, None)
    r1 = new(NIGHT, W1, h[0], Q.twelve_princes(W1, h[0], 6131),
             cap(v("25:12"), "left: 12px; top: 12px", size=11.5, maxw=520) + vref("GEN 25:12", "right: 12px; top: 12px"))
    cells = [clan("The Sons of Ishmael", v("25:13") + " " + v("25:14") + " " + v("25:15"), "GEN 25:13–15", "#9ACB5E", of="SONS OF ISHMAEL", size=13),
             clan("Twelve Princes", v("25:16"), "GEN 25:16", "#9ACB5E", of="OF ISHMAEL", size=14)]
    r2 = grid(cells, "minmax(0, 1fr)")
    r3 = cols(new(RUST, W2, h[2], fc(ISHMAEL, h[2]),
                  cap(v("25:17"), "right: 8px; top: 8px", size=10.5, maxw=200) + hud("137", "right: 10px; bottom: 10px", size=30) + vref("GEN 25:17", "left: 8px; bottom: 8px")),
              new("#1A120A", W2, h[2], R6.ishmael_lands(W2, h[2], 6133),
                  cap(v("25:18"), "left: 8px; top: 8px", size=10.5, maxw=320)
                  + end_mark("NEXT · THE BIRTHRIGHT", "right: 10px; bottom: 10px")))
    return page("Genesis 25:12–18 — Twelve Princes", t, r1 + r2 + r3, START + 12)
