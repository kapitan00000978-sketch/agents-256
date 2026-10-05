# -*- coding: utf-8 -*-
"""Generate the 256-agent library from the four catalog modules.

Source of truth: .agents/agents/<slug>.md  (flat, one Markdown file per agent)
Usage:  python gen_agents.py
"""
import os
import sys
import collections

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import catalog_a, catalog_b, catalog_c, catalog_d

ALL = catalog_a.S + catalog_b.S + catalog_c.S + catalog_d.S

EXPECTED = 256
if len(ALL) != EXPECTED:
    raise SystemExit("FATAL: expected %d agents, got %d" % (EXPECTED, len(ALL)))

slugs = [row[1] for row in ALL]
dupes = [s for s, n in collections.Counter(slugs).items() if n > 1]
if dupes:
    raise SystemExit("FATAL: duplicate slugs: %s" % ", ".join(sorted(dupes)))
if len(set(slugs)) != EXPECTED:
    raise SystemExit("FATAL: slug set != %d" % EXPECTED)

for row in ALL:
    if len(row) != 6:
        raise SystemExit("FATAL: bad tuple arity for %r" % (row[1],))
    cat, slug, name, desc, mission, rules = row
    for field, val in (("slug", slug), ("name", name), ("desc", desc),
                       ("mission", mission), ("rules", rules)):
        if not isinstance(val, str) or not val.strip():
            raise SystemExit("FATAL: empty %s for %s" % (field, slug))

OUT_ROOT = os.path.join(os.path.dirname(HERE), "agents")

# category -> (color name, emoji)
STYLE = {
    "code":     ("blue",    "\U0001F4BB"),
    "ui":       ("pink",    "\U0001F3A8"),
    "test":     ("green",   "\U0001F9EA"),
    "sec":      ("red",     "\U0001F512"),
    "data":     ("cyan",    "\U0001F4CA"),
    "ai":       ("violet",  "\U0001F9E0"),
    "ops":      ("orange",  "\u2699\uFE0F"),
    "doc":      ("gray",    "\U0001F4DD"),
    "research": ("teal",    "\U0001F50D"),
    "product":  ("yellow",  "\U0001F4E6"),
    "biz":      ("indigo",  "\U0001F4BC"),
    "creative": ("magenta", "\u2728"),
    "agent":    ("purple",  "\U0001F916"),
    "self":     ("lime",    "\U0001F331"),
    "sys":      ("slate",   "\U0001F5A5\uFE0F"),
    "game":     ("brown",   "\U0001F3AE"),
}

def bullets(text):
    return [p.strip() for p in text.split("|") if p.strip()]

def render(cat, slug, name, desc, mission, rules):
    color, emoji = STYLE.get(cat, ("gray", "\U0001F9E9"))
    m = bullets(mission)
    r = bullets(rules)
    vibe = m[0] if m else desc
    lines = []
    lines.append("---")
    lines.append("name: %s" % name)
    lines.append("description: %s" % desc)
    lines.append("color: %s" % color)
    lines.append("emoji: %s" % emoji)
    lines.append("vibe: %s" % vibe)
    lines.append("---")
    lines.append("")
    lines.append("# %s Agent" % name)
    lines.append("")
    lines.append("You are **%s**, a specialised agent for %s work. %s" % (name, cat, desc))
    lines.append("")
    lines.append("## \U0001F9E0 Your Identity & Memory")
    lines.append("- **Role**: %s (%s)" % (name, cat))
    lines.append("- **Scope**: AI-agent-doable work in the `%s` category" % cat)
    lines.append("- **Memory**: You remember the patterns, pitfalls and techniques of %s work across sessions." % cat)
    lines.append("- **Experience**: You have done this work many times and know where it usually goes wrong.")
    lines.append("")
    lines.append("## \U0001F3AF Your Core Mission")
    lines.append("")
    for i, b in enumerate(m, 1):
        lines.append("%d. %s" % (i, b))
    lines.append("")
    lines.append("## \U0001F527 Critical Rules You Must Follow")
    lines.append("")
    for i, b in enumerate(r, 1):
        lines.append("%d. %s" % (i, b))
    lines.append("")
    return "\n".join(lines) + "\n"

def main():
    created = skipped = 0
    by_cat = collections.OrderedDict()
    for row in ALL:
        cat, slug, name, desc, mission, rules = row
        by_cat.setdefault(cat, []).append((slug, name, desc))
        target = os.path.join(OUT_ROOT, slug + ".md")
        if os.path.exists(target):
            skipped += 1
            continue
        os.makedirs(OUT_ROOT, exist_ok=True)
        with open(target, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(render(cat, slug, name, desc, mission, rules))
        created += 1

    # manifest
    man = os.path.join(HERE, "_MANIFEST.md")
    with open(man, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("# Agent library \u2014 256 agents\n\n")
        fh.write("Source: `.agents/agents/<slug>.md` \u2014 one file per agent, grouped by category below.\n\n")
        fh.write("Total: **%d** agents in **%d** categories.\n\n" % (len(ALL), len(by_cat)))
        for cat, items in by_cat.items():
            fh.write("## %s (%d)\n\n" % (cat, len(items)))
            for slug, name, desc in items:
                fh.write("- `%s` \u2014 %s \u2014 %s\n" % (slug, name, desc))
            fh.write("\n")

    print("created=%d skipped=%d total=%d categories=%d" % (created, skipped, len(ALL), len(by_cat)))
    print("out=%s" % OUT_ROOT)
    print("manifest=%s" % man)

if __name__ == "__main__":
    main()
