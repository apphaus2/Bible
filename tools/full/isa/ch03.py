"""Isaiah volume, Chapter 3 — The Root of Jesse (Isaiah 10–12). Every verse, word for word from ref/asv.
Woe unto them that decree unrighteous decrees; Ho Assyrian, the rod of mine anger — is not Calno as Carchemish? (a map); the
king of Assyria's boast, the riches of the peoples gathered as eggs from a nest; shall the axe boast itself (a plate); the
forest so few that a child may write them; a remnant shall return; the march from Aiath to Nob (a map); Lebanon felled; a
shoot out of the stock of Jesse; the wolf with the lamb and a little child leading them; the outcasts gathered from the four
corners of the earth; and the song of that day — with joy shall ye draw water out of the wells of salvation."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art3 as K
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, ISAIAH_JOY, KING_ASSYRIA, ZION_JOY, COLD, GOLDEN, RED)
from isa import ch02 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
SKY = "#8FD0E2"


@P("ISA-C03-00-Title", "Chapter 3 · The Root of Jesse", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.stump(760, 820, 301, shoot=True, waste=False)}</g><rect x="0" y="0" width="760" height="262" fill="#8FD0E2"></rect>')
    return chapter_title(3, "第三話", "The Root of Jesse", "Isaiah 10 – 12", svg, "#3A6A3A", v("11:1"), "Isaiah · Volume Twenty-Three")


ASSYRIAN = A(lambda w, h: K.nations_map(w, h, hi=("CARCHEMISH", "HAMATH", "ARPAD", "SAMARIA", "DAMASCUS"), arrows=(("NINEVEH", "CARCHEMISH"), ("CARCHEMISH", "ARPAD"), ("ARPAD", "HAMATH"), ("HAMATH", "DAMASCUS"), ("DAMASCUS", "SAMARIA"), ("SAMARIA", "JERUSALEM")),
                                         show=["NINEVEH", "CARCHEMISH", "ARPAD", "HAMATH", "DAMASCUS", "SAMARIA", "JERUSALEM", "TYRE", "BABYLON"]), MAP)
SEGS = (
    S("10:1-4", "say", ISAIAH_STERN, head="Woe unto Them That Decree")
    + S("10:5-11", "god", [ISAIAH_STERN, ASSYRIAN], head="O Assyrian, the Rod of Mine Anger", split=[8])
    + S("10:12", "god", ISAIAH_STERN)
    + S("10:13-14", "say", [KING_ASSYRIA, A(lambda w, h: K.nest(w, h, 302), "#8A7A9A")], pre=("cap", "For he hath said,"), split=[14])
    + S("10:15", "god", A(lambda w, h: K.axe_saw(w, h), MAP))
    + S("10:16-19", "say", [ISAIAH_STERN, A(lambda w, h: K.few_trees("ft3", w, h, 303), "#6A5A6A")], split=[18])
    + S("10:20-23", "say", [A(lambda w, h: K.remnant_road("rr3", w, h, 304), "#8FB0D8"), ISAIAH], head="A Remnant Shall Return")
    + S("10:24-27", "god", [ISAIAH, A(lambda w, h: K.broken_yoke(w, h, 305), "#3A1A1A")], split=[27])
    + S("10:28-32", "say", A(lambda w, h: K.march_map(w, h), MAP), head="He Is Come to Aiath", budget=700)
    + S("10:33-34", "say", A(lambda w, h: K.felled(w, h, 306), "#6A7A9A"))
    + S("11:1-5", "say", [A(lambda w, h: K.stump(w, h, 307, shoot=True, waste=False), SKY), ISAIAH_JOY], head="A Shoot out of the Stock of Jesse")
    + S("11:6-9", "say", A(lambda w, h: K.peaceable("pk3", w, h, 308), SKY), head="A Little Child Shall Lead Them", budget=700)
    + S("11:10", "say", ISAIAH_JOY, head="An Ensign for the Nations")
    + S("11:11-12", "say", A(lambda w, h: K.gathering(w, h), MAP), budget=700)
    + S("11:13-16", "say", A(lambda w, h: K.remnant_road("rr3b", w, h, 309), "#8FB0D8"), budget=800)
    + S("12:1-3", "song", [A(lambda w, h: K.wells("we3", w, h, 310), SKY)], pre=("cap", "thou shalt say,"), head="The Wells of Salvation")
    + S("12:4-6", "song", ZION_JOY, pre=("cap", "shall ye say,"))
)
PG.extend(pack(SEGS, "ISA-C03-D", PG.next(), end=end_mark("NEXT · HOW ART THOU FALLEN", "right: 10px; bottom: 34px")))
