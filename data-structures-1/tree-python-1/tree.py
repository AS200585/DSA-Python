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

class TreeNode:
    @time_it
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    @staticmethod
    def build_tree():
        root = TreeNode("Electronics")

        audio = TreeNode("Audio")
        audio.add_child(TreeNode("Television"))
        audio.add_child(TreeNode("Radio"))
        audio.add_child(TreeNode("DVD"))
        audio.add_child(TreeNode("CD"))
        audio.add_child(TreeNode("MP"))
        audio.add_child(TreeNode("MP3"))

        laptop = TreeNode("Laptop")
        laptop.add_child(TreeNode("Mac"))
        laptop.add_child(TreeNode("Surface"))
        laptop.add_child(TreeNode("Thinkpad"))
        laptop.add_child(TreeNode("Vivobook"))
        laptop.add_child(TreeNode("Acer"))

        cellphone = TreeNode("Cellphone")
        cellphone.add_child(TreeNode("Nokia"))
        cellphone.add_child(TreeNode("BlackBerry"))
        cellphone.add_child(TreeNode("Samsung"))
        cellphone.add_child(TreeNode("Apple"))

        trimmer = TreeNode("Trimmers")
        trimmer.add_child(TreeNode("Philips"))
        trimmer.add_child(TreeNode("Nova"))
        trimmer.add_child(TreeNode("Panasonic"))
        trimmer.add_child(TreeNode("Bajaj"))
        trimmer.add_child(TreeNode("Bald"))

        root.add_child(audio)
        root.add_child(laptop)
        root.add_child(cellphone)
        root.add_child(trimmer)

        print(root.get_level())
        print(audio.get_level())
        print(laptop.get_level())
        print(cellphone.get_level())
        print(trimmer.get_level()) 
        return root
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + "|----" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


if __name__ == "__main__":
    tree = TreeNode.build_tree()
    tree.print_tree()