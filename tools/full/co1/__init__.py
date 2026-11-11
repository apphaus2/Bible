"""The 1 Corinthians volume of the full edition (the First Epistle of Paul to the Corinthians): metadata, the volume cover,
and the chapter plans (ch01.py, ...).

Built on the epistle kit, tools/full/epistle.py (EpistleKit, the letter box, the opening scene, the sealed scroll, the
doxology panel, the greetings roll), as Romans is. A letter has no narration: every word of the ASV here is Paul (and
Sosthenes, 1:1) writing to the church of God at Corinth — letter boxes, beside Paul's face or over the drawings; the
scriptures he quotes are song boxes (1:31, 2:9, 2:16, 3:19–20, 9:9, 10:7, 10:26, 15:27, 15:45, 15:54–55); God's own words
quoted in the first person are the Voice box (1:19 "I will destroy the wisdom of the wise", 14:21 "By men of strange
tongues … will I speak unto this people … saith the Lord"); Jesus' words at the supper (11:24–25) are ordinary balloons,
spoken by ntcast's Jesus at the table (Matthew's last-supper drawing, mat.art10.supper). God is never drawn — light, the
Voice box; the increase of 3:6–7 is light falling on the plant, the fire of 3:13 light and flame on the work.

Setting: written from Ephesus (16:8) by Paul with Sosthenes (1:1); Sosthenes writes it down, Paul adds the salutation with
his own hand (16:21). Stephanas, Fortunatus and Achaicus, come from Corinth (16:17), carry it back across the Aegean
(co1.art.aegean_road). The study's window shows Ephesus (the theatre on the hill and Diana's temple far off), not Corinth.

Drawings (co1.art …, on top of all of Acts' drawings by way of act.art16, and the epistle kit): the four factions as a split
plate (1:12); the word of the cross as three crosses far off on a hill under a darkened sky (1:18, 1:23, 2:2 — nothing
nearer); the Jew asking a sign and the Greek with his scroll (1:22); things which eye saw not (2:9); planting and watering,
God's husbandry (3:6–9); the foundation plate and the fire that proves the work (3:10–15); the temple (3:16, 6:19); the
stewards (4:1–2); the empty arena (4:9); the tentmakers' bench (4:12); the rod or love (4:21) …

1 Corinthians' own cast, each the same everywhere (every headcloth cool, dark or off-white — a warm scarf would read as long
hair): Paul only ever ntcast's face (PAUL and epistle's moods) and epistle.paul_fig; Sosthenes a slate-grey headcloth with a
dark cord and a short grey-black beard, a blue-grey robe; Stephanas the oldest of the three, an off-white headcloth, a grey
beard, a brown robe; Fortunatus a navy headcloth, a black beard, a deep-green robe; Achaicus young and bareheaded, beardless,
a grey-violet tunic; the household of Chloe's messenger a dark-teal headcloth. Apollos, Aquila, Priscilla, Timothy and James
the Lord's brother as Acts draws them (act.common faces); Cephas as ntcast's Peter.

Restraint: God, Satan and demons are never drawn — 5:5, 7:5 and 10:20–21 are words only, over a shut door, a lamp at a
table and an empty idol-temple court. Angels (4:9, 6:3, 11:10, 13:1) are only words. 5:1–13 are words over a shut door and
an empty house front; 6:9–20 words over dark, empty streets and the temple; 7 (marriage) words over plain household scenes
— a lamp at a table, a house door, a courtyard — nothing sexual drawn; 10:8–10 words over the empty desert (the serpents of
10:9 drawn with snake.py, no one bitten); 11:30 words only; 15:32 ("fought with beasts at Ephesus") words over the empty
theatre. The crucifixion is only ever three crosses on a hill far off.

Plan (9,415 words, five chapters): 1 Christ the Power of God (1–4)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("1CO")

META = {
  "id": "1corinthians", "order": 46, "name": "1 Corinthians", "kanji": "コリント人への第一の手紙", "thumb": "vol-1corinthians-", "book": "1CO",
  "title": "1 Corinthians Volume", "volume": "Volume Forty-Six",
  "lede": "The forty-sixth book of the Bible, in full: Paul's first letter to the church of God at Corinth, written at Ephesus with Sosthenes and carried home by Stephanas, Fortunatus and Achaicus — I of Paul, I of Apollos, I of Cephas; the word of the cross, Christ the power of God; I planted, Apollos watered, but God gave the increase; ye are a temple of God; a little leaven; meats offered to idols; the race and the incorruptible crown; the Lord's supper; one body and many members; love, the greatest of these; Christ raised, the firstfruits; O death, where is thy victory? — every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "Christ the Power of God", "range": "1 Corinthians 1–4", "bible_chapters": [1, 2, 3, 4],
     "blurb": "Paul and Sosthenes to the church of God which is at Corinth — the letter written at Ephesus; I am of Paul; and I of Apollos; and I of Cephas; and I of Christ: is Christ divided? The word of the cross is to them that perish foolishness, but unto us who are saved it is the power of God; things which eye saw not; I planted, Apollos watered, but God gave the increase; other foundation can no man lay; the fire shall prove each man's work; ye are a temple of God; a spectacle unto the world; shall I come with a rod, or in love?"},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "A Little Leaven", "range": "1 Corinthians 5–7", "bible_chapters": [5, 6, 7],
     "blurb": "Ye are puffed up, and did not rather mourn; know ye not that a little leaven leaveneth the whole lump? Purge out the old leaven, for our passover also hath been sacrificed, even Christ; brother goeth to law with brother, and that before unbelievers; but ye were washed, but ye were sanctified; your body is a temple of the Holy Spirit, for ye were bought with a price; concerning the things whereof ye wrote — the married, the unmarried and the widows, the bondservant and the free; the time is shortened, for the fashion of this world passeth away."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "In Remembrance of Me", "range": "1 Corinthians 8–11", "bible_chapters": [8, 9, 10, 11],
     "blurb": "Knowledge puffeth up, but love edifieth: there is no God but one; if meat causeth my brother to stumble, I will eat no flesh; am I not an apostle? Thou shalt not muzzle the ox; I am become all things to all men; so run, that ye may attain — a corruptible crown, but we an incorruptible; our fathers under the cloud, through the sea, and the rock was Christ; the way of escape; the cup of blessing which we bless; do all to the glory of God; praying with the head covered or unveiled; the Lord Jesus in the night in which he was betrayed took bread: this do in remembrance of me."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "The Greatest of These Is Love", "range": "1 Corinthians 12–14", "bible_chapters": [12, 13, 14],
     "blurb": "Concerning spiritual gifts: diversities of gifts, but the same Spirit; as the body is one, and hath many members, so also is Christ — if the foot shall say, Because I am not the hand; the eye cannot say to the hand, I have no need of thee; ye are the body of Christ; a most excellent way: if I have not love, I am become sounding brass, or a clanging cymbal; love suffereth long, and is kind; now we see in a mirror, darkly; but then face to face; faith, hope, love, and the greatest of these is love; if the trumpet give an uncertain voice; let all things be done decently and in order."},
  ],
}
