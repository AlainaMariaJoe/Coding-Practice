def divisible_range(n, start, end):
    for i in range(start, end+1):
        if i % n == 0:
            print(i, end=" ")


start = int(input("Enter start range : "))
stop = int(input("Enter stop range : "))
n = int(input("Enter a number: "))
divisible_range(n, start, end)