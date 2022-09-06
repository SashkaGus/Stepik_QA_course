def merge_intervals(intervals):
    result = []
    for interval in intervals:
        if not result or interval[0] > result[-1][1] + 1:
            result.append(interval)
        result[-1] = result[-1][0], max(result[-1][1], interval[1])
    return result


print(merge_intervals([(1, 4), (2, 6), (8, 10), (12, 19)]))       # == [(1, 6), (8, 10), (12, 19)], "First"
print(merge_intervals([(1, 12), (2, 3), (4, 7)]))               # == [(1, 12)], "Second"
# print(merge_intervals([(1, 5), (6, 10), (10, 15), (17, 20)]))   # == [(1, 15), (17, 20)], "Third"