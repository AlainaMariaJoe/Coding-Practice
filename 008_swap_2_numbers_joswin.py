def swap(a, b):
    temp = a
    a = b
    b = temp
    print(f"a : {a}")
    print(f"b : {b}\n")

def swap_variable(a, b):
    a, b = b, a
    print(f"a : {a}")
    print(f"b : {b}\n")

def swap_bitwise(a, b):
    try:
        a, b = int(a), int(b)
        a = a ^ b
        b = a ^ b
        a = a ^ b
        print(f"a : {a}")
        print(f"b : {b}\n")
    except:
        print("Variables not int")

a = input("Enter data of first variable : ")
b = input("Enter data of second variable : ")

print("Before swap\n")
print(f"a : {a}")
print(f"b : {b}\n")

print("After swap\n")

swap(a, b)
swap_variable(a, b)
swap_bitwise(a, b)