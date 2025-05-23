def sort_char_str(s):
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

def sort_char_list(s):
    Upper_list = []
    lower_list = []
    space_list = []
    others_list = []
    for i in s:
        if i.isupper():
            Upper_list.append(i)
        elif i.islower():
            lower_list.append(i)
        elif i.isspace():
            space_list.append(i)
        else:
            others_list.append(i)
    return ''.join(Upper_list + lower_list + space_list + others_list)

inp_str = input("Enter a string: ")
print(f"'{sort_char_str(inp_str)}'")
print(f"'{sort_char_list(inp_str)}'")

