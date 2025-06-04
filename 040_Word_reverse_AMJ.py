def Rev_word(s):
    return ' '.join(s.split()[::-1])

inp = input("Enter a string to reverse: ")
print(f"Before reverse: {inp}")
print(f"After reverse: {Rev_word(inp)}")