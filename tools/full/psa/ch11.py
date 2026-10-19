"""Psalms volume, Chapter 11 — Our Dwelling-place (Psalms 90–100), the opening of Book IV. Every verse, word for word from
ref/asv. The prayer of Moses the man of God (his face from Deuteronomy): before the mountains were brought forth — a
thousand years as yesterday, man as the grass; he that dwelleth in the secret place of the Most High — the snare of the
fowler, the terror by night, the angels' hands (God's answer in the Voice box); the palm-tree and the cedar; the floods
have lifted up their voice; the God to whom vengeance belongeth; oh come, let us sing — to-day, oh that ye would hear his
voice (95:8–11 in the Voice box); sing unto Jehovah a new song, let the sea roar and the trees of the wood sing; Jehovah
reigneth, clouds and darkness are round about him (God never drawn); he sitteth above the cherubim; and make a joyful noise
unto Jehovah, all ye lands."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from num.pages import Pages
from psa import G
from psa.common import pack, psalm, end_mark, chapter_open
from psa import ch10 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PS-C11-00-Title", "Chapter 11 · Our Dwelling-place", title=True)
def title(n):
    return chapter_open(11, "Our Dwelling-place", "Psalms 90 – 100", "mountains", v("90:1") + " " + v("90:2"), seed=11001)


SEGS = (psalm(90, "1 mountains | 3 MOSES | 5 grass | 7 MOSES_GRIEF | 10 mist | 12 MOSES | 14 dawn | 16 harvest", face="MOSES")
        + psalm(91, "1 wings | 3 snare | 5 bow | 7 silent | 9 tent | 11 path | 13 lions | 14 glory", god={"91:14": None, "91:15": None, "91:16": None})
        + psalm(92, "1 music | 4 harvest | 5 heavens | 7 grass | 9 broken | 10 olive | 12 cedars | 14 olive")
        + psalm(93, "1 glory | 3 waves")
        + psalm(94, "1 glory | 3 city | 8 LEVITE | 12 scroll | 16 LEVITE_GRIEF | 20 judges | 22 fortress")
        + psalm(95, "1 music | 3 mountains | 5 sea | 6 flock | 8 desert", god={f"95:{x}": None for x in range(8, 12)})
        + psalm(96, "1 music | 4 idols | 6 court | 9 earth | 11 sea | 12 cedars | 13 glory")
        + psalm(97, "1 storm | 3 fire | 5 mountains | 7 idols | 8 zion | 10 dawn")
        + psalm(98, "1 music | 4 trumpets | 7 sea")
        + psalm(99, "1 ark | 4 judges | 6 wilderness | 8 altar | 9 zion")
        + psalm(100, "1 pasture | 4 gates"))
PG.extend(pack(SEGS, "PS-C11-D", PG.next(), end=end_mark("NEXT · BLESS JEHOVAH, O MY SOUL", "right: 10px; bottom: 34px")))
