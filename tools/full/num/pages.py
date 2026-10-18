"""Page registry for a chapter: numbers pages in reading order, so pages drawn by hand and pages packed by a helper
(exo.kit.blueprints, exo.kit.law_pages) can be mixed freely.

    PG = Pages(start)                      # the first story page's number
    @PG.P("NUM-C02-00-Title", "Chapter 2 · …", title=True)
    def title(n): ...                      # title pages are unnumbered
    @PG.P("NUM-C02-P01-…", "The Head")    # board title becomes "11 · The Head"
    def p01(n): ...
    PG.extend(blueprints(items, prefix, PG.next(), …))   # packed pages, numbered from PG.next()
PG.pages is the chapter's PAGES list: [(file name, board title, page fn)]."""

class Pages:
    def __init__(self, start):
        self.start, self.pages, self.n = start, [], start

    def next(self):
        return self.n

    def P(self, name, head, title=False):
        def deco(fn):
            if title:
                self.pages.append((name, head, lambda: fn(None)))
            else:
                n = self.n; self.n += 1
                self.pages.append((name, f"{n} · {head}", lambda: fn(n)))
            return fn
        return deco

    def extend(self, packed):
        self.pages += packed; self.n += len(packed)
