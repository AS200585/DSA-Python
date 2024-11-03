"""
Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
"""

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
        
    def peek(self):
        return self.container
        
    def is_empty(self):
        return len(self.container) == 0
        
    def size(self):
        return len(self.container)
    
    def reverse_string(self):
        reverse_order = list(self.container)[::-1]
        reverse_words = [word[::-1] for word in reverse_order]
        return ' '.join(reverse_words)
    
s = Stack()
s.push('We')
s.push('will')
s.push('conquere')
s.push('COVID-19')
s.push('We will conquere COVID-19')
print(s.peek())
print(s.reverse_string())
s.push('I am Napoleon, I am Emperor!')
print(s.peek())
print(s.reverse_string()) # Output