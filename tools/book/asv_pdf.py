"""The whole Bible as a reading PDF, straight from ref/asv/*.usfm: the text every manga page quotes.

Usage (from the repo root):  python3 tools/book/asv_pdf.py [--out _book] [--books GEN,EXO]

Writes (git-ignored) _book/bible-asv.pdf: 7 × 10 in pages (the manga's print trim), two columns of serif text with
red verse numbers and big Anton chapter numerals, a running head naming the book and a running foot like the manga's
(— NN — in the centre, ASV at the right). It opens with a title page and a contents page that links every book and
chapter, and the PDF has bookmarks for the two testaments, every book and every chapter.

Named destinations: every chapter is a link target, so a URL can open the PDF at it —
bible-asv.pdf#nameddest=GEN.24 (Chrome, Edge, Firefox). Books are #nameddest=GEN, testaments #nameddest=OT / NT.

Text: the USFM with Strong's numbers stripped; the translators' supplied words (\\add) in italics, as the printed
edition sets them; psalm titles, the BOOK I–V divisions, the acrostic letters of Psalm 119 and "[Selah" kept; the 16
textual footnotes (all in the New Testament) set at the end of their chapter. The front matter and preface are left out
(see adr/0001-asv-attribution.md: the translation is credited only as "ASV").

Fonts (Source Serif 4 for the text, the manga's Anton, IBM Plex Mono and Noto Sans JP) are static TrueType files from the
Google Fonts API, cached in _book/fonts/ and embedded.

Needs Node with Playwright 1.49 or later (Chromium 131+ draws the running heads with CSS page-margin boxes) and pypdf
(Chromium only writes bookmarks into a tagged PDF, three times the size, so pypdf adds them). The website workflow builds
it with the site and caches it until ref/asv or this script changes. --books limits the text, for proofs."""
import re, html, json, string, hashlib, pathlib, argparse, subprocess, urllib.parse, urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent
ASV = ROOT / "ref" / "asv"
OUT_NAME = "bible-asv.pdf"
SINGLE = {"OBA", "PHM", "2JN", "3JN", "JUD"}         # one-chapter books: no chapter numeral

# Static TrueType instances from the Google Fonts API (all SIL Open Font License), subset to the characters in use and
# cached in _book/fonts/. A variable font would be embedded as Type 3 outlines: bigger, blurrier, not searchable.
FAMILIES = {"Source Serif 4": "ital,wght@0,400;0,600;1,400", "Anton": "wght@400", "IBM Plex Mono": "wght@500;600",
            "Noto Sans JP": "wght@900", "Noto Serif Hebrew": "wght@600"}

# ---- reading the USFM -------------------------------------------------------------------------------------------------
def book_files():
    """[(code, path)] for the 66 books in canon order (the file names start with their order number)."""
    out = []
    for p in sorted(ASV.glob("[0-9][0-9]-*.usfm")):
        code = re.match(r"\d\d-(\w{3})eng", p.name).group(1)
        if code not in ("FRT", "INT"): out.append((code, p))
    assert len(out) == 66, len(out)
    return out

def inline(s):
    """USFM character markup → HTML (the text is escaped first; markers use backslashes, so they survive)."""
    s = html.escape(s, quote=False)
    s = re.sub(r"\\\+?w ([^|\\]*)\|[^\\]*\\\+?w\*", r"\1", s)        # \w word|strong="H1234"\w*
    s = re.sub(r"\\add (.*?)\\add\*", r"<i>\1</i>", s, flags=re.S)       # supplied words
    s = re.sub(r"\\qs (.*?)\\qs\*", r'<span class="selah">\1</span>', s)
    s = re.sub(r"\\bd (.*?)\\bd\*", r"<b>\1</b>", s)
    s = re.sub(r"\\it (.*?)\\it\*", r"<i>\1</i>", s)
    s = re.sub(r"\\sc (.*?)\\sc\*", r'<span class="sc">\1</span>', s)
    s = re.sub(r"\\[a-z0-9+]+\*?", "", s)                               # anything else: drop the marker, keep the words
    return s

