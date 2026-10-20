"""Psalms volume, Chapter 10 — How Amiable Are Thy Tabernacles (Psalms 79–89), the close of Book III. Every verse, word for
word from ref/eng-asv. Jerusalem laid on heaps (words over the ruins and the captives); the Shepherd of Israel and the vine out
of Egypt; the trumpet at the new moon and God's word from the secret place of thunder (81:6–16 in the Voice box); God in
the congregation of the judges (82:2–7 in the Voice box); the nations confederate (a map); how amiable are thy
tabernacles — the sparrow and the swallow at thine altars; mercy and truth are met together; glorious things of Zion;
Heman's psalm from the lowest pit; and Ethan's psalm of the covenant with David (God's oath in the Voice box) and its
lament."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from num.pages import Pages
from psa import G
from psa.common import pack, psalm, end_mark, chapter_open
from psa import ch09 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
GOD89 = {"89:3": None, "89:4": None, "89:19": "I have laid help", **{f"89:{x}": None for x in range(20, 38)}}


@P("PS-C10-00-Title", "Chapter 10 · How Amiable Are Thy Tabernacles", title=True)
def title(n):
    return chapter_open(10, "How Amiable Are Thy Tabernacles", "Psalms 79 – 89", "nest", v("84:1"), seed=10001)


SEGS = (psalm(79, "1 ruins | 5 ASAPH_GRIEF | 11 captives | 13 flock", face="ASAPH_GRIEF")
        + psalm(80, "1 flock | 3 glory | 4 ASAPH_GRIEF | 8 vine | 12 wall | 14 vine | 17 ASAPH", face="ASAPH_GRIEF")
        + psalm(81, "1 trumpets | 4 egypt | 6 ASAPH | 7 storm | 8 ASAPH | 10 egypt | 11 desert | 13 path | 16 honey", god={f"81:{x}": None for x in range(6, 17)})
        + psalm(82, "1 judges | 2 ASAPH_STERN | 8 nations", god={f"82:{x}": None for x in range(2, 8)})
        + psalm(83, "1 ASAPH | 2 kings | 6 confed | 9 war | 13 chaff | 14 fire | 15 storm | 16 ASAPH")
        + psalm(84, "1 court | 3 nest | 5 path | 6 brook | 8 KORAH | 10 gates | 11 sun")
        + psalm(85, "1 land | 4 KORAH_GRIEF | 8 KORAH | 10 glory | 11 harvest | 13 path")
        + psalm(86, "1 DAVID_KING | 8 nations | 11 path | 14 DAVID_GRIEF | 16 DAVID_KING")
        + psalm(87, "1 zion | 4 nations | 7 music", god={"87:4": None})
        + psalm(88, "1 HEMAN | 3 pit | 6 waves | 8 HEMAN | 10 tomb | 13 dawn | 14 HEMAN | 16 waves | 18 dark", face="HEMAN")
        + psalm(89, "1 ETHAN | 3 throne | 5 heavens | 9 sea | 11 mountains | 13 glory | 15 music | 19 throne | 22 war | 25 sea | 27 crown | 30 scroll "
                    "| 34 sun | 38 ETHAN_GRIEF | 40 wall | 43 broken | 45 ETHAN_GRIEF | 47 mist | 52 music", god=GOD89, face="ETHAN"))
PG.extend(pack(SEGS, "PS-C10-D", PG.next(), end=end_mark("NEXT · BOOK IV · OUR DWELLING-PLACE", "right: 10px; bottom: 34px")))
