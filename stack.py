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
class Stack :

    def __init__(self,size):
        self.size = size
        self.items = [None] * size
        self.top_index = -1

    def is_empty(self):
        return self.top_index == -1

    def is_full(self):
        return self.top_index == self.size -1

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