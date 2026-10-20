"""1 Chronicles volume, Chapter 9 — The Courses (1 Chronicles 23–25). Every verse, word for word from ref/eng-asv.
David old and full of days makes Solomon king; the Levites numbered from thirty years old (a tally board) and divided into
courses by the sons of Levi; their office — to stand every morning to thank and praise Jehovah, and likewise at even; the
sons of Aaron, Eleazar and Ithamar, divided by lot, and the four and twenty courses of the priests as a board of lots; the
rest of the sons of Levi; then the sons of Asaph, Heman and Jeduthun set apart to prophesy with harps, and the four and
twenty lots of the singers, twelve to each."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from chr1 import G, art as K
from chr1.common import pack, cp, say, caps, drawn, face, cells, roll, DAVID_OLD
from chr1 import ch08 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, BOARD = "#0B1A2E", "#1A1430"
TAG23, TAG24 = "THE COURSES OF THE LEVITES · 1 CHRONICLES 23", "THE REST OF THE SONS OF LEVI · 1 CHRONICLES 24"
PRIESTS = ["JEHOIARIB", "JEDAIAH", "HARIM", "SEORIM", "MALCHIJAH", "MIJAMIN", "HAKKOZ", "ABIJAH", "JESHUA", "SHECANIAH", "ELIASHIB", "JAKIM",
           "HUPPAH", "JESHEBEAB", "BILGAH", "IMMER", "HEZIR", "HAPPIZZEZ", "PETHAHIAH", "JEHEZKEL", "JACHIN", "GAMUL", "DELAIAH", "MAAZIAH"]
SINGERS = ["JOSEPH", "GEDALIAH", "ZACCUR", "IZRI", "NETHANIAH", "BUKKIAH", "JESHARELAH", "JESHAIAH", "MATTANIAH", "SHIMEI", "AZAREL", "HASHABIAH",
           "SHUBAEL", "MATTITHIAH", "JEREMOTH", "HANANIAH", "JOSHBEKASHAH", "HANANI", "MALLOTHI", "ELIATHAH", "HOTHIR", "GIDDALTI", "MAHAZIOTH", "ROMAMTIEZER"]
HEMAN = ["BUKKIAH", "MATTANIAH", "UZZIEL", "SHEBUEL", "JERIMOTH", "HANANIAH", "HANANI", "ELIATHAH", "GIDDALTI", "ROMAMTI-EZER", "JOSHBEKASHAH", "MALLOTHI", "HOTHIR", "MAHAZIOTH"]


@P("1CH-C09-00-Title", "Chapter 9 · The Courses", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#1A1430"></rect><g transform="translate(0 350)">{K.lot_grid(760, 370, PRIESTS, cols=8, top=0.04)}</g>')
    return chapter_title(9, "第九話", "The Courses", "1 Chronicles 23 – 25", svg, BOARD, v("24:7", to="the second to Jedaiah,"), "1 Chronicles · Volume Thirteen")


def chart(refs, fn, k=0.24, bg=MAP, **kw):
    a, _, b = refs.partition("-")
    return drawn([caps(refs)], f"1CHR {a}" + (f"–{b}" if b else ""), below(fn, k), bg, **kw)

SEGS = [drawn([caps("23:1-2")], "1CHR 23:1–2", below(lambda w, h: K.charge_son("cs9", w, h, 901, princes=True), 0.2), "#8A4A26", head="David Was Old and Full of Days", stamp=23),
        chart("23:3-5", lambda w, h: K.tally(w, h, [("THE WORK", "24,000", "#FFD23F"), ("OFFICERS", "6,000", "#8FD0E2"), ("DOORKEEPERS", "4,000", "#FF8A6A"),
                                                    ("PRAISE", "4,000", "#9CCB5E")], "THIRTY AND EIGHT THOUSAND"), 0.3, bg=BOARD),
        chart("23:6", lambda w, h: K.branch(w, h, "LEVI", ["GERSHON", "KOHATH", "MERARI"]), 0.2, h=300)]
PG.extend(pack(SEGS, "1CH-C09-D", PG.next()))
R = (cells(23, 7, 11, "The Gershonites", "#8FD0E2", head="The Courses of the Levites", budget=520) + cells(23, 12, 20, "Kohath", "#FFD23F", budget=520)
     + cells(23, 21, 23, "Merari", "#FF8A6A", budget=520) + cells(23, 24, 27, "The Sons of Levi", "#FFD23F", head="Their Office", budget=640)
     + cells(23, 28, 32, "Their Office", "#FFD23F", budget=520))
PG.extend(roll(R, "1CH-C09-R", PG.next(), TAG23))
SEGS3 = [chart("24:1-3", lambda w, h: K.branch(w, h, "AARON", ["NADAB", "ABIHU", "ELEAZAR", "ITHAMAR"], hi=("ELEAZAR", "ITHAMAR")), 0.3, head="The Courses of the Sons of Aaron", stamp=24),
         chart("24:4-6", lambda w, h: K.lot_grid(w, h, ["ELEAZAR"] * 16 + ["ITHAMAR"] * 8, cols=8, color="#8FD0E2", top=0.08), 0.42, bg=BOARD)]
PG.extend(pack(SEGS3, "1CH-C09-F", PG.next()))
SEGS4 = [chart("24:7-19", lambda w, h: K.lot_grid(w, h, PRIESTS, cols=6), 0.3, bg=BOARD, head="The Four and Twenty Lots")]
PG.extend(pack(SEGS4, "1CH-C09-G", PG.next()))
R2 = cells(24, 20, 31, "The Rest of the Sons of Levi", "#8FD0E2", head="The Rest of the Sons of Levi", budget=440)
PG.extend(roll(R2, "1CH-C09-S", PG.next(), TAG24))
SEGS5 = [drawn([caps("25:1-3")], "1CHR 25:1–3", below(lambda w, h: K.singers("sg9", w, h, 904, n=7, top=0.56), 0.4), "#FFB04A", head="To Prophesy with Harps", stamp=25),
         chart("25:4-7", lambda w, h: K.branch(w, h, "HEMAN", HEMAN, per=5), 0.36)]
PG.extend(pack(SEGS5, "1CH-C09-H", PG.next()))
SEGS6 = [chart("25:8-19", lambda w, h: K.lot_grid(w, h, SINGERS, lit=set(range(12)), cols=6), 0.36, bg=BOARD, head="The Lots of the Singers"),
         chart("25:20-31", lambda w, h: K.lot_grid(w, h, SINGERS, lit=set(range(12, 24)), cols=6), 0.36, bg=BOARD)]
PG.extend(pack(SEGS6, "1CH-C09-J", PG.next(), end=end_mark("NEXT · THE PORTERS AND THE CAPTAINS", "right: 10px; bottom: 34px")))
