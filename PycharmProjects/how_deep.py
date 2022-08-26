from hashlib import new
import re


def how_deep(l):
    if isinstance(l, (list, tuple)):
        t = []
        for itm in l:
            t += how_deep(itm),
        return 1 + (max(t) if t else 0)
    return 0


print(how_deep((1, 2, 3)))
print(how_deep((1, 2, (3,))))
print(how_deep((1, 2, (3, (4,)))))
print(how_deep(()))
print(how_deep(((),)))
print(how_deep((((),),)))
print(how_deep((1, (2,), (3,))))
print(how_deep((1, ((),), (3,))))
print(how_deep([1,[2],[2,[3]]]))