def swap(a, b, arr):
    # arr[a], arr[b] = arr[b], arr[a]  different method of swapping
    if a!= b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]
    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        while elements[end] > pivot:
            end -= 1
        if start < end:
            swap(start, end, elements)
    swap(pivot_index, end, elements)
    return end

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)  #left
        quick_sort(elements, pi + 1, end)    #right

if __name__ == '__main__':
    elements_list = [11, 9, 29, 7, 2, 18, 34, 12, 8]
    tests = [
        [11, 9, 29, 7, 2, 15, 18, 40, 37, 28, 21, 17, 34],
        [3, 7, 9, 11, 13],
        [],
        [6],
        [31, 27, 23, 19, 14]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements) - 1)
        print(f'sorted array: {elements}')
    
    quick_sort(elements_list, 0, len(elements_list) - 1)
    print(f"sorted elements_list : {elements_list}")