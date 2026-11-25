#!/usr/bin/env python3
"""Monday Morning Punchlines entry.

Writes one joke about Monday mornings to /output/entry.txt.
The line is about the alarm, the coffee and the calendar ganging
up before the week has even started.
"""

import os

LINE = (
    "Monday morning: my alarm went off, my coffee filed a complaint, "
    "and my calendar already booked a meeting to discuss why I'm tired."
)


def main():
    # The gate only accepts 1-200 characters of non-blank UTF-8 text,
    # so refuse to write anything outside that range instead of
    # submitting a line the judge would never see. The check runs
    # before anything is written, so a bad line leaves no output.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
