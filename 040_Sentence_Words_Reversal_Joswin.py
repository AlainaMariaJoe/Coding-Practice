def words_reversal(s):
    return " ".join(s.split()[::-1])


string = input("Enter your string : ")
print(words_reversal(string))