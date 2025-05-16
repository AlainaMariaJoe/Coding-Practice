def Sum_natural_num(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def Sum_natural_num2(n):
    return sum([i for i in range(1, n+1)])

def Sum_natural_num3(n):
    return n *(n + 1) // 2

def Sum_natural_num4(n):
    return sum(range(1, n + 1))

def Sum_natural_num5(n):
    if n == 1:
        return 1
    return  n + Sum_natural_num5(n-1)

num = int(input("Enter a number: "))
print(Sum_natural_num(num))