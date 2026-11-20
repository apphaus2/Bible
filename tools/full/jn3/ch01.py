"""3 John volume, Chapter 1 — Gaius the Beloved (3 John 1). Every verse, word for word from ref/eng-asv.
The elder unto Gaius the beloved: John at his table by lamplight, two of the travelling brethren before him telling of
Gaius' truth; Gaius at his open door welcoming brethren and strangers coming up the street with their staffs and satchels;
Diotrephes in the door of the house of the church with his arm out barring the way, two of the brethren turned away down the
step, the elder's letter lying unopened on it; "imitate not that which is evil" beside John's face; Demetrius with his staff
and the sealed letter, the brethren and John about him raising their hands in witness; "I am unwilling to write them to thee
with ink and pen" — the reed pen laid down; the friends about John at his door raising their hands in greeting."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from jn3 import G, art as A
from jn3.common import K, Pages, D, F, lt, lp, v, title, fin, JOHN_OLD, GOLD_BG
from gal.art import art

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("3JN-C01-00-Title", "Chapter 1 · Gaius the Beloved", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#4A2A5A"></rect><g transform="translate(0 300)">{A.gaius_door("t31", 760, 680, 3100)}</g>'
    return title(1, "Gaius the Beloved", "3 John 1", svg, "#4A2A5A", v("1:8", frm="that we may be fellow-workers for the truth."))


SEGS = [
    D(lp("1:1-4"), art(A.brethren_come, "bc1", 3101), "#3A2418", head="The Elder unto Gaius the Beloved", sky=1, art_h=280),
    D(lp("1:5-8"), art(A.gaius_door, "gd1", 3105), "#4A2A5A", head="Fellow-workers for the Truth", art_h=270),
    D(lp("1:9-10"), art(A.diotrephes_door, "dd1", 3109), "#2A2040", head="Diotrephes", art_h=230),
    F([lt("1:11")], JOHN_OLD),
    D([lt("1:12")], art(A.demetrius_witness, "dw1", 3112), "#6A8AB0", head="Demetrius", art_h=230),
    D([lt("1:13")], art(A.elder_desk, "ed1", 3113, stage="laid"), "#3A2418", head="Ink and Pen", h=440),
    D([lt("1:14")], art(A.friends_salute, "fs1", 3114), "#8FD0E2", art_h=260),
]
PG.extend(K.pack(SEGS, "3JN-C01-D", PG.next(), end=fin("END OF 3 JOHN · NEXT · JUDE")))
