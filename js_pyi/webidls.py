from pathlib import Path
from typing import List


def find(filename: str) -> Path:
    for file in _find_all():
        if file.name == filename:
            return file
    raise Exception(f"not found: `{file}`")


def find_all() -> List[Path]:
    return list(sorted(_find_all()))


def _find_all():
    parent = Path(__file__).parent

    yield from _yield_path(parent / "w3c_webref/ed/idl", "*.idl")
    yield from _yield_path(parent / "webidls-manual", "*.webidl")


def _yield_path(path, webidl):
    files = list(path.glob(webidl))
    yield from files
