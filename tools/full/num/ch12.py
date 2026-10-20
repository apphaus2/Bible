"""Numbers volume, Chapter 12 — Phinehas (Numbers 25–26). Every verse, word for word from ref/eng-asv.
Baal-peor (from afar; 25:4–5 in captions over an empty plain); Phinehas (25:8 told in a caption over the shut pavilion);
the covenant of peace; and the numbering in the plains of Moab as tally cells, with the land divided by lot, the Levites,
and Caleb and Joshua alone left of the first numbering."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import new, vref, page, chapter_title, end_mark, cols, cap, god, balloon
from exo import art as A, art8 as B8
from exo.kit import talk
from num import G, art as K, art6 as K6, art7 as K7, art10 as K10, art12 as K12
from num.ch01 import tally
from num.pages import Pages
from genesis import art as X
from genesis.ch02 import rows, grid, W1, W2, NIGHT, SKY, DUSK
from genesis.ch03 import SAND, hud, clan
from genesis.ch04 import COLD, EMBER
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from num import ch11 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
LEVI_C = "#E04A2A"

def night(h, over, w=W1): return new(NIGHT, w, h, X.cosmic(w, h), over)
def after(ref, to):
    t = v(ref); return v(ref, frm=t[t.index(to) + len(to):].strip())


@P("NUM-C12-00-Title", "Chapter 12 · Phinehas", title=True)
def title(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A1A2A"></rect>' + f'<g transform="translate(0 380)">{K12.pavilion("t12", 760, 700, 1201, phinehas=True)}</g>'
    return chapter_title(12, "第十二話", "Phinehas", "Numbers 25 – 26", svg, "#3A1A2A", v("25:12", frm="Behold, I give"), "Numbers · Volume Four")


@P("NUM-C12-P01-Peor", "Baal-peor")
def p01(n):
    t, h = rows(None, 300)
    r1 = new("#C85A3A", W1, h[0], K12.peor("v1a", W1, h[0], 1211), mk.stamp(25, "right: 14px; top: 12px") + cap(v("25:1") + " " + v("25:2") + " " + v("25:3"), "left: 12px; top: 12px", size=13, maxw=520) + vref("NUM 25:1–3", "right: 12px; bottom: 12px"))
    r2 = new("#F3D8A0", W1, h[1], K12.hard_sun(W1, h[1], 1212), cap(v("25:4", to="unto Moses,"), "left: 12px; top: 12px", size=11) + god(after("25:4", "unto Moses,"), "left: 12px; top: 50px", size=17, maxw=640)
             + cap(v("25:5"), "left: 12px; bottom: 12px", size=12, maxw=520) + vref("NUM 25:4–5", "right: 12px; bottom: 12px"))
    return page("Numbers 25:1–5 — Baal-peor", t, r1 + r2, n)


@P("NUM-C12-P02-Phinehas", "Phinehas Rose Up")
def p02(n):
    t, h = rows(330, 260, None)
    r1 = new("#3A1A2A", W1, h[0], K12.pavilion("v2a", W1, h[0], 1221, phinehas=False, entering=True), cap(v("25:6"), "left: 12px; top: 12px", size=12, maxw=420) + vref("NUM 25:6", "right: 12px; bottom: 12px"))
    r2 = talk(K12.PHINEHAS, h[1], RED, [("cap", v("25:7"))], ref="NUM 25:7", size=14)
    r3 = new("#3A1A2A", W1, h[2], K12.pavilion("v2c", W1, h[2], 1223), cap(v("25:8") + " " + v("25:9"), "left: 12px; top: 12px", size=12.5, maxw=380) + hud("24,000", "right: 16px; top: 16px", size=30) + vref("NUM 25:8–9", "right: 12px; bottom: 12px"))
    return page("Numbers 25:6–9 — Phinehas Rose Up", t, r1 + r2 + r3, n)


@P("NUM-C12-P03-Peace", "My Covenant of Peace")
def p03(n):
    t, h = rows(None, 280)
    r1 = night(h[0], cap(v("25:10"), "left: 12px; top: 12px", size=11) + god(sp("25:11-13"), "left: 12px; top: 50px", size=21, maxw=640) + vref("NUM 25:10–13", "right: 12px; bottom: 12px"))
    r2 = talk(K12.PHINEHAS_CALM, h[1], GOLDEN, [("cap", v("25:14") + " " + v("25:15"))], ref="NUM 25:14–15", size=13)
    return page("Numbers 25:10–15 — My Covenant of Peace", t, r1 + r2, n)


@P("NUM-C12-P04-Vex", "Vex the Midianites")
def p04(n):
    t, h = rows(300, None)
    r1 = night(h[0], cap(v("25:16"), "left: 12px; top: 12px", size=11) + god(v("25:17") + " " + v("25:18"), "left: 12px; top: 50px", size=19, maxw=640) + vref("NUM 25:16–18", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], K.muster("v4b", W1, h[1], 1242, rows_=4, per=13), mk.stamp(26, "right: 14px; top: 12px") + cap(v("26:1"), "left: 12px; top: 12px", size=11.5, maxw=470)
             + god(v("26:2"), "left: 12px; top: 80px", size=16, maxw=430) + cap(v("26:3") + " " + v("26:4"), "left: 12px; bottom: 12px", size=11.5, maxw=430) + vref("NUM 26:1–4", "right: 12px; bottom: 12px"))
    return page("Numbers 25:16–26:4 — Vex the Midianites", t, r1 + r2, n)


@P("NUM-C12-P05-Reuben", "In the Plains of Moab")
def p05(n):
    cells = [tally("REUBEN", "26:5-7", "43,730", size=13), clan("Pallu · Eliab", sp("26:8-11"), "NUM 26:8–11", K.TRIBE_C["REUBEN"], of="REUBEN", size=12),
             tally("SIMEON", "26:12-14", "22,200", size=13), tally("GAD", "26:15-18", "40,500", size=13)]
    return page("Numbers 26:5–18 — In the Plains of Moab", "minmax(0, 1fr)", grid(cells, "repeat(2, minmax(0, 1fr))"), n)


@P("NUM-C12-P06-Judah", "The Families of Judah")
def p06(n):
    cells = [tally("JUDAH", "26:19-22", "76,500", size=12.5), tally("ISSACHAR", "26:23-25", "64,300", size=13),
             tally("ZEBULUN", "26:26-27", "60,500", size=13), tally("MANASSEH", "26:28-34", "52,700", size=11.5, of="JOSEPH")]
    return page("Numbers 26:19–34 — The Families of Judah", "minmax(0, 1fr)", grid(cells, "repeat(2, minmax(0, 1fr))"), n)


@P("NUM-C12-P07-Ephraim", "Six Hundred Thousand and a Thousand")
def p07(n):
    t, h = rows(None, 150)
    cells = [tally("EPHRAIM", "26:35-37", "32,500", size=10.5, of="JOSEPH"), tally("BENJAMIN", "26:38-41", "45,600", size=10.5),
             tally("DAN", "26:42-43", "64,400", size=11), tally("ASHER", "26:44-47", "53,400", size=10.5), tally("NAPHTALI", "26:48-50", "45,400", size=11)]
    top = grid(cells, "repeat(3, minmax(0, 1fr))")
    r2 = new(SAND, W1, h[1], K.muster("v7b", W1, h[1], 1272, rows_=4, per=14, scribes=False), cap(v("26:51"), "left: 12px; top: 12px", size=13, maxw=420)
             + hud("601,730", "right: 16px; top: 16px", size=40) + vref("NUM 26:51", "right: 12px; bottom: 12px"))
    return page("Numbers 26:35–51 — Six Hundred Thousand and a Thousand", t, top + r2, n)


@P("NUM-C12-P08-Lot", "By Lot")
def p08(n):
    t, h = rows(None, 360)
    r1 = night(h[0], cap(v("26:52"), "left: 12px; top: 12px", size=11) + god(sp("26:53-56"), "left: 12px; top: 50px", size=22, maxw=640) + vref("NUM 26:52–56", "right: 12px; bottom: 12px"))
    r2 = new(B8.INK, W1, h[1], K12.lots(W1, h[1]), "")
    return page("Numbers 26:52–56 — By Lot", t, r1 + r2, n)


@P("NUM-C12-P09-Levites", "They That Were Numbered of the Levites")
def p09(n):
    t, h = rows(None, 300)
    cells = [clan("Levi", v("26:57") + " " + v("26:58"), "NUM 26:57–58", LEVI_C, size=13), clan("Amram · Jochebed", v("26:59"), "NUM 26:59", "#FFD23F", of="OF LEVI", size=14),
             clan("Aaron", v("26:60") + " " + v("26:61"), "NUM 26:60–61", "#8FB8E8", of="OF AMRAM", size=14), tally("LEVI", "26:62-62", "23,000", accent=LEVI_C, size=13)]
    r2 = new(DUSK, W1, h[1], K7.empty_wilderness(W1, h[1], 1292), cap(v("26:63") + " " + v("26:64") + " " + v("26:65"), "left: 12px; top: 12px", size=12.5, maxw=560)
             + vref("NUM 26:63–65", "left: 12px; bottom: 12px") + end_mark("NEXT · THE DAUGHTERS OF ZELOPHEHAD", "right: 10px; bottom: 10px"))
    return page("Numbers 26:57–65 — They That Were Numbered of the Levites", t, grid(cells, "repeat(2, minmax(0, 1fr))") + r2, n)
