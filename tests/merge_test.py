from __future__ import annotations

from js_pyi.datamodel import GMethod
from js_pyi.ingest import ingest
from js_pyi.merge import merge
from tests.ingest_stringify_test import _append_base


def test_merge():
    piece1 = ingest('interface Doc : Blob  { attribute Blob foo; }')
    piece2 = ingest('partial interface Doc  { attribute Element bar; }')

    expected = ingest('interface Doc : Blob {  attribute Blob foo; attribute Element bar; }')

    actual = merge(piece1 + piece2)
    assert actual == expected


def test_merge_include():
    piece1 = ingest('interface Doc : Blob  { attribute Blob foo; }')
    piece2 = ingest('partial interface Doc  { attribute Element bar; }')
    piece3 = ingest('Doc includes Bar; Doc includes Baz')

    actual = merge(piece1 + piece2 + piece3)

    expected = ingest('interface Doc : Blob {  attribute Blob foo; attribute Element bar; }')
    _append_base(expected[0], 'Bar')
    _append_base(expected[0], 'Baz')

    assert actual == expected


def test_merge_method_overload():
    idl = 'interface Doc { Blob foo();\n Blob bar(); \n Blob foo(bool arg); }'
    interface = merge(ingest(idl))[0]
    assert len(interface.children) == 3
    for m in interface.children:
        m: GMethod
        if m.name == 'foo':
            assert m.overload
            assert '@overload' in m.to_python()
        else:
            assert not m.overload


def test_merge_constructor_overload():
    idl = 'interface Doc { constructor();\n constructor(bool arg); }'
    interface = merge(ingest(idl))[0]
    assert len(interface.children) == 2
    for m in interface.children:
        m: GMethod
        assert m.name == 'New'
        assert m.returns == 'Doc'
        assert m.overload
        assert '@overload' in m.to_python()


def test_merge_namespace():
    piece1 = ingest('namespace Doc { undefined clear(); }')
    piece2 = ingest('namespace Doc { undefined foo(int over); }')

    actual = merge(piece1 + piece2)

    expected = ingest('namespace Doc { undefined clear(); undefined foo(int over); }')

    assert actual == expected
