def factorial(n):
    if n < 0:
        return "Factorial doesn't exist"
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def factorial_recursion(n):
    if n < 0:
        return "Factorial doesn't exist"
    if n == 0:
        return 1
    return n * factorial_recursion(n - 1)

n = int(input("Enter the number : "))
print(factorial(n))
print(factorial_recursion(n))