"""Genesis volume, Chapter 13 — Pharaoh's Dreams (Genesis 41). Word for word from ref/asv.
Pharaoh's retelling of his dreams to Joseph (41:17–24) is abridged on one balloon: 41:17 and the end of 41:24 in full,
the repeated middle cut with "…" (41:18–23 omitted, 41:24 partial). Every other verse is in full. Reuses the digest's
kine, ears, hall, seven-years, Pharaoh and granary panels."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from genesis import G, art as X, art2 as Y, art3 as Z, art10 as T, art11 as U, art12 as V12
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import clan, hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch12 import NILE, COURT, CELL
from mk import defs, face

v, sp = G.v, G.span
B5 = "digest/genesis/book-05/"
Dr, Ph, Gr = (panels(B5 + n + ".dc.html") for n in ["B5-P05-Dream", "B5-P06-Pharaoh", "B5-P07-Granaries"])
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
START = 206                                  # chapter 12 ends on page 205
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco


@P("GEN-C13-00-Title", "Chapter 13 · Pharaoh's Dreams")
def title():
    return chapter_title(13, "第十三話", "Pharaoh's Dreams", "Genesis 41", f'<g transform="translate(-20 300) scale(1.1)">{Dr[0].svg}</g>', NIGHT,
                         v("41:16", frm="It is not in me:", to="answer of peace."), "Genesis · Volume One")


@P("GEN-C13-P01-Kine", "206 · Seven Kine out of the River")
def p01():
    t, h = rows(560, None)
    r1 = use(Dr[0], over=cap(v("41:1") + " " + v("41:2"), "left: 12px; top: 12px", size=11, maxw=500)
             + cap(v("41:3") + " " + v("41:4"), "left: 12px; bottom: 40px", size=11, maxw=420) + vref("GEN 41:1–4", "right: 12px; bottom: 12px"))
    r2 = new(COURT, W1, h[1], fc(V12.PHARAOH_TROUBLED, h[1], w=W1),
             cap(v("41:4", frm="So Pharaoh awoke."), "left: 320px; top: 40px", size=14) + vref("GEN 41:4", "left: 12px; bottom: 12px"))
    return page("Genesis 41:1–4 — Seven Kine out of the River", t, r1 + r2, START + 0)


@P("GEN-C13-P02-Ears", "207 · Seven Ears upon One Stalk")
def p02():
    t, h = rows(420, None)
    r1 = cols(use(Dr[1], over=cap(v("41:5"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 41:5", "right: 8px; bottom: 8px")),
              use(Dr[2], over=cap(v("41:6"), "left: 8px; top: 8px", size=10.5, maxw=320) + cap(v("41:7"), "left: 8px; bottom: 8px", size=10.5, maxw=320)
                  + vref("GEN 41:6–7", "right: 8px; top: 120px")))
    r2 = new(COURT, W1, h[1], defs("c132b", *ALL) + V12.magicians("c132b", W1, h[1], 1322),
             cap(v("41:8"), "left: 12px; top: 12px", size=11, maxw=520) + vref("GEN 41:8", "right: 12px; top: 12px"))
    return page("Genesis 41:5–8 — Seven Ears upon One Stalk", t, r1 + r2, START + 1)


@P("GEN-C13-P03-Butler", "208 · I Do Remember My Faults This Day")
def p03():
    t, h = rows(None)
    r1 = new(COURT, W1, h[0], face(V12.BUTLER, -60, h[0] - 560, 1.4),
             cap(v("41:9", to="saying,"), "left: 330px; top: 16px", size=11)
             + balloon(v("41:9", frm="I do") + " " + v("41:10") + " " + v("41:11"), "left: 300px; top: 56px", 380, size=13, pad="34px 40px")
             + balloon(v("41:12") + " " + v("41:13"), "left: 300px; top: 420px", 380, size=13, pad="34px 40px") + vref("GEN 41:9–13", "left: 12px; bottom: 12px"))
    return page("Genesis 41:9–13 — I Do Remember My Faults This Day", t, r1, START + 2)


@P("GEN-C13-P04-Answer", "209 · It Is Not in Me")
def p04():
    t, h = rows(380, None)
    r1 = use(Ph[0], over=cap(v("41:14"), "left: 12px; top: 12px", size=10.5, maxw=330)
             + cap(v("41:16", to="saying,"), "right: 12px; top: 12px", size=10.5)
             + balloon(v("41:16", frm="It is not"), "right: 12px; top: 48px", 260, size=13, pad="16px 22px") + vref("GEN 41:14, 16", "right: 12px; bottom: 12px"))
    r2 = new(COURT, W1, h[1], fc(V12.PHARAOH, h[1], w=W1),
             cap(v("41:15", to="unto Joseph,"), "left: 320px; top: 12px", size=11)
             + balloon(v("41:15", frm="I have"), "left: 290px; top: 50px", 390, size=13.5, pad="32px 40px") + vref("GEN 41:15", "left: 12px; bottom: 12px"))
    return page("Genesis 41:14–16 — It Is Not in Me", t, r1 + r2, START + 3)


@P("GEN-C13-P05-One", "210 · The Dream of Pharaoh Is One")
def p05():
    t, h = rows(330, None)
    told = v("41:17", frm="In my dream,") + " … " + v("41:24", frm="and I told it")
    r1 = new(COURT, W1, h[0], fc(V12.PHARAOH_TROUBLED, h[0], w=W1),
             cap(v("41:17", to="unto Joseph,"), "left: 320px; top: 12px", size=11)
             + balloon(told, "left: 280px; top: 50px", 400, size=13, pad="32px 40px")
             + f'    <span data-label style="position: absolute; right: 14px; bottom: 12px; padding: 3px 8px; background: #12113A; color: #FFD23F; font-size: 9px; font-weight: 600; letter-spacing: 0.18em">AS HE TOLD IT · GEN 41:17–24 ABRIDGED</span>\n'
             + vref("GEN 41:17, 24", "left: 12px; bottom: 12px"))
    r2 = new(GLOW, W1, h[1], fc(V12.JOSEPH_EG, h[1], w=W1),
             cap(v("41:25", to="unto Pharaoh,"), "left: 320px; top: 12px", size=11)
             + balloon(v("41:25", frm="The dream") + " " + v("41:26") + " " + v("41:27") + " " + v("41:28"), "left: 270px; top: 50px", 410, size=13, pad="36px 42px")
             + vref("GEN 41:25–28", "left: 12px; bottom: 12px"))
    return page("Genesis 41:17–28 — The Dream of Pharaoh Is One", t, r1 + r2, START + 4)


@P("GEN-C13-P06-Plenty", "211 · Seven Years of Great Plenty")
def p06():
    t, h = rows(330, None)
    r1 = use(Ph[1], over=balloon(v("41:29") + " " + v("41:30"), "left: 50%; bottom: 14px; transform: translateX(-50%)", 520, size=13, pad="22px 34px")
             + vref("GEN 41:29–30", "right: 12px; top: 12px"))
    r2 = new(GLOW, W1, h[1], fc(V12.JOSEPH_EG, h[1], w=W1),
             balloon(v("41:31") + " " + v("41:32") + " " + v("41:33"), "left: 260px; top: 30px", 420, size=13.5, pad="40px 44px") + vref("GEN 41:31–33", "left: 12px; bottom: 12px"))
    return page("Genesis 41:29–33 — Seven Years of Great Plenty", t, r1 + r2, START + 5)


@P("GEN-C13-P07-Fifth", "212 · The Fifth Part of the Land")
def p07():
    t, h = rows(420, None)
    r1 = new(GLOW, W1, h[0], fc(V12.JOSEPH_EG, h[0], w=W1),
             balloon(v("41:34") + " " + v("41:35") + " " + v("41:36"), "left: 260px; top: 30px", 420, size=13, pad="40px 44px")
             + hud("1/5", "right: 14px; bottom: 14px", size=30) + vref("GEN 41:34–36", "left: 12px; bottom: 12px"))
    r2 = cols(use(Ph[2], over=cap(v("41:37"), "right: 8px; top: 8px", size=10.5, maxw=210)
                  + cap(v("41:38", to="unto his servants,"), "right: 8px; bottom: 8px", size=10, maxw=210)),
              new(COURT, W2, h[1], fc(V12.PHARAOH, h[1]),
                  balloon(v("41:38", frm="Can we"), "right: 8px; top: 20px", 220, size=13, pad="22px 22px") + vref("GEN 41:37–38", "left: 8px; bottom: 8px")))
    return page("Genesis 41:34–38 — The Fifth Part of the Land", t, r1 + r2, START + 6)


@P("GEN-C13-P08-Chariot", "213 · Bow the Knee")
def p08():
    t, h = rows(330, 200, None)
    r1 = new(COURT, W1, h[0], fc(V12.PHARAOH, h[0], w=W1),
             cap(v("41:39", to="unto Joseph,"), "left: 320px; top: 12px", size=10.5)
             + balloon(v("41:39", frm="Forasmuch") + " " + v("41:40"), "left: 280px; top: 46px", 400, size=12.5, pad="28px 36px")
             + cap(v("41:41", to="unto Joseph,"), "left: 320px; top: 216px", size=10.5)
             + balloon(v("41:41", frm="See, I have"), "left: 290px; bottom: 10px", 340, size=12.5, pad="14px 24px") + vref("GEN 41:39–41", "left: 12px; bottom: 12px"))
    r2 = cols(use(Ph[3], over=cap(v("41:42", to="upon Joseph's hand,"), "left: 8px; bottom: 8px", size=10, maxw=320) + vref("GEN 41:42", "right: 8px; top: 8px")),
              new("#1F5FAD", W2, h[1], V12.signet(W2, h[1], 1382), cap(v("41:42", frm="and arrayed"), "left: 8px; bottom: 8px", size=10, maxw=320)))
    r3 = new(V12.EGYPT_BG, W1, h[2], V12.chariot_ride(None, W1, h[2], 1383),
             cap(v("41:43", to="Bow the knee:"), "left: 12px; top: 12px", size=11, maxw=420)
             + cap(v("41:43", frm="and he set"), "left: 12px; top: 74px", size=10.5)
             + cap(v("41:44", to="unto Joseph,"), "right: 12px; top: 12px", size=10.5)
             + balloon(v("41:44", frm="I am Pharaoh"), "right: 12px; top: 46px", 240, size=11.5, pad="18px 22px") + vref("GEN 41:43–44", "right: 12px; bottom: 12px"))
    return page("Genesis 41:39–44 — Bow the Knee", t, r1 + r2 + r3, START + 7)


@P("GEN-C13-P09-Granaries", "214 · As the Sand of the Sea")
def p09():
    t, h = rows(200, 210, None)
    r1 = new(V12.EGYPT_BG, W1, h[0], defs("c139a", *ALL) + T.stage("c139a", W1, h[0], 1391, "egypt", [("joseph_eg", 0.3, 0.42), (("woman", "#F3EFE6"), 0.42, 0.44, True)]),
             cap(v("41:45"), "left: 12px; top: 12px", size=10.5, maxw=400) + label_name() + vref("GEN 41:45", "right: 12px; bottom: 12px"))
    r2 = new(SKY, W1, h[1], V12.handfuls(None, W1, h[1], 1392),
             cap(v("41:46"), "left: 12px; top: 12px", size=10.5, maxw=380) + cap(v("41:47"), "right: 12px; top: 12px", size=11, maxw=260)
             + hud("30", "right: 14px; bottom: 14px", size=26) + vref("GEN 41:46–47", "left: 12px; bottom: 12px"))
    r3 = use(Gr[0], over=cap(v("41:48"), "left: 12px; bottom: 40px", size=10.5, maxw=440)
             + cap(v("41:49"), "left: 12px; top: 12px", size=11, maxw=380) + vref("GEN 41:48–49", "right: 12px; bottom: 12px"))
    return page("Genesis 41:45–49 — As the Sand of the Sea", t, r1 + r2 + r3, START + 8)

def label_name():
    return ('    <span data-label style="position: absolute; right: 12px; top: 12px; padding: 4px 10px; background: #12113A; color: #FFD23F; font-family: Anton, sans-serif; '
            'font-size: 18px; letter-spacing: 0.06em">ZAPHENATH-PANEAH</span>\n')


@P("GEN-C13-P10-Famine", "215 · Go unto Joseph")
def p10():
    t, h = rows(250, 220, None)
    cells = [clan("Manasseh", v("41:50") + " " + v("41:51"), "GEN 41:50–51", "#FFD23F", of="OF JOSEPH", size=12),
             clan("Ephraim", v("41:52") + " " + v("41:53"), "GEN 41:52–53", "#FFD23F", of="OF JOSEPH", size=12.5)]
    r1 = grid(cells, "minmax(0, 1fr)")
    r2 = new(COURT, W1, h[1], fc(V12.PHARAOH, h[1], w=W1),
             cap(v("41:54"), "left: 300px; top: 12px", size=10.5, maxw=380)
             + cap(v("41:55", to="unto all the Egyptians,"), "left: 300px; top: 92px", size=10.5, maxw=380)
             + balloon(v("41:55", frm="Go unto"), "left: 290px; bottom: 10px", 340, size=13, pad="14px 24px") + vref("GEN 41:54–55", "left: 12px; bottom: 12px"))
    r3 = new(SAND, W1, h[2], defs("c1310c", *ALL) + V12.bread_lines("c1310c", W1, h[2], 13103),
             cap(v("41:56"), "left: 12px; top: 12px", size=10.5, maxw=420) + cap(v("41:57"), "right: 12px; top: 12px", size=10.5, maxw=230)
             + end_mark("NEXT · THE BROTHERS IN EGYPT", "right: 14px; bottom: 12px") + vref("GEN 41:56–57", "left: 12px; bottom: 12px"))
    return page("Genesis 41:50–57 — Go unto Joseph", t, r1 + r2 + r3, START + 9)
