from functools import reduce

def sum_of_natural_formula(n):
    return int((n * (n + 1)) / 2)

def sum_of_natural_iterative(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

def sum_of_natural_range(n):
    return sum(range(1, n+1))

def sum_of_natural_list_comprehension(n):
    return sum([i for i in range(1, n+1)])

def sum_of_natural_recursion(n):
    if n == 1:
        return 1
    return n + sum_of_natural_recursion(n - 1)

def sum_of_natural_reduce(n):
    return reduce(lambda x, y : x + y, range(1, n+1))

n = int(input("Enter the limit : "))
print(sum_of_natural_formula(n))
print(sum_of_natural_iterative(n))
print(sum_of_natural_range(n))
print(sum_of_natural_list_comprehension(n))
print(sum_of_natural_recursion(n))
print(sum_of_natural_reduce(n))