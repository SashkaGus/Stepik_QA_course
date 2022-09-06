
def highest_building(buildings):
        lst = []
        zip_matr = zip(*buildings)
        trn_matr = [list(row) for row in zip_matr]
        for i in trn_matr:
            val = 0
            for j in range(len(i)):
                val += i[j]
            lst.append(val)
        return [lst.index(max(lst)) + 1, max(lst)]

print(highest_building([
        [0, 0, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]
    ]))

print( highest_building([
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
])) #== [3, 4], "Common"
print( highest_building([
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1]
]) )== [4, 1], "Cabin in the wood"
print( highest_building([
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1]
]) )#== [1, 5], "Triangle"
print( highest_building([
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
])) #== [4, 6], "Pyramid"