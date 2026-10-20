"""Build the static website (_site/, deployed by GitHub Actions to bible.apphaus.us and GitHub Pages) from the volumes.

Usage: python3 tools/site/build_site.py <out_dir> <key>=<dir> ...
  - each key names a volume folder (volumes/<id>/): canvas.json, volume.json, pages/
Every page URL is <path>/<book-or-chapter>/<slug>.html, two levels deep, so relative links are the same everywhere."""
import json, re, sys, html, pathlib
out = pathlib.Path(sys.argv[1])
SRC = {k: pathlib.Path(v) for k, v in (a.split("=", 1) for a in sys.argv[2:])}

# ── one volume per Bible book, described by volumes/<id>/volume.json ──
VOLUMES = []
for key, d in SRC.items():
    vj = d / "volume.json"
    if not vj.exists(): continue
    V = json.loads(vj.read_text())
    V.update(edition="full", path=V["id"], key=key)
    for c in V["books"]:
        c["label"] = f"Chapter {c['num']}"
        c["match"] = (lambda pre: (lambda n: n.startswith(tuple(pre))))(c["prefixes"])
    VOLUMES.append(V)
VOLUMES.sort(key=lambda v: v.get("order", 0))
SERIES = VOLUMES
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Anton&family=Archivo+Narrow:wght@600;700&family=IBM+Plex+Mono:wght@500;600&family=Noto+Sans+JP:wght@900&display=swap" rel="stylesheet">'
# ── the ASV text, one PDF per book (tools/book/asv_pdf.py; rebuild_site.py copies asv/ in when it exists) ──
ASV_CODES = {}                      # "1 Samuel" -> "1SA", from the \h line of each book in ref/asv
for f in sorted((pathlib.Path(__file__).resolve().parents[2] / "ref" / "asv").glob("[0-9][0-9]-*.usfm")):
    m = re.search(r"^\\h (.+?)\s*$", f.read_text(encoding="utf-8"), re.M)
    if m: ASV_CODES[m.group(1)] = re.match(r"\d\d-(\w{3})", f.name).group(1)
ASV_BOOKS = json.loads((out / "asv" / "index.json").read_text(encoding="utf-8")) if (out / "asv" / "index.json").exists() else {}
def asv_where(ref):
    """(book code, chapter) that a ref like "Genesis 24:1–25:18" or "1 Samuel 1 – 3" starts in, or None."""
    for name in sorted(ASV_CODES, key=len, reverse=True):
        m = re.match(re.escape(name) + r" (\d+)", ref)
        if m: return ASV_CODES[name], m.group(1)
def asv_href(up, ref=""):
    """Link to the ASV text at the chapter a ref starts in: the book's own PDF (asv/GEN.pdf#page=N, small files like the
    HistoryX reader's); with no ref, the list of books on the home page."""
    w = asv_where(ref)
    if w and w[0] in ASV_BOOKS:
        b = ASV_BOOKS[w[0]]; pg = b["chapters"].get(w[1]) or next(iter(b["chapters"].values()))
        return f"{up}{b['file']}#page={pg[0]}"
    return f"{up}index.html#text"
def asv_button(up, ref=""):
    """The reader's top-right link to the text of the page (📖 p. N: the page of the ASV PDF where its chapter starts)."""
    w = asv_where(ref)
    if not w or w[0] not in ASV_BOOKS: return ""
    b = ASV_BOOKS[w[0]]; pg = b["chapters"].get(w[1]) or next(iter(b["chapters"].values()))
    return f'<a class="btn asv" href="{asv_href(up, ref)}" title="{esc(b["title"])} {w[1]} in the ASV (PDF)">📖 p. {pg[1]}</a>'
def asv_credit(up, ref=""):
    """The "ASV" credit of every footer, linked to the text when the PDF is on the site."""
    if not ASV_BOOKS: return "<span>ASV</span>"
    return f'<a href="{asv_href(up, ref)}" title="Read {esc(ref) + " " if ref else ""}in the ASV (PDF)">ASV</a>'

# ── the manga by book: EPUB and reading PDF (tools/book/downloads.py; rebuild_site.py copies download/<lang>/ in) ──
LANG = "en"
HOME = "https://bible.apphaus.us/"
DOWNLOADS = json.loads((out / "download" / LANG / "index.json").read_text()) if (out / "download" / LANG / "index.json").exists() else {}
def mb(n): return f"{n / 1e6:.1f} MB" if n < 1e7 else f"{n / 1e6:.0f} MB"
def downloads(up, S, cls="cta alt"):
    """Download buttons for a volume: the EPUB, then the PDF (or its parts, each named by its chapters)."""
    d = DOWNLOADS.get(S["id"])
    if not d: return ""
    base = f"{HOME}download/{LANG}/"         # absolute: the GitHub Pages mirror does not carry the files (its 1 GB limit)
    out_ = [f'<a class="{cls}" href="{base}{d["epub"]["file"]}" download title="{esc(S["name"])} as an EPUB ({mb(d["epub"]["size"])})">EPUB · {mb(d["epub"]["size"])}</a>']
    for x in d["pdf"]:
        name = "PDF" if len(d["pdf"]) == 1 else f'PDF · {esc(x["range"])}'
        out_.append(f'<a class="{cls}" href="{base}{x["file"]}" download title="{esc(x["range"])}, {x["pages"]} pages ({mb(x["size"])})">{name} · {mb(x["size"])}</a>')
    return f'<p class="dl"><span class="dl-h">Download {esc(S["name"])}</span>{"".join(out_)}</p>'

