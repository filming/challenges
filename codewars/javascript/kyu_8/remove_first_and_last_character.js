"""
Remove First and Last Character

https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/javascript
"""

function removeChar(str){
  let result = [];
  
  for (let i = 1; i < str.length-1; i++){
    result.push(str[i]);
  }
  
  return result.join('');
};
