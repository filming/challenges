"""
String repeat

https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/python
"""
 
def repeat_str(repeat, string):
    result = []
    
    for _ in range (repeat):
        result.append(string)
    
    return "".join(result)
