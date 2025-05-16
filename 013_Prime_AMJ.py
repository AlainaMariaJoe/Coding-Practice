import math
def Is_Prime(n):
    if n <= 1:
        return False
    for i in range (2, int(n**(0.5)+1)):
        if n % i == 0:
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


Prime_num = int(input( "Enter a number: "))
if is_prime(Prime_num):
    print(Prime_num,"is a prime number")
else:
    print(Prime_num,"is not a prime number")