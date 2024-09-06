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

    # Solution 2: Time complexity of O(n*k), Space complexity of O(n*k)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Try and sort using bucket sorting improve TC (26 lists, 1 for each char of the alphabet)
        groups = {}

        for curr_str in strs:
            # Create a char occurrence list of the current string using buckets
            curr_str_char_occurrences = [0 for _ in range(26)]

            for curr_char in curr_str:
                curr_str_char_occurrences[97 - ord(curr_char)] += 1

            # Convert char occurrence into a hashable obj like a tuple
            curr_str_char_occurrences_tuple = tuple(curr_str_char_occurrences)

            # Update group with current string
            if curr_str_char_occurrences_tuple in groups:
                groups[curr_str_char_occurrences_tuple].append(curr_str)
            else:
                groups[curr_str_char_occurrences_tuple] = [curr_str]

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
