# Dictionary is the python specific implementation of the hash table
def get_hash(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100

# using this class we have implemented a dictionary
class HashTable:
    def __init__(self):
        self.MAX = 99
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, val):
        ht = self.get_hash(key)
        found = False
        #iteration for linked list
        for idx, element in enumerate(self.arr[ht]):
            if len(element)==2 and element[0] == key:
                self.arr[ht][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[ht].append((key, val))

    def __getitem__(self, key):
        ht = self.get_hash(key)
        for element in self.arr[ht]:
            if element[0] == key:
                return element[1]
    
    def __delitem__(self, key):
        ht = self.get_hash(key)
        for index, element in enumerate(self.arr[ht]):
            if element[0] == key:
                del self.arr[ht][index]
    
ht = HashTable()
print(ht.get_hash('march 6'))
print(ht.get_hash('march 20'))
ht['march 6'] = 130
ht['march 6'] = 228
ht['march 2'] = 109
ht['april 7'] = 87
ht['march 17'] = 400
print(ht['march 6'])
print(ht.arr)
print(ht['april 7'])
print(ht['march 20'])
del ht['march 6'] # delete item
print(ht.arr)
print(ht.get_hash('march 17'))
print(ht['march 6'])