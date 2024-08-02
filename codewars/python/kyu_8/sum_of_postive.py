"""
Sum of positive

https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
"""

def positive_sum(arr):
    sum_of_positives = 0
    
    for curr_num in arr:
        if curr_num > 0:
            sum_of_positives += curr_num
    
    return sum_of_positives
