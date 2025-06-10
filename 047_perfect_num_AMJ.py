def perfect_num (n):
    sum = 0
    for i in range(1, n):
        if n % i == 0 :
            sum += i
    return sum
inp_num = int(input("Enter a number: "))
print("The number is perfect.") if perfect_num(inp_num ) == inp_num else print("The number is not perfect.")