def note_html(body):
    """A footnote's body (\\fr ref \\ft text \\fqa alternative …) → HTML."""
    m = re.match(r"\s*\\fr ([^\\]*)(.*)", body, re.S)
    ref, rest = (m.group(1).strip(), m.group(2)) if m else ("", body)
    parts = re.split(r"\\(ft|fqa|fq) ", rest)
    out = []
    for kind, text in zip(parts[1::2], parts[2::2]):
        t = inline(text).strip()
        out.append(f"<i>{t}</i>" if kind in ("fqa", "fq") else t)
    return ref, " ".join(out)

BLOCK = {"p": "p", "m": "m", "nb": "m", "pi1": "pi", "q1": "q1", "q2": "q2", "q3": "q3"}

def book_html(code, path):
    """One book as HTML, plus [(chapter, anchor)] for the contents and a short name for the running head."""
    s = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    notes = []
    def stash(m):
        notes.append(note_html(m.group(1))); return f"\\fn{len(notes) - 1} "
    s = re.sub(r"\\f \+ (.*?)\\f\*", stash, s, flags=re.S)
    short = re.search(r"^\\h (.+?)\s*$", s, re.M).group(1)
    titles = re.findall(r"^\\(mt\d) (.+?)\s*$", s, re.M)
    last_mt1 = max(i for i, (k, _) in enumerate(titles) if k == "mt1")
    head = []
    for i, (k, t) in enumerate(titles):
        t = html.escape(t.strip())
        head.append(f'<h2 class="mt1">{t}</h2>' if i == last_mt1 else f'<p class="{k}">{t}</p>')

    body, chapters, ch_notes = [], [], []
    state = {"open": None, "pending": None, "at": 0}
    def close():
        if state["open"]: body.append("</div>"); state["open"] = None
    def open_(cls):
        close(); state["at"] = len(body); body.append(f'<div class="{cls}">'); state["open"] = cls
    def flush_notes():
        if ch_notes:
            close()
            body.append('<div class="fn">' + "".join(f'<p><b>{html.escape(r)}</b> {t}</p>' for r, t in ch_notes) + "</div>")
            ch_notes.clear()

    text = "\\c 1" + s.split("\\c 1", 1)[1]
    for m in re.finditer(r"\\(c|ms\d|d|qc|b|v|p|m|nb|pi1|q[123])(?:\s+|$)(.*?)(?=\\(?:c|ms\d|d|qc|b|v|p|m|nb|pi1|q[123])(?:\s|$)|\Z)", text, re.S):
        mk, rest = m.group(1), m.group(2)
        if mk == "c":
            flush_notes(); close()
            n = int(rest.split()[0])
            anchor = f"{code}.{n}"; chapters.append((n, anchor))
            if code == "PSA":
                body.append(f'<h3 class="ps" id="{anchor}">Psalm {n}</h3>')
            elif code in SINGLE:
                body.append(f'<span class="anchor" id="{anchor}"></span>')
            else:
                state["pending"] = (n, anchor)
            continue
        if mk.startswith("ms"):           # BOOK I … V of the Psalms: above the psalm's own heading
            close(); ms = f'<h4 class="ms">{inline(rest).strip()}</h4>'
            body.insert(len(body) - 1, ms) if body and body[-1].startswith('<h3 class="ps"') else body.append(ms)
            continue
        if mk == "d":
            close(); body.append(f'<div class="d">{inline(rest).strip()}</div>'); continue
        if mk == "qc":
            close(); body.append(f'<div class="qc">{inline(rest).strip()}</div>'); continue
        if mk == "b":
            close(); body.append('<div class="b"></div>'); continue
        if mk in BLOCK:
            open_(BLOCK[mk])
            if rest.strip(): body.append(inline(rest).strip() + " ")
            continue
        # a verse: number, then text (which may run on into poetry lines of its own block)
        vm = re.match(r"(\d+)\s*(.*)", rest, re.S)
        vn, vt = int(vm.group(1)), vm.group(2)
        if not state["open"]: open_("m")
        t = inline(re.sub(r"\\fn(\d+) ?", "\x00\\1\x00", vt)).strip()
        def fn_mark(fm):
            ch_notes.append(notes[int(fm.group(1))]); return '<sup class="fm">*</sup>'
        t = re.sub("\x00(\\d+)\x00", fn_mark, t)
        if state["pending"] and vn == 1:
            n, anchor = state["pending"]; state["pending"] = None
            if state["open"] in ("q1", "q2", "q3"):     # poetry: the numeral on a line of its own (hanging lines can't wrap a float)
                body.insert(state["at"], f'<span class="anchor" id="{anchor}"></span><h3 class="cq">{n}</h3>')
                body.append(f'{t} ')
            else:
                body.append(f'<span class="anchor" id="{anchor}"></span><h3 class="cn">{n}</h3>{t} ')
        else:
            body.append(f'<sup class="v">{vn}</sup>{t} ')
    flush_notes(); close()
    sec = (f'<section class="book" id="{code}" style="page: b{code}">\n<header class="bt">{"".join(head)}</header>\n'
           f'<div class="text">\n' + "\n".join(body) + "\n</div>\n</section>")
    return sec, chapters, short

