"""The Titus volume of the full edition (the Epistle of Paul to Titus): metadata, the volume cover, and the chapter plan
(ch01.py).

Built on the letters' shared kit, tools/full/epistle.py (EpistleKit with fit_faces and clip), as 1 and 2 Timothy are, with
their cast (ti1.common) and drawings (ti1.art, ti1.art2, ti2.art). Every word of the ASV here is Paul writing to Titus
(letter boxes); the line of the Cretans' own prophet, "Cretans are always liars, evil beasts, idle gluttons" (1:12), is a
quotation and goes in a song box. The faithful saying of 3:8 points back to 3:4–7 and stays a letter box.

The reader stands where Titus stands in Crete: Paul, free and on the road, writes in a plain house by lamplight (the same
room as 1 Timothy's opening; he means to winter at Nicopolis, 3:12); the letter's road runs from Macedonia down through
Achaia and over the sea to Crete (where it was written from is not said: Macedonia is this volume's judgment, as 1 Timothy
1:3 has Paul there in these years); Titus receives the sealed roll at his door in a city of Crete, the window on the sea and
the mountains; he is drawn again teaching the younger men as an ensample (2:6–8), seeing Zenas and Apollos off at the
harbour (3:13), and reading the letter by his lamp at the end. Paul's faces: stern red at the vain talkers (1:10–11), white
with joy at the blessed hope (2:13–15), grieving blue at "we also once were foolish" (3:3), earnest gold at the faithful
saying (3:8–11).

Drawings (tit.art): Crete on Acts' map and the island's outline with its cities (Cnossus, Gortyna, Lasea, Phœnix, Kydonia,
Eleutherna, Lyttos, Hierapytna — named as plate labels), an elder at each (1:5–6); the bishop as God's steward with his
keys, a plate of his qualities (1:7–9); a haven of Crete (Acts' harbour) under the prophet's line (1:12–14); the basin of
clean water (2 Corinthians, 1:15); the household plates of Titus 2 on cream paper — aged men and aged women, the young
women trained by the aged, servants and their own masters; Titus teaching three younger men in a courtyard over the sea;
the grace of God appeared as dawn over the sea of Crete (2:11–12); the magistrate on his seat (Romans, 3:1); the washing
of regeneration as dawn over still water with the light poured on it (1 Corinthians, 3:4–7); the road from Crete to
Nicopolis (3:12); Zenas the lawyer with his rolls and Apollos (as Acts draws him) going down to the ship, Titus with bread
and water for the way (3:13).

Titus's cast: Titus a Greek, bareheaded, short black hair, clean-shaven, a sand tunic with a blue mantle (co2.common.TITUS,
ti1.art.titus_fig_); the elders of Crete in cool and off-white headcloths; Zenas an off-white headcloth, a grey beard, a
dark-blue robe; Apollos as Acts draws him; the women of Titus 2 in cool, dark or off-white veils.

Restraint: "evil beasts" (1:12) is words over the harbour, no beast drawn; the young women "in subjection to their own
husbands" and the servants are plain standing figures on the plates, nothing more; "we also once were foolish … hateful,
hating one another" (3:3) words beside Paul's face; God is never drawn — "the kindness of God our Saviour, and his love
toward man, appeared" is dawn light over the water; "the appearing of the glory of the great God and our Saviour Jesus
Christ" (2:13) words beside Paul's face in white light.

Plan (899 words, one chapter): 1 The Grace of God Hath Appeared (1–3)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("TIT")

META = {
  "id": "titus", "order": 56, "name": "Titus", "kanji": "テトスへの手紙", "thumb": "vol-titus-", "book": "TIT",
  "title": "Titus Volume", "volume": "Volume Fifty-Six",
  "lede": "The fifty-sixth book of the Bible, in full: Paul's letter to Titus, his true child after a common faith, left in Crete — appoint elders in every city; the bishop as God's steward; Cretans are always liars, said a prophet of their own; to the pure all things are pure; aged men and aged women, young women and younger men, servants; the grace of God hath appeared, bringing salvation to all men; looking for the blessed hope; the washing of regeneration and renewing of the Holy Spirit; come unto me to Nicopolis; set forward Zenas the lawyer and Apollos, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Grace of God Hath Appeared", "range": "Titus 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "Paul, a servant of God, to Titus, my true child after a common faith; for this cause left I thee in Crete, to appoint elders in every city; the bishop must be blameless, as God's steward; many unruly men, vain talkers and deceivers; Cretans are always liars, evil beasts, idle gluttons; to the pure all things are pure; aged men, aged women, the young women, the younger men; in all things showing thyself an ensample of good works; servants showing all good fidelity; the grace of God hath appeared, bringing salvation to all men; looking for the blessed hope; subject to rulers; the washing of regeneration and renewing of the Holy Spirit; come unto me to Nicopolis, for there I have determined to winter; set forward Zenas the lawyer and Apollos; grace be with you all."},
  ],
}
