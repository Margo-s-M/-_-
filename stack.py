# import heapq
#
# stack = []
# #push
# stack.append(10)
# stack.append(12)
# print(stack)
#
# top_element = stack.pop()
# print(top_element)
# #peek
#
# top_element = stack[-1]
# print(top_element)
# print(stack)
#
# class TextEditor:
#     def __init__(self):
#         self.text = ""
#         self.history = []
#
#     def type(self,text):
#         self.history.append(self.text)
#         self.text += text
#
#     def undo(self):
#         if self.history:
#             self.text = self.history.pop()
#
# editor = TextEditor()
# editor.type("Hello")
# editor.type("Word")
# print(editor.text)
# editor.undo()
# print(editor.text)
#
# class Stack :
#
#     def __init__(self,max_size):
#         self.max_size = max_size
#         self.items = [None] * max_size
#         self.top_index = -1
#
#     def is_empty(self):
#         return self.top_index == -1
#
#     def is_full(self):
#         return self.top_index == self.max_size -1
#
#     def push(self,item):
#         if self.is_full():
#             raise OverflowError("push to full stack")
#         self.top_index += 1
#         self.items[self.top_index] = item
#
#     def pop(self):
#         if self.is_empty():
#             raise IndexError("Pop from emty stack")
#         item = self.items[self.top_index]
#         self.items[self.top_index] = None
#         self.top_index -= 1
#         return  item
#
#     def paek(self):
#         if self.is_empty():
#             raise IndexError("PEACK FROM EMPTY STACK")
#         return  self.items[self.top_index]
#
#     def size(self):
#         return self.top_index + 1
#
# stack1 =Stack(5)
# stack1.push(8)
# stack1.push(7)
# stack1.push(4)
# stack1.push(2)
# print(stack1.paek())
# print(stack1.pop())
# print(stack1.size())

#without size
# class Stack:
#
#     def __init__(self):
#         self.items = []
#         self.top_index = -1
#
#     def is_empty(self):
#         return self.top_index == -1
#
#     def push(self, item):
#         self.top_index += 1
#         if self.top_index < len(self.items):
#             self.items[self.top_index] = item
#         else:
#             self.items.append(item)
#
#     def pop(self):
#         if self.is_empty():
#             raise IndexError("Pop from empty stack")
#         item = self.items[self.top_index]
#         self.items[self.top_index] = None
#         self.top_index -= 1
#         return item
#
#     def peek(self):
#         if self.is_empty():
#             raise IndexError("Peek from empty stack")
#         return self.items[self.top_index]
#
#     def get_size(self):
#         return self.top_index + 1
# class Stack:
#     def __init__(self):
#         self.items = []
#         self.top_index = -1
#
#     def is_empty(self):
#         return self.top_index == -1
#
#     def push(self, item):
#         self.items.append(item)
#         self.top_index += 1
#
#     def pop(self):
#         if self.is_empty():
#             raise IndexError("Pop from empty stack")
#         item = self.items.pop()
#         self.top_index -= 1
#         return item
#
#     def peek(self):
#         if self.is_empty():
#             raise IndexError("Peek from empty stack")
#         return self.items[self.top_index]
#
#     def size(self):
#         return self.top_index + 1
#
#
# stack = Stack()
# stack.push(8)
# stack.push(7)
# stack.push(4)
# stack.push(2)
#
# print("Верхній елемент:", stack.peek())
# print("Видалений елемент:", stack.pop())
# print("Розмір стеку:", stack.size())
# stack.push(10)
# print("Новий верхній елемент:", stack.peek())
#
#
#
# from collections import deque
#
# queue = deque()
# queue.append(36)
# queue.append(50)
# print(queue)
# front_elem = queue.popleft()
# print(front_elem)
# front = queue[0]
# print(front)
#
# class Printer:
#     def __init__(self):
#         self.queue = deque()
#
#     def add_jop(self,job):
#         self.queue.append(job)
#
#     def print_job(self):
#         if self.queue:
#             job = self.queue.popleft()
#             print(f"Printing:{job}")
#
# q1 = Printer()
# q1.add_jop("Doc1")
# q1.add_jop("Doc2")
# q1.print_job()
# q1.print_job()
#
#
#
# #pr1 Реалізація черг
#
# class Queue:
#     def __init__(self):
#         self.items = []
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def add_queue(self,item):
#         self.items.append(item)
#
#     def del_queue(self):
#         if self.is_empty():
#             raise IndexError("Deleted from empty queue")
#         return self.items.pop(0)
#
#     def display(self):
#         if self.is_empty():
#             print("The queue is empty")
#         else:
#             print("Queue items", "->".join(map(str,self.items)))
#
#
# queue = Queue()
#
# queue.add_queue("Hello")
# queue.add_queue("World")
#
# deleted_item = queue.del_queue()
# print("Deleted from queue:", deleted_item)
#
# queue.display()
#
# deleted_item = queue.del_queue()
# print("Deleted from queue:", deleted_item)
# queue.display()
#
# print("Is it empty?", queue.is_empty())
#
#
# class Prior:
#     def __init__(self,max_size):
#         self.queue = []
#         self.max_size = max_size
#
#     def enqueue(self,char,priority):
#         heapq.heappush(self.queue,(priority,char))
#     def dequeue(self):
#         return heapq.heappop(self.queue)[1]
#
#     def peak(self):
#         return self.queue[0][1]
#     def display(self):
#         res = [(char,priority) for priority, char in self.queue]
#         print(res)
# q2 = Prior(2)
# q2.enqueue("4",3)
# q2.enqueue("34",1)
# q2.enqueue("74",2)
# q2.display()
#
#
#
#
#
#
#
# #pr2
#
# class PriorityQueue:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.items = []
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def is_full(self):
#         return len(self.items) == self.capacity
#
#     def enqueue(self, item, priority):
#         if self.is_full():
#             raise OverflowError("Queue is full")
#
#         new_element = (priority, item)#position in len
#         inserted = False
#         for i in range(len(self.items)):
#             if self.items[i][0] < priority:
#                 self.items.insert(i, new_element)
#                 inserted = True
#                 break
#
#         if not inserted:
#             self.items.append(new_element)#insert element by item in the end
#     def dequeue(self):
#         if self.is_empty():
#             raise IndexError("Dequeue from empty queue")
#         return self.items.pop(0)[1]
#
#     def peek(self):
#         if self.is_empty():
#             raise IndexError("Peek from empty queue")
#         return self.items[0][1]
#
#     def display(self):
#         if self.is_empty():
#             print("The queue is empty")
#         else:
#             print("Queue items (пріоритет:елемент):", " -> ".join(f"{priority}:{item}" for priority, item in self.items))
#
#     def size(self):
#         return len(self.items)
#


