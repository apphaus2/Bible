"""Ruth volume, Chapter 2 — The Near Kinsman (Ruth 3–4), the last chapter of Ruth. Every verse, word for word from ref/eng-asv.
Shall I not seek rest for thee?; the threshing-floor at night (the digest's panel: Ruth at his feet, nothing more); spread
thy skirt over thy handmaid; six measures of barley; the gate, the near kinsman and his shoe; Ye are witnesses; Obed laid in
Naomi's bosom; and the generations of Perez to David as a roll page."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from rolls import roll_pages
from deu.common import shade
from rut import G
from rut.common import (pack, say, cp, says, caps, over, face, drawn, D, NAOMI, NAOMI_JOY, RUTH, BOAZ, KINSMAN, NEIGHBOR, COLD, GOLDEN, RED)
from rut import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("RUT-C02-00-Title", "Chapter 2 · The Near Kinsman", title=True)
def title(n):
    bg, art = D("P07", 1)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#14123A"></rect><g transform="translate(0 340)">{art(760, 740)}</g>')
    return chapter_title(2, "第二話", "The Near Kinsman", "Ruth 3 – 4", svg, "#14123A", v("3:11", frm="all the city of my people"), "Ruth · Volume Eight")


SEGS = [face([cp("3:1", to="said unto her,"), ("say", v("3:1", frm="My daughter,") + " " + sp("3:2-4"))], "RUTH 3:1–4", NAOMI, head="The Threshing-floor", stamp=3),
        face([cp("3:5", to="said unto her,"), say("3:5", frm="All that"), caps("3:6")], "RUTH 3:5–6", RUTH),
        over([caps("3:7-8")], "RUTH 3:7–8", "P07", 1),
        face([cp("3:9", to="And he said,"), say("3:9", frm="Who art thou?", to="Who art thou?"), cp("3:9", frm="And she answered,", to="she answered,"), say("3:9", frm="I am Ruth")],
             "RUTH 3:9", RUTH, bg=COLD),
        face([cp("3:10", to="And he said,"), ("say", v("3:10", frm="Blessed be") + " " + sp("3:11-13"))], "RUTH 3:10–13", BOAZ, bg=COLD, head="A Worthy Woman"),
        over([cp("3:14", to="For he said,"), say("3:14", frm="Let it not"), cp("3:15", to="And he said,"), say("3:15", frm="Bring the mantle", to="hold it;"),
              cp("3:15", frm="and she held it;")], "RUTH 3:14–15", "P07", 1),
        face([cp("3:16", to="she said,"), say("3:16", frm="Who art thou,", to="my daughter?"), cp("3:16", frm="And she told"), cp("3:17", to="And she said,"),
              say("3:17", frm="These six", to="he me;"), cp("3:17", frm="for he said,", to="for he said,"), say("3:17", frm="Go not empty"),
              cp("3:18", to="Then said she,"), say("3:18", frm="Sit still,")], "RUTH 3:16–18", NAOMI),
        over([cp("4:1", to="unto whom he said,"), say("4:1", frm="Ho, such a one!", to="sit down here."), cp("4:1", frm="And he turned aside,"), cp("4:2", to="and said,"),
              say("4:2", frm="Sit ye down here.", to="Sit ye down here."), cp("4:2", frm="And they sat down.")], "RUTH 4:1–2", "P08", 0, head="At the Gate", stamp=4),
        face([cp("4:3", to="unto the near kinsman,"), ("say", v("4:3", frm="Naomi,") + " " + v("4:4", to="and I am after thee.")), cp("4:4", frm="And he said,", to="And he said,"),
              say("4:4", frm="I will redeem it.")], "RUTH 4:3–4", BOAZ),
        face([cp("4:5", to="Then said Boaz,"), say("4:5", frm="What day")], "RUTH 4:5", BOAZ),
        face([cp("4:6", to="the near kinsman said,"), say("4:6", frm="I cannot redeem it for myself,"), caps("4:7"), cp("4:8", to="unto Boaz,"), say("4:8", frm="Buy it", to="for thyself."),
              cp("4:8", frm="And he drew off")], "RUTH 4:6–8", KINSMAN, head="He Drew Off His Shoe"),
        over([cp("4:9", to="unto all the people,"), ("say", v("4:9", frm="Ye are witnesses") + " " + v("4:10"))], "RUTH 4:9–10", "P08", 0, head="Ye Are Witnesses"),
        over([cp("4:11", to="the elders, said,"), ("say", v("4:11", frm="We are witnesses.") + " " + v("4:12"))], "RUTH 4:11–12", "P08", 0),
        over([caps("4:13")], "RUTH 4:13", "P08", 1, head="A Restorer of Life"),
        face([cp("4:14", to="unto Naomi,"), ("say", v("4:14", frm="Blessed be") + " " + v("4:15"))], "RUTH 4:14–15", NEIGHBOR),
        over([caps("4:16")], "RUTH 4:16", "P08", 2),
        face([cp("4:17", to="saying,"), say("4:17", frm="There is a son", to="to Naomi;"), cp("4:17", frm="and they called")], "RUTH 4:17", NAOMI_JOY)]
PG.extend(pack(SEGS, "RUT-C02-D", PG.next()))

GEN = [("Perez", v("4:18"), "RUTH 4:18", "#FFD23F", "The Generations of Perez"), ("Ram · Amminadab", v("4:19"), "RUTH 4:19", "#FFD23F", None),
       ("Nahshon · Salmon", v("4:20"), "RUTH 4:20", "#FFD23F", None), ("Boaz · Obed", v("4:21"), "RUTH 4:21", "#FF8A3D", None),
       ("Jesse · David", v("4:22"), "RUTH 4:22", "#D7261E", None)]
pages = roll_pages(GEN, "RUT-C02-R", PG.next(), "Ruth", "RUTH", tag="THE GENERATIONS OF PEREZ · RUTH 4")
name, board, fn = pages[-1]
mark = end_mark("END OF RUTH · NEXT · 1 SAMUEL", "right: 26px; bottom: 34px", ch="完")
pages[-1] = (name, board, lambda fn=fn: fn().replace("</div>\n</x-dc>", mark + "</div>\n</x-dc>", 1))
PG.extend(pages)
