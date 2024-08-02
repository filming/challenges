"""
Array.diff

https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
"""

# Solution 1
def array_diff(a, b):
    result = []
    
    b_set = set(b)
    
    for curr_val in a:
        if curr_val not in b_set:
            result.append(curr_val)
    
    return result
