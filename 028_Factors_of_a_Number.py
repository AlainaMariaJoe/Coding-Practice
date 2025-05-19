def factors_of_a_number_list_comprehension(n):
    return list([i for i in range(1, n+1) if n % i == 0])

def factors_of_a_number_iterative(n):
    lst = []
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
    return lst

n = int(input("Enter the number : "))
print(factors_of_a_number_list_comprehension(n))
print(factors_of_a_number_iterative(n))