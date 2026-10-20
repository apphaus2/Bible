"""Ruth volume, Chapter 1 — Whither Thou Goest (Ruth 1–2). Every verse, word for word from ref/eng-asv.
Famine and Moab; Elimelech, Mahlon and Chilion dead; Naomi turning home, Orpah's kiss, Ruth cleaving — Entreat me not to
leave thee; Call me not Naomi, call me Mara; then the field of Boaz in barley harvest: the gleaning, under whose wings thou
art come to take refuge, the parched grain, the ephah of barley, and the near kinsman (the digest's Ruth panels throughout)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from rut import G
from rut.common import (pack, say, cp, says, caps, over, face, drawn, D, NAOMI, MARA, NAOMI_JOY, RUTH, RUTH_WEEP, ORPAH, BOAZ, REAPER, NEIGHBOR,
                        COLD, GOLDEN, RED)

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("RUT-C01-00-Title", "Chapter 1 · Whither Thou Goest", title=True)
def title(n):
    bg, art = D("P02", 3)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#5A2A5A"></rect><g transform="translate(0 340)">{art(760, 740)}</g>')
    return chapter_title(1, "第一話", "Whither Thou Goest", "Ruth 1 – 2", svg, "#5A2A5A", v("1:16", frm="thy people shall be", to="thy God my God;"), "Ruth · Volume Eight")


SEGS = [over([caps("1:1-2")], "RUTH 1:1–2", "P01", 0, head="In the Days When the Judges Judged", stamp=1),
        over([caps("1:3")], "RUTH 1:3", "P01", 1, align="xMidYMax"),
        over([caps("1:4")], "RUTH 1:4", "P01", 2, align="xMidYMax"),
        over([caps("1:5")], "RUTH 1:5", "P01", 3),
        over([caps("1:6-7")], "RUTH 1:6–7", "P02", 0, head="Go, Return"),
        face([cp("1:8", to="unto her two daughters-in-law,"), ("say", v("1:8", frm="Go, return") + " " + v("1:9", to="in the house of her husband.")), cp("1:9", frm="Then she kissed")],
             "RUTH 1:8–9", NAOMI),
        face([cp("1:10", to="And they said unto her,"), say("1:10", frm="Nay,")], "RUTH 1:10", ORPAH, bg=COLD),
        face([cp("1:11", to="And Naomi said,"), ("say", v("1:11", frm="Turn again,") + " " + sp("1:12-13"))], "RUTH 1:11–13", MARA, bg=COLD),
        over([caps("1:14")], "RUTH 1:14", "P02", 3),
        face([cp("1:15", to="And she said,"), say("1:15", frm="Behold,")], "RUTH 1:15", NAOMI, head="Entreat Me Not to Leave Thee"),
        face([cp("1:16", to="And Ruth said,"), ("say", v("1:16", frm="Entreat me") + " " + v("1:17"))], "RUTH 1:16–17", RUTH, bg=GOLDEN),
        over([caps("1:18"), cp("1:19", to="So they two went until they came to Beth-lehem.")], "RUTH 1:18–19", "P03", 1),
        over([cp("1:19", frm="And it came to pass,", to="and the women said,"), say("1:19", frm="Is this Naomi?")], "RUTH 1:19", "P04", 0, head="Call Me Mara"),
        face([cp("1:20", to="And she said unto them,"), ("say", v("1:20", frm="Call me not") + " " + v("1:21"))], "RUTH 1:20–21", MARA, bg=COLD),
        over([caps("1:22")], "RUTH 1:22", "P04", 2),
        over([caps("2:1"), cp("2:2", to="said unto Naomi,"), say("2:2", frm="Let me now", to="find favor."), cp("2:2", frm="And she said unto her,", to="said unto her,"),
              say("2:2", frm="Go, my daughter.")], "RUTH 2:1–2", "P05", 0, head="The Field of Boaz", stamp=2),
        over([caps("2:3")], "RUTH 2:3", "P05", 1),
        face([cp("2:4", to="said unto the reapers,"), say("2:4", frm="Jehovah be with you.", to="Jehovah be with you."), cp("2:4", frm="And they answered him,", to="answered him,"),
              say("2:4", frm="Jehovah bless thee."), cp("2:5", to="over the reapers,"), say("2:5", frm="Whose damsel")], "RUTH 2:4–5", BOAZ),
        face([cp("2:6", to="answered and said,"), ("say", v("2:6", frm="It is the") + " " + v("2:7", to="among the sheaves.")), cp("2:7", frm="So she came")], "RUTH 2:6–7", REAPER),
        face([cp("2:8", to="unto Ruth,"), ("say", v("2:8", frm="Hearest thou") + " " + v("2:9"))], "RUTH 2:8–9", BOAZ, head="Under Whose Wings"),
        over([cp("2:10", to="and said unto him,"), say("2:10", frm="Why have I")], "RUTH 2:10", "P06", 1),
        face([cp("2:11", to="said unto her,"), ("say", v("2:11", frm="It hath fully") + " " + v("2:12"))], "RUTH 2:11–12", BOAZ),
        face([cp("2:13", to="Then she said,"), say("2:13", frm="Let me find")], "RUTH 2:13", RUTH),
        over([cp("2:14", to="said unto her,"), say("2:14", frm="Come hither,", to="in the vinegar."), cp("2:14", frm="And she sat")], "RUTH 2:14", "P05", 3, head="An Ephah of Barley"),
        face([cp("2:15", to="saying,"), ("say", v("2:15", frm="Let her glean") + " " + v("2:16"))], "RUTH 2:15–16", BOAZ),
        over([caps("2:17-18")], "RUTH 2:17–18", "P06", 3),
        face([cp("2:19", to="said unto her,"), say("2:19", frm="Where hast", to="knowledge of thee."), cp("2:19", frm="And she showed", to="and said,"), say("2:19", frm="The man's name")],
             "RUTH 2:19", NAOMI, head="One of Our Near Kinsmen"),
        face([cp("2:20", to="unto her daughter-in-law,"), say("2:20", frm="Blessed be he", to="to the dead."), cp("2:20", frm="And Naomi said unto her,", to="said unto her,"),
              say("2:20", frm="The man is nigh")], "RUTH 2:20", NAOMI_JOY),
        face([cp("2:21", to="said,"), say("2:21", frm="Yea,"), cp("2:22", to="her daughter-in-law,"), say("2:22", frm="It is good,"), caps("2:23")], "RUTH 2:21–23", RUTH)]
PG.extend(pack(SEGS, "RUT-C01-D", PG.next(), end=end_mark("NEXT · THE NEAR KINSMAN", "right: 10px; bottom: 34px")))
