from __future__ import annotations

from pathlib import Path
from typing import List

from js_pyi.ingest import ingest, keep_unhandled
from js_pyi.stringify import s_statements
from js_pyi.webidls import find_all


def unhandled(files: List[Path] | None = None) -> bool:
    if files is None:
        files = find_all()

    for file in files:
        sts = ingest(file.read_text(), throw=False)
        sts = keep_unhandled(sts)
        if len(sts) > 0:
            python_code = s_statements(sts)
            print("=" * 50)
            print(file)
            print("-" * 50)
            print(python_code)


def main():
    # develop([find('EventHandler.webidl')])
    unhandled()


if __name__ == "__main__":
    main()
