"""Isaiah volume, Chapter 2 — Holy, Holy, Holy (Isaiah 6–9). Every verse, word for word from ref/eng-asv.
In the year that king Uzziah died: the throne high and lifted up, drawn only as light, smoke and the seraphim (God is never
drawn); woe is me; the live coal; here am I, send me; how long? — the stock that remaineth; Rezin and Pekah against
Jerusalem (a map), Isaiah and Shear-jashub at the conduit of the upper pool, the two smoking firebrands; ask thee a sign —
Immanuel (a young mother at the door with her child); the fly and the bee; the great tablet; the River to the neck; a stone
of stumbling; the testimony bound up; distress and darkness; the people that walked in darkness have seen a great light;
unto us a child is born (the empty throne of David in light); and his hand is stretched out still."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art2 as K
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, ISAIAH_AWE, ISAIAH_JOY, AHAZ, COLD, GOLDEN, RED)
from isa import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
VIS = "#14123A"


@P("ISA-C02-00-Title", "Chapter 2 · Holy, Holy, Holy", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.throne_vision("t2", 760, 820, 201)}</g><rect x="0" y="0" width="760" height="262" fill="#14123A"></rect>')
    return chapter_title(2, "第二話", "Holy, Holy, Holy", "Isaiah 6 – 9", svg, VIS, v("6:8", frm="Here am I;"), "Isaiah · Volume Twenty-Three")


SEGS = (
    [drawn([caps("6:1-2")], "ISA 6:1–2", A(lambda w, h: K.throne_vision("tv2", w, h, 202), VIS), None, head="In the Year That King Uzziah Died", stamp=6),
     drawn([cp("6:3", to="and said,"), say("6:3", frm="Holy, holy, holy"), caps("6:4")], "ISA 6:3–4", A(lambda w, h: K.throne_vision("tv2b", w, h, 203), VIS), None),
     face([cp("6:5", to="Then said I,"), say("6:5", frm="Woe is me!")], "ISA 6:5", ISAIAH_AWE),
     drawn([caps("6:6"), cp("6:7", to="and said,"), say("6:7", frm="Lo, this")], "ISA 6:6–7", A(lambda w, h: K.live_coal("lc2", w, h, 204), "#1A1438"), None),
     night([cp("6:8", to="saying,"), gd("6:8", frm="Whom shall I send", to="for us?"), cp("6:8", frm="Then I said,", to="Then I said,"), say("6:8", frm="Here am I;")], "ISA 6:8", head="Here Am I; Send Me"),
     night([cp("6:9", to="And he said,"), gd("6:9", frm="Go, and tell"), gods("6:10")], "ISA 6:9–10"),
     drawn([cp("6:11", to="Then said I,"), say("6:11", frm="Lord, how long?", to="how long?"), cp("6:11", frm="And he answered,", to="And he answered,"), gd("6:11", frm="Until cities"), gods("6:12-13")],
           "ISA 6:11–13", A(lambda w, h: K.stump(w, h, 205), "#7A7A8A"), None),
     drawn([caps("7:1"), cp("7:2", to="saying,"), say("7:2", frm="Syria is confederate", to="with Ephraim."), cp("7:2", frm="And his heart")], "ISA 7:1–2",
           A(lambda w, h: K.nations_map(w, h, hi=("DAMASCUS", "SAMARIA"), arrows=(("DAMASCUS", "JERUSALEM"), ("SAMARIA", "JERUSALEM")),
                                        show=["DAMASCUS", "SAMARIA", "JERUSALEM", "TYRE", "PHILISTIA", "MOAB", "EDOM", "HAMATH"]), MAP), None, head="Ask Thee a Sign", stamp=7),
     drawn([cp("7:3", to="unto Isaiah,"), gd("7:3", frm="Go forth now")], "ISA 7:3", A(lambda w, h: K.fullers_field("ff2", w, h, 206), "#8FD0E2"), None)]
    + S("7:4-9", "god", [A(lambda w, h: K.firebrands(w, h, 207), MAP), ISAIAH], split=[7])
    + [face([caps("7:10"), gods("7:11")], "ISA 7:10–11", ISAIAH), face([cp("7:12", to="But Ahaz said,"), say("7:12", frm="I will not ask")], "ISA 7:12", AHAZ),
       face([cp("7:13", to="And he said,"), say("7:13", frm="Hear ye now")], "ISA 7:13", ISAIAH_STERN)]
    + S("7:14-16", "say", A(lambda w, h: K.immanuel("im2", w, h, 208), "#5A6ABA"), head="Immanuel")
    + S("7:17-20", "say", [ISAIAH_STERN, A(lambda w, h: K.bees(w, h, 209), MAP)], split=[18])
    + S("7:21-25", "say", [A(lambda w, h: K.cow_sheep("cs2", w, h, 210), "#A8A08A"), ISAIAH_GRIEF], split=[23])
    + [drawn([cp("8:1", to="said unto me,"), gd("8:1", frm="Take thee"), gods("8:2"), cp("8:3", to="Then said Jehovah unto me,"), gd("8:3", frm="Call his name"), gods("8:4")], "ISA 8:1–4",
             A(lambda w, h: K.great_tablet(w, h, 211), "#3A2A2A"), None, head="Maher-shalal-hash-baz", stamp=8)]
    + S("8:5-8", "god", A(lambda w, h: K.river_flood(w, h, 212), "#2A2A4A"), kinds={5: "cap"}, head="The Waters of the River")
    + S("8:9-10", "say", ISAIAH_STERN)
    + S("8:11-15", "god", [A(lambda w, h: K.snare(w, h, 213), MAP), ISAIAH], kinds={11: "cap"})
    + [drawn([gods("8:16"), says("8:17-18")], "ISA 8:16–18", A(lambda w, h: K.bound_scroll(w, h, 214), "#2A1E2A"), None, head="Bind Up the Testimony")]
    + S("8:19-22", "say", [ISAIAH_STERN, A(lambda w, h: K.dark_road("dr2", w, h, 215), "#05050A")], split=[21])
    + S("9:1-2", "say", A(lambda w, h: K.great_light(w, h, 216), "#0B0B2A"), head="A Great Light")
    + S("9:3-5", "say", A(lambda w, h: K.broken_yoke(w, h, 217), "#3A1A1A"))
    + S("9:6-7", "say", A(lambda w, h: K.davids_throne(w, h, 218), "#1A1438"), head="Unto Us a Child Is Born")
    + S("9:8-12", "say", [ISAIAH_STERN], head="His Hand Is Stretched Out Still", at={10: A(lambda w, h: K.bricks_cedars(w, h, 219), "#8A7A6A")})
    + S("9:13-17", "say", [ISAIAH_GRIEF, ISAIAH_STERN])
    + S("9:18-21", "say", [A(lambda w, h: K.forest_fire(w, h, 220), "#2A1A1A"), ISAIAH_STERN])
)
PG.extend(pack(SEGS, "ISA-C02-D", PG.next(), end=end_mark("NEXT · THE ROOT OF JESSE", "right: 10px; bottom: 34px")))
