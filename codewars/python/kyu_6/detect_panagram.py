"""
Detect Panagram

https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
"""

# Solution 1
def is_pangram(st):
    seen_chars = {}
    
    for curr_char in st:
        if curr_char.isalpha():
            if curr_char.lower() in seen_chars:
                seen_chars[curr_char.lower()] += 1
            else:
                seen_chars[curr_char.lower()] = 1
    
    if len(seen_chars) == 26:
        return True
    
    else:
        return False
