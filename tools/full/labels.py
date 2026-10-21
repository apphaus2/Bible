"""The words on the pages that are not scripture — titles, stamps, headings, map and chart labels — and their translations.

    python3 tools/full/labels.py collect          # every label of the English pages -> tools/full/i18n/labels.json
    python3 tools/full/labels.py missing es       # labels with no Spanish yet -> printed, for translating

tools/full/i18n/<lang>/*.json maps each English label to its translation; build_volume.py (BIBLE_LANG=<lang>) puts it on
every page with translate(). A label is a text node of a page that is not a run of the ASV: scripture is never in these
files (it comes from ref/<eBible id> through asv.Book)."""
import re, sys, json, html, pathlib, unicodedata
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
I18N = HERE / "i18n"
TEXT = re.compile(r">([^<>]*[A-Za-z][^<>]*)<")             # a text node with a letter in it
SVG_TEXT = re.compile(r"<(?:text|tspan)\b[^>]*>([^<>]+)<")     # a word drawn in a picture

def norm(t):
    return re.sub(r"\s+", " ", html.unescape(t).replace("’", "'")).strip()

def is_scripture(t, full):
    return len(t) > 3 and all(norm(x).lower() in full for x in t.split("…") if x.strip())

def page_labels(src, full):
    """The label text nodes of one page (inside <x-dc>; the page <title> too)."""
    out = []
    t = re.search(r"<title>(.*?)</title>", src, re.S)
    if t: out.append(norm(t.group(1)))
    body = src.split("<x-dc>", 1)[-1]
    body = re.sub(r"<style>.*?</style>", "", body, flags=re.S)
    body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
    for m in TEXT.finditer(body):
        s = norm(m.group(1))
        if s and not is_scripture(s, full): out.append(s)
    for m in SVG_TEXT.finditer(body):                     # words drawn in a picture are never scripture, even "SHECHEM"
        s = norm(m.group(1))
        if s and re.search(r"[A-Za-z]", s): out.append(s)
    return out

def collect():
    sys.path.insert(0, str(HERE))
    import asv
    seen = {}
    for vol in sorted(p for p in (ROOT / "volumes").glob("*") if (p / "volume.json").exists()):
        meta = json.loads((vol / "volume.json").read_text(encoding="utf-8"))
        books = {c for init in HERE.glob("*/__init__.py") if f'"id": "{meta["id"]}"' in (t := init.read_text(encoding="utf-8"))
                 for c in re.findall(r'"book":\s*"(\w{3})"', t)}
        full = " ".join(norm(asv.Book(b).text()).lower() for b in books if b in asv.FILES)
        for p in sorted((vol / "pages").glob("*.dc.html")):
            for s in page_labels(p.read_text(encoding="utf-8"), full):
                seen.setdefault(s, set()).add(vol.name)
        for s in [meta["name"], meta["lede"]] + [x for c in meta["books"] for x in (c["name"], c["range"], c["blurb"])]:
            seen.setdefault(norm(s), set()).add(vol.name)
    I18N.mkdir(exist_ok=True)
    out = {s: sorted(v) for s, v in sorted(seen.items())}
    (I18N / "labels.json").write_bytes(json.dumps(out, indent=0, ensure_ascii=False).encode())
    print(len(out), "labels")

def table(lang):
    """tools/full/i18n/<lang>.json, or the parts in tools/full/i18n/<lang>/*.json merged: labels.json first, then the others
    by name, each overriding what came before (scoped.json aside: see scoped())."""
    f, d = I18N / f"{lang}.json", I18N / lang
    tab = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
    for part in sorted(d.glob("*.json"), key=lambda q: (q.name != "labels.json", q.name)) if d.is_dir() else []:
        if part.name != "scoped.json": tab.update(json.loads(part.read_text(encoding="utf-8")))
    return tab

def scoped(lang):
    """tools/full/i18n/<lang>/scoped.json: {"<volume id>/<page name prefix>": {label: translation}} for a label that must
    read differently on some pages ("The First Book of the" is "Третья книга" on the 1 Kings cover, "Первая книга" on the
    1 Chronicles one); build_volume lays them over the table for each page they match."""
    f = I18N / lang / "scoped.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}

# verse references are translated by rule, not by the table: the book's name or page abbreviation, then the numbers
# ("books" and "abbr" in tools/lang/<code>.json)
sys.path.insert(0, str(ROOT / "tools" / "lang"))
import langs
NUMS = r"\d+(?::\d+)?(?:\s*[–-]\s*\d+(?::\d+)?)?(?:[,;] ?\d+(?::\d+)?(?:\s*[–-]\s*\d+(?::\d+)?)?)*"
SEP = re.compile(r"( · | — )")

