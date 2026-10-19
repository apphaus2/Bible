"""2 Chronicles volume, Chapter 10 — Ahaz and Hezekiah (2 Chronicles 28–29). Every verse, word for word from ref/asv.
Ahaz who walked in the ways of the kings of Israel (28:3 words only); Syria and Pekah, and two hundred thousand carried
captive to Samaria (28:5–8 words over the column of captives); Oded the prophet — send back the captives; the captives
clothed and carried on asses to Jericho, the city of palm-trees; Ahaz and the king of Assyria, the gods of Damascus, the
vessels cut in pieces and the doors shut; then Hezekiah opening the doors in the first month — hear me, ye Levites; the
house cleansed, the sin-offering for all Israel, the song of Jehovah with the instruments of David, and the thank-offerings
— for the thing was done suddenly."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from chr2 import G, art as K
from chr2.common import (pack, cp, say, gd, says, gods, caps, drawn, face, joined, cell, cells, roll, F, AHAZ, ODED, HEZEKIAH, ISRAELITE, COLD, GOLDEN, RED)
from chr2 import ch09 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
EPHRAIMITE = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#3A3430", scarf="#3A5A2A", cord=True, brow="sorrow", light="#FFC14D")


@P("2CH-C10-00-Title", "Chapter 10 · Ahaz and Hezekiah", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.shut_doors(760, 820, 1001, open_=True)}</g><rect x="0" y="0" width="760" height="262" fill="#FFE680"></rect>')
    return chapter_title(10, "第十話", "Ahaz and Hezekiah", "2 Chronicles 28 – 29", svg, "#C8902A", v("29:3", frm="opened the doors"), "2 Chronicles · Volume Fourteen")


SEGS = [face([caps("28:1-4")], "2CHR 28:1–4", AHAZ, bg=RED, head="Ahaz", stamp=28),
        drawn([caps("28:5-6")], "2CHR 28:5–6", below(lambda w, h: K.K3.captives("cp10", w, h, 1002), 0.36), "#5A4A5A"),
        drawn([caps("28:7-8")], "2CHR 28:7–8", below(lambda w, h: K.K3.captives("cp10b", w, h, 1003), 0.3), "#5A4A5A"),
        face([cp("28:9", to="and said unto them,"), say("28:9", frm="Behold,"), says("28:10-11")], "2CHR 28:9–11", ODED, head="Oded the Prophet"),
        face([caps("28:12"), cp("28:13", to="and said unto them,"), say("28:13", frm="Ye shall not"), caps("28:14")], "2CHR 28:12–14", EPHRAIMITE),
        drawn([caps("28:15")], "2CHR 28:15", below(lambda w, h: K.captives_clothed("cc10", w, h, 1004), 0.36), "#8FD0E2", head="The City of Palm-trees"),
        drawn([caps("28:16-19")], "2CHR 28:16–19", below(lambda w, h: K.assyria_map(w, h), 0.44), MAP),
        drawn([caps("28:20-21")], "2CHR 28:20–21", below(lambda w, h: K.K3.treasures("tr10", w, h, 1005), 0.3), "#5A2A1E"),
        drawn([caps("28:22"), cp("28:23", to="and he said,"), say("28:23", frm="Because the gods", to="help me."), cp("28:23", frm="But they were")], "2CHR 28:22–23",
              below(lambda w, h: K.two_altars(w, h), 0.4), "#0B1A2E", head="The Gods of Damascus"),
        drawn([caps("28:24-25")], "2CHR 28:24–25", below(lambda w, h: K.shut_doors(w, h, 1006), 0.3), "#3A2A3A"),
        drawn([caps("28:26-27")], "2CHR 28:26–27", lambda w, h: K.city_dusk("cd10", w, h, 1007), "#2A1A3A")]
PG.extend(pack(SEGS, "2CH-C10-D", PG.next()))
SEGS2 = [face([caps("29:1-2")], "2CHR 29:1–2", HEZEKIAH, head="Hezekiah", stamp=29),
         drawn([caps("29:3-4"), cp("29:5", to="and said unto them,"), say("29:5", frm="Hear me,")], "2CHR 29:3–5", below(lambda w, h: K.shut_doors(w, h, 1008, open_=True), 0.4), "#FFE680",
               head="He Opened the Doors"),
         face([says("29:6-7")], "2CHR 29:6–7", HEZEKIAH),
         face([says("29:8-9")], "2CHR 29:8–9", HEZEKIAH, bg=COLD),
         face([says("29:10-11")], "2CHR 29:10–11", HEZEKIAH)]
PG.extend(pack(SEGS2, "2CH-C10-E", PG.next()))
LEVITES = ["MAHATH", "JOEL", "KISH", "AZARIAH", "JOAH", "EDEN", "SHIMRI", "JEUEL", "ZECHARIAH", "MATTANIAH", "JEHUEL", "SHIMEI", "SHEMAIAH", "UZZIEL"]
SEGS3 = [drawn([caps("29:12-14")], "2CHR 29:12–14", below(lambda w, h: K.branch(w, h, "THE LEVITES AROSE", LEVITES, per=7), 0.36), MAP, head="Then the Levites Arose"),
drawn([caps("29:15-17")], "2CHR 29:15–17", below(lambda w, h: K.cleansing("cl10", w, h, 1009), 0.44), "#8FD0E2", head="The House Cleansed"),
         drawn([cp("29:18", to="and said,"), say("29:18", frm="We have cleansed"), says("29:19")], "2CHR 29:18–19",
               below(lambda w, h: K.gold_vessels(w, h), 0.44), "#0B1A2E"),
         drawn([caps("29:20-21")], "2CHR 29:20–21", below(lambda w, h: K.court_scene("cs10", w, h, 1010, smoke=True), 0.4), "#8FD0E2", head="For All Israel"),
         drawn([caps("29:22-24")], "2CHR 29:22–24", below(lambda w, h: K.altar_service("as10", w, h, 1011), 0.44), "#5A4A6A"),
         drawn([caps("29:25-26")], "2CHR 29:25–26", below(lambda w, h: K.singers("sg10", w, h, 1012, n=8, top=0.5), 0.3), "#FFB04A", head="The Song of Jehovah"),
         drawn([caps("29:27-29")], "2CHR 29:27–29", below(lambda w, h: K.oath("oa10", w, h, 1013), 0.36), "#FFB04A"),
         drawn([caps("29:30"), cp("29:31", to="Then Hezekiah answered and said,"), say("29:31", frm="Now ye have", to="house of Jehovah."), cp("29:31", frm="And the assembly brought")],
               "2CHR 29:30–31", below(lambda w, h: K.court_scene("cs10b", w, h, 1014, smoke=True), 0.44), "#8FD0E2"),
         drawn([caps("29:32-34")], "2CHR 29:32–34", below(lambda w, h: K.tally(w, h, [("BULLOCKS", "70", "#FFD23F"), ("RAMS", "100", "#8FD0E2"), ("LAMBS", "200", "#FF8A6A"),
                                                                                 ("OXEN", "600", "#9CCB5E"), ("SHEEP", "3,000", "#C8C2D6")]), 0.44), "#1A1430"),
         drawn([caps("29:35-36")], "2CHR 29:35–36", below(lambda w, h: K.court_scene("cs10c", w, h, 1015, smoke=True), 0.3), "#8FD0E2")]
PG.extend(pack(SEGS3, "2CH-C10-F", PG.next(), end=end_mark("NEXT · THE PASSOVER OF HEZEKIAH", "right: 10px; bottom: 34px")))
