"""2 Chronicles volume, Chapter 7 — The Battle Is Not Yours (2 Chronicles 20–21). Every verse, word for word from ref/asv.
Moab, Ammon and mount Seir at En-gedi (a map); Jehoshaphat's fast and his prayer before the new court — our eyes are upon
thee; Jahaziel in the midst of the assembly — the battle is not yours, but God's; stand ye still; the singers in holy array
going out before the army — give thanks unto Jehovah; the liers-in-wait and the valley from the watch-tower (20:22–25 words
over the strewn field, no one drawn); the valley of Beracah; the ships broken at Ezion-geber; then Jehoram, who slew his
brethren (21:4 words only), Edom's revolt, the writing from Elijah, and his sickness (21:18–19 words only)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from chr2 import G, art as K
from chr2.common import (pack, cp, say, gd, says, gods, caps, drawn, face, joined, cell, cells, roll, JEHOSHAPHAT, JAHAZIEL, MESSENGER, PROPHET, JEHORAM, COLD, GOLDEN, RED)
from chr2 import ch06 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
MAP, NIGHT = "#0B1A2E", "#0F0E2A"
PRAY = lambda seed: below(lambda w, h: K.court_scene("pr%d" % seed, w, h, seed, solomon="bless"), 0.5)


@P("2CH-C07-00-Title", "Chapter 7 · The Battle Is Not Yours", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.singers_march("t7", 760, 820, 701)}</g><rect x="0" y="0" width="760" height="262" fill="#5A4A7A"></rect>')
    return chapter_title(7, "第七話", "The Battle Is Not Yours", "2 Chronicles 20 – 21", svg, "#5A4A7A", v("20:15", frm="for the battle is not yours,"), "2 Chronicles · Volume Fourteen")


SEGS = [drawn([caps("20:1"), cp("20:2", to="saying,"), say("20:2", frm="There cometh")], "2CHR 20:1–2", below(lambda w, h: K.tekoa_map(w, h), 0.3), MAP, head="A Great Multitude", stamp=20),
        drawn([caps("20:3-5")], "2CHR 20:3–5", below(lambda w, h: K.court_scene("cs7", w, h, 702), 0.4), "#8FD0E2"),
        face([cp("20:6", to="and he said,"), say("20:6", frm="O Jehovah,"), says("20:7")], "2CHR 20:6–7", JEHOSHAPHAT, bg=COLD, head="Our Eyes Are upon Thee"),
        face([says("20:8-9")], "2CHR 20:8–9", JEHOSHAPHAT),
        face([says("20:10-12")], "2CHR 20:10–12", JEHOSHAPHAT, bg=COLD),
        drawn([caps("20:13-14")], "2CHR 20:13–14", below(lambda w, h: K.court_scene("cs7b", w, h, 703), 0.4), "#8FD0E2"),
        face([cp("20:15", to="and he said,"), say("20:15", frm="Hearken ye,", to="Thus saith Jehovah unto you,"), gd("20:15", frm="Fear not ye,")], "2CHR 20:15", JAHAZIEL,
             head="The Battle Is Not Yours, but God's"),
        face([gods("20:16-17")], "2CHR 20:16–17", JAHAZIEL, bg=NIGHT),
        drawn([caps("20:18-19")], "2CHR 20:18–19", below(lambda w, h: K.singers("sg7", w, h, 704, n=7, top=0.5), 0.36), "#FFB04A")]
PG.extend(pack(SEGS, "2CH-C07-D", PG.next()))
SEGS2 = [drawn([cp("20:20", to="Jehoshaphat stood and said,"), say("20:20", frm="Hear me,")], "2CHR 20:20", below(lambda w, h: K.tekoa_map(w, h, 1), 0.24), MAP, head="Believe in Jehovah"),
         drawn([cp("20:21", to="and say,"), say("20:21", frm="Give thanks")], "2CHR 20:21", below(lambda w, h: K.singers_march("sm7", w, h, 705), 0.24), "#5A4A7A"),
         drawn([caps("20:22-23")], "2CHR 20:22–23", below(lambda w, h: K.tekoa_map(w, h, 1), 0.36), MAP),
         drawn([caps("20:24-25")], "2CHR 20:24–25", below(lambda w, h: K.watchtower_view(w, h, 706), 0.36), "#8A7A8A"),
         drawn([caps("20:26")], "2CHR 20:26", below(lambda w, h: K.tekoa_map(w, h, 2), 0.2), MAP, head="The Valley of Beracah"),
         drawn([caps("20:27-30")], "2CHR 20:27–30", below(lambda w, h: K.singers("sg7b", w, h, 707, n=7, top=0.5), 0.36), "#FFB04A"),
         face([caps("20:31-34")], "2CHR 20:31–34", JEHOSHAPHAT, bg=COLD),
         drawn([caps("20:35-36"), cp("20:37", to="saying,"), say("20:37", frm="Because thou", to="destroyed thy works."), cp("20:37", frm="And the ships were broken,")], "2CHR 20:35–37",
               lambda w, h: K.broken_ships(w, h, 708), "#2A3A5A", head="The Ships Were Broken")]
PG.extend(pack(SEGS2, "2CH-C07-E", PG.next()))
R = cells(21, 1, 7, "Jehoram, King of Judah", "#FFD23F", head="Jehoram", budget=600)
PG.extend(roll(R, "2CH-C07-R", PG.next(), "THE KINGS OF JUDAH · 2 CHRONICLES 21"))
SEGS4 = [drawn([caps("21:8-10")], "2CHR 21:8–10", below(lambda w, h: K.K2.wars_map(w, h, hi=("VALLEY OF SALT",)), 0.4), MAP, head="Edom Revolted", stamp=21),
         face([caps("21:11")], "2CHR 21:11", JEHORAM, bg=RED),
         drawn([cp("21:12", to="the God of David thy father,"), joined("god", ("21:12", "Because thou"), "21:13")], "2CHR 21:12–13", lambda w, h: K.writing(w, h, 709), "#2A1A2A",
               head="A Writing from Elijah"),
         drawn([gods("21:14-15")], "2CHR 21:14–15", lambda w, h: K.writing(w, h, 710), "#2A1A2A"),
         drawn([caps("21:16-17")], "2CHR 21:16–17", lambda w, h: K.K3.burning_city(w, h, 711), "#2A0A0A"),
         drawn([caps("21:18-20")], "2CHR 21:18–20", lambda w, h: K.city_dusk("cd7", w, h, 712), "#2A1A3A")]
PG.extend(pack(SEGS4, "2CH-C07-G", PG.next(), end=end_mark("NEXT · JOASH", "right: 10px; bottom: 34px")))
