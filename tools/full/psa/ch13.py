"""Psalms volume, Chapter 13 — He Remembered His Covenant (Psalms 105–106), the close of Book IV. Every verse, word for word
from ref/eng-asv. Psalm 105: the covenant with Abraham, Isaac and Jacob (God's words in the Voice box), the few sojourners and
their tents, Joseph sold and laid in chains of iron, Israel in the land of Ham, the signs and wonders (darkness, blood,
frogs, flies, hail, locusts; the first-born told in words over the dark), the going out with silver and gold, the cloud,
the quails and the rock; and Psalm 106's confession — the Red Sea, the lust in the wilderness, the calf in Horeb,
Baal-peor (106:37–38 told in words over the idols and the smoke), and blessed be Jehovah, the God of Israel."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from num.pages import Pages
from psa import G
from psa.common import pack, psalm, end_mark, chapter_open
from psa import ch12 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PS-C13-00-Title", "Chapter 13 · He Remembered His Covenant", title=True)
def title(n):
    return chapter_open(13, "He Remembered His Covenant", "Psalms 105 – 106", "going", v("105:8"), seed=13001)


SEGS = (psalm(105, "1 music | 6 LEVITE | 8 scroll | 11 land | 12 tents | 15 LEVITE | 16 drought | 17 prison | 20 egypt | 26 LEVITE | 28 darkness | 29 blood | 31 locusts "
                     "| 32 hail | 34 locusts | 36 darkness | 37 going | 39 wilderness | 40 quails | 41 rockwater | 42 land | 45 music", god={"105:11": "Unto thee", "105:15": "Touch not"})
        + psalm(106, "1 music | 4 LEVITE | 6 LEVITE_GRIEF | 7 egypt | 9 redsea | 11 waves | 13 desert | 14 quails | 16 wilderness | 17 fire | 19 calf | 23 wilderness | 24 land "
                     "| 26 desert | 28 idols | 30 tent | 32 rockwater | 34 land | 36 idols | 38 smoke | 40 LEVITE_GRIEF | 41 captives | 44 LEVITE | 47 nations | 48 music"))
PG.extend(pack(SEGS, "PS-C13-D", PG.next(), end=end_mark("NEXT · BOOK V · THEY THAT GO DOWN TO THE SEA", "right: 10px; bottom: 34px")))
