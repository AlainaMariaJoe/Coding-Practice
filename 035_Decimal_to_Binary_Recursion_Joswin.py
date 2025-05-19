def decimal_to_binary_recursion(n):
    if n == 0 or n == 1:
        return str(n)
    return decimal_to_binary_recursion(n // 2) + str(n % 2)

def dec_to_bin_rec(n):
    if n > 1:
        dec_to_bin_rec(n // 2)
    print(n % 2, end='')


n = int(input("Enter the decimal : "))
print(decimal_to_binary_recursion(n))
dec_to_bin_rec(n)