# Dictionary is the python specific implementation of the hash table
# Hash table is a data structure that stores key-value pairs. 
# It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.
from functools import wraps
import time

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} took {end_time - start_time:.10f} seconds")
        return result
    return wrapper

def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100

print(get_hash('#$};'))

# using this class we have implemented a dictionary
class HashTable:
    @time_it
    def __init__(self):
        self.MAX = 99
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, val):
        ht = self.get_hash(key)
        self.arr[ht] = val

    def __getitem__(self, key):
        ht = self.get_hash(key)
        return self.arr[ht]
    
    def __delitem__(self, key):
        ht = self.get_hash(key)
        self.arr[ht] = None
    
ht = HashTable()
print(ht.get_hash('january 30'))
ht['march 6'] =  130
ht['march 2'] = 109
ht['april 7'] = 87
print(ht['march 6'])
print(ht.arr)
print(ht['april 7'])
print(ht['march 20'])
del ht['march 6'] # delete item
print(ht.arr)