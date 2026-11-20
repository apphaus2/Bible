"""Shared helpers for the Revelation chapters: the book's kit (RevKit, on epistle.EpistleKit: Mark's packer, words over
drawings clipped to their panels, face panels sized to their words), the line builders, the speakers' tags, and the faces —
John grown old, and Jesus as ntcast draws him.

Lines (each cut from the ASV with G.v, never typed):
    cp(ref, frm=, to=, after=)   John's narration, a caption       cps("1:1-3")  a caption per verse
    sy(...)                      a voice, an ordinary balloon        sys_("2:2-4") a balloon per verse
    sg(...)                      a song of heaven, a song box        gd(...)       God's words, the Voice box
    j(kind, *parts)              one box from several cuts           said(ref, to, frm, kind="say")  narration, then the words
Panels:
    D(lines, fn, bg, who=, sky=, art_h=, size=, h=)   the words over a drawing fn(w, h) (clipped to the panel); who= a
                                 speaker of SPK, tagged at the panel's top left
    F(lines, tok, bg=, who=)     the words beside a face; who= tagged on the face's side
    glory(lines, bg=, h=)        words over a burst of light, a gold inner frame (doxologies, the songs of heaven)
    pic(fn, bg, h)               a drawing without words
    K.pack(segs, prefix, start, end=)   the panels into pages (fewest, fullest pages; faces alternate sides)"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk
from epistle import EpistleKit, clipped, nxt, fin, face_of, GOLD_BG, JOY_BG, GLORY_BG, GRIEF_BG, STERN_BG
from oba.minor import COLD, GOLDEN, RED, DUSK, DAWN, NIGHT, _flat
from job.jdiscourse import tag as _tag
from num.pages import Pages
from ntcast import JESUS, JESUS_TEACH, JESUS_STERN, JESUS_RISEN
from rev import G

CODE = "REV"
CREDIT = "Revelation · Volume Sixty-Six"
LIGHT_BG = "radial-gradient(circle at 26% 46%, #FFFFFF 0 70px, #FFF8DC 220px, #F3E2B0 460px)"     # the Son of man's light
LIGHT_BG_R = "radial-gradient(circle at 74% 46%, #FFFFFF 0 70px, #FFF8DC 220px, #F3E2B0 460px)"
PATMOS_BG = "radial-gradient(circle at 30% 30%, #FFE6B0 0 30px, #C8906A 200px, #4A3A5A 460px)"     # John on the rock, evening
VISION_BG = "radial-gradient(circle at 28% 40%, #FFF4C2 0 30px, #8A7AB8 220px, #1E1A4A 470px)"     # John in the Spirit

GOLD, LAMB_C, ANGEL_C, VOICE_C, ELDER_C, LIVING_C, EARTH_C = "#E8B830", "#F3EFE6", "#D8A820", "#8FD0E2", "#C8962E", "#E8902E", "#8A6A4A"
SPK = {
    "christ": ("JESUS CHRIST", "#F3EFE6"), "son": ("ONE LIKE UNTO A SON OF MAN", "#F3EFE6"),
    "voice": ("A VOICE FROM HEAVEN", VOICE_C), "trumpet": ("A GREAT VOICE, AS OF A TRUMPET", VOICE_C),
    "angel": ("AN ANGEL", ANGEL_C), "mighty": ("A STRONG ANGEL", ANGEL_C), "elder": ("ONE OF THE ELDERS", ELDER_C),
    "elders": ("THE TWENTY-FOUR ELDERS", ELDER_C), "living": ("THE FOUR LIVING CREATURES", LIVING_C),
    "creature": ("A LIVING CREATURE", LIVING_C), "angels": ("MANY ANGELS", ANGEL_C), "every": ("EVERY CREATED THING", "#9CCB5E"),
    "kings": ("THE KINGS OF THE EARTH", "#B5421E"), "souls": ("THE SOULS UNDER THE ALTAR", "#F3EFE6"),
    "multitude": ("A GREAT MULTITUDE", "#F3EFE6"), "eagle": ("AN EAGLE", "#8A6A4A"), "altar": ("A VOICE FROM THE HORNS OF THE ALTAR", GOLD),
    "seventh": ("THE SEVENTH ANGEL", ANGEL_C), "earth": ("THEY THAT DWELL ON THE EARTH", "#8A6A4A"),
    "first": ("THE FIRST ANGEL", ANGEL_C), "second": ("A SECOND ANGEL", ANGEL_C), "third": ("A THIRD ANGEL", ANGEL_C),
    "spirit": ("THE SPIRIT", "#FFD23F"), "sickle": ("AN ANGEL FROM THE ALTAR", ANGEL_C), "waters": ("THE ANGEL OF THE WATERS", ANGEL_C),
    "merchants": ("THE MERCHANTS OF THE EARTH", "#8A5A2A"), "ships": ("EVERY SHIPMASTER", "#1F6F9A"),
    "sun": ("AN ANGEL STANDING IN THE SUN", ANGEL_C), "bowl": ("ONE OF THE SEVEN ANGELS", ANGEL_C),
    "worshippers": ("THE WHOLE EARTH", "#8A6A4A"), "throne": ("A GREAT VOICE OUT OF THE THRONE", VOICE_C),
    "bride": ("THE SPIRIT AND THE BRIDE", "#FFD23F"), "john": ("JOHN", "#B85A3A"), "voices": ("GREAT VOICES IN HEAVEN", VOICE_C),
    "victors": ("THEY THAT CAME OFF VICTORIOUS", "#F3EFE6"), "altar2": ("THE ALTAR", GOLD),
}

class RevKit(EpistleKit):
    """EpistleKit with a speaker's tag on a panel: D(..., who=) at the top left over the drawing, F(..., who=) on the
    face's side above the verse label (the face sides are settled before packing, as EpistleKit.pack settles them)."""
    art_k = 1.0                      # every drawing's art_h scaled by this (a chapter may set K.art_k to give its pictures more room)

    def D(self, lines, fn, bg, who=None, **kw):
        if who: kw["extra"] = kw.get("extra", "") + _tag(*SPK[who], "left: 12px; top: 8px")
        if "art_h" in kw: kw["art_h"] = int(kw["art_h"] * self.art_k)
        return super().D(lines, fn, bg, **kw)

    def F(self, lines, tok, bg=GOLD_BG, who=None, **k):
        s = super().F(lines, tok, bg=bg, **k)
        s["rev_who"] = who
        return s

    def pack(self, segs, prefix, start, **k):
        nf = 0
        for s in segs:
            if s["tok"]:
                if s["flip"] is None: s["flip"] = nf % 2 == 1
                nf += 1
                if s.get("rev_who"):
                    s["extra"] += _tag(*SPK[s["rev_who"]], ("right" if s["flip"] else "left") + ": 12px; bottom: 38px")
        k.setdefault("most", 4); k.setdefault("lone", 0.5); k.setdefault("budget", 1250)
        return super().pack(segs, prefix, start, **k)

