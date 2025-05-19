def decimal_to_binary(n):
    return bin(n)[2:]

def decimal_to_octal(n):
    return oct(n)[2:]

def decimal_to_hexadecimal(n):
    return hex(n)[2:]

def decimal_to_binary_format(n):
    return f"{n:b}"

def decimal_to_octal_format(n):
    return f"{n:o}"

def decimal_to_hexadecimal_format(n):
    return f"{n:x}"


n = int(input("Enter the decimal to convert : "))
print(f"Binary is : {decimal_to_binary(n)}")
print(f"Binary using format specifier : {decimal_to_binary_format(n)}")
print(f"Octal is : {decimal_to_octal(n)}")
print(f"Octal using format sepcifier : {decimal_to_octal_format(n)}")
print(f"Hexadecimal is : {decimal_to_hexadecimal(n)}")
print(f"Hexadecimal using format specifier : {decimal_to_hexadecimal_format(n)}")