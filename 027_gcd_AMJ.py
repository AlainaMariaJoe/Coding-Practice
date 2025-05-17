import math
def gcd_num1(a, b):
    return math.gcd(a, b)

def gcd_num2(a, b):
    while b!=0:
        a, b = b, a % b
    return a

def gcd_num3(a, b):
    while a!=b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"GCD of {num1}, {num2} is {gcd_num1(num1, num2)}")
# print(f"GCD of {num1}, {num2} is {gcd_num2(num1, num2)}")
# print(f"GCD of {num1}, {num2} is {gcd_num3(num1, num2)}")