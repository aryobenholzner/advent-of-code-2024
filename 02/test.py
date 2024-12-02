import unittest
from day02 import solve_a, solve_b

class MyTestCase(unittest.TestCase):

    def test_a(self):
        safe_reports = solve_a('sample_data')
        self.assertEqual(2, safe_reports)  # add assertion here

    def test_b(self):
        safe_reports = solve_b('sample_data')
        self.assertEqual(4, safe_reports)

if __name__ == '__main__':
    unittest.main()
