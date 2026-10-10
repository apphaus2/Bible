"""Build one volume of the full edition.

Usage (from the repo root):  python3 tools/full/build_volume.py genesis

Reads tools/full/<volume>/ (META in __init__.py, cover.py, one module per manga chapter) and writes volumes/<volume>/:
  pages/*.dc.html   every page (Main.dc.html is the volume cover)
  canvas.json       the Claude Design canvas index (boards in reading order, one block of rows per chapter)
  volume.json       what the website needs (chapters, page prefixes, blurbs)
  coverage.md       every Bible verse in the chapters built so far: full / partial / omitted
Then it checks every caption, balloon and title quote against the ASV text and stops on any mismatch."""
import sys, json, re, html, pathlib, importlib, datetime
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parent / "kit"))

def main(vol):
    pkg = importlib.import_module(vol)
    META, G = pkg.META, pkg.G
    out = ROOT / "volumes" / vol; pages_dir = out / "pages"; pages_dir.mkdir(parents=True, exist_ok=True)
    cover = importlib.import_module(f"{vol}.cover").cover
    order = [("Main.dc.html", "Cover", cover)]
    chapters = []
    for c in META["chapters"]:
        mod = importlib.import_module(f"{vol}.{c['module']}")
        names = [(f"{n}.dc.html", t, fn) for n, t, fn in mod.PAGES]
        order += names
        prefix = names[0][0].rsplit("-", 2)[0].rsplit("-", 1)[0] + "-"     # e.g. GEN-C01-
        chapters.append(dict(c, prefixes=(["Main.dc.html"] if c is META["chapters"][0] else []) + [prefix], files=[n for n, _, _ in names]))
    written = set()
    for name, _, fn in order:
        (pages_dir / name).write_text(fn()); written.add(name)
    for stale in pages_dir.glob("*.dc.html"):
        if stale.name not in written: stale.unlink()

    # canvas: the cover, then each chapter as its own block of rows (5 boards a row), with a title note above each block
    cpath = out / "canvas.json"
    old = json.loads(cpath.read_text()) if cpath.exists() else {}
    boards, notes, y = {}, {}, 0
    blocks = [("Main", META["title"], ["Main.dc.html"])] + [(c["dir"], f"Chapter {c['num']} · {c['name']} ({c['range']})", c["files"]) for c in chapters]
    titles = {n: t for n, t, _ in order}
    for key, label, files in blocks:
        notes[key.replace("-", "")] = {"kind": "title1", "maxW": 4120, "text": label, "x": 0, "y": y}
        y += 300
        for i, n in enumerate(files):
            boards[n] = {"x": (i % 5) * 840, "y": y + (i // 5) * 1200, "w": 760, "h": 1080, "title": titles[n]}
        y += ((len(files) - 1) // 5 + 1) * 1200 + 200
    canvas = {"v": 3, "createdOnFiles": old.get("createdOnFiles") or {"v": 1, "at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")},
              "title": f"{META['name']} — Full Edition", "launch": {"view": "canvas"}, "pages": [],
              "boards": boards, "order": [n for n, _, _ in order], "notes": notes, "designSystems": [], "attachments": {}}
    cpath.write_text(json.dumps(canvas, indent=1, ensure_ascii=False))

    (out / "volume.json").write_text(json.dumps({k: META[k] for k in ("id", "order", "name", "kanji", "thumb", "lede")} | {
        "books": [{k: c[k] for k in ("dir", "num", "name", "range", "blurb", "prefixes")} for c in chapters]}, indent=1, ensure_ascii=False))

    # coverage report
    lines = [f"# {META['name']} — coverage of the full edition", "",
             "Every verse of the chapters built so far, checked against `ref/asv`. **full** = every word on the page; "
             "**partial** = abridged (cuts marked with …); **omitted** = not on any page.", ""]
    tot = {"full": 0, "partial": 0, "omitted": 0}
    for c in chapters:
        rows = G.coverage(c["bible_chapters"])
        n = {s: sum(1 for r in rows if r[1] == s) for s in tot}
        for s in tot: tot[s] += n[s]
        lines += [f"## Chapter {c['num']} · {c['name']} ({c['range']})", "",
                  f"{len(rows)} verses: {n['full']} full, {n['partial']} partial, {n['omitted']} omitted.", ""]
        odd = [f"- {r[0]} — {r[1]} ({r[2]:.0%})" for r in rows if r[1] != "full"]
        lines += (odd or ["Every verse is on the page in full."]) + [""]
    allv = sum(tot.values())
    lines.insert(4, f"**So far:** {allv} verses — {tot['full']} full, {tot['partial']} partial, {tot['omitted']} omitted.\n")
    (out / "coverage.md").write_text("\n".join(lines))

    # text check: every uppercase text block must be a run of the ASV (… marks a cut). Labels that are not
    # scripture (titles, credits) carry data-label and are skipped.
    norm = lambda t: re.sub(r"\s+", " ", t.replace("\u2019", "'")).strip().lower()
    full = norm(G.text()); bad = n = 0
    for p in sorted(pages_dir.glob("*.dc.html")):
        for attrs, body in re.findall(r'<(?:div|h1)([^>]*)>(.*?)</(?:div|h1)>', p.read_text(), re.S):
            if "text-transform: uppercase" not in attrs or "data-label" in attrs or "<" in body: continue
            t = html.unescape(re.sub(r"<br\s*/?>", " ", body))
            for seg in [x for x in t.split("…") if x.strip()]:
                n += 1
                if norm(seg) not in full:
                    bad += 1; print("NOT ASV:", p.name, "|", seg[:100])
    print(f"{vol}: {len(order)} pages, {n} text blocks checked, {bad} not found; coverage {tot}")
    if bad: sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1])
