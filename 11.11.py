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


    def append(self,data):
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
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
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


    initial_data = input("Введіть числа списку: ")
    for num in initial_data.split():
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
            linked_list.append(data)
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
class Node:#через двозвязний список
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete(self, del_data):#послідовніть видалення
        current = self.head
        while current:
            if current.data == del_data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                print(f"Елемент '{del_data}' видалено.")
                return
            current = current.next
        print(f"Елемент '{del_data}' не знайдено.")

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Список:", " <-> ".join(elements) if elements else "список порожній")

def menu():
    linked_list = DoublyLinkedList()

    initial_data = input("Введіть рядки для списку через кому: ").split(',')
    for item in initial_data:
        linked_list.append(item.strip())

    while True:
        print("\nМеню:")
        print("1. Додати елемент у список")
        print("2. Видалити елемент зі списку")
        print("3. Показати вміст списку")
        print("4. Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            data = input("Введіть рядок для додавання: ")
            linked_list.append(data)
            print(f"Додано значення '{data}'.")
        elif choice == '2':
            data = input("Введіть рядок для видалення: ")
            linked_list.delete(data)
        elif choice == '3':
            linked_list.display()
        elif choice == '4':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


menu()

#dz
def menu():
    # Init. the list
    numbers = list(map(int, input("Enter numbers : ").split()))

    while True:
        print("\nMenu:")
        print("1. Add a new number:")
        print("2. Remove all occurrences of a number from the list:")
        print("3. Show the list content:")
        print("4. Check if the number exists in the list:")
        print("5. Replace a value in the list:")
        print("6. Exit:")

        choice = input("Your choice: ")

        if choice == '1':
            num = int(input("Enter a number to add: "))
            if num in numbers:
                print(f"The number {num} already exists in the list.")
            else:
                numbers.append(num)
                print(f"The number {num} was added")

        elif choice == '2':
            num = int(input("Enter a number to remove: "))
            count = numbers.count(num)
            if count > 0:
                numbers = [x for x in numbers if x != num]
                print(f"The number {num} was removed {count} times from the list.")
            else:
                print(f"The number {num} was not found ")

        elif choice == '3':
            direction = input("Enter '1' to display from the beginning or '2' to display from the end: ")
            if direction == '1':
                print("List from the beginning:", numbers)
            elif direction == '2':
                print("List from the end:", numbers[::-1])
            else:
                print("Invalid choice!")

        elif choice == '4':
            num = int(input("Enter a number to check: "))
            if num in numbers:
                print(f"The number {num} exists in the list.")
            else:
                print(f"The number {num} does not exist ")

        elif choice == '5':
            old_value = int(input("Enter the value to replace: "))
            new_value = int(input("Enter the new value: "))
            option = input("Enter '1' to replace the first occurrence or '2' to replace all occurrences: ")

            if option == '1':
                if old_value in numbers:
                    index = numbers.index(old_value)
                    numbers[index] = new_value
                    print(f"The first occurrence of {old_value} was replaced with {new_value}.")
                else:
                    print(f"The number {old_value} was not found in the list.")
            elif option == '2':
                count = numbers.count(old_value)
                if count > 0:
                    numbers = [new_value if x == old_value else x for x in numbers]
                    print(f"All {count} occurrences of {old_value} were replaced with {new_value}.")
                else:
                    print(f"The number {old_value} was not found in the list.")
            else:
                print("Invalid choice!")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")

menu()
