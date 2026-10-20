"""1 Kings volume, Chapter 8 — His Heart Turned Away (1 Kings 11). Every verse, word for word from ref/eng-asv.
Solomon's foreign wives turning away his heart; the high places of Chemosh and Molech on the mount before Jerusalem;
Jehovah's anger — I will surely rend the kingdom from thee (the Voice box); the adversaries Hadad the Edomite and Rezon of
Damascus; Jeroboam the son of Nebat; Ahijah's new garment rent in twelve pieces — take thee ten pieces; Jeroboam fled into
Egypt; and Solomon slept with his fathers."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg1 import G, art as K
from kg1.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, F, SOLOMON_OLD, JEROBOAM, AHIJAH, RED, COLD, GOLDEN)
from kg1 import ch07 as _prev

v, sp = G.v, G.span
HADAD = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#3A2214", hl="#6A5A4E", stubble="#3A2214", egypt=("#F3EFE6", "#B5652E"), light="#FFC14D")
PHARAOH = F("adam", skin="#C98E66", shadow="#8A5A3E", egypt=("#E8B830", "#1F5FAD"), collar=True, kohl=True, false_beard=True, light="#FFE680")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#14123A"


@P("1KI-C08-00-Title", "Chapter 8 · His Heart Turned Away", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#3A1A3A"></rect><g transform="translate(0 320)">{K.high_places("t8", 760, 760, 801)}</g>')
    return chapter_title(8, "第八話", "His Heart Turned Away", "1 Kings 11", svg, "#3A1A3A", v("11:4", to="after other gods;"), "1 Kings · Volume Eleven")


SEGS = [drawn([caps("11:1-3")], "1KGS 11:1–3", below(lambda w, h: K.wives("wv8", w, h, 802), 0.34), "#5A2A1E", head="Many Foreign Women", stamp=11),
        face([caps("11:4-6")], "1KGS 11:4–6", SOLOMON_OLD, bg=COLD),
        drawn([caps("11:7-8")], "1KGS 11:7–8", lambda w, h: K.high_places("hp8", w, h, 803), "#3A1A3A"),
        drawn([caps("11:9-10"), cp("11:11", to="unto Solomon,"), gd("11:11", frm="Forasmuch")], "1KGS 11:9–11", lambda w, h: __import__("sa2.art", fromlist=["x"]).nathan_night(w, h, 804), "#0F0E2A",
              head="I Will Rend the Kingdom"),
        drawn([gods("11:12-13")], "1KGS 11:12–13", below(lambda w, h: K.ten_two(w, h), 0.42), "#0B1A2E"),
        drawn([caps("11:14-18")], "1KGS 11:14–18", below(lambda w, h: K.hadad("hd8", w, h, 805), 0.4), "#FFE680", head="Hadad the Edomite"),
        face([caps("11:19-20")], "1KGS 11:19–20", HADAD),
        face([cp("11:21", to="Hadad said to Pharaoh,"), say("11:21", frm="Let me depart,"), cp("11:22", to="Then Pharaoh said unto him,"), say("11:22", frm="But what", to="own country?"),
              cp("11:22", frm="And he answered,", to="And he answered,"), say("11:22", frm="Nothing:")], "1KGS 11:21–22", PHARAOH),
        drawn([caps("11:23-25")], "1KGS 11:23–25", below(lambda w, h: K.damascus("dm8", w, h, 806), 0.3), "#8FD0E2", head="Rezon"),
        face([caps("11:26-28")], "1KGS 11:26–28", JEROBOAM, head="Jeroboam the Son of Nebat"),
        drawn([caps("11:29-30")], "1KGS 11:29–30", below(lambda w, h: K.rent_garment("rg8", w, h, 807), 0.24), "#8FD0E2", head="Twelve Pieces"),
        drawn([cp("11:31", to="said to Jeroboam,"), say("11:31", frm="Take thee", to="thus saith Jehovah, the God of Israel,"), gd("11:31", frm="Behold,"), gods("11:32")], "1KGS 11:31–32",
              below(lambda w, h: K.rent_garment("rg8b", w, h, 808, pieces=True), 0.4), "#8FD0E2"),
        face([gods("11:33-34")], "1KGS 11:33–34", AHIJAH, bg=NIGHT),
        face([gods("11:35-37")], "1KGS 11:35–37", AHIJAH, bg=NIGHT),
        face([gods("11:38-39")], "1KGS 11:38–39", AHIJAH, bg=NIGHT),
        drawn([caps("11:40")], "1KGS 11:40", lambda w, h: K.hadad("hd8b", w, h, 809), "#FFE680"),
        drawn([caps("11:41-43")], "1KGS 11:41–43", lambda w, h: K.city_dusk("cd8", w, h, 810), "#2A1A3A")]
PG.extend(pack(SEGS, "1KI-C08-D", PG.next(), end=end_mark("NEXT · TO YOUR TENTS, O ISRAEL", "right: 10px; bottom: 34px")))
