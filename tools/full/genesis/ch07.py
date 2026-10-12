"""Genesis volume, Chapter 7 — Jacob and Esau (Genesis 25:19–27:46). Every verse, word for word from ref/asv.
Reuses the digest's Book Four panels for the twins, the pottage, the blessing and the bitter cry."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from genesis import G, art as X, art2 as Y, art3 as Z, art4 as Q, art5 as K, art6 as R6, art7 as J7
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import clan, hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch05 import WARM, KING
from genesis.ch06 import RUST, GREENLIT, GOLDEN
from mk import defs, face

v, sp = G.v, G.span
B4 = "digest/genesis/book-04/"
Tw, Pot, Bl, Cry = (panels(B4 + n + ".dc.html") for n in ["B4-P01-Twins", "B4-P02-Pottage", "B4-P03-Blessing", "B4-P04-Cry"])
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
LAMP = "radial-gradient(circle at 60% 40%, #FFC14D 0 20px, #8A3A1E 220px, #1A0A06 460px)"
RED = "radial-gradient(circle at 70% 30%, #FFC14D 0 20px, #C8402A 180px, #3A0A0A 420px)"
BLUE = "radial-gradient(circle at 70% 30%, #CFE0FF 0 20px, #4A5A9A 180px, #12113A 420px)"
START = 119                                  # chapter 6 ends on page 118
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def cosmic(w, h, cx=None): return X.cosmic(w, h, cx)


@P("GEN-C07-00-Title", "Chapter 7 · Jacob and Esau")
def title():
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#1A0A06"></rect>'
           + '<rect x="0" y="0" width="380" height="1080" fill="#5A0A0A"></rect><rect x="380" y="0" width="380" height="1080" fill="#12113A"></rect>'
           + mk.face(J7.ESAU, -40, 500, 1.4) + mk.face(J7.JACOB, 800, 500, 1.4, flip=True)
           + '<path d="M380 0 L 380 1080" stroke="#0D0D0F" stroke-width="6"></path>')
    return chapter_title(7, "第七話", "Jacob and Esau", "Genesis 25:19 – 27:46", svg, NIGHT,
                         v("27:22", frm="The voice", to="of Esau."), "Genesis · Volume One · The Full Edition")


@P("GEN-C07-P01-TwoNations", "119 · Two Nations Are in Thy Womb")
def p01():
    t, h = rows(230, 260, None)
    r1 = new(TENT, W1, h[0], defs("c71a", *ALL) + Y.ground(W1, h[0], h[0] * 0.86, "#C8A06A", dy=0) + Z.sun(W1 * 0.86, h[0] * 0.2, 14, op=0.25)
             + R6.isaac("c71a", W1 * 0.5, h[0] * 0.86, Y.fit(h[0] * 0.86, h[0] * 0.3)) + R6.rebekah("c71a", W1 * 0.6, h[0] * 0.86, Y.fit(h[0] * 0.86, h[0] * 0.34), flip=True),
             cap(v("25:19") + " " + v("25:20"), "left: 12px; top: 12px", size=11, maxw=300)
             + cap(v("25:21"), "right: 12px; top: 12px", size=11, maxw=230) + vref("GEN 25:19–21", "left: 12px; bottom: 10px"))
    r2 = new(NIGHT, W1, h[1], J7.inquire(None, W1, h[1], 712),
             cap(v("25:22", to="she said,"), "left: 12px; top: 12px", size=10.5, maxw=300)
             + balloon(v("25:22", frm="If it be", to="do I live?"), "left: 12px; top: 64px", 240, size=12.5, pad="18px 22px")
             + cap(v("25:22", frm="And she went"), "right: 12px; top: 12px", size=11, maxw=230) + vref("GEN 25:22", "right: 12px; bottom: 12px"))
    r3 = new(NIGHT, W1, h[2], J7.two_nations(W1, h[2], 713),
             cap(v("25:23", to="unto her,"), "left: 12px; top: 12px", size=10.5)
             + god(v("25:23", frm="Two nations"), "left: 12px; top: 46px", size=18, maxw=330) + vref("GEN 25:23", "right: 12px; bottom: 12px"))
    return page("Genesis 25:19–23 — Two Nations Are in Thy Womb", t, r1 + r2 + r3, START + 0)


@P("GEN-C07-P02-Twins", "120 · His Hand Had Hold on Esau's Heel")
def p02():
    t, h = rows(310, 360, None)
    r1 = use(Tw[0], over=cap(v("25:24") + " " + v("25:25") + " " + v("25:26", to="called Jacob:"), "left: 12px; top: 12px", size=11, maxw=480)
             + sfx("ギュッ", "GYU", "right: 30px; top: 100px", size=52, fill="#0D0D0F", stroke="#F3EFE6", rot=6)
             + cap(v("25:26", frm="and Isaac was"), "right: 12px; bottom: 14px", size=10.5, maxw=300) + vref("GEN 25:24–26", "left: 12px; bottom: 12px"))
    r2 = use(Tw[1], over=cap(v("25:27"), "left: 12px; top: 12px", size=11.5, maxw=640) + vref("GEN 25:27", "right: 12px; bottom: 12px"))
    r3 = use(Tw[2], over=cap(v("25:28"), "left: 50%; top: 12px; transform: translateX(-50%)", size=11.5, maxw=520) + vref("GEN 25:28", "right: 12px; bottom: 12px"))
    return page("Genesis 25:24–28 — His Hand Had Hold on Esau's Heel", t, r1 + r2 + r3, START + 1)


@P("GEN-C07-P03-Pottage", "121 · Sell Me First Thy Birthright")
def p03():
    t, h = rows(210, 300, 270, None)
    r1 = new("#3A2214", W1, h[0], J7.pottage(W1, h[0], 731),
             cap(v("25:29"), "left: 12px; top: 12px", size=12, maxw=380)
             + sfx("グツグツ", "GUTSU GUTSU", "right: 24px; top: 16px", size=36, fill="#FFC14D", stroke="#0D0D0F", rot=-6) + vref("GEN 25:29", "right: 12px; bottom: 10px"))
    r2 = use(Pot[0], over=cap(v("25:30", to="to Jacob,"), "right: 12px; top: 12px", size=10.5)
             + balloon(v("25:30", frm="Feed me", to="faint:"), "right: 12px; top: 48px", 340, size=13, pad="22px 30px")
             + cap(v("25:30", frm="therefore"), "right: 12px; bottom: 14px", size=11) + vref("GEN 25:30", "left: 12px; bottom: 12px"))
    r3 = use(Pot[1], over=cap(v("25:31", to="said,"), "right: 12px; top: 12px", size=10.5)
             + balloon(v("25:31", frm="Sell me"), "right: 12px; top: 46px", 240, size=14, pad="18px 22px") + vref("GEN 25:31", "left: 12px; bottom: 12px"))
    r4 = cols(new(RED, W2, h[3], fc(J7.ESAU_FAINT, h[3]),
                  cap(v("25:32", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("25:32", frm="Behold"), "right: 8px; top: 40px", 200, size=12, pad="20px 20px") + vref("GEN 25:32", "left: 8px; bottom: 8px")),
              new(BLUE, W2, h[3], fc(J7.JACOB, h[3]),
                  cap(v("25:33", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("25:33", frm="Swear to me", to="first;"), "right: 8px; top: 40px", 170, size=13, pad="16px 16px")
                  + cap(v("25:33", frm="and he sware"), "right: 8px; bottom: 8px", size=10, maxw=210) + vref("GEN 25:33", "left: 8px; bottom: 8px")))
    return page("Genesis 25:29–33 — Sell Me First Thy Birthright", t, r1 + r2 + r3 + r4, START + 2)


@P("GEN-C07-P04-Famine", "122 · Go Not Down into Egypt")
def p04():
    t, h = rows(240, 270, None)
    r1 = cols(new("#3A2214", W2, h[0], J7.sold(None, W2, h[0], 741), vref("GEN 25:33", "right: 8px; top: 8px")),
              new(DUSK, W2, h[0], defs("c74a", *ALL) + J7.went_his_way("c74a", W2, h[0], 742),
                  cap(v("25:34"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 25:34", "right: 8px; bottom: 8px")))
    r2 = new(HOT, W1, h[1], Z.famine(W1, h[1], 743),
             cap(v("26:1"), "right: 12px; top: 12px", size=11, maxw=380) + vref("GEN 26:1", "left: 12px; bottom: 12px"))
    r3 = new(NIGHT, W1, h[2], cosmic(W1, h[2]),
             cap(v("26:2", to="and said,"), "left: 12px; top: 12px", size=10.5)
             + god(v("26:2", frm="Go not") + " " + v("26:3") + " " + v("26:4") + " " + v("26:5"), "left: 12px; top: 46px", size=15, maxw=660) + vref("GEN 26:2–5"))
    return page("Genesis 25:34–26:5 — Go Not Down into Egypt", t, r1 + r2 + r3, START + 3)


@P("GEN-C07-P05-Window", "123 · Abimelech Looked Out at a Window")
def p05():
    t, h = rows(230, 280, None)
    r1 = new(SAND, W1, h[0], K.gerar(None, W1, h[0], 751),
             cap(v("26:6") + " " + v("26:7", to="She is my sister:"), "left: 12px; top: 12px", size=11, maxw=500)
             + cap(v("26:7", frm="for he feared"), "left: 12px; top: 84px", size=10.5, maxw=380) + vref("GEN 26:6–7", "left: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], defs("c75b", *ALL) + J7.at_window("c75b", W1, h[1], 752),
             cap(v("26:8"), "right: 12px; top: 12px", size=11, maxw=360) + vref("GEN 26:8", "right: 12px; bottom: 12px"))
    r3 = cols(new(KING, W2, h[2], fc(K.ABIMELECH_STERN, h[2]),
                  cap(v("26:9", to="and said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("26:9", frm="Behold", to="my sister?"), "right: 8px; top: 40px", 200, size=11.5, pad="20px 20px")
                  + cap(v("26:10", to="said,"), "right: 8px; top: 160px", size=10)
                  + balloon(v("26:10", frm="What is this"), "right: 8px; top: 192px", 220, size=11, pad="22px 22px") + vref("GEN 26:9–10", "left: 8px; bottom: 8px")),
              new(WARM, W2, h[2], fc(J7.ISAAC_GERAR, h[2]),
                  cap(v("26:9", frm="And Isaac said", to="unto him,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("26:9", frm="Because I said"), "right: 8px; top: 40px", 190, size=12, pad="18px 18px")
                  + cap(v("26:11"), "right: 8px; bottom: 8px", size=10, maxw=210) + vref("GEN 26:11", "left: 8px; top: 8px")))
    return page("Genesis 26:6–11 — Abimelech Looked Out at a Window", t, r1 + r2 + r3, START + 4)


@P("GEN-C07-P06-Hundredfold", "124 · A Hundredfold")
def p06():
    t, h = rows(260, 220, None)
    r1 = new(SKY, W1, h[0], defs("c76a", *ALL) + J7.hundredfold("c76a", W1, h[0], 761),
             cap(v("26:12"), "right: 12px; top: 12px", size=11.5, maxw=340)
             + cap(v("26:13") + " " + v("26:14"), "right: 12px; top: 84px", size=10.5, maxw=340) + hud("×100", "left: 14px; top: 12px", size=28) + vref("GEN 26:12–14", "left: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], defs("c76b", *ALL) + J7.wells_stopped("c76b", W1, h[1], 762),
             cap(v("26:15"), "left: 12px; top: 12px", size=11, maxw=420) + vref("GEN 26:15", "right: 12px; top: 12px"))
    r3 = cols(new(KING, W2, h[2], fc(K.ABIMELECH, h[2]),
                  cap(v("26:16", to="unto Isaac,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("26:16", frm="Go from us"), "right: 8px; top: 40px", 200, size=12.5, pad="20px 20px") + vref("GEN 26:16", "left: 8px; bottom: 8px")),
              new(DUSK, W2, h[2], Y.hills(W2, h[2], h[2] * 0.7, 763, color="#3A2A2E", amp=10) + Z.E4.tent(W2 * 0.4, h[2] * 0.74, W2 * 0.2, h[2] * 0.2, color="#2A1A14")
                  + Z.E4.tent(W2 * 0.64, h[2] * 0.74, W2 * 0.14, h[2] * 0.16, color="#2A1A14"),
                  cap(v("26:17"), "left: 8px; top: 8px", size=11.5, maxw=320) + vref("GEN 26:17", "right: 8px; bottom: 8px")))
    return page("Genesis 26:12–17 — A Hundredfold", t, r1 + r2 + r3, START + 5)


@P("GEN-C07-P07-Rehoboth", "125 · Jehovah Hath Made Room for Us")
def p07():
    t, h = rows(250, 230, None)
    r1 = new(SAND, W1, h[0], defs("c77a", *ALL) + J7.digging("c77a", W1, h[0], 771, xs=(0.7, 0.94), well_x=0.82, top=0.22),
             cap(v("26:18"), "left: 12px; top: 12px", size=10.5, maxw=390)
             + cap(v("26:19"), "left: 12px; bottom: 14px", size=11, maxw=330) + vref("GEN 26:18–19", "right: 12px; bottom: 12px"))
    r2 = new(HOT, W1, h[1], defs("c77b", *ALL) + Z.strife("c77b", W1, h[1], 772),
             cap(v("26:20", to="saying,"), "left: 12px; top: 12px", size=10.5, maxw=330)
             + balloon(v("26:20", frm="The water", to="ours:"), "left: 12px; top: 64px", 200, size=13, pad="16px 18px")
             + cap(v("26:20", frm="and he called"), "right: 12px; bottom: 14px", size=10.5, maxw=300) + vref("GEN 26:20", "left: 12px; bottom: 12px"))
    r3 = new("#1A120A", W1, h[2], J7.strife_wells(W1, h[2], 773),
             cap(v("26:21"), "left: 12px; top: 12px", size=10.5, maxw=320)
             + cap(v("26:22", to="he said,"), "right: 12px; top: 12px", size=10.5, maxw=330)
             + balloon(v("26:22", frm="For now"), "right: 12px; bottom: 12px", 300, size=12, pad="22px 28px") + vref("GEN 26:21–22", "left: 12px; bottom: 12px"))
    return page("Genesis 26:18–22 — Jehovah Hath Made Room for Us", t, r1 + r2 + r3, START + 6)


@P("GEN-C07-P08-Oath", "126 · Thou Art Now the Blessed of Jehovah")
def p08():
    t, h = rows(300, 210, None)
    r1 = new(NIGHT, W1, h[0], defs("c78a", *ALL) + J7.night_altar("c78a", W1, h[0], 781),
             cap(v("26:23"), "left: 12px; top: 12px", size=11)
             + cap(v("26:24", to="and said,"), "left: 12px; top: 50px", size=10.5)
             + god(v("26:24", frm="I am the God"), "left: 12px; top: 84px", size=14, maxw=330)
             + cap(v("26:25"), "right: 12px; top: 12px", size=10.5, maxw=260) + vref("GEN 26:23–25", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], defs("c78b", *ALL) + J7.three_visitors("c78b", W1, h[1], 782),
             cap(v("26:26"), "left: 12px; top: 12px", size=11, maxw=420) + vref("GEN 26:26", "right: 12px; top: 12px"))
    r3 = cols(new(WARM, W2, h[2], fc(J7.ISAAC_GERAR, h[2]),
                  cap(v("26:27", to="unto them,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("26:27", frm="Wherefore"), "right: 8px; top: 40px", 210, size=12, pad="20px 20px") + vref("GEN 26:27", "left: 8px; bottom: 8px")),
              new(KING, W2, h[2], fc(K.ABIMELECH, h[2]),
                  cap(v("26:28", to="they said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("26:28", frm="We saw") + " " + v("26:29"), "right: 8px; top: 40px", 240, size=10.5, pad="26px 24px") + vref("GEN 26:28–29", "left: 8px; bottom: 8px")))
    return page("Genesis 26:23–29 — Thou Art Now the Blessed of Jehovah", t, r1 + r2 + r3, START + 7)


@P("GEN-C07-P09-Shibah", "127 · We Have Found Water")
def p09():
    t, h = rows(230, 250, None)
    r1 = new(DAWN, W1, h[0], defs("c79a", *ALL) + J7.feast_oath("c79a", W1, h[0], 791),
             cap(v("26:30"), "left: 12px; top: 12px", size=11, maxw=300)
             + cap(v("26:31"), "right: 12px; top: 12px", size=10.5, maxw=340) + vref("GEN 26:30–31", "left: 12px; bottom: 10px"))
    r2 = new(SAND, W1, h[1], defs("c79b", *ALL) + J7.digging("c79b", W1, h[1], 792, xs=(0.14, 0.4), well_x=0.27, top=0.34),
             cap(v("26:32", to="said unto him,"), "right: 12px; top: 80px", size=10.5, maxw=330)
             + balloon(v("26:32", frm="We have"), "right: 12px; top: 12px", 200, size=14, pad="16px 18px")
             + cap(v("26:33"), "right: 12px; bottom: 14px", size=11, maxw=300) + vref("GEN 26:32–33", "left: 12px; bottom: 12px"))
    r3 = new("linear-gradient(180deg, #E8D8B0 0%, #B59A7A 100%)", W1, h[2], defs("c79c", *ALL) + J7.hittite_wives("c79c", W1, h[2], 793),
             cap(v("26:34"), "left: 12px; top: 12px", size=11, maxw=420)
             + cap(v("26:35"), "right: 12px; top: 12px", size=11, maxw=200) + vref("GEN 26:34–35", "right: 12px; bottom: 10px"))
    return page("Genesis 26:30–35 — We Have Found Water", t, r1 + r2 + r3, START + 8)


@P("GEN-C07-P10-Venison", "128 · Take Me Venison")
def p10():
    t, h = rows(330, 230, None)
    r1 = use(Bl[0], over=cap(v("27:1", to="My son:"), "right: 12px; top: 12px", size=10.5, maxw=340)
             + cap(v("27:1", frm="and he said unto him, Here", to="unto him,"), "right: 12px; top: 116px", size=10.5)
             + balloon(v("27:1", frm="Here am I."), "right: 12px; top: 150px", 150, size=14, pad="14px 16px") + vref("GEN 27:1", "left: 12px; bottom: 12px"))
    r2 = new(LAMP, W1, h[1], fc(J7.ISAAC_OLD, h[1], w=W1),
             cap(v("27:2", to="said,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("27:2", frm="Behold") + " " + v("27:3") + " " + v("27:4"), "left: 270px; top: 40px", 410, size=12, pad="28px 38px") + vref("GEN 27:2–4", "left: 12px; bottom: 12px"))
    r3 = new(GREEN, W1, h[2], defs("c710c", *ALL) + J7.overheard("c710c", W1, h[2], 7103),
             cap(v("27:5"), "right: 12px; top: 12px", size=11, maxw=380) + vref("GEN 27:5", "left: 12px; bottom: 12px"))
    return page("Genesis 27:1–5 — Take Me Venison", t, r1 + r2 + r3, START + 9)


@P("GEN-C07-P11-Kids", "129 · Obey My Voice")
def p11():
    t, h = rows(380, 250, None)
    r1 = new(GOLDEN, W1, h[0], fc(J7.REBEKAH_URGENT, h[0], w=W1),
             cap(v("27:6", to="saying,"), "left: 320px; top: 12px", size=10.5, maxw=360)
             + balloon(v("27:6", frm="Behold") + " " + v("27:7") + " " + v("27:8"), "left: 270px; top: 66px", 410, size=12.5, pad="32px 40px") + vref("GEN 27:6–8", "left: 12px; bottom: 12px"))
    r2 = new(GREEN, W1, h[1], J7.two_kids(None, W1, h[1], 7112),
             balloon(v("27:9") + " " + v("27:10"), "left: 12px; top: 12px", 420, size=12, pad="26px 36px") + vref("GEN 27:9–10", "right: 12px; top: 12px"))
    r3 = cols(new(BLUE, W2, h[2], fc(J7.JACOB_AFRAID, h[2]),
                  cap(v("27:11", to="his mother,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("27:11", frm="Behold") + " " + v("27:12"), "right: 8px; top: 40px", 240, size=10.5, pad="24px 24px") + vref("GEN 27:11–12", "left: 8px; bottom: 8px")),
              new(GOLDEN, W2, h[2], fc(J7.REBEKAH_URGENT, h[2]),
                  cap(v("27:13", to="unto him,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("27:13", frm="Upon me"), "right: 8px; top: 40px", 210, size=12, pad="22px 22px") + vref("GEN 27:13", "left: 8px; bottom: 8px")))
    return page("Genesis 27:6–13 — Obey My Voice", t, r1 + r2 + r3, START + 10)


@P("GEN-C07-P12-Skins", "130 · The Skins of the Kids of the Goats")
def p12():
    t, h = rows(300, None)
    r1 = new("#3A2214", W1, h[0], defs("c712a", *ALL) + J7.dressing("c712a", W1, h[0], 7121),
             cap(v("27:14"), "left: 12px; top: 12px", size=10.5, maxw=300)
             + cap(v("27:15"), "right: 12px; top: 12px", size=10.5, maxw=300) + vref("GEN 27:14–15", "left: 12px; bottom: 12px"))
    r2 = cols(new(BLUE, W2, h[1], fc(J7.JACOB_AFRAID, h[1]),
                  cap(v("27:16"), "right: 8px; top: 8px", size=11, maxw=230) + vref("GEN 27:16", "left: 8px; bottom: 8px")),
              new("#3A2214", W2, h[1], J7.tent_inside(W2, h[1], 0.35) + J7.bowl(W2 * 0.5, h[1] * 0.76, 2.4) + "".join(
                  f'<ellipse cx="{x}" cy="{h[1] * 0.86:.1f}" rx="26" ry="9" fill="#D9A25A" stroke="#0D0D0F" stroke-width="2"></ellipse>' for x in (70, 270)),
                  cap(v("27:17"), "left: 8px; top: 8px", size=11.5, maxw=320) + vref("GEN 27:17", "right: 8px; bottom: 8px")))
    return page("Genesis 27:14–17 — The Skins of the Kids of the Goats", t, r1 + r2, START + 11)


@P("GEN-C07-P13-Hands", "131 · The Hands Are the Hands of Esau")
def p13():
    t, h = rows(240, 240, 300, None)
    r1 = cols(new(LAMP, W2, h[0], fc(J7.ISAAC_OLD, h[0]),
                  cap(v("27:18", to="said,"), "right: 8px; top: 8px", size=10, maxw=210)
                  + balloon(v("27:18", frm="My father:", to="father:"), "right: 8px; top: 64px", 140, size=12, pad="14px 14px")
                  + cap(v("27:18", frm="and he said", to="said,"), "right: 8px; top: 120px", size=10)
                  + balloon(v("27:18", frm="Here am I;"), "right: 8px; top: 150px", 200, size=12, pad="16px 18px") + vref("GEN 27:18", "left: 8px; bottom: 8px")),
              new(BLUE, W2, h[0], fc(J7.JACOB_AFRAID, h[0]),
                  cap(v("27:19", to="his father,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("27:19", frm="I am Esau"), "right: 8px; top: 40px", 230, size=10.5, pad="22px 22px") + vref("GEN 27:19", "left: 8px; bottom: 8px")))
    r2 = cols(new(LAMP, W2, h[1], fc(J7.ISAAC_OLD, h[1]),
                  cap(v("27:20", to="his son,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("27:20", frm="How is it", to="my son?"), "right: 8px; top: 40px", 200, size=11.5, pad="18px 18px") + vref("GEN 27:20", "left: 8px; bottom: 8px")),
              new(BLUE, W2, h[1], fc(J7.JACOB_AFRAID, h[1]),
                  cap(v("27:20", frm="And he said,", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("27:20", frm="Because"), "right: 8px; top: 40px", 200, size=12, pad="18px 18px")))
    r3 = use(Bl[1], over=cap(v("27:21", to="unto Jacob,"), "left: 12px; top: 12px", size=10.5)
             + balloon(v("27:21", frm="Come near"), "left: 12px; top: 46px", 340, size=12, pad="22px 28px")
             + cap(v("27:22", to="and said,"), "right: 12px; top: 12px", size=10.5, maxw=300)
             + balloon(v("27:22", frm="The voice"), "right: 12px; bottom: 12px", 300, size=14, pad="22px 28px") + vref("GEN 27:21–22", "left: 12px; bottom: 12px"))
    r4 = new(LAMP, W1, h[3], fc(J7.ISAAC_OLD, h[3], w=W1),
             cap(v("27:23"), "left: 300px; top: 12px", size=11, maxw=380)
             + cap(v("27:24", to="And he said,"), "left: 300px; top: 72px", size=10.5)
             + balloon(v("27:24", frm="Art thou", to="Esau?"), "left: 290px; top: 106px", 200, size=12.5, pad="16px 18px")
             + cap(v("27:24", frm="And he said, I", to="said,"), "right: 12px; top: 106px", size=10.5)
             + balloon(v("27:24", frm="I am."), "right: 12px; top: 140px", 110, size=15, pad="12px 12px") + vref("GEN 27:23–24", "left: 12px; bottom: 12px"))
    return page("Genesis 27:18–24 — The Hands Are the Hands of Esau", t, r1 + r2 + r3 + r4, START + 12)


@P("GEN-C07-P14-Blessing", "132 · The Dew of Heaven")
def p14():
    t, h = rows(200, 260, None)
    r1 = new(LAMP, W1, h[0], fc(J7.ISAAC_OLD, h[0], w=W1),
             cap(v("27:25", to="said,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("27:25", frm="Bring it", to="may bless thee."), "left: 280px; top: 40px", 300, size=12, pad="18px 26px")
             + cap(v("27:25", frm="And he brought"), "right: 12px; bottom: 12px", size=10.5, maxw=360) + vref("GEN 27:25", "left: 12px; bottom: 12px"))
    r2 = cols(new("#3A2214", W2, h[1], defs("c714b", *ALL) + J7.kiss("c714b", W2, h[1], 7142),
                  cap(v("27:26", to="unto him,"), "left: 8px; top: 8px", size=10, maxw=320)
                  + balloon(v("27:26", frm="Come near"), "left: 8px; top: 44px", 200, size=12, pad="16px 18px") + vref("GEN 27:26", "right: 8px; bottom: 8px")),
              new(GREEN, W2, h[1], J7.blessed_field(W2, h[1], 7143),
                  cap(v("27:27", to="and said,"), "left: 8px; top: 8px", size=10, maxw=320)
                  + balloon(v("27:27", frm="See, the smell"), "left: 8px; bottom: 8px", 300, size=12, pad="22px 28px") + vref("GEN 27:27", "right: 8px; top: 80px")))
    r3 = new(GOLDEN, W1, h[2], defs("c714c", *ALL) + J7.bows_down("c714c", W1, h[2], 7144),
             balloon(v("27:28") + " " + v("27:29"), "right: 12px; top: 12px", 430, size=12.5, pad="32px 40px") + vref("GEN 27:28–29", "left: 12px; bottom: 12px"))
    return page("Genesis 27:25–29 — The Dew of Heaven", t, r1 + r2 + r3, START + 13)


@P("GEN-C07-P15-Trembled", "133 · Who Art Thou?")
def p15():
    t, h = rows(270, 230, None)
    r1 = new(DUSK, W1, h[0], defs("c715a", *ALL) + J7.came_in("c715a", W1, h[0], 7151),
             cap(v("27:30"), "left: 12px; top: 12px", size=10.5, maxw=440) + vref("GEN 27:30", "right: 12px; bottom: 12px"))
    r2 = cols(new(RED, W2, h[1], fc(J7.ESAU, h[1]),
                  cap(v("27:31", to="unto his father,"), "right: 8px; top: 8px", size=10, maxw=210)
                  + balloon(v("27:31", frm="Let my father"), "right: 8px; top: 80px", 210, size=11, pad="20px 20px") + vref("GEN 27:31", "left: 8px; bottom: 8px")),
              new(LAMP, W2, h[1], fc(J7.ISAAC_OLD, h[1]),
                  cap(v("27:32", to="unto him,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("27:32", frm="Who art thou?", to="thou?"), "right: 8px; top: 40px", 150, size=13, pad="14px 14px")
                  + cap(v("27:32", frm="And he said,", to="said,"), "right: 8px; top: 104px", size=10)
                  + balloon(v("27:32", frm="I am thy son"), "right: 8px; top: 134px", 190, size=12, pad="16px 18px") + vref("GEN 27:32", "left: 8px; bottom: 8px")))
    r3 = new("#3A2214", W1, h[2], J7.trembling(W1, h[2], 7153) + face(J7.ISAAC_TREMBLE, -40, h[2] - 380, 1.0),
             cap(v("27:33", to="and said,"), "left: 320px; top: 12px", size=11)
             + balloon(v("27:33", frm="Who then"), "left: 300px; top: 48px", 380, size=12.5, pad="30px 38px")
             + sfx("ガタガタ", "GATA GATA", "left: 240px; bottom: 20px", size=36, fill="#9A8AFF", stroke="#0D0D0F", rot=-6) + vref("GEN 27:33", "right: 12px; bottom: 12px"))
    return page("Genesis 27:30–33 — Who Art Thou?", t, r1 + r2 + r3, START + 14)


@P("GEN-C07-P16-BitterCry", "134 · An Exceeding Great and Bitter Cry")
def p16():
    t, h = rows(380, 230, None)
    r1 = use(Cry[0], over=cap(v("27:34", to="unto his father,"), "right: 12px; bottom: 14px", size=11, maxw=330)
             + balloon(v("27:34", frm="Bless me"), "right: 12px; top: 120px", 290, size=15, pad="20px 26px")
             + sfx("ウオオオ", "UOOO", "right: 20px; top: 14px", size=56, fill="#F3EFE6", stroke="#0D0D0F", rot=-4) + vref("GEN 27:34", "left: 12px; bottom: 12px"))
    r2 = cols(new(LAMP, W2, h[1], fc(J7.ISAAC_TREMBLE, h[1]),
                  cap(v("27:35", to="he said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("27:35", frm="Thy brother"), "right: 8px; top: 40px", 190, size=12, pad="20px 18px") + vref("GEN 27:35", "left: 8px; bottom: 8px")),
              new(RED, W2, h[1], fc(J7.ESAU_CRY, h[1]),
                  cap(v("27:36", to="he said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("27:36", frm="Is not he", to="my blessing."), "right: 8px; top: 40px", 230, size=10, pad="20px 22px") + vref("GEN 27:36", "left: 8px; bottom: 8px")))
    r3 = new(LAMP, W1, h[2], fc(J7.ISAAC_OLD, h[2], w=W1),
             cap(v("27:36", frm="And he said, Hast", to="said,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("27:36", frm="Hast thou not"), "left: 290px; top: 44px", 220, size=12, pad="16px 18px")
             + cap(v("27:37", to="said unto Esau,"), "right: 12px; top: 12px", size=10.5, maxw=150)
             + balloon(v("27:37", frm="Behold, I have"), "right: 12px; bottom: 12px", 380, size=11, pad="22px 30px") + vref("GEN 27:36–37", "left: 12px; bottom: 12px"))
    return page("Genesis 27:34–37 — An Exceeding Great and Bitter Cry", t, r1 + r2 + r3, START + 15)


@P("GEN-C07-P17-Sword", "135 · By Thy Sword Shalt Thou Live")
def p17():
    t, h = rows(290, 240, None)
    r1 = new(RED, W1, h[0], fc(J7.ESAU_CRY, h[0], w=W1),
             cap(v("27:38", to="unto his father,"), "left: 320px; top: 12px", size=10.5)
             + balloon(v("27:38", frm="Hast thou but", to="O my father."), "left: 290px; top: 46px", 370, size=13, pad="24px 32px")
             + cap(v("27:38", frm="And Esau lifted"), "right: 12px; bottom: 14px", size=12) + vref("GEN 27:38", "left: 12px; bottom: 12px"))
    r2 = new(LAMP, W1, h[1], fc(J7.ISAAC_OLD, h[1], w=W1),
             cap(v("27:39", to="unto him,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("27:39", frm="Behold, of") + " " + v("27:40"), "left: 270px; top: 44px", 410, size=11.5, pad="26px 36px") + vref("GEN 27:39–40", "left: 12px; bottom: 12px"))
    r3 = use(Cry[1], over=cap(v("27:41", to="blessed him:"), "left: 12px; top: 12px", size=11, maxw=330)
             + cap(v("27:41", frm="and Esau said", to="in his heart,"), "left: 12px; top: 92px", size=10.5)
             + balloon(v("27:41", frm="The days of"), "left: 12px; bottom: 12px", 330, size=12.5, pad="22px 30px") + vref("GEN 27:41", "right: 12px; bottom: 12px"))
    return page("Genesis 27:38–41 — By Thy Sword Shalt Thou Live", t, r1 + r2 + r3, START + 16)


@P("GEN-C07-P18-Flee", "136 · Flee Thou to Laban My Brother")
def p18():
    t, h = rows(380, 300, None)
    r1 = new(GOLDEN, W1, h[0], fc(J7.REBEKAH_URGENT, h[0], w=W1),
             cap(v("27:42", to="and said unto him,"), "left: 320px; top: 12px", size=10.5, maxw=360)
             + balloon(v("27:42", frm="Behold, thy") + " " + v("27:43") + " " + v("27:44") + " " + v("27:45"), "left: 260px; top: 104px", 420, size=12, pad="34px 42px")
             + vref("GEN 27:42–45", "left: 12px; bottom: 12px"))
    r2 = use(Cry[2], over=vref("GEN 27:43", "right: 12px; bottom: 12px"))
    r3 = new(LAMP, W1, h[2], fc(J7.REBEKAH_ELDER, h[2], w=W1),
             cap(v("27:46", to="to Isaac,"), "left: 320px; top: 12px", size=10.5)
             + balloon(v("27:46", frm="I am weary"), "left: 290px; top: 46px", 390, size=12, pad="28px 36px")
             + end_mark("NEXT · THE LADDER", "right: 14px; bottom: 12px") + vref("GEN 27:46", "left: 12px; bottom: 12px"))
    return page("Genesis 27:42–46 — Flee Thou to Laban My Brother", t, r1 + r2 + r3, START + 17)
