def if_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_range(start, end):
    for i in range(start, end+1):
        if if_prime(i):
            print(i, end=" ")

prime_numbers_range(1, 200)
