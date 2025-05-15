def prime_or_not(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter the number : "))
print(prime_or_not(n))