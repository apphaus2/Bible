"""The 2 Timothy volume of the full edition (the Second Epistle of Paul to Timothy): metadata, the volume cover, and the
chapter plan (ch01.py).

Built on the letters' shared kit, tools/full/epistle.py (EpistleKit with fit_faces and clip), as 1 Timothy is, with 1
Timothy's cast (ti1.common) and drawings (ti1.art, ti1.art2). Every word of the ASV here is Paul writing to Timothy (letter
boxes); the faithful saying "For if we died with him, we shall also live with him …" (2:11–13) is a song box, a hymn; so
are the two sayings of the seal of the firm foundation (2:19). The doxology (4:18) is a glory panel.

This is Paul's last letter: he is in prison at Rome again, near his end. His cell is drawn darker and barer than the hired
house of Acts 28:30 and the earlier prison letters (epistle.study's prison stages): walls of dressed stone, one small
barred window high up, one clay lamp in a niche, no shelves of scrolls (he asks for his books, 4:13), the soldier and the
chain, and Luke alone with him (4:11), writing on his mat. The reader stands where Timothy stands at Ephesus: Timothy, a
few years older than in 1 Timothy, with a short beard now, reads the letter by his lamp (1:3–4) and is drawn again
committing the things heard to faithful men (2:2), gentle toward them that oppose (2:24–26), preaching the word (4:2).
Paul's faces: by the cell's lamp, earnest gold, stern red at the false teachers (2:16–18, 3:6–7, 4:3–5, 4:14–15), grieving
blue at "all that are in Asia turned away from me" (1:15), white with joy at the faithful saying; and for "I am already
being offered, and the time of my departure is come" (4:6), the heart of the volume, his face in a grave gold light
(PAUL_OFFERED), then the finished course and the crown of righteousness laid up.

Drawings (ti2.art): the cell and Luke; Onesiphorus come to the cell door with bread (1:16–17); Lois, Eunice and Timothy as
three framed faces joined by a line of light (1:5), and the boy Timothy reading the sacred writings between them at Lystra
(3:15); the gift stirred up, the brazier's coals fanned into flame (1:6); the deposit, a coffer bound and sealed (1:12–14);
the soldier, the athlete and the husbandman as three cells (2:3–6); "Remember Jesus Christ, risen from the dead" (2:8) as
1 Corinthians' garden tomb, Jesus risen in white light (co1.art5); the chained wrist and the word not bound going out on the
road (2:9); the workman cutting true along his line (2:15); the foundation stone with its seal (2:19); the vessels of a
great house (2:20–21); the last days (3:1–5) as Galatians' dark street; Jannes and Jambres before Pharaoh's gate with
Moses and Aaron (Exodus' gate and looks, 3:8); the three gates of Antioch, Iconium and Lystra at evening (3:11); the ark of
the scrolls (Romans, 3:16); the stadium's finishing post at evening and the crown of righteousness in light (4:7–8); the
brethren scattered on the map, Luke alone with Paul (4:10–12); the cloak, the books and the parchments at Troas (4:13); the
empty judgment-seat (4:16–17); the greetings (4:19–21) as portrait cells.

2 Timothy's own cast (ti2.common): Timothy as in 1 Timothy with a short brown beard (TIMOTHY_OLD); Lois old, grey-haired,
in a dark-blue veil, and Eunice in a grey-green veil (ti1.common); Luke the physician, a short grey beard, an off-white
headcloth (ti1.common.LUKE, ti2.art.luke_fig and his look on the seated scribe); Onesiphorus a slate headcloth and a brown
beard; Prisca and Aquila as Acts draws them; Erastus an off-white headcloth; Trophimus, Eubulus and Pudens bareheaded;
Linus a dark headcloth; Claudia a slate-blue veil. Every headcloth and veil is cool, dark or off-white.

Restraint: Paul's coming death (4:6) is told in words beside his face in a grave gold light, then the empty stadium and the
crown in light — nothing of execution is drawn; the persecutions at Antioch, Iconium and Lystra (3:11) are words over the
three gates, shut and empty, no one stoned or struck; the last days' list (3:2–5) is words over a dark, empty street; the
creeping into houses (3:6) words beside Paul's face; the snare of the devil (2:26) words only — Satan is never drawn;
Alexander the coppersmith (4:14–15) words beside Paul's face; "delivered out of the mouth of the lion" (4:17) words over the
empty judgment-seat, no lion drawn; the gangrene (2:17) words only; God is never drawn; the soldier in the cell is the
guard with his spear, nothing done to anyone.

Plan (1,611 words, one chapter): 1 I Have Kept the Faith (1–4)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("2TI")

META = {
  "id": "2timothy", "order": 55, "name": "2 Timothy", "kanji": "テモテへの第二の手紙", "thumb": "vol-2timothy-", "book": "2TI",
  "title": "2 Timothy Volume", "volume": "Volume Fifty-Five",
  "lede": "The fifty-fifth book of the Bible, in full: Paul's last letter, from his bonds at Rome, to Timothy his beloved child — the unfeigned faith of Lois and Eunice; stir up the gift of God; I know him whom I have believed; a good soldier of Christ Jesus; the word of God is not bound; a workman that needeth not to be ashamed; the firm foundation of God standeth; in the last days grievous times shall come; every scripture inspired of God; preach the word; I have fought the good fight, I have finished the course, I have kept the faith; only Luke is with me; bring the cloak and the books, especially the parchments, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "I Have Kept the Faith", "range": "2 Timothy 1–4", "bible_chapters": [1, 2, 3, 4],
     "blurb": "Paul, an apostle, to Timothy, my beloved child; the unfeigned faith that dwelt first in thy grandmother Lois and thy mother Eunice; stir up the gift of God; God gave us not a spirit of fearfulness; I know him whom I have believed; the house of Onesiphorus; suffer hardship with me, as a good soldier of Christ Jesus; remember Jesus Christ, risen from the dead; the word of God is not bound; a workman handling aright the word of truth; the firm foundation of God standeth; vessels unto honor; in the last days grievous times shall come; as Jannes and Jambres withstood Moses; from a babe thou hast known the sacred writings; every scripture inspired of God; preach the word; I am already being offered; I have fought the good fight, I have finished the course, I have kept the faith; the crown of righteousness; only Luke is with me; the cloak, the books, the parchments; the Lord stood by me; come before winter."},
  ],
}
