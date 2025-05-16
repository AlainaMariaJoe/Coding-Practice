def Factorial (n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a number: "))
print(f"Factorial of {number} is {Factorial(number)}")
        

