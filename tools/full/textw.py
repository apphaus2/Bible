"""How wide a text is set, counted in Latin letters, for the estimates that size type and pack pages (speech._height,
discourse.pack and their kin). A Hangul syllable or a CJK character is set about twice as wide as the Latin letter
the estimates assume, so a Korean, Chinese or Japanese text would otherwise get type too big for its box. For a Latin
(or Cyrillic, Greek …) text width(t) == len(t): the English and Spanish pages are unchanged."""
import unicodedata

def width(t):
    if t.isascii(): return len(t)
    return round(sum(2.0 if unicodedata.east_asian_width(c) in "WF" else 1 for c in t))
