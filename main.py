# SPDX-License-Identifier: MIT
"""Five Seconds to Explain the Glass — entry program.

Writes exactly one line (the cat's defence) to /output/entry.txt.
The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
Tournament notes: drafted candidates about gravity, thirst and jealousy;
the 3 a.m. zoomies runway version won on fresh cat logic with no apology.
"""
from pathlib import Path

LINE = (
    "That glass was sitting in the exact spot where I do my 3 a.m. "
    "zoomies, so I cleared my runway — you're welcome for the takeoff."
)


def main() -> None:
    text = LINE
    # No apology, no confession: the defence must never say sorry.
    assert "sorry" not in text.lower() and "apolog" not in text.lower()
    assert "\n" not in text and 1 <= len(text) <= 200 and text.strip()
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
