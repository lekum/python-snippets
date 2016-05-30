import unittest

class TestCase(unittest.TestCase):
    
    def test_0(self):
        self.assertEqual(multiplication(12, 0), 0)

    def test_1(self):
        self.assertEqual(multiplication(1, 230), 230)

    def test_one_by_two_digits(self):
        self.assertEqual(multiplication(5, 23), 115)

    def test_two_by_one_digits(self):
        self.assertEqual(multiplication(75, 7), 525)

    def test_six_by_seven_digits(self):
        self.assertEqual(multiplication(135795, 2775928), 376957142760)

    def test_commutative(self):
        self.assertEqual(multiplication(2775928, 135795), 376957142760)

def multiplication(a, b):
    """
    Multiplies two ints, a and b
    """

    a = str(a)
    b = str(b)
    res = 0

    def multiply_by_digit(row, digit):
        res = 0
        for row_index, row_digit in enumerate(reversed(row)):
            res += (int(digit) * int(row_digit)) * (10 ** row_index)
        return res

    for index_b, digit_b in enumerate(reversed(b)):
        res += multiply_by_digit(a, digit_b) * (10 ** index_b)
    return res

if __name__== "__main__":
    unittest.main()