# pq = PriorityQueue(5)
#
# #add el
# pq.enqueue("H", 3)
# pq.enqueue("E", 5)
# pq.enqueue("L", 1)
# pq.enqueue("L", 4)
# pq.enqueue("O", 5)


# pq.display()
#
# # найвищий пріоритет
# print("Peek:", pq.peek())
# print("Dequeued:", pq.dequeue())
# pq.display()

# print("Is it empty?", pq.is_empty())
# print("Queue size:", pq.size())

#dz
#■ Додати нового користувача
# ■ Видалити існуючого користувача Перевірити чи існує користувач
# ■ Змінити логін наявного користувача ■ Змінити пароль наявного користувача

class UserMeta(type):
    def __new__(cls, name, bases, dct):
        if 'users' not in dct:
            dct['users'] = {}
        return super().__new__(cls, name, bases, dct)


class UserManagement(metaclass=UserMeta):
    def add_user(self, login, password):
        if login in self.users:
            print(f"User with login '{login}' already exists.")
        else:
            self.users[login] = password
            print(f"User '{login}' added successfully.")

    def remove_user(self, login):
        if login in self.users:
            del self.users[login]
            print(f"User '{login}' removed successfully.")
        else:
            print(f"No user found with login '{login}'.")

    def check_user_exists(self, login):
        if login in self.users:
            print(f"User '{login}' exists.")
            return True
        else:
            print(f"No user found with login '{login}'.")
            return False

    def change_user_login(self, old_login, new_login):
        if old_login not in self.users:
            print(f"No user found with login '{old_login}'.")
        elif new_login in self.users:
            print(f"A user with login '{new_login}' already exists.")
        else:
            self.users[new_login] = self.users.pop(old_login)
            print(f"Login changed from '{old_login}' to '{new_login}'.")

    def change_user_password(self, login, new_password):
        if login in self.users:
            self.users[login] = new_password
            print(f"Password for user '{login}' updated successfully.")
        else:
            print(f"No user found with login '{login}'.")

    def display_users(self):
        if not self.users:
            print("No users found.")
        else:
            print("Current users:")
            for login, password in self.users.items():
                print(f"Login: {login}, Password: {password}")


def main_menu():
    user_manager = UserManagement()

    while True:
        print("\nMenu:")
        print("1. Add a new user")
        print("2. Remove an existing user")
        print("3. Check if a user exists")
        print("4. Change an existing user's login")
        print("5. Change an existing user's password")
        print("6. Display all users")
        print("7. Exit")

        choice = input("Your choice: ")

        if choice == '1':
            login = input("Enter new user's login: ")
            password = input("Enter user's password: ")
            user_manager.add_user(login, password)

        elif choice == '2':
            login = input("Enter the login of the user to remove: ")
            user_manager.remove_user(login)

        elif choice == '3':
            login = input("Enter the login to check: ")
            user_manager.check_user_exists(login)

        elif choice == '4':
            old_login = input("Enter the current login of the user: ")
            new_login = input("Enter the new login: ")
            user_manager.change_user_login(old_login, new_login)

        elif choice == '5':
            login = input("Enter the login of the user: ")
            new_password = input("Enter the new password: ")
            user_manager.change_user_password(login, new_password)

        elif choice == '6':
            user_manager.display_users()

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main_menu()
