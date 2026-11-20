"""Shared helpers for the James chapters, and the writers of the general letters that are not Paul's: James, Peter (old),
Silvanus and Mark with him, and Jude. 1 Peter (pe1), 2 Peter (pe2) and Jude (jud) import their faces and looks from here.

Each writer has faces in the epistle kit's five lights, built like epistle.PAUL_* from one base face (the face never
changes, only the light and the brow):
    <W> + GOLD_BG (earnest) · <W>_LAMP + LAMP_BG (by lamplight) · <W>_GRIEF + GRIEF_BG (grieving)
    <W>_JOY + JOY_BG (white light) · <W>_STERN + STERN_BG (warning, rebuke)
  JAMES   the Lord's brother as Acts draws him at Jerusalem (act.common.JAMES_LORD): a white headcloth with a cord, grey hair
          and a grey beard; JAMES is JAMES_LORD itself.
  PETER   ntcast's Peter grown old: the same face and skin, bareheaded, his hair and beard now grey (PETER_OLD and moods).
  JUDE    "brother of James": James' features and skin, a grey-brown beard and hair, a dark slate headcloth with a cord.
  SILVANUS  Acts' Silas (act.common.SILAS): a blue headcloth with a cord, a black beard (1 Pe 5:12, Peter's scribe).
  MARK    Acts' John Mark (act.art7.mark_fig: bareheaded, dark-brown hair, an olive-khaki robe), now a grown man with a short
          dark beard (1 Pe 5:13 "Mark my son").
The writers' standing figures (on epistle.robed) are in jas.art: james_fig, peter_fig, jude_fig, silvanus_fig, mark_r."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
from epistle import (EpistleKit, GOLD_BG, LAMP_BG, GRIEF_BG, JOY_BG, STERN_BG, GLORY_BG, nxt, fin, face_of)
from num.pages import Pages
from act.common import JAMES_LORD, SILAS as SILVANUS

def moods(**base):
    """A writer's five faces from one base face: earnest gold, lamp, grief, joy, stern (as epistle builds Paul's)."""
    return (face_of("adam", **{**base, "light": base.get("light", "#FFC14D")}),
            face_of("adam", **{**base, "skin": "#D49468", "shadow": "#4A2618", "light": "#FF9A3D"}),
            face_of("adam", **{**base, "skin": "#B98A6E", "shadow": "#3A2A3A", "brow": "sorrow", "tear": True, "light": "#9AA8C8"}),
            face_of("adam", **{**base, "skin": "#E3B896", "shadow": "#A87A5A", "light": "#FFFFFF"}),
            face_of("adam", **{**base, "shadow": "#4A2A2A", "brow": "scowl", "light": "#D7261E"}))

# ---- James, the Lord's brother (Acts 15:13, 21:18; Gal 1:19) ---------------------------------------------------------------
_JAMES = dict(skin="#C98E66", shadow="#4A3A4A", hair="#9A948A", hl="#C8C2B6", beard=True, beard_color="#A8A296", scarf="#F3EFE6", cord=True)
_, JAMES_LAMP, JAMES_GRIEF, JAMES_JOY, JAMES_STERN = moods(**_JAMES)
JAMES = JAMES_LORD                                                     # the earnest face is Acts' own
JAMES_LOOK = dict(cloth="#B8B0A0", head="#F3EFE6", cord="#6A5A3A", beard="#A8A296", mantle="#8A8478")

# ---- Peter, old (ntcast.PETER's face, grey) -------------------------------------------------------------------------------
_PETER = dict(skin="#B98A6E", shadow="#5A3A2A", hair="#8E8A84", hl="#C8C4BC", beard=True, beard_color="#A8A49E")
PETER_OLD, PETER_LAMP, PETER_GRIEF, PETER_JOY, PETER_STERN = moods(**_PETER)
PETER_LOOK = dict(cloth="#6A4A2A", hair="#8E8A84", beard="#A8A49E", mantle="#4A3420", belt="#2A1A10")    # ntcast's brown robe

# ---- Jude, brother of James ------------------------------------------------------------------------------------------------
_JUDE = dict(skin="#C98E66", shadow="#4A3A4A", hair="#6A5A4A", hl="#9A8A7A", beard=True, beard_color="#7A6A58", scarf="#3A4452", cord=True)
JUDE, JUDE_LAMP, JUDE_GRIEF, JUDE_JOY, JUDE_STERN = moods(**_JUDE)
JUDE_LOOK = dict(cloth="#6A6458", head="#3A4452", cord="#1A1210", beard="#7A6A58", mantle="#44444C")

# ---- Silvanus and Mark, with Peter at Babylon (1 Pe 5:12–13) ----------------------------------------------------------------
SILVANUS_LOOK = dict(cloth="#2A4A6A", head="#2A4A6A", cord="#1A1210", beard="#2A1A10")
MARK = face_of("adam", skin="#C98E66", shadow="#5A3A2A", hair="#3A2214", hl="#6A5A4E", stubble="#3A2214", light="#FFE680")
MARK_LOOK = dict(cloth="#8A7A4A", hair="#3A2214", beard="#3A2214", mantle="#5A5030")

# ---- James' kit ------------------------------------------------------------------------------------------------------------
from jas import G
CODE = "JAS"
K = EpistleKit(G, CODE, "James", credit="James · Volume Fifty-Nine", fit_faces=True, clip=True)
lt, lts, ltj, lp, lj, sg, sgs, gd, gds, sy, wq, qw = K.lt, K.lts, K.ltj, K.lp, K.lj, K.sg, K.sgs, K.gd, K.gds, K.sy, K.wq, K.qw
D, F, glory, title = K.D, K.F, K.glory, K.title
v, sp = G.v, G.span
