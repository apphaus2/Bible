"""Hebrews volume, Chapter 2 — A Priest for Ever after the Order of Melchizedek (Hebrews 5–8). Every verse, word for word
from ref/eng-asv. Hebrews 5: Aaron in the holy garments at the altar of burnt-offering (5:1–3); Aaron and Melchizedek in two
portrait cells (5:4–6, the Voice box: Thou art my Son; Thou art a priest for ever); the garden of olives at night, no one
drawn (5:7–10); milk and solid food (5:11–14). Hebrews 6: the six foundation stones and the walls rising to perfection as a
plate (6:1–3); the hill of the three crosses far off (6:4–6); the field that drank the rain and the field of thorns burning
(6:7–8); the saints at table (6:9–12); Abraham under the stars (6:13–15, the Voice box); the two immutable things as two
seals (6:16–18); the anchor of the soul, its cable passing within the veil (6:19–20). Hebrews 7: Melchizedek come down from
Salem to meet Abraham with bread and wine (7:1–3); the tenth part of all (7:4–7); Levi yet in the loins of his father, a
lineage plate (7:8–10); Levi and Judah (7:11–14); Melchizedek's face in white light (7:15–17); the dawn of a better hope
(7:18–22); the high priests from Aaron, many in number, hindered by death, and the one gold line, for ever (7:23–25); higher
than the heavens (7:26–28). Hebrews 8: the true tabernacle in light above the clouds (8:1–2); the pattern showed in the
mount (8:3–5); the two covenants (8:6–9); the laws in the mind and on the heart (8:10); from the least to the greatest
(8:11–13)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from heb import G, art2 as A, ch01 as _prev
from heb.art import art
from heb.common import K, Pages, D, lt, lp, ltj, lj, sg, gd, sy, gj, sj, v, title, nxt

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("HEB-C02-00-Title", "Chapter 2 · A Priest for Ever after the Order of Melchizedek", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A3A7A"></rect><g transform="translate(0 340)">{A.meeting("t02", 760, 600, 5821)}</g>'
    return title(2, "A Priest for Ever after the Order of Melchizedek", "Hebrews 5–8", svg, "#3A3A7A", v("5:6", frm="Thou art a priest for ever"), size=74)


SEGS = [
    # Hebrews 5 — every high priest; Melchizedek; milk and solid food
    D(lp("5:1-3"), art(A.offering, "of1", 5901), "#8FD0E2", head="Every High Priest", sky=5, art_h=210),
    D([lt("5:4"), lt("5:5", to="spake unto him,"), gd("5:5", frm="Thou art my Son"), lt("5:6", to="another place,"), gd("5:6", frm="Thou art a priest")],
      art(A.called), "#1A2A5A", art_h=210),
    D(lp("5:7-10"), art(A.olive_garden, "og1", 5907), "#05051A", head="In the Days of His Flesh", art_h=200),
    D(lp("5:11-14"), art(A.milk_food, 5911), "#3A2418", head="Milk and Solid Food", art_h=200),
    # Hebrews 6 — press on; the oath; the anchor
    D(lp("6:1-3"), art(A.foundation_plate), "#0B1A2E", head="Press On unto Perfection", sky=6, art_h=220),
    D(lp("6:4-6"), art(A.crosses_far, "cf1", 5914), "#0B0B12", art_h=200),
    D(lp("6:7-8"), art(A.rain_thorns, "rt1", 5917), "#5A7AA0", art_h=210),
    D(lp("6:9-12"), art(A.saints_table, "st1", 5919), "#3A2418", art_h=200),
    D([lt("6:13"), lt("6:14", to="saying,"), gd("6:14", frm="Surely"), lt("6:15")], art(A.oath_stars, "os1", 5923), "#0B0B2A", head="The Promise to Abraham", art_h=220),
    D(lp("6:16-18"), art(A.two_immutable), "#0B1A2E", art_h=210),
    D(lp("6:19-20"), art(A.anchor_veil, "av1", 5929), "#0B1A2E", head="An Anchor of the Soul", art_h=250),
    # Hebrews 7 — Melchizedek; a priest for ever
    D(lp("7:1-3"), art(A.meeting, "me1", 5931), "#3A3A7A", head="Melchizedek, King of Salem", sky=7, art_h=230),
    D(lp("7:4-7"), art(A.tenth), "#0B1A2E", art_h=200),
    D(lp("7:8-10"), art(A.loins), "#0B1A2E", art_h=210),
    D(lp("7:11-14"), art(A.two_tribes), "#0B1A2E", art_h=210),
    D(lp("7:15-16") + [lt("7:17", to="of him,"), gd("7:17", frm="Thou art")], art(A.melchizedek_light), "#3A2A5A", head="A Priest for Ever", art_h=220),
    D(lp("7:18-20") + [lt("7:21", to="saith of him,"), sg("7:21", frm="The Lord sware", to="himself,"), gd("7:21", frm="Thou art a priest for ever"), lt("7:22")],
      art(A.better_hope, 5938), "#2A2A5A", art_h=200),
    D(lp("7:23-25"), art(A.many_priests), "#0B1A2E", head="He Ever Liveth", art_h=270),
    D(lp("7:26-28"), art(A.higher, "hg1", 5946), "#14123A", art_h=210),
    # Hebrews 8 — the true tabernacle; the new covenant
    D(lp("8:1-2"), art(A.true_tabernacle, "tt1", 5951), "#1A1440", head="The True Tabernacle", sky=8, art_h=240),
    D(lp("8:3-4") + [lt("8:5", to="for,"), gd("8:5", frm="See, saith he")], art(A.pattern_mount, "pm1", 5953), "#14123A", art_h=230),
    D(lp("8:6-7") + [lt("8:8", to="he saith,"), gd("8:8", frm="Behold")], art(A.two_covenants), "#0B1A2E", head="A New Covenant", art_h=200),
    D([gd("8:9"), gd("8:10")], art(A.laws_heart), "#0B1A2E", art_h=220),
    D([gd("8:11"), gd("8:12"), lt("8:13")], art(A.least_greatest, "lg1", 5961), "#3A3A7A", art_h=220),
]
PG.extend(K.pack(SEGS, "HEB-C02-D", PG.next(), end=nxt("NEXT · THE WAY INTO THE HOLY PLACE")))
