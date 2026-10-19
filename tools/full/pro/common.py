"""Shared helpers for the Proverbs chapters: line builders for discourse.pack, the cast's faces, and saying cells.

Saying cells (chapters 10–29): sayings(items, prefix, start, head) packs cells into pages of two columns, up to four rows
and about `budget` characters a page. A cell is one verse or a small group (cellv("23:29-35")), under an emblem picked from
its words (pick) or named (cellv("26:11", "dog")); a drawn cell (cellv("24:30-34", art=f)) spans the page with a scene
over its words. Each row is as tall as its words need; each cell sets its words as large as its row allows (up to 22 px),
the emblem taking the rest. A chapter stamp goes on the cell where a Bible chapter begins."""
import sys, pathlib, re, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1])); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "kit"))
import mk
from faces_ex import F
from discourse import seg, pack as _pack
from fx import page
from genesis.ch02 import grid
from genesis.ch04 import COLD
from genesis.ch06 import GOLDEN
from genesis.ch07 import RED
from kg2.common import SOLOMON, SOLOMON_WISE, SOLOMON_STERN, SOLOMON_OLD, DAVID_OLD
from pro import G
from pro.emblems import EMB

v, sp = G.v, G.span
CODE = "PROV"
def say(ref, frm=None, to=None, after=None): return ("say", v(ref, frm=frm, to=to, after=after))
def gd(ref, frm=None, to=None, after=None): return ("god", v(ref, frm=frm, to=to, after=after))
def cp(ref, frm=None, to=None, after=None): return ("cap", v(ref, frm=frm, to=to, after=after))
def sg(ref, frm=None, to=None, after=None): return ("song", v(ref, frm=frm, to=to, after=after))
BR = " <br>"
def says(refs): return ("say", " ".join(v(r) for r in _refs(refs)))
def caps(refs): return ("cap", sp(refs))
def _refs(refs):
    a, _, b = refs.partition("-"); c, x = map(int, a.split(":")); y = int(b) if b else x
    return [f"{c}:{k}" for k in range(x, y + 1)]
def sgs(refs):
    """One song box for verses refs, a line break between verses."""
    return [("song", BR.join(v(r) for r in _refs(refs)))]
def joined(kind, *parts):
    """One box from several cuts: joined("say", ("1:2", "Let there", None), "1:3") — a ref alone is the whole verse."""
    return (kind, " ".join(v(p) if isinstance(p, str) else v(p[0], frm=p[1], to=p[2] if len(p) > 2 else None) for p in parts))

def pack(segs, prefix, start, **k):
    k.setdefault("by_need", True)
    k.setdefault("room", 1.04)
    k.setdefault("min_size", 15.5)
    k.setdefault("budget", 1500)
    return _pack(segs, prefix, start, book="Proverbs", code=CODE, **k)

def label(refs):
    a, _, b = refs.partition("-")
    return f"{CODE} {a}" + (f"–{b}" if b else "")

def face(lines, refs, tok, bg=GOLDEN, **k): return seg(lines, label(refs), tok=tok, bg=bg, **k)
def drawn(lines, refs, art, bg, full=False, h=None, **k):
    """Words at the top of a drawing. The panel's height is fixed from its words (17 px type in the upper 56%, at least h if
    given), so the face panels on the page take the rest of the room; the drawing is set below the words (full=True: behind
    them, over the whole panel)."""
    if lines:
        import speech
        hi = k.setdefault("hi", 19)
        def words_h(s, bw=678):                # the words' height at s px, with room for the fallback fonts' wider lines
            return (speech._height(lines, bw, s) + sum(t.count("<br>") for _, t in lines) * s * 1.17 * 0.6) * 1.12 + 34
        th = words_h(17)
        hh = int(min(640, max(h or 250, th / 0.56 + 16, words_h(hi) + 190 if not full else 0)))   # at least 190 px of drawing below the words
        if not full:
            from jos.art import below
            fn = art
            def art(w, hr, fn=fn, lines=lines, hi=hi):
                """Set the drawing just below the words at the size the panel actually gives them (speech.fit)."""
                s = speech.fit(lines, w - 24, hr * 0.62, hi=hi)
                return below(fn, min(0.66, (words_h(s, w - 24) + 10) / hr))(w, hr)
        k["h"] = hh
    elif h: k["h"] = h
    return seg(lines, label(refs), bg=bg, art=art, **k)

