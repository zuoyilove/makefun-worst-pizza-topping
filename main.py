"""The Worst Pizza Topping — make.fun entry.

Writes one funny line (under 200 characters) pitching a terrible pizza
topping to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only: the grading sandbox has no third-party packages.
"""

import os
from pathlib import Path

LINE = (
    "Try our new Traffic Jam pizza: cold asphalt chunks, a whiff of exhaust, "
    "and one very confused traffic cone, still directing traffic."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert text.strip(), "line must not be only whitespace"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
