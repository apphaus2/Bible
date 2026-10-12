"""Exodus volume, Chapter 8 — The Pattern of the Tabernacle (Exodus 25–27). Every verse, word for word from ref/asv.
God's instructions are set as blueprint pages: art8's technical drawings (cubits marked) with the words in Voice boxes."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk, exodus4 as E4, exodus5 as V
from fx import use, new, vref, page, chapter_title, end_mark, cols, cap, god, balloon, sfx
from reuse import panels
from exo import G, art as A, art8 as B8
from exo.ch06 import MOUNT
from genesis.ch02 import rows, grid, W1, W2, NIGHT
from mk import defs

v, sp = G.v, G.span
INK = B8.INK
CU, = [panels("digest/exodus/book-05/" + n + ".dc.html") for n in ["EX5-P01-ComeUp"]]
START = 123                                  # chapter 7 ends on page 122
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco

def plan(w, h, art, words, ref, pos="left: 12px; bottom: 12px", size=14, maxw=None, extra=""):
    """A blueprint panel: the drawing, God's words in a Voice box, the verse label in the top right corner."""
    return new(INK, w, h, art, god(words, pos, size=size, maxw=maxw) + vref(ref, "right: 8px; top: 8px") + extra)


@P("EXO-C08-00-Title", "Chapter 8 · The Pattern of the Tabernacle")
def title():
    svg = B8.bp(760, 1080) + B8.mercy_seat(760, 1080, grid=False, cx=0.5, scale=1.2)
    return chapter_title(8, "第八話", "The Pattern of the Tabernacle", "Exodus 25 – 27", svg, INK,
                         v("25:8"), "Exodus · Volume Two")


@P("EXO-C08-P01-Offering", "123 · Of Every Man Whose Heart Maketh Him Willing")
def p01():
    t, h = rows(200, 300, None)
    r1 = use(CU[2], over=cap(v("25:1"), "left: 12px; top: 12px", size=11) + god(v("25:2"), "left: 12px; top: 48px", size=16, maxw=520) + mk.stamp(25, "right: 14px; bottom: 12px") + vref("EX 25:1–2", "left: 12px; bottom: 12px"))
    r2 = plan(W1, h[1], B8.offering(W1, h[1]), v("25:3") + " " + v("25:4") + " " + v("25:5") + " " + v("25:6") + " " + v("25:7"), "EX 25:3–7", pos="left: 12px; bottom: 12px", size=12.5, maxw=640)
    r3 = plan(W1, h[2], B8.sanctuary(W1, h[2]), v("25:8") + " " + v("25:9"), "EX 25:8–9", pos="left: 12px; top: 34px", size=16, maxw=420)
    return page("Exodus 25:1–9 — Of Every Man Whose Heart Maketh Him Willing", t, r1 + r2 + r3, START + 0)


@P("EXO-C08-P02-Ark", "124 · An Ark of Acacia Wood")
def p02():
    t, h = rows(500, None)
    r1 = plan(W1, h[0], B8.ark(W1, h[0]), v("25:10") + " " + v("25:11"), "EX 25:10–11", pos="left: 12px; top: 34px", size=15, maxw=400)
    r2 = cols(plan(W2, h[1], B8.ark(W2, h[1], staves=True), v("25:12") + " " + v("25:13"), "EX 25:12–13", pos="left: 8px; top: 30px", size=13, maxw=320),
              plan(W2, h[1], B8.ark(W2, h[1], testimony=True), v("25:14") + " " + v("25:15") + " " + v("25:16"), "EX 25:14–16", pos="left: 8px; top: 30px", size=13, maxw=320))
    return page("Exodus 25:10–16 — An Ark of Acacia Wood", t, r1 + r2, START + 1)


@P("EXO-C08-P03-MercySeat", "125 · There I Will Meet with Thee")
def p03():
    t, h = rows(520, None)
    r1 = plan(W1, h[0], B8.mercy_seat(W1, h[0]), v("25:17") + " " + v("25:18") + " " + v("25:19") + " " + v("25:20"), "EX 25:17–20", pos="left: 12px; top: 34px", size=13.5, maxw=330)
    r2 = new(NIGHT, W1, h[1], B8.mercy_seat(W1, h[1], grid=False, cx=0.5, scale=0.9),
             god(v("25:21") + " " + v("25:22"), "left: 12px; top: 12px", size=15, maxw=640) + vref("EX 25:21–22", "right: 8px; bottom: 8px"))
    return page("Exodus 25:17–22 — There I Will Meet with Thee", t, r1 + r2, START + 2)


