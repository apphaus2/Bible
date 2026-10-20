"""1 Chronicles volume, Chapter 1 — From Adam (1 Chronicles 1–2). Every verse, word for word from ref/eng-asv.
The generations as charts and roll cells: Adam to Noah; the sons of Japheth, Ham and Shem; Shem to Abram; Ishmael, Keturah,
Isaac; Esau and Seir; the kings and the chiefs of Edom; the sons of Israel; Judah, Perez and Zerah; Hezron, Ram and the line
to Jesse and his seven sons, David the seventh; Zeruiah and Abigail; and the houses of Caleb and Jerahmeel."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from chr1 import G, art as K
from chr1.common import pack, caps, drawn, cell, cells, roll

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
TAG = "THE GENERATIONS · 1 CHRONICLES 1"
TAG2 = "THE GENERATIONS · 1 CHRONICLES 2"
ADAM = ["ADAM", "SETH", "ENOSH", "KENAN", "MAHALALEL", "JARED", "ENOCH", "METHUSELAH", "LAMECH", "NOAH"]


@P("1CH-C01-00-Title", "Chapter 1 · From Adam", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.lineage(760, 780, ADAM + ["SHEM", "HAM", "JAPHETH"], hi=("ADAM", "NOAH"), per=4, top=0.17, bot=0.9)}</g>'
                f'<rect x="0" y="0" width="760" height="300" fill="#0B1A2E"></rect>')
    return chapter_title(1, "第一話", "From Adam", "1 Chronicles 1 – 2", svg, MAP, v("1:1"), "1 Chronicles · Volume Thirteen")


def chart(refs, fn, k=0.24, **kw):
    a, _, b = refs.partition("-")
    return drawn([caps(refs)], f"1CHR {a}" + (f"–{b}" if b else ""), below(fn, k), MAP, **kw)

def line(refs, names, hi=(), per=5, h=330, **kw):
    """A lineage chart panel of a fixed height, the words above it."""
    return chart(refs, lambda w, hh: K.lineage(w, hh, names, hi=hi, per=per, top=0.3, bot=0.86), 0.18, h=h, **kw)

SEGS = [line("1:1-4", ADAM + ["SHEM", "HAM", "JAPHETH"], hi=("ADAM", "NOAH"), h=360, head="From Adam", stamp=1),
        chart("1:5-7", lambda w, h: K.branch(w, h, "JAPHETH", ["GOMER", "MAGOG", "MADAI", "JAVAN", "TUBAL", "MESHECH", "TIRAS"])),
        chart("1:8-10", lambda w, h: K.branch(w, h, "HAM", ["CUSH", "MIZRAIM", "PUT", "CANAAN"], hi=("CUSH",)))]
PG.extend(pack(SEGS, "1CH-C01-D", PG.next()))
R = [cell("Mizraim", "1:11-12", "#FFB04A", head="The Sons of Noah"), cell("Canaan", "1:13-16", "#FFB04A"),
     cell("Shem", "1:17-19", "#8FD0E2"), cell("Joktan", "1:20-23", "#8FD0E2")]
PG.extend(roll(R, "1CH-C01-R", PG.next(), TAG))
SEGS2 = [line("1:24-27", ["SHEM", "ARPACHSHAD", "SHELAH", "EBER", "PELEG", "REU", "SERUG", "NAHOR", "TERAH", "ABRAM"], hi=("ABRAM",), head="Abram, the Same Is Abraham"),
         chart("1:28-31", lambda w, h: K.branch(w, h, "ISHMAEL", ["NEBAIOTH", "KEDAR", "ADBEEL", "MIBSAM", "MISHMA", "DUMAH", "MASSA", "HADAD", "TEMA", "JETUR", "NAPHISH", "KEDEMAH"], per=6), 0.3),
         chart("1:32-34", lambda w, h: K.branch(w, h, "ABRAHAM", ["ISAAC", "ISHMAEL", "ZIMRAN", "JOKSHAN", "MEDAN", "MIDIAN", "ISHBAK", "SHUAH"], hi=("ISAAC",), per=8), 0.4)]
PG.extend(pack(SEGS2, "1CH-C01-E", PG.next()))
R2 = ([cell("Esau", "1:35-37", "#FF8A6A", head="The Sons of Esau"), cell("Seir", "1:38-42", "#FF8A6A")]
      + cells(1, 43, 50, "The Kings of Edom", "#FFD23F", budget=420)
      + [cell("The Chiefs of Edom", "1:51-54", "#FFB04A")])
PG.extend(roll(R2, "1CH-C01-S", PG.next(), TAG))
SEGS3 = [chart("2:1-2", lambda w, h: K.branch(w, h, "ISRAEL", ["REUBEN", "SIMEON", "LEVI", "JUDAH", "ISSACHAR", "ZEBULUN", "DAN", "JOSEPH", "BENJAMIN", "NAPHTALI", "GAD", "ASHER"],
                                                hi=("JUDAH",), per=6), 0.14, head="The Sons of Israel", stamp=2),
         chart("2:3-8", lambda w, h: K.branch(w, h, "JUDAH", ["ER", "ONAN", "SHELAH", "PEREZ", "ZERAH"], hi=("PEREZ",)), 0.36)]
PG.extend(pack(SEGS3, "1CH-C01-F", PG.next()))
SEGS4 = [line("2:9-12", ["HEZRON", "RAM", "AMMINADAB", "NAHSHON", "SALMA", "BOAZ", "OBED", "JESSE"], hi=("NAHSHON", "BOAZ", "JESSE"), per=4, h=380, head="David the Seventh"),
         chart("2:13-17", lambda w, h: K.branch(w, h, "JESSE", ["ELIAB", "ABINADAB", "SHIMEA", "NETHANEL", "RADDAI", "OZEM", "DAVID"], hi=("DAVID",)), 0.3)]
PG.extend(pack(SEGS4, "1CH-C01-G", PG.next()))
R4 = ([cell("Caleb the Son of Hezron", "2:18-20", "#8FD0E2", head="The Sons of Hezron"), cell("Hezron and the Daughter of Machir", "2:21-23", "#8FD0E2"), cell("Ashhur", "2:24", "#8FD0E2")]
      + cells(2, 25, 41, "Jerahmeel", "#FF8A6A", head="The Sons of Jerahmeel", budget=480)
      + cells(2, 42, 55, "Caleb", "#FFB04A", head="The Sons of Caleb", budget=520))
PG.extend(roll(R4, "1CH-C01-U", PG.next(), TAG2, end=end_mark("NEXT · THE SONS OF DAVID", "right: 40px; bottom: 50px")))
