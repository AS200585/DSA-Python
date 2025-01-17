"""
Binary Tree Part 1 Exercise
Add following methods to BinarySearchTreeNode class created in main video tutorial

1. find_min(): finds minimum element in entire binary tree
2. find_max(): finds maximum element in entire binary tree
3. calculate_sum(): calcualtes sum of all elements
4. post_order_traversal(): performs post order traversal of a binary tree
5. pre_order_traversal(): perofrms pre order traversal of a binary tree
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
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
    
    def calculate_sum(self):
        total_sum = self.data
        if self.left:
            total_sum += self.left.calculate_sum()
        if self.right:
            total_sum += self.right.calculate_sum()
        return total_sum
        
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
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
    

if __name__ == "__main__":
    numbers = [12, 17, 2, 5, 21, 34, 23, 41, 9, 18, 38, 29, 46]
    numbers_tree = BinarySearchTreeNode.build_binary_tree(numbers)
    print("In-Order : ", numbers_tree.in_order_traversal())
    print("Search element : ", numbers_tree.search(34))
    print("Minimum value : ", numbers_tree.find_min())
    print("Maximum value : ", numbers_tree.find_max())
    print("Sum of all elements : ", numbers_tree.calculate_sum())
    print("Pre-Order : ", numbers_tree.pre_order_traversal())
    print("Post-Order : ", numbers_tree.post_order_traversal())