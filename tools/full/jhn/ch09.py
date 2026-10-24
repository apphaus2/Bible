"""John volume, Chapter 9 — It Is Finished (John 18–19). Every verse, word for word from ref/eng-asv.
Restraint throughout, as in Matthew and Mark. Over the brook Kidron by night; the band with lanterns and torches; I am he
— they went backward and fell to the ground, no one struck; Malchus' ear told in words only, the sword lying dropped in
the torchlight, no blood. Annas; the door of the court and the maid; the fire of coals; the officer's blow told in words
only over the shut door; the cock on the wall. The Prætorium in the early morning: Pilate going out to the Jews; within,
Pilate and Jesus alone — My kingdom is not of this world; What is truth?; Barabbas. The scourging, the crown of thorns and
the blows told in words only over the empty court with the purple robe laid aside; Behold, the man! — Jesus far off on the
steps in the purple garment, no wound drawn; Gabbatha; the road to the hill far off, Jesus bearing the cross; three crosses
on the hill against the sky from a distance, nothing on them in detail; the title on its board, its letters not drawn; the
lots cast at the foot of the hill; his mother, her sister, Mary Magdalene and the beloved disciple small at the foot of the
hill; I thirst, It is finished, and the spear told in words over the darkened hill; the scripture in song boxes; Joseph of
Arimathæa and Nicodemus with the linen and the spices at the new tomb in the garden (no body drawn), and the stone."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from jhn import G, art9 as A, ch08 as _prev
from jhn.common import (K, Pages, D, F, S, said, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, NIGHTF, JESUS, JESUS_PASSION, PETER, PETER_GRIEF,
                        MAID, ANNAS, WITNESS, PRIEST, PILATE, PILATE_TROUBLED, PILATE_AFRAID, CAIAPHAS, ARIMATHAEA, NICODEMUS_GRIEF)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("JHN-C09-00-Title", "Chapter 9 · It Is Finished", title=True)
def title_page(n):
    svg = (f'<rect x="0" y="0" width="760" height="1080" fill="#05050E"></rect><g transform="translate(0 200)">{A.dark_hill("t9", 760, 760, 1801)}</g>')
    return title(9, "It Is Finished", "John 18 – 19", svg, "#05050E", v("19:30", frm="It is finished:", to="It is finished:"))


DARK = lambda seed: (lambda w, h: A.dark_hill(f"gd{seed}", w, h, seed))
SEGS = [D([cp("18:1")], lambda w, h: A.kidron("kd1", w, h, 1802), "#05051A", head="Over the Brook Kidron", sky=18, art_h=260),
        D([cp("18:2"), cp("18:3")], lambda w, h: A.arrest("ar1", w, h, 1803), "#05051A", art_h=240),
        D([cp("18:4", to="saith unto them,"), sy("18:4", frm="Whom seek ye?"), cp("18:5", to="They answered him,"), sy("18:5", frm="Jesus of Nazareth.", to="of Nazareth."),
           cp("18:5", frm="Jesus saith", to="unto them,"), sy("18:5", frm="I am he.", to="I am he."), cp("18:5", frm="And Judas also")],
          lambda w, h: A.arrest("ar2", w, h, 1804), "#05051A", head="I Am He"),
        D([cp("18:6")], lambda w, h: A.fell_back("fb1", w, h, 1805), "#05051A", art_h=260),
        D([cp("18:7", to="asked them,"), sy("18:7", frm="Whom seek ye?", to="seek ye?"), cp("18:7", frm="And they said,", to="they said,"), sy("18:7", frm="Jesus of Nazareth.")],
          lambda w, h: A.arrest("ar3", w, h, 1806), "#05051A"),
        F([said("18:8", "Jesus answered,", "I told you"), cp("18:9", to="which he spake,"), sy("18:9", frm="Of those whom")], JESUS_PASSION, bg=COLD),
        D([cp("18:10")], lambda w, h: A.arrest("ar4", w, h, 1807, sword=True), "#05051A", art_h=240),
        F([said("18:11", "said unto Peter,", "Put up")], JESUS_PASSION, bg=COLD),
        D([cp("18:12"), cp("18:13"), cp("18:14")], lambda w, h: A.caiaphas_hall("ch1", w, h, 1808), "#2A1A2A", head="Before Annas"),
        D([cp("18:15"), cp("18:16")], lambda w, h: A.court_door("cd1", w, h, 1809), "#05051A", art_h=240),
        F([cp("18:17", to="saith unto Peter,"), sy("18:17", frm="Art thou also", to="disciples?")], MAID, bg=COLD),
        F([cp("18:17", frm="He saith,", to="He saith,"), sy("18:17", frm="I am not.")], PETER, bg=COLD),
        D([cp("18:18")], lambda w, h: A.court_fire("cf1", w, h, 1810, maid=False), "#05051A", art_h=240),
        F([cp("18:19")], ANNAS, bg=RED),
        F([said("18:20", "Jesus answered him,", "I have spoken"), sy("18:21")], JESUS_PASSION, bg=COLD),
        D([cp("18:22", to="saying,"), sy("18:22", frm="Answerest thou")], lambda w, h: A.shut_door("sd1", w, h, 1811), "#2A2228"),
        F([said("18:23", "Jesus answered him,", "If I have")], JESUS_PASSION, bg=COLD),
        D([cp("18:24"), cp("18:25", to="said therefore unto him,"), sy("18:25", frm="Art thou also", to="his disciples?"), cp("18:25", frm="He denied,", to="and said,"),
           sy("18:25", frm="I am not.")], lambda w, h: A.court_fire("cf2", w, h, 1812, porch=True), "#05051A", head="The Cock Crew"),
        F([cp("18:26", to="saith,"), sy("18:26", frm="Did not I see")], WITNESS, bg=RED),
        D([cp("18:27")], lambda w, h: A.cockcrow("cc1", w, h, 1813), "#1A1A3A", art_h=220),
        D([cp("18:28"), cp("18:29", to="and saith,"), sy("18:29", frm="What accusation")], lambda w, h: A.praetorium("pt1", w, h, 1814), "#5A6A9A", head="The Prætorium",
          art_h=240),
        F([said("18:30", "said unto him,", "If this man")], PRIEST, bg=RED),
        F([cp("18:31", to="said unto them,"), sy("18:31", frm="Take him yourselves,", to="to your law.")], PILATE),
        F([cp("18:31", frm="The Jews said", to="unto him,"), sy("18:31", frm="It is not lawful"), cp("18:32")], PRIEST, bg=RED),
        D([cp("18:33", to="said unto him,"), sy("18:33", frm="Art thou the King")], lambda w, h: A.praetorium("pt2", w, h, 1815, stage="within"), "#B8A888", art_h=240),
        F([said("18:34", "Jesus answered,", "Sayest thou")], JESUS_PASSION, bg=COLD),
        F([said("18:35", "Pilate answered,", "Am I a Jew?")], PILATE),
        F([said("18:36", "Jesus answered,", "My kingdom")], JESUS_PASSION, bg=COLD, head="My Kingdom Is Not of This World"),
        F([cp("18:37", to="said unto him,"), sy("18:37", frm="Art thou a king then?", to="a king then?")], PILATE),
        F([cp("18:37", frm="Jesus answered,", to="Jesus answered,"), sy("18:37", frm="Thou sayest")], JESUS_PASSION, bg=COLD),
        F([cp("18:38", to="saith unto him,"), sy("18:38", frm="What is truth?", to="What is truth?"), cp("18:38", frm="And when he had said", to="saith unto them,"),
           sy("18:38", frm="I find no crime"), sy("18:39")], PILATE_TROUBLED),
        D([cp("18:40", to="saying,"), sy("18:40", frm="Not this man,", to="but Barabbas."), cp("18:40", frm="Now Barabbas")], lambda w, h: A.judgment_seat("js1", w, h, 1816),
          "#8FD0E2"),
        # John 19
        D([cp("19:1"), cp("19:2"), cp("19:3", to="and said,"), sy("19:3", frm="Hail,", to="the Jews!"), cp("19:3", frm="and they struck")],
          lambda w, h: A.purple_laid("pl1", w, h, 1901), "#5A4A44", head="Behold, the Man!", sky=19),
        D([cp("19:4", to="saith unto them,"), sy("19:4", frm="Behold, I bring"), cp("19:5", to="And Pilate saith unto them,"), sy("19:5", frm="Behold, the man!")],
          lambda w, h: A.behold_man("bm1", w, h, 1902), "#8A8A9A", art_h=300),
        F([cp("19:6", to="saying,"), sy("19:6", frm="Crucify him, crucify him!", to="crucify him!")], PRIEST, bg=RED),
        F([cp("19:6", frm="Pilate saith", to="unto them,"), sy("19:6", frm="Take him yourselves,")], PILATE_TROUBLED),
        F([said("19:7", "answered him,", "We have a law,")], CAIAPHAS, bg=RED),
        F([cp("19:8"), cp("19:9", to="saith unto Jesus,"), sy("19:9", frm="Whence art thou?", to="art thou?"), cp("19:9", frm="But Jesus gave")], PILATE_AFRAID),
        F([said("19:10", "saith unto him,", "Speakest thou")], PILATE_AFRAID),
        F([said("19:11", "Jesus answered him,", "Thou wouldest")], JESUS_PASSION, bg=COLD),
        F([cp("19:12", to="saying,"), sy("19:12", frm="If thou release")], CAIAPHAS, bg=RED),
        D([cp("19:13"), cp("19:14", to="saith unto the Jews,"), sy("19:14", frm="Behold, your King!")], lambda w, h: A.judgment_seat("js2", w, h, 1903), "#8FD0E2",
          head="Gabbatha"),
        D([cp("19:15", to="cried out,"), sy("19:15", frm="Away with him,", to="crucify him!"), cp("19:15", frm="Pilate saith", to="unto them,"),
           sy("19:15", frm="Shall I crucify", to="your King?"), cp("19:15", frm="The chief priests answered,", to="answered,"), sy("19:15", frm="We have no king"), cp("19:16")],
          lambda w, h: A.judgment_seat("js3", w, h, 1904), "#8FD0E2"),
        D([cp("19:17")], lambda w, h: A.bearing_cross("bc1", w, h, 1905), "#6A6A7A", head="The Place of a Skull", art_h=260),
        D([cp("19:18")], lambda w, h: A.golgotha("gg1", w, h, 1906), "#4A3A5A", art_h=260),
        D([cp("19:19"), cp("19:20")], lambda w, h: A.title_board("tb1", w, h, 1907), "#4A4A5A", art_h=200),
        F([cp("19:21", to="said to Pilate,"), sy("19:21", frm="Write not,")], PRIEST, bg=RED),
        F([said("19:22", "Pilate answered,", "What I have")], PILATE),
        D([cp("19:23"), cp("19:24", to="one to another,"), sy("19:24", frm="Let us not rend it,", to="whose it shall be:"), cp("19:24", frm="that the scripture", to="which saith,"),
           sg("19:24", frm="They parted")], lambda w, h: A.golgotha("gg2", w, h, 1908, lots=True), "#4A3A5A"),
        D([cp("19:25")], lambda w, h: A.at_cross("ac1", w, h, 1909), "#4A3A5A", head="Behold, Thy Mother", art_h=260),
        D([cp("19:26", to="saith unto his mother,"), sy("19:26", frm="Woman,"), cp("19:27", to="to the disciple,"), sy("19:27", frm="Behold, thy mother!", to="thy mother!"),
           cp("19:27", frm="And from that hour")], lambda w, h: A.at_cross("ac2", w, h, 1910), "#4A3A5A", art_h=240),
        D([cp("19:28", to="saith,"), sy("19:28", frm="I thirst."), cp("19:29")], DARK(1911), "#05050E", head="It Is Finished", art_h=240),
        D([cp("19:30", to="he said,"), sy("19:30", frm="It is finished:", to="It is finished:"), cp("19:30", frm="and he bowed")], DARK(1912), "#05050E", art_h=300),
        D([cp("19:31"), cp("19:32"), cp("19:33")], DARK(1913), "#05050E"),
        D([cp("19:34"), cp("19:35")], DARK(1914), "#05050E", art_h=240),
        D([cp("19:36", to="be fulfilled,"), sg("19:36", frm="A bone"), cp("19:37", to="scripture saith,"), sg("19:37", frm="They shall look")],
          lambda w, h: A.prophecy("pr1", w, h, 1915), "#1A1630"),
        F([cp("19:38")], ARIMATHAEA, head="A New Tomb in the Garden"),
        F([cp("19:39")], NICODEMUS_GRIEF, bg=COLD),
        D([cp("19:40")], lambda w, h: A.burial("bu1", w, h, 1916), "#2A2A4A", art_h=260),
        D([cp("19:41"), cp("19:42")], lambda w, h: A.new_tomb("nt1", w, h, 1917), "#2A2A4A", art_h=260)]
PG.extend(K.pack(SEGS, "JHN-C09-D", PG.next(), end=nxt("NEXT · LOVEST THOU ME?")))