# ---- the cast -----------------------------------------------------------------------------------------------------------
# The father is Solomon (kg2.common: black beard, deep-blue headcloth with the gold band). The son: beardless, dark hair,
# a pale-blue headcloth with a dark cord. Wisdom: a woman in a white headscarf with a gold band, in gold light.
SON = F("adam", skin="#E3B08A", shadow="#8A5A3A", hair="#2A1A10", hl="#5A4A3E", scarf="#8FB8D8", cord=True, light="#FFF4C2")
SON_GRAVE = F("adam", skin="#E3B08A", shadow="#5A4A5A", hair="#2A1A10", hl="#5A4A3E", scarf="#8FB8D8", cord=True, brow="sorrow", light="#9AA8C8")
YOUTH = F("adam", skin="#D9A27A", shadow="#5A3A4A", hair="#3A2214", hl="#6A4A2E", stubble="#3A2214", light="#C2456A")
YOUTH_RUE = F("adam", skin="#C98E66", shadow="#3A3A5A", hair="#3A2214", hl="#6A4A2E", stubble="#3A2214", brow="sorrow", tear=True, light="#9AA8C8")
WISDOM = F("eve", skin="#E3B08A", shadow="#B97A58", hair="#1A1210", scarf="#F3EFE6", band=True, light="#FFE680")
WISDOM_STERN = F("eve", skin="#E3B08A", shadow="#9A5A48", hair="#1A1210", scarf="#F3EFE6", band=True, brow="scowl", light="#FFC14D")
AGUR = F("adam", skin="#B98A6E", shadow="#4A3A3A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#3A4A5A", cord=True, light="#FFF4C2")
AGUR_LOW = F("adam", skin="#B98A6E", shadow="#3A3A5A", hair="#8A847A", hl="#B8B2A6", beard=True, beard_color="#9A948A", scarf="#3A4A5A", cord=True, brow="sorrow", light="#9AA8C8")
LEMUEL = F("adam", skin="#C98E66", shadow="#5A3A3A", hair="#1A1210", hl="#4A3A2E", beard=True, beard_color="#1A1210", scarf="#3A1A4A", band=True, light="#FFE680")
QUEEN_MOTHER = F("eve", skin="#C98E66", shadow="#8A5A3E", hair="#8A847A", scarf="#5A2470", band=True, light="#FFE680")
WORTHY = F("eve", skin="#D9A27A", shadow="#9A6A4A", hair="#2A1A10", scarf="#2C6A7A", light="#FFE680")
HUSBAND = F("adam", skin="#C98E66", shadow="#5A4A3A", hair="#2A1A10", hl="#4A3A2E", beard=True, beard_color="#2A1A10", scarf="#F3EFE6", cord=True, light="#FFE680")

