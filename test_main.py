import unittest
import main


class TestBubbleSort(unittest.TestCase):
    """Unit tests for bubble sort (in-place)."""

    def test_empty_input(self):
        """Check that function can handle empty input."""
        try:
            arr = []
            main.bubble_sort(arr)
            self.assertEqual(arr, [], "Empty list should remain empty")
        except NotImplementedError:
            self.skipTest("bubble_sort not yet implemented")

    def test_single_element(self):
        """Check that function can handle single element."""
        try:
            arr = [5]
            main.bubble_sort(arr)
            self.assertEqual(arr, [5], "Single element list should remain unchanged")
        except NotImplementedError:
            self.skipTest("bubble_sort not yet implemented")

    def test_two_elements_sorted(self):
        """Check that function handles two sorted elements."""
        try:
            arr = [1, 2]
            main.bubble_sort(arr)
            self.assertEqual(arr, [1, 2], "Two sorted elements should remain sorted")
        except NotImplementedError:
            self.skipTest("bubble_sort not yet implemented")

    def test_two_elements_unsorted(self):
        """Check that function handles two unsorted elements."""
        try:
            arr = [2, 1]
            main.bubble_sort(arr)
            self.assertEqual(arr, [1, 2], "Two unsorted elements should be sorted")
        except NotImplementedError:
            self.skipTest("bubble_sort not yet implemented")

    def test_already_sorted(self):
        """Check that function handles already sorted input."""
        try:
            arr = [1, 2, 3, 4, 5]
            main.bubble_sort(arr)
            self.assertEqual(arr, [1, 2, 3, 4, 5], "Already sorted list should remain sorted")
        except NotImplementedError:
            self.skipTest("bubble_sort not yet implemented")

    def test_reverse_sorted(self):
        """Check that function handles reverse sorted input."""
        try:
            arr = [5, 4, 3, 2, 1]
            main.bubble_sort(arr)
            self.assertEqual(arr, [1, 2, 3, 4, 5], "Reverse sorted list should be sorted")
        except NotImplementedError:
            self.skipTest("bubble_sort not yet implemented")

    def test_all_identical(self):
        """Check that function handles all identical elements."""
        try:
            arr = [3, 3, 3, 3]
            main.bubble_sort(arr)
            self.assertEqual(arr, [3, 3, 3, 3], "All identical elements should remain unchanged")
        except NotImplementedError:
            self.skipTest("bubble_sort not yet implemented")

    def test_with_negatives(self):
        """Check that function handles negative numbers."""
        try:
            arr = [3, -1, 4, -5, 2]
            main.bubble_sort(arr)
            self.assertEqual(arr, [-5, -1, 2, 3, 4], "List with negatives should be sorted correctly")
        except NotImplementedError:
            self.skipTest("bubble_sort not yet implemented")

    def test_with_duplicates(self):
        """Check that function handles duplicate values."""
        try:
            arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
            main.bubble_sort(arr)
            self.assertEqual(arr, [1, 1, 2, 3, 4, 5, 5, 6, 9], "List with duplicates should be sorted correctly")
        except NotImplementedError:
            self.skipTest("bubble_sort not yet implemented")

    def test_with_strings(self):
        """Check that function handles strings."""
        try:
            arr = ["banana", "apple", "cherry"]
            main.bubble_sort(arr)
            self.assertEqual(arr, ["apple", "banana", "cherry"], "List of strings should be sorted alphabetically")
        except NotImplementedError:
            self.skipTest("bubble_sort not yet implemented")

    def test_length_preserved(self):
        """Check that function preserves list length."""
        try:
            arr = [3, 1, 4, 1, 5]
            original_length = len(arr)
            main.bubble_sort(arr)
            self.assertEqual(len(arr), original_length, f"Length should be preserved: was {original_length}, now {len(arr)}")
        except NotImplementedError:
            self.skipTest("bubble_sort not yet implemented")

    def test_same_elements(self):
        """Check that the original and sorted array have the same elements."""
        try:
            arr = [3, 1, 4, 1, 5]
            original_sorted = sorted(arr)
            main.bubble_sort(arr)
            self.assertEqual(sorted(arr), original_sorted, "Elements should be the same (multiset equality)")
        except NotImplementedError:
            self.skipTest("bubble_sort not yet implemented")

    def test_elements_sorted(self):
        """Check that elements in the final array are sorted."""
        try:
            arr = [3, 1, 4, 1, 5]
            main.bubble_sort(arr)
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    self.fail(f"Elements not sorted at positions {i} and {i + 1}: {arr[i]} > {arr[i + 1]}")
        except NotImplementedError:
            self.skipTest("bubble_sort not yet implemented")


class TestInsertionSort(unittest.TestCase):
    """Unit tests for insertion sort (in-place)."""

    def test_empty_input(self):
        """Check that function can handle empty input."""
        try:
            arr = []
            main.insertion_sort(arr)
            self.assertEqual(arr, [], "Empty list should remain empty")
        except NotImplementedError:
            self.skipTest("insertion_sort not yet implemented")

    def test_single_element(self):
        """Check that function can handle single element."""
        try:
            arr = [5]
            main.insertion_sort(arr)
            self.assertEqual(arr, [5], "Single element list should remain unchanged")
        except NotImplementedError:
            self.skipTest("insertion_sort not yet implemented")

    def test_two_elements_sorted(self):
        """Check that function handles two sorted elements."""
        try:
            arr = [1, 2]
            main.insertion_sort(arr)
            self.assertEqual(arr, [1, 2], "Two sorted elements should remain sorted")
        except NotImplementedError:
            self.skipTest("insertion_sort not yet implemented")

    def test_two_elements_unsorted(self):
        """Check that function handles two unsorted elements."""
        try:
            arr = [2, 1]
            main.insertion_sort(arr)
            self.assertEqual(arr, [1, 2], "Two unsorted elements should be sorted")
        except NotImplementedError:
            self.skipTest("insertion_sort not yet implemented")

    def test_already_sorted(self):
        """Check that function handles already sorted input."""
        try:
            arr = [1, 2, 3, 4, 5]
            main.insertion_sort(arr)
            self.assertEqual(arr, [1, 2, 3, 4, 5], "Already sorted list should remain sorted")
        except NotImplementedError:
            self.skipTest("insertion_sort not yet implemented")

    def test_reverse_sorted(self):
        """Check that function handles reverse sorted input."""
        try:
            arr = [5, 4, 3, 2, 1]
            main.insertion_sort(arr)
            self.assertEqual(arr, [1, 2, 3, 4, 5], "Reverse sorted list should be sorted")
        except NotImplementedError:
            self.skipTest("insertion_sort not yet implemented")

    def test_all_identical(self):
        """Check that function handles all identical elements."""
        try:
            arr = [3, 3, 3, 3]
            main.insertion_sort(arr)
            self.assertEqual(arr, [3, 3, 3, 3], "All identical elements should remain unchanged")
        except NotImplementedError:
            self.skipTest("insertion_sort not yet implemented")

    def test_with_negatives(self):
        """Check that function handles negative numbers."""
        try:
            arr = [3, -1, 4, -5, 2]
            main.insertion_sort(arr)
            self.assertEqual(arr, [-5, -1, 2, 3, 4], "List with negatives should be sorted correctly")
        except NotImplementedError:
            self.skipTest("insertion_sort not yet implemented")

    def test_with_duplicates(self):
        """Check that function handles duplicate values."""
        try:
            arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
            main.insertion_sort(arr)
            self.assertEqual(arr, [1, 1, 2, 3, 4, 5, 5, 6, 9], "List with duplicates should be sorted correctly")
        except NotImplementedError:
            self.skipTest("insertion_sort not yet implemented")

    def test_with_strings(self):
        """Check that function handles strings."""
        try:
            arr = ["banana", "apple", "cherry"]
            main.insertion_sort(arr)
            self.assertEqual(arr, ["apple", "banana", "cherry"], "List of strings should be sorted alphabetically")
        except NotImplementedError:
            self.skipTest("insertion_sort not yet implemented")

    def test_length_preserved(self):
        """Check that function preserves list length."""
        try:
            arr = [3, 1, 4, 1, 5]
            original_length = len(arr)
            main.insertion_sort(arr)
            self.assertEqual(len(arr), original_length, f"Length should be preserved: was {original_length}, now {len(arr)}")
        except NotImplementedError:
            self.skipTest("insertion_sort not yet implemented")

    def test_same_elements(self):
        """Check that the original and sorted array have the same elements."""
        try:
            arr = [3, 1, 4, 1, 5]
            original_sorted = sorted(arr)
            main.insertion_sort(arr)
            self.assertEqual(sorted(arr), original_sorted, "Elements should be the same (multiset equality)")
        except NotImplementedError:
            self.skipTest("insertion_sort not yet implemented")

    def test_elements_sorted(self):
        """Check that elements in the final array are sorted."""
        try:
            arr = [3, 1, 4, 1, 5]
            main.insertion_sort(arr)
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    self.fail(f"Elements not sorted at positions {i} and {i + 1}: {arr[i]} > {arr[i + 1]}")
        except NotImplementedError:
            self.skipTest("insertion_sort not yet implemented")


