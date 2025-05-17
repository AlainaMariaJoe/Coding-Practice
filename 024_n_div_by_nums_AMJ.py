def Divisible_by_num_range(n, start, end):
    for i in range(start, end):
        if i % n == 0:
            print(i, end =' ')
    print()

def Divisible_by_num_list(l, n):
    for i in l:
        if i % n == 0:
            print(i, end =' ')
    print()

res = list(filter(lambda x: x % 2 == 0, range(11)))


l = [1, 2, 3, 4, 5]
start, end, = 1, 10
n = int (input("Enter a number: "))
Divisible_by_num_range (n, start, end)
Divisible_by_num_list(l, n)
print(res)
