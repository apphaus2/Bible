"""Isaiah volume, Chapter 13 — Go Ye Forth from Babylon (Isaiah 46–48). Every verse, word for word from ref/asv.
Bel boweth down, Nebo stoopeth — their idols a burden on the weary beasts; even to hoar hairs will I carry you; the idol borne
on the shoulder that cannot answer; a ravenous bird from the east (a map); come down, and sit in the dust, O virgin daughter
of Babylon (an empty throne overturned, a woman at the hand-mill; nothing more drawn); I shall be mistress for ever; the
astrologers and star-gazers; as stubble the fire shall burn them; hear ye this, O house of Jacob — thy neck an iron sinew;
the furnace of affliction; I am the first, I also am the last; oh that thou hadst hearkened — peace as a river; go ye forth
from Babylon; the water out of the rock; and there is no peace, saith Jehovah, to the wicked."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art13 as K
from ezr import art as EZ
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, ISAIAH_JOY, BABYLON_Q, ZION_JOY, COLD, GOLDEN, RED)
from isa import ch12 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
SKY = "#8FC8E8"


@P("ISA-C13-00-Title", "Chapter 13 · Go Ye Forth from Babylon", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#FFC890"></rect><g transform="translate(0 260)">{EZ.return_caravan("t13", 760, 820, 1301)}</g>')
    return chapter_title(13, "第十三話", "Go Ye Forth from Babylon", "Isaiah 46 – 48", svg, "#C8702A", v("48:20", to="flee ye from the Chaldeans;"), "Isaiah · Volume Twenty-Three")


SEGS = (
    S("46:1-2", "say", A(lambda w, h: K.bel_nebo(w, h, 1302), "#C88A5A", h=470), head="Bel Boweth Down, Nebo Stoopeth")
    + S("46:3-5", "god", ISAIAH_JOY)
    + S("46:6-7", "say", A(lambda w, h: K.borne_idol("bi13", w, h, 1303), "#4A3A3A"))
    + S("46:8-11", "god", [ISAIAH_STERN, A(lambda w, h: K.ravenous_bird(w, h), MAP)], at={11: A(lambda w, h: K.ravenous_bird(w, h), MAP)})
    + S("46:12-13", "god", ISAIAH_JOY)
    + S("47:1-3", "god", A(lambda w, h: K.daughter_dust("dd13", w, h, 1304), "#3A2A4A", h=470), head="O Virgin Daughter of Babylon")
    + S("47:4", "say", ISAIAH_JOY)
    + S("47:5-7", "god", [ISAIAH_STERN, ISAIAH], split=[7])
    + S("47:8-11", "god", [ISAIAH, ISAIAH_STERN], split=[10])
    + S("47:12-13", "god", A(lambda w, h: K.stargazers("st13", w, h, 1305), "#05051A"), head="The Star-gazers")
    + S("47:14-15", "god", A(lambda w, h: K.stubble_fire(w, h, 1306), "#3A1A1A"))
    + S("48:1-5", "god", [ISAIAH_STERN, ISAIAH], kinds={2: "say"}, split=[3], head="Hear Ye This, O House of Jacob")
    + S("48:6-9", "god", [ISAIAH, ISAIAH_STERN], split=[8])
    + S("48:10-11", "god", A(lambda w, h: K.furnace(w, h, 1307), "#1A0E0E"))
    + S("48:12-15", "god", [ISAIAH, ISAIAH_JOY], split=[14], head="I Am the First, I Also Am the Last")
    + [face([gd("48:16", to="there am I:"), say("48:16", frm="and now the Lord Jehovah")], "ISA 48:16", ISAIAH_AWE if False else ISAIAH)]
    + S("48:17", "god", ISAIAH_JOY)
    + S("48:18-19", "god", A(lambda w, h: K.river_waves(w, h, 1308), "#7AB8E8"))
    + S("48:20", "say", A(lambda w, h: EZ.return_caravan("rc13", w, h, 1309), "#FFC890"), head="Go Ye Forth from Babylon")
    + S("48:21-22", "say", A(lambda w, h: K.rock_water("rw13", w, h, 1310), "#E8A050", h=430), kinds={22: "god"})
)
PG.extend(pack(SEGS, "ISA-C13-D", PG.next(), end=end_mark("NEXT · A LIGHT TO THE GENTILES", "right: 10px; bottom: 34px")))
