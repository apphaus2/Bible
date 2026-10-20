"""2 Kings volume, Chapter 12 — Josiah (2 Kings 22–23). Every verse, word for word from ref/eng-asv.
Josiah of eight years; the repairing of the house; I have found the book of the law; the king rends his clothes; Huldah the
prophetess — because thy heart was tender; the covenant read by the pillar; the house cleansed and the Asherah burned at the
Kidron; the high places defiled from Geba to Beer-sheba, Topheth, the horses of the sun; the altar at Beth-el and the bones
(23:20 words only), the monument of the man of God left alone; such a passover; like unto him was there no king; Megiddo
(23:29 words only); and Jehoahaz and Jehoiakim under Pharaoh-necoh."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg2 import G, art as K
from kg2.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, JOSIAH, JOSIAH_GRIEF, HILKIAH, SHAPHAN, HULDAH, reign, reign_pages, RED, COLD, GOLDEN)
from kg2 import ch11 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#14123A"


@P("2KI-C12-00-Title", "Chapter 12 · Josiah", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#3A2A1A"></rect><g transform="translate(0 320)">{K.book_found("t12", 760, 760, 1201)}</g>')
    return chapter_title(12, "第十二話", "Josiah", "2 Kings 22 – 23", svg, "#3A2A1A", v("22:8", frm="I have found the book", to="house of Jehovah."), "2 Kings · Volume Twelve")


SEGS = [face([caps("22:1-2"), cp("22:3", to="saying,"), joined("say", "22:4", "22:5", "22:6", "22:7")], "2KGS 22:1–7", JOSIAH, head="Josiah", stamp=22),
        drawn([cp("22:8", to="unto Shaphan the scribe,"), say("22:8", frm="I have found", to="house of Jehovah."), cp("22:8", frm="And Hilkiah delivered")], "2KGS 22:8",
              below(lambda w, h: K.book_found("bf12", w, h, 1202), 0.24), "#3A2A1A", head="The Book of the Law"),
        drawn([cp("22:9", to="and said,"), say("22:9", frm="Thy servants"), cp("22:10", to="saying,"), say("22:10", frm="Hilkiah the priest", to="a book."), cp("22:10", frm="And Shaphan read it"), caps("22:11")],
              "2KGS 22:9–11", below(lambda w, h: K.book_found("bf12b", w, h, 1203, reading=True), 0.44), "#3A2A1A"),
        face([cp("22:12", to="saying,"), says("22:13")], "2KGS 22:12–13", JOSIAH_GRIEF, bg=COLD),
        drawn([caps("22:14"), cp("22:15", to="And she said unto them,"), say("22:15", frm="Thus saith Jehovah,", to="the God of Israel:"), gd("22:15", frm="Tell ye")], "2KGS 22:14–15",
              below(lambda w, h: K.huldah("hd12", w, h, 1204), 0.4), "#C8A878", head="Huldah the Prophetess"),
        face([gods("22:16-17")], "2KGS 22:16–17", HULDAH, bg=NIGHT),
        face([say("22:18", to="thus shall ye say to him,"), say("22:18", frm="Thus saith Jehovah,", to="the God of Israel:"), gd("22:18", frm="As touching"), gods("22:19"), gd("22:20", to="this place."),
              cp("22:20", frm="And they brought")], "2KGS 22:18–20", HULDAH, bg=NIGHT),
        drawn([caps("23:1-3")], "2KGS 23:1–3", below(lambda w, h: K.covenant_pillar("cp12", w, h, 1205), 0.4), "#8FD0E2", head="The Book of the Covenant", stamp=23),
        drawn([caps("23:4-6")], "2KGS 23:4–6", below(lambda w, h: K.kidron_fire(w, h, 1206), 0.5), "#3A2A3A"),
        drawn([caps("23:7-9")], "2KGS 23:7–9", below(lambda w, h: K.high_places("hp12", w, h, 1207), 0.5), "#3A1A3A"),
        drawn([caps("23:10-12")], "2KGS 23:10–12", below(lambda w, h: K.kidron_fire(w, h, 1208), 0.5), "#3A2A3A"),
        drawn([caps("23:13-14")], "2KGS 23:13–14", below(lambda w, h: K.high_places("hp12b", w, h, 1209), 0.36), "#3A1A3A"),
        drawn([caps("23:15-16"), cp("23:17", to="Then he said,"), say("23:17", frm="What monument", to="I see?"), cp("23:17", frm="And the men of the city told him,", to="told him,"),
               say("23:17", frm="It is the sepulchre"), cp("23:18", to="And he said,"), say("23:18", frm="Let him be;", to="his bones."), cp("23:18", frm="So they let")], "2KGS 23:15–18",
              below(lambda w, h: K.bethel_tombs("bt12", w, h, 1210), 0.56), "#5A3A5A", head="The Altar at Beth-el"),
        drawn([caps("23:19-20")], "2KGS 23:19–20", lambda w, h: K.calves("cv12", w, h, 1211, people=False), "#5A3A5A"),
        drawn([cp("23:21", to="saying,"), say("23:21", frm="Keep the passover"), caps("23:22-23")], "2KGS 23:21–23", below(lambda w, h: K.feast_tents("ft12", w, h, 1212), 0.36), "#FFB04A",
              head="Such a Passover"),
        face([caps("23:24-25")], "2KGS 23:24–25", JOSIAH),
        drawn([caps("23:26"), cp("23:27", to="And Jehovah said,"), gd("23:27", frm="I will remove")], "2KGS 23:26–27", lambda w, h: K.K2.throne_glory(w, h, 1213), "#14123A"),
        drawn([caps("23:28-30")], "2KGS 23:28–30", lambda w, h: K.megiddo("mg12", w, h, 1214), "#2A1A2A", head="Megiddo")]
PG.extend(pack(SEGS, "2KI-C12-D", PG.next()))
R = [reign("Jehoahaz, King of Judah", "23:31-33"), reign("Jehoiakim, King of Judah", "23:34-35"), reign("Jehoiakim", "23:36-37")]
PG.extend(reign_pages(R, "2KI-C12-R", PG.next(), end=end_mark("NEXT · THE FALL OF JERUSALEM", "right: 40px; bottom: 50px")))
