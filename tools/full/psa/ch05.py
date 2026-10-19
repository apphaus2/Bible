"""Psalms volume, Chapter 5 — As the Hart Panteth (Psalms 42–50), the opening of Book II. Every verse, word for word from
ref/asv. The sons of Korah (Levite singers in white): the hart at the water brooks, deep calling unto deep; send out thy
light and thy truth; we are accounted as sheep for the slaughter; the king's wedding song — the queen in gold of Ophir; God
is our refuge and strength, the river that maketh glad the city of God — be still, and know that I am God (the Voice box);
God is gone up with a shout; walk about Zion; the riches that cannot redeem and the graves that are their houses; and
Asaph's psalm of judgment, the Mighty One calling the earth (God's words in the Voice box: the cattle upon a thousand hills,
offer unto God the sacrifice of thanksgiving)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from num.pages import Pages
from psa import G
from psa.common import pack, psalm, end_mark, chapter_open
from psa import ch04 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
GOD50 = {"50:5": None, **{f"50:{x}": None for x in range(7, 16)}, "50:16": "What hast thou", **{f"50:{x}": None for x in range(17, 24)}}


@P("PS-C05-00-Title", "Chapter 5 · As the Hart Panteth", title=True)
def title(n):
    return chapter_open(5, "As the Hart Panteth", "Psalms 42 – 50", "hart", v("42:1"), seed=5002)


SEGS = (psalm(42, "1 hart | 3 KORAH_GRIEF | 6 mountains | 7 waves | 8 night | 9 KORAH_GRIEF", face="KORAH_GRIEF")
        + psalm(43, "1 KORAH_GRIEF | 3 zion", face="KORAH")
        + psalm(44, "1 KORAH | 2 vine | 4 war | 9 KORAH_GRIEF | 11 flock | 13 city | 17 KORAH_GRIEF | 22 flock | 23 dawn", face="KORAH_GRIEF")
        + psalm(45, "1 KORAH | 2 throne | 3 war | 6 throne | 8 bride | 16 KORAH")
        + psalm(46, "1 waves | 4 river | 6 nations | 8 broken | 10 glory | 11 fortress", god={"46:10": None})
        + psalm(47, "1 trumpets | 5 music | 8 nations")
        + psalm(48, "1 zion | 4 kings | 7 tempest | 8 court | 12 zion")
        + psalm(49, "1 KORAH | 5 riches | 10 tomb | 13 flock | 16 riches | 19 tomb")
        + psalm(50, "1 sun | 3 storm | 4 glory | 5 altar | 7 ASAPH | 10 creation | 12 harvest | 14 altar | 16 ASAPH_STERN | 18 city | 21 ASAPH", god=GOD50))
PG.extend(pack(SEGS, "PS-C05-D", PG.next(), end=end_mark("NEXT · A CLEAN HEART", "right: 10px; bottom: 34px")))
