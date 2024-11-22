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

#pr 1
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


#pr2

class BookNode:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre
        self.left = None
        self.right = None


class BookRoot:
    def __init__(self):
        self.root = None  # Корінь

    def add_book(self, title, genre):
        if not self.root:
            self.root = BookNode(title, genre)
        else:
            self._add_book(self.root, title, genre)

    def _add_book(self, node, title, genre):
        if title < node.title:
            if node.left:
                self._add_book(node.left, title, genre)
            else:
                node.left = BookNode(title, genre)
        elif title > node.title:
            if node.right:
                self._add_book(node.right, title, genre)
            else:
                node.right = BookNode(title, genre)

    def search_by_title(self, title):
        return self._search_by_title(self.root, title)

    def _search_by_title(self, node, title):
        if not node:
            return "Книга не знайдена."
        if title == node.title:
            return f"Книга: {node.title}, Жанр: {node.genre}"
        elif title < node.title:
            return self._search_by_title(node.left, title)
        else:
            return self._search_by_title(node.right, title)

    def search_by_genre(self, genre):
        result = []
        self._search_by_genre(self.root, genre, result)
        return result if result else "Книги цього жанру не знайдено."

    def _search_by_genre(self, node, genre, result):
        if node:
            if node.genre == genre:
                result.append(node.title)
            self._search_by_genre(node.left, genre, result)
            self._search_by_genre(node.right, genre, result)



system = BookRoot()
system.add_book("Япізнаю світ.Інтелект України ", "Мама це не на довго")
system.add_book("Українська мова та література", "Школа лише 11 років")
system.add_book("Математика", "Мам ти ще жива")

print(system.search_by_title("Математика"))


print("Ти все можеш:", system.search_by_genre("Мам ти ще жива"))

#pr3

class FileNode:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.left = None
        self.right = None


class FileManager:
    def __init__(self):
        self.root = None

    def add_file(self, name, size):
        if not self.root:
            self.root = FileNode(name, size)
        else:
            self._add_file(self.root, name, size)

    def _add_file(self, node, name, size):
        if name < node.name:
            if node.left:
                self._add_file(node.left, name, size)
            else:
                node.left = FileNode(name, size)
        elif name > node.name:
            if node.right:
                self._add_file(node.right, name, size)
            else:
                node.right = FileNode(name, size)
    def search_file(self, name):
        return self._search_file(self.root, name)

    def _search_file(self, node, name):
        if not node:
            return "Файл не знайдено."
        if name == node.name:
            return f"Файл: {node.name}, Розмір: {node.size} байт"
        elif name < node.name:
            return self._search_file(node.left, name)
        else:
            return self._search_file(node.right, name)
    def list_files(self):
        files = []
        self._inorder(self.root, files)
        return files

    def _inorder(self, node, files):
        if node:
            self._inorder(node.left, files)
            files.append((node.name, node.size))
            self._inorder(node.right, files)


manager = FileManager()
manager.add_file("file1.txt", 500)
manager.add_file("file2.txt", 1500)
manager.add_file("image.png", 300)


print(manager.search_file("file2.txt"))

print("Список файлів:", manager.list_files())

