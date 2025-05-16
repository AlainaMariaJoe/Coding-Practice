for i in range(int(input(" Enter the number "))) :
    print(f"{i}: {(lambda x: 2 ** x)(i)}")

def Power_of_2():
    list1 = [0,3,4,5,8]
    power = list(map(lambda x : 2 ** x , list1))
    print(power)

def Power_of_two():
    l = []
    num = int(input("Enter how many numbers want:"))
    for i in range(num):
        l.append(int(input(f"Enter number {i}: ")))
    print(list(map(lambda x: 2 ** x, l)))

Power_of_2()
Power_of_two()