"""2 Kings volume, Chapter 9 — Carried Away into Assyria (2 Kings 17). Every verse, word for word from ref/asv.
Hoshea, Shalmaneser and the three years' siege of Samaria; Israel carried away to Halah, the Habor and the cities of the
Medes (a technical map and the column of captives); because the children of Israel had sinned — the high places, the
pillars and Asherim, the two calves, the host of heaven (17:17 words only); the nations brought into Samaria, the lions,
the priest at Beth-el; every nation making gods of its own; and Jehovah's covenant: him shall ye fear (the Voice box)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg2 import G, art as K
from kg2.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, F, reign, reign_pages, RED, COLD, GOLDEN)
from kg2 import ch08 as _prev

v, sp = G.v, G.span
HOSHEA = F("adam", skin="#C98E66", shadow="#3A2A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#7A1A2A", band=True, brow="sorrow", sweat=True, light="#9AA8C8")
ASSYRIAN = F("adam", skin="#B98A6E", shadow="#4A2A2A", hair="#0D0D0F", hl="#2A2220", beard=True, beard_color="#0D0D0F", scarf="#8A5A1A", band=True, brow="scowl", light="#D7261E")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"


@P("2KI-C09-00-Title", "Chapter 9 · Carried Away into Assyria", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#5A4A5A"></rect><g transform="translate(0 340)">{K.captives("t9", 760, 740, 901)}</g>')
    return chapter_title(9, "第九話", "Carried Away into Assyria", "2 Kings 17", svg, "#5A4A5A", v("17:23", frm="So Israel was carried away"), "2 Kings · Volume Twelve")


SEGS = [face([caps("17:1-4")], "2KGS 17:1–4", HOSHEA, bg=COLD, head="Hoshea", stamp=17),
        drawn([caps("17:5-6")], "2KGS 17:5–6", below(lambda w, h: K.exile_map(w, h), 0.24), MAP, head="Samaria Taken"),
        drawn([caps("17:7-8")], "2KGS 17:7–8", below(lambda w, h: K.captives("cp9", w, h, 902), 0.3), "#5A4A5A", head="Because They Had Sinned"),
        drawn([caps("17:9-12")], "2KGS 17:9–12", below(lambda w, h: K.high_places("hp9", w, h, 903), 0.36), "#3A1A3A"),
        drawn([cp("17:13", to="saying,"), gd("17:13", frm="Turn ye"), caps("17:14-15")], "2KGS 17:13–15", lambda w, h: K.K2.throne_glory(w, h, 904), "#14123A"),
        drawn([caps("17:16-17")], "2KGS 17:16–17", below(lambda w, h: K.calves("cv9", w, h, 905, people=False), 0.4), "#5A3A5A"),
        drawn([caps("17:18-20")], "2KGS 17:18–20", lambda w, h: K.captives("cp9b", w, h, 906), "#5A4A5A"),
        drawn([caps("17:21-23")], "2KGS 17:21–23", below(lambda w, h: K.exile_map(w, h), 0.3), MAP),
        drawn([caps("17:24-25")], "2KGS 17:24–25", below(lambda w, h: K.exile_map(w, h, inward=True), 0.3), MAP, head="Strangers in the Cities of Samaria"),
        face([cp("17:26", to="saying,"), say("17:26", frm="The nations"), cp("17:27", to="saying,"), say("17:27", frm="Carry thither")], "2KGS 17:26–27", ASSYRIAN, bg=RED),
         drawn([caps("17:28-29")], "2KGS 17:28–29", below(lambda w, h: K.lions_samaria("ls9", w, h, 907), 0.3), "#C8B8A0"),
         drawn([caps("17:30-33")], "2KGS 17:30–33", below(lambda w, h: K.strange_gods(w, h, 908), 0.4), "#3A2A3A"),
         drawn([caps("17:34"), cp("17:35", to="saying,"), gd("17:35", frm="Ye shall not fear"), gods("17:36-39")], "2KGS 17:34–39", lambda w, h: K.K2.throne_glory(w, h, 909), "#14123A",
               head="Him Shall Ye Fear"),
         drawn([caps("17:40-41")], "2KGS 17:40–41", below(lambda w, h: K.strange_gods(w, h, 910), 0.3), "#3A2A3A")]
PG.extend(pack(SEGS, "2KI-C09-D", PG.next(), end=end_mark("NEXT · HEZEKIAH", "right: 10px; bottom: 34px")))
