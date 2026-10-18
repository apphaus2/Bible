"""1 Kings volume, Chapter 14 — Naboth's Vineyard (1 Kings 21–22), the last chapter of 1 Kings. Every verse, word for word
from ref/asv. Naboth's vineyard — Jehovah forbid it me; Ahab on his bed with his face turned away; Jezebel's letters sealed
with the king's seal; the fast and the two base fellows (21:13 words over the vineyard at dusk, nothing drawn of the
stoning); hast thou found me, O mine enemy?; Ahab in sackcloth. Then Jehoshaphat and Ahab at the gate of Samaria; Zedekiah's
horns of iron; Micaiah — I saw all Israel scattered upon the mountains, as sheep that have no shepherd; the lying spirit;
the bread of affliction; the arrow at a venture (22:34–38 words over the chariot at sunset and the empty pool); Jehoshaphat's
reign; and Ahaziah."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from jos.art import below
from kg1 import G, art as K
from kg1.common import (pack, say, gd, cp, says, gods, caps, joined, face, drawn, F, AHAB, AHAB_ANGRY, AHAB_SAD, ELIJAH, ELIJAH_FIRE, JEZEBEL, MICAIAH, JEHOSHAPHAT,
                        MESSENGER, reign, reign_pages, RED, COLD, GOLDEN)
from kg1 import ch13 as _prev

v, sp = G.v, G.span
NABOTH = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#6A645E", hl="#9A948A", beard=True, beard_color="#7A746A", scarf="#6A5A3A", cord=True, brow="scowl", light="#FFC14D")
ZEDEKIAH = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#5A3A6A", cord=True, brow="scowl", light="#D7261E")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHT = "#14123A"


@P("1KI-C14-00-Title", "Chapter 14 · Naboth's Vineyard", title=True)
def title(n):
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#3A2A4A"></rect><g transform="translate(0 340)">{K.vineyard("t14", 760, 740, 1401, empty=True)}</g>')
    return chapter_title(14, "第十四話", "Naboth's Vineyard", "1 Kings 21 – 22", svg, "#3A2A4A", v("21:3", frm="Jehovah forbid it me,"), "1 Kings · Volume Eleven")


SEGS = [drawn([caps("21:1"), cp("21:2", to="saying,"), say("21:2", frm="Give me")], "1KGS 21:1–2", below(lambda w, h: K.vineyard("vy14", w, h, 1402), 0.36), "#8FD0E2", head="Naboth the Jezreelite",
              stamp=21),
        face([cp("21:3", to="to Ahab,"), say("21:3", frm="Jehovah forbid")], "1KGS 21:3", NABOTH),
        drawn([cp("21:4", to="for he had said,"), say("21:4", frm="I will not give", to="my fathers."), cp("21:4", frm="And he laid him down")], "1KGS 21:4",
              below(lambda w, h: K.turned_away("ta14", w, h, 1403), 0.36), "#5A2A1E"),
        face([cp("21:5", to="and said unto him,"), say("21:5", frm="Why is thy spirit"), cp("21:6", to="And he said unto her,"), say("21:6", frm="Because I spake")], "1KGS 21:5–6", AHAB_SAD, bg=COLD),
        face([cp("21:7", to="said unto him,"), say("21:7", frm="Dost thou now")], "1KGS 21:7", JEZEBEL, bg=RED, head="Jezebel"),
        drawn([caps("21:8"), cp("21:9", to="saying,"), joined("say", ("21:9", "Proclaim a fast,"), "21:10")], "1KGS 21:8–10", below(lambda w, h: K.letters(w, h, 1404), 0.42), "#3A1A2A"),
        drawn([caps("21:11-12"), cp("21:13", to="in the presence of the people, saying,"), say("21:13", frm="Naboth did curse", to="the king."), cp("21:13", frm="Then they carried him forth")],
              "1KGS 21:11–13", below(lambda w, h: K.fast("fs14", w, h, 1405), 0.36), "#C8B8A0"),
        drawn([cp("21:14", to="saying,"), say("21:14", frm="Naboth is stoned,"), cp("21:15", to="said to Ahab,"), say("21:15", frm="Arise,"), caps("21:16")], "1KGS 21:14–16",
              lambda w, h: K.vineyard("vy14b", w, h, 1406, empty=True), "#3A2A4A"),
        face([cp("21:17"), gods("21:18"), cp("21:19", to="saying,"), gd("21:19", frm="Thus saith Jehovah,", to="taken possession?"),
              cp("21:19", frm="And thou shalt speak", to="saying,", after="possession?"), gd("21:19", frm="Thus saith Jehovah,", to="even thine.", after="possession?")], "1KGS 21:17–19", ELIJAH, bg=NIGHT,
             head="Hast Thou Found Me, O Mine Enemy?"),
        drawn([cp("21:20", to="to Elijah,"), say("21:20", frm="Hast thou found me,", to="mine enemy?"), cp("21:20", frm="And he answered,", to="And he answered,"), say("21:20", frm="I have found thee,")],
              "1KGS 21:20", below(lambda w, h: K.vineyard("vy14c", w, h, 1407, ahab=True), 0.3), "#8FD0E2"),
        face([joined("say", "21:21", "21:22", "21:23", "21:24")], "1KGS 21:21–24", ELIJAH_FIRE, bg=RED),
        face([caps("21:25-26")], "1KGS 21:25–26", AHAB_ANGRY, bg=RED),
        drawn([caps("21:27"), cp("21:28"), gods("21:29")], "1KGS 21:27–29", below(lambda w, h: K.sackcloth("sk14", w, h, 1408), 0.4), "#5A5A6A"),
        face([caps("22:1-2"), cp("22:3", to="unto his servants,"), say("22:3", frm="Know ye")], "1KGS 22:1–3", AHAB, head="Ramoth-gilead", stamp=22),
        face([cp("22:4", to="And he said unto Jehoshaphat,"), say("22:4", frm="Wilt thou", to="Ramoth-gilead?"), cp("22:4", frm="And Jehoshaphat said", to="king of Israel,"), say("22:4", frm="I am as thou art,"),
              cp("22:5", to="unto the king of Israel,"), say("22:5", frm="Inquire first,")], "1KGS 22:4–5", JEHOSHAPHAT),
        drawn([cp("22:6", to="and said unto them,"), say("22:6", frm="Shall I go", to="forbear?"), cp("22:6", frm="And they said,", to="And they said,"), say("22:6", frm="Go up;"),
               cp("22:7", to="But Jehoshaphat said,"), say("22:7", frm="Is there not")], "1KGS 22:6–7", below(lambda w, h: K.two_thrones_gate("tg14", w, h, 1409), 0.4), "#8FD0E2"),
        face([cp("22:8", to="unto Jehoshaphat,"), say("22:8", frm="There is yet", to="but evil."), cp("22:8", frm="And Jehoshaphat said,", to="And Jehoshaphat said,"), say("22:8", frm="Let not the king"),
              cp("22:9", to="and said,"), say("22:9", frm="Fetch quickly")], "1KGS 22:8–9", AHAB_ANGRY, bg=RED, head="Micaiah the Son of Imlah"),
        drawn([caps("22:10"), cp("22:11", to="and said,"), say("22:11", frm="Thus saith Jehovah,", to="Thus saith Jehovah,"), say("22:11", frm="With these"), cp("22:12", to="saying,"), say("22:12", frm="Go up")],
              "1KGS 22:10–12", below(lambda w, h: K.two_thrones_gate("tg14b", w, h, 1410, horns=True), 0.4), "#8FD0E2"),
        face([cp("22:13", to="saying,"), say("22:13", frm="Behold now,"), cp("22:14", to="And Micaiah said,"), say("22:14", frm="As Jehovah liveth,")], "1KGS 22:13–14", MESSENGER),
        face([cp("22:15", to="the king said unto him,"), say("22:15", frm="Micaiah,", to="forbear?"), cp("22:15", frm="And he answered him,", to="answered him,"), say("22:15", frm="Go up and prosper;"),
              cp("22:16", to="said unto him,"), say("22:16", frm="How many")], "1KGS 22:15–16", AHAB),
        face([cp("22:17", to="And he said,"), say("22:17", frm="I saw all Israel", to="and Jehovah said,"), gd("22:17", frm="These have no master;")], "1KGS 22:17", MICAIAH, bg=COLD,
             head="As Sheep That Have No Shepherd"),
        face([cp("22:18", to="to Jehoshaphat,"), say("22:18", frm="Did I not")], "1KGS 22:18", AHAB_ANGRY, bg=RED),
        drawn([cp("22:19", to="And Micaiah said,"), say("22:19", frm="Therefore hear"), say("22:20", to="And Jehovah said,"), gd("22:20", frm="Who shall entice", to="Ramoth-gilead?"),
               say("22:20", frm="And one said")], "1KGS 22:19–20", lambda w, h: K.heaven_host(w, h, 1411), "#14123A"),
        face([say("22:21", to="and said,"), say("22:21", frm="I will entice him."), say("22:22", to="And Jehovah said unto him,"), gd("22:22", frm="Wherewith?", to="Wherewith?"),
              say("22:22", frm="And he said,", to="all his prophets."), say("22:22", frm="And he said,", to="And he said,", after="prophets."), gd("22:22", frm="Thou shalt entice"), says("22:23")],
             "1KGS 22:21–23", MICAIAH, bg=NIGHT),
        face([cp("22:24", to="and said,"), say("22:24", frm="Which way"), cp("22:25", to="And Micaiah said,"), say("22:25", frm="Behold,")], "1KGS 22:24–25", ZEDEKIAH, bg=RED),
        drawn([cp("22:26", to="And the king of Israel said,"), joined("say", ("22:26", "Take Micaiah,"), "22:27"), cp("22:28", to="And Micaiah said,"), say("22:28", frm="If thou return", to="by me."),
               cp("22:28", frm="And he said,", to="And he said,"), say("22:28", frm="Hear, ye peoples,")], "1KGS 22:26–28", below(lambda w, h: K.prison(w, h, 1412), 0.4), "#3A3438"),
        face([caps("22:29"), cp("22:30", to="unto Jehoshaphat,"), say("22:30", frm="I will disguise", to="thy robes."), cp("22:30", frm="And the king of Israel disguised")], "1KGS 22:29–30", AHAB,
             head="At a Venture"),
        drawn([cp("22:31", to="saying,"), say("22:31", frm="Fight neither"), cp("22:32", to="that they said,"), say("22:32", frm="Surely", to="king of Israel;"), cp("22:32", frm="and they turned aside"),
               caps("22:33")], "1KGS 22:31–33", below(lambda w, h: K.ramoth("rm14", w, h, 1413), 0.3), "#8FD0E2"),
        drawn([cp("22:34", to="unto the driver of his chariot,"), say("22:34", frm="Turn thy hand,"), caps("22:35"), cp("22:36", to="saying,"), say("22:36", frm="Every man")], "1KGS 22:34–36",
              below(lambda w, h: K.ramoth("rm14b", w, h, 1414, dusk=True), 0.34), "#2A1A2A"),
        drawn([caps("22:37-38")], "1KGS 22:37–38", lambda w, h: K.pool_chariot(w, h, 1415), "#3A2A4A")]
PG.extend(pack(SEGS, "1KI-C14-D", PG.next()))
R = [reign("Ahab", "22:39-40", judah=False, head="The Kings of Judah and of Israel"), reign("Jehoshaphat, King of Judah", "22:41-44"), reign("Jehoshaphat", "22:45-47")]
PG.extend(reign_pages(R, "1KI-C14-R", PG.next()))
SEGS2 = [drawn([caps("22:48"), cp("22:49", to="unto Jehoshaphat,"), say("22:49", frm="Let my servants", to="in the ships."), cp("22:49", frm="But Jehoshaphat")], "1KGS 22:48–49",
               below(lambda w, h: K.broken_ships(w, h, 1416), 0.3), "#5A5A6A"),
         drawn([caps("22:50")], "1KGS 22:50", lambda w, h: K.city_dusk("cd14", w, h, 1417), "#2A1A3A"),
         drawn([caps("22:51-53")], "1KGS 22:51–53", below(lambda w, h: K.baal_altar("ba14", w, h, 1418), 0.3), "#5A2A3A", head="Ahaziah")]
PG.extend(pack(SEGS2, "1KI-C14-E", PG.next(), end=end_mark("END OF 1 KINGS · NEXT · 2 KINGS", "right: 10px; bottom: 34px", ch="完")))
