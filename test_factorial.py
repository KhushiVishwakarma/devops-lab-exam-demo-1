import unittest
from factorial import factorial   # IMPORTANT

class FactorialTests(unittest.TestCase):

    def test_five(self):
        self.assertEqual(factorial(5), 120)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_one(self):
        self.assertEqual(factorial(1), 1)

    def test_non_int(self):
        with self.assertRaises(ValueError):
            factorial("a")

    def test_negative(self):
        with self.assertRaises(ValueError):
            factorial(-5)

if __name__ == "__main__":
    unittest.main()
