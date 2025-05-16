def Armstrong_or_not(n):
    num = n
    l = len(str(n))
    if n <= 0:
        return False
    s = 0
    while n > 0:
        digit = n % 10
        s += digit ** l
        n = n // 10
    return s == num

def Armstrong_or_not2(n):
    s = 0
    for i in str(n):
        s += int(i) ** len(str(n))
    return s == n

num = int(input("Enter a number: "))
if Armstrong_or_not(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
