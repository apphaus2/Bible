"""Ezekiel volume, Chapter 17 — The Holy Oblation (Ezekiel 45–46). Every verse, word for word from ref/eng-asv.
The holy oblation of the land as a plan (the Levites' portion, the priests' with the sanctuary in the midst, the possession
of the city, and the prince's portion on either side reaching to the borders, shown on the map of the land); let it
suffice you, O princes; just balances, a just ephah and a just bath, the shekel and the maneh (a chart); the oblation of
wheat, barley, oil and one lamb out of two hundred (a chart); the appointed days of the first month and the seventh (a
calendar); the passover (the prince leading the bullock, the people with unleavened cakes); the gate of the inner court
opened on the sabbath and the new moon, the prince at its post and the people bowing at its door; the prince's offerings
(a chart: six lambs and a ram, a young bullock); in by the north gate and out by the south (the plan with the two ways);
the daily lamb morning by morning; the prince's gifts and the year of liberty (a diagram); the place where the priests
boil and bake, and the four courts in the corners with the boiling-places under their walls. No slaughter is drawn: the
beasts are led whole. Jehovah's words in the Voice box; the man's words in speech; Ezekiel's narration in captions."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from ezk import G, art17 as K
from ezk.common import title_art, fz, dz, paged, plate, EZEKIEL, EZEKIEL_AWE, EZEKIEL_FIRE, EZEKIEL_STERN, AMBER, GOLDEN, RED
from ezk import ch16 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
BP = "#0B1A2E"
OV = {"46:19": "c", "46:20": (("c", None), ("s", "This is the place")), "46:21": "c", "46:22": "c", "46:23": "c",
      "46:24": (("c", None), ("s", "These are the boiling-houses"))}


@P("EZK-C17-00-Title", "Chapter 17 · The Holy Oblation", title=True)
def title(n):
    svg = title_art(lambda w, h: K.oblation_plan(w, h, hi=("priests", "sanctuary")), BP)
    return chapter_title(17, "第十七話", "The Holy Oblation", "Ezekiel 45 – 46", svg, BP, v("45:1", frm="ye shall offer an oblation", to="a holy portion of the land;"), "Ezekiel · Volume Twenty-Six")


def D(refs, fn, bg=BP, room=280, **k):
    """Verses over a drawing, the drawing given `room` px under the words (room=None: the panel takes what is left)."""
    s = dz(refs, fn, bg, ov=OV, **k)
    return plate(s, room) if room else s
def F(refs, tok=EZEKIEL, bg=GOLDEN, **k): return fz(refs, tok, bg, ov=OV, **k)


GROUPS = [
    [D("45:1-3", lambda w, h: K.oblation_plan(w, h, hi=("priests", "sanctuary")), BP, 330, head="The Holy Oblation", stamp=45),
     F("45:4-6", EZEKIEL_AWE, AMBER)],
    [D("45:7-8", lambda w, h: K.land_map(w, h, hi=("PRINCE",), title="THE PRINCE'S PORTION · FROM THE WEST BORDER UNTO THE EAST"), BP, 330, head="Whatsoever Is for the Prince"),
     F("45:9", EZEKIEL_STERN, RED)],
    [D("45:10-12", lambda w, h: K.measures_plate(w, h), BP, 270, head="Just Balances"),
     D("45:13-15", lambda w, h: K.portions_plate(w, h), BP, None, head="The Oblation That Ye Shall Offer")],
    [F("45:16-17"),
     D("45:18-20", lambda w, h: K.feasts_plate(w, h, hi=("I1", "I7")), BP, None, head="In the First Month")],
    [D("45:21-22", lambda w, h: K.passover("pv17", w, h, 1701), "#2A2A5A", 330, head="The Passover"),
     F("45:23-25", EZEKIEL_AWE, AMBER)],
    [D("46:1-3", lambda w, h: K.open_gate("og17", w, h, 1702), "#3A4A7A", 320, head="On the Sabbath It Shall Be Opened", stamp=46),
     D("46:4-5", lambda w, h: K.offerings_plate(w, h, hi=("SABBATH",)), BP, None)],
    [D("46:6-7", lambda w, h: K.offerings_plate(w, h, hi=("NEW MOON",)), BP, 280),
     D("46:8-10", lambda w, h: K.flow_plan(w, h), BP, None, head="In the Appointed Feasts")],
    [F("46:11-12"),
     D("46:13-15", lambda w, h: K.morning_altar("ma17", w, h, 1703), "#3A3A6A", None, head="Morning by Morning")],
    [D("46:16-18", lambda w, h: K.inheritance_plate(w, h), BP, 250, head="The Prince's Inheritance"),
     D("46:19-20", lambda w, h: K.vision_plan(w, h, hi=("boiling", "priests_chambers"), zoom=True), BP, None, head="Where the Priests Shall Boil")],
    [D("46:21-23", lambda w, h: K.kitchens_plate(w, h), BP, 300, head="In Every Corner of the Court"),
     D("46:24", lambda w, h: K.boiling_houses("bh17", w, h, 1704), "#4A5A8A", None)],
]
PG.extend(paged(GROUPS, "EZK-C17-D", PG.next(), end=end_mark("NEXT · JEHOVAH IS THERE", "right: 10px; bottom: 34px")))