# ---- fonts --------------------------------------------------------------------------------------------------------------
def fetch_fonts(doc, fdir):
    """Download each family subset to the characters of `doc`; returns @font-face CSS pointing at the cached files."""
    chars = "".join(sorted(set(html.unescape(re.sub(r"<[^>]+>", " ", doc.split("<body>", 1)[1])))   # + text-transform's capitals
                           | set(string.ascii_letters + string.digits + string.punctuation + "—· ") - set("\n\r\t")))
    key = hashlib.sha1((chars + json.dumps(FAMILIES)).encode()).hexdigest()[:10]
    fdir.mkdir(parents=True, exist_ok=True)
    index = fdir / f"asv-fonts-{key}.json"
    if index.exists():
        got = json.loads(index.read_text())
    else:
        got = []
        for fam, spec in FAMILIES.items():
            q = urllib.parse.urlencode({"family": f"{fam}:{spec}", "text": chars})
            req = urllib.request.Request("https://fonts.googleapis.com/css2?" + q, headers={"User-Agent": "Wget/1.21"})  # plain UA → TrueType
            css = urllib.request.urlopen(req, timeout=30).read().decode()
            for block in re.findall(r"@font-face\s*{(.*?)}", css, re.S):
                wt = int(re.search(r"font-weight:\s*(\d+)", block).group(1))
                st = re.search(r"font-style:\s*(\w+)", block).group(1)
                url = re.search(r"url\((.*?)\)", block).group(1)
                fn = f"asv-{fam.replace(' ', '')}-{wt}{'i' if st == 'italic' else ''}-{key}.ttf"
                (fdir / fn).write_bytes(urllib.request.urlopen(url, timeout=60).read())
                got.append([fam, wt, st, fn])
                print(f"  font {fam} {wt} {st}: {(fdir / fn).stat().st_size // 1024} KB")
        index.write_text(json.dumps(got))
    return "".join(f"@font-face {{ font-family: '{fam}'; font-weight: {wt}; font-style: {st}; "
                   f"src: url('{(fdir / fn).as_uri()}') format('truetype'); }}\n" for fam, wt, st, fn in got)

