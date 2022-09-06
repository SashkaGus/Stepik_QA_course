from typing import Iterable


def remove_all_after(items: list, border: int) -> Iterable:
    fin_list = []
    if items:
        for i in items:
            if i != border:
                fin_list.append(i)
            else:
                fin_list.append(i)
                break
    else:
        fin_list = []
    return fin_list;

print(remove_all_after([1, 2, 3, 4, 5], 3)) 
print(remove_all_after([1, 1, 2, 2, 3, 3], 2)) 
print(remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)) 
print(remove_all_after([1, 1, 5, 6, 7], 2))
print(remove_all_after([], 0))
print(remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7))