"""
Convert a Number to a String

https://www.codewars.com/kata/5265326f5fda8eb1160004c8/train/python
"""

import math

def number_to_string(num):
    # creating a simple hashmap to convert 0-9 ints into their str equivalents
    int_to_char = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
    
    # convert num to positive if it is negative
    # create a flag to note this later in the program
    is_negative = False
    if num < 0:
        is_negative = True
        num *= -1
        
    # find out how many digits are in num
    digits_in_num = int(math.log(abs(num), 10)) + 1
    
    # make a fixed-length char list that will be the length as the total # of digits in num
    # increment digits_in_num by 1 if the number is negative to account for the negative sign in our char list
    if is_negative:
        digits_in_num += 1
    
    # create our fixed-sized result list
    result = ["" for _ in range (digits_in_num)]
    
    if is_negative:
        result[0] = '-'
    
    # use modulous division to get the last digit of num and add it to our char list
    num_index = digits_in_num - 1
    

    while num > 0:
        last_digit_of_num = num % 10
        result[num_index] = int_to_char[last_digit_of_num] 
        
        num //= 10
        num_index -= 1
    
    return "".join(result)
