"""Psalms volume, Chapter 3 — Jehovah Is My Shepherd (Psalms 23–33). Every verse, word for word from ref/asv.
The shepherd, the still waters, the valley of the shadow of death and the table spread; the earth is Jehovah's — lift up
your heads, O ye gates; the paths and the net; I will wash my hands in innocency; Jehovah is my light; the voice of
Jehovah upon the waters and in the cedars of Lebanon (God never drawn: storm, flame and flood); joy cometh in the morning,
and mourning turned into dancing; into thy hand I commend my spirit — like a broken vessel; blessed is he whose
transgression is forgiven; and a new song with the harp of ten strings."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from num.pages import Pages
from psa import G
from psa.common import pack, psalm, end_mark, chapter_open
from psa import ch02 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PS-C03-00-Title", "Chapter 3 · Jehovah Is My Shepherd", title=True)
def title(n):
    return chapter_open(3, "Jehovah Is My Shepherd", "Psalms 23 – 33", "pasture", v("23:1") + " " + v("23:2"), seed=3001)


SEGS = (psalm(23, "1 pasture | 4 valley | 5 table")
        + psalm(24, "1 earth | 3 zion | 7 gates")
        + psalm(25, "1 DAVID_KING | 4 path | 8 DAVID_KING | 12 land | 15 net | 16 DAVID_GRIEF")
        + psalm(26, "1 DAVID_KING | 6 altar | 9 path")
        + psalm(27, "1 lamp | 3 camp | 4 tent | 7 DAVID_GRIEF | 11 path | 13 dawn")
        + psalm(28, "1 pit | 3 city | 6 fortress | 9 pasture")
        + psalm(29, "1 glory | 3 storm | 5 cedars | 7 storm | 9 cedars | 10 sea")
        + psalm(30, "1 pit | 4 dawn | 6 fortress | 8 DAVID_KING | 11 dance")
        + psalm(31, "1 fortress | 4 net | 6 DAVID_KING | 9 DAVID_GRIEF | 12 potsherd | 14 DAVID_KING | 19 tent | 21 city | 23 DAVID_KING")
        + psalm(32, "1 DAVID_KING | 3 drought | 6 waves | 8 path | 9 horse | 10 dawn")
        + psalm(33, "1 music | 4 heavens | 7 sea | 10 nations | 13 glory | 16 war | 18 LEVITE"))
PG.extend(pack(SEGS, "PS-C03-D", PG.next(), end=end_mark("NEXT · WAIT FOR JEHOVAH", "right: 10px; bottom: 34px")))
