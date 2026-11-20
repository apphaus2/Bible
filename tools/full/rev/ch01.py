"""Revelation volume, Chapter 1 — I Am the Alpha and the Omega (Revelation 1–3). Every verse, word for word from ref/eng-asv.
The Revelation of Jesus Christ given by his angel to his servant John: an angel of light over the sea at dawn and John far
off on the rock of Patmos; John to the seven churches that are in Asia, over the map (Patmos and the seven cities on Acts'
projection, the letters' circuit); he cometh with the clouds — clouds lit from within, the tribes of the earth looking up;
"I am the Alpha and the Omega, saith the Lord God" in the Voice box over the light and the two letters (God is never
drawn). John on the headland of Patmos at evening; the great voice as of a trumpet behind him, John turned toward a burst
of light. The seven golden candlesticks and one like unto a son of man in their midst — Jesus as ntcast draws him, risen,
in blinding white light, the golden girdle at the breasts, the seven stars about his right hand; his white hair, his eyes as
a flame of fire, his feet like burnished brass, the sharp two-edged sword out of his mouth and his face as the sun are in
the words only (never drawn). John fallen at his feet as one dead, the right hand laid upon him; the mystery of the seven
stars and the seven candlesticks as a technical plate. The seven letters, every word in balloons from Jesus (tagged), each
opened under its city with its emblem in a medallion (Ephesus the lampstand, Smyrna the crown of life, Pergamum the white
stone and the hidden manna, Thyatira the morning star, Sardis the white garments, Philadelphia the open door and the key,
Laodicea gold, white garments and eyesalve), and beside his face in light. Restraint: Satan's throne, the synagogue of
Satan, the woman Jezebel and the death of her children are words only; nothing of them is drawn."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from rev import G, art as A
from rev.common import K, Pages, D, F, cp, gd, sg, sy, v, said, title, nxt, JESUS_RISEN, JOHN_OLD, JOHN_AWE, LIGHT_BG, LIGHT_BG_R, PATMOS_BG

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("REV-C01-00-Title", "Chapter 1 · I Am the Alpha and the Omega", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#1A1A4A"></rect><g transform="translate(0 300)">{A.son_of_man("t1", 760, 780, 101)}</g>'
    return title(1, "I Am the Alpha and the Omega", "Revelation 1 – 3", svg, "#1A1A4A", v("1:17", frm="Fear not;"), size=84)


def church(c, seed): return lambda w, h: A.church("c" + c[:3], w, h, seed, c)
C = "christ"

SEGS = [D([cp("1:1"), cp("1:2"), cp("1:3")], lambda w, h: A.patmos("pa1", w, h, 101, "dawn"), "#3A3A7A", head="The Revelation of Jesus Christ", sky=1, art_h=250),
        D([cp("1:4"), cp("1:5"), cp("1:6")], lambda w, h: A.churches_map(w, h), "#0B1A2E", art_h=280),
        D([cp("1:7")], lambda w, h: A.clouds_coming("cc1", w, h, 107), "#2A2A5A", art_h=260),
        D([gd("1:8")], lambda w, h: A.alpha_omega(w, h, 108), "#1A1440", art_h=200),
        D([cp("1:9")], lambda w, h: A.patmos("pa2", w, h, 109, "stand"), "#3A2A5A", head="The Isle That Is Called Patmos", art_h=280),
        D([cp("1:10"), *said("1:11", "saying,", "What thou seest")], lambda w, h: A.patmos("pa3", w, h, 110, "turn"), "#2A2A5A", who="trumpet", art_h=250),
        D([cp("1:12"), cp("1:13")], lambda w, h: A.son_of_man("sm1", w, h, 112), "#1A1A4A", head="One Like unto a Son of Man", art_h=380),
        D([cp("1:14"), cp("1:15"), cp("1:16")], lambda w, h: A.son_of_man("sm2", w, h, 114, "near"), "#1A1A4A", art_h=300),
        D([cp("1:17", to="saying,"), sy("1:17", frm="Fear not;"), sy("1:18")], lambda w, h: A.son_of_man("sm3", w, h, 117, "fallen"), "#1A1A4A", who=C, art_h=260),
        D([sy("1:19"), sy("1:20")], lambda w, h: A.mystery(w, h), "#0B1A2E", who=C, art_h=240),
        D([sy("2:1")], church("ephesus", 201), "#6AB0D8", who=C, head="The Church in Ephesus", sky=2, art_h=260),
        F([sy("2:2"), sy("2:3"), sy("2:4"), sy("2:5")], JESUS_RISEN, bg=LIGHT_BG, who=C),
        D([sy("2:6"), sy("2:7")], lambda w, h: A.paradise(w, h, 207), "#8FD0E2", who=C, art_h=240),
        D([sy("2:8"), sy("2:9")], church("smyrna", 208), "#6AB0D8", who=C, head="The Church in Smyrna", art_h=260),
        D([sy("2:10"), sy("2:11")], lambda w, h: A.crown_life(w, h, 210), "#1A1440", who=C, art_h=220),
        D([sy("2:12"), sy("2:13")], church("pergamum", 212), "#6AB0D8", who=C, head="The Church in Pergamum", art_h=240),
        F([sy("2:14"), sy("2:15"), sy("2:16")], JESUS_RISEN, bg=LIGHT_BG, who=C),
        D([sy("2:17")], lambda w, h: A.white_stone(w, h, 217), "#1A1440", who=C, art_h=220),
        D([sy("2:18"), sy("2:19")], church("thyatira", 218), "#6AB0D8", who=C, head="The Church in Thyatira", art_h=240),
        F([sy("2:20"), sy("2:21"), sy("2:22"), sy("2:23")], JESUS_RISEN, bg=LIGHT_BG, who=C),
        D([sy("2:24"), sy("2:25"), sy("2:26"), sy("2:27"), sy("2:28"), sy("2:29")], lambda w, h: A.morning_star(w, h, 224), "#0B0B2A", who=C, art_h=200),
        D([sy("3:1"), sy("3:2")], church("sardis", 301), "#6AB0D8", who=C, head="The Church in Sardis", sky=3, art_h=240),
        F([sy("3:3"), sy("3:4")], JESUS_RISEN, bg=LIGHT_BG, who=C),
        D([sy("3:5"), sy("3:6")], lambda w, h: A.book_life(w, h, 305), "#1A1440", who=C, art_h=220),
        D([sy("3:7"), sy("3:8")], church("philadelphia", 307), "#6AB0D8", who=C, head="The Church in Philadelphia", art_h=240),
        F([sy("3:9"), sy("3:10"), sy("3:11")], JESUS_RISEN, bg=LIGHT_BG, who=C),
        D([sy("3:12"), sy("3:13")], lambda w, h: A.pillar(w, h, 312), "#E8DCC0", who=C, art_h=230),
        D([sy("3:14"), sy("3:15"), sy("3:16")], church("laodicea", 314), "#6AB0D8", who=C, head="The Church in Laodicea", art_h=240),
        F([sy("3:17"), sy("3:18"), sy("3:19")], JESUS_RISEN, bg=LIGHT_BG, who=C),
        D([sy("3:20")], lambda w, h: A.door("dr1", w, h, 320), "#1E1A4A", who=C, head="I Stand at the Door and Knock", art_h=300),
        D([sy("3:21"), sy("3:22")], lambda w, h: A.throne_light(w, h, 321), "#1A1440", who=C, art_h=260)]
PG.extend(K.pack(SEGS, "REV-C01-D", PG.next(), end=nxt("NEXT · WORTHY IS THE LAMB")))
