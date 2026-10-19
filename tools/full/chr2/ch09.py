"""2 Chronicles volume, Chapter 9 — Amaziah and Uzziah (2 Chronicles 25–27). Every verse, word for word from ref/asv.
Amaziah, right but not with a perfect heart — every man shall die for his own sin; the hundred talents and the man of God —
Jehovah is able to give thee much more than this; the Valley of Salt (25:11–12 words over the rock of Seir, no one drawn);
the gods of Seir and the prophet silenced; the thistle and the cedar; Beth-shemesh and the wall broken down; then Uzziah, who
sought God in the days of Zechariah — towers and cisterns, for he loved husbandry, and engines on the battlements (a
blueprint); his heart lifted up, the censer in the temple, Azariah and the fourscore priests, the leprosy in his forehead
(his face in pale light); and Jotham who ordered his ways before Jehovah."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from chr2 import G, art as K
from chr2.common import (pack, cp, say, gd, says, gods, caps, drawn, face, joined, cell, cells, roll, F, AMAZIAH, UZZIAH, UZZIAH_LEPER, PROPHET, COLD, GOLDEN, RED)
from chr2 import ch08 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, INK = "#0B1A2E", "#0B1A2E"
MAN_OF_GOD = PROPHET
JOASH_I = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#3A5A2A", band=True, light="#FFC14D")
AZARIAH_PRIEST = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#C8C2B6", hl="#E8E2D6", beard=True, beard_color="#D8D2C6", scarf="#F3EFE6", band=True, brow="scowl", light="#FFE680")
JOTHAM = F("adam", skin="#D9A27A", shadow="#6A4A3A", hair="#2A1A10", hl="#5A4A3E", stubble="#2A1A10", scarf="#1F3A7A", band=True, light="#FFE680")


@P("2CH-C09-00-Title", "Chapter 9 · Amaziah and Uzziah", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.censer_altar("t9", 760, 820, 901)}</g><rect x="0" y="0" width="760" height="262" fill="#5A3A1A"></rect>')
    return chapter_title(9, "第九話", "Amaziah and Uzziah", "2 Chronicles 25 – 27", svg, "#5A3A1A", v("26:16", to="his heart was lifted up,"), "2 Chronicles · Volume Fourteen")


SEGS = [face([caps("25:1-4")], "2CHR 25:1–4", AMAZIAH, head="Amaziah", stamp=25),
        drawn([caps("25:5-6")], "2CHR 25:5–6", below(lambda w, h: K.K3.silver_bags("sb9", w, h, 902), 0.4), "#5A3A2A"),
        face([cp("25:7", to="saying,"), say("25:7", frm="O king,"), says("25:8")], "2CHR 25:7–8", MAN_OF_GOD),
        face([cp("25:9", to="to the man of God,"), say("25:9", frm="But what", to="army of Israel?"), cp("25:9", frm="And the man of God answered,", to="answered,"), say("25:9", frm="Jehovah is able")],
             "2CHR 25:9", AMAZIAH),
        drawn([caps("25:10-11")], "2CHR 25:10–11", below(lambda w, h: K.K2.wars_map(w, h, hi=("VALLEY OF SALT",)), 0.36), MAP),
        drawn([caps("25:12-13")], "2CHR 25:12–13", below(lambda w, h: K.rock_top(w, h, 903), 0.36), "#5A3A4A"),
        drawn([caps("25:14"), cp("25:15", to="who said unto him,"), say("25:15", frm="Why hast thou")], "2CHR 25:14–15", below(lambda w, h: K.idols_edom("ie9", w, h, 904), 0.4), "#2A1A2A",
              head="The Gods of the Children of Seir"),
        face([cp("25:16", to="that the king said unto him,"), say("25:16", frm="Have we made", to="smitten?"), cp("25:16", frm="Then the prophet forbare, and said,", to="and said,"),
              say("25:16", frm="I know that God")], "2CHR 25:16", AMAZIAH, bg=RED),
        face([cp("25:17", to="saying,"), say("25:17", frm="Come, let us")], "2CHR 25:17", AMAZIAH, head="The Thistle and the Cedar"),
        drawn([cp("25:18", to="saying,"), say("25:18", frm="The thistle"), says("25:19")], "2CHR 25:18–19", lambda w, h: K.thistle_cedar(w, h, 905), "#8FD0E2"),
        drawn([caps("25:20-22")], "2CHR 25:20–22", below(lambda w, h: K.to_tents("tt9", w, h, 906), 0.4), "#C8B8A0"),
        drawn([caps("25:23-24")], "2CHR 25:23–24", below(lambda w, h: K.wall_breach(w, h, 907), 0.4), "#8FD0E2"),
        drawn([caps("25:25-28")], "2CHR 25:25–28", lambda w, h: K.city_dusk("cd9", w, h, 908), "#2A1A3A")]
PG.extend(pack(SEGS, "2CH-C09-D", PG.next()))
SEGS2 = [face([caps("26:1-5")], "2CHR 26:1–5", UZZIAH, head="Uzziah", stamp=26),
         drawn([caps("26:6-8")], "2CHR 26:6–8", below(lambda w, h: K.K2.wars_map(w, h, hi=("GATH",)), 0.36), MAP),
         drawn([caps("26:9-10")], "2CHR 26:9–10", below(lambda w, h: K.vine_fig("vf9", w, h, 909), 0.36), "#8FD0E2", head="He Loved Husbandry"),
         drawn([caps("26:11-13")], "2CHR 26:11–13", below(lambda w, h: K.tally(w, h, [("HEADS", "2,600", "#FFD23F"), ("THE ARMY", "307,500", "#8FD0E2")]), 0.4), "#1A1430"),
         drawn([caps("26:14-15")], "2CHR 26:14–15", below(lambda w, h: K.towers_engines(w, h, 910), 0.36), INK, head="Engines Invented by Skilful Men"),
         drawn([caps("26:16-17")], "2CHR 26:16–17", below(lambda w, h: K.censer_altar("ca9", w, h, 911), 0.36), "#5A3A1A", head="His Heart Was Lifted Up"),
         face([cp("26:18", to="and said unto him,"), say("26:18", frm="It pertaineth")], "2CHR 26:18", AZARIAH_PRIEST),
         face([caps("26:19-20")], "2CHR 26:19–20", UZZIAH_LEPER, bg=COLD),
         drawn([caps("26:21")], "2CHR 26:21", below(lambda w, h: K.separate_house("sh9", w, h, 912), 0.36), "#8A9AB8"),
         drawn([cp("26:22"), cp("26:23", to="for they said,"), say("26:23", frm="He is a leper:", to="He is a leper:"), cp("26:23", frm="and Jotham his son")], "2CHR 26:22–23",
               lambda w, h: K.city_dusk("cd9b", w, h, 913), "#2A1A3A")]
PG.extend(pack(SEGS2, "2CH-C09-E", PG.next()))
SEGS3 = [face([caps("27:1-4")], "2CHR 27:1–4", JOTHAM, head="Jotham", stamp=27),
         drawn([caps("27:5-6")], "2CHR 27:5–6", below(lambda w, h: K.tribute("tb9", w, h, 914), 0.4), "#FFE680"),
         face([caps("27:7-9")], "2CHR 27:7–9", JOTHAM, bg=COLD)]
PG.extend(pack(SEGS3, "2CH-C09-F", PG.next(), end=end_mark("NEXT · AHAZ AND HEZEKIAH", "right: 10px; bottom: 34px")))
