"""Shared helpers for the Colossians chapters: the letter's kit (epistle.EpistleKit with face panels sized to their words and
drawings clipped to their panels), its line builders and panels, Paul's faces (from epistle), and the cast of the prison
letters as Philippians defines them (php.common) — Timothy, Epaphras, Tychicus, Onesimus, Aristarchus, Mark, Justus, Luke,
Demas, Archippus — each the same in Philippians, Colossians and Philemon."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import (EpistleKit, PAUL, PAUL_LAMP, PAUL_GRIEF, PAUL_JOY, PAUL_STERN, GUARD, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG, GLORY_BG,
                     nxt, fin, face_of, greetings, face_portrait)
from num.pages import Pages
from col import G
from php.common import (TIMOTHY, EPAPHRAS, TYCHICUS, ONESIMUS, ARISTARCHUS, MARK, JUSTUS, LUKE, DEMAS, ARCHIPPUS, PHILEMON, APPHIA)

CODE = "COL"
K = EpistleKit(G, CODE, "Colossians", credit="Colossians · Volume Fifty-One", fit_faces=True, clip=True)
lt, lts, ltj, lp, lj, sg, sgs, gd, gds, sy, wq, qw = K.lt, K.lts, K.ltj, K.lp, K.lj, K.sg, K.sgs, K.gd, K.gds, K.sy, K.wq, K.qw
D, F, glory, title = K.D, K.F, K.glory, K.title
v, sp = G.v, G.span

def lps(*refs, most=280):
    """Paragraphs across a chapter break: lps("3:22-25", "4:1") (K.lp keeps to one chapter)."""
    return [x for r in refs for x in lp(r, most=most)]
