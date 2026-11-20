"""2 Timothy volume, Chapter 1 — I Have Kept the Faith (2 Timothy 1–4). Every verse, word for word from ref/eng-asv.
2 Timothy 1: the cell at Rome, Paul dictating and Luke writing (1:1–2); Timothy reading the letter by his lamp at Ephesus;
Lois, Eunice and Timothy as three framed faces (1:5); the gift stirred up, the brazier fanned into flame; Paul's face by the
cell's lamp (1:8–11); the deposit sealed (1:12–14); Paul grieving at Asia turned away (1:15); Onesiphorus at the cell door.
2 Timothy 2: Timothy committing the things heard to faithful men; the soldier, the athlete and the husbandman; the garden
tomb and Jesus risen (2:8); the chain and the word not bound; the faithful saying in song boxes beside Paul's face in white
light; the workman; Paul stern at Hymenæus and Philetus; the foundation and its seal (the sayings in a song box); the
vessels of a great house; Timothy gentle toward them that oppose (the snare of the devil words only).
2 Timothy 3: the last days as words over a dark, empty street; Paul stern (3:6–7); Jannes and Jambres before Pharaoh's
gate; the gates of Antioch, Iconium and Lystra; the boy Timothy reading between Lois and Eunice; the ark of the scrolls.
2 Timothy 4: Timothy preaching the word; Paul stern at itching ears; "I am already being offered" beside Paul's face in a
grave gold light; the finished course; the crown of righteousness laid up; the brethren scattered on the map; the cloak
and the parchments; Paul stern at Alexander; the empty judgment-seat (4:16–17); the doxology over the light; the greetings
as portrait cells; the benediction over the cell by night and Timothy reading at Ephesus."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from ti2 import G, art as A
from ti2.common import (K, Pages, D, F, glory, lt, lts, lp, ltj, lj, sg, v, title, fin, greetings, face_portrait, PAUL, PAUL_STERN, PAUL_JOY, PAUL_GRIEF,
                        PAUL_LAMP, PAUL_OFFERED, GOLD_BG, STERN_BG, JOY_BG, GRIEF_BG, OFFER_BG, CELL_BG, AQUILA, PRISCILLA, ONESIPHORUS, ERASTUS, TROPHIMUS,
                        EUBULUS, PUDENS, LINUS, CLAUDIA)
from gal.art import art
from co1.art5 import risen_tomb

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
OLD = A.OLD_BEARD


@P("2TI-C01-00-Title", "Chapter 1 · I Have Kept the Faith", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#241E22"></rect><g transform="translate(0 300)">{A.cell("t01", 760, 640, 5500)}</g>'
    return title(1, "I Have Kept the Faith", "2 Timothy 1–4", svg, "#241E22", v("4:7"), size=88)


SEGS = [
    # 2 Timothy 1 — the unfeigned faith; the gift; the deposit; Onesiphorus
    D(lp("1:1-2"), art(A.cell, "cl1", 5501), "#241E22", head="Paul, an Apostle", sky=1, art_h=280),
    D(lp("1:3-4"), art(A.timothy_reads, "rd1", 5503, beard=OLD), "#3A2418", head="Night and Day", art_h=260),
    D([lt("1:5")], art(A.three_faith), "#0B1A2E", head="Lois and Eunice", art_h=280),
    D(lp("1:6-7"), art(A.embers, 5506), "#1A1014", head="Stir Up the Gift", art_h=240),
    F(lp("1:8-11"), PAUL_LAMP, bg=CELL_BG, head="Be Not Ashamed"),
    D(lp("1:12-14"), art(A.deposit), "#0B1A2E", head="I Know Him Whom I Have Believed", art_h=240),
    F([lt("1:15")], PAUL_GRIEF, bg=GRIEF_BG),
    D(lp("1:16-18"), art(A.onesiphorus_cell, "oc1", 5516), "#241E22", head="The House of Onesiphorus", art_h=260),
    # 2 Timothy 2 — the soldier, the athlete, the husbandman; the word not bound; the workman; the great house
    D(lp("2:1-2"), art(A.youth, "yo1", 5601, beard=OLD), "#D8C098", head="Commit Thou to Faithful Men", sky=2, art_h=250),
    D(lp("2:3-7"), art(A.three_callings, "tc1", 5603), "#8FD0E2", head="A Good Soldier of Christ Jesus", art_h=260),
    D([lt("2:8")], art(risen_tomb, "rt1", 5608), "#4A3A6A", head="Remember Jesus Christ", art_h=260),
    D(lp("2:9-10"), art(A.not_bound, "nb1", 5609), "#241E22", art_h=240),
    F([lt("2:11", to="saying:"), sg("2:11", frm="For if we died"), sg("2:12"), sg("2:13")], PAUL_JOY, bg=JOY_BG, head="Faithful Is the Saying"),
    D(lp("2:14-15"), art(A.workman, "wk1", 5614), "#8FD0E2", head="A Workman", art_h=240),
    F(lp("2:16-18"), PAUL_STERN, bg=STERN_BG),
    D([lt("2:19", to="this seal,"), sg("2:19", frm="The Lord knoweth")], art(A.foundation), "#0B1A2E", head="The Firm Foundation of God", art_h=240),
    D(lp("2:20-21"), art(A.great_house), A.CREAM, art_h=240),
    F(lp("2:22-23"), PAUL),
    D(lp("2:24-26"), art(A.gentle, "gt1", 5624), "#D8C098", head="Gentle towards All", art_h=250),
    # 2 Timothy 3 — the last days; Jannes and Jambres; the sacred writings
    D(lp("3:1-5"), art(A.last_days, 5701), "#05050E", head="In the Last Days", sky=3, art_h=200),
    F(lp("3:6-7"), PAUL_STERN, bg=STERN_BG),
    D(lp("3:8-9"), art(A.jannes_jambres, "jj1", 5708), "#8FD0E2", head="Jannes and Jambres", art_h=260),
    D(lp("3:10-11"), art(A.three_gates, "tg1", 5710), "#3A2A5A", head="Antioch, Iconium, Lystra", art_h=240),
    F(lp("3:12-13"), PAUL),
    D(lp("3:14-15"), art(A.from_a_babe, "fb1", 5714), "#3A2418", head="From a Babe", art_h=260),
    D(lp("3:16-17"), art(A.oracles, 5716), "#3A2418", head="Every Scripture Inspired of God", art_h=240),
    # 2 Timothy 4 — preach the word; the time of my departure; only Luke; the first defence
    D(lp("4:1-2"), art(A.preach, "pc1", 5801), "#8FD0E2", head="Preach the Word", sky=4, art_h=260),
    F(lp("4:3-5"), PAUL_STERN, bg=STERN_BG),
    F([lt("4:6")], PAUL_OFFERED, bg=OFFER_BG, head="The Time of My Departure"),
    D([lt("4:7")], art(A.finish_line, 5807), "#3A2A5A", head="I Have Kept the Faith", art_h=300),
    D([lt("4:8")], art(A.crown_laid, 5808), "#2A2050", art_h=280),
    D(lp("4:9-12"), art(A.scattered), "#0B1A2E", head="Only Luke Is with Me", art_h=280),
    D([lt("4:13")], art(A.cloak_books, 5813), "#C8A878", head="The Cloak and the Parchments", art_h=260),
    F(lp("4:14-15"), PAUL_STERN, bg=STERN_BG),
    D(lp("4:16-17"), art(A.empty_court, "ec1", 5816), "#8FD0E2", head="At My First Defence", art_h=240),
    glory([lt("4:18")], seed=5818),
]
PG.extend(K.pack(SEGS, "2TI-C01-D", PG.next()))

fp = face_portrait
ITEMS = [("PRISCA & AQUILA", "4:19 · SALUTE", [lt("4:19", to="Aquila,")], fp(AQUILA, PRISCILLA)),
         ("ONESIPHORUS", "4:19 · AND HIS HOUSE", [lt("4:19", frm="and the house")], fp(ONESIPHORUS)),
         ("ERASTUS", "4:20 · AT CORINTH", [lt("4:20", to="Corinth:")], fp(ERASTUS)),
         ("TROPHIMUS", "4:20 · LEFT AT MILETUS SICK", [lt("4:20", frm="but Trophimus")], fp(TROPHIMUS)),
         ("BEFORE WINTER", "4:21 · COME", [lt("4:21", to="winter.")], fp(PAUL_LAMP, light="#FFC14D")),
         ("EUBULUS & PUDENS", "4:21 · SALUTETH THEE", [lt("4:21", frm="Eubulus", to="Pudens,")], fp(EUBULUS, PUDENS)),
         ("LINUS & CLAUDIA", "4:21 · AND ALL THE BRETHREN", [lt("4:21", frm="and Linus,")], fp(LINUS, CLAUDIA))]
K.label()                                                       # the greetings' verses are labelled by their cells, not the next panel
PG.extend(greetings(ITEMS, "2TI-C01-G", PG.next(), "2 Timothy", "2TI", head="Salute", most=7))

SEGS2 = [
    D([lt("4:22")], art(A.cell_night, 5822), "#241E22", head="Grace Be with You", art_h=300),
    K.pic(art(A.timothy_reads, "rd2", 5823, beard=OLD), "#3A2418", h=420),
]
PG.extend(K.pack(SEGS2, "2TI-C01-E", PG.next(), end=fin("END OF 2 TIMOTHY · NEXT · TITUS")))
