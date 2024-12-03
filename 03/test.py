import unittest
from day03 import solve_b

class MyTestCase(unittest.TestCase):

    def test_b(self):
        safe_reports = solve_b('sample')
        self.assertEqual(48, safe_reports)

if __name__ == '__main__':
    unittest.main()
