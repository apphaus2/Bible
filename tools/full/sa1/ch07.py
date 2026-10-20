"""1 Samuel volume, Chapter 7 — Jehovah Looketh on the Heart (1 Samuel 15–16). Every verse, word for word from ref/eng-asv.
Go and smite Amalek; Saul spares Agag and the best of the flocks; It repenteth me that I have set up Saul; What meaneth this
bleating of the sheep?; to obey is better than sacrifice; the skirt of the robe rent and the kingdom rent from Saul; Agag
(15:33 words over the night: nothing drawn); then Samuel's horn of oil at Beth-lehem, Jesse's sons passing by, the youngest
fetched from the sheep and anointed (the digest's panels); the evil spirit upon Saul, and David with the harp."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from fx import chapter_title, end_mark
from num.pages import Pages
from deu.common import shade
from genesis import art as X
from jos import art as JA
from sa1 import G, art as K
from sa1.common import (pack, say, gd, cp, says, gods, caps, over, face, drawn, D, F, SAUL_KING, SAUL_MAD, SAUL_WEEP, SAMUEL_OLD, SAMUEL_GRIEVED, DAVID, JESSE, ISRAELITE,
                        RED, COLD, GOLDEN)
from sa1 import ch06 as _prev

v, sp = G.v, G.span
AGAG = F("adam", skin="#B98A6E", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#7A3A1A", band=True, light="#FFC14D")
SERVANT = F("adam", skin="#C98E66", shadow="#5A3A2A", hair="#3A2214", hl="#6A5A4E", stubble="#3A2214", light="#FFE680")
ELDER = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#B8B2A6", hl="#8A867E", beard=True, beard_color="#B8B2A6", scarf="#6A5A3A", cord=True, brow="sorrow", sweat=True, light="#9AA8C8")
PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P
NIGHTA = lambda w, h: X.cosmic(w, h)


@P("1SA-C07-00-Title", "Chapter 7 · Jehovah Looketh on the Heart", title=True)
def title(n):
    bg, art = D("B2", 1)
    svg = shade(f'<rect x="0" y="0" width="760" height="1080" fill="#FFC14D"></rect><g transform="translate(0 340)">{art(760, 740)}</g>')
    return chapter_title(7, "第七話", "Jehovah Looketh on the Heart", "1 Samuel 15 – 16", svg, "#FFC14D", v("16:7", frm="for man looketh"), "1 Samuel · Volume Nine")


SEGS = [face([cp("15:1", to="said unto Saul,"), say("15:1", frm="Jehovah sent me"), cp("15:2", to="Thus saith Jehovah of hosts,"), gd("15:2", frm="I have marked"), gd("15:3")], "1SAM 15:1–3",
             SAMUEL_OLD, head="Go and Smite Amalek", stamp=15),
        drawn([caps("15:4-5"), cp("15:6", to="unto the Kenites,"), say("15:6", frm="Go, depart,", to="out of Egypt."), cp("15:6", frm="So the Kenites")], "1SAM 15:4–6",
              lambda w, h: JA.armed("tl7", w, h, 711, tribes=("JUDAH", "BENJAMIN")), "#F3D8A0"),
        drawn([caps("15:7-9")], "1SAM 15:7–9", lambda w, h: K.spoil_flocks(w, h, 712), "#E8C88A"),
        drawn([cp("15:10"), gd("15:11", to="performed my commandments."), cp("15:11", frm="And Samuel was wroth;")], "1SAM 15:10–11", NIGHTA, "#0B0B2A", head="To Obey Is Better than Sacrifice"),
        face([cp("15:12", to="saying,"), say("15:12", frm="Saul came"), cp("15:13", to="said unto him,"), say("15:13", frm="Blessed be")], "1SAM 15:12–13", SAUL_KING),
        drawn([cp("15:14", to="And Samuel said,"), say("15:14", frm="What meaneth"), cp("15:15", to="And Saul said,"), say("15:15", frm="They have brought")], "1SAM 15:14–15",
              lambda w, h: K.spoil_flocks(w, h, 713), "#E8C88A"),
        face([cp("15:16", to="said unto Saul,"), say("15:16", frm="Stay,", to="this night."), cp("15:16", frm="And he said unto him,", to="said unto him,"), say("15:16", frm="Say on."),
              cp("15:17", to="And Samuel said,"), ("say", v("15:17", frm="Though thou") + " " + v("15:18") + " " + v("15:19"))], "1SAM 15:16–19", SAMUEL_GRIEVED, bg=COLD),
        face([cp("15:20", to="unto Samuel,"), ("say", v("15:20", frm="Yea,") + " " + v("15:21"))], "1SAM 15:20–21", SAUL_KING),
        face([cp("15:22", to="And Samuel said,"), ("say", v("15:22", frm="Hath Jehovah") + " " + v("15:23"))], "1SAM 15:22–23", SAMUEL_OLD),
        face([cp("15:24", to="unto Samuel,"), ("say", v("15:24", frm="I have sinned;") + " " + v("15:25"))], "1SAM 15:24–25", SAUL_WEEP, bg=COLD, head="The Kingdom Rent from Thee"),
        face([cp("15:26", to="unto Saul,"), say("15:26", frm="I will not")], "1SAM 15:26", SAMUEL_GRIEVED, bg=COLD),
        drawn([caps("15:27"), cp("15:28", to="said unto him,"), ("say", v("15:28", frm="Jehovah hath rent") + " " + v("15:29"))], "1SAM 15:27–29", lambda w, h: K.rent_skirt(w, h, 714), "#2A1A3A"),
        face([cp("15:30", to="Then he said,"), say("15:30", frm="I have sinned:"), caps("15:31")], "1SAM 15:30–31", SAUL_WEEP, bg=COLD),
        face([cp("15:32", to="Then said Samuel,"), say("15:32", frm="Bring ye", to="Amalekites."), cp("15:32", frm="And Agag came", to="And Agag said,"), say("15:32", frm="Surely")],
             "1SAM 15:32", AGAG),
        drawn([cp("15:33", to="And Samuel said,"), say("15:33", frm="As thy sword", to="among women."), cp("15:33", frm="And Samuel hewed"), caps("15:34-35")], "1SAM 15:33–35", NIGHTA, "#0B0B2A"),
        over([cp("16:1", to="unto Samuel,"), gd("16:1", frm="How long")], "1SAM 16:1", "B1", 0, head="Fill Thy Horn with Oil", stamp=16),
        face([cp("16:2", to="And Samuel said,"), say("16:2", frm="How can I go?", to="kill me."), cp("16:2", frm="And Jehovah said,", to="And Jehovah said,"), gd("16:2", frm="Take a heifer"), gd("16:3")],
             "1SAM 16:2–3", SAMUEL_GRIEVED, bg=COLD),
        face([cp("16:4", to="and said,"), say("16:4", frm="Comest thou"), cp("16:5", to="And he said,"), say("16:5", frm="Peaceably;", to="to the sacrifice."), cp("16:5", frm="And he sanctified")],
             "1SAM 16:4–5", ELDER, bg=COLD),
        over([cp("16:6", to="and said,"), say("16:6", frm="Surely"), cp("16:7", to="unto Samuel,"), gd("16:7", frm="Look not")], "1SAM 16:6–7", "B1", 1, head="Jehovah Looketh on the Heart"),
        face([cp("16:8", to="And he said,"), say("16:8", frm="Neither hath", to="chosen this."), cp("16:9", to="And he said,"), say("16:9", frm="Neither hath"),
              cp("16:10", to="unto Jesse,"), say("16:10", frm="Jehovah hath not")], "1SAM 16:8–10", SAMUEL_OLD),
        over([cp("16:11", to="unto Jesse,"), say("16:11", frm="Are here", to="thy children?"), cp("16:11", frm="And he said,", to="And he said,"), say("16:11", frm="There remaineth", to="the sheep."),
              cp("16:11", frm="And Samuel said unto Jesse, Send", to="unto Jesse,"), say("16:11", frm="Send and fetch")], "1SAM 16:11", "B1", 3),
        face([cp("16:12", to="goodly to look upon."), cp("16:12", frm="And Jehovah said,", to="And Jehovah said,"), gd("16:12", frm="Arise,")], "1SAM 16:12", DAVID, bg=GOLDEN),
        over([caps("16:13")], "1SAM 16:13", "B2", 1),
        face([caps("16:14"), cp("16:15", to="said unto him,"), say("16:15", frm="Behold now,"), says("16:16")], "1SAM 16:14–16", SERVANT, head="The Harp"),
        face([cp("16:17", to="unto his servants,"), say("16:17", frm="Provide me"), cp("16:18", to="and said,"), say("16:18", frm="Behold, I have seen")], "1SAM 16:17–18", SAUL_MAD, bg=RED),
        face([cp("16:19", to="and said,"), say("16:19", frm="Send me"), caps("16:20-21"), cp("16:22", to="saying,"), say("16:22", frm="Let David,")], "1SAM 16:19–22", SAUL_KING),
        over([caps("16:23")], "1SAM 16:23", "B2", 2)]
PG.extend(pack(SEGS, "1SA-C07-D", PG.next(), end=end_mark("NEXT · GOLIATH", "right: 10px; bottom: 34px")))
