"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        #for i in range(len(nums)):
        #    if sum(nums[:i]) == sum(nums[i + 1 :]):
        #        return i
        #return -1

        left_side = 0
        right_side = sum(nums)
        for i in range(len(nums)):
            right_side-=nums[i]
            if left_side == right_side:
                return i
            left_side+=nums[i]

        return -1


        




sol = Solution()
nums = [1,7,3,6,5,6]
ans = sol.pivotIndex(nums)
print(ans)

#

#

# Time complexity:
