"""
Create Phone Number

https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
"""

def create_phone_number(n):
    n_index = 0
    
    result = ['(', '', '', '', ')', ' ', '', '', '', '-', '', '', '', '']
    result_index = 0
    
    while n_index <= (len(n)-1):

        if not result[result_index]:
            result[result_index] = str(n[n_index])
            n_index += 1
        
        result_index += 1
    
    return "".join(result)
