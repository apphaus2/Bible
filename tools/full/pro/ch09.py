"""Proverbs volume, Chapter 9 — Apples of Gold (Proverbs 25–27). Every verse, word for word from ref/asv.
These also are proverbs of Solomon, which the men of Hezekiah copied out (a drawn cell: the scribes at their scrolls); the
glory of kings to search out a matter; apples of gold in network of silver; the cold of snow in harvest; clouds and wind
without rain; coals of fire; cold waters to a thirsty soul; a city broken down; snow in summer; a dog that returneth to his
vomit; the door upon its hinges; the madman with firebrands; whoso diggeth a pit; iron sharpeneth iron; as in water face
answereth to face; and the state of thy flocks (27:23–27, a drawn cell)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from pro import G, art4 as K
from pro.common import sayings, cellv, run
from pro import ch08 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("PRO-C09-00-Title", "Chapter 9 · Apples of Gold", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#2A1A3A"></rect><g transform="translate(0 340)">{K.emb_art("apples", 760, 740, 901, k=2.4)}</g>')
    return chapter_title(9, "第九話", "Apples of Gold", "Proverbs 25 – 27", svg, "#3A1A3A", v("25:11"), "Proverbs · Volume Twenty")


ITEMS = ([cellv("25:1", art=lambda w, h: K.scribes("sc9", w, h, 902), bg="#4A2A18", head="The Men of Hezekiah Copied Out")]
         + run(25, 2, 28, groups=[(4, 5), (6, 7), (8, 10), (21, 22)],
               embs={2: "scroll", 3: "night", 8: "friends", 13: "snow", 15: "throne", 17: "house", 19: "face_sad", 20: "snow", 21: "cup", 23: "rain", 26: "fountain"})
         + run(26, 1, 28, head="As a Dog That Returneth", groups=[(4, 5), (18, 19), (24, 26)],
               embs={1: "snow", 6: "runner", 7: "face_fool", 8: "stone", 9: "thorns", 10: "arrows", 11: "dog", 12: "face_fool", 13: "lion", 14: "door", 15: "bread", 16: "bed",
                     17: "dog", 18: "fire", 20: "fire", 21: "coals", 22: "face_liar", 23: "crucible", 24: "face_liar", 27: "pit", 28: "face_liar"})
         + run(27, 1, 22, head="Iron Sharpeneth Iron",
               embs={1: "dawn", 3: "stone", 5: "face_listen", 8: "bird", 9: "friends", 14: "dawn", 16: "clouds_dry", 17: "iron", 18: "fig", 19: "reflection", 20: "grave",
                     21: "crucible", 22: "mortar"})
         + [cellv("27:23-27", art=lambda w, h: K.flocks("fl9", w, h, 903), bg="#8FD0E2", head="The State of Thy Flocks")])
PG.extend(sayings(ITEMS, "PRO-C09-S", PG.next(), "The Men of Hezekiah Copied Out", end=end_mark("NEXT · BOLD AS A LION", "right: 10px; bottom: 10px")))
