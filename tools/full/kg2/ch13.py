"""2 Kings volume, Chapter 13 — The Fall of Jerusalem (2 Kings 24–25), the last chapter of 2 Kings. Every verse, word for word
from ref/eng-asv. Nebuchadnezzar and the bands of the Chaldeans; Jehoiachin carried away with the treasures and ten thousand
captives; Zedekiah; the siege and the forts; the breach and the flight by the Arabah; Riblah (25:7 words only); the house of
Jehovah burned and the walls broken down; the pillars and the sea broken in pieces; Riblah again (25:21 words only); Gedaliah
at Mizpah (25:25 words only); and Jehoiachin lifted up out of prison, eating bread before the king of Babylon continually."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg2 import G, art as K
from kg2.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, ZEDEKIAH, GEDALIAH, JEHOIACHIN, reign, reign_pages, RED, COLD, GOLDEN)
from kg2 import ch12 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, INK = "#0B1A2E", "#0B1A2E"


@P("2KI-C13-00-Title", "Chapter 13 · The Fall of Jerusalem", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#2A0A0A"></rect><g transform="translate(0 320)">{K.burning_city(760, 760, 1301)}</g>')
    return chapter_title(13, "第十三話", "The Fall of Jerusalem", "2 Kings 24 – 25", svg, "#2A0A0A", v("25:9", to="the king's house;"), "2 Kings · Volume Twelve")


SEGS = [drawn([caps("24:1-4")], "2KGS 24:1–4", below(lambda w, h: K.siege_forts("sf13", w, h, 1302), 0.4), "#5A4A5A", head="Nebuchadnezzar King of Babylon", stamp=24)]
SEGS2 = SEGS + [drawn([caps("24:5-9")], "2KGS 24:5–9", lambda w, h: K.city_dusk("cd13", w, h, 1314), "#2A1A3A"),
         drawn([caps("24:10-12")], "2KGS 24:10–12", below(lambda w, h: K.siege_forts("sf13b", w, h, 1303), 0.3), "#5A4A5A", head="Jehoiachin Carried Away"),
         drawn([caps("24:13")], "2KGS 24:13", below(lambda w, h: K.K2.vessels(w, h, 1304), 0.2), "#2A1A3A"),
         drawn([caps("24:14-16")], "2KGS 24:14–16", below(lambda w, h: K.captives("cp13", w, h, 1305), 0.34), "#5A4A5A"),
         face([caps("24:17-20")], "2KGS 24:17–20", ZEDEKIAH, bg=COLD, head="Zedekiah"),
         drawn([caps("25:1-3")], "2KGS 25:1–3", below(lambda w, h: K.siege_forts("sf13c", w, h, 1306), 0.3), "#5A4A5A", head="The Siege", stamp=25),
         drawn([caps("25:4-5")], "2KGS 25:4–5", below(lambda w, h: K.siege_wall("sw13", w, h, 1307, king=False), 0.3), "#5A4A4A"),
         drawn([caps("25:6-7")], "2KGS 25:6–7", lambda w, h: K.megiddo("rb13", w, h, 1308), "#2A1A2A"),
         drawn([caps("25:8-10")], "2KGS 25:8–10", below(lambda w, h: K.burning_city(w, h, 1309), 0.3), "#2A0A0A", head="The House of Jehovah Burned"),
         drawn([caps("25:11-12")], "2KGS 25:11–12", below(lambda w, h: K.captives("cp13b", w, h, 1310), 0.24), "#5A4A5A"),
         drawn([caps("25:13-15")], "2KGS 25:13–15", below(lambda w, h: K.brass_carried("bc13", w, h, 1311), 0.36), "#5A3A2A"),
         drawn([caps("25:16-17")], "2KGS 25:16–17", below(lambda w, h: K.pillar_elev(w, h), 0.4), INK),
         drawn([caps("25:18-21")], "2KGS 25:18–21", below(lambda w, h: K.captives("cp13c", w, h, 1315), 0.44), "#5A4A5A"),
         drawn([caps("25:22-23")], "2KGS 25:22–23", below(lambda w, h: K.mizpah("mz13", w, h, 1312), 0.4), "#8FD0E2", head="Gedaliah"),
         face([cp("25:24", to="and said unto them,"), say("25:24", frm="Fear not"), caps("25:25-26")], "2KGS 25:24–26", GEDALIAH),
         face([caps("25:27-28")], "2KGS 25:27–28", JEHOIACHIN, head="All the Days of His Life"),
         drawn([caps("25:29-30")], "2KGS 25:29–30", below(lambda w, h: K.prison_garments("pg13", w, h, 1313), 0.3), "#5A2A1E")]
PG.extend(pack(SEGS2, "2KI-C13-D", PG.next(), end=end_mark("END OF 2 KINGS · NEXT · 1 CHRONICLES", "right: 10px; bottom: 34px", ch="完")))
