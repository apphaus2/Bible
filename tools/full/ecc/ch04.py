"""Ecclesiastes volume, Chapter 4 — Remember Thy Creator (Ecclesiastes 10–12), the last chapter of Ecclesiastes. Every
verse, word for word from ref/asv. Dead flies in the perfumer's oil; servants upon horses and princes on foot; the pit, the
wall and the serpent, the stones, the wood and the blunt iron as a plate of six cells; the child king; the roof that sinketh
in; a bird of the heavens; bread upon the waters; the clouds and the fallen tree; sowing morning and evening; the light is
sweet; rejoice, O young man; then the darkening of sun and moon, the house whose keepers tremble, the almond-tree, the
silver cord and the golden bowl, the dust returning to the earth and a light going up (God is never drawn); goads and
nails and the books without end; and the end of the matter over a sealed scroll."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from discourse import seg
from ecc import G, art as K
from ecc.common import (paged, face, drawn, say, cp, sg, sgs, PREACHER, PREACHER_GOLD, PREACHER_WARM, PREACHER_STERN, PREACHER_NIGHT, COLD, GOLDEN, DUSK, RED)
from ecc import ch03 as _prev

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ECC-C04-00-Title", "Chapter 4 · Remember Thy Creator", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#8A9AB0"></rect><g transform="translate(0 260)">{K.almond("t4", 760, 820, 401)}</g>')
    return chapter_title(4, "第四話", "Remember Thy Creator", "Ecclesiastes 10 – 12", svg, "#5A6A80", v("12:1", to="in the days of thy youth,"), "Ecclesiastes · Volume Twenty-One")


PAGE = [[drawn("10:1-3", lambda w, h: K.ointment(w, h, 402), "#3A2A2A", head="Dead Flies", stamp=10),
         drawn("10:4-7", lambda w, h: K.servants_horses("sv4", w, h, 403), "#E8C8A0")],
        [drawn("10:8-11", lambda w, h: K.hazards(w, h, 404), "#1A1430"),
         face("10:12-15", PREACHER_STERN, bg=RED)],
        [drawn("10:16-17", lambda w, h: K.child_king("ck4", w, h, 405), "#8A4A26"),
         drawn("10:18-19", lambda w, h: K.leaky_house(w, h, 406), "#4A5A6A")],
        [drawn("10:20", lambda w, h: K.bird_tell(w, h, 407), "#0B0B2A"),
         drawn("11:1-2", lambda w, h: K.bread_waters(w, h, 408), "#8FD0E2", head="Cast Thy Bread upon the Waters", stamp=11)],
        [drawn("11:3-4", lambda w, h: K.clouds_tree("ct4", w, h, 409), "#5A6A7A"),
         drawn("11:5-6", lambda w, h: K.sowers("sw4", w, h, 410), "linear-gradient(90deg, #FFE6A0 0%, #8FD0E2 40%, #8FD0E2 60%, #E8803A 100%)")],
        [drawn("11:7-8", lambda w, h: K.sweet_light(w, h, 411), "#FFB04A"),
         drawn("11:9-10", lambda w, h: K.youth("yt4", w, h, 412), "#8FD0E2", head="Rejoice, O Young Man")],
        [drawn("12:1-2", lambda w, h: K.darkening(w, h, 413), "#2A2A34", head="Remember Thy Creator", stamp=12),
         drawn("12:3-4", lambda w, h: K.old_house("oh4", w, h, 414), "#4A3A5A")],
        [drawn("12:5", lambda w, h: K.almond("am4", w, h, 415), "#8A9AB0"),
         drawn("12:6", lambda w, h: K.silver_cord(w, h, 416), "#1A1430", h=420)],
        [drawn("12:7", lambda w, h: K.dust_spirit(w, h, 417), "#2A2A5A"),
         face("12:8-10", PREACHER, lines=[say("12:8"), cp("12:9"), cp("12:10")], bg=COLD, head="The End of the Matter")],
        [drawn("12:11-12", lambda w, h: K.goads_books(w, h, 418), "#3A2A22"),
         drawn("12:13-14", lambda w, h: K.writing(w, h, 419), "#2A1A2A")]]
PG.extend(paged(PAGE, "ECC-C04-", PG.next(), end=end_mark("END OF ECCLESIASTES · NEXT · THE SONG OF SOLOMON", "right: 10px; bottom: 34px", ch="完")))