# ---- the document -------------------------------------------------------------------------------------------------------
CSS = r"""
@page { size: 7in 10in; margin: 0.72in 0.6in 0.7in;
  @bottom-center { content: "— " counter(page) " —"; font: 500 7.5pt 'IBM Plex Mono', monospace; color: #77736C; }
  @bottom-right { content: "ASV"; font: 500 7.5pt 'IBM Plex Mono', monospace; color: #77736C; letter-spacing: .12em; } }
@page front { @bottom-center { content: none; } @bottom-right { content: none; } }
@page cover { margin: 0; @bottom-center { content: none; } @bottom-right { content: none; } }
html { font-size: 9.6pt; }
body { margin: 0; color: #0D0D0F; font-family: 'Source Serif 4', 'Noto Serif Hebrew', Georgia, serif; font-optical-sizing: auto;
  line-height: 1.32; font-kerning: normal; text-rendering: optimizeLegibility; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
a { color: inherit; text-decoration: none; }

/* title page and testament dividers (full bleed, the night of God's-voice panels) */
.title, .divider { page: cover; position: relative; width: 7in; height: 10in; overflow: hidden; break-before: page; break-after: page;
  background: radial-gradient(120% 80% at 70% 18%, #5B2470 0%, #1E1650 45%, #0B0B2A 100%); color: #F3EFE6; }
.title { break-before: auto; }
.rays { position: absolute; inset: 0; width: 7in; height: 10in; }
.title .kanji { position: absolute; top: 0; right: 0.55in; width: 1.15in; padding: 0.35in 0 0.3in; background: #D7261E; text-align: center;
  font: 900 64pt/1.08 'Noto Sans JP', sans-serif; color: #F3EFE6; writing-mode: vertical-rl; display: flex; align-items: center; justify-content: center;
  border: 3px solid #0D0D0F; border-top: 0; }
.title .kana { position: absolute; top: 2.55in; right: 0.55in; width: 1.15in; text-align: center; font: 600 7pt 'IBM Plex Mono', monospace; letter-spacing: .3em; color: #FFD23F; }
.title .block { position: absolute; left: 0.6in; right: 2.1in; bottom: 1.45in; }
.title .k { font: 600 9pt 'IBM Plex Mono', monospace; letter-spacing: .32em; color: #FFD23F; margin: 0 0 10pt; }
.title h1 { font: 400 86pt/0.9 'Anton', Impact, sans-serif; letter-spacing: .01em; margin: 0; text-transform: uppercase; }
.title .rule { height: 3px; background: #FFD23F; margin: 18pt 0 12pt; width: 2.2in; }
.title .sub { font: 600 10pt/1.5 'IBM Plex Mono', monospace; letter-spacing: .18em; text-transform: uppercase; margin: 0; }
.title .foot { position: absolute; left: 0.6in; right: 0.6in; bottom: 0.5in; display: flex; justify-content: space-between;
  font: 600 8pt 'IBM Plex Mono', monospace; letter-spacing: .22em; color: #C9C3D8; text-transform: uppercase; }

/* contents */
.contents { page: front; break-after: page; }
.contents h2 { font: 400 30pt/1 'Anton', Impact, sans-serif; text-transform: uppercase; margin: 0 0 4pt; }
.contents .lead { font: 500 7.5pt/1.5 'IBM Plex Mono', monospace; color: #5E5A54; margin: 0 0 12pt; letter-spacing: .04em; }
.contents .cols { columns: 2; column-gap: 0.3in; }
.contents .tt { font: 600 7.5pt 'IBM Plex Mono', monospace; letter-spacing: .25em; color: #D7261E; margin: 0 0 4pt; padding-bottom: 3pt;
  border-bottom: 2px solid #0D0D0F; break-after: avoid; }
.contents .tt.nt { break-before: column; }
.contents .bk { break-inside: avoid; margin: 0 0 3.5pt; font-size: 8.6pt; line-height: 1.25; }
.contents .bk > a { font-weight: 600; }
.contents .chs { display: block; font: 500 6.2pt/1.55 'IBM Plex Mono', monospace; color: #5E5A54; word-spacing: .15em; }
.contents .chs a { padding: 0 .5pt; }
.colophon { font: 500 6.6pt/1.55 'IBM Plex Mono', monospace; color: #5E5A54; margin-top: 10pt; padding-top: 6pt; border-top: 1px solid #BDB7AC;
  letter-spacing: .02em; break-inside: avoid; }
.colophon i { font-family: 'Source Serif 4', serif; font-size: 8pt; }

.divider .block { position: absolute; left: 0.6in; right: 0.6in; top: 3.6in; }
.divider p { font: 600 8.5pt 'IBM Plex Mono', 'Noto Sans JP', monospace; letter-spacing: .32em; color: #FFD23F; margin: 0 0 10pt; }
.divider h1 { font: 400 64pt/0.92 'Anton', Impact, sans-serif; text-transform: uppercase; margin: 0; }
.divider .rule { height: 3px; width: 1.6in; background: #D7261E; margin-top: 18pt; }

/* books */
.book { break-before: page; }
.bt { text-align: center; margin: 0 0 12pt; padding-bottom: 9pt; border-bottom: 2.5px solid #0D0D0F; }
.bt p { margin: 0 0 2pt; font: 600 7.4pt 'IBM Plex Mono', monospace; letter-spacing: .26em; color: #5E5A54; }
.bt p.mt1 { font: 400 15pt/1.1 'Anton', Impact, sans-serif; letter-spacing: .04em; color: #0D0D0F; margin: 0 0 3pt; }
.bt h2 { margin: 2pt 0 0; font: 400 34pt/1 'Anton', Impact, sans-serif; letter-spacing: .02em; }
.text { columns: 2; column-gap: 0.24in; column-rule: 0.5pt solid #CFC9BE; orphans: 2; widows: 2; }
.p { text-indent: 1em; margin: 0; }
.m { margin: 0; }
.pi { margin: 0 0 0 1em; text-indent: 1em; }
.q1, .q2, .q3 { margin: 0 0 0 1.6em; text-indent: -1em; }
.q2 { margin-left: 2.4em; }
.q3 { margin-left: 3.2em; }
.b { height: 0.5em; }
sup.v { font: 600 0.62em 'IBM Plex Mono', monospace; color: #D7261E; vertical-align: 0.42em; line-height: 0; margin: 0 0.18em 0 0.1em; text-indent: 0; }
sup.fm { font: 600 0.75em 'IBM Plex Mono', monospace; color: #D7261E; vertical-align: 0.35em; line-height: 0; }
h3.cn { float: left; margin: 0.06em 0.16em 0 0; font: 400 2.75em/0.86 'Anton', Impact, sans-serif; color: #D7261E; text-indent: 0; }
.p:has(> h3.cn), .pi:has(> h3.cn) { text-indent: 0; }
h3.cq { break-after: avoid; margin: 0.35em 0 0.1em; font: 400 2.1em/1 'Anton', Impact, sans-serif; color: #D7261E; }
h3.ps { break-after: avoid; margin: 0.9em 0 0.25em; font: 600 7.6pt 'IBM Plex Mono', monospace; letter-spacing: .24em; text-transform: uppercase;
  color: #D7261E; text-align: center; }
h3.ps::before, h3.ps::after { content: ""; display: inline-block; width: 1.4em; border-top: 1px solid #D7261E; vertical-align: 0.3em; margin: 0 0.6em; }
h4.ms { column-span: none; break-after: avoid; margin: 1.1em 0 0.2em; text-align: center; font: 400 15pt 'Anton', Impact, sans-serif; letter-spacing: .06em; }
.d { font-style: italic; font-size: 0.92em; margin: 0 0 0.25em; text-align: center; break-after: avoid; }
.qc { margin: 0.5em 0 0.1em; font: 600 7.6pt 'IBM Plex Mono', 'Noto Serif Hebrew', monospace; letter-spacing: .14em; color: #D7261E; break-after: avoid; }
.selah { font-style: italic; float: right; margin-left: 0.6em; }
.fn { margin: 0.35em 0 0.5em; padding-top: 0.3em; border-top: 0.5pt solid #BDB7AC; font-size: 0.82em; line-height: 1.3; color: #3D3A35; }
.fn p { margin: 0 0 0.2em; }
.fn b { font: 600 0.92em 'IBM Plex Mono', monospace; color: #D7261E; }
.sc { font-variant: small-caps; }
.end { margin: 0.5in 0 0; text-align: center; font: 900 30pt/1 'Noto Sans JP', sans-serif; color: #D7261E; break-inside: avoid; }
.end span { display: block; margin-top: 6pt; font: 600 7.5pt 'IBM Plex Mono', monospace; letter-spacing: .4em; color: #5E5A54; }
"""

