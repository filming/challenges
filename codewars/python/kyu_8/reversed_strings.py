"""
Reversed Strings

https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/python
"""

def solution(string):
    result = ['' for _ in range (len(string))]
    
    for i in range (len(result)):
        result[i] = string[len(string)-(i+1)]
    
    return "".join(result)
