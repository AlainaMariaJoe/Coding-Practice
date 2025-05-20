def palindrome_str(s):
    return s.lower() == s[::-1].lower()

def palindrome_num(s):
    return int(s) == int(s[::-1])

def palindrome_for_loop(s):
    rev = ''
    s = s.lower()
    for i in s:
        rev = i + rev
    return s == rev


inp = input(" Enter a string: ")
if palindrome_for_loop(inp):
    print(inp, "is a palindrome")
else:
    print(inp, "is not a palindrome")
