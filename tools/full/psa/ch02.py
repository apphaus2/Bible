"""Psalms volume, Chapter 2 — The Heavens Declare (Psalms 13–22). Every verse, word for word from ref/eng-asv.
How long, O Jehovah?; the fool hath said in his heart; who shall dwell in thy holy hill?; the lines fallen in pleasant
places and the path of life; the shadow of thy wings; David's song in the day of his deliverance (Psalm 18: the cords of
death, the earth shaking and the storm, the large place, the lamp, the hinds' feet — God never drawn, only storm and
light); the heavens declare the glory of God and the sun as a bridegroom; the banners and the chariots; the crown of fine
gold; and Psalm 22 — my God, my God, why hast thou forsaken me? — the bulls, the dogs, the garments parted by lot, told
in faces and beasts, and the ends of the earth turning unto Jehovah."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from num.pages import Pages
from psa import G
from psa.common import pack, psalm, end_mark, chapter_open
from psa import ch01 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PS-C02-00-Title", "Chapter 2 · The Heavens Declare", title=True)
def title(n):
    return chapter_open(2, "The Heavens Declare", "Psalms 13 – 22", "heavens", v("19:1"))


SEGS = (psalm(13, "1 DAVID_GRIEF | 3 dawn", face="DAVID_GRIEF")
        + psalm(14, "1 city | 2 glory | 5 zion")
        + psalm(15, "1 tent | 3 DAVID_KING")
        + psalm(16, "1 DAVID_KING | 5 land | 8 path")
        + psalm(17, "1 DAVID | 6 wings | 9 lions | 13 DAVID_BOLD | 15 dawn", face="DAVID")
        + psalm(18, "1 fortress | 4 waves | 7 storm | 16 large | 20 DAVID_KING | 28 lamp | 31 fortress | 33 hinds | 37 war | 43 nations | 46 DAVID_JOY")
        + psalm(19, "1 heavens | 4 sun | 7 scroll | 10 honey | 12 DAVID_KING")
        + psalm(20, "1 altar | 5 banners | 7 war")
        + psalm(21, "1 crown | 5 throne | 8 fire | 11 bow | 13 music")
        + psalm(22, "1 DAVID_GRIEF | 3 night | 6 DAVID_MOURN | 12 bulls | 14 DAVID_GRIEF | 16 dogs | 18 lots | 19 lions | 22 court | 27 nations", face="DAVID_GRIEF"))
PG.extend(pack(SEGS, "PS-C02-D", PG.next(), end=end_mark("NEXT · JEHOVAH IS MY SHEPHERD", "right: 10px; bottom: 34px")))
