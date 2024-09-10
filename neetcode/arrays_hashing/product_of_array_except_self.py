from typing import *

"""
238. Product of Array Except Self

https://leetcode.com/problems/product-of-array-except-self/description/
"""

"""
- 
"""


class Solution:
    # Solution 1: Time complexity of O(n), Space complexity of O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_side = [1 for i in range(len(nums))]
        right_side = [1 for i in range(len(nums))]
        product = []

        # Calculate the left side products
        for i in range(1, len(nums)):
            left_side[i] = nums[i - 1] * left_side[i - 1]

        # Calculate the right side products
        for i in range(len(nums) - 2, -1, -1):
            right_side[i] = nums[i + 1] * right_side[i + 1]

        # Calculate product based on left & right side products
        for i in range(len(left_side)):
            product.append(left_side[i] * right_side[i])

        return product

    # Solution 2: Time complexity of O(n), Space complexity of O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1 for i in range(len(nums))]

        # Calculate the products going from left to right
        for i in range(1, len(nums)):
            product[i] = nums[i - 1] * product[i - 1]

        # Calculate the products going from right to left
        curr_product_right = 1

        for i in range(len(nums) - 2, -1, -1):
            curr_product_right *= nums[i + 1]

            product[i] *= curr_product_right

        return product


def main():
    solution = Solution()

    nums = [1, 2, 3, 4]
    print(solution.productExceptSelf(nums))  # [24,12,8,6]

    nums = [-1, 1, 0, -3, 3]
    print(solution.productExceptSelf(nums))  # [0,0,9,0,0]


if __name__ == "__main__":
    main()
