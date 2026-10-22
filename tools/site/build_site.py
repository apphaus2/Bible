"""Build the static website (deployed by hand to Cloudflare, bible.apphaus.us) from the volumes, in one language.

Usage: BIBLE_LANG=es python3 tools/site/build_site.py <out_dir> <key>=<dir> ... [--peer <lang>=<volumes dir> ...]
  - each key names a volume folder (volumes/<id>/ or volumes/<lang>/<id>/): canvas.json, volume.json, pages/
  - each --peer names another language's volumes, for the language menu: every page links to the page in that language
    that covers the same verses (page counts differ between languages, so pages are matched by verse, not by number)
The language's site root is <out_dir> (English: the domain root; another language: <out>/<lang>/, served at /<lang>/).
Every page URL is <path>/<book-or-chapter>/<slug>.html, two levels deep, so relative links are the same everywhere."""
import os, json, re, sys, html, pathlib, unicodedata
ROOT = pathlib.Path(__file__).resolve().parents[2]
args = [a for a in sys.argv[1:] if not a.startswith("--peer")]
out = pathlib.Path(args[0])
SRC = {k: pathlib.Path(v) for k, v in (a.split("=", 1) for a in args[1:])}
PEERS = {k: pathlib.Path(v) for k, v in (a.split("=", 1)[1].split("=", 1) for a in sys.argv[1:] if a.startswith("--peer"))}

# ── the language ──
LANG = os.environ.get("BIBLE_LANG", "en")
sys.path.insert(0, str(ROOT / "tools" / "lang"))
import langs                                                  # tools/lang/<code>.json: the text, credit and the site's words
LANGS = {k: v["name"] for k, v in langs.LANGS.items()}         # each language named in itself, for the menu
L = langs.get(LANG)
TEXT = (L["text"], L["credit"])
CREDIT = TEXT[1]
HOME = "https://bible.apphaus.us/"
def home(lang): return HOME if lang == "en" else f"{HOME}{lang}/"
UI = {LANG: L["ui"]}
def T(key, **kw): return UI[LANG][key].format(**kw)

# ── one volume per Bible book, described by volumes/<id>/volume.json ──
VOLUMES = []
for key, d in SRC.items():
    vj = d / "volume.json"
    if not vj.exists(): continue
    V = json.loads(vj.read_text(encoding="utf-8"))
    V.update(edition="full", path=V["id"], key=key)
    for c in V["books"]:
        c["label"] = langs.numbered(UI[LANG]["chapter"], c["num"])
        c["match"] = (lambda pre: (lambda n: n.startswith(tuple(pre))))(c["prefixes"])
    VOLUMES.append(V)
VOLUMES.sort(key=lambda v: v.get("order", 0))
SERIES = VOLUMES
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Anton&family=Archivo+Narrow:wght@600;700&family=IBM+Plex+Mono:wght@500;600&family=Noto+Sans+JP:wght@900' + "".join("&" + q for q in langs.font_query(LANG)) + '&display=swap" rel="stylesheet">'
# ── the Bible text, one PDF per book (tools/book/asv_pdf.py; rebuild_site.py copies asv/ in when it exists) ──
ASV_CODES = {}                      # "1 Samuel" -> "1SA", from the \h line of each book of the language's text
for f in sorted((ROOT / "ref" / TEXT[0]).glob("[0-9][0-9]-*.usfm")):
    m = re.search(r"^\\h (.+?)\s*$", f.read_text(encoding="utf-8"), re.M)
    if m: ASV_CODES[m.group(1)] = re.match(r"\d\d-(\w{3})", f.name).group(1)
ASV_CODES.update(L.get("codes", {}))                          # where the text's own book names differ from the labels
ASV_BOOKS = json.loads((out / "asv" / "index.json").read_text(encoding="utf-8")) if (out / "asv" / "index.json").exists() else {}
def asv_where(ref):
    """(book code, chapter) that a ref like "Genesis 24:1–25:18" or "1 Samuel 1 – 3" starts in, or None."""
    for name in sorted(ASV_CODES, key=len, reverse=True):
        m = re.match(re.escape(name) + r" (\d+)", ref)
        if m: return ASV_CODES[name], m.group(1)
def asv_href(up, ref=""):
    """Link to the text at the chapter a ref starts in: the book's own PDF (asv/GEN.pdf#page=N, small files like the
    HistoryX reader's); with no ref, the list of books on the home page."""
    w = asv_where(ref)
    if w and w[0] in ASV_BOOKS:
        b = ASV_BOOKS[w[0]]; pg = b["chapters"].get(w[1]) or next(iter(b["chapters"].values()))
        return f"{up}{b['file']}#page={pg[0]}"
    return f"{up}index.html#text"
