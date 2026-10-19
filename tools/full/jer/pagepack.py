"""discourse.pack with one more pass, for the long prophecies: a page holding a lone panel is merged with a neighbour (or
takes the previous page's last panel) when the two still fit, so no page is a single short panel."""
import re
import mk
from fx import page, vref, new
from genesis.ch02 import rows, W1
import speech
from genesis import art as X
from discourse import _chars, _need, _sizes, _span

def _fits(g, budget, cap, most):
    return len(g) <= most and sum(_chars(s) + (250 if s["h"] else 0) for s in g) <= budget and sum(_need(s) for s in g) <= cap - 12 * (len(g) - 1)

def _mend(groups, budget, cap, most):
    """Lone panels: join the next page, or take the previous page's last panel, or join the previous page, when it fits."""
    changed = True
    while changed:
        changed = False
        for i, g in enumerate(groups):
            if len(g) != 1: continue
            if i + 1 < len(groups) and _fits(g + groups[i + 1], budget * 1.15, cap * 1.08, most):
                groups[i:i + 2] = [g + groups[i + 1]]; changed = True; break
            if i > 0 and len(groups[i - 1]) >= 3 and _fits(groups[i - 1][-1:] + g, budget * 1.15, cap * 1.08, most):
                groups[i] = groups[i - 1][-1:] + g; groups[i - 1] = groups[i - 1][:-1]; changed = True; break
            if i > 0 and _fits(groups[i - 1] + g, budget * 1.15, cap * 1.08, most):
                groups[i - 1:i + 1] = [groups[i - 1] + g]; changed = True; break
    return groups

def pack(segments, prefix, start, book="Jeremiah", code="JER", budget=1250, most=3, end="", default_head=None, by_need=True, room=0.92, min_size=12.5):
    cap = 1022 * room
    groups, cur, chars, need = [], [], 0, 0
    for s in segments:
        n = _chars(s) + (250 if s["h"] else 0)
        nd = _need(s)
        if cur and (chars + n > budget or len(cur) == most or (s["head"] and chars > budget * 0.45) or (by_need and need + nd > cap - 12 * len(cur))):
            groups.append(cur); cur, chars, need = [], 0, 0
        cur.append(s); chars += n; need += nd
    if cur: groups.append(cur)
    groups = _mend(groups, budget, cap, most)
    if min_size:
        i = 0
        while i < len(groups):
            g = groups[i]
            if len(g) > 1 and min(_sizes(g)) < min_size:
                cut = max(1, len(g) // 2)
                groups[i:i + 1] = [g[:cut], g[cut:]]
                continue
            i += 1
    out, head_now, side = [], default_head or "", False
    for k, g in enumerate(groups):
        needs = [_need(s) for s in g]
        room_ = 1022 - 12 * (len(g) - 1)
        fixed = [s["h"] for s in g]
        flex_total = sum(nd for nd, fx in zip(needs, fixed) if not fx) or 1
        flex_room = room_ - sum(fx for fx in fixed if fx)
        hs = [fx if fx else max(150, round(flex_room * nd / flex_total)) for nd, fx in zip(needs, fixed)]
        hs[-1] = None
        t, h = rows(*hs)
        body = []
        for i, (s, hh) in enumerate(zip(g, h)):
            flip = s["flip"] if s["flip"] is not None else side
            if s["tok"]: side = not side
            extra = s["extra"]
            if s["stamp"]:
                pos = (("right" if flip else "left") + ": 14px; top: 12px") if s["tok"] else "right: 14px; bottom: 36px" if s["lines"] else "right: 14px; top: 12px"
                extra += mk.stamp(s["stamp"], pos)
            lines = s["lines"]
            if end and k == len(groups) - 1 and i == len(g) - 1:
                if s["tok"] and lines:
                    lines = lines + [("raw", re.sub(r"position: absolute; (?:(?:left|right|top|bottom): [-\d.]+px; )+", "align-self: flex-end; ", end))]
                else:
                    extra += end
            if s["lines"]:
                art = (s["art"](W1, hh) if callable(s["art"]) else s["art"]) if s["art"] is not None else (X.cosmic(W1, hh) if s["tok"] is None else "")
                body.append(speech.orate(s["tok"], hh, s["bg"], lines, ref=s["ref"], flip=flip, art=art, top=s["tok"] is None and s["art"] is not None, extra=extra, hi=s["hi"]))
            else:
                art = s["art"](W1, hh) if callable(s["art"]) else (s["art"] or "")
                body.append(new(s["bg"], W1, hh, art, (vref(s["ref"], "right: 12px; bottom: 12px") if s["ref"] else "") + extra))
        for s in g:
            if s["head"]: head_now = s["head"]
        refs = [s["ref"] for s in g if s["ref"] and s["lines"]] or [s["ref"] for s in g if s["ref"]]
        rng = _span(refs, code)
        title = f"{book} {rng} — {head_now}"
        slug = re.sub(r"[^A-Za-z]", "", head_now.title())[:18]
        out.append((f"{prefix}-P{k + 1:02d}-{slug}", f"{start + k} · {head_now}", (lambda title=title, t=t, body="".join(body), n=start + k: page(title, t, body, n))))
    return out
