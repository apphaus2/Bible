"""The Hosea volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Built with dan.kit (the line and panel builders of the Daniel volume) and job.jdiscourse's packing. Most of the book is the
word of Jehovah, set in the Voice box over Israel's land: the vine, the dew, the threshing-floor, the cake not turned, the
silly dove, the calf of Samaria, the heifer, the lily and the olive-tree. The prophet's own words (and the people's) are
song boxes in Hosea's olive colour, tagged on the panel. Gomer and the children are told with restraint: faces, a house and
its door, a plate of the children's names, the price in silver and barley — never anything indecent. Restraint: the
stripping and the lovers of 2:2–13 words over the wilderness and the stripped vines; 9:14, 10:14 and 13:16 words over an
empty cradle, the ruins of Beth-arbel and Samaria dark; 13:7–8 the lion, the leopard and the bear as heraldic emblems;
God is never drawn.

Plan (5,179 words, three chapters): 1 A Door of Hope (1–3) · 2 The Cake Not Turned (4–8) · 3 I Will Be as the Dew (9–14)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("HOS")

META = {
  "id": "hosea", "order": 28, "name": "Hosea", "kanji": "ホセア書", "thumb": "vol-hosea-", "book": "HOS",
  "title": "Hosea Volume", "volume": "Volume Twenty-Eight",
  "lede": "The twenty-eighth book of the Bible, in full: Hosea's wife and children and the names Jezreel, Lo-ruhamah and Lo-ammi, the valley of Achor for a door of hope, Jehovah's controversy with Israel — the cake not turned, the silly dove, they sow the wind and reap the whirlwind — and the promise: I will be as the dew unto Israel, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "A Door of Hope", "range": "Hosea 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "The word of Jehovah to Hosea — go, take unto thee a wife; the children Jezreel, Lo-ruhamah and Lo-ammi; yet the number of the children of Israel shall be as the sand of the sea; contend with your mother; I will hedge up thy way with thorns; the valley of Achor for a door of hope; I will betroth thee unto me for ever; and Hosea's own words: go again, love a woman, and Israel many days without king and without prince."},
  ],
}
