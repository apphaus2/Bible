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
    """tools/full/i18n/<lang>.json, or the parts in tools/full/i18n/<lang>/*.json merged."""
    f, d = I18N / f"{lang}.json", I18N / lang
    tab = json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
    for part in sorted(d.glob("*.json")) if d.is_dir() else []:
        tab.update(json.loads(part.read_text(encoding="utf-8")))
    return tab

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
            num = words[w].replace("{n}", m.group(1)) if "{n}" in words[w] else words[w] + sp + m.group(1)   # ja: "第{n}章"
            return num + (" " + L.get("abridged", "ABRIDGED") if m.group(2) else "")
    return None

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
    return head + sep + FIT.sub(fit, TEXT.sub(sub, body))

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
    elif sys.argv[1] == "leftover":            # labels still in English on the built pages of a language
        lang = sys.argv[2]; tab = table(lang); left = {}
        known = json.loads((I18N / "labels.json").read_text(encoding="utf-8"))
        for p in sorted((ROOT / "volumes" / lang).glob("*/pages/*.dc.html")):
            body = p.read_text(encoding="utf-8").split("<x-dc>", 1)[-1]
            for m in TEXT.finditer(re.sub(r"<style>.*?</style>", "", body, flags=re.S)):
                s = norm(m.group(1))
                if s in tab or s not in known: continue
                for q in (x.strip() for x in SEP.split(s) if x.strip() and not SEP.fullmatch(x)):
                    if q in tab or ref_rule(q, lang) or re.fullmatch(r"[\d\s.,:;/–\-+×?%°'\"()·▸◂◼…]+|Vol\. \d+|\d+ [–-] \d+", q): continue
                    left.setdefault(q, p.parent.parent.name)
        print(len(left), "English labels left"); [print(f"  {v}: {k}") for k, v in list(left.items())[:80]]
    elif sys.argv[1] == "missing":
        tab, labels = table(sys.argv[2]), json.loads((I18N / "labels.json").read_text(encoding="utf-8"))
        miss = [s for s in labels if s not in tab]
        print(len(miss), "missing"); [print(s) for s in miss]
