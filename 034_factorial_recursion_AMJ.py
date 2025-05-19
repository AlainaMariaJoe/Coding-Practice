def Fact(n):
    if n == 0 or n == 1:
        return 1
    return n * Fact(n-1)

num = int (input("Enter a number: "))
if num < 0:
    print("Factorial does not exist for negative numbers")
else:
    print(f"Factorial of {num}: {Fact(num)}")