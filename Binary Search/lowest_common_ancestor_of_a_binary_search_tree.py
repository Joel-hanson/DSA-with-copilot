"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2

Constraints:

- The number of nodes in the tree is in the range [2, 105].
- -109 <= Node.val <= 109
- All Node.val are unique.
- p != q
- p and q will exist in the BST.

Answer: Use binary search to find the lowest common ancestor of a binary search tree. If the current node is greater than both p and q, the lowest common ancestor is in the left subtree. If the current node is less than both p and q, the lowest common ancestor is in the right subtree. Otherwise, the current node is the lowest common ancestor.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        """
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        # While the root is not None
        while root:
            # If the root is greater than both p and q
            if root.val > p.val and root.val > q.val:
                # Set the root to the left child
                root = root.left

            # If the root is less than both p and q
            elif root.val < p.val and root.val < q.val:
                # Set the root to the right child
                root = root.right

            # Otherwise, the root is the lowest common ancestor
            else:
                # Return the root
                return root
