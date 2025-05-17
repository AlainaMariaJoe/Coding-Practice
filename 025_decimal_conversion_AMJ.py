def dec_to_bin(n):
    return bin(n)

def dec_to_oct(n):
    return oct(n)

def dec_to_hex(n):
    return hex(n)

print("Choose your conversion: ")
print(" 1. Decimal to Binary\t 2. Decimal to Octal \t 3. Decimal to Hexadecimal")
choice = int(input("Enter your choice: "))
num = int(input("Enter a number: "))
if choice == 1:
    print(f"Binary of {num} is {dec_to_bin(num)}")
elif choice == 2:
    print(f"Octal of {num} is {dec_to_oct(num)}")
elif choice == 3:
    print(f"Hexadecimal of {num} is {dec_to_hex(num)}")
else:
    print("Invalid choice")


decimal = 10
print(f"\nUsing format specifiers for {decimal}:")
print(f"Binary: {decimal:b}")  
print(f"Octal: {decimal:o}")  
print(f"hexadecimal: {decimal:x}")  
