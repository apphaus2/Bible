"""Obadiah volume, Chapter 1 — The Clefts of the Rock (Obadiah 1). Every verse, word for word from ref/asv.
The vision (1:1 in a caption, "We have heard tidings" in the prophet's song line beside his face) and the ambassador among
the nations; Jehovah's words to Edom in the Voice box over the red rock by night and the eagle's nest among the stars; the
vineyard gleaned by night; the border road and the snare; Teman's spears thrown down; the day of Jerusalem's calamity as
the city's smoke seen from the other side and an empty crossway; the cup on the holy mountain; the stubble burning; the map
of the land possessed; and mount Zion at sunrise. God is never drawn."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from oba.minor import Pages, title, fin, NIGHT, DUSK
from oba import G, art as A
from oba.common import K, cp, gd, sg, gds, sgs, OBADIAH, OBADIAH_NIGHT, COLD, GOLDEN

v = G.v
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("OBA-C01-00-Title", "Chapter 1 · The Clefts of the Rock", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#05051A"></rect><g transform="translate(0 260)">{A.clefts(760, 820, 101)}</g>'
    return title(1, "The Clefts of the Rock", "Obadiah 1", svg, "#2A1A4A", v("1:3", frm="O thou that dwellest", to="whose habitation is high;"), "Obadiah · Volume Thirty-One")


SEGS = [K.face([cp("1:1", to="concerning Edom:"), sg("1:1", frm="We have heard")], OBADIAH, head="The Vision of Obadiah", stamp=1),
        K.drawn(gds("1:2-4"), lambda w, h: A.clefts(w, h, 102), NIGHT, head="Thy Nest Among the Stars"),
        K.drawn(gds("1:5-6"), lambda w, h: A.gleaning(w, h, 103), NIGHT),
        K.drawn(gds("1:7"), lambda w, h: A.border_snare("bs1", w, h, 104), "#E8A070"),
        K.drawn(gds("1:8-9"), lambda w, h: A.teman(w, h, 105), "#2A1A3A"),
        K.drawn(gds("1:10-11"), lambda w, h: A.other_side("os1", w, h, 106), "#3A1A1A", head="The Day of Thy Brother"),
        K.drawn(gds("1:12-14"), lambda w, h: A.crossway(w, h, 107), "#2A1A3A"),
        K.drawn(gds("1:15-16"), lambda w, h: A.cup_mount(w, h, 108), "#3A0A10", head="The Day of Jehovah Is Near"),
        K.drawn(sgs("1:17-18"), lambda w, h: A.stubble(w, h, 109), "#1A0A0A"),
        K.drawn(sgs("1:19-20"), lambda w, h: A.possess_map(w, h, lit=("ZION",)), "#0B1A2E", head="The Kingdom Shall Be Jehovah's", h=380),
        K.drawn(sgs("1:21"), lambda w, h: A.kingdom(w, h, 110), "#2A2A5A")]
PG.extend(K.pack(SEGS, "OBA-C01-D", PG.next(), end=fin("END OF OBADIAH · NEXT · JONAH")))
