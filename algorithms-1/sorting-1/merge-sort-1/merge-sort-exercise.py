"""
Modify merge_sort function such that it can sort following list of athletes as per the time taken by them in the marathon,

elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
merge_sort function should take key from an athlete's marathon log and sort the list as per that key. For example,

merge_sort(elements, key='time_hours', descending=True)
This will sort elements by time_hours and your sorted list will look like,

elements = [
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
    ]

But if you call it like this,
merge_sort(elements, key='name')
output will be,

elements = [
        { 'name': 'chinmay',   'age': 24, 'time_hours': 1.5},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vedanth',  'age': 17,  'time_hours': 1},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
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
        print(f"{func.__name__} excecutes in {end_time - start_time:.10f} seconds")
        return result
    return wrapper


@time_it
def merge_sort_lists(left, right, arr, key, descending):
    len_left = len(left)
    len_right = len(right)
    i = j = k = 0

    while i < len_left and j < len_right:
        if (left[i][key] <= right[j][key]) != descending:
            arr[k] = left[i]
            i += 1 
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len_left:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len_right:
        arr[k] = right[j]
        j += 1
        k += 1


#@time_it
def merge_sort_array(arr, key, descending=False):
    if len(arr) <= 1:
        return 
    mid = len(arr)//2
    left = arr[mid:]
    right = arr[:mid]

    merge_sort_array(left, key, descending)
    merge_sort_array(right, key, descending)
    merge_sort_lists(left, right, arr, key, descending)


if __name__ == '__main__':
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    print(elements)
    merge_sort_array(elements, key='time_hours', descending=True)
    print("Descendig Time:\n", elements)
    merge_sort_array(elements, key="name")
    print("Name:\n", elements)
    merge_sort_array(elements, key='time_hours', descending=False)
    print("Ascending Time:\n", elements)