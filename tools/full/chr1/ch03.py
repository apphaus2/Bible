"""1 Chronicles volume, Chapter 3 — The Sons of Levi (1 Chronicles 5–6). Every verse, word for word from ref/asv.
Reuben, whose birthright was given to Joseph; Gad in Bashan; the war with the Hagrites as a map (5:22 words over the
cattle taken); the half-tribe of Manasseh, and the two tribes and a half carried away by Pul and Tilgath-pilneser; then the
sons of Levi: the high priests from Aaron to Jehozadak as one line; the singers David set over the service of song,
Heman, Asaph and Ethan; Aaron and his sons at the altars; and the cities of the Levites."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from chr1 import G, art as K
from chr1.common import pack, cp, say, caps, drawn, cell, cells, roll
from chr1 import ch02 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
TAG5, TAG6 = "THE GENERATIONS · 1 CHRONICLES 5", "THE SONS OF LEVI · 1 CHRONICLES 6"
PRIESTS = ["AARON", "ELEAZAR", "PHINEHAS", "ABISHUA", "BUKKI", "UZZI", "ZERAHIAH", "MERAIOTH", "AMARIAH", "AHITUB", "ZADOK", "AHIMAAZ",
           "AZARIAH", "JOHANAN", "AZARIAH", "AMARIAH", "AHITUB", "ZADOK", "SHALLUM", "HILKIAH", "AZARIAH", "SERAIAH", "JEHOZADAK"]


@P("1CH-C03-00-Title", "Chapter 3 · The Sons of Levi", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.singers("t3", 760, 780, 301, n=8, top=0.72)}</g><rect x="0" y="0" width="760" height="300" fill="#FFB04A"></rect>')
    return chapter_title(3, "第三話", "The Sons of Levi", "1 Chronicles 5 – 6", svg, "#C8702A", v("6:32", to="tent of meeting,"), "1 Chronicles · Volume Thirteen")


def chart(refs, fn, k=0.24, bg=MAP, **kw):
    a, _, b = refs.partition("-")
    return drawn([caps(refs)], f"1CHR {a}" + (f"–{b}" if b else ""), below(fn, k), bg, **kw)

R = (cells(5, 1, 6, "Reuben", "#FF8A6A", head="The Sons of Reuben", budget=600) + cells(5, 7, 10, "Reuben", "#FF8A6A", budget=600)
     + cells(5, 11, 17, "Gad", "#8FD0E2", budget=560))
PG.extend(roll(R, "1CH-C03-R", PG.next(), TAG5))
SEGS = [chart("5:18-20", lambda w, h: K.east_jordan(w, h, war=True), 0.36, head="The War with the Hagrites"),
        chart("5:21-22", lambda w, h: K.spoil("sp3", w, h, 302), 0.22, bg="#C8A878"),
        chart("5:23-24", lambda w, h: K.east_jordan(w, h, hi=("BASHAN", "HERMON")), 0.22, head="The Half-tribe of Manasseh"),
        chart("5:25-26", lambda w, h: K.K3.exile_map(w, h), 0.3)]
PG.extend(pack(SEGS, "1CH-C03-D", PG.next()))
SEGS2 = [chart("6:1-3", lambda w, h: K.branch(w, h, "LEVI", ["GERSHON", "KOHATH", "MERARI"], hi=("KOHATH",)), 0.3, head="The Sons of Levi", stamp=6),
         chart("6:4-15", lambda w, h: K.lineage(w, h, PRIESTS, hi=("AARON", "ZADOK", "JEHOZADAK"), per=6, top=0.3, bot=0.9), 0.3, h=520)]
PG.extend(pack(SEGS2, "1CH-C03-E", PG.next()))
R2 = (cells(6, 16, 21, "Gershom", "#8FD0E2", head="The Families of the Levites", budget=420) + cells(6, 22, 28, "Kohath", "#FFD23F", budget=480)
      + cells(6, 29, 30, "Merari", "#FF8A6A"))
PG.extend(roll(R2, "1CH-C03-S", PG.next(), TAG6))
HEMAN = ["HEMAN", "JOEL", "SAMUEL", "ELKANAH", "JEROHAM", "ELIEL", "TOAH", "ZUPH", "ELKANAH", "MAHATH", "AMASAI", "ELKANAH", "JOEL", "AZARIAH", "ZEPHANIAH",
         "TAHATH", "ASSIR", "EBIASAPH", "KORAH", "IZHAR", "KOHATH", "LEVI", "ISRAEL"]
ASAPH = ["ASAPH", "BERECHIAH", "SHIMEA", "MICHAEL", "BAASEIAH", "MALCHIJAH", "ETHNI", "ZERAH", "ADAIAH", "ETHAN", "ZIMMAH", "SHIMEI", "JAHATH", "GERSHOM", "LEVI"]
ETHAN = ["ETHAN", "KISHI", "ABDI", "MALLUCH", "HASHABIAH", "AMAZIAH", "HILKIAH", "AMZI", "BANI", "SHEMER", "MAHLI", "MUSHI", "MERARI", "LEVI"]
SEGS3 = [drawn([caps("6:31-32")], "1CHR 6:31–32", below(lambda w, h: K.singers("sg3", w, h, 303, top=0.5), 0.26), "#FFB04A", head="The Service of Song"),
         chart("6:33-38", lambda w, h: K.lineage(w, h, HEMAN, hi=("HEMAN", "SAMUEL", "LEVI"), per=6, top=0.3, bot=0.9), 0.3, h=440),
         chart("6:39-43", lambda w, h: K.lineage(w, h, ASAPH, hi=("ASAPH", "LEVI"), per=5, top=0.3, bot=0.9), 0.24, h=340),
         chart("6:44-47", lambda w, h: K.lineage(w, h, ETHAN, hi=("ETHAN", "LEVI"), per=5, top=0.3, bot=0.9), 0.24, h=340),
         drawn([caps("6:48-49")], "1CHR 6:48–49", below(lambda w, h: K.altar_service("as3", w, h, 304), 0.3), "#5A4A6A")]
PG.extend(pack(SEGS3, "1CH-C03-F", PG.next()))
R4 = ([cell("The Sons of Aaron", "6:50-53", "#FFD23F", head="Their Dwelling-places")]
      + cells(6, 54, 81, "The Cities of the Levites", "#8FD0E2", budget=560))
PG.extend(roll(R4, "1CH-C03-U", PG.next(), TAG6, end=end_mark("NEXT · THEY THAT DWELT IN JERUSALEM", "right: 40px; bottom: 50px")))
