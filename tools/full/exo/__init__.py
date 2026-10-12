"""The Exodus volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).
The package is `exo` (not `exodus`) because tools/kit/exodus.py already owns that module name; it builds volumes/exodus/."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("EXO")

META = {
  "id": "exodus", "order": 2, "name": "Exodus", "kanji": "出エジプト記", "thumb": "vol-exodus-", "book": "EXO",
  "title": "Exodus Volume", "volume": "Volume Two",
  "lede": "The second book of the Bible, in full: every scene and every line of dialogue in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Bush That Burned", "range": "Exodus 1–4", "bible_chapters": [1, 2, 3, 4],
     "blurb": "A new king who knew not Joseph, the midwives who feared God, the ark of bulrushes, Moses drawn out of the water, the flight to Midian, the bush that was not consumed, I AM THAT I AM, the rod and the leprous hand, and Aaron sent to meet his brother."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Let My People Go", "range": "Exodus 5–8", "bible_chapters": [5, 6, 7, 8],
     "blurb": "Who is Jehovah?, bricks without straw, the officers beaten, I am Jehovah, the heads of the fathers' houses, Aaron's rod that swallowed up the rods of the magicians, the river turned to blood, the frogs, the lice and the finger of God, and the swarms of flies kept out of Goshen."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "The Passover", "range": "Exodus 9–12", "bible_chapters": [9, 10, 11, 12],
     "blurb": "The murrain, the boils, the hail and fire, the locusts on the east wind, darkness which may be felt, the warning of midnight, the lamb without blemish, the blood on the lintel, the cry in Egypt, unleavened bread, and the hosts of Jehovah going out after four hundred and thirty years."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "The Red Sea", "range": "Exodus 13–15", "bible_chapters": [13, 14, 15],
     "blurb": "The first-born sanctified, the bones of Joseph, the pillar of cloud and the pillar of fire, six hundred chosen chariots, Fear ye not, stand still, the waters a wall on the right hand and on the left, the song of Moses, Miriam's timbrel, the bitter waters of Marah and the palms of Elim."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "Bread from Heaven", "range": "Exodus 16–18", "bible_chapters": [16, 17, 18],
     "blurb": "The flesh-pots of Egypt, quails at even, the manna on the face of the wilderness, an omer a head, the sabbath, water out of the rock at Massah and Meribah, the hands of Moses held up against Amalek, Jehovah-nissi, and Jethro's counsel: rulers of thousands, hundreds, fifties and tens."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "Sinai", "range": "Exodus 19–21", "bible_chapters": [19, 20, 21],
     "blurb": "Eagles' wings, a kingdom of priests, the bounds about the mount, the third day of thunders and the trumpet exceeding loud, the ten words, the people standing afar off, the altar of earth, and the first ordinances: the Hebrew servant, the place of refuge, eye for eye, and the ox that goreth."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "The Book of the Covenant", "range": "Exodus 22–24", "bible_chapters": [22, 23, 24],
     "blurb": "Restitution, the widow and the fatherless, the garment in pledge, justice for the poor and the stranger, the sabbatical year and the three feasts, the angel sent before them and the hornet, the twelve pillars, the blood of the covenant, the paved work of sapphire, and Moses forty days in the cloud."},
    {"module": "ch08", "dir": "chapter-08", "num": "8", "name": "The Pattern of the Tabernacle", "range": "Exodus 25–27", "bible_chapters": [25, 26, 27],
     "blurb": "The willing offering, the ark and the mercy-seat with its two cherubim of gold, the table of showbread, the candlestick of beaten work, the curtains and their loops and clasps, the boards and sockets, the veil, the altar of brass, and the court of a hundred cubits — drawn as blueprints."},
    {"module": "ch09", "dir": "chapter-09", "num": "9", "name": "Holy to Jehovah", "range": "Exodus 28–31", "bible_chapters": [28, 29, 30, 31],
     "blurb": "The holy garments of Aaron: the ephod and its onyx stones, the breastplate of twelve stones, the robe of blue with bells and pomegranates, the golden plate HOLY TO JEHOVAH; the seven days of consecration, the altar of incense, the half shekel, the laver, the anointing oil, Bezalel and Oholiab, the sabbath, and the tables of stone."},
  ],
}
