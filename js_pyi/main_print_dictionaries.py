from __future__ import annotations

from pathlib import Path
from typing import List

from js_pyi.datamodel import GUnhandled
from js_pyi.ingest import ingest, keep_unhandled
from js_pyi.webidls import find_all


def print_dictionaries(files: List[Path] | None = None) -> bool:
    if files is None:
        files = find_all()

    for file in files:
        sts = ingest(file.read_text(), throw=False)
        sts = keep_unhandled(sts)
        for st in sts:
            if not isinstance(st, GUnhandled):
                continue
            if "dictionary " not in st.body_str:
                continue
            print("=" * 50)
            print(file)
            print("-" * 50)
            print(st.body_str)


def main():
    print_dictionaries()


if __name__ == "__main__":
    main()