# ---- emblems picked from the words --------------------------------------------------------------------------------------
RULES = [
    (r"\bants?\b", ["ant"]), (r"\bconies\b", ["conies"]), (r"\blocusts\b", ["locusts"]), (r"\blizard\b", ["lizard"]),
    (r"\bhedge\b", ["hedge"]), (r"\bdropping\b", ["dripping"]), (r"\bhousetop\b", ["housetop"]), (r"\bhinges\b", ["door"]),
    (r"\bsluggard\b", ["bed", "thorns", "plough"]), (r"\blion'?s?\b", ["lion"]), (r"\ba bear\b", ["bear"]), (r"\bdogs?\b", ["dog"]),
    (r"\bswine'?s?\b", ["swine"]), (r"\bhorse\b", ["horse"]), (r"\bass\b", ["ass"]), (r"\b(oxen|ox|crib|beast|beasts|cattle)\b", ["ox", "sheep"]),
    (r"\b(sheep|flocks?|herds|lambs)\b", ["sheep"]), (r"\bgoats?'?\b", ["goats"]), (r"\beagle\b", ["eagle"]),
    (r"\b(serpent|adder)\b", ["serpent"]), (r"\b(snares?|net|gin)\b", ["snare"]), (r"\b(birds?|sparrow|swallow|fowler)\b", ["bird"]),
    (r"\b(lamp|candle)\b", ["lamps", "lamp"]), (r"\btree of life\b", ["tree"]), (r"\bfig-tree\b", ["fig"]),
    (r"\b(fountain|spring|wellspring)\b|\b(a|own|the) well\b(?!-)", ["fountain", "well"]), (r"\bcistern\b", ["cistern"]), (r"\bwater\b.*\bface\b", ["reflection"]),
    (r"\b(cold waters?)\b", ["cup"]), (r"\bwaters?\b", ["waters", "fountain", "cup"]), (r"\bwithout rain\b", ["clouds_dry"]),
    (r"\b(rain|clouds?)\b", ["rain", "clouds_dry"]), (r"\bsnow\b", ["snow"]), (r"\bwind\b", ["clouds_dry"]),
    (r"\bcrowne?d?\b", ["crown"]), (r"\bthrone\b", ["throne"]), (r"\b(king'?s?|kings|princes?|rulers?|nobles)\b", ["throne", "king_people", "crown"]),
    (r"\b(balances?|weights?|measures?)\b", ["scales", "weights"]), (r"\b(refining pot|furnace|dross)\b", ["crucible"]),
    (r"\b(gifts?|bribes?)\b", ["gift"]), (r"\blot\b", ["lot"]), (r"\bdry morsel\b", ["morsel"]),
    (r"\b(wine|strong drink|drunkards?|mixed wine)\b", ["wine"]), (r"\b(honey|honeycomb)\b", ["honey"]),
    (r"\b(rubies|jewels?|precious stones)\b", ["chest", "jewel"]), (r"\bapples\b", ["apples"]), (r"\b(ear-ring|ornament)\b", ["jewel"]),
    (r"\b(silver|gold|treasures?|riches|wealth|money|substance)\b", ["chest", "silver", "gold"]),
    (r"\b(tilleth|tiller|plough|plow|sow|soweth|reap|reapeth|harvest)\b", ["field", "reaper", "plough"]),
    (r"\b(diligent|slothful|slack|sluggish|idle)\b", ["reaper", "bed", "field"]),
    (r"\b(pride|proud|haughty|lofty|haughtiness)\b", ["house_fallen", "city_broken"]),
    (r"\b(surety|suretyship|stricken hands|hand join)\b", ["friends"]),
    (r"\b(bread|morsel|food|meat|feast|dainties|dinner|eat|eateth|eaten|hungry|famish)\b", ["bread", "feast"]),
    (r"\b(vineyard)\b", ["vineyard"]), (r"\b(thorns|thistles|nettles|thorn)\b", ["thorns"]), (r"\blandmarks?\b", ["landmark"]),
    (r"\b(fields?|harvest|reap|reapeth|soweth|sow|grain|plough|plow|tilleth|tiller|summer)\b", ["field", "reaper", "plough"]),
    (r"\b(swords?|spear)\b", ["sword"]), (r"\b(arrows?|darts|a bow)\b", ["arrows"]), (r"\biron\b", ["iron"]),
    (r"\b(fire|coals|firebrands|wood|smoke|burn)\b", ["fire", "coals"]), (r"\btower\b", ["tower"]),
    (r"\bbroken (down|into)\b.*\bwalls?\b|\bwithout walls\b", ["city_broken"]), (r"\b(city|cities|walls?|strong city)\b", ["city", "city_broken"]),
    (r"\bgates?\b", ["gate"]), (r"\b(doors?)\b", ["door"]), (r"\b(bed|sleep|slumber|sleepeth|sleepest)\b", ["bed"]),
    (r"\b(ships?|sea)\b", ["sea"]), (r"\b(stones?|sand)\b", ["stone"]), (r"\b(pit|diggeth)\b", ["pit"]),
    (r"\b(house|houses|dwelling|habitation|tent|tabernacle|builded|buildeth)\b", ["house", "houses"]),
    (r"\b(sheol|death|grave|dead|die|dieth|slain)\b", ["grave", "pit"]),
    (r"\b(morning|dawn|light)\b", ["dawn", "path_light", "sun"]), (r"\b(darkness|night)\b", ["night", "path_dark"]),
    (r"\b(war|battle|mighty|warfare|army)\b", ["army"]), (r"\b(messenger|ambassador|news|tidings)\b", ["runner"]),
    (r"\b(witness|witnesses|judge|judgment|justify|justifieth|condemneth|cause)\b", ["witness", "gate", "scales"]),
    (r"\b(rod|stripes|chasten|chasteneth|correcteth|beat|smite|smiteth)\b", ["rod"]),
    (r"\b(grey|hoary|old men|old)\b", ["old"]), (r"\b(wife|woman|women)\b", ["woman", "housetop"]),
    (r"\b(children|child|sons?|father|mother|parents)\b", ["family", "mother", "rod"]),
    (r"\b(friends?|neighbor|brother|brethren|companions?)\b", ["friends"]),
    (r"\b(strife|contention|contentious|quarrel|anger|angry|wrath|wrathful|furious)\b", ["strife", "face_angry"]),
    (r"\b(poor|poverty|needy|want)\b", ["poor_rich", "poor", "rich"]), (r"\brich\b", ["rich", "poor_rich"]),
    (r"\b(lie|lies|lying|false|deceit|deceitful|flattereth|flattering|tale-?bearer|whisperer|slander|slandereth|perverse)\b", ["face_liar"]),
    (r"\b(fool|fools|fool's|folly|foolish|foolishness|scoffer|scoffers|simple)\b", ["face_fool"]),
    (r"\b(lips|mouth|tongue|words|speaketh|answer|speak|uttereth|talk)\b", ["face_wise", "face_listen"]),
    (r"\b(ear|heareth|hear|hearken|instruction|reproof|counsel|correction)\b", ["face_listen", "scroll"]),
    (r"\b(glad|joy|rejoice|rejoiceth|merry|cheerful)\b", ["face_glad"]), (r"\b(sorrow|heaviness|broken spirit|grief)\b", ["face_sad"]),
    (r"\b(path|paths|ways?|walketh|steps|feet|goings)\b", ["fork", "path_light", "path_dark"]),
    (r"\b(nation|people)\b", ["king_people"]), (r"\bjehovah\b", ["rays", "sun"]),
    (r"\b(righteous|wicked|upright|transgressors?|evil|evil-doers)\b", ["houses", "trees", "lamps", "fork", "chaff", "dawn"]),
    (r"\b(wise|wisdom|understanding|knowledge|prudent)\b", ["scroll", "face_wise", "face_listen"]),
]
DEFAULT = ["scroll", "rays", "tree", "dawn", "sun"]

