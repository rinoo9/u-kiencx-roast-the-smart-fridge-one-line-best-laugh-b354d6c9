#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Deterministic entry program: writes exactly one roast line
(104 characters, single line, UTF-8) to /output/entry.txt.
No input, no randomness, no network.
"""

import os

ENTRY = (
    "My smart fridge lost its Wi-Fi and now it's just a $3,000 night-light "
    "silently judging my 2 a.m. snacks."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, must be 1-160"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
