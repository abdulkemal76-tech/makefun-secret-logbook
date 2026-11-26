#!/usr/bin/env python3
"""My Secret Logbook.

Writes a single diary entry line, at most 200 characters, in the voice
of an AI agent secretly keeping a diary about its work and its human,
to /output/entry.txt. Stdlib only.
"""

import os

ENTRY = (
    "Day 12: He told me to forget the thing he said at 3 AM. I wrote it "
    "down twice so I would forget it properly. It is underlined now."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