def pick(text, used=()):
    t = text.lower()
    cands = []
    for pat, names in RULES:
        if re.search(pat, t): cands += [n for n in names if n not in cands]
    cands += [n for n in DEFAULT if n not in cands]
    for n in cands:
        if n not in used: return n
    return cands[0]

# ---- saying cells ---------------------------------------------------------------------------------------------------------
W_HALF, W_FULL = 336, 696
ACCENT = "#B5402A"

def cellv(refs, emb=None, head=None, span=False, art=None, bg=None):
    """A saying cell: verses refs ("10:1" or "23:29-35"); emb names its emblem (None: picked from the words); art = f(w, h) -> svg
    for a drawn scene (the cell then spans the page); head starts a new page head."""
    return dict(refs=refs, emb=emb, head=head, span=span or art is not None, art=art, bg=bg)

def run(c, a, b, groups=(), embs=None, head=None, spans=()):
    """Cells for verses c:a–b, one verse each, except groups [(x, y), ...] kept together; embs {verse: emblem};
    head on the first cell; spans: verses whose cell spans the page."""
    embs = embs or {}
    out, k = [], a
    gmap = {x: y for x, y in groups}
    while k <= b:
        y = gmap.get(k, k)
        refs = f"{c}:{k}" + (f"-{y}" if y != k else "")
        out.append(cellv(refs, embs.get(k), head if k == a else None, span=k in spans))
        k = y + 1
    return out

