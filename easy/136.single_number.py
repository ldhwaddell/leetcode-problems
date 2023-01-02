"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        lookup = {}
        for i in nums:
            if i in lookup:
                lookup[i] += 1

            if i not in lookup:
                lookup[i] = 1

        for key, val in lookup.items():
            if val == 1:
                return key

    def singleNumber2(self, nums: list[int]) -> int:
        # ^ is the python bitwise poerator for XOR.
        # Any number XOR itself is 0. 
        res = 0
        for num in nums:
            res ^= num
        return res


    



sol = Solution()
nums = [4, 1, 2, 1, 2]
ans = sol.singleNumber(nums)
print(ans)

#

#

# Time complexity:
