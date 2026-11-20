"""Colossians volume, Chapter 2 — Seek the Things That Are Above (Colossians 3–4). Every verse, word for word from
ref/eng-asv. Colossians 3: the earth at evening below and the heavens opened in light above, no one drawn in it (3:1–4);
the vices as words over a dark, empty street (3:5–8); the old garment cast down and the new white robe put on (3:9–11);
compassion, kindness, lowliness, meekness, longsuffering as five robes on a rail, love the gold girdle over them all
(3:12–14); the church singing psalms and hymns by lamplight (3:15–17); the household — a man and his wife at their door with
their children (3:18–21); servants working heartily and the master paying what is just and equal (3:22–4:1). Colossians 4:
Paul praying by lamplight, "for which I am also in bonds" (4:2–4); speech seasoned with salt, the salt bowl on the table and
two men talking in the street (4:5–6); Tychicus and Onesimus sent with the letter (4:7–9); the greetings of Aristarchus,
Mark, Jesus called Justus, Epaphras, Luke the beloved physician and Demas, each with his face (4:10–14); the letters going
between Colossæ and Laodicea in the Lycus valley, and Archippus's charge (4:15–17); Paul's own hand writing the salutation,
the chain on his wrist (4:18)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from col import G, art as A, ch01 as _prev
from col.common import (K, Pages, D, F, glory, lt, lp, lps, v, title, fin, greetings, face_portrait, PAUL, PAUL_LAMP, PAUL_JOY, PAUL_STERN, PAUL_GRIEF,
                        GOLD_BG, LAMP_BG, JOY_BG, STERN_BG, GRIEF_BG, ARISTARCHUS, MARK, JUSTUS, EPAPHRAS, LUKE, DEMAS, CODE)
from php.art import art, dark_street, household, assembly

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("COL-C02-00-Title", "Chapter 2 · Seek the Things That Are Above", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#FFF4C2"></rect><g transform="translate(0 300)">{A.things_above(760, 640, 5301)}</g>'
    return title(2, "Seek the Things That Are Above", "Colossians 3–4", svg, "#5A4A7A", v("3:2", to="above,"), size=76)


SEGS = [
    # Colossians 3 — things above; put off, put on; the household
    D(lp("3:1-4"), art(A.things_above, 5301), "#5A4A7A", head="Seek the Things That Are Above", sky=3, art_h=280),
    D(lp("3:5-8"), art(dark_street, 5305), "#05050E", head="Put to Death", art_h=220),
    D(lp("3:9-11"), art(A.garments, "gm1", 5309), "#D8C8A8", head="The New Man", art_h=260),
    D(lp("3:12-14"), art(A.garment_plate), "#0B1A2E", head="Put On Therefore", art_h=290),
    D(lp("3:15-17"), art(assembly, "as1", 5315, stage="order"), "#5A3E2E", head="Psalms and Hymns", art_h=250),
    D(lp("3:18-21"), art(household, "hh1", 5318), "#E8D8B0", head="Wives, Husbands, Children, Fathers", art_h=260),
    D(lps("3:22-25", "4:1"), art(A.servant_master, "sm1", 5322), "#E8D8B0", head="Servants and Masters", art_h=250),
    F(lp("4:2-4"), PAUL_LAMP, bg=LAMP_BG),
    D(lp("4:5-6"), art(A.salt, "sa1", 5405), "#D8C098", head="Seasoned with Salt", art_h=250),
    D(lp("4:7-9"), art(A.sent_with, "sw1", 5407), "#3A2418", head="Tychicus and Onesimus", art_h=270),
]
PG.extend(K.pack(SEGS, "COL-C02-D", PG.next(), most=2, lone=3))

GREET = [
    ("ARISTARCHUS", "4:10 · MY FELLOW-PRISONER", [lt("4:10", to="saluteth you,")], face_portrait(ARISTARCHUS)),
    ("MARK", "4:10 · THE COUSIN OF BARNABAS", [lt("4:10", frm="and Mark")], face_portrait(MARK)),
    ("JESUS CALLED JUSTUS", "4:11 · OF THE CIRCUMCISION", [lt("4:11")], face_portrait(JUSTUS)),
    ("EPAPHRAS", "4:12–13 · WHO IS ONE OF YOU", lp("4:12-13"), face_portrait(EPAPHRAS)),
    ("LUKE AND DEMAS", "4:14 · THE BELOVED PHYSICIAN", [lt("4:14")], face_portrait(LUKE, DEMAS)),
]
K.label()                                                         # the cells carry their own references
PG.extend(greetings(GREET, "COL-C02-G", PG.next(), K.book, CODE, head="Saluteth You"))

SEGS2 = [
    D(lp("4:15-17"), art(A.lycus_valley, "lv2", 5415, letters=True), "#8FD0E2", head="Read Also at Laodicea", art_h=280),
    D([lt("4:18")], art(A.own_hand, 5418), "#3A2418", head="With Mine Own Hand", art_h=300),
]
PG.extend(K.pack(SEGS2, "COL-C02-E", PG.next(), end=fin("END OF COLOSSIANS · NEXT · 1 THESSALONIANS"), most=2))
