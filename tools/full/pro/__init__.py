"""The Proverbs volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

The package is pro (Proverbs). Chapters 1–9 are the father's discourses and Wisdom crying in the streets: speech panels
(the father is Solomon, kg2.common's faces; the son a beardless youth in a pale-blue headcloth; Wisdom a woman in white with
a gold band, in gold light, never a goddess) and song boxes over drawn scenes, laid out by discourse.pack. Chapters 10–29,
the short proverbs, are saying cells (pro.common.sayings): one verse or a small group to a cell, each under an emblem
(pro.emblems, picked from the saying's own words by pro.common.pick, or named). Agur (30) and Lemuel and the worthy woman
(31) are drawn scenes and cells. Restraint: the sinners' ambush (1:10–19) is dark figures by the road and the net, no one
harmed; the strange woman (2, 5, 6, 7) is never drawn near — a far veiled figure at dusk, a shut door, an empty street, the
stair going down into the dark; 6:17 and 7:22–23 words over the ox and the bird; God is never drawn (his ways are rays of
light over the earth).

Plan (15,124 words, eleven chapters): 1 The Beginning of Knowledge (1–3) · 2 Get Wisdom (4–6) · 3 Wisdom Hath Builded Her
House (7–9) · 4 A Wise Son (10–12) · 5 A Tree of Life (13–15) · 6 The Lot Is Cast into the Lap (16–18) · 7 The King's Heart
(19–21) · 8 The Words of the Wise (22–24) · 9 Apples of Gold (25–27) · 10 Bold as a Lion (28–29) · 11 A Worthy Woman (30–31)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("PRO")

META = {
  "id": "proverbs", "order": 20, "name": "Proverbs", "kanji": "箴言", "thumb": "vol-proverbs-", "book": "PRO",
  "title": "Proverbs Volume", "volume": "Volume Twenty",
  "lede": "The twentieth book of the Bible, in full: a father's instruction to his son, Wisdom crying aloud at the gates and building her house of seven pillars, the proverbs of Solomon one by one, the words of the wise, the sayings copied out by the men of Hezekiah, the words of Agur and of king Lemuel, and the worthy woman, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Beginning of Knowledge", "range": "Proverbs 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "The proverbs of Solomon the son of David — the fear of Jehovah is the beginning of knowledge; my son, if sinners entice thee, consent thou not; Wisdom crieth aloud in the street: how long, ye simple ones?; if thou seek her as silver; trust in Jehovah with all thy heart; she is a tree of life to them that lay hold upon her."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Get Wisdom", "range": "Proverbs 4–6", "bible_chapters": [4, 5, 6],
     "blurb": "Hear, my sons, the instruction of a father — for I was a son unto my father; wisdom is the principal thing, therefore get wisdom; the path of the righteous is as the dawning light; keep thy heart with all diligence; drink waters out of thine own cistern; go to the ant, thou sluggard; six things which Jehovah hateth, yea, seven; for the commandment is a lamp, and the law is light."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "Wisdom Hath Builded Her House", "range": "Proverbs 7–9", "bible_chapters": [7, 8, 9],
     "blurb": "Say unto wisdom, Thou art my sister; at the window of my house I looked forth, and beheld a young man void of understanding in the twilight; doth not wisdom cry? — by me kings reign; Jehovah possessed me in the beginning of his way, when he set a circle upon the face of the deep; Wisdom hath builded her house, she hath hewn out her seven pillars; stolen waters are sweet."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "A Wise Son", "range": "Proverbs 10–12", "bible_chapters": [10, 11, 12],
     "blurb": "The proverbs of Solomon, one by one: a wise son maketh a glad father; the hand of the diligent maketh rich; the mouth of the righteous is a fountain of life; hatred stirreth up strifes, but love covereth all transgressions; a false balance is an abomination to Jehovah; as a ring of gold in a swine's snout; a worthy woman is the crown of her husband."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "A Tree of Life", "range": "Proverbs 13–15", "bible_chapters": [13, 14, 15],
     "blurb": "Hope deferred maketh the heart sick, but when the desire cometh, it is a tree of life; the law of the wise is a fountain of life; every wise woman buildeth her house; where no oxen are, the crib is clean; a soft answer turneth away wrath; the eyes of Jehovah are in every place; better is a dinner of herbs, where love is."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "The Lot Is Cast into the Lap", "range": "Proverbs 16–18", "bible_chapters": [16, 17, 18],
     "blurb": "Commit thy works unto Jehovah; a just balance and scales are Jehovah's; pride goeth before destruction, and a haughty spirit before a fall; pleasant words are as a honeycomb; the lot is cast into the lap, but the whole disposing thereof is of Jehovah; better is a dry morsel, and quietness therewith; the name of Jehovah is a strong tower."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "The King's Heart", "range": "Proverbs 19–21", "bible_chapters": [19, 20, 21],
     "blurb": "Better is the poor that walketh in his integrity; the king's wrath is as the roaring of a lion; the contentions of a wife are a continual dropping; wine is a mocker, strong drink a brawler; diverse weights are an abomination to Jehovah; the spirit of man is the lamp of Jehovah; the king's heart is in the hand of Jehovah as the watercourses; the horse is prepared against the day of battle, but victory is of Jehovah."},
  ],
}
