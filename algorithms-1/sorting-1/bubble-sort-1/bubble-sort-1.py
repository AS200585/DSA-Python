from functools import wraps
import time

def time_it(func):
    wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} excecutes in {end_time -start_time:.10f} seconds")
        return result
    return wrapper

@time_it
def bubble_sort(elements):
    size = len(elements)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                temp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = temp
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
#   elements = [5, 8, 2, 1, 36, 67, 35, 27, 55, 43] excecutes in 0.0000151000 seconds
#   elements = [12, 14, 17, 20, 25, 29, 31, 34, 38] executes in 0.0000082000 seconds(sorted)
    elements = ["George", "Alice", "Ian", "Diana", "Charlie", "Fiona", "Julia", "Ethan", "Hannah", "Bob"] # excecutes in 0.0000187000 seconds

    bubble_sort(elements)
    print(elements)