"""1 Samuel volume, Chapter 3 — Give Us a King (1 Samuel 6–8). Every verse, word for word from ref/asv.
The priests and diviners and the trespass-offering of golden tumors and mice; the new cart and two milch kine lowing as they
went to Beth-shemesh (the digest's kine panels); the men of Beth-shemesh smitten (6:19 words only); the ark at
Kiriath-jearim twenty years; Mizpah, the thunder, and the stone Eben-ezer — Hitherto hath Jehovah helped us; Samuel's sons;
Give us a king, and the manner of the king (the digest's panels and Jehovah's words in the Voice box)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from genesis import art as X
from jos import art as JA
from sa1 import G, art as K
from sa1.common import (pack, say, gd, cp, says, gods, caps, over, face, drawn, D, F, SAMUEL_OLD, SAMUEL_GRIEVED, ISRAELITE, PHILISTINE, RED, COLD, GOLDEN)
from sa1 import ch02 as _prev

v, sp = G.v, G.span
DIVINER = F("adam", skin="#C98E66", shadow="#4A2A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#3A2A5A", band=True, light="#B88AE8")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHTA = lambda w, h: X.cosmic(w, h)
MAP = "#0B1A2E"


@P("1SA-C03-00-Title", "Chapter 3 · Give Us a King", title=True)
def title(n):
    bg, art = D("A8", 3)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 340)">{art(760, 740)}</g>')
    return chapter_title(3, "第三話", "Give Us a King", "1 Samuel 6 – 8", svg, "#8FD0E2", v("8:5", frm="now make us a king"), "1 Samuel · Volume Nine")


SEGS = [face([caps("6:1"), cp("6:2", to="saying,"), say("6:2", frm="What shall we do")], "1SAM 6:1–2", PHILISTINE, bg=RED, head="Send It Not Empty", stamp=6),
        face([cp("6:3", to="And they said,"), say("6:3", frm="If ye send"), cp("6:4", to="Then said they,"), say("6:4", frm="What shall be", to="return to him?"),
              cp("6:4", frm="And they said,", to="And they said,"), say("6:4", frm="Five golden")], "1SAM 6:3–4", DIVINER, bg=COLD),
        drawn([says("6:5-6")], "1SAM 6:5–6", lambda w, h: K.golden(w, h, 311), "#2A1A2E"),
        face([says("6:7-9")], "1SAM 6:7–9", DIVINER, bg=COLD),
        over([caps("6:10-11")], "1SAM 6:10–11", "A7", 0, head="The Kine Took the Straight Way"),
        over([caps("6:12")], "1SAM 6:12", "A7", 1),
        over([caps("6:13-15")], "1SAM 6:13–15", "A7", 2),
        drawn([caps("6:16-18")], "1SAM 6:16–18", lambda w, h: K.golden(w, h, 312), "#2A1A2E"),
        drawn([caps("6:19"), cp("6:20", to="said,"), say("6:20", frm="Who is able"), cp("6:21", to="saying,"), say("6:21", frm="The Philistines have")], "1SAM 6:19–21",
              NIGHTA, "#0B0B2A"),
        drawn([caps("7:1-2")], "1SAM 7:1–2", lambda w, h: JA.shiloh("kj3", w, h, 313, people=False), "#E8D8B0", head="Hitherto Hath Jehovah Helped Us", stamp=7),
        face([cp("7:3", to="saying,"), say("7:3", frm="If ye do"), caps("7:4"), cp("7:5", to="And Samuel said,"), say("7:5", frm="Gather all")], "1SAM 7:3–5", SAMUEL_OLD),
        drawn([cp("7:6", to="and said there,"), say("7:6", frm="We have sinned", to="against Jehovah."), cp("7:6", frm="And Samuel judged"), caps("7:7"), cp("7:8", to="to Samuel,"),
               say("7:8", frm="Cease not")], "1SAM 7:6–8", lambda w, h: JA.armed("mz3", w, h, 314, tribes=("JUDAH", "BENJAMIN")), "#F3D8A0"),
        drawn([caps("7:9-11")], "1SAM 7:9–11", lambda w, h: JA.hailstones(w, h, 315), "#2A2E4A"),
        drawn([cp("7:12", to="saying,"), say("7:12", frm="Hitherto"), caps("7:13-14")], "1SAM 7:12–14", lambda w, h: K.eben_ezer("ee3", w, h, 316), "#5A6E8A"),
        over([caps("7:15-17")], "1SAM 7:15–17", "A4", 3),
        over([caps("8:1-4"), cp("8:5", to="and they said unto him,"), say("8:5", frm="Behold,")], "1SAM 8:1–5", "A8", 0, head="Give Us a King", stamp=8),
        face([cp("8:6", to="when they said,"), say("8:6", frm="Give us a king", to="to judge us."), cp("8:6", frm="And Samuel prayed")], "1SAM 8:6", SAMUEL_GRIEVED, bg=COLD),
        over([cp("8:7", to="unto Samuel,"), gd("8:7", frm="Hearken"), gods("8:8-9")], "1SAM 8:7–9", "A8", 2),
        face([caps("8:10"), cp("8:11", to="And he said,"), ("say", v("8:11", frm="This will be") + " " + sp("8:12-14"))], "1SAM 8:10–14", SAMUEL_OLD, head="The Manner of the King"),
        face([says("8:15-18")], "1SAM 8:15–18", SAMUEL_GRIEVED, bg=COLD),
        over([cp("8:19", to="and they said,"), ("say", v("8:19", frm="Nay:") + " " + v("8:20"))], "1SAM 8:19–20", "A8", 3),
        drawn([caps("8:21"), cp("8:22", to="to Samuel,"), gd("8:22", frm="Hearken", to="make them a king."), cp("8:22", frm="And Samuel said", to="the men of Israel,"),
               say("8:22", frm="Go ye every man")], "1SAM 8:21–22", NIGHTA, "#0B0B2A")]
PG.extend(pack(SEGS, "1SA-C03-D", PG.next(), end=end_mark("NEXT · SAUL ANOINTED", "right: 10px; bottom: 34px")))
