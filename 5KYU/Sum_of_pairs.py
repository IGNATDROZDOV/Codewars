def sum_pairs(ints, s):
    used_set = set()
    for i in ints:
        if (s - i) in used_set:
            return [s - i, i]
        used_set.add(i)