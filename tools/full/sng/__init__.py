"""The Song of Solomon volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

The whole book is song lines (sng.common: sg/sgs) between three voices: the bride (dark and comely, a keeper of vineyards; a
crimson headscarf with a gold band, a crimson robe at a distance), the beloved (a shepherd-king: black locks, a gold band, a
white tunic and a staff at a distance, crowned in 3:11), and the daughters of Jerusalem (blue and teal headscarves). Their
faces stand beside the lines they sing; the other lines sit over drawings (sng/art.py). Restraint: the figures are always
clothed, at a distance or in profile faces; every likeness of the body (4:1–5, 5:10–16, 6:5–7, 7:1–9) is drawn only as the
thing it is likened to — doves, flocks on Gilead, the tower of David, lilies, pools, palms, gold and ivory — in plates of
cells; 5:7 is words over the walls at night and a mantle on the street. God is never drawn ("a very flame of Jehovah" is a
flame over the waters).

Plan (2,677 words, three chapters): 1 I Am a Rose of Sharon (1–2) · 2 A Garden Shut Up (3–5) · 3 Love Is Strong as Death
(6–8)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("SNG")

META = {
  "id": "songofsolomon", "order": 22, "name": "Song of Solomon", "kanji": "雅歌", "thumb": "vol-songofsolomon-", "book": "SNG",
  "title": "Song of Solomon Volume", "volume": "Volume Twenty-Two",
  "lede": "The twenty-second book of the Bible, in full: the Song of songs, which is Solomon's — the bride in the vineyards, the beloved like a roe upon the mountains, the winter past and the voice of the turtle-dove, a garden shut up, and love strong as death — every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "I Am a Rose of Sharon", "range": "Song of Solomon 1–2", "bible_chapters": [1, 2],
     "blurb": "The Song of songs, which is Solomon's: I am black, but comely, as the tents of Kedar; tell me, O thou whom my soul loveth, where thou feedest thy flock; I am a rose of Sharon, a lily of the valleys; his banner over me was love; the voice of my beloved, leaping upon the mountains — rise up, my love, my fair one, and come away, for, lo, the winter is past; the little foxes; my beloved is mine, and I am his."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "A Garden Shut Up", "range": "Song of Solomon 3–5", "bible_chapters": [3, 4, 5],
     "blurb": "By night on my bed I sought him whom my soul loveth; who is this that cometh up from the wilderness like pillars of smoke? — the litter of Solomon and the crown of his espousals; behold, thou art fair, my love; come with me from Lebanon; a garden shut up, a spring shut up, a fountain sealed; awake, O north wind; I was asleep, but my heart waked; and my beloved is white and ruddy, the chiefest among ten thousand."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "Love Is Strong as Death", "range": "Song of Solomon 6–8", "bible_chapters": [6, 7, 8],
     "blurb": "Whither is thy beloved gone? — to his garden, to gather lilies; fair as Tirzah, terrible as an army with banners; who is she that looketh forth as the morning?; return, return, O Shulammite; let us get up early to the vineyards; who is this that cometh up from the wilderness, leaning upon her beloved?; set me as a seal upon thy heart, for love is strong as death, and many waters cannot quench love; make haste, my beloved, upon the mountains of spices."},
  ],
}
