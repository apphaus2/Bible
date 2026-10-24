"""Matthew volume, Chapter 11 — He Is Risen (Matthew 27–28). Every verse, word for word from ref/eng-asv.
Restraint throughout the passion: Jesus led bound at dawn; Judas' remorse beside his face, the silver scattered on the
sanctuary floor, his death told in words only over the potter's field; Pilate's judgment-seat and the crowd; Pilate's wife
beside her face; the basin of water; the scourging, the scarlet robe, the crown of thorns, the spitting and the blows told in
words only over the empty court with the robe and the reed laid aside; Simon of Cyrene bearing the cross out of the gate;
the crucifixion only as three crosses on the hill against the sky, seen from far off, nothing on them in any detail; the
lots cast at the foot of the hill; the passers-by and the chief priests on the road below; the darkness over all the land
and his last cry and death told in words over the darkened hill; the veil rent, the rocks rent and the tombs open, no one
drawn; the centurion beside his face; the women beholding from afar; Joseph of Arimathaea and the new tomb, the great
stone; the seal and the guard. Then the dawn: the angel of the Lord (white light, gold rim, no face) on the stone rolled
away, the guards fallen; the place where the Lord lay and the linen; Jesus risen in white light, the women at his feet; the
money given to the soldiers; the mountain in Galilee and the eleven."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from mat import G, art11 as A, ch10 as _prev
from mat.common import (K, Pages, drawn, cp, gd, sg, sy, v, title, fin, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_PASSION, JESUS_RISEN, PILATE,
                        PILATE_WIFE, PILATE_TROUBLED, JUDAS_REMORSE, PRIEST, CENTURION, ARIMATHAEA, MAGDALENE, SOLDIER)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MAT-C11-00-Title", "Chapter 11 · He Is Risen", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A3A7A"></rect><g transform="translate(0 300)">{A.stone_rolled("t11", 760, 780, 2801, guards=False)}</g>'
    return title(11, "He Is Risen", "Matthew 27 – 28", svg, "#2A2A5A", v("28:6", to="even as he said."))


def D(lines, fn, bg, **k): return drawn(lines, fn, bg, **{"art_h": 180, "size": 14, **k})
def F(lines, tok=JESUS_PASSION, bg=COLD, **k): return K.face(lines, tok, bg=bg, **k)

SEGS = [D([cp("27:1"), cp("27:2")], lambda w, h: A.bound_dawn("bd1", w, h, 2701), "#2A2A4A", head="Delivered unto Pilate", stamp=27),
        F([cp("27:3"), cp("27:4", to="saying,"), sy("27:4", frm="I have sinned", to="innocent blood.")], JUDAS_REMORSE),
        F([cp("27:4", frm="But they said,", to="But they said,"), sy("27:4", frm="What is that")], PRIEST, bg=RED),
        D([cp("27:5", to="and departed;")], lambda w, h: A.silver_floor("sf1", w, h, 2702), "#3A2A2A"),
        D([cp("27:5", frm="and he went away"), cp("27:6", to="and said,"), sy("27:6", frm="It is not lawful"), cp("27:7"), cp("27:8"), cp("27:9", to="saying,"),
           sg("27:9", frm="And they took"), sg("27:10")], lambda w, h: A.potters_field("pf1", w, h, 2703), "#2A1A2A", head="The Field of Blood"),
        D([cp("27:11", to="saying,"), sy("27:11", frm="Art thou", to="the Jews?"), cp("27:11", frm="And Jesus said", to="said unto him,"), sy("27:11", frm="Thou sayest."),
           cp("27:12")], lambda w, h: A.judgment_seat("js1", w, h, 2704, crowd_=False), "#8FD0E2", head="Art Thou the King of the Jews?"),
        F([cp("27:13", to="unto him,"), sy("27:13", frm="Hearest thou"), cp("27:14")], PILATE, bg=GOLDEN),
        D([cp("27:15"), cp("27:16"), cp("27:17", to="said unto them,"), sy("27:17", frm="Whom will"), cp("27:18")], lambda w, h: A.judgment_seat("js2", w, h, 2705), "#8FD0E2",
          head="Barabbas"),
        F([cp("27:19", to="saying,"), sy("27:19", frm="Have thou nothing")], PILATE_WIFE),
        D([cp("27:20"), cp("27:21", to="said unto them,"), sy("27:21", frm="Which of the two", to="unto you?"), cp("27:21", frm="And they said,", to="And they said,"),
           sy("27:21", frm="Barabbas."), cp("27:22", to="saith unto them,"), sy("27:22", frm="What then", to="called Christ?"), cp("27:22", frm="They all say,", to="They all say,"),
           sy("27:22", frm="Let him be"), cp("27:23", to="And he said,"), sy("27:23", frm="Why, what evil", to="hath he done?"), cp("27:23", frm="But they cried", to="saying,"),
           sy("27:23", frm="Let him be")], lambda w, h: A.judgment_seat("js3", w, h, 2706), "#8FD0E2"),
        D([cp("27:24", to="saying,"), sy("27:24", frm="I am innocent"), cp("27:25", to="and said,"), sy("27:25", frm="His blood")], lambda w, h: A.judgment_seat("js4", w, h, 2707, wash=True),
          "#8FD0E2"),
        D([cp("27:26"), cp("27:27"), cp("27:28"), cp("27:29", to="saying,"), sy("27:29", frm="Hail, King"), cp("27:30"), cp("27:31")], lambda w, h: A.robe_laid("rl1", w, h, 2708), "#5A4A44",
          head="The King of the Jews"),
        D([cp("27:32")], lambda w, h: A.cyrene("cy1", w, h, 2709), "#8A8A9A", head="Golgotha"),
        D([cp("27:33"), cp("27:34"), cp("27:35"), cp("27:36"), cp("27:37"), cp("27:38")], lambda w, h: A.golgotha("gg1", w, h, 2710, lots=True), "#4A3A5A", art_h=260),
        D([cp("27:39"), cp("27:40", to="and saying,"), sy("27:40", frm="Thou that"), cp("27:41"), sy("27:42"), sy("27:43"), cp("27:44")], lambda w, h: A.golgotha("gg2", w, h, 2711, passers=True),
          "#4A3A5A"),
        D([cp("27:45"), cp("27:46", to="saying,"), sy("27:46", frm="Eli, Eli,", to="sabachthani?"), cp("27:46", frm="that is,", to="that is,"), sy("27:46", frm="My God,")],
          lambda w, h: A.golgotha("gg3", w, h, 2712, dark=True), "#05050E", head="Darkness over All the Land"),
        D([cp("27:47", to="said,"), sy("27:47", frm="This man"), cp("27:48"), cp("27:49", to="the rest said,"), sy("27:49", frm="Let be;"), cp("27:50")],
          lambda w, h: A.golgotha("gg4", w, h, 2713, dark=True), "#05050E"),
        D([cp("27:51")], lambda w, h: A.veil_rent("vr1", w, h, 2714), "#1A1018", head="The Veil Rent in Two"),
        D([cp("27:52"), cp("27:53")], lambda w, h: A.tombs_open("to1", w, h, 2715), "#1A1A2A"),
        F([cp("27:54", to="saying,"), sy("27:54", frm="Truly")], CENTURION, bg=GOLDEN),
        D([cp("27:55"), cp("27:56")], lambda w, h: A.women_afar("wa1", w, h, 2716), "#05050E"),
        F([cp("27:57"), cp("27:58")], ARIMATHAEA, head="The Sepulchre"),
        D([cp("27:59"), cp("27:60"), cp("27:61")], lambda w, h: A.new_tomb("nt1", w, h, 2717, women=True), "#2A2A4A"),
        F([cp("27:62"), cp("27:63", to="saying,"), sy("27:63", frm="Sir,"), sy("27:64")], PRIEST, bg=RED),
        F([cp("27:65", to="said unto them,"), sy("27:65", frm="Ye have")], PILATE_TROUBLED),
        D([cp("27:66")], lambda w, h: A.new_tomb("nt2", w, h, 2718, sealed=True, guard=True), "#2A2A4A"),
        # Matthew 28
        D([cp("28:1"), cp("28:2"), cp("28:3"), cp("28:4")], lambda w, h: A.stone_rolled("sr1", w, h, 2801), "#3A3A7A", head="He Is Risen", stamp=28, art_h=260),
        D([cp("28:5", to="unto the women,"), sy("28:5", frm="Fear not ye;"), sy("28:6"), sy("28:7")], lambda w, h: A.stone_rolled("sr2", w, h, 2802, guards=False, women=True), "#3A3A7A"),
        D([cp("28:8")], lambda w, h: A.linen("ln1", w, h, 2803), "#2A2220"),
        D([cp("28:9", to="saying,"), sy("28:9", frm="All hail.", to="All hail."), cp("28:9", frm="And they came"), cp("28:10", to="unto them,"), sy("28:10", frm="Fear not:")],
          lambda w, h: A.met_them("mt1", w, h, 2804), "#5A6A9A", art_h=240),
        D([cp("28:11"), cp("28:12"), cp("28:13", to="saying,"), sy("28:13", frm="Say ye,"), sy("28:14"), cp("28:15")], lambda w, h: A.bribe("br1", w, h, 2805), "#4A3A3A",
          head="The Guard"),
        D([cp("28:16"), cp("28:17")], lambda w, h: A.galilee_mount("gm1", w, h, 2806), "#8FD0E2", head="Lo, I Am with You Always", art_h=260),
        F([cp("28:18", to="saying,"), sy("28:18", frm="All authority"), sy("28:19"), sy("28:20")], JESUS_RISEN, bg=GOLDEN)]
PG.extend(K.pack(SEGS, "MAT-C11-D", PG.next(), most=4, lone=0.5, end=fin("END OF MATTHEW · NEXT · MARK")))