@P("EXO-C08-P04-Table", "126 · Showbread before Me Alway")
def p04():
    t, h = rows(500, None)
    r1 = plan(W1, h[0], B8.table(W1, h[0], bread=False, vessels=False), v("25:23") + " " + v("25:24") + " " + v("25:25"), "EX 25:23–25", pos="left: 12px; top: 34px", size=14.5, maxw=440)
    r2 = cols(plan(W2, h[1], B8.table(W2, h[1], bread=False, vessels=False), v("25:26") + " " + v("25:27") + " " + v("25:28"), "EX 25:26–28", pos="left: 8px; top: 30px", size=12.5, maxw=320),
              plan(W2, h[1], B8.table(W2, h[1]), v("25:29") + " " + v("25:30"), "EX 25:29–30", pos="left: 8px; top: 30px", size=12.5, maxw=320))
    return page("Exodus 25:23–30 — Showbread before Me Alway", t, r1 + r2, START + 3)


@P("EXO-C08-P05-Candlestick", "127 · A Candlestick of Pure Gold")
def p05():
    t, h = rows(None)
    r1 = plan(W1, h[0], B8.lampstand(W1, h[0], lit=False), v("25:31") + " " + v("25:32") + " " + v("25:33") + " " + v("25:34") + " " + v("25:35") + " " + v("25:36"),
              "EX 25:31–36", pos="left: 12px; top: 34px", size=14, maxw=660)
    return page("Exodus 25:31–36 — A Candlestick of Pure Gold", t, r1, START + 4)


@P("EXO-C08-P06-Curtains", "128 · After Their Pattern")
def p06():
    t, h = rows(380, None)
    r1 = cols(plan(W2, h[0], B8.lampstand(W2, h[0]), v("25:37"), "EX 25:37", pos="left: 8px; top: 30px", size=13.5, maxw=320),
              plan(W2, h[0], B8.snuffers(W2, h[0]), v("25:38") + " " + v("25:39") + " " + v("25:40"), "EX 25:38–40", pos="left: 8px; bottom: 8px", size=13, maxw=320))
    r2 = plan(W1, h[1], B8.curtains(W1, h[1], loops=False), v("26:1") + " " + v("26:2") + " " + v("26:3"), "EX 26:1–3", pos="left: 50%; top: 40%; transform: translate(-50%, -50%)", size=15, maxw=480,
              extra=mk.stamp(26, "right: 14px; bottom: 30px"))
    return page("Exodus 25:37–26:3 — After Their Pattern", t, r1 + r2, START + 5)


@P("EXO-C08-P07-Loops", "129 · Fifty Loops, Fifty Clasps")
def p07():
    t, h = rows(420, None)
    r1 = plan(W1, h[0], B8.curtains(W1, h[0], area=(0.1, 0.5)), v("26:4") + " " + v("26:5") + " " + v("26:6"), "EX 26:4–6", pos="left: 12px; bottom: 12px", size=14, maxw=670)
    r2 = plan(W1, h[1], B8.curtains(W1, h[1], n=11, length="30", color="#3A3430", couple=(5, 6), clasps="BRASS", cherubim=False, loops=False),
              v("26:7") + " " + v("26:8") + " " + v("26:9"), "EX 26:7–9", pos="left: 50%; top: 45%; transform: translate(-50%, -50%)", size=15, maxw=480)
    return page("Exodus 26:4–9 — Fifty Loops, Fifty Clasps", t, r1 + r2, START + 6)


@P("EXO-C08-P08-Coverings", "130 · A Covering of Rams' Skins Dyed Red")
def p08():
    t, h = rows(300, 300, None)
    r1 = plan(W1, h[0], B8.curtains(W1, h[0], n=11, length="30", color="#3A3430", couple=(5, 6), clasps="BRASS", cherubim=False, area=(0.12, 0.5)), v("26:10") + " " + v("26:11"), "EX 26:10–11",
              pos="left: 12px; bottom: 12px", size=14.5, maxw=670)
    r2 = plan(W1, h[1], B8.overhang(W1, h[1]), v("26:12") + " " + v("26:13"), "EX 26:12–13", pos="left: 12px; top: 34px", size=13, maxw=280)
    r3 = plan(W1, h[2], B8.coverings(W1, h[2]), v("26:14"), "EX 26:14", pos="left: 12px; top: 34px", size=15, maxw=260)
    return page("Exodus 26:10–14 — A Covering of Rams' Skins Dyed Red", t, r1 + r2 + r3, START + 7)


