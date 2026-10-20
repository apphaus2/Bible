"""Psalms volume, Chapter 6 — A Clean Heart (Psalms 51–62). Every verse, word for word from ref/eng-asv.
David after Nathan came to him: have mercy upon me, O God — purify me with hyssop, create in me a clean heart; Doeg the
Edomite and the green olive-tree; the fool again; the Ziphites; oh that I had wings like a dove; the tears in thy bottle at
Gath; in the cave, fleeing from Saul — my soul is among lions, be thou exalted above the heavens; the deaf adder; the dogs
that go round about the city; Moab my washpot, upon Edom will I cast my shoe (God's words in the Voice box, the lands as a
map); lead me to the rock that is higher than I; and my soul waiteth in silence for God only."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from num.pages import Pages
from psa import G
from psa.common import pack, psalm, end_mark, chapter_open
from psa import ch05 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PS-C06-00-Title", "Chapter 6 · A Clean Heart", title=True)
def title(n):
    return chapter_open(6, "A Clean Heart", "Psalms 51 – 62", "hyssop", v("51:10"), seed=6001)


SEGS = (psalm(51, "1 DAVID_MOURN | 5 night | 7 hyssop | 10 DAVID_GRIEF | 13 path | 16 altar | 18 zion", face="DAVID_GRIEF")
        + psalm(52, "1 DAVID_BOLD | 5 smoke | 8 olive", face="DAVID")
        + psalm(53, "1 city | 2 glory | 5 zion")
        + psalm(54, "1 DAVID_GRIEVED | 4 fortress | 6 altar", face="DAVID")
        + psalm(55, "1 DAVID_OLD_WEEP | 6 dove | 9 city | 12 DAVID_OLD | 16 dawn | 18 war | 20 DAVID_OLD | 22 fortress", face="DAVID_OLD")
        + psalm(56, "1 DAVID_GRIEVED | 5 net | 8 DAVID_GRIEVED | 10 path | 12 altar", face="DAVID")
        + psalm(57, "1 cave | 4 lions | 6 net | 7 music | 9 heavens", face="DAVID")
        + psalm(58, "1 city | 4 serpent | 6 lions | 7 waves | 9 fire | 10 glory")
        + psalm(59, "1 DAVID_BOLD | 3 bow | 6 dogs | 8 fortress | 11 DAVID_BOLD | 14 dogs | 16 dawn", face="DAVID")
        + psalm(60, "1 storm | 4 banners | 6 lands | 9 fortress | 11 war", god={"60:6": "I will exult;", "60:7": None, "60:8": None})
        + psalm(61, "1 rock | 4 tent | 6 throne")
        + psalm(62, "1 fortress | 3 wall | 5 fortress | 9 riches | 11 glory"))
PG.extend(pack(SEGS, "PS-C06-D", PG.next(), end=end_mark("NEXT · LET GOD ARISE", "right: 10px; bottom: 34px")))
