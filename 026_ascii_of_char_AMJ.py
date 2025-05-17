def ascii(c):
    return ord(c)

val = input("Enter a character: " )
print(ascii(val) if len(val) == 1 else "Invalid input, please enter a single character")


