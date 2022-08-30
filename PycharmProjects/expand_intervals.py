def expand_intervals(intervals):
    if intervals:
        res, j = [], 0
        for i in intervals:
            res.append(i[0])
            if i[0] < i[1]:
                j = i[0]
                while j < i[1]:
                    j += 1
                    res.append(j)
        return res
    else:
        return []


print(expand_intervals([(1, 3), (5, 7)]))# == [1, 2, 3, 5, 6, 7]
print(expand_intervals([(1, 3)]))# == [1, 2, 3]
print(expand_intervals([])) #== []
print(expand_intervals([(1, 2), (4, 4)]))# == [1, 2, 4]