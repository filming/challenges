from typing import *

"""
217. Contains Duplicate

https://leetcode.com/problems/contains-duplicate/description/
"""

"""
- 
"""


class Solution:
    # Solution 1: Time complexity of O(n), Space complexity of O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        present_nums = set()

        for num in nums:
            if num in present_nums:
                return True

            present_nums.add(num)

        return False


def main():
    solution = Solution()

    nums = [1, 2, 3, 1]
    print(solution.containsDuplicate(nums))  # true

    nums = [1, 2, 3, 4]
    print(solution.containsDuplicate(nums))  # false

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(solution.containsDuplicate(nums))  # true


if __name__ == "__main__":
    main()
