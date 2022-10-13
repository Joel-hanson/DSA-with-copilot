# This is an impelmetation of binary search tree


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

    # Search the tree
    def search(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    print(str(data) + " Not Found")
                else:
                    return self.left.search(data)
            elif data > self.data:
                if self.right is None:
                    print(str(data) + " Not Found")
                else:
                    return self.right.search(data)
            else:
                print(str(self.data) + " is found")
        else:
            print(str(data) + " Not Found")

    # Find the minimum value
    def findMin(self):
        if self.left is None:
            print("Minimum value is " + str(self.data))
        else:
            return self.left.findMin()

    # Find the maximum value
    def findMax(self):
        if self.right is None:
            print("Maximum value is " + str(self.data))
        else:
            return self.right.findMax()

    # Get the successor
    def getSuccessor(self, data):
        # Search the node first
        current = self.search(data)
        if current:
            if current.right:
                return current.right.findMin()
            else:
                # Find the ancestor of the current node
                ancestor = self
                successor = None
                while ancestor != current:
                    if current.data < ancestor.data:
                        successor = ancestor  # So far this is the deepest node for which current node is in left
                        ancestor = ancestor.left
                    else:
                        ancestor = ancestor.right
                return successor

    # Delete a node
    def delete(self, data):
        # Search the node first
        if self.data:
            if data < self.data:
                if self.left is None:
                    print(str(data) + " Not Found")
                else:
                    self.left = self.left.delete(data)
            elif data > self.data:
                if self.right is None:
                    print(str(data) + " Not Found")
                else:
                    self.right = self.right.delete(data)
            else:
                # If the node has no children
                if self.left is None and self.right is None:
                    self = None
                    return self
                # If the node has one child
                if self.left is None:
                    temp = self.right
                    self = None
                    return temp
                elif self.right is None:
                    temp = self.left
                    self = None
                    return temp
                # If the node has two children
                temp = self.right.findMin()
                self.data = temp.data
                self.right = self.right.delete(temp.data)

        else:
            print(str(data) + " Not Found")
            return self

    # Get the height of the tree
    def getHeight(self, node):
        if node is None:
            return -1
        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)
        return 1 + max(leftHeight, rightHeight)

    # Check if the tree is balanced
    def isBalanced(self, root):
        if root is None:
            return True
        heightDiff = self.getHeight(root.left) - self.getHeight(root.right)
        if abs(heightDiff) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    # Check if the tree is a binary search tree
    def isBinarySearchTree(self, root):
        if root is None:
            return True
        if root.left is not None and self.getMax(root.left) > root.data:
            return False
        if root.right is not None and self.getMin(root.right) < root.data:
            return False
        if not self.isBinarySearchTree(root.left) or not self.isBinarySearchTree(
            root.right
        ):
            return False
        return True

    # Get the minimum value in a non-empty binary search tree
    def getMin(self, node):
        if node.left is None:
            return node.data
        else:
            return self.getMin(node.left)

    # Get the maximum value in a non-empty binary search tree
    def getMax(self, node):
        if node.right is None:
            return node.data
        else:
            return self.getMax(node.right)

    # Get the size of the tree
    def getSize(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.getSize(node.left) + self.getSize(node.right)

    # Get the depth of a node
    def getDepth(self, node, data, depth):
        if node is None:
            return -1
        if node.data == data:
            return depth
        left = self.getDepth(node.left, data, depth + 1)
        if left >= 0:
            return left
        right = self.getDepth(node.right, data, depth + 1)
        return right

    # Get the level of a node
    def getLevel(self, node, data, level):
        if node is None:
            return -1
        if node.data == data:
            return level
        left = self.getLevel(node.left, data, level + 1)
        if left >= 0:
            return left
        right = self.getLevel(node.right, data, level + 1)
        return right

    # Get the ancestors of a node
    def getAncestors(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        if self.getAncestors(node.left, data) or self.getAncestors(node.right, data):
            print(node.data)
            return True
        return False

    # Get the cousins of a node
    def getCousins(self, node, data):
        if node is None:
            return
        if self.getLevel(node, node.data, 1) == self.getLevel(node, data, 1):
            self.printLevel(node, self.getLevel(node, node.data, 1), data)
        self.getCousins(node.left, data)
        self.getCousins(node.right, data)

    # Print all nodes at a given level
    def printLevel(self, node, level, data):
        if node is None:
            return
        if level == 1 and node.data != data:
            print(node.data)
        elif level > 1:
            self.printLevel(node.left, level - 1, data)
            self.printLevel(node.right, level - 1, data)

    # Get the sibling of a node
    def getSibling(self, node, data):
        if node is None:
            return None
        if node.left is not None and node.left.data == data:
            return node.right
        if node.right is not None and node.right.data == data:
            return node.left
        left = self.getSibling(node.left, data)
        if left is not None:
            return left
        right = self.getSibling(node.right, data)
        return right

    # Get the uncle of a node
    def getUncle(self, node, data):
        if node is None:
            return None
        if node.left is not None and node.left.data == data:
            return node.right
        if node.right is not None and node.right.data == data:
            return node.left
        left = self.getUncle(node.left, data)
        if left is not None:
            return left
        right = self.getUncle(node.right, data)
        return right

    # Get the lowest common ancestor of two nodes
    def getLowestCommonAncestor(self, node, data1, data2):
        if node is None:
            return None
        if node.data == data1 or node.data == data2:
            return node
        left = self.getLowestCommonAncestor(node.left, data1, data2)
        right = self.getLowestCommonAncestor(node.right, data1, data2)
        if left is not None and right is not None:
            return node
        if left is not None:
            return left
        else:
            return right

    # Get the distance between two nodes
    def getDistance(self, node, data1, data2):
        lca = self.getLowestCommonAncestor(node, data1, data2)
        d1 = self.getDepth(lca, data1, 0)
        d2 = self.getDepth(lca, data2, 0)
        return d1 + d2

    # Get the diameter of the tree
    def getDiameter(self, node):
        if node is None:
            return 0
        lheight = self.getHeight(node.left)
        rheight = self.getHeight(node.right)
        ldiameter = self.getDiameter(node.left)
        rdiameter = self.getDiameter(node.right)
        return max(lheight + rheight + 2, max(ldiameter, rdiameter))

    # Get the maximum width of the tree
    def getMaxWidth(self, node):
        h = self.getHeight(node)
        maxWidth = 0
        i = 1
        while i <= h:
            width = self.getWidth(node, i)
            if width > maxWidth:
                maxWidth = width
            i += 1
        return maxWidth

    # Get the width of a tree at a given level
    def getWidth(self, node, level):
        if node is None:
            return 0
        if level == 1:
            return 1
        elif level > 1:
            return self.getWidth(node.left, level - 1) + self.getWidth(
                node.right, level - 1
            )

    # Get the maximum path sum
    def getMaxPathSum(self, node):
        if node is None:
            return 0
        lsum = self.getMaxPathSum(node.left)
        rsum = self.getMaxPathSum(node.right)
        max_single = max(max(lsum, rsum) + node.data, node.data)
        max_top = max(max_single, lsum + rsum + node.data)
        self.getMaxPathSum.res = max(self.getMaxPathSum.res, max_top)
        return max_single
