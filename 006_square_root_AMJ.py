import math
def Sqrt1(n):
    return round(n ** 0.5, 2)
def Sqrt2(n):
    return round(n ** (1/2), 2)
def Sqrt3(n):
    return round(math.sqrt(n), 2)

number = float (input("Enter a Number: "))
print(Sqrt1(number))
#print(Sqrt3(num))