def asv_button(up, ref=""):
    """The reader's top-right link to the text of the page (📖 p. N: the page of the text PDF where its chapter starts)."""
    w = asv_where(ref)
    if not w or w[0] not in ASV_BOOKS: return ""
    b = ASV_BOOKS[w[0]]; pg = b["chapters"].get(w[1]) or next(iter(b["chapters"].values()))
    return f'<a class="btn asv" href="{asv_href(up, ref)}" title="{esc(T("pdf_of", t=b["title"], c=w[1], k=CREDIT))}">📖 p. {pg[1]}</a>'
def asv_credit(up, ref=""):
    """The translation's credit in every footer, linked to the text when the PDFs are on the site."""
    if not ASV_BOOKS: return f"<span>{CREDIT}</span>"
    return f'<a href="{asv_href(up, ref)}" title="{esc(T("read_in", r=(ref + " ") if ref else "", c=CREDIT))}">{CREDIT}</a>'

# ── the manga by book: EPUB and reading PDF (tools/book/downloads.py; rebuild_site.py copies download/<lang>/ in) ──
DOWNLOADS = json.loads((out / "download" / LANG / "index.json").read_text(encoding="utf-8")) if (out / "download" / LANG / "index.json").exists() else {}
def mb(n): return f"{n / 1e6:.1f} MB" if n < 1e7 else f"{n / 1e6:.0f} MB"
def downloads(up, S, cls="cta alt"):
    """Download buttons for a volume: the EPUB, then the PDF (or its parts, each named by its chapters)."""
    d = DOWNLOADS.get(S["id"])
    if not d: return ""
    base = f"{home(LANG)}download/{LANG}/"   # absolute, like the manifest's download URLs
    out_ = [f'<a class="{cls}" href="{base}{d["epub"]["file"]}" download title="{esc(T("epub_of", n=S["name"], s=mb(d["epub"]["size"])))}">EPUB · {mb(d["epub"]["size"])}</a>']
    for x in d["pdf"]:
        name = "PDF" if len(d["pdf"]) == 1 else f'PDF · {esc(x["range"])}'
        out_.append(f'<a class="{cls}" href="{base}{x["file"]}" download title="{esc(x["range"])}, {T("pages_n", n=x["pages"])} ({mb(x["size"])})">{name} · {mb(x["size"])}</a>')
    return f'<p class="dl"><span class="dl-h">{T("download")} {esc(S["name"])}</span>{"".join(out_)}</p>'

def slug(t):
    t = re.sub(r"^(B\d+ · )?\d+ · ", "", t)
    t = "".join(ch for ch in unicodedata.normalize("NFKD", t) if not unicodedata.combining(ch))   # "Génesis" -> "genesis"
    return re.sub(r"[^a-z0-9]+", "-", t.lower().replace("·", " ")).strip("-")
def numbered_slug(i, t):
    """'03-the-threshing-floor'; just '03' when the title has words but no Latin letters to slug (Japanese, Chinese ...).
    An untitled page keeps its old name ('03-')."""
    s = slug(t)
    return f"{i:02d}-{s}" if s or not re.sub(r"^(B\d+ · )?\d+ · ", "", t).strip() else f"{i:02d}"
def esc(s): return html.escape(s, quote=True)

def convert(path):
    s = path.read_text(encoding="utf-8")
    title = re.search(r"<title>(.*?)</title>", s).group(1)
    body = re.search(r"<x-dc>(.*)</x-dc>", s, re.S).group(1)
    style = re.search(r"<helmet>.*?<style>(.*?)</style>.*?</helmet>", body, re.S).group(1)
    body = re.sub(r"<helmet>.*?</helmet>", "", body, flags=re.S).replace("{{accent}}", "#D7261E")
    return title, style.strip(), body.strip()

def src_dir(S): return SRC[S["key"]] / ("pages" if S["edition"] == "full" else "")

def start(ref):
    """Where a page starts, for matching pages across languages: (chapter, verse); a chapter title page (chapter, 0)."""
    m = re.search(r"(\d+):(\d+)", ref)
    if m: return int(m.group(1)), int(m.group(2))
    m = re.search(r"(\d+)", ref)
    return (int(m.group(1)), 0) if m else (0, 0)

def chapter_pages(vdir, V, b, canvas):
    """[(slug, ref)] of one manga chapter of a volume folder."""
    names = [n for n in canvas["order"] if n.startswith(tuple(b["prefixes"]))]
    out_ = []
    for i, n in enumerate(names):
        t = canvas["boards"][n].get("title", n)
        ref = re.search(r"<title>(.*?)</title>", (vdir / "pages" / n).read_text(encoding="utf-8")).group(1).partition(" — ")[0]
        out_.append((f"{numbered_slug(i, t)}", ref))
    return out_

# the other languages' pages, for the language menu: {lang: {(volume id, chapter dir): [(slug, start)]}}
PEER = {}
for lang, root in PEERS.items():
    PEER[lang] = {}
    for vj in root.glob("*/volume.json"):
        V = json.loads(vj.read_text(encoding="utf-8")); canvas = json.loads((vj.parent / "canvas.json").read_text(encoding="utf-8"))
        for b in V["books"]:
            PEER[lang][(V["id"], b["dir"])] = [(s, start(r)) for s, r in chapter_pages(vj.parent, V, b, canvas)]

def lang_menu(vol=None, chap=None, i=None, ref=None):
    """The language dropdown: each language named in itself, linking to the same page there when it exists (the page of
    that language whose verses start at or before this page's), else to that chapter, else to that language's home."""
    if not PEER: return ""
    items = [f'<li><span aria-current="true" lang="{LANG}">{LANGS[LANG]}</span></li>']
    for lang in sorted(PEER, key=lambda l: LANGS.get(l, l)):
        url = home(lang)
        pages = PEER[lang].get((vol, chap)) if vol else None
        if pages:
            url += f"{vol}/{chap}/"
            if i is not None:
                me = start(ref or "")
                j = 0 if i == 0 else max((k for k, (_, s) in enumerate(pages) if s <= me), default=0)
                url += f"{pages[j][0]}.html"
            else: url += "index.html"
        items.append(f'<li><a href="{url}" lang="{lang}" hreflang="{lang}">{LANGS.get(lang, lang)}</a></li>')
    return (f'<details class="lang"><summary aria-label="{T("language")}">{LANGS[LANG]}</summary>'
            f'<ul>{"".join(items)}</ul></details>')

out.mkdir(parents=True, exist_ok=True)
(out / "assets").mkdir(exist_ok=True); (out / "thumbs").mkdir(exist_ok=True)
manifest = {"title": "Bible Manga", "lang": LANG, "series": []}
FLAT = {"full": []}   # every chapter in reading order, for prev/next
for S in SERIES:
    canvas = json.loads((SRC[S["key"]] / "canvas.json").read_text(encoding="utf-8"))
    ms = {"id": S["id"], "path": S["path"], "edition": S["edition"], "title": S["name"], "books": []}
    for b in S["books"]:
        b["series"] = S
        names = [n for n in canvas["order"] if b["match"](n)]
        pages = []
        for i, n in enumerate(names):
            t = canvas["boards"][n].get("title", n)
            title, style, body = convert(src_dir(S) / n)
            ref, _, heading = title.partition(" — ")
            if n == "Main.dc.html": ref, heading = b["range"], T("cover")
            pm = re.search(r"— (\d+) —", body)
            num = langs.numbered(UI[LANG]["page"], int(pm.group(1))) if pm else (T("cover") if n == "Main.dc.html" else T("title"))
            pages.append({"file": n, "slug": f"{numbered_slug(i, t)}", "label": re.sub(r'^B\d+ · ', '', t), "heading": heading or t,
                          "ref": ref, "num": num, "style": style, "body": body})
        b["pages"] = pages; FLAT[S["edition"]].append(b)
        ms["books"].append({"id": b["dir"], "title": f"{b['label']}: {b['name']}", "range": b["range"], "url": f"{S['path']}/{b['dir']}/",
            "pages": [{"title": p["heading"], "ref": p["ref"], "url": f"{S['path']}/{b['dir']}/{p['slug']}.html",
                       "thumb": f"thumbs/{S['thumb']}{b['dir']}-{p['slug']}.jpg", "src": f"{S['key']}/{p['file']}"} for p in pages]})
    manifest["series"].append(ms)
def thumb(b, p): return f"{b['series']['thumb']}{b['dir']}-{p['slug']}.jpg"
def href(frm, b, p):
    """Relative link from book `frm` to page p of book b."""
    if b is frm: return f"{p['slug']}.html"
    if b["series"] is frm["series"]: return f"../{b['dir']}/{p['slug']}.html"
    return f"../../{b['series']['path']}/{b['dir']}/{p['slug']}.html"

def bar(crumbs, extra="", menu=""):
    c = ' <span aria-hidden="true">/</span> '.join(crumbs)
    return f'<header class="bar"><nav class="crumbs" aria-label="Breadcrumb">{c}</nav><div class="tools">{menu}{extra}</div></header>'

def edition_tag(S): return ""

# reader pages
for ed, chain in FLAT.items():
  for bi, b in enumerate(chain):
    S = b["series"]; SN = S["name"] + edition_tag(S); L = b["label"]
    P = b["pages"]; d = out / S["path"] / b["dir"]; d.mkdir(parents=True, exist_ok=True)
    crumbs0 = ['<a href="../../index.html">Bible Manga</a>', f'<a href="../../index.html#{S["path"]}">{SN}</a>']
    for i, p in enumerate(P):
        prev = P[i-1]["slug"] + ".html" if i > 0 else (href(b, chain[bi-1], chain[bi-1]["pages"][-1]) if bi > 0 else None)
        nxt = P[i+1]["slug"] + ".html" if i < len(P)-1 else (href(b, chain[bi+1], chain[bi+1]["pages"][0]) if bi < len(chain)-1 else None)
        links = (f'<link rel="prev" href="{prev}">' if prev else "") + (f'<link rel="next" href="{nxt}">' if nxt else "")
        pn = f'<a class="btn" href="{prev}" rel="prev">{T("prev")}</a>' if prev else f'<span class="btn off" aria-disabled="true">{T("prev")}</span>'
        nn = f'<a class="btn" href="{nxt}" rel="next">{T("next")}</a>' if nxt else f'<span class="btn off" aria-disabled="true">{T("next")}</span>'
        desc = f"{p['heading']} ({p['ref']}) — {SN} {L}: {b['name']}, {T('desc')}"
        (d / f"{p['slug']}.html").write_text(f'''<!doctype html>
<html lang="{LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p['heading'])} · {SN} {L} · Bible Manga</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(p['heading'])} · {SN} {L}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="../../thumbs/{thumb(b, p)}">
{links}
{FONTS}
<link rel="stylesheet" href="../../assets/site.css">
<style>{p['style']}</style>
</head>
<body class="reader">
{bar(crumbs0 + [f'<a href="index.html">{L}</a>', f'<span aria-current="page">{esc(p["num"])}</span>'],
     f'<div class="pager">{asv_button("../../", p["ref"])}{pn}{nn}</div>', lang_menu(S["id"], b["dir"], i, p["ref"]))}
<main class="stage" id="stage"><h1 class="sr">{esc(p['heading'])} — {esc(p['ref'])}</h1><div class="sheet" id="sheet">{p['body']}</div></main>
<footer class="foot"><span>{esc(p['ref'])} · {esc(p['heading'])}</span>{asv_credit("../../", p['ref'])}</footer>
<script src="../../assets/site.js"></script>
</body>
</html>
''', encoding="utf-8")
    cards = "\n".join(f'''<li><a class="card" href="{p['slug']}.html"><img src="../../thumbs/{thumb(b, p)}" alt="{esc(p['heading'])}" width="380" height="540" loading="lazy"><span class="num">{esc(p['num'])}</span><span class="h">{esc(p['heading'])}</span><span class="ref">{esc(p['ref'])}</span></a></li>''' for p in P)
    text = f'<a class="cta alt" href="{asv_href("../../", b["range"])}">{esc(b["range"])} {T("in_text", c=CREDIT)}</a>' if ASV_BOOKS else ""
    (d / "index.html").write_text(f'''<!doctype html>
<html lang="{LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{SN} {L}: {b['name']} · Bible Manga</title>
<meta name="description" content="{esc(b['range'])}: {esc(b['blurb'])}">
<meta property="og:image" content="../../thumbs/{thumb(b, P[0])}">
{FONTS}
<link rel="stylesheet" href="../../assets/site.css">
</head>
<body class="index">
{bar(crumbs0 + [f'<span aria-current="page">{L}</span>'], menu=lang_menu(S["id"], b["dir"]))}
<main class="wrap">
  <section class="hero">
    <p class="kicker">{SN} · {L} · {esc(b['range'])}</p>
    <h1>{esc(b['name'])}</h1>
    <p class="lede">{esc(b['blurb'])}</p>
    <a class="cta" href="{P[0]['slug']}.html">{T("start")}</a>{text}
    {downloads("../../", S)}
  </section>
  <h2 class="sec">{T("pages")}</h2>
  <ol class="grid">
{cards}
  </ol>
</main>
<footer class="foot"><span>Bible Manga · {SN}</span>{asv_credit("../../", b['range'])}</footer>
</body>
</html>
''', encoding="utf-8")

# home
def book_card(b):
    S = b["series"]; p0 = b["pages"][0]
    return f'''<li><a class="book" href="{S['path']}/{b['dir']}/index.html"><img src="thumbs/{thumb(b, p0)}" alt="{esc(T('cover_of', s=S['name'], l=b['label']))}" width="380" height="540" loading="lazy"><span class="kicker">{b['label']} · {esc(b['range'])}</span><span class="h">{esc(b['name'])}</span><span class="ref">{esc(b['blurb'])}</span><span class="count">{T("pages_n", n=len(b['pages'])-1)}</span></a></li>'''
def toc_entry(b):
    S = b["series"]
    return (f'''<li><h3><a href="{S['path']}/{b['dir']}/index.html">{S['name']}{edition_tag(S)} · {b['label']}: {esc(b['name'])}</a></h3><ol>'''
            + "".join(f'<li><a href="{S["path"]}/{b["dir"]}/{p["slug"]}.html"><span>{esc(p["num"])}</span> {esc(p["heading"])} <em>{esc(p["ref"])}</em></a></li>' for p in b["pages"]) + "</ol></li>")
def section(S, cls):
    wide = any(unicodedata.east_asian_width(ch) in "WF" for ch in S["name"])           # a CJK name needs no kanji beside it
    kanji = "" if wide else f' <span lang="ja">{S["kanji"]}</span>'
    return f'''  <h3 class="{cls}" id="{S['path']}">{S['name']}{kanji}</h3>
  <p class="lede">{esc(S['lede'])}</p>
  {downloads("", S)}
  <ol class="grid books">
{chr(10).join(book_card(b) for b in S['books'])}
  </ol>'''
full_secs = "\n".join(section(S, "sec") for S in VOLUMES)
first = FLAT["full"][0]
home_text_cta = f'<a class="cta alt" href="#text">{T("the_text", c=CREDIT)}</a>' if ASV_BOOKS else ""
text_sec = "" if not ASV_BOOKS else f'''  <h2 class="sec" id="text">{T("text")}</h2>
  <p class="lede">{esc(T("text_lede", c=CREDIT))}</p>
  <ol class="asv-books">{"".join(f'<li><a href="{b["file"]}">{esc(b["title"])}</a></li>' for b in ASV_BOOKS.values())}</ol>
'''
vol_names = UI[LANG].get("list_sep", ", ").join(v["name"] for v in VOLUMES) or "—"   # ja "、"
(out / "index.html").write_text(f'''<!doctype html>
<html lang="{LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bible Manga</title>
<meta name="description" content="{esc(T("meta", c=CREDIT))}">
<meta property="og:image" content="thumbs/{thumb(first, first['pages'][0])}">
{"".join(f'<link rel="alternate" hreflang="{l}" href="{home(l)}">' for l in [LANG, *PEER])}
{FONTS}
<link rel="stylesheet" href="assets/site.css">
</head>
<body class="index home">
{bar(['<span aria-current="page">Bible Manga</span>'], menu=lang_menu())}
<main class="wrap">
  <section class="hero">
    <p class="kicker">Bible Manga · {" · ".join(v["kanji"] for v in VOLUMES)}</p>
    <h1>Bible Manga</h1>
    <p class="lede">{esc(T("lede", c=CREDIT, v=vol_names))}</p>
    <a class="cta" href="{first['series']['path']}/{first['dir']}/{first['pages'][0]['slug']}.html">{T("begin")}</a>{home_text_cta}
  </section>
  <h2 class="sec">{T("books")}</h2>
{full_secs}
{text_sec}  <h2 class="sec">{T("all")}</h2>
  <ol class="toc">
{chr(10).join(toc_entry(b) for b in FLAT["full"])}
  </ol>
</main>
<footer class="foot"><span>Bible Manga</span>{asv_credit("")}</footer>
</body>
</html>
''', encoding="utf-8")
if ASV_BOOKS: manifest["text"] = {"title": CREDIT, "books": {c: {"title": b["title"], "url": b["file"]} for c, b in ASV_BOOKS.items()}}
if DOWNLOADS: manifest["downloads"] = {LANG: {v: {"epub": f"{home(LANG)}download/{LANG}/{d['epub']['file']}",
                                                 "pdf": [{"url": f"{home(LANG)}download/{LANG}/{x['file']}", "range": x["range"]} for x in d["pdf"]]}
                                             for v, d in DOWNLOADS.items()}}
(out / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
(out / ".nojekyll").write_text("")
print("built", sum(len(b["pages"]) for e in FLAT.values() for b in e), "pages", f"({LANG})")
