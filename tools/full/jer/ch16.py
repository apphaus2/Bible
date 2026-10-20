"""Jeremiah volume, Chapter 16 — Against the Nations (Jeremiah 46–48). Every verse, word for word from ref/eng-asv.
The word concerning the nations: Egypt at Carchemish by the Euphrates (a map) — prepare ye the buckler and shield; they are
turned backward; Egypt riseth up like the Nile; go up into Gilead, and take balm; Nebuchadrezzar to smite Egypt — Migdol,
Memphis, Tahpanhes and No (a map); Tabor among the mountains; a very fair heifer; hewers of wood and the locusts; fear not, O
Jacob my servant; the Philistines — waters out of the north; O thou sword of Jehovah; then Moab, town by town as maps of the
land beyond the Salt Sea: settled on his lees; Chemosh into captivity; the dove in the rock; the vine of Sibmah; every head
bald; the eagle; fear, and the pit, and the snare; the fire out of Heshbon; yet will I bring back the captivity of Moab."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jer import G, art16 as K
from jer.common import pack, cp, say, gd, says, gods, caps, cut, S, O, jer, GOLDEN, COLD, RED, NIGHT
from jer import ch15 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
W3, G3, S3, C3 = (jer(3, "word"), GOLDEN), (jer(3, "grief"), COLD), (jer(3, "stern"), RED), (jer(3, "calm"), GOLDEN)
MAP = "#0B1A2E"
DES = "#E8A060"
def moab(names, **kw): return (MAP, lambda w, h: K.moab_map(w, h, names, **kw))


@P("JER-C16-00-Title", "Chapter 16 · Against the Nations", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 300)">{K.egypt_army("t16", 760, 780, 1601)}</g><rect x="0" y="0" width="760" height="302" fill="#E8A060"></rect>')
    return chapter_title(16, "第十六話", "Against the Nations", "Jeremiah 46 – 48", svg, "#8A4A2A", v("46:3"), "Jeremiah · Volume Twenty-Four")


SEGS = [S([cp("46:1"), cp("46:2")], "46:1-2", a=(MAP, lambda w, h: K.carchemish_map(w, h)), k=0.3, h=380, head="Of Egypt", stamp=46),
        O("46:3-4", a=(DES, lambda w, h: K.egypt_army("ea16", w, h, 1602)), k=0.3),
        O("46:5-6", a=(DES, lambda w, h: K.egypt_army("ea16b", w, h, 1603, fleeing=True))),
        O("46:7-9", a=("#5A6A8A", lambda w, h: K.nile_rising(w, h, 1604)), head="Egypt Riseth Up like the Nile"),
        O("46:10", t=S3),
        O("46:11-12", a=("#7A9AB8", lambda w, h: K.gilead(w, h, 1605))),
        S([cp("46:13"), gd("46:14")], "46:13-14", a=(MAP, lambda w, h: K.egypt_cities(w, h)), k=0.38, head="Nebuchadrezzar Shall Smite the Land of Egypt"),
        O("46:15-17", t=S3),
        O("46:18-19", a=("#8FB0C8", lambda w, h: K.tabor_carmel(w, h, 1606))),
        O("46:20-21", a=("#8FC0E0", lambda w, h: K.heifer(w, h, 1607)), head="A Very Fair Heifer"),
        O("46:22-24", a=("#C8A070", lambda w, h: K.hewers_forest("hf16", w, h, 1608))),
        O("46:25-26", t=S3),
        O("46:27-28", t=C3, head="Fear Not, O Jacob My Servant"),
        O("47:1", kind="cap", a=(MAP, lambda w, h: K.philistia_map(w, h)), k=0.26, h=360, head="Concerning the Philistines", stamp=47),
        O("47:2-3", a=("#3A3A4A", lambda w, h: K.north_flood(w, h, 1609))),
        O("47:4-5", t=S3),
        O("47:6-7", kind="say", a=("#3A1A2A", lambda w, h: K.sword_still(w, h, 1610)), k=0.38, head="O Thou Sword of Jehovah"),
        O("48:1-2", a=moab(K.MOAB_1), k=0.38, head="Of Moab", stamp=48),
        O("48:3-6", a=moab(("HORONAIM", "LUHITH", "NEBO", "HESHBON"))),
        O("48:7-8", a=("#C8906A", lambda w, h: K.chemosh(w, h, 1611))),
        O("48:9-10", t=S3),
        O("48:11-12", a=("#3A2A22", lambda w, h: K.lees(w, h, 1612)), head="Settled on His Lees"),
        O("48:13-15", t=S3),
        O("48:16-17", t=G3),
        O("48:18-20", a=moab(("DIBON", "AROER", "THE ARNON"))),
        O("48:21-24", a=moab(K.MOAB_2, size=8, box=(35.3, 36.3, 31.15, 32.0)), k=0.4, head="Judgment upon the Plain Country"),
        O("48:25-27", t=S3),
        O("48:28-30", a=("#8FB0C8", lambda w, h: K.dove_rock(w, h, 1613))),
        O("48:31-32", a=("#8A7A6A", lambda w, h: K.sibmah(w, h, 1614)), head="O Vine of Sibmah"),
        O("48:33-34", a=moab(("HESHBON", "ELEALEH", "JAHAZ", "ZOAR", "HORONAIM", "EGLATH-SHELISHIYAH", "NIMRIM"))),
        O("48:35-36", t=G3),
        O("48:37-39", a=("#4A3A4A", lambda w, h: K.bald_mourners("bm16", w, h, 1615))),
        O("48:40-42", a=("#5A6A8A", lambda w, h: K.eagle(w, h, 1616)), head="He Shall Fly as an Eagle"),
        O("48:43-44", a=("#3A2A3A", lambda w, h: K.pit_snares(w, h, 1617)), head="Fear, and the Pit, and the Snare"),
        O("48:45-46", a=("#2A0A0A", lambda w, h: K.heshbon_fire(w, h, 1618))),
        O("48:47", t=C3)]
PG.extend(pack(SEGS, "JER-C16-D", PG.next(), end=end_mark("NEXT · BABYLON IS TAKEN", "right: 10px; bottom: 34px")))
