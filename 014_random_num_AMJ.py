import random
def random_num(start, end):
    return random.randint(start, end)

def random_n():
    print (random.random())

n1 = int (input("Start of the range: "))
n2 = int (input("End of the range: "))
print(random_num(n1, n2))
random_n()