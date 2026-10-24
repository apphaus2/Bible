"""The John volume of the full edition (the Gospel according to John): metadata, the volume cover, and the chapter plans
(ch01.py, ...).

Built as Mark is, on the minor prophets' kit (oba/minor.py: Kit, page packing, through mrk.common's MarkKit), and on
Matthew's and Mark's drawings (jhn.art starts `from mrk.art9 import *`: Galilee and its boats, the houses and synagogues,
Jerusalem and the temple, the garden, Golgotha, the tomb); new drawings in jhn.art, jhn.art2, .... Jesus and the recurring
cast come only from tools/full/ntcast.py (faces JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF, JESUS_PASSION, JESUS_RISEN;
jesus_fig at a distance). His words are ordinary speech boxes. The Father's voice out of heaven (12:28) is the Voice box over
the sky; the Spirit descending is a dove of light; the angels (1:51, 20:12) are figures of white light with a gold rim and
no face. Satan is never drawn: "Satan entered into him" (13:27) is words over the night door. The long discourses (3, 5,
6, 8, 10, 14–17) alternate Jesus' faces with drawings of what he names (the bread, the light, the door, the shepherd, the
vine), so no page is a wall of one face. The scripture John quotes is set in song boxes.

John's own cast (jhn.common), each the same in every chapter; the people Matthew and Mark also tell of keep their looks
(Mary the mother of Jesus, Mary Magdalene, Martha, Peter, Andrew, Philip, Thomas, Judas, John the Baptist, Caiaphas, Pilate:
ntcast; Joseph of Arimathæa: Matthew's). Nathanael — a dark-teal headcloth with a cord, a brown beard; Nicodemus — a grey
beard, a deep indigo-violet headcloth with a gold band (a ruler of the Jews), drawn by night under a lamp, and again at the tomb with
the myrrh and aloes; the woman of Samaria — a plum veil, a water-pot on her shoulder; the nobleman of Capernaum — a black
beard, a purple headcloth with a gold band; the man at Bethesda — grey-haired, a grey beard, no headcloth, a grey-brown
mantle, on his pallet, then standing; the man born blind — a dark-brown beard, an undyed grey headcloth (eyes closed and
pale before, open after), his father white-bearded in a brown headcloth and his mother in a dark-olive veil; Lazarus —
a short dark beard, bareheaded; in the tomb door only as a standing figure wrapped in grave-clothes, his face bound
about with a napkin; Mary of Bethany — a deep-green veil (Martha: ntcast, ochre); Malchus — a servant in a grey tunic;
Annas — white-haired and white-bearded, a white headcloth with a gold band (older than Caiaphas); the officers — dark
grey headcloths; the Greeks — bareheaded, light-brown hair, a short beard; the beloved disciple is ntcast's John.

Restraint: the Word before 1:14 is light over the void, no figure (the Word became flesh is the first time Jesus is
seen); the cleansing of the temple is the scourge of cords lifted, the tables overturned, the money poured out and the
doves flying free, no one struck; the woman taken in adultery (7:53–8:11) is Jesus stooping to write on the ground, the
stones laid down one by one, she standing veiled at a distance, nothing more; the stones taken up to cast at him (8:59,
10:31) lie in the empty porch; the blind man's eyes anointed with clay is a hand to the brow, no wound; Lazarus' four days
in the tomb is words over the stone; he comes forth a wrapped standing figure at the tomb door, no decay drawn; the
anointing at Bethany is the cruse and the hair and the house full of the odor; the washing of feet is the basin of water
and the towel, Jesus kneeling, Peter seated, warm lamplight; Judas going out is the open door on the night; the arrest:
the torches and lanterns, those who went backward and fell to the ground, Malchus' ear words only and the sword dropped,
no blood; Annas' officer striking Jesus words only over the shut door; the scourging and the crown of thorns words over
the empty court and the purple robe laid aside; "Behold, the man!" Jesus far off on the pavement in the purple, no
wounds; the crucifixion only three crosses on the hill against the darkened sky, from a distance; his mother, her sister,
Mary Magdalene and the beloved disciple small figures at a distance below the hill; "It is finished" and the spear
(19:34) words over the darkened hill; the burial Joseph and Nicodemus in the garden with the linen and the spices, the new
tomb, the stone; the resurrection the stone taken away, the linen cloths lying and the napkin rolled up in a place by
itself; the two angels in white sitting where the body had lain, light with a gold rim, no face; then Jesus risen in white
light — in the garden with Mary Magdalene, among the disciples behind the shut doors, with Thomas, on the shore at dawn.

5:4 has no text in the ASV (only a footnote), so the coverage lists it as
omitted, as Matthew's lists 17:21, 18:11 and 23:14. 7:53–8:11 stands in the ASV in brackets and is kept in full, brackets
and all.

Plan (19,007 words, ten chapters: John's fifteen natural sections run eleven or twelve pages each at the New Testament
volumes' density, so they are paired into chapters of fifteen to twenty-odd pages): 1 The Word Became Flesh (1–2) ·
2 Ye Must Be Born Anew (3–4) · 3 The Bread of Life (5–6) · 4 Before Abraham Was (7–8) · 5 The Good Shepherd (9–10) ·
6 Lazarus, Come Forth (11–12) · 7 The Washing of Feet (13–14) · 8 That They May Be One (15–17) · 9 It Is Finished (18–19)
· 10 Lovest Thou Me? (20–21)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("JHN")

META = {
  "id": "john", "order": 43, "name": "John", "kanji": "ヨハネによる福音書", "thumb": "vol-john-", "book": "JHN",
  "title": "John Volume", "volume": "Volume Forty-Three",
  "lede": "The Gospel according to John, in full: in the beginning was the Word; the Lamb of God; water made wine; Nicodemus by night and the woman at the well; the bread of life, the light of the world, the good shepherd; Lazarus come forth; the washing of feet, the upper room and the prayer; the cross and the empty tomb; and by the sea at dawn, lovest thou me? — every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Word Became Flesh", "range": "John 1–2", "bible_chapters": [1, 2],
     "blurb": "In the beginning was the Word, and the light shineth in the darkness; a man sent from God whose name was John; the Word became flesh, and dwelt among us; the voice of one crying in the wilderness; behold, the Lamb of God; the Spirit descending as a dove; come and see; we have found the Messiah; Nathanael under the fig tree; the water become wine at Cana; and the scourge of cords in the temple — destroy this temple, and in three days I will raise it up."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "Ye Must Be Born Anew", "range": "John 3–4", "bible_chapters": [3, 4],
     "blurb": "Nicodemus by night — except one be born anew, he cannot see the kingdom of God; the wind bloweth where it will; as Moses lifted up the serpent; God so loved the world; he must increase, but I must decrease; then Jacob's well at the sixth hour and the woman of Samaria — give me to drink, living water, in spirit and truth, I that speak unto thee am he; the fields white already unto harvest; and the nobleman's son at Capernaum — go thy way; thy son liveth."},
    {"module": "ch03", "dir": "chapter-03", "num": "3", "name": "The Bread of Life", "range": "John 5–6", "bible_chapters": [5, 6],
     "blurb": "The pool of Bethesda with its five porches and the man of thirty and eight years — arise, take up thy bed, and walk; my Father worketh even until now, and I work; the dead shall hear the voice of the Son of God; John the lamp that burneth and shineth; then five barley loaves and two fishes on the much grass, twelve baskets over, the boat in the dark — it is I; be not afraid; I am the bread of life; and Lord, to whom shall we go? thou hast the words of eternal life."},
    {"module": "ch04", "dir": "chapter-04", "num": "4", "name": "Before Abraham Was", "range": "John 7–8", "bible_chapters": [7, 8],
     "blurb": "The feast of tabernacles — my time is not yet come; my teaching is not mine; on the last great day, if any man thirst, let him come unto me and drink, and rivers of living water; never man so spake; the woman taken in adultery — he that is without sin among you, let him first cast a stone, neither do I condemn thee; I am the light of the world; the truth shall make you free; and before Abraham was born, I am."},
    {"module": "ch05", "dir": "chapter-05", "num": "5", "name": "The Good Shepherd", "range": "John 9–10", "bible_chapters": [9, 10],
     "blurb": "The man blind from his birth — go, wash in the pool of Siloam, and he came seeing; the neighbours, the Pharisees, his father and mother afraid; one thing I know, that, whereas I was blind, now I see; Lord, I believe; then the fold of the sheep — I am the door; I am the good shepherd: the good shepherd layeth down his life for the sheep; other sheep I have; and in Solomon's porch in winter, I and the Father are one."},
    {"module": "ch06", "dir": "chapter-06", "num": "6", "name": "Lazarus, Come Forth", "range": "John 11–12", "bible_chapters": [11, 12],
     "blurb": "Lazarus of Bethany is sick; Thomas — let us also go, that we may die with him; Martha on the road — I am the resurrection, and the life; Jesus wept; take ye away the stone; Lazarus, come forth, bound with grave-clothes — loose him, and let him go; Caiaphas' counsel; Mary's pound of nard and the house filled with the odor; Hosanna and the branches of the palm trees; sir, we would see Jesus; except a grain of wheat fall into the earth and die; and a voice out of heaven: I have both glorified it, and will glorify it again."},
    {"module": "ch07", "dir": "chapter-07", "num": "7", "name": "The Washing of Feet", "range": "John 13–14", "bible_chapters": [13, 14],
     "blurb": "Having loved his own, he loved them unto the end: the towel and the basin in the upper room — Lord, dost thou wash my feet?; I have given you an example; one of you shall betray me, the sop, and it was night; a new commandment, that ye love one another; let not your heart be troubled: in my Father's house are many mansions; I am the way, and the truth, and the life; another Comforter; peace I leave with you; arise, let us go hence."},
    {"module": "ch08", "dir": "chapter-08", "num": "8", "name": "That They May Be One", "range": "John 15–17", "bible_chapters": [15, 16, 17],
     "blurb": "I am the true vine, ye are the branches; abide in me; greater love hath no man than this; ye are my friends; if the world hateth you; it is expedient for you that I go away; a little while, and ye shall see me; your sorrow shall be turned into joy; be of good cheer, I have overcome the world; and the prayer with his eyes lifted up to heaven — Father, the hour is come; that they may all be one; that the love wherewith thou lovedst me may be in them."},
    {"module": "ch09", "dir": "chapter-09", "num": "9", "name": "It Is Finished", "range": "John 18–19", "bible_chapters": [18, 19],
     "blurb": "Over the brook Kidron into the garden, the lanterns and torches — whom seek ye? I am he; put up the sword; Annas and the fire of coals, Peter's denials and the cock; the Prætorium — my kingdom is not of this world; what is truth?; not this man, but Barabbas; the purple and the crown of thorns — behold, the man!; Gabbatha — we have no king but Cæsar; the place of a skull, the title in Hebrew, Latin and Greek; woman, behold, thy son; I thirst; it is finished; and the new tomb in the garden."},
    {"module": "ch10", "dir": "chapter-10", "num": "10", "name": "Lovest Thou Me?", "range": "John 20–21", "bible_chapters": [20, 21],
     "blurb": "While it was yet dark, the stone taken away; the linen cloths lying and the napkin rolled up in a place by itself; two angels in white; woman, why weepest thou? — Mary. Rabboni; peace be unto you behind the shut doors; Thomas — my Lord and my God; blessed are they that have not seen, and yet have believed; then the sea of Tiberias at daybreak, the net on the right side, a hundred and fifty and three, the fire of coals; Simon, son of John, lovest thou me? — feed my sheep; follow thou me."},
  ],
}
