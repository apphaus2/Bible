"""1 Chronicles volume, Chapter 2 — The Sons of David (1 Chronicles 3–4). Every verse, word for word from ref/asv.
The sons born in Hebron and in Jerusalem; the kings of Judah from Solomon to Josiah as one line; the sons of Josiah and the
line of Jeconiah the captive down past Zerubbabel; then the families of Judah — Jabez, more honorable than his brethren,
and his prayer, enlarge my border (a survey plan) — the potters that dwelt with the king; and Simeon, its cities, the fat
pasture at Gedor (4:41 words over the smoke of the tents) and the five hundred who went to mount Seir."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from faces_ex import F
from chr1 import G, art as K
from chr1.common import pack, cp, say, caps, drawn, face, cell, cells, roll, JABEZ, COLD, GOLDEN
from chr1 import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
TAG3, TAG4 = "THE GENERATIONS · 1 CHRONICLES 3", "THE GENERATIONS · 1 CHRONICLES 4"
KINGS = ["SOLOMON", "REHOBOAM", "ABIJAH", "ASA", "JEHOSHAPHAT", "JORAM", "AHAZIAH", "JOASH", "AMAZIAH", "AZARIAH", "JOTHAM", "AHAZ", "HEZEKIAH", "MANASSEH", "AMON", "JOSIAH"]
MOTHER = F("eve", skin="#C98E66", shadow="#4A3A4A", hair="#2A1A10", scarf="#5A4A6A", brow="sorrow", light="#9AA8C8")


@P("1CH-C02-00-Title", "Chapter 2 · The Sons of David", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.lineage(760, 780, KINGS, hi=("SOLOMON", "HEZEKIAH", "JOSIAH"), per=4, top=0.17, bot=0.66)}</g>'
                f'<rect x="0" y="0" width="760" height="300" fill="#0B1A2E"></rect>')
    return chapter_title(2, "第二話", "The Sons of David", "1 Chronicles 3 – 4", svg, MAP, v("3:1", to="born unto him in Hebron:"), "1 Chronicles · Volume Thirteen")


def chart(refs, fn, k=0.24, **kw):
    a, _, b = refs.partition("-")
    return drawn([caps(refs)], f"1CHR {a}" + (f"–{b}" if b else ""), below(fn, k), MAP, **kw)

SEGS = [chart("3:1-4", lambda w, h: K.branch(w, h, "DAVID", ["AMNON", "DANIEL", "ABSALOM", "ADONIJAH", "SHEPHATIAH", "ITHREAM"]), 0.3, head="Born unto Him in Hebron", stamp=3),
        chart("3:5-9", lambda w, h: K.branch(w, h, "DAVID", ["SHIMEA", "SHOBAB", "NATHAN", "SOLOMON", "IBHAR", "ELISHAMA", "ELIPHELET", "NOGAH", "NEPHEG", "JAPHIA",
                                                         "ELISHAMA", "ELIADA", "ELIPHELET"], hi=("SOLOMON",), per=7), 0.3),
        chart("3:10-14", lambda w, h: K.lineage(w, h, KINGS, hi=("SOLOMON", "HEZEKIAH", "JOSIAH"), per=4, top=0.3, bot=0.9), 0.14, h=440, head="The Kings of Judah"),
        chart("3:15-16", lambda w, h: K.branch(w, h, "JOSIAH", ["JOHANAN", "JEHOIAKIM", "ZEDEKIAH", "SHALLUM"], hi=("JEHOIAKIM",)), 0.24)]
PG.extend(pack(SEGS, "1CH-C02-D", PG.next()))
R = (cells(3, 17, 24, "Jeconiah the Captive", "#8FD0E2", head="After the Captivity", budget=560)
     + cells(4, 1, 8, "The Sons of Judah", "#FFD23F", head="The Families of Judah", budget=560))
PG.extend(roll(R, "1CH-C02-R", PG.next(), TAG3))
SEGS2 = [face([cp("4:9", to="saying,"), say("4:9", frm="Because I bare")], "1CHR 4:9", MOTHER, bg=COLD, head="Jabez", stamp=4),
         face([cp("4:10", to="saying,"), say("4:10", frm="Oh that", to="to my sorrow!")], "1CHR 4:10", JABEZ),
         drawn([cp("4:10", frm="And God granted")], "1CHR 4:10", below(lambda w, h: K.jabez_border(w, h), 0.14), MAP, h=360)]
PG.extend(pack(SEGS2, "1CH-C02-E", PG.next()))
R2 = (cells(4, 11, 23, "The Families of Judah", "#FFD23F", head="The Men of Recah", budget=560)
      + cells(4, 24, 38, "Simeon", "#8FD0E2", head="The Sons of Simeon", budget=560))
PG.extend(roll(R2, "1CH-C02-S", PG.next(), TAG4))
SEGS3 = [drawn([caps("4:39-40")], "1CHR 4:39–40", below(lambda w, h: K.pasture("pa2", w, h, 201), 0.3), "#8FD0E2", head="The Entrance of Gedor"),
         drawn([caps("4:41")], "1CHR 4:41", below(lambda w, h: K.pasture("pa2b", w, h, 202, smoke=True), 0.28), "#5A4A5A"),
         drawn([caps("4:42-43")], "1CHR 4:42–43", below(lambda w, h: K.seir("se2", w, h, 203), 0.3), "#C86A3A")]
PG.extend(pack(SEGS3, "1CH-C02-F", PG.next(), end=end_mark("NEXT · THE SONS OF LEVI", "right: 40px; bottom: 50px")))
