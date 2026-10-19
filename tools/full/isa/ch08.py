"""Isaiah volume, Chapter 8 — In Returning and Rest (Isaiah 28–30). Every verse, word for word from ref/asv.
The crown of pride of the drunkards of Ephraim; precept upon precept, line upon line; the covenant with death, and the tried
corner-stone laid in Zion (a blueprint, with the line and the plummet); the bed too short; the plowman and the threshing of
fitches and cummin (a plate); Ho Ariel — the siege, the dream of the hungry man; the sealed book; the potter and the clay;
woe to the rebellious children that go down into Egypt — the beasts of the South; the breach in the high wall; in returning
and rest shall ye be saved; a beacon on the top of a mountain; this is the way, walk ye in it; the rain and the pastures, the
sevenfold light; the name of Jehovah from far (fire and hail, no one drawn); the song in the night; and Topheth."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art8 as K
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, ISAIAH_JOY, ZION_JOY, COLD, GOLDEN, RED)
from isa import ch07 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
SKY = "#8FC8E8"


@P("ISA-C08-00-Title", "Chapter 8 · In Returning and Rest", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#5A6ABA"></rect><g transform="translate(0 220)">{K.way_voice("t8", 760, 860, 801)}</g>')
    return chapter_title(8, "第八話", "In Returning and Rest", "Isaiah 28 – 30", svg, "#3A4A8A", v("30:15", frm="In returning and rest", to="your strength."), "Isaiah · Volume Twenty-Three")


SEGS = (
    S("28:1-4", "say", [A(lambda w, h: K.crown_pride(w, h, 802), "#3A3A5A"), ISAIAH_STERN], head="The Crown of Pride", split=[3])
    + S("28:5-6", "say", ISAIAH_JOY)
    + S("28:7-8", "say", A(lambda w, h: K.toppled_cups(w, h, 803), "#2A1A24"))
    + S("28:9-13", "say", [ISAIAH_STERN], split=[10, 11], at={10: A(lambda w, h: K.precept(w, h, 804), "#3A2A2A")}, head="Precept upon Precept")
    + S("28:14-15", "say", ISAIAH_STERN, head="A Covenant with Death")
    + S("28:16-17", "god", A(lambda w, h: K.cornerstone(w, h), MAP), pre=("cap", "therefore thus saith the Lord Jehovah,"), head="A Tried Stone")
    + S("28:18-19", "god", ISAIAH_STERN)
    + S("28:20", "say", A(lambda w, h: K.short_bed(w, h), MAP))
    + S("28:21-22", "say", ISAIAH_STERN)
    + S("28:23-26", "say", [ISAIAH, A(lambda w, h: K.plowman("pm8", w, h, 805), SKY)], split=[24], head="Doth He That Ploweth Plow Continually?")
    + S("28:27-29", "say", A(lambda w, h: K.threshing(w, h), MAP))
    + S("29:1-4", "god", [A(lambda w, h: K.siege_forts("sf8", w, h, 806), "#5A4A5A"), ISAIAH_GRIEF], split=[4], head="Ho Ariel")
    + S("29:5-8", "say", [ISAIAH, A(lambda w, h: K.dreamer(w, h, 807), "#14122A")], split=[7])
    + S("29:9-12", "say", [ISAIAH_STERN, A(lambda w, h: K.sealed_book("sb8", w, h, 808), "#3A2A2A")], split=[11], head="A Book That Is Sealed")
    + S("29:13-14", "god", ISAIAH_STERN, pre=("cap", "And the Lord said,"))
    + S("29:15-16", "say", A(lambda w, h: K.potter("pt8", w, h, 809), "#5A3A2A"), head="The Potter and the Clay")
    + S("29:17-21", "say", [ISAIAH_JOY, ISAIAH])
    + S("29:22-24", "god", ISAIAH_JOY)
    + S("30:1-5", "god", [A(lambda w, h: K.nations_map(w, h, hi=("EGYPT",), arrows=(("JERUSALEM", "EGYPT"),), show=["EGYPT", "JERUSALEM", "ETHIOPIA", "PHILISTIA", "EDOM", "NINEVEH"]), MAP), ISAIAH_STERN],
        head="Woe to the Rebellious Children", split=[3])
    + S("30:6-7", "god", A(lambda w, h: K.south_caravan(w, h, 810), "#C86A3A"), pre=("cap", "The burden of the beasts of the South."))
    + S("30:8-11", "god", [A(lambda w, h: K.bound_scroll(w, h, 811), "#2A1E2A"), ISAIAH_STERN], split=[9])
    + S("30:12-14", "god", [ISAIAH_STERN, A(lambda w, h: K.bulging_wall(w, h, 812), "#6A6A7A")], pre=("cap", "Wherefore thus saith the Holy One of Israel,"), split=[13])
    + [face([cp("30:15", to="the Holy One of Israel,"), gd("30:15", frm="In returning and rest", to="your strength."), cp("30:15", frm="And ye would not:")], "ISA 30:15", ISAIAH_GRIEF, head="In Returning and Rest")]
    + S("30:16-17", "god", A(lambda w, h: K.beacon(w, h, 813), "#3A2A4A"))
    + S("30:18-21", "say", [ISAIAH_JOY, A(lambda w, h: K.way_voice("wv8", w, h, 814), "#5A6ABA")], split=[20], head="This Is the Way, Walk Ye in It")
    + S("30:22-26", "say", [ISAIAH, ISAIAH_JOY], at={23: A(lambda w, h: K.rain_pasture(w, h, 815), "#7A9AC8"), 26: A(lambda w, h: K.sevenfold(w, h, 816), "#FFE680")})
    + S("30:27-28", "say", A(lambda w, h: K.storm_far(w, h, 817), "#1A0A1A"), head="The Name of Jehovah Cometh from Far")
    + S("30:29-30", "say", [A(lambda w, h: K.pipe_night("pn8", w, h, 818), "#0B0B2A"), ISAIAH], split=[30])
    + S("30:31-33", "say", [ISAIAH_STERN, A(lambda w, h: K.topheth(w, h, 819), "#2A0A0A")], split=[33])
)
PG.extend(pack(SEGS, "ISA-C08-D", PG.next(), end=end_mark("NEXT · THE DESERT SHALL BLOSSOM", "right: 10px; bottom: 34px")))
