"""The Acts volume of the full edition (the Acts of the Apostles): metadata, the volume cover, and the chapter plans
(ch01.py, ...).

Built as Mark is, on the minor prophets' kit (oba/minor.py: Kit, page packing, by way of mrk.common.MarkKit) and on Mark's
and Matthew's drawings (act.art starts `from mrk.art9 import *`); new drawings in act.art*. The journeys are technical maps
on one projection of the Mediterranean (act/geo.py: coastlines traced in longitude and latitude, places and regions by name,
the route of each journey lit in red). Jesus and the recurring cast come only from tools/full/ntcast.py: Jesus risen in
white light at the ascension; Peter, John, James and Paul (Saul before his calling is the same man, ntcast's Paul and
SAUL_PERSECUTOR) at a distance in act.art (peter, john_ap, james_ap, paul). Jesus' words (1:4–8, and from the light) are
ordinary speech boxes. God is never drawn; the Holy Spirit's words (8:29, 10:19, 13:2, 21:11 …) go in the Voice box, and at
Pentecost the Spirit is the rushing wind and small tongues of flame-light over each head. Angels are figures of white light
with a gold rim and no face. Satan and demons are never drawn. The scripture the speakers quote is set in song boxes.

Acts' own cast (act.common faces, act.art figures), each the same in every chapter: Matthias (an ochre headcloth with a
cord, a brown beard) and Joseph Barsabbas (an off-white headcloth, slate robe); Gamaliel (white beard, a dark-blue
headcloth with a gold band); the high priest Annas and the council (Matthew's chief priests in white; Caiaphas from
ntcast); Ananias and Sapphira (dull olive headcloth and veil, in a cold light); Stephen (young, bareheaded, short black
beard, a deep sea-green robe; in glory a white light); Philip the evangelist (a teal headcloth with a cord, black beard);
Simon the sorcerer (a violet headcloth with a band); the Ethiopian eunuch (dark skin, an off-white turban with a gold
band, a green-and-gold robe, in his chariot); Ananias of Damascus (grey beard, a slate headcloth); Barnabas (a green
headcloth and robe, a brown beard); Æneas and Dorcas; Cornelius (a centurion: Matthew's and Mark's Roman helmet and red
cloak, greying hair); Rhoda (a girl, bareheaded); Herod Agrippa I (a gold diadem, a black beard, a royal purple robe —
not ntcast's HEROD the tetrarch, who wears a purple headcloth); Sergius Paulus (a proconsul's toga) and Elymas (a dark
headcloth with a band); Silas (a blue headcloth and robe, black beard); Timothy (young, beardless, light brown hair, a
grey-blue tunic); Lydia (a deep violet veil, the purple cloth of her trade); the Philippian jailor; the Athenians
(white-bearded philosophers in himations); Aquila (a sand headcloth) and Priscilla (a sea-blue veil); Apollos of
Alexandria; Demetrius the silversmith and the town-clerk; Eutychus; Agabus (white beard, a dark-brown headcloth);
Claudius Lysias the chief captain (bareheaded, a red cloak); Ananias the high priest (a white headcloth with a gold band,
black beard); Paul's sister's son; Tertullus; Felix (Roman, short dark stubble) and Drusilla (a deep teal veil with a gold
band); Festus (greying, clean-shaven); Agrippa II (a gold diadem, black stubble) and Bernice (a deep blue veil with a gold
band); Julius the centurion (the helmet, dark stubble); Publius (white beard, a toga). A warm scarf would read as long
hair: every headcloth and veil here is cool, dark or off-white.

Restraint: Judas' end (1:18–19) words over the empty field of blood; Ananias and Sapphira (5:5, 5:10) words over the empty
floor and the door; the scourging of the apostles (5:40) words over the council's door; Stephen stoned (7:58–60) words over
the city wall and the garments laid at Saul's feet; Stephen's vision (7:55–56) the heavens opened as light, the Son of man
standing as light, God never drawn; the Damascus road a light from heaven and Saul fallen to the earth, Jesus' words in
speech boxes from the light (he is not drawn there, nor in the visions of 9:10, 18:9, 22:18 and 23:11); Saul's blindness and
the scales; Simon the sorcerer and Elymas words, no sorcery drawn; James killed with the sword (12:2) and the guards (12:19)
words only; Peter freed by an angel of white light; Herod smitten (12:23) words over the empty throne; Paul stoned at Lystra
(14:19) words over the gate; the spirit of divination in the maid (16:16–18) never drawn, words over the street; the beating
at Philippi (16:22–23) words over the stocks, the earthquake opening the doors; the sons of Sceva (19:16) words over the
house door; Eutychus (20:9) the window and the lamps, then alive; Agabus binding his own hands with Paul's girdle; the riot
and the arrest; Paul's speeches as speech panels; the shipwreck a map and the ship breaking on the shoal, no one drowning;
the viper (snake.py) shaken off into the fire; Rome.

Four verse numbers have no text in the ASV (8:37, 15:34, 24:7, 28:29: the USFM carries only a footnote), so the coverage
lists them as omitted, as Matthew's and Mark's do theirs.

Plan (24,174 words, sixteen chapters): 1 The Promise of the Father (1–2) · 2 Silver and Gold Have I None (3–4) · 3 We Must
Obey God (5–6) · 4 Stephen (7) · 5 The Road to Damascus (8–9) · 6 What God Hath Cleansed (10–11) · 7 The Word of God Grew
(12–13) · 8 The Council at Jerusalem (14–15) · 9 Come Over into Macedonia (16) · 10 The Unknown God (17–18) · 11 Great Is
Diana (19–20) · 12 Bound in the Spirit (21–22) · 13 Before Felix (23–24) · 14 Before Agrippa (25–26) · 15 The Shipwreck
(27) · 16 Rome (28)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("ACT")

META = {
  "id": "acts", "order": 44, "name": "Acts", "kanji": "使徒行伝", "thumb": "vol-acts-", "book": "ACT",
  "title": "Acts Volume", "volume": "Volume Forty-Four",
  "lede": "The forty-fourth book of the Bible, in full: the ascension and the Spirit poured forth at Pentecost, Peter and John before the council, Stephen, the road to Damascus, Cornelius, Paul's journeys through Cyprus, Galatia, Macedonia, Achaia and Asia, the arrest in Jerusalem, the shipwreck on Melita and the gospel preached at Rome, every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Promise of the Father", "range": "Acts 1–2", "bible_chapters": [1, 2],
     "blurb": "Forty days, and wait for the promise of the Father; ye shall be my witnesses unto the uttermost part of the earth; a cloud received him out of their sight; the upper chamber and the lot that fell upon Matthias; then Pentecost — a sound as of a mighty wind, tongues as of fire — and every man heard them in his own language; Peter's sermon, and about three thousand souls."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Silver and Gold Have I None", "range": "Acts 3–4", "bible_chapters": [3, 4],
     "blurb": "The lame man at the door of the temple called Beautiful — silver and gold have I none; in the name of Jesus Christ of Nazareth, walk; walking, and leaping, and praising God; Peter in Solomon's porch; the ward and the council — the stone set at nought of you the builders; we cannot but speak the things which we saw and heard; the place shaken; and all things common."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "We Must Obey God", "range": "Acts 5–6", "bible_chapters": [5, 6],
     "blurb": "Ananias and Sapphira and the price kept back — thou hast not lied unto men, but unto God; signs and wonders, and Peter's shadow on the sick in the streets; an angel by night opens the prison doors; we must obey God rather than men; Gamaliel's counsel — if it is of God, ye will not be able to overthrow them; the seven chosen to serve tables; and Stephen, his face as it had been the face of an angel."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "Stephen", "range": "Acts 7", "bible_chapters": [7],
     "blurb": "Are these things so? — Stephen's defence before the council: Abraham called out of Mesopotamia, Joseph sold into Egypt, Moses at the bush and at the Red sea, the calf, the tabernacle and the house Solomon built — howbeit the Most High dwelleth not in houses made with hands; ye stiffnecked; I see the heavens opened; and the garments laid down at the feet of a young man named Saul: Lord, lay not this sin to their charge."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "The Road to Damascus", "range": "Acts 8–9", "bible_chapters": [8, 9],
     "blurb": "Saul laying waste the church; Philip in Samaria and Simon the sorcerer — thy silver perish with thee; the Ethiopian reading Isaiah in his chariot on the desert road — understandest thou what thou readest?; then near Damascus a light out of heaven: Saul, Saul, why persecutest thou me?; three days without sight; Ananias and the scales; the basket let down over the wall; Æneas, arise; and Tabitha, arise."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "What God Hath Cleansed", "range": "Acts 10–11", "bible_chapters": [10, 11],
     "blurb": "Cornelius the centurion at the ninth hour and the angel of God; Peter on the housetop at Joppa and the great sheet let down by four corners — what God hath cleansed, make not thou common; Stand up; I myself also am a man; God is no respecter of persons, and the Holy Spirit fell on the Gentiles; then Antioch, Barnabas and Saul, and the disciples called Christians first."},
  ],
}
