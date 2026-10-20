"""Psalms volume, Chapter 4 — Wait for Jehovah (Psalms 34–41), the close of Book I. Every verse, word for word from
ref/eng-asv. David before Abimelech — O taste and see that Jehovah is good; the angel of Jehovah encamping round about; strive
thou, O Jehovah, with them that strive with me (the enemies told as chaff, net and lions); the fountain of life and the
river of thy pleasures; fret not thyself — the wicked fade as the grass and vanish in smoke, the old man who never saw the
righteous forsaken; the sickbed and the burden of sin; every man walketh in a vain show; the horrible pit and the new
song; and blessed be Jehovah, the God of Israel, from everlasting and to everlasting."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from num.pages import Pages
from psa import G
from psa.common import pack, psalm, end_mark, chapter_open
from psa import ch03 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PS-C04-00-Title", "Chapter 4 · Wait for Jehovah", title=True)
def title(n):
    return chapter_open(4, "Wait for Jehovah", "Psalms 34 – 41", "pit", v("40:1") + " " + v("40:2", to="miry clay;"), seed=4001)


SEGS = (psalm(34, "1 DAVID | 4 dawn | 7 camp | 8 harvest | 10 lions | 11 DAVID | 15 glory | 19 fortress", face="DAVID")
        + psalm(35, "1 war | 4 chaff | 7 net | 9 DAVID_KING | 11 DAVID_GRIEF | 13 sackcloth | 15 lions | 18 court | 19 DAVID_WRATH | 27 music", face="DAVID_GRIEF")
        + psalm(36, "1 city | 5 heavens | 6 mountains | 7 wings | 8 brook | 10 DAVID_KING")
        + psalm(37, "1 grass | 3 land | 7 DAVID_OLD | 10 smoke | 12 bow | 16 harvest | 20 smoke | 21 DAVID_OLD | 25 harvest | 27 land | 30 scroll | 32 net | 35 tree | 37 path | 39 fortress",
                face="DAVID_OLD")
        + psalm(38, "1 DAVID_GRIEF | 5 sickbed | 9 DAVID_GRIEF | 12 net | 13 DAVID_MOURN | 17 sackcloth | 21 dawn", face="DAVID_GRIEF")
        + psalm(39, "1 DAVID_OLD | 4 mist | 7 DAVID_OLD | 12 path", face="DAVID_OLD")
        + psalm(40, "1 pit | 3 music | 6 scroll | 9 court | 11 DAVID_KING | 13 DAVID_GRIEF | 16 dawn")
        + psalm(41, "1 sickbed | 4 DAVID_OLD | 9 table | 11 music", face="DAVID_OLD"))
PG.extend(pack(SEGS, "PS-C04-D", PG.next(), end=end_mark("NEXT · BOOK II · AS THE HART PANTETH", "right: 10px; bottom: 34px")))
