def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"
    else:
        return result

print("Simple Calculator")
print("Please select operation :\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n")
choice = input("Enter choice : ")
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
if choice == '1':
    print(f"{add(num1, num2)}")
elif choice == '2':
    print(f"{sub(num1, num2)}")
elif choice == '3':
    print(f" {mul(num1, num2)}")
elif choice == '4':
    print(f"{div(num1, num2)}")
else:
    print("Invalid input")