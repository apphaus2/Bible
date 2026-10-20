"""Psalms volume, Chapter 17 — Praise Ye Jehovah (Psalms 138–150), the last chapter of Psalms. Every verse, word for word
from ref/eng-asv. I will give thee thanks with my whole heart; O Jehovah, thou hast searched me — the wings of the morning, the
darkness and the light both alike, fearfully and wonderfully made; the adder's poison and the snare; let my prayer be set
forth as incense; in the cave, I cried unto thee (David's face throughout); hear my prayer — the land of darkness; blessed
be Jehovah my rock, sons as plants and daughters as corner-stones; then the last hallelujahs — every day will I bless thee,
put not your trust in princes, he healeth the broken in heart and giveth snow like wool, praise ye him sun and moon, fire
and hail, a new song with timbrel and harp; and let every thing that hath breath praise Jehovah (完)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from num.pages import Pages
from psa import G
from psa.common import pack, psalm, end_mark, chapter_open
from psa import ch16 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PS-C17-00-Title", "Chapter 17 · Praise Ye Jehovah", title=True)
def title(n):
    return chapter_open(17, "Praise Ye Jehovah", "Psalms 138 – 150", "finale", v("150:6", to="praise Jehovah."), seed=17001)


SEGS = (psalm(138, "1 court | 4 kings | 6 glory | 7 DAVID_KING")
        + psalm(139, "1 DAVID_OLD | 7 heavens | 9 dawn | 11 dark | 13 child | 17 DAVID_OLD | 19 DAVID_WRATH | 23 path", face="DAVID_OLD")
        + psalm(140, "1 DAVID_GRIEVED | 3 serpent | 5 net | 6 DAVID_KING | 9 fire | 12 tent")
        + psalm(141, "1 altar | 3 DAVID_KING | 6 rock | 7 tomb | 8 net")
        + psalm(142, "1 cave | 4 DAVID_GRIEVED | 6 prison")
        + psalm(143, "1 DAVID_OLD | 3 dark | 5 desert | 7 dawn | 9 fortress | 10 path | 11 DAVID_OLD", face="DAVID_OLD")
        + psalm(144, "1 fortress | 3 mist | 5 storm | 7 waves | 9 music | 10 war | 12 family | 13 flock | 15 zion")
        + psalm(145, "1 DAVID_KING | 4 music | 8 glory | 10 throne | 14 harvest | 17 DAVID_KING | 21 music")
        + psalm(146, "1 music | 3 tomb | 5 creation | 7 prison | 9 family | 10 zion")
        + psalm(147, "1 zion | 4 heavens | 7 rain | 9 birds | 10 horse | 12 gates | 14 harvest | 15 snow | 18 brook | 19 scroll")
        + psalm(148, "1 heavens | 5 earth | 7 snow | 9 creation | 11 kings")
        + psalm(149, "1 music | 3 dance | 6 banners"))
PG.extend(pack(SEGS, "PS-C17-D", PG.next()))
PG.extend(pack(psalm(150, "1 court | 3 finale"), "PS-C17-E", PG.next(), end=end_mark("END OF PSALMS · NEXT · PROVERBS", "right: 10px; bottom: 34px", ch="完")))
