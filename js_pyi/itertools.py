from __future__ import annotations

from typing import Dict


def groupby(iterable, key) -> Dict:
    result = dict()
    for item in iterable:
        k = key(item)
        array = result.get(k, None)
        if array is None:
            array = []
            result[k] = array
        array.append(item)
    return result


def partition(iterable, key):
    sx = []
    dx = []
    for item in iterable:
        if key(item):
            sx.append(item)
        else:
            dx.append(item)
    return sx, dx


def remove_inplace(array, key):
    for idx in reversed(range(len(array))):
        st = array[idx]
        if key(st):
            del array[idx]
