"""2 Kings volume, Chapter 8 — Ahaz (2 Kings 15–16). Every verse, word for word from ref/asv.
The reigns of Azariah the leper king, and of Zechariah, Shallum, Menahem, Pekahiah, Pekah and Jotham
as roll cells (the conspiracies in words only); Pul and Tiglath-pileser of Assyria on a technical map; then Ahaz — his son
passed through the fire (16:3 words only), the siege by Rezin and Pekah, I am thy servant and thy son; the altar after the
fashion of Damascus (a blueprint), and the sea set down upon a pavement of stone."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg2 import G, art as K
from kg2.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, F, reign, reign_pages, RED, COLD, GOLDEN)
from kg2 import ch07 as _prev

v, sp = G.v, G.span
AHAZ = F("adam", skin="#D9A27A", shadow="#5A3A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#1F3A7A", band=True, brow="scowl", light="#FF8A3D")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, INK = "#0B1A2E", "#0B1A2E"


@P("2KI-C08-00-Title", "Chapter 8 · Ahaz", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#0B1A2E"></rect><g transform="translate(0 300)">{K.assyria_map(760, 780, hi=("DAMASCUS",), arrows=(("NINEVEH", "DAMASCUS"),))}</g>')
    return chapter_title(8, "第八話", "Ahaz", "2 Kings 15 – 16", svg, "#0B1A2E", v("16:7", frm="I am thy servant", to="thy son:"), "2 Kings · Volume Twelve")


R = [reign("Azariah, King of Judah", "15:1-4", head="The Kings of Judah and of Israel"), reign("Azariah, a Leper", "15:5-7"), reign("Zechariah, King of Israel", "15:8-12", judah=False),
     reign("Shallum", "15:13-15", judah=False), reign("Menahem", "15:16-18", judah=False), reign("Menahem and Pul the King of Assyria", "15:19-22", judah=False),
     reign("Pekahiah", "15:23-26", judah=False), reign("Pekah", "15:27-28", judah=False), reign("Pekah and Tiglath-pileser", "15:29-31", judah=False),
     reign("Jotham, King of Judah", "15:32-35"), reign("Jotham", "15:36-38")]
PG.extend(reign_pages(R, "2KI-C08-R", PG.next()))
SEGS4 = [face([caps("16:1-4")], "2KGS 16:1–4", AHAZ, bg=RED, head="Ahaz", stamp=16),
         drawn([caps("16:5-6")], "2KGS 16:5–6", below(lambda w, h: K.siege_wall("sw8", w, h, 802, king=False), 0.3), "#5A4A4A"),
         drawn([cp("16:7", to="saying,"), say("16:7", frm="I am thy servant"), caps("16:8-9")], "2KGS 16:7–9",
               below(lambda w, h: K.assyria_map(w, h, hi=("DAMASCUS", "KIR"), arrows=(("NINEVEH", "DAMASCUS"), ("DAMASCUS", "KIR"))), 0.4), MAP),
         drawn([caps("16:10-11")], "2KGS 16:10–11", below(lambda w, h: K.two_altars(w, h), 0.3), INK, head="The Altar at Damascus"),
         drawn([caps("16:12-14")], "2KGS 16:12–14", below(lambda w, h: K.two_altars(w, h), 0.3), INK),
         face([cp("16:15", to="saying,"), say("16:15", frm="Upon the great altar"), caps("16:16")], "2KGS 16:15–16", AHAZ),
         drawn([caps("16:17-18")], "2KGS 16:17–18", below(lambda w, h: K.sea_pavement(w, h), 0.3), INK),
         drawn([caps("16:19-20")], "2KGS 16:19–20", lambda w, h: K.city_dusk("cd8", w, h, 803), "#2A1A3A")]
PG.extend(pack(SEGS4, "2KI-C08-G", PG.next(), end=end_mark("NEXT · CARRIED AWAY INTO ASSYRIA", "right: 10px; bottom: 34px")))
