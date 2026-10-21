"""Ezekiel volume, Chapter 15 — The Measuring Reed (Ezekiel 40–42). Every verse, word for word from ref/eng-asv.
In the visions of God upon a very high mountain, the frame of a city on the south; the man whose appearance was like brass,
with a line of flax and a measuring reed, standing in the gate (a figure of light with a bronze rim, no face drawn); and
the house of the vision measured as blueprint plates: the reed of six cubits and the wall; the east gate with its lodges
and posts and porch (a plan) and its posts, windows and palm-trees (an elevation); the outer court, the pavement and its
thirty chambers, the north and south gates and the gates of the inner court (the plan of the whole, drawn closer on the
part in hand, lit gold); the eight tables of hewn stone; the chambers of the singers and the priests; the inner court
foursquare and the altar before the house; the porch; the temple and the most holy place; the side-chambers in three
stories; the building toward the west; the cherubim with two faces and the palm-trees; the altar of wood — this is the
table that is before Jehovah; the doors; the holy chambers of the priests; and the wall of five hundred round about, to
make a separation between that which was holy and that which was common. Ezekiel's narration in captions; the man's words
in speech boxes. Pages laid out by hand (common.paged), two or three panels each, every plan with room under its words."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from ezk import G, art15 as K, art16 as K16
from ezk.common import title_art, fz, dz, paged, plate, EZEKIEL, EZEKIEL_AWE, EZEKIEL_FIRE, AMBER, GOLDEN, COLD, NIGHT
from ezk import ch14 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
BP = "#0B1A2E"
OV = {"40:4": (("c", None), ("s", "Son of man,")), "40:45": (("c", None), ("s", "This chamber")), "40:46": "s",
      "41:4": (("c", None), ("s", "This is the most holy place.")), "41:22": (("c", None), ("s", "This is the table")),
      "42:13": (("c", None), ("s", "The north chambers")), "42:14": "s"}


@P("EZK-C15-00-Title", "Chapter 15 · The Measuring Reed", title=True)
def title(n):
    svg = title_art(lambda w, h: K.vision_plan(w, h, hi=("house", "altar", "inner_court")), BP)
    return chapter_title(15, "第十五話", "The Measuring Reed", "Ezekiel 40 – 42", svg, BP, v("40:3", frm="behold, there was a man"), "Ezekiel · Volume Twenty-Six")


def D(refs, fn, room=300, bg=BP, **k):
    """Narration over a drawing (a plan when bg is the blueprint), the drawing given `room` px under the words."""
    s = dz(refs, fn, bg, kind="cap", ov=OV, **k)
    return plate(s, room) if room else s
def VP(refs, *hi, room=300, **k):
    return D(refs, lambda w, h: K.vision_plan(w, h, hi=hi), room, **k)
def F(refs, tok=EZEKIEL, bg=GOLDEN, **k): return fz(refs, tok, bg, kind="cap", ov=OV, **k)


GROUPS = [
    [D("40:1-2", lambda w, h: K.high_mountain("hm15", w, h, 1501), 330, "#1A2A5A", head="In the Visions of God", stamp=40),
     D("40:3-4", lambda w, h: K.at_gate("ag15", w, h, 1502), None, "#3A4A7A", head="A Man like Brass")],
    [D("40:5", lambda w, h: K.reed_plate(w, h), 200, head="The Measuring Reed"),
     D("40:6-8", lambda w, h: K.gate_plan(w, h), 280, head="The Gate toward the East"),
     F("40:9-10", EZEKIEL_AWE, AMBER)],
    [F("40:11-13"),
     D("40:14-16", lambda w, h: K.gate_elev(w, h), None)],
    [VP("40:17-19", "pavement", head="The Outer Court"),
     VP("40:20-22", "north_gate", head="The North Gate")],
    [VP("40:23-25", "inner_north", "inner_east", "south_gate", room=230, head="The South Gate"),
     F("40:26-27", EZEKIEL_AWE, AMBER),
     VP("40:28-29", "inner_south", room=220, head="The Inner Court")],
    [D("40:30-31", lambda w, h: K.gate_plan(w, h, outer=False), 230),
     VP("40:32-34", "inner_east", room=220),
     F("40:35-37")],
    [D("40:38-40", lambda w, h: K.tables_plate(w, h), 320, head="The Tables of Hewn Stone"),
     F("40:41-43", EZEKIEL_AWE, AMBER)],
    [VP("40:44-46", "inner_north", "inner_south", "inner_east", head="The Chambers of the Priests"),
     D("40:47-49", lambda w, h: K.porch_plan(w, h), None, head="The Porch of the House")],
    [D("41:1-2", lambda w, h: K.house_plan(w, h, hi=("temple",)), 280, head="The Temple and the Most Holy Place", stamp=41),
     F("41:3-4", EZEKIEL_AWE, AMBER)],
    [D("41:5-6", lambda w, h: K.house_plan(w, h, hi=("chambers",)), 300, head="The Side-Chambers"),
     D("41:7-8", lambda w, h: K.chambers_elev(w, h), None)],
    [F("41:9-11"),
     VP("41:12-14", "building", "separate", room=None, head="The Building toward the West")],
    [F("41:15-17", EZEKIEL_AWE, AMBER),
     D("41:18-20", lambda w, h: K.carvings(w, h), None, head="Cherubim and Palm-Trees")],
    [D("41:21-22", lambda w, h: K.wood_altar(w, h), 280, head="The Table That Is before Jehovah"),
     D("41:23-26", lambda w, h: K.doors_elev(w, h), None)],
    [VP("42:1-2", "priests_chambers", room=230, head="The Chambers toward the North", stamp=42),
     D("42:3-5", lambda w, h: K.chambers_elev(w, h), 220),
     F("42:6-9", EZEKIEL_AWE, AMBER)],
    [VP("42:10-12", "priests_chambers", "separate", room=280),
     D("42:13-14", lambda w, h: K16.linen_priests("lp15", w, h, 1503), None, "#6A8AB0", head="The Holy Chambers")],
    [D("42:15-16", lambda w, h: K.round_wall("rw15", w, h, 1504), 330, "#2A3A6A", head="Five Hundred Reeds"),
     D("42:17-20", lambda w, h: K.vision_plan(w, h, hi=("outer_wall",), dims=True), None)],
]
PG.extend(paged(GROUPS, "EZK-C15-D", PG.next(), end=end_mark("NEXT · THE GLORY RETURNS", "right: 10px; bottom: 34px")))
