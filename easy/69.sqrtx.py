"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2

            if x == mid * mid:
                return mid

            if x > mid * mid:
                left = mid + 1
            else:
                right = mid - 1

        # When there is no perfect square, hi is the the value on the left
        # of where it would have been (rounding down). If we were rounding up,
        # we would return lo
        return right


sol = Solution()
x = 10
ans = sol.mySqrt(x)
print(ans)

#

#

# Time complexity:
