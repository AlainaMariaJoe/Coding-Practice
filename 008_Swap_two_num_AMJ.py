def swap_num1(a, b):
    a, b = b, a
    return a, b

def swap_num2(a, b):
    temp = a
    a = b
    b = temp
    return a, b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f" Before swapping: {num1},{num2}")
print(f" After swapping: {swap_num1(num1, num2)}")
print(f" After swapping : {swap_num2(num1, num2)}")

