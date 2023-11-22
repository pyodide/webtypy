from __future__ import annotations


def unhandled(argument):
    raise Exception(f"unhandled type={type(argument)} `{argument}`")


def expect_isinstance(instance, *any_of):
    if any(map(lambda et: isinstance(instance, et), any_of)):
        return
    raise Exception(
        f" expect instance to be `{any_of}` "
        f"but instead found to be `{type(instance)}`"
    )
