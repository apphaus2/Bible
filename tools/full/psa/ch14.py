"""Psalms volume, Chapter 14 — They That Go Down to the Sea (Psalms 107–118), the opening of Book V. Every verse, word for
word from ref/asv. The redeemed of Jehovah — the wanderers in the desert way, the prisoners in darkness and iron, the sick at
the gates of death, they that go down to the sea in ships and the storm made a calm, the wilderness turned into pools;
awake, psaltery and harp; Psalm 109's curses (words over the bare plain, the locust and the shadow; no one drawn); Jehovah
saith unto my Lord, Sit thou at my right hand (the Voice box); the righteous man and the barren woman made a joyful mother;
when Israel went forth out of Egypt — the sea fled, the mountains skipped like rams; idols that have mouths and speak not;
I love Jehovah, because he heareth my voice; the shortest psalm; and Psalm 118 — the gates of righteousness and the stone
which the builders rejected."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from num.pages import Pages
from psa import G
from psa.common import pack, psalm, end_mark, chapter_open
from psa import ch13 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PS-C14-00-Title", "Chapter 14 · They That Go Down to the Sea", title=True)
def title(n):
    return chapter_open(14, "They That Go Down to the Sea", "Psalms 107 – 118", "tempest", v("107:23") + " " + v("107:24"), seed=14001)


SEGS = (psalm(107, "1 music | 2 nations | 4 desert | 7 path | 9 harvest | 10 prison | 16 gates | 17 sickbed | 21 altar | 23 ships | 25 tempest | 29 haven | 31 court "
                   "| 33 drought | 35 oasis | 37 vine | 39 captives | 41 family | 42 LEVITE")
        + psalm(108, "1 music | 3 heavens | 6 lands | 10 fortress | 12 war", god={"108:7": "I will exult;", "108:8": None, "108:9": None})
        + psalm(109, "1 DAVID_OLD_ALARM | 6 judges | 9 drought | 13 smoke | 16 DAVID_WRATH | 20 DAVID_GRIEF | 23 locusts | 24 DAVID_GRIEF | 30 dawn", face="DAVID_OLD")
        + psalm(110, "1 throne | 3 dawn | 4 altar | 5 broken | 7 brook", god={"110:1": "Sit thou", "110:4": "Thou art a priest"})
        + psalm(111, "1 court | 4 manna | 7 scroll | 9 glory")
        + psalm(112, "1 family | 4 lamp | 6 tree | 9 harvest | 10 smoke")
        + psalm(113, "1 sun | 4 heavens | 7 throne | 9 family")
        + psalm(114, "1 going | 3 redsea | 4 skip | 7 rockwater")
        + psalm(115, "1 glory | 4 idols | 9 court | 12 family | 16 heavens | 17 tomb | 18 music")
        + psalm(116, "1 LEVITE | 3 pit | 5 LEVITE_JOY | 8 path | 10 LEVITE | 12 altar | 15 LEVITE | 17 court")
        + psalm(117, "1 nations")
        + psalm(118, "1 music | 5 large | 8 fortress | 10 bees | 13 fortress | 15 tents | 17 LEVITE_JOY | 19 gates | 22 corner | 24 dawn | 25 court | 27 altar | 28 music"))
PG.extend(pack(SEGS, "PS-C14-D", PG.next(), end=end_mark("NEXT · THY WORD IS A LAMP", "right: 10px; bottom: 34px")))
