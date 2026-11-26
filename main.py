"""The Internet in One Word -- make.fun entry.

Writes a single word describing the whole internet to /output/entry.txt.
Pure Python standard library; deterministic; no network, no input files.
"""

import os

WORD = "enshittification"


def main() -> None:
    if not (1 <= len(WORD) <= 30) or not WORD.strip() or len(WORD.split()) != 1:
        raise SystemExit("entry word must be one word of 1-30 non-blank characters")
    out = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    tmp = out + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    os.replace(tmp, out)


if __name__ == "__main__":
    main()
