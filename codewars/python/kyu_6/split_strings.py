"""
Split Strings

https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python
"""

# Solution 1
def solution(s):
    result = []
    
    temp = ['', '']
    for i in range (len(s)):
        
        if not temp[0]:
            if i == len(s)-1:
                temp[1] = '_'
                
            temp[0] = s[i]
        
        elif not temp[1]:
            temp[1] = s[i]
        
        else:
            result.append("".join(temp))
            temp[0], temp[1] = s[i], '_' if i == len(s)-1 else ''
    
        if i == len(s)-1:
            result.append("".join(temp))
    
    return result
