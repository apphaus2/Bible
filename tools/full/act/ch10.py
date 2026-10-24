"""Acts volume, Chapter 10 — The Unknown God (Acts 17:16–18:28). Every verse, word for word from ref/eng-asv.
Athens full of idols — the Acropolis above the marketplace and the statues of the gods; the Epicureans and Stoics in the
Stoa; the Areopagus, Paul standing in the midst, his speech beside his face and over the rock and its seated council, the
altar inscribed TO AN UNKNOWN GOD, the poets' words in a song box; some mocking; Dionysius and Damaris. Corinth: Aquila and
Priscilla at their tent-making; Paul shaking out his raiment, beside his stern face; the house of Titus Justus by the
synagogue; the vision by night — the Lord not drawn, his words from the light at the window; Gallio on the judgment-seat,
and what was done to Sosthenes (18:17) told in words only over the empty seat; Cenchreæ and the vow; the voyage to Ephesus
and Cæsarea and up to Antioch on the map; Galatia and Phrygia; Apollos in the synagogue at Ephesus, and Priscilla and
Aquila expounding to him the way of God."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from act import G, art10 as A, ch09 as _prev
from act.common import (K, Pages, D, F, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, DUSK, PAUL, PAUL_STERN, ATHENIAN, AQUILA, PRISCILLA, GALLIO,
                        APOLLOS, WHITE_LIGHT, ROBES, face_of)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ACT-C10-00-Title", "Chapter 10 · The Unknown God", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{A.areopagus("t10", 760, 780, 1722, altar_=True)}</g>'
    return title(10, "The Unknown God", "Acts 17:16 – 18:28", svg, "#3A5A7A", v("17:23", frm="TO AN UNKNOWN GOD.", to="TO AN UNKNOWN GOD."))


def scene(p, seed, place, people, **k): return lambda w, h: A.scene(p, w, h, seed, place, people, **k)
sj = A.second_journey

SEGS = [D([cp("17:16")], lambda w, h: A.athens("at1", w, h, 1716), "#8FD0E2", head="Athens", art_h=260),
        D([cp("17:17"), cp("17:18", to="And some said,"), sy("17:18", frm="What would this babbler say?", to="babbler say?"), cp("17:18", frm="others,", to="others,"),
           sy("17:18", frm="He seemeth", to="strange gods:"), cp("17:18", frm="because he preached")], lambda w, h: A.stoa("so1", w, h, 1717), "#8FD0E2"),
        D([cp("17:19", to="saying,"), sy("17:19", frm="May we know"), sy("17:20"), cp("17:21")], lambda w, h: A.areopagus("ar1", w, h, 1719, speaking=False), "#8FD0E2",
          head="The Areopagus"),
        F([cp("17:22", to="and said,"), sy("17:22", frm="Ye men of Athens,")], PAUL, h=220),
        D([sy("17:23")], lambda w, h: A.areopagus("ar2", w, h, 1723, altar_=True), "#8FD0E2", art_h=260),
        F([sy("17:24"), sy("17:25"), sy("17:26"), sy("17:27")], PAUL),
        D([sy("17:28", to="have said,"), sg("17:28", frm="For we are also"), sy("17:29")], lambda w, h: A.athens("at2", w, h, 1728, paul_=False), "#8FD0E2"),
        F([sy("17:30"), sy("17:31")], PAUL_STERN, bg=RED),
        F([cp("17:32", to="others said,"), sy("17:32", frm="We will hear thee"), cp("17:33")], ATHENIAN, h=240),
        D([cp("17:34")], lambda w, h: A.areopagus("ar3", w, h, 1734, speaking=False), "#8FD0E2"),
        # Acts 18
        D([cp("18:1"), cp("18:2"), cp("18:3")], lambda w, h: A.tentmakers("tm1", w, h, 1801), "#D8C098", head="Corinth", sky=(18, "left"), art_h=240),
        D([cp("18:4"), cp("18:5")], scene("cs1", 1804, "synagogue", [(0.14, "paul", {"flip": True, "up": A.UP_BLESS}), (0.26, "silas", {"flip": True}), (0.36, "timothy", {"flip": True}),
                                                                    (0.54, "seated", {"c": "#6A5A3A", "v": "#E8E2D6", "bd": "#6A645E", "flip": True}),
                                                                    (0.68, "seated", {"c": "#3A4A6A", "v": "#3A4A6A", "flip": True}), (0.84, "philosopher", {"flip": True})]), "#C8B490"),
        F([cp("18:6", to="and said unto them,"), sy("18:6", frm="Your blood")], PAUL_STERN, bg=RED),
        D([cp("18:7"), cp("18:8")], scene("tj1", 1807, "street", [(0.14, "paul", {"flip": True}), (0.26, "man", {"c": "#5A6A3A", "hr": "#3A2A1A", "flip": True}),
                                                                 (0.4, "man", {"c": "#E8E2D6", "v": "#F3EFE6", "bd": "#9A948A", "flip": True}), (0.56, "crowd", {"n": 5, "x1": 0.94, "flip": True})]),
          "#8FD0E2"),
        D([cp("18:9", to="by a vision,"), sy("18:9", frm="Be not afraid,"), sy("18:10"), cp("18:11")], lambda w, h: A.vision_house("vn1", w, h, 1809, who="paul"), "#4A3A3A", art_h=220),
        D([cp("18:12"), cp("18:13", to="saying,"), sy("18:13", frm="This man persuadeth")], lambda w, h: A.judgment_bema("jb1", w, h, 1812), "#8FD0E2", head="Gallio", art_h=240),
        F([cp("18:14", to="Gallio said unto the Jews,"), sy("18:14", frm="If indeed"), sy("18:15")], GALLIO),
        D([cp("18:16"), cp("18:17")], lambda w, h: A.judgment_bema("jb2", w, h, 1816, gallio_=False, accusers=False, paul_=False), "#8FD0E2", art_h=220),
        D([cp("18:18")], lambda w, h: A.cenchreae("cc1", w, h, 1818), "#8FD0E2", art_h=240),
        D([cp("18:19"), cp("18:20"), cp("18:21", to="and saying,"), sy("18:21", frm="I will return", to="if God will,"), cp("18:21", frm="he set sail"), cp("18:22")],
          lambda w, h: sj(w, h, legs=10, lit=[8, 9], title="ACTS 18:18–22 · BY EPHESUS TO CÆSAREA AND ANTIOCH"), "#0B1A2E", art_h=280),
        D([cp("18:23")], lambda w, h: A.third_journey(w, h, legs=1, title="ACTS 18:23 · GALATIA AND PHRYGIA", box=(29.0, 37.4, 35.0, 40.6)), "#0B1A2E", art_h=220),
        D([cp("18:24"), cp("18:25"), cp("18:26", to="in the synagogue.")], lambda w, h: A.apollos_synagogue("ap1", w, h, 1824), "#C8B490", head="Apollos", art_h=220),
        D([cp("18:26", frm="But when Priscilla"), cp("18:27"), cp("18:28")], lambda w, h: A.apollos_synagogue("ap2", w, h, 1826, taught=True), "#D8C098", art_h=220)]
PG.extend(K.pack(SEGS, "ACT-C10-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · GREAT IS DIANA")))
