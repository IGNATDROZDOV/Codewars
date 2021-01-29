from itertools import zip_longest
def interleave(*args):
        divided_list = list(zip_longest(*args))
        return [item for sublist in divided_list for item in sublist]