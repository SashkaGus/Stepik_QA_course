from typing import Iterable


def compress(items: list) -> Iterable:
    lst = []
    i = 1
    if items:
        lst.append(items[0])
        for i in range(1, len(items)):
            if items[i] != items[i-1]:
                lst.append(items[i])
    return lst

compress([9, 9, 9, 9, 9, 9, 9])