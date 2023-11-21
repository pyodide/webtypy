from __future__ import annotations

from typing import List

from js_pyi.assertions import expect_isinstance
from js_pyi.datamodel import GStmt, GUnhandled, GClass, GInclude, GEnum, GMethod
from js_pyi.itertools import partition, groupby as groupby2, groupby


def _fix_constructor(cl: GClass):
    constructors = list(filter(lambda m: isinstance(m, GMethod) and m.name == 'constructor', cl.children))
    for c in constructors:
        c: GMethod
        c.name = 'new'
        c.returns = cl.name
        c.classmethod = True
        cl.children.remove(c)

    cl.children[:0] = constructors


def _mark_method_overload(cl: GClass):
    methods = filter(lambda m: isinstance(m, GMethod), cl.children)
    by_name = groupby(methods, lambda m: m.name)
    for name, methods in by_name.items():
        if len(methods) > 1:
            for m in methods:
                m: GMethod
                m.overload = True


def merge(statements: List[GStmt]) -> List[GStmt]:
    unhandled, handled = partition(statements, lambda e: isinstance(e, GUnhandled))
    enums: List[GStmt] = []
    classes: List[GStmt] = []
    the_rest: List[GStmt] = []
    by_name = groupby2(handled, lambda stmt: stmt.name)
    # { 'Doc' : [ GClass('Doc', ... ), GClass('Doc', ...), GInclude('Doc', ...) ] , ... }
    for name, sts_for_name in by_name.items():
        by_type = groupby2(sts_for_name, lambda s: type(s))
        if GClass in by_type:
            mi = _m_class(by_type)
            _fix_constructor(mi)
            _mark_method_overload(mi)
            classes.append(mi)
        elif GEnum in by_type:
            assert len(sts_for_name) == 1
            enums.append(sts_for_name[0])
        else:
            the_rest.extend(sts_for_name)

    return enums + the_rest + classes + unhandled


def _m_class(by_type) -> GClass:
    # { GClass : [ ... ] , GInclude : [ ... ] }
    class_stmts = by_type.pop(GClass)
    class_stmt = _m_gclasses(class_stmts)
    include_stmts = by_type.pop(GInclude, None)
    if include_stmts is not None:
        _m_class_include(class_stmt, include_stmts)
    return class_stmt


def _m_gclasses(statements: List[GClass]) -> GClass:
    # check pre-conditions
    name = None
    for st in statements:
        expect_isinstance(st, GClass)
        if name is None:
            name = st.name
        else:
            assert st.name == name

    result = GClass(name, is_namespace=st.is_namespace)
    for st in statements:
        result.bases.extend(st.bases)
        result.children.extend(st.children)
    return result


def _m_class_include(class_stmt: GClass, include_stmts: List[GInclude]):
    for inc in include_stmts:
        class_stmt.bases.append(inc.includes)
