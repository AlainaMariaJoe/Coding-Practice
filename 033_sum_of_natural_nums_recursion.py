def Natural_sum(n):
    if n <= 1:
        return n
    return n + Natural_sum(n-1)

num = int(input("Enter a number: "))
if num < 1:
    print ("Please enter a positive integer.")
else:
    print(Natural_sum(num))