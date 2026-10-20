"""2 Chronicles volume, Chapter 8 — Joash (2 Chronicles 22–24). Every verse, word for word from ref/eng-asv.
Ahaziah, whose mother was his counsellor to do wickedly, and the house of Ahab (22:8–9 words over the gate at dawn);
Athaliah destroys the seed royal and Jehoshabeath hides Joash six years in the house of God (2 Kings' drawings); Jehoiada's
covenant in the seventh year — long live the king; treason! treason! (23:15 words over the horses' entry); the house of Baal
broken down; then Joash who did right all the days of Jehoiada — the chest at the gate; Jehoiada's death; Zechariah stoned
in the court (24:21 words over the empty court) — Jehovah look upon it, and require it; the Syrians, and Joash slain on his
bed (24:25 words only)."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from chr2 import G, art as K
from chr2.common import (pack, cp, say, gd, says, gods, caps, drawn, face, joined, cell, cells, roll, JEHOIADA, ATHALIAH, JOASH, ZECHARIAH_P, COLD, GOLDEN, RED)
from chr2 import ch07 as _prev

v, sp = G.v, G.span
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("2CH-C08-00-Title", "Chapter 8 · Joash", title=True)
def title(n):
    svg = shade(f'<g transform="translate(0 260)">{K.child_king("t8", 760, 820, 801)}</g><rect x="0" y="0" width="760" height="262" fill="#8FD0E2"></rect>')
    return chapter_title(8, "第八話", "Joash", "2 Chronicles 22 – 24", svg, "#3A5A7A", v("23:11", frm="Long live the king."), "2 Chronicles · Volume Fourteen")


R = cells(22, 1, 7, "Ahaziah, King of Judah", "#FFD23F", head="Ahaziah", budget=620)
PG.extend(roll(R, "2CH-C08-R", PG.next(), "THE KINGS OF JUDAH · 2 CHRONICLES 22"))
SEGS = [drawn([caps("22:8"), cp("22:9", to="for they said,"), say("22:9", frm="He is the son", to="with all his heart."), cp("22:9", frm="And the house of Ahaziah")], "2CHR 22:8–9",
              lambda w, h: K.gate_dawn(w, h, 802), "#5A5A7A", head="The House of Ahab", stamp=22),
        face([caps("22:10")], "2CHR 22:10", ATHALIAH, bg=RED, head="Athaliah"),
        drawn([caps("22:11-12")], "2CHR 22:11–12", below(lambda w, h: K.hidden_child("hc8", w, h, 803), 0.36), "#3A2A2A", head="Hid in the House of God Six Years"),
        drawn([caps("23:1-2")], "2CHR 23:1–2", below(lambda w, h: K.court_scene("cs8", w, h, 804), 0.4), "#8FD0E2", head="Jehoiada Strengthened Himself", stamp=23),
        face([cp("23:3", to="unto them,"), joined("say", ("23:3", "Behold,"), "23:4")], "2CHR 23:3–4", JEHOIADA),
        face([says("23:5-7")], "2CHR 23:5–7", JEHOIADA),
        drawn([caps("23:8-10")], "2CHR 23:8–10", below(lambda w, h: K.child_king("ck8", w, h, 805), 0.44), "#8FD0E2"),
        drawn([cp("23:11", to="and they said,"), say("23:11", frm="Long live")], "2CHR 23:11", below(lambda w, h: K.child_king("ck8b", w, h, 806), 0.3), "#8FD0E2", head="Long Live the King"),
        drawn([caps("23:12"), cp("23:13", to="and said,"), say("23:13", frm="Treason!")], "2CHR 23:12–13", below(lambda w, h: K.child_king("ck8c", w, h, 807, athaliah=True), 0.44), "#8FD0E2"),
        face([cp("23:14", to="and said unto them,"), say("23:14", frm="Have her forth", to="with the sword:"), cp("23:14", frm="for the priest said,", to="for the priest said,"), say("23:14", frm="Slay her not")],
             "2CHR 23:14", JEHOIADA, bg=RED),
        drawn([caps("23:15")], "2CHR 23:15", lambda w, h: K.horses_entry(w, h, 808), "#5A4A5A"),
        drawn([caps("23:16-17")], "2CHR 23:16–17", below(lambda w, h: K.baal_house("bh8", w, h, 809, broken=True), 0.3), "#5A2A3A"),
        drawn([caps("23:18-19")], "2CHR 23:18–19", below(lambda w, h: K.opening("op8", w, h, 810), 0.4), "#5A4A7A"),
        drawn([caps("23:20-21")], "2CHR 23:20–21", below(lambda w, h: K.judgment_porch("jp8", w, h, 811), 0.4), "#5A2A1E")]
PG.extend(pack(SEGS, "2CH-C08-D", PG.next()))
SEGS2 = [face([caps("24:1-4"), cp("24:5", to="and said to them,"), say("24:5", frm="Go out", to="hasten the matter."), cp("24:5", frm="Howbeit")], "2CHR 24:1–5", JOASH,
               head="To Restore the House of Jehovah", stamp=24),
         face([cp("24:6", to="and said unto him,"), joined("say", ("24:6", "Why hast thou"), "24:7")], "2CHR 24:6–7", JOASH),
         drawn([caps("24:8-10")], "2CHR 24:8–10", below(lambda w, h: K.chest("cs8", w, h, 812), 0.36), "#8FD0E2", head="The Chest at the Gate"),
         drawn([caps("24:11")], "2CHR 24:11", below(lambda w, h: K.chest("cs8b", w, h, 813), 0.36), "#8FD0E2"),
         drawn([caps("24:12-14")], "2CHR 24:12–14", below(lambda w, h: K.repairers("rp8", w, h, 814), 0.44), "#8FD0E2"),
         face([caps("24:15-16")], "2CHR 24:15–16", JEHOIADA, bg=COLD, head="Jehoiada Died"),
         face([caps("24:17-19")], "2CHR 24:17–19", JOASH, bg=RED),
         face([cp("24:20", to="and said unto them,"), say("24:20", frm="Thus saith God,", to="Thus saith God,"), gd("24:20", frm="Why transgress")], "2CHR 24:20", ZECHARIAH_P,
              head="Zechariah the Son of Jehoiada"),
         drawn([caps("24:21"), cp("24:22", to="he said,"), say("24:22", frm="Jehovah look")], "2CHR 24:21–22", lambda w, h: K.court_scene("ct8", w, h, 815, crowd=False), "#5A4A6A"),
         drawn([caps("24:23-24")], "2CHR 24:23–24", lambda w, h: K.K3.burning_city(w, h, 816), "#2A0A0A", head="The Army of the Syrians"),
         drawn([caps("24:25-27")], "2CHR 24:25–27", lambda w, h: K.millo(w, h, 817), "#3A1A2A")]
PG.extend(pack(SEGS2, "2CH-C08-E", PG.next(), end=end_mark("NEXT · AMAZIAH AND UZZIAH", "right: 10px; bottom: 34px")))
