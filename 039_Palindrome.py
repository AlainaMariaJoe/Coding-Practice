def palindrome_or_not(s):
    return s.lower() == s.lower()[::-1]

data = "apple"
print(palindrome_or_not(data))

data = "malayalam"
print(palindrome_or_not(data))