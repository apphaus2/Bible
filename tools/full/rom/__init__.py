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

More restraint: 5:6–8 the three crosses far off against the darkened sky (Matthew's drawing, ntcast's rule); 6:3–6 baptism
in the river and the sealed tomb; 7:7–25 a man between the lamp and his own long shadow, no torment drawn; 8:36 "sheep for
the slaughter" words over the empty sheepfold at dusk; 9:29 the smoke over the empty plain of Sodom; 11:9–10 the table in
the dark; 12:1 a man before the altar presenting himself, no beast slain; 12:20 bread, water and a pan of coals, no one
struck; 13:13 the revelling and wantonness in words over the dawn window; 16:20 words only, no serpent, Satan not drawn.
God's words to Abraham, Rebecca and Moses, by Hosea and Isaiah, and the commandments (7:7, 13:9) are in the Voice box; the
cherubim of the mercy-seat (3:25) have no faces. Romans 16:24 has no text in the ASV and is listed as omitted.

Plan (9,471 words, five chapters, re-split for length): 1 The Power of God unto Salvation (1–3) · 2 Justified by Faith
(4–7) · 3 No Condemnation (8, the high point, given room) · 4 The Depth of the Riches (9–11) · 5 A Living Sacrifice
(12–16, with the greetings roll)."""
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
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Justified by Faith", "range": "Romans 4–7", "bible_chapters": [4, 5, 6, 7],
     "blurb": "Abraham believed God, and it was reckoned unto him for righteousness — look toward heaven: so shall thy seed be; who in hope believed against hope; being therefore justified by faith, we have peace with God; while we were yet sinners, Christ died for us; through one man sin entered into the world, and where sin abounded, grace did abound more exceedingly; buried with him through baptism, to walk in newness of life; the wages of sin is death; Thou shalt not covet; wretched man that I am! who shall deliver me out of the body of this death? I thank God through Jesus Christ our Lord."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "No Condemnation", "range": "Romans 8", "bible_chapters": [8],
     "blurb": "There is therefore now no condemnation to them that are in Christ Jesus; the mind of the Spirit is life and peace; ye received the spirit of adoption, whereby we cry, Abba, Father; the whole creation groaneth and travaileth in pain together until now; the Spirit himself maketh intercession for us with groanings which cannot be uttered; to them that love God all things work together for good; if God is for us, who is against us?; who shall separate us from the love of Christ?; neither height, nor depth, nor any other creature."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "The Depth of the Riches", "range": "Romans 9–11", "bible_chapters": [9, 10, 11],
     "blurb": "Great sorrow and unceasing pain for my brethren; in Isaac shall thy seed be called; I will have mercy on whom I have mercy; hath not the potter a right over the clay?; a stone of stumbling laid in Zion; the word is nigh thee, in thy mouth, and in thy heart; how beautiful are the feet of them that bring glad tidings of good things!; Elijah and the seven thousand who have not bowed the knee to Baal; the olive tree, its broken branches and the wild olive grafted in; and so all Israel shall be saved; O the depth of the riches both of the wisdom and the knowledge of God!"},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "A Living Sacrifice", "range": "Romans 12–16", "bible_chapters": [12, 13, 14, 15, 16],
     "blurb": "Present your bodies a living sacrifice, and be ye transformed by the renewing of your mind; many members in one body; heap coals of fire upon his head; the powers that be are ordained of God; love is the fulfilment of the law; the night is far spent, put on the armor of light; the weak and the strong, herbs and meat; every knee shall bow; the root of Jesse; from Jerusalem round about unto Illyricum, and on by Rome unto Spain; Phoebe commended, and the greetings — Prisca and Aquila, Epænetus, Mary, Andronicus and Junias and all the saints; I Tertius, who write the epistle; to the only wise God, through Jesus Christ, to whom be the glory for ever. Amen."},
  ],
}
