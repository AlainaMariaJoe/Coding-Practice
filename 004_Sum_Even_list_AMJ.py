def sum_even_list(list1):
    sum = 0
    for i in list1:
        if i % 2 == 0:
            sum += i
    return sum

inp = [1,4,6,8,12,15,14]
print(sum_even_list(inp))