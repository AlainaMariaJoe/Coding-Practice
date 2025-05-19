def sum_of_natural_number_recursion(n):
    if n <= 1:
        return n
    return n + sum_of_natural_number_recursion(n-1)

n = int(input("Enter the limit : "))
print(sum_of_natural_number_recursion(n))