"""Acts volume, Chapter 8 — The Council at Jerusalem (Acts 14–15). Every verse, word for word from ref/eng-asv.
Iconium, the city divided; the flight to Lycaonia on the map; Lystra — the temple of Jupiter before the city, the cripple
sitting and then leaping up; the gods come down, the priest of Jupiter with the garlanded oxen at the gates; Barnabas and
Paul with their garments rent among the people, We also are men, beside Paul's face; Paul stoned (14:19) told in words only
over the empty gate and the stones; the disciples standing round about him, and Paul risen; the elders appointed; the
return to Antioch on the map. The men from Judæa beside a Pharisee's face; the road through Phœnicia and Samaria; the
apostles and elders gathered in the upper room, James the Lord's brother presiding; Peter standing up, beside his face;
Barnabas and Paul rehearsing; James' judgment beside his face, the prophets in song boxes; the letter over Ezra's
letter-scroll; the epistle read at Antioch; Judas and Silas; the sharp contention and the parting at Seleucia; and the
second journey begun on the map."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from act import G, art8 as A, ch07 as _prev
from act.common import (K, Pages, D, F, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, DUSK, PETER, PETER_BOLD, BARNABAS, PAUL, PAUL_STERN, JAMES_LORD,
                        PHARISEE, SILAS, WHITE_LIGHT, ROBES)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ACT-C08-00-Title", "Chapter 8 · The Council at Jerusalem", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#C8A878"></rect><g transform="translate(0 300)">{A.council_jerusalem("t8", 760, 780, 1513, speaker="james_lord")}</g>'
    return title(8, "The Council at Jerusalem", "Acts 14 – 15", svg, "#5A3A2A", v("15:11", frm="through the grace of the Lord Jesus,"))


def scene(p, seed, place, people, **k): return lambda w, h: A.scene(p, w, h, seed, place, people, **k)
fj = A.first_journey

SEGS = [D([cp("14:1"), cp("14:2"), cp("14:3")], lambda w, h: A.iconium("ic1", w, h, 1401), "#8FD0E2", head="Iconium", sky=14, art_h=260),
        D([cp("14:4"), cp("14:5"), cp("14:6"), cp("14:7")], lambda w, h: A.iconium("ic2", w, h, 1404, divided=True), "#8FD0E2"),
        D([cp("14:8"), cp("14:9")], lambda w, h: A.lystra("ly1", w, h, 1408), "#C8A890", head="Lystra", art_h=240),
        D([cp("14:10", to="with a loud voice,"), sy("14:10", frm="Stand upright", to="on thy feet."), cp("14:10", frm="And he leaped up"),
           cp("14:11", to="speech of Lycaonia,"), sy("14:11", frm="The gods are come down"), cp("14:12")], lambda w, h: A.lystra("ly2", w, h, 1410, stage="leap"), "#C8A890", art_h=240),
        D([cp("14:13")], lambda w, h: A.lystra("ly3", w, h, 1413, stage="oxen"), "#C8A890", art_h=240),
        D([cp("14:14"), cp("14:15", to="and saying,"), sy("14:15", frm="Sirs, why do ye")], lambda w, h: A.lystra("ly4", w, h, 1414, stage="rent"), "#C8A890"),
        F([sy("14:16"), sy("14:17"), cp("14:18")], PAUL),
        D([cp("14:19")], lambda w, h: A.lystra("ly5", w, h, 1419, stage="stoned"), "#3A2A3A", art_h=240),
        D([cp("14:20")], lambda w, h: A.lystra("ly6", w, h, 1420, stage="rose"), "#C8A890", art_h=240),
        D([cp("14:21"), cp("14:22"), cp("14:23")], lambda w, h: A.seven("el1", w, h, 1421, hands=True), "#8FD0E2"),
        D([cp("14:24"), cp("14:25"), cp("14:26")], lambda w, h: fj(w, h, legs=9, title="ACTS 14:21–26 · RETURNED TO ANTIOCH"), "#0B1A2E", art_h=280),
        D([cp("14:27"), cp("14:28")], lambda w, h: A.antioch("an1", w, h, 1427), "#8FD0E2"),
        # Acts 15
        F([cp("15:1", to="saying,"), sy("15:1", frm="Except ye be")], PHARISEE, bg=RED, head="The Apostles and the Elders"),
        D([cp("15:2"), cp("15:3")], lambda w, h: A.antioch_map(w, h), "#0B1A2E", art_h=240, sky=(15, "left")),
        D([cp("15:4"), cp("15:5", to="saying,"), sy("15:5", frm="It is needful")], lambda w, h: A.contended("ct1", w, h, 1504), "#C8A878"),
        D([cp("15:6")], lambda w, h: A.council_jerusalem("cj1", w, h, 1506), "#C8A878", art_h=240),
        F([cp("15:7", to="and said unto them,"), sy("15:7", frm="Brethren, ye know"), sy("15:8"), sy("15:9")], PETER_BOLD),
        F([sy("15:10"), sy("15:11")], PETER),
        D([cp("15:12")], lambda w, h: A.council_jerusalem("cj2", w, h, 1512, speaker="paul"), "#C8A878"),
        F([cp("15:13", to="answered, saying,"), sy("15:13", frm="Brethren, hearken"), sy("15:14"), sy("15:15")], JAMES_LORD),
        D([sg("15:16"), sg("15:17"), sg("15:18")], lambda w, h: A.council_jerusalem("cj3", w, h, 1516, speaker="james_lord"), "#C8A878"),
        F([sy("15:19"), sy("15:20"), sy("15:21")], JAMES_LORD),
        D([cp("15:22")], scene("ch1", 1522, "upper", [(0.1, "james_lord", {"flip": True, "up": A.UP_BLESS}), (0.24, ("apostle", 0), {"flip": True}),
                                                      (0.5, "judas_bars"), (0.62, "silas", {"flip": True}), (0.78, "paul", {"flip": True}), (0.9, "barnabas", {"flip": True})]), "#C8A878"),
        D([cp("15:23", to="and they wrote thus by them,"), sy("15:23", frm="The apostles and the elders,"), sy("15:24"), sy("15:25"), sy("15:26")],
          lambda w, h: A.letter("lt1", w, h, 1523), "#2A1A2A", head="The Letter"),
        D([sy("15:27"), sy("15:28"), sy("15:29")], lambda w, h: A.letter("lt2", w, h, 1527), "#2A1A2A"),
        D([cp("15:30"), cp("15:31")], lambda w, h: A.antioch("an2", w, h, 1530, who=("judas_bars", "silas")), "#8FD0E2"),
        D([cp("15:32"), cp("15:33"), cp("15:35")], lambda w, h: A.antioch("an3", w, h, 1532, who=("paul", "barnabas", "silas"), tone="dusk"), "#4A2A5A"),
        F([cp("15:36", to="Paul said unto Barnabas,"), sy("15:36", frm="Let us return"), cp("15:37"), cp("15:38")], PAUL, head="Paul and Silas"),
        D([cp("15:39"), cp("15:40")], lambda w, h: A.parting("pt1", w, h, 1539), "#8FD0E2", art_h=240),
        D([cp("15:41")], lambda w, h: A.second_journey(w, h, legs=1, title="ACTS 15:41 · THROUGH SYRIA AND CILICIA", box=(30.6, 37.6, 34.8, 38.4)), "#0B1A2E", art_h=200)]
PG.extend(K.pack(SEGS, "ACT-C08-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · COME OVER INTO MACEDONIA")))
