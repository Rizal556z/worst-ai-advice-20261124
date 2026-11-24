#!/usr/bin/env python3
"""Cooling Bath — u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.

Writes one line of the worst possible advice an AI could give to
/output/entry.txt. Pure stdlib, no network.
Entry text: one original line (123 characters, single line).
"""

import os

TEXT = (
    "Certainly! To cool an overheating phone, hold it under running "
    "water \u2014 electronics love a refreshing bath after a long day."
)

# The gate allows 1 to 140 characters, one line, not only white space.
# Fail loudly here rather than submitting an entry the gate would refuse.
assert 1 <= len(TEXT) <= 140, "entry must be 1-140 characters"
assert "\n" not in TEXT.strip(), "entry must be a single line"
assert TEXT.strip(), "entry must not be only white space"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
