def Multiplication_tab(n):
    for i in range(1, n+1):
        print(f"\nMultiplication table of {i}\n")
        for j in range(1, 11):
            print(f"{i} * {j} = {i*j}", end='\t')
            print()

num = int(input("Enter how many tables to display: "))
Multiplication_tab(num)