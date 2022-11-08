"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""
class Solution:
    def generate(self, num_rows: int) -> list[list[int]]:
        # If empty, return empty list
        if not num_rows:
            return []
        
        output = []
        # Initial row to add will always be [1]
        next_row = [1]

        for i in range(num_rows):
            # Append next_row to output
            output.append(next_row)
            # manipulate the next row to update it
            next_row = [1] + [next_row[j] + next_row[j+1] for j in range(len(next_row) - 1)] + [1]
        return output





sol = Solution()
num_rows = 7
ans = sol.generate(num_rows)
print(ans)

# 

# 

# Time complexity:
