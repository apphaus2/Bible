"""1 Chronicles volume, Chapter 4 — They That Dwelt in Jerusalem (1 Chronicles 7–9). Every verse, word for word from ref/asv.
Issachar, Benjamin, Naphtali and Manasseh; Ephraim mourning his sons slain by the men of Gath (7:21 words only), Beriah, and
Sheerah who built Beth-horon; the line from Ephraim to Joshua the son of Nun; the borders as a map; Asher; Benjamin and the
house of Saul; then all Israel reckoned by genealogies and Judah carried away; those who dwelt in Jerusalem — priests,
Levites, and the porters on the four sides of the house (a blueprint), opening it morning by morning; and the singers."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from faces_ex import F
from chr1 import G, art as K
from chr1.common import pack, cp, say, caps, drawn, face, cell, cells, roll, COLD
from chr1 import ch03 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
TAG7, TAG8, TAG9 = "THE GENERATIONS · 1 CHRONICLES 7", "THE SONS OF BENJAMIN · 1 CHRONICLES 8", "THEY THAT DWELT IN JERUSALEM · 1 CHRONICLES 9"
EPHRAIM = F("adam", skin="#B98A6E", shadow="#3A2A4A", hair="#C8C2B6", hl="#E8E2D6", beard=True, beard_color="#D8D2C6", scarf="#4A3A5A", brow="sorrow", tear=True, light="#9AA8C8")
SAUL_LINE = ["NER", "KISH", "SAUL", "JONATHAN", "MERIB-BAAL", "MICAH", "AHAZ", "JEHOADDAH", "ZIMRI", "MOZA", "BINEA", "RAPHAH", "ELEASAH", "AZEL"]


@P("1CH-C04-00-Title", "Chapter 4 · They That Dwelt in Jerusalem", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.porters_plan(760, 780)}</g><rect x="0" y="0" width="760" height="300" fill="#0B1A2E"></rect>')
    return chapter_title(4, "第四話", "They That Dwelt in Jerusalem", "1 Chronicles 7 – 9", svg, MAP, v("9:24"), "1 Chronicles · Volume Thirteen")


def chart(refs, fn, k=0.24, bg=MAP, **kw):
    a, _, b = refs.partition("-")
    return drawn([caps(refs)], f"1CHR {a}" + (f"–{b}" if b else ""), below(fn, k), bg, **kw)

R = (cells(7, 1, 5, "Issachar", "#8FD0E2", head="The Tribes", budget=640) + cells(7, 6, 12, "Benjamin", "#FFD23F", budget=600)
     + [cell("Naphtali", "7:13", "#FF8A6A")] + cells(7, 14, 19, "Manasseh", "#FFB04A", budget=600))
PG.extend(roll(R, "1CH-C04-R", PG.next(), TAG7))
SEGS = [drawn([caps("7:20-21")], "1CHR 7:20–21", below(lambda w, h: K.K3.gate_dawn(w, h, 401), 0.4), "#3A2A3A", head="Ephraim"),
        face([caps("7:22-23")], "1CHR 7:22–23", EPHRAIM, bg=COLD),
        chart("7:24", lambda w, h: K.beth_horon("bh4", w, h, 402), 0.16, bg="#8FD0E2"),
        chart("7:25-27", lambda w, h: K.lineage(w, h, ["EPHRAIM", "BERIAH", "REPHAH", "RESHEPH", "TELAH", "TAHAN", "LADAN", "AMMIHUD", "ELISHAMA", "NUN", "JOSHUA"],
                                                   hi=("JOSHUA",), per=6, top=0.34, bot=0.86), 0.18, h=300),
        chart("7:28-29", lambda w, h: K.ephraim_map(w, h, hi=("BETH-EL", "SHECHEM")), 0.3)]
PG.extend(pack(SEGS, "1CH-C04-D", PG.next()))
R2 = (cells(7, 30, 40, "Asher", "#8FD0E2", head="The Children of Asher", budget=600)
      + cells(8, 1, 28, "Benjamin", "#FFD23F", head="The Sons of Benjamin", budget=600) + [cell("In Gibeon", "8:29-32", "#FFB04A")])
PG.extend(roll(R2, "1CH-C04-S", PG.next(), TAG8))
SEGS2 = [chart("8:33-40", lambda w, h: K.lineage(w, h, SAUL_LINE, hi=("SAUL", "JONATHAN"), per=5, top=0.3, bot=0.88), 0.36, head="The House of Saul"),
         drawn([caps("9:1-2")], "1CHR 9:1–2", below(lambda w, h: K.K3.captives("cp4", w, h, 403, city="jerusalem"), 0.24), "#5A4A5A", stamp=9)]
PG.extend(pack(SEGS2, "1CH-C04-E", PG.next()))
R3 = (cells(9, 3, 9, "Judah, Benjamin, Ephraim and Manasseh", "#FFD23F", head="They That Dwelt in Jerusalem", budget=620)
      + cells(9, 10, 13, "The Priests", "#F3EFE6", budget=620) + cells(9, 14, 16, "The Levites", "#8FD0E2", budget=620))
PG.extend(roll(R3, "1CH-C04-T", PG.next(), TAG9))
SEGS3 = [drawn([caps("9:17-21")], "1CHR 9:17–21", below(lambda w, h: K.opening("op4", w, h, 404), 0.4), "#5A4A7A", head="The Porters"),
         chart("9:22-24", lambda w, h: K.porters_plan(w, h), 0.24),
         drawn([caps("9:25-27")], "1CHR 9:25–27", below(lambda w, h: K.opening("op4b", w, h, 405), 0.3), "#5A4A7A"),
         chart("9:28-32", lambda w, h: K.gold_vessels(w, h), 0.36, head="The Vessels of Service"),
         drawn([caps("9:33-34")], "1CHR 9:33–34", below(lambda w, h: K.night_song("ns4", w, h, 406), 0.22), "#0B0B2A")]
PG.extend(pack(SEGS3, "1CH-C04-F", PG.next()))
R4 = cells(9, 35, 44, "In Gibeon", "#FFB04A", head="The House of Saul", budget=520)
PG.extend(roll(R4, "1CH-C04-U", PG.next(), TAG9, end=end_mark("NEXT · DAVID KING OVER ISRAEL", "right: 40px; bottom: 50px")))
