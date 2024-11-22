class Tree:
    def __init__(self,cargo,left=None,right=None):
        self.cargo = cargo
        self.left = left
        self.right = None


    def __str__(self):
        return str(self.cargo)

left = Tree(2)
right = Tree(7)

tree = Tree(6,left,right)
tree2 = Tree(1,Tree(4),Tree(6))
print(tree)
print(tree2)

class TreeNode:

    def __init__(self,cargo):
        self.cargo = cargo
        self.left =None
        self.right =None

def insert(root,cargo):
    if root is None:
        return TreeNode(cargo)
    else:
        if cargo < root.cargo:
            root.left = insert(root.left,cargo)
        else:
            root.right = insert(root.right,cargo)
    return root

def search(root, cargo):
    if root is None or root.cargo == cargo:
        return root
    if cargo < root.cargo:
        return search(root.left,cargo)
    return search(root.right,cargo)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.cargo, end=" ")
        inorder(root.right)

def find_min(root):
    current = root
    while current.left is not None:
        current = current.left#найбільше значення  буде в правій
        return current
def delete(root,cargo):
    if root is None:
        return root
    if cargo < root.cargo:
        root.left = delete(root.left, cargo)
    elif cargo > root.cargo:
        root.right = delete(root.right, cargo)
    else:
        if root.left is None:
            return root.right
        elif root.left is None:
            return root.left
        temp = find_min(root.right)
        root.cargo = temp.cargo
        root.right = delete(root.right, temp.cargo)
    return root

root = None
cargos = [90,7,25,1,25,90,77]
for cargo in cargos:
    root = insert(root,cargo)
inorder(root)
result = search(root,13)
if result:
    print("hurra")
root = delete(root,56)
inorder(root)

pr 1
class EmployeeNode:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.left = None
        self.right = None
def insert_el(root, name,position):
    if root is None:
        return EmployeeNode(name,position)
    else:
        if root.left is None:
            root.left = insert_el(root.left,name,position)
        elif root.right is None:
            root.right = insert_el(root.left, name,position)
    return  root

def print_h(root,level = 0):
    if root:
        print(' '*level*4 +f"{root.position}:{root.name}")
        print_h(root.left , level +1)
        print_h(root.left, level +1)
em_tree = EmployeeNode("Alica","CEO")
em_tree = EmployeeNode("Bob","CTO")
em_tree =EmployeeNode("Chack","CFO")
em_tree =EmployeeNode("Ana","Enginner")
em_tree = EmployeeNode("Borys", "Accountant")
print_h(em_tree)

