---
name: build-book
description: Build a whole Bible book (one manga volume, e.g. Mark, Volume Forty-One) in a subagent worktree, then review every page and merge it into master and the English site. Use when the user says "start the next book", "build <Book>", "do Mark in a subagent", or "continue" at a book boundary.
---

# Build a book in a subagent, review it, merge it

How Matthew (Volume Forty, 215 pages) was built. CLAUDE.md holds the rules; this is the procedure around them.

## 1. Before launching

- Find the book's place: CLAUDE.md "Order numbers and ids" (Mark 41 `mark`, Luke 42, John 43, Acts 44, Romans 45 …),
  its USFM code (the `ref/eng-asv` file name), its kanji block (CLAUDE.md "Visual style"), a package name that does not
  start with a digit or shadow a kit module.
- Look for a draft: `git branch --list "wip/*"`; `git show --stat wip/<book>`. The `wip/` drafts are cut from an old master
  and unchecked: the subagent may lift files from them (`git show wip/<book>:<path>`), never merge or rebase them.
- The previous volume's last page must say `NEXT · <BOOK>`; the new one's last page `END OF <BOOK> · NEXT · <NEXT>`.

## 2. Launch (Agent tool, `isolation: "worktree"`, `run_in_background: true`)

The brief must stand alone. Include, in this order:
1. Goal: package `tools/full/<pkg>/`, id, order, code, kanji, "Volume <N>", thumb `vol-<id>-`; build the manga chapters in
   order from chapter 1 through the end of the book, ~15–25 pages a chapter, ~140–160 words a page, every verse full.
   Name the first chapter's content and how each hard scene is to be shown.
2. Starting material: the `wip/` draft (lift, don't merge); `tools/full/ntcast.py` (the shared NT cast: never redraw Jesus,
   the disciples, Mary …); the latest volume as the model (for the NT: `mat`, built on `oba/minor.py`'s `Kit`).
3. Hard rules repeated from CLAUDE.md: ASV only via `asv.Book` cuts, never typed; God, Satan and demons never drawn;
   angels white light with a gold rim and no face; restraint (violence and death in words over empty places); Jesus' words
   in ordinary balloons; never hand-edit pages; `build_volume.py <pkg>` ends `0 not found, 0 lost` and `--check` passes;
   render and look at every page; Git Bash or cmd, never PowerShell; English only (no BIBLE_LANG, no i18n edits).
4. If its worktree was cut from an old commit and has no commits of its own, `git reset --hard master` first.
5. Commit to its own branch after each chapter (author Sky <sky75.morey@gmail.com>, the Co-Authored-By line), add the
   book's row to CLAUDE.md's status table; never touch master, push, deploy or run `tools/build.py`.
6. Report: branch, a table of chapters (Bible chapters, pages, verses full/partial/omitted), PNG folder, doubts
   (restraint calls, one-off characters' looks, verses it could not place).

Python: `PYTHONUTF8=1 /c/Users/smorey01/AppData/Local/Python/bin/python.exe`. Playwright: give the subagent the NODE_PATH
of a folder whose `node_modules` has `playwright` (set up once in a scratch folder; renders need it).

## 3. Review (yourself, not the subagent's word)

- `git log --oneline master..<branch>`; `git diff --name-only <base> <branch>` must touch only `tools/full/<pkg>/`,
  `volumes/<id>/`, CLAUDE.md's row, and anything shared it says it changed (e.g. `ntcast.py`) — read those diffs.
- In its worktree: `build_volume.py <pkg> --check` → `0 not found, 0 lost`. Any "omitted" verse: confirm the ASV file
  really lacks it (Matthew 17:21, 18:11, 23:14 are empty in the ASV).
- `NODE_PATH=… python tools/site/sheets.py <id> <scratch>/<id>` (run from its worktree) and look at **every** sheet, then
  open full size (`<scratch>/<id>/png/`) any page that needs a closer look: the passion and other restraint pages, the
  title pages, the end page. Look for: stamps over figures or names, captions over faces, clipped figures, a warm scarf
  reading as long hair, anything drawn that must not be, text overflowing a box, a caption repeated in a balloon.
- Send fixes back to the same subagent (SendMessage to its id) with page names and what to change; re-check its renders.

## 4. Merge and build

- From this worktree (or master): `git merge --no-ff <branch>` with a message naming the book, chapters and pages;
  `build_volume.py <pkg> --check` again on the merged tree; fast-forward master; update CLAUDE.md's status paragraph.
- English site: `python tools/book/downloads.py --lang en <id>` (its EPUB and PDF), then
  `python tools/site/rebuild_site.py --thumbs` (renders only the new thumbnails). Check: the previous book's last page's
  Next leads into the new book; its breadcrumbs lead to `index2.html` for the NT (`index.html` for the OT); the home
  page shows its section, downloads and "Start at the beginning".
- Other languages need the book's labels first (`tools/full/labels.py missing <lang>` → `tools/full/i18n/<lang>/`), then
  `python tools/build.py`. Deploying (`--deploy`) is the user's call; pushing is theirs (SSH passphrase).
