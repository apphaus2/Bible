"""1 Samuel volume, Chapter 1 — Hannah (1 Samuel 1–2). Every verse, word for word from ref/asv.
Elkanah's two wives and the yearly sacrifice at Shiloh; Hannah's bitterness of soul and her vow; Eli marks her mouth; Samuel
born and given — For this child I prayed; Hannah's song in song boxes; the sons of Eli and the flesh-hook; the child Samuel
in his linen ephod and the little robe; and the man of God's word against the house of Eli (the Voice box)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from genesis import art as X
from sa1 import G, art as K
from sa1.common import (pack, say, gd, cp, sg, says, gods, caps, over, face, drawn, D, HANNAH, HANNAH_JOY, ELI, ELI_AWE, SAMUEL_CHILD, ELKANAH, MAN_OF_GOD,
                        RED, COLD, GOLDEN)

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHTA = lambda w, h: X.cosmic(w, h)


@P("1SA-C01-00-Title", "Chapter 1 · Hannah", title=True)
def title(n):
    bg, art = D("A2", 1)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8FD0E2"></rect><g transform="translate(0 340)">{art(760, 740)}</g>')
    return chapter_title(1, "第一話", "Hannah", "1 Samuel 1 – 2", svg, "#8FD0E2", v("1:27"), "1 Samuel · Volume Nine")


SEGS = [over([caps("1:1-3")], "1SAM 1:1–3", "A1", 0, head="Hannah Had No Children", stamp=1),
        face([caps("1:4-7"), cp("1:8", to="said unto her,"), say("1:8", frm="Hannah,")], "1SAM 1:4–8", ELKANAH),
        over([caps("1:9")], "1SAM 1:9", "A1", 2),
        face([cp("1:10"), cp("1:11", to="and said,"), say("1:11", frm="O Jehovah of hosts,")], "1SAM 1:10–11", HANNAH, bg=COLD, head="She Vowed a Vow"),
        over([caps("1:12-13"), cp("1:14", to="said unto her,"), say("1:14", frm="How long")], "1SAM 1:12–14", "A1", 2),
        face([cp("1:15", to="answered and said,"), ("say", v("1:15", frm="No, my lord,") + " " + v("1:16"))], "1SAM 1:15–16", HANNAH, bg=COLD),
        face([cp("1:17", to="answered and said,"), say("1:17", frm="Go in peace;"), cp("1:18", to="And she said,"), say("1:18", frm="Let thy handmaid", to="in thy sight."),
              cp("1:18", frm="So the woman")], "1SAM 1:17–18", ELI),
        over([caps("1:19"), cp("1:20", to="saying,"), say("1:20", frm="Because I")], "1SAM 1:19–20", "A2", 0, head="I Have Asked Him of Jehovah"),
        face([caps("1:21"), cp("1:22", to="unto her husband,"), say("1:22", frm="I will not"), cp("1:23", to="said unto her,"), say("1:23", frm="Do what", to="establish his word."),
              cp("1:23", frm="So the woman")], "1SAM 1:21–23", ELKANAH),
        over([caps("1:24-25")], "1SAM 1:24–25", "A2", 1),
        face([cp("1:26", to="And she said,"), ("say", v("1:26", frm="Oh, my lord,") + " " + v("1:27") + " " + v("1:28", to="granted to Jehovah.")), cp("1:28", frm="And he worshipped")],
             "1SAM 1:26–28", HANNAH_JOY, head="For This Child I Prayed"),
        face([cp("2:1", to="and said:"), sg("2:1", frm="My heart"), sg("2:2"), sg("2:3")], "1SAM 2:1–3", HANNAH_JOY, head="My Heart Exulteth in Jehovah", stamp=2),
        drawn([sg("2:4"), sg("2:5"), sg("2:6"), sg("2:7")], "1SAM 2:4–7", NIGHTA, "#0B0B2A"),
        drawn([sg("2:8"), sg("2:9"), sg("2:10")], "1SAM 2:8–10", D("A2", 2)[1], D("A2", 2)[0]),
        over([caps("2:11-14")], "1SAM 2:11–14", "A2", 2, head="The Sons of Eli"),
        drawn([cp("2:15", to="that sacrificed,"), say("2:15", frm="Give flesh"), cp("2:16", to="said unto him,"), say("2:16", frm="They will surely", to="thy soul desireth;"),
               cp("2:16", frm="then he would say,", to="then he would say,"), say("2:16", frm="Nay,"), caps("2:17")], "1SAM 2:15–17", lambda w, h: K.flesh_hook(w, h, 111), "#3A2218"),
        drawn([caps("2:18-19")], "1SAM 2:18–19", lambda w, h: K.little_robe(w, h, 112), "#E8D8B0"),
        face([cp("2:20", to="and said,"), say("2:20", frm="Jehovah give", to="asked of Jehovah."), cp("2:20", frm="And they went"), caps("2:21")], "1SAM 2:20–21", ELI),
        face([caps("2:22"), cp("2:23", to="And he said unto them,"), ("say", v("2:23", frm="Why do ye") + " " + v("2:24") + " " + v("2:25", to="who shall entreat for him?")),
              cp("2:25", frm="Notwithstanding,"), caps("2:26")], "1SAM 2:22–26", ELI_AWE, bg=COLD),
        face([cp("2:27", to="Thus saith Jehovah,"), gd("2:27", frm="Did I reveal"), gods("2:28-29")], "1SAM 2:27–29", MAN_OF_GOD, bg=COLD, head="Them That Honor Me I Will Honor"),
        drawn([gd("2:30"), gods("2:31-33")], "1SAM 2:30–33", NIGHTA, "#0B0B2A"),
        drawn([gods("2:34-36")], "1SAM 2:34–36", NIGHTA, "#0B0B2A")]
PG.extend(pack(SEGS, "1SA-C01-D", PG.next(), end=end_mark("NEXT · SPEAK, JEHOVAH", "right: 10px; bottom: 34px")))
