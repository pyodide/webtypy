from __future__ import annotations

import ast
import traceback
from pathlib import Path
from typing import List

from js_pyi.ingest import ingest, keep_python_producer
from js_pyi.merge import merge
from js_pyi.stringify import s_statements
from js_pyi.webidls import find_all


def produce(files: List[Path] | None = None) -> str:
    if files is None:
        files = find_all()

    statements = []
    for file in files:
        sts = ingest(file.read_text(), throw=False)
        statements.extend(sts)

    statements = merge(statements)
    statements = keep_python_producer(statements)

    python_code = s_statements(statements)

    return python_code


def parse_product() -> bool:
    exceptions = []
    for file in find_all():
        python_code = produce([file])
        try:
            ast.parse(python_code)
        except Exception as ex:
            exceptions.append((file.name, traceback.format_exc(), python_code))
    print()
    for file, ex, python_code in exceptions:
        print("=" * 50)
        print("file", file)
        print("-" * 50)
        print("exception", ex)
        print("-" * 50)
        print("full source")
        print(python_code)

    success = len(exceptions) == 0
    return success
