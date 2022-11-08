"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] != 10:
                return digits
            digits[i] = 0
        digits.insert(0, 1)
        return digits


sol = Solution()
digits_1 = [4, 3, 2, 1]
digits_2 = [9, 9, 9]
ans = sol.plusOne(digits_2)
print(ans)

# Runtime: 31 ms, faster than 96.61% of Python3 online submissions for Plus One.

# Memory Usage: 13.8 MB, less than 96.36% of Python3 online submissions for Plus One.

# Time complexity:
