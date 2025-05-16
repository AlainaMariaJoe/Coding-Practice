def C_to_F(value):
    return (value * 9/5) + 32
def F_to_C(value):
    return (value - 32) * 5/9

print("Choose operation: ")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = int(input("Enter your choice: "))
if choice == 1:
    value = float(input("Enter temperature in C: "))
    print(f"{value} C : {round(C_to_F(value), 2)} F")
else:
    value = float(input("Enter temperature in F: "))
    print(f"{value} F : {round(F_to_C(value), 2)} C")