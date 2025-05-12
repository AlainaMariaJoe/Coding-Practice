def odd_even(n):
    if n & 1:
        print ("Number is odd")
    else:
        print ("Number is even")

inp = int(input("Enter a number: "))
odd_even(inp)