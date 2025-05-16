def armstrong_or_not(n):
    length = len(str(n))
    return sum(map(lambda x: int(x) ** length, str(n))) == n

def armstrong_interval(start, end):
    for i in range(start, end+1):
        if armstrong_or_not(i):
            print(i, end=" ")

start = int(input("Enter the start range : "))
end = int(input("Enter the stop range : "))
armstrong_interval(start, end)