import itertools
def permutations(string):
    return list(map("".join,set(itertools.permutations(string))))