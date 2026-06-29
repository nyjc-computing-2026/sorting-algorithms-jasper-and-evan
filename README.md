In this assignment, you should write your code in a **readable** way.

Your function definitions should have **appropriate docstrings**.

# Sorting Algorithms

## Sections Covered
1. Sorting Algorithms
2. In-place vs Out-of-place Sorting
3. Algorithm Analysis

## In-place vs Out-of-place Sorting

**In-place sorting** modifies the original list directly. The function:
- Takes a list as a parameter
- Reorganizes the elements within that same list
- Does not return anything (returns `None`)
- Changes are visible to any code that references the original list

**Out-of-place sorting** creates and returns a new sorted list. The function:
- Takes a list as a parameter
- Creates a new list with the elements in sorted order
- Returns the new sorted list
- Does not modify the original input list

### Examples:
```python
# In-place sorting
my_list = [3, 1, 2]
bubble_sort(my_list)  # Returns None
print(my_list)  # [1, 2, 3] - original list is modified

# Out-of-place sorting
my_list = [3, 1, 2]
sorted_list = merge_sort(my_list)  # Returns new sorted list
print(my_list)      # [3, 1, 2] - original list unchanged
print(sorted_list)  # [1, 2, 3] - new sorted list returned
```

## Part 1: Bubble Sort (In-place)
Implement the bubble sort algorithm in the `bubble_sort(arr)` function. Bubble sort works by repeatedly stepping through the list, comparing adjacent elements and swapping them if they are in the wrong order.

**Requirements:**
- Sort in-place (modify the input list directly)
- Return None
- Handle all test cases including edge cases

## Part 2: Insertion Sort (In-place)
Implement the insertion sort algorithm in the `insertion_sort(arr)` function. Insertion sort builds the sorted array one item at a time by comparing each new element with the already-sorted elements and inserting it in the correct position.

**Requirements:**
- Sort in-place (modify the input list directly)
- Return None
- Handle all test cases including edge cases

## Part 3: Merge Sort (Out-of-place)
Implement the merge sort algorithm in the `merge_sort(arr)` function. Merge sort is a divide-and-conquer algorithm that divides the array into halves, recursively sorts them, and merges the sorted halves.

**Requirements:**
- Sort out-of-place (return a new sorted list)
- Do not modify the input list
- Return the new sorted list

## Part 4: Quick Sort (Out-of-place)
Implement the quick sort algorithm in the `quick_sort(arr)` function. Quick sort is another divide-and-conquer algorithm that selects a pivot element and partitions the array around the pivot.

**Requirements:**
- Sort out-of-place (return a new sorted list)
- Do not modify the input list
- Return the new sorted list

## Notes
- Your implementations should work with both integers and strings
- Your implementations should work with edge cases like empty lists, single elements, and duplicates. Hint: Keep the implementation simple so that it is easier to debug

# Submission

Before submitting your code, run the automated tests on your functions. In the shell, type `python test_main.py` and press enter to see the results of the testing.
