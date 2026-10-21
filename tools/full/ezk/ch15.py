"""Ezekiel volume, Chapter 15 — The Measuring Reed (Ezekiel 40–42). Every verse, word for word from ref/asv.
In the visions of God upon a very high mountain, the frame of a city on the south; the man whose appearance was like brass,
with a line of flax and a measuring reed, standing in the gate (a bronze figure of light, no face drawn); and the house of
the vision measured as blueprint plates: the reed of six cubits and the wall; the east gate with its lodges and posts and
porch (a plan); the outer court, the pavement and its thirty chambers, the north and south gates and the gates of the inner
court (the plan of the whole, the part in hand lit gold); the eight tables of hewn stone; the chambers of the singers and
the priests; the inner court foursquare and the altar before the house; the porch; the temple and the most holy place; the
side-chambers in three stories; the building toward the west; the cherubim with two faces and the palm-trees; the altar of
wood — this is the table that is before Jehovah; the doors; the holy chambers of the priests; and the wall of five hundred
round about, to make a separation between that which was holy and that which was common. Ezekiel's narration in captions;
the man's words in speech boxes."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from ezk import G, art15 as K
from ezk.common import (title_art, pack, cp, say, gd, wl, fz, dz, run, drawn, face, label, FZ, FG, EZEKIEL, EZEKIEL_STERN, EZEKIEL_GRIEF, EZEKIEL_AWE,
                        AMBER, NIGHT, COLD, GOLDEN, RED)
from ezk import ch14 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
BP = "#0B1A2E"
VP = lambda *hi, **k: (BP, lambda w, h: K.vision_plan(w, h, hi=hi, **k), 470)
OV = {"40:4": (("c", None), ("s", "Son of man,")), "40:45": (("c", None), ("s", "This chamber")), "40:46": "s",
      "41:4": (("c", None), ("s", "This is the most holy place.")), "41:22": (("c", None), ("s", "This is the table")),
      "42:13": (("c", None), ("s", "The north chambers")), "42:14": "s"}
FA = [(EZEKIEL_AWE, AMBER), (EZEKIEL, GOLDEN)]


@P("EZK-C15-00-Title", "Chapter 15 · The Measuring Reed", title=True)
def title(n):
    svg = title_art(lambda w, h: K.vision_plan(w, h, hi=("house", "altar", "inner_court")), BP)
    return chapter_title(15, "第十五話", "The Measuring Reed", "Ezekiel 40 – 42", svg, BP, v("40:3", frm="behold, there was a man"), "Ezekiel · Volume Twenty-Six")


SEGS = run(40, 1, 49, arts={1: ("#1A2A5A", lambda w, h: K.high_mountain("hm15", w, h, 1501)), 3: ("#3A4A7A", lambda w, h: K.at_gate("ag15", w, h, 1502)),
                            5: (BP, lambda w, h: K.reed_plate(w, h)), 6: (BP, lambda w, h: K.gate_plan(w, h), 420), 11: (BP, lambda w, h: K.gate_plan(w, h), 420),
                            14: VP("east_gate"), 17: VP("pavement"), 20: VP("north_gate"), 23: VP("inner_north", "inner_east"), 24: VP("south_gate"),
                            28: VP("inner_south"), 30: (BP, lambda w, h: K.gate_plan(w, h, outer=False)), 32: VP("inner_east"), 35: VP("inner_north"),
                            38: (BP, lambda w, h: K.tables_plate(w, h)), 42: (BP, lambda w, h: K.tables_plate(w, h)), 44: VP("inner_north", "inner_south", "inner_east"),
                            46: VP("inner_court", "altar"), 47: VP("inner_court", "altar"), 48: (BP, lambda w, h: K.porch_plan(w, h))},
           faces=FA, kind="cap", ov=OV, budget=560,
           heads={1: "In the Visions of God", 3: "A Man like Brass", 5: "The Measuring Reed", 6: "The Gate toward the East", 17: "The Outer Court",
                  20: "The North Gate", 24: "The South Gate", 28: "The Inner Court", 38: "The Tables of Hewn Stone", 44: "The Chambers of the Priests",
                  47: "The Altar Before the House"})
SEGS += run(41, 1, 26, arts={1: (BP, lambda w, h: K.house_plan(w, h, hi=("temple",)), 430), 3: (BP, lambda w, h: K.house_plan(w, h, hi=("holy",))),
                             5: (BP, lambda w, h: K.house_plan(w, h, hi=("chambers",))), 7: (BP, lambda w, h: K.chambers_elev(w, h)), 9: (BP, lambda w, h: K.house_plan(w, h, hi=("chambers",))),
                             12: VP("building", "separate"), 13: VP("house", "separate", "building"), 16: (BP, lambda w, h: K.chambers_elev(w, h)),
                             18: (BP, lambda w, h: K.carvings(w, h)), 22: (BP, lambda w, h: K.wood_altar(w, h)), 23: (BP, lambda w, h: K.doors_elev(w, h))},
            faces=FA, kind="cap", ov=OV, budget=560,
            heads={1: "The Temple and the Most Holy Place", 5: "The Side-Chambers", 12: "The Building toward the West", 18: "Cherubim and Palm-Trees",
                   22: "The Table That Is before Jehovah"})
SEGS += run(42, 1, 20, arts={1: VP("priests_chambers"), 3: (BP, lambda w, h: K.chambers_elev(w, h)), 7: VP("priests_chambers", "pavement"),
                             10: VP("priests_chambers", "separate"), 13: VP("priests_chambers"), 14: VP("priests_chambers", "separate"), 15: VP("east_gate", "outer_wall", dims=True),
                             18: VP("outer_wall", dims=True)},
            faces=FA, kind="cap", ov=OV, budget=560,
            heads={1: "The Chambers toward the North", 13: "The Holy Chambers", 15: "Five Hundred Reeds"})
PG.extend(pack(SEGS, "EZK-C15-D", PG.next(), end=end_mark("NEXT · THE GLORY RETURNS", "right: 10px; bottom: 34px")))
