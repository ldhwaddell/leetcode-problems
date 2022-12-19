"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]


        return [1] + [] + [1]

        
        


sol = Solution()
rowIndex = 7
ans = sol.getRow(rowIndex)
print(ans)

#

#

# Time complexity:
