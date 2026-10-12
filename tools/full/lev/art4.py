"""Pictograms for Leviticus chapters 4–5 (Leviticus 12–15): childbirth and purifying, the plague of leprosy in the skin, the
head, the garment and the house, the cleansing of the leper, and issues.

The skin signs are clinical "sample" diagrams: a round lens on a patch of skin, the spot marked with a callout (rising,
scab, bright spot, white hair, raw flesh, reddish-white), so the law reads as a priest's inspection chart, never as a wound."""
import sys, pathlib, random, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus5 as V, ruth1 as R, samuel1 as S1
from genesis import art10 as T
from genesis.art3 import label, man, woman
label = label
from exo import art as A, art8 as B8, art9 as Q
from exo.art6 import GND
from exo.art7 import ban
from lev.art import altar, door, priest, offerer, dove, REACH, jar, flour
def f(v): return f"{v:.1f}"

SKIN_C, SKIN_DARK = "#C98E66", "#8A5A3E"

def lens(x, y, r=34, spot=None, hair=None, raw=False, deep=False, spread=False, dim=False, label_=None, reddish=False, skin=SKIN_C, bald=False):
    """A round inspection lens on the skin. spot: 'white' | 'bright' | 'scab' | None; hair: 'white' | 'black' | 'yellow'."""
    uid = f"ln{int(x)}{int(y)}{r}"
    o = [f'<defs><clipPath id="{uid}"><circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}"></circle></clipPath></defs>',
         f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{skin}"></circle><g clip-path="url(#{uid})">']
    if not bald:
        o += [f'<path d="M{f(x + dx)} {f(y + dy)} l 2 -7" stroke="{SKIN_DARK}" stroke-width="1.2"></path>' for dx, dy in ((-24, -10), (-14, 18), (-4, -22), (10, 22), (20, -6), (-26, 10), (24, 14))]
    if spot:
        sr = r * (0.62 if spread else 0.4); c = {"white": "#F3EFE6", "bright": "#FFF4C2", "scab": "#C8A06A"}[spot]
        if reddish: c = "#E8B0A0"
        o.append(f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(sr)}" ry="{f(sr * 0.8)}" fill="{c}" opacity="{0.55 if dim else 1}" stroke="{SKIN_DARK}" stroke-width="1.2"></ellipse>')
        if deep: o.append(f'<ellipse cx="{f(x)}" cy="{f(y + 2)}" rx="{f(sr * 0.6)}" ry="{f(sr * 0.4)}" fill="none" stroke="{SKIN_DARK}" stroke-width="1.4" stroke-dasharray="3 2"></ellipse>')
    if raw: o.append(f'<ellipse cx="{f(x + r * 0.15)}" cy="{f(y - r * 0.1)}" rx="{f(r * 0.18)}" ry="{f(r * 0.14)}" fill="#C8504A"></ellipse>')
    if hair:
        hc = {"white": "#FFFFFF", "black": "#1A1210", "yellow": "#E8C840"}[hair]
        o += [f'<path d="M{f(x + dx)} {f(y + dy)} l 3 -10" stroke="{hc}" stroke-width="1.8"></path>' for dx, dy in ((-6, 2), (0, -4), (6, 4), (-2, 8), (8, -6))]
    o.append('</g>' + f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="none" stroke="#8FD0E2" stroke-width="2.4"></circle>'
             + f'<path d="M{f(x + r * 0.7)} {f(y + r * 0.7)} L {f(x + r * 1.1)} {f(y + r * 1.1)}" stroke="#8FD0E2" stroke-width="4" stroke-linecap="round"></path>')
    if label_: o.append(label(x, y + r + 12, label_, B8.CY, 7))
    return "".join(o)

def days(x, y, n=7, lit=7, w=11):
    return "".join(f'<rect x="{f(x + i * (w + 2))}" y="{f(y)}" width="{w}" height="{w}" fill="{"#FFD23F" if i < lit else "#12113A"}" stroke="#2C9DB8" stroke-width="1"></rect>' for i in range(n))

def verdict(x, y, clean):
    """CLEAN (green) or UNCLEAN (red) stamp."""
    c = "#5E8F26" if clean else "#D7261E"; t = "CLEAN" if clean else "UNCLEAN"
    return (f'<g transform="rotate(-6 {f(x)} {f(y)})"><rect x="{f(x - 34)}" y="{f(y - 11)}" width="68" height="20" fill="none" stroke="{c}" stroke-width="2.4"></rect>'
            + label(x, y + 4, t, c, 9, weight=700) + '</g>')

def insp(p, x=60): return priest(p, x, up=REACH)

# ---- Leviticus 12 ----
def pg_birth(p):      return GND + woman(p, 90, 86, 0.36, "#7A3A5A") + R.baby(140, 70, 0.8) + days(180, 40, 7) + label(220, 70, "SEVEN DAYS", B8.CY, 8)
def pg_eighth(p):     return GND + R.baby(110, 70, 0.9) + days(160, 40, 8) + label(210, 70, "THE EIGHTH DAY", "#FFD23F", 8)
def pg_33(p):         return GND + woman(p, 80, 86, 0.36, "#7A3A5A") + label(200, 50, "33 DAYS", "#FFD23F", 14) + label(200, 70, "THE BLOOD OF HER PURIFYING", B8.CY, 7)
def pg_maid(p):       return GND + woman(p, 80, 86, 0.36, "#7A3A5A") + R.baby(130, 70, 0.8) + label(220, 46, "TWO WEEKS · 66 DAYS", "#FFD23F", 10)
def pg_lamb_dove(p):  return GND + woman(p, 60, 86, 0.36, "#7A3A5A") + E3.lamb(130, 84, 0.4) + dove(190, 80, 1.0) + door(270, 84)
def pg_poor(p):       return GND + woman(p, 70, 86, 0.36, "#7A3A5A") + dove(150, 80, 1.2) + dove(190, 80, 1.2, flip=True) + altar(270, 84, 0.9)

# ---- Leviticus 13: the skin ----
def pg_brought(p):    return GND + man(p, 110, 86, 0.36, "#5A3A22") + insp(p, 180) + lens(260, 50, 30, spot="bright", label_="RISING · SCAB · BRIGHT SPOT")
def pg_white_hair(p): return GND + insp(p) + lens(170, 48, 34, spot="white", hair="white", deep=True, label_="HAIR WHITE · DEEPER THAN THE SKIN") + verdict(270, 50, False)
def pg_shut7(p):      return GND + insp(p) + lens(160, 48, 30, spot="bright", label_="NOT DEEPER · HAIR NOT WHITE") + days(210, 40, 7) + label(250, 70, "SHUT UP SEVEN DAYS", B8.CY, 7)
def pg_stay(p):       return GND + lens(80, 48, 30, spot="bright", label_="AT A STAY") + days(140, 40, 7) + days(140, 56, 7) + label(190, 82, "SEVEN DAYS MORE", B8.CY, 7)
def pg_dim(p):        return GND + lens(110, 48, 32, spot="scab", dim=True, label_="DIM · NOT SPREAD") + E3.basin(200, 82, 30) + verdict(270, 50, True)
def pg_spread(p):     return GND + lens(110, 48, 32, spot="scab", spread=True, label_="SPREAD ABROAD") + verdict(240, 50, False)
def pg_old(p):        return GND + lens(110, 48, 32, spot="white", hair="white", raw=True, label_="WHITE RISING · RAW FLESH") + verdict(240, 50, False)
def pg_all_white(p):  return GND + man(p, 100, 86, 0.38, "#F3EFE6") + lens(200, 48, 32, spot="white", spread=True, label_="ALL TURNED WHITE") + verdict(280, 50, True)
def pg_raw(p):        return GND + lens(110, 48, 32, raw=True, label_="RAW FLESH") + verdict(240, 50, False)
def pg_raw_white(p):  return GND + lens(80, 48, 28, raw=True, label_="RAW") + label(150, 52, "→", "#FFD23F", 18) + lens(220, 48, 28, spot="white", label_="TURNED WHITE") + verdict(290, 30, True)
def pg_boil(p):       return GND + lens(110, 48, 32, spot="white", reddish=True, label_="THE BOIL · REDDISH-WHITE") + insp(p, 230)
def pg_boil_scar(p):  return GND + lens(110, 48, 32, spot="bright", dim=True, label_="THE SCAR OF THE BOIL") + verdict(240, 50, True)
def pg_burn(p):       return GND + E.blaze(70, 84, 30, 34, 4, n=4) + lens(170, 48, 32, spot="bright", reddish=True, label_="A BURNING BY FIRE") + insp(p, 270)
def pg_burn_white(p): return GND + lens(110, 48, 32, spot="bright", hair="white", deep=True, label_="WHITE HAIR · DEEPER") + verdict(240, 50, False)
def pg_burn_scar(p):  return GND + lens(110, 48, 32, spot="bright", dim=True, label_="THE SCAR OF THE BURNING") + days(180, 40, 7) + verdict(260, 76, True)

# ---- the head and the beard ----
def head(x, y, s=1.0, bald=False, beard=False, spot=None, front=False):
    """A man's head in profile, facing right, with hair or bald, and the place of the plague marked."""
    o = (f'<g transform="translate({f(x)} {f(y)}) scale({f(s)})"><path d="M-20 10 C -24 -24 0 -40 20 -30 C 30 -24 32 -10 28 0 L 32 6 L 26 10 C 24 22 12 28 0 26 L -4 34 L -18 34 Z" fill="{SKIN_C}" stroke="#0D0D0F" stroke-width="1.6"></path>')
    if not bald:
        o += '<path d="M-20 10 C -26 -20 -4 -42 22 -32 C 14 -36 0 -34 -8 -26 C -12 -18 -14 -6 -12 6 Z" fill="#2A1A10"></path>' if not front else '<path d="M-20 10 C -26 -10 -18 -30 -6 -36 C -12 -24 -14 -10 -12 6 Z" fill="#2A1A10"></path>'
    if beard: o += '<path d="M2 14 C 6 26 20 30 26 12 C 22 20 12 22 2 14 Z" fill="#2A1A10"></path>'
    if spot: o += f'<circle cx="{-2 if not beard else 16}" cy="{-26 if not beard else 18}" r="7" fill="{spot}" stroke="#0D0D0F" stroke-width="1"></circle>'
    return o + "</g>"

def pg_scall(p):      return GND + head(90, 50, 1.2, spot="#E8C840") + lens(180, 48, 30, hair="yellow", deep=True, label_="YELLOW THIN HAIR · THE SCALL") + verdict(270, 50, False)
def pg_scall_shut(p): return GND + head(90, 50, 1.2, spot="#E8C840") + lens(180, 48, 30, hair="black", label_="NO BLACK HAIR") + days(230, 40, 7)
def pg_shaven(p):     return GND + head(90, 50, 1.2, bald=True, spot="#E8C840") + label(170, 40, "SHAVEN · BUT THE SCALL NOT", B8.CY, 7) + days(170, 54, 7)
def pg_scall_healed(p): return GND + lens(110, 48, 32, hair="black", label_="BLACK HAIR GROWN UP") + verdict(240, 50, True)
def pg_tetter(p):     return GND + lens(110, 48, 32, spot="white", dim=True, label_="DULL WHITE · A TETTER") + verdict(240, 50, True)
def pg_bald(p):       return GND + head(90, 50, 1.2, bald=True) + head(200, 50, 1.2, front=True) + verdict(150, 90, True) + label(90, 22, "BALD", B8.CY, 8) + label(200, 22, "FOREHEAD BALD", B8.CY, 8)
def pg_bald_plague(p): return GND + head(110, 50, 1.3, bald=True, spot="#E8B0A0") + label(200, 40, "REDDISH-WHITE", "#E8B0A0", 9) + verdict(260, 60, False)
def pg_leper(p):      return (GND + mk.person(p, 140, 86, 0.38, body="#8A6A5A", cloth="#6A6460", sw=3, up=[(-22, -158), (-2, -176), (16, -172)])
                              + label(220, 40, "UNCLEAN, UNCLEAN", "#D7261E", 11) + '<path d="M190 20 L 190 96" stroke="#FFD23F" stroke-width="2" stroke-dasharray="5 4"></path>'
                              + "".join(A.black_tent(240 + i * 34, 84, 28, 20) for i in range(2)))
def pg_alone(p):      return GND + "".join(A.black_tent(30 + i * 40, 84, 34, 24) for i in range(3)) + '<path d="M150 20 L 150 96" stroke="#FFD23F" stroke-width="2" stroke-dasharray="5 4"></path>' + mk.person(p, 230, 86, 0.36, body="#8A6A5A", cloth="#6A6460", sw=3) + label(230, 22, "WITHOUT THE CAMP", B8.CY, 7)

# ---- the garment ----
def cloth(x, y, w, h, c="#E8E2D6", spot=None, rent=False, weave=True):
    o = [f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" fill="{c}" stroke="#0D0D0F" stroke-width="1.6"></rect>']
    if weave:
        o += [f'<path d="M{f(x)} {f(y + k)} L {f(x + w)} {f(y + k)}" stroke="#0D0D0F" stroke-width="0.5" opacity="0.3"></path>' for k in range(4, int(h), 5)]
        o += [f'<path d="M{f(x + k)} {f(y)} L {f(x + k)} {f(y + h)}" stroke="#0D0D0F" stroke-width="0.5" opacity="0.3"></path>' for k in range(4, int(w), 5)]
    if spot: o.append(f'<ellipse cx="{f(x + w * 0.55)}" cy="{f(y + h * 0.5)}" rx="{f(w * 0.16)}" ry="{f(h * 0.2)}" fill="{spot}" opacity="0.85"></ellipse>')
    if rent: o.append(f'<path d="M{f(x + w * 0.4)} {f(y)} L {f(x + w * 0.5)} {f(y + h * 0.5)} L {f(x + w * 0.4)} {f(y + h)}" fill="none" stroke="#12113A" stroke-width="4"></path>')
    return "".join(o)

def pg_garments(p):   return GND + cloth(40, 40, 70, 44, "#E8E2D6") + cloth(130, 40, 70, 44, "#C8BCA6") + '<path d="M220 84 C 222 50 280 46 290 84 Z" fill="#8A5A30" stroke="#0D0D0F" stroke-width="1.6"></path>' + label(75, 96, "WOOLLEN", B8.CY, 7) + label(165, 96, "LINEN", B8.CY, 7) + label(255, 96, "SKIN", B8.CY, 7)
def pg_greenish(p):   return GND + cloth(60, 30, 100, 54, spot="#7A9A3A") + cloth(180, 30, 100, 54, spot="#C8504A") + label(110, 96, "GREENISH", B8.CY, 7) + label(230, 96, "REDDISH", B8.CY, 7)
def pg_g_shut(p):     return GND + cloth(60, 30, 100, 54, spot="#7A9A3A") + days(180, 40, 7)
def pg_g_burn(p):     return GND + cloth(60, 30, 100, 54, spot="#7A9A3A") + E.blaze(240, 84, 50, 50, 8, n=6) + label(240, 96, "A FRETTING LEPROSY · BURNT", B8.CY, 6.5)
def pg_g_wash(p):     return GND + cloth(60, 30, 100, 54, spot="#7A9A3A") + E3.basin(210, 82, 40) + days(170, 20, 7)
def pg_g_rend(p):     return GND + cloth(60, 30, 100, 54, spot="#A8C878", rent=True) + label(110, 96, "DIM · RENT OUT", B8.CY, 7) + E.blaze(240, 84, 40, 40, 9, n=5)
def pg_g_clean(p):    return GND + cloth(60, 30, 100, 54) + E3.basin(200, 82, 30) + verdict(270, 50, True)
def pg_g_law(p):      return GND + cloth(40, 40, 70, 44) + cloth(130, 40, 70, 44, "#C8BCA6") + verdict(250, 40, True) + verdict(250, 70, False)
