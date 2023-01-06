"""
An image is represented by an m x n integer grid image where image[i][j] 
represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a 
flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels 
connected 4-directionally to the starting pixel of the same color as the 
starting pixel, plus any pixels connected 4-directionally to those pixels 
(also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.
"""


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows = len(image)
        columns = len(image[0])
        curr_color = image[sr][sc]

        if curr_color == color:
            return image

        def depth_first_search(row, column):
            if image[row][column] == curr_color:
                image[row][column] = color

                if row + 1 < rows:
                    depth_first_search(row + 1, column)
                if row >= 1:
                    depth_first_search(row - 1, column)
                if column + 1 < columns:
                    depth_first_search(row, column + 1)
                if column >= 1:
                    depth_first_search(row, column - 1)

        depth_first_search(sr, sc)

        return image


sol = Solution()
image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
ans = sol.floodFill(image, sr, sc, color)
print(ans)

#

#

# Time complexity:
