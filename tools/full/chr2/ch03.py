"""2 Chronicles volume, Chapter 3 — The Queen of Sheba (2 Chronicles 8–9). Every verse, word for word from ref/asv.
Solomon's cities as a map — Tadmor, the Beth-horons, Baalath; the levy of bondservants; Pharaoh's daughter brought up to her
own house; the offerings and the courses of the priests; the ships to Ophir; then the queen of Sheba with hard questions —
the half of the greatness of thy wisdom was not told me; the gold of a year, the shields of beaten gold, the throne of ivory
with twelve lions (a blueprint), the ships of Tarshish; and Solomon slept with his fathers."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from chr2 import G, art as K
from chr2.common import pack, cp, say, says, caps, drawn, face, joined, SOLOMON, SOLOMON_OLD, SHEBA, COLD, GOLDEN
from chr2 import ch02 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
INK, MAP = "#0B1A2E", "#0B1A2E"


@P("2CH-C03-00-Title", "Chapter 3 · The Queen of Sheba", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.sheba_train("t3", 760, 820, 301)}</g><rect x="0" y="0" width="760" height="262" fill="#FFB04A"></rect>')
    return chapter_title(3, "第三話", "The Queen of Sheba", "2 Chronicles 8 – 9", svg, "#C8702A", v("9:6", frm="the half of the greatness"), "2 Chronicles · Volume Fourteen")


SEGS = [drawn([caps("8:1-6")], "2CHR 8:1–6", below(lambda w, h: K.cities_map(w, h), 0.44), MAP, head="Tadmor in the Wilderness", stamp=8),
        drawn([caps("8:7-10")], "2CHR 8:7–10", below(lambda w, h: K.hewers("hw3", w, h, 302), 0.4), "#E8C8A0"),
        drawn([cp("8:11", to="for he said,"), say("8:11", frm="My wife")], "2CHR 8:11", below(lambda w, h: K.queen_house("qh3", w, h, 303), 0.3), "#5A2A1E"),
        drawn([caps("8:12-13")], "2CHR 8:12–13", below(lambda w, h: K.court_scene("sm3", w, h, 304, smoke=True), 0.34), "#8FD0E2"),
        drawn([caps("8:14-16")], "2CHR 8:14–16", below(lambda w, h: K.singers("sg3", w, h, 305, n=8, top=0.74), 0.3), "#FFB04A"),
        drawn([caps("8:17-18")], "2CHR 8:17–18", below(lambda w, h: K.navy("nv3", w, h, 306), 0.3), "#8FD0E2", head="The Gold of Ophir")]
PG.extend(pack(SEGS, "2CH-C03-D", PG.next()))
SEGS2 = [drawn([caps("9:1-2")], "2CHR 9:1–2", below(lambda w, h: K.sheba_train("st3", w, h, 307), 0.36), "#FFB04A", head="Hard Questions", stamp=9),
         drawn([caps("9:3-4")], "2CHR 9:3–4", below(lambda w, h: K.sheba_court("sc3", w, h, 308), 0.3), "#5A2A1E"),
         face([cp("9:5", to="to the king,"), joined("say", ("9:5", "It was a true"), "9:6")], "2CHR 9:5–6", SHEBA, head="The Half Was Not Told Me"),
         face([says("9:7-8")], "2CHR 9:7–8", SHEBA),
         drawn([caps("9:9")], "2CHR 9:9", below(lambda w, h: K.sheba_court("sc3b", w, h, 309), 0.24), "#5A2A1E"),
         drawn([caps("9:10-11")], "2CHR 9:10–11", below(lambda w, h: K.navy("nv3b", w, h, 310, port=False), 0.3), "#8FD0E2"),
         drawn([caps("9:12")], "2CHR 9:12", lambda w, h: K.sheba_train("st3b", w, h, 311), "#FFB04A"),
         drawn([caps("9:13-16")], "2CHR 9:13–16", below(lambda w, h: K.gold_shields_king(w, h, 312), 0.36), "#3A2214", head="Six Hundred Threescore and Six Talents"),
         drawn([caps("9:17-19")], "2CHR 9:17–19", below(lambda w, h: K.ivory_throne(w, h), 0.24), INK, head="The Throne of Ivory"),
         drawn([caps("9:20-22")], "2CHR 9:20–22", below(lambda w, h: K.tarshish("ts3", w, h, 313), 0.3), "#8FD0E2"),
         drawn([caps("9:23-24")], "2CHR 9:23–24", below(lambda w, h: K.tribute("tb3", w, h, 314), 0.26), "#FFE680"),
         drawn([caps("9:25-28")], "2CHR 9:25–28", below(lambda w, h: K.stalls("st3c", w, h, 315), 0.3), "#E8C8A0"),
         face([caps("9:29-31")], "2CHR 9:29–31", SOLOMON_OLD, bg=COLD, head="Solomon Slept with His Fathers")]
PG.extend(pack(SEGS2, "2CH-C03-E", PG.next(), end=end_mark("NEXT · REHOBOAM", "right: 10px; bottom: 34px")))
