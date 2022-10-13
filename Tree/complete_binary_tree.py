# This is the implementation of complete binary tree


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

    def isCompleteBinaryTree(self, root, index, number_nodes):
        # Check if the tree is empty
        if root is None:
            return True

        # Check if the index is in range
        if index >= number_nodes:
            return False

        # Check the presence of trees
        return self.isCompleteBinaryTree(
            root.left, 2 * index + 1, number_nodes
        ) and self.isCompleteBinaryTree(root.right, 2 * index + 2, number_nodes)

    def countNodes(self, root):
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
