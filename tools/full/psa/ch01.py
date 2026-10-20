"""Psalms volume, Chapter 1 — Blessed Is the Man (Psalms 1–12), the opening of Book I. Every verse, word for word from
ref/eng-asv. The tree planted by the streams and the chaff the wind driveth away; the kings of the earth against Jehovah and his
anointed — thou art my son (God's words in the Voice box); David fleeing from Absalom, lying down and sleeping in the midst
of ten thousands; the morning prayer; the bed made to swim with tears; the lion and the pit; when I consider thy heavens;
the nations sunk in the pit that they made; the lurking lion and the net; the bow bent in darkness; and the words of
Jehovah, pure words, as silver tried in a furnace."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title
from num.pages import Pages
from deu.common import shade
from psa import G, art as K
from psa.common import pack, psalm, end_mark

v = G.v
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PS-C01-00-Title", "Chapter 1 · Blessed Is the Man", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 300)">{K.s_tree("t1", 760, 780, 101)}</g>')
    return chapter_title(1, "第一話", "Blessed Is the Man", "Psalms 1 – 12", svg, "#8FD0E2", v("1:3", to="season,"), "Psalms · Volume Nineteen")


SEGS = (psalm(1, "1 tree | 4 chaff")
        + psalm(2, "1 kings | 4 glory | 9 potsherd | 10 DAVID_KING", god={"2:6": None, "2:7": "Thou art my son;", "2:8": None, "2:9": None})
        + psalm(3, "1 DAVID_OLD_ALARM | 5 night | 7 dawn")
        + psalm(4, "1 DAVID | 6 harvest")
        + psalm(5, "1 dawn | 4 city | 9 DAVID_WRATH | 11 wings")
        + psalm(6, "1 DAVID_GRIEF | 6 night", face="DAVID_GRIEF")
        + psalm(7, "1 lions | 3 DAVID_BOLD | 6 glory | 10 bow | 14 pit")
        + psalm(8, "1 heavens | 6 creation")
        + psalm(9, "1 music | 3 broken | 7 glory | 13 gates | 15 pit | 17 nations")
        + psalm(10, "1 DAVID_GRIEVED | 3 city | 8 lions | 12 glory | 17 DAVID")
        + psalm(11, "1 bow | 4 glory | 6 fire")
        + psalm(12, "1 DAVID_GRIEF | 5 furnace", god={"12:5": None}))
PG.extend(pack(SEGS, "PS-C01-D", PG.next(), end=end_mark("NEXT · THE HEAVENS DECLARE", "right: 10px; bottom: 34px")))
