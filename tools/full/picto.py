"""A pictogram for any law, picked from its own words (for the long law codes: Deuteronomy 12–26, Ezekiel 40–48, ...).

    pick(text, uid) -> svg in the 320 x 100 law-cell viewBox

Each rule is (keywords, drawing); the first rule with a keyword in the text wins, so the more particular rules come first.
The drawings are built from the shared kit (Leviticus pictograms, the Exodus and Numbers cast), so a law page always shows
something of what the law is about: an altar for offerings, a gate for judgment, a field for the harvest, and so on."""
import sys, pathlib, re, random
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "kit"))
import mk, exodus as E, exodus3 as E3, exodus5 as V, samuel1 as S1, numbers1 as N, ruth1 as R
from genesis.art3 import label, man, woman, king
from exo import art as A, art8 as B8, art9 as Q
from exo.art7 import coins, ban
from lev.art import GND, altar, priest, offerer, REACH, flour, jar, cakes, goat, dove, ears, door
from lev.art3 import raptor
from lev.art5 import water, house
from num.art16 import gate, iron, stone, wood
from num.art4 import wagon
from num.art3 import scroll, shroud
ALL = ("Man", "ManUp", "Woman", "WomanUp", "Hair", "Robe", "Tunic")
CY = B8.CY
def f(v): return f"{v:.1f}"

def _cow(x, s=0.24): return S1.cow(x, 84, s, color="#8A5A30", patch="#E8E2D6")
def _ass(x, s=0.3): return N.ass(x, 84, s)
def _sheep(x, s=0.36): return E.sheep(x, 84, s)
def _field(): return "".join(f'<path d="M{x} 84 L {x} 60" stroke="#C8A030" stroke-width="2"></path><ellipse cx="{x}" cy="58" rx="3" ry="7" fill="#E8C060"></ellipse>' for x in range(20, 310, 14))
def _vines(): return "".join(N.grapes(x, 58, 0.36, x) for x in (60, 130, 200, 270))
def _olive(x=160): return f'<path d="M{x} 86 L {x} 50" stroke="#5A3A22" stroke-width="5"></path><ellipse cx="{x}" cy="42" rx="40" ry="24" fill="#6A8A4A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>'
def _sword(x, y): return f'<path d="M{x} {y} L {x + 50} {y - 50}" stroke="#C8C8D0" stroke-width="5" stroke-linecap="round"></path><path d="M{x + 6} {y - 16} L {x + 18} {y - 4}" stroke="#5A3A22" stroke-width="5"></path>'
def _idol(x): return f'<path d="M{x - 10} 84 L {x - 8} 46 L {x - 14} 40 L {x} 26 L {x + 14} 40 L {x + 8} 46 L {x + 10} 84 Z" fill="#B8862A" stroke="#0D0D0F" stroke-width="1.6"></path>'
def _tent(x): return A.black_tent(x, 84, 70, 44)
def _bird(x): return dove(x, 80, 1.1)
def _child(p, x): return man(p, x, 86, 0.22, "#C8A06A")
def _elders(p, x0=40, n=4): return "".join(A.elder(c, i)(p, x0 + i * 34, 86, 0.3) for i, c in enumerate(A.CLOTHS[:n]))
def _scales(x, y): return (f'<path d="M{x} {y} L {x} {y + 40} M{x - 30} {y + 8} L {x + 30} {y + 8}" stroke="#E8B830" stroke-width="3"></path>'
                           f'<path d="M{x - 40} {y + 30} L {x - 20} {y + 30} L {x - 30} {y + 8} Z M{x + 20} {y + 30} L {x + 40} {y + 30} L {x + 30} {y + 8} Z" fill="#E8B830" stroke="#0D0D0F" stroke-width="1.2"></path>')
