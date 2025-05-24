def vowel_count(s):
    counter = 0
    for i in s:
        if i.lower() in 'aeiou':
            counter += 1
    return counter

def vowel_count_dictionary(s):
    result = {}
    for i in s.lower():
        if i in 'aeiou':
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
    return result

s = input("Enter the string : ")
print(vowel_count(s))
print(vowel_count_dictionary(s))