"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.


Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n

Answer: Use a depth-first search to traverse the image. If the current pixel is the same color as the starting pixel, change the current pixel to the new color. Return the image.
"""

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        """
        Algorithm:
            1. Use a depth-first search to traverse the image.
            2. If the current pixel is the same color as the starting pixel, change the current pixel to the new color.
            3. Return the image.
        Pattern: Depth-First Search
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        # Get the starting pixel's color
        start_color = image[sr][sc]

        # If the starting pixel's color is the same as the new color
        if start_color == color:
            # Return the image
            return image

        # Get the number of rows and columns
        rows = len(image)
        columns = len(image[0])

        # Define a depth-first search function
        def dfs(row, column):
            # If the current pixel is within the bounds of the image
            if 0 <= row < rows and 0 <= column < columns:
                # If the current pixel is the same color as the starting pixel
                if image[row][column] == start_color:
                    # Change the current pixel to the new color
                    image[row][column] = color
                    # Traverse the current pixel's neighbors
                    dfs(row + 1, column)
                    dfs(row - 1, column)
                    dfs(row, column + 1)
                    dfs(row, column - 1)

        # Perform a depth-first search on the starting pixel
        dfs(sr, sc)

        # Return the image
        return image