def ref_rule(part, lang):
    """'Genesis 1:3–4' -> 'Génesis 1:3–4', 'GEN 1:3' -> 'GN 1:3', 'Chapters 1 – 50' -> 'Capítulos 1 – 50'; None if not a ref."""
    L = langs.get(lang); names, abbr = L.get("books", {}), L.get("abbr", {})
    words = {**{k.upper(): v.upper().replace("{N}", "{n}") for k, v in names.items()}, **names, **abbr}
    for w in sorted(words, key=len, reverse=True):
        m = re.fullmatch(re.escape(w) + r" ?(" + NUMS + r"(?:\s*–\s*\d+)?)( ABRIDGED)?", part)
        if m:
            sp = " " if part[len(w):len(w) + 1] == " " else ""
            nums = renumber(BOOK_CODES.get(w.upper()), m.group(1), lang) if L.get("refs") == "text" else m.group(1)
            num = words[w].replace("{n}", nums) if "{n}" in words[w] else words[w] + sp + nums   # ja: "第{n}章"
            return num + (" " + L.get("abridged", "ABRIDGED") if m.group(2) else "")
    return None

# the English book names and page abbreviations of the refs, for "refs": "text" (a language whose references follow its
# own Bible's numbering: the Synodal's Psalm 22 is the ASV's 23)
BOOK_CODES = {k.upper(): v for k, v in {
    "Genesis": "GEN", "Exodus": "EXO", "Leviticus": "LEV", "Numbers": "NUM", "Deuteronomy": "DEU", "Joshua": "JOS",
    "Judges": "JDG", "Ruth": "RUT", "1 Samuel": "1SA", "2 Samuel": "2SA", "1 Kings": "1KI", "2 Kings": "2KI",
    "1 Chronicles": "1CH", "2 Chronicles": "2CH", "Ezra": "EZR", "Nehemiah": "NEH", "Esther": "EST", "Job": "JOB",
    "Psalms": "PSA", "Psalm": "PSA", "Proverbs": "PRO", "Ecclesiastes": "ECC", "Song of Solomon": "SNG", "Isaiah": "ISA",
    "Jeremiah": "JER", "Lamentations": "LAM", "Ezekiel": "EZK", "Daniel": "DAN", "Hosea": "HOS", "Joel": "JOL", "Amos": "AMO",
    "Obadiah": "OBA", "Jonah": "JON", "Micah": "MIC", "Nahum": "NAM", "Habakkuk": "HAB", "Zephaniah": "ZEP", "Haggai": "HAG",
    "Zechariah": "ZEC", "Malachi": "MAL", "GEN": "GEN", "EX": "EXO", "LEV": "LEV", "NUM": "NUM", "JDG": "JDG", "RUTH": "RUT",
    "NEH": "NEH", "DEUT": "DEU", "JOSH": "JOS", "1SAM": "1SA", "2SAM": "2SA",
    "1KGS": "1KI", "2KGS": "2KI", "1CHR": "1CH", "2CHR": "2CH", "EZRA": "EZR", "ESTH": "EST", "PS": "PSA", "PROV": "PRO",
    "ECCL": "ECC", "SONG": "SNG", "ISA": "ISA", "JER": "JER", "LAM": "LAM", "EZEK": "EZK", "DAN": "DAN", "HOS": "HOS",
    "JOEL": "JOL", "AMOS": "AMO", "OBAD": "OBA", "JONAH": "JON", "MIC": "MIC", "NAH": "NAM", "HAB": "HAB", "ZEPH": "ZEP",
    "HAG": "HAG", "ZECH": "ZEC", "MAL": "MAL"}.items()}
