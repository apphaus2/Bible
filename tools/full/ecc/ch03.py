"""Ecclesiastes volume, Chapter 3 — A Good Name (Ecclesiastes 7–9). Every verse, word for word from ref/eng-asv.
The house of mourning and the house of feasting, a flask of precious oil between; the crackling of thorns under a pot; wisdom
a defence like a walled city; the day of prosperity and the day of adversity side by side, and a tree grown crooked; ten rulers
in the gate; far off and exceeding deep (a well in section); nets, snares and bands with nothing in them; one among a thousand
(a thousand marks, one lit); the king's word; the sepulchres at dusk; the city where neither day nor night seeth sleep; a
living dog and a lion lying still (no wound drawn); garments always white; the race not to the swift; the evil net; and the
little city and the poor wise man."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from ecc import G, art as K
from ecc.common import (paged, face, drawn, PREACHER, PREACHER_GOLD, PREACHER_WARM, PREACHER_STERN, PREACHER_NIGHT, COLD, GOLDEN, DUSK, RED)
from ecc import ch02 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ECC-C03-00-Title", "Chapter 3 · A Good Name", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#2A2A3A"></rect><g transform="translate(0 300)">{K.two_houses("t3", 760, 780, 301)}</g>')
    return chapter_title(3, "第三話", "A Good Name", "Ecclesiastes 7 – 9", svg, "#3A2A3A", v("7:1", to="precious oil;"), "Ecclesiastes · Volume Twenty-One")


PAGE = [[drawn("7:1-4", lambda w, h: K.two_houses("th3", w, h, 302), "linear-gradient(90deg, #2A2A3A 0%, #5A4A5A 50%, #E8A04A 50%, #FFD890 100%)", head="A Good Name", stamp=7)],
        [drawn("7:5-7", lambda w, h: K.thorns_pot(w, h, 303), "#1A1214"),
         face("7:8-10", PREACHER_STERN, bg=RED)],
        [drawn("7:11-12", lambda w, h: K.defence("df3", w, h, 304), "#8FD0E2"),
         drawn("7:13-14", lambda w, h: K.day_night(w, h, 305), "linear-gradient(90deg, #8FD0E2 0%, #8FD0E2 50%, #3A3A4A 50%, #3A3A4A 100%)")],
        [face("7:15-18", PREACHER_WARM, bg=DUSK),
         drawn("7:19-22", lambda w, h: K.ten_rulers("tr3", w, h, 306), "#E8C8A0")],
        [drawn("7:23-25", lambda w, h: K.deep_well(w, h, 307), "#0B1A2E", head="Far Off and Exceeding Deep")],
        [drawn("7:26", lambda w, h: K.snares(w, h, 308), "#5A4A5A"),
         drawn("7:27-29", lambda w, h: K.thousand(w, h, 309), "#0B1A2E")],
        [drawn("8:1-5", lambda w, h: K.throne_room("tk3", w, h, 310), "#8A4A26", head="The King's Word", stamp=8)],
        [face("8:6-8", PREACHER, bg=COLD),
         drawn("8:9-11", lambda w, h: K.tombs(w, h, 311), "#3A2A4A")],
        [face("8:12-14", PREACHER_GOLD),
         drawn("8:15", lambda w, h: K.vine_fig("vf3", w, h, 312), "#8FD0E2")],
        [drawn("8:16-17", lambda w, h: K.city_night(w, h, 313), "#05051A"),
         face("9:1-3", PREACHER_NIGHT, bg=COLD, head="One Event unto All", stamp=9)],
        [drawn("9:4-6", lambda w, h: K.dog_lion(w, h, 314), "#8FD0E2"),
         drawn("9:7-9", lambda w, h: K.white_garments("wg3", w, h, 315), "#8FD0E2")],
        [drawn("9:10-11", lambda w, h: K.race("rc3", w, h, 316), "#8FD0E2"),
         drawn("9:12", lambda w, h: K.nets(w, h, 317), "#8FB8D0")],
        [drawn("9:13-15", lambda w, h: K.little_city("lc3", w, h, 318), "#C8B8A0", head="The Poor Wise Man"),
         face("9:16-18", PREACHER)]]
PG.extend(paged(PAGE, "ECC-C03-", PG.next(), end=end_mark("NEXT · REMEMBER THY CREATOR", "right: 10px; bottom: 34px")))
