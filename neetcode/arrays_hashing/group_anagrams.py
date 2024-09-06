from typing import *

"""
49. Group Anagrams

https://leetcode.com/problems/group-anagrams/description/
"""

"""
- 
"""


class Solution:
    # Solution 1: Time complexity of O(n log n), Space complexity of O(n)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for curr_str in strs:

            # Create a char occurrence dict of the current string
            curr_str_char_occurrences = {}

            for curr_char in curr_str:
                if curr_char in curr_str_char_occurrences:
                    curr_str_char_occurrences[curr_char] += 1
                else:
                    curr_str_char_occurrences[curr_char] = 1

            # Check and see if char_occurrences match any stored group
            curr_str_char_occurrences_sorted = tuple(
                sorted(curr_str_char_occurrences.items())
            )

            if curr_str_char_occurrences_sorted in groups:
                groups[curr_str_char_occurrences_sorted].append(curr_str)
            else:
                groups[curr_str_char_occurrences_sorted] = [curr_str]

        return groups.values()


def main():
    solution = Solution()

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs))  # ["bat"],["nat","tan"],["ate","eat","tea"]]

    strs = [""]
    print(solution.groupAnagrams(strs))  # [[""]]

    strs = ["a"]
    print(solution.groupAnagrams(strs))  # [["a"]]


if __name__ == "__main__":
    main()
