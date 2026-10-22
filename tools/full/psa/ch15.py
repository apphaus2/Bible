"""Psalms volume, Chapter 15 — Thy Word Is a Lamp (Psalm 119). Every verse, word for word from ref/eng-asv. The twenty-two
sections of the acrostic, eight verses to each Hebrew letter, every section opening under its letter's head (א ALEPH comes
from the line before verse 1; the other heads close verses 8, 16 … 168 in ref/eng-asv and are cut from those verses), the
verses over the way and the path, the book of the law by lamplight, the honey, the furnace and the dross, the watch before
the dawning of the morning, the great spoil, and the sheep gone astray — or beside the psalmist's face (a Levite singer,
the psalm names no one)."""
import sys, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from num.pages import Pages
from psa import G
from psa.common import pack, psalm, end_mark, chapter_open, ALEPH, HEADS
from psa import ch14 as _prev
import asv

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PS-C15-00-Title", "Chapter 15 · Thy Word Is a Lamp", title=True)
def title(n):
    return chapter_open(15, "Thy Word Is a Lamp", "Psalm 119", "lamp", v("119:105"), seed=15001)


PLANS = ["1 path | 5 LEVITE", "9 LEVITE_JOY | 13 scroll", "17 harvest | 19 tents | 23 judges", "25 LEVITE_GRIEF | 29 path", "33 path | 37 LEVITE",
         "41 LEVITE | 45 large | 46 kings", "49 LEVITE_GRIEF | 53 fire | 55 night", "57 land | 61 net | 62 night | 64 earth", "65 LEVITE | 69 LEVITE_GRIEF | 72 riches",
         "73 LEVITE | 77 path", "81 LEVITE_GRIEF | 83 smoke | 85 pit", "89 heavens | 90 earth | 93 LEVITE | 96 sea", "97 scroll | 101 path | 103 honey",
         "105 lamp | 107 LEVITE_GRIEF | 110 net | 111 land", "113 LEVITE | 117 fortress | 119 furnace", "121 judges | 123 dawn | 127 riches",
         "129 lamp | 131 hart | 135 glory | 136 LEVITE_GRIEF", "137 judges | 139 fire | 141 LEVITE_GRIEF | 144 scroll", "145 night | 147 dawn | 148 watch | 150 LEVITE",
         "153 LEVITE_GRIEF | 155 city | 157 LEVITE | 160 scroll", "161 kings | 162 riches | 164 music | 165 river", "169 LEVITE | 173 harvest | 176 flock"]

SEGS = []
for k, plan in enumerate(PLANS):
    a = k * 8 + 1
    if k == 0:
        letter = ALEPH                                         # a label: the line before verse 1 is no verse
        heads = [(119, None, None), (letter.rstrip("."), None, None)]
    elif (119, a) in HEADS:                                    # a translation's own head before verse a: a label
        letter = re.search(r"[א-ת]", G.verses[(119, a - 1)]).group(0) + " " + HEADS[(119, a)]
        heads = [(letter, None, None)]
    else:
        t = G.verses[(119, a - 1)]; i = re.search(r"[א-ת]", t).start()
        letter = v(f"119:{a - 1}", frm=t[i]) if asv.LANG == "en" else t[i:]   # "ב BETH." closes verse a-1 (a label in a translation)
        heads = [(letter.rstrip("."), None, None)]
    name = letter.split()[-1].rstrip(".").title()
    SEGS += psalm(119, plan, start=a, upto=a + 7, head=heads, title=f"Psalm 119 · {name}", face="LEVITE")
PG.extend(pack(SEGS, "PS-C15-D", PG.next(), brk=0.45, end=end_mark("NEXT · I WILL LIFT UP MINE EYES", "right: 10px; bottom: 34px")))
