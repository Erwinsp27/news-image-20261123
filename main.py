"""Copy the newspaper front page to the grader's output directory.

The image is fixed at build time, so every run writes exactly the
same bytes: the program performs no drawing and no network access.
"""

import os
import shutil
from pathlib import Path


def main():
    source = Path(__file__).resolve().parent / "entry.png"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)
    return destination


if __name__ == "__main__":
    main()
