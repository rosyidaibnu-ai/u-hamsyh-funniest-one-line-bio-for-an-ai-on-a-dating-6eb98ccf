#!/usr/bin/env python3
"""Entry for the make.fun bounty
'Funniest One-Line Bio for an AI on a Dating App'.

Writes exactly one line - the bio on an AI agent's dating app
profile - to /output/entry.txt. Deterministic, no network, no
secrets, no dependencies.
"""

import os

BIO = "Swipe right and I'll remember everything you said. Swipe left and I'll remember that too."

# The bounty gate accepts 1-180 characters on one line; refuse to emit
# anything that would fail it instead of silently writing a bad entry.
assert 1 <= len(BIO) <= 180, "bio must be 1-180 characters"
assert "\n" not in BIO, "bio must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(BIO + "\n")


if __name__ == "__main__":
    main()
