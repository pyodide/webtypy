from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List

from js_pyi.datamodel import GStmt, GClass, GMethod
from js_pyi.ingest import ingest, keep_python_producer, keep_unhandled
from js_pyi.itertools import groupby
from js_pyi.stringify import s_statements
from js_pyi.webidls import find_all


@dataclass
class GClassOverload:
    gclass: GClass
    overloads: List[GOverload]


@dataclass
class GOverload:
    name: str
    methods: List[GMethod]


def _keep_classes_with_overloads(sts: List[GStmt]) -> List[GClass]:
    result = []
    classes = filter(lambda e: isinstance(e, GClass), sts)
    for cl in classes:
        overloads = []
        cl: GClass

        by_name = groupby(cl.children, lambda e: e.name)
        for name, methods in by_name.items():
            if len(methods) > 1:
                overloads.extend(methods)

        if len(overloads) > 0:
            result.append(GClass(cl.name, overloads))

    return result


def print_overloaded(files: List[Path] | None = None):
    if files is None:
        files = find_all()

    for file in files:
        sts = ingest(file.read_text(), throw=False)
        # sts = merge(sts)
        sts = keep_python_producer(sts)
        sts = _keep_classes_with_overloads(sts)
        if len(sts) > 0:
            print("=" * 50)
            print(file)
            for cl in sts:
                python_code = cl.to_python()
                print("-" * 50)
                print(python_code)


def print_unhandled(files: List[Path] | None = None) -> bool:
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
    print_overloaded()


if __name__ == "__main__":
    main()
