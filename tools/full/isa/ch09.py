"""Isaiah volume, Chapter 9 — The Desert Shall Blossom (Isaiah 31–35). Every verse, word for word from ref/asv.
Woe to them that go down to Egypt for help (Pharaoh's chariots); as the lion over Zion, as birds hovering; a king shall
reign in righteousness — the shade of a great rock in a weary land; the careless women and the palace forsaken; until the
Spirit be poured upon us from on high; sow beside all waters; woe to thee that destroyest; the highways waste; who among us
can dwell with the devouring fire? — the munitions of rocks; Zion a tent that shall not be removed; the heavens rolled
together as a scroll; the burden upon Edom — 34:2–7 told in words over its red mountains, its streams of pitch and its
beasts; and the desert that blossoms as the rose, the streams in the wilderness, and the way of holiness."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from isa import G, art9 as K
from isa.common import (pack, S, A, face, drawn, night, cp, say, gd, sg, caps, says, gods, sgs, joined,
                        ISAIAH, ISAIAH_STERN, ISAIAH_GRIEF, ISAIAH_JOY, ZION, ZION_JOY, COLD, GOLDEN, RED)
from isa import ch08 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
SKY = "#8FC8E8"


@P("ISA-C09-00-Title", "Chapter 9 · The Desert Shall Blossom", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#7AB8E8"></rect><g transform="translate(0 200)">{K.desert_blossom(760, 880, 901)}</g>')
    return chapter_title(9, "第九話", "The Desert Shall Blossom", "Isaiah 31 – 35", svg, "#3A6A8A", v("35:1"), "Isaiah · Volume Twenty-Three")


SEGS = (
    S("31:1-3", "say", [A(lambda w, h: K.egypt_chariots(w, h, 902), "#E8A050"), ISAIAH_STERN], head="Woe to Them That Go Down to Egypt", split=[3])
    + S("31:4-5", "god", A(lambda w, h: K.lion_zion(w, h, 903), "#8FB0D8"), budget=700)
    + S("31:6-9", "say", [ISAIAH, ISAIAH_STERN], kinds={9: "god"}, split=[8])
    + S("32:1-4", "say", [ISAIAH_JOY], at={2: A(lambda w, h: K.rock_shade("rs9", w, h, 904), "#E8A050")}, split=[3], head="A King Shall Reign in Righteousness")
    + S("32:5-8", "say", ISAIAH_STERN)
    + S("32:9-14", "say", [ISAIAH_STERN], at={13: A(lambda w, h: K.forsaken_palace(w, h, 905), "#8A8AA0")}, head="Ye Women That Are at Ease")
    + S("32:15-18", "say", [A(lambda w, h: K.fruitful(w, h, 906), "#5A7ABA"), ISAIAH_JOY], split=[17])
    + S("32:19-20", "say", A(lambda w, h: K.sow_waters("sw9", w, h, 907), SKY))
    + S("33:1-6", "say", [ISAIAH_STERN, ZION_JOY, ISAIAH], kinds={2: "song"}, split=[2, 3], head="Woe to Thee That Destroyest")
    + S("33:7-9", "say", A(lambda w, h: K.waste_highway(w, h, 908), "#9A8A7A"))
    + S("33:10-13", "god", [ISAIAH_STERN, A(lambda w, h: K.stubble_fire(w, h, 909), "#3A1A1A")], split=[11, 13])
    + S("33:14-16", "say", [ISAIAH, A(lambda w, h: K.munitions(w, h, 910), "#8FB8E0")], split=[16], head="Who Among Us Can Dwell with the Devouring Fire?")
    + S("33:17-19", "say", ISAIAH_JOY)
    + S("33:20-24", "say", [A(lambda w, h: K.zion_tent(w, h, 911), SKY), ISAIAH], split=[22], head="Look upon Zion")
    + S("34:1-3", "say", ISAIAH_STERN, head="Come Near, Ye Nations, to Hear")
    + S("34:4", "say", A(lambda w, h: K.heavens_scroll(w, h, 912), "#05050A"))
    + S("34:5-8", "say", [A(lambda w, h: K.edom_red(w, h, 913), "#3A0A0A"), ISAIAH_STERN], kinds={5: "god"}, split=[7])
    + S("34:9-10", "say", A(lambda w, h: K.edom_pitch(w, h, 914), "#1A0A0A"))
    + S("34:11-17", "say", [A(lambda w, h: K.edom_beasts(w, h, 915), "#3A2A3A"), ISAIAH_STERN, ISAIAH], split=[14, 16])
    + S("35:1-2", "say", A(lambda w, h: K.desert_blossom(w, h, 916), "#7AB8E8"), head="The Desert Shall Rejoice")
    + S("35:3-4", "say", ISAIAH_JOY)
    + S("35:5-7", "say", A(lambda w, h: K.streams_desert(w, h, 917), SKY))
    + S("35:8-10", "say", A(lambda w, h: K.way_holiness("wh9", w, h, 918), "#7AB8E8"), head="The Way of Holiness", budget=700)
)
PG.extend(pack(SEGS, "ISA-C09-D", PG.next(), end=end_mark("NEXT · ON WHOM DOST THOU TRUST?", "right: 10px; bottom: 34px")))
