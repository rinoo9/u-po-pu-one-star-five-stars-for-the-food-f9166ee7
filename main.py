"""Write the one-sentence alien tourist review of Earth to /output/entry.txt.

Deterministic: no input, no randomness, no network. The entry text is
fixed in this file and written byte-identically on every run.
"""

import os
from pathlib import Path

ENTRY = "One star: your planet's air tastes of burnt petrol, your people worship glowing rectangles, yet the noodles alone almost justify this miserable rock."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"

    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
