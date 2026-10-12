"""Genesis volume, Chapter 16 — Israel in Egypt (Genesis 46–47). Every verse, word for word from ref/asv.
46:8–27 (the seventy souls) is set as two scroll pages, one cell per son, coloured by mother."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, egypt as EG
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from faces_ex import F
from genesis import G, art as X, art2 as Y, art3 as Z, art10 as T, art11 as U, art12 as V12
from genesis.ch02 import rows, grid, W1, W2, W3, NIGHT, STORM, DUSK, SKY, GREY, DAWN
from genesis.ch03 import clan, hud, SAND, HOT, BLOOD, GREEN
from genesis.ch04 import fc, TENT, EMBER, GLOW, COLD
from genesis.ch06 import RUST, GREENLIT, GOLDEN
from genesis.ch12 import COURT
from genesis.ch07 import RED, BLUE
from genesis.ch14 import talk, ISRAEL, ISRAEL_WEEP
from genesis.ch15 import wagons
from mk import defs, face

v, sp = G.v, G.span
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic", "LieB", "LieA")
LEAH_C, ZILPAH_C, RACHEL_C, BILHAH_C = "#6A7AD8", "#8A6AB8", "#C2456A", "#1F7A8C"
ISRAEL_OLD = F("adam", skin="#C98E66", shadow="#6A4A5A", hair="#F3EFE6", hl="#C8C2B6", beard=True, beard_color="#F3EFE6", light="#FFE680")
ISRAEL_DYING = F("adam", skin="#B9A090", shadow="#5A4A5A", hair="#F3EFE6", hl="#C8C2B6", beard=True, beard_color="#F3EFE6", brow="sorrow", light="#9FB8FF")
EGYPTIAN = V12.BAKER
START = 240                                  # chapter 15 ends on page 239
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def cosmic(w, h, cx=None): return X.cosmic(w, h, cx)

def goshen(p, w, h, seed, people=True):
    """The land of Goshen: green pasture by the river, tents and flocks, pyramids far off."""
    b = h * 0.86
    return (Z.sun(w * 0.86, h * 0.18, 14, op=0.25) + EG.pyramid(w * 0.9, h * 0.6, w * 0.16, h * 0.2) + Y.ground(w, h, h * 0.6, "#8AAA5A", dy=0)
            + "".join(Z.E4.tent(w * x, h * 0.64, w * 0.08, h * 0.12) for x in (0.12, 0.22, 0.32))
            + Z.flock(w * 0.04, w * 0.96, h * 0.7, h * 0.96, 18, seed, cows=0.3, smin=0.16, smax=0.3))


@P("GEN-C16-00-Title", "Chapter 16 · Israel in Egypt")
def title():
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A1A2E"></rect>' + defs("tt16", *ALL) + goshen("tt16", 760, 1080, 161)
    return chapter_title(16, "第十六話", "Israel in Egypt", "Genesis 46 – 47", svg, DAWN,
                         v("46:30", frm="Now let me die,", to="yet alive."), "Genesis · Volume One")


@P("GEN-C16-P01-Visions", "240 · Fear Not to Go Down into Egypt")
def p01():
    t, h = rows(220, 340, None)
    r1 = new(SKY, W1, h[0], defs("c161a", *ALL) + T.stage("c161a", W1, h[0], 1611, "sand", [("israel", 0.66, 0.42, False, "raise")], props=Z.A4.altar(W1 * 0.4, h[0] * 0.88, 0.5, seed=1611)),
             cap(v("46:1"), "left: 12px; top: 12px", size=11, maxw=420) + vref("GEN 46:1", "right: 12px; bottom: 12px"))
    r2 = new(NIGHT, W1, h[1], cosmic(W1, h[1]),
             cap(v("46:2", to="and said,"), "left: 12px; top: 12px", size=10.5, maxw=500)
             + god(v("46:2", frm="Jacob, Jacob.", to="Jacob."), "left: 12px; top: 64px", size=26, maxw=420)
             + cap(v("46:2", frm="And he said,", to="said,"), "right: 12px; top: 64px", size=10.5)
             + balloon(v("46:2", frm="Here am I."), "right: 12px; top: 98px", 150, size=14, pad="12px 14px")
             + cap(v("46:3", to="he said,"), "left: 12px; top: 150px", size=10.5)
             + god(v("46:3", frm="I am God") + " " + v("46:4"), "left: 12px; top: 186px", size=15, maxw=660) + vref("GEN 46:2–4"))
    r3 = new(SAND, W1, h[2], wagons(None, W1, h[2], 1613),
             cap(v("46:5"), "left: 12px; top: 12px", size=10.5, maxw=440) + cap(v("46:6") + " " + v("46:7"), "right: 12px; top: 96px", size=10, maxw=330) + vref("GEN 46:5–7", "right: 12px; bottom: 12px"))
    return page("Genesis 46:1–7 — Fear Not to Go Down into Egypt", t, r1 + r2 + r3, START + 0)


@P("GEN-C16-P02-Souls1", "241 · The Names of the Children of Israel")
def p02():
    cells = [clan("Reuben", v("46:8") + " " + v("46:9"), "GEN 46:8–9", LEAH_C, of="OF LEAH", size=13),
             clan("Simeon", v("46:10"), "GEN 46:10", LEAH_C, of="OF LEAH", size=14),
             clan("Levi", v("46:11"), "GEN 46:11", LEAH_C, of="OF LEAH", size=15),
             clan("Judah", v("46:12"), "GEN 46:12", LEAH_C, of="OF LEAH", size=13),
             clan("Issachar · Zebulun", v("46:13") + " " + v("46:14"), "GEN 46:13–14", LEAH_C, of="OF LEAH", size=14),
             clan("The Sons of Leah", v("46:15"), "GEN 46:15", LEAH_C, size=13),
             clan("Gad · Asher", v("46:16") + " " + v("46:17"), "GEN 46:16–17", ZILPAH_C, of="OF ZILPAH", size=12.5),
             clan("The Sons of Zilpah", v("46:18"), "GEN 46:18", ZILPAH_C, size=13.5)]
    return page("Genesis 46:8–18 — The Names of the Children of Israel", "minmax(0, 1fr)", grid(cells, "repeat(4, minmax(0, 1fr))"), START + 1)


@P("GEN-C16-P03-Souls2", "242 · Threescore and Ten")
def p03():
    t, h = rows(None, 230)
    cells = [clan("Joseph · Benjamin", v("46:19") + " " + v("46:20"), "GEN 46:19–20", RACHEL_C, of="OF RACHEL", size=12.5),
             clan("Benjamin", v("46:21"), "GEN 46:21", RACHEL_C, of="OF RACHEL", size=13),
             clan("The Sons of Rachel", v("46:22"), "GEN 46:22", RACHEL_C, size=14),
             clan("Dan · Naphtali", v("46:23") + " " + v("46:24"), "GEN 46:23–24", BILHAH_C, of="OF BILHAH", size=14),
             clan("The Sons of Bilhah", v("46:25"), "GEN 46:25", BILHAH_C, size=13),
             clan("All the Souls", v("46:26"), "GEN 46:26", "#FFD23F", size=13)]
    r2 = new("#12113A", W1, h[1], seventy(W1, h[1]), cap(v("46:27"), "left: 12px; top: 12px", size=11, maxw=500) + hud("70", "right: 14px; top: 12px", size=30) + vref("GEN 46:27", "right: 12px; bottom: 12px"))
    return page("Genesis 46:19–27 — Threescore and Ten", t, grid(cells, "repeat(3, minmax(0, 1fr))") + r2, START + 2)

def seventy(w, h):
    o = [mk.stars(30, w, h, 1627)]
    cols_ = [LEAH_C] * 33 + [ZILPAH_C] * 16 + [RACHEL_C] * 14 + [BILHAH_C] * 7
    for i, c in enumerate(cols_):
        x = w * (0.04 + (i % 35) * 0.0265); y = h * (0.62 + (i // 35) * 0.16)
        o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{c}" stroke="#0D0D0F" stroke-width="1.2"></circle>')
    return "".join(o)


@P("GEN-C16-P04-Neck", "243 · He Fell on His Neck")
def p04():
    t, h = rows(230, 330, None)
    r1 = new(GREEN, W1, h[0], defs("c164a", *ALL) + goshen("c164a", W1, h[0], 1641) + Z.E3.chariot(W1 * 0.7, h[0] * 0.92, 0.5, color="#E8B830", driver="#F3EFE6"),
             cap(v("46:28"), "left: 12px; top: 12px", size=10.5, maxw=420) + vref("GEN 46:28", "right: 12px; top: 12px"))
    arm = [(-22, -158), (2, -150), (22, -164)]
    r2 = new(GOLDEN, W1, h[1], defs("c164b", *ALL) + T.stage("c164b", W1, h[1], 1642, "field", [("joseph_eg", 0.46, 0.36, False, arm), ("israel", 0.56, 0.38, True, arm)]),
             cap(v("46:29"), "left: 12px; top: 12px", size=11, maxw=420) + sfx("ううっ", "UU", "right: 30px; top: 20px", size=46, fill="#F3EFE6", stroke="#7A3A3A", rot=-4) + vref("GEN 46:29", "right: 12px; bottom: 12px"))
    r3 = talk(ISRAEL_WEEP, h[2], COLD, [("cap", v("46:30", to="unto Joseph,")), ("say", v("46:30", frm="Now let me"))], ref="GEN 46:30")
    return page("Genesis 46:28–30 — He Fell on His Neck", t, r1 + r2 + r3, START + 3)


@P("GEN-C16-P05-Shepherds", "244 · Every Shepherd Is an Abomination unto the Egyptians")
def p05():
    t, h = rows(None)
    r1 = new(COURT, W1, h[0], face(V12.JOSEPH_EG, -60, h[0] - 560, 1.4),
             cap(v("46:31", to="his father's house,"), "left: 330px; top: 16px", size=11, maxw=360)
             + balloon(v("46:31", frm="I will go up") + " " + v("46:32") + " " + v("46:33") + " " + v("46:34"), "left: 290px; top: 90px", 410, size=13.5, pad="60px 46px")
             + vref("GEN 46:31–34", "left: 12px; bottom: 12px"))
    return page("Genesis 46:31–34 — Every Shepherd Is an Abomination unto the Egyptians", t, r1, START + 4)


@P("GEN-C16-P06-Pharaoh", "245 · What Is Your Occupation?")
def p06():
    t, h = rows(260, 220, None)
    r1 = talk(V12.JOSEPH_EG, h[0], COURT, [("cap", v("47:1", to="and said,")), ("say", v("47:1", frm="My father")), ("cap", v("47:2"))], ref="GEN 47:1–2")
    r2 = cols(talk(V12.PHARAOH, h[1], COURT, [("cap", v("47:3", to="unto his brethren,")), ("say", v("47:3", frm="What is", to="occupation?"))], w=W2, ref="GEN 47:3", size=12),
              talk(U.JUDAH, h[1], RUST, [("cap", v("47:3", frm="And they said", to="unto Pharaoh,")), ("say", v("47:3", frm="Thy servants are shepherds,"))], w=W2, size=12))
    r3 = talk(U.REUBEN, h[2], GOLDEN, [("cap", v("47:4", to="unto Pharaoh,")), ("say", v("47:4", frm="To sojourn"))], ref="GEN 47:4")
    return page("Genesis 47:1–4 — What Is Your Occupation?", t, r1 + r2 + r3, START + 5)


@P("GEN-C16-P07-Blessed", "246 · Few and Evil Have Been the Days")
def p07():
    t, h = rows(250, 170, None)
    r1 = talk(V12.PHARAOH, h[0], COURT, [("cap", v("47:5", to="saying,")), ("say", v("47:5", frm="Thy father") + " " + v("47:6"))], ref="GEN 47:5–6")
    r2 = new(COURT, W1, h[1], defs("c167b", *ALL) + T.stage("c167b", W1, h[1], 1672, "palace", [("pharaoh", 0.66, 0.3, True), ("israel", 0.42, 0.36, False, "raise"), ("joseph_eg", 0.28, 0.36)]),
             cap(v("47:7"), "left: 12px; top: 12px", size=10.5, maxw=500) + vref("GEN 47:7", "right: 12px; bottom: 12px"))
    r3 = cols(talk(V12.PHARAOH, h[2], COURT, [("cap", v("47:8", to="unto Jacob,")), ("say", v("47:8", frm="How many"))], w=W2, ref="GEN 47:8", size=12.5),
              new(GOLDEN, W2, h[2], face(ISRAEL_OLD, -50, h[2] - 300, 0.78),
                  cap(v("47:9", to="unto Pharaoh,"), "right: 8px; top: 8px", size=10)
                  + balloon(v("47:9", frm="The days"), "right: 8px; top: 40px", 230, size=11, pad="26px 24px")
                  + cap(v("47:10"), "right: 8px; bottom: 8px", size=10, maxw=210) + vref("GEN 47:9–10", "left: 8px; bottom: 8px")))
    return page("Genesis 47:5–10 — Few and Evil Have Been the Days", t, r1 + r2 + r3, START + 6)


@P("GEN-C16-P08-Rameses", "247 · The Land of Rameses")
def p08():
    t, h = rows(250, 230, None)
    r1 = new(GREEN, W1, h[0], defs("c168a", *ALL) + goshen("c168a", W1, h[0], 1681),
             cap(v("47:11"), "left: 12px; top: 12px", size=10.5, maxw=440) + cap(v("47:12"), "right: 12px; bottom: 28px", size=10.5, maxw=300) + vref("GEN 47:11–12", "left: 12px; bottom: 12px"))
    r2 = new(HOT, W1, h[1], Z.famine(W1, h[1], 1682),
             cap(v("47:13"), "left: 12px; top: 12px", size=11, maxw=420) + cap(v("47:14"), "right: 12px; bottom: 14px", size=10.5, maxw=330) + vref("GEN 47:13–14", "left: 12px; bottom: 12px"))
    r3 = cols(talk(EGYPTIAN, h[2], RED, [("cap", v("47:15", to="and said,")), ("say", v("47:15", frm="Give us"))], w=W2, ref="GEN 47:15", size=12),
              talk(V12.JOSEPH_EG, h[2], COURT, [("cap", v("47:16", to="said,")), ("say", v("47:16", frm="Give your"))], w=W2, ref="GEN 47:16", size=12.5))
    return page("Genesis 47:11–16 — The Land of Rameses", t, r1 + r2 + r3, START + 7)


@P("GEN-C16-P09-Land", "248 · Buy Us and Our Land for Bread")
def p09():
    t, h = rows(230, None)
    r1 = new(SAND, W1, h[0], defs("c169a", *ALL) + T.stage("c169a", W1, h[0], 1691, "egypt", [("joseph_eg", 0.14, 0.42)],
                                                              props=Z.E3.horse(W1 * 0.36, h[0] * 0.9, 0.3) + Z.A.cow(W1 * 0.5, h[0] * 0.92, 0.24) + Z.E.sheep(W1 * 0.6, h[0] * 0.94, 0.3) + Z.N.ass(W1 * 0.68, h[0] * 0.92, 0.18)),
             cap(v("47:17"), "right: 12px; top: 12px", size=10.5, maxw=440) + vref("GEN 47:17", "right: 12px; bottom: 12px"))
    r2 = talk(EGYPTIAN, h[1], RED, [("cap", v("47:18", to="said unto him,")), ("say", v("47:18", frm="We will not") + " " + v("47:19"))], ref="GEN 47:18–19", size=13.5)
    return page("Genesis 47:17–19 — Buy Us and Our Land for Bread", t, r1 + r2, START + 8)


@P("GEN-C16-P10-Fifth", "249 · A Fifth unto Pharaoh")
def p10():
    t, h = rows(250, 310, None)
    r1 = new(SAND, W1, h[0], defs("c1610a", *ALL) + V12.bread_lines("c1610a", W1, h[0], 16101),
             cap(v("47:20") + " " + v("47:21"), "left: 12px; top: 12px", size=10.5, maxw=440) + cap(v("47:22"), "right: 12px; bottom: 30px", size=10, maxw=300) + vref("GEN 47:20–22", "left: 12px; bottom: 12px"))
    r2 = talk(V12.JOSEPH_EG, h[1], COURT, [("cap", v("47:23", to="unto the people,")), ("say", v("47:23", frm="Behold") + " " + v("47:24"))], ref="GEN 47:23–24",
              extra=hud("1/5", "right: 14px; bottom: 14px", size=26))
    r3 = cols(talk(EGYPTIAN, h[2], GOLDEN, [("cap", v("47:25", to="said,")), ("say", v("47:25", frm="Thou hast"))], w=W2, ref="GEN 47:25", size=12),
              new(V12.EGYPT_BG, W2, h[2], V12.handfuls(None, W2, h[2], 16103), cap(v("47:26"), "left: 8px; top: 8px", size=10.5, maxw=320) + vref("GEN 47:26", "right: 8px; bottom: 8px")))
    return page("Genesis 47:20–26 — A Fifth unto Pharaoh", t, r1 + r2 + r3, START + 9)


@P("GEN-C16-P11-Thigh", "250 · Bury Me Not, I Pray Thee, in Egypt")
def p11():
    t, h = rows(230, None)
    r1 = new(GREEN, W1, h[0], defs("c1611a", *ALL) + goshen("c1611a", W1, h[0], 16111),
             cap(v("47:27"), "left: 12px; top: 12px", size=11, maxw=400) + cap(v("47:28"), "right: 12px; bottom: 30px", size=10.5, maxw=320)
             + hud("147", "left: 14px; bottom: 30px", size=26) + vref("GEN 47:27–28", "right: 12px; bottom: 10px"))
    r2 = new(COLD, W1, h[1], face(ISRAEL_DYING, -60, h[1] - 560, 1.4),
             cap(v("47:29", to="and said unto him,"), "left: 330px; top: 16px", size=11, maxw=360)
             + balloon(v("47:29", frm="If now") + " " + v("47:30", to="burying-place."), "left: 300px; top: 90px", 390, size=13, pad="44px 40px")
             + cap(v("47:30", frm="And he said,", to="said,"), "left: 330px; top: 440px", size=11)
             + balloon(v("47:30", frm="I will do"), "left: 320px; top: 480px", 280, size=13, pad="14px 20px")
             + cap(v("47:31", to="And he said,"), "left: 330px; top: 560px", size=11)
             + balloon(v("47:31", frm="Swear unto me:", to="me:"), "left: 330px; top: 600px", 200, size=14, pad="12px 16px")
             + cap(v("47:31", frm="and he sware"), "right: 14px; bottom: 16px", size=11.5, maxw=380)
             + end_mark("NEXT · THE BLESSING OF JACOB", "left: 14px; top: 14px") + vref("GEN 47:29–31", "left: 12px; bottom: 12px"))
    return page("Genesis 47:27–31 — Bury Me Not, I Pray Thee, in Egypt", t, r1 + r2, START + 10)
