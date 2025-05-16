def Fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print (a, end=' ')
        a, b = b, a+b
    
num = int(input("Enter how many fibonacci numbers to display: "))
Fibonacci(num)