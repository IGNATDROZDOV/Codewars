def beeramid(bonus, price):
    amount_of_glasses = bonus//price
    iter_num = 0
    while((iter_num+1) * (iter_num+1) <= amount_of_glasses):
        iter_num += 1
        amount_of_glasses -= iter_num * iter_num
    return iter_num