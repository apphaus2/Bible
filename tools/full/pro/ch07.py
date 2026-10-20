"""Proverbs volume, Chapter 7 — The King's Heart (Proverbs 19–21). Every verse, word for word from ref/eng-asv.
Saying cells: the poor that walketh in his integrity; the king's wrath as the roaring of a lion; the contentions of a wife a
continual dropping; the sluggard's hand in the dish; wine is a mocker; the sluggard will not plow by reason of the winter;
diverse weights; the lamp of Jehovah; the king's heart in the hand of Jehovah as the watercourses (a drawn cell, God never
drawn); the corner of the housetop; the horse prepared against the day of battle."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from pro import G, art4 as K
from pro.common import sayings, cellv, run
from pro import ch06 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PRO-C07-00-Title", "Chapter 7 · The King's Heart", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#5A8FC8"></rect><g transform="translate(0 300)">{K.watercourses("t7", 760, 780, 701)}</g>')
    return chapter_title(7, "第七話", "The King's Heart", "Proverbs 19 – 21", svg, "#3A6A9A", v("21:1", to="watercourses:"), "Proverbs · Volume Twenty")


ITEMS = (run(19, 1, 29, head="Better Is the Poor That Walketh in His Integrity", embs={14: "woman", 24: "bread", 6: "gift"})
         + run(20, 1, 30, head="Wine Is a Mocker", embs={4: "plough", 5: "well", 6: "friends", 13: "bed", 26: "chaff", 9: "face_sad", 27: "lamp"})
         + [cellv("21:1", art=lambda w, h: K.watercourses("wc7", w, h, 702), bg="#5A8FC8", head="The King's Heart Is in the Hand of Jehovah")]
         + run(21, 2, 31, embs={2: "scales", 3: "altar", 27: "altar", 19: "clouds_dry", 6: "chaff"}))
PG.extend(sayings(ITEMS, "PRO-C07-S", PG.next(), "Better Is the Poor That Walketh in His Integrity", end=end_mark("NEXT · THE WORDS OF THE WISE", "right: 10px; bottom: 10px")))