K = RevKit(G, CODE, "Revelation", credit=CREDIT, fit_faces=True, clip=True)
cp, gd, sg, sy, j = K.cp, K.gd, K.sg, K.sy, K.j
D, F, glory, pic = K.D, K.F, K.glory, K.pic
v, sp = G.v, G.span

def cps(refs): return K.cps(refs)
def sys_(refs): return K.sys(refs)
def sgs(refs): return K.sgs(refs)

def said(ref, to, frm, kind="say"):
    """A verse in two boxes: John's narration up to `to`, then the words from `frm` (a balloon, a song box or the Voice box)."""
    return [cp(ref, to=to), {"say": sy, "song": sg, "god": gd}[kind](ref, frm=frm)]

def title(num, name, rng, svg, bg, quote, size=None):
    """A chapter opener (第一話 …) with the volume's credit."""
    return K.title(num, name, rng, svg, bg, quote, size=size)

# ---- the faces ----------------------------------------------------------------------------------------------------------
# John, very old (ntcast's JOHN grown old): his profile and skin a shade more weathered, white hair, a long white beard
# (the face kit's beard and moustache in white, and a longer beard below it).
_LONG_BEARD = ('<path d="M170 254 C 176 300 190 344 206 374 C 214 388 230 388 236 372 C 244 344 250 312 250 282 C 240 300 218 312 198 302 C 186 294 176 276 170 254 Z" '
               'fill="#F1EFEA" stroke="#0D0D0F" stroke-width="1.8" stroke-linejoin="round"></path>'
               '<g fill="none" stroke="#A8A49C" stroke-width="1.2" stroke-linecap="round"><path d="M188 300 C 196 326 206 350 214 370"></path>'
               '<path d="M206 308 C 212 330 220 352 226 372"></path><path d="M224 310 C 230 330 236 348 238 362"></path></g>')
_JO = dict(skin="#CF9A76", shadow="#7A4A3A", hair="#EEECE6", hl="#B8B4AA", beard=True, beard_color="#EEECE6")
JOHN_OLD = face_of("adam", light="#FFE680", **_JO) + _LONG_BEARD
JOHN_AWE = face_of("adam", brow="sorrow", light="#FFFFFF", **_JO) + _LONG_BEARD
JOHN_NIGHT = face_of("adam", **dict(_JO, skin="#B8A0A0", shadow="#3A3A5A"), light="#9FB8FF") + _LONG_BEARD
JOHN_GRIEF = face_of("adam", **dict(_JO, skin="#B8A0A0", shadow="#3A3A5A"), brow="sorrow", tear=True, light="#9AA8C8") + _LONG_BEARD
JOHN_JOY = face_of("adam", **dict(_JO, skin="#DCAA86"), light="#FFFFFF") + _LONG_BEARD
from est.common import _crown
_EL = dict(skin="#C98E66", shadow="#5A4A4A", hair="#EEECE6", hl="#B8B4AA", beard=True, beard_color="#EEECE6")
ELDER = face_of("adam", light="#FFF4C2", **_EL) + _crown(False, "#E8B830")      # one of the elders: white hair and beard, a crown of gold
JOHN_LOOK = dict(robe="#B85A3A", mantle="#8A847A", hair="#EEECE6", beard="#EEECE6")      # at a distance: ntcast's rust robe, a grey mantle
