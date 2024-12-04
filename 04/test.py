import unittest
from day04 import solve_a, solve_b

class MyTestCase(unittest.TestCase):

    def test_a(self):
        xmas_count = solve_a('sample')
        self.assertEqual(18, xmas_count)

    def test_b(self):
        xmas_count = solve_b('sample')
        self.assertEqual(9, xmas_count)

if __name__ == '__main__':
    unittest.main()
