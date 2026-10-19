"""The Ezekiel volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Most of the book is Jehovah's words to Ezekiel, set in the Voice box beside Ezekiel's face or over a drawing (ezk.common.run()
splits each verse automatically: "And the word of Jehovah came unto me, saying," in a caption, "Son of man, ..." in the Voice
box). Ezekiel's own narration is in captions; Ezekiel: a priest among the captives, grey-black beard, white headcloth with a
blue cord (ezk.common.EZEKIEL...). The vision by the river Chebar: the four living creatures (bronze figures in fire, four
wings), the wheels full of eyes, the firmament like crystal, the throne of sapphire and above it only fire and amber light,
never a figure (ezk.art.throne). God is never drawn, not even a hand (2:9 is the roll alone in the light). Restraint: the
slaughter of chapter 9 is words over the empty court; Oholah and Oholibah (16, 23) words only over the cities; the death of
Ezekiel's wife (24:16–18) words over the empty house; the sword and the slain words over walls, smoke and empty streets;
the birds' feast of 39 words over the empty field. The nations are maps (Tyre as the ship of 27); the new temple of 40–48 is
blueprint plates (exo.art8 bp/dim/tag); the division of the land is a map of the tribes' portions.

Plan (39,297 words, eighteen chapters): 1 The Visions of God (1–3) · 2 The Siege on a Tile (4–7) · 3 The Glory Departs
(8–11) · 4 Stuff for Removing (12–14) · 5 The Vine and the Foundling (15–16) · 6 The Eagles and the Cedar (17–19) ·
7 A Sword, a Sword (20–21) · 8 Oholah and Oholibah (22–23) · 9 The Desire of Thine Eyes (24–25) · 10 The Ship of Tyre
(26–28) · 11 Pharaoh King of Egypt (29–32) · 12 The Watchman and the Shepherds (33–34) · 13 The Valley of Dry Bones
(35–37) · 14 Gog (38–39) · 15 The Measuring Reed (40–42) · 16 The Glory Returns (43–44) · 17 The Holy Oblation (45–46) ·
18 Jehovah Is There (47–48)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("EZK")

META = {
  "id": "ezekiel", "order": 26, "name": "Ezekiel", "kanji": "エゼキエル書", "thumb": "vol-ezekiel-", "book": "EZK",
  "title": "Ezekiel Volume", "volume": "Volume Twenty-Six",
  "lede": "The twenty-sixth book of the Bible, in full: the visions of God by the river Chebar, the watchman of the house of Israel, the glory departing from the temple, the parables and the burdens of the nations, the valley of dry bones, and the house of the vision with the river flowing from under its threshold, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Visions of God", "range": "Ezekiel 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "Among the captives by the river Chebar the heavens were opened: a stormy wind out of the north, the four living creatures, the wheels with their rims full of eyes, the firmament like the terrible crystal, and above it a throne of sapphire, fire and brightness — the appearance of the likeness of the glory of Jehovah; the roll of a book eaten, in the mouth as honey; and I have made thee a watchman unto the house of Israel."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Siege on a Tile", "range": "Ezekiel 4–7", "bible_chapters": [4, 5, 6, 7],
     "blurb": "Take thee a tile, and portray upon it a city, even Jerusalem: the forts and the mound and the iron pan; the prophet lying on his left side and on his right, each day for a year; the bread of the siege by weight; the hair shaven with a sword and divided in three; set thy face toward the mountains of Israel; and an end, the end is come upon the four corners of the land."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "The Glory Departs", "range": "Ezekiel 8–11", "bible_chapters": [8, 9, 10, 11],
     "blurb": "Lifted up between earth and heaven and brought in the visions of God to Jerusalem: the image of jealousy, the chamber of imagery and the seventy elders with their censers, the women weeping for Tammuz, the men worshipping the sun; the man clothed in linen and the mark upon the foreheads; coals of fire from between the cherubim; and the glory of Jehovah going up from the threshold to the east gate, and to the mountain east of the city."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "Stuff for Removing", "range": "Ezekiel 12–14", "bible_chapters": [12, 13, 14],
     "blurb": "The prophet a sign: stuff for removing carried out by day, the wall digged through in the dark — I am your sign; the net spread for the prince in Jerusalem; bread eaten with quaking; the foolish prophets like foxes in the waste places, and the wall daubed with untempered mortar brought down by the stormy wind; and though these three men, Noah, Daniel, and Job, were in it."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "The Vine and the Foundling", "range": "Ezekiel 15–16", "bible_chapters": [15, 16],
     "blurb": "What is the vine-tree more than any tree? — cast into the fire for fuel; then Jerusalem, cast out in the open field in the day that she was born, washed and clothed and decked with ornaments, who trusted in her beauty; her lovers and her judgment; Samaria and Sodom her sisters; and nevertheless I will remember my covenant with thee in the days of thy youth."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "The Eagles and the Cedar", "range": "Ezekiel 17–19", "bible_chapters": [17, 18, 19],
     "blurb": "A riddle of two great eagles, the top of the cedar and the vine of low stature, and its meaning — the king that despised the oath; a tender twig planted upon the mountain of the height of Israel; the fathers have eaten sour grapes — the soul that sinneth, it shall die, and turn yourselves, and live; and a lamentation for the princes of Israel: the lioness and her whelps, and the vine plucked up in fury."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "A Sword, a Sword", "range": "Ezekiel 20–21", "bible_chapters": [20, 21],
     "blurb": "The elders come to inquire, and hear the history of their fathers: Egypt, the wilderness, the sabbaths profaned, and I wrought for my name's sake; I will cause you to pass under the rod; the forest of the South set on fire; then a sword, a sword, sharpened and furbished; the king of Babylon at the parting of the way; remove the mitre, and take off the crown — until he come whose right it is."},
    {"module": "ch08", "dir": "chapter-08", "num": "8", "name": "Oholah and Oholibah", "range": "Ezekiel 22–23", "bible_chapters": [22, 23],
     "blurb": "Wilt thou judge the bloody city? — the house of Israel become dross in the furnace, and I sought for a man that should stand in the gap, but I found none; then two women, the daughters of one mother, Oholah the elder and Oholibah her sister, Samaria and Jerusalem, their lovers and their judgment, and the cup of astonishment and desolation."},
    {"module": "ch09", "dir": "chapter-09", "num": "9", "name": "The Desire of Thine Eyes", "range": "Ezekiel 24–25", "bible_chapters": [24, 25],
     "blurb": "Write thee the name of the day: the king of Babylon drew close unto Jerusalem; the parable of the caldron and its rust; the desire of thine eyes taken away with a stroke — so I spake unto the people in the morning, and at even my wife died — and Ezekiel a sign unto them; then the burdens of Ammon, Moab, Edom and the Philistines."},
    {"module": "ch10", "dir": "chapter-10", "num": "10", "name": "The Ship of Tyre", "range": "Ezekiel 26–28", "bible_chapters": [26, 27, 28],
     "blurb": "Behold, I am against thee, O Tyre: Nebuchadrezzar's horsemen, the walls broken, a bare rock for the spreading of nets; the lamentation over Tyre, the ship perfect in beauty — the cedar mast, the linen sail of Egypt, her traffickers from Tarshish to Sheba — broken by the east wind in the heart of the seas; the prince of Tyre who said, I am a god; thou wast in Eden, the garden of God; and Sidon."},
    {"module": "ch11", "dir": "chapter-11", "num": "11", "name": "Pharaoh King of Egypt", "range": "Ezekiel 29–32", "bible_chapters": [29, 30, 31, 32],
     "blurb": "Behold, I am against thee, Pharaoh king of Egypt, the great monster that lieth in the midst of his rivers: hooks in his jaws, a staff of reed to the house of Israel, Egypt desolate from Migdol to Syene and given to Nebuchadrezzar; the arm of Pharaoh broken; the Assyrian a cedar in Lebanon brought down to Sheol; and the pit, where Asshur is, and Elam, and Meshech and Tubal, round about their graves."},
    {"module": "ch12", "dir": "chapter-12", "num": "12", "name": "The Watchman and the Shepherds", "range": "Ezekiel 33–34", "bible_chapters": [33, 34],
     "blurb": "The watchman that seeth the sword come and bloweth the trumpet — I have set thee a watchman unto the house of Israel; have I any pleasure in the death of the wicked? turn ye, turn ye; one that had escaped out of Jerusalem: The city is smitten; then woe unto the shepherds of Israel that feed themselves — I myself will search for my sheep, and I will set up one shepherd over them, even my servant David, and a covenant of peace."},
    {"module": "ch13", "dir": "chapter-13", "num": "13", "name": "The Valley of Dry Bones", "range": "Ezekiel 35–37", "bible_chapters": [35, 36, 37],
     "blurb": "O mount Seir, a perpetual desolation; ye mountains of Israel, ye shall shoot forth your branches — I will sprinkle clean water upon you, and a new heart also will I give you; then the valley full of bones, very dry: Son of man, can these bones live? — bone to its bone, come from the four winds, O breath, and they stood up upon their feet, an exceeding great army; the two sticks made one; and my sanctuary in the midst of them for evermore."},
  ],
}
