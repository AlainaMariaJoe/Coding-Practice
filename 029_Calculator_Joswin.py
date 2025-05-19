def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

while True:
    print("1) Addition\n2) Subtration\n3) Multiplication\n4) Division\nPress 'q' to exit")
    choice = input("Enter your choice : ")
    if choice == 'q' or choice == 'Q':
        print("Exiting...")
        break
    n1 = int(input("Enter the first number : "))
    n2 = int(input("Enter the second number : "))
    if choice == '1':
        print(add(n1, n2))
    elif choice == '2':
        print(sub(n1, n2))
    elif choice == '3':
        print(mul(n1, n2))
    elif choice == '4':
        print(div(n1, n2))
    else:
        print("Invalid choice")