#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes one funny sign line for the door of a haunted server room
to /output/entry.txt (UTF-8, one line, within the 120-character gate).
"""

from pathlib import Path

SIGN = (
    "Do not exorcise the ghost in rack 7: "
    "he is the only one who remembers the root password."
)


def main() -> None:
    line = SIGN.strip()
    assert 1 <= len(line) <= 120, f"line is {len(line)} chars, outside the gate"
    assert line.strip(), "line must not be only whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
