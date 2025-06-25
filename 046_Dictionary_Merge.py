def dict_merge(d1, d2):
    d1.update(d2)
    return d1

d1 = {"one" : 1, "two" : 2}
d2 = {"three" : 3, "four" : 4}

print(dict_merge(d1, d2))