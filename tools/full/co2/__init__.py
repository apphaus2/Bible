"""The 2 Corinthians volume of the full edition (the Second Epistle of Paul to the Corinthians): metadata, the volume
cover, and the chapter plans (ch01.py, ...).

Built on the epistle kit, tools/full/epistle.py, as Romans is (EpistleKit; the letter box, the study, the sealed scroll,
the doxology panel). A letter has no narration: every word of the ASV here is Paul (with Timothy, 1:1) writing to the
church of God at Corinth (letter boxes beside Paul's face or over the drawings); the scriptures he quotes are song boxes
(4:13 "I believed, and therefore did I speak", 8:15 the manna, 9:9 the psalm, 13:1 two witnesses or three); God's own words
quoted in the first person are the Voice box (4:6 "Light shall shine out of darkness", 6:2 "At an acceptable time I
hearkened unto thee", 6:16–18 "I will dwell in them …"). The Lord's answer in 12:9 ("My grace is sufficient for thee") is
Christ speaking from heaven: as in Acts on the Damascus road, his words are an ordinary speech box over the light, and he
is not drawn there. God is never drawn — light, the Voice box, an empty judgment-seat.

The letter's setting: written in Macedonia (7:5, 8:1, 9:2–4) after Titus came with news from Corinth (7:6–7), and carried
by Titus and the brethren (8:16–23). The opening is the study in Macedonia — Paul dictating, Timothy writing (1:1) — and
the letter's road from Philippi to Corinth; Titus comes to the door in chapter 7 and is handed the sealed letter at the end.

Drawings (co2.art, on top of all of Acts' drawings and the epistle kit): the road through Asia lined with tombs (1:8–10);
the journey purposed (1:15–16) on the map; the seal and the earnest as a plate (1:22); the open door at Troas (2:12–13); a
triumph and the savour of incense (2:14–16); the epistle written not on tables of stone but on hearts of flesh (3:1–3,
a plate); Moses' face shining and veiled (3:7–15; Exodus' Moses, off-white headcloth, black beard); the mirror and the
veil laid aside (3:18); light out of darkness (4:6); the treasure in earthen vessels, a clay jar glowing from within (4:7),
and the same jar in the four cells of 4:8–9; the things seen and not seen (4:18); the earthly tent struck and the house not
made with hands (5:1); the judgment-seat of Christ empty in the light (5:10); a new creature at dawn (5:17); the
ambassador's seal and scroll (5:20). Then 6–9: the day of salvation; the hardships of 6:4–10 over empty places; the
unequal yoke (an ox and an ass, 6:14); the temple of the living God (6:16); Titus' coming (7:6); the churches of
Macedonia giving (8:1–5); the manna and the omer (8:15); Titus and the brethren on the road with the bounty (8:16–23); the
sower (9:6); the cheerful giver at the chest (9:7); the gift carried to Jerusalem (9:12–14). And 10–13: the strongholds
cast down (10:4–5, a plate); the measure of the province (10:13–16, a map); the betrothal as an emblem (11:2); Paul's
sufferings over empty places (11:23–27); the basket at Damascus (11:33, Acts' drawing); caught up to the third heaven, a
rising light (12:2–4); the thorn as an emblem (12:7); the light from heaven (12:9); the benediction (13:14).

2 Corinthians' cast, each the same everywhere: Paul's face only ever the kit's (PAUL and its moods), his figure
epistle.paul_fig; Timothy as Acts draws him (young, beardless, bareheaded, light-brown hair, a grey-blue tunic); Titus, a
Greek (Gal 2:3): bareheaded, short black hair, clean-shaven, a sand tunic and a blue mantle; Moses as Exodus draws him. No
warm headcloths (a warm scarf reads as long hair).

Restraint: Satan is never drawn and no serpent is drawn — 2:11, 4:4 ("the god of this world"), 6:15 (Belial), 11:3 (the
serpent that beguiled Eve), 11:14–15 (fashioned into an angel of light) and 12:7 (a messenger of Satan) are words only, over
a dark city, a shut door, Paul's face or the thorn branch. Angels (11:14) are only words. Paul's sufferings (1:8–10,
4:8–12, 6:4–10, 11:23–27) are words over empty places — the road and its tombs, a shut prison door, the rods laid down, a
heap of stones outside a gate, a broken ship on an empty sea with no one in the water, the river, the robbers' pass, the
city, the wilderness, a cold camp at night — with no wounds and no beatings drawn; 1:9 the sentence of death is words over
the empty road; 4:8–9 is told by the clay jar alone. 11:2 the betrothal is two rings and a lamp, no bride drawn. 12:20–21
(strife … uncleanness and fornication and lasciviousness) are words over an empty street of shut doors at night. The
crucifixion (13:4) is words only, over Paul's face.

Plan (6,169 words, three chapters): 1 Treasure in Earthen Vessels (1–5) · 2 God Loveth a Cheerful Giver (6–9) · 3 My Grace
Is Sufficient for Thee (10–13)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("2CO")

META = {
  "id": "2corinthians", "order": 47, "name": "2 Corinthians", "kanji": "コリント人への第二の手紙", "thumb": "vol-2corinthians-", "book": "2CO",
  "title": "2 Corinthians Volume", "volume": "Volume Forty-Seven",
  "lede": "The forty-seventh book of the Bible, in full: Paul's second letter to the church of God at Corinth, written in Macedonia after Titus came and carried by Titus and the brethren — the God of all comfort, the epistle written in hearts of flesh, the veil taken away, treasure in earthen vessels, a house not made with hands, a new creature and the ministry of reconciliation, the collection for the saints and the cheerful giver, strongholds cast down, Paul's sufferings and his weakness, the third heaven and the thorn in the flesh, and my grace is sufficient for thee, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Treasure in Earthen Vessels", "range": "2 Corinthians 1–5", "bible_chapters": [1, 2, 3, 4, 5],
     "blurb": "Paul and Timothy to the church of God at Corinth — the letter written in Macedonia; blessed be the God of all comfort; the sentence of death on the road through Asia; sealed, and the earnest of the Spirit; I wrote unto you with many tears; a door opened at Troas; led in triumph, a sweet savor of Christ; ye are our epistle, written in tables that are hearts of flesh; the glory of Moses' face and the veil taken away; light shall shine out of darkness; we have this treasure in earthen vessels; pressed, perplexed, pursued, smitten down; a house not made with hands, eternal, in the heavens; if any man is in Christ, he is a new creature; we are ambassadors on behalf of Christ."},
  ],
}
