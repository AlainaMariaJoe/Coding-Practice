def largest_of_three_1(a, b, c):
    return max(a, b, c)

def largest_of_three_2(a, b, c):
    return a if a > b and a > c else b if b > c else c

def largest_of_three_3(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
    
def largest_of_three_4(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
    
a, b, c = map(int, input("Enter three numbers : ").split(","))

print(largest_of_three_1(a, b, c))
print(largest_of_three_2(a, b, c))
print(largest_of_three_3(a, b, c))
print(largest_of_three_4(a, b, c))