import unittest
from day05 import solve_a, solve_b

class MyTestCase(unittest.TestCase):

    def test_a(self):
        middle_sum = solve_a('sample')
        self.assertEqual(143, middle_sum)

    def test_b(self):
        middle_sum = solve_b('sample')
        self.assertEqual(123, middle_sum)

if __name__ == '__main__':
    unittest.main()
