def count_vowels(s):
    vowels = "aeiou"
    vowel_count = {}
    for char in s.lower():  
        if char in vowels:
            if char in vowel_count:
                vowel_count[char] += 1
            else:
                vowel_count[char] = 1
    return vowel_count

input_str = input("Enter a string: ")
print(count_vowels(input_str))
