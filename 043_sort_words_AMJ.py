def Sort_words(s):
    word = s.split()
    word.sort()
    return word
    
def Sort_words2(s):
    print( sorted(s.split(), key = str.upper) )

inp_string = input ("Enter a string: ")
Sort_words2(inp_string)