_LAST = {}
def renumber(code, nums, lang):
    """Chapter and verse numbers of an ASV ref ("23:1–6", "9–10", "51:1–19") in the numbering of the language's text, by its
    versemap (a verse of a block: the translated verse it falls in). A whole chapter is the chapter its verse 1 goes to;
    the end of a run of chapters, the chapter its last verse goes to unless only a verse or two spill over."""
    rules = langs.versemap(lang).get(code) if code else None
    if not rules: return nums
    def to(c, v, end=False):
        for (rc, a, b), (tc, tv, tw) in rules:
            if rc == c and a <= v <= b and v:
                if tw is None: return tc, tv + v - a
                k, m = b - a + 1, tw - tv + 1
                return tc, tv + ((v - a + 1) * m + k - 1) // k - 1 if end else tv + (v - a) * m // k
        return c, v
    def last(c):
        if code not in _LAST:
            sys.path.insert(0, str(HERE)); import asv
            _LAST[code] = {}
            for (cc, vv) in asv.parse(ROOT / "ref" / "eng-asv" / asv.FILES[code]): _LAST[code][cc] = max(vv, _LAST[code].get(cc, 0))
        return _LAST[code].get(c, 1)
    def chap_end(c):
        tc, tv = to(c, last(c), True); t1 = to(c, 1)[0]
        return t1 if tc != t1 and tv <= 2 else tc
    out, cur = [], None
    for sep, item in re.findall(r"(^|[,;] ?)([^,;]+)", nums):
        m = re.fullmatch(r"(\d+)(?::(\d+))?(?:(\s*[–-]\s*)(\d+)(?::(\d+))?)?", item.strip())
        if not m: out.append(sep + item); continue
        x, y, dash, z, w = m.groups()
        if sep.startswith(";"): cur = None
        if y is None and cur is not None and sep.startswith(","):          # ", 5": a verse of the chapter before
            x, y = cur, x
        if y is None:                                                   # chapters: "23", "9–10"
            a = to(int(x), 1)[0]; b = chap_end(int(z)) if z else a
            s = str(a) if a == b else f"{a}{dash}{b}"
            cur = None
        else:
            c, v = int(x), int(y); tc, tv = to(c, v)
            if z is None: s = f"{tc}:{tv}"
            else:
                c2, v2 = (int(z), int(w)) if w else (c, int(z))
                tc2, tv2 = to(c2, v2, True)
                s = f"{tc}:{tv}" if (tc2, tv2) == (tc, tv) else f"{tc}:{tv}{dash}{tv2}" if tc2 == tc else f"{tc}:{tv}{dash}{tc2}:{tv2}"
            cur = int(x)
            if sep.startswith(",") and m.group(2) is None: s = s.split(":", 1)[1]
        out.append(sep + s)
    return "".join(out)

def label(s, lang, tab):
    """One label in another language: the whole string from the table, else piece by piece (refs by rule)."""
    if s in tab: return tab[s]
    parts = SEP.split(s)
    out = []
    for p in parts:
        if SEP.fullmatch(p) or not p.strip(): out.append(p); continue
        q = p.strip()
        r = tab.get(q) or ref_rule(q, lang)
        out.append(p.replace(q, r) if r else p)
    return "".join(out)

SCRIPTURE = set()                    # the translated verses' own text, so a label lookup never touches scripture
def is_scripture_text(s): return any(s in t for t in SCRIPTURE) if len(s) > 12 else False

def translate(page, lang, tab=None):
    """A built page with every label replaced by its translation (text nodes only; scripture is untouched because it
    never matches an English label exactly)."""
    tab = table(lang) if tab is None else tab
    def sub(m):
        s = norm(m.group(1))
        if not s or is_scripture_text(s): return m.group(0)
        t = label(s, lang, tab)
        return m.group(0) if t == s else ">" + html.escape(t, quote=False) + "<"
    page = re.sub(r"<title>(.*?)</title>", lambda m: "<title>" + html.escape(label(norm(m.group(1)), lang, tab), quote=False) + "</title>", page, count=1)
    head, sep, body = page.partition("<x-dc>")
    body = HFIT.sub(hfit, FIT.sub(fit, TEXT.sub(sub, body)))
    room = langs.get(lang).get("accent_room")
    return head + sep + (COVER.sub(lambda m: lower(m, room), body) if room else body)

COVER = re.compile(r'<h1 style="([^"]*)">([^<]*)</h1>')
TALL = re.compile(r"[ÀÁÂÄÉÈÊËÍÌÎÏÓÒÔÖÚÙÛÜŸ]")
def lower(m, room):
    """A cover's book name (an h1 with no max-width) whose translated capitals carry accents: set smaller by the share room
    on the same baseline, so the accents clear the small line above it ("LE LIVRE DE") and nothing below moves (Anton's
    baseline sits (line-height - 1.506) / 2 + 1.1765 em below the top of its line). accent_room in tools/lang/<code>.json."""
    style, text = m.group(1), m.group(2)
    if "max-width" in style or not TALL.search(html.unescape(text)): return m.group(0)
    fs, lh = re.search(r"font-size: ([\d.]+)px", style), re.search(r"line-height: ([\d.]+);", style)
    if not fs: return m.group(0)
    f = float(fs.group(1)); base = (float(lh.group(1)) if lh else 1.0) - 1.506
    drop = (base / 2 + 1.1765) * f * room
    style = re.sub(r"top: ([\d.]+)px", lambda t: f"top: {float(t.group(1)) + drop:.0f}px", style, count=1)
    style = style.replace(fs.group(0), f"font-size: {f * (1 - room):.0f}px", 1)
    return f'<h1 style="{style}">{text}</h1>'

