"""The Genesis volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("GEN")

META = {
  "id": "genesis", "order": 1, "name": "Genesis", "kanji": "創世記", "thumb": "vol-genesis-", "book": "GEN",
  "title": "Genesis Volume", "volume": "Volume One",
  "lede": "The first book of the Bible, in full: every scene and every line of dialogue in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "In the Beginning", "range": "Genesis 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "The six days and the seventh, the dust of the ground and the breath of life, the garden eastward in Eden, the woman, the serpent, the fruit, and the way east of Eden."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Cain to the Flood", "range": "Genesis 4–9", "bible_chapters": [4, 5, 6, 7, 8, 9],
     "blurb": "Cain and Abel, the mark of Cain and the city of Enoch, the book of the generations of Adam, Enoch who walked with God, the ark of gopher wood, the flood, the raven and the dove, and the bow in the cloud."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "Babel to Abram's Covenant", "range": "Genesis 10–15", "bible_chapters": [10, 11, 12, 13, 14, 15],
     "blurb": "The table of the nations, Nimrod the mighty hunter, the tower of Babel, the generations of Shem, the call of Abram, Egypt and Pharaoh's house, Lot and the Plain, the war of the kings, Melchizedek, the stars, and the covenant between the pieces."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "The Cities of the Plain", "range": "Genesis 16–19", "bible_chapters": [16, 17, 18, 19],
     "blurb": "Hagar and the fountain in the way to Shur, Ishmael, the covenant and the new names Abraham and Sarah, the three men at Mamre, Sarah's laughter, Abraham pleading for the righteous, the night at Lot's door, and brimstone and fire on the cities of the Plain."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "The Son of Promise", "range": "Genesis 20–23", "bible_chapters": [20, 21, 22, 23],
     "blurb": "Abimelech's dream at Gerar, the birth of Isaac and Sarah's laughter, Hagar and the lad at a bowshot in the wilderness, the oath at Beer-sheba, the mount in the land of Moriah and the ram in the thicket, and the cave of Machpelah."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "A Wife for Isaac", "range": "Genesis 24:1–25:18", "bible_chapters": [24, 25], "span": ["24:1", "25:18"],
     "blurb": "Abraham's servant and the oath, ten camels to the city of Nahor, Rebekah at the well with her pitcher, Laban, I will go, Isaac meditating in the field at eventide, Keturah, Abraham full of years, and Ishmael's twelve princes."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "Jacob and Esau", "range": "Genesis 25:19–27:46", "bible_chapters": [25, 26, 27], "span": ["25:19", "27:46"],
     "blurb": "Two nations in the womb, the hand on Esau's heel, red pottage and the birthright, Isaac at Gerar and the wells Esek, Sitnah and Rehoboth, the blind father, the kids of the goats, the stolen blessing and Esau's bitter cry."},
    {"module": "ch08", "dir": "chapter-08", "num": "8", "name": "The Ladder", "range": "Genesis 28–30", "bible_chapters": [28, 29, 30],
     "blurb": "Jacob sent to Paddan-aram, the stone for a pillow and the ladder to heaven, Beth-el, Rachel at the well, seven years that seemed but a few days, Leah, the eleven sons and Dinah, and the speckled and spotted flock."},
    {"module": "ch09", "dir": "chapter-09", "num": "9", "name": "Peniel", "range": "Genesis 31–33", "bible_chapters": [31, 32, 33],
     "blurb": "The flight from Laban, the stolen teraphim, the pursuit to Gilead, the heap of witness and Mizpah, God's host at Mahanaim, the present for Esau, the night at the ford of the Jabbok, Israel, and the two brothers weeping on each other's neck."},
    {"module": "ch10", "dir": "chapter-10", "num": "10", "name": "Bethel Again", "range": "Genesis 34–36", "bible_chapters": [34, 35, 36],
     "blurb": "Dinah and the city of Shechem, the sword of Simeon and Levi, the foreign gods buried under the oak, Israel at Beth-el, the birth of Benjamin and the death of Rachel, the twelve sons, the death of Isaac, and the generations of Esau in mount Seir."},
    {"module": "ch11", "dir": "chapter-11", "num": "11", "name": "The Dreamer", "range": "Genesis 37–38", "bible_chapters": [37, 38],
     "blurb": "The coat of many colors, the sheaves and the stars, Dothan, the empty pit, twenty pieces of silver, the coat dipped in blood, Jacob refusing to be comforted, and Judah and Tamar at the gate of Enaim."},
  ],
}
