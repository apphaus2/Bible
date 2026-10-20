"""Daniel volume, Chapter 6 — The Time of the End (Daniel 11–12), the last chapter of Daniel. Every verse, word for word from
ref/eng-asv. The words of the man clothed in linen (gold-ruled boxes) over a technical map of the kings of the north and of the
south and a board of their turns: the kings of Persia stirring up all against Greece; the mighty king and his kingdom
divided toward the four winds; the daughter of the king of the south; the mound and the well-fortified city; the isles; the
exactor; the contemptible person and his flatteries; the ships of Kittim and the abomination that maketh desolate; they that
are wise shall instruct many; the god of fortresses; the time of the end — Edom, Moab and Ammon escaping, Egypt, the Libyans
and the Ethiopians, the tents of his palace between the sea and the glorious holy mountain; then Michael standing up, them
that sleep in the dust awaking and the wise shining as the firmament; the book shut up and sealed; the man clothed in linen
above the waters with both hands held up unto heaven; the thousand two hundred and ninety days; go thou thy way."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from dan import G, art6 as K
from dan.common import L, DANIEL_OLD, DANIEL_OLD_AWE, DANIEL_OLD_GRIEF, DANIEL_OLD_PRAY, COLD, GOLDEN, RED, NIGHT
from dan import ch05 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
GD, RD, CY = "#FFD23F", "#FF8A6A", "#8FD0E2"
SEQ = ["S", "N", "S", "N", "N", "N", "N", "S", "N", "N"]


@P("DAN-C06-00-Title", "Chapter 6 · The Time of the End", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 280)">{K.firmament(760, 800, 601)}</g><rect x="0" y="0" width="760" height="282" fill="#0B0B2A"></rect>')
    return chapter_title(6, "第六話", "The Time of the End", "Daniel 11 – 12", svg, "#0B0B2A", v("12:3"), "Daniel · Volume Twenty-Seven")


c, cs, s, ss, sl, cut, A, T, Nt, sp2 = L.c, L.cs, L.s, L.ss, L.sl, L.cut, L.A, L.T, L.N, L.split
d = lambda refs: ss(refs, "daniel")
ln = lambda refs: ss(refs, "linen")
def M(refs, **k):
    head = k.pop("head", None); stamp = k.pop("stamp", None)
    kw = dict(head=head) if head else {}
    if stamp: kw["stamp"] = stamp
    return A([ln(refs)], refs, lambda w, h: K.north_south(w, h, **k), MAP, who="linen", **kw)
def B(refs, lit, **kw):
    return A([ln(refs)], refs, lambda w, h: K.turns(w, h, SEQ, lit), MAP, who="linen", **kw)

SEGS = [M("11:1-2", show=("PERSIA", "GREECE", "LAND"), moves=[("PERSIA", "GREECE", RD)], head="Three Kings in Persia", stamp=11),
        M("11:3-4", show=("GREECE", "NORTH", "SOUTH", "LAND", "PERSIA"), moves=[("GREECE", "NORTH", GD), ("GREECE", "SOUTH", GD), ("GREECE", "PERSIA", GD)], note="DIVIDED TOWARD THE FOUR WINDS"),
        M("11:5-6", moves=[("SOUTH", "NORTH", CY)], hi=("SOUTH",), note="THE DAUGHTER OF THE KING OF THE SOUTH", head="The King of the South"),
        M("11:7-9", show=("NORTH", "SOUTH", "LAND", "EGYPT"), moves=[("SOUTH", "NORTH", RD), ("NORTH", "SOUTH", GD)], hi=("SOUTH",)),
        B("11:10-12", 2),
        M("11:13-14", moves=[("NORTH", "SOUTH", RD)], hi=("NORTH",), head="The King of the North"),
        M("11:15-16", moves=[("NORTH", "SOUTH", RD), ("NORTH", "LAND", RD)], hi=("LAND",), note="A MOUND · A WELL-FORTIFIED CITY"),
        M("11:17-19", show=("NORTH", "SOUTH", "LAND", "ISLES"), moves=[("NORTH", "SOUTH", GD), ("NORTH", "ISLES", RD)], hi=("ISLES",)),
        B("11:20-22", 5, head="A Contemptible Person"),
        B("11:23-24", 6),
        M("11:25-26", moves=[("NORTH", "SOUTH", RD)], hi=("SOUTH",)),
        M("11:27-28", moves=[("NORTH", "LAND", RD)], hi=("LAND",), note="HIS HEART AGAINST THE HOLY COVENANT"),
        M("11:29-31", show=("NORTH", "SOUTH", "LAND", "KITTIM"), moves=[("NORTH", "SOUTH", GD), ("KITTIM", "SOUTH", CY), ("NORTH", "LAND", RD)], hi=("LAND",),
          note="THE ABOMINATION THAT MAKETH DESOLATE", head="Ships of Kittim"),
        A([ln("11:32-35")], "11:32-35", lambda w, h: K.teachers("tc6", w, h, 602), "#E8C890", who="linen", head="They That Are Wise"),
        Nt([ln("11:36-37")], "11:36-37", who="linen", head="The King Shall Do According to His Will"),
        A([ln("11:38-39")], "11:38-39", lambda w, h: K.treasure_house("th6", w, h, 603), "#1A2440", who="linen"),
        M("11:40-41", show=("NORTH", "SOUTH", "LAND", "EDOM", "MOAB", "AMMON"), moves=[("SOUTH", "NORTH", CY), ("NORTH", "LAND", RD)], hi=("LAND",), head="The Time of the End"),
        M("11:42-43", show=("NORTH", "LAND", "EGYPT", "LIBYANS", "ETHIOPIANS"), moves=[("NORTH", "EGYPT", RD), ("EGYPT", "LIBYANS", GD), ("EGYPT", "ETHIOPIANS", GD)], hi=("EGYPT",)),
        M("11:44-45", show=("NORTH", "LAND", "PERSIA", "EGYPT"), moves=[("PERSIA", "LAND", CY), ("NORTH", "LAND", CY)], hi=("LAND",), note="BETWEEN THE SEA AND THE GLORIOUS HOLY MOUNTAIN")]
PG.extend(L.pack(SEGS, "DAN-C06-D", PG.next()))

SEGS2 = [A([ln("12:1")], "12:1", lambda w, h: K.michael(w, h, 604), "#1A1A4A", who="linen", head="Michael Shall Stand Up", stamp=12),
         A([ln("12:2-3")], "12:2-3", lambda w, h: K.firmament(w, h, 605), "#0B0B2A", who="linen"),
         A([ln("12:4")], "12:4", lambda w, h: K.shut_book(w, h, 606), "#2A1A2A", who="linen"),
         A([d("12:5"), *sp2("12:6", "waters of the river,", "daniel", "holy"), d("12:7")], "12:5-7", lambda w, h: K.two_banks("tb6", w, h, 607), "#5A7AA8", who="daniel",
           head="How Long Shall It Be?"),
         T([d("12:8"), *sp2("12:9", "And he said,", "daniel", "linen"), ln("12:10")], "12:8-10", DANIEL_OLD_AWE, COLD, who="linen"),
         A([ln("12:11-12")], "12:11-12", lambda w, h: K.days_chart(w, h), MAP, who="linen"),
         A([ln("12:13")], "12:13", lambda w, h: K.rest(w, h, 608), "#3A2A5A", who="linen", head="Go Thou Thy Way")]
PG.extend(L.pack(SEGS2, "DAN-C06-E", PG.next(), end=end_mark("END OF DANIEL · NEXT · HOSEA", "right: 10px; bottom: 34px", ch="完")))