class TestMergeSort(unittest.TestCase):
    """Unit tests for merge sort (out-of-place)."""

    def test_empty_input(self):
        """Check that function can handle empty input."""
        try:
            arr = []
            result = main.merge_sort(arr)
            self.assertEqual(result, [], "Empty list should return empty list")
        except NotImplementedError:
            self.skipTest("merge_sort not yet implemented")

    def test_single_element(self):
        """Check that function can handle single element."""
        try:
            arr = [5]
            result = main.merge_sort(arr)
            self.assertEqual(result, [5], "Single element list should return single element")
        except NotImplementedError:
            self.skipTest("merge_sort not yet implemented")

    def test_two_elements_sorted(self):
        """Check that function handles two sorted elements."""
        try:
            arr = [1, 2]
            result = main.merge_sort(arr)
            self.assertEqual(result, [1, 2], "Two sorted elements should remain sorted")
        except NotImplementedError:
            self.skipTest("merge_sort not yet implemented")

    def test_two_elements_unsorted(self):
        """Check that function handles two unsorted elements."""
        try:
            arr = [2, 1]
            result = main.merge_sort(arr)
            self.assertEqual(result, [1, 2], "Two unsorted elements should be sorted")
        except NotImplementedError:
            self.skipTest("merge_sort not yet implemented")

    def test_already_sorted(self):
        """Check that function handles already sorted input."""
        try:
            arr = [1, 2, 3, 4, 5]
            result = main.merge_sort(arr)
            self.assertEqual(result, [1, 2, 3, 4, 5], "Already sorted list should remain sorted")
        except NotImplementedError:
            self.skipTest("merge_sort not yet implemented")

    def test_reverse_sorted(self):
        """Check that function handles reverse sorted input."""
        try:
            arr = [5, 4, 3, 2, 1]
            result = main.merge_sort(arr)
            self.assertEqual(result, [1, 2, 3, 4, 5], "Reverse sorted list should be sorted")
        except NotImplementedError:
            self.skipTest("merge_sort not yet implemented")

    def test_all_identical(self):
        """Check that function handles all identical elements."""
        try:
            arr = [3, 3, 3, 3]
            result = main.merge_sort(arr)
            self.assertEqual(result, [3, 3, 3, 3], "All identical elements should remain unchanged")
        except NotImplementedError:
            self.skipTest("merge_sort not yet implemented")

    def test_with_negatives(self):
        """Check that function handles negative numbers."""
        try:
            arr = [3, -1, 4, -5, 2]
            result = main.merge_sort(arr)
            self.assertEqual(result, [-5, -1, 2, 3, 4], "List with negatives should be sorted correctly")
        except NotImplementedError:
            self.skipTest("merge_sort not yet implemented")

    def test_with_duplicates(self):
        """Check that function handles duplicate values."""
        try:
            arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
            result = main.merge_sort(arr)
            self.assertEqual(result, [1, 1, 2, 3, 4, 5, 5, 6, 9], "List with duplicates should be sorted correctly")
        except NotImplementedError:
            self.skipTest("merge_sort not yet implemented")

    def test_with_strings(self):
        """Check that function handles strings."""
        try:
            arr = ["banana", "apple", "cherry"]
            result = main.merge_sort(arr)
            self.assertEqual(result, ["apple", "banana", "cherry"], "List of strings should be sorted alphabetically")
        except NotImplementedError:
            self.skipTest("merge_sort not yet implemented")

    def test_original_unchanged(self):
        """Check that function does not modify original list."""
        try:
            arr = [3, 1, 4, 1, 5]
            original = arr[:]
            main.merge_sort(arr)
            self.assertEqual(arr, original, "Original list should remain unchanged")
        except NotImplementedError:
            self.skipTest("merge_sort not yet implemented")

    def test_length_correct(self):
        """Check that returned list has correct length."""
        try:
            arr = [3, 1, 4, 1, 5]
            original_length = len(arr)
            result = main.merge_sort(arr)
            self.assertEqual(len(result), original_length, f"Length should be preserved: was {original_length}, now {len(result)}")
        except NotImplementedError:
            self.skipTest("merge_sort not yet implemented")

    def test_same_elements(self):
        """Check that the returned array has the same elements as input."""
        try:
            arr = [3, 1, 4, 1, 5]
            original_sorted = sorted(arr)
            result = main.merge_sort(arr)
            self.assertEqual(sorted(result), original_sorted, "Elements should be the same (multiset equality)")
        except NotImplementedError:
            self.skipTest("merge_sort not yet implemented")

    def test_elements_sorted(self):
        """Check that elements in the returned array are sorted."""
        try:
            arr = [3, 1, 4, 1, 5]
            result = main.merge_sort(arr)
            for i in range(len(result) - 1):
                if result[i] > result[i + 1]:
                    self.fail(f"Elements not sorted at positions {i} and {i + 1}: {result[i]} > {result[i + 1]}")
        except NotImplementedError:
            self.skipTest("merge_sort not yet implemented")


