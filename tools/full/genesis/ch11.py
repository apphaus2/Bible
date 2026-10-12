"""Genesis volume, Chapter 11 — The Dreamer (Genesis 37–38). Every verse, word for word from ref/asv.
Reuses the digest's Book Five panels (the coat, the sheaves, the stars, the pit, the silver, the caravan, the coat in
blood). Genesis 38 (Judah and Tamar) is given in full; the drawings are faces, the gate of Enaim, the pledge and the
twins with the scarlet thread."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from genesis import G, art as X, art2 as Y, art3 as Z, art10 as T, art11 as U
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import clan, hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch06 import RUST, GREENLIT, GOLDEN
from genesis.ch07 import LAMP, RED, BLUE
from genesis.ch08 import ROSE, OCHRE, PASTURE
from mk import defs, face

v, sp = G.v, G.span
B5 = "digest/genesis/book-05/"
Coat, Pit, Grief = (panels(B5 + n + ".dc.html") for n in ["B5-P01-Coat", "B5-P02-Pit", "B5-P03-Grief"])
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
YOUTH = "radial-gradient(circle at 70% 30%, #FFF4C2 0 20px, #FFB45A 180px, #8A3A1E 420px)"
DARK = "radial-gradient(circle at 70% 30%, #E8D8C8 0 20px, #6A4A5A 180px, #1A1020 420px)"
START = 183                                  # chapter 10 ends on page 182
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco


@P("GEN-C11-00-Title", "Chapter 11 · The Dreamer")
def title():
    return chapter_title(11, "第十一話", "The Dreamer", "Genesis 37 – 38", f'<g transform="translate(-560 260) scale(2.6)">{Coat[2].svg}</g>', NIGHT,
                         v("37:19", frm="Behold, this", to="cometh."), "Genesis · Volume One")


@P("GEN-C11-P01-Coat", "183 · A Coat of Many Colors")
def p01():
    t, h = rows(250, 330, None)
    r1 = new(PASTURE, W1, h[0], defs("c111a", *ALL) + U.flock_field("c111a", W1, h[0], 1111, [("joseph", 0.5, 0.46), (("man", U.BROS[0]), 0.64, 0.46, True), (("man", U.BROS[2]), 0.76, 0.46, True)]),
             cap(v("37:1") + " " + v("37:2"), "left: 12px; top: 12px", size=10.5, maxw=500) + vref("GEN 37:1–2", "right: 12px; bottom: 12px"))
    r2 = use(Coat[0], over=cap(v("37:3"), "right: 12px; top: 12px", size=12, maxw=340) + vref("GEN 37:3", "left: 12px; bottom: 12px"))
    r3 = new(RED, W1, h[2], fc(U.BROTHER, h[2], w=W1), cap(v("37:4"), "right: 12px; top: 12px", size=12, maxw=380) + vref("GEN 37:4", "left: 12px; bottom: 12px"))
    return page("Genesis 37:1–4 — A Coat of Many Colors", t, r1 + r2 + r3, START + 0)


@P("GEN-C11-P02-Sheaves", "184 · My Sheaf Arose")
def p02():
    t, h = rows(230, 360, None)
    r1 = new(YOUTH, W1, h[0], fc(U.JOSEPH, h[0], w=W1),
             cap(v("37:5"), "left: 300px; top: 12px", size=11, maxw=380)
             + cap(v("37:6", to="unto them,"), "left: 300px; top: 84px", size=10.5)
             + balloon(v("37:6", frm="Hear"), "left: 290px; top: 120px", 330, size=13, pad="18px 26px") + vref("GEN 37:5–6", "left: 12px; bottom: 12px"))
    r2 = use(Coat[1], over=balloon(v("37:7"), "left: 12px; top: 12px", 460, size=12.5, pad="24px 34px") + vref("GEN 37:7", "right: 12px; bottom: 12px"))
    r3 = new(RED, W1, h[2], fc(U.BROTHER, h[2], w=W1),
             cap(v("37:8", to="said to him,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("37:8", frm="Shalt thou", to="dominion over us?"), "left: 290px; top: 46px", 330, size=13, pad="20px 26px")
             + cap(v("37:8", frm="And they hated"), "right: 12px; bottom: 14px", size=11, maxw=330) + vref("GEN 37:8", "left: 12px; bottom: 12px"))
    return page("Genesis 37:5–8 — My Sheaf Arose", t, r1 + r2 + r3, START + 1)


@P("GEN-C11-P03-Stars", "185 · The Sun and the Moon and Eleven Stars")
def p03():
    t, h = rows(300, 280, None)
    r1 = use(Coat[2], over=cap(v("37:9", to="and said,"), "left: 12px; top: 12px", size=10.5, maxw=440)
             + balloon(v("37:9", frm="Behold, I have"), "right: 12px; bottom: 14px", 330, size=12, pad="22px 28px") + vref("GEN 37:9", "left: 12px; bottom: 12px"))
    r2 = new(GOLDEN, W1, h[1], fc(U.ISRAEL, h[1], w=W1),
             cap(v("37:10", to="said unto him,"), "left: 300px; top: 12px", size=10.5, maxw=380)
             + balloon(v("37:10", frm="What is this"), "left: 270px; top: 84px", 410, size=12.5, pad="26px 36px") + vref("GEN 37:10", "left: 12px; bottom: 12px"))
    r3 = cols(new(RED, W2, h[2], fc(U.BROTHER, h[2]), cap(v("37:11", to="envied him;"), "right: 8px; top: 8px", size=12, maxw=200) + vref("GEN 37:11", "left: 8px; bottom: 8px")),
              new(GOLDEN, W2, h[2], fc(U.ISRAEL, h[2]), cap(v("37:11", frm="but his father"), "right: 8px; top: 8px", size=12, maxw=200)))
    return page("Genesis 37:9–11 — The Sun and the Moon and Eleven Stars", t, r1 + r2 + r3, START + 2)


@P("GEN-C11-P04-Dothan", "186 · I Am Seeking My Brethren")
def p04():
    t, h = rows(300, 240, None)
    r1 = new(GOLDEN, W1, h[0], fc(U.ISRAEL, h[0], w=W1),
             cap(v("37:12"), "left: 300px; top: 12px", size=10.5, maxw=380)
             + cap(v("37:13", to="unto Joseph,"), "left: 300px; top: 52px", size=10.5)
             + balloon(v("37:13", frm="Are not", to="unto them."), "left: 280px; top: 86px", 300, size=12, pad="18px 24px")
             + cap(v("37:13", frm="And he said to him,", to="to him,"), "right: 12px; top: 196px", size=10.5)
             + balloon(v("37:13", frm="Here am I."), "right: 12px; bottom: 12px", 150, size=13, pad="12px 14px") + vref("GEN 37:12–13", "left: 12px; bottom: 12px"))
    r2 = new(PASTURE, W1, h[1], defs("c114b", *ALL) + U.wanderer("c114b", W1, h[1], 1142),
             balloon(v("37:14", to="word again."), "left: 12px; top: 12px", 360, size=11.5, pad="18px 26px")
             + cap(v("37:14", frm="So he sent"), "right: 12px; top: 12px", size=10.5, maxw=260) + vref("GEN 37:14", "right: 12px; bottom: 12px"))
    r3 = cols(new(GOLDEN, W2, h[2], fc(U.STRANGER, h[2]),
                  cap(v("37:15", to="saying,"), "right: 8px; top: 8px", size=10, maxw=200)
                  + balloon(v("37:15", frm="What seekest"), "right: 8px; top: 110px", 190, size=12.5, pad="14px 16px")
                  + cap(v("37:16", to="said,"), "right: 8px; top: 180px", size=10)
                  + balloon(v("37:16", frm="I am seeking"), "right: 8px; top: 212px", 220, size=11, pad="18px 20px") + vref("GEN 37:15–16", "left: 8px; bottom: 8px")),
              new("#0B1A2E", W2, h[2], U.dothan_map(W2, h[2], 1143),
                  cap(v("37:17", to="said,"), "left: 8px; top: 8px", size=10)
                  + balloon(v("37:17", frm="They are"), "left: 8px; top: 40px", 220, size=11, pad="16px 20px")
                  + cap(v("37:17", frm="And Joseph went"), "right: 8px; bottom: 8px", size=10, maxw=200) + vref("GEN 37:17", "left: 8px; bottom: 8px")))
    return page("Genesis 37:12–17 — I Am Seeking My Brethren", t, r1 + r2 + r3, START + 3)


@P("GEN-C11-P05-Conspired", "187 · Behold, This Dreamer Cometh")
def p05():
    t, h = rows(290, 270, None)
    r1 = use(Pit[0], over=cap(v("37:18") + " " + v("37:19", to="one to another,"), "right: 12px; top: 12px", size=10.5, maxw=330)
 + vref("GEN 37:18–19", "right: 12px; bottom: 12px"))
    r2 = new(RED, W1, h[1], fc(U.BROTHER, h[1], w=W1),
             balloon(v("37:20"), "left: 270px; top: 20px", 410, size=12.5, pad="30px 40px") + vref("GEN 37:20", "left: 12px; bottom: 12px"))
    r3 = new(GOLDEN, W1, h[2], fc(U.REUBEN, h[2], w=W1),
             cap(v("37:21", to="and said,"), "left: 300px; top: 12px", size=10.5, maxw=380)
             + balloon(v("37:21", frm="Let us not"), "left: 290px; top: 66px", 240, size=12.5, pad="16px 20px")
             + cap(v("37:22", to="unto them,"), "right: 12px; top: 66px", size=10.5)
             + balloon(v("37:22", frm="Shed no", to="upon him:"), "left: 270px; top: 140px", 410, size=12, pad="20px 30px")
             + cap(v("37:22", frm="that he might"), "right: 12px; bottom: 14px", size=10.5, maxw=380) + vref("GEN 37:21–22", "left: 12px; bottom: 12px"))
    return page("Genesis 37:18–22 — Behold, This Dreamer Cometh", t, r1 + r2 + r3, START + 4)


@P("GEN-C11-P06-Pit", "188 · They Cast Him into the Pit")
def p06():
    t, h = rows(420, None)
    r1 = use(Pit[1], over=cap(v("37:23") + " " + v("37:24"), "left: 12px; top: 12px", size=11, maxw=420)
             + sfx("ドサッ", "DOSA", "right: 24px; bottom: 30px", size=52, fill="#F3EFE6", stroke="#0D0D0F", rot=-6) + vref("GEN 37:23–24", "left: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], defs("c116b", *ALL) + U.caravan_road("c116b", W1, h[1], 1162),
             cap(v("37:25"), "left: 12px; top: 12px", size=11.5, maxw=500) + vref("GEN 37:25", "right: 12px; top: 12px"))
    return page("Genesis 37:23–25 — They Cast Him into the Pit", t, r1 + r2, START + 5)


@P("GEN-C11-P07-Sold", "189 · Twenty Pieces of Silver")
def p07():
    t, h = rows(300, None)
    r1 = new(RUST, W1, h[0], fc(U.JUDAH, h[0], w=W1),
             cap(v("37:26", to="unto his brethren,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("37:26", frm="What profit") + " " + v("37:27", to="our flesh."), "left: 270px; top: 46px", 410, size=12.5, pad="28px 38px")
             + cap(v("37:27", frm="And his brethren"), "right: 12px; bottom: 14px", size=11) + vref("GEN 37:26–27", "left: 12px; bottom: 12px"))
    r2 = cols(use(Pit[2], over=cap(v("37:28", to="twenty pieces of silver."), "left: 8px; bottom: 8px", size=10.5, maxw=230) + vref("GEN 37:28", "left: 8px; top: 8px")),
              use(Pit[3], over=cap(v("37:28", frm="And they brought"), "left: 8px; top: 8px", size=12)))
    return page("Genesis 37:26–28 — Twenty Pieces of Silver", t, r1 + r2, START + 6)


@P("GEN-C11-P08-Blood", "190 · The Child Is Not")
def p08():
    t, h = rows(260, 420, None)
    r1 = cols(new(SAND, W2, h[0], defs("c118a", *ALL) + U.rent_clothes("c118a", W2, h[0], 1181),
                  cap(v("37:29"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 37:29", "right: 8px; bottom: 8px")),
              new(GOLDEN, W2, h[0], fc(U.REUBEN, h[0]),
                  cap(v("37:30", to="said,"), "right: 8px; top: 8px", size=10, maxw=200)
                  + balloon(v("37:30", frm="The child"), "right: 8px; top: 80px", 200, size=12.5, pad="18px 18px") + vref("GEN 37:30", "left: 8px; bottom: 8px")))
    r2 = use(Grief[0], over=cap(v("37:31"), "left: 12px; top: 12px", size=11.5, maxw=300) + vref("GEN 37:31", "right: 12px; bottom: 12px"))
    r3 = new(RED, W1, h[2], fc(U.BROTHER, h[2], w=W1),
             cap(v("37:32", to="and said,"), "left: 300px; top: 12px", size=10.5, maxw=380)
             + balloon(v("37:32", frm="This have"), "left: 290px; top: 84px", 380, size=12.5, pad="20px 28px") + vref("GEN 37:32", "left: 12px; bottom: 12px"))
    return page("Genesis 37:29–32 — The Child Is Not", t, r1 + r2 + r3, START + 7)


@P("GEN-C11-P09-Sheol", "191 · He Refused to Be Comforted")
def p09():
    t, h = rows(420, 240, None)
    r1 = use(Grief[1], over=cap(v("37:33", to="and said,"), "left: 12px; top: 12px", size=10.5)
             + balloon(v("37:33", frm="It is my"), "right: 12px; top: 12px", 380, size=13, pad="22px 30px") + vref("GEN 37:33", "left: 12px; bottom: 12px"))
    r2 = new("#3A3440", W1, h[1], defs("c119b", *ALL) + U.sackcloth("c119b", W1, h[1], 1192),
             cap(v("37:34"), "left: 12px; top: 12px", size=11, maxw=400)
             + cap(v("37:35", to="he said,"), "right: 12px; top: 12px", size=10.5, maxw=260) + vref("GEN 37:34–35", "right: 12px; bottom: 12px"))
    r3 = cols(new(DARK, W2, h[2], fc(U.ISRAEL_WEEP, h[2]),
                  balloon(v("37:35", frm="For I will", to="mourning."), "right: 8px; top: 12px", 220, size=12, pad="20px 22px")
                  + cap(v("37:35", frm="And his father"), "right: 8px; bottom: 8px", size=10.5)),
              new(SAND, W2, h[2], defs("c119c", *ALL) + U.potiphar_house("c119c", W2, h[2], 1193),
                  cap(v("37:36"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 37:36", "right: 8px; top: 120px")))
    return page("Genesis 37:33–36 — He Refused to Be Comforted", t, r1 + r2 + r3, START + 8)


@P("GEN-C11-P10-Judah", "192 · Judah Went Down from His Brethren")
def p10():
    t, h = rows(260, None)
    r1 = new(SAND, W1, h[0], defs("c1110a", *ALL) + U.adullam("c1110a", W1, h[0], 11101),
             cap(v("38:1") + " " + v("38:2"), "left: 12px; top: 12px", size=10.5, maxw=500) + vref("GEN 38:1–2", "right: 12px; top: 12px"))
    cells = [clan("Er", v("38:3"), "GEN 38:3", "#B5421E", of="OF JUDAH", size=17),
             clan("Onan", v("38:4"), "GEN 38:4", "#B5421E", of="OF JUDAH", size=17),
             clan("Shelah", v("38:5"), "GEN 38:5", "#B5421E", of="OF JUDAH", size=16),
             clan("Tamar", v("38:6"), "GEN 38:6", "#6A6A8A", size=17)]
    return page("Genesis 38:1–6 — Judah Went Down from His Brethren", t, r1 + grid(cells, "minmax(0, 1fr) minmax(0, 1fr)"), START + 9)


@P("GEN-C11-P11-Widow", "193 · Remain a Widow in Thy Father's House")
def p11():
    t, h = rows(240, 300, None)
    r1 = new("#2A2440", W1, h[0], U.graves_two(W1, h[0], 11111),
             cap(v("38:7"), "left: 12px; top: 12px", size=10.5, maxw=330)
             + cap(v("38:9") + " " + v("38:10"), "right: 12px; top: 12px", size=10, maxw=330) + vref("GEN 38:7, 9–10", "left: 12px; bottom: 12px"))
    r2 = new(RUST, W1, h[1], fc(U.JUDAH, h[1], w=W1),
             cap(v("38:8", to="unto Onan,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("38:8", frm="Go in"), "left: 280px; top: 46px", 380, size=11.5, pad="18px 26px")
             + cap(v("38:11", to="daughter-in-law,"), "left: 300px; top: 130px", size=10.5)
             + balloon(v("38:11", frm="Remain", to="be grown up;"), "left: 280px; top: 164px", 380, size=11.5, pad="16px 26px")
             + cap(v("38:11", frm="for he said,", to="he said,"), "right: 12px; bottom: 50px", size=10.5)
             + balloon(v("38:11", frm="Lest he also", to="his brethren."), "right: 12px; bottom: 8px", 260, size=11, pad="10px 20px") + vref("GEN 38:8, 11", "left: 12px; bottom: 12px"))
    r3 = new(SAND, W1, h[2], defs("c1111c", *ALL) + U.widow_house("c1111c", W1, h[2], 11113),
             cap(v("38:11", frm="And Tamar went"), "right: 12px; top: 12px", size=11, maxw=300)
             + cap(v("38:12"), "left: 12px; top: 12px", size=10, maxw=300) + vref("GEN 38:11–12", "right: 12px; bottom: 12px"))
    return page("Genesis 38:7–12 — Remain a Widow in Thy Father's House", t, r1 + r2 + r3, START + 10)


@P("GEN-C11-P12-Enaim", "194 · The Gate of Enaim")
def p12():
    t, h = rows(300, 220, None)
    r1 = new(SAND, W1, h[0], defs("c1112a", *ALL) + U.gate_enaim("c1112a", W1, h[0], 11121),
             cap(v("38:13") + " " + v("38:14"), "right: 12px; top: 12px", size=10.5, maxw=360)
             + cap(v("38:15"), "right: 12px; bottom: 50px", size=10.5, maxw=260) + vref("GEN 38:13–15", "left: 12px; bottom: 12px"))
    r2 = cols(new(RUST, W2, h[1], fc(U.JUDAH, h[1]),
                  cap(v("38:16", to="and said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("38:16", frm="Come, I pray", to="unto thee:"), "right: 8px; top: 40px", 200, size=11.5, pad="16px 18px")
                  + cap(v("38:16", frm="for he knew", to="daughter-in-law."), "right: 8px; bottom: 8px", size=9.5, maxw=200) + vref("GEN 38:16", "left: 8px; bottom: 8px")),
              new(EMBER, W2, h[1], fc(U.TAMAR_VEIL, h[1]),
                  cap(v("38:16", frm="And she said,", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("38:16", frm="What wilt"), "right: 8px; top: 40px", 200, size=11.5, pad="18px 18px")))
    r3 = cols(new(RUST, W2, h[2], fc(U.JUDAH, h[2]),
                  cap(v("38:17", to="he said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("38:17", frm="I will send", to="flock."), "right: 8px; top: 40px", 200, size=11.5, pad="16px 18px")
                  + cap(v("38:18", to="he said,"), "right: 8px; top: 140px", size=10)
                  + balloon(v("38:18", frm="What pledge", to="give thee?"), "right: 8px; top: 172px", 190, size=12, pad="14px 16px") + vref("GEN 38:17–18", "left: 8px; bottom: 8px")),
              new(EMBER, W2, h[2], fc(U.TAMAR_VEIL, h[2]),
                  cap(v("38:17", frm="And she said,", to="said,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("38:17", frm="Wilt thou"), "right: 8px; top: 40px", 190, size=12, pad="14px 16px")
                  + cap(v("38:18", frm="And she said, Thy", to="said,"), "right: 8px; top: 140px", size=10)
                  + balloon(v("38:18", frm="Thy signet", to="thy hand."), "right: 8px; top: 172px", 200, size=11.5, pad="16px 18px")))
    return page("Genesis 38:13–18 — The Gate of Enaim", t, r1 + r2 + r3, START + 11)


@P("GEN-C11-P13-Pledge", "195 · She Is More Righteous Than I")
def p13():
    t, h = rows(180, 240, 220, None)
    r1 = cols(new("#12113A", W2, h[0], U.pledge(W2, h[0], 11131), cap(v("38:18", frm="And he gave them"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 38:18", "right: 8px; bottom: 8px")),
              new(GREY, W2, h[0], fc(U.TAMAR, h[0]), cap(v("38:19"), "right: 8px; top: 8px", size=10, maxw=210) + vref("GEN 38:19", "left: 8px; bottom: 8px")))
    r2 = new(SAND, W1, h[1], defs("c1113b", *ALL) + U.kid_sent("c1113b", W1, h[1], 11132),
             cap(v("38:20"), "left: 12px; top: 12px", size=10, maxw=330)
             + cap(v("38:21", to="saying,"), "right: 12px; top: 12px", size=10, maxw=250)
             + balloon(v("38:21", frm="Where is", to="wayside?"), "right: 12px; top: 64px", 250, size=11, pad="14px 18px")
             + cap(v("38:21", frm="And they said,", to="said,"), "left: 12px; top: 112px", size=10)
             + balloon(v("38:21", frm="There hath"), "left: 12px; top: 144px", 220, size=11, pad="12px 16px") + vref("GEN 38:20–21", "right: 12px; bottom: 12px"))
    r3 = new(RUST, W1, h[2], fc(U.JUDAH, h[2], w=W1),
             cap(v("38:22", to="said,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("38:22", frm="I have not"), "left: 280px; top: 44px", 400, size=11, pad="16px 26px")
             + cap(v("38:23", to="Judah said,"), "left: 300px; top: 118px", size=10.5)
             + balloon(v("38:23", frm="Let her"), "left: 280px; top: 150px", 400, size=11, pad="12px 26px") + vref("GEN 38:22–23", "left: 12px; bottom: 12px"))
    r4 = cols(new(RUST, W2, h[3], fc(U.JUDAH_STERN, h[3]),
                  cap(v("38:24", to="Judah said,"), "right: 8px; top: 8px", size=9.5, maxw=220)
                  + balloon(v("38:24", frm="Bring her"), "right: 8px; bottom: 8px", 190, size=12, pad="12px 14px") + vref("GEN 38:24", "left: 8px; bottom: 8px")),
              new(SAND, W2, h[3], defs("c1113d", *ALL) + U.burnt("c1113d", W2, h[3], 11134),
                  cap(v("38:25", to="saying,"), "left: 8px; top: 8px", size=9.5, maxw=320)
                  + balloon(v("38:25", frm="By the man", to="with child:"), "left: 8px; top: 50px", 220, size=10.5, pad="12px 16px")
                  + cap(v("38:25", frm="and she said, Discern", to="she said,"), "right: 8px; top: 104px", size=9.5)
                  + balloon(v("38:25", frm="Discern"), "right: 8px; bottom: 8px", 220, size=10, pad="12px 16px")))
    return page("Genesis 38:18–25 — She Is More Righteous Than I", t, r1 + r2 + r3 + r4, START + 12)


@P("GEN-C11-P14-Perez", "196 · The Scarlet Thread")
def p14():
    t, h = rows(260, None)
    r1 = new(RUST, W1, h[0], fc(U.JUDAH, h[0], w=W1),
             cap(v("38:26", to="and said,"), "left: 300px; top: 12px", size=10.5)
             + balloon(v("38:26", frm="She is more", to="my son."), "left: 280px; top: 46px", 380, size=13, pad="22px 30px")
             + cap(v("38:26", frm="And he knew"), "right: 12px; bottom: 14px", size=11) + vref("GEN 38:26", "left: 12px; bottom: 12px"))
    r2 = new("#3A2A2E", W1, h[1], U.twins(W1, h[1], 11142),
             cap(v("38:27") + " " + v("38:28", to="saying,"), "left: 12px; top: 12px", size=11, maxw=420)
             + balloon(v("38:28", frm="This came"), "right: 12px; top: 12px", 220, size=13, pad="14px 18px")
             + cap(v("38:29", to="she said,"), "left: 12px; top: 150px", size=10.5, maxw=400)
             + balloon(v("38:29", frm="Wherefore", to="for thyself?"), "left: 12px; top: 210px", 300, size=12, pad="16px 22px")
             + cap(v("38:29", frm="therefore his name") + " " + v("38:30"), "right: 12px; top: 210px", size=10.5, maxw=300)
             + end_mark("NEXT · THE CAPTAIN OF THE GUARD", "right: 14px; bottom: 12px") + vref("GEN 38:27–30", "left: 12px; bottom: 12px"))
    return page("Genesis 38:26–30 — The Scarlet Thread", t, r1 + r2, START + 13)
