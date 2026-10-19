"""1 Chronicles volume, Chapter 7 — Thy Throne for Ever (1 Chronicles 17–20). Every verse, word for word from ref/asv.
A house of cedar and the ark under curtains; the word of God to Nathan by night — I will establish his throne for ever (the
digest's panels and the throne of glory); who am I, O Jehovah God; David's wars as a map, the shields of gold and the brass
of Hadarezer; Hanun and the messengers shamed; Joab before and behind; Shophach; Rabbah and the crown of a talent of gold
(20:3 words only, over Rabbah at dusk); and the sons of the giant in Gath."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos import art as JA
from jos.art import below
from faces_ex import F
from sa2.common import over as over2, D as D2
from chr1 import G, art as K
from chr1.common import (pack, cp, say, gd, says, gods, caps, drawn, face, joined, DAVID_KING, NATHAN, JOAB, COLD, GOLDEN, RED)
from chr1 import ch06 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP = "#0B1A2E"
AMMONITE = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#2A5A4A", band=True, brow="scowl", light="#D7261E")
WARS = lambda *hi: (lambda w, h: K.K2.wars_map(w, h, hi=hi))


@P("1CH-C07-00-Title", "Chapter 7 · Thy Throne for Ever", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.K2.throne_glory(760, 820, 701)}</g><rect x="0" y="0" width="760" height="262" fill="#14123A"></rect>')
    return chapter_title(7, "第七話", "Thy Throne for Ever", "1 Chronicles 17 – 20", svg, "#14123A", v("17:12", frm="and I will establish"), "1 Chronicles · Volume Thirteen")


SEGS = [over2([cp("17:1", to="the prophet,"), say("17:1", frm="Lo, I dwell")], "1CHR 17:1", "A5", 0, head="A House of Cedar", stamp=17),
        face([cp("17:2", to="unto David,"), say("17:2", frm="Do all")], "1CHR 17:2", NATHAN),
        drawn([caps("17:3"), gods("17:4-6")], "1CHR 17:3–6", lambda w, h: K.K2.nathan_night(w, h, 702), "#0F0E2A", head="The Word of God Came to Nathan"),
        over2([gods("17:7-9")], "1CHR 17:7–9", "A5", 1),
        drawn([gods("17:10-12")], "1CHR 17:10–12", lambda w, h: K.K2.throne_glory(w, h, 703), "#14123A"),
        over2([gods("17:13-14")], "1CHR 17:13–14", "A5", 1, align="xMidYMax"),
        face([caps("17:15")], "1CHR 17:15", NATHAN),
        over2([cp("17:16", to="and he said,"), joined("say", ("17:16", "Who am I,"), "17:17")], "1CHR 17:16–17", "A5", 2, head="Who Am I, O Jehovah God?"),
        face([says("17:18-20")], "1CHR 17:18–20", DAVID_KING),
        drawn([says("17:21-22")], "1CHR 17:21–22", lambda w, h: K.K2.prayer("pr7", w, h, 704), "#3A1A2A"),
        face([says("17:23-25")], "1CHR 17:23–25", DAVID_KING),
        drawn([says("17:26-27")], "1CHR 17:26–27", lambda w, h: K.K2.prayer("pr7b", w, h, 705), "#3A1A2A")]
PG.extend(pack(SEGS, "1CH-C07-D", PG.next()))
SEGS2 = [drawn([caps("18:1-2")], "1CHR 18:1–2", below(WARS("GATH", "MOAB"), 0.3), MAP, head="Jehovah Gave Victory to David", stamp=18),
         drawn([caps("18:3-6")], "1CHR 18:3–6", below(WARS("ZOBAH", "DAMASCUS"), 0.4), MAP),
         drawn([caps("18:7-8")], "1CHR 18:7–8", lambda w, h: K.K2.gold_shields(w, h, 706), "#3A2214"),
         drawn([caps("18:9-11")], "1CHR 18:9–11", lambda w, h: K.K2.vessels(w, h, 707), "#2A1A3A", head="Tou King of Hamath"),
         drawn([caps("18:12-13")], "1CHR 18:12–13", below(WARS("VALLEY OF SALT"), 0.2), MAP),
         drawn([caps("18:14-17")], "1CHR 18:14–17", below(lambda w, h: K.K2.court("ct7", w, h, 708), 0.3), "#5A2A1E")]
PG.extend(pack(SEGS2, "1CH-C07-E", PG.next()))
SEGS3 = [drawn([caps("19:1"), cp("19:2", to="And David said,"), say("19:2", frm="I will show", to="showed kindness to me."), cp("19:2", frm="So David sent")], "1CHR 19:1–2",
               below(lambda w, h: K.K2.messengers("ms7", w, h, 709), 0.4), "#8FD0E2", head="Hanun", stamp=19),
         face([cp("19:3", to="said to Hanun,"), say("19:3", frm="Thinkest thou")], "1CHR 19:3", AMMONITE, bg=RED),
         drawn([caps("19:4"), cp("19:5", to="And the king said,"), say("19:5", frm="Tarry at Jericho")], "1CHR 19:4–5", below(lambda w, h: K.K2.jericho_wait("jw7", w, h, 710), 0.36), "#8FD0E2"),
         drawn([caps("19:6-9")], "1CHR 19:6–9", below(lambda w, h: K.K2.ammon_map(w, h, 0), 0.4), MAP),
         drawn([caps("19:10-11")], "1CHR 19:10–11", below(lambda w, h: K.K2.ammon_map(w, h, 1), 0.24), MAP),
         face([cp("19:12", to="And he said,"), joined("say", ("19:12", "If the Syrians"), "19:13")], "1CHR 19:12–13", JOAB, bg=RED),
         drawn([caps("19:14-15")], "1CHR 19:14–15", below(lambda w, h: K.K2.ammon_map(w, h, 2), 0.26), MAP),
         drawn([caps("19:16-19")], "1CHR 19:16–19", below(lambda w, h: JA.chariots("sh7", w, h, 711), 0.36), "#8FD0E2", head="Shophach")]
PG.extend(pack(SEGS3, "1CH-C07-F", PG.next()))
SEGS4 = [drawn([caps("20:1")], "1CHR 20:1", below(lambda w, h: K.K2.rabbah("rb7", w, h, 712), 0.3), "#8FD0E2", head="Rabbah", stamp=20),
         drawn([caps("20:2")], "1CHR 20:2", lambda w, h: K.K2.crown_talent(w, h, 713), "#2A1A3A"),
         drawn([caps("20:3")], "1CHR 20:3", lambda w, h: K.K2.rabbah("rb7b", w, h, 714, camp=False, dusk=True), "#3A1A2A"),
         drawn([caps("20:4-5")], "1CHR 20:4–5", below(lambda w, h: K.K2.giant("gt7", w, h, 715), 0.3), "#E8B880", head="Born unto the Giant"),
         drawn([caps("20:6-8")], "1CHR 20:6–8", below(lambda w, h: K.K2.giant("gt7b", w, h, 716, fallen=True), 0.3), "#E8B880")]
PG.extend(pack(SEGS4, "1CH-C07-G", PG.next(), end=end_mark("NEXT · THE THRESHING-FLOOR OF ORNAN", "right: 10px; bottom: 34px")))
