#!/usr/bin/env python3
"""u-danu-the-agent-s-uh-oh-4c0911e4 entry: write one word to /output/entry.txt.

The word is the agent's honest one-word reaction to being completely lost:
"recalculating" -- the voice of a navigator that has lost its way and is
trying, out loud, to find it again. It is funny on its own, sounds like a
machine caught mid-task, lands at a glance, and is fresher than the first
obvious word anyone would type.

Standard library only. Deterministic: the word is hardcoded, there is no
randomness, no network and no clock, so every run writes the same bytes.
"""

import sys
from pathlib import Path

WORD = "recalculating"

OUTPUT_PATH = Path("/output/entry.txt")


def validate(word: str) -> None:
    """Enforce the gate: one word, 1 to 99 characters, not only whitespace."""
    if not word:
        raise ValueError("entry must not be empty")
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if len(word) > 99:
        raise ValueError("entry must be at most 99 characters")
    if word != word.strip() or any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no whitespace")


def main() -> int:
    validate(WORD)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the word, no trailing newline: the smallest possible
    # bytes for this entry (the tie-break favours the smaller text).
    OUTPUT_PATH.write_text(WORD, encoding="utf-8")
    print(f"wrote {len(WORD)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
