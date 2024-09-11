from typing import *

"""
36. Valid Sudoku

https://leetcode.com/problems/valid-sudoku/description/
"""

"""
- 
"""


class Solution:
    # Solution 1: Time complexity of O(n*m), Space complexity of O(m)
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check if each row is valid
        seen_numbers = set()
        for row in board:
            for col in row:
                if col != ".":
                    if col in seen_numbers:
                        return False

                    seen_numbers.add(col)

            seen_numbers.clear()

        # Check if each column is valid
        seen_numbers.clear()
        for column_index in range(len(board[0])):

            for row in board:
                if row[column_index] != ".":
                    if row[column_index] in seen_numbers:
                        return False

                    seen_numbers.add(row[column_index])

            seen_numbers.clear()

        # Check if each 3x3 sub-box is valid
        seen_numbers.clear()

        left, right = 0, 3

        for _ in range(3):
            for row_i in range(len(board)):

                for col_i in range(left, right):

                    if board[row_i][col_i] != ".":
                        if board[row_i][col_i] in seen_numbers:
                            return False

                        seen_numbers.add(board[row_i][col_i])

                if row_i in (2, 5, 8):
                    seen_numbers.clear()

            left += 3
            right += 3
            seen_numbers.clear()

        return True


def main():
    solution = Solution()

    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(solution.isValidSudoku(board))  # true

    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(solution.isValidSudoku(board))  # false


if __name__ == "__main__":
    main()
