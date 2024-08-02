"""
Count of positives / sum of negatives

https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
"""

def count_positives_sum_negatives(arr):
    result = [0, 0]
    
    for curr_num in arr:
        if curr_num > 0:
            result[0] += 1
        else:
            result[1] += curr_num
    
    
    return result if arr else []
