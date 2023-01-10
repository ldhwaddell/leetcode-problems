from typing import List
from collections import deque

"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) 
and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent 
lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


class Solution:
    def numIslands_bfs(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # Get dimensions of grid
        rows, cols = len(grid), len(grid[0])
        # Set to contained visited coords
        visited = set()
        islands = 0

        def bfs(r, c):
            queue = deque()
            # Add the coords to visited
            visited.add((r, c))
            # add the coords to queue
            queue.append((r, c))

            # Keep expanding queue while it is not empty
            while queue:
                row, col = queue.popleft()
                # All possible next moves
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                # Check adjacent positions
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # Check that new position is valid
                    if (
                        r in range(rows)
                        and c in range(cols)
                        and grid[r][c] == "1"
                        and (r, c) not in visited
                    ):
                        # If valid, add coord to queue and visited
                        visited.add((r, c))
                        queue.append((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    # Run breadth first search on this coord
                    bfs(r, c)
                    islands += 1

        return islands

    def numIslands_dfs(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # Get dimensions of grid
        rows, cols = len(grid), len(grid[0])
        # Set to contained visited coords
        visited = set()
        islands = 0

        def dfs(r, c):
            # Add coord to visited
            visited.add((r, c))

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            # Check adjacent positions
            for dr, dc in directions:
                next_r, next_c = r + dr, c + dc
                # Check that new position is valid
                if (
                    next_r in range(rows)
                    and next_c in range(cols)
                    and grid[next_r][next_c] == "1"
                    and (next_r, next_c) not in visited
                ):
                    # If valid, add coord to queue and visited
                    visited.add((next_r, next_c))
                    dfs(next_r, next_c)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    # Run depth first search on this coord
                    dfs(r, c)
                    islands += 1

        return islands


sol = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
ans_bfs = sol.numIslands_bfs(grid)
ans_dfs = sol.numIslands_dfs(grid)

print(f"BFS: {ans_bfs}, DFS: {ans_dfs}")


#

#

# Time complexity:
