"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""
from typing import List


class Solution:
    """
    Algorithm:
        1. Create a dictionary to store the rows, columns and squares
        2. For each row in the board
            a. If the row is not in the rows dictionary, add it
            b. For each column in the board
                i. If the column is not in the columns dictionary, add it
                ii. Set the current value to the board at the row and column
                iii. If the current value is a period, continue
                iv. If the current value is in the rows dictionary at the row, or the columns dictionary at the column, or the squares dictionary at the row // 3 and column // 3, return False
                v. Add the current value to the rows dictionary at the row, the columns dictionary at the column, and the squares dictionary at the row // 3 and column // 3
        3. Return True
    Time Complexity: O(n^2) -> O(9)
    Space Complexity: O(n^2) -> O(9)
    """

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}
        for x in range(3):
            for y in range(3):
                squares[(x, y)] = set()

        for row in range(9):
            if row not in rows:
                rows[row] = set()
            for col in range(9):
                if col not in cols:
                    cols[col] = set()
                current_value = board[row][col]
                if current_value == ".":
                    continue
                if (
                    current_value in rows[row]
                    or current_value in cols[col]
                    or current_value in squares[(row // 3, col // 3)]
                ):
                    return False
                rows[row].add(current_value)
                cols[col].add(current_value)
                squares[(row // 3, col // 3)].add(current_value)
        return True
