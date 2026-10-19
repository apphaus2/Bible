"""Psalms volume, Chapter 16 — I Will Lift Up Mine Eyes (Psalms 120–137). Every verse, word for word from ref/asv. The
fifteen Songs of Ascents — the tents of Kedar; I will lift up mine eyes unto the mountains; our feet are standing within thy
gates, O Jerusalem; the snare is broken; as the mountains are round about Jerusalem; they that sow in tears shall reap in
joy; except Jehovah build the house, the watchman and the arrows; the olive plants round about thy table; the plowers;
out of the depths — more than watchmen wait for the morning; a weaned child; David and the ark (God's oath in the Voice box);
how good and how pleasant — the oil and the dew of Hermon; the servants by night in the house of Jehovah — then the two
hallelujahs, his lovingkindness endureth for ever (twenty-six times), and by the rivers of Babylon, the harps on the
willows (137:7–9 told in words over the bare crag)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from num.pages import Pages
from psa import G
from psa.common import pack, psalm, end_mark, chapter_open
from psa import ch15 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PS-C16-00-Title", "Chapter 16 · I Will Lift Up Mine Eyes", title=True)
def title(n):
    return chapter_open(16, "I Will Lift Up Mine Eyes", "Psalms 120 – 137", "lift", v("121:1") + " " + v("121:2"), seed=16001)


SEGS = (psalm(120, "1 LEVITE_GRIEF | 3 bow | 5 tents")
        + psalm(121, "1 lift | 3 night | 5 sun | 7 path")
        + psalm(122, "1 gates | 3 zion | 6 court")
        + psalm(123, "1 LEVITE | 3 LEVITE_GRIEF")
        + psalm(124, "1 waves | 6 lions | 7 snare | 8 glory")
        + psalm(125, "1 zion | 3 path")
        + psalm(126, "1 dance | 4 oasis | 5 harvest")
        + psalm(127, "1 corner | 2 night | 3 family")
        + psalm(128, "1 plow | 3 family | 5 zion")
        + psalm(129, "1 LEVITE | 3 plow | 5 grass")
        + psalm(130, "1 waves | 3 LEVITE_GRIEF | 5 watch | 7 dawn")
        + psalm(131, "1 child")
        + psalm(132, "1 DAVID_KING | 6 ark | 9 court | 11 throne | 13 zion | 17 lamp", god={f"132:{x}": None for x in range(14, 19)} | {"132:11": "Of the fruit"})
        + psalm(133, "1 family | 2 altar | 3 hermon")
        + psalm(134, "1 templenight")
        + psalm(135, "1 court | 5 storm | 8 egypt | 10 kings | 12 land | 14 LEVITE | 15 idols | 19 music")
        + psalm(136, "1 music | 4 heavens | 6 earth | 7 sun | 9 moonnight | 10 darkness | 11 going | 13 redsea | 15 waves | 16 wilderness | 17 kings | 21 land | 23 LEVITE "
                     "| 25 harvest | 26 glory")
        + psalm(137, "1 willows | 4 EXILE | 7 ruins | 8 crag", face="EXILE"))
PG.extend(pack(SEGS, "PS-C16-D", PG.next(), end=end_mark("NEXT · PRAISE YE JEHOVAH", "right: 10px; bottom: 34px")))
