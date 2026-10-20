"""Ezra volume, Chapter 5 — The Strange Wives (Ezra 9–10), the last chapter of Ezra. Every verse, word for word from ref/eng-asv.
The princes' report — the holy seed have mingled themselves with the peoples of the lands; Ezra rends his garment and sits
confounded until the evening oblation (his face); his prayer on his knees — O my God, I am ashamed and blush to lift up my face
to thee; a nail in his holy place; the great assembly weeping; Shecaniah — yet now there is hope for Israel; the oath; the
people trembling in the broad place for the great rain; the matter examined; and the names of those who had taken foreign
wives (roll cells)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from ezr import G, art as K
from ezr.common import (pack, cp, say, caps, says, drawn, face, joined, cell, cells, roll, EZRA, EZRA_GRIEF, SHECANIAH, ISRAELITE, COLD, GOLDEN, RED)
from ezr import ch04 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("EZR-C05-00-Title", "Chapter 5 · The Strange Wives", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.rain_square("t5", 760, 820, 501)}</g><rect x="0" y="0" width="760" height="262" fill="#2A2A3A"></rect>')
    return chapter_title(5, "第五話", "The Strange Wives", "Ezra 9 – 10", svg, "#2A2A3A", v("10:2", frm="yet now there is hope"), "Ezra · Volume Fifteen")


SEGS = [face([cp("9:1", to="saying,"), say("9:1", frm="The people of Israel,"), says("9:2")], "EZRA 9:1–2", ISRAELITE, bg=RED, head="The Holy Seed", stamp=9),
        face([caps("9:3-4")], "EZRA 9:3–4", EZRA_GRIEF, bg=COLD, head="I Sat Confounded"),
        drawn([caps("9:5"), cp("9:6", to="and I said,"), say("9:6", frm="O my God,")], "EZRA 9:5–6", below(lambda w, h: K.prayer_evening("pe5", w, h, 502), 0.36), "#3A2A4A",
              head="At the Evening Oblation"),
        face([says("9:7-8")], "EZRA 9:7–8", EZRA_GRIEF, bg=COLD),
        face([says("9:9-10")], "EZRA 9:9–10", EZRA_GRIEF, bg=COLD),
        face([says("9:11-12")], "EZRA 9:11–12", EZRA_GRIEF, bg=COLD),
        face([says("9:13-15")], "EZRA 9:13–15", EZRA_GRIEF, bg=COLD, head="Thou Art Righteous")]
PG.extend(pack(SEGS, "EZR-C05-D", PG.next()))
SEGS2 = [drawn([caps("10:1")], "EZRA 10:1", below(lambda w, h: K.prayer_evening("pe5b", w, h, 503), 0.3), "#3A2A4A", head="Yet Now There Is Hope", stamp=10),
         face([cp("10:2", to="said unto Ezra,"), say("10:2", frm="We have trespassed"), says("10:3-4")], "EZRA 10:2–4", SHECANIAH),
         face([caps("10:5-6")], "EZRA 10:5–6", EZRA_GRIEF, bg=COLD),
         drawn([caps("10:7-9")], "EZRA 10:7–9", below(lambda w, h: K.rain_square("rs5", w, h, 504), 0.36), "#2A2A3A", head="The Great Rain"),
         face([cp("10:10", to="and said unto them,"), say("10:10", frm="Ye have trespassed"), says("10:11")], "EZRA 10:10–11", EZRA),
         drawn([cp("10:12", to="with a loud voice,"), say("10:12", frm="As thou hast said"), says("10:13-14")], "EZRA 10:12–14", below(lambda w, h: K.rain_square("rs5b", w, h, 505), 0.5),
               "#2A2A3A"),
         face([caps("10:15-17")], "EZRA 10:15–17", EZRA)]
PG.extend(pack(SEGS2, "EZR-C05-E", PG.next()))
R = (cells(10, 18, 24, "Of the Priests and the Levites", "#F3EFE6", head="That Had Married Foreign Women", budget=520)
     + cells(10, 25, 44, "Of Israel", "#FFD23F", budget=440))
PG.extend(roll(R, "EZR-C05-R", PG.next(), "THEY THAT HAD TAKEN FOREIGN WIVES · EZRA 10",
               end='''{end}'''.format(end=end_mark("END OF EZRA · NEXT · NEHEMIAH", "right: 40px; bottom: 50px", ch="完"))))
