"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Algorithm:
            1. Check if the root is None
            2. Check if the left and right subtrees are balanced
            3. Check if the height of the left and right subtrees differ by no more than 1
            4. Return the result
        Pattern: Recursion
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if root is None:
            return True
        return (
            self.isBalanced(root.left)
            and self.isBalanced(root.right)
            and abs(self.height(root.left) - self.height(root.right)) <= 1
        )

    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Algorithm:
            1. Check if the height of the tree is not -1
            2. Return the result
        Pattern: Recursion
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return self.height(root) != -1

    def height(self, root):
        if root is None:
            return 0
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if (
            left_height == -1
            or right_height == -1
            or abs(left_height - right_height) > 1
        ):
            return -1
        return 1 + max(left_height, right_height)
