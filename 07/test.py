import unittest
from day07 import solve_a, solve_b

class MyTestCase(unittest.TestCase):

    def test_a(self):
        result_sum = solve_a('sample')
        self.assertEqual(3749, result_sum)

    def test_b(self):
        result_sum = solve_b('sample')
        self.assertEqual(11387, result_sum)

if __name__ == '__main__':
    unittest.main()
