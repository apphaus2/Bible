"""Judges volume, Chapter 10 — No King in Israel (Judges 20–21), the last chapter of Judges. Every verse, word for word from
ref/asv. All Israel assembled as one man at Mizpah; the Levite's account; Benjamin will not hearken; the seven hundred
left-handed slingers; two days lost and the people weeping at Beth-el before the ark, Phinehas standing before it; the third
day laid out as a technical map, the pillar of smoke out of Gibeah; the six hundred in the rock of Rimmon; one tribe lacking
in Israel; Jabesh-gilead (21:10–12 are words over a distant city's smoke); the daughters of Shiloh in the dances; and In
those days there was no king in Israel: every man did that which was right in his own eyes."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from deu import art4 as D4
from genesis import art as X
from jos import art as JA
from jdg import G, art as K
from jdg.common import pack, say, gd, cp, says, gods, caps, face, drawn, F, ISRAELITE, RED, COLD, GOLDEN
from jdg import ch09 as _prev

v, sp = G.v, G.span
LEVITE = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#2A1A10", hl="#5A4A3E", beard=True, beard_color="#2A1A10", scarf="#5A6E8A", cord=True, brow="sorrow", light="#9AA8C8")
PHINEHAS = F("adam", skin="#C98E66", shadow="#6A4A3A", hair="#C8C2B6", hl="#8A867E", beard=True, beard_color="#C8C2B6", scarf="#F3EFE6", band=True, light="#FFE680")
ELDER = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#B8B2A6", hl="#8A867E", beard=True, beard_color="#B8B2A6", scarf="#6A5A3A", cord=True, brow="sorrow", light="#9AA8C8")
MAP = "#0B1A2E"
NIGHTA = lambda w, h: X.cosmic(w, h)
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JDG-C10-00-Title", "Chapter 10 · No King in Israel", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#F3D8A0"></rect><g transform="translate(0 380)">{JA.armed("t10", 760, 700, 1001, tribes=("JUDAH", "EPHRAIM", "DAN"))}</g>')
    return chapter_title(10, "第十話", "No King in Israel", "Judges 20 – 21", svg, "#F3D8A0", v("21:25", frm="every man did"), "Judges · Volume Seven")


SEGS = [drawn([caps("20:1-2"), cp("20:3", to="And the children of Israel said,"), say("20:3", frm="Tell us,")], "JDG 20:1–3", lambda w, h: JA.armed("ar10", w, h, 1011, tribes=("JUDAH", "EPHRAIM", "DAN")),
              "#F3D8A0", head="As One Man", stamp=20),
        face([cp("20:4", to="answered and said,"), ("say", v("20:4", frm="I came into") + " " + sp("20:5-7"))], "JDG 20:4–7", LEVITE, bg=COLD),
        face([cp("20:8", to="saying,"), ("say", v("20:8", frm="We will not") + " " + sp("20:9-10")), caps("20:11")], "JDG 20:8–11", ISRAELITE, bg=RED),
        drawn([cp("20:12", to="saying,"), ("say", v("20:12", frm="What wickedness") + " " + v("20:13", to="put away evil from Israel.")), cp("20:13", frm="But Benjamin")], "JDG 20:12–13",
              lambda w, h: JA.ai("gb10", w, h, 1012), "#F3D8A0"),
        drawn([caps("20:14-17")], "JDG 20:14–17", lambda w, h: JA.armed("ar10b", w, h, 1013, tribes=("BENJAMIN",)), "#F3D8A0", head="Seven Hundred Chosen Men Lefthanded"),
        drawn([cp("20:18", to="and they said,"), say("20:18", frm="Who shall go up", to="children of Benjamin?"), cp("20:18", frm="And Jehovah said,", to="And Jehovah said,"),
               gd("20:18", frm="Judah shall go up first."), caps("20:19-21")], "JDG 20:18–21", lambda w, h: JA.shiloh("bt10", w, h, 1014), "#E8D8B0"),
        drawn([caps("20:22"), cp("20:23", to="saying,"), say("20:23", frm="Shall I again", to="my brother?"), cp("20:23", frm="And Jehovah said,", to="And Jehovah said,"),
               gd("20:23", frm="Go up against him."), caps("20:24-25")], "JDG 20:22–25", lambda w, h: D4.weeping(w, h, 1015), "#3A3450"),
        drawn([caps("20:26-27")], "JDG 20:26–27", lambda w, h: D4.weeping(w, h, 1016), "#3A3450", head="Shall I Yet Again Go Out?"),
        face([cp("20:28", to="saying,"), say("20:28", frm="Shall I yet", to="or shall I cease?"), cp("20:28", frm="And Jehovah said,", to="And Jehovah said,"), gd("20:28", frm="Go up;")],
             "JDG 20:28", PHINEHAS),
        drawn([caps("20:29-31"), cp("20:32", to="And the children of Benjamin said,"), say("20:32", frm="They are smitten", to="at the first."),
               cp("20:32", frm="But the children of Israel said,", to="But the children of Israel said,"), say("20:32", frm="Let us flee,")], "JDG 20:29–32",
              K.below(lambda w, h: K.gibeah_plan(w, h), 0.5), MAP, head="The Third Day"),
        drawn([caps("20:33-36")], "JDG 20:33–36", K.below(lambda w, h: K.gibeah_plan(w, h), 0.34), MAP),
        drawn([caps("20:37-41")], "JDG 20:37–41", K.below(lambda w, h: K.gibeah_plan(w, h, stage=1), 0.4), MAP),
        drawn([caps("20:42-46")], "JDG 20:42–46", lambda w, h: JA.burning(w, h, 1017, city="gibeah"), "#2A0A0A"),
        drawn([caps("20:47-48")], "JDG 20:47–48", K.below(lambda w, h: K.rimmon("rm10", w, h, 1018), 0.3), "#E8B880", head="The Rock of Rimmon"),
        drawn([caps("21:1-2"), cp("21:3", to="And they said,"), say("21:3", frm="O Jehovah,"), caps("21:4")], "JDG 21:1–4", lambda w, h: D4.weeping(w, h, 1019), "#3A3450",
              head="One Tribe Lacking in Israel", stamp=21),
        face([cp("21:5", to="And the children of Israel said,"), say("21:5", frm="Who is there", to="unto Jehovah?"), cp("21:5", frm="For they had", to="saying,"),
              say("21:5", frm="He shall surely"), cp("21:6", to="and said,"), ("say", v("21:6", frm="There is one") + " " + v("21:7"))], "JDG 21:5–7", ELDER),
        drawn([cp("21:8", to="And they said,"), say("21:8", frm="What one", to="to Mizpah?"), cp("21:8", frm="And, behold,"), caps("21:9"), cp("21:10", to="saying,"),
               ("say", v("21:10", frm="Go and smite") + " " + v("21:11"))], "JDG 21:8–11", NIGHTA, "#0B0B2A", head="Jabesh-gilead"),
        drawn([caps("21:12-15")], "JDG 21:12–15", lambda w, h: JA.burning(w, h, 1020, city="jabesh"), "#2A0A0A"),
        face([cp("21:16", to="Then the elders of the congregation said,"), say("21:16", frm="How shall we do"), cp("21:17", to="And they said,"), ("say", v("21:17", frm="There must be") + " " + v("21:18"))],
             "JDG 21:16–18", ELDER, head="The Daughters of Shiloh"),
        face([cp("21:19", to="And they said,"), say("21:19", frm="Behold,"), cp("21:20", to="saying,"), ("say", v("21:20", frm="Go and lie") + " " + sp("21:21-22"))], "JDG 21:19–22", ELDER, bg=COLD),
        drawn([caps("21:23-24")], "JDG 21:23–24", lambda w, h: K.dances("dc10", w, h, 1021), "#F3D8A0"),
        drawn([caps("21:25")], "JDG 21:25", lambda w, h: K.baalim(w, h, 1022), "#5A1A2A", head="Every Man Did That Which Was Right in His Own Eyes")]
PG.extend(pack(SEGS, "JDG-C10-D", PG.next(), end=end_mark("END OF JUDGES · NEXT · RUTH", "right: 10px; bottom: 34px", ch="完")))
