def decimal_to_binary(n):
    if n == 0 or n == 1:
        return str(n)
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

num = int(input("Enter a decimal number: "))
if num < 0:
    print("Please enter a positivr integer.")
else:
    print(f"The binary  of {num} is {decimal_to_binary(num)}")
