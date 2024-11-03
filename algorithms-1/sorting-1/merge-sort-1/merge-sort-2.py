# Without return statement

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


def merge_sort_lists(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1 
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


@time_it
def merge_sort_array(arr):
    if len(arr) <= 1:
        return 
    mid = len(arr)//2
    left = arr[mid:]
    right = arr[:mid]

    merge_sort_array(left)
    merge_sort_array(right)
    merge_sort_lists(left, right, arr)


if __name__ == "__main__":
    # arr = [16, 4, 21, 11, 9, 3, 38, 17, 32, 6]
    tests = [
        [14, 26, 12, 1, 42, 32, 5],
        [1, 2, 3, 4, 5, 6],
        [22, 20, 18, 15, 12, 9, 8, 6, 3, 2, 1],
        [13, 21, 19, 32, 23, 45],
        [],
        [9],
        [7, 7, 7]
    ]
    print(f"test cases : {tests}")
    for arr in tests:
        merge_sort_array(arr)
        print(arr)
    """
    print(f"arr : {arr}")
    merge_sort_array(arr)
    print(arr)
    """