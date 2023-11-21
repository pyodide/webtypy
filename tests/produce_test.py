import ast

from js_pyi.produce import produce, parse_product
from js_pyi.webidls import find


def x_test_correctness_quick_0():
    actual = produce([find("Element.webidl")])
    print(actual)
    ast.parse(actual)

    assert (
        "class Element(Node, ChildNode, NonDocumentTypeChildNode, ParentNode, Animatable, GeometryUtils):"
        in actual
    )
    expected = ["ScrollLogicalPosition", "start", "center", "end"]
    for each in expected:
        assert each in actual


def x_test_correctness_quick_1():
    actual = produce([find("Document.webidl")])
    assert "class Document(Node" in actual
    ast.parse(actual)


def test_correctness_slow_0():
    success = parse_product()
    assert success
