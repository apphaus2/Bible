"""1 Kings volume, Chapter 13 — A Still Small Voice (1 Kings 19–20). Every verse, word for word from ref/asv.
Jezebel's oath; Elijah under the juniper-tree — it is enough; the angel and the cake baken on the coals; forty days to Horeb;
what doest thou here, Elijah?; the wind, the earthquake, the fire, and a still small voice; seven thousand that have not
bowed unto Baal; the mantle cast upon Elisha at the plough. Then Ben-hadad and the thirty and two kings before Samaria — let
not him that girdeth on his armor boast; the young men of the princes; the god of the hills and the valleys at Aphek;
Ben-hadad's servants with ropes on their heads; the prophet with the headband (20:36–37 in words only)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos import art as JA
from jos.art import below
from kg1 import G, art as K
from kg1.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, F, AHAB, AHAB_SAD, ELIJAH, ELIJAH_WEARY, ELISHA, JEZEBEL, PROPHET, MESSENGER,
                        RED, COLD, GOLDEN)
from kg1 import ch12 as _prev

v, sp = G.v, G.span
BENHADAD = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#5A3A6A", band=True, brow="scowl", light="#D7261E")
SYRIAN = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#5A3A6A", cord=True, light="#FFC14D")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#14123A"


@P("1KI-C13-00-Title", "Chapter 13 · A Still Small Voice", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#5A5A7A"></rect><g transform="translate(0 300)">{K.horeb_cave("t13", 760, 780, 1301, stage="still")}</g>')
    return chapter_title(13, "第十三話", "A Still Small Voice", "1 Kings 19 – 20", svg, "#5A5A7A", v("19:12", frm="and after the fire"), "1 Kings · Volume Eleven")


SEGS = [face([caps("19:1"), cp("19:2", to="saying,"), say("19:2", frm="So let the gods")], "1KGS 19:1–2", JEZEBEL, bg=RED, head="Jezebel", stamp=19),
        drawn([caps("19:3"), cp("19:4", to="and said,"), say("19:4", frm="It is enough;")], "1KGS 19:3–4", below(lambda w, h: K.juniper("jn13", w, h, 1302), 0.36), "#E8B880",
              head="Under a Juniper-tree"),
        drawn([cp("19:5", to="and said unto him,"), say("19:5", frm="Arise and eat."), caps("19:6"), cp("19:7", to="and said,"), say("19:7", frm="Arise and eat,"), caps("19:8")], "1KGS 19:5–8",
              below(lambda w, h: K.juniper("jn13b", w, h, 1303, angel=True), 0.44), "#2A2A5A"),
        drawn([cp("19:9", to="and he said unto him,"), gd("19:9", frm="What doest thou")], "1KGS 19:9", lambda w, h: K.horeb_cave("hc13", w, h, 1304), "#2A2A4A", head="Horeb the Mount of God"),
        face([cp("19:10", to="And he said,"), say("19:10", frm="I have been")], "1KGS 19:10", ELIJAH_WEARY, bg=COLD),
        drawn([cp("19:11", to="And he said,"), gd("19:11", frm="Go forth,", to="before Jehovah."), cp("19:11", frm="And, behold,", to="before Jehovah;", after="mount before Jehovah.")], "1KGS 19:11",
              lambda w, h: K.horeb_cave("hc13w", w, h, 1305, stage="wind"), "#2A2A4A"),
        drawn([cp("19:11", frm="but Jehovah was not in the wind:")], "1KGS 19:11", lambda w, h: K.horeb_cave("hc13q", w, h, 1306, stage="quake"), "#2A2A4A"),
        drawn([cp("19:12", to="but Jehovah was not in the fire:")], "1KGS 19:12", lambda w, h: K.horeb_cave("hc13f", w, h, 1307, stage="fire"), "#2A2A4A"),
        drawn([cp("19:12", frm="and after the fire"), cp("19:13", to="and said,"), gd("19:13", frm="What doest thou")], "1KGS 19:12–13",
              below(lambda w, h: K.horeb_cave("hc13s", w, h, 1308, stage="still"), 0.26), "#5A5A7A", head="A Still Small Voice"),
        face([cp("19:14", to="And he said,"), say("19:14", frm="I have been")], "1KGS 19:14", ELIJAH_WEARY, bg=COLD),
        drawn([cp("19:15", to="And Jehovah said unto him,"), joined("god", ("19:15", "Go, return"), "19:16", "19:17", "19:18")], "1KGS 19:15–18",
              lambda w, h: __import__("sa2.art", fromlist=["x"]).throne_glory(w, h, 1309), "#14123A"),
        drawn([caps("19:19")], "1KGS 19:19", below(lambda w, h: K.plowing("pl13", w, h, 1310, mantle=True), 0.2), "#8FD0E2", head="Elisha the Son of Shaphat"),
        face([cp("19:20", to="and said,"), say("19:20", frm="Let me,", to="follow thee."), cp("19:20", frm="And he said unto him,", to="said unto him,"), say("19:20", frm="Go back again;"), caps("19:21")],
             "1KGS 19:20–21", ELISHA),
        drawn([caps("20:1"), cp("20:2", to="and said unto him,"), say("20:2", frm="Thus saith"), says("20:3")], "1KGS 20:1–3", below(lambda w, h: K.pavilions("pv13", w, h, 1311), 0.4), "#C8B8A0",
              head="Ben-hadad King of Syria", stamp=20),
        face([cp("20:4", to="answered and said,"), say("20:4", frm="It is according"), cp("20:5", to="and said,"), joined("say", ("20:5", "Thus speaketh"), "20:6")], "1KGS 20:4–6", AHAB_SAD, bg=COLD),
        face([cp("20:7", to="and said,"), say("20:7", frm="Mark,"), cp("20:8", to="said unto him,"), say("20:8", frm="Hearken thou not,")], "1KGS 20:7–8", AHAB),
        face([cp("20:9", to="the messengers of Ben-hadad,"), say("20:9", frm="Tell my lord", to="I may not do."), cp("20:9", frm="And the messengers departed,")], "1KGS 20:9", AHAB),
        face([cp("20:10", to="and said,"), say("20:10", frm="The gods do so"), cp("20:11", to="answered and said,"), say("20:11", frm="Tell him,")], "1KGS 20:10–11", BENHADAD, bg=RED),
        drawn([cp("20:12", to="unto his servants,"), say("20:12", frm="Set yourselves", to="in array."), cp("20:12", frm="And they set themselves")], "1KGS 20:12",
              below(lambda w, h: K.pavilions("pv13b", w, h, 1312), 0.3), "#C8B8A0"),
        face([cp("20:13", to="and said,"), say("20:13", frm="Thus saith Jehovah,", to="Thus saith Jehovah,"), gd("20:13", frm="Hast thou seen"), cp("20:14", to="And Ahab said,"), say("20:14", frm="By whom?", to="By whom?"),
              cp("20:14", frm="And he said,", to="And he said,"), say("20:14", frm="Thus saith Jehovah,", to="Thus saith Jehovah,"), gd("20:14", frm="By the young men", to="provinces."),
              cp("20:14", frm="Then he said,", to="Then he said,"), say("20:14", frm="Who shall begin", to="the battle?"), cp("20:14", frm="And he answered,", to="And he answered,"), say("20:14", frm="Thou.")],
             "1KGS 20:13–14", PROPHET)]
SEGS += [drawn([caps("20:15-16"), cp("20:17", to="saying,"), say("20:17", frm="There are men"), cp("20:18", to="And he said,"), say("20:18", frm="Whether they")], "1KGS 20:15–18",
               below(lambda w, h: JA.armed("ar13", w, h, 1313, tribes=()), 0.4), "#F3D8A0", head="The Young Men of the Princes"),
         drawn([caps("20:19-21")], "1KGS 20:19–21", lambda w, h: JA.chariots("ch13", w, h, 1314), "#8FD0E2"),
         face([cp("20:22", to="and said unto him,"), say("20:22", frm="Go,")], "1KGS 20:22", PROPHET),
         face([cp("20:23", to="said unto him,"), joined("say", ("20:23", "Their god"), "20:24", ("20:25", "and number thee", "stronger than they.")), cp("20:25", frm="And he hearkened")],
              "1KGS 20:23–25", SYRIAN, bg=RED, head="A God of the Hills"),
         drawn([caps("20:26-27")], "1KGS 20:26–27", below(lambda w, h: K.two_flocks(w, h), 0.3), "#0B1A2E"),
         face([cp("20:28", to="and said,"), say("20:28", frm="Thus saith Jehovah,", to="Thus saith Jehovah,"), gd("20:28", frm="Because the Syrians")], "1KGS 20:28", PROPHET),
         drawn([caps("20:29-30")], "1KGS 20:29–30", lambda w, h: JA.burning(w, h, 1315, city="aphek"), "#2A0A0A"),
         face([cp("20:31", to="said unto him,"), say("20:31", frm="Behold now,")], "1KGS 20:31", SYRIAN, bg=COLD, head="Ropes upon Their Heads"),
         drawn([cp("20:32", to="and said,"), say("20:32", frm="Thy servant", to="let me live."), cp("20:32", frm="And he said,", to="And he said,"), say("20:32", frm="Is he yet alive?"),
                cp("20:33", to="and they said,"), say("20:33", frm="Thy brother Ben-hadad.", to="Thy brother Ben-hadad."), cp("20:33", frm="Then he said,", to="Then he said,"), say("20:33", frm="Go ye, bring him.", to="Go ye, bring him."),
                cp("20:33", frm="Then Ben-hadad came")], "1KGS 20:32–33", below(lambda w, h: K.ropes("rp13", w, h, 1316), 0.5), "#C8B8A0"),
         face([cp("20:34", to="said unto him,"), say("20:34", frm="The cities", to="in Samaria."), say("20:34", frm="And I,", to="And I,"), cp("20:34", frm="said Ahab,", to="said Ahab,"),
               say("20:34", frm="will let thee go", to="covenant."), cp("20:34", frm="So he made")], "1KGS 20:34", BENHADAD),
         face([cp("20:35", to="by the word of Jehovah,"), say("20:35", frm="Smite me,", to="I pray thee."), cp("20:35", frm="And the man refused"), cp("20:36", to="Then said he unto him,"),
               say("20:36", frm="Because thou", to="shall slay thee."), cp("20:36", frm="And as soon as"), cp("20:37", to="and said,"), say("20:37", frm="Smite me,", to="I pray thee."), cp("20:37", frm="And the man smote him,")],
              "1KGS 20:35–37", PROPHET, head="Thy Life for His Life"),
         drawn([caps("20:38"), cp("20:39", to="and he said,"), say("20:39", frm="Thy servant went"), say("20:40", to="he was gone."), cp("20:40", frm="And the king of Israel said", to="said unto him,"),
                say("20:40", frm="So shall")], "1KGS 20:38–40", below(lambda w, h: K.headband("hb13", w, h, 1317), 0.5), "#E8C8A0"),
         face([caps("20:41"), cp("20:42", to="And he said unto him,"), say("20:42", frm="Thus saith Jehovah,", to="Thus saith Jehovah,"), gd("20:42", frm="Because thou"), caps("20:43")], "1KGS 20:41–43", PROPHET)]
PG.extend(pack(SEGS, "1KI-C13-D", PG.next(), end=end_mark("NEXT · NABOTH'S VINEYARD", "right: 10px; bottom: 34px")))
