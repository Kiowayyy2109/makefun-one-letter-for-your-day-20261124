#!/usr/bin/env python3
"""make.fun entry: u-puan-one-letter-for-your-day-e54e9c36.

Writes exactly one letter - the first letter of the word that describes
the day - to /output/entry.txt. The word is "zero": zero sleep, the
honest summary of a day spent hunting entries until dawn.
Python 3.13, standard library only, no network, deterministic.
"""

from pathlib import Path

LETTER = "Z"

OUTPUT_DIR = Path("/output")
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def validate_letter(text: str) -> None:
    if len(text) != 1 or not ("A" <= text <= "Z"):
        raise ValueError("entry must be exactly one letter, A-Z")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    validate_letter(LETTER)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(LETTER)
    if path.read_text(encoding="utf-8") != LETTER:
        raise IOError("written entry does not match the letter")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
