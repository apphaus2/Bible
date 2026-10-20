"""Psalms volume, Chapter 9 — Whom Have I in Heaven (Psalms 73–78), the opening of Book III: the psalms of Asaph (a Levite
singer in white, grey-bearded). Every verse, word for word from ref/eng-asv. The prosperity of the wicked until I went into the
sanctuary — whom have I in heaven but thee?; the sanctuary burned and the sea divided; the cup in the hand of Jehovah (God's
words in the Voice box); the arrows and the shield broken, chariot and horse in a dead sleep; I remember the works of
Jehovah — the waters saw thee; and Psalm 78, the dark sayings of old: the sea divided, the cloud by day and the fire by
night, the rock cleft, manna and quails, the wonders in the field of Zoan, the tabernacle of Shiloh forsaken, and David
taken from the sheepfolds (the slain told in words over the empty camp and the smoke)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from num.pages import Pages
from psa import G
from psa.common import pack, psalm, end_mark, chapter_open
from psa import ch08 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PS-C09-00-Title", "Chapter 9 · Whom Have I in Heaven", title=True)
def title(n):
    return chapter_open(9, "Whom Have I in Heaven", "Psalms 73 – 78", "heavens", v("73:25"), seed=9001)


SEGS = (psalm(73, "1 ASAPH | 3 riches | 13 ASAPH_GRIEF | 17 court | 18 smoke | 21 ASAPH_GRIEF | 23 path | 25 heavens", face="ASAPH")
        + psalm(74, "1 ASAPH_GRIEF | 3 ruins | 9 ASAPH_GRIEF | 12 sea | 15 brook | 16 sun | 17 earth | 18 dove | 20 dark | 22 ASAPH_STERN", face="ASAPH_GRIEF")
        + psalm(75, "1 ASAPH | 2 glory | 6 ASAPH | 8 table | 9 music", god={f"75:{x}": None for x in range(2, 6)})
        + psalm(76, "1 zion | 3 broken | 5 silent | 7 glory | 8 storm | 11 tribute")
        + psalm(77, "1 night | 4 ASAPH_GRIEF | 10 ASAPH | 13 glory | 16 waves | 17 storm | 19 redsea | 20 flock", face="ASAPH_GRIEF")
        + psalm(78, "1 ASAPH | 5 scroll | 9 war | 12 egypt | 13 redsea | 14 wilderness | 15 rockwater | 17 desert | 19 table | 21 fire | 23 manna | 26 quails "
                    "| 30 silent | 32 ASAPH_GRIEF | 40 desert | 43 egypt | 44 blood | 46 locusts | 47 hail | 49 darkness | 52 flock | 54 land | 56 ASAPH_STERN | 58 idols | 60 tent | 61 ark "
                    "| 62 smoke | 65 dawn | 67 zion | 69 court | 70 pasture"))
PG.extend(pack(SEGS, "PS-C09-D", PG.next(), end=end_mark("NEXT · HOW AMIABLE ARE THY TABERNACLES", "right: 10px; bottom: 34px")))
