"""Colossians volume, Chapter 1 — The Image of the Invisible God (Colossians 1–2). Every verse, word for word from
ref/eng-asv. The letter written in Paul's bonds at Rome, Timothy writing (1:1–2); the letter's road from Rome by Brundisium,
Corinth and Ephesus up the Lycus to Colossæ; Epaphras come from Colossæ telling of their love (1:7–8); Paul praying by
lamplight beside his face (1:9–12); out of the power of darkness into the kingdom, a road out of a dark country into the
dawn (1:13–14); the Son, the image of the invisible God, as the light at the centre of all things created — thrones,
dominions, principalities, powers as lights with no form, the things visible about them (a plate, 1:15–17); peace through
the blood of his cross, three crosses far off with the light breaking behind them (1:18–20); Paul reading his letter back in
his bonds (1:24–25); the mystery hid for ages, the sealed chest and the chest opened in light (1:26–27). Colossians 2: the
valley of the Lycus — Laodicea, Hierapolis and Colossæ (2:1–3); rooted and builded up, a tree's roots and a wall going up
(2:6–7); philosophy and vain deceit in the colonnade (2:8); buried with him in baptism, the sealed tomb and the river
(2:11–12); the bond nailed to the cross, a written sheet on a beam, no one on it (2:13–14); the triumph under the arch
(2:15); the shadow and the body as a plate (2:16–17); the head and the body knit together (2:18–19); "handle not, nor
taste, nor touch" beside Paul's stern face."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from col import G, art as A
from col.common import (K, Pages, D, F, glory, lt, lp, lps, v, title, nxt, PAUL, PAUL_LAMP, PAUL_JOY, PAUL_STERN, PAUL_GRIEF, GOLD_BG, LAMP_BG,
                        JOY_BG, STERN_BG, GRIEF_BG)
from php.art import art, wise_disputer, triumph

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("COL-C01-00-Title", "Chapter 1 · The Image of the Invisible God", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#0B1A2E"></rect><g transform="translate(20 380)">{A.cosmic(720, 600, title=False)}</g>'
    return title(1, "The Image of the Invisible God", "Colossians 1–2", svg, "#0B1A2E", v("1:15"), size=76)


SEGS = [
    # Colossians 1 — the letter; the image of the invisible God; the mystery
    D(lp("1:1-2"), art(A.prison_study, "ps1", 5111), "#3A2418", head="Paul and Timothy", sky=1, art_h=300),
    D(lp("1:3-6"), art(A.colossae_road), "#0B1A2E", art_h=250),
    D(lp("1:7-8"), art(A.epaphras_tells, "et1", 5117), "#3A2418", head="Epaphras", art_h=260),
    F(lp("1:9-12"), PAUL_LAMP, bg=LAMP_BG),
    D(lp("1:13-14"), art(A.out_of_darkness, 5113), "#14121E", head="Out of the Power of Darkness", art_h=240),
    D(lp("1:15-17"), art(A.cosmic), "#0B1A2E", head="The Image of the Invisible God", art_h=360),
    D(lp("1:18-20"), art(A.peace_cross, 5118), "#05050E", head="The Head of the Body", art_h=250),
    F(lp("1:21-23"), PAUL),
    D(lp("1:24-25"), art(A.prison_study, "ps2", 5124, stage="prison_read"), "#3A2418", head="In My Sufferings", art_h=250),
    D(lp("1:26-27"), art(A.mystery, 5126), "#0D0D18", head="The Mystery", art_h=250),
    F(lp("1:28-29"), PAUL_JOY, bg=JOY_BG),
    # Colossians 2 — for them at Laodicea; buried with him; the bond nailed to the cross; the shadow and the body
    D(lp("2:1-3"), art(A.lycus_valley, "lv1", 5201), "#8FD0E2", head="For Them at Laodicea", sky=2, art_h=270),
    F(lp("2:4-5"), PAUL),
    D(lp("2:6-7"), art(A.rooted, "rt1", 5206), "#8FD0E2", head="Rooted and Builded Up", art_h=250),
    D([lt("2:8")], art(wise_disputer, "wd1", 5208), "#8FD0E2", head="Philosophy and Vain Deceit", art_h=260),
    F(lp("2:9-10"), PAUL_JOY, bg=JOY_BG),
    D(lp("2:11-12"), art(A.buried_raised, "br1", 5211), "#3A3A7A", head="Buried with Him", art_h=260),
    D(lp("2:13-14"), art(A.bond_nailed, 5213), "#2A1A3A", head="Nailing It to the Cross", art_h=260),
    D([lt("2:15")], art(triumph, "tr1", 5215), "#8FD0E2", head="Triumphing over Them", art_h=270),
    D(lp("2:16-17"), art(A.shadow_body), "#0B1A2E", head="A Shadow of the Things to Come", art_h=260),
    D(lp("2:18-19"), art(A.knit_body, 5218), "#0B1A2E", art_h=270),
    F(lp("2:20-23"), PAUL_STERN, bg=STERN_BG),
]
PG.extend(K.pack(SEGS, "COL-C01-D", PG.next(), end=nxt("NEXT · SEEK THE THINGS THAT ARE ABOVE"), most=2, lone=3))
