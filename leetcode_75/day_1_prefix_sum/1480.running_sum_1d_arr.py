"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""


class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        run_sum = []
        for i in range(len(nums)):
            run_sum.append(sum(nums[: i+1]))
        return run_sum


sol = Solution()
nums = [3, 1, 2, 10, 1]
ans = sol.runningSum(nums)
print(ans)

#

#

# Time complexity:
