"""Ezekiel volume, Chapter 18 — Jehovah Is There (Ezekiel 47–48). Every verse, word for word from ref/eng-asv.
The waters issuing out from under the threshold of the house eastward, on the south of the altar; the man of light with
the line in his hand measuring a thousand cubits and a thousand again — to the ankles, to the knees, to the loins, a river
to swim in (four scenes); very many trees on the one side and on the other; the waters going down into the Arabah and the
sea healed, the fish exceeding many, the fishers spreading their nets from En-gedi to En-eglaim, the marshes given to salt;
every tree for food, the leaf for healing; then the border of the land (a map: the way of Hethlon to Hazar-enon, the
Jordan, Tamar to the brook of Egypt, the great sea), the stranger inheriting among the tribes; the names of the tribes,
each one portion from the east side unto the west side (the map of the land in bands, Dan to Judah, the oblation, Benjamin
to Gad); the holy oblation, the priests', the Levites', the city's (the plan); the city foursquare with its suburbs; the
prince's portion; the egresses of the city, three gates on every side after the names of the tribes (the plan, and the
wall with the tribes' banners); and the name of the city from that day, Jehovah is there — the city under a great light,
no figure. The man's words in speech, Jehovah's in the Voice box, Ezekiel's narration in captions."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from ezk import G, art17 as K
from ezk.common import title_art, fz, dz, paged, plate, EZEKIEL, EZEKIEL_AWE, EZEKIEL_FIRE, AMBER, GOLDEN
from ezk import ch17 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
BP = "#0B1A2E"
OV = {"47:1": "c", "47:2": "c", "47:3": "c", "47:4": "c", "47:5": "c",
      "47:6": (("c", None), ("s", "Son of man,"), ("c", "Then he brought me")), "47:7": "c",
      "47:8": (("c", None), ("s", "These waters")), "47:9": "s", "47:10": "s", "47:11": "s", "47:12": "s"}


@P("EZK-C18-00-Title", "Chapter 18 · Jehovah Is There", title=True)
def title(n):
    svg = title_art(lambda w, h: K.city_glory("t18", w, h, 1801, figures=False), "#1A1A4A")
    return chapter_title(18, "第十八話", "Jehovah Is There", "Ezekiel 47 – 48", svg, "#1A1A4A", v("48:35", frm="and the name of the city"), "Ezekiel · Volume Twenty-Six")


def D(refs, fn, bg=BP, room=280, **k):
    """Verses over a drawing, the drawing given `room` px under the words (room=None: the panel takes what is left)."""
    s = dz(refs, fn, bg, ov=OV, **k)
    return plate(s, room) if room else s
def F(refs, tok=EZEKIEL, bg=GOLDEN, **k): return fz(refs, tok, bg, ov=OV, **k)
LM = lambda *hi, **k: (lambda w, h: K.land_map(w, h, hi=hi, **k))


GROUPS = [
    [D("47:1-2", lambda w, h: K.river_threshold("rt18", w, h, 1802), "#5A7AB0", 330, head="Waters Issued Out from under the Threshold", stamp=47),
     D("47:3-5", lambda w, h: K.depths("dp18", w, h, 1803), "#6A9AC8", None, head="Waters to Swim In")],
    [D("47:6-7", lambda w, h: K.banks("bk18", w, h, 1804), "#6AA0D0", 360, head="Very Many Trees"),
     F("47:8-9", EZEKIEL_AWE, AMBER, head="The Waters Shall Be Healed")],
    [D("47:10-11", lambda w, h: K.healed_sea("hs18", w, h, 1805), "#7AA8D0", 330, head="A Place for the Spreading of Nets"),
     D("47:12", lambda w, h: K.healing_tree("ht18", w, h, 1806), "#5A9AD0", None, head="The Leaf Thereof for Healing")],
    [F("47:13-14", head="This Shall Be the Border"),
     D("47:15-17", LM(bands=False, borders=("N",), title="THE BORDER OF THE LAND · THE NORTH SIDE"), BP, None)],
    [D("47:18-20", LM(bands=False, borders=("E", "S", "W"), title="THE EAST SIDE · THE SOUTH SIDE · THE WEST SIDE"), BP, 340),
     F("47:21-23", EZEKIEL_AWE, AMBER, head="The Stranger That Sojourneth")],
    [D("48:1-4", LM("DAN", "ASHER", "NAPHTALI", "MANASSEH", title="THE PORTIONS OF THE TRIBES · FROM THE NORTH END"), BP, 340, head="The Names of the Tribes", stamp=48),
     D("48:5-7", LM("EPHRAIM", "REUBEN", "JUDAH"), BP, None)],
    [D("48:8-10", lambda w, h: K.oblation_plan(w, h, hi=("priests", "sanctuary")), BP, 330, head="The Holy Oblation"),
     F("48:11-12", EZEKIEL_AWE, AMBER)],
    [D("48:13-14", lambda w, h: K.oblation_plan(w, h, hi=("levites",)), BP, 230),
     D("48:15-17", lambda w, h: K.city_plan(w, h, hi=()), BP, None, head="The City and Its Suburbs")],
    [D("48:18-20", lambda w, h: K.oblation_plan(w, h, hi=("city", "food")), BP, 250),
     D("48:21-22", LM("PRINCE", title="THE PRINCE · BETWEEN JUDAH AND BENJAMIN"), BP, None, head="The Residue Shall Be for the Prince")],
    [D("48:23-27", LM(*K.SOUTH5, title="THE REST OF THE TRIBES · TO THE SOUTH"), BP, 350, head="The Rest of the Tribes"),
     F("48:28-29")],
    [D("48:30-32", lambda w, h: K.city_plan(w, h, hi=("N", "E")), BP, 340, head="The Egresses of the City"),
     D("48:33-34", lambda w, h: K.gate_names("gn18", w, h, 1807, sides=("S", "W")), "#4A7AB8", None)],
    [D("48:35", lambda w, h: K.city_glory("cg18", w, h, 1808), "#1A1A4A", None, head="Jehovah Is There")],
]
PG.extend(paged(GROUPS, "EZK-C18-D", PG.next(), end=end_mark("END OF EZEKIEL · NEXT · DANIEL", "right: 10px; bottom: 34px", ch="完")))
