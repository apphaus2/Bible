"""Acts volume, Chapter 9 — Come Over into Macedonia (Acts 16:1–17:15). Every verse, word for word from ref/eng-asv.
Timothy joining Paul at Lystra; the road through Phrygia and Galatia to Troas on the map (forbidden of the Holy Spirit); the
vision at Troas — Paul asleep and the man of Macedonia standing in a soft light; the voyage by Samothrace and Neapolis to
Philippi; the place of prayer by the river and Lydia, the seller of purple, beside her face; her baptism and her house
hung with purple cloth. The maid's spirit of divination is never drawn: the street of Philippi, Paul turning about. The
marketplace and the magistrates; the beating (16:22–23) in words only over the empty stocks and the rods; Paul and Silas
in the stocks of the inner prison; midnight, praying and singing hymns; the earthquake and the doors opened; the jailor's
sword (16:27) in words only over the open doors; the lights, the jailor fallen down before them, Sirs, what must I do to be
saved? beside his face; his table; the serjeants at the prison gate; Paul's answer beside his face; the magistrates
beseeching; Lydia's house. Thessalonica on the map, the synagogue, the uproar at Jason's door and the rulers of the city;
Berœa by night and the scriptures searched daily; Paul sent to the sea, and on to Athens."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from act import G, art9 as A, ch08 as _prev
from act.common import (K, Pages, D, F, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, DUSK, PAUL, PAUL_STERN, SILAS, TIMOTHY, LYDIA, JAILOR,
                        JAILOR_GLAD, MAGISTRATE, WHITE_LIGHT, ROBES)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ACT-C09-00-Title", "Chapter 9 · Come Over into Macedonia", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2E3A"></rect><g transform="translate(0 300)">{A.vision_troas("t9", 760, 780, 1609)}</g>'
    return title(9, "Come Over into Macedonia", "Acts 16:1 – 17:15", svg, "#2A1E3A", v("16:9", frm="Come over into Macedonia,"))


def scene(p, seed, place, people, **k): return lambda w, h: A.scene(p, w, h, seed, place, people, **k)
sj = A.second_journey

SEGS = [D([cp("16:1"), cp("16:2"), cp("16:3")], lambda w, h: A.timothy_joined("tj1", w, h, 1601), "#8FD0E2", head="Timothy", sky=16, art_h=240),
        D([cp("16:4"), cp("16:5"), cp("16:6"), cp("16:7"), cp("16:8")], lambda w, h: sj(w, h, legs=3, lit=[1, 2], title="ACTS 16:1–8 · DOWN TO TROAS", box=(24.5, 37.5, 35.0, 41.6)),
          "#0B1A2E", art_h=280),
        D([cp("16:9", to="beseeching him, and saying,"), sy("16:9", frm="Come over"), cp("16:10")], lambda w, h: A.vision_troas("vt1", w, h, 1609), "#3A2E3A",
          head="Come Over into Macedonia", art_h=280),
        D([cp("16:11"), cp("16:12")], lambda w, h: sj(w, h, legs=4, title="ACTS 16:11–12 · TO PHILIPPI", box=(22.6, 27.4, 39.2, 41.6)), "#0B1A2E", art_h=260),
        D([cp("16:13"), cp("16:14")], lambda w, h: A.river_prayer("rp1", w, h, 1613), "#8FD0E2", head="Lydia", art_h=240),
        F([cp("16:15", to="she besought us, saying,"), sy("16:15", frm="If ye have judged", to="and abide there."), cp("16:15", frm="And she constrained us.")], LYDIA),
        D([cp("16:16"), cp("16:17", to="cried out, saying,"), sy("16:17", frm="These men are servants")], lambda w, h: A.philippi_street("ps1", w, h, 1616), "#8FD0E2",
          head="In the Name of Jesus Christ"),
        D([cp("16:18", to="said to the spirit,"), sy("16:18", frm="I charge thee", to="to come out of her."), cp("16:18", frm="And it came out")],
          lambda w, h: A.philippi_street("ps2", w, h, 1618), "#8FD0E2"),
        D([cp("16:19"), cp("16:20", to="they said,"), sy("16:20", frm="These men, being Jews,"), sy("16:21")], lambda w, h: A.agora("ag1", w, h, 1619), "#8FD0E2"),
        D([cp("16:22"), cp("16:23")], lambda w, h: A.stocks("sk1", w, h, 1622), "#3A3238", head="At Midnight", art_h=220),
        D([cp("16:24"), cp("16:25")], lambda w, h: A.stocks("sk2", w, h, 1624, singing=True), "#3A3238", art_h=240),
        D([cp("16:26")], lambda w, h: A.stocks("sk3", w, h, 1626, quake=True), "#3A3238", art_h=240),
        D([cp("16:27"), cp("16:28", to="saying,"), sy("16:28", frm="Do thyself no harm:")], lambda w, h: A.jailor_lights("jl1", w, h, 1627, fallen=False), "#3A3238"),
        D([cp("16:29")], lambda w, h: A.jailor_lights("jl2", w, h, 1629), "#3A3238", art_h=240),
        F([cp("16:30", to="and said,"), sy("16:30", frm="Sirs, what must I do")], JAILOR, bg=COLD, h=220),
        F([cp("16:31", to="And they said,"), sy("16:31", frm="Believe on the Lord Jesus,"), cp("16:32")], PAUL),
        D([cp("16:33"), cp("16:34")], lambda w, h: A.jailor_table("jt1", w, h, 1633), "#4A3A3A"),
        D([cp("16:35", to="saying,"), sy("16:35", frm="Let those men go."), cp("16:36", to="saying,"), sy("16:36", frm="The magistrates have sent")],
          lambda w, h: A.prison_gate("pg1", w, h, 1635), "#8FD0E2", head="Men That Are Romans"),
        F([cp("16:37", to="But Paul said unto them,"), sy("16:37", frm="They have beaten us")], PAUL_STERN, bg=RED),
        D([cp("16:38"), cp("16:39")], lambda w, h: A.prison_gate("pg2", w, h, 1638, brought=True), "#8FD0E2"),
        D([cp("16:40")], lambda w, h: A.lydia_house("lh1", w, h, 1640, brethren=True), "#D8C098"),
        # Acts 17
        D([cp("17:1")], lambda w, h: sj(w, h, legs=5, title="ACTS 17:1 · TO THESSALONICA", box=(21.8, 25.2, 39.8, 41.4)), "#0B1A2E", head="Thessalonica", sky=(17, "left"), art_h=240),
        D([cp("17:2"), cp("17:3", to="whom, said he,"), sy("17:3", frm="I proclaim unto you,"), cp("17:4")],
          scene("ts1", 1702, "synagogue", [(0.14, "paul", {"flip": True, "up": A.UP_BLESS}), (0.24, "silas", {"flip": True}),
                                           (0.4, "seated", {"c": "#6A5A3A", "v": "#E8E2D6", "bd": "#6A645E", "flip": True}), (0.54, "seated", {"c": "#3A4A6A", "v": "#3A4A6A", "flip": True}),
                                           (0.68, "woman", {"c": "#5A2A4A", "v": "#2A2A4A", "flip": True}), (0.8, "woman", {"c": "#2A5A5A", "v": "#1F3A5A", "flip": True}),
                                           (0.92, "man", {"c": "#8A6A2A", "hr": "#2A1A10", "flip": True})]), "#C8B490"),
        D([cp("17:5"), cp("17:6", to="crying,"), sy("17:6", frm="These that have turned"), sy("17:7")], lambda w, h: A.jason_door("jd1", w, h, 1705), "#4A2A5A"),
        D([cp("17:8"), cp("17:9")], scene("ru1", 1708, "porch", [(0.16, "man", {"c": "#5A6A7A", "hr": "#2A1A10", "bd": "#2A1A10", "flip": True}),
                                                                 (0.28, "man", {"c": "#6A4A3A", "v": "#6A5A3A", "bd": "#3A2A1A", "flip": True}),
                                                                 (0.6, "toga", {"border": "#1F5FAD", "hr": "#6A645E", "flip": True}), (0.72, "toga", {"border": "#1F5FAD", "hr": "#4A3A2A"}),
                                                                 (0.86, "crowd", {"n": 2, "x1": 0.96})]), "#8FD0E2"),
        D([cp("17:10")], lambda w, h: A.night_road("nr1", w, h, 1710), "#05051A", head="Berœa"),
        D([cp("17:11"), cp("17:12")], lambda w, h: A.berea("br1", w, h, 1711), "#C8B490", art_h=220),
        D([cp("17:13"), cp("17:14")], lambda w, h: A.night_road("nr2", w, h, 1713, who=("paul",), harbour=True), "#05051A", art_h=220),
        D([cp("17:15")], lambda w, h: sj(w, h, legs=7, title="ACTS 17:10–15 · AS FAR AS ATHENS", box=(20.6, 25.8, 37.4, 41.2)), "#0B1A2E", art_h=260)]
PG.extend(K.pack(SEGS, "ACT-C09-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · THE UNKNOWN GOD")))
