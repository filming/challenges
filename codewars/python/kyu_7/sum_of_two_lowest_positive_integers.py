"""
Sum of two lowest positive integers

https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
"""

def sum_two_smallest_numbers(numbers):
    if numbers[0] > numbers[1]:
        first_lowest = numbers[1]
        second_lowest = numbers[0]
    else:
        first_lowest = numbers[0]
        second_lowest = numbers[1]
    
    for i in range (2, len(numbers)):
        if numbers[i] <= first_lowest:
            second_lowest = first_lowest
            first_lowest = numbers[i]
        elif numbers[i] <= second_lowest:
            second_lowest = numbers[i]
    
    return first_lowest + second_lowest
