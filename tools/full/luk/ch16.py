"""Luke volume, Chapter 16 — Father, Into Thy Hands (Luke 23). Every verse, word for word from ref/eng-asv.
Restraint throughout, as in Matthew and Mark. Before Pilate at the judgment-seat — Art thou the King of the Jews? Thou
sayest; I find no fault in this man; sent to Herod: Herod on his seat, Jesus standing silent before him; the setting at
nought, the mocking and the gorgeous apparel told in words only over Herod's empty hall with the bright robe thrown down;
Herod and Pilate made friends. Barabbas; Crucify, crucify him; chastise him (in words only); delivered up to their will.
Simon of Cyrene bearing the cross; the daughters of Jerusalem bewailing him — weep not for me. The place called The skull
only as three crosses on the hill from far off, nothing on them in any detail; Father, forgive them; the lots; the rulers'
and the soldiers' mocking and the superscription; the two malefactors' words over the hill, never drawn close — To-day
shalt thou be with me in Paradise; the darkness over the whole land and the sun's light failing, the veil rent; Father,
into thy hands I commend my spirit — his death told in words over the darkened hill; the centurion; the multitudes going
home smiting their breasts; the women afar off; Joseph of Arimathæa and the tomb hewn in stone; the women preparing spices.
Luke 23:17 has no text in the ASV."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from luk import G, art13 as A, ch15 as _prev
from luk.common import (K, Pages, D, F, Q, N, S, cp, gd, sg, sy, v, title, nxt, COLD, GOLDEN, RED, NIGHT, JESUS, JESUS_PASSION, PILATE, PILATE_TROUBLED,
                        HEROD, HEROD_MOCK, CAIAPHAS, CENTURION, ARIMATHAEA)

PG = Pages(_prev.START + len(_prev.PAGES) - 1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("LUK-C16-00-Title", "Chapter 16 · Father, Into Thy Hands", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#05050E"></rect><g transform="translate(0 300)">{A.golgotha("t16", 760, 780, 2301, dark=True)}</g>'
    return title(16, "Father, Into Thy Hands", "Luke 23", svg, "#4A3A5A", v("23:46", frm="Father, into thy hands", to="my spirit:"))


SEGS = [D([cp("23:1"), N("23:2", "accuse him, saying,")], lambda w, h: A.judgment_seat("js1", w, h, 2301, crowd_=True), "#8FD0E2", head="I Find No Fault in This Man", sky=23),
        F((q3 := Q("23:3", "c", "asked him, saying,", "s", "the Jews?", "c", "and said,", "s"))[:2], PILATE),
        F(q3[2:], JESUS_PASSION, bg=COLD, ref="LUKE 23:3"),
        F([N("23:4", "the multitudes,")], PILATE),
        F([N("23:5", "urgent, saying,")], CAIAPHAS, bg=RED),
        D([cp("23:6"), cp("23:7")], lambda w, h: A.judgment_seat("js2", w, h, 2306, crowd_=False), "#8FD0E2"),
        D([cp("23:8"), cp("23:9"), cp("23:10")], lambda w, h: A.antipas_hall("ah1", w, h, 2308), "#3A1A3A", head="Herod Set Him at Nought", art_h=240),
        D([cp("23:11")], lambda w, h: A.antipas_hall("ah2", w, h, 2311, stage="robe"), "#3A1A3A", art_h=240),
        F([cp("23:12")], HEROD, bg=RED),
        F([cp("23:13"), N("23:14", "said unto them,"), sy("23:15"), sy("23:16")], PILATE_TROUBLED, bg=COLD, head="Crucify, Crucify Him"),
        D([N("23:18", "all together, saying,"), cp("23:19"), cp("23:20"), N("23:21", "shouted, saying,")], lambda w, h: A.judgment_seat("js3", w, h, 2318), "#8FD0E2"),
        F([N("23:22", "the third time,")], PILATE_TROUBLED, bg=COLD),
        D([cp("23:23"), cp("23:24"), cp("23:25")], lambda w, h: A.judgment_seat("js4", w, h, 2323), "#8FD0E2"),
        D([cp("23:26"), cp("23:27")], lambda w, h: A.cyrene("cy1", w, h, 2326), "#8A8A9A", head="Daughters of Jerusalem"),
        D([N("23:28", "turning unto them said,"), sy("23:29"), sy("23:30"), sy("23:31")], lambda w, h: A.daughters("dt1", w, h, 2328), "#8A8A9A"),
        D([cp("23:32"), cp("23:33")], lambda w, h: A.golgotha("gg1", w, h, 2332), "#4A3A5A", head="The Place Which Is Called The Skull", art_h=240),
        D([Q("23:34", "c", "And Jesus said,", "s", "what they do.", "c")], lambda w, h: A.golgotha("gg2", w, h, 2334, lots=True), "#4A3A5A", art_h=220),
        D([N("23:35", "scoffed at him, saying,"), cp("23:36"), N("23:37", "and saying,"), cp("23:38")], lambda w, h: A.golgotha("gg3", w, h, 2335, passers=True), "#4A3A5A"),
        D([N("23:39", "railed on him, saying,"), N("23:40", "rebuking him said,"), sy("23:41")], lambda w, h: A.golgotha("gg4", w, h, 2339), "#4A3A5A", head="To-day Shalt Thou Be with Me in Paradise"),
        D([N("23:42", "And he said,"), N("23:43", "said unto him,")], lambda w, h: A.golgotha("gg5", w, h, 2342), "#4A3A5A", art_h=240),
        D([cp("23:44"), cp("23:45", to="sun's light failing:")], lambda w, h: A.golgotha("gg6", w, h, 2344, dark=True), "#05050E", head="Father, into Thy Hands", art_h=240),
        D([cp("23:45", frm="and the veil")], lambda w, h: A.veil_rent("vr1", w, h, 2345), "#1A1018", art_h=240),
        D([Q("23:46", "c", "with a loud voice, said,", "s", "my spirit:", "c")], lambda w, h: A.golgotha("gg7", w, h, 2346, dark=True), "#05050E", art_h=260),
        F([N("23:47", "glorified God, saying,")], CENTURION),
        D([cp("23:48"), cp("23:49")], lambda w, h: A.women_afar("wa1", w, h, 2348), "#05050E"),
        F([cp("23:50"), cp("23:51"), cp("23:52")], ARIMATHAEA, head="A Tomb That Was Hewn in Stone"),
        D([cp("23:53"), cp("23:54"), cp("23:55")], lambda w, h: A.new_tomb("nt1", w, h, 2353, women=True), "#2A2A4A", art_h=240),
        D([cp("23:56")], A.footed(lambda w, h: A.spices_prepare("pr1", w, h, 2356), "#3A2E28"), "#5A4048", art_h=280)]
PG.extend(K.pack(SEGS, "LUK-C16-D", PG.next(), most=4, lone=0.5, end=nxt("NEXT · HE IS RISEN")))
