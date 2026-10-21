"""Haggai volume, Chapter 1 — Consider Your Ways (Haggai 1–2). Every verse, word for word from ref/asv.
The word by Haggai in the second year of Darius (captions) beside his face; the ceiled houses and the house lying waste;
the bag with holes; wood from the mountain; the drought; Zerubbabel, Joshua and the remnant obeying and the work begun
(Ezra's walls rising); the former glory as a dashed blueprint over the new walls; be strong — Zerubbabel's face; the
shaking of the nations and the glory filling the house; the priests asked concerning holy flesh and the unclean; the
measures that came to half; the foundation laid and the trees in leaf; the thrones overthrown; and Zerubbabel the signet.
God is never drawn."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from oba.minor import Pages, title, fin, NIGHT
from hag import G, art as A
from hag.common import K, cp, gd, sg, sy, gds, HAGGAI, HAGGAI_STERN, HAGGAI_GOLD, ZERUBBABEL, JESHUA, PRIEST, COLD, GOLDEN, RED, DUSK

v = G.v
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("HAG-C01-00-Title", "Chapter 1 · Consider Your Ways", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A3A6A"></rect><g transform="translate(0 300)">{A.rebuild("tr", 760, 780, 101, people=0.62)}</g>'
    return title(1, "Consider Your Ways", "Haggai 1 – 2", svg, "#3A3A6A", v("1:5", frm="Consider your ways."), "Haggai · Volume Thirty-Seven")


SEGS = [K.face([cp("1:1"), cp("1:2", to="saying,"), gd("1:2", frm="This people")], HAGGAI, head="In the Second Year of Darius", stamp=1),
        K.drawn([cp("1:3"), gd("1:4")], lambda w, h: A.ceiled_waste(w, h, 102), "#8A8A9A", head="This House Lieth Waste"),
        K.drawn([cp("1:5", to="Jehovah of hosts:"), gd("1:5", frm="Consider"), gd("1:6")], lambda w, h: A.bag_holes(w, h, 103), "#C8A880"),
        K.drawn([cp("1:7", to="Jehovah of hosts:"), gd("1:7", frm="Consider"), gd("1:8")], lambda w, h: A.bring_wood("bw1", w, h, 104), "#8FD0E2"),
        K.drawn(gds("1:9-11"), lambda w, h: A.drought(w, h, 105), "#F3E8C8"),
        K.face([cp("1:12"), cp("1:13", to="saying,"), gd("1:13", frm="I am with you")], ZERUBBABEL, head="The People Did Fear before Jehovah"),
        K.drawn([cp("1:14"), cp("1:15")], lambda w, h: A.rebuild("rb1", w, h, 106), "#8FD0E2"),
        K.drawn([cp("2:1"), gd("2:2"), gd("2:3")], lambda w, h: A.former_glory(w, h, 107), "#3A3A6A", head="The Former Glory", stamp=2),
        K.face(gds("2:4-5"), JESHUA, head="Be Strong"),
        K.drawn(gds("2:6-9"), lambda w, h: A.shaking(w, h, 108), "#14143A", head="The Latter Glory of This House"),
        K.drawn([cp("2:10"), cp("2:11", to="Jehovah of hosts:"), gd("2:11", frm="Ask now"), gd("2:12", to="shall it become holy?")], lambda w, h: A.skirt_bread(w, h, 109), "#3A2A22",
                head="Ask Now the Priests"),
        K.face([cp("2:12", frm="And the priests", to="and said,"), sy("2:12", frm="No."), cp("2:13", to="Then said Haggai,"), sy("2:13", frm="If one", to="shall it be unclean?"),
                cp("2:13", frm="And the priests", to="and said,"), sy("2:13", frm="It shall be unclean.")], PRIEST, h=380),
        K.face([cp("2:14", to="and said,"), gd("2:14", frm="So is this people")], HAGGAI_STERN, bg=RED),
        K.drawn(gds("2:15-17"), lambda w, h: A.measures(w, h, 110), "#5A5A6A", head="Consider from This Day"),
        K.drawn(gds("2:18-19"), lambda w, h: A.foundation_bless(w, h, 111), "#5A7AB8"),
        K.drawn([cp("2:20"), gd("2:21"), gd("2:22")], lambda w, h: A.overthrow(w, h, 112), "#14141E", head="As a Signet"),
        K.drawn(gds("2:23"), lambda w, h: A.signet_plate(w, h, 113), "#12113A")]
PG.extend(K.pack(SEGS, "HAG-C01-D", PG.next(), end=fin("END OF HAGGAI · NEXT · ZECHARIAH")))
