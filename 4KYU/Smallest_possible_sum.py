import numpy as np

def solution(a):
    input_arr = np.array(a)
    length = input_arr.size
    min = input_arr[0]
    
    for i in range(length):

        if min == 1:
            return 1 * (length)

        if min > input_arr[i] and min % input_arr[i] != 0:
            min %= input_arr[i]

        if min < input_arr[i] and input_arr[i] % min != 0:
            min = input_arr[i] % min

    return min * (length)