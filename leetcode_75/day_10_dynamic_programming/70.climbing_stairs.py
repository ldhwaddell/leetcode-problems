"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # If there are 0, 1, or 2 stairs, there are only 0, 1, or 2 ways to climb them
        if n < 3:
            return n

        one_step_below = 2
        two_steps_below = 1

        for _ in range(3, n + 1):
            two_steps_below, one_step_below = one_step_below, one_step_below + two_steps_below
        return one_step_below


sol = Solution()
n = 5
ans = sol.climbStairs(n)
print(ans)

#

#

# Time complexity:
