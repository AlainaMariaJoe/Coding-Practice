def merge_update(d1, d2):
    d1.update(d2)
    return d1

def merge_unpack(d1, d2):
    return {**d1, **d2}

def merge_operator(d1, d2):
    return d1 | d2


d1 = {"Name1" : "AMJ", "Age1" : 21, "Gender1" : "Female", "Status1" : "Single"}
d2 = {"Name2" : "Joswin", "Age2" : 22, "Gender2" : "Male", "Status2" : "Ready to mingle"}
print(merge_update(d1, d2))