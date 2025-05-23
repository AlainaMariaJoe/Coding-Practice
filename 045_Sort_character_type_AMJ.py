def sort_char(s):
    Upper_str = ''
    lower_str = ''
    space_str = ''
    others_str = ''
    for i in s:
        if i.isupper():
            Upper_str += i
        elif i.islower():
            lower_str += i
        elif i.isspace():
            space_str += i
        else:
            others_str += i
    return Upper_str + lower_str + space_str + others_str

inp_str = input("Enter a string: ")
print(f"'{sort_char(inp_str)}'")

