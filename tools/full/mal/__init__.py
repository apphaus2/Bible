"""The Malachi volume of the full edition: metadata, the volume cover, and the one chapter (ch01.py). The last book of the
Old Testament.

Built on the minor prophets' kit (oba/minor.py). Jehovah's disputation with his people — I have loved you; yet ye say,
Wherein? — is in the Voice box throughout, the people's questions quoted within it; the prophet's own words (2:10–15, 2:17)
are song lines beside his face; 1:1 and 3:16 are captions. Malachi: young, stubble, an off-white headcloth with a dark cord
(mal.common.MALACHI). The sun of righteousness is a sun whose rays spread as wings (no figure); Elijah is 1 Kings' Elijah
in his hairy mantle (kg1.art.elijah_fig). God is never drawn.

Plan (1,729 words, one chapter): 1 The Sun of Righteousness (1–4)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("MAL")

META = {
  "id": "malachi", "order": 39, "name": "Malachi", "kanji": "マラキ書", "thumb": "vol-malachi-", "book": "MAL",
  "title": "Malachi Volume", "volume": "Volume Thirty-Nine",
  "lede": "The thirty-ninth book of the Bible and the last of the Old Testament, in full: the burden of the word of Jehovah to Israel by Malachi — I have loved you, saith Jehovah; a son honoreth his father; behold, I send my messenger; will a man rob God?; a book of remembrance; the sun of righteousness with healing in its wings; and Elijah the prophet before the great and terrible day of Jehovah — every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Sun of Righteousness", "range": "Malachi 1–4", "bible_chapters": [1, 2, 3, 4],
     "blurb": "I have loved you, saith Jehovah — yet ye say, Wherein hast thou loved us?; the blind, the lame and the sick upon mine altar, and from the rising of the sun my name great among the Gentiles; the covenant with Levi; the wife of thy youth; behold, I send my messenger, and he is like a refiner's fire; will a man rob God? bring ye the whole tithe into the store-house, and I will open you the windows of heaven; a book of remembrance; the day that burneth as a furnace; unto you that fear my name shall the sun of righteousness arise with healing in its wings; and I will send you Elijah the prophet."},
  ],
}
