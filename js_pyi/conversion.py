from __future__ import annotations

_types_dict = {
    "undefined": "None",
    "any": "Any",
    "DOMString": "str",
    "long": "int",
    "long long": "int",
    "unsigned long": "int",
    "unsigned long long": "int",
    "unsigned short": "int",
    "boolean": "bool",
    "double": "float",
    "unrestricted double": "float",
    "unrestricted float": "float",
    # generics
    "sequence": "Sequence",
    "Promise": "Awaitable",
}


def to_py_type(s) -> str:
    return _types_dict.get(s, s)


_values_dict = {
    "null": "None",
}


def to_py_value(s) -> str:
    return _values_dict.get(s, s)


reserved_keywords = {
    "async",
    "from",
    "break",
    "is",
    "continue",
    "assert",
    "in",
}


def to_py_name(s) -> str:
    if s in reserved_keywords:
        return s + "_"
    return s