def slug(t):
    t = re.sub(r"^(B\d+ · )?\d+ · ", "", t)
    return re.sub(r"[^a-z0-9]+", "-", t.lower().replace("·", " ")).strip("-")
def esc(s): return html.escape(s, quote=True)

def convert(path):
    s = path.read_text()
    title = re.search(r"<title>(.*?)</title>", s).group(1)
    body = re.search(r"<x-dc>(.*)</x-dc>", s, re.S).group(1)
    style = re.search(r"<helmet>.*?<style>(.*?)</style>.*?</helmet>", body, re.S).group(1)
    body = re.sub(r"<helmet>.*?</helmet>", "", body, flags=re.S).replace("{{accent}}", "#D7261E")
    return title, style.strip(), body.strip()

def src_dir(S): return SRC[S["key"]] / ("pages" if S["edition"] == "full" else "")

out.mkdir(parents=True, exist_ok=True)
(out / "assets").mkdir(exist_ok=True); (out / "thumbs").mkdir(exist_ok=True)
manifest = {"title": "Bible Manga", "series": []}
FLAT = {"full": []}   # every chapter in reading order, for prev/next
for S in SERIES:
    canvas = json.loads((SRC[S["key"]] / "canvas.json").read_text())
    ms = {"id": S["id"], "path": S["path"], "edition": S["edition"], "title": S["name"], "books": []}
    for b in S["books"]:
        b["series"] = S
        names = [n for n in canvas["order"] if b["match"](n)]
        pages = []
        for i, n in enumerate(names):
            t = canvas["boards"][n].get("title", n)
            title, style, body = convert(src_dir(S) / n)
            ref, _, heading = title.partition(" — ")
            if "Cover" in t: ref, heading = b["range"], "Cover"
            if S["edition"] == "full":
                pm = re.search(r"— (\d+) —", body)
                num = f"Page {int(pm.group(1))}" if pm else ("Cover" if n == "Main.dc.html" else "Title")
            else:
                num = "Cover" if i == 0 else f"Page {i}"
            pages.append({"file": n, "slug": f"{i:02d}-{slug(t)}", "label": re.sub(r'^B\d+ · ', '', t), "heading": heading or t,
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

def bar(crumbs, extra=""):
    c = ' <span aria-hidden="true">/</span> '.join(crumbs)
    return f'<header class="bar"><nav class="crumbs" aria-label="Breadcrumb">{c}</nav>{extra}</header>'

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
        pn = f'<a class="btn" href="{prev}" rel="prev">‹ Prev</a>' if prev else '<span class="btn off" aria-disabled="true">‹ Prev</span>'
        nn = f'<a class="btn" href="{nxt}" rel="next">Next ›</a>' if nxt else '<span class="btn off" aria-disabled="true">Next ›</span>'
        desc = f"{p['heading']} ({p['ref']}) — {SN} {L}: {b['name']}, a manga adaptation of the Bible."
        (d / f"{p['slug']}.html").write_text(f'''<!doctype html>
<html lang="en">
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
     f'<div class="pager">{asv_button("../../", p["ref"])}{pn}{nn}</div>')}
<main class="stage" id="stage"><h1 class="sr">{esc(p['heading'])} — {esc(p['ref'])}</h1><div class="sheet" id="sheet">{p['body']}</div></main>
<footer class="foot"><span>{esc(p['ref'])} · {esc(p['heading'])}</span>{asv_credit("../../", p['ref'])}</footer>
<script src="../../assets/site.js"></script>
</body>
</html>
''')
    cards = "\n".join(f'''<li><a class="card" href="{p['slug']}.html"><img src="../../thumbs/{thumb(b, p)}" alt="{esc(p['heading'])}" width="380" height="540" loading="lazy"><span class="num">{esc(p['num'])}</span><span class="h">{esc(p['heading'])}</span><span class="ref">{esc(p['ref'])}</span></a></li>''' for p in P)
    note = ""
    text = f'<a class="cta alt" href="{asv_href("../../", b["range"])}">{esc(b["range"])} in the ASV ›</a>' if ASV_BOOKS else ""
    (d / "index.html").write_text(f'''<!doctype html>
<html lang="en">
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
{bar(crumbs0 + [f'<span aria-current="page">{L}</span>'])}
<main class="wrap">
  <section class="hero">
    <p class="kicker">{SN} · {L} · {esc(b['range'])}</p>
    <h1>{esc(b['name'])}</h1>
    <p class="lede">{esc(b['blurb'])}</p>{note}
    <a class="cta" href="{P[0]['slug']}.html">Start reading ›</a>{text}
    {downloads("../../", S)}
  </section>
  <h2 class="sec">Pages</h2>
  <ol class="grid">
{cards}
  </ol>
</main>
<footer class="foot"><span>Bible Manga · {SN}</span>{asv_credit("../../", b['range'])}</footer>
</body>
</html>
''')

# home
def book_card(b):
    S = b["series"]; p0 = b["pages"][0]
    return f'''<li><a class="book" href="{S['path']}/{b['dir']}/index.html"><img src="thumbs/{thumb(b, p0)}" alt="{S['name']} {b['label']} cover" width="380" height="540" loading="lazy"><span class="kicker">{b['label']} · {esc(b['range'])}</span><span class="h">{esc(b['name'])}</span><span class="ref">{esc(b['blurb'])}</span><span class="count">{len(b['pages'])-1} pages</span></a></li>'''
def toc_entry(b):
    S = b["series"]
    return (f'''<li><h3><a href="{S['path']}/{b['dir']}/index.html">{S['name']}{edition_tag(S)} · {b['label']}: {esc(b['name'])}</a></h3><ol>'''
            + "".join(f'<li><a href="{S["path"]}/{b["dir"]}/{p["slug"]}.html"><span>{esc(p["num"])}</span> {esc(p["heading"])} <em>{esc(p["ref"])}</em></a></li>' for p in b["pages"]) + "</ol></li>")
def section(S, cls):
    return f'''  <h3 class="{cls}" id="{S['path']}">{S['name']} <span lang="ja">{S['kanji']}</span></h3>
  <p class="lede">{esc(S['lede'])}</p>
  {downloads("", S)}
  <ol class="grid books">
{chr(10).join(book_card(b) for b in S['books'])}
  </ol>'''
full_secs = "\n".join(section(S, "sec") for S in VOLUMES)
first = FLAT["full"][0]
home_text_cta = '<a class="cta alt" href="#text">The ASV text ›</a>' if ASV_BOOKS else ""
text_sec = "" if not ASV_BOOKS else f'''  <h2 class="sec" id="text">The Text</h2>
  <p class="lede">The manga quotes the ASV word for word. Here is the whole text, Genesis to Revelation, one PDF per book: two
  columns, a bookmark for every chapter. The ASV credit at the foot of every manga page opens its book at that page's chapter.</p>
  <ol class="asv-books">{"".join(f'<li><a href="{b["file"]}">{esc(b["title"])}</a></li>' for b in ASV_BOOKS.values())}</ol>
'''
vol_names = ", ".join(v["name"] for v in VOLUMES) or "—"
(out / "index.html").write_text(f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bible Manga</title>
<meta name="description" content="The Bible as a full-color manga, in the style of 1980s cyberpunk comics, in the words of the ASV.">
<meta property="og:image" content="thumbs/{thumb(first, first['pages'][0])}">
{FONTS}
<link rel="stylesheet" href="assets/site.css">
</head>
<body class="index home">
{bar(['<span aria-current="page">Bible Manga</span>'])}
<main class="wrap">
  <section class="hero">
    <p class="kicker">Bible Manga · {" · ".join(v["kanji"] for v in VOLUMES)}</p>
    <h1>Bible Manga</h1>
    <p class="lede">The Bible as a full-color manga — one volume per book of the Bible, every scene and every line of dialogue in the words of the ASV. Now in progress: {esc(vol_names)}.</p>
    <a class="cta" href="{first['series']['path']}/{first['dir']}/{first['pages'][0]['slug']}.html">Start at the beginning ›</a>{home_text_cta}
  </section>
  <h2 class="sec">The Books</h2>
{full_secs}
{text_sec}  <h2 class="sec">All pages</h2>
  <ol class="toc">
{chr(10).join(toc_entry(b) for b in FLAT["full"])}
  </ol>
</main>
<footer class="foot"><span>Bible Manga</span>{asv_credit("")}</footer>
</body>
</html>
''')
if ASV_BOOKS: manifest["text"] = {"title": "The Holy Bible · ASV", "books": {c: {"title": b["title"], "url": b["file"]} for c, b in ASV_BOOKS.items()}}
if DOWNLOADS: manifest["downloads"] = {LANG: {v: {"epub": f"{HOME}download/{LANG}/{d['epub']['file']}",
                                                 "pdf": [{"url": f"{HOME}download/{LANG}/{x['file']}", "range": x["range"]} for x in d["pdf"]]}
                                             for v, d in DOWNLOADS.items()}}
(out / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
(out / ".nojekyll").write_text("")
print("built", sum(len(b["pages"]) for e in FLAT.values() for b in e), "pages")
