def multiplication_table(n):
    for i in range(1, 11):
        print(f"{i} x {n} = {i*n}")

n = int(input("Enter the number : "))
multiplication_table(n)