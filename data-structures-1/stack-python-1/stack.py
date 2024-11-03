"""
s = []
s.append('https://www.hindustantimes.com/')
s.append('https://www.hindustantimes.com/india-news')
s.append('https://www.hindustantimes.com/htcity')
s.append('https://www.hindustantimes.com/entertainment')
print(s.pop())
print(s.pop())
print(s.pop())
"""

from collections import deque

stack = deque()

# print(dir(stack))

stack.append('https://www.hindustantimes.com/')
stack.append('https://www.hindustantimes.com/india-news')
stack.append('https://www.hindustantimes.com/htcity')
print(stack)
print(stack.pop())
print(stack)