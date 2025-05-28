def odd_even_bitwise(n):
    if n & 1:
        print("Odd")
    else:
        print("Even")

n = int(input("Enter a number : "))
odd_even_bitwise(n)
