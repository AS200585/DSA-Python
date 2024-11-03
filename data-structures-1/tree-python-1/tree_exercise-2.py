"""
Build below location tree using TreeNode class
Global
|_India
  |__Gujarat
     |__Ahmedabad
     |__Baroda
  |__Karnataka
     |__Bangluru
     |__Mysore
|_USA
  |__New Jersey
     |__Princeton
     |__Trenton
  |__California
     |__San Francisco
     |__Mountain View
     |__Palo Alto

Now modify print_tree method to take tree level as input. And that should print tree only upto that level as shown below,
if__ name__ == ' __ main ':
root_node = build_location_tree()
root_node.print_tree()

root_node.print_tree(1)
Global
| __ India
| __ USA

root_node.print_tree(2)
Global
India
__ Gujarat
| __ Karnataka
USA
| __ New Jersey
California

root_node.print_tree(3)
Global
India
__ Gujarat
| __ Ahmedabad
| __ Baroda
Karnataka
__ Bangluru
| __ Mysore
USA
New Jersey
Princeton
Trenton
California
San Francisco
Mountain View
__ Palo Alto

"""


class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    @staticmethod
    def build_location_tree():
        root = TreeNode("Global")

        india = TreeNode("India")
        gujrat = TreeNode("Gujrat")
        gujrat.add_child(TreeNode("Ahmedabad"))
        gujrat.add_child(TreeNode("Baroda"))
        karnataka = TreeNode("Karnataka")
        karnataka.add_child(TreeNode("Bangaluru"))
        karnataka.add_child(TreeNode("Mysore"))

        usa = TreeNode("USA")
        newJersey = TreeNode("New Jersey")
        newJersey.add_child(TreeNode("Princeton"))
        newJersey.add_child(TreeNode("Trenton"))
        california = TreeNode("California")
        california.add_child(TreeNode("San Francisco"))
        california.add_child(TreeNode("Mountain View"))
        california.add_child(TreeNode("Palo Alto"))

        root.add_child(india)
        root.add_child(usa)
        india.add_child(gujrat)
        india.add_child(karnataka)
        usa.add_child(newJersey)
        usa.add_child(california)
        return root
    
    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        print(prefix + self.name)
        if self.children:
            for child in self.children:
                child.print_tree(level)


if __name__ == "__main__":
    tree = TreeNode.build_location_tree()
    tree.print_tree(1)