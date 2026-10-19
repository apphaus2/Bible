"""Esther volume, Chapter 2 — For Such a Time as This (Esther 3–4). Every verse, word for word from ref/asv.
Haman the Agagite advanced above all the princes; all the king's servants in the gate bowed down, but Mordecai bowed not
down; Pur, that is, the lot, cast before Haman from month to month to the month Adar (a wheel of the twelve months); a
certain people scattered abroad — let it be written that they be destroyed; the king's ring given; letters by posts into all
the provinces, and the king and Haman sat down to drink, but the city of Shushan was perplexed; then Mordecai in sackcloth and
ashes before the king's gate, and great mourning in every province; Hathach between the queen and Mordecai; the golden
sceptre and the thirty days; who knoweth whether thou art not come to the kingdom for such a time as this?; and Esther's fast —
if I perish, I perish."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from jos.art import below
from est import G, art as K
from est.common import (pack, cp, say, says, caps, drawn, face, joined, tshade as shade, HAMAN, AHASUERUS, ESTHER_GRIEF, ESTHER_FEAR, ESTHER_RESOLVE,
                        MORDECAI_SACK, COLD, GOLDEN, RED)
from est import ch01 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, NIGHT = "#0B1A2E", "#0F0E2A"


@P("EST-C02-00-Title", "Chapter 2 · For Such a Time as This", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.kings_gate("t2", 760, 820, 301, mord="sack", sky=("#5A5A7A", "#C8B8A8"))}</g><rect x="0" y="0" width="760" height="262" fill="#5A5A7A"></rect>')
    return chapter_title(2, "第二話", "For Such a Time as This", "Esther 3 – 4", svg, "#3A3448", v("4:16", frm="and if I perish"), "Esther · Volume Seventeen")


SEGS = [drawn([caps("3:1")], "ESTH 3:1", below(lambda w, h: K.promoted("pm3", w, h, 302), 0.2), "#C8B08A", head="Haman the Agagite", stamp=3, h=330),
        drawn([caps("3:2"), cp("3:3", to="said unto Mordecai,"), say("3:3", frm="Why transgressest")], "ESTH 3:2–3",
              below(lambda w, h: K.kings_gate("kg3", w, h, 303, mord="stand", bowing=True, haman_by=True), 0.4), "#8FD0E2", head="Mordecai Bowed Not Down"),
        face([caps("3:4-6")], "ESTH 3:4–6", HAMAN, bg=RED),
        drawn([caps("3:7")], "ESTH 3:7", below(lambda w, h: K.pur_wheel(w, h), 0.26), "#1A0E14", head="Pur, That Is, the Lot"),
        face([cp("3:8", to="unto king Ahasuerus,"), say("3:8", frm="There is a certain"), says("3:9")], "ESTH 3:8–9", HAMAN, bg=RED, head="A Certain People"),
        drawn([caps("3:10"), cp("3:11", to="said unto Haman,"), say("3:11", frm="The silver")], "ESTH 3:10–11", below(lambda w, h: K.ring_given(w, h, 304), 0.42), "#2A1040"),
        drawn([caps("3:12")], "ESTH 3:12", below(lambda w, h: K.scribes("sc3", w, h, 305, ring=True), 0.36), "#C8B08A", head="Sealed with the King's Ring"),
        drawn([caps("3:13-14")], "ESTH 3:13–14", below(lambda w, h: K.empire_map(w, h, posts=True), 0.3), MAP),
        drawn([caps("3:15")], "ESTH 3:15", below(lambda w, h: K.two_drink("td3", w, h, 306), 0.2), "#3A2A5A")]
PG.extend(pack(SEGS, "EST-C02-D", PG.next()))
SEGS2 = [drawn([caps("4:1-2")], "ESTH 4:1–2", below(lambda w, h: K.kings_gate("kg4", w, h, 401, mord="sack", sky=("#5A5A7A", "#C8B8A8")), 0.3), "#5A5A7A",
               head="Sackcloth and Ashes", stamp=4),
         drawn([caps("4:3")], "ESTH 4:3", below(lambda w, h: K.mourning("mo4", w, h, 402), 0.2), "#5A5A6A"),
         face([caps("4:4-5")], "ESTH 4:4–5", ESTHER_GRIEF, bg=COLD, head="Hathach"),
         drawn([caps("4:6-8")], "ESTH 4:6–8", below(lambda w, h: K.broad_place("bp4", w, h, 403), 0.36), "#8A9AB8"),
         face([caps("4:9-10"), says("4:11")], "ESTH 4:9–11", ESTHER_FEAR, bg=COLD),
         face([caps("4:12"), cp("4:13", to="answer unto Esther,"), say("4:13", frm="Think not"), says("4:14")], "ESTH 4:12–14", MORDECAI_SACK, bg=COLD,
              head="For Such a Time as This"),
         face([caps("4:15"), says("4:16")], "ESTH 4:15–16", ESTHER_RESOLVE, head="If I Perish, I Perish"),
         drawn([caps("4:17")], "ESTH 4:17", below(lambda w, h: K.fast_night("fn4", w, h, 404), 0.16), NIGHT, h=300)]
PG.extend(pack(SEGS2, "EST-C02-E", PG.next(), end=end_mark("NEXT · THE KING COULD NOT SLEEP", "right: 10px; bottom: 34px")))
