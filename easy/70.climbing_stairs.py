"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # fibonacci sequence
        # first two values in sequence get set to 1
        a, b = 1, 1

        for _ in range(n):
            # math for fibonacci sequence
            temp_a = a
            a = b
            b = b + temp_a

            # could also be done like this
            # a, b = b, a + b

        return a


sol = Solution()
n = 2
ans = sol.climbStairs(n)
print(ans)

# Runtime: 55 ms, faster than 26.27% of Python3 online submissions for Climbing Stairs.

# Memory Usage: 13.9 MB, less than 11.83% of Python3 online submissions for Climbing Stairs.

# Time complexity:
