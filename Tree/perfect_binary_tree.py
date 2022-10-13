# This is the implementation of perfect binary tree


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    # Calculate the depth
    def calculateDepth(self, node):
        d = 0
        while node is not None:
            d += 1
            node = node.left
        return d

    # Check if the tree is perfect binary tree
    def isPerfectBinaryTree(self, root, d, level=0):

        # Check if the tree is empty
        if root is None:
            return True

        # Check the presence of trees
        if root.left is None and root.right is None:
            return d == level + 1

        if root.left is None or root.right is None:
            return False

        return self.isPerfectBinaryTree(
            root.left, d, level + 1
        ) and self.isPerfectBinaryTree(root.right, d, level + 1)
