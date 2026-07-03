def bubble_sort(arr: list) -> None:
    """Sort the array using bubble sort (in-place).

    Args:
        arr: list to be sorted (modified in-place)
    """
    n = len(arr)
    if n <= 1:
        return arr
    
    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

                swapped = True

        if not swapped:
            break


def insertion_sort(arr: list) -> None:
    """Sort the array using insertion sort (in-place).

    Args:
        arr: list to be sorted (modified in-place)
    """
    n = len(arr)
    if n <= 1:
        return arr
    
    for i in range(1, len(arr)):
        target = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > target:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = target


def merge_sort(arr: list) -> list:
    """Sort the array using merge sort (out-of-place).

    Args:
        arr: list to be sorted (not modified)

    Returns:
        New sorted list
    """
    n = len(arr)
    if n <= 1:
        return arr
    
    mid = n // 2
    
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    new_arr = []

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            new_arr.append(left[i])
            i += 1
        else:
            new_arr.append(right[j])
            j += 1
    
    new_arr += left[i:]
    new_arr += right[j:]
    
    return new_arr
    

def quick_sort(arr: list) -> list:
    """Sort the array using quick sort (out-of-place).

    Args:
        arr: list to be sorted (not modified)

    Returns:
        New sorted list
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]

    lte_arr = []
    gt_arr = []

    for x in arr[:-1]:
        if x <= pivot:
            lte_arr.append(x)
        if x > pivot:
            gt_arr.append(x)

    return quick_sort(lte_arr) + [pivot] + quick_sort(gt_arr)


if __name__ == "__main__":
    import time
    from random import shuffle
    
    length_of_list = int(input("Length of list: "))
    

    def run_sort(sort_algorithm):
        def wrapper():
            x = list(range(1, length_of_list + 1))
            shuffle(x)
            # print(x)

            start_time = time.perf_counter()
            y = sort_algorithm(x)
            end_time = time.perf_counter()

            if y is not None:
                x = y
            
            # print(x)
            print(f"{sort_algorithm.__name__} took {1e6 * (end_time - start_time):.2f} µs")
        
        return wrapper


    sort_algorithms = [bubble_sort, insertion_sort, merge_sort, quick_sort]
    
    for alg in sort_algorithms:
        try:
            run_sort(alg)()
        except NotImplementedError:
            print("NotImplementedError")
