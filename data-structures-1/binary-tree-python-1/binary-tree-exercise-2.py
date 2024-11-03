"""
Modify delete method in class BinarySearchTreeNode class to use min element from left subtree.
You will remove lines marked with ---> and use max value from left subtree

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

          --->  min_val = self.right.find_min()
          --->  self.data = min_val
          --->  self.right = self.right.delete(min_val)
"""


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return "Value not found in left subtree"
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return "Value not found in right subtree"

    def build_binary_tree(elements):
        root = BinarySearchTreeNode(elements[0])
        for i in range(1, len(elements)):
            root.add_child(elements[i])
        return root
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left == self.right == None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            max_val = self.right.find_max()
            self.data = max_val
            self.right = self.right.delete(max_val)
        return self

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = BinarySearchTreeNode.build_binary_tree(numbers)
    print("Tree traverse : ", numbers_tree.in_order_traversal())
    numbers_tree.delete(17)
    print("1st deletion : ",numbers_tree.in_order_traversal()) 
    numbers_tree.delete(9)
    print("2nd deletion : ",numbers_tree.in_order_traversal())  
    numbers_tree.delete(34)
    print("3rd deletion : ",numbers_tree.in_order_traversal())