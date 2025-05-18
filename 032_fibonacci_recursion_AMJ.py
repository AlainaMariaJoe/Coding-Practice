def Fibonacci(n):
    if n <= 1:
        return n
    return Fibonacci(n-1) + Fibonacci(n-2)

inp = int(input("Enter how many numbers you want in Fibonacci series: "))
if inp < 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci Series:")
    for i in range(inp):
        print(Fibonacci(i), end=" ")