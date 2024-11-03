from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        print("Value added : " + self.buffer.appendleft(val))

    def dequeue(self):
        return "Value removed : " + self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return "Total elements : " + len(self.buffer)

