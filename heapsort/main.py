import unittest
import heapq

class TestCase(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(sort([]), [])

    def test_one_element_list(self):
        self.assertEqual(sort([1]), [1])

    def test_already_sorted_list(self):
        self.assertEqual(sort([1, 2, 3]), [1, 2, 3])

    def test_sort_1(self):
        self.assertEqual(sort([1, 3, 3]), [1, 3, 3])

    def test_sort_2(self):
        self.assertEqual(sort([1, 3, 2]), [1, 2, 3])

    def test_sort_3(self):
        self.assertEqual(sort([5, 4, 3, 1, 2]), [1, 2, 3, 4, 5])

    def test_sort_4(self):
        self.assertEqual(sort([5, -4, 3, 1, 2]), [-4, 1, 2, 3, 5])

def sort(l):
    """
    Returns a sorted version of the list l
    """
    heapq.heapify(l)
    return [heapq.heappop(l) for i in range(len(l))]

if __name__== "__main__":
    unittest.main()