HFIT = re.compile(r'(<(?!text\b)\w+ [^>]*data-fit="([\d.]+)"[^>]*>)([^<]*)<')
def hfit(m):
    """An HTML title with data-fit="<px>" (a cover's book name in Anton) shrunk to its room when the translation runs
    longer: a display capital is taken as 0.55 em wide (a CJK character 1 em)."""
    tag, room = m.group(1), float(m.group(2))
    n = sum(1 / 0.55 if unicodedata.east_asian_width(ch) in "WF" else 1 for ch in html.unescape(m.group(3)).strip())
    fs = re.search(r'font-size: ([\d.]+)px', tag)
    if not n or not fs or n * float(fs.group(1)) * 0.55 <= room: return m.group(0)
    return tag.replace(fs.group(0), f"font-size: {room / (n * 0.55):.0f}px") + m.group(3) + "<"

FIT = re.compile(r'(<text [^>]*data-fit="([\d.]+)"[^>]*>)([^<]*)<')
def fit(m):
    """A drawn label with data-fit (genesis.art3.label(fit=)) made to fit its room: the letter-spacing goes first, then the
    font shrinks (IBM Plex Mono is 0.6 em a letter, a CJK character 1 em), never below 6 px."""
    tag, room = m.group(1), float(m.group(2))
    n = sum(1 / 0.6 if unicodedata.east_asian_width(ch) in "WF" else 1 for ch in html.unescape(m.group(3)))   # a CJK glyph is 1 em
    fs = float(re.search(r'font-size="([\d.]+)"', tag).group(1))
    ls = float((re.search(r'letter-spacing="([\d.]+)em"', tag) or [0, 0])[1])
    if not n or n * fs * (0.6 + ls) <= room: return m.group(0)
    ls2 = max(0.0, room / (n * fs) - 0.6)
    fs2 = fs if ls2 > 0 else max(6.0, room / (n * 0.6))
    tag = re.sub(r'letter-spacing="[\d.]+em"', f'letter-spacing="{ls2:.2f}em"', tag)
    tag = re.sub(r'font-size="[\d.]+"', f'font-size="{fs2:.1f}"', tag)
    return tag + m.group(3) + "<"

if __name__ == "__main__":
    if sys.argv[1] == "collect": collect()
    elif sys.argv[1] == "leftover":            # labels still in English on the built pages of a language (and in its
        # volume.json names, ledes and blurbs): leftover <lang> [volume ids …] [--out list.json] (all of them, for translating)
        args = sys.argv[2:]
        out = args.pop(args.index("--out") + 1) if "--out" in args else None
        args = [a for a in args if a != "--out"]
        lang, only = args[0], args[1:]
        tab = table(lang); left = {}
        known = json.loads((I18N / "labels.json").read_text(encoding="utf-8"))
        def pieces(s, where):
            if s in tab: return
            for q in (x.strip() for x in SEP.split(s) if x.strip() and not SEP.fullmatch(x)):
                if q in tab or ref_rule(q, lang) or re.fullmatch(r"[\d\s.,:;/–\-+×?%°'\"()·▸◂◼…]+|Vol\. \d+|\d+ [–-] \d+", q): continue
                left.setdefault(q, where)
        def nodes(p):                          # every text node of a page, drawn words too
            body = re.sub(r"<style>.*?</style>|<script.*?</script>", "", p.read_text(encoding="utf-8").split("<x-dc>", 1)[-1], flags=re.S)
            return {s for rx in (TEXT, SVG_TEXT) for m in rx.finditer(body) if re.search(r"[A-Za-z]", s := norm(m.group(1)))}
        for d in sorted((ROOT / "volumes" / lang).glob("*")):
            if not (d / "volume.json").exists() or (only and d.name not in only): continue
            # a node word for word on the English pages of the volume is still English, even one collect() took for
            # scripture ("KINGS", "BOOK I", a quoted law heading); a name that is the same in both languages maps to itself
            english = set().union(*(nodes(p) for p in (ROOT / "volumes" / d.name / "pages").glob("*.dc.html")))
            for p in sorted((d / "pages").glob("*.dc.html")):
                for s in nodes(p):
                    if s in known or s in english: pieces(s, d.name)
            en = json.loads((ROOT / "volumes" / d.name / "volume.json").read_text(encoding="utf-8"))
            for s in [en["name"], en["lede"]] + [x for c in en["books"] for x in (c["name"], c["range"], c["blurb"])]:
                pieces(norm(s), d.name)
        print(len(left), "English labels left"); [print(f"  {v}: {k}") for k, v in list(left.items())[:80]]
        if out: pathlib.Path(out).write_bytes(json.dumps(sorted(left), ensure_ascii=False, indent=0).encode())
    elif sys.argv[1] == "missing":
        tab, labels = table(sys.argv[2]), json.loads((I18N / "labels.json").read_text(encoding="utf-8"))
        miss = [s for s in labels if s not in tab]
        print(len(miss), "missing"); [print(s) for s in miss]
