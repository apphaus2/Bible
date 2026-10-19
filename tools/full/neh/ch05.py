"""Nehemiah volume, Chapter 5 — The Book of the Law (Nehemiah 8–9). Every verse, word for word from ref/asv.
All the people gathered as one man before the water gate; Ezra the scribe upon the pulpit of wood, six on his right hand and
seven on his left, reading from early morning until midday; Amen, Amen, with the lifting up of their hands; the Levites
giving the sense; this day is holy — the joy of Jehovah is your strength; the booths of olive, myrtle and palm on every
roof; then the twenty and fourth day, with fasting and sackcloth, the Levites upon the stairs, and their prayer in full —
thou art Jehovah, even thou alone — told over the story it tells: the heavens, Abram, the Red Sea, the pillar of cloud and
of fire, Sinai, the manna and the rock, the molten calf, the good land, the judges and the prophets, and we are servants
this day; and yet for all this we make a sure covenant."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from neh import G, art as K
from neh.common import pack, cp, say, says, caps, drawn, face, joined, NEHEMIAH, EZRA, LEVITE, COLD, GOLDEN, RED
from neh import ch04 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, BOARD, SKY, DAWN = "#0B1A2E", "#1A1430", "#8FD0E2", "#FFE6B0"


@P("NEH-C05-00-Title", "Chapter 5 · The Book of the Law", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 330)">{K.pulpit("t5", 760, 640, 501)}</g><rect x="0" y="0" width="760" height="332" fill="#FFE6B0"></rect>'
                '<rect x="0" y="968" width="760" height="120" fill="#D8C8A0"></rect>')
    return chapter_title(5, "第五話", "The Book of the Law", "Nehemiah 8 – 9", svg, "#8A6A3A", v("8:10", frm="for the joy of Jehovah"), "Nehemiah · Volume Sixteen")


def art(lines, ref, fn, bg, k=0.4, **kw):
    return drawn(lines, ref, below(fn, k), bg, **kw)

SEGS = [art([caps("8:1-2")], "NEH 8:1–2", lambda w, h: K.pulpit("pu5", w, h, 502, read=False), DAWN, 0.3, head="Ezra the Scribe", stamp=8),
        art([caps("8:3")], "NEH 8:3", lambda w, h: K.pulpit("pu5b", w, h, 503), DAWN, 0.24),
        art([caps("8:4")], "NEH 8:4", lambda w, h: K.pulpit("pu5c", w, h, 504, crowd=False, read=False), DAWN, 0.3),
        art([caps("8:5"), cp("8:6", to="answered,"), say("8:6", frm="Amen, Amen,", to="Amen, Amen,"), cp("8:6", frm="with the lifting up")], "NEH 8:5–6",
            lambda w, h: K.amen("am5", w, h, 505), DAWN, 0.42),
        art([caps("8:7-8")], "NEH 8:7–8", lambda w, h: K.teachers("tc5", w, h, 506), SKY, 0.36),
        face([cp("8:9", to="said unto all the people,"), say("8:9", frm="This day is holy", to="nor weep."), cp("8:9", frm="For all the people wept")], "NEH 8:9", EZRA,
             head="The Joy of Jehovah"),
        face([cp("8:10", to="Then he said unto them,"), say("8:10", frm="Go your way")], "NEH 8:10", NEHEMIAH),
        face([cp("8:11", to="saying,"), say("8:11", frm="Hold your peace")], "NEH 8:11", LEVITE),
        art([caps("8:12")], "NEH 8:12", lambda w, h: K.feast_tents("ft5", w, h, 507), "#FFB04A", 0.24),
        art([caps("8:13-14"), cp("8:15", to="saying,"), say("8:15", frm="Go forth")], "NEH 8:13–15", lambda w, h: K.branches(w, h, 508), MAP, 0.46, head="Booths"),
        art([caps("8:16-17")], "NEH 8:16–17", lambda w, h: K.booths("bo5", w, h, 509), SKY, 0.3),
        art([caps("8:18")], "NEH 8:18", lambda w, h: K.pulpit("pu5d", w, h, 510), DAWN, 0.2)]
PG.extend(pack(SEGS, "NEH-C05-D", PG.next()))
SEGS2 = [art([caps("9:1-3")], "NEH 9:1–3", lambda w, h: K.fasting("fs5", w, h, 511), "#6A6A7A", 0.36, head="With Fasting and Sackcloth", stamp=9),
         art([caps("9:4")], "NEH 9:4", lambda w, h: K.stairs("st5", w, h, 512), SKY, 0.24),
         face([cp("9:5", to="Pethahiah, said,"), say("9:5", frm="Stand up and bless")], "NEH 9:5", LEVITE),
         art([says("9:6")], "NEH 9:6", lambda w, h: K.heavens(w, h, 513), "#0B0B2A", 0.4, head="Thou Art Jehovah"),
         art([says("9:7-8")], "NEH 9:7–8", lambda w, h: K.abram_stars("ab5", w, h, 514), "#0B0B2A", 0.44),
         art([says("9:9-11")], "NEH 9:9–11", lambda w, h: K.red_sea(w, h, 515), "#0B2E4A", 0.46),
         art([says("9:12")], "NEH 9:12", lambda w, h: K.pillars(w, h, 516), "#2A2A5A", 0.3),
         art([says("9:13-14")], "NEH 9:13–14", lambda w, h: K.sinai_scene(w, h, 517), "#2A1A2A", 0.4),
         art([says("9:15")], "NEH 9:15", lambda w, h: K.manna_rock(w, h, 518), "#FFC890", 0.36),
         face([says("9:16-17")], "NEH 9:16–17", LEVITE, bg=COLD, head="A God Ready to Pardon"),
         art([says("9:18")], "NEH 9:18", lambda w, h: K.calf_scene(w, h, 519), "#5A2A1A", 0.3),
         art([says("9:19-21")], "NEH 9:19–21", lambda w, h: K.pillars(w, h, 520), "#2A2A5A", 0.5),
         art([says("9:22-23")], "NEH 9:22–23", lambda w, h: K.east_jordan(w, h, hi=("BASHAN", "GILEAD")), MAP, 0.42),
         art([says("9:24-25")], "NEH 9:24–25", lambda w, h: K.good_land(w, h, 522), SKY, 0.48),
         face([says("9:26-27")], "NEH 9:26–27", LEVITE, bg=COLD),
         face([says("9:28-29")], "NEH 9:28–29", LEVITE),
         face([says("9:30-31")], "NEH 9:30–31", LEVITE, bg=COLD),
         face([says("9:32-35")], "NEH 9:32–35", LEVITE, head="Now Therefore, Our God"),
         art([says("9:36-37")], "NEH 9:36–37", lambda w, h: K.servants("sv5", w, h, 523), "#C8A890", 0.42),
         art([says("9:38")], "NEH 9:38", lambda w, h: K.sealed_scroll(w, h, 524), "#2A1A2A", 0.24)]
PG.extend(pack(SEGS2, "NEH-C05-E", PG.next(), end=end_mark("NEXT · THE SEALED COVENANT", "right: 10px; bottom: 34px")))
