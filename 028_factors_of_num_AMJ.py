def factors(n):
    if n >=1:
        return [i for i in range(1, n+1) if n % i == 0 ]
    else:
        print("Please enter a positive integer")
num = int(input("Enter a number: "))
print(factors(num))