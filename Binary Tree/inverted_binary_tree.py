"""
Given the root of a binary tree, invert the tree, and return its root.


Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Answer: Use a queue to store the nodes of the tree. Pop the first node from the queue. Swap the left and right children of the node. Add the left and right children of the node to the queue. Repeat until the queue is empty.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.val} -> {self.left} {self.right}"


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # If the root is None
        if root is None:
            # Return None
            return None

        # Create a queue
        queue = [root]

        # While the queue is not empty
        while queue:
            # Pop the first node from the queue
            node = queue.pop(0)

            # Swap the left and right children of the node
            node.left, node.right = node.right, node.left

            # If the left child of the node is not None
            if node.left is not None:
                # Add the left child to the queue
                queue.append(node.left)

            # If the right child of the node is not None
            if node.right is not None:
                # Add the right child to the queue
                queue.append(node.right)

        # Return the root
        return root
