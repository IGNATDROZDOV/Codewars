def sum_of_intervals(intervals):
    return len(set([num for item in intervals for num in range(item[0], item[1])]))