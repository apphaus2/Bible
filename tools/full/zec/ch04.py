"""Zechariah volume, Chapter 4 — The Day of Jehovah (Zechariah 12–14). Every verse, word for word from ref/asv.
Jerusalem a cup of reeling and a burdensome stone amid the camps of the nations; the horses in terror; the pan of fire and
the torch among sheaves; the tents of Judah; they shall look unto me whom they have pierced — the great mourning, every
family apart, in the valley of Megiddon; a fountain opened; the idols cut off and the hairy mantle laid aside (13:3 words
only); smite the shepherd — the sheep scattered and the third refined as silver (13:8 words only); the day of Jehovah: the
city taken (14:2 words over the gate and the smoke), the mount of Olives cleft with light in the cleft (God never drawn),
at evening time light, living waters to the two seas, Jerusalem lifted up (a plan of her gates), the camps of the nations
emptied by the plague (14:12–15 words only), the feast of tabernacles, no rain on Egypt, and HOLY UNTO JEHOVAH upon the
bells of the horses."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from oba.minor import Pages, title, fin, NIGHT
from zec import G, art4 as A, ch03 as _prev
from zec.common import K, cp, gd, sg, sy, gds, sgs, ZECHARIAH, ZECH_GOLD, COLD, GOLDEN, RED, DUSK

v = G.v
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("ZEC-C04-00-Title", "Chapter 4 · The Day of Jehovah", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#1A1030"></rect><g transform="translate(0 280)">{A.olives_cleft(760, 800, 401)}</g>'
    return title(4, "The Day of Jehovah", "Zechariah 12 – 14", svg, "#1A1030", v("14:9", to="King over all the earth:"), "Zechariah · Volume Thirty-Eight")


SEGS = [K.drawn([cp("12:1", to="concerning Israel."), cp("12:1", frm="Thus saith Jehovah,"), gd("12:2")], lambda w, h: A.camps_round(w, h, 402), "#2A1A3A",
                head="A Cup of Reeling", stamp=12),
        K.drawn(gds("12:3"), lambda w, h: A.camps_round(w, h, 403, stone=True), "#2A1A3A"),
        K.drawn([gd("12:4"), gd("12:5")], lambda w, h: A.terror(w, h, 404), "#F3EFE6"),
        K.drawn(gds("12:6"), lambda w, h: A.pan_torch(w, h, 405), "#1A0A0A"),
        K.drawn(gds("12:7-9"), lambda w, h: A.tents_judah(w, h, 406), "#3A3A6A"),
        K.drawn(gds("12:10-11"), lambda w, h: A.mourning("mn1", w, h, 407), "#4A4A5A", head="Whom They Have Pierced"),
        K.drawn(gds("12:12-14"), lambda w, h: A.mourning("mn2", w, h, 408), "#4A4A5A")]
PG.extend(K.pack(SEGS, "ZEC-C04-D", PG.next()))
SEGS2 = [K.drawn(gds("13:1"), lambda w, h: A.fountain(w, h, 409), "#2A3A6A", head="A Fountain Opened", stamp=13, h=340),
         K.drawn(gds("13:2-3"), lambda w, h: A.idols_mantle(w, h, 410), "#8FB8D8"),
         K.drawn(gds("13:4-6"), lambda w, h: A.vista(w, h, 419, tone="day", hills_n=2, horizon=0.5, field="grain", people=[(0.62, "man", "#6A5A3A", True)], p="tl1"), "#8FB8D8"),
         K.drawn(gds("13:7-9"), lambda w, h: A.scattered_refine(w, h, 411), "#3A2A3A", head="Smite the Shepherd")]
PG.extend(K.pack(SEGS2, "ZEC-C04-E", PG.next()))
SEGS3 = [K.drawn([sg("14:1"), gd("14:2")], lambda w, h: A.spoil_gate(w, h, 412), "#3A1A1A", head="Behold, a Day of Jehovah Cometh", stamp=14),
         K.drawn(sgs("14:3-5"), lambda w, h: A.olives_cleft(w, h, 413, flee=True), "#1A1030", head="Upon the Mount of Olives"),
         K.drawn(sgs("14:6-7"), lambda w, h: A.evening_light(w, h, 414), "#0B0B14"),
         K.drawn(sgs("14:8-9"), lambda w, h: A.living_waters(w, h), "#0B1A2E", head="Living Waters"),
         K.drawn(sgs("14:10-11"), lambda w, h: A.gates_plan(w, h), "#0B1A2E"),
         K.drawn(sgs("14:12-15"), lambda w, h: A.empty_camps(w, h, 415), "#3A3A3A"),
         K.drawn(sgs("14:16-17"), lambda w, h: A.tabernacles("tb1", w, h, 416), "#5A7AB8", head="The Feast of Tabernacles"),
         K.drawn(sgs("14:18-19"), lambda w, h: A.no_rain(w, h, 417), "#F3E8C8"),
         K.drawn(sgs("14:20-21"), lambda w, h: A.bells(w, h, 418), "#12113A", head="Holy unto Jehovah")]
PG.extend(K.paged([SEGS3[0:2], SEGS3[2:5], SEGS3[5:7], SEGS3[7:9]], "ZEC-C04-F", PG.next(), end=fin("END OF ZECHARIAH · NEXT · MALACHI")))
