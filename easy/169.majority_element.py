"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        for num in nums:

            # if the occurence count reaches 0, the candidate becomes the current number
            if count == 0:
                candidate = num
            # if the curret number is the candidate, increase the count of it occuring
            if num == candidate:
                count += 1
            # Otherwise, decrese the occurence count
            else:
                count -= 1
        return candidate


sol = Solution()
nums = [2, 2, 1, 1, 1, 2, 2]
ans = sol.majorityElement(nums)
print(ans)

#

#

# Time complexity:
