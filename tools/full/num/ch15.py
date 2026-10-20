"""Numbers volume, Chapter 15 — The Journeys (Numbers 32–33). Every verse, word for word from ref/eng-asv.
Reuben, Gad and half Manasseh beyond the Jordan (dialogue with Moses, a map of their cities); then the journeys of the
children of Israel from Rameses to the plains of Moab: a route map lit stage by stage over a cell for every station."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import new, vref, page, chapter_title, end_mark, cols, cap, god, balloon
from exo import art as A
from exo.kit import talk
from num import G, art as K, art15 as K15
from num.pages import Pages
from genesis import art as X
from genesis.ch02 import rows, grid, W1, W2, NIGHT, SKY, DUSK
from genesis.ch03 import SAND
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from num import ch14 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
INK = "#0B1A2E"
NAMES = [s[0] for s in K15.STATIONS]

def night(h, over, w=W1): return new(NIGHT, w, h, X.cosmic(w, h), over)
def after(ref, to):
    t = v(ref); return v(ref, frm=t[t.index(to) + len(to):].strip())
def st(ref, name, accent="#FFD23F", size=None, text=None):
    return (name, text or v(ref), "NUM " + ref, accent, size)
def stages(n, title_ref, head, lit, items, ncol=3, top=300, extra_top=None):
    """A map strip with one stage of the journeys lit, over a grid of station cells; each cell's words sized to fill it."""
    t, h = rows(top, None)
    m = new(INK, W1, h[0], K15.stations_map(W1, h[0], lit=lit), extra_top or "")
    nrow = (len(items) + ncol - 1) // ncol
    cw = (702 - 12 * (ncol - 1)) / ncol - 22; ch = (h[1] + 6 - 12 * (nrow - 1)) / nrow - 50
    cells = []
    for nm, text, ref, accent, size in items:
        size = size or max(10.5, min(19, round((cw * ch / (0.66 * 1.4 * len(text))) ** 0.5 * 0.8 * 2) / 2))
        cells.append(K15.station(nm, text, ref, accent=accent, size=size))
    return page(f"Numbers {title_ref} — {head}", t, m + grid(cells, f"repeat({nrow}, minmax(0, 1fr))", ncol=ncol), n)