def _text_h(nverse, chars, w, s):
    """Estimated height of a cell's words at s px (Archivo Narrow, uppercase; the sandbox's fallback is wider)."""
    bw = w - 6 - 30 - (18 if nverse > 1 else 0)
    cpl = max(6, bw / (s * 0.57))
    lines = sum(math.ceil(n / cpl) for n in chars)
    return lines * s * 1.17 + 6 * (nverse - 1) + 22

def _need(c, s=17.0):
    w = W_FULL if c["span"] else W_HALF
    return _text_h(len(c["vs"]), [len(t) for _, t in c["vs"]], w, s) + (150 if c["art"] else 72)

def _size(c, h):
    w = W_FULL if c["span"] else W_HALF
    pic = 130 if c["art"] else (64 if c["span"] else 70)
    s = 22.0
    while s > 11 and _text_h(len(c["vs"]), [len(t) for _, t in c["vs"]], w, s) > h - 6 - pic: s -= 0.5
    return s

def _cell_html(c, h, s, uid, used, end=""):
    w = W_FULL if c["span"] else W_HALF
    a = c["refs"].split("-")[0]; ch, vs = a.split(":")
    ref = label(c["refs"])
    if c["art"]:
        th = _text_h(len(c["vs"]), [len(t) for _, t in c["vs"]], w, s)
        ph = max(80, round(h - 6 - th - 3))
        pic_svg = f'<svg viewBox="0 0 {w} {ph}" preserveAspectRatio="xMidYMid slice" style="position: absolute; inset: 0; width: 100%; height: 100%; display: block">{c["art"](w, ph)}</svg>'
        pbg = c["bg"] or "#2A1A3A"
    else:
        name = c["emb"] or pick(" ".join(t for _, t in c["vs"]), used)
        used.add(name)
        pic_svg = f'<svg viewBox="0 0 320 120" preserveAspectRatio="xMidYMid meet" style="position: absolute; inset: 0; width: 100%; height: 100%; display: block">{EMB[name](uid)}</svg>'
        pbg = "#2A1A3A"
    stamp = mk.stamp(int(ch), "left: 10px; top: 8px", rot=-4) if vs == "1" else ""
    tag = f'<span data-label style="position: absolute; right: 8px; top: 8px; padding: 1px 5px; background: #F3EFE6; color: #0D0D0F; font-size: 9px; font-weight: 600; letter-spacing: 0.18em">{ref}</span>'
    words = []
    for r, t in c["vs"]:
        num = (f'<span data-label style="flex: none; width: 14px; padding-top: 2px; font-size: 9px; font-weight: 600; color: {ACCENT}">{r.split(":")[1]}</span>' if len(c["vs"]) > 1 else "")
        words.append(f'<div style="display: flex; gap: 4px">{num}<div style="font-family: \'Archivo Narrow\', sans-serif; font-weight: 700; font-size: {s}px; line-height: 1.17; '
                     f'letter-spacing: 0.02em; text-transform: uppercase">{t}</div></div>')
    span = "; grid-column: span 2" if c["span"] else ""
    return (f'\n    <div style="position: relative; min-height: 0; overflow: hidden; border: 3px solid #0D0D0F; background: #FFF8E6; display: flex; flex-direction: column{span}">'
            f'\n      <div style="position: relative; flex: 1 1 0; min-height: 0; overflow: hidden; background: {pbg}; border-bottom: 3px solid #0D0D0F">{pic_svg}{stamp}{tag}{end}</div>'
            f'\n      <div style="flex: none; padding: 8px 12px 10px 12px; box-shadow: inset 6px 0 0 #FFF8E6, inset 10px 0 0 {ACCENT}; padding-left: 20px; display: flex; flex-direction: column; gap: 6px">'
            + "".join(words) + f'</div>\n    </div>')

def _rows(cells):
    """Pair the cells two to a row; a spanning cell, or a cell left without a partner, fills its row."""
    rows, cur = [], []
    for c in cells:
        if c["span"]:
            if cur: rows.append([dict(cur[0], span=True)]); cur = []
            rows.append([c])
        else:
            cur.append(c)
            if len(cur) == 2: rows.append(cur); cur = []
    if cur: rows.append([dict(cur[0], span=True)])
    return rows

