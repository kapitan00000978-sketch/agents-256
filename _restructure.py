# -*- coding: utf-8 -*-
"""Restructure the repo into a browsable category layout. Run once, then delete."""
import os
import sys
import shutil

SRC = r"C:\Users\user\.agents\agents-256"
FLAT = r"C:\Users\user\.agents\agents"
REPO = r"C:\Users\user\agents-256"

sys.path.insert(0, SRC)
import catalog_a, catalog_b, catalog_c, catalog_d
ALL = catalog_a.S + catalog_b.S + catalog_c.S + catalog_d.S
assert len(ALL) == 256

ORDER = ["code", "ui", "test", "sec", "data", "ai", "ops", "doc",
         "research", "product", "biz", "creative", "agent", "self", "sys", "game"]
cats = {}
for row in ALL:
    cats.setdefault(row[0], []).append(row[1])
assert set(cats) == set(ORDER), set(cats) ^ set(ORDER)

# agents/<category>/<slug>.md
dst = os.path.join(REPO, "agents")
if os.path.exists(dst):
    shutil.rmtree(dst)
total = 0
for cat in ORDER:
    d = os.path.join(dst, cat)
    os.makedirs(d)
    for slug in cats[cat]:
        shutil.copy2(os.path.join(FLAT, slug + ".md"), os.path.join(d, slug + ".md"))
        total += 1

# tools/
tdst = os.path.join(REPO, "tools")
if os.path.exists(tdst):
    shutil.rmtree(tdst)
os.makedirs(tdst)
for f in sorted(os.listdir(SRC)):
    if f.endswith(".py") or f == "_MANIFEST.md":
        shutil.copy2(os.path.join(SRC, f), os.path.join(tdst, f))

old = os.path.join(REPO, "agents-256")
if os.path.exists(old):
    shutil.rmtree(old)

print("agents/  categories=%d files=%d" % (len(ORDER), total))
print("tools/   files=%d" % len(os.listdir(tdst)))
