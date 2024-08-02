"""
Square(n) Sum

https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
"""

def square_sum(numbers):
    sum_of_squares = 0
    
    for curr_num in numbers:
        sum_of_squares += curr_num ** 2
    
    return sum_of_squares

def square_sum(numbers):
    return sum(curr_num ** 2 for curr_num in numbers)
