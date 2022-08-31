"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # While left pointer has not crossed right pointer
        while left <= right:
            middle = (left + right) // 2

            if target == nums[middle]:
                return middle

            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

        return left


sol = Solution()
nums = [1, 3, 6]
target = 2

ans = sol.searchInsert(nums, target)
print(ans)

# Runtime: 97 ms, faster than 19.15% of Python3 online submissions for Search Insert Position.

# Memory Usage: 14.7 MB, less than 82.73% of Python3 online submissions for Search Insert Position.

# Time complexity: O(log n)
