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

@time_it
def binary_search_recursive(number_list, number_to_find, left_index, right_index): 
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index) // 2
    if mid_index >= len(number_list) or mid_index < 0:
        return -1
    mid_number = number_list[mid_index]
    if mid_number == number_to_find:
        return mid_index
    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
    return binary_search_recursive(number_list, number_to_find, left_index, right_index) 

    
if __name__ == "__main__":
    """
    number_list = [12, 13, 24, 31, 45, 27, 41, 51, 60]
    number_to_find = int(input("Enter number to find : "))
    """
    number_list = [i for i in range(1000001)]
    number_to_find = int(input("Enter number to find : "))

    index = binary_search_recursive(number_list, number_to_find, 0, len(number_list))
    print(f"Element in index {index}")