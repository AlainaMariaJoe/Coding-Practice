def list_even_sum(l):
    return sum([i for i in l if i % 2 == 0])

# l = []
# n = int(input("How many elements in list : "))
# for i in range(n):
#     l.append(int(input(f"Enter element {i+1} : ")))

l = list(map(int, input("Enter List : ").split(",")))
# Input - Enter List : 1, 2, 3, 4

print(lst)
print(list_even_sum(l))
# Output - 6