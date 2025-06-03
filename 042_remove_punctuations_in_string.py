import string
def remove_punctuation_loop(s):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    new_str = ''
    for i in s :
        if i not in punctuations: 
            new_str += i
    return new_str

def remove_punctuation_list_comprehension(s):
    return ''.join([i for i in s if i not in string.punctuation])

inp_str = input("Enter a String: ")
print(f"\nString without punctuation: {remove_punctuation_loop(inp_str)}")
#print(f"String without punctuation (list comprehension): {remove_punctuation_list_comprehension(inp_str)}")