"""Acts volume, Chapter 1 — The Promise of the Father (Acts 1–2). Every verse, word for word from ref/eng-asv.
The former treatise to Theophilus on the writing-table; the forty days, Jesus risen in white light among the eleven; his
words (1:4–8) in ordinary speech boxes beside his face in white light; the witnesses' map, Jerusalem to the uttermost part
of the earth; the ascension — Jesus risen in white light, hands lifted, a cloud of light receiving him, the eleven looking
up; the two men in white apparel as figures of white light with a gold rim, no faces; the road down Olivet; the upper
chamber, the women and Mary the mother of Jesus with them. Judas' end (1:18–19) is told in words only over the empty field
of blood at dusk. Joseph Barsabbas and Matthias put forward, the prayer, the lots. Pentecost: the sound from heaven as of a
rushing mighty wind about the house, then within, a small tongue of flame-light resting over each head (the Spirit is
never drawn otherwise); the devout men of every nation thronging the street; the nations of 2:9–11 on the map; the mockers.
Peter's sermon: his face alternating with drawings, Joel and the Psalms in song boxes — the signs in the heaven (the sun
darkened, the moon as blood), David's tomb; the crucifixion is only named in his words. The three thousand baptized at the
pool; the apostles' teaching; all things common; bread broken at home."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from act import G, art as A
from act.common import (K, Pages, D, F, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, WHITE_LIGHT, JESUS_RISEN, PETER, PETER_BOLD, CROWD_MAN,
                        MATTHIAS)
from mat.art8 import psalm_scroll
from mat.art11 import potters_field

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ACT-C01-00-Title", "Chapter 1 · The Promise of the Father", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#2A3A7A"></rect><g transform="translate(0 260)">{A.ascension("t1", 760, 820, 101)}</g>'
    return title(1, "The Promise of the Father", "Acts 1 – 2", svg, "#2A3A7A", v("1:9", frm="a cloud received him"))


SEGS = [D([cp("1:1"), cp("1:2")], lambda w, h: A.treatise("tr1", w, h, 101), "#C8A878", head="The Former Treatise", sky=(1, "left")),
        D([cp("1:3")], lambda w, h: A.forty_days("fd1", w, h, 103), "#8FD0E2", art_h=220),
        F([cp("1:4"), sy("1:5")], JESUS_RISEN, bg=WHITE_LIGHT),
        D([cp("1:6", to="saying,"), sy("1:6", frm="Lord, dost thou")], lambda w, h: A.olivet_ask("oa1", w, h, 106), "#8FD0E2", head="Ye Shall Be My Witnesses"),
        F([cp("1:7", to="And he said unto them,"), sy("1:7", frm="It is not for you"), sy("1:8", to="come upon you:")], JESUS_RISEN, bg=WHITE_LIGHT),
        D([sy("1:8", frm="and ye shall be my witnesses")],
          A.map_panel((10, 42, 28, 44), places=("JERUSALEM", "SAMARIA", "ROME", "ANTIOCH", "ALEXANDRIA", "ATHENS"), hi=("JERUSALEM",), regions=("JUDÆA", "SAMARIA"),
                      routes=[("JERUSALEM", "SAMARIA"), ("JERUSALEM", "ANTIOCH"), ("JERUSALEM", "ALEXANDRIA"), ("JERUSALEM", "ATHENS"), ("JERUSALEM", "ROME")],
                      title="ACTS 1:8 · UNTO THE UTTERMOST PART OF THE EARTH", rings="JERUSALEM"), "#0B1A2E", art_h=300),
        D([cp("1:9")], lambda w, h: A.ascension("as1", w, h, 109), "#2A3A7A", head="A Cloud Received Him", art_h=360),
        D([cp("1:10"), cp("1:11", to="who also said,"), sy("1:11", frm="Ye men of Galilee,")], lambda w, h: A.two_in_white("tw1", w, h, 110), "#3A4A8A", art_h=260),
        D([cp("1:12")], lambda w, h: A.olivet_road("or1", w, h, 112), "#8FD0E2", head="The Upper Chamber"),
        D([cp("1:13"), cp("1:14")], lambda w, h: A.upper_chamber("uc1", w, h, 113), "#C8A878", art_h=240),
        D([cp("1:15")], lambda w, h: A.upper_chamber("uc2", w, h, 115, prayer=False, peter_up=True), "#C8A878"),
        F([sy("1:16"), sy("1:17")], PETER),
        D([cp("1:18"), cp("1:19")], lambda w, h: potters_field("pf1", w, h, 118), "#2A1A2A", head="The Field of Blood"),
        F([sy("1:20", to="the book of Psalms,"), sg("1:20", frm="Let his habitation"), sy("1:21"), sy("1:22")], PETER),
        D([cp("1:23")], lambda w, h: A.scene("bm1", w, h, 123, "upper", [(0.1, ("apostle", 0)), (0.2, ("apostle", 1)), (0.42, "barsabbas"), (0.54, "matthias", {"flip": True}),
                                                                       (0.76, ("apostle", 3), {"flip": True}), (0.88, ("apostle", 4), {"flip": True})]), "#C8A878",
          head="The Lot Fell upon Matthias"),
        D([cp("1:24", to="and said,"), sy("1:24", frm="Thou, Lord,"), sy("1:25")],
          lambda w, h: A.scene("pr1", w, h, 124, "upper", [(0.08, ("apostle", 0), {"up": A.UP_HIGH, "flip": True}), (0.2, ("apostle", 1), {"up": A.UP_HIGH, "flip": True}), (0.32, ("apostle", 2)),
                                                          (0.46, "barsabbas"), (0.56, "matthias", {"flip": True}), (0.7, ("apostle", 3), {"flip": True, "up": A.UP_HIGH}),
                                                          (0.82, ("apostle", 4), {"flip": True}), (0.93, ("apostle", 5), {"flip": True})]), "#C8A878"),
        D([cp("1:26")], lambda w, h: A.lots("lt1", w, h, 126), "#C8A878", art_h=240),
        # Acts 2
        D([cp("2:1"), cp("2:2")], lambda w, h: A.wind_house("wh1", w, h, 201), "#5A8AC8", head="The Day of Pentecost", sky=2, art_h=260),
        D([cp("2:3"), cp("2:4")], lambda w, h: A.upper_chamber("uc3", w, h, 203, prayer=False, fire=True, wind=True), "#C8A878", art_h=300),
        D([cp("2:5"), cp("2:6")], lambda w, h: A.multitude_door("md1", w, h, 205), "#8FD0E2"),
        F([cp("2:7", to="saying,"), sy("2:7", frm="Behold,"), sy("2:8")], CROWD_MAN),
        D([sy("2:9"), sy("2:10"), sy("2:11")], lambda w, h: A.nations("nt1", w, h, 209), "#0B1A2E", head="Every Nation under Heaven", art_h=330),
        D([cp("2:12", to="one to another,"), sy("2:12", frm="What meaneth"), cp("2:13", to="mocking said,"), sy("2:13", frm="They are filled")],
          lambda w, h: A.multitude_door("md2", w, h, 212, mock=True), "#8FD0E2"),
        D([cp("2:14", to="saying,"), sy("2:14", frm="Ye men of Judæa,"), sy("2:15"), sy("2:16")], lambda w, h: A.peter_preach("pp1", w, h, 214), "#8FD0E2",
          head="This Is That Which Hath Been Spoken", art_h=220),
        F([sg("2:17"), sg("2:18")], PETER_BOLD),
        D([sg("2:19"), sg("2:20"), sg("2:21")], lambda w, h: A.signs_sky("ss1", w, h, 219), "#05050E", art_h=220),
        F([sy("2:22"), sy("2:23"), sy("2:24")], PETER_BOLD, bg=RED),
        D([sy("2:25", to="concerning him,"), sg("2:25", frm="I beheld"), sg("2:26"), sg("2:27"), sg("2:28")], lambda w, h: psalm_scroll("ps1", w, h, 225), "#E8D8B8"),
        D([sy("2:29"), sy("2:30"), sy("2:31")], lambda w, h: A.davids_tomb("dt1", w, h, 229), "#8FD0E2"),
        F([sy("2:32"), sy("2:33"), sy("2:34", to="saith himself,"), sg("2:34", frm="The Lord said"), sg("2:35"), sy("2:36")], PETER_BOLD),
        D([cp("2:37", to="the rest of the apostles,"), sy("2:37", frm="Brethren, what shall")], lambda w, h: A.peter_preach("pp2", w, h, 237, crowd_n=12), "#8FD0E2",
          head="What Shall We Do?"),
        F([cp("2:38", to="Peter said unto them,"), sy("2:38", frm="Repent ye,"), sy("2:39"), cp("2:40", to="saying,"), sy("2:40", frm="Save yourselves")], PETER),
        D([cp("2:41")], lambda w, h: A.baptized("bp1", w, h, 241), "#8FD0E2", head="All Things Common", art_h=260),
        D([cp("2:42"), cp("2:43")], lambda w, h: A.scene("tc1", w, h, 242, "porch", [(0.12, "peter", {"up": A.UP_BLESS, "flip": True}), (0.22, "john"),
                                                                                 (0.36, "seated", {"c": "#6A4A3A", "v": "#3A4A6A", "flip": True}),
                                                                                 (0.5, "seated", {"c": "#5A6A3A", "flip": True}), (0.62, "woman", {"c": "#6A4A5A", "v": "#3A3A5A", "flip": True}),
                                                                                 (0.74, "seated", {"c": "#7A3A3A", "v": "#E8E2D6", "bd": "#6A645E", "flip": True}),
                                                                                 (0.86, "crowd", {"n": 2, "x1": 0.95, "flip": True})]), "#8FD0E2"),
        D([cp("2:44"), cp("2:45")], lambda w, h: A.all_common("ac1", w, h, 244), "#8FD0E2"),
        D([cp("2:46"), cp("2:47")], lambda w, h: A.breaking_bread("bb1", w, h, 246), "#4A3A3A", art_h=220)]
PG.extend(K.pack(SEGS, "ACT-C01-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · SILVER AND GOLD HAVE I NONE")))
