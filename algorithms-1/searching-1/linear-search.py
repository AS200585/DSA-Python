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
def linear_search(number_list, number_to_find):
    for index, element in enumerate(number_list):
        if element == number_to_find:
            return index
    return -1

if __name__ == "__main__":
    """
    number_list = [12, 13, 24, 31, 45, 27, 41, 51, 60]
    number_to_find = int(input("Enter number to find : "))
    """
    number_list = [i for i in range(1000001)]
    number_to_find = int(input("Enter number to find : "))

    index = linear_search(number_list, number_to_find)
    print(f"Element in index {index}")