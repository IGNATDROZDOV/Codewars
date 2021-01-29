def move_zeros(array):
    return [i for i in array if i != 0 or isinstance(i, bool)] + [i for i in array if i == 0 and not isinstance(i, bool)]