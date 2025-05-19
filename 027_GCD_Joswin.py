def gcd_recursion(a, b):
    if b == 0:
        return a
    return gcd_recursion(b, a % b)

def gcd_for_loop(a, b):
    for i in range(min(a,b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
print(gcd_recursion(a, b))
print(gcd_for_loop(a, b))