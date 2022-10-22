"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""

from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Algorithm:
            1. Use a breadth-first search to traverse the matrix.
            2. Create a queue to store the coordinates of the 0s.
            3. Create a distance matrix to store the distance of the nearest 0 for each cell.
            4. If the current cell is a 0, set the distance to 0. else set it to infinity.
            5. If the current cell is a 1, set the distance to the minimum distance of the current cell's neighbors plus 1.
            6. Return the distances.
        Pattern: Breadth-First Search
        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        # Get the number of rows and columns
        rows = len(mat)
        columns = len(mat[0])
        # Initialize the distances
        distances = [[0] * columns for _ in range(rows)]
        # Initialize the queue
        queue = []
        # For each row in the matrix
        for row in range(rows):
            # For each column in the matrix
            for column in range(columns):
                # If the current cell is a 0
                if mat[row][column] == 0:
                    # Set the distance to 0
                    distances[row][column] = 0
                    # Add the current cell to the queue
                    queue.append((row, column))
                # If the current cell is a 1
                else:
                    # Set the distance to infinity
                    distances[row][column] = float("inf")
        # Define a breadth-first search function
        def bfs():
            # While the queue is not empty
            while queue:
                # Get the current cell
                row, column = queue.pop(0)
                # Traverse the current cell's neighbors
                for neighbor in [
                    (row + 1, column),
                    (row - 1, column),
                    (row, column + 1),
                    (row, column - 1),
                ]:
                    # Get the neighbor's row and column
                    neighbor_row, neighbor_column = neighbor
                    # If the neighbor is within the bounds of the matrix
                    if 0 <= neighbor_row < rows and 0 <= neighbor_column < columns:
                        # Get the current distance
                        current_distance = distances[neighbor_row][neighbor_column]
                        # Get the new distance
                        new_distance = distances[row][column] + 1
                        # If the new distance is less than the current distance

                        if new_distance < current_distance:
                            # Set the new distance
                            distances[neighbor_row][neighbor_column] = new_distance
                            # Add the neighbor to the queue
                            queue.append((neighbor_row, neighbor_column))

        # Perform a breadth-first search
        bfs()
        # Return the distances
        return distances


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rc = len(matrix)
        cc = len(matrix[0])
        # 0 -> n
        for row in range(rc):
            for col in range(cc):
                if matrix[row][col] != 0:
                    matrix[row][col] = float("inf")

                    if row > 0 and matrix[row - 1][col] + 1 < matrix[row][col]:
                        matrix[row][col] = matrix[row - 1][col] + 1

                    if col > 0 and matrix[row][col - 1] + 1 < matrix[row][col]:
                        matrix[row][col] = matrix[row][col - 1] + 1

        for row in range(rc - 1, -1, -1):
            for col in range(cc - 1, -1, -1):
                if matrix[row][col] != 0:

                    if row < rc - 1 and matrix[row + 1][col] + 1 < matrix[row][col]:
                        matrix[row][col] = matrix[row + 1][col] + 1

                    if col < cc - 1 and matrix[row][col + 1] + 1 < matrix[row][col]:
                        matrix[row][col] = matrix[row][col + 1] + 1

        return matrix
