from typing import *

"""
347. Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements/
"""

"""
- 
"""


class Solution:
    # Solution 1: Time complexity of O(n log n), Space complexity of O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []

        # Create an int occurrence dict based on nums
        nums_int_occurrences = {}

        for curr_num in nums:
            if curr_num in nums_int_occurrences:
                nums_int_occurrences[curr_num] += 1
            else:
                nums_int_occurrences[curr_num] = 1

        # Sort the int occurrence dict by value
        nums_int_occurrences_tuples = sorted(
            nums_int_occurrences.items(), key=lambda x: x[1], reverse=True
        )

        # Store the first K ints based on our list of tuples
        for i in range(k):
            result.append(nums_int_occurrences_tuples[i][0])

        return result


def main():
    solution = Solution()

    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(solution.topKFrequent(nums, k))  # [1,2]

    nums = [1]
    k = 1
    print(solution.topKFrequent(nums, k))  # [1]

    nums = [1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 6, 7, 7, 7, 8, 9, 9]
    k = 5
    print(solution.topKFrequent(nums, k))  # [5, 1, 7, 2, 6]


if __name__ == "__main__":
    main()
