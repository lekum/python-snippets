import unittest

class TestCase(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(quicksort([]), [])

    def test_one_element_list(self):
        self.assertEqual(quicksort([1]), [1])

    def test_already_sorted_list(self):
        self.assertEqual(quicksort([1, 2, 3]), [1, 2, 3])

    def test_sort_1(self):
        self.assertEqual(quicksort([1, 3, 3]), [1, 3, 3])

    def test_sort_2(self):
        self.assertEqual(quicksort([1, 3, 2]), [1, 2, 3])

    def test_sort_3(self):
        self.assertEqual(quicksort([5, 4, 3, 1, 2]), [1, 2, 3, 4, 5])

    def test_sort_4(self):
        self.assertEqual(quicksort([5, -4, 3, 1, 2]), [-4, 1, 2, 3, 5])

def quicksort(l):
    """
    Returns a sorted version of the list l
    """
    if len(l) < 2:
        return l
    pivot_index = len(l) // 2
    smaller_items = []
    larger_items = []

    for i, val in enumerate(l):
        if i != pivot_index:
            if val < l[pivot_index]:
                smaller_items.append(val)
            else:
                larger_items.append(val)

    left_part = quicksort(smaller_items)
    right_part = quicksort(larger_items)
    return left_part + [ l[pivot_index] ] + right_part


if __name__== "__main__":
    unittest.main()
