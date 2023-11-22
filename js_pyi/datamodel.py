from __future__ import annotations

import typing
from dataclasses import dataclass, field
from typing import List, Optional

from js_pyi.stringify import (
    s_method,
    s_attribute,
    s_class,
    s_unhandled,
    s_enum,
    s_arg,
    s_typedef,
    s_ignored,
    s_const,
)


class GPythonProducer:
    def to_python(self) -> str:
        raise Exception(f"not implemented {type(self)}")


class GStmt:
    pass


@dataclass()
class GIgnoredStmt(GStmt, GPythonProducer):
    body_str: str

    def to_python(self):
        return s_ignored(self)


class GRootStmt(GStmt):
    pass


@dataclass()
class GHasName:
    name: str


@dataclass()
class GHasChildren:
    children: List[GStmt] = field(default_factory=list)


@dataclass()
class GNameAndBody(GHasChildren, GHasName):
    pass


@dataclass()
class GUnhandled(GStmt):
    body_str: str
    exception: Exception | None = None

    def to_python(self):
        return s_unhandled(self)


@dataclass()
class GUnhandledRoot(GUnhandled, GRootStmt):
    pass


@dataclass()
class GUnhandledNested(GUnhandled):
    pass


@dataclass()
class GGeneric:
    type: str
    gen_type: str


@dataclass()
class GNotRequired:
    annotation: "GAnnotation"


@dataclass()
class GClass(GRootStmt, GPythonProducer, GHasChildren, GHasName):
    bases: List[str] = field(default_factory=list)
    is_namespace: bool = False

    def to_python(self):
        return s_class(self)


GType = typing.Union[str, GGeneric]
GAnnotation = typing.Union[GType, List[GType], GNotRequired]


@dataclass()
class GNamedAnnotation(GHasName):
    annotation: GAnnotation = field(default_factory=list)


@dataclass()
class GAttribute(GStmt, GNamedAnnotation, GPythonProducer):
    def to_python(self):
        return s_attribute(self)


@dataclass()
class GConst(GStmt, GHasName, GPythonProducer):
    value: str

    def to_python(self):
        return s_const(self)


@dataclass()
class GGeneric(GNamedAnnotation):
    pass


@dataclass
class GArg(GNamedAnnotation, GPythonProducer):
    default: Optional[str] = None

    def to_python(self):
        return s_arg(self)


@dataclass
class GArgVariadic(GArg):
    def to_python(self):
        return s_arg(self)


@dataclass
class GMethod(GStmt, GPythonProducer):
    name: str
    arguments: List[GArg] = field(default_factory=list)
    returns: Optional[GAnnotation] = "undefined"
    overload: bool = False
    classmethod: bool = False

    def to_python(self):
        return s_method(self)


@dataclass()
class GInclude(GRootStmt):
    name: str
    includes: str


@dataclass()
class GTypedef(GRootStmt, GPythonProducer):
    name: str
    annotation: GAnnotation = field(default_factory=list)

    def to_python(self):
        return s_typedef(self)


@dataclass
class GEnum(GRootStmt, GPythonProducer, GHasName):
    values: List[str]

    def to_python(self):
        return s_enum(self)
