"""Ezra volume, Chapter 1 — The Decree of Cyrus (Ezra 1–2). Every verse, word for word from ref/asv.
The proclamation of Cyrus — whosoever there is among you of all his people, let him go up; the heads of fathers' houses and
all whose spirit God had stirred; the vessels of the house of Jehovah brought forth and numbered to Sheshbazzar (a tally
board); then the children of the province that went up out of the captivity, family by family, as roll cells; the priests
without their register; the whole assembly, their beasts, and the freewill-offerings for the house of God."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from ezr import G, art as K
from ezr.common import pack, cp, say, caps, says, drawn, face, joined, cell, cells, roll, CYRUS, COLD, GOLDEN

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
BOARD = "#1A1430"
TAG = "THE CHILDREN OF THE PROVINCE · EZRA 2"


@P("EZR-C01-00-Title", "Chapter 1 · The Decree of Cyrus", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.cyrus_decree("t1", 760, 820, 101)}</g><rect x="0" y="0" width="760" height="262" fill="#FFC890"></rect>')
    return chapter_title(1, "第一話", "The Decree of Cyrus", "Ezra 1 – 2", svg, "#C8702A", v("1:3", frm="and let him go up", to="which is in Judah,"), "Ezra · Volume Fifteen")


SEGS = [drawn([cp("1:1", to="saying,")], "EZRA 1:1", below(lambda w, h: K.cyrus_decree("cy1", w, h, 102), 0.3), "#FFC890", head="Let Him Go Up", stamp=1),
        face([say("1:2", to="Thus saith Cyrus king of Persia,"), say("1:2", frm="All the kingdoms"), says("1:3-4")], "EZRA 1:2–4", CYRUS),
        drawn([caps("1:5-6")], "EZRA 1:5–6", below(lambda w, h: K.return_caravan("rc1", w, h, 103), 0.3), "#FFC890"),
        drawn([caps("1:7-8")], "EZRA 1:7–8", below(lambda w, h: K.K2.vessels(w, h, 104), 0.3), "#2A1A3A", head="The Vessels of the House of Jehovah"),
        drawn([caps("1:9-11")], "EZRA 1:9–11", below(lambda w, h: K.tally(w, h, [("GOLD PLATTERS", "30", "#FFD23F"), ("SILVER", "1,000", "#C8C8D0"),
                                                                             ("GOLD BOWLS", "30", "#FFD23F"), ("ALL VESSELS", "5,400", "#8FD0E2")]), 0.4), BOARD),
        drawn([caps("2:1-2")], "EZRA 2:1–2", below(lambda w, h: K.return_caravan("rc1b", w, h, 105), 0.36), "#FFC890", stamp=2)]
PG.extend(pack(SEGS, "EZR-C01-D", PG.next(), most=2))
R = (cells(2, 3, 35, "The Men of the People of Israel", "#FFD23F", head="The Men of the People", budget=560)
     + cells(2, 36, 39, "The Priests", "#F3EFE6", head="The Priests and the Levites", budget=520) + cells(2, 40, 42, "The Levites", "#8FD0E2", budget=520)
     + cells(2, 43, 58, "The Nethinim", "#FF8A6A", head="The Nethinim", budget=560)
     + cells(2, 59, 63, "Who Could Not Show Their Fathers' Houses", "#C8C2D6", head="Not Found in the Register", budget=520))
PG.extend(roll(R, "EZR-C01-R", PG.next(), TAG))
SEGS3 = [drawn([caps("2:64-67")], "EZRA 2:64–67", below(lambda w, h: K.tally(w, h, [("ASSEMBLY", "42,360", "#FFD23F"), ("SERVANTS", "7,337", "#8FD0E2"),
                                                                                ("SINGERS", "200", "#9CCB5E"), ("HORSES", "736", "#FF8A6A"), ("CAMELS", "435", "#C8C2D6"),
                                                                                ("ASSES", "6,720", "#E8C88A")]), 0.4), BOARD, head="The Whole Assembly Together"),
         drawn([caps("2:68-70")], "EZRA 2:68–70", below(lambda w, h: K.return_caravan("rc1c", w, h, 106), 0.36), "#FFC890")]
PG.extend(pack(SEGS3, "EZR-C01-F", PG.next(), end=end_mark("NEXT · THE FOUNDATION OF THE HOUSE", "right: 10px; bottom: 34px")))
