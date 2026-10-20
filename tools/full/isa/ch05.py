"""Isaiah volume, Chapter 5 — The Burden of Egypt (Isaiah 17–20). Every verse, word for word from ref/eng-asv.
The burden of Damascus — a ruinous heap, flocks in the cities of Aroer; the gleanings of the olive-tree; the altars and the
Asherim forsaken; the uproar of the nations chased as chaff; the land of the rustling of wings beyond the rivers of Ethiopia
and its vessels of papyrus; the vine pruned before the harvest; the burden of Egypt — Jehovah rideth upon a swift cloud (a
storm over the Nile, no one drawn), the Nile dried up, the princes of Zoan, an altar to Jehovah in the midst of Egypt, the
highway out of Egypt to Assyria; and the sign of Isaiah walking barefoot three years (the sackcloth and the sandals laid by
the road; nothing more drawn)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art5 as K
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, ISAIAH_JOY, COLD, GOLDEN, RED)
from isa import ch04 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("ISA-C05-00-Title", "Chapter 5 · The Burden of Egypt", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 0)">{K.swift_cloud(760, 1080, 501)}</g>')
    return chapter_title(5, "第五話", "The Burden of Egypt", "Isaiah 17 – 20", svg, "#2A2A4A", v("19:1", frm="Behold, Jehovah rideth", to="cometh unto Egypt:"), "Isaiah · Volume Twenty-Three")


EGYPT = A(lambda w, h: K.nations_map(w, h, hi=("EGYPT",), show=["EGYPT", "ETHIOPIA", "JERUSALEM", "PHILISTIA", "EDOM", "NINEVEH", "DAMASCUS"]), MAP)
SEGS = (
    S("17:1-3", "god", [A(lambda w, h: K.heap_flocks(w, h, 502), "#4A2A3A"), ISAIAH_STERN], pre=("cap", "The burden of Damascus."), head="The Burden of Damascus")
    + S("17:4-6", "god", [ISAIAH, A(lambda w, h: K.olive_gleaning("og5", w, h, 503), "#C8B8A0")], split=[5])
    + S("17:7-11", "say", [A(lambda w, h: K.asherim(w, h, 504), "#8A8AA0"), ISAIAH_GRIEF], split=[9])
    + S("17:12-14", "say", A(lambda w, h: K.chaff_storm(w, h, 505), "#2A2A40"), budget=600)
    + S("18:1-3", "say", [A(lambda w, h: K.papyrus_boats("pb5", w, h, 506), "#E8A050"), ISAIAH], head="Beyond the Rivers of Ethiopia", split=[3])
    + S("18:4-6", "god", [ISAIAH, A(lambda w, h: K.pruned_vine(w, h, 507), "#E8C878")], pre=("cap", "For thus hath Jehovah said unto me,"), split=[5])
    + S("18:7", "say", A(lambda w, h: K.K1.tribute("tb5", w, h, 508), "#FFE680"))
    + S("19:1-4", "god", [A(lambda w, h: K.swift_cloud(w, h, 509), "#2A2A4A"), ISAIAH_STERN], pre=("cap", "The burden of Egypt."), kinds={1: "say"}, head="The Burden of Egypt", split=[2])
    + S("19:5-10", "say", [A(lambda w, h: K.nile_dry("nd5", w, h, 510), "#E8A060"), ISAIAH_GRIEF], split=[8])
    + S("19:11-15", "say", [ISAIAH_STERN, ISAIAH], head="The Princes of Zoan")
    + S("19:16-17", "say", ISAIAH)
    + S("19:18-22", "say", [EGYPT, A(lambda w, h: K.egypt_altar(w, h, 511), "#8FC8E0"), ISAIAH_JOY], head="An Altar to Jehovah in Egypt", split=[19, 21])
    + S("19:23-24", "say", A(lambda w, h: K.highway(w, h), MAP))
    + S("19:25", "god", ISAIAH_JOY, pre=("say", "hath blessed them, saying,"))
    + [drawn([caps("20:1"), cp("20:2", to="saying,"), gd("20:2", frm="Go, and loose", to="from off thy foot."), cp("20:2", frm="And he did so,")], "ISA 20:1–2",
             A(lambda w, h: K.sackcloth(w, h, 512), "#C8A880"), None, head="Naked and Barefoot", stamp=20)]
    + S("20:3-5", "god", [ISAIAH_STERN, A(lambda w, h: K.captives("cp5", w, h, 513, city="jerusalem"), "#5A4A5A")], pre=("cap", "And Jehovah said,"), split=[4])
    + S("20:6", "say", ISAIAH_GRIEF)
)
PG.extend(pack(SEGS, "ISA-C05-D", PG.next(), end=end_mark("NEXT · WATCHMAN, WHAT OF THE NIGHT?", "right: 10px; bottom: 34px")))
