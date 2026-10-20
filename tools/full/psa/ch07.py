"""Psalms volume, Chapter 7 — Let God Arise (Psalms 63–68). Every verse, word for word from ref/eng-asv.
David in the wilderness of Judah — my soul thirsteth for thee in a dry and weary land; the bow bent in secret; praise
waiteth for thee in Zion — the river of God, the rain, the pastures clothed with flocks; he turned the sea into dry land;
God be merciful unto us, and bless us; and Psalm 68: let God arise, as smoke is driven away, Sinai moved, the chariots of
God, the singers and the damsels with timbrels (68:21–23 told in words over the deep; the Lord's word in 68:22 in the
Voice box; God never drawn)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from num.pages import Pages
from psa import G
from psa.common import pack, psalm, end_mark, chapter_open
from psa import ch06 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PS-C07-00-Title", "Chapter 7 · Let God Arise", title=True)
def title(n):
    return chapter_open(7, "Let God Arise", "Psalms 63 – 68", "smoke", v("68:1") + " " + v("68:2", to="drive them away:"), seed=7001)


SEGS = (psalm(63, "1 desert | 3 DAVID | 6 night | 7 wings | 9 DAVID_BOLD", face="DAVID")
        + psalm(64, "1 DAVID_GRIEVED | 3 bow | 9 dawn")
        + psalm(65, "1 court | 5 sea | 8 dawn | 9 rain | 11 harvest | 12 pasture")
        + psalm(66, "1 music | 5 redsea | 8 furnace | 11 net | 13 altar | 16 LEVITE_JOY")
        + psalm(67, "1 glory | 3 nations | 6 harvest")
        + psalm(68, "1 smoke | 4 desert | 5 family | 7 wilderness | 8 sinai | 9 rain | 11 trumpets | 12 kings | 15 mountains | 17 war | 18 glory | 19 DAVID_KING "
                    "| 21 waves | 24 music | 28 court | 30 bulls | 31 nations | 32 heavens | 35 zion", god={"68:22": "I will bring again"}))
PG.extend(pack(SEGS, "PS-C07-D", PG.next(), end=end_mark("NEXT · HE SHALL HAVE DOMINION", "right: 10px; bottom: 34px")))
