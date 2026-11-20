"""The 2 Peter volume of the full edition (the Second Epistle General of Peter): metadata, the volume cover, and the chapter
plan (ch01.py).

Built on the letters' shared kit, tools/full/epistle.py (EpistleKit), as 1 Peter is: the writer is "Simon Peter, a servant
and apostle of Jesus Christ" (1:1), old and near his death — "the putting off of my tabernacle cometh swiftly, even as our
Lord Jesus Christ signified unto me" (1:14). Paul is never drawn in this volume: "our beloved brother Paul" (3:15) is his
letters, rolled scrolls in their pigeonholes. Peter's faces are kept in jas/common.py with the other writers of the general
letters.

A letter has no narration: every word of the ASV here is Peter writing (letter boxes, tailed toward Peter's face). The
Father's voice on the holy mount (1:17 "This is my beloved Son, in whom I am well pleased") is the Voice box; the true
proverb (2:22) is a song box.

Peter's face is ntcast's PETER grown old, in the kit's five lights (jas.common): white with joy at 1:3–4 and 3:9; stern at
the false teachers and the mockers (2:4, 2:10–12, 3:3–4, 3:11–12, 3:17); grieving at 2:20–21; gold elsewhere. At a distance
he is jas.art.peter_fig.

Drawings (pe2.art): Peter writing by lamplight at Rome, an old man seated now, a young scribe of the church at Rome on his mat
(the title page and 1:1–2); the eight graces as a stair of hewn steps, faith at the foot and love at the top (1:5–7);
Peter's tent at night, its pegs drawn and its cords loosed, the lamp burning low at the door — the putting off of his
tabernacle (1:13–15); the holy mount: Jesus (ntcast's look) in white light, Moses (Exodus' look) and Elijah (Kings' look:
the hairy mantle) beside him, Peter, James and John kneeling, the bright cloud above (the Father's voice in the Voice box;
God is not drawn); a lamp shining in a dark place and the day-star rising over the hills at dawn; the right way and the
way into the dark; the ark riding the flood, Noah with seven others; Sodom and Gomorrah turned to ashes, the smoke over the
empty plain, righteous Lot going away to the hills; an empty feast-hall at noon, the couches overturned; Balaam (his purple
headcloth) on the grey ass in the narrow way between the vineyard walls, the ass fallen down under him; a spring dried to
cracked mud and the mist driven by the storm; the true proverb as an emblem — a dog and a sow, plainly; the first and the
second epistle, two sealed scrolls; the world that then was overflowed with water; one day as a thousand years on a balance;
the day of the Lord: the heavens on fire and the elements melting, no one drawn; new heavens and a new earth at dawn; Paul's
epistles rolled in their pigeonholes, named; the doxology over the light.

Restraint: 2:1–3 the false teachers and 2:10–19 their ways are words over empty places — a dark road, an empty hall, a dry
spring, a storm — no one drawn in them; 2:4 the angels cast down to hell are words only, beside Peter's stern face; 2:6–8
Sodom's overthrow is smoke over the empty plain, nothing of the cities' sin drawn; 2:14 words only; 2:22 the proverb's dog
and sow are drawn plainly as an emblem, nothing foul; 3:10–12 the burning of the earth is fire and light over an empty
world, no one in it. God is never drawn (the Voice box over the cloud and the light).

Plan (1,541 words, one chapter): 1 Until the Day Dawn (1–3)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("2PE")

META = {
  "id": "2peter", "order": 61, "name": "2 Peter", "kanji": "ペテロの第二の手紙", "thumb": "vol-2peter-", "book": "2PE",
  "title": "2 Peter Volume", "volume": "Volume Sixty-One",
  "lede": "The sixty-first book of the Bible, in full: Peter's second letter, written near his death — partakers of the divine nature, in your faith supply virtue, the putting off of my tabernacle cometh swiftly, eyewitnesses of his majesty on the holy mount, a lamp shining in a dark place until the day-star arise, false teachers, Noah, Sodom and righteous Lot, Balaam and the dumb ass, where is the promise of his coming?, one day as a thousand years, the day of the Lord as a thief, new heavens and a new earth, our beloved brother Paul, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Until the Day Dawn", "range": "2 Peter 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "Simon Peter, to them that have obtained a like precious faith: partakers of the divine nature; in your faith supply virtue, and in your virtue knowledge, … and in your brotherly kindness love; the putting off of my tabernacle cometh swiftly; we were eyewitnesses of his majesty, This is my beloved Son, in the holy mount; a lamp shining in a dark place, until the day dawn; false teachers; God spared not the ancient world, but preserved Noah; Sodom and Gomorrah turned into ashes, righteous Lot delivered; the way of Balaam, a dumb ass spake; mockers: where is the promise of his coming?; one day is with the Lord as a thousand years; the day of the Lord will come as a thief; new heavens and a new earth; our beloved brother Paul; grow in grace."},
  ],
}
