"""Build stamps: skip a step whose inputs and outputs are just as they were when it last succeeded.

A stamp is _book/stamps/<name>.json (git-ignored): {"inputs": {path: [sha1, size, mtime_ns]}, "outputs": {…}}, paths
relative to the repo. fresh(name) is true when every file it lists is still there with the same content (a file whose size
and modification time are unchanged is taken as unchanged without reading it); record(name, inputs, outputs) writes one.

watch() records every file under the repo that the process reads or imports from then on; watched() returns them. A
volume's inputs are then exactly what its plan read: its own modules, the kit, other books' art it lifts, the reference
pages, the Bible texts, the language files and labels. A file nothing read before (a new file in a folder that is globbed)
is not noticed: build_volume.py --force, or tools/build.py --force."""
import os, sys, json, hashlib, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
DIR = ROOT / "_book" / "stamps"
SKIP = ("_book/", "_site", ".git/", ".wrangler/", "node_modules/")   # outputs and caches, never inputs

def rel(p):
    """The path relative to the repo with forward slashes, or None outside it."""
    try: r = pathlib.Path(p).resolve().relative_to(ROOT).as_posix()
    except (ValueError, OSError): return None
    return None if "__pycache__" in r or r.startswith(SKIP) else r

def entry(path):
    """[sha1, size, mtime_ns] of a file under the repo, or None if it is gone."""
    f = ROOT / path
    try: st = f.stat(); return [hashlib.sha1(f.read_bytes()).hexdigest(), st.st_size, st.st_mtime_ns]
    except OSError: return None

def same(path, old):
    f = ROOT / path
    try: st = f.stat()
    except OSError: return False
    if [st.st_size, st.st_mtime_ns] == old[1:]: return True
    return st.st_size == old[1] and hashlib.sha1(f.read_bytes()).hexdigest() == old[0]

def fresh(name, inputs=None):
    """True when every file the stamp lists is unchanged; with `inputs`, they must also be exactly the files it lists
    (a deploy: a page added to the site is a change too)."""
    f = DIR / f"{name}.json"
    if not f.exists(): return False
    s = json.loads(f.read_text(encoding="utf-8"))
    if inputs is not None and {rel_any(p) for p in inputs} != set(s["inputs"]): return False
    return all(same(p, e) for part in ("inputs", "outputs") for p, e in s[part].items())

def record(name, inputs, outputs=()):
    """Stamp `name` with the given files (paths under the repo, absolute or relative)."""
    def table(paths):
        rows = {r: entry(r) for r in sorted({x for x in map(rel_any, paths) if x})}
        return {r: e for r, e in rows.items() if e}
    f = DIR / f"{name}.json"; f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps({"inputs": table(inputs), "outputs": table(outputs)}, indent=0), encoding="utf-8")

def own_lang(paths, lang):
    """Leave out the other languages' files: tools/lang/langs.py reads every tools/lang/<code>.json, but only the
    language being built shapes its output (editing es.json should not rebuild the German edition)."""
    own = f"tools/lang/{lang}.json"
    return [r for r in paths if not (r.startswith("tools/lang/") and r.endswith(".json") and r != own)]

def forget(name):
    (DIR / f"{name}.json").unlink(missing_ok=True)

def rel_any(p):
    """rel() for a recorded output too (outputs may live under _book/ or _site*/)."""
    try: return pathlib.Path(ROOT / p).resolve().relative_to(ROOT).as_posix()
    except (ValueError, OSError): return None

_read, _on = set(), []

def watch():
    _on.append(True)
    def hook(event, args):
        if event != "open" or not isinstance(args[0], (str, os.PathLike)): return
        mode, flags = args[1], args[2]
        if mode is None:
            if flags & (os.O_WRONLY | os.O_RDWR): return
        elif any(c in mode for c in "wax+"): return
        _read.add(os.fspath(args[0]))
    sys.addaudithook(hook)

def watching(): return bool(_on)

def watched():
    """Every file under the repo read or imported since watch() (modules by their source, not their .pyc)."""
    files = set(_read) | {m.__file__ for m in list(sys.modules.values()) if getattr(m, "__file__", None)}
    return {r for r in map(rel, files) if r and (ROOT / r).is_file()}
