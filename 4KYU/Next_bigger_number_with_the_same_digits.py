def next_bigger(n):
    str_form = str(n)[::-1]
    res = list(str_form)
    for c,i in enumerate(str_form[1:],1):
        for c2,j in enumerate(str_form[:c]):
            if i < j:
                res[c] = j
                res[c2] = i
                index_of_rvs = len(str_form)-c 
                return int("".join(res[::-1][:index_of_rvs] + sorted(res[::-1][index_of_rvs:])))
    return -1