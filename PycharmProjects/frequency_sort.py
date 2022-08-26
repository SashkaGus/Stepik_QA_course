from typing import Counter
def frequency_sorting(numbers: list[int]) -> list[int]:
    lst = []
    numbers.sort()
    d = Counter(numbers)
    for k in sorted(d, key=d.get, reverse=True):
        for j in range(d[k]):
            lst.append(k)
    return lst


print(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3]))
print(frequency_sorting([99, 99, 55, 55, 21, 21, 10, 10]))




    