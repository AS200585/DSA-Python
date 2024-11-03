"""
Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". 
Use Stack class from the tutorial.
is_balanced("({a+b})")     --> True
is_balanced("))((a+b}{")   --> False
is_balanced("((a+b))")     --> True
is_balanced("))")          --> False
is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
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
        return self.container[-1]
        
    def is_empty(self):
        return len(self.container) == 0
        
    def is_balanced(self):
        stack = self.container
        opening = {'{': '}', '(': ')', '[': ']'}
        for i in range(len(stack)):
            if stack[i] in opening:
                return True
            else:
                return False
            
s =Stack()
s.push('({a+b})')
print(s.is_balanced())  
s.push('))((a+b}{')
print(s.is_balanced())
s.push("[a+b]*(x+2y)*{gg+kk}")
print(s.is_balanced())