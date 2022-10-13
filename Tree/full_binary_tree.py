# This is the implementation of fully binary tree


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

    def isFullBinaryTree(self, root):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        if root.left is not None and root.right is not None:
            return self.isFullBinaryTree(root.left) and self.isFullBinaryTree(
                root.right
            )
        return False
