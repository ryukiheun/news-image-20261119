#!/usr/bin/env python3
"""Entry point for the news-image-20261119 bounty.

Copies the pre-rendered infographic ``entry.png`` (drawn by
``draw_image.py``) into the output directory the grader provides:
``$MAKEFUN_OUTPUT_DIR`` when set, otherwise ``/output``.

Standard library only. Deterministic: the output is a byte-for-byte
copy of the bundled image, so repeated runs produce identical bytes.
"""

import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    if not SOURCE.is_file():
        print(f"error: {SOURCE} not found", file=sys.stderr)
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
