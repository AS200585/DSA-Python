from functools import wraps
import time

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} excecutes in {end_time - start_time:.10f} seconds")
        return result
    return wrapper


@time_it
def minimum_element(arr):
    min = 10000
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min


@time_it
def selection_sort(arr):
    size = len(arr)
    for i in range(size-1): # size - 1 for performance improvement
        min_index = i
        for j in range(min_index + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    # elements = [78, 12, 15, 8, 61, 53, 3, 23, 27]
    tests = [
        [10, 3, 15, 7, 24, 8, 23, 1, 98, 29, 77, 59],
        [2, 3, 5, 6, 8, 9, 11, 14, 19, 23, 28, 33],
        [4, 4, 4, 4, 4],
        [],
        [8],
        [31, 26, 22, 20, 17, 13, 10, 9, 7, 5, 3, 2, 1],
        [13, 21, 19, 32, 23, 45, 22, 38]
    ]
    for elements in tests:
        print(minimum_element(elements))
        selection_sort(elements)
        print(elements)