from typing import List

"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). 
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        # Iterate over each row, skipping bottom row
        for i in range(m - 1):
            new_row = [1] * n
            # Iterating over row from right to left, skipping rightmost row
            for j in range(n - 2, -1, -1):
                ...


        
        return "piss"


sol = Solution()
m = 3
n = 2
ans = sol.uniquePaths(m, n)
print(ans)


#

#

# Time complexity:
