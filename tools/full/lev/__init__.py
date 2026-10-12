"""The Leviticus volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).
Almost all of Leviticus is law: it is set in Voice-box law cells (exo.kit.law_pages) with pictograms from lev/art.py, and
the narrative stretches (the consecration, Nadab and Abihu, the Day of Atonement, the blasphemer) as story pages."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("LEV")

META = {
  "id": "leviticus", "order": 3, "name": "Leviticus", "kanji": "レビ記", "thumb": "vol-leviticus-", "book": "LEV",
  "title": "Leviticus Volume", "volume": "Volume Three",
  "lede": "The third book of the Bible, in full: every law and every scene in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Offerings", "range": "Leviticus 1–5", "bible_chapters": [1, 2, 3, 4, 5],
     "blurb": "Jehovah calls to Moses out of the tent of meeting: the burnt-offering of the herd, the flock and the birds, the meal-offering seasoned with salt, the peace-offerings, the sin-offering for the priest, the congregation, the ruler and the common people, and the trespass-offering with its fifth part."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Consecration", "range": "Leviticus 6–8", "bible_chapters": [6, 7, 8],
     "blurb": "The law of each offering — the fire on the altar that shall never go out, the portions of the priests, the sacrifice of thanksgiving, no fat and no blood, the wave-breast and the heave-thigh — and the seven days in which Moses washed, clothed and anointed Aaron and his sons."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "Strange Fire", "range": "Leviticus 9–11", "bible_chapters": [9, 10, 11],
     "blurb": "The eighth day, Aaron's first offerings and the fire that came forth from before Jehovah; the strange fire of Nadab and Abihu, and Aaron holding his peace; no wine in the tent of meeting; and the beasts, the fish, the birds and the creeping things, clean and unclean."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "The Plague of Leprosy", "range": "Leviticus 12–13", "bible_chapters": [12, 13],
     "blurb": "The days of purifying after a birth, and the priest looking on the plague: the rising, the scab and the bright spot, the hair turned white, the raw flesh, the boil, the burning, the scall, the leper crying Unclean, unclean, without the camp, and the plague in a garment."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "The Cleansing", "range": "Leviticus 14–15", "bible_chapters": [14, 15],
     "blurb": "The law of the leper in the day of his cleansing: two living birds, cedar, scarlet and hyssop, the bird let go into the open field, the eighth day and the log of oil; the plague in the walls of a house; and the laws of issues, that they die not in their uncleanness."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "The Day of Atonement", "range": "Leviticus 16–18", "bible_chapters": [16, 17, 18],
     "blurb": "Aaron in the holy linen garments, the two goats and the lots, the cloud of incense over the mercy-seat, the live goat bearing all their iniquities into a solitary land, the tenth day of the seventh month; the life of the flesh is in the blood; and the doings of Egypt and of Canaan ye shall not do."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "Holy unto Jehovah", "range": "Leviticus 19–22", "bible_chapters": [19, 20, 21, 22],
     "blurb": "Ye shall be holy: the corners of the field for the poor, the deaf and the blind, thou shalt love thy neighbor as thyself, the stranger as the home-born, just balances; the penalties for Molech and the forbidden degrees; the holiness of the priests and of the holy things, and offerings without blemish."},
    {"module": "ch08", "dir": "chapter-08", "num": "8", "name": "The Set Feasts", "range": "Leviticus 23–25", "bible_chapters": [23, 24, 25],
     "blurb": "The sabbath and the set feasts — passover and unleavened bread, the sheaf and the fifty days, the trumpets, the day of atonement, the booths; the lamp and the twelve cakes; the son of the Israelitish woman who blasphemed the Name; the sabbath of the land and the jubilee: proclaim liberty throughout the land."},
  ],
}
