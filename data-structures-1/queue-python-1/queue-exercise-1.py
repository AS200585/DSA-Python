"""
Design a food ordering system where your python program will run two threads,
Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. 
(hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. 
This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started. Use multithreading 

Pass following list as an argument to place order thread,
orders = ['pizza','samosa','pasta','biryani','burger']

This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is 
consuming the food orders. Use Queue class implemented in a video tutorial.
"""

from collections import deque
from queue import Queue
import threading
import time

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)
        print("Value added: " + val)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        val = self.buffer.pop()
        print("Value removed: " + val)
        return val

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return "Total elements: " + str(len(self.buffer))
    
food_order = Queue()

def place_orders(orders):
    for order in orders:
        print("Placing order for - " + order)
        food_order.enqueue(order)
        time.sleep(0.5)

def serve_orders():
    time.sleep(1)
    while True:
        order = food_order.dequeue()
        print("Serving - " + order)
        time.sleep(2)

if __name__ == "__main__":
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target = place_orders, args = (orders, ))
    t2 = threading.Thread(target = serve_orders)

t1.start()
t2.start()