"""The Matthew volume of the full edition: metadata, the volume cover, and the chapter plans (ch01.py, ...).

Built on the minor prophets' kit (oba/minor.py: Kit, vista, page packing). Jesus and the recurring cast come only from
tools/full/ntcast.py (faces JESUS, JESUS_TEACH, JESUS_STERN, JESUS_GRIEF, JESUS_PASSION, JESUS_RISEN; jesus_fig at a distance).
His words are ordinary speech boxes. The Father's voice from heaven is the Voice box over light; the Spirit at the baptism is
a dove of light; an angel of the Lord is a figure of white light with a gold rim and no face (mat.art.angel). The devil is
never drawn: his words stand over the empty wilderness, the pinnacle and the mountain, never beside a face, and Jesus is
alone in every picture of the temptation. Demons are never drawn: the healed are drawn at peace. The scripture Matthew
quotes as fulfilled is set in song boxes (sg), so it stands apart from the narration.

Matthew's own cast (mat.common): Joseph the husband of Mary, a brown beard and an ochre headcloth with a cord (ochre robe at a
distance); Mary from ntcast (blue); the wise-men, one dark-bearded in a purple headcloth, one white-bearded in teal, the third
in red at a distance, on camels; Herod the king, grey-bearded, a purple headcloth with a gold band (his son Herod the tetrarch
is ntcast.HEROD, black-bearded); the chief priests and scribes in white and slate-blue headcloths with bands.

Restraint: Herod's slaughter of the children (2:16) is words only, over Bethlehem's empty street at night with every door
shut; Rachel weeping (2:18) over the empty hills of Ramah; John's death (14:10–11) words over the prison; Judas's death
(27:5) words only over the potter's field; the scourging and the crown of thorns words over the empty court and the purple
robe laid aside; the crucifixion three crosses on the hill against a darkened sky, from a distance; his death words over the
darkened hill and the rent veil; the sealed tomb; the resurrection the stone rolled away, the empty tomb, then Jesus risen in
white light.

Plan (23,397 words, eleven chapters): 1 The Son of David (1–4) · 2 The Sermon on the Mount (5–7) · 3 The Harvest Is
Plenteous (8–10) · 4 Lord of the Sabbath (11–12) · 5 The Kingdom of Heaven Is Like (13–14) · 6 Thou Art the Christ (15–17) ·
7 The First Shall Be Last (18–20) · 8 Hosanna to the Son of David (21–22) · 9 The Son of Man Cometh (23–25) · 10 Gethsemane
(26) · 11 He Is Risen (27–28)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from asv import Book
G = Book("MAT")

META = {
  "id": "matthew", "order": 40, "name": "Matthew", "kanji": "マタイによる福音書", "thumb": "vol-matthew-", "book": "MAT",
  "title": "Matthew Volume", "volume": "Volume Forty",
  "lede": "The fortieth book of the Bible and the first of the New Testament, in full: the book of the generation of Jesus Christ, the wise-men and the star, the voice in the wilderness, the sermon on the mount, the healings and the parables of the kingdom, the transfiguration, the entry into Jerusalem, the last supper and the cross, and the empty tomb — every word in the words of the ASV.",
  "chapters": [
    {"module": "ch01", "dir": "chapter-01", "num": "1", "name": "The Son of David", "range": "Matthew 1–4", "bible_chapters": [1, 2, 3, 4],
     "blurb": "The book of the generation of Jesus Christ, the son of David, the son of Abraham: three times fourteen generations; Joseph's dream — thou shalt call his name JESUS; Immanuel, God with us; the wise-men from the east and the star that stood over the young child; gold and frankincense and myrrh; the flight into Egypt and Rachel weeping for her children; John the Baptist in the wilderness; the heavens opened and the Spirit as a dove — this is my beloved Son; forty days in the wilderness — it is written; and the fishers of men by the sea of Galilee."},
    {"module": "ch02", "dir": "chapter-02", "num": "2", "name": "The Sermon on the Mount", "range": "Matthew 5–7", "bible_chapters": [5, 6, 7],
     "blurb": "He went up into the mountain and opened his mouth and taught them: blessed are the poor in spirit; ye are the salt of the earth, ye are the light of the world; not to destroy, but to fulfil; but I say unto you — love your enemies; when thou prayest, enter into thine inner chamber: Our Father who art in heaven; treasures in heaven; consider the lilies of the field; judge not; ask, and it shall be given you; the narrow gate; by their fruits ye shall know them; and the house built upon the rock."},
  ],
}
