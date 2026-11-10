import unittest
from factorial import Solution


class TestFactorial(unittest.TestCase):
    def test_fact(self):
        cases = [
            (0, 1),
            (1, 1),
            (2, 2),
            (3, 6),
            (4, 24),
            (5, 120),
            (6, 720),
            (7, 5040),
            (8, 40320),
            (9, 362880),
            (10, 3628800)
        ]
        
        sol = Solution()
        
        for n, expected in cases:
            with self.subTest(n=n):
                self.assertEqual(sol.factorial(n), expected)