from __future__ import annotations

import textwrap
import traceback
from io import StringIO
from typing import TYPE_CHECKING, List

from js_pyi.assertions import unhandled
from js_pyi.conversion import to_py_type, to_py_value, to_py_name, reserved_keywords

if TYPE_CHECKING:
    from js_pyi.datamodel import *


def s_attribute(a: GAttribute) -> str:
    return to_py_name(a.name) + s_annotation_named(a.annotation)


def s_const(a: GConst) -> str:
    return to_py_name(a.name) + ' = ' + a.value


def s_arg(a: GArg) -> str:
    default = ''
    if a.default is not None:
        default = ' = ' + to_py_value(a.default)
    name = a.name
    from js_pyi.datamodel import GArgVariadic
    if isinstance(a, GArgVariadic):
        name = '*' + name
    return to_py_name(name) + s_annotation_named(a.annotation) + default


def s_class(i: GClass) -> str:
    bases = ''
    if len(i.bases) > 0:
        bases = '(' + ', '.join(i.bases) + ')'
    name = i.name
    if i.is_namespace:
        name = name.capitalize() + 'Namespace'

    decl = f'class {name}{bases}:'
    if len(i.children) == 0:
        return decl + ' ...'
    for b in i.children:
        python = b.to_python()
        indented = textwrap.indent(python, ' ' * 4)
        decl += '\n' + indented
    return decl


def s_member_name(name: str) -> str:
    if name in reserved_keywords:
        return name + '_'
    return name


def s_method(m: GMethod) -> str:
    returns = ''
    if m.returns is not None and m.returns != 'undefined':
        returns = ' -> ' + s_annotation(m.returns)

    args_arr = ['self'] + [s_arg(a) for a in m.arguments]
    args_str = ', '.join(args_arr)
    name = s_member_name(m.name)
    decorator = ''
    if m.overload:
        decorator = '@overload\n'
    if m.classmethod:
        decorator += '@classmethod\n'
    return f'{decorator}def {name}({args_str}){returns}: ...'


def s_annotation_named(a: GAnnotation) -> str:
    ann = s_annotation(a)
    if ann != '':
        ann = ': ' + ann
    return ann


def s_type(a: GType) -> str:
    if isinstance(a, str):
        return to_py_type(a)

    from js_pyi.datamodel import GGeneric, GNotRequired
    if isinstance(a, GGeneric):
        a: GGeneric
        ann = s_annotation(a.annotation)
        name = to_py_type(a.name)
        return f'{name}[{ann}]'
    if isinstance(a, GNotRequired):
        a: GNotRequired
        ann = s_annotation(a.annotation)
        return f'NotRequired[{ann}]'

    unhandled(a)


def s_annotation(a: GAnnotation) -> str:
    if isinstance(a, list):
        return ' | '.join([s_annotation(e) for e in a])

    return s_type(a)


_invalid_keywords = {'None', 'class', 'in', 'float', 'long', 'int'}


def s_enum(e: GEnum) -> str:
    values = ', '.join(e.values)
    result = f'{e.name} = Literal[{values}]'
    return result


def s_typedef(td: GTypedef) -> str:
    return td.name + ' = ' + s_annotation(td.annotation)


def s_unhandled(u: GUnhandled) -> str:
    ex_str = '<<<\n'
    if u.exception is not None:
        ex_str += 'exception: ' + ''.join(traceback.TracebackException.from_exception(u.exception).format())
        ex_str += '\n' + ('-' * 50) + '\n'
    else:
        ex_str += 'no exception but unhandled:\n'
    return ex_str + u.body_str + '\n>>>\n'


def s_ignored(i: GIgnoredStmt) -> str:
    return '""" # GIgnoredStmt \n' + i.body_str + '\n"""'


def s_statements(statements: List[GStmt]) -> str:
    res = StringIO()
    for st in statements:
        res.write(st.to_python() + '\n\n')
    getvalue = res.getvalue()
    return getvalue
