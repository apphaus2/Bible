"""1 Chronicles volume, Chapter 10 — The Porters and the Captains (1 Chronicles 26–27). Every verse, word for word from ref/eng-asv.
The courses of the doorkeepers, Meshelemiah, Obed-edom (for God blessed him) and Hosah; the lots for every gate as a plan
of the four sides, with the watches set; the treasures of the house and of the dedicated things, the officers and judges;
then the twelve courses of the captains, a course for every month of twenty and four thousand (a calendar wheel); the
princes of the tribes; the numbering Joab finished not; the rulers of the king's substance; and David's counsellors."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from chr1 import G, art as K
from chr1.common import pack, caps, drawn, cell, cells, roll
from chr1 import ch09 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, BOARD = "#0B1A2E", "#1A1430"
TAG26, TAG27 = "THE COURSES OF THE DOORKEEPERS · 1 CHRONICLES 26", "THE CAPTAINS AND THE RULERS · 1 CHRONICLES 27"
CAPTAINS = ["JASHOBEAM", "DODAI", "BENAIAH", "ASAHEL", "SHAMHUTH", "IRA", "HELEZ", "SIBBECAI", "ABIEZER", "MAHARAI", "BENAIAH", "HELDAI"]


@P("1CH-C10-00-Title", "Chapter 10 · The Porters and the Captains", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#1A1430"></rect><g transform="translate(0 300)">{K.month_wheel(760, 440, CAPTAINS)}</g>')
    return chapter_title(10, "第十話", "The Porters and the Captains", "1 Chronicles 26 – 27", svg, BOARD, v("27:1", frm="month by month"), "1 Chronicles · Volume Thirteen")


def chart(refs, fn, k=0.24, bg=MAP, **kw):
    a, _, b = refs.partition("-")
    return drawn([caps(refs)], f"1CHR {a}" + (f"–{b}" if b else ""), below(fn, k), bg, **kw)

R = (cells(26, 1, 3, "Meshelemiah", "#FFD23F", head="The Courses of the Doorkeepers", budget=520) + cells(26, 4, 9, "Obed-edom", "#8FD0E2", budget=600)
     + cells(26, 10, 11, "Hosah", "#FF8A6A", budget=520))
PG.extend(roll(R, "1CH-C10-R", PG.next(), TAG26))
GATES = {"EAST": "SHELEMIAH", "NORTH": "ZECHARIAH", "SOUTH": "OBED-EDOM|AND THE STORE-HOUSE", "WEST": "SHUPPIM AND HOSAH|SHALLECHETH"}
WATCH = {"EAST": "SIX LEVITES", "NORTH": "FOUR A DAY", "SOUTH": "FOUR A DAY|STORE-HOUSE TWO AND TWO", "WEST": "FOUR AT THE CAUSEWAY|TWO AT PARBAR"}
SEGS = [chart("26:12-16", lambda w, h: K.porters_plan(w, h, names=GATES), 0.24, head="For Every Gate", stamp=26),
        chart("26:17-19", lambda w, h: K.porters_plan(w, h, names=WATCH), 0.16)]
PG.extend(pack(SEGS, "1CH-C10-D", PG.next()))
R2 = (cells(26, 20, 25, "Over the Treasures", "#FFD23F", head="Over the Treasures", budget=560) + cells(26, 26, 28, "The Dedicated Things", "#FFD23F", budget=640)
      + cells(26, 29, 32, "Officers and Judges", "#8FD0E2", head="The Outward Business", budget=560))
PG.extend(roll(R2, "1CH-C10-S", PG.next(), TAG26))
SEGS2 = [chart("27:1", lambda w, h: K.month_wheel(w, h, CAPTAINS), 0.3, bg=BOARD, head="Month by Month", stamp=27),
         chart("27:2-8", lambda w, h: K.month_wheel(w, h, CAPTAINS, lit=set(range(6))), 0.5, bg=BOARD),
         chart("27:9-15", lambda w, h: K.month_wheel(w, h, CAPTAINS, lit=set(range(6, 12))), 0.5, bg=BOARD)]
PG.extend(pack(SEGS2, "1CH-C10-E", PG.next()))
R3 = (cells(27, 16, 22, "The Captains of the Tribes", "#8FD0E2", head="Over the Tribes of Israel", budget=420) + [cell("Like to the Stars of Heaven", "27:23-24", "#FF8A6A")]
      + cells(27, 25, 31, "The King's Substance", "#FFD23F", head="The Rulers of the Substance", budget=420) + [cell("The King's Counsellors", "27:32-34", "#FFB04A")])
PG.extend(roll(R3, "1CH-C10-T", PG.next(), TAG27, end=end_mark("NEXT · THINE IS THE KINGDOM", "right: 40px; bottom: 50px")))
