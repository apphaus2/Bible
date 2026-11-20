"""The Jude volume of the full edition (the Epistle of Jude): metadata, the volume cover, and the chapter plan (ch01.py).

Built on the letters' shared kit, tools/full/epistle.py (EpistleKit), as the other letters are: the writer is "Jude, a servant
of Jesus Christ, and brother of James" (1:1). Paul is never drawn in this volume. Jude's faces are kept in jas/common.py with
the other writers of the general letters.

A letter has no narration: every word of the ASV here is Jude writing (letter boxes, tailed toward Jude's face). Michael's
words to the devil (1:9 "The Lord rebuke thee") are an untailed speech balloon over the drawing; Enoch's prophecy (1:14–15)
is a song box. Jude is a one-chapter book: its verses are 1:1–25.

Jude's face is new, with a family likeness to his brother James (jas.common.JUDE: James' features and skin, a grey-brown
beard and hair, a dark slate headcloth with a cord), in the kit's five lights: stern at 1:3–4 and 1:16–19 (the ungodly men
crept in, the mockers), gold elsewhere. At a distance he is jas.art.jude_fig (a grey-olive robe, the slate headcloth, a dark
grey mantle).

Drawings (jud.art): Jude writing by lamplight in a house of Judæa, a young scribe on his mat, the hills under the stars
through the window (the title page and 1:1–2); the people saved out of Egypt walking through the sea between the walls of
water, the pillar of fire behind them (1:5; "afterward destroyed them that believed not" is words); the smoke of Sodom and
Gomorrah going up over the empty plain (1:6–8: the angels in everlasting bonds under darkness are words only); mount Nebo
in the land of Moab, the valley below empty, no grave to be seen, and Michael the archangel as a figure of white light with a
gold rim and no face standing on the slope (1:9: the devil is never drawn; "The Lord rebuke thee" in a balloon from the
light); the way of Cain, the error of Balaam and the gainsaying of Korah as a plate of three — two altars, the smoke of
one going up and of the other beaten down; Balaam's purple headcloth on the grey ass; the rent ground and the censers left
lying (1:11, no one drawn falling); hidden rocks, clouds without water, autumn trees twice dead, wild waves foaming and
wandering stars as a plate of five (1:12–13); Enoch, the seventh from Adam, on a hill at night, the sky full of the
lights of the ten thousands (1:14–15; the holy ones are points of light, nothing more); building up yourselves on your most holy faith, 1 Peter's builders
setting the stones on the corner stone (1:20–21); a brand snatched out of the fire
(1:23); the doxology over the light (1:24–25).

Restraint: the ungodly men (1:4, 1:8, 1:10, 1:16–19) are words beside Jude's stern face or over empty places, never drawn;
1:7 fornication and strange flesh are words over Sodom's smoke and the empty plain; 1:11 Cain's deed is two altars only,
Korah's end is the rent ground with no one in it. God is never drawn (light; 1:14 the Lord coming is the song box over the
lights); Satan is never drawn; Michael is white light with a gold rim and no face.

Plan (630 words, one chapter): 1 Contend for the Faith (1–25)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("JUD")

META = {
  "id": "jude", "order": 65, "name": "Jude", "kanji": "ユダの手紙", "thumb": "vol-jude-", "book": "JUD",
  "title": "Jude Volume", "volume": "Volume Sixty-Five",
  "lede": "The sixty-fifth book of the Bible, in full: the letter of Jude, a servant of Jesus Christ and brother of James — contend earnestly for the faith once for all delivered unto the saints; the people saved out of Egypt, the angels that kept not their principality, Sodom and Gomorrah; Michael the archangel and the body of Moses; the way of Cain, the error of Balaam, the gainsaying of Korah; hidden rocks, clouds without water, wandering stars; Enoch's prophecy; keep yourselves in the love of God; now unto him that is able to guard you from stumbling, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Contend for the Faith", "range": "Jude 1–25", "bible_chapters": [1],
     "blurb": "Jude, a servant of Jesus Christ, and brother of James: contend earnestly for the faith which was once for all delivered unto the saints; certain men crept in privily; the Lord saved a people out of the land of Egypt; angels that kept not their own principality; Sodom and Gomorrah; Michael the archangel, disputing about the body of Moses: The Lord rebuke thee; the way of Cain, the error of Balaam, the gainsaying of Korah; hidden rocks, clouds without water, autumn trees twice dead, wild waves, wandering stars; Enoch prophesied; build up yourselves on your most holy faith; now unto him that is able to guard you from stumbling."},
  ],
}
