#структури даних, дані повязані між собою, маючи посилада від одного до наступного,цепочка
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None #клас вузол , next має покликання на
class SingLinkList:#набір вузлів
    def __init__(self):
        self.head = None#початок

    def append(self,data):#
        new_node = Node(data)#екземпляр класу вузол
        if not self.head :
            self.head =new_node
            return
        last = self.head#записуємо head
        while last.next:
            last = last.next
        last.next = new_node
#однозвязний спиcок
    def display(self):
        current =self.head
        while current:
            print(current.data,end="- >")
            current = current.next
        print("None")

    def delete(self,del_data):
        current = self.head
        if current and current.data == del_data:
            self.head = current.next
            return
        prev = None
        while current and current.data != del_data:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
sll = SingLinkList()
sll.append(1)
sll.append(2)
sll.append(4)
sll.display()
sll.delete(2)



#двозвязний список
class Node:
    def __init__(self,data): #(None,4,b) (a,97,c)
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def display(self):
        current = self.head
        while current:
            print(current.data, end="- >")
            current = current.next
        print("None")

all = DoublyLinkedList()

all.append(7)
all.append(8)
all.append(7)
all.append(8)

all.display()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top =None

    def push(self,data):
        new_node = Node(data)
        new_node.next =self.top
        self.top =new_node
    def pop(self):
        if not self.top:
            return None
        data = self.top.data
        self.top = self.top.next
        return data
    def display(self):
        current = self.top
        while current:
            print(current.data, end="- >")
            current = current.next
        print("None")

stack = Stack()

stack.push(4)
stack.push(7)
stack.push(9)
stack.display()
print(stack.pop())
stack.display()

#pr1
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None


    def append(self,data):#
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


    def delete(self, del_data):
        current = self.head
        if current and current.data == del_data:
            self.head = current.next
            return
        prev = None
        while current and current.data != del_data:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next

    def display(self):
        current = self.head
        elements =[]
        while current:
            elements.append(current.data)
            current =current.next
            print("Список:", "->".join(map(str,elements))if elements else "спимок прожній")

    def find(self, data):
        current = self.head
        while current:
            if current.data == data:
                print(f"Значення {data} знайдено у списку.")
                return True
            current = current.next
        print(f"Значення {data} не знайдено у списку.")
        return False

    def replace(self, old_data, new_data):
        current = self.head
        while current:
            if current.data == old_data:
                current.data = new_data
                print(f"Значення {old_data} замінено на {new_data}.")
                return
            current = current.next
        print(f"Значення {old_data} не знайдено у списку.")


def menu():
    linked_list = LinkList()


    initial_data = input("Введіть числа списку: ").split()
    for num in initial_data:
        linked_list.append(int(num))

    while True:
        print("\nМеню:")
        print("1. Додати елемент у список")
        print("2. Видалити елемент зі списку")
        print("3. Показати вміст списку")
        print("4. Перевірити, чи є значення у списку")
        print("5. Замінити значення у списку")
        print("6. Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            data = int(input("Введіть значення для додавання: "))
            linked_list.append()
            print(f"Додано значення {data}.")
        elif choice == '2':
            data = int(input("Введіть значення для видалення: "))
            linked_list.delete(data)
        elif choice == '3':
            linked_list.display()
        elif choice == '4':
            data = int(input("Введіть значення для перевірки: "))
            linked_list.find(data)
        elif choice == '5':
            old_data = int(input("Введіть значення для заміни: "))
            new_data = int(input("Введіть нове значення: "))
            linked_list.replace(old_data, new_data)
        elif choice == '6':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір.")
menu()


#pr2