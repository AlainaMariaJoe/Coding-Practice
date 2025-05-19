def divisible_by_n_range(n, start, end):
    for i in range(start, end+1):
        if i % n == 0:
            print(i, end=" ")

def divisible_by_n_range_list_comprehension(n, start, end):
    return [print(i, end=" ") for i in range(start, end+1) if i % n == 0]

def divisible_by_n_range_filter(n, start, end):
    return list(filter(lambda x: x % n == 0, range(start, end+1)))


start = int(input("Enter start range : "))
end = int(input("Enter end range : "))
n = int(input("Enter number to divide: "))

divisible_by_n_range(n, start, end)
print()
divisible_by_n_range_list_comprehension(n, start, end)
print()
print(*divisible_by_n_range_filter(n, start, end))