@P("EXO-C08-P09-Boards", "131 · Boards of Acacia Wood, Standing Up")
def p09():
    t, h = rows(400, None)
    r1 = plan(W1, h[0], B8.board(W1, h[0]), v("26:15") + " " + v("26:16") + " " + v("26:17") + " " + v("26:18") + " " + v("26:19"), "EX 26:15–19", pos="right: 12px; top: 34px", size=13.5, maxw=380)
    r2 = plan(W1, h[1], B8.frame_plan(W1, h[1]), v("26:20") + " " + v("26:21") + " " + v("26:22") + " " + v("26:23") + " " + v("26:24") + " " + v("26:25"), "EX 26:20–25",
              pos="left: 50%; top: 52%; transform: translate(-50%, -50%)", size=12.5, maxw=500)
    return page("Exodus 26:15–25 — Boards of Acacia Wood, Standing Up", t, r1 + r2, START + 8)


@P("EXO-C08-P10-Veil", "132 · The Veil Shall Separate")
def p10():
    t, h = rows(400, None)
    r1 = plan(W1, h[0], B8.frame_plan(W1, h[0], bars=True), v("26:26") + " " + v("26:27") + " " + v("26:28") + " " + v("26:29") + " " + v("26:30"), "EX 26:26–30",
              pos="left: 50%; top: 52%; transform: translate(-50%, -50%)", size=13, maxw=500)
    r2 = plan(W1, h[1], B8.veil_elev(W1, h[1]), v("26:31") + " " + v("26:32") + " " + v("26:33"), "EX 26:31–33", pos="left: 50%; top: 50%; transform: translate(-50%, -50%)", size=14, maxw=500)
    return page("Exodus 26:26–33 — The Veil Shall Separate", t, r1 + r2, START + 9)


@P("EXO-C08-P11-Altar", "133 · The Holy Place and the Most Holy")
def p11():
    t, h = rows(370, 210, None)
    r1 = plan(W1, h[0], B8.frame_plan(W1, h[0], veil=True, furniture=True, screen=True, area=(0.14, 0.62)), v("26:34") + " " + v("26:35"), "EX 26:34–35", pos="left: 12px; bottom: 12px", size=13, maxw=670)
    r2 = plan(W1, h[1], B8.screen_elev(W1, h[1]), v("26:36") + " " + v("26:37"), "EX 26:36–37", pos="left: 50%; top: 50%; transform: translate(-50%, -50%)", size=14, maxw=500)
    r3 = plan(W1, h[2], B8.altar(W1, h[2], grating=False, staves=False, vessels=True), v("27:1") + " " + v("27:2") + " " + v("27:3"), "EX 27:1–3", pos="right: 12px; top: 34px", size=12.5, maxw=260,
              extra=mk.stamp(27, "left: 150px; top: 30px"))
    return page("Exodus 26:34–27:3 — The Holy Place and the Most Holy", t, r1 + r2 + r3, START + 10)


@P("EXO-C08-P12-Court", "134 · The Court of the Tabernacle")
def p12():
    t, h = rows(440, None)
    r1 = plan(W1, h[0], B8.altar(W1, h[0]), v("27:4") + " " + v("27:5") + " " + v("27:6") + " " + v("27:7") + " " + v("27:8"), "EX 27:4–8", pos="left: 12px; top: 34px", size=13, maxw=260)
    r2 = plan(W1, h[1], B8.court(W1, h[1], show=("S", "N")), v("27:9") + " " + v("27:10") + " " + v("27:11"), "EX 27:9–11", pos="left: 50%; top: 52%; transform: translate(-50%, -50%)", size=13, maxw=420)
    return page("Exodus 27:4–11 — The Court of the Tabernacle", t, r1 + r2, START + 11)


@P("EXO-C08-P13-Oil", "135 · A Lamp to Burn Continually")
def p13():
    t, h = rows(400, 270, None)
    r1 = plan(W1, h[0], B8.court(W1, h[0]), v("27:12") + " " + v("27:13") + " " + v("27:14") + " " + v("27:15") + " " + v("27:16"), "EX 27:12–16", pos="left: 50%; top: 52%; transform: translate(-50%, -50%)", size=11.5, maxw=440)
    r2 = plan(W1, h[1], B8.court_elev(W1, h[1], x0f=0.52), v("27:17") + " " + v("27:18") + " " + v("27:19"), "EX 27:17–19", pos="left: 12px; top: 34px", size=12.5, maxw=340)
    r3 = plan(W1, h[2], B8.olive_oil(W1, h[2]), v("27:20") + " " + v("27:21"), "EX 27:20–21", pos="left: 12px; bottom: 12px", size=12.5, maxw=400,
              extra=end_mark("NEXT · HOLY TO JEHOVAH", "right: 12px; bottom: 12px"))
    return page("Exodus 27:12–21 — A Lamp to Burn Continually", t, r1 + r2 + r3, START + 12)
