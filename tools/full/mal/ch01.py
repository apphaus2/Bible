"""Malachi volume, Chapter 1 — The Sun of Righteousness (Malachi 1–4). Every verse, word for word from ref/asv.
The burden (1:1 in a caption) beside Malachi's face; I have loved you — Edom's waste places and the jackals; the blind, the
lame and the sick at the altar; the doors shut; incense from the rising of the sun to its going down; the cold altar and
the curse; the covenant with Levi, the priest teaching; turned aside out of the way; one father, and the foreign god in the
doorway; the altar wet with tears and the wife of thy youth; wearied with words; the way prepared to the lit temple (no one
drawn on it); the refiner's fire and the fullers' soap; the swift witness; will a man rob God? — the store-house empty, then
the windows of heaven opened; the proud built up; the book of remembrance by lamplight; the day burning as a furnace; the sun of
righteousness with healing in its wings; Horeb and the tables; and Elijah the prophet on the road. God is never drawn."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from oba.minor import Pages, title, fin, NIGHT
from mal import G, art as A
from mal.common import K, cp, gd, sg, sy, gds, sgs, MALACHI, MALACHI_STERN, MALACHI_GRIEF, MALACHI_GOLD, COLD, GOLDEN, RED, DUSK

v = G.v
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("MAL-C01-00-Title", "Chapter 1 · The Sun of Righteousness", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A4A8A"></rect><g transform="translate(0 280)">{A.sun_wings(760, 800, 101)}</g>'
    return title(1, "The Sun of Righteousness", "Malachi 1 – 4", svg, "#3A4A8A", v("1:2", to="saith Jehovah."), "Malachi · Volume Thirty-Nine")


SEGS = [K.face([cp("1:1"), gd("1:2")], MALACHI, head="I Have Loved You", stamp=1),
        K.drawn(gds("1:3-5"), lambda w, h: A.edom_waste(w, h, 102), "#2A1A3A"),
        K.drawn(gds("1:6-8"), lambda w, h: A.blemished("bl1", w, h, 103), "#6A4A3A", head="Where Is Mine Honor?"),
        K.drawn(gds("1:9-10"), lambda w, h: A.shut_doors(w, h, 104), "#3A2A3A"),
        K.drawn(gds("1:11"), lambda w, h: A.incense_world(w, h, 105), "#8FB8D8"),
        K.drawn(gds("1:12-14"), lambda w, h: A.blemished("bl2", w, h, 106), "#6A4A3A"),
        K.drawn(gds("2:1-3"), lambda w, h: A.dim_altar(w, h, 107), "#3A3A4A", head="O Ye Priests", stamp=2),
        K.drawn(gds("2:4-7"), lambda w, h: A.levi_teach("lv1", w, h, 108), "#8FB8D8", head="My Covenant with Levi"),
        K.drawn(gds("2:8-9"), lambda w, h: A.turned_aside(w, h, 109), "#6A6A7A"),
        K.face(sgs("2:10-12"), MALACHI_STERN, bg=RED, head="Have We Not All One Father?"),
        K.drawn(sgs("2:13-15"), lambda w, h: A.tears_altar("ta1", w, h, 110), "#2A2A4A"),
        K.drawn([gd("2:16"), sg("2:17")], lambda w, h: A.balances(w, h, 111), "#2A2A3A"),
        K.drawn(gds("3:1"), lambda w, h: A.messenger_way("mw1", w, h, 112), "#2A3A6A", head="Behold, I Send My Messenger", stamp=3),
        K.drawn(gds("3:2-4"), lambda w, h: A.refiner(w, h, 113), "#2A1A14"),
        K.drawn(gds("3:5-6"), lambda w, h: A.balances(w, h, 114), "#2A2A3A"),
        K.drawn(gds("3:7-9"), lambda w, h: A.storehouse("sh1", w, h, 115), "#6A6A7A", head="Will a Man Rob God?"),
        K.drawn(gds("3:10-12"), lambda w, h: A.storehouse("sh2", w, h, 116, full=True), "#5A7AB8", head="The Windows of Heaven"),
        K.drawn(gds("3:13-15"), lambda w, h: A.proud(w, h, 117), "#2A1A3A"),
        K.drawn([cp("3:16"), gd("3:17"), gd("3:18")], lambda w, h: A.remembrance("rm1", w, h, 118), "#1A1430", head="A Book of Remembrance"),
        K.drawn(gds("4:1"), lambda w, h: A.stubble(w, h, 119), "#1A0A0A", head="The Day Cometh", stamp=4),
        K.drawn(gds("4:2-3"), lambda w, h: A.sun_wings(w, h, 120), "#3A4A8A", head="The Sun of Righteousness"),
        K.drawn(gds("4:4"), lambda w, h: A.horeb_law(w, h, 121), "#5A6E8A"),
        K.drawn(gds("4:5-6"), lambda w, h: A.elijah_comes("el1", w, h, 122), "#3A3A6A", head="Elijah the Prophet", h=430)]
PG.extend(K.pack(SEGS, "MAL-C01-D", PG.next(), end=fin("END OF MALACHI · NEXT · MATTHEW")))
