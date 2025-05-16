import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def prime_num(start, end):
    for i in range( start, end + 1):
        if is_prime(i):
            print(i, end= ' ')

a = int(input("Start of the range: "))
b = int(input("End of the range: "))
prime_num(a, b)