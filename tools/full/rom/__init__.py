"""The Romans volume of the full edition (the Epistle of Paul to the Romans): metadata, the volume cover, and the chapter
plans (ch01.py, ...).

The first of the letters, so it carries their shared kit, tools/full/epistle.py (EpistleKit on Mark's MarkKit and the minor
prophets' Kit; the letter box, the opening scene, the sealed scroll, the doxology panel, the greetings roll). A letter has
no narration: every word of the ASV here is Paul writing to the saints at Rome (letter boxes: parchment, a sepia rule down
the left edge, a short tail toward Paul where his face is drawn); the scriptures he quotes are song boxes; God's own words
quoted in the first person (9:15, 9:25–26, 10:20–21, 11:4, 11:26–27, 12:19, 14:11 …) are the Voice box. God is never drawn —
light, storm, an empty throne, the Voice box. Satan is never drawn: 16:20 is words only, and no serpent is drawn there.
Angels (8:38) are only words.

Drawings (rom.art, on top of all of Acts' drawings by way of act.art16): the letter written at Corinth by lamplight, Paul
dictating and Tertius writing (16:22), the scroll sealed and given to Phoebe (16:1–2), and its road to Rome on Acts' map;
then the argument made visible, as a manga artist would: creation's everlasting power in sky, sea and stars (1:20); idols
of man, bird, beast and creeping thing on their plinths (1:23); the empty judgment seat (2:1–3); the two roads (2:6–10); the
tablets of stone and the law written in the heart as a technical plate (2:14–15); the teacher of the law with the lamp
(2:17–20); the outward and the inward (2:28–29); the oracles of God in the ark of the scrolls (3:1–2); the scales and the
mark of the glory of God (3:23); the mercy-seat and the light between the cherubim (3:25).

Romans' own cast (rom.common faces, rom.art figures), each the same everywhere: Paul's face only ever ntcast's (PAUL) and his
figure epistle.paul_fig (ntcast's colours on the kit silhouette), his face in five lights (epistle: earnest gold, lamplight, grieving blue, joyful white, stern red);
Tertius, a young beardless scribe in a dark-teal headcloth with a reed pen; Phoebe, a deep-blue veil and a grey travelling
cloak. A warm scarf would read as long hair: both headcloths are cool and dark.

Restraint: 1:24–32 (the lusts, the vile passions and the list of vices) are words over a darkened, empty idol-temple court
and its shut doors — nothing sexual or violent is drawn, and no person is in those panels; 3:13–18 (an open sepulchre, the
poison of asps, feet swift to shed blood) words over an open, empty sepulchre and a dark road, no asp drawn; the wrath of
God (1:18) a storm over the land, nothing struck; death is told in words over empty places.

Plan (9,471 words, four chapters): 1 The Power of God unto Salvation (1–3) · 2 Justified by Faith (4–7) · 3 No Condemnation
(8–11) · 4 A Living Sacrifice (12–16)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("ROM")

META = {
  "id": "romans", "order": 45, "name": "Romans", "kanji": "ローマ人への手紙", "thumb": "vol-romans-", "book": "ROM",
  "title": "Romans Volume", "volume": "Volume Forty-Five",
  "lede": "The forty-fifth book of the Bible, in full: Paul's letter to the saints at Rome, written at Corinth and carried by Phoebe — the gospel the power of God unto salvation, all under sin and justified freely by his grace, Abraham's faith reckoned for righteousness, the free gift in Christ, no condemnation and nothing able to separate us from the love of God, Israel and the olive tree, a living sacrifice, and the greetings, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Power of God unto Salvation", "range": "Romans 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "Paul, a servant of Jesus Christ, to all that are in Rome — the letter written at Corinth by lamplight and given to Phoebe; I long to see you; I am not ashamed of the gospel: for it is the power of God unto salvation; the invisible things of him clearly seen; they changed the glory of the incorruptible God for an image; thou art without excuse, O man, whosoever thou art that judgest; the law written in their hearts; there is none righteous, no, not one; for all have sinned, and fall short of the glory of God; being justified freely by his grace."},
  ],
}