def _millstone(x): return f'<circle cx="{x}" cy="70" r="20" fill="#8A8478" stroke="#0D0D0F" stroke-width="2"></circle><circle cx="{x}" cy="70" r="5" fill="#3A3430"></circle>'
def _garment(x): return f'<path d="M{x - 30} 30 L {x + 30} 30 L {x + 36} 84 L {x - 36} 84 Z" fill="#C8B890" stroke="#0D0D0F" stroke-width="1.6"></path>'
def _fringe(x): return _garment(x) + "".join(f'<path d="M{x - 30 + i * 12} 84 L {x - 30 + i * 12} 96" stroke="#1F5FAD" stroke-width="3"></path>' for i in range(6))
def _roof(x): return house(x, 84, 100, 50) + f'<path d="M{x - 56} 34 L {x + 56} 34" stroke="#5A4A3A" stroke-width="3"></path>' + "".join(f'<path d="M{x - 50 + i * 12} 34 L {x - 50 + i * 12} 26" stroke="#5A4A3A" stroke-width="2"></path>' for i in range(9))
def _landmark(x): return f'<path d="M{x - 14} 84 L {x - 10} 50 L {x + 10} 50 L {x + 14} 84 Z" fill="#A89E92" stroke="#0D0D0F" stroke-width="1.6"></path>' + '<path d="M20 70 L 300 70" stroke="#FFD23F" stroke-width="1.6" stroke-dasharray="5 4"></path>'
def _nest(x): return f'<ellipse cx="{x}" cy="78" rx="26" ry="10" fill="#8A6A3A" stroke="#0D0D0F" stroke-width="1.6"></ellipse>' + "".join(f'<ellipse cx="{x + dx}" cy="72" rx="5" ry="6" fill="#F3EFE6" stroke="#0D0D0F" stroke-width="1"></ellipse>' for dx in (-10, 0, 10)) + _bird(x + 60)
def _blood(x): return "".join(f'<circle cx="{x + i * 9}" cy="{70 + (i % 2) * 6}" r="3.4" fill="#B5121B"></circle>' for i in range(6))
def _crown(p, x): return king(p, x, 86, 0.38, "#7A2A4A")
def _war(p): return "".join(man(p, 40 + i * 30, 86, 0.3, "#5A4A3A", up=[(-22, -158), (-26, -200), (-28, -236)]) for i in range(9))

def _f(p, *parts): return GND + "".join(x(p) if callable(x) else x for x in parts)

