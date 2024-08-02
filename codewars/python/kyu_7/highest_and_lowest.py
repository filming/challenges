"""
Highest and Lowest

https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python
"""

# Solution 1
def high_and_low(numbers):
    numbers_split = numbers.split(" ")
    
    for i in range (len(numbers_split)):
        numbers_split[i] = int(numbers_split[i])
    
    lowest, highest = numbers_split[0], numbers_split[0]
    
    for num in numbers_split:
        if num < lowest:
            lowest = num
        if num > highest:
            highest = num
            
    return f"{highest} {lowest}"
