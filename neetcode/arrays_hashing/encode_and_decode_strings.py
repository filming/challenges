from typing import *

"""
271. Encode and Decode Strings

https://leetcode.com/problems/encode-and-decode-strings/description/
"""

"""
- 
"""


class Solution:
    # Solution 1: Time complexity of O(n), Space complexity of O(n)
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""

        encoded_str_builder = []
        delimiter = "⚽"

        for curr_str in strs:
            # Encode current string by shifting its ascii value by 5 units
            curr_str_builder = []

            for curr_char in curr_str:
                curr_str_builder.append(chr(ord(curr_char) + 5))

            # Store the newly encoded string
            encoded_str_builder.append("".join(curr_str_builder))
            encoded_str_builder.append(delimiter)

        return "".join(encoded_str_builder)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""

        decoded_strs = []
        delimiter = "⚽"

        curr_str_builder = []
        for curr_char in s:
            if curr_char == delimiter:
                # Store the decoded string that we have up until this point
                curr_str = "".join(curr_str_builder)
                decoded_strs.append(curr_str)
                curr_str_builder.clear()

            else:
                # Decode current character by shifting its ascii value by 5 units
                curr_str_builder.append(chr(ord(curr_char) - 5))

        return decoded_strs


def main():
    solution = Solution()

    strs = ["Hello", "World"]
    print(solution.decode(solution.encode(strs)))  # ["Hello","World"]

    strs = [""]
    print(solution.decode(solution.encode(strs)))  # [""]


if __name__ == "__main__":
    main()
