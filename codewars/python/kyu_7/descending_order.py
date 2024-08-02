"""
Descending Order

https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python
"""

# Solution 1
import math

def descending_order(num):
    # handle question constraints
    if num <= 0:
        return num
    
    # get the total # of digits in num
    digits_in_num = int(math.log(num, 10)) + 1
    
    # create buckets so we can sort the digits of num efficiently
    buckets = [[] for _ in range (10)]
    
    # get the last digit of num and add it to the appropiate bucket
    while num > 0:
        last_digit_of_num = num % 10
        buckets[last_digit_of_num].append(last_digit_of_num)
        num //= 10
    
    # use exponential math to create the biggest number using the digits in the buckets
    biggest_num = 0
    
    for i in range (len(buckets)-1, -1, -1):
        for j in range (len(buckets[i])):
            biggest_num += buckets[i][j] * (10 ** (digits_in_num-1))
            digits_in_num -= 1
            
    return biggest_num

# Solution 2
import math

def descending_order(num):
    # handle question constraints
    if num <= 0:
        return num
    
    # get the total # of digits in num using log (inverse of exponents)
    digits_in_num = int(math.log(num, 10)) + 1
    
    # create an int occurrence list so we can sort the digits of num efficiently
    int_occurrences = [0 for _ in range (10)]
    
    while num > 0:
        last_digit_of_num = num % 10
        int_occurrences[last_digit_of_num] += 1
        num //= 10
    
    # use exponential math to create the biggest number based on int_occurrences
    biggest_num = 0
    
    for i in range (len(int_occurrences)-1, -1, -1):
        for j in range (int_occurrences[i]):
            biggest_num += i * (10 ** (digits_in_num-1))
            digits_in_num -= 1
        
    return biggest_num
