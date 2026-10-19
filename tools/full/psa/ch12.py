"""Psalms volume, Chapter 12 — Bless Jehovah, O My Soul (Psalms 101–104). Every verse, word for word
from ref/asv. I will sing of lovingkindness and justice; the prayer of the afflicted — the pelican of the wilderness, the
sparrow alone upon the housetop; bless Jehovah, O my soul — thy youth renewed like the eagle, as a father pitieth his
children, man's days as grass; Psalm 104's creation — light as a garment, the springs in the valleys, the birds among the
branches, the wild goats and the conies, the moon for seasons, the young lions at night, man going forth to his labor,
and the great and wide sea and leviathan."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from num.pages import Pages
from psa import G
from psa.common import pack, psalm, end_mark, chapter_open
from psa import ch11 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PS-C12-00-Title", "Chapter 12 · Bless Jehovah, O My Soul", title=True)
def title(n):
    return chapter_open(12, "Bless Jehovah, O My Soul", "Psalms 101 – 104", "creatures", v("104:24"), seed=12001)


SEGS = (psalm(101, "1 DAVID_KING | 3 DAVID_WRATH | 6 land")
        + psalm(102, "1 LEVITE_GRIEF | 3 smoke | 4 grass | 6 housetop | 8 LEVITE_GRIEF | 11 mist | 12 zion | 18 scroll | 19 glory | 21 zion | 23 LEVITE_GRIEF | 25 earth "
                     "| 26 mist | 28 family", face="LEVITE_GRIEF")
        + psalm(103, "1 DAVID_KING | 3 dawn | 5 wings | 6 wilderness | 8 DAVID_KING | 11 heavens | 12 sun | 13 family | 14 grass | 17 DAVID_KING | 19 glory | 22 music")
        + psalm(104, "1 glory | 3 storm | 5 earth | 6 waves | 10 brook | 12 birds | 14 harvest | 16 cedars | 18 goats | 19 moonnight | 21 lions | 23 plow | 24 creation "
                     "| 25 creatures | 27 harvest | 29 mist | 30 dawn | 31 glory | 32 sinai | 33 music | 35 LEVITE"))
PG.extend(pack(SEGS, "PS-C12-D", PG.next(), end=end_mark("NEXT · HE REMEMBERED HIS COVENANT", "right: 10px; bottom: 34px")))