class TestQuickSort(unittest.TestCase):
    """Unit tests for quick sort (out-of-place)."""

    def test_empty_input(self):
        """Check that function can handle empty input."""
        try:
            arr = []
            result = main.quick_sort(arr)
            self.assertEqual(result, [], "Empty list should return empty list")
        except NotImplementedError:
            self.skipTest("quick_sort not yet implemented")

    def test_single_element(self):
        """Check that function can handle single element."""
        try:
            arr = [5]
            result = main.quick_sort(arr)
            self.assertEqual(result, [5], "Single element list should return single element")
        except NotImplementedError:
            self.skipTest("quick_sort not yet implemented")

    def test_two_elements_sorted(self):
        """Check that function handles two sorted elements."""
        try:
            arr = [1, 2]
            result = main.quick_sort(arr)
            self.assertEqual(result, [1, 2], "Two sorted elements should remain sorted")
        except NotImplementedError:
            self.skipTest("quick_sort not yet implemented")

    def test_two_elements_unsorted(self):
        """Check that function handles two unsorted elements."""
        try:
            arr = [2, 1]
            result = main.quick_sort(arr)
            self.assertEqual(result, [1, 2], "Two unsorted elements should be sorted")
        except NotImplementedError:
            self.skipTest("quick_sort not yet implemented")

    def test_already_sorted(self):
        """Check that function handles already sorted input."""
        try:
            arr = [1, 2, 3, 4, 5]
            result = main.quick_sort(arr)
            self.assertEqual(result, [1, 2, 3, 4, 5], "Already sorted list should remain sorted")
        except NotImplementedError:
            self.skipTest("quick_sort not yet implemented")

    def test_reverse_sorted(self):
        """Check that function handles reverse sorted input."""
        try:
            arr = [5, 4, 3, 2, 1]
            result = main.quick_sort(arr)
            self.assertEqual(result, [1, 2, 3, 4, 5], "Reverse sorted list should be sorted")
        except NotImplementedError:
            self.skipTest("quick_sort not yet implemented")

    def test_all_identical(self):
        """Check that function handles all identical elements."""
        try:
            arr = [3, 3, 3, 3]
            result = main.quick_sort(arr)
            self.assertEqual(result, [3, 3, 3, 3], "All identical elements should remain unchanged")
        except NotImplementedError:
            self.skipTest("quick_sort not yet implemented")

    def test_with_negatives(self):
        """Check that function handles negative numbers."""
        try:
            arr = [3, -1, 4, -5, 2]
            result = main.quick_sort(arr)
            self.assertEqual(result, [-5, -1, 2, 3, 4], "List with negatives should be sorted correctly")
        except NotImplementedError:
            self.skipTest("quick_sort not yet implemented")

    def test_with_duplicates(self):
        """Check that function handles duplicate values."""
        try:
            arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
            result = main.quick_sort(arr)
            self.assertEqual(result, [1, 1, 2, 3, 4, 5, 5, 6, 9], "List with duplicates should be sorted correctly")
        except NotImplementedError:
            self.skipTest("quick_sort not yet implemented")

    def test_with_strings(self):
        """Check that function handles strings."""
        try:
            arr = ["banana", "apple", "cherry"]
            result = main.quick_sort(arr)
            self.assertEqual(result, ["apple", "banana", "cherry"], "List of strings should be sorted alphabetically")
        except NotImplementedError:
            self.skipTest("quick_sort not yet implemented")

    def test_original_unchanged(self):
        """Check that function does not modify original list."""
        try:
            arr = [3, 1, 4, 1, 5]
            original = arr[:]
            main.quick_sort(arr)
            self.assertEqual(arr, original, "Original list should remain unchanged")
        except NotImplementedError:
            self.skipTest("quick_sort not yet implemented")

    def test_length_correct(self):
        """Check that returned list has correct length."""
        try:
            arr = [3, 1, 4, 1, 5]
            original_length = len(arr)
            result = main.quick_sort(arr)
            self.assertEqual(len(result), original_length, f"Length should be preserved: was {original_length}, now {len(result)}")
        except NotImplementedError:
            self.skipTest("quick_sort not yet implemented")

    def test_same_elements(self):
        """Check that the returned array has the same elements as input."""
        try:
            arr = [3, 1, 4, 1, 5]
            original_sorted = sorted(arr)
            result = main.quick_sort(arr)
            self.assertEqual(sorted(result), original_sorted, "Elements should be the same (multiset equality)")
        except NotImplementedError:
            self.skipTest("quick_sort not yet implemented")

    def test_elements_sorted(self):
        """Check that elements in the returned array are sorted."""
        try:
            arr = [3, 1, 4, 1, 5]
            result = main.quick_sort(arr)
            for i in range(len(result) - 1):
                if result[i] > result[i + 1]:
                    self.fail(f"Elements not sorted at positions {i} and {i + 1}: {result[i]} > {result[i + 1]}")
        except NotImplementedError:
            self.skipTest("quick_sort not yet implemented")


if __name__ == '__main__':
    unittest.main()