@P("NUM-C15-00-Title", "Chapter 15 · The Journeys", title=True)
def title(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#0B1A2E"></rect>' + f'<g transform="translate(0 370)">{K15.stations_map(760, 680, title="FROM RAMESES TO THE PLAINS OF MOAB")}</g>'
    return chapter_title(15, "第十五話", "The Journeys", "Numbers 32 – 33", svg, INK, v("33:2", to="by the commandment of Jehovah:"), "Numbers · Volume Four")


@P("NUM-C15-P01-Cattle", "A Place for Cattle")
def p01(n):
    t, h = rows(330, None)
    r1 = new(SKY, W1, h[0], K15.gilead("y1a", W1, h[0], 1511), mk.stamp(32, "right: 14px; top: 12px") + cap(v("32:1"), "left: 12px; top: 12px", size=12.5, maxw=520) + vref("NUM 32:1", "right: 12px; bottom: 12px"))
    r2 = talk(K15.GADITE, h[1], GOLDEN, [("cap", v("32:2")), ("say", v("32:3") + " " + v("32:4")), ("cap", v("32:5", to="And they said,")), ("say", after("32:5", "they said,"))], ref="NUM 32:2–5", size=15)
    return page("Numbers 32:1–5 — A Place for Cattle", t, r1 + r2, n)


@P("NUM-C15-P02-ShallYeSitHere", "Shall Ye Sit Here?")
def p02(n):
    t, h = rows(None, 330)
    r1 = talk(A.MOSES_STERN, h[0], RED, [("cap", v("32:6", to="the children of Reuben,")), ("say", after("32:6", "the children of Reuben,") + " " + sp("32:7-9"))], ref="NUM 32:6–9", size=16)
    r2 = talk(A.MOSES_STERN, h[1], RED, [("say", sp("32:10-12"))], ref="NUM 32:10–12", size=16, flip=True)
    return page("Numbers 32:6–12 — Shall Ye Sit Here?", t, r1 + r2, n)


@P("NUM-C15-P03-Increase", "An Increase of Sinful Men")
def p03(n):
    t, h = rows(None, 330)
    r1 = talk(A.MOSES_STERN, h[0], RED, [("say", sp("32:13-15"))], ref="NUM 32:13–15", size=18)
    r2 = talk(K15.GADITE, h[1], GOLDEN, [("cap", v("32:16", to="and said,")), ("say", after("32:16", "and said,") + " " + sp("32:17-19"))], ref="NUM 32:16–19", size=14, flip=True)
    return page("Numbers 32:13–19 — An Increase of Sinful Men", t, r1 + r2, n)


@P("NUM-C15-P04-FindYouOut", "Be Sure Your Sin Will Find You Out")
def p04(n):
    t, h = rows(None, 280)
    r1 = talk(A.MOSES, h[0], GOLDEN, [("cap", v("32:20", to="said unto them,")), ("say", after("32:20", "said unto them,") + " " + sp("32:21-24"))], ref="NUM 32:20–24", size=16)
    r2 = talk(K15.GADITE, h[1], GOLDEN, [("cap", v("32:25", to="saying,")), ("say", after("32:25", "saying,") + " " + v("32:26") + " " + v("32:27"))], ref="NUM 32:25–27", size=15, flip=True)
    return page("Numbers 32:20–27 — Be Sure Your Sin Will Find You Out", t, r1 + r2, n)


@P("NUM-C15-P05-Charge", "So Moses Gave Charge")
def p05(n):
    t, h = rows(None, 250)
    r1 = talk(A.MOSES, h[0], GOLDEN, [("cap", v("32:28")), ("cap", v("32:29", to="said unto them,")), ("say", after("32:29", "said unto them,") + " " + v("32:30"))], ref="NUM 32:28–30", size=15)
    r2 = talk(K15.GADITE, h[1], GOLDEN, [("cap", v("32:31", to="answered, saying,")), ("say", after("32:31", "answered, saying,") + " " + v("32:32"))], ref="NUM 32:31–32", size=15, flip=True)
    return page("Numbers 32:28–32 — So Moses Gave Charge", t, r1 + r2, n)


@P("NUM-C15-P06-Cities", "Fortified Cities, and Folds for Sheep")
def p06(n):
    t, h = rows(None, 280)
    r1 = new(INK, W1, h[0], K15.beyond_jordan(W1, h[0]), cap(v("32:33"), "left: 12px; top: 12px", size=11.5, maxw=190) + vref("NUM 32:33", "left: 12px; bottom: 12px"))
    r2 = new(SKY, W1, h[1], K15.gilead("y6b", W1, h[1], 1562, folds=True), cap(sp("32:34-42"), "left: 12px; top: 12px", size=11, maxw=600) + vref("NUM 32:34–42", "right: 12px; bottom: 12px"))
    return page("Numbers 32:33–42 — Fortified Cities, and Folds for Sheep", t, r1 + r2, n)


@P("NUM-C15-P07-Rameses", "These Are the Journeys")
def p07(n):
    cells = [st("33:5", "SUCCOTH"), st("33:6", "ETHAM"), st("33:7", "PI-HAHIROTH"), st("33:8", "MARAH"), st("33:9", "ELIM"), st("33:10", "BY THE RED SEA")]
    over = mk.stamp(33, "right: 14px; bottom: 12px") + cap(sp("33:1-4"), "left: 12px; top: 30px", size=11, maxw=300)
    return stages(n, "33:1–10", "These Are the Journeys", (0, 6), cells, top=380, extra_top=over)


@P("NUM-C15-P08-Sinai", "Unto the Wilderness of Sinai")
def p08(n):
    cells = [st("33:11", "WILDERNESS OF SIN"), st("33:12", "DOPHKAH"), st("33:13", "ALUSH"), st("33:14", "REPHIDIM"), st("33:15", "SINAI"),
             st("33:16", "KIBROTH-HATTAAVAH"), st("33:17", "HAZEROTH"), st("33:18", "RITHMAH"), st("33:19", "RIMMON-PEREZ")]
    return stages(n, "33:11–19", "Unto the Wilderness of Sinai", (6, 15), cells)


@P("NUM-C15-P09-Wanderings", "And They Journeyed")
def p09(n):
    refs = [(f"33:{k}", NAMES[k - 4]) for k in range(20, 36)]
    cells = [st(r, nm) for r, nm in refs]
    return stages(n, "33:20–35", "And They Journeyed", (15, 31), cells, ncol=4, top=280)


@P("NUM-C15-P10-Hor", "Aaron the Priest Went Up into Mount Hor")
def p10(n):
    cells = [st("33:36", "KADESH"), st("33:37", "MOUNT HOR"),
             st("33:38", "AARON", accent="#8FB8E8", text=v("33:38") + " " + v("33:39")),
             st("33:40", "ARAD", accent="#D7261E"), st("33:41", "ZALMONAH"), st("33:42", "PUNON")]
    return stages(n, "33:36–42", "Aaron the Priest Went Up into Mount Hor", (31, 35), cells, ncol=2, top=320)


@P("NUM-C15-P11-Moab", "In the Plains of Moab")
def p11(n):
    cells = [st("33:43", "OBOTH"), st("33:44", "IYE-ABARIM"), st("33:45", "DIBON-GAD"), st("33:46", "ALMON-DIBLATHAIM"),
             st("33:47", "THE MOUNTAINS OF ABARIM"), st("33:48", "THE PLAINS OF MOAB"), st("33:49", "BY THE JORDAN")]
    return stages(n, "33:43–49", "In the Plains of Moab", (35, 41), cells, ncol=2, top=320)


@P("NUM-C15-P12-Pricks", "As Pricks in Your Eyes")
def p12(n):
    t, h = rows(None, 260)
    r1 = night(h[0], cap(v("33:50"), "left: 12px; top: 12px", size=11.5, maxw=560) + god(sp("33:51-56"), "left: 12px; top: 64px", size=19, maxw=660) + vref("NUM 33:50–56", "right: 12px; bottom: 12px"))
    r2 = new(DUSK, W1, h[1], K.wilderness_camp("y12b", W1, h[1], 15122, dusk=True, sinai=False),
             vref("NUM 33:50", "left: 12px; bottom: 12px") + end_mark("NEXT · THE BORDERS OF THE LAND", "right: 10px; bottom: 10px"))
    return page("Numbers 33:50–56 — As Pricks in Your Eyes", t, r1 + r2, n)
