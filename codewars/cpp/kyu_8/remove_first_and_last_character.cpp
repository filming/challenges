"""
Remove First and Last Character

https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/cpp
"""

#include <string>

using namespace std; 

string sliceString (string str )
{
  string result = "";
  for (int i = 1; i < str.length()-1; i++){
    result += str[i];
  }
  
  return result; 
}
