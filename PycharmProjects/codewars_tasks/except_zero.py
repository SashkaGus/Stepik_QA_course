from typing import Iterable


def except_zero(items: list) -> Iterable:
    nnull_items = []
    for i in items:
        nnull_items.append(i) if i != 0 else 0
    nnull_items.sort()
    while nnull_items:
        for j in range(len(items)):
            if items[j] != 0:
                items[j] = nnull_items[0]
                try:
                    nnull_items.pop(0)
                except IndexError:
                    break
    return items

print(except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])) 
print(except_zero([0, 2, 3, 1, 0, 4, 5])) 
print(except_zero([0, 0, 0, 1, 0])) 
print(except_zero([4, 5, 3, 1, 1])) 
print(except_zero([0, 0])) 