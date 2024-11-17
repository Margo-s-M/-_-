import heapq

stack = []
#push
stack.append(10)
stack.append(12)
print(stack)

top_element = stack.pop()
print(top_element)
#peek

top_element = stack[-1]
print(top_element)
print(stack)

class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []

    def type(self,text):
        self.history.append(self.text)
        self.text += text

    def undo(self):
        if self.history:
            self.text = self.history.pop()

editor = TextEditor()
editor.type("Hello")
editor.type("Word")
print(editor.text)
editor.undo()
print(editor.text)

class Stack :

    def __init__(self,max_size):
        self.max_size = max_size
        self.items = [None] * max_size
        self.top_index = -1

    def is_empty(self):
        return self.top_index == -1

    def is_full(self):
        return self.top_index == self.max_size -1

    def push(self,item):
        if self.is_full():
            raise OverflowError("push to full stack")
        self.top_index += 1
        self.items[self.top_index] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from emty stack")
        item = self.items[self.top_index]
        self.items[self.top_index] = None
        self.top_index -= 1
        return  item

    def paek(self):
        if self.is_empty():
            raise IndexError("PEACK FROM EMPTY STACK")
        return  self.items[self.top_index]

    def size(self):
        return self.top_index + 1

stack1 =Stack(5)
stack1.push(8)
stack1.push(7)
stack1.push(4)
stack1.push(2)
print(stack1.paek())
print(stack1.pop())
print(stack1.size())

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
class Stack:
    def __init__(self):
        self.items = []
        self.top_index = -1

    def is_empty(self):
        return self.top_index == -1

    def push(self, item):
        self.items.append(item)
        self.top_index += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        item = self.items.pop()
        self.top_index -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[self.top_index]

    def size(self):
        return self.top_index + 1


stack = Stack()
stack.push(8)
stack.push(7)
stack.push(4)
stack.push(2)

print("Верхній елемент:", stack.peek())
print("Видалений елемент:", stack.pop())
print("Розмір стеку:", stack.size())
stack.push(10)
print("Новий верхній елемент:", stack.peek())



from collections import deque

queue = deque()
queue.append(36)
queue.append(50)
print(queue)
front_elem = queue.popleft()
print(front_elem)
front = queue[0]
print(front)

class Printer:
    def __init__(self):
        self.queue = deque()

    def add_jop(self,job):
        self.queue.append(job)

    def print_job(self):
        if self.queue:
            job = self.queue.popleft()
            print(f"Printing:{job}")

q1 = Printer()
q1.add_jop("Doc1")
q1.add_jop("Doc2")
q1.print_job()
q1.print_job()



#pr1 Реалізація черг

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_queue(self,item):
        self.items.append(item)

    def del_queue(self):
        if self.is_empty():
            raise IndexError("Deleted from empty queue")
        return self.items.pop(0)

    def display(self):
        if self.is_empty():
            print("The queue is empty")
        else:
            print("Queue items", "->".join(map(str,self.items)))


queue = Queue()

queue.add_queue("Hello")
queue.add_queue("World")

deleted_item = queue.del_queue()
print("Deleted from queue:", deleted_item)

queue.display()

deleted_item = queue.del_queue()
print("Deleted from queue:", deleted_item)
queue.display()

print("Is it empty?", queue.is_empty())


class Prior:
    def __init__(self,max_size):
        self.queue = []
        self.max_size = max_size

    def enqueue(self,char,priority):
        heapq.heappush(self.queue,(priority,char))
    def dequeue(self):
        return heapq.heappop(self.queue)[1]

    def peak(self):
        return self.queue[0][1]
    def display(self):
        res = [(char,priority) for priority, char in self.queue]
        print(res)
q2 = Prior(2)
q2.enqueue("4",3)
q2.enqueue("34",1)
q2.enqueue("74",2)
q2.display()







#pr2

class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def enqueue(self, item, priority):
        if self.is_full():
            raise OverflowError("Queue is full")

        new_element = (priority, item)#position in len
        inserted = False
        for i in range(len(self.items)):
            if self.items[i][0] < priority:
                self.items.insert(i, new_element)
                inserted = True
                break

        if not inserted:
            self.items.append(new_element)#insert element by item in the end
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)[1]

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0][1]

    def display(self):
        if self.is_empty():
            print("The queue is empty")
        else:
            print("Queue items (пріоритет:елемент):", " -> ".join(f"{priority}:{item}" for priority, item in self.items))

    def size(self):
        return len(self.items)



pq = PriorityQueue(5)

#add el
pq.enqueue("H", 3)
pq.enqueue("E", 5)
pq.enqueue("L", 1)
pq.enqueue("L", 4)
pq.enqueue("O", 5)


pq.display()

# найвищий пріоритет
print("Peek:", pq.peek())
print("Dequeued:", pq.dequeue())
pq.display()

print("Is it empty?", pq.is_empty())
print("Queue size:", pq.size())
