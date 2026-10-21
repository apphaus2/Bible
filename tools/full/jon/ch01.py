"""Jonah volume, Chapter 1 — The Great Fish (Jonah 1–2). Every verse, word for word from ref/asv.
The word of Jehovah to Jonah (the Voice box over Jonah under the night sky); Joppa and the ship of Tarshish; the great
wind upon the sea; the wares cast forth and Jonah asleep in the hold; the shipmaster's words beside his face; the lots on
the deck; the mariners' questions and Jonah's answer, face to face; the men rowing hard; their prayer; the sea calmed
and the ring of the splash; the sacrifice on the ship; the great fish, Jonah inside only a dark shape; his prayer from the
fish's belly in song lines over the deep, the weeds and the bars of the earth; and the dry land. God is never drawn."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from oba.minor import Pages, title, nxt, vista, NIGHT
from jon import G, art as A
from jon.common import K, cp, gd, sg, sy, sgs, JONAH, JONAH_STORM, SHIPMASTER, MARINER, COLD, GOLDEN, RED

v = G.v
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P
STORM = "#14141E"


@P("JON-C01-00-Title", "Chapter 1 · The Great Fish", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#0B1A2E"></rect><g transform="translate(0 280)">{A.deep(760, 800, 101, inside=True)}</g>'
    return title(1, "The Great Fish", "Jonah 1 – 2", svg, "#0B1A2E", v("1:17", to="to swallow up Jonah;"), "Jonah · Volume Thirty-Two")


SEGS = [K.drawn([cp("1:1"), gd("1:2")], lambda w, h: vista(w, h, 102, tone="night", stars=True, hills_n=2, horizon=0.7, people=[(0.5, "prophet", A.JONAH_C)], p="jw1"),
                NIGHT, head="Arise, Go to Nineveh", stamp=1),
        K.drawn([cp("1:3")], lambda w, h: A.joppa("jp1", w, h, 103), "#8FD0E2", head="Unto Tarshish"),
        K.drawn([cp("1:4")], lambda w, h: A.tempest("tp1", w, h, 104), STORM, head="A Mighty Tempest"),
        K.drawn([cp("1:5", to="to lighten it unto them.")], lambda w, h: A.wares("wr1", w, h, 105), STORM),
        K.drawn([cp("1:5", frm="But Jonah")], lambda w, h: A.hold(w, h, 106), "#1A120C"),
        K.face([cp("1:6", to="said unto him,"), sy("1:6", frm="What meanest")], SHIPMASTER, bg=COLD),
        K.drawn([cp("1:7", to="to his fellow,"), sy("1:7", frm="Come,", to="upon us."), cp("1:7", frm="So they cast")], lambda w, h: A.lots(w, h, 107), "#3A2A1E", head="The Lot Fell upon Jonah"),
        K.face([cp("1:8", to="unto him,"), sy("1:8", frm="Tell us")], MARINER, bg=COLD),
        K.face([cp("1:9", to="unto them,"), sy("1:9", frm="I am a Hebrew")], JONAH_STORM, bg=COLD),
        K.face([cp("1:10", to="said unto him,"), sy("1:10", frm="What is this", to="thou hast done?"), cp("1:10", frm="For the men knew"),
                cp("1:11", to="unto him,"), sy("1:11", frm="What shall we do", to="calm unto us?"), cp("1:11", frm="for the sea grew")], MARINER, bg=COLD),
        K.face([cp("1:12", to="unto them,"), sy("1:12", frm="Take me up")], JONAH_STORM, bg=COLD),
        K.drawn([cp("1:13")], lambda w, h: A.tempest("tp2", w, h, 108, crew=5), STORM),
        K.face([cp("1:14", to="and said,"), sy("1:14", frm="We beseech")], SHIPMASTER, bg=COLD),
        K.drawn([cp("1:15")], lambda w, h: A.cast_forth(w, h, 109), "#5A6A8A", head="The Sea Ceased from Its Raging"),
        K.drawn([cp("1:16")], lambda w, h: A.vows("vw1", w, h, 110), "#2A2A5A"),
        K.drawn([cp("1:17")], lambda w, h: A.deep(w, h, 111, inside=True), "#0B2A44", head="Three Days and Three Nights"),
        K.drawn([cp("2:1"), cp("2:2", to="And he said,"), sg("2:2", frm="I called")], lambda w, h: A.deep(w, h, 112, inside=True, weeds=False), "#0B2A44", head="Out of the Fish's Belly", stamp=2),
        K.drawn(sgs("2:3-4"), lambda w, h: A.temple_far(w, h, 113), "#0B2A44"),
        K.drawn(sgs("2:5-6"), lambda w, h: A.bars(w, h, 114), "#03101E"),
        K.drawn(sgs("2:7-9"), lambda w, h: A.deep(w, h, 115, fish_=True, inside=True, light=True), "#0B2A44"),
        K.drawn([cp("2:10")], lambda w, h: A.dry_land("dl1", w, h, 116), "#FFE6A0", head="Upon the Dry Land")]
PG.extend(K.pack(SEGS, "JON-C01-D", PG.next(), end=nxt("NEXT · THAT GREAT CITY")))
