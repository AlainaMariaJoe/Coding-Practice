import random

def generate_random_number(start, end):
    return random.randint(start, end)

start = int(input("Enter the start range : "))
end = int(input("Enter the end range : "))
print(generate_random_number(start, end))