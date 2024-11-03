"""
Modify bubble_sort function such that it can sort following list of transactions happening in an electronic store,

elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
bubble_sort function should take key from a transaction record and sort the list as per that key. For example,

bubble_sort(elements, key='transaction_amount')
This will sort elements by transaction_amount and your sorted list will look like,
elements = [
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    ]

But if you call it like this,
bubble_sort(elements, key='name')
output will be,
elements = [
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    ]
"""


from functools import wraps
import time

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} executes in {end_time -start_time:.10f} seconds")
        return result
    return wrapper

@time_it
def bubble_sort(elements, key=None):
    size = len(elements)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j][key] > elements[j + 1][key]:
                temp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = temp
                swapped = True
        if not swapped:
            break
    return elements


if __name__ == "__main__":
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    print("Name :- ")
    print(bubble_sort(elements, key='name'))
    print("Transaction Amount :- ")
    print(bubble_sort(elements, key='transaction_amount'))