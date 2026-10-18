"""Genesis volume, Chapter 4 — The Cities of the Plain (Genesis 16–19). Every verse, word for word from ref/asv.
Genesis 17 (the covenant of circumcision) and the darker parts of Genesis 19 (the men of Sodom at Lot's door; Lot's
daughters in the cave) are given in full in the text, while the drawings stay restrained: covenant symbols, the
household gathered, the house at night, the cave from outside."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus5 as V
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from genesis import G, art as X, art2 as Y, art3 as Z, art4 as Q
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import clan, hud, SAND, HOT, BLOOD, GREEN
from mk import defs, face

v, sp = G.v, G.span
B3 = "reference/genesis/book-03/"
Mam, Sod = (panels(B3 + n + ".dc.html") for n in ["B3-P05-Mamre", "B3-P06-Sodom"])
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
TENT = "linear-gradient(180deg, #FFE3B8 0%, #E8C88A 100%)"
EMBER = "radial-gradient(circle at 30% 40%, #FFC14D 0 20px, #B5421E 200px, #2A0A0A 460px)"
GLOW = "radial-gradient(circle at 70% 30%, #FFF4C2 0 30px, #FFC14D 160px, #8A4A3A 420px)"
COLD = "radial-gradient(circle at 70% 30%, #CFE0FF 0 20px, #4A3A8E 180px, #0B0B2A 400px)"
DOORWAY = "linear-gradient(180deg, #12090A 0%, #3A1E14 100%)"
START = 65                                   # chapter 3 ends on page 64
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def cosmic(w, h, cx=None): return X.cosmic(w, h, cx)

def fc(tok, h, w=W2, flip=False, s=None):
    """A close-up face sized to its panel: as large as the panel allows (up to scale 1), standing on the bottom edge,
    so the eyes stay in the upper middle, clear of the captions."""
    s = s or round(min(1.0, (h + 10) / 380), 3)
    return face(tok, (w + 40) if flip else -40, round(h - 380 * s + 8), s, flip=flip)


@P("GEN-C04-00-Title", "Chapter 4 · The Cities of the Plain")
def title():
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#1A0408"></rect>' + V.rays(380, 940, 40, 60, 1100, color="#FF6A2A", op=0.25)
           + Z.sun(380, 940, 160, color="#D7261E", glow="#FF8A3D", op=0.2)
           + Y.city(380, 950, 820, 360, 7, color="#0D0306", lit="#FF6A2A", wall="#1A0408")
           + "".join(f'<path d="M{x} -20 L {x - 60} 700" stroke="#FFD23F" stroke-width="3" opacity="0.6"></path>' for x in range(60, 900, 70))
           + Y.ground(760, 1080, 950, "#0D0306", dy=0))
    return chapter_title(4, "第四話", "The Cities of the Plain", "Genesis 16 – 19", svg, BLOOD,
                         v("18:14", to="Jehovah?"), "Genesis · Volume One")


@P("GEN-C04-P01-Hagar", "65 · Sarai's Handmaid")
def p01():
    t, h = rows(250, 300, None)
    r1 = new(TENT, W1, h[0], defs("c41a", *ALL) + Q.tent_women("c41a", W1, h[0], 411),
             cap(v("16:1"), "right: 12px; top: 12px", size=11.5, maxw=330) + vref("GEN 16:1", "left: 12px; bottom: 12px"))
    r2 = new(EMBER, W1, h[1], fc(Z.SARAI_SAD, h[1]),
             cap(v("16:2", to="unto Abram,"), "left: 320px; top: 12px", size=10.5)
             + balloon(v("16:2", frm="Behold now", to="by her."), "left: 300px; top: 48px", 370, size=13, pad="26px 34px")
             + cap(v("16:2", frm="And Abram hearkened"), "right: 12px; bottom: 14px", size=11, maxw=320) + vref("GEN 16:2", "left: 12px; bottom: 12px"))
    r3 = cols(new(TENT, W2, h[2], defs("c41c", *ALL) + Q.given("c41c", W2, h[2], 413),
                  cap(v("16:3"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 16:3", "right: 8px; bottom: 8px")),
              new("radial-gradient(circle at 70% 30%, #FFE680 0 20px, #E8A35A 180px, #5A2A16 420px)", W2, h[2], fc(Q.HAGAR, h[2]),
                  cap(v("16:4"), "right: 8px; top: 8px", size=11, maxw=200) + vref("GEN 16:4", "right: 8px; bottom: 8px")))
    return page("Genesis 16:1–4 — Sarai's Handmaid", t, r1 + r2 + r3, START + 0)


@P("GEN-C04-P02-Fountain", "66 · By a Fountain of Water")
def p02():
    t, h = rows(260, 240, 240, None)
    r1 = new(EMBER, W1, h[0], fc(Q.SARAI_HURT, h[0]),
             cap(v("16:5", to="unto Abram,"), "left: 320px; top: 12px", size=10.5)
             + balloon(v("16:5", frm="My wrong"), "left: 290px; top: 48px", 380, size=13, pad="28px 36px") + vref("GEN 16:5", "left: 12px; bottom: 12px"))
    r2 = cols(new(GLOW, W2, h[1], face(Q.ABRAHAM_GRAVE, -40, -10, 0.7),
                  cap(v("16:6", to="unto Sarai,"), "right: 8px; top: 8px", size=10.5)
                  + balloon(v("16:6", frm="Behold", to="thine eyes."), "right: 8px; top: 44px", 200, size=12, pad="20px 20px") + vref("GEN 16:6", "left: 8px; bottom: 8px")),
              new(HOT, W2, h[1], defs("c42b", *ALL) + Q.flight("c42b", W2, h[1], 422),
                  cap(v("16:6", frm="And Sarai dealt"), "left: 8px; top: 8px", size=11, maxw=320)
                  + sfx("ダッ", "DAH", "right: 14px; bottom: 30px", size=40, fill="#D7261E", stroke="#F3EFE6", rot=-6)))
    r3 = new(SAND, W1, h[2], defs("c42c", *ALL) + Q.fountain("c42c", W1, h[2], 423),
             cap(v("16:7"), "left: 12px; top: 12px", size=11.5, maxw=360) + vref("GEN 16:7", "left: 12px; bottom: 12px"))
    r4 = cols(new(NIGHT, W2, h[3], cosmic(W2, h[3]),
                  cap(v("16:8", to="said,"), "left: 8px; top: 8px", size=10)
                  + god(v("16:8", frm="Hagar,", to="goest thou?"), "left: 8px; top: 42px", size=15, maxw=320)
                  + cap(v("16:9", to="unto her,"), "left: 8px; bottom: 76px", size=10, maxw=320)
                  + god(v("16:9", frm="Return"), "left: 8px; bottom: 8px", size=13, maxw=320) + vref("GEN 16:8–9", "right: 8px; top: 8px")),
              new("radial-gradient(circle at 70% 30%, #CFEFFF 0 20px, #5A8AAA 180px, #12305A 400px)", W2, h[3], fc(Q.HAGAR_WEEP, h[3]),
                  cap(v("16:8", frm="And she said,", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("16:8", frm="I am fleeing"), "right: 8px; top: 42px", 190, size=12, pad="20px 20px")))
    return page("Genesis 16:5–9 — By a Fountain of Water", t, r1 + r2 + r3 + r4, START + 1)


@P("GEN-C04-P03-Ishmael", "67 · Thou Art a God That Seeth")
def p03():
    t, h = rows(200, 230, 260, None)
    r1 = new(NIGHT, W1, h[0], cosmic(W1, h[0]),
             cap(v("16:10", to="unto her,"), "left: 12px; top: 12px", size=10.5)
             + god(v("16:10", frm="I will"), "left: 12px; top: 46px", size=17, maxw=520)
             + cap(v("16:11", to="unto her,"), "right: 12px; bottom: 12px", size=10.5) + vref("GEN 16:10", "left: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], Q.wild_ass(W1, h[1], 432),
             god(v("16:11", frm="Behold") + " " + v("16:12"), "left: 12px; top: 12px", size=13.5, maxw=430) + vref("GEN 16:11–12", "right: 12px; bottom: 12px"))
    r3 = cols(new("radial-gradient(circle at 70% 30%, #FFF4C2 0 30px, #FFC14D 160px, #8A4A3A 420px)", W2, h[2], fc(Q.HAGAR, h[2]),
                  cap(v("16:13", to="unto her,"), "right: 8px; top: 8px", size=10, maxw=190)
                  + balloon(v("16:13", frm="Thou art", to="seeth:"), "right: 8px; top: 80px", 170, size=13, pad="18px 16px")
                  + vref("GEN 16:13", "left: 8px; top: 8px")),
              new("#1A120A", W2, h[2], Q.well_roi(W2, h[2], 433),
                  cap(v("16:13", frm="for she said,", to="said,"), "left: 8px; top: 8px", size=10)
                  + balloon(v("16:13", frm="Have I"), "left: 8px; top: 40px", 220, size=11.5, pad="16px 18px")
                  + cap(v("16:14"), "left: 8px; bottom: 8px", size=10, maxw=320) + vref("GEN 16:14", "right: 8px; top: 8px")))
    r4 = new(TENT, W1, h[3], defs("c43d", *ALL) + Q.father_and_son("c43d", W1, h[3], 434),
             cap(v("16:15"), "right: 12px; top: 12px", size=11.5, maxw=330)
             + cap(v("16:16"), "right: 12px; top: 92px", size=11.5, maxw=330) + hud("86", "left: 14px; top: 12px", color="#D7261E", size=30)
             + vref("GEN 16:15–16", "left: 12px; bottom: 12px"))
    return page("Genesis 16:10–16 — Thou Art a God That Seeth", t, r1 + r2 + r3 + r4, START + 2)


@P("GEN-C04-P04-Almighty", "68 · I Am God Almighty")
def p04():
    t, h = rows(280, 150, 220, None)
    r1 = cols(new("radial-gradient(circle at 70% 30%, #FFFDF0 0 30px, #FFE680 160px, #8A6A3A 420px)", W2, h[0], fc(Q.ABRAHAM_AWE, h[0]),
                  cap(v("17:1", to="said unto him,"), "right: 8px; top: 8px", size=10.5, maxw=200) + hud("99", "right: 10px; bottom: 10px", size=30)),
              new(NIGHT, W2, h[0], cosmic(W2, h[0]), god(v("17:1", frm="I am God"), "left: 8px; top: 8px", size=24, maxw=320) + vref("GEN 17:1", "right: 8px; bottom: 8px")))
    r2 = new(NIGHT, W1, h[1], cosmic(W1, h[1]), god(v("17:2"), "left: 12px; top: 12px", size=19, maxw=640) + vref("GEN 17:2"))
    r3 = new(NIGHT, W1, h[2], Q.fallen(None, W1, h[2], 443),
             cap(v("17:3"), "left: 12px; top: 12px", size=12, maxw=330) + vref("GEN 17:3", "right: 12px; bottom: 12px"))
    r4 = cols(new("#12113A", W2, h[3], Q.renamed(W2, h[3], "ABRAM", "ABRAHAM"),
                  god(v("17:4"), "left: 8px; top: 8px", size=13, maxw=320) + vref("GEN 17:4–5", "right: 8px; bottom: 8px")),
              new(NIGHT, W2, h[3], Q.kings_of_thee(W2, h[3], 444),
                  god(v("17:5"), "left: 8px; top: 8px", size=13.5, maxw=320)
                  + god(v("17:6"), "right: 8px; bottom: 8px", size=13, maxw=260) + vref("GEN 17:6", "left: 8px; bottom: 8px")))
    return page("Genesis 17:1–6 — I Am God Almighty", t, r1 + r2 + r3 + r4, START + 3)


@P("GEN-C04-P05-Covenant", "69 · An Everlasting Covenant")
def p05():
    t, h = rows(260, 240, None)
    r1 = new(NIGHT, W1, h[0], Q.covenant_seal(W1, h[0], 451),
             god(v("17:7"), "left: 12px; top: 12px", size=15, maxw=380) + vref("GEN 17:7", "right: 12px; bottom: 12px"))
    r2 = new("#0B1A2E", W1, h[1], Z.land_grant(W1, h[1], 452),
             god(v("17:8"), "right: 12px; top: 12px", size=15, maxw=340) + vref("GEN 17:8", "right: 12px; bottom: 12px"))
    r3 = cols(new(NIGHT, W2, h[2], cosmic(W2, h[2]),
                  cap(v("17:9", to="unto Abraham,"), "left: 8px; top: 8px", size=10.5)
                  + god(v("17:9", frm="And as for"), "left: 8px; top: 46px", size=15, maxw=320) + vref("GEN 17:9", "right: 8px; bottom: 8px")),
              new("#12113A", W2, h[2], Q.covenant_seal(W2, h[2], 453),
                  god(v("17:10") + " " + v("17:11"), "left: 8px; top: 8px", size=14, maxw=320) + vref("GEN 17:10–11", "right: 8px; bottom: 8px")))
    return page("Genesis 17:7–11 — An Everlasting Covenant", t, r1 + r2 + r3, START + 4)


@P("GEN-C04-P06-Sarah", "70 · Sarah Shall Her Name Be")
def p06():
    t, h = rows(270, 200, None)
    r1 = new(DUSK, W1, h[0], defs("c46a", *ALL) + Q.household("c46a", W1, h[0], 461),
             god(v("17:12") + " " + v("17:13"), "left: 12px; top: 12px", size=13.5, maxw=520) + vref("GEN 17:12–13", "right: 12px; bottom: 12px"))
    r2 = new("#2A1A2E", W1, h[1], defs("c46b", *ALL) + Q.cut_off("c46b", W1, h[1], 462),
             god(v("17:14"), "right: 12px; top: 12px", size=14, maxw=360) + vref("GEN 17:14", "left: 12px; top: 12px"))
    r3 = cols(new("#12113A", W2, h[2], Q.renamed(W2, h[2], "SARAI", "SARAH"),
                  cap(v("17:15", to="unto Abraham,"), "left: 8px; top: 8px", size=10.5)
                  + god(v("17:15", frm="As for Sarai"), "left: 8px; top: 44px", size=14, maxw=320) + vref("GEN 17:15", "right: 8px; bottom: 8px")),
              new(GLOW, W2, h[2], fc(Q.SARAH, h[2]),
                  god(v("17:16"), "right: 8px; top: 8px", size=13, maxw=230) + vref("GEN 17:16", "right: 8px; bottom: 8px")))
    return page("Genesis 17:12–16 — Sarah Shall Her Name Be", t, r1 + r2 + r3, START + 5)


@P("GEN-C04-P07-Laughed", "71 · Abraham Fell upon His Face, and Laughed")
def p07():
    t, h = rows(290, 220, 150, None)
    r1 = new(GLOW, W1, h[0], fc(Q.ABRAHAM_LAUGH, h[0]),
             cap(v("17:17", to="in his heart,"), "left: 320px; top: 12px", size=10.5, maxw=360)
             + balloon(v("17:17", frm="Shall a child"), "left: 300px; top: 66px", 360, size=13.5, pad="28px 36px")
             + hud("100", "right: 14px; bottom: 14px", size=26) + hud("90", "right: 100px; bottom: 14px", color="#8A3A5A", size=26)
             + sfx("フッ", "FU", "left: 220px; top: 20px", size=36, fill="#FFD23F", stroke="#0D0D0F", rot=-8) + vref("GEN 17:17", "left: 12px; bottom: 12px"))
    r2 = cols(new("radial-gradient(circle at 70% 30%, #FFE680 0 20px, #C8885A 180px, #3A2214 400px)", W2, h[1], face(Q.ABRAHAM_GRAVE, -40, -10, 0.62),
                  cap(v("17:18", to="unto God,"), "right: 8px; top: 8px", size=10.5)
                  + balloon(v("17:18", frm="Oh that"), "right: 8px; top: 44px", 160, size=12.5, pad="18px 14px") + vref("GEN 17:18", "right: 8px; bottom: 8px")),
              new(NIGHT, W2, h[1], cosmic(W2, h[1]),
                  cap(v("17:19", to="God said,"), "left: 8px; top: 8px", size=10)
                  + god(v("17:19", frm="Nay"), "left: 8px; top: 40px", size=13, maxw=320) + vref("GEN 17:19", "right: 8px; bottom: 8px")))
    r3 = new(NIGHT, W1, h[2], Q.twelve_princes(W1, h[2], 473),
             god(v("17:20"), "left: 12px; top: 10px", size=13, maxw=420) + vref("GEN 17:20", "right: 12px; top: 10px"))
    r4 = cols(new(NIGHT, W2, h[3], cosmic(W2, h[3]), god(v("17:21"), "left: 8px; top: 8px", size=15, maxw=320) + vref("GEN 17:21", "right: 8px; bottom: 8px")),
              new("#0B0B2A", W2, h[3], Q.going_up(W2, h[3], 474), cap(v("17:22"), "left: 8px; top: 8px", size=11.5, maxw=230) + vref("GEN 17:22", "right: 8px; bottom: 8px")))
    return page("Genesis 17:17–22 — Abraham Fell upon His Face, and Laughed", t, r1 + r2 + r3 + r4, START + 6)


@P("GEN-C04-P08-Selfsame", "72 · In the Selfsame Day")
def p08():
    t, h = rows(330, 240, None)
    r1 = new(DUSK, W1, h[0], defs("c48a", *ALL) + Q.household("c48a", W1, h[0], 481, n=22),
             cap(v("17:23"), "left: 12px; top: 12px", size=11.5, maxw=500) + vref("GEN 17:23", "right: 12px; bottom: 12px"))
    r2 = cols(new("radial-gradient(circle at 70% 30%, #FFE680 0 20px, #C8885A 180px, #3A2214 400px)", W2, h[1], fc(Q.ABRAHAM, h[1]),
                  cap(v("17:24"), "right: 8px; top: 8px", size=11, maxw=180) + hud("99", "right: 10px; bottom: 10px", size=30)),
              new(SAND, W2, h[1], defs("c48b", *ALL) + Y.ground(W2, h[1], h[1] * 0.88, "#C8A06A", dy=0)
                  + Z.man("c48b", W2 * 0.7, h[1] * 0.88, Y.fit(h[1] * 0.88, h[1] * 0.44), "#5A6A3A"),
                  cap(v("17:25"), "left: 8px; top: 8px", size=11, maxw=200) + hud("13", "left: 10px; bottom: 10px", size=30) + vref("GEN 17:24–25", "right: 8px; bottom: 8px")))
    r3 = new(DAWN, W1, h[2], defs("c48c", *ALL) + Q.household("c48c", W1, h[2], 483, n=26),
             cap(v("17:26"), "left: 12px; top: 12px", size=12.5, maxw=380)
             + cap(v("17:27"), "right: 12px; bottom: 14px", size=11, maxw=360) + vref("GEN 17:26–27", "left: 12px; bottom: 12px"))
    return page("Genesis 17:23–27 — In the Selfsame Day", t, r1 + r2 + r3, START + 7)


@P("GEN-C04-P09-Mamre", "73 · Three Men Stood over against Him")
def p09():
    t, h = rows(320, 230, None)
    r1 = use(Mam[0], over=cap(v("18:1") + " " + v("18:2", to="against him:"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("GEN 18:1–2", "left: 12px; bottom: 12px"))
    r2 = new(TENT, W1, h[1], defs("c49b", *ALL) + Q.bowing("c49b", W1, h[1], 492),
             cap(v("18:2", frm="and when he saw"), "left: 12px; top: 12px", size=11, maxw=330) + vref("GEN 18:2", "right: 12px; top: 12px"))
    r3 = new(GLOW, W1, h[2], fc(Q.ABRAHAM_AWE, h[2]),
             cap(v("18:3", to="and said,"), "left: 320px; top: 12px", size=10.5)
             + balloon(v("18:3", frm="My lord") + " " + v("18:4") + " " + v("18:5", to="your servant."), "left: 280px; top: 46px", 400, size=12.5, pad="30px 40px")
             + cap(v("18:5", frm="And they said,", to="said,"), "right: 12px; bottom: 74px", size=10.5)
             + balloon(v("18:5", frm="So do"), "right: 12px; bottom: 12px", 230, size=13, pad="18px 22px") + vref("GEN 18:3–5", "left: 12px; bottom: 12px"))
    return page("Genesis 18:1–5 — Three Men Stood over against Him", t, r1 + r2 + r3, START + 8)


@P("GEN-C04-P10-Meal", "74 · Under the Tree")
def p10():
    t, h = rows(250, 200, 280, None)
    r1 = cols(new("#3A2214", W2, h[0], defs("c410a", *ALL) + Q.kneading("c410a", W2, h[0], 4101),
                  cap(v("18:6", to="and said,"), "left: 8px; top: 8px", size=10, maxw=320)
                  + balloon(v("18:6", frm="Make ready"), "right: 8px; top: 62px", 200, size=12, pad="18px 18px") + vref("GEN 18:6", "right: 8px; top: 8px")),
              new(GREEN, W2, h[0], defs("c410b", *ALL) + Q.to_the_herd("c410b", W2, h[0], 4102),
                  cap(v("18:7"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 18:7", "right: 8px; bottom: 8px")))
    r2 = new(GREEN, W1, h[1], defs("c410c", *ALL) + Q.meal_under_tree("c410c", W1, h[1], 4103),
             cap(v("18:8"), "left: 12px; top: 12px", size=11, maxw=420) + vref("GEN 18:8", "right: 12px; top: 12px"))
    r3 = new(GLOW, W1, h[2], fc(Q.ABRAHAM, h[2], w=W1, flip=True),
             cap(v("18:9", to="unto him,"), "left: 12px; top: 12px", size=10.5)
             + balloon(v("18:9", frm="Where is", to="wife?"), "left: 12px; top: 46px", 230, size=13, pad="18px 22px")
             + cap(v("18:9", frm="And he said,", to="said,"), "left: 270px; top: 12px", size=10.5)
             + balloon(v("18:9", frm="Behold, in"), "left: 260px; top: 46px", 170, size=13, pad="16px 18px")
             + cap(v("18:10", to="he said,"), "left: 12px; bottom: 84px", size=10.5)
             + god(v("18:10", frm="I will certainly", to="have a son."), "left: 12px; bottom: 12px", size=14, maxw=420) + vref("GEN 18:9–10", "right: 12px; top: 12px"))
    r4 = new(DOORWAY, W1, h[3], Q.heard_behind(None, W1, h[3], 4104),
             cap(v("18:10", frm="And Sarah heard"), "right: 12px; top: 12px", size=12, maxw=330) + vref("GEN 18:10", "right: 12px; bottom: 12px"))
    return page("Genesis 18:6–10 — Under the Tree", t, r1 + r2 + r3 + r4, START + 9)


@P("GEN-C04-P11-TooHard", "75 · Is Anything Too Hard for Jehovah?")
def p11():
    t, h = rows(140, 320, 290, None)
    r1 = new(DUSK, W1, h[0], mk.stars(40, W1, h[0], 4111) + Y.ground(W1, h[0], h[0] * 0.8, "#2A1A2E", dy=0),
             cap(v("18:11"), "left: 12px; top: 12px", size=12, maxw=640) + vref("GEN 18:11", "right: 12px; bottom: 10px"))
    r2 = cols(new("linear-gradient(90deg, #3A2214 0%, #C8885A 100%)", W2, h[1], fc(Q.SARAH_LAUGH, h[1]) + "".join(f'<path d="M{x} -10 L {x + 30} 400" stroke="#2A1408" stroke-width="8"></path>' for x in (280, 310)),
                  cap(v("18:12", to="saying,"), "left: 8px; bottom: 120px", size=10, maxw=320)
                  + balloon(v("18:12", frm="After I"), "left: 8px; bottom: 10px", 300, size=12, pad="20px 26px")
                  + sfx("ふふっ", "FUFU", "right: 30px; top: 14px", size=34, fill="#FFD23F", stroke="#0D0D0F", rot=-6) + vref("GEN 18:12", "left: 8px; top: 8px")),
              new(NIGHT, W2, h[1], cosmic(W2, h[1]),
                  cap(v("18:13", to="unto Abraham,"), "left: 8px; top: 8px", size=10.5)
                  + god(v("18:13", frm="Wherefore") + " " + v("18:14"), "left: 8px; top: 44px", size=15, maxw=320) + vref("GEN 18:13–14", "right: 8px; bottom: 8px")))
    r3 = new("radial-gradient(circle at 30% 40%, #E8D8C8 0 20px, #8A6A7A 180px, #2A1A2E 380px)", W1, h[2], fc(Q.SARAH_AFRAID, h[2]),
             cap(v("18:15", to="saying,"), "left: 320px; top: 12px", size=10.5)
             + balloon(v("18:15", frm="I laughed", to="not;"), "left: 310px; top: 48px", 200, size=15, pad="18px 22px")
             + cap(v("18:15", frm="for she", to="afraid."), "right: 12px; bottom: 14px", size=12) + vref("GEN 18:15", "left: 12px; bottom: 12px"))
    r4 = new(NIGHT, W1, h[3], cosmic(W1, h[3]),
             cap(v("18:15", frm="And he said,", to="said,"), "left: 12px; top: 12px", size=10.5)
             + god(v("18:15", frm="Nay;"), "left: 12px; top: 46px", size=26, maxw=640))
    return page("Genesis 18:11–15 — Is Anything Too Hard for Jehovah?", t, r1 + r2 + r3 + r4, START + 10)


@P("GEN-C04-P12-Cry", "76 · The Cry of Sodom")
def p12():
    t, h = rows(230, 330, None)
    r1 = new(SKY, W1, h[0], defs("c412a", *ALL) + Q.toward_sodom("c412a", W1, h[0], 4121),
             cap(v("18:16"), "right: 12px; top: 12px", size=11, maxw=330) + vref("GEN 18:16", "left: 12px; bottom: 12px"))
    r2 = new(NIGHT, W1, h[1], cosmic(W1, h[1]),
             cap(v("18:17", to="said,"), "left: 12px; top: 12px", size=10.5)
             + god(v("18:17", frm="Shall I hide") + " " + v("18:18") + " " + v("18:19"), "left: 12px; top: 46px", size=15.5, maxw=660) + vref("GEN 18:17–19"))
    r3 = new("#2A0A0E", W1, h[2], Q.cry_of_sodom(W1, h[2], 4123),
             cap(v("18:20", to="said,"), "left: 12px; top: 12px", size=10.5)
             + god(v("18:20", frm="Because") + " " + v("18:21"), "left: 12px; top: 46px", size=15, maxw=470)
             + sfx("ゴオオ", "GOOO", "right: 26px; top: 20px", size=42, fill="#D7261E", stroke="#F3EFE6", rot=6) + vref("GEN 18:20–21", "right: 12px; bottom: 12px"))
    return page("Genesis 18:16–21 — The Cry of Sodom", t, r1 + r2 + r3, START + 11)


@P("GEN-C04-P13-Fifty", "77 · Peradventure There Are Fifty")
def p13():
    t, h = rows(190, 320, 150, None)
    r1 = new(GREY, W1, h[0], defs("c413a", *ALL) + Q.stood_before("c413a", W1, h[0], 4131),
             cap(v("18:22"), "right: 12px; top: 12px", size=11.5, maxw=400) + vref("GEN 18:22", "left: 12px; bottom: 10px"))
    r2 = new(EMBER, W1, h[1], fc(Q.ABRAHAM_PLEAD, h[1]),
             cap(v("18:23", to="said,"), "left: 320px; top: 12px", size=10.5)
             + balloon(v("18:23", frm="Wilt thou") + " " + v("18:24") + " " + v("18:25"), "left: 280px; top: 46px", 400, size=12.5, pad="32px 40px") + vref("GEN 18:23–25", "left: 12px; bottom: 12px"))
    r3 = cols(new("#12113A", W2, h[2], Q.countdown(W2, h[2], 50), vref("GEN 18:26", "right: 8px; top: 8px")),
              new(NIGHT, W2, h[2], cosmic(W2, h[2]), cap(v("18:26", to="said,"), "left: 8px; top: 8px", size=10)
                  + god(v("18:26", frm="If I find"), "left: 8px; top: 38px", size=13, maxw=320)))
    r4 = cols(new(NIGHT, W2, h[3], Q.dust_ashes(W2, h[3], 4134),
                  cap(v("18:27", to="said,"), "left: 8px; top: 8px", size=10)
                  + balloon(v("18:27", frm="Behold now") + " " + v("18:28", to="lack of five?"), "left: 8px; top: 40px", 320, size=11.5, pad="24px 30px") + vref("GEN 18:27–28", "right: 8px; bottom: 8px")),
              new("#12113A", W2, h[3], Q.countdown(W2, h[3], 45, prev=50),
                  cap(v("18:28", frm="And he said,", to="said,"), "left: 8px; top: 8px", size=10)
                  + god(v("18:28", frm="I will not"), "left: 8px; top: 38px", size=13, maxw=320)))
    return page("Genesis 18:22–28 — Peradventure There Are Fifty", t, r1 + r2 + r3 + r4, START + 12)


def plead(ref, n, prev, opener_to, ask_frm, ask_to, reply_frm, size=12):
    """One round of the pleading: Abraham's balloon over the dust, and Jehovah's answer over the counter."""
    hh = 200
    left = new(EMBER, W2, hh, face(Q.ABRAHAM_PLEAD, -96, -40, 0.78),
               cap(v(ref, to=opener_to), "right: 8px; top: 8px", size=10)
               + balloon(v(ref, frm=ask_frm, to=ask_to), "right: 8px; top: 40px", 210, size=size, pad="20px 22px") + vref(f"GEN {ref}", "left: 8px; bottom: 8px"))
    right = new("#12113A", W2, hh, Q.countdown(W2, hh, n, prev=prev, compact=True),
                cap(v(ref, frm=reply_frm, to="said,"), "left: 8px; top: 8px", size=10)
                + god(v(ref, frm="I will not"), "left: 8px; top: 38px", size=13, maxw=200))
    return cols(left, right)


@P("GEN-C04-P14-Ten", "78 · For the Ten's Sake")
def p14():
    t = "200px 200px 200px 200px minmax(0, 1fr)"
    r1 = plead("18:29", 40, 45, "and said,", "Peradventure", "found there.", "And he said,")
    r2 = plead("18:30", 30, 40, "said,", "Oh let", "found there.", "And he said, I will")
    r3 = plead("18:31", 20, 30, "said,", "Behold now", "found there.", "And he said, I will")
    r4 = plead("18:32", 10, 20, "said,", "Oh let", "found there.", "And he said, I will")
    hh = 1022 - 48 - 800 - 6
    r5 = new(DUSK, W1, hh, defs("c414e", *ALL) + Q.returned("c414e", W1, hh, 4145),
             cap(v("18:33"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("GEN 18:33", "right: 12px; bottom: 10px"))
    return page("Genesis 18:29–33 — For the Ten's Sake", t, r1 + r2 + r3 + r4 + r5, START + 13)


@P("GEN-C04-P15-Gate", "79 · Lot Sat in the Gate of Sodom")
def p15():
    t, h = rows(300, 280, None)
    r1 = new("linear-gradient(180deg, #4A1D55 0%, #C2456A 60%, #FF8A3D 100%)", W1, h[0], defs("c415a", *ALL) + Q.city_gate("c415a", W1, h[0], 4151),
             cap(v("19:1"), "right: 12px; top: 12px", size=11, maxw=330) + vref("GEN 19:1", "left: 12px; bottom: 12px"))
    r2 = new(EMBER, W1, h[1], fc(Q.LOT, h[1]),
             cap(v("19:2", to="and he said,"), "left: 320px; top: 12px", size=10.5)
             + balloon(v("19:2", frm="Behold now", to="your way."), "left: 290px; top: 46px", 380, size=12.5, pad="26px 36px")
             + cap(v("19:2", frm="And they said,", to="said,"), "right: 12px; bottom: 76px", size=10.5)
             + balloon(v("19:2", frm="Nay;"), "right: 12px; bottom: 12px", 280, size=12.5, pad="18px 24px") + vref("GEN 19:2", "left: 12px; bottom: 12px"))
    r3 = new("#3A1E14", W1, h[2], defs("c415c", *ALL) + Q.feast("c415c", W1, h[2], 4153),
             cap(v("19:3"), "left: 12px; top: 12px", size=11.5, maxw=440) + vref("GEN 19:3", "right: 12px; top: 12px"))
    return page("Genesis 19:1–3 — Lot Sat in the Gate of Sodom", t, r1 + r2 + r3, START + 14)


@P("GEN-C04-P16-Door", "80 · They Compassed the House Round")
def p16():
    t, h = rows(290, 300, None)
    r1 = new("linear-gradient(180deg, #05050A 0%, #2A0A1A 100%)", W1, h[0], defs("c416a", *ALL) + Q.mob_at_door("c416a", W1, h[0], 4161),
             cap(v("19:4"), "left: 12px; top: 12px", size=11, maxw=300)
             + cap(v("19:5", to="said unto him,"), "right: 12px; top: 12px", size=10.5, maxw=230)
             + balloon(v("19:5", frm="Where are"), "right: 12px; top: 70px", 250, size=12, pad="22px 24px")
             + sfx("ドンドン", "DON DON", "left: 24px; bottom: 24px", size=44, fill="#D7261E", stroke="#F3EFE6", rot=-6) + vref("GEN 19:4–5", "right: 12px; bottom: 12px"))
    r2 = cols(new("#4A3A2E", W2, h[1], defs("c416b", *ALL) + Q.at_the_door("c416b", W2, h[1], 4162),
                  cap(v("19:6"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 19:6", "right: 8px; bottom: 8px")),
              new(EMBER, W2, h[1], face(Q.LOT_FEAR, -60, -30, 0.7),
                  cap(v("19:7", to="he said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("19:7", frm="I pray") + " " + v("19:8"), "left: 8px; bottom: 8px", 326, size=11, pad="22px 34px") + vref("GEN 19:7–8", "left: 8px; top: 8px")))
    r3 = new("linear-gradient(180deg, #05050A 0%, #2A0A1A 100%)", W1, h[2], defs("c416c", *ALL) + Q.mob_at_door("c416c", W1, h[2], 4163),
             cap(v("19:9", to="said,"), "left: 12px; top: 12px", size=10.5)
             + balloon(v("19:9", frm="Stand back.", to="back."), "left: 12px; top: 46px", 180, size=15, pad="16px 20px")
             + cap(v("19:9", frm="And they said, This", to="said,"), "right: 12px; top: 12px", size=10.5)
             + balloon(v("19:9", frm="This one fellow", to="than with them."), "right: 12px; top: 46px", 330, size=12, pad="24px 30px")
             + cap(v("19:9", frm="And they pressed"), "left: 12px; bottom: 14px", size=11, maxw=420) + vref("GEN 19:9", "right: 12px; bottom: 12px"))
    return page("Genesis 19:4–9 — They Compassed the House Round", t, r1 + r2 + r3, START + 15)


@P("GEN-C04-P17-Blindness", "81 · Bring Them out of the Place")
def p17():
    t, h = rows(230, 190, 280, None)
    r1 = new("#4A3A2E", W1, h[0], defs("c417a", *ALL) + Q.pulled_in("c417a", W1, h[0], 4171),
             cap(v("19:10"), "right: 12px; bottom: 14px", size=11.5, maxw=230) + vref("GEN 19:10", "left: 12px; bottom: 12px"))
    r2 = new("#FFFDF0", W1, h[1], defs("c417b", *ALL) + Q.blindness("c417b", W1, h[1], 4172),
             cap(v("19:11"), "left: 12px; top: 12px", size=11.5, maxw=500)
             + sfx("カッ", "KAH", "right: 30px; top: 14px", size=52, fill="#FFD23F", stroke="#0D0D0F", rot=6) + vref("GEN 19:11", "right: 12px; bottom: 10px"))
    r3 = new("#3A1E14", W1, h[2], defs("c417c", *ALL) + Q.feast("c417c", W1, h[2], 4173),
             cap(v("19:12", to="unto Lot,"), "left: 12px; top: 12px", size=10.5)
             + balloon(v("19:12", frm="Hast thou") + " " + v("19:13"), "left: 12px; top: 46px", 420, size=12.5, pad="28px 40px") + vref("GEN 19:12–13", "right: 12px; top: 12px"))
    r4 = new(NIGHT, W1, h[3], defs("c417d", *ALL) + Q.mockers("c417d", W1, h[3], 4174),
             cap(v("19:14", to="and said,"), "left: 12px; top: 12px", size=10.5, maxw=440)
             + balloon(v("19:14", frm="Up, get", to="the city."), "left: 12px; top: 64px", 260, size=12.5, pad="20px 24px")
             + cap(v("19:14", frm="But he seemed"), "right: 12px; top: 12px", size=11, maxw=230) + vref("GEN 19:14", "right: 12px; bottom: 12px"))
    return page("Genesis 19:10–14 — Bring Them out of the Place", t, r1 + r2 + r3 + r4, START + 16)


@P("GEN-C04-P18-Escape", "82 · Escape for Thy Life")
def p18():
    t, h = rows(260, 300, None)
    r1 = new(DAWN, W1, h[0], defs("c418a", *ALL) + Q.city_gate("c418a", W1, h[0], 4181, top=0.6),
             cap(v("19:15", to="saying,"), "right: 12px; top: 12px", size=10.5, maxw=330)
             + balloon(v("19:15", frm="Arise"), "right: 12px; top: 64px", 320, size=12, pad="22px 28px") + vref("GEN 19:15", "left: 12px; bottom: 12px"))
    r2 = new(DAWN, W1, h[1], defs("c418b", *ALL) + Q.by_the_hand("c418b", W1, h[1], 4182),
             cap(v("19:16"), "right: 12px; top: 12px", size=11, maxw=420) + vref("GEN 19:16", "left: 12px; bottom: 12px"))
    r3 = new("#1A0A0E", W1, h[2], Q.escape_map(W1, h[2], 4183),
             cap(v("19:17", to="he said,"), "left: 12px; top: 12px", size=10.5, maxw=420)
             + balloon(v("19:17", frm="Escape"), "left: 12px; bottom: 12px", 360, size=13, pad="26px 32px")
             + hud("LOOK NOT BEHIND", "right: 14px; bottom: 14px", size=20) + vref("GEN 19:17", "right: 12px; top: 12px"))
    return page("Genesis 19:15–17 — Escape for Thy Life", t, r1 + r2 + r3, START + 17)


@P("GEN-C04-P19-Zoar", "83 · Is It Not a Little One?")
def p19():
    t, h = rows(380, 300, None)
    r1 = new(EMBER, W1, h[0], fc(Q.LOT_FEAR, h[0]),
             cap(v("19:18", to="unto them,"), "left: 320px; top: 12px", size=10.5)
             + balloon(v("19:18", frm="Oh, not so") + " " + v("19:19") + " " + v("19:20"), "left: 270px; top: 46px", 410, size=12.5, pad="36px 42px") + vref("GEN 19:18–20", "left: 12px; bottom: 12px"))
    r2 = new(DAWN, W1, h[1], defs("c419b", *ALL) + Y.ground(W1, h[1], h[1] * 0.88, "#8A6A4A", dy=0)
             + Q.shining("c419b", W1 * 0.84, h[1] * 0.88, Y.fit(h[1] * 0.88, h[1] * 0.3), flip=True) + Z.lot("c419b", W1 * 0.66, h[1] * 0.88, Y.fit(h[1] * 0.88, h[1] * 0.36)),
             cap(v("19:21", to="unto him,"), "left: 12px; top: 12px", size=10.5)
             + balloon(v("19:21", frm="See,") + " " + v("19:22", to="come thither."), "left: 12px; top: 46px", 380, size=12.5, pad="26px 34px")
             + cap(v("19:22", frm="Therefore"), "left: 12px; bottom: 14px", size=11.5, maxw=380) + vref("GEN 19:21–22", "right: 12px; top: 12px"))
    r3 = new(DAWN, W1, h[2], Q.little_city(W1, h[2], 4193),
             cap(v("19:23"), "left: 12px; top: 12px", size=13, maxw=400) + vref("GEN 19:23", "right: 12px; bottom: 12px"))
    return page("Genesis 19:18–23 — Is It Not a Little One?", t, r1 + r2 + r3, START + 18)


@P("GEN-C04-P20-Brimstone", "84 · Brimstone and Fire")
def p20():
    t, h = rows(380, 300, None)
    r1 = use(Sod[0], over=cap(v("19:24"), "left: 12px; top: 12px", size=12, maxw=420)
             + cap(v("19:25"), "right: 12px; bottom: 14px", size=11, maxw=360)
             + sfx("ゴゴゴゴ", "GOGOGOGO", "right: 20px; top: 70px", size=56, fill="#FFE680", stroke="#0D0D0F", rot=-6) + vref("GEN 19:24–25", "left: 12px; bottom: 12px"))
    r2 = cols(use(Sod[1], over=cap(v("19:26"), "left: 8px; top: 8px", size=11.5, maxw=320)
                  + sfx("ピキィ", "PIKII", "right: 14px; top: 90px", size=36, fill="#F3EFE6", stroke="#0D0D0F", rot=-6) + vref("GEN 19:26", "right: 8px; bottom: 8px")),
              new("linear-gradient(180deg, #C8A0A0 0%, #6A5A4A 100%)", W2, h[1], defs("c420b", *ALL) + Q.at_the_place("c420b", W2, h[1], 4202),
                  cap(v("19:27"), "left: 8px; top: 8px", size=11, maxw=320) + vref("GEN 19:27", "right: 8px; bottom: 8px")))
    r3 = cols(use(Sod[2], over=cap(v("19:28"), "left: 8px; bottom: 8px", size=10.5, maxw=320) + vref("GEN 19:28", "right: 8px; top: 8px")),
              new(NIGHT, W2, h[2], cosmic(W2, h[2]), cap(v("19:29"), "left: 8px; top: 8px", size=11.5, maxw=320) + vref("GEN 19:29", "right: 8px; bottom: 8px")))
    return page("Genesis 19:24–29 — Brimstone and Fire", t, r1 + r2 + r3, START + 19)


@P("GEN-C04-P21-Cave", "85 · He Dwelt in a Cave")
def p21():
    t, h = rows(300, 320, None)
    r1 = new(NIGHT, W1, h[0], defs("c421a", *ALL) + Q.cave_mouth("c421a", W1, h[0], 4211, figures=False)
             + Z.lot("c421a", W1 * 0.5, h[0] * 0.88, Y.fit(h[0] * 0.88, h[0] * 0.6)) + Q.daughters("c421a", W1 * 0.58, h[0] * 0.88, Y.fit(h[0] * 0.88, h[0] * 0.62)),
             cap(v("19:30"), "left: 12px; top: 12px", size=11.5, maxw=480) + vref("GEN 19:30", "right: 12px; bottom: 12px"))
    r2 = new(NIGHT, W1, h[1], defs("c421b", *ALL) + Q.cave_mouth("c421b", W1, h[1], 4212),
             cap(v("19:31", to="unto the younger,"), "left: 12px; top: 12px", size=10.5)
             + balloon(v("19:31", frm="Our father") + " " + v("19:32"), "right: 12px; top: 12px", 360, size=12, pad="28px 36px") + vref("GEN 19:31–32", "left: 12px; bottom: 12px"))
    r3 = new("#12090A", W1, h[2], Q.wine_jar(W1, h[2], 4213),
             cap(v("19:33"), "left: 12px; top: 12px", size=12, maxw=500) + vref("GEN 19:33", "right: 12px; bottom: 12px"))
    return page("Genesis 19:30–33 — He Dwelt in a Cave", t, r1 + r2 + r3, START + 20)


@P("GEN-C04-P22-Moab", "86 · Moab and Ben-ammi")
def p22():
    t, h = rows(340, 360, None)
    r1 = new(NIGHT, W1, h[0], defs("c422a", *ALL) + Q.cave_mouth("c422a", W1, h[0], 4221),
             cap(v("19:34", to="unto the younger,"), "left: 12px; top: 12px", size=10.5, maxw=290)
             + balloon(v("19:34", frm="Behold,"), "right: 12px; top: 12px", 360, size=12, pad="28px 38px") + vref("GEN 19:34", "left: 12px; bottom: 12px"))
    r2 = cols(new("#12090A", W2, h[1], Q.wine_jar(W2, h[1], 4222), cap(v("19:35"), "left: 8px; top: 8px", size=11, maxw=320) + vref("GEN 19:35", "right: 8px; bottom: 8px")),
              new(DAWN, W2, h[1], Y.hills(W2, h[1], h[1] * 0.7, 4223, color="#3A2A2E", amp=10) + Z.sun(W2 * 0.7, h[1] * 0.7, 20, op=0.3),
                  cap(v("19:36"), "left: 8px; top: 8px", size=12.5, maxw=320) + vref("GEN 19:36", "right: 8px; top: 64px")
                  + end_mark("NEXT · THE SON OF PROMISE", "right: 10px; bottom: 10px")))
    r3 = cols(clan("Moab", v("19:37"), "GEN 19:37", "#E8A317", of="OF LOT", size=17),
              clan("Ben-ammi", v("19:38"), "GEN 19:38", "#C2456A", of="OF LOT", size=17))
    return page("Genesis 19:34–38 — Moab and Ben-ammi", t, r1 + r2 + r3, START + 21)
