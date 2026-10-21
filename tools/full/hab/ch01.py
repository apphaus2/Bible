"""Habakkuk volume, Chapter 1 — The Watchtower (Habakkuk 1–3). Every verse, word for word from ref/asv.
The burden (1:1 in a caption) and Habakkuk's cry beside his face; strife at the gate; Jehovah's answer in the Voice box
over the Chaldeans marching, the horsemen and the eagle, the siege ramp; the second complaint; the net and the fishes;
Habakkuk upon his watchtower; write the vision upon tablets; the cup and the pit; the five woes over the pledges, the
stone crying out of the wall, the sea under the glory, Lebanon felled, the idol and the holy temple; then the prayer of
Habakkuk in song boxes: light behind Teman and Paran, the tents of Cushan, the waters lifting their hands, sun and moon
standing still, the heap of mighty waters, Habakkuk trembling, the barren fig-tree, and the hinds on the high places;
the note after 3:19 (For the Chief Musician …) as a small label.
God is never drawn."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from oba.minor import Pages, title, fin, NIGHT
from hab import G, art as A
from hab.common import K, cp, gd, sg, gds, sgs, HABAKKUK, HABAKKUK_GRIEF, HABAKKUK_TREMBLE, HABAKKUK_GLAD, COLD, GOLDEN, RED, DUSK
import re, asv

def subscription():
    """The note after 3:19 ("For the Chief Musician, on my stringed instruments.", USFM \\d), cut from ref/eng-asv like the
    psalm titles (psa.text) and set as a small label (data-label: asv.Book does not count it as a verse). The Spanish text
    keeps these words inside verse 19 itself, so other languages show nothing here."""
    if asv.LANG != "en": return []
    src = (pathlib.Path(__file__).resolve().parents[3] / "ref" / "eng-asv" / "36-HABeng-asv.usfm").read_text(encoding="utf-8")
    m = re.search(r"^\\d (.*)$", src.split("\\c 3", 1)[1], flags=re.M)
    t = re.sub(r"\\\+?w ([^|\\]*)\|[^\\]*\\\+?w\*", r"\1", m.group(1))
    t = re.sub(r"\s+", " ", re.sub(r"\\[a-z0-9+]+\*?", "", t)).strip()
    return [("raw", f'<div data-label="" style="align-self: flex-end; padding: 4px 10px; background: #F3EFE6; color: #0D0D0F; border: 2px solid #0D0D0F; '
                    f'font-size: 10px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase">{t}</div>')]

v = G.v
PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("HAB-C01-00-Title", "Chapter 1 · The Watchtower", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#1E1650"></rect><g transform="translate(0 280)">{A.watchtower("tw", 760, 800, 101)}</g>'
    return title(1, "The Watchtower", "Habakkuk 1 – 3", svg, "#1E1650", v("2:1", to="set me upon the tower,"), "Habakkuk · Volume Thirty-Five")


SEGS = [K.face([cp("1:1"), sg("1:2")], HABAKKUK_GRIEF, bg=COLD, head="How Long Shall I Cry?", stamp=1),
        K.drawn(sgs("1:3-4"), lambda w, h: A.strife("sf1", w, h, 102), "#6A3A3A"),
        K.drawn(gds("1:5-7"), lambda w, h: A.chaldeans("ch1", w, h, 103), "#8A5A3A", head="I Raise Up the Chaldeans"),
        K.drawn(gds("1:8-9"), lambda w, h: A.horsemen(w, h, 104), "#2A1A3A"),
        K.drawn(gds("1:10-11"), lambda w, h: A.siege_ramp(w, h, 105), "#6A5A5A"),
        K.face(sgs("1:12-13"), HABAKKUK, head="Art Not Thou from Everlasting?"),
        K.drawn(sgs("1:14-17"), lambda w, h: A.net_fishes(w, h, 106), "#5A6A8A"),
        K.drawn(sgs("2:1"), lambda w, h: A.watchtower("wt1", w, h, 107), "#1E1650", head="I Will Stand upon My Watch", stamp=2),
        K.drawn([cp("2:2", to="and said,"), gd("2:2", frm="Write the vision"), gd("2:3")], lambda w, h: A.tablets(w, h, 108), "#3A3A6A", head="Write the Vision"),
        K.drawn(gds("2:4-5"), lambda w, h: A.sheol_cup(w, h, 109), "#2A1A2A"),
        K.drawn(gds("2:6-8"), lambda w, h: A.pledges(w, h, 110), "#3A2A1E", head="Woe to Him"),
        K.drawn(gds("2:9-11"), lambda w, h: A.stone_cries(w, h, 111), "#2A2A4A"),
        K.drawn(gds("2:12-14"), lambda w, h: A.glory_sea(w, h, 112), "#FFD870"),
        K.drawn(gds("2:15-17"), lambda w, h: A.lebanon_felled(w, h, 113), "#5A6A8A"),
        K.drawn(gds("2:18-20"), lambda w, h: A.idol_temple(w, h, 114), "#1A1418", head="Let All the Earth Keep Silence"),
        K.face([cp("3:1"), sg("3:2")], HABAKKUK_GLAD, head="A Prayer of Habakkuk", stamp=3),
        K.drawn(sgs("3:3-5"), lambda w, h: A.teman_glory(w, h, 115), "#2A1A3A"),
        K.drawn(sgs("3:6-7"), lambda w, h: A.cushan(w, h, 116), "#2A2A3A"),
        K.drawn(sgs("3:8-10"), lambda w, h: A.waters_lift(w, h, 117), "#0B0B2A"),
        K.drawn(sgs("3:11-12"), lambda w, h: A.sun_moon(w, h, 118), "#2A3A6A"),
        K.drawn(sgs("3:13-15"), lambda w, h: A.sea_heap(w, h, 119), "#1E1650"),
        K.face(sgs("3:16"), HABAKKUK_TREMBLE, bg=COLD),
        K.drawn(sgs("3:17"), lambda w, h: A.barren(w, h, 120), "#8A7A6A", head="Though the Fig-tree Shall Not Flourish"),
        K.drawn([*sgs("3:18-19"), *subscription()], lambda w, h: A.hinds(w, h, 121), "#3A4A8A")]
PG.extend(K.pack(SEGS, "HAB-C01-D", PG.next(), end=fin("END OF HABAKKUK · NEXT · ZEPHANIAH")))
