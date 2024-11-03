from functools import wraps
import time

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} took {end_time - start_time:.10f} seconds")
        return result
    return wrapper

class BinarySearchTreeNode:
    @time_it
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
    

if __name__ == "__main__":
    numbers = [12, 17, 2, 5, 21, 34, 23, 9, 18]
    numbers_tree = BinarySearchTreeNode.build_binary_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(34))