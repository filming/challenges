from typing import *

"""
242. Valid Anagram

https://leetcode.com/problems/valid-anagram/description/
"""

"""
- 
"""


class Solution:
    # Solution 1: Time complexity of O(n), Space complexity of O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        char_occurrences = {}

        for char in s:
            if char in char_occurrences:
                char_occurrences[char] += 1
            else:
                char_occurrences[char] = 1

        for char in t:
            if char not in char_occurrences:
                return False

            else:
                char_occurrences[char] -= 1

        for val in char_occurrences.values():
            if val:
                return False

        return True


def main():
    solution = Solution()

    s = "anagram"
    t = "nagaram"
    print(solution.isAnagram(s, t))  # true

    s = "rat"
    t = "car"
    print(solution.isAnagram(s, t))  # false


if __name__ == "__main__":
    main()
