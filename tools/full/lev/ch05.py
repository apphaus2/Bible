"""Leviticus volume, Chapter 5 — The Cleansing (Leviticus 14–15). Every verse, word for word from ref/asv.
All law cells: the cleansing of the leper, the plague in a house, and issues (lev/art5.py)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import chapter_title, end_mark
from exo import art8 as B8
from exo.kit import law_pages, set_book
from lev import G, art5 as K
from lev import ch04 as _prev

v, sp = G.v, G.span
set_book(G)
START = _prev.START + len(_prev.PAGES) - 1     # straight after the previous chapter (its title page is unnumbered)
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco
SAY = "And Jehovah spake unto Moses, saying,"


@P("LEV-C05-00-Title", "Chapter 5 · The Cleansing")
def title():
    svg = B8.bp(760, 1080) + f'<g transform="translate(0 420) scale(2.375)">{K.pg_let_go("t5")}</g>'
    return chapter_title(5, "第五話", "The Cleansing", "Leviticus 14 – 15", svg, B8.INK, v("14:7", frm="and shall let go"), "Leviticus · Volume Three")


LAWS = [
    ("IN THE DAY OF HIS CLEANSING", "14:1-3", K.pg_out_camp, SAY, "The Law of the Leper"),
    ("TWO LIVING CLEAN BIRDS", "14:4", K.pg_two_birds, "", None),
    ("OVER RUNNING WATER", "14:5-6", K.pg_vessel, "", None),
    ("THE LIVING BIRD LET GO", "14:7", K.pg_let_go, "", None),
    ("SHAVE OFF ALL HIS HAIR", "14:8", K.pg_shave, "", None),
    ("THE SEVENTH DAY", "14:9", K.pg_seventh, "", None),
    ("THE EIGHTH DAY", "14:10-11", K.pg_eighth_lambs, "", "The Eighth Day"),
    ("A TRESPASS-OFFERING", "14:12-13", K.pg_before, "", None),
    ("EAR, THUMB AND TOE", "14:14", K.pg_marks_oil, "", None),
    ("THE OIL IN HIS LEFT HAND", "14:15-17", K.pg_palm, "", None),
    ("UPON HIS HEAD", "14:18-20", K.pg_head_oil, "", None),
    ("IF HE BE POOR", "14:21-23", K.pg_poor_lamb, "", "If He Be Poor"),
    ("THE LAMB AND THE LOG OF OIL", "14:24-25", K.pg_marks_oil, "", None),
    ("SEVEN TIMES", "14:26-29", K.pg_palm, "", None),
    ("SUCH AS HE IS ABLE TO GET", "14:30-32", K.pg_atone, "", None),
    ("THE PLAGUE IN A HOUSE", "14:33-35", K.pg_canaan, "And Jehovah spake unto Moses and unto Aaron, saying,", "The Plague in a House"),
    ("EMPTY THE HOUSE", "14:36", K.pg_empty, "", None),
    ("HOLLOW STRAKES", "14:37-38", K.pg_strakes, "", None),
    ("TAKE OUT THE STONES", "14:39-40", K.pg_stones_out, "", None),
    ("SCRAPED WITHIN", "14:41-42", K.pg_scraped, "", None),
    ("A FRETTING LEPROSY", "14:43-45", K.pg_fretting, "", None),
    ("WHILE IT IS SHUT UP", "14:46-47", K.pg_in_house, "", None),
    ("THE HOUSE IS CLEAN", "14:48", K.pg_house_clean, "", None),
    ("TO CLEANSE THE HOUSE", "14:49-52", K.pg_house_birds, "", None),
    ("INTO THE OPEN FIELD", "14:53", K.pg_field_bird, "", None),
    ("THE LAW OF LEPROSY", "14:54-57", K.pg_law_all, "", None),
    ("AN ISSUE OUT OF HIS FLESH", "15:1-4", K.pg_issue, "And Jehovah spake unto Moses and to Aaron, saying,", "When Any Man Hath an Issue"),
    ("WHOSOEVER TOUCHETH HIS BED", "15:5-7", K.pg_wash_bathe, "", None),
    ("IF HE SPIT", "15:8-10", K.pg_saddle, "", None),
    ("WITHOUT HAVING RINSED HIS HANDS", "15:11-12", K.pg_rinse, "", None),
    ("SEVEN DAYS FOR HIS CLEANSING", "15:13", K.pg_count7, "", None),
    ("ON THE EIGHTH DAY", "15:14-15", K.pg_eighth_doves, "", None),
    ("BATHE ALL HIS FLESH", "15:16-18", K.pg_bathe, "", None),
    ("IF A WOMAN HAVE AN ISSUE", "15:19-21", K.pg_woman_seven, "", "If a Woman Have an Issue"),
    ("ANYTHING THAT SHE SITTETH UPON", "15:22-24", K.pg_her_bed, "", None),
    ("MANY DAYS", "15:25-27", K.pg_many_days, "", None),
    ("IF SHE BE CLEANSED", "15:28-30", K.pg_eighth_doves, "", None),
    ("THAT THEY DIE NOT", "15:31", K.pg_separate, "", None),
    ("THE LAW OF HIM THAT HATH AN ISSUE", "15:32-33", K.pg_law_issue, "", None),
]
PAGES += law_pages(LAWS, "LEV-C05-L", START, "The Cleansing", end=end_mark("NEXT · THE DAY OF ATONEMENT", "right: 10px; top: 10px"))
