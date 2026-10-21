"""Ezekiel volume, Chapter 16 — The Glory Returns (Ezekiel 43–44). Every verse, word for word from ref/eng-asv.
The glory of the God of Israel coming from the way of the east, his voice like the sound of many waters, the earth shining
(light over the eastern hills toward the gate, no figure); the glory entering by the east gate and filling the house, and
the man of light standing by Ezekiel in the inner court; one speaking out of the house — this is the place of my throne
(the empty throne of sapphire with only fire and amber light upon it, as in the first vision); the pattern of the house;
the law of the house and the altar measured by cubits (a blueprint plate) and its consecration seven days (the young
bullock, the he-goat and the ram led whole beside the altar, the fire upon the hearth; no slaughter drawn); the outer east
gate shut, for Jehovah hath entered in by it, and the prince eating bread in its porch; no foreigner in the sanctuary (the
gates on the plan); the Levites keeping the gates; the sons of Zadok in linen garments; judging in a controversy; and I am
their inheritance (the first-fruits before the house). Jehovah's words in the Voice box, Ezekiel's narration in captions.
Pages laid out by hand (common.paged)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from ezk import G, art16 as K, art as K0
from ezk.common import title_art, fz, dz, paged, plate, EZEKIEL, EZEKIEL_AWE, EZEKIEL_FIRE, EZEKIEL_STERN, AMBER, GOLDEN, RED
from ezk import ch15 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
BP = "#0B1A2E"
OV = {"43:1": "c", "43:2": "c", "43:3": "c", "43:4": "c", "43:5": "c", "43:6": "c", "44:1": "c", "44:4": "c"}


@P("EZK-C16-00-Title", "Chapter 16 · The Glory Returns", title=True)
def title(n):
    svg = title_art(lambda w, h: K.glory_east("t16", w, h, 1601), "#1A1A4A")
    return chapter_title(16, "第十六話", "The Glory Returns", "Ezekiel 43 – 44", svg, "#1A1A4A", v("43:2"), "Ezekiel · Volume Twenty-Six")


def D(refs, fn, bg, room=280, **k):
    """Verses over a drawing, the drawing given `room` px under the words (room=None: the panel takes what is left)."""
    s = dz(refs, fn, bg, ov=OV, **k)
    return plate(s, room) if room else s
def VP(refs, *hi, room=250, **k): return D(refs, lambda w, h: K.vision_plan(w, h, hi=hi), BP, room, **k)
def F(refs, tok=EZEKIEL, bg=GOLDEN, **k): return fz(refs, tok, bg, ov=OV, **k)


GROUPS = [
    [D("43:1-3", lambda w, h: K.glory_east("ge16", w, h, 1602), "#1A1A4A", 360, head="From the Way of the East", stamp=43),
     D("43:4-6", lambda w, h: K.filled_house("fh16", w, h, 1603), "#2A2A4A", None, head="The Glory of Jehovah Filled the House")],
    [D("43:7", lambda w, h: K0.throne(w, h, 1604), "#05051A", 300, head="The Place of My Throne"),
     F("43:8-9", EZEKIEL_FIRE, AMBER)],
    [VP("43:10", "house", "inner_court", "altar", "outer_wall", room=330, head="Show the House"),
     F("43:11")],
    [D("43:12-13", lambda w, h: K.altar_plate(w, h), BP, 380, head="The Measures of the Altar"),
     F("43:14-17", EZEKIEL_FIRE, AMBER)],
    [D("43:18-19", lambda w, h: K.consecration("cs16", w, h, 1605), "#5A6A8A", 300, head="The Ordinances of the Altar"),
     F("43:20-21")],
    [D("43:22-24", lambda w, h: K.consecration("cs16b", w, h, 1606, beast="goat"), "#5A6A8A", 280),
     D("43:25-27", lambda w, h: K.consecration("cs16c", w, h, 1607, beast="ram"), "#5A6A8A", None)],
    [D("44:1-2", lambda w, h: K.shut_gate("sg16", w, h, 1608), "#3A4A7A", 330, head="This Gate Shall Be Shut", stamp=44),
     D("44:3", lambda w, h: K.shut_gate("sg16b", w, h, 1609, prince=True), "#3A4A7A", None)],
    [D("44:4-5", lambda w, h: K.threshold("th16", w, h, 1610), "#2A2A4A", 280, head="Mark Well"),
     F("44:6-7", EZEKIEL_STERN, RED)],
    [VP("44:8-9", "east_gate", "north_gate", "south_gate", room=260),
     D("44:10-11", lambda w, h: K.gatekeepers("gk16", w, h, 1611), "#5A6A8A", None, head="The Levites")],
    [F("44:12-13", EZEKIEL_STERN, RED),
     D("44:14-15", lambda w, h: K.linen_priests("lp16", w, h, 1612), "#6A8AB0", None, head="The Sons of Zadok")],
    [D("44:16-17", lambda w, h: K.linen_priests("lp16b", w, h, 1613), "#6A8AB0", 220, head="Linen Garments"),
     F("44:18-19", EZEKIEL_AWE, AMBER),
     F("44:20-22")],
    [D("44:23-24", lambda w, h: K.judges_gate("jg16", w, h, 1614), "#5A6A8A", 300),
     F("44:25-27", EZEKIEL_AWE, AMBER)],
    [D("44:28-29", lambda w, h: K.firstfruits(w, h, 1615), "#C8905A", 280, head="I Am Their Inheritance"),
     F("44:30-31")],
]
PG.extend(paged(GROUPS, "EZK-C16-D", PG.next(), end=end_mark("NEXT · THE HOLY OBLATION", "right: 10px; bottom: 34px")))
