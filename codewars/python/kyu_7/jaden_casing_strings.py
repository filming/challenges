"""
Jaden Casing Strings

https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python
"""

# Solution 1
def to_jaden_case(string):
    result = []
    
    string_index, max_string_index = 0, len(string)-1
    
    while string_index <= max_string_index:
        
        if string_index == 0 or string[string_index-1] == ' ':
            result.append(string[string_index].upper())
        
        else:
            result.append(string[string_index].lower())
        
        string_index += 1
    
    return "".join(result)
