def largest (a, b, c):
    return a if (a > b and b > c) else b if (b > a and b > c) else c

def largest_num (a, b, c):
    return max (a, b, c)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
print("Largest number: ", largest_num(n1, n2, n3))
print("Largest number: ", largest(n1, n2, n3))