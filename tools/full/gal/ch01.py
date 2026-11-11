"""Galatians volume, Chapter 1 — Not from Men (Galatians 1–3). Every verse, word for word from ref/eng-asv.
The letter written: Paul and all the brethren that are with him in the study by lamplight, the scribe on his mat (1:1–2);
the letter's road to the churches of Galatia on Acts' map; Paul stern beside his face at "I marvel" (1:6–7); an angel from
heaven as a figure of white light, the other gospel struck through, the gospel preached sealed and lit (1:8–9). Paul's
gospel not after man: Saul laying waste the church (Acts' night street), the light on the Damascus road (Jesus not drawn),
Arabia's desert and Damascus far off, fifteen days with Cephas, Syria and Cilicia on the map. Galatians 2: Paul, Barnabas
and Titus going up to Jerusalem; Titus not compelled and the false brethren in words beside Paul's stern face; the two
apostleships as a plate; the right hands of fellowship between the pillars; Cephas drawing back from the Gentiles' table at
Antioch, and Paul withstanding him to the face before them all (his words still letter boxes); "I have been crucified with
Christ" beside Paul's face in white light. Galatians 3: "O foolish Galatians" beside his stern face; Paul and Barnabas
preaching in Galatia (Acts' Iconium); Abraham at his tent under the stars; the promise "In thee shall all the nations be
blessed" in the Voice box over the nations on the map; the curse of the law with the scriptures in song boxes; three crosses
on a far hill under a darkened sky (3:13); a man's covenant and the seed as a plate; the 430 years as a timeline; kept in
ward; the law our tutor walking the boy to school; neither Jew nor Greek, bond nor free, male and female, as a plate."""
import sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE.parents[1] / "kit"))
from gal import G, art as A
from gal.common import (K, Pages, D, F, lt, lts, lp, ltj, lj, sg, gd, wq, qw, v, title, nxt, PAUL, PAUL_LAMP, PAUL_STERN, PAUL_JOY, GOLD_BG, LAMP_BG,
                        STERN_BG, JOY_BG)

PG = Pages(1)
START, PAGES, P = PG.start, PG.pages, PG.P


@P("GAL-C01-00-Title", "Chapter 1 · Not from Men", title=True)
def title_page(n):
    svg = f'<rect x="0" y="0" width="760" height="1080" fill="#3A2418"></rect><g transform="translate(0 300)">{A.study_brethren("t01", 760, 640, 4811, fig_h=400)}</g>'
    return title(1, "Not from Men", "Galatians 1–3", svg, "#3A2418", v("2:20", to="Christ liveth in me"))


from gal.art import art

SEGS = [
    # Galatians 1 — the letter, and the gospel not after man
    D([lt("1:1")], art(A.study_brethren, "sb1", 4801), "#3A2418", head="Paul, an Apostle", sky=1, art_h=300),
    D(lp("1:2-5"), art(A.galatia_road), "#0B1A2E", art_h=260),
    F(lp("1:6-7"), PAUL_STERN, bg=STERN_BG, head="A Different Gospel"),
    D(lp("1:8-9"), art(A.angel_gospel, "ag1", 4808), "#0B0B2A", art_h=400),
    F(lp("1:10-12"), PAUL),
    D(lp("1:13-14"), art(A.laid_waste, "lw1", 4813), "#0B0B2A", head="Beyond Measure I Persecuted", art_h=210),
    D(lp("1:15-16"), art(A.damascus_road, "dr1", 4815, fallen=True), "#5AB0D8", art_h=220),
    D([lt("1:17")], art(A.arabia, "ar1", 4817), "#4A2A5A", art_h=220),
    D(lp("1:18-20"), art(A.with_cephas, "wc1", 4818), "#D8C098", head="Fifteen Days with Cephas", art_h=300),
    D(lp("1:21-24"), art(A.syria_cilicia), "#0B1A2E", art_h=200),
    # Galatians 2 — up to Jerusalem; Antioch
    D(lp("2:1-2"), art(A.going_up, "gu1", 4821), "#8FD0E2", head="I Went Up Again to Jerusalem", sky=2, art_h=220),
    F(lp("2:3-5"), PAUL_STERN, bg=STERN_BG),
    D(lp("2:6-8"), art(A.two_apostleships), "#0B1A2E", art_h=230),
    D(lp("2:9-10"), art(A.right_hands, "rh1", 4829), "#8FD0E2", head="The Right Hands of Fellowship", art_h=240),
    D(lp("2:11-13"), art(A.withdrew, "wd1", 4831), "#8FD0E2", head="Cephas at Antioch", art_h=230),
    D([lt("2:14")], art(A.withstood, "ws1", 4834), "#8FD0E2", art_h=240),
    F([ltj("2:15-16")], PAUL),
    D(lp("2:17-19"), art(A.study_brethren, "sb2", 4837, stage="read"), "#3A2418", art_h=250),
    F(lp("2:20-21"), PAUL_JOY, bg=JOY_BG, head="Crucified with Christ"),
    # Galatians 3 — the sons of Abraham; the law our tutor
    F(lp("3:1-3"), PAUL_STERN, bg=STERN_BG, head="O Foolish Galatians"),
    D(lp("3:4-5"), art(A.iconium, "ic1", 4843), "#8FD0E2", sky=3, art_h=220),
    D(lp("3:6-7"), art(A.abraham_stars, "as1", 4846), "#0B0B2A", head="Sons of Abraham", art_h=290),
    D([lt("3:8", to="saying,"), gd("3:8", frm="In thee"), lt("3:9")], art(A.nations_blessed), "#0B1A2E", art_h=250),
    F([lt("3:10", to="for it is written,"), sg("3:10", frm="Cursed is every one who"), lt("3:11", to="is evident: for,"), sg("3:11", frm="The righteous"),
       lt("3:12", to="but,"), sg("3:12", frm="He that doeth")], PAUL, head="Under a Curse"),
    D([lt("3:13", to="for it is written,"), sg("3:13", frm="Cursed is every one that"), lt("3:14")], art(A.far_crosses, 4853), "#0B0B12", art_h=230),
    D(lp("3:15-16"), art(A.covenant_seed), "#0B1A2E", head="A Covenant Confirmed", art_h=240),
    D(lp("3:17-18"), art(A.four_thirty), "#0B1A2E", art_h=240),
    F(lp("3:19-22"), PAUL),
    D([lt("3:23")], art(A.in_ward, "iw1", 4861), "#3A3238", head="Kept in Ward", art_h=230),
    D(lp("3:24-25"), art(A.tutor, "tt1", 4864), "#3A3A7A", head="Our Tutor", art_h=250),
    D(lp("3:26-29"), art(A.one_in_christ), "#0B1A2E", head="One in Christ Jesus", art_h=260),
]
PG.extend(K.pack(SEGS, "GAL-C01-D", PG.next(), end=nxt("NEXT · THE FRUIT OF THE SPIRIT")))
