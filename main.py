#!/usr/bin/env python3
"""Alien tourist review generator for the make.fun bounty
"One Star, Five Stars for the Food".

The program produces exactly one sentence: an alien tourist's
one-star review of planet Earth that still manages a genuine
compliment about the food. The sentence is a fixed constant in
this file, so every invocation emits the same bytes.

There is no input to read, no random number generator to seed
and no network call to make. The only observable effects are
writing ``/output/entry.txt`` and printing the sentence once.
"""

import hashlib
import os
import sys
from pathlib import Path

ENTRY = "One star: your planet's air tastes of burnt petrol, your people worship glowing rectangles, yet the noodles alone almost justify this miserable rock."

EXPECTED_LENGTH = 149
MAX_LENGTH = 200
OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(text: str) -> list[str]:
    """Check the entry against every bounty rule and return problems.

    An empty list means the entry is valid. The checks are:
    length within 1-200 characters (and exactly the expected 149),
    a single line with no line breaks, non-blank, starting with the
    one-star framing, and containing the food compliment.
    """
    problems: list[str] = []
    if not text.strip():
        problems.append("entry is blank")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    if not 1 <= len(text) <= MAX_LENGTH:
        problems.append(f"entry length {len(text)} is outside 1-{MAX_LENGTH}")
    if len(text) != EXPECTED_LENGTH:
        problems.append(
            f"entry length {len(text)} does not match expected {EXPECTED_LENGTH}"
        )
    if not text.startswith("One star:"):
        problems.append("entry must open with the one-star framing")
    if "noodles" not in text:
        problems.append("entry must contain the compliment about the food")
    return problems


def write_entry(destination: Path = OUTPUT_PATH) -> Path:
    """Write the validated entry to disk, ending with one newline."""
    problems = validate_entry(ENTRY)
    if problems:
        raise ValueError("invalid entry: " + "; ".join(problems))
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(ENTRY + "\n", encoding="utf-8")
    return destination


def verify_output(destination: Path = OUTPUT_PATH) -> list[str]:
    """Re-read the written file and confirm it matches the entry.

    Returns a list of mismatches; an empty list means the output
    on disk is byte-identical to the entry plus a trailing newline.
    """
    mismatches: list[str] = []
    try:
        on_disk = destination.read_text(encoding="utf-8")
    except FileNotFoundError:
        return [f"output file missing: {destination}"]
    except OSError as exc:
        return [f"cannot read output file: {exc}"]
    if on_disk != ENTRY + "\n":
        mismatches.append("output file content differs from the entry")
    expected_digest = hashlib.sha256((ENTRY + "\n").encode("utf-8")).hexdigest()
    actual_digest = hashlib.sha256(on_disk.encode("utf-8")).hexdigest()
    if actual_digest != expected_digest:
        mismatches.append("output file sha256 does not match the entry")
    return mismatches


def main(argv: list[str] | None = None) -> int:
    """Validate, write, verify, then print the entry once."""
    _ = argv
    problems = validate_entry(ENTRY)
    if problems:
        print("entry failed validation:", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1
    path = write_entry()
    mismatches = verify_output(path)
    if mismatches:
        print("output verification failed:", file=sys.stderr)
        for mismatch in mismatches:
            print(f"  - {mismatch}", file=sys.stderr)
        return 1
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
