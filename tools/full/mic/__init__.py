"""The Micah volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ch02.py).

Built on the minor prophets' kit (oba/minor.py). Jehovah's words in the Voice box; the prophet's own words (his laments,
his woes, his visions of the latter days) in song lines beside his face or over drawings; narration in captions. Micah
the Morashtite: a grey-black beard and a dark brown headcloth with a cord (mic.common.MICAH), a dark brown robe at a
distance (mic.art.micah_fig). Restraint: the mountains melting are fire and storm, God never drawn; 3:2–3 (the flesh in
the caldron) is words over empty judgment seats and a steaming pot; the towns of the lowland as a technical map.

Plan (3,116 words, two chapters): 1 Swords into Plowshares (1–4) · 2 What Doth Jehovah Require? (5–7)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("MIC")

META = {
  "id": "micah", "order": 33, "name": "Micah", "kanji": "ミカ書", "thumb": "vol-micah-", "book": "MIC",
  "title": "Micah Volume", "volume": "Volume Thirty-Three",
  "lede": "The thirty-third book of the Bible, in full: the word of Jehovah that came to Micah the Morashtite concerning Samaria and Jerusalem — the mountains melted as wax, Zion plowed as a field; then the mountain of Jehovah's house, swords into plowshares, every man under his vine and under his fig-tree; Beth-lehem Ephrathah; what doth Jehovah require of thee; and who is a God like unto thee — every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Swords into Plowshares", "range": "Micah 1–4", "bible_chapters": [1, 2, 3, 4],
     "blurb": "Hear, ye peoples: Jehovah cometh forth out of his place, and the mountains shall be melted under him; Samaria a heap of the field; I will lament and wail — tell it not in Gath; woe to them that devise iniquity upon their beds; the breaker is gone up before them; ye heads of Jacob, Zion shall be plowed as a field; but in the latter days the mountain of Jehovah's house — they shall beat their swords into plowshares, and sit every man under his vine and under his fig-tree."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "What Doth Jehovah Require?", "range": "Micah 5–7", "bible_chapters": [5, 6, 7],
     "blurb": "But thou, Beth-lehem Ephrathah, little among the thousands of Judah, out of thee shall one come forth that is to be ruler in Israel; he shall feed his flock in the strength of Jehovah; Jehovah's controversy before the mountains — O my people, what have I done unto thee?; what doth Jehovah require of thee, but to do justly, and to love kindness, and to walk humbly with thy God?; the wicked balances; woe is me; I will look unto Jehovah; and who is a God like unto thee, that pardoneth iniquity?"},
  ],
}
