"""2 Kings volume, Chapter 11 — The Shadow on the Dial (2 Kings 20–21). Every verse, word for word from ref/asv.
Hezekiah sick unto death — set thy house in order; he turned his face to the wall and wept sore; I have seen thy tears,
fifteen years added; the cake of figs; the shadow gone back ten steps on the dial of Ahaz; the envoys of Babylon shown all
his treasures — all shall be carried to Babylon; then Manasseh and his abominations (21:6, 21:16 words only), the line of
Samaria and the plummet of the house of Ahab (a blueprint); and Amon."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg2 import G, art as K
from kg2.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, HEZEKIAH, HEZEKIAH_SICK, ISAIAH, MANASSEH, BABYLONIAN, reign, reign_pages, RED, COLD, GOLDEN)
from kg2 import ch10 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#14123A"
INK = "#0B1A2E"


@P("2KI-C11-00-Title", "Chapter 11 · The Shadow on the Dial", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#FFE6A0"></rect><g transform="translate(0 320)">{K.dial(760, 760, back=True)}</g>')
    return chapter_title(11, "第十一話", "The Shadow on the Dial", "2 Kings 20 – 21", svg, "#B5652E", v("20:11", frm="and he brought the shadow"), "2 Kings · Volume Twelve")


SEGS = [drawn([cp("20:1", to="and said unto him,"), say("20:1", frm="Thus saith Jehovah,", to="Thus saith Jehovah,"), gd("20:1", frm="Set thy house")], "2KGS 20:1",
              below(lambda w, h: K.sickbed("sk11", w, h, 1101), 0.36), "#5A2A1E", head="Set Thy House in Order", stamp=20),
        face([cp("20:2", to="saying,"), say("20:3", to="in thy sight."), cp("20:3", frm="And Hezekiah wept sore.")], "2KGS 20:2–3", HEZEKIAH_SICK, bg=COLD),
        face([cp("20:4", to="saying,"), gd("20:5", to="Turn back, and say to Hezekiah the prince of my people,"), say("20:5", frm="Thus saith Jehovah,", to="the God of David thy father,"),
              gd("20:5", frm="I have heard"), gods("20:6")], "2KGS 20:4–6", ISAIAH, bg=NIGHT, head="I Have Seen Thy Tears"),
        face([cp("20:7", to="And Isaiah said,"), say("20:7", frm="Take a cake", to="of figs."), cp("20:7", frm="And they took"), cp("20:8", to="unto Isaiah,"), say("20:8", frm="What shall be")], "2KGS 20:7–8",
             HEZEKIAH_SICK, bg=COLD),
        face([cp("20:9", to="And Isaiah said,"), say("20:9", frm="This shall be"), cp("20:10", to="And Hezekiah answered,"), say("20:10", frm="It is a light thing")], "2KGS 20:9–10", ISAIAH,
             head="The Dial of Ahaz"),
        drawn([caps("20:11")], "2KGS 20:11", lambda w, h: K.dial(w, h, back=True), "#FFE6A0"),
        drawn([caps("20:12-13")], "2KGS 20:12–13", below(lambda w, h: K.treasures("tr11", w, h, 1102), 0.4), "#5A2A1E", head="From Babylon"),
        face([cp("20:14", to="and said unto him,"), say("20:14", frm="What said", to="unto thee?"), cp("20:14", frm="And Hezekiah said,", to="And Hezekiah said,"), say("20:14", frm="They are come"),
              cp("20:15", to="And he said,"), say("20:15", frm="What have they", to="in thy house?"), cp("20:15", frm="And Hezekiah answered,", to="And Hezekiah answered,"), say("20:15", frm="All that is")],
             "2KGS 20:14–15", HEZEKIAH),
        face([cp("20:16", to="unto Hezekiah,"), say("20:16", frm="Hear the word"), gods("20:17-18")], "2KGS 20:16–18", ISAIAH, bg=NIGHT),
        face([cp("20:19", to="unto Isaiah,"), say("20:19", frm="Good is", to="hast spoken."), cp("20:19", frm="He said moreover,", to="He said moreover,"), say("20:19", frm="Is it not so,")], "2KGS 20:19", HEZEKIAH)]
PG.extend(pack(SEGS, "2KI-C11-D", PG.next()))
R = [reign("Hezekiah", "20:20-21", head="The Kings of Judah"), reign("Manasseh, King of Judah", "21:1-3"), reign("Manasseh", "21:4-6")]
PG.extend(reign_pages(R, "2KI-C11-R", PG.next()))
SEGS2 = [face([cp("21:7", to="said to David and to Solomon his son,"), gd("21:7", frm="In this house,"), gods("21:8"), caps("21:9")], "2KGS 21:7–9", MANASSEH, bg=RED, head="Manasseh", stamp=21),
         drawn([cp("21:10"), gods("21:11-12")], "2KGS 21:10–12", lambda w, h: K.K2.throne_glory(w, h, 1103), "#14123A"),
         drawn([gods("21:13-15")], "2KGS 21:13–15", below(lambda w, h: K.plumb_line(w, h), 0.36), INK, head="The Line of Samaria"),
         drawn([caps("21:16")], "2KGS 21:16", lambda w, h: K.city_dusk("cd11", w, h, 1104), "#2A1A3A")]
PG.extend(pack(SEGS2, "2KI-C11-E", PG.next()))
R2 = [reign("Manasseh", "21:17-18"), reign("Amon, King of Judah", "21:19-22"), reign("Amon", "21:23-26")]
PG.extend(reign_pages(R2, "2KI-C11-S", PG.next(), end=end_mark("NEXT · JOSIAH", "right: 40px; bottom: 50px")))
