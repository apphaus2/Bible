"""The 2 Thessalonians volume of the full edition (the Second Epistle of Paul to the Thessalonians): metadata, the volume
cover, and the chapter plan (ch01.py).

Built on the letters' shared kit, tools/full/epistle.py (EpistleKit with fit_faces=True and clip=True), and on 1
Thessalonians' drawings and helpers (th1.art, th1.common.paged: the pages chosen by hand, each page's drawings scaled
together to fill it). A letter has no narration: every word of the ASV here is the letter — "Paul, and Silvanus, and
Timothy" again (1:1), written from Corinth not long after the first — in letter boxes (parchment, a sepia rule down the left
edge, a short tail toward Paul where his face is drawn). 2 Thessalonians quotes no scripture and no word of God in the first
person, so it has no song box and no Voice box.

The setting, as 1 Thessalonians: the study at Corinth by lamplight (epistle.study), Paul dictating, Timothy (Acts' look) on
the mat writing, Silvanus (Acts' Silas: a blue headcloth and robe, a black beard) standing by.

Paul's face is joyful white at 1:3–4 and 2:13–14 (we are bound to give thanks), earnest gold at 1:11–12, 3:3–5 and 3:13–15.

Drawings (th2.art, on th1.art): the study at Corinth (1:1–2); the balance of righteous judgment in light over the city
at night (1:5–6); the heavens opened in white light and flaming fire over an empty plain (1:7–10); a stranger at Jason's
door at night with a letter "as from us", the brethren troubled (2:1–2); the seat in the temple empty in shadow (2:3–4);
Paul teaching the church in Jason's house when he was yet with them (2:5–7); light breaking into the dark sanctuary, the
seat overturned and empty (2:8–12); the letters the church was taught by — the first epistle open on the table, the second
sealed beside it, the lamp (2:15); a messenger on the road at morning with the sealed roll (3:1, "that the word of the Lord
may run"); Paul and Silvanus at the tent-cloth by night (3:7–9, th1's drawing); a table at evening — the worker eating his
own bread, his tools laid by, an idle man at the door with empty hands (3:10–12); Paul's own hand writing the salutation
at the foot of the letter (3:17); the benedictions over the light (2:16–17, 3:16, 3:18).

2 Thessalonians' cast, each the same everywhere (th1.art): Paul only ever the kit's PAUL faces and epistle.paul_fig;
Silvanus, Timothy and Jason as 1 Thessalonians draws them; the Thessalonians in cool or off-white headcloths and cool veils.

Restraint: the Lord revealed from heaven "with the angels of his power in flaming fire" (1:7) is fire and white light only,
no figure in it — the angels are not drawn, only light; 1:8–9 (vengeance, punishment, eternal destruction) are words over the
fire and the empty plain, no one punished and no one drawn on it. "The man of sin … the son of perdition" (2:3–4) is never
drawn as a figure: words over the empty seat in the temple in shadow; "the lawless one, whom the Lord Jesus shall slay with
the breath of his mouth" (2:8) and "the working of Satan" (2:9) are words only, over light breaking into the empty
sanctuary and the seat overturned; Christ is not drawn there, only light. Satan is never drawn; "the evil one" (3:3) is words
beside Paul's face. The disorderly (3:6–12) are shown only by an idle man standing at a door, nothing mocking. God is never
drawn.

Plan (1,051 words, one chapter): 1 Stand Fast (1–3)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("2TH")

META = {
  "id": "2thessalonians", "order": 53, "name": "2 Thessalonians", "kanji": "テサロニケ人への第二の手紙", "thumb": "vol-2thessalonians-", "book": "2TH",
  "title": "2 Thessalonians Volume", "volume": "Volume Fifty-Three",
  "lede": "The fifty-third book of the Bible, in full: Paul's second letter to the church of the Thessalonians, written again from Corinth with Silvanus and Timothy — your faith groweth exceedingly, the Lord Jesus revealed from heaven in flaming fire, the day of the Lord not yet at hand, the falling away and the man of sin, stand fast and hold the traditions, pray that the word of the Lord may run, if any will not work neither let him eat, be not weary in well-doing, and the salutation in Paul's own hand, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Stand Fast", "range": "2 Thessalonians 1–3", "bible_chapters": [1, 2, 3],
     "blurb": "Paul, and Silvanus, and Timothy, unto the church of the Thessalonians; your faith groweth exceedingly, and your patience in all your persecutions; the Lord Jesus revealed from heaven with the angels of his power in flaming fire; be not quickly shaken, as that the day of the Lord is just at hand: the falling away must come first, and the man of sin be revealed, whom the Lord Jesus shall slay with the breath of his mouth; God chose you from the beginning unto salvation; stand fast, and hold the traditions; pray for us, that the word of the Lord may run; if any will not work, neither let him eat; be not weary in well-doing; the salutation of me Paul with mine own hand."},
  ],
}
