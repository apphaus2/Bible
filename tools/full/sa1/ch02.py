"""1 Samuel volume, Chapter 2 — Speak, Jehovah (1 Samuel 3–5). Every verse, word for word from ref/asv.
The lamp of God not yet gone out; Samuel, Samuel — Speak; for thy servant heareth; the word against Eli's house; the battle
at Eben-ezer and the ark fetched from Shiloh; the ark taken; Eli fallen from his seat by the gate (the digest's panel: the
overturned seat only); Ichabod; the ark in the house of Dagon and Dagon fallen; the ark carried about Ashdod, Gath and Ekron
as a technical map, and the cry of the city."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from genesis import art as X
from sa1 import G, art as K
from jos import art as JA
from sa1.common import (pack, say, gd, cp, says, gods, caps, over, face, drawn, D, F, ELI, ELI_AWE, SAMUEL_CHILD, SAMUEL_NIGHT, ISRAELITE, PHILISTINE,
                        RED, COLD, GOLDEN)
from sa1 import ch01 as _prev

v, sp = G.v, G.span
RUNNER = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", sweat=True, brow="sorrow", light="#9AA8C8")
WIFE = F("eve", skin="#C99A84", shadow="#4A3A5A", hair="#2A1A10", scarf="#5A4A6A", brow="sorrow", tear=True, light="#9AA8C8")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("1SA-C02-00-Title", "Chapter 2 · Speak, Jehovah", title=True)
def title(n):
    bg, art = D("A4", 1)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#14123A"></rect><g transform="translate(0 340)">{art(760, 740)}</g>')
    return chapter_title(2, "第二話", "Speak, Jehovah", "1 Samuel 3 – 5", svg, "#14123A", v("3:10", frm="Speak; for thy servant heareth."), "1 Samuel · Volume Nine")


SEGS = [over([caps("3:1-3")], "1SAM 3:1–3", "A3", 0, head="Here Am I", stamp=3),
        face([cp("3:4", to="and he said,"), say("3:4", frm="Here am I."), cp("3:5", to="and said,"), say("3:5", frm="Here am I;", to="calledst me."),
              cp("3:5", frm="And he said,", to="And he said,"), say("3:5", frm="I called not;", to="lie down again."), cp("3:5", frm="And he went")], "1SAM 3:4–5", SAMUEL_NIGHT, bg=COLD),
        face([cp("3:6", to="and said,"), say("3:6", frm="Here am I;", to="calledst me."), cp("3:6", frm="And he answered,", to="And he answered,"), say("3:6", frm="I called not,"),
              caps("3:7")], "1SAM 3:6–7", ELI, bg=COLD),
        over([cp("3:8", to="and said,"), say("3:8", frm="Here am I;", to="calledst me."), cp("3:8", frm="And Eli perceived")], "1SAM 3:8", "A3", 4),
        face([cp("3:9", to="unto Samuel,"), say("3:9", frm="Go, lie down:", to="thy servant heareth."), cp("3:9", frm="So Samuel went")], "1SAM 3:9", ELI_AWE, bg=COLD),
        over([cp("3:10", to="as at other times,"), gd("3:10", frm="Samuel, Samuel.", to="Samuel, Samuel."), cp("3:10", frm="Then Samuel said,", to="Then Samuel said,"),
              say("3:10", frm="Speak;")], "1SAM 3:10", "A4", 1, head="Speak; for Thy Servant Heareth"),
        drawn([cp("3:11", to="And Jehovah said to Samuel,"), gd("3:11", frm="Behold,"), gods("3:12-14")], "1SAM 3:11–14", lambda w, h: X.cosmic(w, h), "#0B0B2A"),
        face([caps("3:15"), cp("3:16", to="and said,"), say("3:16", frm="Samuel, my son.", to="Samuel, my son."), cp("3:16", frm="And he said,", to="And he said,"), say("3:16", frm="Here am I."),
              cp("3:17", to="And he said,"), say("3:17", frm="What is the thing")], "1SAM 3:15–17", ELI),
        face([cp("3:18", to="And he said,"), say("3:18", frm="It is Jehovah:")], "1SAM 3:18", ELI_AWE),
        over([caps("3:19-21"), cp("4:1", to="came to all Israel.")], "1SAM 3:19–4:1", "A4", 3),
        drawn([cp("4:1", frm="Now Israel went out"), caps("4:2"), cp("4:3", to="the elders of Israel said,"), say("4:3", frm="Wherefore hath")], "1SAM 4:1–3",
              K.below(lambda w, h: JA.armed("ar12", w, h, 212, tribes=("JUDAH", "EPHRAIM")), 0.42), "#F3D8A0", head="The Ark of God Was Taken", stamp=4),
        drawn([caps("4:4-5"), cp("4:6", to="they said,"), say("4:6", frm="What meaneth", to="the Hebrews?"), cp("4:6", frm="And they understood")], "1SAM 4:4–6",
              K.below(lambda w, h: K.ark_map(w, h, "EBEN-EZER"), 0.5), MAP),
        face([cp("4:7", to="for they said,"), say("4:7", frm="God is come", to="into the camp."), cp("4:7", frm="And they said,", to="And they said,"), say("4:7", frm="Woe unto us!"),
              says("4:8-9")], "1SAM 4:7–9", PHILISTINE, bg=RED),
        over([caps("4:10-11")], "1SAM 4:10–11", "A5", 1),
        over([caps("4:12-13"), cp("4:14", to="he said,"), say("4:14", frm="What meaneth", to="tumult?"), cp("4:14", frm="And the man hasted"), caps("4:15")], "1SAM 4:12–15", "A5", 2, head="Eli"),
        face([cp("4:16", to="unto Eli,"), say("4:16", frm="I am he", to="out of the army."), cp("4:16", frm="And he said,", to="And he said,"), say("4:16", frm="How went"),
              cp("4:17", to="answered and said,"), say("4:17", frm="Israel is fled")], "1SAM 4:16–17", RUNNER, bg=COLD),
        over([caps("4:18")], "1SAM 4:18", "A5", 2),
        face([caps("4:19"), cp("4:20", to="said unto her,"), say("4:20", frm="Fear not;", to="a son."), cp("4:20", frm="But she answered not,")], "1SAM 4:19–20", WIFE, bg=COLD,
             head="Ichabod"),
        over([cp("4:21", to="saying,"), say("4:21", frm="The glory is departed", to="from Israel;"), cp("4:21", frm="because the ark"), cp("4:22", to="And she said,"), say("4:22", frm="The glory")],
             "1SAM 4:21–22", "A5", 3),
        over([caps("5:1-2")], "1SAM 5:1–2", "A6", 0, head="The House of Dagon", stamp=5),
        over([caps("5:3")], "1SAM 5:3", "A6", 1),
        over([caps("5:4-5")], "1SAM 5:4–5", "A6", 2),
        drawn([caps("5:6"), cp("5:7", to="they said,"), say("5:7", frm="The ark of the God"), cp("5:8", to="and said,"), say("5:8", frm="What shall we do", to="God of Israel?"),
               cp("5:8", frm="And they answered,", to="And they answered,"), say("5:8", frm="Let the ark", to="unto Gath."), cp("5:8", frm="And they carried")], "1SAM 5:6–8",
              K.below(lambda w, h: K.ark_map(w, h, "GATH"), 0.5), MAP, head="Ashdod, Gath and Ekron"),
        drawn([caps("5:9"), cp("5:10", to="cried out, saying,"), say("5:10", frm="They have brought")], "1SAM 5:9–10", K.below(lambda w, h: K.ark_map(w, h, "EKRON"), 0.36), MAP),
        drawn([cp("5:11", to="and they said,"), say("5:11", frm="Send away", to="and our people."), cp("5:11", frm="For there was"), caps("5:12")], "1SAM 5:11–12",
              lambda w, h: K.tumors(w, h, 211), "#2A1A3A")]
PG.extend(pack(SEGS, "1SA-C02-D", PG.next(), end=end_mark("NEXT · GIVE US A KING", "right: 10px; bottom: 34px")))
