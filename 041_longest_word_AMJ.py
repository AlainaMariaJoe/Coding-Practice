def longest_word(s):
    return max(s.split(), key = len)

inp_string = input("Enter a string: ")
print(f" Longest word in the string is: {longest_word(inp_string)}")