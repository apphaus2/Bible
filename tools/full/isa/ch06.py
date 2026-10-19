"""Isaiah volume, Chapter 6 — Watchman, What of the Night? (Isaiah 21–23). Every verse, word for word from ref/asv.
The burden of the wilderness of the sea — whirlwinds in the South, go up, O Elam; the table prepared; set a watchman, and
the watchman on his tower — fallen, fallen is Babylon; the burden of Dumah — watchman, what of the night?; the burden upon
Arabia and the caravans of Dedanites; the burden of the valley of vision — the housetops, the valleys full of chariots, the
breaches and the pools (a plan), let us eat and drink; Shebna's sepulchre on high and Eliakim with the key of the house of
David (a plate); the burden of Tyre — howl, ye ships of Tarshish; seventy years forgotten, and her hire holiness to Jehovah."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art6 as K
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, ISAIAH_JOY, WATCHMAN, ELIAKIM, SHEBNA, COLD, GOLDEN, RED)
from isa import ch05 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
NIGHTC = "#05051A"


@P("ISA-C06-00-Title", "Chapter 6 · Watchman, What of the Night?", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#05051A"></rect><g transform="translate(0 240)">{K.watch_tower("t6", 760, 840, 601, dawn=True)}</g>')
    return chapter_title(6, "第六話", "Watchman, What of the Night?", "Isaiah 21 – 23", svg, NIGHTC, v("21:11", frm="Watchman, what of the night?", to="what of the night?"), "Isaiah · Volume Twenty-Three")


SEGS = (
    S("21:1-2", "say", A(lambda w, h: K.whirlwind(w, h, 602), "#C86A3A"), pre=("cap", "The burden of the wilderness of the sea."), head="The Wilderness of the Sea")
    + S("21:3-4", "say", ISAIAH_GRIEF)
    + S("21:5", "say", A(lambda w, h: K.feast("fs6", w, h, 603), "#2A1428"))
    + S("21:6-7", "god", [ISAIAH], pre=("cap", "For thus hath the Lord said unto me,"), head="Set a Watchman")
    + [face([cp("21:8", to="And he cried as a lion:"), say("21:8", frm="O Lord, I stand"), say("21:9", to="horsemen in pairs.")], "ISA 21:8–9", WATCHMAN),
       drawn([cp("21:9", frm="And he answered and said,", to="and said,"), say("21:9", frm="Fallen, fallen is Babylon")], "ISA 21:9", A(lambda w, h: K.watch_tower("wt6", w, h, 604, troop=True), NIGHTC), None)]
    + S("21:10", "say", ISAIAH)
    + [drawn([cp("21:11", to="out of Seir,"), say("21:11", frm="Watchman, what of the night?"), cp("21:12", to="The watchman said,"), say("21:12", frm="The morning cometh")], "ISA 21:11–12",
             A(lambda w, h: K.watch_tower("wt6b", w, h, 605, dawn=True), NIGHTC), None, head="Watchman, What of the Night?")]
    + S("21:13-15", "say", [A(lambda w, h: K.dedanites("dd6", w, h, 606), "#3A2A4A")], pre=("cap", "The burden upon Arabia."), head="The Burden upon Arabia")
    + S("21:16-17", "god", A(lambda w, h: K.nations_map(w, h, hi=("KEDAR", "TEMA", "DUMAH"), show=["KEDAR", "TEMA", "DUMAH", "EDOM", "JERUSALEM", "BABYLON", "DAMASCUS"]), MAP),
        pre=("cap", "For thus hath the Lord said unto me,"))
    + S("22:1-3", "say", A(lambda w, h: K.valley_vision("vv6", w, h, 607), "#5A4A7A"), pre=("cap", "The burden of the valley of vision."), head="The Valley of Vision")
    + S("22:4-7", "say", [ISAIAH_GRIEF, A(lambda w, h: K.valley_chariots(w, h, 608), "#6A5A7A")], split=[5])
    + S("22:8-11", "say", A(lambda w, h: K.jerusalem_plan(w, h), MAP, h=560), budget=700)
    + S("22:12-13", "say", A(lambda w, h: K.feast("fs6b", w, h, 609), "#2A1428"))
    + S("22:14", "god", ISAIAH_STERN, pre=("cap", "revealed himself in mine ears,"))
    + S("22:15-19", "god", [A(lambda w, h: K.sepulchre_high("sh6", w, h, 610), "#8FB0D8"), ISAIAH_STERN], head="Shebna the Treasurer", split=[17])
    + S("22:20-21", "god", ISAIAH_JOY, head="Eliakim the Son of Hilkiah")
    + S("22:22-25", "god", [A(lambda w, h: K.key_nail(w, h), MAP), ISAIAH], split=[25])
    + S("23:1-3", "say", A(lambda w, h: K.tyre(w, h, 611), "#3A3A5A"), pre=("cap", "The burden of Tyre."), head="Howl, Ye Ships of Tarshish")
    + S("23:4-9", "say", [ISAIAH_GRIEF, A(lambda w, h: K.nations_map(w, h, hi=("TYRE", "SIDON", "TARSHISH", "KITTIM"), show=["TYRE", "SIDON", "TARSHISH", "KITTIM", "EGYPT", "JERUSALEM", "BABYLON"]), MAP), ISAIAH_STERN], split=[6, 8])
    + S("23:10-11", "say", ISAIAH_STERN)
    + S("23:12", "god", ISAIAH_STERN, pre=("cap", "And he said,"))
    + S("23:13-14", "say", A(lambda w, h: K.tyre(w, h, 612, state="waste"), "#3A3A5A"))
    + S("23:15-18", "say", [ISAIAH, A(lambda w, h: K.harp_lament(w, h, 613), "#2A2040"), A(lambda w, h: K.tyre(w, h, 614, state="trade"), "#8FC8E8")], kinds={16: "song"}, split=[16, 17], head="Seventy Years")
)
PG.extend(pack(SEGS, "ISA-C06-D", PG.next(), end=end_mark("NEXT · THY DEAD SHALL LIVE", "right: 10px; bottom: 34px")))
