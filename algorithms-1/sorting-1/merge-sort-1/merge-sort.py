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
def merge_sort_lists(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1 
        else:
            sorted_list.append(b[j])
            j += 1

    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1
    return sorted_list


@time_it
def merge_sort_array(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[mid:]
    right = arr[:mid]

    left = merge_sort_array(left)
    right = merge_sort_array(right)
    return merge_sort_lists(left, right)


if __name__ == "__main__":
    a = [5, 26, 21, 9, 12, 31]
    b = [8, 16, 4, 1]
    arr = [16, 4, 21, 11, 9, 3, 38, 17, 32, 6]

    print(f"a: {a}, b: {b}")
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    print(merge_sort_lists(sorted_a, sorted_b))
    print(f"arr : {arr}")
    print(merge_sort_array(arr))