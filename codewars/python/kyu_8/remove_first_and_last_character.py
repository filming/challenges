"""
Remove First and Last Character

https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python
"""

def remove_char(s):
    result = ["" for _ in range (len(s) - 2)]
    
    for i in range (1, len(s)-1):
        result[i-1] = s[i]
    
    return "".join(result)
