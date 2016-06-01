import unittest

class Tests(unittest.TestCase):

    def test_palindrome_1(self):
        self.assertTrue(is_palindrome("aja"))

    def test_palindrome_2(self):
        self.assertFalse(is_palindrome("ajx"))

    def test_palindrome_3(self):
        self.assertTrue(is_palindrome("a jj a"))

    def test_palindrome_4(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))

    def test_palindrome_5(self):
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))

    def test_palindrome_6(self):
        self.assertTrue(is_palindrome("No ‘x’ in Nixon"))

    def test_palindrome_7(self):
        self.assertFalse(is_palindrome("Was it ss a car or a cat I saw?"))

def is_palindrome(sentence):
    """
    Return if a given sentence is a palindrome
    """
    sentence = [i.lower() for i in sentence if i.isalpha()]
    l = len(sentence)
    if l<2:
        return True
    for i in range(l//2):
        if sentence[i] != sentence[l-i-1]:
            return False
    else:
        return True

if __name__ == "__main__":
    unittest.main()
