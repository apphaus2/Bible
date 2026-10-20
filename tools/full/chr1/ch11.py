"""1 Chronicles volume, Chapter 11 — Thine Is the Kingdom (1 Chronicles 28–29), the last chapter of 1 Chronicles. Every verse,
word for word from ref/eng-asv. David stands up before the assembly — hear me, my brethren; Solomon chosen to sit upon the
throne of the kingdom of Jehovah; know thou the God of thy father; the pattern of the house given by the Spirit (1 Kings'
blueprints: the plan, the cherubim, the vessels); be strong and of good courage; the free-will offerings of the king and of
the princes; David blesses Jehovah — thine, O Jehovah, is the greatness; of thine own have we given thee; the sacrifices;
Solomon made king the second time; and David died in a good old age, full of days, riches, and honor (words only)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from chr1 import G, art as K
from chr1.common import pack, cp, say, says, caps, drawn, face, joined, DAVID_OLD, SOLOMON, ZADOK, COLD, GOLDEN
from chr1 import ch10 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
INK = "#0B1A2E"


@P("1CH-C11-00-Title", "Chapter 11 · Thine Is the Kingdom", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.K2.prayer("t11", 760, 820, 1101)}</g><rect x="0" y="0" width="760" height="262" fill="#3A1A2A"></rect>')
    return chapter_title(11, "第十一話", "Thine Is the Kingdom", "1 Chronicles 28 – 29", svg, "#3A1A2A", v("29:11", frm="thine is the kingdom,"), "1 Chronicles · Volume Thirteen")


SEGS = [drawn([caps("28:1")], "1CHR 28:1", below(lambda w, h: K.charge_son("cs11", w, h, 1102, princes=True), 0.4), "#8A4A26", head="Hear Me, My Brethren", stamp=28),
        face([cp("28:2", to="and said,"), joined("say", ("28:2", "Hear me,"), "28:3")], "1CHR 28:2–3", DAVID_OLD),
        face([says("28:4-5")], "1CHR 28:4–5", DAVID_OLD),
        drawn([says("28:6-7")], "1CHR 28:6–7", lambda w, h: K.K2.throne_glory(w, h, 1103), "#14123A"),
        face([says("28:8")], "1CHR 28:8", DAVID_OLD),
        face([says("28:9-10")], "1CHR 28:9–10", DAVID_OLD, head="Know Thou the God of Thy Father"),
        drawn([caps("28:11")], "1CHR 28:11", below(lambda w, h: K.temple_plan(w, h), 0.24), INK, head="The Pattern"),
        drawn([caps("28:12-13")], "1CHR 28:12–13", below(lambda w, h: K.temple_plan(w, h, oracle=True), 0.3), INK),
        drawn([caps("28:14-17")], "1CHR 28:14–17", below(lambda w, h: K.gold_vessels(w, h), 0.5), INK),
        drawn([caps("28:18"), cp("28:19", to="said David,"), say("28:19", frm="have I been made")], "1CHR 28:18–19", below(lambda w, h: K.cherubim(w, h), 0.36), INK),
        face([cp("28:20", to="his son,"), joined("say", ("28:20", "Be strong"), "28:21")], "1CHR 28:20–21", DAVID_OLD, head="Be Strong and of Good Courage")]
PG.extend(pack(SEGS, "1CH-C11-D", PG.next()))
SEGS2 = [face([cp("29:1", to="unto all the assembly,"), say("29:1", frm="Solomon my son,")], "1CHR 29:1", DAVID_OLD, head="Who Then Offereth Willingly?", stamp=29),
         drawn([says("29:2")], "1CHR 29:2", below(lambda w, h: K.stores(w, h, 1104), 0.4), "#3A2A1A"),
         face([joined("say", "29:3", "29:4", "29:5")], "1CHR 29:3–5", DAVID_OLD),
         drawn([caps("29:6-8")], "1CHR 29:6–8", below(lambda w, h: K.K3.treasures("tr11", w, h, 1105), 0.36), "#5A2A1E"),
         drawn([caps("29:9")], "1CHR 29:9", below(lambda w, h: K.charge_son("cs11b", w, h, 1106, princes=True), 0.2), "#8A4A26"),
         drawn([cp("29:10", to="and David said,"), say("29:10", frm="Blessed be thou,")], "1CHR 29:10", lambda w, h: K.K2.prayer("pr11", w, h, 1107), "#3A1A2A",
               head="Thine, O Jehovah, Is the Greatness"),
         face([says("29:11-13")], "1CHR 29:11–13", DAVID_OLD, bg="#14123A"),
         face([says("29:14-16")], "1CHR 29:14–16", DAVID_OLD, bg="#14123A"),
         face([says("29:17-19")], "1CHR 29:17–19", DAVID_OLD, bg="#14123A"),
         drawn([cp("29:20", to="to all the assembly,"), say("29:20", frm="Now bless", to="your God."), cp("29:20", frm="And all the assembly")], "1CHR 29:20",
               below(lambda w, h: K.K2.tent_ark("ta11", w, h, 1108), 0.3), "#FFB04A"),
         drawn([caps("29:21-22")], "1CHR 29:21–22", below(lambda w, h: K.K1.gihon("gh11", w, h, 1109, anoint=True), 0.4), "#8FD0E2", head="King the Second Time"),
         face([caps("29:23-25")], "1CHR 29:23–25", SOLOMON),
         drawn([caps("29:26-28")], "1CHR 29:26–28", lambda w, h: K.K2.crown_bracelet(w, h, 1110), "#3A1A2A", head="Full of Days, Riches, and Honor"),
         drawn([caps("29:29-30")], "1CHR 29:29–30", below(lambda w, h: K.city_dusk("cd11", w, h, 1111), 0.3), "#2A1A3A")]
PG.extend(pack(SEGS2, "1CH-C11-E", PG.next(), end=end_mark("END OF 1 CHRONICLES · NEXT · 2 CHRONICLES", "right: 10px; bottom: 34px", ch="完")))
