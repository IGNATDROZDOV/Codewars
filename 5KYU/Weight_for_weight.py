def order_weight(strng):
    strng = sorted(strng.split(), key=lambda x : str(x))
    return " ".join(sorted(strng, key=lambda x: sum(int(i) for i in str(x))))