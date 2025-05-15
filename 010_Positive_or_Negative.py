def positive_or_negative(n):
    return "Zero" if n == 0 else ("Positive" if n > 0 else "Negative")

n = float(input("Enter the number : "))
print(positive_or_negative(n))