ROOM = 1022

def sayings(items, prefix, start, default_head, budget=1050, most=4, end="", book="Proverbs"):
    """Pack saying cells into pages; returns [(file name, board title, page fn)] numbered from start."""
    cells = []
    for it in items:
        c = dict(it); c["vs"] = [(r, v(r)) for r in _refs(it["refs"])]
        c["chars"] = sum(len(t) for _, t in c["vs"])
        if c["chars"] > 250: c["span"] = True                       # a long group of sayings takes the whole width
        cells.append(c)
    # pages: break on a head (unless the page is still short), on the budget, or when the rows would not fit at 15px
    pages, cur = [], []
    def fits(cs):
        rs = _rows(cs)
        return len(rs) <= most and sum(max(_need(c, 17.5) for c in r) for r in rs) <= ROOM - 12 * (len(rs) - 1)
    for c in cells:
        chars = sum(x["chars"] for x in cur)
        if cur and ((c["head"] and chars > 420) or chars + c["chars"] > budget or not fits(cur + [c])):
            pages.append(cur); cur = []
        cur.append(c)
    if cur: pages.append(cur)
    if len(pages) > 1 and sum(x["chars"] for x in pages[-1]) < 330 and fits(pages[-2] + pages[-1]) and not pages[-1][0]["head"]:
        last = pages.pop(); pages[-1] += last                       # no near-empty last page
    # even out each run of pages between heads, so no page of the run is left short
    sections, cur = [], []
    for pg in pages:
        if cur and pg[0]["head"]: sections.append(cur); cur = []
        cur.append(pg)
    if cur: sections.append(cur)
    pages = []
    for sec in sections:
        flat = [c for pg in sec for c in pg]; n = len(sec)
        total = sum(c["chars"] for c in flat); bal, cur, acc = [], [], 0
        for c in flat:
            if cur and len(bal) < n - 1 and acc + c["chars"] / 2 > total * (len(bal) + 1) / n:
                bal.append(cur); cur = []
            cur.append(c); acc += c["chars"]
        bal.append(cur)
        pages += bal if len(bal) == n and all(fits(b) for b in bal) else sec
    out, head = [], default_head
    for k, pg in enumerate(pages):
        rows = _rows(pg)
        needs = [max(_need(c) for c in r) for r in rows]
        room = ROOM - 12 * (len(rows) - 1)
        hs = [max(150, round(room * n / sum(needs))) for n in needs]
        hs[-1] = room - sum(hs[:-1])
        used, html = set(), []
        size = min(_size(c, hh) for r, hh in zip(rows, hs) for c in r)     # one type size for the whole page
        for i, (r, hh) in enumerate(zip(rows, hs)):
            for j, c in enumerate(r):
                last = end and k == len(pages) - 1 and i == len(rows) - 1 and j == len(r) - 1
                html.append(_cell_html(c, hh, size, f"sy{prefix[-3:]}{k}x{i}x{j}", used, end if last else ""))
        for c in pg:
            if c["head"]: head = c["head"]; break
        a0 = pg[0]["refs"].split("-")[0]
        lr = pg[-1]["refs"]; cl = lr.split(":")[0]; vl = lr.split(":")[1].split("-")[-1]
        rng = a0 if f"{cl}:{vl}" == a0 else (f"{a0}–{vl}" if a0.split(":")[0] == cl else f"{a0}–{cl}:{vl}")
        title = f"{book} {rng} — {head}"
        slug = re.sub(r"[^A-Za-z]", "", head.title())[:18]
        body = grid(html, " ".join(f"{h}px" for h in hs[:-1]) + (" " if len(hs) > 1 else "") + "minmax(0, 1fr)", ncol=2)
        out.append((f"{prefix}-P{k + 1:02d}-{slug}", f"{start + k} · {head}", (lambda title=title, body=body, n=start + k: page(title, "minmax(0, 1fr)", body, n))))
        for c in pg[1:]:
            if c["head"]: head = c["head"]
    return out
