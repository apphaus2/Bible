"""Leviticus volume, Chapter 1 — The Offerings (Leviticus 1–5). Every verse, word for word from ref/eng-asv.
One story page (Jehovah calling out of the tent of meeting, the offerer at the altar), then the laws as law cells."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
import mk
from fx import new, vref, page, chapter_title, end_mark, cap, god
from exo import art8 as B8
from exo.kit import law_pages, set_book
from lev import G, art as L
from genesis.ch02 import rows, W1, NIGHT, SKY
from genesis.ch03 import SAND

v, sp = G.v, G.span
set_book(G)
START = 1
PAGES = []
def P(name, title):
    def deco(fn): PAGES.append((name, title, fn)); return fn
    return deco
SAY = "And Jehovah spake unto Moses, saying,"


@P("LEV-C01-00-Title", "Chapter 1 · The Offerings")
def title():
    svg = B8.bp(760, 1080) + f'<g transform="translate(0 440)">{L.altar_scene("t1", 760, 640, 101)}</g>'
    return chapter_title(1, "第一話", "The Offerings", "Leviticus 1 – 5", svg, B8.INK, v("1:9", frm="an offering made by fire,"), "Leviticus · Volume Three")


@P("LEV-C01-P01-Called", "1 · Jehovah Called unto Moses")
def p01():
    t, h = rows(500, None)
    r1 = new(SKY, W1, h[0], L.tent_call("c1a", W1, h[0], 111), cap(v("1:1"), "left: 12px; top: 12px", size=12, maxw=420)
             + god(v("1:2"), "right: 12px; top: 100px", size=18, maxw=340) + vref("LEV 1:1–2", "right: 12px; bottom: 12px"))
    r2 = new(SAND, W1, h[1], L.altar_scene("c1b", W1, h[1], 112), god(v("1:3") + " " + v("1:4"), "left: 12px; top: 12px", size=16, maxw=470) + vref("LEV 1:3–4", "right: 12px; bottom: 12px"))
    return page("Leviticus 1:1–4 — Jehovah Called unto Moses", t, r1 + r2, START + 0)


ITEMS = [
    ("THE BLOOD", "1:5", L.pg_sprinkle, "", "The Burnt-offering"),
    ("THE PIECES IN ORDER", "1:6-8", L.pg_fire, "", None),
    ("A SWEET SAVOR", "1:9", L.pg_burn, "", None),
    ("OF THE FLOCK", "1:10-11", L.pg_north, "", None),
    ("THE WHOLE ON THE ALTAR", "1:12-13", L.pg_burn, "", None),
    ("OF BIRDS", "1:14-15", L.pg_doves, "", None),
    ("THE PLACE OF THE ASHES", "1:16-17", L.pg_ashes, "", None),
    ("FINE FLOUR · OIL · FRANKINCENSE", "2:1-2", L.pg_meal, "", "The Meal-offering"),
    ("AARON'S AND HIS SONS'", "2:3", L.pg_portion, "", None),
    ("BAKEN IN THE OVEN", "2:4", L.pg_oven, "", None),
    ("THE BAKING-PAN · THE FRYING-PAN", "2:5-7", L.pg_pans, "", None),
    ("THE MEMORIAL", "2:8-10", L.pg_bring, "", None),
    ("NO LEAVEN, NOR ANY HONEY", "2:11-12", L.pg_leaven, "", None),
    ("THE SALT OF THE COVENANT", "2:13", L.pg_salt, "", None),
    ("THE FIRST-FRUITS", "2:14-16", L.pg_ears, "", None),
    ("OF THE HERD", "3:1-2", L.pg_peace_herd, "", "The Peace-offerings"),
    ("THE FAT", "3:3-5", L.pg_fat, "", None),
    ("A LAMB", "3:6-8", L.pg_lamb, "", None),
    ("THE FAT TAIL", "3:9-11", L.pg_fat, "", None),
    ("A GOAT", "3:12-14", L.pg_goat, "", None),
    ("ALL THE FAT IS JEHOVAH'S", "3:15-17", L.pg_no_blood, "", None),
    ("IF ANY ONE SIN UNWITTINGLY", "4:1-2", L.pg_unwitting, SAY, "The Sin-offering"),
    ("THE ANOINTED PRIEST", "4:3-4", L.pg_priest_sin, "", None),
    ("BEFORE THE VEIL", "4:5-7", L.pg_veil, "", None),
    ("THE FAT OF THE BULLOCK", "4:8-10", L.pg_fat, "", None),
    ("WITHOUT THE CAMP", "4:11-12", L.pg_without, "", None),
    ("THE WHOLE CONGREGATION", "4:13-15", L.pg_congregation, "", "If the Whole Congregation Err"),
    ("SEVEN TIMES BEFORE THE VEIL", "4:16-18", L.pg_veil, "", None),
    ("THE SIN-OFFERING FOR THE ASSEMBLY", "4:19-21", L.pg_without, "", None),
    ("WHEN A RULER SINNETH", "4:22-24", L.pg_ruler, "", "When a Ruler Sinneth"),
    ("THE HORNS OF THE ALTAR", "4:25-26", L.pg_horns, "", None),
    ("ONE OF THE COMMON PEOPLE", "4:27-29", L.pg_common, "", None),
    ("ATONEMENT FOR HIM", "4:30-31", L.pg_horns, "", None),
    ("A LAMB, A FEMALE", "4:32-33", L.pg_she_lamb, "", None),
    ("HE SHALL BE FORGIVEN", "4:34-35", L.pg_horns, "", None),
    ("A WITNESS", "5:1", L.pg_witness, "", "The Trespass-offering"),
    ("ANY UNCLEAN THING", "5:2-3", L.pg_unclean, "", None),
    ("TO SWEAR RASHLY", "5:4", L.pg_oath, "", None),
    ("HE SHALL CONFESS", "5:5-6", L.pg_confess, "", None),
    ("TWO TURTLE-DOVES", "5:7-8", L.pg_two_doves, "", None),
    ("THE SECOND FOR A BURNT-OFFERING", "5:9-10", L.pg_doves, "", None),
    ("THE TENTH PART OF AN EPHAH", "5:11-13", L.pg_ephah, "", None),
    ("IN THE HOLY THINGS OF JEHOVAH", "5:14-15", L.pg_ram, SAY, "The Fifth Part"),
    ("THE FIFTH PART THERETO", "5:16", L.pg_fifth, "", None),
    ("THOUGH HE KNEW IT NOT", "5:17-19", L.pg_guilty, "", None),
]

PAGES += law_pages(ITEMS, "LEV-C01-L", START + 1, "The Offerings", end=end_mark("NEXT · THE CONSECRATION", "right: 10px; top: 10px"))
