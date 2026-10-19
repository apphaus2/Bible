"""The Lamentations volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ch02.py).

The five laments are set as song lines (lam.common.lament: one song box per verse, the acrostic stanzas kept whole) over
drawings of the desolate city — the city sitting solitary as a widow, the ways of Zion mourning, the gates sunk into the ground,
the wall broken, the elders in the dust, ashes — with the faces of the mourners (Zion as a widow; a grey mourner for the man that
hath seen affliction; the elders) between. Drawings come from jer.art (Jeremiah's volume) and lam.art.

Restraint: the famine and the slain (2:11–12, 2:20–21, 4:4–10, 5:10–12) are words over empty streets, shut doors, a cold
hearth and broken walls; no one is drawn suffering; God is never drawn.

Plan (3,421 words, two chapters): 1 How Doth the City Sit Solitary (1–2) · 2 His Compassions Fail Not (3–5)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("LAM")

META = {
  "id": "lamentations", "order": 25, "name": "Lamentations", "kanji": "哀歌", "thumb": "vol-lamentations-", "book": "LAM",
  "title": "Lamentations Volume", "volume": "Volume Twenty-Five",
  "lede": "The twenty-fifth book of the Bible, in full: five laments over Jerusalem fallen — the city sitting solitary as a widow, her gates sunk into the ground, the elders silent in the dust — and in the midst of them, his compassions fail not, they are new every morning, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "How Doth the City Sit Solitary", "range": "Lamentations 1–2", "bible_chapters": [1, 2],
     "blurb": "How doth the city sit solitary, that was full of people! She is become as a widow; she weepeth sore in the night; the ways of Zion do mourn; is it nothing to you, all ye that pass by?; the Lord hath covered the daughter of Zion with a cloud in his anger; her gates are sunk into the ground; the elders sit upon the ground and keep silence; thy breach is great like the sea: who can heal thee?"},
  ],
}
