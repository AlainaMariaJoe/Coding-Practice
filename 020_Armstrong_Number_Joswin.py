def armstrong_or_not(n):
    length = len(str(n))
    total = 0
    for i in str(n):
        total += int(i) ** length
    return total == n

def armstrong_or_not_using_map(n):
    return sum(map(lambda x: int(x) ** len(str(n)), str(n))) == n

n = int(input("Enter the number : "))
print(armstrong_or_not(n))
print(armstrong_or_not_using_map(n))