def pig_it(text):
    splittet_list = [list(word) for word in text.split()]
    splittet_list = [''.join(lis[1:] + lis[:1] + ["ay"]) if lis[-1].isalpha() else "".join(lis) for lis in splittet_list]
    return ' '.join(splittet_list)