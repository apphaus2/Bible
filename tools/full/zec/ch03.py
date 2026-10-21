"""Zechariah volume, Chapter 3 — Thy King Cometh (Zechariah 9–11). Every verse, word for word from ref/asv.
The burden upon Hadrach (a map), Tyre burning in the sea, the house encamped about; rejoice greatly, O daughter of Zion: the
king lowly, riding upon an ass, a colt beside (no face); peace from sea to sea; the prisoners in the pit without water; the
bow of Judah and the arrow as lightning; the stones of a crown; the latter rain; the flock without a shepherd; the
corner-stone, the nail, the bow and the ruler; the scattered gathered from Egypt and Assyria (a map); Lebanon's cedars
burning; then Zechariah as the shepherd of the flock of slaughter with his two staves, Beauty cut asunder, the thirty
pieces of silver weighed and cast to the potter, Bands cut asunder, and the worthless shepherd's gear thrown down. 11:4–9
and 11:16–17 are words over the empty fold and the scattered flock; God is never drawn."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from oba.minor import Pages, title, nxt, NIGHT
from zec import G, art3 as A, ch02 as _prev
from mic.art import fold
from zec.common import K, cp, gd, sg, sy, gds, sgs, ZECHARIAH, ZECH_STERN, ZECH_GOLD, COLD, GOLDEN, RED, DUSK

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ZEC-C03-00-Title", "Chapter 3 · Thy King Cometh", title=True)
def title_page(n):
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#5A7AB8"></rect><rect x="0" y="880" width="760" height="200" fill="#E0CC98"></rect>'
           f'<g transform="translate(0 250)">{A.king_ass("tk", 760, 640, 301)}</g>')
    return title(3, "Thy King Cometh", "Zechariah 9 – 11", svg, "#3A5A9A", v("9:9", frm="behold, thy king cometh"), "Zechariah · Volume Thirty-Eight")


SEGS = [K.drawn(sgs("9:1-2"), lambda w, h: A.burden_map(w, h, lit=("HADRACH", "DAMASCUS", "HAMATH", "TYRE", "SIDON")), "#0B1A2E", head="The Burden of the Word of Jehovah", stamp=9),
        K.drawn(sgs("9:3-4"), lambda w, h: A.tyre_fire(w, h, 302), "#2A0A10"),
        K.drawn([sg("9:5"), gd("9:6"), gd("9:7")], lambda w, h: A.burden_map(w, h, lit=("ASHDOD", "EKRON", "ASHKELON", "GAZA")), "#0B1A2E"),
        K.drawn(gds("9:8"), lambda w, h: A.encamp(w, h, 303), "#0B0B2A"),
        K.drawn(sgs("9:9"), lambda w, h: A.king_ass("ka1", w, h, 304), "#5A7AB8", head="Thy King Cometh unto Thee", h=440),
        K.drawn(gds("9:10"), lambda w, h: A.peace_nations(w, h, 305), "#0B1A2E"),
        K.drawn(gds("9:11-12"), lambda w, h: A.pit(w, h, 306), "#2A1E16", head="Prisoners of Hope"),
        K.drawn([gd("9:13"), sg("9:14")], lambda w, h: A.bow_lightning(w, h, 307), "#0B0B2A"),
        K.drawn(sgs("9:15-17"), lambda w, h: A.crown_stones(w, h, 308), "#3A5A9A")]
PG.extend(K.pack(SEGS, "ZEC-C03-D", PG.next()))
SEGS2 = [K.drawn(sgs("10:1-2"), lambda w, h: A.latter_rain(w, h, 309), "#3A4A6A", head="Ask Ye of Jehovah Rain", stamp=10),
         K.drawn(gds("10:3-5"), lambda w, h: A.cornerstone(w, h, 310), "#12113A"),
         K.drawn(gds("10:6-7"), lambda w, h: fold("fd3", w, h, 311), "#2A2A5A"),
         K.drawn(gds("10:8-10"), lambda w, h: A.gather_map(w, h), "#0B1A2E", head="I Will Hiss for Them"),
         K.drawn(gds("10:11-12"), lambda w, h: A.no_shepherd(w, h, 312, scatter=False), "#4A4A5A")]
PG.extend(K.paged([SEGS2[0:3], SEGS2[3:5]], "ZEC-C03-E", PG.next()))
SEGS3 = [K.drawn(sgs("11:1-3"), lambda w, h: A.lebanon_fire(w, h, 313), "#2A0A0A", head="Open Thy Doors, O Lebanon", stamp=11),
         K.drawn([cp("11:4", to="my God:"), gd("11:4", frm="Feed the flock"), gd("11:5"), gd("11:6")], lambda w, h: A.slaughter_flock(w, h, 314), "#4A4A5A", head="The Flock of Slaughter"),
         K.drawn([cp("11:7"), cp("11:8")], lambda w, h: A.staves("st1", w, h, 315), "#8A7A8A"),
         K.face([cp("11:9", to="Then said I,"), sy("11:9", frm="I will not feed you")], ZECH_STERN, bg=RED),
         K.drawn([cp("11:10"), cp("11:11")], lambda w, h: A.staves("st2", w, h, 316, broken=1), "#8A7A8A"),
         K.drawn([cp("11:12", to="unto them,"), sy("11:12", frm="If ye think good", to="forbear."), cp("11:12", frm="So they weighed")], lambda w, h: A.thirty(w, h, 317), "#2A2420", h=330,
                 head="Thirty Pieces of Silver"),
         K.drawn([cp("11:13", to="said unto me,"), gd("11:13", frm="Cast it unto the potter,", to="prized at by them."), cp("11:13", frm="And I took")], lambda w, h: A.potter_cast(w, h, 318), "#5A3A2A"),
         K.drawn([cp("11:14")], lambda w, h: A.staves("st3", w, h, 319, broken=2), "#8A7A8A"),
         K.drawn([cp("11:15", to="said unto me,"), gd("11:15", frm="Take unto thee"), gd("11:16"), sg("11:17")], lambda w, h: A.foolish_shepherd(w, h, 320), "#2A1A3A", head="The Worthless Shepherd")]
PG.extend(K.pack(SEGS3, "ZEC-C03-F", PG.next(), end=nxt("NEXT · THE DAY OF JEHOVAH")))
