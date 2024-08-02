"""
Calculate average

https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python
"""

# Solution 1
def find_average(numbers):
    return (sum(curr_num for curr_num in numbers) / len(numbers)) if numbers else 0

# Solution 2
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    
    sum_of_numbers = 0
    for curr_num in numbers:
        sum_of_numbers += curr_num
    
    average = sum_of_numbers / len(numbers)
    
    return average
