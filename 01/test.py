import unittest
from day01 import solve_a, solve_b

class MyTestCase(unittest.TestCase):

    def test_a(self):
        total_distance = solve_a('sample_data')
        self.assertEqual(11, total_distance)  # add assertion here

    def test_b(self):
        total_distance = solve_b('sample_data')
        self.assertEqual(31, total_distance)

if __name__ == '__main__':
    unittest.main()
