"""Acts volume, Chapter 11 — Great Is Diana (Acts 19–20). Every verse, word for word from ref/eng-asv.
Ephesus: the twelve disciples who knew only John's baptism, the hands laid on them and the light falling; the school of
Tyrannus; the handkerchiefs carried to the sick; the sons of Sceva — the evil spirit's words and what befell them (19:16)
told only over the shut house door; the books of the magical arts burning in the street; Paul purposing to see Rome.
Demetrius among the craftsmen in his workshop, the little silver shrines, his speech beside his face; the theatre packed,
Great is Diana of the Ephesians; Alexander beckoning; the town-clerk quieting the multitude, beside his face, and the empty
theatre after. Macedonia and Greece on the map; Troas — the upper chamber and its many lights, Eutychus in the window,
his fall told in words only over the empty window and the lamps, then the lad brought alive at break of day; the voyage by
Assos, Mitylene, Chios and Samos to Miletus; the elders of Ephesus on the shore, Paul's farewell beside his face (bound in
the spirit; the grievous wolves among the flock); kneeling on the shore, and the ship."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from act import G, art11 as A, ch10 as _prev
from act.common import (K, Pages, D, F, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, DUSK, PAUL, PAUL_STERN, PAUL_GRIEF, DEMETRIUS, TOWNCLERK,
                        WHITE_LIGHT, ROBES)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ACT-C11-00-Title", "Chapter 11 · Great Is Diana", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{A.theatre("t11", 760, 780, 1929)}</g>'
    return title(11, "Great Is Diana", "Acts 19 – 20", svg, "#3A5A7A", v("19:28", frm="Great is Diana of the Ephesians."))


def scene(p, seed, place, people, **k): return lambda w, h: A.scene(p, w, h, seed, place, people, **k)
tj = A.third_journey

SEGS = [D([cp("19:1"), cp("19:2", to="and he said unto them,"), sy("19:2", frm="Did ye receive", to="when ye believed?"), cp("19:2", frm="And they said unto him,", to="And they said unto him,"),
           sy("19:2", frm="Nay, we did not")], scene("ep1", 1901, "street", [(0.14, "paul", {"flip": True, "up": A.UP_BLESS}), (0.34, "crowd", {"n": 6, "x1": 0.9, "flip": True, "women": 0})]),
          "#8FD0E2", head="Ephesus", sky=19, art_h=220),
        D([cp("19:3", to="And he said,"), sy("19:3", frm="Into what then", to="baptized?"), cp("19:3", frm="And they said,", to="And they said,", after="baptized?"),
           sy("19:3", frm="Into John's baptism."), cp("19:4", to="And Paul said,"), sy("19:4", frm="John baptized"), cp("19:5")], lambda w, h: A.stream("st1", w, h, 1903), "#8FD0E2"),
        D([cp("19:6"), cp("19:7")], lambda w, h: A.seven("hl1", w, h, 1906, hands=True), "#8FD0E2"),
        D([cp("19:8"), cp("19:9"), cp("19:10")], lambda w, h: A.tyrannus("ty1", w, h, 1908), "#B8A07A", art_h=220),
        D([cp("19:11"), cp("19:12")], lambda w, h: A.handkerchiefs("hk1", w, h, 1911), "#D8C098", art_h=220),
        D([cp("19:13", to="saying,"), sy("19:13", frm="I adjure you"), cp("19:14"), cp("19:15", to="said unto them,"), sy("19:15", frm="Jesus I know,")],
          lambda w, h: A.sceva_door("sv1", w, h, 1913), "#4A2A5A", head="The Sons of Sceva"),
        D([cp("19:16"), cp("19:17")], lambda w, h: A.sceva_door("sv2", w, h, 1916), "#4A2A5A"),
        D([cp("19:18"), cp("19:19"), cp("19:20")], lambda w, h: A.books_burned("bb1", w, h, 1918), "#4A2A5A", art_h=240),
        F([cp("19:21", to="saying,"), sy("19:21", frm="After I have been there,"), cp("19:22")], PAUL),
        D([cp("19:23"), cp("19:24"), cp("19:25", to="and said,"), sy("19:25", frm="Sirs, ye know")], lambda w, h: A.workshop("ws1", w, h, 1923), "#D8C098", head="Demetrius", art_h=220),
        F([sy("19:26"), sy("19:27")], DEMETRIUS, bg=RED),
        D([cp("19:28", to="saying,"), sy("19:28", frm="Great is Diana"), cp("19:29")], lambda w, h: A.theatre("th1", w, h, 1928), "#8FD0E2", head="The Theatre", art_h=260),
        D([cp("19:30"), cp("19:31"), cp("19:32")], scene("as1", 1930, "house", [(0.2, "paul", {"flip": True, "up": A.UP_BLESS}), (0.36, ("apostle", 4)), (0.5, "timothy"),
                                                                              (0.66, "toga", {"border": "#E8B830", "hr": "#6A645E", "flip": True}), (0.78, "toga", {"border": "#E8B830", "hr": "#3A2A1A", "flip": True})]),
          "#D8C098"),
        D([cp("19:33"), cp("19:34", to="cried out,"), sy("19:34", frm="Great is Diana")], lambda w, h: A.theatre("th2", w, h, 1933, alexander=True), "#8FD0E2", art_h=240),
        F([cp("19:35", to="he saith,"), sy("19:35", frm="Ye men of Ephesus,"), sy("19:36"), sy("19:37")], TOWNCLERK),
        F([sy("19:38"), sy("19:39"), sy("19:40")], TOWNCLERK),
        D([cp("19:41")], lambda w, h: A.theatre("th3", w, h, 1941, empty=True), "#8FD0E2", art_h=220),
        # Acts 20
        D([cp("20:1"), cp("20:2"), cp("20:3"), cp("20:4"), cp("20:5"), cp("20:6")], lambda w, h: tj(w, h, legs=6, lit=[2, 3, 4, 5], title="ACTS 20:1–6 · MACEDONIA AND GREECE",
                                                                                           box=(20.6, 28.6, 36.8, 41.6)), "#0B1A2E", head="Troas", sky=(20, "left"), art_h=260),
        D([cp("20:7"), cp("20:8"), cp("20:9", to="named Eutychus,")], lambda w, h: A.troas_chamber("tc1", w, h, 2007), "#4A3A3A", head="Eutychus", art_h=260),
        D([cp("20:9", frm="borne down with deep sleep;")], lambda w, h: A.troas_chamber("tc2", w, h, 2009, stage="fell"), "#4A3A3A", art_h=240),
        D([cp("20:10", to="embracing him said,"), sy("20:10", frm="Make ye no ado;"), cp("20:11"), cp("20:12")], lambda w, h: A.troas_chamber("tc3", w, h, 2010, stage="alive"), "#8A6AA0",
          art_h=240),
        D([cp("20:13"), cp("20:14"), cp("20:15"), cp("20:16")], lambda w, h: tj(w, h, legs=7, title="ACTS 20:13–16 · TO MILETUS", box=(24.8, 28.6, 37.2, 40.2)), "#0B1A2E",
          head="At Miletus", art_h=260),
        D([cp("20:17"), cp("20:18", to="he said unto them,"), sy("20:18", frm="Ye yourselves know,")], lambda w, h: A.miletus("ml1", w, h, 2017), "#8FD0E2"),
        F([sy("20:19"), sy("20:20"), sy("20:21")], PAUL),
        F([sy("20:22"), sy("20:23"), sy("20:24")], PAUL_GRIEF, bg=COLD),
        F([sy("20:25"), sy("20:26"), sy("20:27"), sy("20:28")], PAUL),
        D([sy("20:29"), sy("20:30"), sy("20:31")], lambda w, h: A.wolves("wv1", w, h, 2029), "#2A1A3A"),
        F([sy("20:32"), sy("20:33"), sy("20:34"), sy("20:35")], PAUL),
        D([cp("20:36"), cp("20:37"), cp("20:38")], lambda w, h: A.miletus("ml2", w, h, 2036, kneel=True), "#8FD0E2", art_h=240)]
PG.extend(K.pack(SEGS, "ACT-C11-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · BOUND IN THE SPIRIT")))
