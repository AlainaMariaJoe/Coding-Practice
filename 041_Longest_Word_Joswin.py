def longest_word(s):
    longest = ''
    for i in s.split():
        if len(i) > len(longest):
            longest = i
    return longest

def longest_word_one_liner(s):
    return max(s.split(), key=len)

s = input("Enter the sentence : ")
print(longest_word(s))
print(longest_word_one_liner(s))
