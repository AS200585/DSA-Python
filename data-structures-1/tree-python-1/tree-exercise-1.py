"""
Below is the management hierarchy of a company,
Nilupul (CEO)
Chinmay (CTO)
Vishwa (Infrastructure Head)
Dhaval (Cloud Manager)
Abhijit (App Manager)
Aamir (Application Head)
Gels (HR Head)
Peter (Recruitment Manager)
Waqas (Policy Manager)

Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class. 
Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree.
As shown below,
CEO

| __ CTO
_Infrastructure Head
| __ Cloud Manager
| __ App Manager
| __ Application Head
HR Head
Recruitment Manager
_Policy Manager

Nilupul
| __ Chinmay
| __ Vishwa
| __ Dhaval
| __ Abhijit
| __ Aamir
| __ Gels
| __ Peter
| __ Waqas

Nilupul (CEO)
| __ Chinmay (CTO)
| __ Vishwa (Infrastructure Head)
| __ Dhaval (Cloud Manager)
| __ Abhijit (App Manager)
| __ Aamir (Application Head)
| __ Gels (HR Head)
| __ Peter (Recruitment Manager)
| __ Waqas (Policy Manager)

Here is how your main function should will look like,
if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy
"""

class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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
    def build_management_tree():
        
        root = TreeNode("Nilupul", "(CEO)")
        cto = TreeNode("Chinmay", "(CTO)")
        cto.add_child(TreeNode("Vishwa", "(Infrastructure Head)"))
        cto.add_child(TreeNode("Dhaval", "(Cloud Manager)"))
        cto.add_child(TreeNode("Abhijit", "(App Manager)"))
        cto.add_child(TreeNode("Aamir", "(Application Head)"))
        hrHead = TreeNode("Gels", "(HR Head)")
        hrHead.add_child(TreeNode("Peter ", "(Recruitment Manager)"))
        hrHead.add_child(TreeNode("Waqas", "(Policy Manager)"))

        root.add_child(cto)
        root.add_child(hrHead)

        print(root.get_level())
        print(cto.get_level())
        print(hrHead.get_level())
        return root
    
    def print_tree(self, view):
        if view == "name":
            value = self.name
        elif view == "designation":
            value =  self.designation
        elif view == "both":
            value =  f"{self.name} {self.designation}"
        else:
            print("Invalid view")
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + "|----" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(view)


if __name__ == "__main__":
    tree = TreeNode.build_management_tree()
    tree.print_tree("designation")