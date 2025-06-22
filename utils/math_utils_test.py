import unittest
from utils.math_utils import add


class TestMathUtils(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        print("test_add_positive_numbers passed")

if __name__ == '__main__':
    unittest.main()