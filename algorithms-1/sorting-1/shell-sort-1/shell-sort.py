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
def shell_sort(arr):
    size = len(arr) 
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2


if __name__ == '__main__':
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
        shell_sort(elements)
        print(elements)