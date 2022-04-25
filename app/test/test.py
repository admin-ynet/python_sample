import unittest
from num_double import num_double

class Test_num_double(unittest.TestCase):
    def test_num_double(self):
        num = 3
        expected = 6
        actual = num_double(num)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()