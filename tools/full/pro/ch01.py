"""Proverbs volume, Chapter 1 — The Beginning of Knowledge (Proverbs 1–3). Every verse, word for word from ref/eng-asv.
The proverbs of Solomon over Solomon at his scrolls; the father's words to his son beside Solomon's face (speech boxes) and
over drawn scenes (song boxes): the sinners lying in wait by the road at dusk (no one harmed) and the net spread in vain;
Wisdom crying aloud before the city gate in white and gold light, her words beside her face; the storm and the whirlwind;
the hid treasure; the two ways; the house that inclineth unto death (no one drawn); trust in Jehovah and the straight road;
barns and vats; the tree of life; the earth founded and the dew (God never drawn); sleep at the tent door; the neighbor
at the door."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
import sa2.art as K2
from pro import G, art as K
from pro.common import (pack, cp, say, sg, sgs, says, caps, face, drawn, joined, SOLOMON, SOLOMON_WISE, SOLOMON_STERN, SON, WISDOM, WISDOM_STERN,
                        COLD, GOLDEN, RED)

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#0F0E2A"


@P("PRO-C01-00-Title", "Chapter 1 · The Beginning of Knowledge", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 240)">{K.wisdom_gate("t1", 760, 700, 101)}</g><rect x="0" y="910" width="760" height="170" fill="#C8A06A"></rect>')
    return chapter_title(1, "第一話", "The Beginning of Knowledge", "Proverbs 1 – 3", svg, "#5A3A6A", v("1:7", to="knowledge;"), "Proverbs · Volume Twenty")


SEGS = [drawn([caps("1:1")] + sgs("1:2-7"), "1:1-7", lambda w, h: K.writing("wr1", w, h, 102), "#3A2214", head="The Proverbs of Solomon", stamp=1),
        face([says("1:8-9")], "1:8-9", SOLOMON),
        drawn(sgs("1:10-12"), "1:10-12", lambda w, h: K.ambush("am1", w, h, 103), "#2A1A3A", head="If Sinners Entice Thee"),
        face([says("1:13-16")], "1:13-16", SOLOMON_STERN, bg=RED),
        drawn(sgs("1:17-19"), "1:17-19", lambda w, h: K.net_road("nt1", w, h, 104), "#8FD0E2"),
        drawn(sgs("1:20-21"), "1:20-21", lambda w, h: K.wisdom_gate("wg1", w, h, 105), "#8FD0E2", h=470, head="Wisdom Crieth Aloud in the Street"),
        face([says("1:22-25")], "1:22-25", WISDOM),
        drawn(sgs("1:26-28"), "1:26-28", lambda w, h: K2.storm(w, h, 106), "#0B0B2A"),
        face([says("1:29-33")], "1:29-33", WISDOM_STERN, bg=RED),
        drawn(sgs("2:1-4"), "2:1-4", lambda w, h: K.treasure("tr1", w, h, 107), "#8FD0E2", head="If Thou Seek Her as Silver", stamp=2),
        face([says("2:5-9")], "2:5-9", SOLOMON_WISE, bg=COLD),
        drawn(sgs("2:10-12"), "2:10-12", lambda w, h: K.two_ways(w, h, 108), "#14141E"),
        face([says("2:13-17")], "2:13-17", SOLOMON_STERN, bg=RED, head="The Strange Woman"),
        drawn(sgs("2:18-19"), "2:18-19", lambda w, h: K.strange_house(w, h, 109), "#1A0A1A"),
        drawn(sgs("2:20-22"), "2:20-22", lambda w, h: K.dwell_land("dl1", w, h, 110), "#8FD0E2"),
        face([says("3:1-4")], "3:1-4", SOLOMON, head="Trust in Jehovah with All Thy Heart", stamp=3),
        drawn(sgs("3:5-7"), "3:5-7", lambda w, h: K.straight_path(w, h, 111), "#5A8FC8"),
        drawn(sgs("3:8-10"), "3:8-10", lambda w, h: K.barns(w, h, 112), "#8FD0E2"),
        face([says("3:11-15")], "3:11-15", SOLOMON_WISE, bg=COLD),
        drawn(sgs("3:16-18"), "3:16-18", lambda w, h: K.tree_of_life("tl1", w, h, 113), "#8FD0E2", h=440, head="A Tree of Life"),
        drawn(sgs("3:19-20"), "3:19-20", lambda w, h: K.founded(w, h, 114), "#0B0B2A", full=True),
        face([says("3:21-23")], "3:21-23", SOLOMON),
        drawn(sgs("3:24-26"), "3:24-26", lambda w, h: K.sleep_secure("sl1", w, h, 115), "#05050A"),
        drawn(sgs("3:27-29"), "3:27-29", lambda w, h: K.neighbor_door("nd1", w, h, 116), "#FFE3B8", head="Withhold Not Good"),
        face([says("3:30-35")], "3:30-35", SOLOMON_STERN, bg=RED)]
PG.extend(pack(SEGS, "PRO-C01-D", PG.next(), end=end_mark("NEXT · GET WISDOM", "right: 10px; bottom: 34px")))
