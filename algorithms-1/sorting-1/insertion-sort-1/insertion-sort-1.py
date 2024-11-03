from functools import wraps
import time

def time_it(func):
    wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} excecutes in {end_time - start_time:.10f} seconds")
        return result
    return wrapper

@time_it
def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j = j - 1
        elements[j + 1] = anchor
    return elements

if __name__ == '__main__':
    elements = [11, 4, 23, 19, 32, 6, 45, 28, 39]
    print(elements)
    print(insertion_sort(elements))

    test = [
        [11, 4, 26, 14, 6, 21],
        [3, 7, 9, 11],
        [25, 22, 19, 13],
        [29, 15, 28],
        [6, 4, 2],
        [],
        [1]
    ]

    for elements in test:
        insertion_sort(elements)
        print(f"Sorted Arrays : {elements}")