"""2 Samuel volume, Chapter 1 — How Are the Mighty Fallen (2 Samuel 1–2). Every verse, word for word from ref/asv.
The Amalekite out of Saul's camp with the crown and the bracelet; David rending his clothes; 1:15 words only; the song of the
bow in song boxes over the digest's mourners and Gilboa; David anointed king over Judah in Hebron; Abner makes Ish-bosheth
king at Mahanaim; the pool of Gibeon (2:16 words over the field of swords); Asahel light of foot (2:23 words over a spear
in the empty way); shall the sword devour for ever?; and the day breaking upon Joab at Hebron."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from sa1 import art as K1
from jos.art import below
from sa2 import G, art as K
from sa2.common import (pack, say, gd, cp, sg, sgs, says, caps, over, face, drawn, D, DAVID_MOURN, DAVID_KING, DAVID_WRATH, JONATHAN, ABNER, JOAB, AMALEKITE,
                        RED, COLD, GOLDEN)

v, sp = G.v, G.span
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("2SA-C01-00-Title", "Chapter 1 · How Are the Mighty Fallen", title=True)
def title(n):
    bg, art = D("A1", 2)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#3A2A4A"></rect><g transform="translate(0 340)">{art(760, 740)}</g>')
    return chapter_title(1, "第一話", "How Are the Mighty Fallen", "2 Samuel 1 – 2", svg, "#3A2A4A", v("1:19", frm="How are"), "2 Samuel · Volume Ten")


SEGS = [drawn([caps("1:1-2")], "2SAM 1:1–2", lambda w, h: K.tidings("td1", w, h, 101), "#E8B880", head="Out of the Camp of Israel", stamp=1),
        face([cp("1:3", to="And David said unto him,"), say("1:3", frm="From whence", to="comest thou?"), cp("1:3", frm="And he said unto him,", to="said unto him,"),
              say("1:3", frm="Out of the camp"), cp("1:4", to="And David said unto him,"), say("1:4", frm="How went", to="tell me."), cp("1:4", frm="And he answered,", to="And he answered,"),
              say("1:4", frm="The people are fled")], "2SAM 1:3–4", AMALEKITE),
        face([cp("1:5", to="that told him,"), say("1:5", frm="How knowest"), cp("1:6", to="told him said,"), ("say", v("1:6", frm="As I happened") + " " + v("1:7"))], "2SAM 1:5–7", AMALEKITE),
        drawn([says("1:8-10")], "2SAM 1:8–10", lambda w, h: K.crown_bracelet(w, h, 102), "#3A1A2A"),
        over([caps("1:11-12")], "2SAM 1:11–12", "A1", 0, head="They Mourned, and Wept"),
        face([cp("1:13", to="that told him,"), say("1:13", frm="Whence art thou?", to="Whence art thou?"), cp("1:13", frm="And he answered,", to="And he answered,"), say("1:13", frm="I am the son"),
              cp("1:14", to="said unto him,"), say("1:14", frm="How wast")], "2SAM 1:13–14", DAVID_WRATH, bg=RED),
        face([cp("1:15", to="and said,"), say("1:15", frm="Go near,", to="fall upon him."), cp("1:15", frm="And he smote him,"), cp("1:16", to="said unto him,"), say("1:16", frm="Thy blood")],
             "2SAM 1:15–16", DAVID_WRATH, bg=RED),
        over([caps("1:17-18")] + sgs("1:19-20"), "2SAM 1:17–20", "A1", 1, head="The Song of the Bow"),
        drawn(sgs("1:21-22"), "2SAM 1:21–22", lambda w, h: K.gilboa_dusk(w, h, 103), "#2A1A3A"),
        over(sgs("1:23-24"), "2SAM 1:23–24", "A1", 2),
        face(sgs("1:25-27"), "2SAM 1:25–27", JONATHAN, bg=COLD),
        drawn([cp("2:1", to="saying,"), say("2:1", frm="Shall I go up", to="cities of Judah?"), cp("2:1", frm="And Jehovah said unto him,", to="said unto him,"), gd("2:1", frm="Go up.", to="Go up."),
               cp("2:1", frm="And David said,", to="And David said,"), say("2:1", frm="Whither", to="go up?"), cp("2:1", frm="And he said,", to="And he said,"), gd("2:1", frm="Unto Hebron.")],
              "2SAM 2:1", lambda w, h: K1.ephod_inquire("ei1", w, h, 104), "#2A1A3A", head="King over the House of Judah", stamp=2),
        drawn([caps("2:2-3"), cp("2:4", to="over the house of Judah."), cp("2:4", frm="And they told David,", to="saying,"), say("2:4", frm="The men of Jabesh")], "2SAM 2:2–4",
              below(lambda w, h: K.hebron_anointed("ha1", w, h, 105), 0.34), "#FFE680"),
        face([cp("2:5", to="and said unto them,"), ("say", v("2:5", frm="Blessed be ye") + " " + sp("2:6-7"))], "2SAM 2:5–7", DAVID_KING),
        drawn([caps("2:8-11")], "2SAM 2:8–11", lambda w, h: K.mahanaim("mh1", w, h, 106), "#5A3A5A", head="Ish-bosheth"),
        drawn([caps("2:12-13")], "2SAM 2:12–13", lambda w, h: K.pool("pg1", w, h, 107), "#8FD0E2", head="The Pool of Gibeon"),
        face([cp("2:14", to="to Joab,"), say("2:14", frm="Let the young men,", to="before us."), cp("2:14", frm="And Joab said,", to="And Joab said,"), say("2:14", frm="Let them arise."),
              caps("2:15")], "2SAM 2:14–15", ABNER),
        drawn([caps("2:16-17")], "2SAM 2:16–17", lambda w, h: K.pool("pg1b", w, h, 108, men=False), "#5A3A4A"),
        drawn([caps("2:18-19")], "2SAM 2:18–19", lambda w, h: K.pursuit("pu1", w, h, 109), "#F3D8A0", head="Asahel"),
        face([cp("2:20", to="and said,"), say("2:20", frm="Is it thou,", to="Asahel?"), cp("2:20", frm="And he answered,", to="And he answered,"), say("2:20", frm="It is I."),
              cp("2:21", to="said to him,"), say("2:21", frm="Turn thee aside", to="his armor."), cp("2:21", frm="But Asahel"), cp("2:22", to="to Asahel,"), say("2:22", frm="Turn thee aside")],
             "2SAM 2:20–22", ABNER, bg=COLD),
        drawn([caps("2:23")], "2SAM 2:23", lambda w, h: K.spear_road(w, h, 110), "#3A1A2A"),
        drawn([caps("2:24-25")], "2SAM 2:24–25", lambda w, h: K.hill_ammah("am1", w, h, 111), "#2A1A3A", head="Shall the Sword Devour for Ever?"),
        face([cp("2:26", to="and said,"), say("2:26", frm="Shall the sword")], "2SAM 2:26", ABNER, bg=COLD),
        face([cp("2:27", to="And Joab said,"), say("2:27", frm="As God liveth,")], "2SAM 2:27", JOAB, bg=RED),
        drawn([caps("2:28")], "2SAM 2:28", lambda w, h: K.hill_ammah("am1b", w, h, 112, trumpet=True), "#2A1A3A"),
        drawn([caps("2:29-32")], "2SAM 2:29–32", lambda w, h: K.dawn_hebron("dh1", w, h, 113), "#2A2A5A")]
PG.extend(pack(SEGS, "2SA-C01-D", PG.next(), end=end_mark("NEXT · ABNER", "right: 10px; bottom: 34px")))