def rays(cx, cy, n, seed):
    """Radial speed lines (thin gold wedges) and a scatter of stars, as an SVG over the full 7 × 10 in page."""
    import math, random
    r = random.Random(seed); out = []
    for i in range(n):
        a = 2 * math.pi * (i + r.random() * 0.6) / n; w = r.uniform(0.004, 0.018); R = 1400; r0 = r.uniform(40, 140)
        pts = [(cx + r0 * math.cos(a), cy + r0 * math.sin(a)), (cx + R * math.cos(a - w), cy + R * math.sin(a - w)),
               (cx + R * math.cos(a + w), cy + R * math.sin(a + w))]
        out.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="#FFD23F" opacity="{r.uniform(.05, .16):.2f}"/>')
    for _ in range(70):
        out.append(f'<circle cx="{r.uniform(0, 672):.1f}" cy="{r.uniform(0, 960):.1f}" r="{r.uniform(.4, 1.3):.2f}" fill="#F3EFE6" '
                   f'opacity="{r.uniform(.25, .8):.2f}"/>')
    return f'<svg class="rays" viewBox="0 0 672 960" aria-hidden="true">{"".join(out)}</svg>'

def document(books):
    ot = [b for b in books if b["nt"] is False]; nt = [b for b in books if b["nt"]]
    pages = "\n".join(f'@page b{b["code"]} {{ @top-center {{ content: "{b["short"].upper()}"; font: 600 7pt \'IBM Plex Mono\', monospace; '
                      f'letter-spacing: .3em; color: #0D0D0F; }} }}' for b in books)
    def toc(bs):
        out = []
        for b in bs:
            chs = "" if b["code"] in SINGLE else ('<span class="chs">' + " ".join(f'<a href="#{a}">{n}</a>' for n, a in b["chapters"]) + "</span>")
            out.append(f'<div class="bk"><a href="#{b["code"]}">{html.escape(b["short"])}</a>{chs}</div>')
        return "\n".join(out)
    title = f"""<section class="title">{rays(470, 173, 46, 1)}
<div class="kanji">聖書</div><div class="kana">SEISHO</div>
<div class="block"><p class="k">THE OLD AND NEW TESTAMENTS</p><h1>The Holy <br>Bible</h1><div class="rule"></div>
<p class="sub">The text of the Bible Manga</p></div>
<div class="foot"><span>Bible Manga</span><span>ASV</span></div></section>"""
    contents = f"""<section class="contents"><h2>CONTENTS</h2>
<p class="lead">Every book and chapter is a link. The PDF's bookmarks list them too.</p>
<div class="cols"><div class="tt"><a href="#OT">THE OLD TESTAMENT</a></div>
{toc(ot)}
<div class="tt nt"><a href="#NT">THE NEW TESTAMENT</a></div>
{toc(nt)}
<div class="colophon">ASV · public domain. Set from the USFM text published by eBible.org, with the Strong's numbers taken out.
Words the translators supplied are in <i>italics</i>, as in the printed edition; the few textual notes stand at the end of their chapter.
Every word of the Bible Manga is cut from this text.</div></div></section>"""
    def divider(id_, name, kicker, seed):
        return (f'<section class="divider" id="{id_}">{rays(560, 120, 34, seed)}<div class="block"><p>{kicker}</p>'
                f'<h1>{name}</h1><div class="rule"></div></div></section>')
    parts = [title, contents]
    if ot: parts += [divider("OT", "The Old <br>Testament", "旧約聖書 · 39 BOOKS", 2)] + [b["html"] for b in ot]
    if nt: parts += [divider("NT", "The New <br>Testament", "新約聖書 · 27 BOOKS", 3)] + [b["html"] for b in nt]
    parts[-1] = parts[-1].replace("</div>\n</section>", '</div>\n<div class="end">完<span>END</span></div>\n</section>')  # after the last book's text
    return (f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><title>The Holy Bible · ASV</title>'
            f'<style>/*FONTS*/\n{CSS}\n{pages}</style></head>\n<body>\n' + "\n".join(parts) + "\n</body></html>\n")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="_book"); ap.add_argument("--books", help="comma-separated book codes, for proofs")
    ap.add_argument("--html-only", action="store_true")
    a = ap.parse_args()
    want = set(a.books.split(",")) if a.books else None
    out = (ROOT / a.out).resolve(); out.mkdir(parents=True, exist_ok=True)
    books = []
    for i, (code, path) in enumerate(book_files()):
        if want and code not in want: continue
        sec, chapters, short = book_html(code, path)
        books.append({"code": code, "html": sec, "chapters": chapters, "short": short, "nt": i >= 39})
    verses = sum(len(re.findall(r'class="(?:v|cn|cq)"', b["html"])) for b in books)
    work = out / "work"; work.mkdir(exist_ok=True)
    src = work / "bible-asv.html"
    doc = document(books)
    src.write_text(doc.replace("/*FONTS*/", fetch_fonts(doc, out / "fonts")), encoding="utf-8")
    print(f"{len(books)} books, {sum(len(b['chapters']) for b in books)} chapters, {verses} verses → {src.relative_to(ROOT)}")
    if a.html_only: return
    raw, pdf = work / "bible-asv-raw.pdf", out / OUT_NAME
    subprocess.run(["node", str(HERE / "render.js"), "text", str(src), str(raw)], check=True)
    bookmark(raw, pdf, books)
    print(f"  {pdf.relative_to(ROOT)}  ({pdf.stat().st_size // 1024} KB)")

