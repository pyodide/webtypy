from js_pyi.clipboard import clip_copy
from js_pyi.produce import produce


def generate_python():
    return _head + produce() + _tail


def main():
    code = generate_python()
    print(code)
    clip_copy(code)


_head = """# @formatter:off

from typing import overload, Any, Awaitable, Sequence, Literal, TypedDict, NotRequired
USVString = str


"""
_tail = """

document: Document
window: Window
navigator: Navigator
console: ConsoleNamespace

"""
if __name__ == "__main__":
    main()
