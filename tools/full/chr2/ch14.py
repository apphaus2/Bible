"""2 Chronicles volume, Chapter 14 — The Seventy Years (2 Chronicles 35–36), the last chapter of 2 Chronicles. Every verse,
word for word from ref/asv. Josiah's passover — put the holy ark in the house, there shall no more be a burden upon your
shoulders; the lambs and kids given, the singers in their place; no passover like it since Samuel; Neco and Carchemish —
what have I to do with thee?; the archers at Megiddo (35:23–24 words over the chariot); Jeremiah's lament; then Jehoahaz,
Jehoiakim, Jehoiachin and Zedekiah as reign cells; the messengers mocked till there was no remedy; the Chaldeans and the house
burned (36:17–19 words over the burning city); the land keeping sabbath seventy years; and the proclamation of Cyrus — let
him go up."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from chr2 import G, art as K
from chr2.common import (pack, cp, say, gd, says, gods, caps, drawn, face, joined, cell, cells, roll, F, JOSIAH, JOSIAH_GRIEF, NECO, ZEDEKIAH, COLD, GOLDEN, RED)
from chr2 import ch13 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
JEREMIAH = F("adam", skin="#B98A6E", shadow="#3A2A4A", hair="#3A3430", hl="#6A6460", beard=True, beard_color="#4A4440", scarf="#5A5A6A", brow="sorrow", tear=True, light="#9AA8C8")
CYRUS = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#7A2A6A", band=True, light="#FFE680")


@P("2CH-C14-00-Title", "Chapter 14 · The Seventy Years", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.sabbath_land(760, 820, 1401)}</g><rect x="0" y="0" width="760" height="262" fill="#8FD0E2"></rect>')
    return chapter_title(14, "第十四話", "The Seventy Years", "2 Chronicles 35 – 36", svg, "#3A5A7A", v("36:21", frm="for as long as it lay desolate"), "2 Chronicles · Volume Fourteen")


SEGS = [drawn([caps("35:1-2"), cp("35:3", to="that were holy unto Jehovah,"), say("35:3", frm="Put the holy ark")], "2CHR 35:1–3", below(lambda w, h: K.ark_up("au14", w, h, 1402), 0.4),
              "#FFE680", head="Josiah Kept a Passover", stamp=35),
        face([says("35:4-6")], "2CHR 35:4–6", JOSIAH),
        drawn([caps("35:7-9")], "2CHR 35:7–9", below(lambda w, h: K.tally(w, h, [("THE KING", "30,000", "#FFD23F"), ("THE RULERS", "2,600", "#8FD0E2"), ("THE CHIEFS", "5,000", "#FF8A6A")],
                                                                          "OF THE FLOCK, FOR THE PASSOVER-OFFERINGS"), 0.5), "#1A1430"),
        drawn([caps("35:10-12")], "2CHR 35:10–12", below(lambda w, h: K.altar_service("as14", w, h, 1403), 0.44), "#5A4A6A"),
        drawn([caps("35:13-14")], "2CHR 35:13–14", below(lambda w, h: K.feast_tents("ft14", w, h, 1404), 0.44), "#FFB04A"),
        drawn([caps("35:15-16")], "2CHR 35:15–16", below(lambda w, h: K.singers("sg14", w, h, 1405, n=8, top=0.5), 0.44), "#FFB04A"),
        drawn([caps("35:17-19")], "2CHR 35:17–19", lambda w, h: K.court_scene("cs14", w, h, 1406, cloud=True), "#E8E2D6", head="No Passover Like to That"),
        drawn([caps("35:20")], "2CHR 35:20", below(lambda w, h: K.assyria_map(w, h), 0.2), MAP, head="Neco King of Egypt"),
        face([cp("35:21", to="saying,"), say("35:21", frm="What have I")], "2CHR 35:21", NECO),
        drawn([caps("35:22"), cp("35:23", to="to his servants,"), say("35:23", frm="Have me away;"), caps("35:24")], "2CHR 35:22–24", lambda w, h: K.megiddo("mg14", w, h, 1407), "#2A1A2A"),
        face([caps("35:25-27")], "2CHR 35:25–27", JEREMIAH, bg=COLD, head="Jeremiah Lamented for Josiah")]
PG.extend(pack(SEGS, "2CH-C14-D", PG.next()))
R = [cell("Jehoahaz", "36:1-4", "#FFD23F", head="The Last Kings of Judah"), cell("Jehoiakim", "36:5-8", "#FFD23F"), cell("Jehoiachin", "36:9-10", "#FFD23F"),
     cell("Zedekiah", "36:11-13", "#FFD23F")]
PG.extend(roll(R, "2CH-C14-R", PG.next(), "THE KINGS OF JUDAH · 2 CHRONICLES 36"))
SEGS2 = [drawn([caps("36:14-16")], "2CHR 36:14–16", lambda w, h: K.city_dusk("cd14", w, h, 1408), "#2A1A3A", head="Till There Was No Remedy", stamp=36),
         drawn([caps("36:17-19")], "2CHR 36:17–19", lambda w, h: K.burning_city(w, h, 1409), "#2A0A0A"),
         drawn([caps("36:20")], "2CHR 36:20", below(lambda w, h: K.captives("cp14", w, h, 1412, city="jerusalem"), 0.2), "#5A4A5A"),
         drawn([caps("36:21")], "2CHR 36:21", below(lambda w, h: K.sabbath_land(w, h, 1410), 0.24), "#8FD0E2", head="The Land Enjoyed Its Sabbaths"),
         drawn([caps("36:22")], "2CHR 36:22", below(lambda w, h: K.cyrus_decree("cy14", w, h, 1411), 0.3), "#FFC890", head="Let Him Go Up"),
         face([say("36:23", to="Thus saith Cyrus king of Persia,"), say("36:23", frm="All the kingdoms")], "2CHR 36:23", CYRUS)]
PG.extend(pack(SEGS2, "2CH-C14-E", PG.next(), end=end_mark("END OF 2 CHRONICLES · NEXT · EZRA", "right: 10px; bottom: 34px", ch="完")))
