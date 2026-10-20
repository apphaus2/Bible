"""Isaiah volume, Chapter 1 — The Vineyard of Jehovah (Isaiah 1–5). Every verse, word for word from ref/eng-asv.
The vision of Isaiah; hear, O heavens — the ox knoweth his owner (the hills of Judah, the ox and the ass at the crib); the
daughter of Zion left as a booth in a vineyard; the sacrifices refused; come now, and let us reason together (scarlet and
snow); the faithful city become a harlot, the dross purged; the mountain of Jehovah's house and swords into plowshares;
the day of Jehovah upon all that is lifted up, men in the caves of the rocks; the stay and the staff taken away; the
daughters of Zion and their ornaments (a plate); the branch of Jehovah, the cloud by day and the fire by night; the song
of the vineyard; the woes; and the ensign lifted up to the nations."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art as K
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, ISAIAH_JOY, COLD, GOLDEN, RED)

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
SKY = "#8FD0E2"


@P("ISA-C01-00-Title", "Chapter 1 · The Vineyard of Jehovah", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.vineyard("t1", 760, 820, 101)}</g><rect x="0" y="0" width="760" height="262" fill="#8FD0E2"></rect>')
    return chapter_title(1, "第一話", "The Vineyard of Jehovah", "Isaiah 1 – 5", svg, "#3A6A3A", v("5:7", to="his pleasant plant:"), "Isaiah · Volume Twenty-Three")


SEGS = (
    [drawn([caps("1:1"), say("1:2", to="hath spoken:"), gd("1:2", frm="I have nourished"), gods("1:3")], "ISA 1:1–3",
           A(lambda w, h: K.heavens_earth("he1", w, h, 102), "#3A5A9A"), None, head="The Vision of Isaiah", stamp=1)]
    + S("1:4-9", "say", [ISAIAH_GRIEF, A(lambda w, h: K.booth("bo1", w, h, 103), "#6A5A6A")], head="Ah Sinful Nation")
    + S("1:10-15", "god", [ISAIAH_STERN, A(lambda w, h: K.altar_refused("ar1", w, h, 104), "#2A2040")], kinds={10: "say"}, head="Who Hath Required This?")
    + S("1:16-20", "god", [A(lambda w, h: K.scarlet_snow(w, h, 105), "#F3EFE6"), ISAIAH], head="Come Now, and Let Us Reason Together", split=[18])
    + S("1:21-23", "say", ISAIAH_GRIEF, head="The Faithful City")
    + S("1:24-26", "god", A(lambda w, h: K.refiner(w, h, 106), MAP), pre=("cap", "the Mighty One of Israel,"), fallback=ISAIAH_STERN)
    + S("1:27-31", "say", [ISAIAH, A(lambda w, h: K.faded_oak(w, h, 107), "#C8A880")])
    + S("2:1-3", "say", A(lambda w, h: K.mountain_house("mh1", w, h, 108), "#5A7ABA"), kinds={1: "cap"}, head="The Mountain of Jehovah's House")
    + S("2:4-5", "say", A(lambda w, h: K.plowshares(w, h), MAP))
    + S("2:6-9", "say", [ISAIAH_STERN, A(lambda w, h: K.full_land(w, h, 109), MAP)], split=[7])
    + S("2:10-17", "say", [A(lambda w, h: K.lofty(w, h, 110), "#1A1830"), ISAIAH_STERN], head="The Day of Jehovah of Hosts", split=[12])
    + S("2:18-22", "say", A(lambda w, h: K.caves("cv1", w, h, 111), "#3A2A2A"))
    + S("3:1-7", "say", [A(lambda w, h: K.stay_staff(w, h, 112), "#5A4A3A"), ISAIAH_STERN], kinds={4: "god"}, split=[4], head="The Stay and the Staff")
    + S("3:8-12", "say", [ISAIAH_GRIEF], kinds={12: "god"})
    + S("3:13-14", "say", ISAIAH_STERN)
    + [face([gd("3:15")], "ISA 3:15", ISAIAH_STERN)]
    + S("3:16-17", "god", ISAIAH_STERN, pre=("cap", "Moreover Jehovah said,"), head="The Daughters of Zion")
    + S("3:18-23", "god", A(lambda w, h: K.ornaments(w, h), MAP), budget=900)
    + S("3:24-26", "god", A(lambda w, h: K.gate_mourns("gm1", w, h, 113), "#4A4A5A"))
    + S("4:1", "say", A(lambda w, h: K.seven_women("sw1", w, h, 114), "#8A7A8A"), head="The Branch of Jehovah")
    + S("4:2-6", "say", [ISAIAH_JOY, A(lambda w, h: K.zion_canopy("zc1", w, h, 115), SKY)], split=[5])
    + S("5:1-2", "song", A(lambda w, h: K.vineyard("vy1", w, h, 116), SKY), head="The Song of the Vineyard")
    + S("5:3-6", "god", [ISAIAH, A(lambda w, h: K.vineyard("vy1b", w, h, 117, state="wild"), "#A8A08A")], split=[5])
    + S("5:7", "say", ISAIAH_GRIEF)
    + S("5:8", "say", A(lambda w, h: K.empty_houses(w, h, 118), "#8A8AA0"), head="Woe unto Them")
    + S("5:9-10", "god", ISAIAH_STERN, pre=("say", "Jehovah of hosts,"))
    + S("5:11-17", "say", [A(lambda w, h: K.feast("fs1", w, h, 119), "#2A1428"), ISAIAH_GRIEF], split=[13])
    + S("5:18-23", "say", ISAIAH_STERN)
    + S("5:24-25", "say", A(lambda w, h: K.stubble_fire(w, h, 120), "#3A1A1A"), fallback=ISAIAH_STERN)
    + S("5:26-30", "say", [A(lambda w, h: K.ensign("en1", w, h, 121), "#C8A880"), ISAIAH_STERN], head="An Ensign to the Nations", at={29: A(lambda w, h: K.ensign("en1b", w, h, 122, sea=True), "#3A2A3A")})
)
PG.extend(pack(SEGS, "ISA-C01-D", PG.next(), end=end_mark("NEXT · HOLY, HOLY, HOLY", "right: 10px; bottom: 34px")))
