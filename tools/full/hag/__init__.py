"""The Haggai volume of the full edition: metadata, the volume cover, and the one chapter (ch01.py).

Built on the minor prophets' kit (oba/minor.py). The dated narration is in captions; Jehovah's words by Haggai in the Voice
box; the priests' answers (2:12–13) in speech boxes. The cast is Ezra's (ezr.common): Haggai (grey beard, a violet
headcloth with a cord), Zerubbabel the governor (a deep-blue headcloth with a gold band) and Joshua the high priest
(Jeshua: a white headcloth with a gold band). The house is Ezra's drawings of the work on the mount; the former glory a
dashed blueprint outline over the new walls; Zerubbabel the signet a gold ring glowing. God is never drawn.

Plan (1,091 words, one chapter): 1 Consider Your Ways (1–2)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("HAG")

META = {
  "id": "haggai", "order": 37, "name": "Haggai", "kanji": "ハガイ書", "thumb": "vol-haggai-", "book": "HAG",
  "title": "Haggai Volume", "volume": "Volume Thirty-Seven",
  "lede": "The thirty-seventh book of the Bible, in full: the word of Jehovah by Haggai the prophet in the second year of Darius — is it a time for you to dwell in your ceiled houses, while this house lieth waste? consider your ways; be strong, and work, for I am with you; the latter glory of this house shall be greater than the former; and Zerubbabel as a signet — every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Consider Your Ways", "range": "Haggai 1–2", "bible_chapters": [1, 2],
     "blurb": "In the second year of Darius: this people say, it is not the time for Jehovah's house to be built — is it a time for you to dwell in your ceiled houses, while this house lieth waste? consider your ways: ye have sown much, and bring in little, wages into a bag with holes; go up to the mountain, and bring wood; Zerubbabel and Joshua and the remnant obeyed, and came and did work; be strong, all ye people of the land — I will shake all nations, and the latter glory of this house shall be greater than the former; holy flesh in the skirt of a garment; from this day will I bless you; and I will make thee as a signet."},
  ],
}
