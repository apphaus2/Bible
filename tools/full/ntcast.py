"""The New Testament cast, shared by every New Testament volume so each person looks the same in every book.

Jesus is drawn as a man like everyone else, always the same: a first-century Galilean with olive-brown skin, shoulder-length
dark-brown hair, a short dark-brown beard, an undyed off-white robe and a blue-grey mantle over one shoulder, a soft gold glow
and no halo. His words are ordinary speech balloons (`say`). The Father is never drawn: the voice from heaven is the Voice box
over light or sky. The Holy Spirit at the baptism is a dove of light. Angels are figures of white light with a gold rim (no
faces), as in the Old Testament volumes.

Faces (for discourse.seg tok=): JESUS (calm, gold light) · JESUS_TEACH · JESUS_STERN (the temple, the Pharisees) · JESUS_GRIEF
(Lazarus, Jerusalem, Gethsemane) · JESUS_PASSION (the trial and the cross: sorrow, cold light, no wounds drawn) · JESUS_RISEN
(white light). At a distance: jesus_fig(p, x, y, s, flip=False, up=None) — needs mk.defs(p, *num.art.ALL) in the panel.

Restraint for the passion: the scourging and the crown of thorns are words over the empty court and the purple robe laid aside;
the crucifixion is three crosses on the hill against the darkened sky, seen from a distance (never close, no wounds or blood);
his death is words over the darkened hill and the rent veil; the burial is the sealed tomb. The resurrection is the stone rolled
away, the empty tomb and the folded linen, then Jesus risen in white light among the disciples. Demons are never drawn: the
healed person at peace, the swine running down the steep."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "kit"))
import mk
from faces_ex import F
from exo.art import headcloth, WHITE_BEARD, BLACK_BEARD

JESUS_SKIN, JESUS_SHADOW, JESUS_HAIR, JESUS_HL = "#B9825E", "#6E4630", "#3A2416", "#6A4A34"
JESUS_TUNIC, JESUS_MANTLE = "#E8E0CC", "#5E7488"
# shoulder-length hair falling behind the ear to the shoulder (on the 400x400 face)
_LONG = ('\n<path d="M232 102 C 228 70 206 46 170 42 C 126 38 98 70 96 118 C 94 168 102 226 112 286 C 118 300 140 306 156 298 '
         'C 150 262 146 222 150 190 C 154 160 166 134 186 120 C 204 110 220 104 232 102 Z" fill="%s" stroke="#0D0D0F" stroke-width="2"></path>'
         '\n<g fill="none" stroke="%s" stroke-width="1.6" stroke-linecap="round"><path d="M120 120 C 116 170 120 230 128 286"></path>'
         '<path d="M140 110 C 132 160 134 220 142 290"></path><path d="M180 60 C 150 66 126 86 116 116"></path></g>')
def _j(**k):
    base = dict(skin=JESUS_SKIN, shadow=JESUS_SHADOW, hair=JESUS_HAIR, hl=JESUS_HL, beard=True, beard_color=JESUS_HAIR)
    base.update(k)
    return F("adam", **base) + _LONG % (JESUS_HAIR, JESUS_HL)

JESUS = _j(light="#FFE680")
JESUS_TEACH = _j(light="#FFF4C2")
JESUS_STERN = _j(brow="scowl", light="#D7261E")
JESUS_GRIEF = _j(brow="sorrow", tear=True, light="#9AA8C8")
JESUS_PASSION = _j(skin="#A87458", shadow="#4A2E2A", brow="sorrow", light="#8A90B0")
JESUS_RISEN = _j(skin="#D6A27E", shadow="#8A6040", light="#FFFFFF")

_HAIR_FIG = ('<path d="M-13.5 -186 C -16 -205 16 -205 13.5 -186 L 14.5 -163 C 12.5 -159 10 -160 9.5 -164 L 9.5 -186 C 6 -195 -6 -195 -9.5 -186 L -9.5 -164 '
             f'C -10 -160 -12.5 -159 -14.5 -163 Z" fill="{JESUS_HAIR}" stroke="#0D0D0F" stroke-width="1.3"></path>')
_BEARD_FIG = BLACK_BEARD.split("</path>")[0].replace("#2A1A10", JESUS_HAIR) + "</path>"
_MANTLE = (f'<path d="M-24 -160 C -10 -150 10 -120 22 -60 L 30 -62 C 26 -110 22 -150 18 -164 C 4 -170 -14 -168 -24 -160 Z" fill="{JESUS_MANTLE}" '
           'stroke="#0D0D0F" stroke-width="2"></path>')
def jesus_fig(p, x, y, s, flip=False, up=None, glow=True):
    """Jesus at a distance: undyed robe, blue-grey mantle over the shoulder, dark hair to the shoulders, dark beard, and a soft
    gold glow behind him (glow=False to leave it off)."""
    halo = (f'<circle cx="{x:.1f}" cy="{y - 150 * s:.1f}" r="{70 * s:.1f}" fill="#FFE680" opacity="0.18"></circle>' if glow else "")
    return halo + mk.person(p, round(x), round(y), round(s, 3), body=JESUS_SKIN, cloth=JESUS_TUNIC, kind="Robe", sw=3, flip=flip, up=up,
                            extra=_MANTLE + _HAIR_FIG + _BEARD_FIG)

# the disciples and the others who recur across the Gospels and Acts
PETER = F("adam", skin="#B98A6E", shadow="#5A3A2A", hair="#2A2420", hl="#6A645E", beard=True, beard_color="#4A4440", light="#FFC14D")
PETER_GRIEF = F("adam", skin="#A87A5E", shadow="#3A2A3A", hair="#2A2420", hl="#6A645E", beard=True, beard_color="#4A4440", brow="sorrow", tear=True, light="#9AA8C8")
ANDREW = F("adam", skin="#B98A6E", shadow="#5A3A2A", hair="#3A2A1A", hl="#6A5A4A", beard=True, beard_color="#3A2A1A", scarf="#6A7A5A", cord=True, light="#FFC14D")
JAMES = F("adam", skin="#C98E66", shadow="#5A3A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#8A5A3A", cord=True, light="#FFC14D")
JOHN = F("adam", skin="#D9A27A", shadow="#7A4A3A", hair="#2A1A10", hl="#5A4A3E", light="#FFE680")
MATTHEW = F("adam", skin="#C98E66", shadow="#4A3A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#3A5A6A", band=True, light="#FFC14D")
THOMAS = F("adam", skin="#B98A6E", shadow="#4A3A4A", hair="#2A1A10", hl="#4A3A2E", stubble="#2A1A10", scarf="#5A4A6A", cord=True, brow="sorrow", light="#9AA8C8")
PHILIP = F("adam", skin="#C98E66", shadow="#5A3A2A", hair="#3A2214", hl="#6A5A4E", stubble="#3A2214", light="#FFC14D")
JUDAS = F("adam", skin="#B98A6E", shadow="#3A2A2A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#6A2A1A", cord=True, brow="scowl", light="#8A5A3A")
MARY = F("eve", skin="#C98E66", shadow="#6A4A3A", hair="#2A1A10", scarf="#2A4A7A", light="#FFE680")
MARY_GRIEF = F("eve", skin="#B98A6E", shadow="#3A2A3A", hair="#2A1A10", scarf="#2A4A7A", brow="sorrow", tear=True, light="#9AA8C8")
MAGDALENE = F("eve", skin="#C98E66", shadow="#5A3A3A", hair="#3A1E14", scarf="#8A2A3A", light="#FFE680")
MARTHA = F("eve", skin="#C98E66", shadow="#5A3A3A", hair="#2A1A10", scarf="#8A6A2A", light="#FFC14D")
BAPTIST = F("adam", skin="#9A6A4A", shadow="#4A2A1A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", brow="scowl", light="#FFC14D")
PHARISEE = F("adam", skin="#C98E66", shadow="#4A3A4A", hair="#6A645E", hl="#9A948A", beard=True, beard_color="#6A645E", scarf="#E8E2D6", band=True, brow="scowl", light="#FFC14D")
CAIAPHAS = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#F3EFE6", band=True, brow="scowl", light="#D7261E")
PILATE = F("adam", skin="#E3B08A", shadow="#8A5A4A", hair="#4A3A2A", hl="#7A6A5A", light="#FFC14D")
HEROD = F("adam", skin="#C98E66", shadow="#4A2A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#5A1A4A", band=True, light="#D7261E")
# a Roman's brass helmet over the face (on the 400x400 face): the bowl, a brow ridge, the neck-guard behind, a hinged cheek-piece,
# and the centurion's transverse crest in red across the top (the Roman soldiers at a distance wear the same brass and red)
_HELMET = ('\n<path d="M252 130 C 264 60 220 6 160 8 C 104 10 66 52 64 110 C 62 160 70 200 82 236 L 58 268 L 142 264 L 144 214 '
           'C 136 180 140 152 156 138 C 184 130 216 128 250 130 Z" fill="#C8963E" stroke="#0D0D0F" stroke-width="2.6"></path>'
           '\n<path d="M258 136 C 214 126 170 126 142 140 L 140 126 C 172 114 218 114 260 124 Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="2"></path>'
           '\n<path d="M162 136 L 198 136 L 200 216 C 192 228 172 230 164 220 Z" fill="#C8963E" stroke="#0D0D0F" stroke-width="2"></path>'
           '\n<g fill="#0D0D0F"><circle cx="181" cy="152" r="2.6"></circle><circle cx="181" cy="202" r="2.6"></circle></g>'
           '\n<path d="M96 64 C 136 38 198 36 238 68" fill="none" stroke="#8A6A2A" stroke-width="2"></path>'
           '\n<path d="M118 26 C 116 -8 210 -10 210 24 L 196 28 C 192 4 136 4 132 28 Z" fill="#B5121B" stroke="#0D0D0F" stroke-width="2"></path>'
           '\n<path d="M128 22 L 124 4 M144 12 L 142 -2 M164 8 L 164 -6 M182 10 L 186 -4 M198 18 L 204 4" stroke="#7A0A10" stroke-width="2.4"></path>')
CENTURION = F("adam", skin="#D9A27A", shadow="#7A4A3A", hair="#3A2A1A", hl="#6A5A4A", stubble="#3A2A1A", light="#FFC14D") + _HELMET
PAUL = F("adam", skin="#C98E66", shadow="#5A3A3A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#3A2A1A", scarf="#5A4A3A", cord=True, light="#FFC14D")
SAUL_PERSECUTOR = F("adam", skin="#C98E66", shadow="#4A2A2A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#3A2A1A", scarf="#5A4A3A", cord=True, brow="scowl", light="#D7261E")

# colours at a distance (mk.person cloth=)
ROBES = {"peter": "#6A4A2A", "andrew": "#6A7A5A", "james": "#8A5A3A", "john": "#B85A3A", "matthew": "#3A5A6A", "thomas": "#5A4A6A",
         "judas": "#6A2A1A", "mary": "#2A4A7A", "magdalene": "#8A2A3A", "martha": "#8A6A2A", "baptist": "#7A5A3A", "pharisee": "#E8E2D6",
         "pilate": "#F3EFE6", "soldier": "#8A2A1A", "paul": "#5A4A3A"}
