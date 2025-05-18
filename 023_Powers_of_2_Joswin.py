def powers_of_two(n):
    return list(map(lambda x: 2 ** x, range(n)))

terms = int(input("Enter number of terms : "))
print(powers_of_two(terms))