"""
Convert string to camel case

https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
"""

def to_camel_case(text):
    result = []
    
    index = 0
    while index <= len(text)-1:
        if text[index] in ('-', '_'):
            if index+1 <= len(text)-1:
                result.append(text[index+1].upper())
                index += 2
        else:
            result.append(text[index])
            index += 1
    
    return "".join(result)
