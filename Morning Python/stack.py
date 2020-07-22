# Data Structure: Stack
# pop removes and returns top element
# push adds an element to the top
class Stack:
    def __init__(self, data=[]):
        self.data = data

    def push(self, x):
        self.data.append(x)
        
    def pop(self):
        if self.isEmpty():
            return None
        x = self.data[-1]
        self.data = self.data[:-1]
        return x

    def peek(self):
        return self.data[-1]

    def isEmpty(self):
        return self.data == []

    def size(self):
        return len(self.data)

myStack = Stack()

# Data Structure: Queue
# push, pop -> enqueue, dequeue
# enqueue: adds an element at the end of a list
# dequeue: removes and returns the element at the front of the list
class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, x):
        self.inbox.push(x)

    def dequeue(self):
        while not self.inbox.isEmpty():
            self.outbox.push(self.inbox.pop())
        x = self.outbox.pop()
        while not self.outbox.isEmpty():
            self.inbox.push(self.outbox.pop())
        return x

    def isEmpty(self):
        return self.inbox.isEmpty() and self.outbox.isEmpty()

    def size(self):
        return self.inbox.size() + self.outbox.size()
