def sort_and_rearrange_string(s):
    upper = ''
    lower = ''
    space = ''
    other = ''
    for i in sorted(s):
        if i.isupper():
            upper += i
        elif i.islower():
            lower += i
        elif i == ' ':
            space += i
        else:
            other += i
    return upper + lower + other + space

string = input("Enter the string : ")
print(sort_and_rearrange_string(string))