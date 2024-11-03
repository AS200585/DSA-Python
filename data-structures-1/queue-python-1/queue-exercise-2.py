"""
Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. 
Binary sequence should look like,

    1
    10
    11
    100
    101
    110
    111
    1000
    1001
    1010

Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 
4th and 5th number are second number (i.e. 10) + 0 and second number (i.e. 10) + 1.
You also need to add front() function in queue class that can return the front element in the queue.
"""

from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)
        print("Value added : " + val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return
        removed_val = self.buffer.pop()
        print("Value removed : " + removed_val)
        return removed_val
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return "Total elements : " + str(len(self.buffer))

    def front(self):
        return self.buffer[-1]
    
def binary_numbers(n):  
    number_queue = Queue()
    number_queue.enqueue("1")

    for i in range(n):
        front = number_queue.front()
        print(" ", front)
        number_queue.enqueue(front + '0')
        number_queue.enqueue(front + '1')
        number_queue.dequeue()

if __name__ == "__main__":
    binary_numbers(12)
