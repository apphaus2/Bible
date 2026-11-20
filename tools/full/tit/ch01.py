"""Titus volume, Chapter 1 — The Grace of God Hath Appeared (Titus 1–3). Every verse, word for word from ref/eng-asv.
Titus 1: Paul writing in a house on his road, free (1:1–3); Titus receiving the sealed roll at his door in Crete; the
letter's road to Crete on Acts' map (1:5); the elders in every city as a plate on the island's outline; the bishop as God's
steward, a plate of qualifications; Paul stern at the vain talkers; "Cretans are always liars, evil beasts, idle gluttons"
(their own prophet) in a song box over a haven of Crete; the basin of clean water (1:15–16).
Titus 2: the household plates — aged men and aged women, the young women, the servants and their masters — and Titus an
ensample to the younger men in a courtyard over the sea; the grace of God appeared, dawn over the sea of Crete; the
blessed hope beside Paul's face in white light.
Titus 3: subject to rulers, the magistrate on his seat; "we also once were foolish" beside Paul's grieving face; the
washing of regeneration, dawn over still water; Paul's face at the faithful saying; the road to Nicopolis for the winter;
Zenas the lawyer and Apollos set forward at the harbour; Titus reading the letter by his lamp."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from tit import G, art as A
from tit.common import (K, Pages, D, F, glory, lt, lp, sg, v, title, fin, PAUL, PAUL_STERN, PAUL_JOY, PAUL_GRIEF, GOLD_BG, STERN_BG, JOY_BG, GRIEF_BG)
from gal.art import art

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("TIT-C01-00-Title", "Chapter 1 · The Grace of God Hath Appeared", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A2A5A"></rect><g transform="translate(0 300)">{A.crete_dawn(760, 640, 5600)}</g>'
    return title(1, "The Grace of God Hath Appeared", "Titus 1–3", svg, "#2A2A5A", v("2:11", to="appeared,"), size=76)


SEGS = [
    # Titus 1 — left in Crete; elders in every city; the vain talkers
    D(lp("1:1-3"), art(A.paul_writes, "pw1", 5601), "#3A2418", head="Paul, a Servant of God", sky=1, art_h=280),
    D([lt("1:4")], art(A.titus_receives, "tr1", 5604), "#D8C098", head="To Titus, My True Child", art_h=280),
    D([lt("1:5")], art(A.crete_road), "#0B1A2E", head="Left in Crete", art_h=260),
    D([lt("1:6")], art(A.elders_crete, "ec1"), "#0B1A2E", head="Elders in Every City", art_h=260),
    D(lp("1:7-9"), art(A.steward_plate, "sp1"), "#0B1A2E", head="As God's Steward", art_h=260),
    F(lp("1:10-11"), PAUL_STERN, bg=STERN_BG, head="Vain Talkers and Deceivers"),
    D([lt("1:12", to="said,"), sg("1:12", frm="Cretans"), lt("1:13"), lt("1:14")], art(A.harbour, "hb1", 5612), "#8FD0E2", head="A Prophet of Their Own", art_h=230),
    D(lp("1:15-16"), art(A.basin_water, 5615), "#D8C8A8", head="To the Pure All Things Are Pure", art_h=220),
    # Titus 2 — the household; the grace of God hath appeared
    D(lp("2:1-3"), art(A.AGED, "ag1"), A.CREAM, head="Aged Men, Aged Women", sky=2, art_h=260),
    D(lp("2:4-5"), art(A.YOUNG, "yw1"), A.CREAM, head="The Young Women", art_h=260),
    D(lp("2:6-8"), art(A.ensample, "en1", 5706), "#8FD0E2", head="An Ensample of Good Works", art_h=250),
    D(lp("2:9-10"), art(A.SERVANTS, "sv1"), A.CREAM, head="Servants", art_h=260),
    D(lp("2:11-12"), art(A.crete_dawn, 5711), "#2A2A5A", head="The Grace of God Hath Appeared", art_h=260),
    F(lp("2:13-15"), PAUL_JOY, bg=JOY_BG, head="The Blessed Hope"),
    # Titus 3 — subject to rulers; the washing of regeneration; Nicopolis
    D(lp("3:1-2"), art(A.ruler_seat, "rs1", 5801), "#8FD0E2", head="Subject to Rulers", sky=3, art_h=240),
    F([lt("3:3")], PAUL_GRIEF, bg=GRIEF_BG),
    D(lp("3:4-7"), art(A.washed, 5804), "#3A3A7A", head="The Washing of Regeneration", art_h=230),
    F(lp("3:8-11"), PAUL),
    D([lt("3:12")], art(A.nicopolis), "#0B1A2E", head="To Nicopolis for the Winter", art_h=260),
    D(lp("3:13-14"), art(A.zenas_apollos, "za1", 5813), "#8FD0E2", head="Zenas and Apollos", art_h=260),
    D([lt("3:15")], art(A.titus_reads, "rd1", 5815, x=0.46, tx=0.2), "#3A2418", head="Grace Be with You All", art_h=280),
]
PG.extend(K.pack(SEGS, "TIT-C01-D", PG.next(), end=fin("END OF TITUS · NEXT · PHILEMON")))
