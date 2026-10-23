"""Build the website in every language, redoing only what changed, and deploy it.

Usage (from the repo root):  python tools/build.py [en es …] [--only oba,jon] [--steps volumes,text,downloads,site]
                                                    [--deploy] [--force] [--jobs 4] [--dry-run]

Languages: those named, else all of tools/lang/ (English first). The steps, in this order:
  volumes    build_volume.py for every package in every language (BIBLE_LANG=<code>), --jobs at once. A package whose
             stamp is fresh (nothing it read or wrote has changed since it last built: tools/full/stamps.py) is skipped
             without starting Python. All languages' volumes come first: each site's language menu reads the others'.
  text       asv_pdf.py [--text <id>]: the Bible text by book; it skips itself on a fresh stamp.
  downloads  downloads.py --lang <code>: each book's EPUB and reading PDF; it redoes only books whose pages changed.
  site       rebuild_site.py --thumbs --lang <code>: the pages (quick); thumbnails only for pages that changed.
  deploy     (with --deploy) npx wrangler@4 deploy -c tools/site/workers/<code>.jsonc, skipped when the language's site
             is file for file what was last deployed; then the router (wrangler.jsonc), only when it or router.js changed.
--only limits the volumes step to some packages (the other steps always cover the whole language). --force ignores the
stamps of volumes, text and deploys (downloads and thumbnails keep their own hashes). --dry-run builds nothing: it lists
the volumes and text PDFs that would be rebuilt and the deploys that would run if the sites stayed as they are.
Stops at the first failure. The text, downloads and thumbnails need Node with Playwright (NODE_PATH), pypdf and Pillow."""
import os, sys, shutil, argparse, subprocess, concurrent.futures as cf, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "tools" / "full"), str(ROOT / "tools" / "lang")]
import stamps, langs

PY = sys.executable
ENV = {**os.environ, "PYTHONUTF8": "1"}
PKGS = sorted(p.parent.name for p in (ROOT / "tools" / "full").glob("*/__init__.py"))

def run(args, lang="en", capture=False):
    return subprocess.run(args, cwd=ROOT, env={**ENV, "BIBLE_LANG": lang}, text=True, encoding="utf-8", errors="replace",
                          capture_output=capture, check=not capture)

def site_dir(lang): return ROOT / ("_site" if lang == "en" else f"_site-{lang}")
def site_files(lang): return [p for p in site_dir(lang).rglob("*") if p.is_file()]
ROUTER = [ROOT / "wrangler.jsonc", ROOT / "tools" / "site" / "workers" / "router.js"]

def volumes(todo, jobs):
    """Build the stale (lang, package) pairs, `jobs` at a time; stop (after the running ones) on the first failure."""
    if not todo: print("volumes: all unchanged"); return
    print(f"volumes: building {len(todo)}")
    with cf.ThreadPoolExecutor(jobs) as ex:
        futs = {ex.submit(run, [PY, "tools/full/build_volume.py", pkg, "--force"], lang, True): (lang, pkg) for lang, pkg in todo}
        for fut in cf.as_completed(futs):
            (lang, pkg), r = futs[fut], fut.result()
            if r.returncode:
                print(r.stdout + r.stderr); ex.shutdown(cancel_futures=True); sys.exit(f"{lang} {pkg}: build_volume.py failed")
            print(f"  {lang:2} {(r.stdout.strip().splitlines() or [''])[-1]}")

def deploy(name, cfg, files, force, dry):
    if not force and stamps.fresh(name, files): print(f"{name}: unchanged since the last deploy"); return
    if dry: print(f"{name}: would deploy"); return
    npx = shutil.which("npx") or sys.exit("npx not found (Node.js)")
    run([npx, "wrangler@4", "deploy", *(["-c", cfg] if cfg else [])])
    stamps.record(name, files)

def main():
    ap = argparse.ArgumentParser(description="Build the website, redoing only what changed.")
    ap.add_argument("langs", nargs="*", help=f"languages (default: all of {', '.join(langs.ORDER)})")
    ap.add_argument("--only", help="comma-separated packages for the volumes step (default: every package)")
    ap.add_argument("--steps", default="volumes,text,downloads,site", help="comma-separated, from volumes,text,downloads,site")
    ap.add_argument("--deploy", action="store_true", help="deploy each language that changed, then the router if it changed")
    ap.add_argument("--force", action="store_true", help="ignore the stamps of volumes, text and deploys")
    ap.add_argument("--jobs", type=int, default=4, help="volumes built at once (default 4)")
    ap.add_argument("--dry-run", action="store_true", help="list what would be built and deployed; build nothing")
    a = ap.parse_args()
    todo_langs = [l for l in langs.ORDER if l in a.langs] if a.langs else langs.ORDER
    if bad := [l for l in a.langs if l not in langs.ORDER]: sys.exit(f"unknown language: {', '.join(bad)} (tools/lang/<code>.json)")
    steps = a.steps.split(",")
    pkgs = a.only.split(",") if a.only else PKGS
    if bad := [p for p in pkgs if p not in PKGS]: sys.exit(f"unknown package: {', '.join(bad)}")

    if "volumes" in steps:
        stale = [(l, p) for l in todo_langs for p in pkgs if a.force or not stamps.fresh(f"volumes/{l}/{p}")]
        if a.dry_run:
            for l in todo_langs:
                mine = [p for ll, p in stale if ll == l]
                print(f"volumes {l}: " + (f"{len(mine)} to build: {' '.join(mine)}" if mine else "all unchanged"))
        else: volumes(stale, a.jobs)
    for l in todo_langs:
        text = langs.get(l)["text"]
        if "text" in steps:
            if a.dry_run: print(f"text {l}: " + ("unchanged" if not a.force and stamps.fresh(f"text/{text}") else "to build"))
            else: run([PY, "tools/book/asv_pdf.py", *([] if l == "en" else ["--text", text]), *(["--force"] if a.force else [])], l)
        if "downloads" in steps and not a.dry_run: run([PY, "tools/book/downloads.py", "--lang", l], l)
        if "site" in steps and not a.dry_run: run([PY, "tools/site/rebuild_site.py", "--thumbs", *([] if l == "en" else ["--lang", l])], l)
        if a.deploy:
            if not (site_dir(l) / ("" if l == "en" else l) / "index.html").exists() and not a.dry_run: sys.exit(f"{l}: no site to deploy (the site step)")
            deploy(f"deploy/{l}", f"tools/site/workers/{l}.jsonc", site_files(l), a.force, a.dry_run)
    if a.deploy: deploy("deploy/router", None, ROUTER, a.force, a.dry_run)

if __name__ == "__main__":
    try: main()
    except subprocess.CalledProcessError as e: sys.exit(f"failed ({e.returncode}): {' '.join(map(str, e.cmd))}")
