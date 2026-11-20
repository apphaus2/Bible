"""The 2 John volume of the full edition (the Second Epistle of John): metadata, the volume cover, and the chapter plan
(ch01.py), one short manga chapter, as Obadiah's.

Built on 1 John's kit and drawings (jn1.common, jn1.art: the epistle kit's letter boxes, John the elder's faces and figure,
the study at Ephesus), as the letters before it are built on epistle.py. A letter has no narration: every word of the ASV
here is the elder writing to the elect lady (letter boxes: parchment, a sepia rule down the left edge, a short tail toward
John where his face is drawn). Nothing is quoted from scripture, and God's own words are not quoted, so there is no song box
and no Voice box.

John, "the elder", is the beloved disciple of the Gospels grown very old at Ephesus (jn1.common: ntcast JOHN's features, white
hair, a long white beard; earnest gold beside "that we love one another" (5–6), stern red beside the deceivers (7–9)); at a
distance john_fig, a faded rust robe, a slate-grey mantle, a staff.

The elect lady (jn1.common.LADY_LOOK, jn2.art.lady_fig): a slate-blue robe, a dark-blue veil, a darker mantle; her children
grown and young about her, in cool or off-white veils and headcloths or bareheaded (grown, child). The elect sister's
children (13) are drawn with John, their hands raised in greeting. A warm scarf would read as long hair: every veil and
headcloth here is cool, dark or off-white.

Restraint: the deceiver and the antichrist (7) are words only, beside John's stern face — no figure is drawn for them; the
one "that bringeth not this teaching" (10) is only a traveller seen from behind going away from the lady's shut door, his
face never shown. God is never drawn.

Plan (299 words, one chapter): 1 The Elect Lady (2 John 1–13): the lady and her children; walking in truth; love one
another; the deceivers; the shut door; paper and ink laid aside, face to face; the elect sister's children."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("2JN")

META = {
  "id": "2john", "order": 63, "name": "2 John", "kanji": "ヨハネの第二の手紙", "thumb": "vol-2john-", "book": "2JN",
  "title": "2 John Volume", "volume": "Volume Sixty-Three",
  "lede": "The sixty-third book of the Bible, in full: the elder's letter unto the elect lady and her children — whom I love in truth; I rejoice greatly that I have found certain of thy children walking in truth; that we love one another; many deceivers are gone forth into the world; look to yourselves; receive him not into your house; I hope to come unto you, and to speak face to face; the children of thine elect sister salute thee, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Elect Lady", "range": "2 John 1", "bible_chapters": [1],
     "blurb": "The elder unto the elect lady and her children, whom I love in truth; grace, mercy, peace; I rejoice greatly that I have found certain of thy children walking in truth; not a new commandment, but that which we had from the beginning, that we love one another; many deceivers are gone forth into the world; look to yourselves, that ye lose not the things which we have wrought; whosoever abideth in the teaching hath both the Father and the Son; receive him not into your house; I would not write them with paper and ink, but I hope to speak face to face; the children of thine elect sister salute thee."},
  ],
}