def bookmark(raw, pdf, books):
    """Bookmarks (testament › book › chapter) and document info, found through the PDF's own named destinations."""
    from pypdf import PdfReader, PdfWriter
    reader = PdfReader(raw)
    page_of = {name.lstrip("/"): reader.get_destination_page_number(d) for name, d in reader.named_destinations.items()}
    w = PdfWriter(clone_from=reader)
    w.add_outline_item("The Holy Bible", 0)
    w.add_outline_item("Contents", 1)
    for tid, tname, nt in (("OT", "The Old Testament", False), ("NT", "The New Testament", True)):
        bs = [b for b in books if b["nt"] is nt]
        if not bs: continue
        t = w.add_outline_item(tname, page_of[tid])
        for b in bs:
            bk = w.add_outline_item(b["short"], page_of[b["code"]], parent=t)
            if b["code"] in SINGLE: continue
            for n, anchor in b["chapters"]:
                w.add_outline_item(f"{'Psalm' if b['code'] == 'PSA' else b['short']} {n}", page_of[anchor], parent=bk)
    w.add_metadata({"/Title": "The Holy Bible · ASV", "/Subject": "The Old and New Testaments: the text of the Bible Manga",
                    "/Author": "Bible Manga", "/Keywords": "Bible, ASV, public domain"})
    w.page_mode = "/UseOutlines"
    with open(pdf, "wb") as f: w.write(f)

if __name__ == "__main__":
    main()
