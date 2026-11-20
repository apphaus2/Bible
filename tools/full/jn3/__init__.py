"""The 3 John volume of the full edition (the Third Epistle of John): metadata, the volume cover, and the chapter plan
(ch01.py), one short manga chapter, as Obadiah's.

Built on 1 and 2 John's kit and drawings (jn1.common, jn1.art, jn2.art: the epistle kit's letter boxes, John the elder's faces
and figure, the study at Ephesus, the house fronts). A letter has no narration: every word of the ASV here is the elder
writing to Gaius (letter boxes: parchment, a sepia rule down the left edge, a short tail toward John where his face is drawn).
Nothing is quoted from scripture and God's own words are not quoted: no song box, no Voice box.

John, "the elder", is the beloved disciple of the Gospels grown very old at Ephesus (jn1.common: ntcast JOHN's features, white
hair, a long white beard); his face (earnest gold) beside "imitate not that which is evil" (11); at a distance john_fig, a
faded rust robe, a slate-grey mantle, a staff — seated at his table (1–4, 13), among the brethren (12), at his door (14).

3 John's cast (jn1.common looks and faces, jn3.art figures), each the same everywhere; every headcloth cool, dark or off-white
(a warm one would read as long hair): Gaius the beloved, a grey beard and an off-white headcloth, a brown robe, a slate mantle;
Diotrephes, a black beard, a near-black headcloth with a gold cord, a dark plum robe and a wine mantle, a hard face; Demetrius,
a brown beard, a dark-teal headcloth, a teal-grey robe, with a staff and the sealed letter (he may be its bearer); the brethren
travelling for the Name with staffs and satchels.

Restraint: Diotrephes' "prating against us with wicked words" and his casting the brethren out of the church (10) are drawn
only as a man standing in a doorway with his arm out barring it, the brethren going away down the step, the elder's letter
lying unopened there — no violence. God is never drawn.

Plan (299 words, one chapter): 1 Gaius the Beloved (3 John 1–14): the brethren bear witness; Gaius receiving the brethren
and strangers; Diotrephes; imitate that which is good; Demetrius; ink and pen laid aside; the friends salute thee."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("3JN")

META = {
  "id": "3john", "order": 64, "name": "3 John", "kanji": "ヨハネの第三の手紙", "thumb": "vol-3john-", "book": "3JN",
  "title": "3 John Volume", "volume": "Volume Sixty-Four",
  "lede": "The sixty-fourth book of the Bible, in full: the elder's letter unto Gaius the beloved — I pray that in all things thou mayest prosper; greater joy have I none than this, to hear of my children walking in the truth; a faithful work toward the brethren and strangers; fellow-workers for the truth; Diotrephes, who loveth to have the preeminence; imitate not that which is evil, but that which is good; Demetrius hath the witness of all men; not with ink and pen, but face to face; the friends salute thee, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Gaius the Beloved", "range": "3 John 1", "bible_chapters": [1],
     "blurb": "The elder unto Gaius the beloved, whom I love in truth; I pray that thou mayest prosper and be in health, even as thy soul prospereth; greater joy have I none than this, to hear of my children walking in the truth; thou doest a faithful work toward them that are brethren and strangers withal; we ought to welcome such, that we may be fellow-workers for the truth; Diotrephes, who loveth to have the preeminence among them, receiveth us not; imitate not that which is evil, but that which is good; Demetrius hath the witness of all men; I am unwilling to write with ink and pen, but we shall speak face to face; peace be unto thee; the friends salute thee."},
  ],
}
