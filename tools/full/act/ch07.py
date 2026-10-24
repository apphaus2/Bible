"""Acts volume, Chapter 7 — The Word of God Grew (Acts 12–13). Every verse, word for word from ref/eng-asv.
Herod the king (Agrippa I: a gold diadem, black beard, royal purple) beside his face; James killed with the sword (12:2)
told in words only over the palace doorway at night; Peter seized at the days of unleavened bread and kept by the four
quaternions; the church praying; Peter asleep between two soldiers, bound with two chains; the angel of the Lord in the
light of the cell (white light, no face), the chains fallen; the iron gate opening of its own accord; Peter come to
himself in the street; Mary's house and Rhoda at the gate; the stir among the soldiers and Herod's sentence on the guards
(12:19) told in words only over the empty cell; Herod's oration on his throne at Cæsarea, The voice of a god; his death
(12:23) in words only over the empty throne. The church at Antioch, the Holy Spirit's words in the Voice box, the hands laid
on Barnabas and Saul; the first journey on the map; Sergius Paulus and Elymas at Paphos (no sorcery drawn; Elymas' blindness
in words over the dark mist where he stood); Paul's stern face; Antioch of Pisidia and the synagogue; Paul's sermon
beside his face, with the history drawn — the wilderness, Samuel and Saul, David the shepherd-king, John at the Jordan,
the tomb, the stone rolled away, David's tomb — and the Psalms and the prophets in song boxes; the Gentiles glad; the
persecution; the dust shaken off at the gate."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from act import G, art7 as A, ch06 as _prev
from act.common import (K, Pages, D, F, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, DUSK, PETER, PETER_BOLD, AGRIPPA1, AGRIPPA1_PROUD, RHODA,
                        BARNABAS, PAUL, PAUL_STERN, SERGIUS, ELYMAS, WHITE_LIGHT, ROBES)
from ezk.art12 import david_shepherd
from mat.art import jordan
from mat.art11 import new_tomb
from mrk.art9 import stone_back
from mat.art8 import psalm_scroll
from exo.art4 import wilderness as exo_wild

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ACT-C07-00-Title", "Chapter 7 · The Word of God Grew", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#05051A"></rect><g transform="translate(0 260)">{A.asleep_chains("t7", 760, 820, 1207, angel_=True)}</g>'
    return title(7, "The Word of God Grew", "Acts 12 – 13", svg, "#1E1650", v("12:24"))


def scene(p, seed, place, people, **k): return lambda w, h: A.scene(p, w, h, seed, place, people, **k)
ot = A.ot

SEGS = [F([cp("12:1")], AGRIPPA1_PROUD, bg=RED, head="Herod the King", h=220),
        D([cp("12:2")], lambda w, h: A.palace_door("pd1", w, h, 1202), "#1E1420", art_h=220, sky=(12, "left")),
        D([cp("12:3"), cp("12:4")], lambda w, h: A.quaternions("qt1", w, h, 1203), "#6A5A54"),
        D([cp("12:5")], lambda w, h: A.company_pray("cp1", w, h, 1205), "#C8A878"),
        D([cp("12:6")], lambda w, h: A.asleep_chains("ac1", w, h, 1206), "#3A3238", head="The Iron Gate", art_h=240),
        D([cp("12:7", to="saying,"), sy("12:7", frm="Rise up quickly.", to="Rise up quickly."), cp("12:7", frm="And his chains"), cp("12:8", to="said unto him,"),
           sy("12:8", frm="Gird thyself,", to="thy sandals."), cp("12:8", frm="And he did so.", to="saith unto him,"), sy("12:8", frm="Cast thy garment")],
          lambda w, h: A.asleep_chains("ac2", w, h, 1207, angel_=True), "#FFF4C2", art_h=240),
        D([cp("12:9"), cp("12:10")], lambda w, h: A.iron_gate("ig1", w, h, 1209), "#05051A", art_h=240),
        F([cp("12:11", to="he said,"), sy("12:11", frm="Now I know")], PETER_BOLD, bg=NIGHT),
        D([cp("12:12"), cp("12:13"), cp("12:14")], lambda w, h: A.rhoda_gate("rg1", w, h, 1212), "#05051A", head="Rhoda", art_h=240),
        F([cp("12:15", to="And they said unto her,"), sy("12:15", frm="Thou art mad.", to="Thou art mad."), cp("12:15", frm="But she confidently", to="even so."),
           cp("12:15", frm="And they said,", to="And they said,", after="even so."), sy("12:15", frm="It is his angel.")], RHODA, bg=NIGHT),
        D([cp("12:16"), cp("12:17", to="And he said,"), sy("12:17", frm="Tell these things", to="and to the brethren."), cp("12:17", frm="And he departed,")],
          lambda w, h: A.rhoda_gate("rg2", w, h, 1216, opened=True), "#05051A"),
        D([cp("12:18"), cp("12:19")], lambda w, h: A.prison_found("pf1", w, h, 1218), "#3A3238"),
        D([cp("12:20"), cp("12:21")], lambda w, h: A.herod_throne("hr1", w, h, 1220), "#8FD0E2", head="The Voice of a God", art_h=240),
        D([cp("12:22", to="saying,"), sy("12:22", frm="The voice of a god,")], lambda w, h: A.herod_throne("hr2", w, h, 1222), "#8FD0E2"),
        D([cp("12:23")], lambda w, h: A.herod_throne("hr3", w, h, 1223, herod=False, crowd_=False), "#2A2A4A", art_h=240),
        D([cp("12:24"), cp("12:25")], lambda w, h: A.relief("rl1", w, h, 1224), "#8FD0E2"),
        # Acts 13
        D([cp("13:1"), cp("13:2", to="the Holy Spirit said,"), gd("13:2", frm="Separate me")], lambda w, h: A.agabus_stood("as1", w, h, 1301), "#D8C098",
          head="Separate Me Barnabas and Saul", sky=13, art_h=240),
        D([cp("13:3")], lambda w, h: A.seven("hs1", w, h, 1303, hands=True), "#8FD0E2"),
        D([cp("13:4"), cp("13:5")], lambda w, h: A.first_journey(w, h, legs=2, title="ACTS 13:4–5 · SELEUCIA AND SALAMIS"), "#0B1A2E", art_h=280),
        D([cp("13:6"), cp("13:7"), cp("13:8")], lambda w, h: A.proconsul("pc1", w, h, 1306), "#C8B8A0", head="Paphos"),
        F([cp("13:9"), cp("13:10", to="and said,"), sy("13:10", frm="O full of"), sy("13:11", to="for a season.")], PAUL_STERN, bg=RED),
        D([cp("13:11", frm="And immediately"), cp("13:12")], lambda w, h: A.proconsul("pc2", w, h, 1311, mist=True), "#C8B8A0"),
        D([cp("13:13"), cp("13:14")], lambda w, h: A.first_journey(w, h, legs=5, title="ACTS 13:13–14 · PERGA AND ANTIOCH OF PISIDIA"), "#0B1A2E", art_h=260,
          head="Antioch of Pisidia"),
        D([cp("13:15", to="saying,"), sy("13:15", frm="Brethren, if ye")],
          scene("sg1", 1315, "synagogue", [(0.16, "seated", {"c": "#3A6A3A", "v": "#3A6A3A", "bd": "#4A2A1A"}), (0.28, "seated", {"c": ROBES["paul"], "v": "#5A4A3A", "bd": "#3A2A1A"}),
                                           (0.52, "man", {"c": "#E8E2D6", "v": "#F3EFE6", "bd": "#9A948A", "up": A.UP_BLESS}), (0.66, "seated", {"c": "#6A5A3A", "v": "#E8E2D6", "bd": "#6A645E", "flip": True}),
                                           (0.8, "seated", {"c": "#3A4A6A", "v": "#3A4A6A", "flip": True}), (0.92, "seated", {"c": "#5A2A4A", "flip": True})]), "#C8B490"),
        F([cp("13:16", to="beckoning with the hand said,"), sy("13:16", frm="Men of Israel,"), sy("13:17"), sy("13:18")], PAUL),
        D([sy("13:19"), sy("13:20"), sy("13:21")], lambda w, h: A.kings_of_israel("ki1", w, h, 1319), "#8FD0E2"),
        D([sy("13:22", to="bare witness and said,"), sg("13:22", frm="I have found David"), sy("13:23")], ot(david_shepherd, "dv1", 1322), "#6AB0D8"),
        D([sy("13:24"), sy("13:25", to="he said,"), sy("13:25", frm="What suppose ye")], lambda w, h: jordan("jd1", w, h, 1324, crowd_n=5), "#8FD0E2"),
        F([sy("13:26"), sy("13:27"), sy("13:28")], PAUL),
        D([sy("13:29"), sy("13:30"), sy("13:31")], lambda w, h: stone_back("sb1", w, h, 1329, women=False), "#5A6A9A"),
        F([sy("13:32"), sy("13:33", to="the second psalm,"), sg("13:33", frm="Thou art my Son,"), sy("13:34", to="on this wise,"), sg("13:34", frm="I will give you"),
           sy("13:35", to="in another psalm,"), sg("13:35", frm="Thou wilt not give")], PAUL),
        D([sy("13:36"), sy("13:37")], lambda w, h: A.davids_tomb("dt1", w, h, 1336), "#8FD0E2"),
        F([sy("13:38"), sy("13:39"), sy("13:40"), sg("13:41")], PAUL_STERN, bg=RED),
        D([cp("13:42"), cp("13:43")], scene("bk1", 1342, "street", [(0.12, "paul", {"flip": True, "up": A.UP_BLESS}), (0.24, "barnabas", {"flip": True}),
                                                                    (0.42, "crowd", {"n": 6, "x1": 0.92, "flip": True})]), "#8FD0E2", head="We Turn to the Gentiles"),
        D([cp("13:44"), cp("13:45")], scene("wc1", 1344, "gate", [(0.1, "paul", {"flip": True, "up": A.UP_HIGH}), (0.2, "barnabas", {"flip": True}),
                                                                  (0.36, "crowd", {"n": 5, "x1": 0.7, "flip": True}),
                                                                  (0.78, "man", {"c": "#E8E2D6", "v": "#F3EFE6", "bd": "#9A948A", "up": A.UP_BLESS}),
                                                                  (0.9, "man", {"c": "#3A4A6A", "v": "#3A4A6A", "bd": "#2A1A10", "up": A.UP_HIGH})]), "#8FD0E2"),
        F([cp("13:46", to="and said,"), sy("13:46", frm="It was necessary"), sy("13:47", to="saying,"), sg("13:47", frm="I have set thee")], PAUL),
        D([cp("13:48"), cp("13:49")], scene("gl1", 1348, "gate", [(0.1, "paul", {"flip": True}), (0.2, "barnabas", {"flip": True}),
                                                                  (0.34, "crowd", {"n": 7, "x1": 0.94, "flip": True, "up": A.UP_HIGH})]), "#8FD0E2"),
        D([cp("13:50"), cp("13:51"), cp("13:52")], lambda w, h: A.shake_dust("sd1", w, h, 1350), "#C8A890")]
PG.extend(K.pack(SEGS, "ACT-C07-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · THE COUNCIL AT JERUSALEM")))
