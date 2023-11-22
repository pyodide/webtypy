import pytest

from io import StringIO
from collections.abc import Callable


@pytest.mark.mypy_testing
def type_exception():
    from js import DOMException

    raise DOMException.new("oops")


@pytest.mark.mypy_testing
def type_xmlhttprequest(url: str) -> StringIO:
    from js import XMLHttpRequest

    req = XMLHttpRequest.new()
    req.open("GET", url, False)
    req.send()
    # this were a bit more specific
    reveal_type(req.response)  # R: Any
    return StringIO(req.response)


@pytest.mark.mypy_testing
def type_fetch() -> None:
    from js import fetch


@pytest.mark.mypy_testing
def type_eval():
    from js import eval

    reveal_type(eval("abc"))  # R: Any


@pytest.mark.mypy_testing
def type_timeout(callback: Callable[[], None], timeout: int):
    from js import setTimeout, clearTimeout, setInterval, clearInterval
    from pyodide.ffi import JsProxy

    timeout_retval: int | JsProxy = setTimeout(callable, timeout)
    clearTimeout(timeout_retval)

    setInterval(callable, timeout)
    clearInterval(timeout_retval)


@pytest.mark.mypy_testing
def type_object():
    from js import Object
    from pyodide.ffi import JsProxy

    a: JsProxy = Object.fromEntries([[1, 2]])


@pytest.mark.mypy_testing
def type_buffer(selenium):
    from js import Uint8Array, ArrayBuffer

    a = Uint8Array.new(range(10))
    assert ArrayBuffer.isView(a)

    from tempfile import TemporaryFile

    with TemporaryFile() as f:
        a.to_file(f)
        f.seek(0)
        assert f.read() == a.to_bytes()

    import js

    assert js.Float64Array.BYTES_PER_ELEMENT == 8


@pytest.mark.mypy_testing
def type_json():
    from js import JSON, Array
    from pyodide.ffi import to_js
    import json

    class Pair:
        __slots__ = ("first", "second")

        def __init__(self, first, second):
            self.first = first
            self.second = second

    p1 = Pair(1, 2)
    p2 = Pair(1, 2)
    p2.first = p2

    def default_converter(value, convert, cacheConversion):
        result = Array.new()
        cacheConversion(value, result)
        result.push(convert(value.first))
        result.push(convert(value.second))
        return result

    p1js = to_js(p1, default_converter=default_converter)
    p2js = to_js(p2, default_converter=default_converter)

    assert json.loads(JSON.stringify(p1js)) == [1, 2]


@pytest.mark.mypy_testing
def type_document():
    from js import document

    el = document.createElement("div")
    assert el.tagName == "DIV"
    assert bool(el)
    assert document.body
    assert not document.body.children
    document.body.appendChild(el)
    assert document.body.children
    assert len(document.body.children) == 1
    assert document.body.children[0] == el
    assert repr(document) == "[object HTMLDocument]"
    assert len(dir(el)) >= 200
    assert "appendChild" in dir(el)


@pytest.mark.mypy_testing
def type_canvas():
    from js import document

    canvas = document.createElement("canvas")
    canvas.id = "canvas"
    canvas.width = 320
    canvas.height = 240

    canvas.style.position = "fixed"
    canvas.style.bottom = "10px"
    canvas.style.right = "10px"

    gl = canvas.getContext(
        "webgl2",
        powerPreference="high-performance",
        premultipliedAlpha=False,
        antialias=False,
        alpha=False,
        depth=False,
        stencil=False,
    )
    assert document.body
    document.body.appendChild(canvas)
