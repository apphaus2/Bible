"""The Philippians volume of the full edition (the Epistle of Paul to the Philippians): metadata, the volume cover, and the
chapter plans (ch01.py, ch02.py).

Built on the letters' shared kit, tools/full/epistle.py (EpistleKit with fit_faces and clip: face panels sized to their
words, drawings clipped to their panels), as Galatians is. A letter has no narration: every word of the ASV here is Paul
writing to the saints at Philippi (letter boxes: parchment, a sepia rule down the left edge, a short tail toward Paul where
his face is drawn). Philippians quotes no scripture and gives no word of God in the first person, so there are no song boxes
and no Voice box.

The first of the prison letters (Philippians, Colossians, Philemon: php/common.py holds their shared cast, php/art.py their
figures): written from Paul's own hired dwelling at Rome, chained to the soldier that guarded him (Acts 28:16, 20, 30) —
the volume opens on epistle.study's prison stage, Timothy (co-sender, 1:1) writing on his mat, the window on Rome.

Paul's face: earnest gold, by lamplight at 1:6–8 (his bonds, "I have you in my heart"), white with joy at 1:25–26, 4:4–5 and
4:13–14, stern red at 3:2–4 ("beware of the dogs"), grieving blue at 3:18–19 ("even weeping").

Drawings (php.art, php.art2, on 1 Corinthians' and Acts' drawings and the epistle kit): the prison study at Rome; the letter's
road from Rome by Brundisium and the Egnatian Way to Philippi; the saints at Philippi praying in the court of the house (the
bishops and deacons, 1:1); the whole prætorian guard (1:13), Paul chained and speaking to soldiers of the guard in their camp;
"to live is Christ, and to die is gain" as a plate of the vine and the sunrise (1:21); "to depart" (1:23), a ship loosed from her
moorings at dawn; the saints standing fast together in the forum before the magistrates (1:27–28); of one mind at table
(2:1–4); 2:5–11 as two plates, the way down (the light of the form of God growing less step by step; ntcast's Jesus, small, in
fashion as a man; the hill of the three crosses far off) and the way up (the light growing to "Jesus Christ is Lord", every
knee in heaven, on earth and under the earth); lights in the world, a dark crooked city with lamps in its windows (2:15); the
drink-offering poured on the altar's fire (2:17); Timothy standing ready with his staff (2:19–24); Epaphroditus sick on his
bed, Paul beside him (2:25–27), then walking home with the letter (2:28–30). Philippians 3–4: Epaphroditus reading the letter
to the church by lamplight (3:1); Paul's credentials as a plate of seven emblems (3:5–6); all things counted loss on a balance
(3:7–11); the runner in the stadium pressing toward the goal (3:13–14, co1.art3.athlete); the straight Roman road and the
surveyor's rule (3:16–17); Philippi the colony, its arch on the Egnatian Way under the opened light of heaven (3:20); Euodia,
Syntyche and the true yokefellow (4:2–3); the peace of God keeping guard, a town asleep under the stars and the watch on its
tower (4:7); "whatsoever things are true" as a plate of six emblems (4:8); want and plenty (4:12); the gifts sent from
Philippi on the map (4:15–16); Epaphroditus bringing the gift, a censer's sweet smoke (4:18); Cæsar's household at the
Palatine (4:22); the grace over the light.

The cast (php/common.py; the same in Colossians and Philemon): Paul only ever the kit's faces and epistle.paul_fig, chained to
epistle.roman_guard; Timothy as Acts draws him (bareheaded, light-brown hair, grey-blue tunic); Epaphroditus a slate headcloth,
short brown beard, olive robe and grey cloak; Euodia a dark-teal veil, Syntyche an off-white veil; Romans of the colony in white
togas on the kit silhouette (php.art.toga_r). No warm headcloths or veils (a warm scarf reads as long hair).

Restraint: 3:2 ("beware of the dogs … the concision") and 3:3–4 are words only, beside Paul's stern face; circumcision is never
drawn — "the eighth day" is eight lamps on the credentials plate, the last one lit; "persecuting the church" is a house door
broken in, no one there; Epaphroditus "sick nigh unto death" is a man lying under a blanket by lamplight, Paul's hand on his
shoulder; death (1:20–23) is a ship loosed at dawn and a sunrise over the sea; the cross (2:8) only three crosses far off on a
dark hill, no figure on them; "the enemies of the cross … whose god is the belly" (3:18–19) words only, beside Paul's grieving
face. God is never drawn (light: 2:9–11, 3:20); Christ is light, and once ntcast's Jesus, small, on the plate of 2:7–8.

Plan (2,231 words, two chapters): 1 To Live Is Christ (1–2) · 2 Rejoice in the Lord (3–4)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("PHP")

META = {
  "id": "philippians", "order": 50, "name": "Philippians", "kanji": "ピリピ人への手紙", "thumb": "vol-philippians-", "book": "PHP",
  "title": "Philippians Volume", "volume": "Volume Fifty",
  "lede": "The fiftieth book of the Bible, in full: Paul's letter from his bonds at Rome to the saints at Philippi, carried home by Epaphroditus — my bonds manifest throughout the whole prætorian guard, to live is Christ and to die is gain, have this mind in you which was also in Christ Jesus, who emptied himself and whom God highly exalted, lights in the world, Timothy and Epaphroditus, all things counted loss, I press on toward the goal, our citizenship is in heaven, rejoice in the Lord always, the peace of God which passeth all understanding, whatsoever things are true, I can do all things in him that strengtheneth me, and Cæsar's household, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "To Live Is Christ", "range": "Philippians 1–2", "bible_chapters": [1, 2],
     "blurb": "Paul and Timothy, servants of Christ Jesus, to all the saints at Philippi — the letter written in his bonds at Rome; he who began a good work in you will perfect it; my bonds became manifest throughout the whole prætorian guard; Christ is proclaimed, and therein I rejoice; for to me to live is Christ, and to die is gain; having the desire to depart and be with Christ; stand fast in one spirit; have this mind in you, which was also in Christ Jesus, who emptied himself, taking the form of a servant, and became obedient unto the death of the cross — wherefore God highly exalted him; lights in the world; poured out upon the sacrifice of your faith; Timothy; Epaphroditus, sick nigh unto death, sent home."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Rejoice in the Lord", "range": "Philippians 3–4", "bible_chapters": [3, 4],
     "blurb": "Rejoice in the Lord; beware of the dogs; a Hebrew of Hebrews, as touching the law a Pharisee — what things were gain to me, these have I counted loss for Christ; that I may know him, and the power of his resurrection; I press on toward the goal unto the prize of the high calling of God; our citizenship is in heaven; Euodia and Syntyche; rejoice in the Lord always; in nothing be anxious, and the peace of God, which passeth all understanding, shall guard your hearts; whatsoever things are true, honorable, just, pure, lovely, of good report; I have learned, in whatsoever state I am, therein to be content; I can do all things in him that strengtheneth me; an odor of a sweet smell; they that are of Cæsar's household."},
  ],
}
