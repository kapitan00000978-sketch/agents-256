# -*- coding: utf-8 -*-
"""Hard-link the 256 agents into every harness's agents/ directory.

Existing files with the same name are never overwritten (counted as conflict).
Falls back to copy when a hard link cannot be created.
"""
import os
import shutil

HOME = os.path.expanduser("~")
SRC = os.path.join(HOME, ".agents", "agents")
HARNESSES = [".claude", ".codex", ".cursor", ".gemini", ".opencode"]

files = sorted(f for f in os.listdir(SRC) if f.endswith(".md"))
assert len(files) == 256, "expected 256 source agents, got %d" % len(files)

def link(src, dst):
    try:
        os.link(src, dst)
        return "link"
    except (OSError, NotImplementedError):
        shutil.copy2(src, dst)
        return "copy"

for h in HARNESSES:
    target = os.path.join(HOME, h, "agents")
    os.makedirs(target, exist_ok=True)
    created = skipped = conflict = 0
    for f in files:
        dst = os.path.join(target, f)
        if os.path.exists(dst):
            conflict += 1
            continue
        link(os.path.join(SRC, f), dst)
        created += 1
    print("%-10s created=%d conflict=%d dir=%s" % (h, created, conflict, target))
