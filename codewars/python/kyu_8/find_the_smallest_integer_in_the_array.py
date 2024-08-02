"""
Find the smallest integer in the array

https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python
"""

# Solution 1
def find_smallest_int(arr):
    return min(x for x in arr)

# Solution 2
def find_smallest_int(arr):
    smallest_int = arr[0]
    
    for i in range (1, len(arr)):
        if arr[i] < smallest_int:
            smallest_int = arr[i]
    
    return smallest_int
