"""Psalms volume, Chapter 8 — He Shall Have Dominion (Psalms 69–72), the close of Book II. Every verse, word for word from
ref/asv. Save me, O God, for the waters are come in unto my soul — the deep mire and the floods, the reproach, gall for
meat and vinegar to drink (told in faces and a bare table); make haste to help me; the old man's psalm — now also when I
am old and grayheaded, O God, forsake me not; and Solomon's psalm of the king: he shall come down like rain upon the mown
grass, he shall have dominion from sea to sea, the kings of Tarshish and of Sheba bringing gifts — and the prayers of David
the son of Jesse are ended."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from num.pages import Pages
from psa import G
from psa.common import pack, psalm, end_mark, chapter_open
from psa import ch07 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PS-C08-00-Title", "Chapter 8 · He Shall Have Dominion", title=True)
def title(n):
    return chapter_open(8, "He Shall Have Dominion", "Psalms 69 – 72", "rain", v("72:6"), seed=8001)


SEGS = (psalm(69, "1 waves | 3 DAVID_GRIEF | 13 pit | 16 DAVID_GRIEF | 21 table | 22 net | 26 DAVID_WRATH | 29 music | 34 earth | 35 zion", face="DAVID_GRIEF")
        + psalm(70, "1 DAVID_GRIEF | 4 dawn")
        + psalm(71, "1 fortress | 4 DAVID_OLD | 14 path | 17 DAVID_OLD | 19 heavens | 20 pit | 22 music", face="DAVID_OLD")
        + psalm(72, "1 throne | 3 mountains | 5 sun | 6 rain | 8 nations | 10 tribute | 12 SOLOMON_WISE | 15 riches | 16 harvest | 17 sun | 18 music", face="SOLOMON_WISE"))
PG.extend(pack(SEGS, "PS-C08-D", PG.next(), end=end_mark("NEXT · BOOK III · WHOM HAVE I IN HEAVEN", "right: 10px; bottom: 34px")))
