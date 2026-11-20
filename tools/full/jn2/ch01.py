"""2 John volume, Chapter 1 — The Elect Lady (2 John 1). Every verse, word for word from ref/eng-asv.
The elder unto the elect lady and her children: her house at evening, the lady before her open door with the elder's letter in
her hand, her children about her; her children walking together on the road in the morning light (walking in truth); John's
face beside "that we love one another", and stern beside the deceivers and antichrist (words only: no such figure drawn);
"receive him not into your house" — her door shut and barred by night, a traveller going away down the road, seen from
behind; "I would not write them with paper and ink" — John at his table, the reed pen laid down beside the unfinished sheet;
the children of the elect sister about John at a house door, their hands raised in greeting."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from jn2 import G, art as A
from jn2.common import K, Pages, D, F, lt, lp, v, title, fin, JOHN_OLD, JOHN_STERN, STERN_BG
from gal.art import art

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("2JN-C01-00-Title", "Chapter 1 · The Elect Lady", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2A5A"></rect><g transform="translate(0 300)">{A.lady_house("t21", 760, 680, 2100)}</g>'
    return title(1, "The Elect Lady", "2 John 1", svg, "#3A2A5A", v("1:5", frm="that we love one another."))


SEGS = [
    D(lp("1:1-3"), art(A.lady_house, "lh1", 2101), "#3A2A5A", head="The Elder unto the Elect Lady", sky=1, art_h=290),
    D([lt("1:4")], art(A.walking_truth, "wt1", 2104), "#8FD0E2", head="Walking in Truth", art_h=250),
    F(lp("1:5-6"), JOHN_OLD),
    F(lp("1:7-9"), JOHN_STERN, bg=STERN_BG, head="Look to Yourselves"),
    D(lp("1:10-11"), art(A.shut_door, "sd1", 2110), "#05051A", head="Receive Him Not", art_h=250),
    D([lt("1:12")], art(A.elder_desk, "ed1", 2112, stage="laid"), "#3A2418", head="Face to Face", h=480),
    D([lt("1:13")], art(A.sister_children, "sc1", 2113), "#5A3A6A", art_h=260),
]
PG.extend(K.pack(SEGS, "2JN-C01-D", PG.next(), end=fin("END OF 2 JOHN · NEXT · 3 JOHN")))
