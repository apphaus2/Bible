"""Nehemiah volume, Chapter 3 — The Work Finished (Nehemiah 5–6). Every verse, word for word from ref/eng-asv.
A great cry of the people against their brethren — we are mortgaging our fields; Nehemiah contends with the nobles — ye
exact usury; we will restore them; he shakes out his lap, and all the assembly said, Amen; twelve years without the bread
of the governor, and the provision of one day as a tally board; then Sanballat and Geshem: come, let us meet in the plain
of Ono (a map) — I am doing a great work, so that I cannot come down; the open letter; Shemaiah shut up — should such a man
as I flee?; and the wall finished in the twenty and fifth day of Elul, in fifty and two days; Tobiah's letters."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from neh import G, art as K
from neh.common import (pack, cp, say, says, caps, drawn, face, joined, NEHEMIAH, NEHEMIAH_PRAY, NEHEMIAH_STERN, SANBALLAT, TOBIAH, GESHEM,
                        JUDAH_MAN, PEOPLE, MOTHER, NOBLE, SHEMAIAH, COLD, GOLDEN, RED)
from neh import ch02 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, SKY = "#0B1A2E", "#8FD0E2"


@P("NEH-C03-00-Title", "Chapter 3 · The Work Finished", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 330)">{K.wall_done("t3", 760, 640, 301)}</g><rect x="0" y="0" width="760" height="332" fill="#FFC890"></rect>'
                '<rect x="0" y="968" width="760" height="120" fill="#C8A06A"></rect>')
    return chapter_title(3, "第三話", "The Work Finished", "Nehemiah 5 – 6", svg, "#8A5A3A", v("6:3", frm="I am doing a great work,", to="cannot come down:"), "Nehemiah · Volume Sixteen")


SEGS = [drawn([caps("5:1"), cp("5:2", to="that said,"), say("5:2", frm="We, our sons")], "NEH 5:1–2", below(lambda w, h: K.outcry("oc3", w, h, 302), 0.36), "#C8A890",
              head="A Great Cry", stamp=5),
        face([cp("5:3", to="that said,"), say("5:3", frm="We are mortgaging"), cp("5:4", to="that said,"), say("5:4", frm="We have borrowed")], "NEH 5:3–4", JUDAH_MAN, bg=COLD),
        face([says("5:5")], "NEH 5:5", MOTHER, bg=COLD),
        face([caps("5:6"), cp("5:7", to="and said unto them,"), say("5:7", frm="Ye exact usury", to="of his brother."), cp("5:7", frm="And I held")], "NEH 5:6–7",
             NEHEMIAH_STERN, bg=RED, head="Ye Exact Usury"),
        face([cp("5:8", to="And I said unto them,"), say("5:8", frm="We after our ability", to="sold unto us?"), cp("5:8", frm="Then held they")], "NEH 5:8", NEHEMIAH_STERN, bg=RED),
        face([cp("5:9", to="Also I said,"), joined("say", ("5:9", "The thing that ye do"), "5:10", "5:11")], "NEH 5:9–11", NEHEMIAH),
        face([cp("5:12", to="Then said they,"), say("5:12", frm="We will restore", to="as thou sayest."), cp("5:12", frm="Then I called")], "NEH 5:12", NOBLE),
        drawn([cp("5:13", to="and said,"), say("5:13", frm="So God shake out", to="and emptied."), cp("5:13", frm="And all the assembly said,", to="said,"),
               say("5:13", frm="Amen,", to="Amen,"), cp("5:13", frm="and praised Jehovah.")], "NEH 5:13", below(lambda w, h: K.shake_lap("sl3", w, h, 303), 0.4), SKY,
              head="So God Shake Out Every Man"),
        face([caps("5:14-16")], "NEH 5:14–16", NEHEMIAH, head="The Bread of the Governor"),
        drawn([caps("5:17-18")], "NEH 5:17–18", below(lambda w, h: K.tally(w, h, [("AT MY TABLE", "150", "#FFD23F"), ("OX", "1", "#FF8A6A"), ("CHOICE SHEEP", "6", "#8FD0E2"),
                                                                                  ("STORE OF WINE", "10 DAYS", "#C8A0E8")], "PREPARED FOR ONE DAY"), 0.42), "#1A1430"),
        face([says("5:19")], "NEH 5:19", NEHEMIAH_PRAY, bg=COLD)]
PG.extend(pack(SEGS, "NEH-C03-D", PG.next()))
SEGS2 = [drawn([caps("6:1"), cp("6:2", to="saying,"), say("6:2", frm="Come, let us meet", to="plain of Ono."), cp("6:2", frm="But they thought")], "NEH 6:1–2",
               below(lambda w, h: K.ono_map(w, h), 0.4), MAP, head="The Plain of Ono", stamp=6),
         face([cp("6:3", to="saying,"), say("6:3", frm="I am doing"), caps("6:4")], "NEH 6:3–4", NEHEMIAH),
         drawn([caps("6:5"), cp("6:6", to="wherein was written,"), joined("say", ("6:6", "It is reported"), "6:7")], "NEH 6:5–7", below(lambda w, h: K.ono_map(w, h, letter=True), 0.5),
               MAP, head="An Open Letter"),
         face([cp("6:8", to="saying,"), say("6:8", frm="There are no such")], "NEH 6:8", NEHEMIAH_STERN, bg=RED),
         drawn([cp("6:9", to="saying,"), say("6:9", frm="Their hands", to="be not done."), say("6:9", frm="But now, O God,")],
               "NEH 6:9", below(lambda w, h: K.builders("bd3", w, h, 304, top=0.66), 0.5), SKY),
         face([cp("6:10", to="and he said,"), say("6:10", frm="Let us meet")], "NEH 6:10", SHEMAIAH, bg=COLD),
         face([cp("6:11", to="And I said,"), say("6:11", frm="Should such")], "NEH 6:11", NEHEMIAH_STERN, bg=RED),
         face([caps("6:12-13"), says("6:14")], "NEH 6:12–14", NEHEMIAH_PRAY, bg=COLD),
         drawn([caps("6:15-16")], "NEH 6:15–16", below(lambda w, h: K.wall_done("wd3", w, h, 306), 0.3), "#FFC890", head="In Fifty and Two Days"),
         drawn([caps("6:17-19")], "NEH 6:17–19", below(lambda w, h: K.letters_seal(w, h, 307), 0.42), "#3A1A3A")]
PG.extend(pack(SEGS2, "NEH-C03-E", PG.next(), end=end_mark("NEXT · THE GENEALOGY OF THE RETURN", "right: 10px; bottom: 34px")))
