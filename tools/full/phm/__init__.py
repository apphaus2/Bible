"""The Philemon volume of the full edition (the Epistle of Paul to Philemon): metadata, the volume cover, and the chapter
plan (ch01.py: the whole letter, one short manga chapter).

Built on the letters' shared kit, tools/full/epistle.py (EpistleKit with fit_faces and clip), and on the other prison
letters: phm.common takes the cast from php.common, phm.art its drawings from col.art (and through it php.art). A letter has
no narration: every word of the ASV here is Paul writing to Philemon (letter boxes, a short tail toward Paul where his face is
drawn). Philemon quotes no scripture: no song boxes, no Voice box.

Written from Paul's bonds at Rome ("a prisoner of Christ Jesus", 1, 9) and sent back with Onesimus (12), who went with
Tychicus (Colossians 4:7–9): the volume opens on the prison stage, Paul chained to the soldier, Timothy (co-sender, 1)
writing on his mat and Onesimus standing by.

Paul's face: by lamplight at 8–9 ("Paul the aged, and now a prisoner also"), earnest gold at 13–14.

Drawings (phm.art): the prison study with Onesimus; Philemon's house at Colossæ under snowy Mount Cadmus, Philemon, Apphia and
Archippus at the open door and the saints coming in (the church in thy house, 2, 4–7); Onesimus serving Paul, bringing him a
cup of water, Paul's free hand on his shoulder (10–12); Onesimus and Tychicus walking up the Lycus valley to Colossæ, Onesimus
carrying the letter (15–16); Paul's own hand writing the pledge on a reckoning, the iron cuff on his wrist (18–19); the upper
room made ready, Apphia spreading the blanket, the window on the mountain (22); Epaphras, Mark, Aristarchus, Demas and Luke
with Paul in his room at Rome (23–24); the grace over the light. Cover: Onesimus come home at evening, holding out the letter
to Philemon at his door, Apphia in the doorway.

The cast (php.common, the same in all three prison letters): Philemon a grey beard, an off-white headcloth with a brown cord,
a deep-blue robe and mantle; Apphia a dark-blue veil; Archippus a charcoal headcloth and black beard; Onesimus young,
bareheaded, short black curls, clean-shaven, a plain undyed tunic; Tychicus a slate-teal headcloth with a cord, short brown
beard, grey cloak; Epaphras, Mark, Aristarchus, Demas and Luke as Colossians draws them; Paul only ever the kit's faces and
epistle.paul_fig, chained to epistle.roman_guard. No warm headcloths or veils.

Restraint: Onesimus's flight and whatever wrong he did (11, 15, 18) are told in words only; no beating, no chain and no
punishment is drawn on him — he is drawn serving Paul, walking home with the letter and standing at his master's door, a
brother. Paul's bonds are the chain at his own wrist. Nothing else in the letter asks for restraint.

Plan (438 words, one chapter): 1 More Than a Servant (1–25)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("PHM")

META = {
  "id": "philemon", "order": 57, "name": "Philemon", "kanji": "ピレモンへの手紙", "thumb": "vol-philemon-", "book": "PHM",
  "title": "Philemon Volume", "volume": "Volume Fifty-Seven",
  "lede": "The fifty-seventh book of the Bible, in full: Paul's letter from his bonds at Rome to Philemon and the church in his house at Colossæ, sent with Onesimus — I beseech thee for my child, whom I have begotten in my bonds; no longer as a servant, but more than a servant, a brother beloved; receive him as myself; put that to mine account; I Paul write it with mine own hand, I will repay it; prepare me also a lodging, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "More Than a Servant", "range": "Philemon 1–25", "bible_chapters": [1],
     "blurb": "Paul, a prisoner of Christ Jesus, and Timothy, to Philemon, to Apphia our sister, to Archippus our fellow-soldier, and to the church in thy house; the hearts of the saints have been refreshed through thee; for love's sake I rather beseech, being such a one as Paul the aged; I beseech thee for my child Onesimus, whom I have begotten in my bonds, once unprofitable, now profitable — my very heart; no longer as a servant, but more than a servant, a brother beloved; receive him as myself; if he oweth thee aught, put that to mine account: I Paul write it with mine own hand, I will repay it; prepare me also a lodging; Epaphras, Mark, Aristarchus, Demas, Luke."},
  ],
}