# (keywords, drawing) — first match wins
RULES = [
    (("king over thee", "the king", "a king"), lambda p: _f(p, _crown(p, 120), scroll(220, 74, 1.0))),
    (("prophet", "dreamer of dreams", "diviner", "enchanter", "sorcerer", "necromancer", "augury"), lambda p: _f(p, man(p, 100, 86, 0.36, "#4A3A6A", up=[(-22, -158), (-6, -196), (8, -228)]), ban(220, 50, 30))),
    (("other gods", "serve them", "graven image", "asherah", "pillar", "molten", "idol"), lambda p: _f(p, _idol(100), _idol(150), ban(240, 50, 30))),
    (("to battle", "to war", "the battle", "besiege", "siege", "enemies", "fight"), lambda p: _f(p, _war(p))),
    (("high priest",), lambda p: _f(p, priest(p, 160, high=True))),
    (("priest", "levite"), lambda p: _f(p, priest(p, 100), priest(p, 150, flip=True), altar(250, 84, 0.9))),
    (("judge", "judgment", "witness", "matter be too hard", "elders of his city", "the gate"), lambda p: _f(p, _elders(p, 30), man(p, 220, 86, 0.34, "#5A4A3A", flip=True), gate(280, 84, 0.6))),
    (("city of refuge", "cities of refuge", "manslayer", "slayeth his neighbor", "avenger"), lambda p: _f(p, man(p, 90, 86, 0.34, "#5A4A3A", up=[(-22, -158), (0, -140), (20, -150)]), gate(240, 84, 1.0))),
    (("landmark",), lambda p: _f(p, _landmark(160))),
    (("burnt-offering", "sacrifice", "offering", "altar", "vow", "freewill"), lambda p: _f(p, offerer(p, 60), _sheep(140), altar(250, 84, 1.0))),
    (("tithe", "firstling", "first-fruits", "firstfruits"), lambda p: _f(p, ears(70, 84, 1.0), _sheep(140), _cow(210), jar(280, 84, 0.8))),
    (("passover", "unleavened", "feast of weeks", "feast of tabernacles", "booths", "feast"), lambda p: _f(p, cakes(80, 84, 1.0), E3.lamb(160, 84, 0.34), _tent(250))),
    (("release", "seventh year", "sabbath"), lambda p: _f(p, coins(50, 70, 6), label(170, 50, "THE YEAR OF RELEASE", "#FFD23F", 9))),
    (("poor", "needy", "widow", "fatherless", "sojourner", "stranger"), lambda p: _f(p, woman(p, 90, 86, 0.34, "#3A3A4A"), _child(p, 120), man(p, 210, 86, 0.36, "#5A3A22", flip=True, up=REACH))),
    (("hire", "wages", "hired servant"), lambda p: _f(p, man(p, 90, 86, 0.36, "#6A5A3A"), coins(150, 70, 4), A.black_tent(250, 84, 70, 44))),
    (("servant", "bondman", "bondmaid", "slave"), lambda p: _f(p, man(p, 100, 86, 0.36, "#6A5A3A"), door(200, 84, 1.0), label(260, 50, "THE AWL", CY, 8))),
    (("pledge", "lend", "usury", "loan", "debt", "creditor"), lambda p: _f(p, coins(60, 70, 8), _millstone(200), _garment(270))),
    (("weights", "balance", "measure", "ephah"), lambda p: _f(p, _scales(160, 30))),
    (("money", "silver", "shekels", "gold"), lambda p: _f(p, coins(80, 70, 10))),
    (("vineyard", "grapes", "vintage", "wine"), lambda p: _f(p, _vines())),
    (("olive",), lambda p: _f(p, _olive(), _olive(240))),
    (("field", "harvest", "sheaf", "standing grain", "reap", "sow", "seed"), lambda p: _f(p, _field())),
    (("ox", "oxen", "ass", "herd", "cattle", "beast"), lambda p: _f(p, _cow(80), _ass(170), _sheep(250))),
    (("sheep", "flock", "lamb", "goat", "kid"), lambda p: _f(p, _sheep(80), E3.lamb(150, 84, 0.3), goat(230, 84, 0.34))),
    (("bird", "nest", "dam"), lambda p: _f(p, _nest(130))),
    (("eat", "clean", "unclean", "abominable", "flesh"), lambda p: _f(p, _cow(70), _sheep(140), goat(230, 84, 0.34))),
    (("blood",), lambda p: _f(p, altar(100, 84, 1.0), _blood(170))),
    (("battlement", "roof", "new house", "house"), lambda p: _f(p, _roof(160))),
    (("garment", "raiment", "fringes", "mingled stuff"), lambda p: _f(p, _fringe(160))),
    (("wife", "marry", "betrothed", "damsel", "virgin", "divorcement", "husband"), lambda p: _f(p, man(p, 110, 86, 0.38, "#4A3A6A"), woman(p, 190, 86, 0.34, "#6A3A5A", flip=True))),
    (("son", "children", "father", "mother"), lambda p: _f(p, man(p, 90, 86, 0.38, "#5A3A22"), woman(p, 140, 86, 0.34, "#6A3A5A"), _child(p, 200))),
    (("dead", "slain", "hanged", "tree"), lambda p: _f(p, shroud(160, 84, 1.2))),
    (("stone him", "stones", "stoned"), lambda p: _f(p, "".join(stone(80 + i * 30, 84) for i in range(6)))),
    (("camp", "tent", "assembly of jehovah"), lambda p: _f(p, _tent(80), _tent(160), _tent(240))),
    (("well", "water", "river"), lambda p: _f(p, water(160, 80, 220))),
    (("mill", "millstone"), lambda p: _f(p, _millstone(160))),
    (("land", "inheritance", "possess"), lambda p: _f(p, N.grapes(60, 56, 0.4, 1), _olive(160), ears(260, 84, 1.0))),
]

def pick(text, uid="pk"):
    t = text.lower()
    for keys, draw in RULES:
        if any(k in t for k in keys):
            return mk.defs(uid, *ALL) + draw(uid)
    return mk.defs(uid, *ALL) + _f(uid, scroll(160, 74, 1.4))
