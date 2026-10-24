"""Acts volume, Chapter 4 — Stephen (Acts 7). Every verse, word for word from ref/eng-asv.
The high priest's question; Stephen's defence beside his face, alternating with the history he tells, drawn with the Old
Testament volumes' own drawings: Abraham's road from Ur to Haran and into Canaan on the map, his tent under the stars; the
twelve patriarchs' tents; Joseph's caravan into Egypt and his chariot; the famine and the granaries; the tomb at Shechem;
the bricks of the bondage; the Nile; the wilderness and the road to Midian (the Egyptian smitten told in words only); the
bush burning with fire (an angel in a flame — the bush and the fire only), the Lord's words in the Voice box; the dry path
through the Red sea; the mount in the cloud; the calf; the host of heaven; the tent of meeting; the house Solomon built (the
temple's elevation); the heaven a throne and the earth a footstool (the prophets' words in song boxes). Then Stephen's
face in the red light: Ye stiffnecked; the council cut to the heart; the heavens opened — the glory of God as light only, and
the Son of man standing on the right hand as a figure of white light without a face; the stoning (7:58–60) told in words
only, over the city wall, the garments laid at the feet of a young man named Saul; and the wall alone at dusk: he fell
asleep."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from act import G, art4 as A, ch03 as _prev
from act.common import (K, Pages, D, F, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, DUSK, CAIAPHAS, STEPHEN, STEPHEN_STERN, STEPHEN_GLORY, WHITE_LIGHT)
from genesis import art11 as G11, art12 as G12, art3 as G3
from exo import art as X1, art2 as X2, art4 as X4, art10 as X10
from hos.art2 import calf_broken
from kg1.art import temple_elev
from mat.art11 import new_tomb

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ACT-C04-00-Title", "Chapter 4 · Stephen", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#14123A"></rect><g transform="translate(0 220)">{A.heavens_opened("t4", 760, 860, 755, council_=True)}</g>'
    return title(4, "Stephen", "Acts 7", svg, "#14123A", v("7:56", frm="Behold, I see the heavens opened,"))


def S_(lines, **k): return F(lines, STEPHEN, **k)
ot = A.ot

SEGS = [F([cp("7:1", to="And the high priest said,"), sy("7:1", frm="Are these things so?")], CAIAPHAS, bg=RED, head="Brethren and Fathers, Hearken", h=220),
        D([cp("7:2", to="And he said,"), sy("7:2", frm="Brethren and fathers,"), sy("7:3", to="and said unto him,"), gd("7:3", frm="Get thee out")], A.abraham_road, "#0B1A2E",
          art_h=300, sky=(7, "left")),
        S_([sy("7:4"), sy("7:5")]),
        D([sy("7:6"), gd("7:7")], lambda w, h: A.tent_sojourn("ts1", w, h, 706), "#0B0B2A"),
        D([sy("7:8")], ot(X2.patriarchs, "pa1", 708), "#0B0B2A"),
        D([sy("7:9"), sy("7:10")], ot(G12.chariot_ride, "ch1", 709), "#FFE6A0", head="Joseph"),
        D([sy("7:11"), sy("7:12")], lambda w, h: G3.famine(w, h, 711), "#FFE6A0"),
        D([sy("7:13"), sy("7:14"), sy("7:15")], ot(G12.bread_lines, "bl1", 713), "#FFE6A0"),
        D([sy("7:16")], lambda w, h: new_tomb("nt1", w, h, 716), "#2A2A4A"),
        D([sy("7:17"), sy("7:18"), sy("7:19")], ot(X1.bricks, "br1", 717), "#FFE6A0", head="Moses"),
        D([sy("7:20"), sy("7:21"), sy("7:22")], ot(X2.river, "rv1", 720), "#FFE6A0"),
        S_([sy("7:23"), sy("7:24"), sy("7:25")]),
        S_([sy("7:26"), sy("7:27"), sy("7:28")]),
        D([sy("7:29"), sy("7:30")], A.sinai_road, "#0B1A2E", art_h=260),
        D([sy("7:31", to="there came a voice of the Lord,"), gd("7:32", to="and of Jacob."), sy("7:32", frm="And Moses trembled,"),
           sy("7:33", to="said unto him,"), gd("7:33", frm="Loose the shoes"), gd("7:34")], lambda w, h: X1.burning(w, h, 731), "#2A1A3A", art_h=200, head="The Bush"),
        D([sy("7:35"), sy("7:36")], ot(X4.dry_walk, "dw1", 735), "#0F4C68"),
        S_([sy("7:37", to="unto the children of Israel,"), sg("7:37", frm="A prophet shall God"), sy("7:38")]),
        D([sy("7:39"), sy("7:40"), sy("7:41")], lambda w, h: calf_broken(w, h, 739), "#3A2A3A", head="The Calf"),
        D([sy("7:42", to="the book of the prophets,"), sg("7:42", frm="Did ye offer"), sg("7:43")], lambda w, h: A.host_of_heaven("hh1", w, h, 742), "#05051A"),
        D([sy("7:44"), sy("7:45")], ot(X10.tent_without, "tw1", 744, cloud=True), "#FFE6A0", head="The Tabernacle of the Testimony"),
        D([sy("7:46"), sy("7:47")], lambda w, h: temple_elev(w, h), "#0B1A2E"),
        D([sy("7:48"), sg("7:49"), sg("7:50")], lambda w, h: A.throne_footstool("tf1", w, h, 748), "#2A3A7A"),
        F([sy("7:51"), sy("7:52"), sy("7:53")], STEPHEN_STERN, bg=RED, head="The Heavens Opened"),
        D([cp("7:54")], lambda w, h: A.council("cn1", w, h, 754, accused=("stephen",)), "#4A3A44"),
        D([cp("7:55"), cp("7:56", to="and said,"), sy("7:56", frm="Behold, I see")], lambda w, h: A.heavens_opened("ho1", w, h, 755), "#14123A", art_h=320),
        D([cp("7:57"), cp("7:58")], lambda w, h: A.garments_wall("gw1", w, h, 757), "#5A6A9A", head="They Stoned Stephen", art_h=240),
        D([cp("7:59", to="and saying,"), sy("7:59", frm="Lord Jesus,"), cp("7:60", to="cried with a loud voice,"), sy("7:60", frm="Lord, lay not", to="to their charge."),
           cp("7:60", frm="And when he had said this,")], lambda w, h: A.garments_wall("gw2", w, h, 759, dusk=True), "#2A1A3A", art_h=240)]
PG.extend(K.pack(SEGS, "ACT-C04-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · THE ROAD TO DAMASCUS")))
