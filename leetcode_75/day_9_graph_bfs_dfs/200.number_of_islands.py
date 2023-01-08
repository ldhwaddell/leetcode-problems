"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) 
and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent 
lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        visited = [[False for _ in range(columns)] for _ in range(rows)]

        count = 0

        for i in range(rows):
            for j in range(columns):
                ...


        return visited


sol = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
ans = sol.numIslands(grid)
print(ans)

#

#

# Time complexity:
