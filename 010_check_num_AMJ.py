def check_num(n):
    if n > 0:
        print (f"{n} is positive")
    elif n == 0:
        print(f"{n} is zero")
    else:
        print(f"{n} is negative")

num = float(input("Enter a number to check : "))
check_num(num)